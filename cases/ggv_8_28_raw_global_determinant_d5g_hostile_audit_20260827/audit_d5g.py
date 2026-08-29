#!/usr/bin/env python3
"""Independent hostile audit of the D5G raw-global determinant artifact.

This script does not import the producer compiler.  It reconstructs the
whole truncated bivariate expression in a different sparse representation,
checks all serialized provenance records, and uses closed-form reductions
for the H-division and M-cokernel checks.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "cases/ggv_8_28_raw_global_determinant_d5g_20260827"
SOURCE = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"

CHARGED_HASHES = {
    "source": (
        SOURCE,
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    ),
    "producer_preregistration": (
        PRODUCER / "PREREGISTRATION.md",
        "72e8ba988a0aaeccb86f473bf89b66847481c4e645998f5456e2ad0acb803541",
    ),
    "producer_compiler": (
        PRODUCER / "compile_d5g.py",
        "059d9f32351f5bb5132e0a9cb10e68c35f78ac8504a8323732463f9126897b95",
    ),
    "producer_direct": (
        PRODUCER / "DIRECT_DETERMINANT.json",
        "069ab7a5fdb133aa2ffb0063e5f36c5664a070798de6ea00520698207e24838d",
    ),
    "producer_certificate": (
        PRODUCER / "D22_CERTIFICATE.json",
        "6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a",
    ),
    "producer_result": (
        PRODUCER / "RESULT.json",
        "e20f4a67953eeab86d21bea5fbaf149dffe20b65b0af052354490b3bc04aa8da",
    ),
    "producer_readme": (
        PRODUCER / "README.md",
        "64f63865feeb1bd7e64ad6c8be1bc3abd28d3dc995a5a65ef8971a6954606870",
    ),
    "producer_freeze": (
        PRODUCER / "FREEZE.sha256",
        "838b1160f3ddf38fcbf360bd200ee2057e72da2b1b0ba8788d43b83720cdd043",
    ),
    "producer_report": (
        ROOT / "xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md",
        "59e9bf2c6713b84ef848bae693a7e88f62c679ff56bad34fce4d3a28548663f3",
    ),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


# The independent series representation is
# (t degree, X degree, sorted raw-variable tuple) -> rational coefficient.
def clean(poly):
    return {key: Q(value) for key, value in poly.items() if Q(value)}


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, Q(0)) + value
    return clean(out)


def scale(poly, scalar):
    return clean({key: Q(scalar) * value for key, value in poly.items()})


def dx(poly):
    return clean(
        {(tdeg, xdeg - 1, variables): Q(xdeg) * value
         for (tdeg, xdeg, variables), value in poly.items() if xdeg}
    )


def dt(poly):
    return clean(
        {(tdeg - 1, xdeg, variables): Q(tdeg) * value
         for (tdeg, xdeg, variables), value in poly.items() if tdeg}
    )


def times_t(poly):
    return {
        (tdeg + 1, xdeg, variables): value
        for (tdeg, xdeg, variables), value in poly.items()
        if tdeg < 22
    }


def multiply(left, right):
    out = {}
    for (ta, xa, va), ca in left.items():
        for (tb, xb, vb), cb in right.items():
            if ta + tb > 22:
                continue
            key = (ta + tb, xa + xb, tuple(sorted(va + vb)))
            out[key] = out.get(key, Q(0)) + ca * cb
    return clean(out)


def series_digest(poly):
    encoded = [
        [tdeg, xdeg, list(variables), str(poly[tdeg, xdeg, variables])]
        for tdeg, xdeg, variables in sorted(poly)
    ]
    return hashlib.sha256(compact(encoded)).hexdigest()


def x_digest(poly):
    encoded = [
        [xdeg, list(variables), str(poly[xdeg, variables])]
        for xdeg, variables in sorted(poly)
    ]
    return hashlib.sha256(compact(encoded)).hexdigest()


def validate_support(source):
    census = {}
    for kind, shift, maximum_x, prefix in (
        ("F", 8, 16, "f"),
        ("G", 12, 24, "g"),
    ):
        # Direct enumeration of the lattice polygon mS, followed by the
        # chart-weight cut 0<=shift+3i-j<=22.
        expected = set()
        for xdeg in range(maximum_x + 1):
            lower_y = max(0, 4 * xdeg - shift)
            upper_y = 3 * xdeg + shift
            for ydeg in range(lower_y, upper_y + 1):
                weight = shift + 3 * xdeg - ydeg
                if 0 <= weight <= 22:
                    expected.add((weight, f"{prefix}_{xdeg}_{ydeg}", xdeg, ydeg))
        actual = set()
        by_weight = [0] * 23
        for slot in source["raw_slots_through_weight_22"][kind]:
            xdeg = int(slot["raw_exponents"]["x"])
            ydeg = int(slot["raw_exponents"]["y"])
            weight = int(slot["weight"])
            assert weight == shift + 3 * xdeg - ydeg
            assert slot["slot"] == f"{prefix}_{xdeg}_{ydeg}"
            assert slot["raw_monomial"] == f"x^{xdeg}*y^{ydeg}"
            assert slot["chart_image"] == f"t^{weight}*X^{xdeg}"
            actual.add((weight, slot["slot"], xdeg, ydeg))
            by_weight[weight] += 1
        assert actual == expected
        census[kind] = {
            "all_slots": len(actual),
            "weight_zero_slots": by_weight[0],
            "positive_slots": len(actual) - by_weight[0],
            "counts_weight_0_through_22": by_weight,
        }
    assert census["F"]["positive_slots"] + census["G"]["positive_slots"] == 400
    return census


def make_series(source):
    # Direct binomial expansion of (X^8-1)^2 and (X^8-1)^3.
    F = {
        (0, 0, ()): Q(1),
        (0, 8, ()): Q(-2),
        (0, 16, ()): Q(1),
    }
    G = {
        (0, 0, ()): Q(-1),
        (0, 8, ()): Q(3),
        (0, 16, ()): Q(-3),
        (0, 24, ()): Q(1),
    }
    F_rows = [
        (0, 0, (), Q(1), "F0:X^0:1"),
        (0, 8, (), Q(-2), "F0:X^8:-2"),
        (0, 16, (), Q(1), "F0:X^16:1"),
    ]
    G_rows = [
        (0, 0, (), Q(-1), "G0:X^0:-1"),
        (0, 8, (), Q(3), "G0:X^8:3"),
        (0, 16, (), Q(-3), "G0:X^16:-3"),
        (0, 24, (), Q(1), "G0:X^24:1"),
    ]
    positive_slots = []
    for kind, target, rows in (("F", F, F_rows), ("G", G, G_rows)):
        for slot in source["raw_slots_through_weight_22"][kind]:
            if int(slot["weight"]) == 0:
                continue
            weight = int(slot["weight"])
            xdeg = int(slot["raw_exponents"]["x"])
            variable = slot["slot"]
            key = (weight, xdeg, (variable,))
            assert key not in target
            target[key] = Q(1)
            rows.append((weight, xdeg, (variable,), Q(1), variable))
            positive_slots.append(variable)
    assert len(positive_slots) == 400
    assert len(set(positive_slots)) == 400
    return F, G, F_rows, G_rows, positive_slots


def build_expression(F, G):
    # Construct the four differentiated products, not the producer's
    # coefficient recurrence.
    return add(
        scale(multiply(dx(F), G), 12),
        scale(multiply(F, dx(G)), -8),
        scale(times_t(multiply(dx(F), dt(G))), -1),
        times_t(multiply(dt(F), dx(G))),
    )


def decode_direct(direct):
    out = {}
    for row in direct["D"]:
        weight = int(row["weight"])
        for variables, xdeg, coefficient in row["terms"]:
            key = (weight, int(xdeg), tuple(variables))
            out[key] = Q(coefficient)
    return clean(out)


def expected_contributions(F_rows, G_rows):
    by_weight = [[] for _ in range(23)]
    aggregate = {}
    for i, fx, fvars, fc, fsource in F_rows:
        for j, gx, gvars, gc, gsource in G_rows:
            n = i + j
            if n > 22:
                continue
            variables = tuple(sorted(fvars + gvars))
            xdeg = fx + gx - 1
            if fx and 12 - j:
                coefficient = Q(12 - j) * fx * fc * gc
                by_weight[n].append(
                    [n, i, j, "FX_G", fsource, gsource, xdeg, str(coefficient)]
                )
                key = (n, xdeg, variables)
                aggregate[key] = aggregate.get(key, Q(0)) + coefficient
            if gx and i - 8:
                coefficient = Q(i - 8) * gx * fc * gc
                by_weight[n].append(
                    [n, i, j, "F_GX", fsource, gsource, xdeg, str(coefficient)]
                )
                key = (n, xdeg, variables)
                aggregate[key] = aggregate.get(key, Q(0)) + coefficient
    return [sorted(row) for row in by_weight], clean(aggregate)


# X-polynomials use (X degree, raw-variable tuple) -> rational coefficient.
def decode_x(items):
    return clean(
        {(int(xdeg), tuple(variables)): Q(coefficient)
         for variables, xdeg, coefficient in items}
    )


def x_add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, Q(0)) + value
    return clean(out)


def x_scale(poly, scalar):
    return clean({key: Q(scalar) * value for key, value in poly.items()})


def divide_x8_minus_1_closed(poly):
    quotient = {}
    remainder = {}
    for (degree, variables), coefficient in poly.items():
        residue = degree % 8
        quotient_length = degree // 8
        rkey = (residue, variables)
        remainder[rkey] = remainder.get(rkey, Q(0)) + coefficient
        # X^degree=(X^8-1)*sum_(a=0)^(q-1)X^(residue+8a)+X^residue.
        for a in range(quotient_length):
            qkey = (residue + 8 * a, variables)
            quotient[qkey] = quotient.get(qkey, Q(0)) + coefficient
    return clean(quotient), clean(remainder)


def m_remainder_closed(poly):
    remainder = {}
    for (degree, variables), coefficient in poly.items():
        residue = degree % 8
        quotient_length = degree // 8
        if residue == 7:
            continue
        factor = Q(1)
        for step in range(1, quotient_length + 1):
            factor *= Q(residue + 8 * step - 7, residue + 8 * step + 5)
        key = (residue, variables)
        remainder[key] = remainder.get(key, Q(0)) + coefficient * factor
    return clean(remainder)


def m_apply(poly):
    out = {}
    for (degree, variables), coefficient in poly.items():
        high = (degree + 7, variables)
        out[high] = out.get(high, Q(0)) + Q(4 * (degree + 12)) * coefficient
        if degree:
            low = (degree - 1, variables)
            out[low] = out.get(low, Q(0)) - Q(4 * degree) * coefficient
    return clean(out)


def difference_count(left, right):
    return sum(left.get(key, Q(0)) != right.get(key, Q(0)) for key in set(left) | set(right))


def audit():
    observed_hashes = {}
    for label, (path, expected) in CHARGED_HASHES.items():
        got = digest(path)
        assert got == expected, (label, got, expected)
        observed_hashes[label] = got

    source = json.loads(SOURCE.read_bytes())
    direct = json.loads((PRODUCER / "DIRECT_DETERMINANT.json").read_bytes())
    certificate = json.loads((PRODUCER / "D22_CERTIFICATE.json").read_bytes())
    producer_result = json.loads((PRODUCER / "RESULT.json").read_bytes())

    support_census = validate_support(source)
    F, G, F_rows, G_rows, positive_slots = make_series(source)
    expression = build_expression(F, G)
    producer_expression = decode_direct(direct)
    assert expression == producer_expression

    contributions, contribution_sum = expected_contributions(F_rows, G_rows)
    assert contribution_sum == expression
    contribution_digests = []
    for weight, row in enumerate(direct["D"]):
        assert int(row["weight"]) == weight
        assert row["contributions"] == contributions[weight]
        contribution_hash = hashlib.sha256(compact(contributions[weight])).hexdigest()
        assert row["contribution_sha256"] == contribution_hash
        assert int(row["contribution_count"]) == len(contributions[weight])
        contribution_digests.append(contribution_hash)
    assert direct["D22_contributions"] == contributions[22]
    assert certificate["D22_contributions"] == contributions[22]
    all_contribution_digest = hashlib.sha256(compact(contribution_digests)).hexdigest()
    assert direct["all_contribution_digests_sha256"] == all_contribution_digest

    term_counts = [
        sum(1 for tdeg, _, _ in expression if tdeg == weight)
        for weight in range(23)
    ]
    contribution_counts = [len(row) for row in contributions]
    assert term_counts[0] == 0
    assert contribution_counts[0] == 17
    assert sum(term_counts) == int(direct["total_final_terms"]) == 32135
    assert sum(contribution_counts) == int(direct["total_contributions"]) == 58572

    D22 = {
        (xdeg, variables): coefficient
        for (tdeg, xdeg, variables), coefficient in expression.items()
        if tdeg == 22
    }
    assert D22 == decode_x(certificate["D22"])

    quotient, h_remainder = divide_x8_minus_1_closed(D22)
    artifact_quotient = decode_x(certificate["H_division"]["Q22"])
    artifact_h_remainder = decode_x(certificate["H_division"]["R22"])
    assert quotient == artifact_quotient
    assert h_remainder == artifact_h_remainder

    m_remainder = m_remainder_closed(D22)
    artifact_y = decode_x(certificate["M_reduction"]["Y22"])
    artifact_m_remainder = decode_x(certificate["M_reduction"]["rM22"])
    assert m_remainder == artifact_m_remainder
    assert x_add(m_apply(artifact_y), artifact_m_remainder) == D22

    # Replay every claimed leading cancellation in the producer trace.
    work = dict(D22)
    accumulated_y = {}
    for index, (variables, degree, coefficient, source_degree, y_coefficient) in enumerate(
        certificate["M_reduction"]["trace"]
    ):
        variables = tuple(variables)
        degree = int(degree)
        coefficient = Q(coefficient)
        source_degree = int(source_degree)
        y_coefficient = Q(y_coefficient)
        assert degree == max(xdeg for xdeg, _ in work), index
        assert work.get((degree, variables), Q(0)) == coefficient, index
        assert source_degree == degree - 7
        assert y_coefficient == coefficient / Q(4 * (degree + 5))
        key = (source_degree, variables)
        accumulated_y[key] = accumulated_y.get(key, Q(0)) + y_coefficient
        work = x_add(work, x_scale(m_apply({key: y_coefficient}), -1))
    assert clean(accumulated_y) == artifact_y
    assert clean(work) == artifact_m_remainder

    expected_vector = []
    for degree in range(7):
        entries = [
            [list(variables), str(coefficient)]
            for (xdeg, variables), coefficient in sorted(
                artifact_m_remainder.items(), key=lambda item: item[0][1]
            )
            if xdeg == degree
        ]
        expected_vector.append(entries)
    assert expected_vector == certificate["M_reduction"]["seven_vector"]

    # Strengthen the H mutation check: not merely "changed", but the exact
    # unique differences forced by H=M(X/52)-12/13.
    mutation = certificate["H_mutation"]
    mutated_D22 = decode_x(mutation["mutated_D22"])
    mutated_q = decode_x(mutation["Q22_mutated"])
    mutated_h_remainder = decode_x(mutation["R22_mutated"])
    mutated_y = decode_x(mutation["M_preimage_mutated"])
    mutated_m_remainder = decode_x(mutation["M_remainder_mutated"])
    H = {(8, ()): Q(1), (0, ()): Q(-1)}
    assert x_add(D22, H) == mutated_D22
    assert x_add(quotient, {(0, ()): Q(1)}) == mutated_q
    assert h_remainder == mutated_h_remainder
    assert x_add(artifact_y, {(1, ()): Q(1, 52)}) == mutated_y
    assert x_add(artifact_m_remainder, {(0, ()): Q(-12, 13)}) == mutated_m_remainder

    expected_mutated_vector = []
    for degree in range(7):
        entries = [
            [list(variables), str(coefficient)]
            for (xdeg, variables), coefficient in sorted(
                mutated_m_remainder.items(), key=lambda item: item[0][1]
            )
            if xdeg == degree
        ]
        expected_mutated_vector.append(entries)
    assert expected_mutated_vector == mutation["seven_vector_mutated"]

    # Independent structural forms of the two source/compiler mutations.
    F_dropped = {
        key: value for key, value in F.items() if key[2] != ("f_0_1",)
    }
    dropped_expression = build_expression(F_dropped, G)
    offset_expression = add(expression, multiply(F, dx(G)))
    assert dropped_expression != expression
    assert offset_expression != expression

    # Validate every dependency hash serialized in the producer result.
    dependency_hashes = {}
    for label, pin in producer_result["pins"].items():
        got = digest(ROOT / pin["path"])
        assert got == pin["sha256"]
        dependency_hashes[label] = got
    assert producer_result["local_naturality_dependency"]["consumed"] is False
    assert producer_result["target_status"].startswith("NO_TARGET_VERDICT")

    return {
        "status": "PASS-D5G-INDEPENDENT-HOSTILE-AUDIT",
        "scope": (
            "literal generic raw D0..D22 plus exact H and M decompositions; "
            "no local naturality, equations, target, face, or JC2 verdict"
        ),
        "charged_hashes": observed_hashes,
        "dependency_hashes": dependency_hashes,
        "independent_derivation": {
            "chart": "x=t^3*X, y=t^-1, F=t^8*f, G=t^12*g",
            "jacobian": "J(f,g)=t^-22*(12*F_X*G-8*F*G_X-t*(F_X*G_t-F_t*G_X))",
            "coefficient": "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')",
        },
        "raw_structural_replay": {
            "support_census": support_census,
            "positive_slots": len(positive_slots),
            "term_counts_D0_through_D22": term_counts,
            "total_final_terms": sum(term_counts),
            "contribution_counts_D0_through_D22": contribution_counts,
            "total_contributions": sum(contribution_counts),
            "all_contribution_digests_sha256": all_contribution_digest,
            "independent_series_sha256": series_digest(expression),
            "D0": "ZERO_FROM_17_NONZERO_PRECOMBINATION_CONTRIBUTIONS",
        },
        "D22": {
            "term_count": len(D22),
            "independent_sha256": x_digest(D22),
            "H_division": {
                "Q22_terms": len(quotient),
                "R22_terms": len(h_remainder),
                "Q22_sha256": x_digest(quotient),
                "R22_sha256": x_digest(h_remainder),
                "max_Q22_degree": max(xdeg for xdeg, _ in quotient),
                "max_R22_degree": max(xdeg for xdeg, _ in h_remainder),
                "status": "EXACT_MATCH",
            },
            "M_reduction": {
                "Y22_terms": len(artifact_y),
                "rM22_terms": len(artifact_m_remainder),
                "Y22_sha256": x_digest(artifact_y),
                "rM22_sha256": x_digest(artifact_m_remainder),
                "max_Y22_degree": max(xdeg for xdeg, _ in artifact_y),
                "max_rM22_degree": max(xdeg for xdeg, _ in artifact_m_remainder),
                "trace_steps": len(certificate["M_reduction"]["trace"]),
                "status": "EXACT_MATCH_AND_TRACE_REPLAY",
            },
        },
        "mutations": {
            "add_H": (
                "EXACT: delta Q=1, delta R=0, delta Y=X/52, "
                "delta rM=-12/13"
            ),
            "drop_f_0_1": {
                "changed_coefficients": difference_count(expression, dropped_expression),
                "independent_series_sha256": series_digest(dropped_expression),
            },
            "replace_i_minus_8_by_i_minus_7": {
                "changed_coefficients": difference_count(expression, offset_expression),
                "independent_series_sha256": series_digest(offset_expression),
            },
        },
        "dependency_scope": {
            "d4r1_result_consumed": False,
            "d4r1_freeze_hash_read_only": True,
            "local_naturality": "LOCKED_OUT_OF_D5G",
            "target_verdict": "NONE",
        },
    }


def main():
    result = pretty(audit())
    if len(sys.argv) == 2 and sys.argv[1] == "--print":
        sys.stdout.buffer.write(result)
        return
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        expected = Path(sys.argv[2]).read_bytes()
        assert expected == result
        print("PASS D5G independent hostile audit")
        return
    raise SystemExit("usage: audit_d5g.py --print | audit_d5g.py --check RESULT.json")


if __name__ == "__main__":
    main()
