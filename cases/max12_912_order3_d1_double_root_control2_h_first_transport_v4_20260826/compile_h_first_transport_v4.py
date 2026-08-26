#!/usr/bin/env python3
"""AWS-only exact first transport of corrected W into cusp h."""

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
TORIC = (ROOT / "cases" /
         "max12_912_order3_d1_double_root_toric_blowup_20260825" /
         "compile_toric_blowup.py")
TORIC_SHA = "c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490"
V1 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826" /
      "compile_q2_first_lift.py")
V1_SHA = "0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45"
W_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"


class TransportFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_h_first_transport_v4_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise TransportFailure((name, "hash"))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise TransportFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def coefficient_images(t):
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


def embed(base, t, polynomial):
    out = {}
    for monomial, coefficient in polynomial.items():
        powers = {name: exponent for name, exponent in zip(base.NAMES, monomial)
                  if exponent}
        out = t.add(out, t.monomial(coefficient, **powers))
    return out


def specialize_h_zero(t, polynomial):
    hp = t.INDEX["h"]
    return t.clean({m: c for m, c in polynomial.items() if m[hp] == 0})


def divide_h(t, polynomial):
    hp = t.INDEX["h"]
    out = {}
    for monomial, coefficient in polynomial.items():
        if monomial[hp] < 1:
            raise TransportFailure(("not h divisible", monomial))
        exponent = list(monomial)
        exponent[hp] -= 1
        out[tuple(exponent)] = coefficient
    return t.clean(out)


def project_base(base, t, polynomial):
    allowed = set(base.NAMES)
    out = {}
    for monomial, coefficient in polynomial.items():
        e = dict(zip(t.NAMES, monomial))
        if any(power for name, power in e.items() if name not in allowed):
            raise TransportFailure(("non-base projection", e))
        target = tuple(e[name] for name in base.NAMES)
        out[target] = out.get(target, Fraction(0)) + coefficient
    return base.clean(out)


def record(t, monomial, coefficient):
    e = dict(zip(t.NAMES, monomial))
    form = {
        "eta": e["h"],
        "delta": e["q2"],
        "beta": e["q1"] + e["q0"],
        "alpha": e["r2"] + e["r1"] + e["r0"],
        "constant": e["la"] - 20,
        "t": e["tau"],
        "H_over_L": e["rho"],
    }
    return {"coefficient": str(coefficient), "exponents": e,
            "difference_form": form}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="h_transport.json")
    args = parser.parse_args()
    tag = require_aws()
    t = load(TORIC, TORIC_SHA, "h_transport_toric_frozen")
    base = load(V1, V1_SHA, "h_transport_v1_frozen")
    charged = t.load_charged_source()
    built = charged.build()
    tails = built["tails"]

    # Independent ordinary-homogeneity checksum used by the axis reduction.
    homogeneity = {}
    for ell in range(1, 9):
        weights = set()
        for monomial, coefficient in tails[ell].items():
            if coefficient:
                weights.add(sum((9-i)*monomial[i] for i in range(8))
                            + 6*monomial[8])
        if weights != {12+ell}:
            raise TransportFailure(("ordinary homogeneity", ell, weights))
        homogeneity[str(ell)] = 12+ell

    images = coefficient_images(t)
    table = t.source_power_table(images, tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(-1, t.monomial(Fraction(2, 3), la=15)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))

    fs = base.multipliers()
    fs[1] = base.add(fs[1], base.mon(Fraction(1, 12), q2=1))
    fs[2] = base.add(fs[2], base.mon(Fraction(-1, 9), q2=1))
    wh = {}
    indices = list(range(1, 9))
    if args.order == "reverse":
        indices.reverse()
    for ell in indices:
        wh = t.add(wh, t.multiply(embed(base, t, fs[ell]), rows[ell]))
    w0 = specialize_h_zero(t, wh)
    projected = project_base(base, t, w0)
    if base.digest(projected) != W_SHA or len(projected) != 37:
        raise TransportFailure(("h=0 custody", base.digest(projected),
                                len(projected)))
    correction = divide_h(t, t.add(wh, t.scale(-1, w0)))
    if not correction:
        raise TransportFailure("unexpected h-independent witness")

    records = [record(t, m, c) for m, c in wh.items()]
    records.sort(key=lambda x: json.dumps(x["exponents"], sort_keys=True))
    thresholds = []
    bad_for_small_eta = []
    threshold_face = []
    for item in records:
        e, f = item["exponents"], item["difference_form"]
        is_target = e["la"] == 20 and sum(e.values()) == 20
        is_tau = e["la"] == 20 and e["tau"] == 1 and sum(e.values()) == 21
        if is_target or is_tau:
            continue
        # At alpha=15/2, beta=delta=5 boundary, before eta contribution.
        base_constant = (Fraction(f["constant"]) + 5*f["beta"]
                         + 5*f["delta"] + Fraction(15, 2)*f["alpha"])
        item["alpha15_2_beta5u_delta5v_eta"] = {
            "constant": str(base_constant),
            "u": f["beta"], "v": f["delta"], "eta": f["eta"],
        }
        if f["eta"] and base_constant < 0:
            value = -base_constant / f["eta"]
            thresholds.append(value)
            bad_for_small_eta.append(item)
    eta0 = max(thresholds) if thresholds else Fraction(0)
    for item in records:
        data = item.get("alpha15_2_beta5u_delta5v_eta")
        if data is None:
            continue
        value = Fraction(data["constant"]) + eta0 * data["eta"]
        if value == 0:
            threshold_face.append(item["exponents"])

    correction_blob = json.dumps(t.canonical(correction), separators=(",", ":"))
    canonical = {
        "w0_sha256": W_SHA,
        "wh_term_count": len(wh),
        "h_correction_term_count": len(correction),
        "h_correction_sha256": sha256(correction_blob.encode()).hexdigest(),
        "ordinary_homogeneity": homogeneity,
        "records": records,
        "eta_uniform_threshold_open_quadrant": str(eta0),
        "terms_bad_for_some_positive_eta": bad_for_small_eta,
        "threshold_face_monomials": sorted(
            threshold_face, key=lambda x: json.dumps(x, sort_keys=True)),
        "axis_unit_normalization": {
            "f": "a^-9*f(a*z)", "Lambda": "a^-1*Lambda",
            "rho": "a^-1*rho", "tau": "tau",
            "q2_q1_q0": ["a^-4*q2", "a^-5*q1", "a^-6*q0"],
            "r2_r1_r0": ["a^-7*r2", "a^-8*r1", "a^-9*r0"],
            "loads": "k,mu,nu unchanged",
        },
        "firewall": "unchanged corrected multipliers only; low terms trigger syzygy lift",
    }
    blob = json.dumps(canonical, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print(f"W0_SHA256={W_SHA}")
    print(f"WH_TERM_COUNT={len(wh)}")
    print(f"H_CORRECTION_TERM_COUNT={len(correction)}")
    print(f"H_CORRECTION_SHA256={canonical['h_correction_sha256']}")
    print(f"ETA_THRESHOLD={eta0}")
    print(f"BAD_SMALL_ETA_TERMS={len(bad_for_small_eta)}")
    print(f"THRESHOLD_FACE_TERMS={len(threshold_face)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_H_FIRST_TRANSPORT_V4")


if __name__ == "__main__":
    main()
