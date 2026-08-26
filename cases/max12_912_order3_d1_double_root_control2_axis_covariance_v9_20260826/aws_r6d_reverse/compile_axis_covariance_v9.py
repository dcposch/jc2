#!/usr/bin/env python3
"""AWS-only exact unit-axis covariance compiler for the frozen V8 witness."""

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
V8 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826" /
      "compile_hq_linear_filtered_lift_v8.py")
V8_SHA = "ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247"
W8_SHA = "e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b"
W0_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"
HQ = {1: {"q1": Fraction(-1, 36)},
      2: {"q0": Fraction(-1, 72)}}
CHARACTER = {
    "la": 1, "tau": 0, "rho": 1, "h": 3,
    "q2": 4, "q1": 5, "q0": 6,
    "r2": 7, "r1": 8, "r0": 9,
}


class CovarianceFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_axis_covariance_v9_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise CovarianceFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise CovarianceFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def coefficient_images(t, moving_axis):
    if moving_axis:
        p = t.scale(-3, t.monomial(a=2))
        c = t.add(t.scale(2, t.monomial(a=3)), t.monomial(h=1))
    else:
        p = t.constant(-3)
        c = t.add(t.constant(2), t.monomial(h=1))
    q2, q1, q0 = (t.monomial(q2=1), t.monomial(q1=1),
                  t.monomial(q0=1))
    r2, r1, r0 = (t.monomial(r2=1), t.monomial(r1=1),
                  t.monomial(r0=1))
    return (
        t.add(t.add(t.power(c, 3), t.multiply(c, q0)), r0),
        t.add(t.add(t.scale(3, t.multiply(p, t.power(c, 2))),
                    t.add(t.multiply(p, q0), t.multiply(c, q1))), r1),
        t.add(t.add(t.scale(3, t.multiply(t.power(p, 2), c)),
                    t.add(t.multiply(p, q1), t.multiply(c, q2))), r2),
        t.add(t.add(t.power(p, 3), t.scale(3, t.power(c, 2))),
              t.add(q0, t.multiply(p, q2))),
        t.add(t.scale(6, t.multiply(p, c)), q1),
        t.add(t.scale(3, t.power(p, 2)), q2),
        t.scale(3, c),
        t.scale(3, p),
        {},
    )


def build_rows(t, tails, moving_axis):
    table = t.source_power_table(coefficient_images(t, moving_axis), tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(
        -1, t.monomial(Fraction(2, 3), la=15)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))
    return rows


def fixed_multipliers(t, base, v4, v7, v8):
    base_fs = base.multipliers()
    base_fs[1] = base.add(base_fs[1], base.mon(Fraction(1, 12), q2=1))
    base_fs[2] = base.add(base_fs[2], base.mon(Fraction(-1, 9), q2=1))
    fs = {}
    for ell in range(1, 9):
        fs[ell] = v4.embed(base, t, base_fs[ell])
        fs[ell] = t.add(fs[ell], t.monomial(v7.G1[ell - 1], h=1))
        fs[ell] = t.add(fs[ell], t.monomial(v8.D2[ell - 1], h=2))
        for qvar, scalar in HQ.get(ell, {}).items():
            fs[ell] = t.add(fs[ell],
                            t.monomial(scalar, h=1, **{qvar: 1}))
    return fs


def character_weight(t, monomial):
    e = dict(zip(t.NAMES, monomial))
    forbidden = {"p", "c", "a", "x", "y", "k", "mu", "nu"}
    if any(e[name] for name in forbidden):
        raise CovarianceFailure(("forbidden fixed variable", e))
    return sum(CHARACTER.get(name, 0) * power for name, power in e.items())


def transport(t, polynomial, prefactor):
    out = {}
    for monomial, coefficient in polynomial.items():
        exponent = list(monomial)
        if exponent[t.INDEX["a"]]:
            raise CovarianceFailure("fixed polynomial already contains a")
        axis_power = prefactor - character_weight(t, monomial)
        if axis_power < 0:
            raise CovarianceFailure(("negative cleared axis power",
                                     prefactor, axis_power,
                                     dict(zip(t.NAMES, monomial))))
        exponent[t.INDEX["a"]] = axis_power
        key = tuple(exponent)
        out[key] = out.get(key, Fraction(0)) + coefficient
    return t.clean(out)


