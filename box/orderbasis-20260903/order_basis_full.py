#!/usr/bin/env python3
"""Full D1 monomial order-basis audit for descended two-point rows.

This driver is intentionally local to the 2026-09-04 lane.  It does not edit
ledgers and it treats prime marks in row labels as labels, never derivatives.

The repaired chart uses a necessary over-approximation:

* h has the fixed top face for the requested partition, plus every D1-allowed
  lower monomial.
* each h-adic coefficient alpha_i/beta_i uses the full D1 monomial inventory
  at threshold i*B.
* scalar target translations are kept; the triangular shear is kept only if it
  is safe in this full monomial basis.  It is not safe on the requested rows.

The heavy h-adic Jacobian row extraction is emitted as Singular code so Python
does not perform large multivariate divisions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.sA4mxQ/inputs")
RECEIPT = ROOT / "xmodel/order-basis-full-gpt55-20260903.run.v2"
DEFAULT_CHARS = (0, 32051, 32057)


@dataclass(frozen=True)
class Row:
    key: str
    label: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


ROWS = {
    "2515": Row("25_15_21_2_k2", "(25,15;21;2;k=2)", 25, 15, 21, 2, 2),
    "d108": Row("24_16_18_7_k4", "(24,16;18;7;k=4)", 24, 16, 18, 7, 4),
    "k16a": Row("16_12_13_3_k1", "(16,12;13;3;k=1)", 16, 12, 13, 3, 1),
    "k16b": Row("28_20_25_3_k1", "(28,20;25;3;k=1)", 28, 20, 25, 3, 1),
    "banked": Row("15_10_11_3_k2", "(15,10;11;3;k=2)", 15, 10, 11, 3, 2),
}


def qstr(value: F | int | sp.Expr) -> str:
    if isinstance(value, F):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    return str(value)


def sstr(expr: sp.Expr) -> str:
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    den = sp.expand(den)
    if den == 1:
        out = str(num)
    elif den == -1:
        out = str(-num)
    else:
        out = f"({num})/({den})"
    return out.replace("**", "^")


def clean_name(text: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", text)
    out = re.sub(r"_+", "_", out).strip("_")
    if not out:
        out = "v"
    if out[0].isdigit():
        out = "v" + out
    return out


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_check() -> dict:
    fields: dict[str, dict[str, str]] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        match = re.match(r"charged_input_(\d+)_(sha256|basename)=(.*)", line)
        if match:
            fields.setdefault(match.group(1), {})[match.group(2)] = match.group(3)
    checks = []
    manifest_lines = []
    for index in sorted(fields, key=int):
        rec = fields[index]
        path = INPUTS / rec["basename"]
        got = sha256_file(path)
        ok = got == rec["sha256"]
        manifest_lines.append(f"{rec['sha256']}  {path}")
        checks.append({
            "index": int(index),
            "basename": rec["basename"],
            "path": str(path),
            "expected": rec["sha256"],
            "got": got,
            "ok": ok,
        })
    manifest_path = HERE / "charged_input_manifest.sha256"
    manifest_path.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    return {
        "receipt": str(RECEIPT.relative_to(ROOT)),
        "input_dir": str(INPUTS),
        "manifest": str(manifest_path.relative_to(ROOT)),
        "manifest_sha256": sha256_file(manifest_path),
        "ok": bool(checks) and all(item["ok"] for item in checks),
        "checks": checks,
    }


def closed_form(row: Row) -> dict:
    K = math.gcd(row.n, row.m)
    e = row.n // K
    q = row.m // K
    u = K - row.V2
    R = row.n - row.M2 - 1
    Pi = e + q
    if R == 0 or (Pi * row.V2 - 1) == 0:
        raise ZeroDivisionError("bad closed-form denominator")
    delta2 = -F(row.k + 1, R)
    delta1 = F((row.k + 1) * (Pi * u - R), R * (Pi * row.V2 - 1))
    B = row.V2 * delta1 + u * delta2
    return {
        "K": K,
        "e": e,
        "q": q,
        "u": u,
        "R": R,
        "Pi": Pi,
        "delta1": delta1,
        "delta2": delta2,
        "B": B,
        "lambda_P": e * B,
        "lambda_Q": q * B,
        "d3prime": math.gcd(K, row.M2),
    }


def partitions(total: int, cap: int | None = None) -> Iterable[tuple[int, ...]]:
    if total == 0:
        yield ()
        return
    high = total if cap is None else min(total, cap)
    for first in range(high, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def allowed_partitions(row: Row) -> list[tuple[int, ...]]:
    C = closed_form(row)
    return [part for part in partitions(C["u"]) if len(part) + 1 <= row.n - row.M2]


def parse_partition(text: str) -> tuple[int, ...]:
    values = tuple(int(piece) for piece in re.split(r"[+,]", text.strip()) if piece)
    if not values or tuple(sorted(values, reverse=True)) != values:
        raise argparse.ArgumentTypeError("use a descending partition such as 3 or 2+1")
    return values


def order_allowed(delta1: F, threshold: F, xpow: int, ypow: int) -> bool:
    return -F(xpow) + delta1 * F(ypow) >= threshold


def h_inventory(row: Row, C: dict) -> list[tuple[int, int]]:
    out = []
    for ypow in range(C["K"], -1, -1):
        for xpow in range(0, C["u"] + 1):
            if xpow + ypow >= C["K"]:
                continue
            if order_allowed(C["delta1"], C["B"], xpow, ypow):
                out.append((xpow, ypow))
    return out


def coeff_inventory(C: dict, deficit: int) -> list[tuple[int, int]]:
    """D1 monomial inventory for one h-adic coefficient.

    deg_y is below deg_y(h)=K.  The total-degree cap is the conservative local
    finite envelope used by the earlier D1 count lanes.
    """
    out = []
    threshold = deficit * C["B"]
    for ypow in range(C["K"] - 1, -1, -1):
        max_x = math.floor(C["delta1"] * ypow - threshold)
        for xpow in range(max_x + 1):
            if xpow >= 0 and xpow + ypow <= deficit * C["K"]:
                out.append((xpow, ypow))
    return out


def monomial_expr(mon: tuple[int, int], x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    xpow, ypow = mon
    return x**xpow * y**ypow


def monomial_label(mon: tuple[int, int]) -> str:
    xpow, ypow = mon
    parts = []
    if xpow:
        parts.append("x" if xpow == 1 else f"x^{xpow}")
    if ypow:
        parts.append("y" if ypow == 1 else f"y^{ypow}")
    return "*".join(parts) if parts else "1"


def top_face(row: Row, part: Sequence[int], x: sp.Symbol, y: sp.Symbol) -> dict:
    if sum(part) != closed_form(row)["u"]:
        raise ValueError("partition sum is not u'")
    slopes = list(sp.symbols(f"s2:{len(part) + 1}")) if len(part) > 1 else []
    factors: list[sp.Expr] = []
    names: list[str] = []
    for _ in range(part[0]):
        factors.append(y - x)
        names.append("y-x")
    for slope, count in zip(slopes, part[1:]):
        for _ in range(count):
            factors.append(y - slope * x)
            names.append(f"y-{slope}*x")
    for _ in range(row.V2):
        factors.append(y)
        names.append("y")
    top = sp.Integer(1)
    for factor in factors:
        top *= factor
    omega = sp.Integer(1)
    for slope in slopes:
        omega *= slope * (slope - 1)
    for index, left in enumerate(slopes):
        for right in slopes[index + 1:]:
            omega *= left - right
    pieces = [f"(y-x)^{part[0]}"]
    for index, count in enumerate(part[1:], start=2):
        pieces.append(f"(y-s{index}*x)^{count}")
    return {
        "top": sp.expand(top),
        "slopes": slopes,
        "factors": factors,
        "factor_names": names,
        "omega": sp.expand(omega),
        "factored": f"y^{row.V2}*" + "*".join(pieces),
    }


def sparse_tower(row: Row, part: Sequence[int], C: dict, x: sp.Symbol, y: sp.Symbol) -> dict:
    face = top_face(row, part, x, y)
    params = list(sp.symbols(f"b1:{C['K'] + 1}"))
    prefix = sp.Integer(1)
    tower: dict[int, sp.Expr] = {}
    weights: dict[int, F] = {}
    outer = 0
    center = 0
    for degree, factor in enumerate(face["factors"], start=1):
        prefix = sp.expand(prefix * factor)
        if factor == y:
            center += 1
        else:
            outer += 1
        weights[degree] = outer * C["delta2"] + center * C["delta1"]
        if degree == 1:
            tower[degree] = prefix
        elif degree == 2:
            tower[degree] = sp.expand(factor * tower[degree - 1] + params[0] * y + params[1])
        else:
            tower[degree] = sp.expand(factor * tower[degree - 1] + params[degree - 1])
    return {"face": face, "params": params, "tower": tower, "weights": weights, "h": tower[C["K"]]}


def poly_coeff_vector(expr: sp.Expr, mons: Sequence[tuple[int, int]], variables: Sequence[sp.Symbol],
                      x: sp.Symbol, y: sp.Symbol) -> list[sp.Expr]:
    poly = sp.Poly(sp.expand(expr), x, y)
    return [sp.expand(poly.coeff_monomial(x**a * y**b)) for a, b in mons]


def linear_map_rank(images: Sequence[sp.Expr], inventory: Sequence[tuple[int, int]], variables: Sequence[sp.Symbol],
                    x: sp.Symbol, y: sp.Symbol) -> dict:
    if not images:
        return {"rank": 0, "image_count": 0, "cokernel_dim": len(inventory), "pivot_monomials": [], "omitted_monomials": [monomial_label(m) for m in inventory]}
    columns = [poly_coeff_vector(image, inventory, variables, x, y) for image in images]
    matrix = sp.Matrix.hstack(*[sp.Matrix(col) for col in columns])
    _, pivots = matrix.rref()
    rank = len(pivots)
    pivot_rows: list[int] = []
    if rank:
        colspace = matrix.columnspace()
        pivot_rows = []
        row_matrix = matrix.T
        _, row_pivots = row_matrix.rref()
        pivot_rows = [int(item) for item in row_pivots]
    pivot_set = set(pivot_rows)
    return {
        "rank": rank,
        "image_count": len(images),
        "cokernel_dim": len(inventory) - rank,
        "pivot_monomials": [monomial_label(inventory[i]) for i in pivot_rows],
        "omitted_monomials": [monomial_label(mon) for i, mon in enumerate(inventory) if i not in pivot_set],
    }


def diagnose_partition(row: Row, part: Sequence[int]) -> dict:
    C = closed_form(row)
    x, y = sp.symbols("x y")
    sparse = sparse_tower(row, part, C, x, y)
    h_mons = h_inventory(row, C)
    sparse_h_lower = sp.expand(sparse["h"] - sparse["face"]["top"])
    h_images = [sp.diff(sparse_h_lower, param) for param in sparse["params"]]
    h_map = linear_map_rank(h_images, h_mons, sparse["params"], x, y)

    prefix_items = [(sp.Integer(1), F(0), "1")]
    for degree in range(C["K"] - 1, 0, -1):
        prefix_items.append((sparse["tower"][degree], sparse["weights"][degree], f"H{degree}"))
    prefix_items.append((x, C["delta2"], "x"))
    # Keep the previous chart's exact duplicate behavior.
    deduped: list[tuple[sp.Expr, F, str]] = []
    for item in prefix_items:
        if not any(sp.expand(item[0] - old[0]) == 0 for old in deduped):
            deduped.append(item)

    coefficient_maps = []
    for kind, deficits in (("alpha", range(1, C["e"] + 1)), ("beta", range(2, C["q"] + 1))):
        for deficit in deficits:
            threshold = deficit * C["B"]
            full = coeff_inventory(C, deficit)
            sparse_basis = [expr for expr, weight, _name in deduped if weight >= threshold]
            mapped = linear_map_rank(sparse_basis, full, [], x, y)
            coefficient_maps.append({
                "kind": kind,
                "deficit": deficit,
                "threshold": qstr(threshold),
                "full_dim": len(full),
                "sparse_dim": len(sparse_basis),
                "rank_in_full_inventory": mapped["rank"],
                "cokernel_dim": len(full) - mapped["rank"],
                "omitted_sample": mapped["omitted_monomials"][:20],
            })

    full_gauge = full_basis_gauge_audit(row, C)
    return {
        "row": asdict(row),
        "partition": list(part),
        "closed_form": serial_closed_form(C),
        "top_face": sparse["face"]["factored"],
        "omega": sstr(sparse["face"]["omega"]),
        "h_inventory_count": len(h_mons),
        "h_inventory": [monomial_label(mon) for mon in h_mons],
        "sparse_h_support_count": len([m for m in poly_coeff_vector(sparse_h_lower, h_mons, sparse["params"], x, y) if m != 0]),
        "h_map": h_map,
        "coefficient_maps": coefficient_maps,
        "full_gauge_audit": full_gauge,
        "diagnosis": {
            "h_support_truncation_present": h_map["cokernel_dim"] > 0,
            "sparse_prefix_basis_omits_coefficients": any(item["cokernel_dim"] > 0 for item in coefficient_maps),
            "delta1_zero": C["delta1"] == 0,
        },
    }


def serial_closed_form(C: dict) -> dict:
    return {
        "K": C["K"],
        "e": C["e"],
        "q": C["q"],
        "u": C["u"],
        "R": C["R"],
        "Pi": C["Pi"],
        "d3prime": C["d3prime"],
        "delta1": qstr(C["delta1"]),
        "delta2": qstr(C["delta2"]),
        "B": qstr(C["B"]),
        "lambda_P": qstr(C["lambda_P"]),
        "lambda_Q": qstr(C["lambda_Q"]),
    }


def full_basis_gauge_audit(row: Row, C: dict) -> dict:
    alpha = {i: coeff_inventory(C, i) for i in range(1, C["e"] + 1)}
    beta = {i: coeff_inventory(C, i) for i in range(2, C["q"] + 1)}
    shear = C["e"] - C["q"]
    alpha_shear = alpha.get(shear, [])
    scalar = alpha_shear == [(0, 0)]
    embeds = scalar
    if embeds:
        for deficit, basis in beta.items():
            target = set(alpha.get(deficit + shear, []))
            if not set(basis) <= target:
                embeds = False
                break
    gauges = []
    notes = []
    if scalar and embeds:
        gauges.append(f"P -> P - alpha_{shear} Q")
    else:
        notes.append(f"shear alpha_{shear} omitted in full monomial basis")
    if (0, 0) in beta.get(C["q"], []):
        gauges.append(f"Q -> Q - const(beta_{C['q']})")
    if (0, 0) in alpha.get(C["e"], []):
        gauges.append(f"P -> P - const(alpha_{C['e']})")
    return {
        "shear_index": shear,
        "alpha_shear_dim": len(alpha_shear),
        "alpha_shear_scalar": scalar,
        "shifted_beta_embeds": embeds,
        "gauges_to_apply": gauges,
        "gauge_notes": notes,
        "alpha_dims_pre_translation": [len(alpha[i]) for i in range(1, C["e"] + 1)],
        "beta_dims_pre_translation": [len(beta[i]) for i in range(2, C["q"] + 1)],
    }


def build_full_spec(row: Row, part: Sequence[int]) -> dict:
    C = closed_form(row)
    if C["B"] >= 0:
        raise ValueError("nonnegative B is outside this order-basis chart")
    x, y = sp.symbols("x y")
    face = top_face(row, part, x, y)
    h_mons = h_inventory(row, C)
    h_params = [sp.Symbol(f"h_{a}_{b}") for a, b in h_mons]
    h = face["top"] + sum(param * monomial_expr(mon, x, y) for param, mon in zip(h_params, h_mons))
    h = sp.expand(h)
    alpha_mons = {i: coeff_inventory(C, i) for i in range(1, C["e"] + 1)}
    beta_mons = {i: coeff_inventory(C, i) for i in range(2, C["q"] + 1)}

    gauge = full_basis_gauge_audit(row, C)
    gauges = []
    notes = list(gauge["gauge_notes"])
    # The shear is intentionally conditional.  The requested rows fail here.
    if gauge["alpha_shear_scalar"] and gauge["shifted_beta_embeds"]:
        alpha_mons[gauge["shear_index"]] = []
        gauges.append(f"P -> P - alpha_{gauge['shear_index']} Q")
    if (0, 0) in beta_mons.get(C["q"], []):
        beta_mons[C["q"]] = [mon for mon in beta_mons[C["q"]] if mon != (0, 0)]
        gauges.append(f"Q -> Q - const(beta_{C['q']})")
    if (0, 0) in alpha_mons.get(C["e"], []):
        alpha_mons[C["e"]] = [mon for mon in alpha_mons[C["e"]] if mon != (0, 0)]
        gauges.append(f"P -> P - const(alpha_{C['e']})")

    slopes = list(face["slopes"])
    params: list[sp.Symbol] = h_params + slopes
    setup = [f"poly h = {sstr(h)};"]
    for i in range(1, C["e"] + 1):
        expr = sp.Integer(0)
        for a, b in alpha_mons[i]:
            symbol = sp.Symbol(f"A{i}_{a}_{b}")
            params.append(symbol)
            expr += symbol * x**a * y**b
        setup.append(f"poly AA{i} = {sstr(expr)};")
    for i in range(2, C["q"] + 1):
        expr = sp.Integer(0)
        for a, b in beta_mons[i]:
            symbol = sp.Symbol(f"B{i}_{a}_{b}")
            params.append(symbol)
            expr += symbol * x**a * y**b
        setup.append(f"poly BB{i} = {sstr(expr)};")
    c = sp.Symbol("c")
    params.append(c)
    sat = sp.expand(c * face["omega"])
    low_terms = [("1", C["q"])] + [(f"BB{i}", C["q"] - i) for i in range(2, C["q"] + 1)]
    high_terms = [("1", C["e"])] + [(f"AA{i}", C["e"] - i) for i in range(1, C["e"] + 1)]
    meta = {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "chart": "full_D1_monomial_overapprox",
        "closed_form": serial_closed_form(C),
        "top_face_factored": face["factored"],
        "omega": sstr(face["omega"]),
        "saturation_factor": sstr(sat),
        "h_inventory": [list(mon) for mon in h_mons],
        "h_inventory_count": len(h_mons),
        "h_parameters": [str(param) for param in h_params],
        "alpha_inventories": {str(i): [list(mon) for mon in alpha_mons[i]] for i in range(1, C["e"] + 1)},
        "beta_inventories": {str(i): [list(mon) for mon in beta_mons[i]] for i in range(2, C["q"] + 1)},
        "alpha_dims": [len(alpha_mons[i]) for i in range(1, C["e"] + 1)],
        "beta_dims": [len(beta_mons[i]) for i in range(2, C["q"] + 1)],
        "gauge_audit": gauge,
        "gauges": gauges,
        "gauge_notes": notes,
        "params_without_T": len(params),
        "levels_cap": C["e"] + C["q"] + 2 * C["K"] + 12,
    }
    return {
        "meta": meta,
        "setup": setup,
        "params": params,
        "sat": sat,
        "low_terms": low_terms,
        "high_terms": high_terms,
    }


def stem_for(row: Row, part: Sequence[int], suffix: str = "full") -> str:
    return f"{row.key}_part_{'_'.join(map(str, part))}_{suffix}"


def native_builder_text(spec: dict, rows_path: Path) -> str:
    meta = spec["meta"]
    params_without_c = [str(param) for param in spec["params"] if str(param) != "c"]
    coeff_field = ",".join(params_without_c + ["c"])
    K = int(meta["closed_form"]["K"])
    level_cap = int(meta["levels_cap"])
    lines = [
        "// generated by order_basis_full.py -- full D1 native builder",
        f"// row {meta['row']['label']} partition {meta['partition_label']}",
        f"ring R=(0,{coeff_field}),(y,x),dp;",
        "option(redSB);",
        f"string rowsfile = \"{rows_path.resolve()}\";",
        'write(":w " + rowsfile, "source_index|h_power|x_power|y_power|expr");',
        "int source_idx = 0;",
        "int max_nf_deg = -1;",
        "int target_xk_nonzero = 0;",
        "intvec WY = 1,0;",
        "intvec WX = 0,1;",
        r"""
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
  return(0);
}

