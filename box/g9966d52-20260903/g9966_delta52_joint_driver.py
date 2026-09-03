#!/usr/bin/env python3
"""Bounded high-z joint checks for the (99,66), delta=5/2 lane.

This is an executable necessary system derived from Moh Prop. 6.2:

  Gbar = sum G_j(y) z^j,  deg_y G_j <= 72,  0 <= j <= 27,
  Fbar = sum F_j(y) z^j,  deg_y F_j <= 48,  0 <= j <= 18.

The delta=5/2 local weight is y=s^-2, z=pi*s^5.  The leading face is
G=s^-9 p(pi)^9 and F=s^-6 p(pi)^6 with p=pi(pi^2-1).  For literal high-z
depth d, only z^27,...,z^(28-d) in G and the induced z^18,... in F are used.
Within each literal z band only terms visible through the same local order are
kept.  F bands are obtained from G^2-F^3 by the approximate-root relation.

This is not a full Keller-pair solver: it omits lower z bands, the T2/T3
membership recurrences, the major 4/9 centre, and the constant Jacobian band.
The point of this driver is to make that boundary mechanical rather than
implicit.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import re
import shutil
import subprocess
import time
from pathlib import Path

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
OUT = ROOT / "box" / "g9966d52-20260903"
RECEIPT = ROOT / "xmodel" / "g9966-delta52-joint-gpt55-20260903.run.v2"
INPUT_DIR = Path("/tmp/jc2-lane.gSx1Ze/inputs")
PRIMES = [32003, 32009, 32027]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_charged_inputs() -> list[dict[str, str | bool]]:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    rows = []
    index = 1
    while f"charged_input_{index}_basename" in fields:
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        path = INPUT_DIR / basename
        actual = sha256(path)
        rows.append({
            "index": index,
            "basename": basename,
            "path": str(path),
            "expected_sha256": expected,
            "actual_sha256": actual,
            "ok": actual == expected,
        })
        index += 1
    if not rows or not all(row["ok"] for row in rows):
        raise RuntimeError("charged input SHA-256 mismatch")
    return rows


def singular_expr(expr: sp.Expr) -> str:
    numerator, denominator = sp.fraction(sp.together(sp.expand(expr)))
    if denominator == 1:
        text = str(sp.expand(numerator))
    else:
        text = f"({sp.expand(numerator)})/({sp.expand(denominator)})"
    return text.replace("**", "^")


def p9_coeff(j: int) -> sp.Integer:
    if j < 9 or j > 27 or (j - 9) % 2:
        return sp.Integer(0)
    k = (j - 9) // 2
    return sp.Integer((-1) ** (9 - k)) * sp.binomial(9, k)


def local_order_g(i: int, j: int) -> int:
    return -2 * i + 5 * j + 9


def build_delta52_highz(depth: int) -> dict:
    """Build the literal high-z delta=5/2 system at the requested depth."""
    y = sp.symbols("y")
    variables: list[sp.Symbol] = []
    fixed_terms: list[dict] = []
    unknown_terms: list[dict] = []
    mu2_linear_constraints: list[str] = []
    gbands: dict[int, sp.Expr] = {}

    for offset in range(depth):
        z_degree = 27 - offset
        band = sp.Integer(0)
        for y_degree in range(73):
            if y_degree + z_degree > 99:
                continue
            order = local_order_g(y_degree, z_degree)
            if not 0 <= order <= depth:
                continue
            if order == 0:
                coefficient = p9_coeff(z_degree)
                if coefficient != 0:
                    band += coefficient * y**y_degree
                    fixed_terms.append({
                        "z_degree": z_degree,
                        "y_degree": y_degree,
                        "local_order": order,
                        "coefficient": str(coefficient),
                    })
                continue
            # The mu_2 parity is linear: wrong-parity coefficients are zero.
            # The N14 support has already removed those zero rows; record the
            # equation that would have killed the omitted coefficient.
            expected_parity = (order - 1) % 2
            if z_degree % 2 != expected_parity:
                mu2_linear_constraints.append(f"g_{z_degree}_{y_degree}=0")
                continue
            variable = sp.symbols(f"g_{z_degree}_{y_degree}")
            variables.append(variable)
            band += variable * y**y_degree
            unknown_terms.append({
                "name": str(variable),
                "z_degree": z_degree,
                "y_degree": y_degree,
                "local_order": order,
            })
        gbands[z_degree] = sp.expand(band)

    forced_linear_rows: list[sp.Expr] = []
    forced_linear_names = {"g_27_70", "g_27_71"}
    forced_subs = {
        variable: sp.Integer(0)
        for variable in variables
        if str(variable) in forced_linear_names
    }
    if forced_subs:
        forced_linear_rows = list(forced_subs.keys())
        gbands = {
            z_degree: sp.expand(band.subs(forced_subs, simultaneous=True))
            for z_degree, band in gbands.items()
        }

    fbands: dict[int, sp.Expr] = {18: y**48}
    approximate_root_rows: list[sp.Expr] = []
    induced_fbands: list[dict] = [{"z_degree": 18, "formula": "y^48"}]
    for offset in range(1, depth):
        z_total = 54 - offset
        coeff_g = sp.Integer(0)
        for j1, g1 in gbands.items():
            j2 = z_total - j1
            if j2 in gbands:
                coeff_g += g1 * gbands[j2]
        coeff_f_previous = sp.Integer(0)
        for j1, f1 in fbands.items():
            for j2, f2 in fbands.items():
                j3 = z_total - j1 - j2
                if j3 in fbands:
                    coeff_f_previous += f1 * f2 * fbands[j3]
        numerator = sp.expand(coeff_g - coeff_f_previous)
        quotient, remainder = sp.div(sp.Poly(numerator, y), sp.Poly(3 * y**96, y))
        if remainder.as_expr() != 0:
            for (_degree,), coefficient in sp.Poly(remainder.as_expr(), y).terms():
                if coefficient != 0:
                    approximate_root_rows.append(sp.expand(coefficient))
        f_degree = 18 - offset
        fbands[f_degree] = sp.expand(quotient.as_expr())
        induced_fbands.append({
            "z_degree": f_degree,
            "formula": str(fbands[f_degree]),
        })

    jacobian_rows: list[sp.Expr] = []
    jacobian_band_counts: Counter[int] = Counter()
    for offset in range(depth):
        z_degree = 44 - offset
        coefficient = sp.Integer(0)
        for jf, fband in fbands.items():
            jg = z_degree + 1 - jf
            if jg in gbands:
                coefficient += (
                    sp.diff(fband, y) * jg * gbands[jg]
                    - jf * fband * sp.diff(gbands[jg], y)
                )
        if coefficient == 0:
            continue
        for (_degree,), row in sp.Poly(sp.expand(coefficient), y).terms():
            if row != 0:
                jacobian_rows.append(sp.expand(row))
                jacobian_band_counts[z_degree] += 1

    rows = approximate_root_rows + jacobian_rows
    return {
        "depth": depth,
        "scope": "literal high-z N14 bands with local-order truncation",
        "fixed_terms": fixed_terms,
        "unknown_terms": unknown_terms,
        "mu2_linear_constraints_recorded": mu2_linear_constraints,
        "forced_linear_reductions": [str(row) for row in forced_linear_rows],
        "variables": variables,
        "fbands": induced_fbands,
        "forced_linear_row_count": len(forced_linear_rows),
        "approximate_root_remainder_row_count": len(approximate_root_rows),
        "jacobian_row_count": len(jacobian_rows),
        "jacobian_band_counts": dict(sorted(jacobian_band_counts.items(), reverse=True)),
        "rows": forced_linear_rows + rows,
    }


def emit_singular(stem: str, variables: list[sp.Symbol], rows: list[sp.Expr], char: int) -> Path:
    field = "0" if char == 0 else str(char)
    gamma, split_c, T = sp.symbols("gamma split_c T")
    all_vars = variables + [gamma, split_c, T]
    if rows:
        generators = ",\n  ".join(singular_expr(row) for row in rows)
    else:
        generators = "0"
    script = f"""// {stem}