def specialize_a_one(t, polynomial):
    out = {}
    ap = t.INDEX["a"]
    for monomial, coefficient in polynomial.items():
        exponent = list(monomial)
        exponent[ap] = 0
        key = tuple(exponent)
        out[key] = out.get(key, Fraction(0)) + coefficient
    return t.clean(out)


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="axis_covariance.json")
    args = parser.parse_args()
    tag = require_aws()

    v8 = load(V8, V8_SHA, "axis_v9_v8_frozen")
    v7 = v8.load(v8.V7, v8.V7_SHA, "axis_v9_v7_frozen")
    v6 = v7.load(v7.V6, v7.V6_SHA, "axis_v9_v6_frozen")
    v5 = v6.load(v6.V5, v6.V5_SHA, "axis_v9_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "axis_v9_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "axis_v9_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "axis_v9_base_frozen")
    tails = t.load_charged_source().build()["tails"]

    ordinary_homogeneity = {}
    for ell in range(1, 9):
        weights = {sum((9 - i) * monomial[i] for i in range(8))
                   + 6 * monomial[8]
                   for monomial, coefficient in tails[ell].items()
                   if coefficient}
        if weights != {12 + ell}:
            raise CovarianceFailure(("ordinary homogeneity", ell, weights))
        ordinary_homogeneity[str(ell)] = 12 + ell

    fixed_rows = build_rows(t, tails, False)
    moving_rows = build_rows(t, tails, True)
    row_covariance_sha = []
    for ell in range(1, 9):
        transported = transport(t, fixed_rows[ell], 12 + ell)
        if transported != moving_rows[ell]:
            raise CovarianceFailure(("row covariance", ell,
                                     t.digest(transported),
                                     t.digest(moving_rows[ell])))
        row_covariance_sha.append(t.digest(transported))

    fs = fixed_multipliers(t, base, v4, v7, v8)
    indices = list(range(1, 9))
    if args.order == "reverse":
        indices.reverse()
    w8 = {}
    for ell in indices:
        product = (t.multiply(fs[ell], fixed_rows[ell])
                   if args.order == "forward"
                   else t.multiply(fixed_rows[ell], fs[ell]))
        w8 = t.add(w8, product)
    if t.digest(w8) != W8_SHA:
        raise CovarianceFailure(("V8 custody", t.digest(w8), W8_SHA))
    w0 = v7.coefficient_h(t, w8, 0)
    if base.digest(v4.project_base(base, t, w0)) != W0_SHA:
        raise CovarianceFailure("h-zero custody")

    deficits = []
    for ell in range(1, 9):
        for monomial in fs[ell]:
            deficits.append(character_weight(t, monomial) - (8 - ell))
    clearing_power = max([0] + deficits)
    if clearing_power != 3:
        raise CovarianceFailure(("axis clearing power", clearing_power))

    moving_fs = {ell: transport(t, fs[ell],
                                clearing_power + 8 - ell)
                 for ell in range(1, 9)}
    universal = {}
    for ell in indices:
        product = (t.multiply(moving_fs[ell], moving_rows[ell])
                   if args.order == "forward"
                   else t.multiply(moving_rows[ell], moving_fs[ell]))
        universal = t.add(universal, product)
    transported_w8 = transport(t, w8, clearing_power + 20)
    if universal != transported_w8:
        raise CovarianceFailure(("full transported identity",
                                 t.digest(universal), t.digest(transported_w8)))
    if specialize_a_one(t, universal) != w8:
        raise CovarianceFailure("a=1 specialization")

    p = t.scale(-3, t.monomial(a=2))
    c = t.add(t.scale(2, t.monomial(a=3)), t.monomial(h=1))
    discriminant = t.add(t.scale(-4, t.power(p, 3)),
                         t.scale(-27, t.power(c, 2)))
    expected_discriminant = t.scale(-27, t.multiply(
        t.monomial(h=1),
        t.add(t.scale(4, t.monomial(a=3)), t.monomial(h=1))))
    if discriminant != expected_discriminant:
        raise CovarianceFailure("discriminant factorization")

    target = next(iter(t.monomial(a=3, la=20)))
    split_target = next(iter(t.monomial(a=3, la=20, tau=1)))
    if universal.get(target) != 1 or universal.get(split_target) != 1:
        raise CovarianceFailure(("universal target coefficients",
                                 universal.get(target),
                                 universal.get(split_target)))

    records = []
    for monomial, coefficient in universal.items():
        e = dict(zip(t.NAMES, monomial))
        records.append({
            "coefficient": frac(coefficient),
            "exponents": e,
            "difference_from_a3_la20": {
                "axis": e["a"] - 3,
                "eta": e["h"],
                "delta": e["q2"],
                "beta_q1": e["q1"],
                "beta_q0": e["q0"],
                "alpha_r2": e["r2"],
                "alpha_r1": e["r1"],
                "alpha_r0": e["r0"],
                "constant": e["la"] - 20,
                "T_over_L": e["tau"],
                "H_over_L": e["rho"],
            },
        })
    records.sort(key=lambda item: json.dumps(item["exponents"], sort_keys=True))
    payload = {
        "tag": tag,
        "order": args.order,
        "v8_sha256": V8_SHA,
        "w8_sha256": W8_SHA,
        "w0_sha256": W0_SHA,
        "ordinary_homogeneity": ordinary_homogeneity,
        "character_weights": CHARACTER,
        "row_covariance_sha256": row_covariance_sha,
        "fixed_multiplier_sha256": [t.digest(fs[ell]) for ell in range(1, 9)],
        "axis_deficits": sorted(deficits),
        "minimal_common_axis_denominator": clearing_power,
        "cleared_multiplier_sha256": [t.digest(moving_fs[ell])
                                       for ell in range(1, 9)],
        "universal_witness_sha256": t.digest(universal),
        "universal_witness_terms": len(universal),
        "universal_witness": t.canonical(universal),
        "a_one_specialization_sha256": t.digest(specialize_a_one(t, universal)),
        "discriminant_sha256": t.digest(discriminant),
        "discriminant": t.canonical(discriminant),
        "target_monomial": dict(zip(t.NAMES, target)),
        "target_coefficient": "1",
        "split_target_monomial": dict(zip(t.NAMES, split_target)),
        "split_target_coefficient": "1",
        "records": records,
        "status": "UNIT_AXIS_COVARIANCE_EXACT",
        "firewall": (
            "localize at a; fixed loads and charged source; triple root and "
            "moving loads remain open"),
    }
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=UNIT_AXIS_COVARIANCE_EXACT")
    print(f"CLEARING_POWER={clearing_power}")
    print(f"UNIVERSAL_WITNESS_SHA256={t.digest(universal)}")
    print(f"UNIVERSAL_WITNESS_TERMS={len(universal)}")
    print(f"DISCRIMINANT_SHA256={t.digest(discriminant)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_AXIS_COVARIANCE_V9")


if __name__ == "__main__":
    main()
