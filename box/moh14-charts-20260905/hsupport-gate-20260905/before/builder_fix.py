#!/usr/bin/env python3
"""builder_fix.py -- repair the s'=3 native builders emitted by
order_basis_full.native_builder_text.

AUDIT 17(qqqqqq) reported a Singular *type* bug in native_append_coeffs
(`string(cc)`).  That is NOT what the failing stems do.  Measured here
(box/moh14-charts-20260905, math-hq + r7i workers):

  * stem V2_1 (144 unknowns) under the emitted builder reaches 64.2 GB RSS
    in 6 min with ZERO data rows written; stem V1_2 (230) reached 184 GB on
    an r7i in 20 min.  Both were OOM-killed on 61 GB c7i workers, leaving a
    header-only rows.tsv -- which downstream looks exactly like "0 generators".
  * No Singular error text is produced; the `halt 1` in the .out files is
    Singular's exit banner after SIGTERM/OOM, and stderr is empty.

The real defect is the *ring*: the builder puts all N unknowns in the
COEFFICIENT FIELD, `ring R=(0,p1,...,pN),(y,x),dp;`.  Every coefficient is
then a `transext` fraction over N transcendentals, and the repeated
y-division by h allocates fraction objects without bound.

FIX (three parts, all mechanical, all math-preserving):

  1. Move the unknowns into the polynomial ring:
         ring R=0,(y,x,p1,...,pN),(lp(1),dp(N+1));
     The y-first block makes lead(h) = y^K (h is monic in y), so the
     y-division of the emitted code is exactly Singular's own determinate
     division.  No denominators are ever created -- h is monic, so the
     original loop never produced any either.
  2. Replace the interpreted `native_y_div` loop (which calls deg()/coef()
     over the whole polynomial once per division step) with a single
     `division(f, ideal(h))` call in C.
  3. Replace the nested coef(rem,x) / coef(.,y) double loop in
     native_append_coeffs with one `coef(rem, x*y)` call.

Row ORDER changes (one pass over x*y monomials instead of a nested pass),
so source_index values are permuted; the row SET is unchanged and that is
what the downstream ideal consumes.  `regression_compare` checks the set.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RING_RE = re.compile(r"^ring R=\(0,(?P<params>.*?)\),\(y,x\),dp;$", re.M)
YDIV_RE = re.compile(
    r"^  list LD(?P<lvl>\d+) = native_y_div\(H(?P=lvl), h, (?P<K>\d+), WY\);$", re.M)
PROC_START = "proc native_coeff_y(poly rem, int wanty, intvec WY)"
SETUP_START = "\npoly h = "

NEW_PROCS = r"""
proc native_coeff_y(poly rem, int wanty, intvec WY)
{
  matrix CY = coef(rem, y);
  int j;
  for (j = 1; j <= ncols(CY); j++)
  {
    if (deg(CY[1,j], WY) == wanty)
    {
      return(CY[2,j]);
    }
  }
  return(0);
}

proc native_coeff_xy(poly rem, int wantx, int wanty, intvec WX, intvec WY)
{
  matrix CX = coef(rem, x);
  int i;
  int j;
  for (i = 1; i <= ncols(CX); i++)
  {
    if (deg(CX[1,i], WX) == wantx)
    {
      matrix CY = coef(CX[2,i], y);
      for (j = 1; j <= ncols(CY); j++)
      {
        if (deg(CY[1,j], WY) == wanty)
        {
          return(CY[2,j]);
        }
      }
    }
  }
  return(poly(0));
}

// determinate division by the y-monic h; lead(h)=y^K under (lp(1),dp)
proc native_y_div_fast(poly dividend, ideal HDIV)
{
  list dv = division(dividend, HDIV);
  poly qq = dv[1][1,1];
  poly rr = dv[2][1];
  if (dv[3][1,1] != 1)
  {
    print("NATIVE_FAIL division_unit_not_one");
  }
  list out = qq, rr;
  return(out);
}

