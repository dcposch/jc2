#!/usr/bin/env python3
"""Exact complete D0..D35 raw determinant compiler and R7R1 cutoff gate."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

PINS = {
    "preregistration": (
        "cases/ggv_8_28_raw_global_determinant_d5g35_20260827/PREREGISTRATION.md",
        "3eb156e7400abbf0fe0e21f705d5246d681b911fc1eff8ebec4db1b38e303b95",
    ),
    "structural_D35_addendum": (
        "cases/ggv_8_28_raw_global_determinant_d5g35_20260827/STRUCTURAL_D35_ADDENDUM.md",
        "1131ebafe5fdd60dc062e2796c283352bbd1c13ac505c71b7db5174d32804258",
    ),
    "d3_raw": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json",
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    ),
    "d5g_freeze": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/FREEZE.sha256",
        "838b1160f3ddf38fcbf360bd200ee2057e72da2b1b0ba8788d43b83720cdd043",
    ),
    "d5g_direct": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/DIRECT_DETERMINANT.json",
        "069ab7a5fdb133aa2ffb0063e5f36c5664a070798de6ea00520698207e24838d",
    ),
    "d5g_certificate": (
        "cases/ggv_8_28_raw_global_determinant_d5g_20260827/D22_CERTIFICATE.json",
        "6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a",
    ),
    "d5g_independent_hostile_audit": (
        "xmodel/ggv-8_28-raw-global-determinant-d5g-hostile-audit-sol-ultra-20260827.md",
        "14913814fce76629836da359f630727b92167d3a23912c9fa265ac8d71f800d2",
    ),
    "r7_audit": (
        "xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-hostile-audit-sol2-20260827.md",
        "2dd9d8f11e0fadff303c8afade0c1f4e52f1a1df4b5afffcea17d5e3d7890a18",
    ),
    "r7r1_freeze": (
        "cases/ggv_quarter_root_characteristic_r7r1_20260827/FREEZE.md",
        "489647cf5726c46401f4c48c394de64d01ff73fff3a5d3168231428add1c0ea5",
    ),
    "r7r1_report": (
        "xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md",
        "9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1",
    ),
    "r7r1_verifier": (
        "cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py",
        "1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa",
    ),
    "r7r1_pending_different_model_review_prompt": (
        "xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-prompt-20260827.md",
        "dd2ae15c4d33837aa65972070980bb0500ceeb41f6daa5c5d5775a623bfe8419",
    ),
}

MAX_WEIGHT = 35


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qstr(value) -> str:
    return str(Q(value))


def compact(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2) + "\n").encode()


# Sparse C[X].  Keys are (sorted raw-variable tuple, X degree).
def pclean(poly):
    return {key: Q(value) for key, value in poly.items() if Q(value)}


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Q(0)) + value
        if not out[key]:
            del out[key]
    return out


def pscale(a, scalar):
    return pclean({key: Q(scalar) * value for key, value in a.items()})


def pmul(a, b):
    out = {}
    for (va, xa), ca in a.items():
        for (vb, xb), cb in b.items():
            key = (tuple(sorted(va + vb)), xa + xb)
            out[key] = out.get(key, Q(0)) + ca * cb
    return pclean(out)


def encode_poly(poly):
    return [[list(raw_vars), x_degree, qstr(poly[raw_vars, x_degree])] for raw_vars, x_degree in sorted(poly)]


def decode_poly(items):
    out = {}
    for raw_vars, x_degree, coefficient in items:
        key = (tuple(raw_vars), int(x_degree))
        out[key] = out.get(key, Q(0)) + Q(coefficient)
    return pclean(out)


H = {((), 0): Q(-1), ((), 8): Q(1)}
F0 = pmul(H, H)
G0 = pmul(F0, H)


def enumerate_polygon(kind):
    if kind == "F":
        i_max, offset, lower_shift = 16, 8, 8
    else:
        i_max, offset, lower_shift = 24, 12, 12
    rows = []
    for i in range(i_max + 1):
        lower = max(0, 4 * i - lower_shift)
        upper = 3 * i + offset
        for j in range(lower, upper + 1):
            weight = offset + 3 * i - j
            rows.append((f"{kind.lower()}_{i}_{j}", i, j, weight))
    return sorted(rows)


def verify_complete_source(source):
    observed = {}
    for kind in ("F", "G"):
        rows = sorted(
            (
                slot["slot"],
                int(slot["raw_exponents"]["x"]),
                int(slot["raw_exponents"]["y"]),
                int(slot["weight"]),
            )
            for slot in source["raw_slots_through_weight_22"][kind]
        )
        expected = enumerate_polygon(kind)
        assert rows == expected
        weights = [row[3] for row in rows if row[3] > 0]
        observed[kind] = {
            "row_count": len(rows),
            "weight_zero_count": sum(row[3] == 0 for row in rows),
            "positive_weight_count": len(weights),
            "maximum_positive_weight": max(weights),
            "polygon_enumeration_sha256": hashlib.sha256(compact(expected)).hexdigest(),
        }
    assert observed["F"] == {
        **observed["F"],
        "row_count": 141,
        "weight_zero_count": 17,
        "positive_weight_count": 124,
        "maximum_positive_weight": 14,
    }
    assert observed["G"] == {
        **observed["G"],
        "row_count": 301,
        "weight_zero_count": 25,
        "positive_weight_count": 276,
        "maximum_positive_weight": 21,
    }
    return observed


def rows_from_source(source):
    rows = {"F": {0: F0}, "G": {0: G0}}
    sources = {
        "F": {0: {((), x): f"F0:X^{x}:{qstr(c)}" for (raw, x), c in F0.items()}},
        "G": {0: {((), x): f"G0:X^{x}:{qstr(c)}" for (raw, x), c in G0.items()}},
    }
    for kind in ("F", "G"):
        for slot in source["raw_slots_through_weight_22"][kind]:
            if slot["weight"] == 0:
                continue
            weight = int(slot["weight"])
            x_degree = int(slot["raw_exponents"]["x"])
            key = ((slot["slot"],), x_degree)
            rows[kind].setdefault(weight, {})[key] = Q(1)
            sources[kind].setdefault(weight, {})[key] = slot["slot"]
    return rows, sources


def determinant(source):
    rows, sources = rows_from_source(source)
    all_D = []
    contribution_digests = []
    total_contributions = 0
    for n in range(MAX_WEIGHT + 1):
        out = {}
        contributions = []
        for i in range(n + 1):
            j = n - i
            Fi = rows["F"].get(i, {})
            Gj = rows["G"].get(j, {})
            for (fv, fx), fc in Fi.items():
                for (gv, gx), gc in Gj.items():
                    raw_vars = tuple(sorted(fv + gv))
                    fsource = sources["F"][i][fv, fx]
                    gsource = sources["G"][j][gv, gx]
                    if fx and 12 - j:
                        coefficient = Q(12 - j) * Q(fx) * fc * gc
                        key = (raw_vars, fx + gx - 1)
                        out[key] = out.get(key, Q(0)) + coefficient
                        contributions.append([n, i, j, "FX_G", fsource, gsource, key[1], qstr(coefficient)])
                    if gx and i - 8:
                        coefficient = Q(i - 8) * Q(gx) * fc * gc
                        key = (raw_vars, fx + gx - 1)
                        out[key] = out.get(key, Q(0)) + coefficient
                        contributions.append([n, i, j, "F_GX", fsource, gsource, key[1], qstr(coefficient)])
        out = pclean(out)
        contributions = sorted(contributions)
        digest = hashlib.sha256(compact(contributions)).hexdigest()
        all_D.append({
            "weight": n,
            "term_count": len(out),
            "terms": encode_poly(out),
            "contribution_count": len(contributions),
            "contribution_sha256": digest,
            "contributions": contributions,
        })
        contribution_digests.append(digest)
        total_contributions += len(contributions)
    return {
        "schema": "GGV-8_28-D5G35-COMPLETE-DIRECT-DETERMINANT-v1",
        "ring": "C[X], C=Q[400 positive-weight D3 raw slots]",
        "recurrence": "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')",
        "source_weight_bounds": {
            "F": 14,
            "G": 21,
            "maximum_pair_sum": 35,
            "highest_potentially_nonzero_determinant_row": 34,
        },
        "leading_rows": {"F0": encode_poly(F0), "G0": encode_poly(G0)},
        "D": all_D,
        "total_final_terms": sum(item["term_count"] for item in all_D),
        "total_contributions": total_contributions,
        "all_contribution_digests_sha256": hashlib.sha256(compact(contribution_digests)).hexdigest(),
        "D22_contributions": all_D[22]["contributions"],
        "D23_contributions": all_D[23]["contributions"],
        "D24_contributions": all_D[24]["contributions"],
    }


# Independent dense Q[X,t]/(t^36) implementation.  It does not call the
# sparse determinant recurrence above.
def utrim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return tuple(poly)


def uadd(a, b):
    return utrim([(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(max(len(a), len(b)))])


def uscale(a, scalar):
    return utrim([Q(scalar) * coefficient for coefficient in a])


def umul(a, b):
    if not a or not b:
        return ()
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            out[i + j] += ca * cb
    return utrim(out)


def uder(a):
    return utrim([Q(i) * a[i] for i in range(1, len(a))])


def tadd(a, b):
    return [uadd(x, y) for x, y in zip(a, b)]


def tscale(a, scalar):
    return [uscale(x, scalar) for x in a]


def tmul(a, b):
    out = [()] * (MAX_WEIGHT + 1)
    for n in range(MAX_WEIGHT + 1):
        value = ()
        for i in range(n + 1):
            value = uadd(value, umul(a[i], b[n - i]))
        out[n] = value
    return out


def tdx(a):
    return [uder(poly) for poly in a]


def tdt(a):
    return [uscale(a[n + 1], n + 1) if n < MAX_WEIGHT else () for n in range(MAX_WEIGHT + 1)]


def tshift(a):
    return [()] + a[:MAX_WEIGHT]


def independent_dense_control(source, direct):
    slots = sorted(
        slot["slot"]
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
        if slot["weight"] > 0
    )
    assignment = {
        slot: Q((index % 17) + 1) * (-1 if index % 3 == 1 else 1)
        for index, slot in enumerate(slots)
    }
    F = [()] * (MAX_WEIGHT + 1)
    G = [()] * (MAX_WEIGHT + 1)
    for target, fixed in ((F, F0), (G, G0)):
        top = max(x_degree for _, x_degree in fixed)
        dense = [Q(0)] * (top + 1)
        for (_, x_degree), coefficient in fixed.items():
            dense[x_degree] += coefficient
        target[0] = utrim(dense)
    for kind, target in (("F", F), ("G", G)):
        for slot in source["raw_slots_through_weight_22"][kind]:
            weight = int(slot["weight"])
            if not weight:
                continue
            x_degree = int(slot["raw_exponents"]["x"])
            dense = list(target[weight]) + [Q(0)] * max(0, x_degree + 1 - len(target[weight]))
            dense[x_degree] += assignment[slot["slot"]]
            target[weight] = utrim(dense)

    FX, GX, Ft, Gt = tdx(F), tdx(G), tdt(F), tdt(G)
    E = tadd(
        tadd(tscale(tmul(FX, G), 12), tscale(tmul(F, GX), -8)),
        tscale(tshift(tadd(tmul(FX, Gt), tscale(tmul(Ft, GX), -1))), -1),
    )
    direct_numeric = []
    for n in range(MAX_WEIGHT + 1):
        sparse = decode_poly(direct["D"][n]["terms"])
        top = max((x_degree for _, x_degree in sparse), default=-1)
        dense = [Q(0)] * (top + 1)
        for (raw_vars, x_degree), coefficient in sparse.items():
            value = coefficient
            for slot in raw_vars:
                value *= assignment[slot]
            dense[x_degree] += value
        direct_numeric.append(utrim(dense))
    assert E == direct_numeric
    encoded = [[qstr(coefficient) for coefficient in poly] for poly in E]
    mutated_23 = [list(poly) for poly in encoded]
    mutated_23[23] = list(mutated_23[23]) or ["0"]
    mutated_23[23][0] = qstr(Q(mutated_23[23][0]) + 1)
    mutated_24 = [list(poly) for poly in encoded]
    mutated_24[24] = list(mutated_24[24]) or ["0"]
    mutated_24[24][0] = qstr(Q(mutated_24[24][0]) + 1)
    assert mutated_23 != encoded
    assert mutated_24 != encoded
    return {
        "status": "PASS-INDEPENDENT-DENSE-QXT-ALL-D0-D35",
        "assignment_sha256": hashlib.sha256(compact({slot: qstr(value) for slot, value in assignment.items()})).hexdigest(),
        "E0_through_E35_sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        "nonzero_weight_count": sum(bool(poly) for poly in E),
        "D23_numeric_sha256": hashlib.sha256(compact(encoded[23])).hexdigest(),
        "D24_numeric_sha256": hashlib.sha256(compact(encoded[24])).hexdigest(),
        "D23_plus_1_full_series_sha256": hashlib.sha256(compact(mutated_23)).hexdigest(),
        "D24_plus_1_full_series_sha256": hashlib.sha256(compact(mutated_24)).hexdigest(),
        "D23_D24_mutation_status": "PASS: EACH DIFFERS EXACTLY IN ITS NAMED CONSTANT COEFFICIENT",
    }


def coefficient_groups(item, target):
    groups = {}
    for raw_vars, x_degree, coefficient in item["terms"]:
        key = int(x_degree)
        groups.setdefault(key, {})[tuple(raw_vars)] = Q(coefficient)
    if target:
        groups.setdefault(0, {})[()] = groups.setdefault(0, {}).get((), Q(0)) - Q(target)
    encoded = {}
    for x_degree, terms in groups.items():
        terms = {raw: coefficient for raw, coefficient in terms.items() if coefficient}
        if terms:
            encoded[x_degree] = [[list(raw), qstr(coefficient)] for raw, coefficient in sorted(terms.items())]
    return encoded


def build_gate(direct):
    generators = []
    rows = []
    for n, item in enumerate(direct["D"]):
        target = 1 if n == 22 else 0
        groups = coefficient_groups(item, target)
        row_generators = []
        for x_degree in sorted(groups):
            expression = groups[x_degree]
            record = {
                "weight": n,
                "X_degree": x_degree,
                "target_coefficient": 1 if n == 22 and x_degree == 0 else 0,
                "terms": expression,
                "term_count": len(expression),
                "sha256": hashlib.sha256(compact(expression)).hexdigest(),
            }
            row_generators.append(len(generators))
            generators.append(record)
        rows.append({
            "weight": n,
            "target": target,
            "source_term_count": item["term_count"],
            "generator_indices": row_generators,
            "generator_count": len(row_generators),
            "source_terms_sha256": hashlib.sha256(compact(item["terms"])).hexdigest(),
        })
    assert rows[0]["generator_count"] == 0
    assert all(rows[n]["generator_count"] > 0 for n in range(1, MAX_WEIGHT))
    assert rows[35]["generator_count"] == 0
    assert direct["D"][35]["terms"] == []
    assert direct["D"][35]["contributions"] == [
        [35, 14, 21, "FX_G", "f_2_0", "g_3_0", 4, "-18"],
        [35, 14, 21, "F_GX", "f_2_0", "g_3_0", 4, "18"],
    ]

    def mutated_row(weight):
        groups = coefficient_groups(direct["D"][weight], 0)
        constant = {tuple(raw): Q(coefficient) for raw, coefficient in groups.get(0, [])}
        constant[()] = constant.get((), Q(0)) + Q(1)
        encoded = [[list(raw), qstr(coefficient)] for raw, coefficient in sorted(constant.items()) if coefficient]
        return {
            "mutation": f"D{weight}->D{weight}+1",
            "mutated_X0_generator": encoded,
            "mutated_X0_sha256": hashlib.sha256(compact(encoded)).hexdigest(),
            "original_X0_sha256": hashlib.sha256(compact(groups.get(0, []))).hexdigest(),
            "gate_verdict": "REJECTED",
        }

    return {
        "schema": "GGV-8_28-D5G35-EXACT-TARGET-GATE-v1",
        "ring": "C=Q[400 positive-weight D3 raw slots]",
        "target": "D0=...=D21=0, D22=1, D23=...=D35=0",
        "rows": rows,
        "generators": generators,
        "generator_count": len(generators),
        "source_term_count": sum(item["term_count"] for item in direct["D"]),
        "status": "UNSOLVED-EXACT-GATE; NO SPECIALIZATION CLAIM",
        "structural_rows": {
            "D35": "IDENTICALLY ZERO: -18+18 on f_2_0*g_3_0*X^4",
            "rows_above_D35": "ZERO BY COMPLETE SOURCE SUPPORT",
            "last_nontrivial_gate_row": "D34=0",
        },
        "mutations": {"D23_plus_1": mutated_row(23), "D24_plus_1": mutated_row(24)},
    }


def build_result(source_bytes, direct_bytes, direct, gate_bytes, gate):
    observed = {}
    for key, (relative, expected) in PINS.items():
        got = sha256(ROOT / relative)
        assert got == expected, (key, got, expected)
        observed[key] = {"path": relative, "sha256": got}
    source = json.loads(source_bytes)
    census = verify_complete_source(source)
    expected_direct = determinant(source)
    assert direct_bytes == compact(expected_direct)
    assert gate_bytes == compact(build_gate(direct))

    old_direct = json.loads((ROOT / PINS["d5g_direct"][0]).read_bytes())
    assert direct["D"][:23] == old_direct["D"]
    assert direct["D22_contributions"] == old_direct["D22_contributions"]
    d22_certificate = json.loads((ROOT / PINS["d5g_certificate"][0]).read_bytes())
    assert direct["D"][22]["terms"] == d22_certificate["D22"]

    dense = independent_dense_control(source, direct)
    assert direct["D"][34]["term_count"] == 4
    assert direct["D"][34]["terms"] == [
        [["f_2_0", "g_3_1"], 4, "2"],
        [["f_2_0", "g_4_4"], 5, "8"],
        [["f_2_1", "g_3_0"], 4, "-3"],
        [["f_3_4", "g_3_0"], 5, "-12"],
    ]
    assert direct["D"][35]["term_count"] == 0
    assert not direct["D"][35]["terms"]
    assert gate["mutations"]["D23_plus_1"]["mutated_X0_sha256"] != gate["mutations"]["D23_plus_1"]["original_X0_sha256"]
    assert gate["mutations"]["D24_plus_1"]["mutated_X0_sha256"] != gate["mutations"]["D24_plus_1"]["original_X0_sha256"]

    row_census = [
        {
            "weight": n,
            "term_count": item["term_count"],
            "contribution_count": item["contribution_count"],
            "terms_sha256": hashlib.sha256(compact(item["terms"])).hexdigest(),
            "contributions_sha256": item["contribution_sha256"],
        }
        for n, item in enumerate(direct["D"])
    ]
    return {
        "status": "PASS-D5G35-COMPLETE-RAW-DETERMINANT-AND-UNSOLVED-TARGET-GATE",
        "scope": "complete direct raw determinant D0..D35 from the frozen D3 source, exact target gate, and provisional corrected-R7R1 q1/q2 cutoff interface",
        "pins": observed,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_completeness": {
            "polygon_census": census,
            "raw_positive_total": census["F"]["positive_weight_count"] + census["G"]["positive_weight_count"],
            "maximum_pair_sum": census["F"]["maximum_positive_weight"] + census["G"]["maximum_positive_weight"],
            "highest_potentially_nonzero_determinant_row": 34,
            "D35": "STRUCTURALLY ZERO AFTER EXACT -18+18 CANCELLATION",
            "rows_beyond_35": "STRUCTURALLY ZERO BY SUPPORT",
            "status": "PASS-INDEPENDENT-COMPLETE-POLYGON-ENUMERATION",
        },
        "custody": {
            "D0_through_D22_byte_equal_to_frozen_independently_hostile_audited_D5G": True,
            "frozen_D5G_direct_sha256": PINS["d5g_direct"][1],
            "D22_certificate_reused_unchanged": PINS["d5g_certificate"][1],
            "direct_D0_D35_sha256": hashlib.sha256(direct_bytes).hexdigest(),
            "target_gate_sha256": hashlib.sha256(gate_bytes).hexdigest(),
        },
        "census": {
            "weights": 36,
            "total_final_terms": direct["total_final_terms"],
            "total_contributions": direct["total_contributions"],
            "target_generators": gate["generator_count"],
            "D23_terms": direct["D"][23]["term_count"],
            "D23_contributions": direct["D"][23]["contribution_count"],
            "D24_terms": direct["D"][24]["term_count"],
            "D24_contributions": direct["D"][24]["contribution_count"],
            "D35_terms": direct["D"][35]["term_count"],
            "D35_contributions": direct["D"][35]["contribution_count"],
            "D35_contribution_identity": "(-18+18)*f_2_0*g_3_0*X^4=0",
            "D34_exact_terms": direct["D"][34]["terms"],
        },
        "row_census": row_census,
        "independent_dense_control": dense,
        "exact_target_gate": {
            "artifact_sha256": hashlib.sha256(gate_bytes).hexdigest(),
            "target": gate["target"],
            "generator_count": gate["generator_count"],
            "status": gate["status"],
        },
        "D23_D24_mutations": {
            "D23_plus_1": {
                **gate["mutations"]["D23_plus_1"],
                "R7R1_effect": "revokes q1 and every higher-row license; q0 remains licensed if rows through D22 hold",
            },
            "D24_plus_1": {
                **gate["mutations"]["D24_plus_1"],
                "R7R1_effect": "revokes q2 and every higher-row license; q0,q1 remain licensed if rows through D23 hold",
            },
            "dense_negative_control": "adding 1 to either dense D23 or D24 disagrees with the independently recomputed determinant coefficient",
        },
        "R7R1_interface": {
            "dependency_status": "PROVISIONAL CORRECTED R7R1; DIFFERENT-MODEL REVIEW PENDING",
            "cutoff_rule": "E=t^22+O(t^N) licenses exactly q_n with n+22<N",
            "licenses": [
                {"required_rows": "D0..D21=0,D22=1", "congruence": "mod t^23", "licensed": ["q0"], "not_licensed": ["q1", "q2"]},
                {"required_rows": "D0..D21=0,D22=1,D23=0", "congruence": "mod t^24", "licensed": ["q0", "q1"], "not_licensed": ["q2"]},
                {"required_rows": "D0..D21=0,D22=1,D23=0,D24=0", "congruence": "mod t^25", "licensed": ["q0", "q1", "q2"], "not_licensed": []},
            ],
            "q1": "F1/(4*p^5) dX exact in L only after the D23 gate",
            "q2": "(F2/(4H)-F1^2/(16H^3)) dX rationally exact only after the D24 gate",
            "full_gate_consequence": "would give the exact polynomial identity E=t^22: D35 is structurally zero after cancellation and all higher rows vanish by support",
            "finite_tower_claim": "NOT MADE: exact E licenses an infinite de Rham tower; bounded raw support does not truncate Q",
        },
        "verdict": {
            "complete_compiler": "PASS",
            "target_gate": "FROZEN BUT UNSOLVED",
            "q1_q2_interface": "TYPED AND CONDITIONAL",
            "specialization": "NO VERDICT",
            "landing_or_face": "NO VERDICT",
        },
        "claims_not_made": ["target-gate solution", "Keller specialization", "finite de Rham tower", "GGV landing", "8_28 face/family exclusion", "G2-PSC", "G2-BD", "counterexample", "JC2"],
    }


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--write-direct":
        source_path, out_path = map(Path, sys.argv[2:])
        source_bytes = source_path.read_bytes()
        assert hashlib.sha256(source_bytes).hexdigest() == PINS["d3_raw"][1]
        source = json.loads(source_bytes)
        verify_complete_source(source)
        out_path.write_bytes(compact(determinant(source)))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 4 and sys.argv[1] == "--write-gate":
        direct_path, out_path = map(Path, sys.argv[2:])
        direct = json.loads(direct_path.read_bytes())
        out_path.write_bytes(compact(build_gate(direct)))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 6 and sys.argv[1] == "--write-result":
        source_path, direct_path, gate_path, out_path = map(Path, sys.argv[2:])
        source_bytes, direct_bytes, gate_bytes = source_path.read_bytes(), direct_path.read_bytes(), gate_path.read_bytes()
        result = build_result(source_bytes, direct_bytes, json.loads(direct_bytes), gate_bytes, json.loads(gate_bytes))
        out_path.write_bytes(pretty(result))
        print(f"WROTE {out_path} {out_path.stat().st_size} bytes")
        return
    if len(sys.argv) == 6 and sys.argv[1] == "--check":
        source_path, direct_path, gate_path, result_path = map(Path, sys.argv[2:])
        source_bytes, direct_bytes, gate_bytes = source_path.read_bytes(), direct_path.read_bytes(), gate_path.read_bytes()
        direct, gate = json.loads(direct_bytes), json.loads(gate_bytes)
        assert direct_bytes == compact(determinant(json.loads(source_bytes)))
        assert gate_bytes == compact(build_gate(direct))
        assert result_path.read_bytes() == pretty(build_result(source_bytes, direct_bytes, direct, gate_bytes, gate))
        print("PASS D5G35 complete determinant, target gate, and R7R1 cutoff replay")
        return
    raise SystemExit("usage: --write-direct SOURCE OUT | --write-gate DIRECT OUT | --write-result SOURCE DIRECT GATE OUT | --check SOURCE DIRECT GATE RESULT")


if __name__ == "__main__":
    main()