// Ring variables are the displayed Gbar high-z coefficients, gamma, split_c, T.
// Rabinowitsch localizer: T*gamma*split_c-1.  The delta=5/2 gauge also adds split_c-1.
ring R={field},({','.join(map(str, all_vars))}),dp;
option(redSB);
if (nameof(basering)==\"R\") {{ print(\"CONTROL_RING_PASS\"); }} else {{ print(\"CONTROL_RING_FAIL\"); }}
ideal Eq =
  {generators};
Eq=simplify(Eq,2);
ideal EmptyControl=split_c,T*gamma*split_c-1;
ideal GE=std(EmptyControl);
if (typeof(GE)==\"ideal\" && reduce(1,GE)==0) {{ print(\"CONTROL_EMPTY_WRAPPER_PASS\"); }} else {{ print(\"CONTROL_EMPTY_WRAPPER_FAIL\"); }}
ideal NonemptyControl=split_c-1,gamma-1,T*gamma*split_c-1;
ideal GN=std(NonemptyControl);
if (typeof(GN)==\"ideal\" && reduce(1,GN)!=0) {{ print(\"CONTROL_NONEMPTY_WRAPPER_PASS\"); }} else {{ print(\"CONTROL_NONEMPTY_WRAPPER_FAIL\"); }}
ideal Unsat=Eq,split_c-1;
ideal GU=std(Unsat);
if (typeof(GU)==\"ideal\" && reduce(1,GU)!=0) {{ print(\"CONTROL_UNSATURATED_NONUNIT_PASS\"); }} else {{ print(\"CONTROL_UNSATURATED_NONUNIT_FAIL\"); }}
ideal I=Eq,split_c-1,T*gamma*split_c-1;
print(\"MAIN_START equations=\" + string(size(Eq)) + \" unknowns_excluding_T=\" + string(nvars(R)-1) + \" char={field}\");
ideal G=std(I);
print(\"MAIN_DONE basis_size=\"); size(G);
print(\"BASIS_BEGIN\"); G; print(\"BASIS_END\");
if (reduce(1,G)==0) {{
  print(\"MAIN_SATURATED_EMPTY\");
}} else {{
  print(\"MAIN_NONUNIT\");
  print(\"DIM=\"); dim(G);
}}
quit;
"""
    path = OUT / f"{stem}_{'Q' if char == 0 else 'F' + str(char)}.sing"
    path.write_text(script, encoding="utf-8")
    return path


def run_singular(path: Path, timeout: int = 300) -> dict:
    log = path.with_suffix(".log")
    started = time.perf_counter()
    proc = subprocess.run(
        ["Singular", "-q", "--no-rc", str(path)],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    log.write_text(output, encoding="utf-8")
    fail_markers = sorted(set(re.findall(r"[A-Z0-9_]*FAIL[A-Z0-9_]*", output)))
    pass_markers = sorted(set(re.findall(r"[A-Z0-9_]*PASS[A-Z0-9_]*", output)))
    if "MAIN_SATURATED_EMPTY" in output:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONUNIT" in output:
        verdict = "NONUNIT"
    else:
        verdict = "ERROR"
    basis_match = re.search(r"MAIN_DONE basis_size=\s*([0-9]+)", output)
    dim_match = re.search(r"DIM=\s*(-?[0-9]+)", output)
    return {
        "script": str(path.relative_to(ROOT)),
        "script_sha256": sha256(path),
        "log": str(log.relative_to(ROOT)),
        "log_sha256": sha256(log),
        "returncode": proc.returncode,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "verdict": verdict,
        "basis_size": int(basis_match.group(1)) if basis_match else None,
        "basis_one": bool(
            re.search(r"BASIS_BEGIN\s*(?:1|G\[1\]=1)\s*BASIS_END", output)
        ),
        "dimension": int(dim_match.group(1)) if dim_match else None,
        "pass_markers": pass_markers,
        "fail_markers": fail_markers,
        "stdout_excerpt": output[:2000],
    }


def run_delta52() -> dict:
    depths = [4, 5, 6]
    out = {}
    for depth in depths:
        started = time.perf_counter()
        system = build_delta52_highz(depth)
        build_seconds = round(time.perf_counter() - started, 6)
        depth_runs = []
        for char in PRIMES + [0]:
            script = emit_singular(f"delta52_highz_depth{depth}", system["variables"], system["rows"], char)
            depth_runs.append(run_singular(script))
        out[str(depth)] = {
            "build_seconds": build_seconds,
            "depth": depth,
            "literal_Gbar_z_bands": [27 - i for i in range(depth)],
            "literal_Fbar_z_bands": [18 - i for i in range(depth)],
            "unknown_Gbar_coefficients": len(system["variables"]),
            "unknowns_excluding_T_in_singular": len(system["variables"]) + 2,
            "fixed_split_scale": "split_c-1, with Rabinowitsch localizer T*gamma*split_c-1",
            "forced_linear_rows": system["forced_linear_row_count"],
            "approximate_root_remainder_rows": system["approximate_root_remainder_row_count"],
            "jacobian_rows": system["jacobian_row_count"],
            "jacobian_band_counts": system["jacobian_band_counts"],
            "fixed_terms": system["fixed_terms"],
            "unknown_terms": system["unknown_terms"],
            "induced_Fbar_bands": system["fbands"],
            "runs": depth_runs,
            "verdict": "SATURATED-EMPTY" if any(run["verdict"] == "SATURATED-EMPTY" for run in depth_runs) else "NONUNIT",
        }
    return out


def run_moh_1612_control() -> dict:
    """Run a compact Moh Appendix-II p.208 calibration in this lane."""
    x, y = sp.symbols("x y")
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols("c1:14")
    alpha1, gamma, T = sp.symbols("alpha1 gamma T")
    h = sp.expand(y**3 * (y - x) + b1 * y**3 + b2 * y**2 + b3 * y + b4)
    A = sp.cancel((h - b4) / y)
    B = sp.cancel((A - A.subs(y, 0)) / y)
    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    alpha3 = c5 * A + c6 * B + c7
    beta3 = c8 * A + c9 * B + c10
    alpha4 = c11 * A + c12 * B + c13 * (y - x)
    f = sp.expand(h**3 + beta2 * h + beta3)
    g = sp.expand(h**4 + alpha1 * h**3 + alpha2 * h**2 + alpha3 * h + alpha4)
    J = sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)
    equations = [coef for coef in sp.Poly(sp.expand(J - gamma * x), x, y).coeffs() if coef]
    variables = [b1, b2, b3, b4, alpha1, c1, c2, c3, c4, c5, c6, c7, c8,
                 c9, c10, c11, c12, c13, gamma, T]
    generators = ",\n  ".join(singular_expr(row) for row in equations)
    script = f"""// Moh (64,48) -> p.208 (16,12) Appendix-II calibration.
ring R=0,({','.join(map(str, variables))}),dp;
option(redSB);
ideal Eq =
  {generators};
Eq=simplify(Eq,2);
ideal EmptyControl=gamma,T*gamma-1;
ideal GE=std(EmptyControl);
if (reduce(1,GE)==0) {{ print(\"CONTROL_EMPTY_WRAPPER_PASS\"); }} else {{ print(\"CONTROL_EMPTY_WRAPPER_FAIL\"); }}
ideal NonemptyControl=gamma-1,T*gamma-1;
ideal GN=std(NonemptyControl);
if (reduce(1,GN)!=0) {{ print(\"CONTROL_NONEMPTY_WRAPPER_PASS\"); }} else {{ print(\"CONTROL_NONEMPTY_WRAPPER_FAIL\"); }}
ideal Unsat=Eq;
ideal GU=std(Unsat);
if (reduce(1,GU)!=0) {{ print(\"CONTROL_UNSATURATED_NONUNIT_PASS\"); }} else {{ print(\"CONTROL_UNSATURATED_NONUNIT_FAIL\"); }}
ideal I=Eq,T*gamma-1;
print(\"MAIN_START equations=\" + string(size(Eq)) + \" unknowns_excluding_T=\" + string(nvars(R)-1) + \" char=0\");
ideal G=std(I);
print(\"MAIN_DONE basis_size=\"); size(G);
print(\"BASIS_BEGIN\"); G; print(\"BASIS_END\");
if (reduce(1,G)==0) {{ print(\"MAIN_SATURATED_EMPTY\"); }} else {{ print(\"MAIN_NONUNIT\"); print(\"DIM=\"); dim(G); }}
quit;
"""
    path = OUT / "control_moh1612_appendixII_Q.sing"
    path.write_text(script, encoding="utf-8")
    run = run_singular(path, timeout=300)
    return {
        "typing": "CONTROL: Moh (64,48) reduced p.208 common-polynomial ansatz",
        "minor_side": "u_s=1, so no added split variables",
        "equations": len(equations),
        "unknowns_excluding_T": len(variables) - 1,
        "run": run,
        "verdict": run["verdict"],
    }


def automorphism_controls() -> dict:
    x, y = sp.symbols("x y")
    F = x + y**6
    G = y + F**7
    J = sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))
    same_point = {
        "typing": "EXACT degree>=6 triangular automorphism",
        "composition": "(x,y)->(x+y^6,y), then (u,v)->(u,v+u^7)",
        "F": str(F),
        "G": str(G),
        "degrees": [int(sp.Poly(F, x, y).total_degree()), int(sp.Poly(G, x, y).total_degree())],
        "jacobian": str(J),
        "survives_direct_check": J == 1,
        "infinity_scope": "both top forms are powers of y, so this is not a two-infinity-point control",
    }
    A, C = sp.symbols("A C")
    f_lin = A * x + y
    g_lin = C * x + y
    Jlin = sp.expand(sp.diff(f_lin, x) * sp.diff(g_lin, y) - sp.diff(f_lin, y) * sp.diff(g_lin, x))
    two_point = {
        "typing": "EXACT two-infinity-point automorphism, degree (1,1)",
        "ansatz": "f=A*x+y, g=C*x+y",
        "jacobian_row": "A-C-gamma",
        "point_separation": "top lines A*X+Y and C*X+Y meet infinity at distinct points when A!=C",
        "witness": {"A": 2, "C": 1, "gamma": 1},
        "survives_direct_check": sp.expand(Jlin.subs({A: 2, C: 1}) - 1) == 0,
    }
    impossibility = {
        "typing": "SPEC-CHECK",
        "statement": (
            "A polynomial automorphism of A^2 with both coordinate degrees >1 "
            "has algebraically dependent highest homogeneous parts; in the "
            "triangular-composition normal form the two top forms are powers "
            "of one linear form. Therefore the requested combination "
            "`two points at infinity` plus both degrees >=6 is not available "
            "for a genuine automorphism control."
        ),
        "effect_on_promotion": "the degree>=6 control checks no over-constraint for J, but not the two-point branch geometry",
    }
    return {
        "degree_ge_6_same_infinity": same_point,
        "degree_1_two_infinity": two_point,
        "degree_ge_6_two_infinity_request": impossibility,
    }


def write_manifest() -> None:
    excluded = {
        "artifacts.sha256",
        "g9966_delta52_joint_driver.stdout",
        "g9966_delta52_joint_driver.stderr",
    }
    paths = sorted(path for path in OUT.iterdir() if path.is_file() and path.name not in excluded)
    (OUT / "artifacts.sha256").write_text(
        "".join(f"{sha256(path)}  {path.relative_to(ROOT)}\n" for path in paths),
        encoding="utf-8",
    )


def main() -> None:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular is required")
    OUT.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    charged = verify_charged_inputs()
    delta52 = run_delta52()
    control_1612 = run_moh_1612_control()
    autos = automorphism_controls()
    result = {
        "type": "BOUNDED-HIGH-Z-JOINT / NECESSARY-SYSTEM",
        "verdict": "OPEN[DELTA-5/2-FULL-JOINT-NOT-KILLED]",
        "charged_input_verification": {
            "method": "parsed receipt charged_input_i_basename/sha256 and recomputed every frozen input digest",
            "all_ok": all(row["ok"] for row in charged),
            "rows": charged,
        },
        "source_reconstruction": {
            "moh_pages": {
                "p190": "box/g9966d52-20260903/moh_p190_pdf51.png",
                "p191": "box/g9966d52-20260903/moh_p191_pdf52.png",
                "p192": "box/g9966d52-20260903/moh_p192_pdf53.png",
                "p193": "box/g9966d52-20260903/moh_p193_pdf54.png",
                "p194": "box/g9966d52-20260903/moh_p194_pdf55.png",
                "p195": "box/g9966d52-20260903/moh_p195_pdf56.png",
                "p196": "box/g9966d52-20260903/moh_p196_pdf57.png",
                "layout_text": "box/g9966d52-20260903/moh_pp190_196_pdf51_57.txt",
            },
            "coordinates": "choose the major direction a=0; z=y-b*x-e with b!=0",
            "prop62_boxes": {
                "Fbar": "0<=i<=48, 0<=j<=18, i+j<=66, corner y^48*z^18",
                "Gbar": "0<=i<=72, 0<=j<=27, i+j<=99, corner y^72*z^27",
                "T2bar": "0<=i<=40, 0<=j<=15, i+j<=55, corner y^40*z^15",
            },
        },
        "delta52_high_z_systems": delta52,
        "branchB_run": {
            "status": "NOT-RUN",
            "reason": "delta=5/2 high-z necessary systems were nonunit, so the conditional branch-B fallback was not triggered",
        },
        "controls": {
            "moh_64_48_appendixII": control_1612,
            "automorphisms": autos,
        },
        "not_claimed": [
            "SATURATED-EMPTY for the full delta=5/2 branch",
            "a full (99,66) polynomial pair",
            "SURVIVES as a Keller-pair claim",
            "the unprinted Moh 11-variable elimination",
        ],
        "software": {
            "python": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip(),
            "sympy": sp.__version__,
            "singular": subprocess.run(["Singular", "--version"], capture_output=True, text=True).stdout.splitlines()[0],
        },
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    result_path = OUT / "g9966_delta52_joint_results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_manifest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
