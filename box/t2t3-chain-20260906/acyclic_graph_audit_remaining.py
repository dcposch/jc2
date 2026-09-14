#!/usr/bin/env python3
"""Exact-Q acyclic presentations for the remaining T2/T3 branches.

This is the delta52/D108 companion to ``acyclic_graph_audit.py``.  The older
file is intentionally left byte-for-byte fixed so its delta2 receipt keeps a
valid driver hash.  No Groebner basis is computed here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import resource
import time
from collections import Counter, defaultdict
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TERM = re.compile(r"^\((.*)\)\*tt\^(\d+)\*zz\^(\d+)$")
SPECS = {
    "99-delta52": {
        "input": ROOT / "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
        "k": 33, "D2": 55, "n2": 3, "D3": 145,
        "t2z": 40, "t2p": 15, "t3z": 105, "t3p": 40,
        "lam2": "leader55", "zlam2": "Z55", "sep": "c", "zsep": "Zc",
        "output": HERE / "acyclic-graph-delta52.json",
        "source_support": {
            "delta": "5/2", "base": "pi*(pi^2-c)",
            "strict_below_zero": True,
            "attained_rows": [
                {"depth": 21, "target": "P"}, {"depth": 63, "target": "P^3"},
                {"depth": 189, "target": "P^9", "object": "F"},
                {"depth": 126, "target": "P^6", "object": "G"},
            ],
        },
    },
    "108-free-mean": {
        "input": ROOT / "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
        "k": 36, "D2": 63, "n2": 4, "D3": 227,
        "t2z": 49, "t2p": 14, "t3z": 176, "t3p": 51,
        "lam2": "leader63", "zlam2": "Z63", "sep": "c", "zsep": "Zc",
        "output": HERE / "acyclic-graph-d108-free-mean.json",
        "source_support": {
            "delta": "3", "base": "(pi-minor_mean)^2-c", "free_mean": True,
            "strict_below_zero": True,
            "attained_rows": [
                {"depth": 8, "target": "-P"}, {"depth": 32, "target": "P^4"},
                {"depth": 96, "target": "P^12", "object": "F"},
                {"depth": 64, "target": "P^8", "object": "G"},
            ],
        },
    },
}


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def hash_lines(lines):
    return hash_text("".join(str(x) + "\n" for x in lines))


def split_top(text):
    pieces = []
    start = depth = 0
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "+" and depth == 0:
            pieces.append(text[start:i])
            start = i + 1
    pieces.append(text[start:])
    return [x for x in pieces if x]


def run(tag, verify_polynomials=True):
    started = time.monotonic()
    spec = SPECS[tag]
    data = json.loads(spec["input"].read_text())
    if tag.startswith("99"):
        assert data["branch"] == "delta52" and data["stage"] == 8
        assert data["field"] == "Q" and data["residual_rows"] == []
        frozen_names = list(data["full_free_coordinates"])
        residual_text = [value for _, value in data["residual_rows"]]
        source_map_counts = {key: len(value) for key, value in data["maps"].items()}
    else:
        frozen_names = list(data["names"])
        residual_text = list(data["residual_strings"])
        source_map_counts = {"h": None, "D": None, "C": None}
        assert data["k"] == spec["k"] and data["target"] == spec["D2"]
        assert "minor_mean" in frozen_names
    source = sorted(set(frozen_names) | {spec["zsep"]})
    ctx = fmpq_mpoly_ctx.get(tuple(source), "lex")
    zero = ctx.constant(0)

    def addpoly(*tables):
        out = {}
        for table in tables:
            for pos, value in table.items():
                out[pos] = out.get(pos, zero) + value
        return {p: v for p, v in out.items() if not v.is_zero()}

    def mulpoly(left, right, cap=None):
        out = {}
        for (r, z), u in left.items():
            for (s, w), v in right.items():
                if cap is None or r + s <= cap:
                    pos = (r + s, z + w)
                    out[pos] = out.get(pos, zero) + u * v
        return {p: v for p, v in out.items() if not v.is_zero()}

    def map_table(table):
        return {(r, z): fmpq_mpoly(e.replace("**", "^"), ctx=ctx) for r, z, e in table}

    def string_table(text):
        out = {}
        for piece in split_top(text):
            match = TERM.match(piece)
            if not match:
                raise ValueError("unparsed normalized term: " + piece[:180])
            expression, r, z = match.groups()
            pos = (int(r), int(z))
            value = fmpq_mpoly(expression.replace("**", "^"), ctx=ctx)
            out[pos] = out.get(pos, zero) + value
        return {p: v for p, v in out.items() if not v.is_zero()}

    if tag.startswith("99"):
        maps = data["maps"]
        h3, c2, c3, D0, C0 = [map_table(maps[key]) for key in ["h3", "C2", "C3", "B2", "A3"]]
        h0 = addpoly(mulpoly(mulpoly(h3, h3), h3), mulpoly(c2, h3), c3)
    else:
        h0, D0, C0 = [string_table(data[key]) for key in ["h_expr", "D_expr", "C_expr"]]
        source_map_counts = {"h": len(h0), "D": len(D0), "C": len(C0)}

    # Independently check the common two-point top carried by each frozen map.
    h_top_z = 24 if spec["k"] == 33 else 28
    h_top_power = 9 if spec["k"] == 33 else 8
    expected_h_top = {
        h_top_z + i: ctx.constant(math.comb(h_top_power, i))
        for i in range(h_top_power + 1)
    }
    actual_h_top = {z: value for (r, z), value in h0.items() if r == 0}
    assert actual_h_top == expected_h_top

    rows = []
    graph = []

    def atom_stage(table, label, source_poly=False):
        out = {}
        for (r, z), expression in sorted(table.items()):
            name = f"x{label}_{r}_{z}"
            graph.append(name)
            rhs = str(expression) if source_poly else expression
            rows.append((f"def_{label}_{r}_{z}", name + "-(" + rhs + ")", "graph", name))
            out[(r, z)] = name
        return out

    h = atom_stage(h0, "h", True)
    D = atom_stage(D0, "D", True)
    C = atom_stage(C0, "C", True)

    def neg(expression):
        return "-(" + expression + ")"

    def scale(expression, coefficient):
        return f"({coefficient})*({expression})"

    def adds(*tables):
        out = defaultdict(list)
        for table in tables:
            for pos, expression in table.items():
                out[pos].append(expression)
        return {p: "+".join(expressions) for p, expressions in out.items()}

    def shift(table, r=0, z=0, factor=None):
        return {(i + r, j + z): (scale(e, factor) if factor is not None else e) for (i, j), e in table.items()}

    def mul(left, right, cap=None):
        out = defaultdict(list)
        for (r, z), u in left.items():
            for (s, w), v in right.items():
                if cap is None or r + s <= cap:
                    out[(r + s, z + w)].append(f"({u})*({v})")
        return {p: "+".join(expressions) for p, expressions in out.items()}

    def lift(table, label):
        return atom_stage(table, label, False)

    k, D2, n2, D3 = [spec[key] for key in ["k", "D2", "n2", "D3"]]
    defect = n2 * D2 - D3
    lead = 6 * k - 2 - D2
    qcap = lead + defect
    H = lift(adds(h, {(k, 0): "-target_b/6"}), "H")
    v = lift(adds(D, {(2 * k - 1, 0): "target_a/3+target_b^2/18"}), "v")
    V = adds(C, shift(D, k, factor="-target_b/4"),
             {(3 * k - 1, 0): "target_a*target_b/12+target_b^3/54-target_c/2"})
    assert min(r for r, _ in V) >= 1
    U = lift({(r - 1, z): scale(e, "8/3") for (r, z), e in V.items()}, "U")
    R = adds(mul(v, v), {p: neg(e) for p, e in mul(U, H).items()})
    Rlow = {}
    rhigh = 0
    for (r, z), expression in sorted(R.items()):
        if z >= k:
            rows.append((f"T2_Rhigh_{r}_{z}", expression, "T2_upper", None))
            rhigh += 1
        else:
            Rlow[(r, z)] = expression
    Rlow = lift(Rlow, "R")
    HH = lift(mul(H, H, qcap - min(r for r, _ in Rlow)), "HH")
    vU = lift(mul(v, U, qcap - 1), "vU")
    pp = "target_d+target_b*target_c/2-(target_a+target_b^2/4)^2/3"
    Q = adds(
        {p: scale(e, "3/4") for p, e in mul(Rlow, HH, qcap).items()},
        shift(mul(vU, H, qcap - 1), 1, factor="-1/8"),
        shift(mul(v, Rlow, qcap - 1), 1),
        shift(mul(U, U, qcap - 2), 2, factor="-9/64"),
        shift(HH, 4 * k - 2, factor=pp),
        shift(v, 4 * k - 1, factor=pp),
    )
    Q = {p: e for p, e in Q.items() if p[0] <= qcap}

    # Frozen source residual equations are part of the presentation.  The 99
    # charts have zero; the repaired D108 free-mean chart has fourteen.
    for i, expression in enumerate(residual_text):
        rows.append((f"source_residual_{i}", expression, "source_residual", None))

    need = set(Q)
    need.update((lead, z) for z in range(D2 + 1))
    Qjet = {}
    for (r, z) in sorted(need):
        if r < lead:
            rows.append((f"T2_strict_{r}_{z}", Q.get((r, z), "0"), "T2_strict", None))
            continue
        qname = f"xQ_{r - lead}_{z}"
        graph.append(qname)
        rows.append((f"def_Q_{r - lead}_{z}", qname + "-(" + Q.get((r, z), "0") + ")", "graph", qname))
        Qjet[(r - lead, z)] = qname
        delta = r - lead
        if delta == 0:
            target = f"{math.comb(spec['t2p'], z - spec['t2z'])}*{spec['lam2']}" if spec["t2z"] <= z <= D2 else "0"
            rows.append((f"T2_face_{z}", qname + "-(" + target + ")", "T2_face", None))
        elif z > D2 - delta:
            rows.append((f"T2_support_{delta}_{z}", qname, "T2_support", None))

    ht = {p: e for p, e in h.items() if p[0] <= defect}
    F = lift(mul(mul(ht, ht, defect), ht, defect), "F")
    G = lift(mul(ht, ht, defect), "G")
    Qsq = lift(mul(Qjet, Qjet, defect), "Qsq")
    if n2 == 3:
        FG = lift(mul(F, G, defect), "FG")
        FQ = lift(mul(F, Qjet, defect - 11), "FQ")
        T3 = adds(mul(Qsq, Qjet, defect),
                  {p: scale(e, "t3eq") for p, e in FG.items()},
                  shift(FQ, 11, factor="t3_fq"))
        recurrence_names = ["t3eq", "t3_fq"]
        recurrence = "Q^3+t3eq*F*G+t^11*t3_fq*F*Q"
        equality = f"t3eq+{spec['lam2']}^3"
    else:
        Qfour = lift(mul(Qsq, Qsq, defect), "Qfour")
        Gsq = lift(mul(G, G, defect), "Gsq")
        FG2 = lift(mul(F, Gsq, defect), "FG2")
        FG = lift(mul(F, G, defect - 9), "FG")
        FGQ = lift(mul(FG, Qjet, defect - 9), "FGQ")
        FQ2 = lift(mul(F, Qsq, defect - 18), "FQ2")
        T3 = adds(Qfour,
                  {p: scale(e, "t3eq") for p, e in FG2.items()},
                  shift(FGQ, 9, factor="t3_fgq"),
                  shift(FQ2, 18, factor="t3_fq2"))
        recurrence_names = ["t3eq", "t3_fgq", "t3_fq2"]
        recurrence = "Q^4+t3eq*F*G^2+t^9*t3_fgq*F*G*Q+t^18*t3_fq2*F*Q^2"
        equality = f"t3eq+{spec['lam2']}^4"
    rows.append(("T3_equality_coefficient", equality, "T3_recurrence", None))
    for (r, z), expression in sorted(T3.items()):
        if r < defect:
            rows.append((f"T3_strict_{r}_{z}", expression, "T3_strict", None))
    face_z = set(range(D3 + 1)) | {z for (r, z) in T3 if r == defect}
    for z in sorted(face_z):
        target = f"{math.comb(spec['t3p'], z - spec['t3z'])}*lambda3" if spec["t3z"] <= z <= D3 else "0"
        rows.append((f"T3_face_{z}", T3.get((defect, z), "0") + "-(" + target + ")", "T3_face", None))
    rows += [
        ("inverse_T2", f"{spec['zlam2']}*{spec['lam2']}-1", "inverse", None),
        ("inverse_T3", "Z3*lambda3-1", "inverse", None),
        ("inverse_separation", f"{spec['zsep']}*{spec['sep']}-1", "inverse", None),
    ]

    all_names = source + recurrence_names + ["lambda3", "Z3"] + graph
    assert len(all_names) == len(set(all_names))
    if not verify_polynomials:
        # Fast path for the bounded Singular streamer: the complete expression
        # and generator hashes are checked there against the prior fully
        # audited JSON.  Avoid rebuilding thousands of transient FLINT local
        # contexts merely to repeat that receipt.
        return {
            "rows": rows,
            "graph": graph,
            "all_names": all_names,
            "record": json.loads(spec["output"].read_text()),
            "spec": spec,
        }
    created = set(source + recurrence_names + ["lambda3", "Z3"])
    parsed_terms = 0
    maximum = (0, None)
    graph_ledger = []
    roundtrip = []
    for name, expression, kind, pivot in rows:
        local_names = sorted(set(re.findall(r"\b[A-Za-z_]\w*\b", expression)))
        if not local_names:
            assert expression in {"0", "0-(0)"}
            continue
        local_ctx = fmpq_mpoly_ctx.get(tuple(local_names), "lex")
        local_index = {v: i for i, v in enumerate(local_names)}
        polynomial = fmpq_mpoly(expression.replace("**", "^"), ctx=local_ctx)
        parsed_terms += len(polynomial)
        maximum = max(maximum, (len(polynomial), name))
        if pivot:
            pi = local_index[pivot]
            occurrences = [(mon, coefficient) for mon, coefficient in polynomial.terms() if mon[pi]]
            assert len(occurrences) == 1
            assert occurrences[0][0][pi] == 1 and sum(occurrences[0][0]) == 1
            assert occurrences[0][1] == 1
            dependencies = {
                local_names[i] for mon, _ in polynomial.terms()
                for i, exponent in enumerate(mon) if exponent and i != pi
            }
            assert dependencies <= created, (name, sorted(dependencies - created)[:10])
            created.add(pivot)
            graph_ledger.append(f"{name}\t{pivot}\t1\t{hash_text(expression)}")
            # Check the inverse image immediately, so no large parsed-row
            # collection survives into a second pass (material for D108 RSS).
            generators = list(local_ctx.gens())
            image = -(polynomial - generators[pi])
            substitution = generators.copy()
            substitution[pi] = image
            assert polynomial.compose(*substitution, ctx=local_ctx).is_zero()
            roundtrip.append(f"{name}\t{pivot}\t{hash_text(str(image))}")

    blocks = Counter(kind for _, _, kind, _ in rows)
    t2_vector = [math.comb(spec["t2p"], z - spec["t2z"]) if spec["t2z"] <= z <= D2 else 0 for z in range(D2 + 1)]
    t3_vector = [math.comb(spec["t3p"], z - spec["t3z"]) if spec["t3z"] <= z <= D3 else 0 for z in range(D3 + 1)]
    source_support = dict(spec["source_support"])
    source_support.update({
        "separation": spec["sep"], "inverse": f"{spec['zsep']}*{spec['sep']}-1",
        "frozen_map_support_counts": source_map_counts,
        "frozen_residual_count": len(residual_text),
        "frozen_residual_sha256": hash_lines(residual_text),
        "common_h_top": f"z^{h_top_z}*(1+z)^{h_top_power}",
        "common_h_top_exactly_checked": True,
    })
    if n2 == 3:
        passive_support = [
            {"shift": 33, "monomial": "G^2"}, {"shift": 44, "monomial": "G*Q"},
            {"shift": 55, "monomial": "Q^2"}, {"shift": 66, "monomial": "F"},
            {"shift": 99, "monomial": "G"}, {"shift": 110, "monomial": "Q"},
            {"shift": 165, "monomial": "1"},
        ]
    else:
        passive_support = [
            {"shift": 36, "monomial": "F^2"}, {"shift": 45, "monomial": "G^2*Q"},
            {"shift": 54, "monomial": "G*Q^2"}, {"shift": 63, "monomial": "Q^3"},
            {"shift": 72, "monomial": "F*G"}, {"shift": 81, "monomial": "F*Q"},
            {"shift": 108, "monomial": "G^2"}, {"shift": 117, "monomial": "G*Q"},
            {"shift": 126, "monomial": "Q^2"}, {"shift": 144, "monomial": "F"},
            {"shift": 180, "monomial": "G"}, {"shift": 189, "monomial": "Q"},
            {"shift": 252, "monomial": "1"},
        ]
        source_support["stage8_prefix_warning"] = "finite schedule reaches local powers only through 12; F/G power-96/64 target data are required source-support data, not claimed as rows newly imposed by this checker"
    input_permutation = [f"{i}\t{name}\t{source.index(name)}\t{name}" for i, name in enumerate(frozen_names)]
    record = {
        "status": "EXACT_ACYCLIC_PRESENTATION_AUDITED_NO_GB_DECISION",
        "case": tag, "field": "Q",
        "input": str(spec["input"].relative_to(ROOT)),
        "input_sha256": hashlib.sha256(spec["input"].read_bytes()).hexdigest(),
        "source_free_generators": len(frozen_names),
        "source_plus_added_inverse_generators": len(source),
        "source_input_to_presentation_map": "name-identity with the recorded order permutation",
        "source_input_to_presentation_map_count": len(input_permutation),
        "source_input_to_presentation_map_sha256": hash_lines(input_permutation),
        "source_input_images_exactly_parsed_in_coefficient_ring": True,
        "source_residual_rows": len(residual_text),
        "source_support": source_support,
        "presentation_generator_count": len(all_names),
        "presentation_generator_order_sha256": hash_lines(all_names),
        "graph_generator_count": len(graph), "graph_row_count": blocks["graph"],
        "graph_rows_all_monic_rational_leader_plus_one": True,
        "graph_dependencies_all_preceding": True,
        "graph_ledger_sha256": hash_lines(graph_ledger),
        "all_graph_roundtrip_count": len(roundtrip),
        "all_graph_roundtrips_exact_zero": True,
        "roundtrip_images_sha256": hash_lines(roundtrip),
        "semantic_quotient_generator_count_before_constraint_pivots": len(all_names) - len(graph),
        "constraint_row_count": len(rows) - blocks["graph"], "total_row_count": len(rows),
        "row_block_counts": dict(sorted(blocks.items())),
        "row_labels_sha256": hash_lines(name for name, _, _, _ in rows),
        "row_expressions_sha256": hash_lines(expression for _, expression, _, _ in rows),
        "parsed_exact_term_count": parsed_terms,
        "maximum_row_terms": maximum[0], "maximum_row_label": maximum[1],
        "supports": {"h": len(h), "D": len(D), "C": len(C), "R_high": rhigh,
                     "Q_expression": len(Q), "Q_defect_jet": len(Qjet),
                     "F": len(F), "G": len(G), "T3_expression": len(T3)},
        "T2_depths": {"H_adic": lead, "physical": 3 * (2 * k) - D2, "defect": defect},
        "T2_face": f"{spec['lam2']}*z^{spec['t2z']}*(1+z)^{spec['t2p']}",
        "T2_face_slots": len(t2_vector), "T2_face_vector_sha256": hash_lines(t2_vector),
        "T3_recurrence_active": recurrence, "T3_equality_unit_row": equality,
        "T3_passive_standard_coefficients_omitted_as_free_extension": passive_support,
        "T3_passive_free_extension_dimension": len(passive_support),
        "T3_face": f"lambda3*z^{spec['t3z']}*(1+z)^{spec['t3p']}",
        "T3_face_slots": len(t3_vector), "T3_face_vector_sha256": hash_lines(t3_vector),
        "localizers": [f"{spec['zlam2']}*{spec['lam2']}-1", "Z3*lambda3-1", f"{spec['zsep']}*{spec['sep']}-1"],
        "no_raw_Jacobian_rows": True, "no_saturation": True,
        "build_wall_seconds": round(time.monotonic() - started, 3),
        "peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "decision": "COMPUTE_BOUND_OPEN",
        "decision_reason": "exact graph quotient remains above 100 generators; no exact-Q Groebner basis was launched",
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    spec["output"].write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: record[key] for key in ["case", "presentation_generator_count", "graph_generator_count", "semantic_quotient_generator_count_before_constraint_pivots", "total_row_count", "row_block_counts", "parsed_exact_term_count", "build_wall_seconds", "peak_RSS_KiB", "decision"]}, indent=2, sort_keys=True))
    # The bounded Singular streamer consumes this in-memory presentation.  It
    # deliberately receives the full incidence graph, not a projected core.
    return {
        "rows": rows,
        "graph": graph,
        "all_names": all_names,
        "record": record,
        "spec": spec,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=sorted(SPECS), required=True)
    run(parser.parse_args().case)
