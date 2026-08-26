#!/usr/bin/env python3
"""AWS-only exact halfspace certificate for the corrected q2 witness."""

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
V2 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826" /
      "compile_q2_syzygy_lift_v2.py")
V2_SHA = "5c8e74ffa2acee40ab8ab0c2e68c44ddcbc2927722994c0d7488eb6c389f4611"
W_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"


class ConeFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_q2_cone_v3_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_v2():
    if sha256(V2.read_bytes()).hexdigest() != V2_SHA:
        raise ConeFailure("V2 hash")
    spec = importlib.util.spec_from_file_location("q2_syzygy_v2_frozen", V2)
    if spec is None or spec.loader is None:
        raise ConeFailure("V2 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def build_corrected(v2):
    base = v2.load_v1()
    tails = base.load_charged().build()["tails"]
    images = base.coefficient_images()
    rows = {
        ell: base.add(base.substitute(tails[ell], images),
                      base.scale(-1, base.target(ell)))
        for ell in range(1, 9)
    }
    fs = base.multipliers()
    fs[1] = base.add(fs[1], base.mon(Fraction(1, 12), q2=1))
    fs[2] = base.add(fs[2], base.mon(Fraction(-1, 9), q2=1))
    corrected = {}
    for ell in range(1, 9):
        corrected = base.add(corrected, base.mul(fs[ell], rows[ell]))
    if len(corrected) != 37 or base.digest(corrected) != W_SHA:
        raise ConeFailure(("corrected W custody", len(corrected),
                           base.digest(corrected)))
    return base, corrected


def form(base, monomial):
    e = dict(zip(base.NAMES, monomial))
    return {
        "delta": e["q2"],
        "beta": e["q1"] + e["q0"],
        "alpha": e["r2"] + e["r1"] + e["r0"],
        "constant": e["la"] - 20,
        "t": e["tau"],
        "h": e["rho"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="cone_certificate.json")
    args = parser.parse_args()
    tag = require_aws()
    v2 = load_v2()
    base, corrected = build_corrected(v2)
    items = sorted(corrected.items())
    if args.order == "reverse":
        items = list(reversed(items))

    records = []
    grouped = {}
    beta_face = []
    delta_face = []
    corner_face = []
    for monomial, coefficient in items:
        e = dict(zip(base.NAMES, monomial))
        f = form(base, monomial)
        is_target = e["la"] == 20 and sum(e.values()) == 20
        is_tau_target = (e["la"] == 20 and e["tau"] == 1
                         and sum(e.values()) == 21)
        record = {
            "coefficient": str(coefficient),
            "exponents": e,
            "difference_form": f,
            "target": is_target,
            "positive_split_target": is_tau_target,
        }
        records.append(record)
        key = tuple(f[name] for name in
                    ("delta", "beta", "alpha", "constant", "t", "h"))
        grouped.setdefault(key, []).append(record)
        if is_target or is_tau_target:
            continue
        # alpha=15/2, beta=5+u, delta=5+v.
        c = (Fraction(f["constant"]) + 5 * f["beta"]
             + 5 * f["delta"] + Fraction(15, 2) * f["alpha"])
        q = f["beta"]
        d = f["delta"]
        if c < 0 or q < 0 or d < 0 or (c == 0 and q + d == 0):
            raise ConeFailure(("quadrant certificate", record, c, q, d))
        record["alpha_15_2_beta5u_delta5v"] = {
            "constant": str(c), "u": q, "v": d,
        }
        # Tie sets on open coordinate boundary rays.
        if c == 0 and d == 0:
            beta_face.append(e)
        if c == 0 and q == 0:
            delta_face.append(e)
        if c == 0:
            corner_face.append(e)

    records = sorted(records, key=lambda x: json.dumps(x["exponents"], sort_keys=True))
    grouped_records = []
    for key, members in sorted(grouped.items()):
        grouped_records.append({
            "form_tuple_delta_beta_alpha_constant_t_h": list(key),
            "multiplicity": len(members),
            "monomials": sorted((x["exponents"] for x in members),
                                key=lambda x: json.dumps(x, sort_keys=True)),
        })
    canonical = {
        "corrected_w_sha256": W_SHA,
        "term_count": len(records),
        "distinct_form_count": len(grouped_records),
        "records": records,
        "grouped_forms": grouped_records,
        "beta5_delta_gt5_tie_monomials": sorted(
            beta_face, key=lambda x: json.dumps(x, sort_keys=True)),
        "delta5_beta_gt5_tie_monomials": sorted(
            delta_face, key=lambda x: json.dumps(x, sort_keys=True)),
        "beta5_delta5_corner_tie_monomials": sorted(
            corner_face, key=lambda x: json.dumps(x, sort_keys=True)),
        "theorem": (
            "alpha=15/2,beta>5,delta>5,t>0 gives unique least la^20; "
            "in particular 5<beta<6 and later q2 activation delta>beta"
        ),
        "firewall": "witness cone only; equality faces require saturation",
    }
    blob = json.dumps(canonical, sort_keys=True, indent=2) + "\n"
    output = Path(args.output)
    output.write_text(blob)
    print(f"ORDER={args.order}")
    print(f"W_SHA256={W_SHA}")
    print(f"TERM_COUNT={len(records)}")
    print(f"DISTINCT_FORM_COUNT={len(grouped_records)}")
    print(f"BETA_FACE_TIES={len(beta_face)}")
    print(f"DELTA_FACE_TIES={len(delta_face)}")
    print(f"CORNER_FACE_TIES={len(corner_face)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_Q2_CONE_V3")


if __name__ == "__main__":
    main()
