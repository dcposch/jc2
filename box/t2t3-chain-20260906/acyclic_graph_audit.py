#!/usr/bin/env python3
"""Exact-Q circuit audit of the delta=2 attained T2/T3 defect chart.

This deliberately preserves every arithmetic circuit coefficient as a new
generator with a monic `new-(old expression)` row.  It proves an exact
acyclic presentation and measures its quotient, but does not claim that the
remaining 449-variable ideal is small enough for a Groebner decision.
"""
from __future__ import annotations

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
INPUT = ROOT / "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json"
OUTPUT = HERE / "acyclic-graph-delta2.json"


def digest_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def digest_lines(lines):
    return digest_text("".join(str(x) + "\n" for x in lines))


started = time.monotonic()
data = json.loads(INPUT.read_text())
assert data["branch"] == "delta2" and data["stage"] == 8
assert data["field"] == "Q" and data["residual_rows"] == []
maps = data["maps"]
source = sorted(set(data["full_free_coordinates"]) | {"Zrho"})
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


def source_table(key):
    return {(r, z): fmpq_mpoly(e.replace("**", "^"), ctx=ctx) for r, z, e in maps[key]}


h3, c2, c3, D0, C0 = map(source_table, ["h3", "C2", "C3", "B2", "A3"])
h0 = addpoly(mulpoly(mulpoly(h3, h3), h3), mulpoly(c2, h3), c3)

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


# The exact depressed-cubic circuit, in the H-adic normalization.  Physical
# T2 depth 143 becomes circuit depth 141 after the documented two-unit shed.
H = lift(adds(h, {(33, 0): "-target_b/6"}), "H")
v = lift(adds(D, {(65, 0): "target_a/3+target_b^2/18"}), "v")
V = adds(C, shift(D, 33, factor="-target_b/4"),
         {(98, 0): "target_a*target_b/12+target_b^3/54-target_c/2"})
assert min(r for r, _ in V) >= 1
U = lift({(r - 1, z): scale(e, "8/3") for (r, z), e in V.items()}, "U")
R = adds(mul(v, v), {p: neg(e) for p, e in mul(U, H).items()})
Rlow = {}
rhigh = 0
for (r, z), expression in sorted(R.items()):
    if z >= 33:
        rows.append((f"T2_Rhigh_{r}_{z}", expression, "T2_upper", None))
        rhigh += 1
    else:
        Rlow[(r, z)] = expression
Rlow = lift(Rlow, "R")
HH = lift(mul(H, H, 161 - min(r for r, _ in Rlow)), "HH")
vU = lift(mul(v, U, 160), "vU")
pp = "target_d+target_b*target_c/2-(target_a+target_b^2/4)^2/3"
Q = adds(
    {p: scale(e, "3/4") for p, e in mul(Rlow, HH, 161).items()},
    shift(mul(vU, H, 160), 1, factor="-1/8"),
    shift(mul(v, Rlow, 160), 1),
    shift(mul(U, U, 159), 2, factor="-9/64"),
    shift(HH, 130, factor=pp),
    shift(v, 131, factor=pp),
)
Q = {p: e for p, e in Q.items() if p[0] <= 161}

# Retain the Q jet as graph coordinates.  At the face, include all 56 slots;
# an absent circuit coefficient is an exact zero, not an omitted condition.
need = set(Q)
need.update((141, z) for z in range(56))
Qjet = {}
for (r, z) in sorted(need):
    if r < 141:
        rows.append((f"T2_strict_{r}_{z}", Q.get((r, z), "0"), "T2_strict", None))
        continue
    qname = f"xQ_{r - 141}_{z}"
    graph.append(qname)
    rows.append((f"def_Q_{r - 141}_{z}", qname + "-(" + Q.get((r, z), "0") + ")", "graph", qname))
    Qjet[(r - 141, z)] = qname
    defect = r - 141
    if defect == 0:
        target = f"{math.comb(15, z - 40)}*leader55" if 40 <= z <= 55 else "0"
        rows.append((f"T2_face_{z}", qname + "-(" + target + ")", "T2_face", None))
    elif z > 55 - defect:
        rows.append((f"T2_support_{defect}_{z}", qname, "T2_support", None))

# Through defect 20 the outer corrections start too late, hence F=h^3,G=h^2.
ht = {p: e for p, e in h.items() if p[0] <= 20}
F = lift(mul(mul(ht, ht, 20), ht, 20), "F")
G = lift(mul(ht, ht, 20), "G")
Qsq = lift(mul(Qjet, Qjet, 20), "Qsq")
FG = lift(mul(F, G, 20), "FG")
FQ = lift(mul(F, Qjet, 9), "FQ")
T3 = adds(
    mul(Qsq, Qjet, 20),
    {p: scale(e, "t3eq") for p, e in FG.items()},
    shift(FQ, 11, factor="t3_fq"),
)
rows.append(("T3_equality_coefficient", "t3eq+leader55^3", "T3_recurrence", None))
for (r, z), expression in sorted(T3.items()):
    if r < 20:
        rows.append((f"T3_strict_{r}_{z}", expression, "T3_strict", None))

# Complete attained face: every z=0,...,145 slot plus every generated slot
# above 145.  The two-point target is lambda3*z^105*(1+z)^40.
t3_face_z = set(range(146)) | {z for (r, z) in T3 if r == 20}
for z in sorted(t3_face_z):
    target = f"{math.comb(40, z - 105)}*lambda3" if 105 <= z <= 145 else "0"
    rows.append((f"T3_face_{z}", T3.get((20, z), "0") + "-(" + target + ")", "T3_face", None))
