#!/usr/bin/env python3
"""Reproduce the Xu (7.1) offset-one, charged-data-only audit.

The frozen roster does not contain the realization map that links the three
composite series T_s(sigma), g(sigma), and (T_s)_f(sigma).  Consequently this
driver forms exactly the row ideal justified by the charged inputs, keeps the
missing intrinsic coefficients free, and does not mistake that relaxation for
an attained Keller pair.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


INPUT_DIR = Path("/tmp/jc2-lane.X7L3gT/inputs")
DEFAULT_OUTPUT = Path("box/xu71-offset-one-20260906/xu71-offset-one.json")

EXPECTED = {
    "xu71-es-leaves-sol56-20260906.md": "c76be040e115dc3fab84098eef218d157948afe8717318fd2cc6f20e1aa576b9",
    "roster.jsonl": "cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf",
    "split_window.py": "be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd",
    "xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf": "00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21",
    "moh1983_jram340_configurations_of_roots.pdf": "6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51",
    "FALLACY-v2.md": "e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def qtext(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def load_split_window(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("charged_split_window_offset", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen split_window.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def skeleton_mapping(source: dict[str, Any]) -> dict[str, Any]:
    """Declare the roster-array to charged one-based-index map."""
    return {
        "n": source["n"],
        "m": source["m"],
        "s": source["s"],
        "M": {i + 1: x for i, x in enumerate(source["M"])},
        "d": {i + 1: x for i, x in enumerate(source["d"])},
        "V": {i + 2: x for i, x in enumerate(source["V"])},
    }


def face_chart(u: int, denominator: int, partition: list[int]) -> dict[str, Any]:
    key = (u, denominator, tuple(partition))
    charts = {
        (2, 1, (1, 1)): ("pi^2-c", False, "midpoint gauge"),
        (3, 1, (2, 1)): ("pi^2*(pi-c)", False, "double root 0, simple root c"),
        (3, 1, (1, 1, 1)): ("pi*(pi-1)*(pi-r)", True, "ordered roots 0,1,r"),
        (4, 1, (3, 1)): ("pi^3*(pi-c)", False, "triple root 0, simple root c"),
        (5, 1, (4, 1)): ("pi^4*(pi-c)", False, "quadruple root 0, simple root c"),
        (3, 2, (1, 1, 1)): ("pi*(pi^2-c)", False, "fixed zero plus Q=2 orbit"),
        (4, 2, (2, 2)): ("(pi^2-c)^2", False, "double Q=2 orbit"),
        (4, 2, (2, 1, 1)): ("pi^2*(pi^2-c)", False, "double zero plus Q=2 orbit"),
        (4, 3, (1, 1, 1, 1)): ("pi*(pi^3-c)", False, "fixed zero plus Q=3 orbit"),
        (5, 2, (3, 1, 1)): ("pi^3*(pi^2-c)", False, "triple zero plus Q=2 orbit"),
        (5, 2, (2, 2, 1)): ("pi*(pi^2-c)^2", False, "simple zero plus double Q=2 orbit"),
        (5, 2, (1, 1, 1, 1, 1)): (
            "pi*(pi^2-1)*(pi^2-r)", True, "fixed zero and two Q=2 orbits"
        ),
        (5, 3, (2, 1, 1, 1)): ("pi^2*(pi^3-c)", False, "double zero plus Q=3 orbit"),
        (5, 4, (1, 1, 1, 1, 1)): ("pi*(pi^4-c)", False, "fixed zero plus Q=4 orbit"),
    }
    if key not in charts:
        raise AssertionError(f"missing face chart {key}")
    p, collision_ratio, gauge = charts[key]
    if collision_ratio:
        presentation = "Q[r,c,Zc]/(c-r*(r-1),Zc*c-1)"
        generators = ["r", "c", "Zc", "pi"]
        quotient_images = {"r": "r", "c": "r*(r-1)", "Zc": "1/(r*(r-1))", "pi": "pi"}
    else:
        presentation = "Q[c,Zc]/(Zc*c-1)"
        generators = ["c", "Zc", "pi"]
        quotient_images = {"c": "c", "Zc": "1/c", "pi": "pi"}
    return {
        "p": p,
        "collision_ratio_chart": collision_ratio,
        "presentation": presentation,
        "generator_order": generators,
        "quotient_images": quotient_images,
        "gauge": gauge,
        "scope": "chosen face chart; rho/lambda do not choose its modulus value",
    }


def q_witness(
    p: sp.Expr,
    p_display: str,
    u: int,
    W: int,
    theta: Fraction,
    kappa: Fraction,
    partition: list[int],
    pi: sp.Symbol,
    c: sp.Symbol,
    eta: sp.Symbol,
) -> tuple[sp.Expr, str, bool]:
    lam = tuple(partition)
    if theta.denominator == 1:
        th = theta.numerator
        assert kappa.denominator == 1 and kappa >= 0
        kap = kappa.numerator
        factor = u * th + 1
        integral = sp.integrate(sp.expand(p**th), pi)
        expr = factor * p**kap * integral + eta * p**kap
        display = f"{factor}*p^{kap}*Integral(p^{th},dpi)+eta*p^{kap}"
        return expr, display, True
    if len(lam) == 2 and lam[1] == 1 and theta == Fraction(1, lam[0]):
        root_mult = lam[0]
        expr = pi ** (root_mult * W - 1) * (pi - c) ** (W + 1) * (
            pi + sp.Rational(root_mult, root_mult + 1) * c
        )
        display = (
            f"pi^{root_mult * W - 1}*(pi-c)^{W + 1}*"
            f"(pi+{root_mult}/{root_mult + 1}*c)"
        )
        return expr, display, False
    if lam == (2, 2) and theta == Fraction(3, 2):
        base = pi**2 - c
        integral = sp.integrate(base**3, pi)
        expr = 7 * base ** (2 * W - 3) * integral + eta * base ** (2 * W - 3)
        return expr, f"7*(pi^2-c)^{2 * W - 3}*Integral((pi^2-c)^3,dpi)+eta*(pi^2-c)^{2 * W - 3}", True
    if lam == (2, 1, 1) and theta == Fraction(3, 2):
        expr = pi ** (2 * W - 3) * (pi**2 - c) ** (W + 1) * (pi**2 + sp.Rational(2, 5) * c)
        return expr, f"pi^{2 * W - 3}*(pi^2-c)^{W + 1}*(pi^2+2*c/5)", False
    if lam == (2, 1, 1, 1) and theta == Fraction(5, 2):
        expr = pi ** (2 * W - 5) * (pi**3 - c) ** (W + 1) * (pi**3 + sp.Rational(2, 7) * c)
        return expr, f"pi^{2 * W - 5}*(pi^3-c)^{W + 1}*(pi^3+2*c/7)", False
    raise AssertionError((p_display, W, theta, kappa, lam))


def verify_fractional_face(
    W: int,
    X: Fraction,
    alpha: Fraction,
    constant: int,
    theta: Fraction,
    partition: list[int],
    pi: sp.Symbol,
    c: sp.Symbol,
) -> bool:
    """Check a fractional template after cancelling its displayed factors.

    This is the exact rational-function calculation used to avoid expanding
    powers as large as p^186 merely to rediscover the integrating-factor
    identity.
    """
    sx = sp.Rational(X.numerator, X.denominator)
    sa = sp.Rational(alpha.numerator, alpha.denominator)
    lam = tuple(partition)
    if len(lam) == 2 and lam[1] == 1 and theta == Fraction(1, lam[0]):
        root_mult = lam[0]
        h = pi + sp.Rational(root_mult, root_mult + 1) * c
        residual = (
            sa * (root_mult / pi + 1 / (pi - c))
            - sx * ((root_mult * W - 1) / pi + (W + 1) / (pi - c) + 1 / h)
            - constant * pi / ((pi - c) * h)
        )
    elif lam == (2, 2) and theta == Fraction(3, 2):
        base = pi**2 - c
        integral = pi**7 / 7 - 3 * c * pi**5 / 5 + c**2 * pi**3 - c**3 * pi
        residual = (
            sa * (4 * pi / base)
            - sx * ((2 * W - 3) * 2 * pi / base + sp.diff(integral, pi) / integral)
            - constant * base**3 / (7 * integral)
        )
    elif lam == (2, 1, 1) and theta == Fraction(3, 2):
        base = pi**2 - c
        h = pi**2 + sp.Rational(2, 5) * c
        residual = (
            sa * (2 / pi + 2 * pi / base)
            - sx * ((2 * W - 3) / pi + (W + 1) * 2 * pi / base + 2 * pi / h)
            - constant * pi**3 / (base * h)
        )
    elif lam == (2, 1, 1, 1) and theta == Fraction(5, 2):
        base = pi**3 - c
        h = pi**3 + sp.Rational(2, 7) * c
        residual = (
            sa * (2 / pi + 3 * pi**2 / base)
            - sx * ((2 * W - 5) / pi + (W + 1) * 3 * pi**2 / base + 3 * pi**2 / h)
            - constant * pi**5 / (base * h)
        )
    else:
        raise AssertionError((theta, lam))
    return sp.factor(sp.together(residual)) == 0


def singular_program(leaves: list[dict[str, Any]]) -> str:
    lines = ["option(redSB);", ""]
    for index, leaf in enumerate(leaves, 1):
        leaf_id = leaf["leaf_id"]
        K = leaf["K"]
        collision = leaf["face_chart"]["collision_ratio_chart"]
        lines.extend(
            [
                f"ring R{index}=0,(r,c,Zc,U,H,z,eta),dp;",
                f"poly row=U-{K}*H;",
                (
                    "ideal I=c-r*(r-1),Zc*c-1,row;"
                    if collision
                    else "ideal I=Zc*c-1,row;"
                ),
                "ideal G=std(I);",
                f"int pass{index}=1;",
                f"if (row==0) {{ pass{index}=0; }}",
                f"if (reduce(1,G)!=1) {{ pass{index}=0; }}",
                f"poly solved=subst(row,H,U/{K});",
                f"if (solved!=0) {{ pass{index}=0; }}",
                f"if (diff(row,z)!=0) {{ pass{index}=0; }}",
                "ideal N=I,c;",
                f"if (reduce(1,std(N))!=0) {{ pass{index}=0; }}",
                (
                    f'if (pass{index}==1) {{ print("{leaf_id}|ROW_NONZERO=1|NF1=1|OFFSET_IDEAL_UNIT=0|'
                    'TRIANGULAR_H_SOLVE=1|ARC_Z_FREE=1|C0_NEGCTRL_UNIT=1|STATUS=SURVIVES_RESIDUAL"); }'
                ),
                f'if (pass{index}==0) {{ print("{leaf_id}|FAIL"); }}',
                "",
            ]
        )
    lines.append("exit;")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=INPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    hashes: dict[str, Any] = {}
    for basename, expected in EXPECTED.items():
        actual = sha256(args.inputs / basename)
        status = "PASS" if actual == expected else "FAIL"
        hashes[basename] = {"expected": expected, "actual": actual, "status": status}
    if any(item["status"] != "PASS" for item in hashes.values()):
        raise SystemExit("real charged-input content mismatch")

    split_window = load_split_window(args.inputs / "split_window.py")
    rows = [json.loads(line) for line in (args.inputs / "roster.jsonl").read_text().splitlines()]
    family = [row for row in rows if row["split_window"].get("applies") is True]
    assert len(family) == 20

    pi, c, r, eta = sp.symbols("pi c r eta")
    leaves: list[dict[str, Any]] = []
    for roster_line, row in enumerate(rows, 1):
        if row not in family:
            continue
        source = row["source"]
        view = split_window.skeleton_view(skeleton_mapping(source))
        regenerated = split_window.screen_view(view)["survivors"]
        stored = row["split_window"]["leaves"]
        assert [(x["rho"], x["lambda"], x["Q"], x["t"], x["k"]) for x in stored] == [
            (x["rho"], x["partition"], x["Q"], x["t"], x["k"]) for x in regenerated
        ]
        ds = view.d[view.s - 1]
        E = Fraction(view.n, ds)
        assert E.denominator == 1
        for leaf_index, stored_leaf in enumerate(stored, 1):
            rho = Fraction(stored_leaf["rho"])
            X = view.u * rho - view.v
            theta = (rho - 1) / (view.v - view.u * rho)
            kappa = Fraction(view.W) - theta
            alpha = view.W * X - 1 + rho
            beta = E * X
            gamma = (view.W + E) * X
            degree_q = view.W * view.u + 1
            K = int(E) * (view.v - view.u)
            assert alpha + beta - 1 == gamma + rho - 2

            chart = face_chart(view.u, rho.denominator, stored_leaf["lambda"])
            p = sp.sympify(chart["p"].replace("^", "**"), locals={"pi": pi, "c": c, "r": r})
            qexpr, qdisplay, eta_free = q_witness(
                p, chart["p"], view.u, view.W, theta, kappa,
                stored_leaf["lambda"], pi, c, eta,
            )
            if theta.denominator == 1:
                th = theta.numerator
                low = sp.Poly(sp.expand(p**th), pi)
                integral = sp.integrate(low.as_expr(), pi)
                leading_check = (
                    sp.expand(sp.diff(integral, pi) - low.as_expr()) == 0
                    and kappa.denominator == 1
                    and kappa + theta == view.W
                    and -X * (view.u * theta + 1) == view.v - view.u
                    and degree_q == view.u * view.W + 1
                )
            else:
                leading_check = verify_fractional_face(
                    view.W, X, alpha, view.v - view.u, theta,
                    stored_leaf["lambda"], pi, c,
                )
            if not leading_check:
                raise AssertionError(f"leading face failure {row['row_id']}-L{leaf_index:02d}")

            leaf_id = f"{row['row_id']}-L{leaf_index:02d}"
            endpoint = (
                f"({qtext(alpha + 1)})*R*(p^{int(E)})_pi+({qtext(alpha)})*q*S_pi"
                f"-({qtext(beta + 1)})*q_pi*S-({qtext(beta)})*R_pi*p^{int(E)}+M-{K}*H"
            )
            leaves.append(
                {
                    "leaf_id": leaf_id,
                    "row_id": row["row_id"],
                    "roster_jsonl_line": roster_line,
                    "source_tower": {
                        "n": view.n, "m": view.m, "s": view.s,
                        "M": list(view.M), "d": list(view.d), "V": list(view.V),
                        "mu_s": view.mu_s,
                    },
                    "rho": qtext(rho),
                    "lambda": stored_leaf["lambda"],
                    "u": view.u, "v": view.v, "E": int(E), "W": view.W,
                    "X": qtext(X), "alpha": qtext(alpha), "beta": qtext(beta), "gamma": qtext(gamma),
                    "degree_q": degree_q, "K": K,
                    "raw_offset_one_t_power": qtext(gamma + rho - 1),
                    "face_chart": chart,
                    "q": qdisplay,
                    "homogeneous_face_eta_free": eta_free,
                    "leading_face_check": "PASS_EXACT_Q",
                    "normalized_series": {
                        "A0": "q", "B0": f"p^{int(E)}", "C0": f"-{K}*p^{view.W + int(E)}",
                        "A1_intrinsic": "R(pi)", "B1_intrinsic": "S(pi)",
                        "C1_intrinsic": f"-{K}*H(pi)",
                        "middle_offset_convolution": "M(pi)",
                    },
                    "offset_one_row_in_S_pi": endpoint + "=0",
                    "coefficient_block_map": {
                        "domain": "Q[face moduli, coefficients of R,S,H and all 0<offset<1 series]",
                        "U_k_image": "[pi^k] of the endpoint terms plus the middle convolution M",
                        "block_ideal": f"<face localizer relations, U_k-{K}*H_k>",
                        "triangular_change": f"H_k |-> H_k-U_k/{K}",
                    },
                    "decision": "SURVIVES[XU71_OFFSET_ONE_RESIDUAL]",
                    "realization_open": "OPEN[XU71_OFFSET_ONE_REALIZATION_MAP_MISSING]",
                    "not_vacuous": True,
                    "not_attainment": True,
                }
            )

    assert len(leaves) == 36
    program = singular_program(leaves)
    proc = subprocess.run(
        ["Singular", "-q"], input=program, text=True, capture_output=True, check=False
    )
    if proc.returncode != 0 or proc.stderr.strip():
        raise SystemExit(f"Singular failure rc={proc.returncode}: {proc.stderr.strip()}")
    printed = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if len(printed) != 36 or any(line.endswith("|FAIL") for line in printed):
        raise SystemExit("unexpected Singular decision lines: " + repr(printed))
    by_id = {line.split("|", 1)[0]: line for line in printed}
    assert set(by_id) == {leaf["leaf_id"] for leaf in leaves}
    for leaf in leaves:
        leaf["singular_printed_line"] = by_id[leaf["leaf_id"]]

    result = {
        "schema": "jc2.xu71-offset-one/v1",
        "scope": "offset-one row ideal only; the missing realization ideal is not invented",
        "input_verification": hashes,
        "source_correction": {
            "xu_p12_typo": "the displayed T_s exponent/deg(q) uses -mu_s+n-2",
            "forced_repair": "use -mu_s-2, as in Proposition 7.3, Xu p.13, and exponent alignment in (7.1)",
        },
        "ring_maps": {
            "puiseux": "x->t^-1, y->sum_{j<rho}a_j*t^j+pi*t^rho",
            "normalization": "a_s->1,a_1->1,b->-E*(v-u),J->1",
            "arc_jet": "pi->pi+z(pi)*t; its offset contribution is z*F0_pi+z_pi*F0",
            "coefficient_block": "U_k maps to coefficient pi^k of every offset-one term except -K*H",
        },
        "universal_rows": {
            "full_h": "sum_{r+s=h}((alpha+r)A_r(B_s)_pi-(beta+s)(A_r)_pi B_s)+C_h=0",
            "offset_one": "sum_{r+s=1}((alpha+r)A_r(B_s)_pi-(beta+s)(A_r)_pi B_s)+C_1=0",
            "support_warning": "include all rational r,s in (0,1); M denotes that convolution",
        },
        "singular": {
            "executable": "Singular -q",
            "coefficient_field": "Q",
            "generator_order": ["r", "c", "Zc", "U", "H", "z", "eta"],
            "method": "one exact triangular coefficient block per leaf; all coefficient blocks tensor independently",
            "printed_lines": printed,
        },
        "leaves": leaves,
        "verdict": {
            "family_C_rows": 20,
            "typed_ES_leaves": 36,
            "dead": 0,
            "survives_with_residual": 36,
            "vacuous": 0,
            "offset_row_systems_proper": 36,
            "actual_realization_systems_formed": 0,
        },
        "opens": [
            "OPEN[XU71_OFFSET_ONE_REALIZATION_MAP_MISSING]",
            "OPEN[XU71_OFFSET_ONE_RATIONAL_SUPPORT_UNSERIALIZED]",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.output.stat().st_size > 2_000_000:
        raise SystemExit("JSON exceeds the 2 MB report+JSON discipline by itself")
    print("\n".join(printed))
    print(json.dumps(result["verdict"], sort_keys=True))


if __name__ == "__main__":
    main()
