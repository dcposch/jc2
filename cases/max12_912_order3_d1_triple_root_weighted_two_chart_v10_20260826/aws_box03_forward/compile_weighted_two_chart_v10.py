#!/usr/bin/env python3
"""AWS-only exact weighted triple-root two-chart discriminator."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V9 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826" /
      "compile_axis_covariance_v9.py")
V9_SHA = "55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1"
UNIVERSAL_SHA = "53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0"
SQUAREFREE = (ROOT / "xmodel" /
              "max12-912-order3-d1-squarefree-common-cubic-order20-obstruction-20260825.md")
SQUAREFREE_SHA = "1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac"
SQUAREFREE_REVIEW = (ROOT / "xmodel" /
                     "max12-912-order3-d1-squarefree-common-cubic-order20-review-grok-20260825.md")
SQUAREFREE_REVIEW_SHA = "6883ef76710176ae9e091249224730e3ff181fa76c66c767b53b26c770c101d5"
V8_PROMOTION = (ROOT / "xmodel" /
                "max12-912-order3-d1-double-root-control2-hq-linear-filtered-lift-promotion-20260826.md")
V8_PROMOTION_SHA = "b503f6a70c39c256ba27f27823d5788bf5787badc507efa3079433064eb142e3"
V8_REVIEW = (ROOT / "xmodel" /
             "max12-912-order3-d1-double-root-control2-hq-linear-filtered-lift-review-grok-20260826.md")
V8_REVIEW_SHA = "2c3dbbd50089892197dd5ad5c0fb90776b5c2d2dea4ac2752f3b1a3218cc7d4c"


class TwoChartFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_triple_root_weighted_two_chart_v10_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise TwoChartFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise TwoChartFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def reconstruct(v9, order):
    v8 = v9.load(v9.V8, v9.V8_SHA, "twochart_v8_frozen")
    v7 = v8.load(v8.V7, v8.V7_SHA, "twochart_v7_frozen")
    v6 = v7.load(v7.V6, v7.V6_SHA, "twochart_v6_frozen")
    v5 = v6.load(v6.V5, v6.V5_SHA, "twochart_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "twochart_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "twochart_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "twochart_base_frozen")
    tails = t.load_charged_source().build()["tails"]
    moving_rows = v9.build_rows(t, tails, True)
    fixed_rows = v9.build_rows(t, tails, False)
    fs = v9.fixed_multipliers(t, base, v4, v7, v8)
    deficits = [v9.character_weight(t, monomial) - (8 - ell)
                for ell in range(1, 9) for monomial in fs[ell]]
    clearing = max([0] + deficits)
    if clearing != 3:
        raise TwoChartFailure(("clearing drift", clearing))
    moving_fs = {ell: v9.transport(t, fs[ell], clearing + 8 - ell)
                 for ell in range(1, 9)}
    indices = list(range(1, 9))
    if order == "reverse":
        indices.reverse()
    universal = {}
    for ell in indices:
        product = (t.multiply(moving_fs[ell], moving_rows[ell])
                   if order == "forward"
                   else t.multiply(moving_rows[ell], moving_fs[ell]))
        universal = t.add(universal, product)
    if t.digest(universal) != UNIVERSAL_SHA:
        raise TwoChartFailure(("universal custody", t.digest(universal)))
    for ell in range(1, 9):
        if v9.transport(t, fixed_rows[ell], 12 + ell) != moving_rows[ell]:
            raise TwoChartFailure(("row covariance drift", ell))
    return t, universal


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def discriminant(t, p, c):
    return t.add(t.scale(-4, t.power(p, 3)),
                 t.scale(-27, t.power(c, 2)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="weighted_two_chart.json")
    args = parser.parse_args()
    tag = require_aws()
    v9 = load(V9, V9_SHA, "twochart_v9_frozen")
    for path, expected, label in (
        (SQUAREFREE, SQUAREFREE_SHA, "squarefree theorem"),
        (SQUAREFREE_REVIEW, SQUAREFREE_REVIEW_SHA, "squarefree review"),
        (V8_PROMOTION, V8_PROMOTION_SHA, "V8 promotion"),
        (V8_REVIEW, V8_REVIEW_SHA, "V8 review"),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise TwoChartFailure((label, got, expected))

    t, universal = reconstruct(v9, args.order)
    charged = t.load_charged_source()
    tails = charged.build()["tails"]
    ordinary_homogeneity = {}
    for ell in range(1, 9):
        weights = {sum((9 - i) * monomial[i] for i in range(8))
                   + 6 * monomial[8]
                   for monomial, coefficient in tails[ell].items()
                   if coefficient}
        if weights != {12 + ell}:
            raise TwoChartFailure(("ordinary homogeneity", ell, weights))
        ordinary_homogeneity[str(ell)] = 12 + ell
    if ordinary_homogeneity["3"] != 15 or \
       ordinary_homogeneity["6"] != 18 or \
       ordinary_homogeneity["8"] != 20:
        raise TwoChartFailure(("target-weight bridge", ordinary_homogeneity))
    target = next(iter(t.monomial(a=3, la=20)))
    split_target = next(iter(t.monomial(a=3, la=20, tau=1)))
    records = []
    face_count = 0
    for monomial, coefficient in universal.items():
        e = dict(zip(t.NAMES, monomial))
        axis_coefficient = (
            e["a"] - 3 + e["la"] - 20 + e["rho"]
            + 3 * e["h"] + 4 * e["q2"] + 5 * e["q1"]
            + 6 * e["q0"] + 7 * e["r2"] + 8 * e["r1"]
            + 9 * e["r0"])
        if axis_coefficient != 0:
            raise TwoChartFailure(("axis coefficient", e, axis_coefficient))
        corner = (Fraction(e["la"] - 20) + e["rho"]
                  + 5 * (e["q2"] + e["q1"] + e["q0"])
                  + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"]))
        slopes = {
            "u": e["q1"] + e["q0"],
            "v": e["q2"],
            "eta": e["h"],
            "T": e["tau"],
            "H": e["rho"],
        }
        role = None
        if monomial == target:
            role = "target"
        elif monomial == split_target:
            role = "positive_split_target"
        else:
            if corner < 0:
                raise TwoChartFailure(("negative a-chart corner", e, corner))
            if corner == 0:
                face_count += 1
                if not any(slopes.values()):
                    raise TwoChartFailure(("nonstrict a-chart tie", e))
        records.append({
            "coefficient": frac(coefficient),
            "exponents": e,
            "axis_coefficient": axis_coefficient,
            "ell_corner": frac(corner),
            "open_slopes": slopes,
            "role": role,
        })
    if face_count != 30:
        raise TwoChartFailure(("face count", face_count))
    records.sort(key=lambda item: json.dumps(item["exponents"], sort_keys=True))

    # Use x for the a-chart coordinate s and y for the h-chart coordinate b.
    s = t.monomial(x=1)
    b = t.monomial(y=1)
    p_a = t.constant(-3)
    c_a = t.add(t.constant(2), s)
    delta_a = discriminant(t, p_a, c_a)
    expected_a = t.scale(-27, t.multiply(
        s, t.add(t.constant(4), s)))
    if delta_a != expected_a:
        raise TwoChartFailure("a-chart discriminant")

    p_h = t.scale(-3, t.power(b, 2))
    c_h = t.add(t.scale(2, t.power(b, 3)), t.constant(1))
    delta_h = discriminant(t, p_h, c_h)
    expected_h = t.scale(-27, t.add(
        t.scale(4, t.power(b, 3)), t.constant(1)))
    if delta_h != expected_h:
        raise TwoChartFailure("h-chart discriminant")

    # On 4*b^3+1=0, the overlap coordinate s=b^-3 equals -4.
    overlap_identity = t.add(t.scale(-4, t.power(b, 3)), t.constant(-1))
    if overlap_identity != t.scale(-1, t.add(
            t.scale(4, t.power(b, 3)), t.constant(1))):
        raise TwoChartFailure("overlap identity")

    # The opposite-axis coordinate a'=-a has h'=h+4a^3 and preserves p,c.
    # Coefficient identities: -3(-a)^2=-3a^2 and
    # 2(-a)^3+(h+4a^3)=2a^3+h.
    p_original = t.scale(-3, t.monomial(a=2))
    p_opposite = t.scale(-3, t.monomial(a=2))
    c_original = t.add(t.scale(2, t.monomial(a=3)), t.monomial(h=1))
    c_opposite = t.add(t.scale(-2, t.monomial(a=3)),
                       t.add(t.monomial(h=1),
                             t.scale(4, t.monomial(a=3))))
    if p_original != p_opposite or c_original != c_opposite:
        raise TwoChartFailure("opposite-axis coordinate")

    payload = {
        "tag": tag,
        "order": args.order,
        "v9_sha256": V9_SHA,
        "universal_witness_sha256": UNIVERSAL_SHA,
        "squarefree_theorem_sha256": SQUAREFREE_SHA,
        "squarefree_review_sha256": SQUAREFREE_REVIEW_SHA,
        "v8_promotion_sha256": V8_PROMOTION_SHA,
        "v8_review_sha256": V8_REVIEW_SHA,
        "ordinary_homogeneity": ordinary_homogeneity,
        "a_chart": {
            "substitution": "h=a^3*s",
            "positive_rescaled_lambda": "ell=wt(Lambda)-wt(a)>0",
            "axis_coefficients_all_zero": True,
            "non_target_zero_corner_face_count": face_count,
            "records": records,
            "residual_discriminant_sha256": t.digest(delta_a),
            "residual_discriminant": t.canonical(delta_a),
            "double_root_values": ["s=0", "s=-4"],
        },
        "h_chart": {
            "substitution": "h=t^3,a=t*b",
            "positive_rescaled_lambda": "ell=wt(Lambda)-wt(t)>0",
            "scaling_covariance": (
                "row i scales by t^(12+i), including fixed targets of "
                "weights 15,18,20"),
            "residual_discriminant_sha256": t.digest(delta_h),
            "residual_discriminant": t.canonical(delta_h),
            "squarefree_open": "4*b^3+1 != 0",
            "nonsquarefree_divisor_maps_to": "a-chart s=-4",
            "opposite_axis": "a'=-a,h'=h+4a^3",
        },
        "status": (
            "WEIGHTED_TWO_CHART_DIRECTIONAL_COVER_EXACT_"
            "CONDITIONAL_V9_REVIEW"),
        "firewall": (
            "frozen ordinary common-cubic source only; requires V9 review "
            "and positive rescaled Lambda; central a=h=0 arc, moving loads "
            "in the V8 witness, other source charts, D1 and JC2 remain open"),
    }
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=WEIGHTED_TWO_CHART_DIRECTIONAL_COVER_EXACT_CONDITIONAL_V9_REVIEW")
    print(f"A_CHART_FACE_COUNT={face_count}")
    print(f"A_CHART_DISCRIMINANT_SHA256={t.digest(delta_a)}")
    print(f"H_CHART_DISCRIMINANT_SHA256={t.digest(delta_h)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_WEIGHTED_TWO_CHART_V10")


if __name__ == "__main__":
    main()
