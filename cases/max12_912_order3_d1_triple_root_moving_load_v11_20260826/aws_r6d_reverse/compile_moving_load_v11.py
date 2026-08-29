#!/usr/bin/env python3
"""AWS-only exact full-load discriminator for the frozen V8/V9 witness."""

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
V9_REVIEW = (ROOT / "xmodel" /
             "max12-912-order3-d1-double-root-control2-axis-covariance-review-grok-20260826.md")
V9_REVIEW_SHA = "f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226"
SUPPORT_REVIEW = (ROOT / "xmodel" /
                  "max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md")
SUPPORT_REVIEW_SHA = "a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee"


class MovingLoadFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_triple_root_moving_load_v11_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise MovingLoadFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise MovingLoadFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def full_character_weight(v9, t, monomial):
    e = dict(zip(t.NAMES, monomial))
    forbidden = {"p", "c", "a", "x", "y"}
    if any(e[name] for name in forbidden):
        raise MovingLoadFailure(("forbidden fixed variable", e))
    return sum(v9.CHARACTER.get(name, 0) * power
               for name, power in e.items())


def transport_full(v9, t, polynomial, prefactor):
    out = {}
    for monomial, coefficient in polynomial.items():
        exponent = list(monomial)
        if exponent[t.INDEX["a"]]:
            raise MovingLoadFailure("fixed polynomial already contains a")
        axis_power = prefactor - full_character_weight(v9, t, monomial)
        if axis_power < 0:
            raise MovingLoadFailure(("negative full-load axis power",
                                     prefactor, axis_power,
                                     dict(zip(t.NAMES, monomial))))
        exponent[t.INDEX["a"]] = axis_power
        key = tuple(exponent)
        out[key] = out.get(key, Fraction(0)) + coefficient
    return t.clean(out)


def build_full_rows(v9, t, tails, moving_axis):
    images = list(v9.coefficient_images(t, moving_axis))
    images[-1] = t.monomial(la=6, k=1)
    table = t.source_power_table(tuple(images), tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(
        -1, t.monomial(la=15, mu=1)))
    rows[6] = t.add(rows[6], t.scale(
        -1, t.monomial(la=18, nu=1)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))
    return rows


def specialize_fixed_loads(t, polynomial):
    kp = t.INDEX["k"]
    mp = t.INDEX["mu"]
    np = t.INDEX["nu"]
    out = {}
    for monomial, coefficient in polynomial.items():
        if monomial[kp] or monomial[np]:
            continue
        exponent = list(monomial)
        coefficient *= Fraction(2, 3) ** exponent[mp]
        exponent[mp] = 0
        key = tuple(exponent)
        out[key] = out.get(key, Fraction(0)) + coefficient
    return t.clean(out)


def frac(value):
    value = Fraction(value)
    return (str(value.numerator) if value.denominator == 1
            else f"{value.numerator}/{value.denominator}")


