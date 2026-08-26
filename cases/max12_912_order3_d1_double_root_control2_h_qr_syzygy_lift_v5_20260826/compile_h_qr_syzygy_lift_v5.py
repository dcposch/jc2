#!/usr/bin/env python3
"""AWS-only exact first graded h/Q-R syzygy correction."""

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
V4 = (ROOT / "cases" /
      "max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826" /
      "compile_h_first_transport_v4.py")
V4_SHA = "3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306"
W0_SHA = "ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b"


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
        "max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_module(path, expected, name):
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


def qr_component(t, polynomial):
    out = {}
    allowed = {"q2", "q1", "q0", "r2", "r1", "r0"}
    for monomial, coefficient in polynomial.items():
        e = dict(zip(t.NAMES, monomial))
        qdegree = e["q2"] + e["q1"] + e["q0"]
        rdegree = e["r2"] + e["r1"] + e["r0"]
        if qdegree != 1 or rdegree != 1:
            continue
        if any(power for name, power in e.items() if name not in allowed):
            continue
        out[monomial] = coefficient
    return t.clean(out)


def exact_rref(t, sources, target):
    monomials = sorted(set(target).union(*(set(source) for source in sources)))
    rows = len(monomials)
    columns = len(sources)
    matrix = []
    transform = []
    for index, monomial in enumerate(monomials):
        matrix.append([source.get(monomial, Fraction(0)) for source in sources]
                      + [target.get(monomial, Fraction(0))])
        transform.append([Fraction(int(index == j)) for j in range(rows)])
    pivots = []
    pivot_row = 0
    for column in range(columns):
        selected = next((row for row in range(pivot_row, rows)
                         if matrix[row][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        transform[pivot_row], transform[selected] = (
            transform[selected], transform[pivot_row])
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        transform[pivot_row] = [entry / pivot
                                for entry in transform[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [left - factor * right for left, right in
                           zip(matrix[row], matrix[pivot_row])]
            transform[row] = [left - factor * right for left, right in
                              zip(transform[row], transform[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    inconsistent = next((row for row in range(rows)
                         if all(not matrix[row][column]
                                for column in range(columns))
                         and matrix[row][-1]), None)
    if inconsistent is not None:
        dual = transform[inconsistent]
        for column, source in enumerate(sources):
            pairing = sum(dual[row] * source.get(monomials[row], Fraction(0))
                          for row in range(rows))
            if pairing:
                raise LiftFailure(("bad dual source pairing", column, pairing))
        target_pairing = sum(dual[row] * target.get(monomials[row], Fraction(0))
                             for row in range(rows))
        if not target_pairing:
            raise LiftFailure("bad dual target pairing")
        return {
            "status": "INCONSISTENT",
            "monomials": monomials,
            "matrix": matrix,
            "pivots": pivots,
            "dual": dual,
            "target_pairing": target_pairing,
        }
    solution = [Fraction(0)] * columns
    for row, column in enumerate(pivots):
        solution[column] = matrix[row][-1]
    check = {}
    for scalar, source in zip(solution, sources):
        check = t.add(check, t.scale(scalar, source))
    if check != target:
        raise LiftFailure(("solution check", check, target))
    return {
        "status": "SOLVABLE",
        "monomials": monomials,
        "matrix": matrix,
        "pivots": pivots,
        "solution": solution,
    }


def frac(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def rational_matrix(matrix):
    return [[frac(entry) for entry in row] for row in matrix]


def weight_record(t, monomial, coefficient):
    e = dict(zip(t.NAMES, monomial))
    form = {
        "eta": e["h"],
        "delta": e["q2"],
        "beta": e["q1"] + e["q0"],
        "alpha": e["r2"] + e["r1"] + e["r0"],
        "constant": e["la"] - 20,
        "T_over_L": e["tau"],
        "H_over_L": e["rho"],
    }
    return {"coefficient": frac(coefficient), "exponents": e,
            "difference_form": form}


def analyze_threshold(t, polynomial):
    records = [weight_record(t, monomial, coefficient)
               for monomial, coefficient in polynomial.items()]
    records.sort(key=lambda item: json.dumps(item["exponents"], sort_keys=True))
    thresholds = []
    for item in records:
        e = item["exponents"]
        is_target = e["la"] == 20 and sum(e.values()) == 20
        is_tau = e["la"] == 20 and e["tau"] == 1 and sum(e.values()) == 21
        if is_target or is_tau:
            item["role"] = "target" if is_target else "positive_split_target"
            continue
        form = item["difference_form"]
        constant = (Fraction(form["constant"]) + 5 * form["beta"]
                    + 5 * form["delta"]
                    + Fraction(15, 2) * form["alpha"])
        item["alpha15_2_beta5u_delta5v_eta"] = {
            "constant": frac(constant), "u": form["beta"],
            "v": form["delta"], "eta": form["eta"],
            "T_over_L": form["T_over_L"],
            "H_over_L": form["H_over_L"],
        }
        if form["eta"] and constant < 0:
            thresholds.append(-constant / form["eta"])
    eta0 = max(thresholds) if thresholds else Fraction(0)
    face = []
    open_strict = True
    for item in records:
        data = item.get("alpha15_2_beta5u_delta5v_eta")
        if data is None:
            continue
        at_face = Fraction(data["constant"]) + eta0 * data["eta"]
        if at_face == 0:
            face.append(item)
            if not (data["u"] or data["v"] or data["T_over_L"]
                    or data["H_over_L"]):
                open_strict = False
    return records, eta0, face, open_strict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("forward", "reverse"), required=True)
    parser.add_argument("--output", default="h_qr_lift.json")
    args = parser.parse_args()
    tag = require_aws()
    v4 = load_module(V4, V4_SHA, "h_qr_v4_frozen")
    t = v4.load(v4.TORIC, v4.TORIC_SHA, "h_qr_toric_frozen")
    base = v4.load(v4.V1, v4.V1_SHA, "h_qr_base_frozen")
    tails = t.load_charged_source().build()["tails"]
    rows = {ell: t.substitute(tails[ell],
                              t.source_power_table(v4.coefficient_images(t), tails))
            for ell in range(1, 9)}
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
        raise LiftFailure("h=0 witness custody")
    c1 = v4.specialize_h_zero(
        t, v4.divide_h(t, t.add(wh, t.scale(-1, w0))))
    target_qr = qr_component(t, c1)
    if len(target_qr) != 8:
        raise LiftFailure(("expected eight worst QR terms", len(target_qr)))
    for monomial in target_qr:
        e = dict(zip(t.NAMES, monomial))
        boundary = (5 * (e["q2"] + e["q1"] + e["q0"])
                    + Fraction(15, 2) * (e["r2"] + e["r1"] + e["r0"])
                    + e["la"] - 20)
        if boundary != Fraction(-15, 2):
            raise LiftFailure(("QR boundary drift", e, boundary))
    row0 = {ell: v4.specialize_h_zero(t, rows[ell]) for ell in range(1, 9)}
    sources = [qr_component(t, row0[ell]) for ell in range(1, 9)]
    solved = exact_rref(t, sources, t.scale(-1, target_qr))
    payload = {
        "tag": tag,
        "order": args.order,
        "v4_sha256": V4_SHA,
        "w0_sha256": W0_SHA,
        "c1_qr_sha256": t.digest(target_qr),
        "c1_qr_terms": t.canonical(target_qr),
        "row_qr_sha256": [t.digest(source) for source in sources],
        "graded_monomials": [dict(zip(t.NAMES, monomial))
                             for monomial in solved["monomials"]],
        "graded_rank": len(solved["pivots"]),
        "graded_pivot_columns_zero_based": solved["pivots"],
        "rref_augmented": rational_matrix(solved["matrix"]),
        "status": solved["status"],
    }
    if solved["status"] == "INCONSISTENT":
        payload["dual_cokernel"] = {
            "coefficients_by_monomial": [frac(x) for x in solved["dual"]],
            "target_pairing": frac(solved["target_pairing"]),
        }
        payload["firewall"] = (
            "graded QR obstruction for scalar h corrections only; "
            "not a no-lift theorem without multiplier-support completeness")
        blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
        Path(args.output).write_text(blob)
        print(f"ORDER={args.order}")
        print("STATUS=INCONSISTENT_WITH_DUAL")
        print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
        print("PASS_H_QR_SYZYGY_LIFT_V5_COKERNEL")
        return
    solution = solved["solution"]
    corrected_fs = {
        ell: t.add(fs[ell], t.monomial(solution[ell-1], h=1))
        for ell in range(1, 9)
    }
    corrected = {}
    for ell in indices:
        corrected = t.add(corrected,
                          t.multiply(corrected_fs[ell], rows[ell]))
    corrected_w0 = v4.specialize_h_zero(t, corrected)
    if corrected_w0 != w0:
        raise LiftFailure("corrected h=0 mismatch")
    corrected_c1 = v4.specialize_h_zero(
        t, v4.divide_h(t, t.add(corrected, t.scale(-1, w0))))
    residual_qr = qr_component(t, corrected_c1)
    if residual_qr:
        raise LiftFailure(("QR piece did not cancel", residual_qr))
    records, eta0, face, open_strict = analyze_threshold(t, corrected)
    payload.update({
        "solution": [frac(x) for x in solution],
        "solution_sha256": sha256(json.dumps(
            [frac(x) for x in solution], separators=(",", ":")).encode()).hexdigest(),
        "corrected_witness_sha256": t.digest(corrected),
        "corrected_witness_terms": len(corrected),
        "corrected_c1_sha256": t.digest(corrected_c1),
        "corrected_c1_terms": len(corrected_c1),
        "residual_qr_terms": 0,
        "eta_uniform_infimum": frac(eta0),
        "eta_equal_infimum_is_strict_on_open_quadrant": open_strict,
        "threshold_face_terms": face,
        "records": records,
        "firewall": (
            "one scalar h-syzygy correction of the worst QR grade only; "
            "iterate remaining low grades; no formal h-adic lift"),
    })
    blob = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path(args.output).write_text(blob)
    print(f"ORDER={args.order}")
    print("STATUS=SOLVABLE")
    print("SOLUTION=" + ",".join(frac(x) for x in solution))
    print(f"C1_QR_SHA256={t.digest(target_qr)}")
    print(f"CORRECTED_WITNESS_SHA256={t.digest(corrected)}")
    print(f"CORRECTED_WITNESS_TERMS={len(corrected)}")
    print(f"ETA_UNIFORM_INFIMUM={frac(eta0)}")
    print(f"ETA_EQUAL_OPEN_STRICT={int(open_strict)}")
    print(f"CERTIFICATE_SHA256={sha256(blob.encode()).hexdigest()}")
    print("PASS_H_QR_SYZYGY_LIFT_V5_SOLVABLE")


if __name__ == "__main__":
    main()