proc native_append_coeffs(poly rem, int hpow, string rowsfile, intvec WX, intvec WY)
{
  if (rem == 0)
  {
    return();
  }
  int dx = deg(rem, WX);
  if (dx > max_nf_deg)
  {
    max_nf_deg = dx;
  }
  // one pass: the buckets are the (x,y) monomials of THIS level only,
  // which is cheaper than the nested coef(.,x) then coef(.,y) double pass.
  matrix CM = coef(rem, x*y);
  int i;
  for (i = 1; i <= ncols(CM); i++)
  {
    if (CM[2,i] != 0)
    {
      write(":a " + rowsfile,
        string(source_idx) + "|" + string(hpow) + "|" +
        string(deg(CM[1,i], WX)) + "|" + string(deg(CM[1,i], WY)) + "|" +
        string(CM[2,i]));
      source_idx = source_idx + 1;
    }
  }
}
"""


def fix_text(text: str) -> tuple[str, dict]:
    m = RING_RE.search(text)
    if not m:
        raise ValueError("builder does not carry the transext ring line")
    params = [p for p in m.group("params").split(",") if p]
    n = len(params)
    nvars = n + 2
    ring = "ring R=0,(y,x,%s),(lp(1),dp(%d));" % (",".join(params), nvars - 1)
    out = text[:m.start()] + ring + text[m.end():]

    zeros = ",0" * n
    if "intvec WY = 1,0;" not in out or "intvec WX = 0,1;" not in out:
        raise ValueError("weight intvecs not found")
    out = out.replace("intvec WY = 1,0;", "intvec WY = 1,0" + zeros + ";")
    out = out.replace("intvec WX = 0,1;", "intvec WX = 0,1" + zeros + ";")

    i0 = out.index(PROC_START)
    i1 = out.index(SETUP_START, i0)
    out = out[:i0] + NEW_PROCS.strip() + out[i1:]

    ks = set(int(mm.group("K")) for mm in YDIV_RE.finditer(out))
    if len(ks) != 1:
        raise ValueError("expected one y-division degree, saw %s" % sorted(ks))
    K = ks.pop()
    out = YDIV_RE.sub(
        lambda mm: "  list LD%s = native_y_div_fast(H%s, HDIV);" % (
            mm.group("lvl"), mm.group("lvl")),
        out)

    anchor = "\npoly H0 = 0;"
    j = out.index(anchor)
    gate = (
        "\nideal HDIV = h;"
        "\nif (lead(h) == y^%d) { print(\"NATIVE_GATE lead_h_is_yK=1\"); }"
        " else { print(\"NATIVE_GATE lead_h_is_yK=0\"); }" % K
    )
    out = out[:j] + gate + out[j:]
    out = out.replace(
        "// generated by order_basis_full.py -- full D1 native builder",
        "// generated by order_basis_full.py -- full D1 native builder\n"
        "// REPAIRED by builder_fix.py: unknowns moved from the transext\n"
        "// coefficient field into the polynomial ring (y-first block order),\n"
        "// y-division delegated to division(), coef(rem,x*y) single pass.",
        1)
    return out, {"parameters": n, "K": K, "nvars": nvars}


def read_row_set(path: Path) -> set:
    rows = set()
    with path.open() as fh:
        header = fh.readline()
        if not header.startswith("source_index|"):
            raise ValueError("bad header in %s" % path)
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("|", 4)
            expr = parts[4].strip()
            if expr.startswith("(") and expr.endswith(")"):
                expr = expr[1:-1]
            rows.add((parts[1], parts[2], parts[3], expr))
    return rows


def regression_compare(old: Path, new: Path) -> dict:
    a = read_row_set(old)
    b = read_row_set(new)
    return {
        "old_rows": len(a), "new_rows": len(b), "identical": a == b,
        "only_old": len(a - b), "only_new": len(b - a),
    }


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--compare":
        import json
        print(json.dumps(regression_compare(Path(argv[2]), Path(argv[3])), indent=2))
        return 0
    src = Path(argv[1])
    dst = Path(argv[2]) if len(argv) > 2 else src
    text, info = fix_text(src.read_text(encoding="utf-8"))
    dst.write_text(text, encoding="utf-8")
    print("FIXED %s -> %s parameters=%d K=%d" % (
        src.name, dst.name, info["parameters"], info["K"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


# --- semantic (term-multiset) comparison -----------------------------------
_TERM_SPLIT = re.compile(r"(?=[+-])")


def term_key(term: str) -> tuple:
    term = term.strip()
    if not term:
        return ()
    sign = 1
    while term[:1] in "+-":
        if term[0] == "-":
            sign = -sign
        term = term[1:].strip()
    factors = term.split("*")
    coeff = 1
    mons = []
    for f in factors:
        f = f.strip()
        if not f:
            continue
        if re.fullmatch(r"\d+", f):
            coeff *= int(f)
        else:
            mons.append(f)
    return (sign * coeff, tuple(sorted(mons)))


def poly_terms(expr: str) -> tuple:
    return tuple(sorted(term_key(t) for t in _TERM_SPLIT.split(expr) if t.strip()))


def semantic_compare(old: Path, new: Path) -> dict:
    a = {(h, x, y): poly_terms(e) for (h, x, y, e) in read_row_set(old)}
    b = {(h, x, y): poly_terms(e) for (h, x, y, e) in read_row_set(new)}
    same_keys = set(a) == set(b)
    bad = [k for k in a if same_keys and a[k] != b[k]]
    return {"old_rows": len(a), "new_rows": len(b), "same_keys": same_keys,
            "mismatched_polys": len(bad), "identical": same_keys and not bad,
            "examples": bad[:3]}
