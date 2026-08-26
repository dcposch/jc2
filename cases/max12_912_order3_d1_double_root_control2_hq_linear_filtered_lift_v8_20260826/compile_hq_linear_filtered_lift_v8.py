#!/usr/bin/env python3
"""AWS-only exact 24-column h*Q filtered syzygy lift."""

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
V7 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826" /
      "compile_h2_qr_syzygy_lift_v7.py")
V7_SHA = "a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3"
W0_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"
W7_SHA = "efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5"
D2 = [Fraction(5, 24), Fraction(-2, 9)] + [Fraction(0)] * 6
QVARS = ("q2", "q1", "q0")


class FilteredLiftFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise FilteredLiftFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise FilteredLiftFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def q2r_component(t, polynomial):
    out = {}
    allowed = {"q2", "q1", "q0", "r2", "r1", "r0"}
    for monomial, coefficient in polynomial.items():
        e = dict(zip(t.NAMES, monomial))
        qdegree = e["q2"] + e["q1"] + e["q0"]
        rdegree = e["r2"] + e["r1"] + e["r0"]
        if qdegree != 2 or rdegree != 1:
            continue
        if any(power for name, power in e.items() if name not in allowed):
            continue
        out[monomial] = coefficient
    return t.clean(out)


def projected_union(t, v5, v6, polynomial):
    return t.add(t.add(v5.qr_component(t, polynomial),
                       v6.grade5_component(t, polynomial)),
                 q2r_component(t, polynomial))


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def vector_json(vector):
    return [frac(value) for value in vector]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="hq_linear_filtered_lift.json")
    args = parser.parse_args()
    tag = require_aws()

    v7 = load(V7, V7_SHA, "hq_v8_v7_frozen")
    v6 = v7.load(v7.V6, v7.V6_SHA, "hq_v8_v6_frozen")
    v5 = v6.load(v6.V5, v6.V5_SHA, "hq_v8_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "hq_v8_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "hq_v8_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "hq_v8_base_frozen")

    tails = t.load_charged_source().build()["tails"]
    table = t.source_power_table(v4.coefficient_images(t), tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(
        -1, t.monomial(Fraction(2, 3), la=15)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))

    base_fs = base.multipliers()
    base_fs[1] = base.add(base_fs[1], base.mon(Fraction(1, 12), q2=1))
    base_fs[2] = base.add(base_fs[2], base.mon(Fraction(-1, 9), q2=1))
    fs7 = {}
    for ell in range(1, 9):
        fs7[ell] = v4.embed(base, t, base_fs[ell])
        fs7[ell] = t.add(fs7[ell], t.monomial(v7.G1[ell - 1], h=1))
        fs7[ell] = t.add(fs7[ell], t.monomial(D2[ell - 1], h=2))

    indices = list(range(1, 9))
    if args.order == "reverse":
        indices.reverse()
    w7 = {}
    for ell in indices:
        product = (t.multiply(fs7[ell], rows[ell])
                   if args.order == "forward"
                   else t.multiply(rows[ell], fs7[ell]))
        w7 = t.add(w7, product)
    w0 = v7.coefficient_h(t, w7, 0)
    if base.digest(v4.project_base(base, t, w0)) != W0_SHA:
        raise FilteredLiftFailure("h=0 witness custody")
    if t.digest(w7) != W7_SHA:
        raise FilteredLiftFailure(("V7 witness custody", t.digest(w7), W7_SHA))

    c1 = v7.coefficient_h(t, w7, 1)
    if v5.qr_component(t, c1) or v6.grade5_component(t, c1):
        raise FilteredLiftFailure("V7 earlier h-linear cancellation drift")
    target_q2r = q2r_component(t, c1)
    if len(target_q2r) != 8:
        raise FilteredLiftFailure(("expected eight h Q2R terms", len(target_q2r)))
    for monomial in target_q2r:
        e = dict(zip(t.NAMES, monomial))
        boundary = (5 * (e["q2"] + e["q1"] + e["q0"])
                    + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"])
                    + e["la"] - 20)
        if boundary != Fraction(-5, 2):
            raise FilteredLiftFailure(("h Q2R boundary drift", e, boundary))

    row0 = {ell: v7.coefficient_h(t, rows[ell], 0)
            for ell in range(1, 9)}
    labels = [(ell, qvar) for ell in range(1, 9) for qvar in QVARS]
    sources = []
    for ell, qvar in labels:
        qmon = t.monomial(**{qvar: 1})
        raw = (t.multiply(qmon, row0[ell])
               if args.order == "forward"
               else t.multiply(row0[ell], qmon))
        sources.append(projected_union(t, v5, v6, raw))
    target_union = t.scale(-1, projected_union(t, v5, v6, c1))
    if target_union != t.scale(-1, target_q2r):
        raise FilteredLiftFailure("projected target union drift")
    solved = v5.exact_rref(t, sources, target_union)

    payload = {
        "tag": tag,
        "order": args.order,
        "v7_sha256": V7_SHA,
        "w0_sha256": W0_SHA,
        "w7_sha256": W7_SHA,
        "rows_full_sha256": [t.digest(rows[ell]) for ell in range(1, 9)],
        "rows_h0_sha256": [t.digest(row0[ell]) for ell in range(1, 9)],
        "v7_multiplier_sha256": [t.digest(fs7[ell]) for ell in range(1, 9)],
        "h_q2r_sha256": t.digest(target_q2r),
        "h_q2r_terms": t.canonical(target_q2r),
        "column_labels": [{"row_one_based": ell, "qvar": qvar}
                          for ell, qvar in labels],
        "column_source_sha256": [t.digest(source) for source in sources],
        "projected_monomials": [dict(zip(t.NAMES, monomial))
                                for monomial in solved["monomials"]],
        "projected_rank": len(solved["pivots"]),
        "projected_pivots_zero_based": solved["pivots"],
        "rref_augmented": v5.rational_matrix(solved["matrix"]),
        "status": solved["status"],
    }
    if solved["status"] == "INCONSISTENT":
        payload["dual_cokernel"] = {
            "coefficients_by_projected_monomial": vector_json(solved["dual"]),
            "target_pairing": frac(solved["target_pairing"]),
        }
        payload["firewall"] = (
            "complete only for 24 h*q_j row columns and the stated grade union")
        blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
        Path(args.output).write_text(blob)
        print(f"ORDER={args.order}")
        print("STATUS=INCONSISTENT_WITH_DUAL")
        print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
        print("PASS_HQ_LINEAR_FILTERED_LIFT_V8_COKERNEL")
        return

    solution = solved["solution"]
    corrections = {ell: {} for ell in range(1, 9)}
    for scalar, (ell, qvar) in zip(solution, labels):
        corrections[ell] = t.add(
            corrections[ell], t.monomial(scalar, h=1, **{qvar: 1}))
    corrected_fs = {ell: t.add(fs7[ell], corrections[ell])
                    for ell in range(1, 9)}
    corrected = {}
    for ell in indices:
        product = (t.multiply(corrected_fs[ell], rows[ell])
                   if args.order == "forward"
                   else t.multiply(rows[ell], corrected_fs[ell]))
        corrected = t.add(corrected, product)
    if v7.coefficient_h(t, corrected, 0) != w0:
        raise FilteredLiftFailure("corrected h=0 mismatch")
    corrected_c1 = v7.coefficient_h(t, corrected, 1)
    residual_union = projected_union(t, v5, v6, corrected_c1)
    if residual_union:
        raise FilteredLiftFailure(("projected union did not cancel", residual_union))
    records, eta0, face, open_strict = v5.analyze_threshold(t, corrected)
    payload.update({
        "solution": vector_json(solution),
        "solution_sha256": sha256(json.dumps(
            vector_json(solution), separators=(",", ":")).encode()).hexdigest(),
        "multiplier_correction_sha256": [t.digest(corrections[ell])
                                          for ell in range(1, 9)],
        "corrected_witness_sha256": t.digest(corrected),
        "corrected_witness_terms": len(corrected),
        "corrected_c1_sha256": t.digest(corrected_c1),
        "corrected_c1_terms": len(corrected_c1),
        "residual_projected_union_terms": 0,
        "eta_uniform_infimum": frac(eta0),
        "eta_equal_infimum_is_strict_on_open_quadrant": open_strict,
        "threshold_face_terms": face,
        "records": records,
        "firewall": (
            "exact 24-column h*Q correction through Q-R, R2/Q3, Q2R grades; "
            "other multiplier supports and later h grades remain open"),
    })
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=SOLVABLE")
    print("SOLUTION=" + ",".join(vector_json(solution)))
    print(f"PROJECTED_RANK={len(solved['pivots'])}")
    print(f"CORRECTED_WITNESS_SHA256={t.digest(corrected)}")
    print(f"ETA_UNIFORM_INFIMUM={frac(eta0)}")
    print(f"ETA_EQUAL_OPEN_STRICT={int(open_strict)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_HQ_LINEAR_FILTERED_LIFT_V8_SOLVABLE")


if __name__ == "__main__":
    main()