def reconstruct(v9, order):
    v8 = v9.load(v9.V8, v9.V8_SHA, "movingload_v8_frozen")
    v7 = v8.load(v8.V7, v8.V7_SHA, "movingload_v7_frozen")
    v6 = v7.load(v7.V6, v7.V6_SHA, "movingload_v6_frozen")
    v5 = v6.load(v6.V5, v6.V5_SHA, "movingload_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "movingload_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "movingload_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "movingload_base_frozen")
    tails = t.load_charged_source().build()["tails"]
    fixed_rows = v9.build_rows(t, tails, False)
    moving_rows = v9.build_rows(t, tails, True)
    fs = v9.fixed_multipliers(t, base, v4, v7, v8)
    deficits = [v9.character_weight(t, monomial) - (8 - ell)
                for ell in range(1, 9) for monomial in fs[ell]]
    clearing = max([0] + deficits)
    if clearing != 3:
        raise MovingLoadFailure(("clearing drift", clearing))
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
        raise MovingLoadFailure(("universal custody", t.digest(universal)))
    for ell in range(1, 9):
        if v9.transport(t, fixed_rows[ell], 12 + ell) != moving_rows[ell]:
            raise MovingLoadFailure(("fixed row covariance drift", ell))
    return t, tails, moving_fs, universal, indices


def central_boundary_check(t):
    p = t.monomial(p=1)
    c = t.monomial(c=1)
    coefficients = (
        t.power(c, 3),
        t.scale(3, t.multiply(p, t.power(c, 2))),
        t.scale(3, t.multiply(t.power(p, 2), c)),
        t.add(t.power(p, 3), t.scale(3, t.power(c, 2))),
        t.scale(6, t.multiply(p, c)),
        t.scale(3, t.power(p, 2)),
        t.scale(3, c),
        t.scale(3, p),
    )
    if any(t.specialize_zero(poly, {"p", "c"}) for poly in coefficients):
        raise MovingLoadFailure("central boundary coefficient did not vanish")
    return [t.digest(poly) for poly in coefficients]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="moving_load_v11.json")
    args = parser.parse_args()
    tag = require_aws()
    v9 = load(V9, V9_SHA, "movingload_v9_frozen")
    for path, expected, label in (
        (V9_REVIEW, V9_REVIEW_SHA, "V9 review"),
        (SUPPORT_REVIEW, SUPPORT_REVIEW_SHA, "support review"),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise MovingLoadFailure((label, got, expected))

    t, tails, moving_fs, fixed_universal, indices = reconstruct(v9, args.order)
    fixed_full_rows = build_full_rows(v9, t, tails, False)
    moving_full_rows = build_full_rows(v9, t, tails, True)
    row_covariance_sha = []
    for ell in range(1, 9):
        transported = transport_full(v9, t, fixed_full_rows[ell], 12 + ell)
        if transported != moving_full_rows[ell]:
            raise MovingLoadFailure(("full-load row covariance", ell,
                                     t.digest(transported),
                                     t.digest(moving_full_rows[ell])))
        row_covariance_sha.append(t.digest(transported))

    full_universal = {}
    for ell in indices:
        product = (t.multiply(moving_fs[ell], moving_full_rows[ell])
                   if args.order == "forward"
                   else t.multiply(moving_full_rows[ell], moving_fs[ell]))
        full_universal = t.add(full_universal, product)
    fixed_specialization = specialize_fixed_loads(t, full_universal)
    if fixed_specialization != fixed_universal:
        raise MovingLoadFailure(("fixed-load specialization",
                                 t.digest(fixed_specialization),
                                 t.digest(fixed_universal)))
    load_residual = t.add(full_universal, t.scale(-1, fixed_universal))

    target = next(iter(t.monomial(a=3, la=20)))
    split_target = next(iter(t.monomial(a=3, la=20, tau=1)))
    if full_universal.get(target) != 1 or full_universal.get(split_target) != 1:
        raise MovingLoadFailure(("target drift", full_universal.get(target),
                                 full_universal.get(split_target)))

    records = []
    obstructions = []
    corner_histogram = {}
    full_face_count = 0
    for monomial, coefficient in full_universal.items():
        e = dict(zip(t.NAMES, monomial))
        axis_coefficient = (
            e["a"] - 3 + e["la"] - 20 + e["rho"]
            + 3 * e["h"] + 4 * e["q2"] + 5 * e["q1"]
            + 6 * e["q0"] + 7 * e["r2"] + 8 * e["r1"]
            + 9 * e["r0"])
        if axis_coefficient != 0:
            raise MovingLoadFailure(("axis coefficient", e, axis_coefficient))
        corner = (Fraction(e["la"] - 20) + e["rho"]
                  + 5 * (e["q2"] + e["q1"] + e["q0"])
                  + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"]))
        slopes = {
            "u": e["q1"] + e["q0"], "v": e["q2"], "eta": e["h"],
            "T": e["tau"], "H": e["rho"],
        }
        role = ("target" if monomial == target else
                "positive_split_target" if monomial == split_target else None)
        corner_histogram[frac(corner)] = corner_histogram.get(frac(corner), 0) + 1
        obstruction = None
        if role is None:
            if corner < 0:
                obstruction = "negative_corner"
            elif corner == 0:
                full_face_count += 1
                if not any(slopes.values()):
                    obstruction = "nonstrict_load_tie"
        record = {
            "coefficient": frac(coefficient), "exponents": e,
            "axis_coefficient": axis_coefficient,
            "ell_corner": frac(corner), "open_slopes": slopes,
            "role": role, "obstruction": obstruction,
        }
        records.append(record)
        if obstruction:
            obstructions.append(record)
    records.sort(key=lambda item: json.dumps(item["exponents"], sort_keys=True))
    obstructions.sort(key=lambda item: json.dumps(item["exponents"], sort_keys=True))

    sensitivity = {}
    for name in ("k", "mu", "nu"):
        position = t.INDEX[name]
        sensitivity[name] = sum(1 for monomial in load_residual
                                if monomial[position])
    status = ("EXISTING_WITNESS_FULL_CONSTANT_LOAD_UNIFORM"
              if not obstructions else
              "EXISTING_WITNESS_NOT_FULL_CONSTANT_LOAD_UNIFORM")
    payload = {
        "tag": tag,
        "order": args.order,
        "v9_sha256": V9_SHA,
        "v9_review_sha256": V9_REVIEW_SHA,
        "support_review_sha256": SUPPORT_REVIEW_SHA,
        "universal_fixed_sha256": UNIVERSAL_SHA,
        "full_load_rows_sha256": row_covariance_sha,
        "full_load_universal_sha256": t.digest(full_universal),
        "full_load_universal_terms": len(full_universal),
        "fixed_specialization_sha256": t.digest(fixed_specialization),
        "load_residual_sha256": t.digest(load_residual),
        "load_residual_terms": len(load_residual),
        "load_sensitivity_term_counts": sensitivity,
        "corner_histogram": corner_histogram,
        "non_target_zero_corner_face_count": full_face_count,
        "obstruction_count": len(obstructions),
        "obstructions": obstructions,
        "records": records,
        "central_vertex": {
            "boundary_coefficient_sha256": central_boundary_check(t),
            "all_boundary_coefficients_zero_at_p_c_zero": True,
            "reviewed_projective_status": (
                "affine common-cubic cone vertex; irrelevant for Proj; "
                "not a strict coefficient-infinity leading centre"),
        },
        "status": status,
        "firewall": (
            "constant-field k,mu,nu only; nonpositive rescaled Lambda is a "
            "separate Lambda-leading chart/order question; other source "
            "charts, landing/accessibility, D1 and JC2 remain open"),
    }
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print(f"STATUS={status}")
    print(f"FULL_LOAD_UNIVERSAL_SHA256={t.digest(full_universal)}")
    print(f"LOAD_RESIDUAL_SHA256={t.digest(load_residual)}")
    print(f"LOAD_RESIDUAL_TERMS={len(load_residual)}")
    print(f"LOAD_SENSITIVITY={json.dumps(sensitivity, sort_keys=True)}")
    print(f"OBSTRUCTION_COUNT={len(obstructions)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_MOVING_LOAD_V11")


if __name__ == "__main__":
    main()