rows += [
    ("inverse_T2", "Z55*leader55-1", "inverse", None),
    ("inverse_T3", "Z3*lambda3-1", "inverse", None),
    ("inverse_separation", "Zrho*rho-1", "inverse", None),
]

all_names = source + ["t3eq", "t3_fq", "lambda3", "Z3"] + graph
assert len(all_names) == len(set(all_names))
created = set(source + ["t3eq", "t3_fq", "lambda3", "Z3"])
parsed_terms = 0
max_terms = (0, None)
parsed = []
graph_ledger = []
for name, expression, kind, pivot in rows:
    local_names = sorted(set(re.findall(r"\b[A-Za-z_]\w*\b", expression)))
    if not local_names:
        parsed.append((None, None, None))
        assert expression in {"0", "0-(0)"}
        continue
    local_ctx = fmpq_mpoly_ctx.get(tuple(local_names), "lex")
    local_index = {v: i for i, v in enumerate(local_names)}
    polynomial = fmpq_mpoly(expression.replace("**", "^"), ctx=local_ctx)
    parsed.append((polynomial, local_ctx, local_index))
    parsed_terms += len(polynomial)
    if len(polynomial) > max_terms[0]:
        max_terms = (len(polynomial), name)
    if pivot:
        pi = local_index[pivot]
        occurrences = [(mon, coefficient) for mon, coefficient in polynomial.terms() if mon[pi]]
        assert len(occurrences) == 1
        assert occurrences[0][0][pi] == 1 and sum(occurrences[0][0]) == 1
        assert occurrences[0][1] == 1
        dependencies = {
            local_names[i]
            for mon, _ in polynomial.terms()
            for i, exponent in enumerate(mon)
            if exponent and i != pi
        }
        assert dependencies <= created, (name, sorted(dependencies - created)[:10])
        created.add(pivot)
        graph_ledger.append(f"{name}\t{pivot}\t1\t{digest_text(expression)}")

# Check every graph row by exact substitution, not a sample.  Since each row
# has a local context, this remains small and also validates the sign used for
# its inverse image.
roundtrip = []
for (name, expression, kind, pivot), (polynomial, local_ctx, local_index) in zip(rows, parsed):
    if not pivot:
        continue
    generators = list(local_ctx.gens())
    pi = local_index[pivot]
    image = -(polynomial - generators[pi])
    substitutions = generators.copy()
    substitutions[pi] = image
    assert polynomial.compose(*substitutions, ctx=local_ctx).is_zero()
    roundtrip.append(f"{name}\t{pivot}\t{digest_text(str(image))}")

block_counts = Counter(kind for _, _, kind, _ in rows)
t2_vector = [math.comb(15, z - 40) if 40 <= z <= 55 else 0 for z in range(56)]
t3_vector = [math.comb(40, z - 105) if 105 <= z <= 145 else 0 for z in range(146)]
record = {
    "status": "EXACT_ACYCLIC_PRESENTATION_AUDITED_NO_GB_DECISION",
    "case": "99-delta2",
    "field": "Q",
    "input": str(INPUT.relative_to(ROOT)),
    "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    "source_stage": data["stage"],
    "source_free_generators": len(data["full_free_coordinates"]),
    "source_residual_rows": len(data["residual_rows"]),
    "source_plus_separation_inverse_generators": len(source),
    "presentation_generator_count": len(all_names),
    "presentation_generator_order_sha256": digest_lines(all_names),
    "graph_generator_count": len(graph),
    "graph_row_count": block_counts["graph"],
    "graph_rows_all_monic_rational_leader_plus_one": True,
    "graph_dependencies_all_preceding": True,
    "graph_ledger_sha256": digest_lines(graph_ledger),
    "all_graph_roundtrip_count": len(roundtrip),
    "all_graph_roundtrips_exact_zero": True,
    "roundtrip_images_sha256": digest_lines(roundtrip),
    "semantic_quotient_generator_count_before_constraint_pivots": len(all_names) - len(graph),
    "constraint_row_count": len(rows) - block_counts["graph"],
    "total_row_count": len(rows),
    "row_block_counts": dict(sorted(block_counts.items())),
    "row_labels_sha256": digest_lines(name for name, _, _, _ in rows),
    "row_expressions_sha256": digest_lines(expression for _, expression, _, _ in rows),
    "parsed_exact_term_count": parsed_terms,
    "maximum_row_terms": max_terms[0],
    "maximum_row_label": max_terms[1],
    "supports": {
        "h": len(h), "D": len(D), "C": len(C), "R_high": rhigh,
        "Q_expression": len(Q), "Q_defect_jet": len(Qjet), "F": len(F),
        "G": len(G), "T3_expression": len(T3),
    },
    "T2_depths": {"H_adic": 141, "physical": 143, "defect": 20},
    "T2_face": "leader55*z^40*(1+z)^15",
    "T2_face_slots": len(t2_vector),
    "T2_face_vector_sha256": digest_lines(t2_vector),
    "T3_recurrence_active": "Q^3+t3eq*F*G+t^11*t3_fq*F*Q",
    "T3_equality_unit_row": "t3eq+leader55^3",
    "T3_face": "lambda3*z^105*(1+z)^40",
    "T3_face_slots": len(t3_vector),
    "T3_face_vector_sha256": digest_lines(t3_vector),
    "localizers": ["Z55*leader55-1", "Z3*lambda3-1", "Zrho*rho-1"],
    "no_raw_Jacobian_rows": True,
    "no_saturation": True,
    "build_wall_seconds": round(time.monotonic() - started, 3),
    "peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "decision": "COMPUTE_BOUND_OPEN",
    "decision_reason": "exact graph quotient still has 449 generators; no exact-Q Groebner basis was launched",
    "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
OUTPUT.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps(record, indent=2, sort_keys=True))
