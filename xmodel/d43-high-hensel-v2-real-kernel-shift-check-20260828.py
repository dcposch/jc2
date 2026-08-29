#!/usr/bin/env python3
"""Independent corrected real-kernel attack on the D43 schema-v2 validator.

This checker is review evidence, not a campaign runner.  It constructs the
alternate p^2 point as ``deterministic_p2 + p * kernel_digit``.  The packet's
opt-in fixture instead calls ``apply_digits`` with step p, which first reduces
the deterministic p^2 coordinates modulo p and therefore loses the registered
inhomogeneous correction.
"""

from __future__ import annotations

from copy import deepcopy
import json
import os
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, "cases")
sys.path.insert(0, CASES)

import d43_source_high_hensel as H


def kernel_for_free_column(context, free_column):
    kernel = [0] * len(context["essential_labels"])
    kernel[free_column] = 1
    for row, pivot in enumerate(context["factor"]["pivot_columns"]):
        kernel[pivot] = -context["factor"]["rref"][row][free_column] \
            % H.PRIME
    direct = [
        sum(matrix_row[index] * kernel[index]
            for index in range(len(kernel))) % H.PRIME
        for matrix_row in context["essential_jacobian"]
    ]
    if any(direct):
        raise AssertionError("constructed vector is not in the source kernel")
    return kernel


def add_kernel_digit(payload, labels, kernel):
    shifted = deepcopy(payload)
    modulus = H.PRIME ** 2
    for label, digit in zip(labels, kernel):
        key = H.coordinate_key(label)
        shifted["coordinates"][key] = (
            int(payload["coordinates"][key]) + H.PRIME * int(digit)
        ) % modulus
    return shifted


def combine(left, left_scale, right, right_scale):
    return [
        (left_scale * a + right_scale * b) % H.PRIME
        for a, b in zip(left, right)
    ]


def run():
    certificate = os.path.join(CASES, "d43_full_certificate_p105337.json")
    reference = os.path.join(CASES, "d43_char0_lift_p105337.json")
    context = H.prepare_d43_context(certificate, reference)
    initial = H._initial_payload(context)
    p2 = H.lift_one_point_digit(context, initial)
    if p2["status"] != H.STATUS_FINITE:
        raise AssertionError("registered deterministic p2 lift is not finite")

    frame = H._frame_from_payload(p2)
    modulus = H.PRIME ** 2
    candidates = []
    for free_column in context["factor"]["free_columns"]:
        kernel = kernel_for_free_column(context, free_column)
        shifted = add_kernel_digit(p2, context["essential_labels"], kernel)
        rows = H.source_rows_with_x(
            context, shifted["coordinates"], frame, modulus)
        if any(rows):
            raise AssertionError(
                "correct p2-plus-kernel shift broke raw rows at free column %d"
                % free_column)
        gate = H.template_relation_gate(
            shifted["coordinates"], frame, modulus)
        e_digit = (int(gate["E_residue_modulus"]) // H.PRIME) % H.PRIME
        candidates.append((free_column, kernel, e_digit, shifted, gate))
        if gate["pass"]:
            selected = ("single", [free_column], kernel, shifted, gate)
            break
    else:
        selected = None

    if selected is None:
        nonzero = [item for item in candidates if item[2]]
        if len(nonzero) < 2:
            raise AssertionError("could not construct a nonzero E-tangent kernel")
        c1, k1, d1, _s1, _g1 = nonzero[0]
        c2, k2, d2, _s2, _g2 = nonzero[1]
        kernel = combine(k1, d2, k2, -d1)
        if not any(kernel):
            raise AssertionError("E-tangent kernel combination vanished")
        shifted = add_kernel_digit(p2, context["essential_labels"], kernel)
        rows = H.source_rows_with_x(
            context, shifted["coordinates"], frame, modulus)
        if any(rows):
            raise AssertionError("combined E-tangent shift broke raw rows")
        gate = H.template_relation_gate(
            shifted["coordinates"], frame, modulus)
        if not gate["pass"]:
            raise AssertionError("combined source-kernel shift does not preserve E")
        selected = ("combination", [c1, c2], kernel, shifted, gate)

    kind, columns, kernel, shifted, gate = selected
    shifted["template_relation_gate"] = gate
    rejection = None
    try:
        H.validate_resume_payload(shifted, context)
    except ValueError as error:
        rejection = str(error)
    if rejection is None:
        raise AssertionError("schema-v2 validator accepted a stale-history shift")
    if "semantic state-chain replay mismatch" not in rejection:
        raise AssertionError(
            "alternate point was rejected for the wrong reason: %s" % rejection)

    changed = sum(
        shifted["coordinates"][key] != p2["coordinates"][key]
        for key in shifted["coordinates"])
    report = {
        "status": "PASS_CORRECT_REAL_KERNEL_SHIFT_REJECTED_BY_SEMANTIC_CHAIN",
        "construction": kind,
        "free_columns": columns,
        "nonzero_kernel_digits": sum(bool(value) for value in kernel),
        "changed_p2_coordinates": changed,
        "raw_rows_zero_mod_p2": 184,
        "template_gate_pass": bool(gate["pass"]),
        "E_residue_mod_p2": int(gate["E_residue_modulus"]),
        "validator_rejection": rejection,
    }
    print(json.dumps(report, indent=1, sort_keys=True))
    return report


if __name__ == "__main__":
    run()