proc native_y_div(poly dividend, poly divisor, int y_degree, intvec WY)
{
  poly q = 0;
  poly r = dividend;
  int d;
  poly lc;
  poly term;
  while (r != 0 && deg(r, WY) >= y_degree)
  {
    d = deg(r, WY);
    lc = native_coeff_y(r, d, WY);
    term = lc * y^(d - y_degree);
    q = q + term;
    r = r - term * divisor;
  }
  list out = q, r;
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
  matrix CX = coef(rem, x);
  int i;
  int j;
  int xp;
  int yp;
  matrix CY;
  poly cc;
  for (i = 1; i <= ncols(CX); i++)
  {
    xp = deg(CX[1,i], WX);
    CY = coef(CX[2,i], y);
    for (j = 1; j <= ncols(CY); j++)
    {
      cc = CY[2,j];
      if (cc != 0)
      {
        yp = deg(CY[1,j], WY);
        write(":a " + rowsfile,
          string(source_idx) + "|" + string(hpow) + "|" +
          string(xp) + "|" + string(yp) + "|" + string(cc));
        source_idx = source_idx + 1;
      }
    }
  }
}
""".strip(),
    ]
    lines.extend(spec["setup"])
    for level in range(level_cap + 1):
        lines.append(f"poly H{level} = 0;")
    lines.append("poly tmpSame;")
    lines.append("poly tmpLower;")
    for aa, r in spec["low_terms"]:
        for bb, s in spec["high_terms"]:
            lines.append(
                f"tmpSame = diff(({aa}),x)*diff(({bb}),y)-diff(({aa}),y)*diff(({bb}),x);"
            )
            lines.append(f"if (tmpSame != 0) {{ H{r + s} = H{r + s} + tmpSame; }}")
            if r + s - 1 >= 0 and (r != 0 or s != 0):
                lines.append(
                    f"tmpLower = ({s})*({bb})*(diff(({aa}),x)*diff(h,y)-diff(({aa}),y)*diff(h,x))"
                    f"+({r})*({aa})*(diff(h,x)*diff(({bb}),y)-diff(h,y)*diff(({bb}),x));"
                )
                lines.append(f"if (tmpLower != 0) {{ H{r + s - 1} = H{r + s - 1} + tmpLower; }}")
    for level in range(level_cap):
        lines.append(f"if (H{level} != 0) {{")
        lines.append(f"  list LD{level} = native_y_div(H{level}, h, {K}, WY);")
        lines.append(f"  H{level} = LD{level}[2];")
        lines.append(f"  if (LD{level}[1] != 0) {{ H{level + 1} = H{level + 1} + LD{level}[1]; }}")
        lines.append("}")
    lines.append("poly level0_before = H0;")
    lines.append(f"poly target_xk = native_coeff_xy(level0_before, {meta['row']['k']}, 0, WX, WY);")
    lines.append("int level0_deg_x = deg(level0_before, WX);")
    lines.append(f"H0 = H0 - c*x^{meta['row']['k']};")
    for level in range(level_cap + 1):
        lines.append(f"native_append_coeffs(H{level}, {level}, rowsfile, WX, WY);")
    lines.append('print("NATIVE_GATE level0_deg_x_before_minus_c=" + string(level0_deg_x));')
    lines.append('if (target_xk != 0) { print("NATIVE_GATE target_xk_level0_nonzero=1"); } else { print("NATIVE_GATE target_xk_level0_nonzero=0"); }')
    lines.append('print("NATIVE_DONE equations=" + string(source_idx));')
    lines.append('print("NATIVE_DONE max_nf_deg_x_after_minus_c=" + string(max_nf_deg));')
    lines.append("quit;")
    return "\n".join(lines) + "\n"


def write_native_builder(row: Row, part: Sequence[int]) -> dict:
    spec = build_full_spec(row, part)
    stem = stem_for(row, part)
    rows_path = HERE / "rows" / f"{stem}_rows.tsv"
    builder_path = HERE / "builders" / f"{stem}_builder.sing"
    meta_path = HERE / "meta" / f"{stem}.json"
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    builder_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    builder_path.write_text(native_builder_text(spec, rows_path), encoding="utf-8")
    payload = {
        "manifest_ok": manifest_check()["ok"],
        "meta": spec["meta"],
        "variables": [str(param) for param in spec["params"]],
        "sat": sstr(spec["sat"]),
        "builder": str(builder_path.relative_to(ROOT)),
        "rows_path": str(rows_path.relative_to(ROOT)),
    }
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"meta_path": str(meta_path.relative_to(ROOT)), **payload}


def parse_builder_log(path: Path) -> dict:
    out: dict[str, int] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("NATIVE_GATE ") or line.startswith("NATIVE_DONE "):
            _prefix, rest = line.split(" ", 1)
            if "=" in rest:
                key, value = rest.split("=", 1)
                try:
                    out[key] = int(value)
                except ValueError:
                    pass
    return out


def read_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        header = next(handle, None)
        if header is None:
            return rows
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            source, hpow, xpow, ypow, expr = line.split("|", 4)
            rows.append({
                "source_index": int(source),
                "h_power": int(hpow),
                "x_power": int(xpow),
                "y_power": int(ypow),
                "expr": expr,
            })
    return rows


def write_system_from_rows(meta_path: Path, characteristic: int, algorithm: str) -> dict:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    rows = read_rows(rows_path)
    builder_log = Path(str(ROOT / payload["builder"]) + ".out")
    gate = parse_builder_log(builder_log)
    meta = payload["meta"]
    meta["equations"] = len(rows)
    meta["row_file"] = {
        "path": payload["rows_path"],
        "sha256": sha256_file(rows_path),
        "bytes": rows_path.stat().st_size,
    }
    meta["native_gate"] = gate
    variables = payload["variables"] + ["T"]
    sat = payload["sat"]
    suffix = "Q" if characteristic == 0 else f"p{characteristic}"
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    system_path = HERE / "systems" / f"{stem}_{suffix}_{algorithm}.sing"
    system_path.parent.mkdir(parents=True, exist_ok=True)
    alg_call = "std(I)" if algorithm == "std" else "slimgb(I)"
    generators = [row["expr"] for row in rows] + [f"T*({sat})-1"]
    lines = [
        "// generated by order_basis_full.py -- full D1 system",
        f"// meta {meta_path.relative_to(ROOT)}",
        f"// row {meta['row']['label']} partition {meta['partition_label']}",
        f"// saturation by {sat}",
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        "ideal CE=(" + sat + "),T*(" + sat + ")-1;",
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=(" + sat + ")-1,T*(" + sat + ")-1;",
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        f'print("MAIN_START equations={len(rows)} unknowns={len(payload["variables"])} char={characteristic} algorithm={algorithm}");',
        "ideal I=" + ",\n".join(generators) + ";",
        f"ideal G={alg_call};",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); print("dim="); dim(G); }',
        "quit;",
    ]
    system_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    payload.setdefault("systems", {})[f"{suffix}_{algorithm}"] = str(system_path.relative_to(ROOT))
    payload["meta"] = meta
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"system": str(system_path.relative_to(ROOT)), "equations": len(rows), "unknowns": len(payload["variables"])}


def run_singular(path: Path, timeout: int = 1800) -> dict:
    env = os.environ.copy()
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[key] = "1"
    started = time.monotonic()
    cmd = [
        "timeout",
        str(timeout),
        "Singular",
        "--cpus=1",
        "--threads=1",
        "--flint-threads=1",
        "-q",
        "--no-rc",
        str(path),
    ]
    result = subprocess.run(cmd, cwd=str(ROOT), env=env, text=True, capture_output=True)
    stdout = result.stdout or ""
    stderr = result.stderr or ""
    out_path = Path(str(path) + ".out")
    err_path = Path(str(path) + ".err")
    out_path.write_text(stdout, encoding="utf-8", errors="replace")
    err_path.write_text(stderr, encoding="utf-8", errors="replace")
    if "MAIN_SATURATED_EMPTY" in stdout:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in stdout:
        verdict = "NONTRIVIAL"
    elif "NATIVE_DONE" in stdout:
        verdict = "BUILDER-DONE"
    elif "TAME_J_PASS" in stdout and "TAME_SURVIVES" in stdout:
        verdict = "TAME-CONTROL-PASS"
    elif "OMITTED_ROW_FALSE_POINT_THROUGH" in stdout and "RESTORED_ROW_EMPTY" in stdout:
        verdict = "OMITTED-ROW-CONTROL-PASS"
    elif result.returncode == 124:
        verdict = "TIMEOUT"
    else:
        verdict = "ERROR"
    return {
        "script": str(path.relative_to(ROOT)),
        "returncode": result.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "stdout": str(out_path.relative_to(ROOT)),
        "stderr": str(err_path.relative_to(ROOT)),
        "verdict": verdict,
        "control_ring_pass": "CONTROL_RING_PASS" in stdout,
        "control_empty_pass": "CONTROL_EMPTY_PASS" in stdout,
        "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in stdout,
        "stdout_tail": stdout.splitlines()[-20:],
        "stderr_tail": stderr.splitlines()[-20:],
    }


def parse_system_result(run: dict) -> dict:
    lines = run.get("stdout_tail", [])
    basis = None
    for index, line in enumerate(lines):
        if line.strip() == "MAIN_DONE basis_size=" and index + 1 < len(lines):
            basis = lines[index + 1].strip()
    return {**run, "basis_size": basis}


def write_tame_control(chars: Sequence[int]) -> list[dict]:
    records = []
    for char in chars:
        suffix = "Q" if char == 0 else f"p{char}"
        path = HERE / "controls" / f"tame_automorphism_{suffix}.sing"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join([
            "// (Q,P)=(y,y^2-x), inverse y=Q, x=Q^2-P",
            f"ring A={char},(x,y),dp;",
            "poly Q=y;",
            "poly P=y^2-x;",
            "poly J=diff(Q,x)*diff(P,y)-diff(Q,y)*diff(P,x);",
            'if (J-1==0) { print("TAME_J_PASS"); } else { print("TAME_J_FAIL"); }',
            f"ring R={char},(c,T),dp;",
            "ideal I=c-1,T*c-1;",
            "ideal G=std(I);",
            'if (reduce(1,G)!=0) { print("TAME_SURVIVES"); } else { print("TAME_FALSE_EMPTY"); }',
            "quit;",
        ]) + "\n", encoding="utf-8")
        records.append(parse_system_result(run_singular(path)))
    return records


def write_omitted_row_control() -> dict:
    """A tiny positive control: dropping the target row lets a false point pass.

    This is the same algebraic shape as the charged sparse artefact: <T*c-1>
    is nonempty, but adding the omitted row -c makes it empty.
    """
    path = HERE / "controls" / "omitted_target_row_control_Q.sing"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join([
        "// Deliberately omitted necessary row control.",
        "ring R=0,(c,T),dp;",
        "ideal I=T*c-1;",
        "ideal G=std(I);",
        'if (reduce(1,G)!=0) { print("OMITTED_ROW_FALSE_POINT_THROUGH"); } else { print("OMITTED_ROW_FAIL"); }',
        "ideal K=-c,T*c-1;",
        "ideal H=std(K);",
        'if (reduce(1,H)==0) { print("RESTORED_ROW_EMPTY"); } else { print("RESTORED_ROW_FAIL"); }',
        "quit;",
    ]) + "\n", encoding="utf-8")
    return parse_system_result(run_singular(path))


def run_requested_control_set() -> dict:
    return {
        "tame": write_tame_control(DEFAULT_CHARS),
        "omitted_row": write_omitted_row_control(),
    }


def select_rows(text: str) -> list[Row]:
    if text == "all":
        return [ROWS["2515"], ROWS["d108"]]
    return [ROWS[name] for name in text.split(",") if name]


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("manifest")

    diag = sub.add_parser("diagnose")
    diag.add_argument("--rows", default="all")
    diag.add_argument("--all-partitions", action="store_true")
    diag.add_argument("--partition", type=parse_partition)
    diag.add_argument("--write", action="store_true")

    emit = sub.add_parser("emit-builder")
    emit.add_argument("--row", choices=sorted(ROWS), required=True)
    emit.add_argument("--partition", type=parse_partition, required=True)

    system = sub.add_parser("emit-system")
    system.add_argument("--meta", required=True)
    system.add_argument("--char", type=int, default=0)
    system.add_argument("--algorithm", choices=("std", "slimgb"), default="std")

    run = sub.add_parser("run-singular")
    run.add_argument("script")
    run.add_argument("--timeout", type=int, default=1800)

    controls = sub.add_parser("controls")
    controls.add_argument("--write", action="store_true")

    args = parser.parse_args()

    if args.cmd == "manifest":
        result = manifest_check()
        print(json.dumps(result, indent=2, sort_keys=True))
        if not result["ok"]:
            raise SystemExit(1)
        return

    if args.cmd == "diagnose":
        records = []
        for row in select_rows(args.rows):
            parts = allowed_partitions(row) if args.all_partitions else [args.partition]
            if not parts or parts == [None]:
                raise SystemExit("use --partition or --all-partitions")
            for part in parts:
                records.append(diagnose_partition(row, part))
        payload = {"manifest_ok": manifest_check()["ok"], "diagnostics": records}
        if args.write:
            path = HERE / "diagnostics.json"
            path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            payload["path"] = str(path.relative_to(ROOT))
        print(json.dumps(payload, indent=2, sort_keys=True))
        return

    if args.cmd == "emit-builder":
        row = ROWS[args.row]
        if args.partition not in allowed_partitions(row):
            raise SystemExit("partition not allowed for row")
        print(json.dumps(write_native_builder(row, args.partition), indent=2, sort_keys=True))
        return

    if args.cmd == "emit-system":
        print(json.dumps(write_system_from_rows(ROOT / args.meta, args.char, args.algorithm), indent=2, sort_keys=True))
        return

    if args.cmd == "run-singular":
        print(json.dumps(parse_system_result(run_singular(ROOT / args.script, args.timeout)), indent=2, sort_keys=True))
        return

    if args.cmd == "controls":
        payload = run_requested_control_set()
        if args.write:
            path = HERE / "controls" / "controls.json"
            path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            payload["path"] = str(path.relative_to(ROOT))
        print(json.dumps(payload, indent=2, sort_keys=True))
        return


if __name__ == "__main__":
    main()
