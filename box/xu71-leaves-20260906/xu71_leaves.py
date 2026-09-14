#!/usr/bin/env python3
"""Exact-Q audit of the family-C split leaves against Xu (7.1).

This driver intentionally stops at the first coefficient not present in the
charged inputs.  It verifies the frozen inputs, regenerates the split-screen
parameters, supplies an exact polynomial witness for every *leading* face ODE,
and records the universal offset-one row without inventing its missing jets.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


INPUT_DIR = Path("/tmp/jc2-lane.lw2JIQ/inputs")
DEFAULT_OUTPUT = Path("box/xu71-leaves-20260906/xu71-leaves.json")

EXPECTED = {
    "roster.jsonl": "cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf",
    "residual65-structure-fable5-20260905.md": "7d3ffbba4791a64c7c7d9e28546de67190d96edd3a47b431c116fec35394c927",
    "split-window-gate-opus5-20260905.md": "b72b7a3cd132f959dd7e083d10e8c1bdbd16637be3bf6066406d6c7172f707c5",
    "cone-vertex-gate-opus5-20260905.md": "72dfcd371f338767e303c6da0eab02337f257ad29409a9fc6b60cd2e85c20ecd",
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


def q(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def qtext(value: Any) -> str:
    value = q(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def load_split_window(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("charged_split_window", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load charged split_window.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def skeleton_mapping(source: dict[str, Any]) -> dict[str, Any]:
    """Declare the roster-array -> charged 1-based mapping explicitly."""
    return {
        "n": source["n"],
        "m": source["m"],
        "s": source["s"],
        "M": {index + 1: value for index, value in enumerate(source["M"])},
        "d": {index + 1: value for index, value in enumerate(source["d"])},
        "V": {index + 2: value for index, value in enumerate(source["V"])},
    }


def face_chart(u: int, denominator: int, partition: list[int]) -> dict[str, Any]:
    """One declared affine/Galois chart covering the partition stratum.

    The chart is an added normalization, not data serialized by the roster.
    The two exceptional charts need c(c-1), not merely c, inverted.
    """
    lam = tuple(partition)
    key = (u, denominator, lam)
    q1 = {
        (2, 1, (1, 1)): (
            "pi^2-c",
            "c",
            "translate the root midpoint to 0; c is the squared half-distance",
        ),
        (3, 1, (2, 1)): ("pi^2*(pi-c)", "c", "put the double root at 0 and the simple root at c"),
        (3, 1, (1, 1, 1)): (
            "pi*(pi-1)*(pi-r)",
            "r*(r-1)",
            "order three roots and use the affine gauge 0,1,r",
        ),
        (4, 1, (3, 1)): ("pi^3*(pi-c)", "c", "put the triple root at 0 and the simple root at c"),
        (5, 1, (4, 1)): ("pi^4*(pi-c)", "c", "put the quadruple root at 0 and the simple root at c"),
    }
    galois = {
        (3, 2, (1, 1, 1)): ("pi*(pi^2-c)", "c", "fixed zero plus one nonzero Q=2 orbit"),
        (4, 2, (2, 2)): ("(pi^2-c)^2", "c", "one Q=2 orbit, both roots double"),
        (4, 2, (2, 1, 1)): ("pi^2*(pi^2-c)", "c", "double fixed zero plus one simple Q=2 orbit"),
        (4, 3, (1, 1, 1, 1)): ("pi*(pi^3-c)", "c", "fixed zero plus one Q=3 orbit"),
        (5, 2, (3, 1, 1)): ("pi^3*(pi^2-c)", "c", "triple fixed zero plus one simple Q=2 orbit"),
        (5, 2, (2, 2, 1)): ("pi*(pi^2-c)^2", "c", "simple fixed zero plus one double Q=2 orbit"),
        (5, 2, (1, 1, 1, 1, 1)): (
            "pi*(pi^2-1)*(pi^2-r)",
            "r*(r-1)",
            "fixed zero; scale one of two Q=2 orbits to +/-1",
        ),
        (5, 3, (2, 1, 1, 1)): ("pi^2*(pi^3-c)", "c", "double fixed zero plus one simple Q=3 orbit"),
        (5, 4, (1, 1, 1, 1, 1)): ("pi*(pi^4-c)", "c", "fixed zero plus one Q=4 orbit"),
    }
    table = q1 if denominator == 1 else galois
    if key not in table:
        raise AssertionError(f"unmapped face chart {key}")
    polynomial, collision, gauge = table[key]
    root_modulus_is_c = collision == "c"
    if root_modulus_is_c:
        presentation = "Q[c,Zc]/(Zc*c-1)"
        generators = ["c", "Zc", "pi"]
        quotient_images = {"c": "c", "Zc": "c^-1"}
        specialization = "c |-> c0 != 0; Zc |-> c0^-1; pi |-> pi"
    else:
        presentation = f"Q[r,c,Zc]/(c-({collision}),Zc*c-1)"
        generators = ["r", "c", "Zc", "pi"]
        quotient_images = {"r": "r", "c": collision, "Zc": f"({collision})^-1"}
        collision_at_r0 = collision.replace("r", "r0")
        specialization = (
            f"r |-> r0 with {collision_at_r0} != 0; "
            f"c |-> {collision_at_r0}; Zc |-> ({collision_at_r0})^-1; pi |-> pi"
        )
    return {
        "coefficient_field": "Q",
        "base_change": f"Q -> {presentation}",
        "polynomial_ring": f"({presentation})[pi]",
        "generator_order": generators,
        "face_polynomial_p": polynomial,
        "collision_polynomial_L": collision,
        "localizer_relation": "Zc*c-1",
        "root_modulus_is_localized_c": root_modulus_is_c,
        "quotient_generator_images": quotient_images,
        "specialization_map_to_K_pi": specialization,
        "face_coefficient_map": "p_i |-> coefficient [pi^i] of the displayed p; q_j |-> [pi^j] of the displayed q witness",
        "gauge_map": gauge,
        "scope": "added universal chart; the roster itself serializes only rho and the multiplicity partition",
    }


def witness_description(
    u: int, W: int, theta: Fraction, partition: list[int], polynomial: str
) -> dict[str, Any]:
    """Return an exact polynomial q witness for the normalized face ODE."""
    lam = tuple(partition)
    if theta.denominator == 1:
        th = theta.numerator
        multiplier = u * th + 1
        return {
            "kind": "integer-theta integrating-factor witness",
            "q": f"{multiplier}*p^{W-th}*Integral(p^{th},dpi)",
            "p_substitution": polynomial,
            "polynomial": True,
            "monic": True,
            "degree": u * W + 1,
            "proof": "I'=p^theta; alpha=X*(W-theta); -X*(u*theta+1)=v-u",
            "homogeneous_solution_note": f"eta*p^{W-th} may also be added",
        }
    if len(lam) == 2 and lam[1] == 1 and theta == Fraction(1, lam[0]):
        r = lam[0]
        return {
            "kind": "fractional two-root witness",
            "q": f"pi^{r*W-1}*(pi-c)^{W+1}*(pi+{r}/{r+1}*c)",
            "polynomial": True,
            "monic": True,
            "degree": u * W + 1,
            "proof": "substitute y^r=pi-c into (u*theta+1)*Integral(p^theta,dpi)",
        }
    if lam == (2, 2) and theta == Fraction(3, 2):
        return {
            "kind": "fractional double-orbit witness",
            "q": f"7*(pi^2-c)^{2*W-3}*Integral((pi^2-c)^3,dpi)",
            "polynomial": True,
            "monic": True,
            "degree": u * W + 1,
            "proof": "p=(pi^2-c)^2, hence p^(3/2)=(pi^2-c)^3 on the declared chart",
            "homogeneous_solution_note": f"eta*(pi^2-c)^{2*W-3} may also be added",
        }
    if lam == (2, 1, 1) and theta == Fraction(3, 2):
        return {
            "kind": "fractional fixed-double witness",
            "q": f"pi^{2*W-3}*(pi^2-c)^{W+1}*(pi^2+2/5*c)",
            "polynomial": True,
            "monic": True,
            "degree": u * W + 1,
            "proof": "substitute y^2=pi^2-c into 7*Integral(p^(3/2),dpi)",
        }
    if lam == (2, 1, 1, 1) and theta == Fraction(5, 2):
        return {
            "kind": "fractional fixed-double Q=3 witness",
            "q": f"pi^{2*W-5}*(pi^3-c)^{W+1}*(pi^3+2/7*c)",
            "polynomial": True,
            "monic": True,
            "degree": u * W + 1,
            "proof": "substitute y^2=pi^3-c into (27/2)*Integral(p^(5/2),dpi)",
        }
    raise AssertionError((u, W, theta, lam))


def verify_fractional_witness(
    W: int, X: Fraction, alpha: Fraction, constant: int, theta: Fraction, partition: list[int]
) -> bool:
    """Check the high powers through their exact logarithmic derivatives."""
    pi, c = sp.symbols("pi c")
    sx = sp.Rational(X.numerator, X.denominator)
    sa = sp.Rational(alpha.numerator, alpha.denominator)
    lam = tuple(partition)
    if len(lam) == 2 and lam[1] == 1 and theta == Fraction(1, lam[0]):
        r = lam[0]
        h = pi + sp.Rational(r, r + 1) * c
        residual = (
            sa * (r / pi + 1 / (pi - c))
            - sx * ((r * W - 1) / pi + (W + 1) / (pi - c) + 1 / h)
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


def verify_integer_witness(polynomial: str, u: int, theta: int) -> bool:
    """Check only the low-degree antiderivative; high powers cancel formally."""
    pi, c, r = sp.symbols("pi c r")
    p = sp.sympify(polynomial.replace("^", "**"), locals={"pi": pi, "c": c, "r": r})
    base = sp.Poly(sp.expand(p**theta), pi)
    integral = sp.integrate(base.as_expr(), pi)
    return (
        sp.Poly(p, pi).degree() == u
        and sp.Poly(p, pi).LC() == 1
        and sp.expand(sp.diff(integral, pi) - base.as_expr()) == 0
        and sp.Poly(integral, pi).degree() == u * theta + 1
        and sp.Poly(integral, pi).LC() == sp.Rational(1, u * theta + 1)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=INPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    hashes: dict[str, Any] = {}
    for basename, expected in EXPECTED.items():
        actual = sha256(args.inputs / basename)
        hashes[basename] = {"expected": expected, "actual": actual, "status": "PASS" if actual == expected else "FAIL"}
    if any(item["status"] != "PASS" for item in hashes.values()):
        raise SystemExit("real charged-input content mismatch")

    split_window = load_split_window(args.inputs / "split_window.py")
    rows = [json.loads(line) for line in (args.inputs / "roster.jsonl").read_text().splitlines()]
    family = [row for row in rows if row["split_window"].get("applies") is True]
    assert len(family) == 20
    assert {row["row_id"] for row in family} == {row["row_id"] for row in rows if row["source"]["u_s"] >= 2}

    typed = [
        leaf
        for row in family
        for leaf in row["split_window"]["leaves"]
        if leaf["type"] == "ES_NECESSARY_LEAF_NOT_ATTAINMENT"
    ]
    assert len(typed) == 36
    assert sum(row["split_window"]["leaf_count"] for row in family) == 36
    assert sum(len(row["split_window"]["leaves"]) for row in family) == 36

    stale_report = (args.inputs / "residual65-structure-fable5-20260905.md").read_text()
    stale_38_occurrences = len(re.findall(r"\b38 (?:ES |typed ES |leaves)", stale_report))

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
        for leaf_index, leaf in enumerate(stored, 1):
            rho = Fraction(leaf["rho"])
            X = view.u * rho - view.v
            theta = (rho - 1) / (view.v - view.u * rho)
            kappa = Fraction(view.W) - theta
            alpha = view.W * X - 1 + rho
            beta = E * X
            gamma = (view.W + E) * X
            degree_q = view.W * view.u + 1
            constant = view.v - view.u
            assert rho.denominator == leaf["Q"] and 1 < rho < Fraction(view.v, view.u)
            assert rho.denominator <= view.u and sum(leaf["lambda"]) == view.u
            assert qtext(theta) == leaf["t"] and qtext(kappa) == leaf["k"]
            assert alpha == X * kappa
            assert -X * (view.u * theta + 1) == constant
            assert alpha + beta - 1 == gamma + rho - 2

            chart = face_chart(view.u, rho.denominator, leaf["lambda"])
            pi_symbol, c_symbol, r_symbol = sp.symbols("pi c r")
            p_expr = sp.sympify(
                chart["face_polynomial_p"].replace("^", "**"),
                locals={"pi": pi_symbol, "c": c_symbol, "r": r_symbol},
            )
            p_poly = sp.Poly(p_expr, pi_symbol)
            assert p_poly.degree() == view.u and p_poly.LC() == 1
            if rho.denominator > 1:
                assert all(
                    (view.u - monomial[0]) % rho.denominator == 0
                    for monomial, coefficient in p_poly.terms()
                    if coefficient != 0
                )
            coefficient_images = {
                f"p_{degree}": str(sp.expand(p_poly.coeff_monomial(pi_symbol**degree))).replace("**", "^")
                for degree in range(view.u + 1)
            }
            chart["face_coefficient_images"] = coefficient_images
            chart["image_checks"] = {
                "degree_p_equals_u": True,
                "p_monic": True,
                "G_allowed_degrees": True,
                "collision_coordinate_inverted_by_Zc": True,
            }
            witness = witness_description(view.u, view.W, theta, leaf["lambda"], chart["face_polynomial_p"])
            if theta.denominator == 1:
                leading_check = (
                    verify_integer_witness(chart["face_polynomial_p"], view.u, theta.numerator)
                    and
                    kappa.denominator == 1
                    and kappa + theta == view.W
                    and -X * (view.u * theta + 1) == constant
                    and witness["degree"] == degree_q
                )
                check_method = "exact Q[c,pi] antiderivative plus integrating-factor identities"
            else:
                leading_check = verify_fractional_witness(
                    view.W, X, alpha, constant, theta, leaf["lambda"]
                )
                check_method = "exact SymPy Q(c,pi) logarithmic-derivative normal form"
            assert leading_check

            special = None
            special_control = None
            if row["row_id"] == "R012" and rho == 3:
                special = "D=108, delta=3 (same leaf; not an extra count)"
                special_control = {
                    "p": "pi^2-c",
                    "q": "(pi^2-c)^23*(pi^5-(10/3)c*pi^3+5c^2*pi)",
                    "charged_face_source": "cone-vertex-gate-opus5-20260905.md:171-176",
                }
            elif row["row_id"] == "R015" and rho == 2:
                special = "(99,66), delta=2 / Xu (8.2) (same leaf; not an extra count)"
                special_control = {
                    "p": "pi^2*(pi+3*a)",
                    "q": "pi^25*(pi+3*a)^14*(pi-2*a)",
                    "chart_map": "canonical c=-3*a",
                    "source": "Xu v4 printed p.13, equation (8.2)",
                }
            elif row["row_id"] == "R015" and rho == Fraction(5, 2):
                special = "(99,66), delta=5/2 / Xu open case (same leaf; not an extra count)"
                special_control = {
                    "p": "pi*(pi^2-c)",
                    "q": "p^10*(10*Integral(p^3,dpi))",
                    "normalization_note": "Xu's literal q1'=-2p^3 differs by an absorbed nonzero leading scalar",
                    "source": "Xu v4 printed p.13, delta=5/2 paragraph",
                }

            leaves.append(
                {
                    "leaf_id": f"{row['row_id']}-L{leaf_index:02d}",
                    "row_id": row["row_id"],
                    "roster_jsonl_line": roster_line,
                    "D_user_to_source_n": source["n"],
                    "source_m": source["m"],
                    "source_delta_not_split_order": source["delta"],
                    "u": view.u,
                    "v": view.v,
                    "d_s": ds,
                    "E": int(E),
                    "W": view.W,
                    "rho": qtext(rho),
                    "P": rho.numerator,
                    "Q": rho.denominator,
                    "lambda_partition_not_Moh_lambda_s": leaf["lambda"],
                    "galois_zero_choices_not_separate_leaves": leaf["galois_zero_choices"],
                    "X": qtext(X),
                    "theta_split_screen_not_Xu_t": qtext(theta),
                    "kappa": qtext(kappa),
                    "alpha": qtext(alpha),
                    "beta": qtext(beta),
                    "gamma": qtext(gamma),
                    "degree_q": degree_q,
                    "leading_face_ode": f"({qtext(alpha)})*q*p_pi-({qtext(X)})*p*q_pi-({constant})*p^{view.W+1}=0",
                    "face_chart": chart,
                    "leading_witness": witness,
                    "leading_check": {"status": "PASS", "method": check_method},
                    "offset_one_raw_t_power": qtext(gamma + rho - 1),
                    "offset_one_row_general": "sum_{r+s=1}((alpha+r)A_r*(B_s)_pi-(beta+s)*(A_r)_pi*B_s)+C_1=0",
                    "offset_one_row_if_integer_gap": "(alpha+1)A_1(B_0)_pi+alpha*A_0(B_1)_pi-(beta+1)(A_0)_pi*B_1-beta*(A_1)_pi*B_0+C_1=0",
                    "charged_A1_B1_C1_present": False,
                    "arc_translation_control": "if pi->pi+z*t only, F_1=z*d(F_0)/dpi=0 modulo F_0",
                    "special_alias": special,
                    "special_control": special_control,
                    "xu71_decision": "OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]",
                    "leaf_status": "SURVIVES_THIS_LANE_AS_NECESSARY_ONLY_NOT_ATTAINMENT",
                    "not_classified_as": [
                        "ES_LEAF_DEAD_BY_XU71",
                        "MODULUS_ONLY_ROOT_C_EQ_0",
                        "OPEN[XU71-PLUS-ONE-VACUOUS]",
                    ],
                }
            )

    assert len(leaves) == 36
    assert all(leaf["leading_check"]["status"] == "PASS" for leaf in leaves)
    per_row = {
        row["row_id"]: {
            "leaf_count": len([leaf for leaf in leaves if leaf["row_id"] == row["row_id"]]),
            "dead_count": 0,
            "surviving_necessary_leaf_count": len([leaf for leaf in leaves if leaf["row_id"] == row["row_id"]]),
            "all_leaves_dead": False,
            "D2_alternative_retained": True,
        }
        for row in family
    }

    output = {
        "schema": "jc2.xu71-es-leaves/v1",
        "scope": "necessary face audit only; no carrier, attainment, or polynomial pair is asserted",
        "input_verification": hashes,
        "count_reconciliation": {
            "one_line_reducer": "jq -s '[.[]|select(.split_window.applies==true)|.split_window.leaves[]?|select(.type==\"ES_NECESSARY_LEAF_NOT_ATTAINMENT\")]|length' roster.jsonl",
            "family_C_rows": 20,
            "typed_ES_leaf_records": 36,
            "residual_report_printed_price": 38,
            "stale_38_phrase_occurrences_detected": stale_38_occurrences,
            "decision": 36,
            "open": "OPEN[ROSTER-ES-LEAF-COUNT-36-VS-38]",
        },
        "coordinate_map": {
            "source": "Xu arXiv:1604.07683v4, pp.1-2 and equation (7.1) on printed/PDF p.12",
            "field": "K algebraically closed, characteristic 0; exact coefficient arithmetic below is over Q",
            "map": "phi_sigma: K[x,y] -> K[pi]<<t>>, x |-> t^-1, y |-> sum_{j<rho} a_j*t^j+pi*t^rho",
            "coordinates": ["t", "pi"],
            "determinant_order": "A_t*B_pi-A_pi*B_t",
            "xu_identity": "Jac_{t,pi}(T_s(sigma),g(sigma))=-(T_s)_f(sigma)*t^(rho-2) for J=1",
            "warning": "rho is the split order; roster source.delta is a different array; theta is the split-screen auxiliary and is not Xu's t",
        },
        "universal_offset_rows": {
            "series": [
                "T_s(sigma)=t^alpha*sum_r A_r(pi)t^r",
                "g(sigma)=t^beta*sum_s B_s(pi)t^s",
                "(T_s)_f(sigma)=t^gamma*sum_h C_h(pi)t^h",
            ],
            "exponent_identity": "alpha+beta-1=gamma+rho-2",
            "row_h": "F_h=sum_{r+s=h}((alpha+r)A_r(B_s)_pi-(beta+s)(A_r)_pi B_s)+C_h=0",
            "raw_plus_one_power": "t^(gamma+rho-1), not bare t^(rho-1) unless t^gamma was first factored",
            "missing_support_fact": "the charged inputs do not rule out rational offsets 0<r<1",
            "missing_coefficients": ["A_1", "B_1", "C_1"],
            "actual_leaf_vacuity_proved": False,
            "arc_translation_only_control": "F_1=z*d(F_0)/dpi=0 modulo F_0",
        },
        "leaves": leaves,
        "per_row": per_row,
        "verdict": {
            "leading_face_ode_admitted": 36,
            "ES_LEAF_DEAD_BY_XU71": 0,
            "modulus_conditions_with_only_localized_root_c0": 0,
            "OPEN_XU71_PLUS_ONE_VACUOUS_actual_leaves": 0,
            "OPEN_XU71_PLUS_ONE_ARC_JET_DATA_MISSING": 36,
            "rows_with_every_leaf_dead": [],
            "surviving_necessary_leaves": 36,
            "family_C_row_residual": 20,
            "D2_alternatives_retained": 20,
            "overall_charged_residual_after_lane": 65,
            "fallacy_v2": "necessary != sufficient; no floor/attainment promotion; no exit-price assertion",
        },
        "opens": [
            "OPEN[ROSTER-ES-LEAF-COUNT-36-VS-38]",
            "OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]",
            "OPEN[XU71-OFFSET-ONE-SUPPORT]",
            "OPEN[XU71-FACE-GAUGE-LOCALIZER-MAP]",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    if args.output.stat().st_size > 1_000_000:
        raise SystemExit("JSON exceeds 1 MB disk-discipline cap")
    print(json.dumps(output["verdict"], sort_keys=True))


if __name__ == "__main__":
    main()
