#!/usr/bin/env python3
"""Compile the exact slope-uniform D1 coefficient-infinity gate.

All source reconstruction and polynomial output are AWS-only.  The emitted
Singular program computes a saturated boundary ideal; this compiler itself
makes no component, arc, Taylor, D1, or JC2 claim.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = (ROOT / "cases" /
          "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
          "compile_gate_v2.py")
PARENT_SHA256 = "b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c"
ISOTRIVIAL_REVIEW = (ROOT / "xmodel" /
    "max12-912-order3-d1-isotrivial-strict-rees-saturation-20260825.md")
ISOTRIVIAL_REVIEW_SHA256 = "bdb369f187284df82935488288d3752c4781e527eec1c38da80b757a26f50c38"
SUPPORT_REVIEW = (ROOT / "xmodel" /
    "max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md")
SUPPORT_REVIEW_SHA256 = "a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee"

# B_i=C_i(p,c)+X_i is a polynomial automorphism over Q.  The entries are
# sparse polynomials in (p,c), represented by exponent-pair dictionaries.
CUBE_PC = {
    7: {(1, 0): Fraction(3)},
    6: {(0, 1): Fraction(3)},
    5: {(2, 0): Fraction(3)},
    4: {(1, 1): Fraction(6)},
    3: {(3, 0): Fraction(1), (0, 2): Fraction(3)},
    2: {(2, 1): Fraction(3)},
    1: {(1, 2): Fraction(3)},
    0: {(0, 3): Fraction(1)},
}
CUBE_STRING = {
    7: "3*p",
    6: "3*c",
    5: "3*p^2",
    4: "6*p*c",
    3: "p^3+3*c^2",
    2: "3*p^2*c",
    1: "3*p*c^2",
    0: "c^3",
}
TARGET_VARIABLE = {3: 11, 6: 12}  # in B0..B7,q,rho,k,mu,nu


class SlopeUniformFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_slope_uniform_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_parent():
    got = sha256(PARENT.read_bytes()).hexdigest()
    if got != PARENT_SHA256:
        raise SlopeUniformFailure(("parent hash mismatch", got, PARENT_SHA256))
    for path, expected in ((ISOTRIVIAL_REVIEW, ISOTRIVIAL_REVIEW_SHA256),
                           (SUPPORT_REVIEW, SUPPORT_REVIEW_SHA256)):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise SlopeUniformFailure(("review hash mismatch", str(path),
                                       got, expected))
    spec = importlib.util.spec_from_file_location("d1_slope_uniform_parent", PARENT)
    if spec is None or spec.loader is None:
        raise SlopeUniformFailure(str(PARENT))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_ordinary_twist(raw, parent):
    """Rebuild D_l from ordinary tails via r_l=t^(2l mod 3)D_l."""
    independent = parent.load_module(
        parent.INDEPENDENT_PATH, "d1_slope_uniform_ordinary_rebuild"
    )
    ordinary = independent.build()["tails"]
    digests = {}
    for ell in range(1, 9):
        rebuilt = {}
        quotient_power = (2 * ell) % 3
        for monomial, scalar in ordinary[ell].items():
            t_power = sum((index % 3) * monomial[index]
                          for index in range(8))
            if t_power < quotient_power or (t_power - quotient_power) % 3:
                raise SlopeUniformFailure(("ordinary twist character", ell,
                                           monomial, t_power,
                                           quotient_power))
            s_power = (t_power - quotient_power) // 3
            descended = tuple(monomial[:8]) + (
                s_power, monomial[8], 0, 0
            )
            add_term(rebuilt, descended, scalar)
        rebuilt = clean(rebuilt)
        if rebuilt != raw[ell]:
            raise SlopeUniformFailure(("ordinary twist mismatch", ell))
        digests[f"ordinary_r{ell}"] = independent.coefficient_digest(
            ordinary[ell]
        )
        digests[f"descended_D{ell}"] = row_digest(rebuilt)
    return digests


def clean(value):
    return {monomial: scalar for monomial, scalar in value.items() if scalar}


def add_term(value, monomial, scalar):
    value[monomial] = value.get(monomial, Fraction(0)) + scalar


def raw_tail_rows(rows):
    """Remove the three inhomogeneous targets from the reviewed rows."""
    out = {}
    for ell in range(1, 9):
        value = dict(rows[ell])
        target = [0] * 12
        if ell == 3:
            target[10] = 1  # mu
        elif ell == 6:
            target[11] = 1  # nu
        target = tuple(target)
        if ell in (3, 6, 8):
            if value.get(target) != -1:
                raise SlopeUniformFailure(("target coefficient", ell,
                                           value.get(target)))
            del value[target]
        for monomial in value:
            if monomial[10] or monomial[11]:
                raise SlopeUniformFailure(("raw tail contains load", ell,
                                           monomial))
        out[ell] = clean(value)
    return out


def verify_raw_weights(raw):
    report = {}
    for ell in range(1, 9):
        expected = 12 + ell
        checked = 0
        for monomial, scalar in raw[ell].items():
            if not scalar:
                continue
            weight = sum((9 - index) * monomial[index]
                         for index in range(8)) + 6 * monomial[9]
            if weight != expected:
                raise SlopeUniformFailure(("raw weighted homogeneity", ell,
                                           monomial, weight, expected))
            checked += 1
        report[f"D{ell}"] = {
            "expected_weight": expected,
            "checked_nonzero_monomials": checked,
            "sha256": row_digest(raw[ell]),
        }
    return report


def transform_rows(raw):
    """Apply s=1+q, Lambda=q^3*rho, kbar=Lambda^6*k exactly."""
    out = {}
    for ell in range(1, 9):
        value = {}
        for monomial, scalar in raw[ell].items():
            a_exp = monomial[:8]
            s_exp = monomial[8]
            k_exp = monomial[9]
            for q_from_s in range(s_exp + 1):
                transformed = list(a_exp) + [
                    q_from_s + 18 * k_exp,
                    6 * k_exp,
                    k_exp,
                    0,
                    0,
                ]
                add_term(value, tuple(transformed),
                         scalar * comb(s_exp, q_from_s))

        weight = 12 + ell
        target = [0] * 13
        target[8] = 3 * weight
        target[9] = weight
        if ell in TARGET_VARIABLE:
            target[TARGET_VARIABLE[ell]] = 1
            add_term(value, tuple(target), Fraction(-1))
        elif ell == 8:
            add_term(value, tuple(target), Fraction(-1))
        out[ell] = clean(value)
    return out


def pc_add(left, right):
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return clean(out)


def pc_mul(left, right):
    out = {}
    for (lp, lc), lv in left.items():
        for (rp, rc), rv in right.items():
            exponent = (lp + rp, lc + rc)
            out[exponent] = out.get(exponent, Fraction(0)) + lv * rv
    return clean(out)


def pc_pow(value, exponent):
    out = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        out = pc_mul(out, value)
    return out


def exceptional_rows(raw):
    """Specialize s=1,k=0 in the raw tails."""
    out = {}
    for ell in range(1, 9):
        value = {}
        for monomial, scalar in raw[ell].items():
            if monomial[9]:
                continue
            add_term(value, tuple(monomial[:8]), scalar)
        out[ell] = clean(value)
    return out


def verify_common_cubic(exceptional):
    for ell in range(1, 9):
        evaluated = {}
        for monomial, scalar in exceptional[ell].items():
            term = {(0, 0): scalar}
            for index, exponent in enumerate(monomial):
                term = pc_mul(term, pc_pow(CUBE_PC[index], exponent))
            evaluated = pc_add(evaluated, term)
        if evaluated:
            raise SlopeUniformFailure(("common-cubic source check", ell,
                                       evaluated))


def row_digest(value):
    serial = [[list(monomial), scalar.numerator, scalar.denominator]
              for monomial, scalar in sorted(value.items())]
    return sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()


def coefficient_string(value, coordinates):
    terms = []
    for monomial, scalar in sorted(value.items(), reverse=True):
        factors = []
        for index, exponent in enumerate(monomial[:8]):
            if not exponent:
                continue
            if coordinates == "B":
                atom = f"B{index}"
            elif index <= 5:
                atom = f"({CUBE_STRING[index]}+X{index})"
            else:
                atom = f"({CUBE_STRING[index]})"
            factors.append(atom if exponent == 1 else f"({atom})^{exponent}")
        for atom, exponent in zip(("q", "rho", "k", "mu", "nu"),
                                  monomial[8:]):
            if exponent == 1:
                factors.append(atom)
            elif exponent:
                factors.append(f"{atom}^{exponent}")
        coefficient = (str(scalar.numerator) if scalar.denominator == 1
                       else f"({scalar.numerator}/{scalar.denominator})")
        body = "*".join(factors)
        terms.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(terms).replace("+-", "-") or "0"


def singular_source(transformed, tag, coordinates, chart, control_only):
    if coordinates == "normal":
        projective = ["p", "c"] + [f"X{i}" for i in range(6)]
    else:
        projective = [f"B{i}" for i in range(8)]
    variables = ["q", "rho"] + projective + ["k", "mu", "nu"]
    if chart != "global":
        variables.append("v")
    first, second, third, *rest = projective
    toy_arc = [f"{first}-1", f"{second}-q", f"{third}-rho"] + rest
    axis = ["q", "rho", f"{first}-1"] + projective[1:]
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({','.join(variables)}),(dp(2),dp(8),dp({len(variables)-10}));",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(
            f"poly Psi{ell}={coefficient_string(transformed[ell], coordinates)};"
        )
    source_ideal = (f"{','.join(toy_arc)}" if control_only
                    else "Psi1,Psi2,Psi3,Psi4,Psi5,Psi6,Psi7,Psi8")
    lines.extend([
        f"ideal I={source_ideal};",
        "ideal QR=q*rho;",
        f"ideal irrelevant={','.join(projective)};",
        f"poly projective_product={'*'.join(projective)};",
        "ideal PROJECTIVE_PRODUCT=projective_product;",
        # Synthetic saturation controls run before source ideal operations.
        "ideal toy_pure=q,rho;",
        "list TP=sat(toy_pure,QR);",
        "ideal GTP=std(TP[1]);",
        "if (reduce(1,GTP)!=0) { print(\"FAIL_PURE_BOUNDARY_CONTROL\"); quit; }",
        f"ideal toy_arc={','.join(toy_arc)};",
        "list TAK=sat(toy_arc,QR);",
        "ideal toy_arc_boundary=TAK[1],q,rho;",
        "list TAH=sat(toy_arc_boundary,irrelevant);",
        "ideal GTAH=std(TAH[1]);",
        "if (reduce(1,GTAH)==0) { print(\"FAIL_STRICT_ARC_CONTROL\"); quit; }",
        f"ideal toy_slope_three=rho-1,{first}-1,{','.join(projective[1:])};",
        "list TS3K=sat(toy_slope_three,QR);",
        "ideal toy_slope_three_boundary=TS3K[1],q,rho;",
        "list TS3H=sat(toy_slope_three_boundary,irrelevant);",
        "ideal GTS3H=std(TS3H[1]);",
        "if (reduce(1,GTS3H)!=0) { print(\"FAIL_SLOPE_THREE_CONTROL\"); quit; }",
        f"ideal toy_axis={','.join(axis)};",
        "list TA_GOOD=sat(toy_axis,irrelevant);",
        "ideal GTA_GOOD=std(TA_GOOD[1]);",
        "if (reduce(1,GTA_GOOD)==0) { print(\"FAIL_IRRELEVANT_IDEAL_AXIS_CONTROL\"); quit; }",
        "list TA_BAD=sat(toy_axis,PROJECTIVE_PRODUCT);",
        "ideal GTA_BAD=std(TA_BAD[1]);",
        "if (reduce(1,GTA_BAD)!=0) { print(\"FAIL_PRODUCT_AXIS_NEGATIVE_CONTROL\"); quit; }",
        'print("PASS_SYNTHETIC_SATURATION_CONTROLS");',
        f'print("AWS_TAG={tag}");',
        f'print("COORDINATES={coordinates}");',
        f'print("CHART={chart}");',
        f'print("CONTROL_ONLY={int(control_only)}");',
        'print("COEFFICIENT_RING=POLYNOMIAL_Q_K_MU_NU_NO_LOCALIZATION");',
        'print("SOURCE_SCOPE=ALL_EIGHT_REVIEWED_D1_ROWS");',
        'print("REPARAMETERIZATION=Lambda=q^3*rho");',
        'print("START_K_SATURATION");',
        "list KS=sat(I,QR);",
        "ideal K=std(KS[1]);",
        'print("K_SATURATION_API=LIST_IDEAL_ONLY");',
        'print("K_GENERATOR_COUNT="+string(size(K)));',
        'print("START_SEQUENTIAL_SATURATION_CONTROL");',
        "ideal QIDEAL=q;",
        "ideal RHOIDEAL=rho;",
        "list KQ_LIST=sat(I,QIDEAL);",
        "list KSEQ_LIST=sat(KQ_LIST[1],RHOIDEAL);",
        "ideal KSEQ=std(KSEQ_LIST[1]);",
        "ideal K_MOD_KSEQ=reduce(K,KSEQ);",
        "ideal KSEQ_MOD_K=reduce(KSEQ,K);",
        "if (size(K_MOD_KSEQ)!=0 || size(KSEQ_MOD_K)!=0)",
        "{",
        '  print("FAIL_PRODUCT_SEQUENTIAL_SATURATION_DISAGREEMENT");',
        "  quit;",
        "}",
        'print("PASS_PRODUCT_SEQUENTIAL_SATURATION_AGREEMENT");',
    ])
    if chart == "global":
        lines.append("ideal boundary=K,q,rho;")
    else:
        chart_variable = ("p" if chart == "p" and coordinates == "normal"
                          else "c" if chart == "c" and coordinates == "normal"
                          else "B7" if chart == "p" else "B6")
        lines.append(f"ideal boundary=K,q,rho,v*{chart_variable}-1;")
    lines.extend([
        'print("START_PROJECTIVE_BOUNDARY_SATURATION");',
        "list HS=sat(boundary,irrelevant);",
        "ideal H=std(HS[1]);",
        'print("H_SATURATION_API=LIST_IDEAL_ONLY");',
        'print("H_GENERATOR_COUNT="+string(size(H)));',
        "if (reduce(1,H)==0)",
        "{",
        '  print("SLOPE_UNIFORM_H_IS_UNIT=1");',
        "}",
        "else",
        "{",
        '  print("SLOPE_UNIFORM_H_IS_UNIT=0");',
        '  print("H_BASIS_BEGIN");',
        "  H;",
        '  print("H_BASIS_END");',
        "}",
        'print("PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS");',
        'print("FIREWALL=H_UNIT_EXCLUDES_STRICT_ARCS_ONLY;NONUNIT_IS_SURVIVOR_NOT_EXISTENCE");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--coordinates", choices=("normal", "B"),
                        default="normal")
    parser.add_argument("--chart", choices=("global", "p", "c"),
                        default="global")
    parser.add_argument("--control-only", action="store_true")
    args = parser.parse_args()
    tag = require_aws()
    parent = load_parent()
    _, _, _, rows, parent_payload = parent.compile_all()
    raw = raw_tail_rows(rows)
    raw_weight_report = verify_raw_weights(raw)
    twist_digests = verify_ordinary_twist(raw, parent)
    transformed = transform_rows(raw)
    exceptional = exceptional_rows(raw)
    verify_common_cubic(exceptional)

    if args.singular:
        print(singular_source(transformed, tag, args.coordinates,
                              args.chart, args.control_only), end="")
        return

    # Pullback identities are exponent identities, not sampled evidence:
    # q=tau^n,rho=tau^(m-3n) gives q^18*rho^6=tau^(6m) and
    # q^(3w)*rho^w=tau^(mw), for every coprime m/n>3.
    payload = {
        "aws_tag": tag,
        "parent_compiler_sha256": PARENT_SHA256,
        "isotrivial_source_review_sha256": ISOTRIVIAL_REVIEW_SHA256,
        "exceptional_support_grok_review_sha256": SUPPORT_REVIEW_SHA256,
        "parent_row_sha256": parent_payload["row_sha256"],
        "raw_tail_sha256": {f"T{ell}": row_digest(raw[ell])
                             for ell in range(1, 9)},
        "raw_weighted_homogeneity": raw_weight_report,
        "ordinary_twist_exact_rebuild": twist_digests,
        "psi_sha256": {f"Psi{ell}": row_digest(transformed[ell])
                        for ell in range(1, 9)},
        "psi_supports": {f"Psi{ell}": len(transformed[ell])
                         for ell in range(1, 9)},
        "equations": {
            "q": "s-1",
            "Lambda": "q^3*rho",
            "kbar": "q^18*rho^6*k",
            "Psi_l": (
                "T_l(1+q,B,q^18*rho^6*k)-"
                "q^(3*(12+l))*rho^(12+l)*delta_l"
            ),
            "delta": {"3": "mu", "6": "nu", "8": "1"},
        },
        "pullback_identity": {
            "strict_slope": "q=tau^n,rho=tau^(m-3n),coprime m/n>3",
            "Lambda": "tau^m",
            "kbar": "tau^(6m)*k",
            "target_weight_w": "tau^(m*w)",
        },
        "common_cubic_normal_change": {
            "B7": "3*p", "B6": "3*c",
            **{f"B{i}": f"{CUBE_STRING[i]}+X{i}" for i in range(6)},
            "polynomial_automorphism_over_Q": True,
            "all_eight_exceptional_rows_zero_at_X_zero": True,
        },
        "ideals": {
            "K": "(Psi1,...,Psi8):(q*rho)^infinity",
            "H": "((K+(q,rho)):irrelevant_projective_ideal^infinity)",
            "projective_saturation_is_ideal_not_coordinate_product": True,
        },
        "coordinates": args.coordinates,
        "chart": args.chart,
        "control_only": args.control_only,
        "scope": (
            "source-exact slope-uniform strict-boundary compiler only; "
            "H=1 would exclude strict coefficient-infinity arcs, while "
            "H nonunit is only a survivor scheme; no rationality, Taylor, "
            "D1, counterexample, or JC2 inference"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-SLOPE-UNIFORM-COMPILER")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
