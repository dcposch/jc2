#!/usr/bin/env python3
"""reduce_msp.py — reduce all integer coefficients of a mod-p .ms file into [0,p).

Hazard (AUDIT.md 2026-08-10): msolve 0.10.1 parses integer tokens with a
64-bit clamp (values > 2^63-1 are read as LONG_MAX = 9223372036854775807),
so any .ms file at char p > 0 carrying a coefficient above 2^63-1 is
SILENTLY CORRUPTED at parse time. Coefficients in [p, 2^63) are reduced
correctly by msolve itself (verified by micro-test + reduced-twin GB
byte-comparison), but the standing rule is now: ALL p>0 emissions must
ship with coefficients already reduced into [0,p).

Usage: reduce_msp.py IN.ms OUT.ms
  - line 1: variable list (copied verbatim)
  - line 2: characteristic p (must be > 0)
  - rest:   polynomials; every integer token not preceded by '^' is
            reduced mod p (sign folded in: -c -> p - (c mod p) as +(...)
            is NOT done; we keep the sign and reduce the magnitude, which
            msolve handles exactly for magnitudes < p).

Built-in guard (independent-parser round-trip): both files are re-parsed
by the tiny evaluator below (exact Python bignum arithmetic, no msolve
code) and every polynomial is evaluated at 2 random points mod p; the
script asserts per-row equality IN ≡ OUT (mod p), equal row counts, and
that OUT contains no token >= p. Exits nonzero on any mismatch.
"""
import re, sys, random

TOK = re.compile(r"(\^?)(\d+)")

def reduce_text(body: str, p: int) -> str:
    def sub(m):
        if m.group(1):          # exponent: leave untouched
            return m.group(0)
        return str(int(m.group(2)) % p)
    return TOK.sub(sub, body)

# ---- independent parser/evaluator (no shared code with the emitters) ----
TERM = re.compile(r"([+-]?)([^+-]+)")
FACT = re.compile(r"([A-Za-z_][A-Za-z_0-9]*)(?:\^(\d+))?$")

def eval_poly(poly: str, point: dict, p: int) -> int:
    poly = "".join(poly.split())
    if not poly:
        return 0
    acc = 0
    for sign, term in TERM.findall(poly):
        val = -1 if sign == "-" else 1
        for f in term.split("*"):
            if not f:
                continue
            if f[0].isdigit():
                val *= int(f)
            else:
                m = FACT.match(f)
                assert m, f"bad factor {f!r}"
                val *= pow(point[m.group(1)], int(m.group(2) or 1), p)
        acc += val
    return acc % p

def parse_ms(path: str):
    with open(path) as fh:
        txt = fh.read()
    assert "(" not in txt, f"{path}: parenthesized input (separate hazard)"
    lines = txt.split("\n")
    vars_ = [v.strip() for v in lines[0].split(",") if v.strip()]
    p = int(lines[1].strip())
    body = "\n".join(lines[2:])
    polys = [q for q in (s.strip() for s in body.split(",")) if q]
    return vars_, p, polys

def main(src, dst):
    vars_, p, _ = parse_ms(src)
    assert p > 0, f"{src}: char 0 file, nothing to reduce"
    with open(src) as fh:
        head_vars = fh.readline()
        head_char = fh.readline()
        body = fh.read()
    with open(dst, "w") as out:
        out.write(head_vars)
        out.write(head_char)
        out.write(reduce_text(body, p))
    # ---- round-trip guard ----
    v1, p1, polys1 = parse_ms(src)
    v2, p2, polys2 = parse_ms(dst)
    assert v1 == v2 and p1 == p2 == p, "header mismatch"
    assert len(polys1) == len(polys2), \
        f"row count changed: {len(polys1)} -> {len(polys2)}"
    for m in TOK.finditer(open(dst).read().split("\n", 2)[2]):
        if not m.group(1):
            assert int(m.group(2)) < p, f"unreduced token survived: {m.group(2)}"
    rng = random.Random(20260810)
    for trial in range(2):
        pt = {v: rng.randrange(1, p) for v in v1}
        for i, (a, b) in enumerate(zip(polys1, polys2)):
            ea, eb = eval_poly(a, pt, p), eval_poly(b, pt, p)
            assert ea == eb, f"row {i}: {ea} != {eb} (trial {trial})"
    print(f"OK {src} -> {dst}: {len(polys1)} rows, p={p}, "
          f"round-trip guard PASS (2 points)")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
