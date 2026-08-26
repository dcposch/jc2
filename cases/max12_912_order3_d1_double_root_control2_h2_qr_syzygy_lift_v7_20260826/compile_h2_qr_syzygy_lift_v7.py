#!/usr/bin/env python3
"""AWS-only exact h^2 Q-R filtered syzygy lift."""

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
V6 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826" /
      "compile_h_grade5_kernel_lift_v6.py")
V6_SHA = "c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce"
W0_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"
W6_SHA = "3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833"
C1_V6_SHA = "6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3"
G1 = [Fraction(5, 2), Fraction(-25, 18), Fraction(0), Fraction(1, 4),
      Fraction(-1, 3), Fraction(0), Fraction(0), Fraction(0)]


class LiftFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise LiftFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise LiftFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def coefficient_h(t, polynomial, degree):
    position = t.INDEX["h"]
    out = {}
    for monomial, coefficient in polynomial.items():
        if monomial[position] != degree:
            continue
        exponent = list(monomial)
        exponent[position] = 0
        out[tuple(exponent)] = coefficient
    return t.clean(out)


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def vector_json(vector):
    return [frac(value) for value in vector]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="h2_qr_lift.json")
    args = parser.parse_args()
    tag = require_aws()
    v6 = load(V6, V6_SHA, "h2_qr_v6_frozen")
    v5 = v6.load(v6.V5, v6.V5_SHA, "h2_qr_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "h2_qr_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "h2_qr_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "h2_qr_base_frozen")
    tails = t.load_charged_source().build()["tails"]
    table = t.source_power_table(v4.coefficient_images(t), tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(-1, t.monomial(Fraction(2, 3), la=15)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))
    base_fs = base.multipliers()
    base_fs[1] = base.add(base_fs[1], base.mon(Fraction(1, 12), q2=1))
    base_fs[2] = base.add(base_fs[2], base.mon(Fraction(-1, 9), q2=1))
    fs = {ell: t.add(v4.embed(base, t, base_fs[ell]),
                     t.monomial(G1[ell-1], h=1)) for ell in range(1, 9)}
    indices = list(range(1, 9))
    if args.order == "reverse":
        indices.reverse()
    w6 = {}
    for ell in indices:
        w6 = t.add(w6, t.multiply(fs[ell], rows[ell]))
    w0 = coefficient_h(t, w6, 0)
    if base.digest(v4.project_base(base, t, w0)) != W0_SHA:
        raise LiftFailure("h=0 witness custody")
    if t.digest(w6) != W6_SHA:
        raise LiftFailure(("V6 full witness custody", t.digest(w6), W6_SHA))
    c1 = coefficient_h(t, w6, 1)
    if t.digest(c1) != C1_V6_SHA:
        raise LiftFailure(("V6 h-linear custody", t.digest(c1), C1_V6_SHA))
    if v5.qr_component(t, c1) or v6.grade5_component(t, c1):
        raise LiftFailure("V6 lower-grade cancellation drift")
    c2 = coefficient_h(t, w6, 2)
    target_qr = v5.qr_component(t, c2)
    if len(target_qr) != 8:
        raise LiftFailure(("expected eight h2 QR terms", len(target_qr)))
    for monomial in target_qr:
        e = dict(zip(t.NAMES, monomial))
        boundary = (5 * (e["q2"] + e["q1"] + e["q0"])
                    + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"])
                    + e["la"] - 20)
        if boundary != Fraction(-15, 2):
            raise LiftFailure(("h2 QR boundary drift", e, boundary))
    row0 = [coefficient_h(t, rows[ell], 0) for ell in range(1, 9)]
    sources = [v5.qr_component(t, row) for row in row0]
    solved = v5.exact_rref(t, sources, t.scale(-1, target_qr))
    payload = {
        "tag": tag, "order": args.order, "v6_sha256": V6_SHA,
        "w0_sha256": W0_SHA, "w6_sha256": W6_SHA,
        "c1_v6_sha256": C1_V6_SHA,
        "h2_qr_sha256": t.digest(target_qr),
        "h2_qr_terms": t.canonical(target_qr),
        "row_qr_sha256": [t.digest(source) for source in sources],
        "graded_monomials": [dict(zip(t.NAMES, monomial))
                             for monomial in solved["monomials"]],
        "graded_rank": len(solved["pivots"]),
        "graded_pivots_zero_based": solved["pivots"],
        "rref_augmented": v5.rational_matrix(solved["matrix"]),
        "status": solved["status"],
    }
    if solved["status"] == "INCONSISTENT":
        payload["dual_cokernel"] = {
            "coefficients_by_monomial": vector_json(solved["dual"]),
            "target_pairing": frac(solved["target_pairing"]),
        }
        payload["firewall"] = "scalar h2 correction only"
        blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
        Path(args.output).write_text(blob)
        print(f"ORDER={args.order}")
        print("STATUS=INCONSISTENT_WITH_DUAL")
        print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
        print("PASS_H2_QR_SYZYGY_LIFT_V7_COKERNEL")
        return
    d = solved["solution"]
    corrected_fs = {ell: t.add(fs[ell], t.monomial(d[ell-1], h=2))
                    for ell in range(1, 9)}
    corrected = {}
    for ell in indices:
        corrected = t.add(corrected,
                          t.multiply(corrected_fs[ell], rows[ell]))
    if coefficient_h(t, corrected, 0) != w0 or coefficient_h(t, corrected, 1) != c1:
        raise LiftFailure("lower h coefficients changed")
    corrected_c2 = coefficient_h(t, corrected, 2)
    if v5.qr_component(t, corrected_c2):
        raise LiftFailure("h2 QR did not cancel")
    records, eta0, face, open_strict = v5.analyze_threshold(t, corrected)
    payload.update({
        "solution": vector_json(d),
        "solution_sha256": sha256(json.dumps(
            vector_json(d), separators=(",", ":")).encode()).hexdigest(),
        "corrected_witness_sha256": t.digest(corrected),
        "corrected_witness_terms": len(corrected),
        "corrected_c2_sha256": t.digest(corrected_c2),
        "corrected_c2_terms": len(corrected_c2),
        "residual_h2_qr_terms": 0,
        "eta_uniform_infimum": frac(eta0),
        "eta_equal_infimum_is_strict_on_open_quadrant": open_strict,
        "threshold_face_terms": face,
        "records": records,
        "firewall": "one scalar h2 QR correction; iterate remaining grades",
    })
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=SOLVABLE")
    print("H2_SOLUTION=" + ",".join(vector_json(d)))
    print(f"CORRECTED_WITNESS_SHA256={t.digest(corrected)}")
    print(f"ETA_UNIFORM_INFIMUM={frac(eta0)}")
    print(f"ETA_EQUAL_OPEN_STRICT={int(open_strict)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_H2_QR_SYZYGY_LIFT_V7_SOLVABLE")


if __name__ == "__main__":
    main()
