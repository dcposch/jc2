#!/usr/bin/env python3
"""AWS-only eta-five correction inside the exact Q-R scalar kernel."""

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
V5 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826" /
      "compile_h_qr_syzygy_lift_v5.py")
V5_SHA = "8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366"
W0_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"
G0 = [Fraction(11, 6), Fraction(-11, 12)] + [Fraction(0)] * 6


class GradeFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load(path, expected, name):
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise GradeFailure((name, "hash", got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise GradeFailure((name, "import"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def grade5_component(t, polynomial):
    out = {}
    allowed = {"q2", "q1", "q0", "r2", "r1", "r0"}
    for monomial, coefficient in polynomial.items():
        e = dict(zip(t.NAMES, monomial))
        qdegree = e["q2"] + e["q1"] + e["q0"]
        rdegree = e["r2"] + e["r1"] + e["r0"]
        if (qdegree, rdegree) not in ((0, 2), (3, 0)):
            continue
        if any(power for name, power in e.items() if name not in allowed):
            continue
        out[monomial] = coefficient
    return t.clean(out)


def linear_combination(t, scalars, polynomials):
    out = {}
    for scalar, polynomial in zip(scalars, polynomials):
        out = t.add(out, t.scale(scalar, polynomial))
    return out


def kernel_basis(rref, pivots, columns):
    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [Fraction(0)] * columns
        vector[free_column] = Fraction(1)
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -rref[row][free_column]
        basis.append(vector)
    return free, basis


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def vector_json(vector):
    return [frac(value) for value in vector]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="h_grade5_lift.json")
    args = parser.parse_args()
    tag = require_aws()
    v5 = load(V5, V5_SHA, "h_grade5_v5_frozen")
    v4 = v5.load_module(v5.V4, v5.V4_SHA, "h_grade5_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "h_grade5_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "h_grade5_base_frozen")
    tails = t.load_charged_source().build()["tails"]
    table = t.source_power_table(v4.coefficient_images(t), tails)
    rows = {ell: t.substitute(tails[ell], table) for ell in range(1, 9)}
    rows[3] = t.add(rows[3], t.scale(-1, t.monomial(Fraction(2, 3), la=15)))
    rows[8] = t.add(rows[8], t.scale(-1, t.add(
        t.monomial(la=20), t.monomial(la=20, tau=1))))
    base_fs = base.multipliers()
    base_fs[1] = base.add(base_fs[1], base.mon(Fraction(1, 12), q2=1))
    base_fs[2] = base.add(base_fs[2], base.mon(Fraction(-1, 9), q2=1))
    fs = {ell: v4.embed(base, t, base_fs[ell]) for ell in range(1, 9)}
    indices = list(range(1, 9))
    if args.order == "reverse":
        indices.reverse()
    wh = {}
    for ell in indices:
        wh = t.add(wh, t.multiply(fs[ell], rows[ell]))
    w0 = v4.specialize_h_zero(t, wh)
    if base.digest(v4.project_base(base, t, w0)) != W0_SHA:
        raise GradeFailure("h=0 witness custody")
    c1 = v4.specialize_h_zero(
        t, v4.divide_h(t, t.add(wh, t.scale(-1, w0))))
    row0 = [v4.specialize_h_zero(t, rows[ell]) for ell in range(1, 9)]

    qr_sources = [v5.qr_component(t, row) for row in row0]
    qr_target = t.scale(-1, v5.qr_component(t, c1))
    qr_solved = v5.exact_rref(t, qr_sources, qr_target)
    if qr_solved["status"] != "SOLVABLE":
        raise GradeFailure("V5 QR system unexpectedly inconsistent")
    if qr_solved["solution"] != G0 or len(qr_solved["pivots"]) != 3:
        raise GradeFailure(("V5 QR solution/rank drift", qr_solved["solution"],
                            qr_solved["pivots"]))
    free_columns, qr_kernel = kernel_basis(
        qr_solved["matrix"], qr_solved["pivots"], 8)
    if len(qr_kernel) != 5:
        raise GradeFailure(("QR kernel dimension", len(qr_kernel)))
    for vector in qr_kernel:
        if v5.qr_component(t, linear_combination(t, vector, row0)):
            raise GradeFailure(("bad QR kernel vector", vector))

    residual0 = t.add(c1, linear_combination(t, G0, row0))
    next_piece = grade5_component(t, residual0)
    if not next_piece:
        raise GradeFailure("missing eta-five residual")
    for monomial in next_piece:
        e = dict(zip(t.NAMES, monomial))
        boundary = (5 * (e["q2"] + e["q1"] + e["q0"])
                    + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"])
                    + e["la"] - 20)
        if boundary != -5:
            raise GradeFailure(("grade-five boundary drift", e, boundary))
    kernel_grade_sources = [grade5_component(
        t, linear_combination(t, vector, row0)) for vector in qr_kernel]
    grade_solved = v5.exact_rref(
        t, kernel_grade_sources, t.scale(-1, next_piece))
    payload = {
        "tag": tag,
        "order": args.order,
        "v5_sha256": V5_SHA,
        "w0_sha256": W0_SHA,
        "qr_rank": len(qr_solved["pivots"]),
        "qr_pivots_zero_based": qr_solved["pivots"],
        "qr_free_columns_zero_based": free_columns,
        "qr_kernel_basis": [vector_json(vector) for vector in qr_kernel],
        "qr_kernel_basis_sha256": sha256(json.dumps(
            [vector_json(vector) for vector in qr_kernel],
            separators=(",", ":")).encode()).hexdigest(),
        "grade5_residual_sha256": t.digest(next_piece),
        "grade5_residual_terms": t.canonical(next_piece),
        "grade5_source_sha256": [t.digest(source)
                                 for source in kernel_grade_sources],
        "grade5_monomials": [dict(zip(t.NAMES, monomial))
                             for monomial in grade_solved["monomials"]],
        "grade5_rank": len(grade_solved["pivots"]),
        "grade5_pivots_zero_based": grade_solved["pivots"],
        "grade5_rref_augmented": v5.rational_matrix(grade_solved["matrix"]),
        "status": grade_solved["status"],
    }
    if grade_solved["status"] == "INCONSISTENT":
        payload["dual_cokernel"] = {
            "coefficients_by_monomial": vector_json(grade_solved["dual"]),
            "target_pairing": frac(grade_solved["target_pairing"]),
        }
        payload["firewall"] = (
            "complete obstruction only for scalar h corrections preserving "
            "the QR cancellation; polynomial multiplier corrections open")
        blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
        Path(args.output).write_text(blob)
        print(f"ORDER={args.order}")
        print("STATUS=INCONSISTENT_WITH_DUAL")
        print(f"GRADE5_RESIDUAL_SHA256={t.digest(next_piece)}")
        print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
        print("PASS_H_GRADE5_KERNEL_LIFT_V6_COKERNEL")
        return

    kernel_solution = grade_solved["solution"]
    g = list(G0)
    for scalar, vector in zip(kernel_solution, qr_kernel):
        g = [left + scalar * right for left, right in zip(g, vector)]
    corrected_fs = {
        ell: t.add(fs[ell], t.monomial(g[ell-1], h=1))
        for ell in range(1, 9)
    }
    corrected = {}
    for ell in indices:
        corrected = t.add(corrected,
                          t.multiply(corrected_fs[ell], rows[ell]))
    if v4.specialize_h_zero(t, corrected) != w0:
        raise GradeFailure("corrected h=0 mismatch")
    corrected_c1 = v4.specialize_h_zero(
        t, v4.divide_h(t, t.add(corrected, t.scale(-1, w0))))
    if v5.qr_component(t, corrected_c1):
        raise GradeFailure("QR cancellation lost")
    if grade5_component(t, corrected_c1):
        raise GradeFailure("grade-five component did not cancel")
    records, eta0, face, open_strict = v5.analyze_threshold(t, corrected)
    payload.update({
        "kernel_solution": vector_json(kernel_solution),
        "full_scalar_h_correction": vector_json(g),
        "full_scalar_h_correction_sha256": sha256(json.dumps(
            vector_json(g), separators=(",", ":")).encode()).hexdigest(),
        "corrected_witness_sha256": t.digest(corrected),
        "corrected_witness_terms": len(corrected),
        "corrected_c1_sha256": t.digest(corrected_c1),
        "corrected_c1_terms": len(corrected_c1),
        "residual_qr_terms": 0,
        "residual_grade5_terms": 0,
        "eta_uniform_infimum": frac(eta0),
        "eta_equal_infimum_is_strict_on_open_quadrant": open_strict,
        "threshold_face_terms": face,
        "records": records,
        "firewall": (
            "complete scalar h correction through closed-corner grade -5; "
            "iterate remaining grades; polynomial multipliers and h-adic lift open"),
    })
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=SOLVABLE")
    print("KERNEL_SOLUTION=" + ",".join(vector_json(kernel_solution)))
    print("FULL_H_CORRECTION=" + ",".join(vector_json(g)))
    print(f"CORRECTED_WITNESS_SHA256={t.digest(corrected)}")
    print(f"ETA_UNIFORM_INFIMUM={frac(eta0)}")
    print(f"ETA_EQUAL_OPEN_STRICT={int(open_strict)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_H_GRADE5_KERNEL_LIFT_V6_SOLVABLE")


if __name__ == "__main__":
    main()
