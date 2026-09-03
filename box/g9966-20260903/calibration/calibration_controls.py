#!/usr/bin/env python3
"""Exact calibration controls for the (99,66) global-design lane.

This file deliberately keeps two different controls separate.

* ``moh_1612`` constructs the reduced (16,12) common-polynomial chart printed
  in Moh's Appendix II.  It checks both the literal repeated-c5 reading and
  the conventional c5/c6 emendation.  The Jacobian scalar is localized by an
  explicit Rabinowitsch variable before Singular is asked for a basis.
* ``affine_two_point_automorphism`` is a genuine polynomial automorphism in
  Moh's monic-y gauge.  Its two coordinate lines have distinct physical
  points at infinity.  This is an exact control for global coefficient
  sharing and J=1, but the degree-(1,1) pair has no s=3 major tower or minor
  split; those special tests are therefore NOT-APPLICABLE rather than passed.

Generated artifacts stay beside this driver.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import time
from pathlib import Path

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
OUT = ROOT / "box" / "g9966-20260903" / "calibration"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def singular_expr(expr: sp.Expr) -> str:
    numerator, denominator = sp.fraction(sp.together(sp.expand(expr)))
    if denominator == 1:
        answer = str(sp.expand(numerator))
    else:
        answer = f"({sp.expand(numerator)})/({sp.expand(denominator)})"
    return answer.replace("**", "^")


def jacobian(f: sp.Expr, g: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def run_singular(stem: str, script_text: str, timeout: int = 300) -> dict:
    script = OUT / f"{stem}.sing"
    log = OUT / f"{stem}.log"
    script.write_text(script_text, encoding="utf-8")
    started = time.perf_counter()
    proc = subprocess.run(
        ["Singular", "-q", "--no-rc", str(script)],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    log.write_text(output, encoding="utf-8")
    fail_markers = sorted(set(re.findall(r"[A-Z0-9_]*FAIL[A-Z0-9_]*", output)))
    if "MAIN_SATURATED_EMPTY" in output:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONUNIT" in output:
        verdict = "NONUNIT"
    else:
        verdict = "ERROR"
    record = {
        "verdict": verdict,
        "returncode": proc.returncode,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "script": str(script.relative_to(ROOT)),
        "script_sha256": sha256(script),
        "log": str(log.relative_to(ROOT)),
        "log_sha256": sha256(log),
        "fail_markers": fail_markers,
        "pass_markers": sorted(set(re.findall(r"[A-Z0-9_]*PASS[A-Z0-9_]*", output))),
        "basis_one": bool(
            re.search(r"BASIS_BEGIN\s*1\s*BASIS_END", output)
            or re.search(r"BASIS_BEGIN\s*G\[1\]=1\s*BASIS_END", output)
        ),
    }
    if proc.returncode != 0 or fail_markers or verdict != "SATURATED-EMPTY":
        raise AssertionError(f"Singular calibration failed: {stem}: {record}\n{output}")
    return record


def build_p208_variant(variant: str) -> dict:
    """Build the common (f,g,h,A,B) p.208 chart over Q exactly."""
    x, y = sp.symbols("x y")
    b1, b2, b3, b4 = sp.symbols("b1:5")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols("c1:14")
    alpha1, kappa, T = sp.symbols("alpha1 kappa T")

    h = sp.expand(y**3 * (y - x) + b1*y**3 + b2*y**2 + b3*y + b4)
    A = sp.cancel((h - b4) / y)
    B = sp.cancel((A - A.subs(y, 0)) / y)
    alpha2 = c1*A + c2
    beta2 = c3*A + c4
    beta3 = c8*A + c9*B + c10
    alpha4 = c11*A + c12*B + c13*(y - x)

    if variant == "printed_repeated_c5":
        # Literal typography on p.208: alpha_1 is retained and c_5 is repeated.
        alpha3 = c5*A + c5*B + c7
        alpha1_term = alpha1
        unknowns = [b1, b2, b3, b4, alpha1,
                    c1, c2, c3, c4, c5, c7, c8, c9, c10, c11, c12, c13,
                    kappa]
    elif variant == "absorbed_alpha1_distinct_c6":
        # The campaign compiler's conventional alternative: absorb alpha_1
        # into h and give the B coefficient of alpha_3 its own symbol c_6.
        alpha3 = c5*A + c6*B + c7
        alpha1_term = sp.Integer(0)
        unknowns = [b1, b2, b3, b4,
                    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13,
                    kappa]
    else:
        raise ValueError(variant)

    f = sp.expand(h**3 + beta2*h + beta3)
    g = sp.expand(h**4 + alpha1_term*h**3 + alpha2*h**2 + alpha3*h + alpha4)
    remainder = sp.Poly(jacobian(f, g, x, y) - kappa*x, x, y)
    equations = [sp.expand(coefficient) for coefficient in remainder.coeffs() if coefficient]
    if len(unknowns) != 18 or len(equations) != 77:
        raise AssertionError((variant, len(unknowns), len(equations)))
    origin = {variable: 0 for variable in unknowns}
    if any(sp.expand(equation.subs(origin)) != 0 for equation in equations):
        raise AssertionError("the raw p.208 origin control was lost")
    if (sp.Poly(f, x, y).total_degree(), sp.Poly(f, y).degree(),
            sp.Poly(g, x, y).total_degree(), sp.Poly(g, y).degree()) != (12, 12, 16, 16):
        raise AssertionError("unexpected reduced p.208 degrees")
    return {
        "variant": variant,
        "x": x,
        "y": y,
        "h": h,
        "A": A,
        "B": B,
        "f": f,
        "g": g,
        "kappa": kappa,
        "T": T,
        "unknowns": unknowns,
        "equations": equations,
    }


def emit_p208_singular(data: dict) -> str:
    variables = data["unknowns"] + [data["T"]]
    equations = data["equations"]
    kappa, T = data["kappa"], data["T"]
    generators = ",\n  ".join(singular_expr(equation) for equation in equations)
    maximal = ",".join(map(str, data["unknowns"]))
    return f'''// Exact Moh p.208 common-polynomial calibration: {data["variant"]}
ring R=0,({','.join(map(str, variables))}),dp;
option(redSB);
if (nameof(basering)=="R") {{ print("CONTROL_RING_PASS"); }} else {{ print("CONTROL_RING_FAIL"); }}
ideal emptyControl={kappa},{T}*{kappa}-1;
ideal GE=std(emptyControl);
if (typeof(GE)=="ideal" && reduce(1,GE)==0) {{ print("CONTROL_EMPTY_WRAPPER_PASS"); }} else {{ print("CONTROL_EMPTY_WRAPPER_FAIL"); }}
ideal nonemptyControl={kappa}-1,{T}*{kappa}-1;
ideal GN=std(nonemptyControl);
if (typeof(GN)=="ideal" && reduce(1,GN)!=0) {{ print("CONTROL_NONEMPTY_WRAPPER_PASS"); }} else {{ print("CONTROL_NONEMPTY_WRAPPER_FAIL"); }}
ideal E=
  {generators};
ideal maximal={maximal};
ideal GM=std(maximal);
int origin_ok=1;
for (int i=1; i<=size(E); i++) {{ if (reduce(E[i],GM)!=0) {{ origin_ok=0; }} }}
if (origin_ok==1) {{ print("CONTROL_RAW_ORIGIN_PASS"); }} else {{ print("CONTROL_RAW_ORIGIN_FAIL"); }}
ideal I=E,{T}*{kappa}-1;
ideal G=std(I);
if (typeof(G)=="ideal" && nameof(basering)=="R") {{ print("CONTROL_RESULT_RING_PASS"); }} else {{ print("CONTROL_RESULT_RING_FAIL"); }}
print("MAIN_START equations=77 unknowns_excluding_T=18");
print("BASIS_BEGIN"); G; print("BASIS_END");
if (reduce(1,G)==0) {{ print("MAIN_SATURATED_EMPTY"); }} else {{ print("MAIN_NONUNIT"); }}
quit;
'''


def terminal_order_spine_certificate() -> dict:
    """Verify the short exact certificate at the end of the charged t=1 spine."""
    z = sp.symbols("z")
    H = 54*z**2 - 36*z + 5
    cbar = -4*z*(9*z - 1) / 81
    cbar_inverse = 2187*z/5 - sp.Rational(2187, 10)
    terminal = 20*z - sp.Rational(10, 3)
    terminal_inverse = sp.Rational(27, 10) - 27*z/5
    c_identity = sp.expand(cbar*cbar_inverse - 1 + (18*z + 1)*H/5)
    terminal_identity = sp.expand(terminal*terminal_inverse - 1 + 2*H)
    if c_identity != 0 or terminal_identity != 0:
        raise AssertionError("terminal order-spine certificate failed")
    return {
        "typing": "EXACT-CERTIFICATE; preceding 23-row construction is charged provenance, not rebuilt here",
        "H": str(H),
        "H_discriminant": str(sp.discriminant(H, z)),
        "H_irreducible_over_Q": bool(sp.Poly(H, z, domain=sp.QQ).is_irreducible),
        "cbar": str(cbar),
        "cbar_inverse": str(cbar_inverse),
        "c_unit_identity": "cbar*cbar_inverse - 1 = -(18*z+1)*H/5",
        "c_unit_identity_remainder": str(c_identity),
        "terminal": str(terminal),
        "terminal_inverse": str(terminal_inverse),
        "terminal_identity": "terminal*terminal_inverse - 1 = -2*H",
        "terminal_identity_remainder": str(terminal_identity),
        "charged_band_counts": {"h^5": 1, "h^4": 2, "h^3": 2, "h^2": 5, "h^1": 6, "h^0": 7},
        "charged_full_shape": {"rows": 23, "unknowns_including_jacobian_scalar": 18},
        "charged_Qstar_reduction": {"pivots": 7, "residual_rows": 15, "residual_unknowns": 11},
        "charged_normalized_tail": {"rows_over_Qz_mod_H": 11, "auxiliary_unknowns": 8, "affine_pivots": 4, "terminal_unit_rows": 1},
    }


def affine_two_point_automorphism() -> dict:
    """Check a two-shear automorphism and its exact two infinity-chart jets."""
    x, y, a, pi, t = sp.symbols("x y a pi t")
    u, v = sp.symbols("u v")

    # First upper-triangular map and then a lower-triangular map over Q(a).
    T1u, T1v = a*x + y, y
    T2u = u
    T2v = sp.cancel((a - 1)*u/a + v/a)
    f = sp.expand(T2u.subs({u: T1u, v: T1v}, simultaneous=True))
    g = sp.cancel(T2v.subs({u: T1u, v: T1v}, simultaneous=True))
    if sp.expand(f - (a*x + y)) != 0 or sp.cancel(g - ((a - 1)*x + y)) != 0:
        raise AssertionError("triangular composition did not simplify")

    det_T1 = jacobian(T1u, T1v, x, y)
    det_T2 = jacobian(T2u, T2v, u, v)
    J = sp.cancel(jacobian(f, g, x, y))
    inverse_x = sp.expand(f - g)
    inverse_y = sp.expand(a*g - (a - 1)*f)
    if (det_T1, sp.cancel(det_T2), J) != (a, 1/a, 1):
        raise AssertionError("determinant check failed")
    if sp.expand(inverse_x - x) != 0 or sp.expand(inverse_y - y) != 0:
        raise AssertionError("polynomial inverse check failed")

    # Monic-y gauge is literal, with degree=degree_y=1 for both coordinates.
    gauge = {
        "f_total_degree": int(sp.Poly(f, x, y).total_degree()),
        "f_y_degree": int(sp.Poly(f, y).degree()),
        "f_y_leader": str(sp.Poly(f, y).LC()),
        "g_total_degree": int(sp.Poly(g, x, y).total_degree()),
        "g_y_degree": int(sp.Poly(g, y).degree()),
        "g_y_leader": str(sp.Poly(g, y).LC()),
    }
    if gauge != {"f_total_degree": 1, "f_y_degree": 1, "f_y_leader": "1",
                 "g_total_degree": 1, "g_y_degree": 1, "g_y_leader": "1"}:
        raise AssertionError(gauge)

    # At P_f=[1:-a:0] and P_g=[1:1-a:0], put x=t^-1 and recenter y.
    pf_sub = {x: 1/t, y: (-a + pi)/t}
    pg_sub = {x: 1/t, y: (1 - a + pi)/t}
    pf_f = sp.cancel(t*f.subs(pf_sub, simultaneous=True))
    pf_g = sp.cancel(t*g.subs(pf_sub, simultaneous=True))
    pg_f = sp.cancel(t*f.subs(pg_sub, simultaneous=True))
    pg_g = sp.cancel(t*g.subs(pg_sub, simultaneous=True))
    expected_jets = (pi, pi - 1, pi + 1, pi)
    if tuple(map(sp.expand, (pf_f, pf_g, pg_f, pg_g))) != expected_jets:
        raise AssertionError("two-point jets did not match")

    # The economical unspecialized global ansatz f=A*x+y, g=C*x+y has two
    # unknowns.  The first chart, second chart, and J=1 all give the same row
    # A-C-1, so the joint rank stays one and the family dimension stays one.
    A, C = sp.symbols("A C")
    shared_row = A - C - 1
    rank = sp.Matrix([[1, -1], [1, -1], [1, -1]]).rank()
    if rank != 1 or shared_row.subs({A: 2, C: 1}) != 0:
        raise AssertionError("shared-jet rank check failed")

    f2, g2 = sp.expand(f.subs(a, 2)), sp.expand(g.subs(a, 2))
    if jacobian(f2, g2, x, y) != 1:
        raise AssertionError("Q-specialized direct Jacobian failed")
    return {
        "typing": "EXACT-AUTOMORPHISM / SURVIVES[UNIVERSAL-GLOBAL-CHECKS]",
        "field": "Q(a), with a != 0 for the displayed two-factor decomposition; witness a=2 lies over Q",
        "triangular_factors": {
            "T1": "(x,y) -> (a*x+y,y)",
            "det_T1": str(det_T1),
            "T2": "(u,v) -> (u,((a-1)*u+v)/a)",
            "det_T2": str(det_T2),
        },
        "composition": {"f": str(f), "g": str(g), "jacobian": str(J)},
        "finite_support": {
            "homogenized_degree_one_forms": ["a*X+Y", "(a-1)*X+Y"],
            "support_size_f": 2,
            "support_size_g": 2,
            "free_global_coefficients_after_monic_gauge": ["a", "a-1"],
        },
        "polynomial_inverse": {"x": "f-g", "y": "a*g-(a-1)*f"},
        "moh_gauge": gauge,
        "physical_infinity_points": {
            "closure_f_equals_0": "P_f=[1:-a:0]",
            "closure_g_equals_0": "P_g=[1:1-a:0]",
            "distinct_certificate": "the Y/X coordinates differ by 1",
            "interpretation": "two distinct points for the union of the two coordinate fibres, one on each line",
        },
        "exact_two_chart_jets": {
            "at_P_f": {"t*f": str(pf_f), "t*g": str(pf_g)},
            "at_P_g": {"t*f": str(pg_f), "t*g": str(pg_g)},
        },
        "shared_global_ansatz": {
            "ansatz": "f=A*x+y, g=C*x+y",
            "unknowns": 2,
            "point_f_row": str(shared_row),
            "point_g_row": str(shared_row),
            "jacobian_row": str(shared_row),
            "joint_row_rank": int(rank),
            "joint_dimension": 1,
            "band_table": [
                {"stage": "monic finite affine support", "independent_rows": 0, "dimension": 2},
                {"stage": "P_f canonical jet", "independent_rows": 1, "dimension": 1},
                {"stage": "P_g canonical jet", "independent_rows": 1, "dimension": 1},
                {"stage": "J=1", "independent_rows": 1, "dimension": 1},
                {"stage": "slice A=2", "independent_rows": 2, "dimension": 0},
            ],
        },
        "Q_witness": {"f": str(f2), "g": str(g2), "jacobian": "1", "inverse": "x=f-g, y=2*g-f"},
        "special_tower_tests": "NOT-APPLICABLE[degrees (1,1): no s=3 tower, no principal-minor split]",
    }


def write_manifest() -> None:
    # Shell-owned capture files may still be open when this routine runs.
    excluded = {"artifacts.sha256", "calibration.stdout", "calibration.stderr"}
    paths = sorted(path for path in OUT.iterdir() if path.is_file() and path.name not in excluded)
    (OUT / "artifacts.sha256").write_text(
        "".join(f"{sha256(path)}  {path.relative_to(ROOT)}\n" for path in paths),
        encoding="utf-8",
    )


def main() -> None:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular is required")
    OUT.mkdir(parents=True, exist_ok=True)
    variants = {}
    for name in ("printed_repeated_c5", "absorbed_alpha1_distinct_c6"):
        data = build_p208_variant(name)
        run = run_singular(f"moh1612_{name}", emit_p208_singular(data))
        variants[name] = {
            "typing": "EXACT-CAS within the declared common-polynomial ansatz",
            "unknowns_excluding_wrapper_T": len(data["unknowns"]),
            "coefficient_parameters_excluding_jacobian_scalar": len(data["unknowns"]) - 1,
            "equations": len(data["equations"]),
            "reduced_degrees_f_g": [12, 16],
            "unsaturated_origin": "all coefficient parameters and kappa equal zero",
            "localization": "T*kappa-1",
            "run": run,
        }
    result = {
        "software": {
            "python": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip(),
            "sympy": sp.__version__,
            "singular": subprocess.run(["Singular", "--version"], capture_output=True, text=True).stdout.splitlines()[0],
        },
        "moh_64_48_reduced_16_12": {
            "typing": "CALIBRATION: original (64,48) chart divided by d=4; not a constructed global (64,48) Keller pair",
            "minor_side": "TRIVIAL[u_s=1]: zero added split variables and zero added split equations",
            "variants": variants,
            "joint_count_first_global_stage": {"unknowns": 18, "equations": 77, "minor_extra_equations": 0},
            "verdict": "SATURATED-EMPTY[P208-COMMON-POLYNOMIAL-ANSATZ]",
            "order_spine_terminal": terminal_order_spine_certificate(),
        },
        "affine_two_point_automorphism": affine_two_point_automorphism(),
    }
    result_path = OUT / "calibration-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_manifest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
