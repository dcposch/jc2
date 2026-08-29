#!/usr/bin/env python3
"""Exact DEP-D3 factor-local raw-to-Morse cleanup DAG compiler.

All symbolic coefficients live over A=Q[c]/(c^8-1).  The expression DAG is
division-free in raw variables; the only divisions are exact inversions of
displayed constant units of A in formal-series recurrences.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
N = 22

PINS = {
    "preregistration": (
        "cases/ggv_8_28_raw_to_morse_cleanup_dag_d4_20260827/PREREGISTRATION.md",
        "8983eb7d4156a4d823277fa4f44fbe8ac6b7cbddeea19819ca9be20c0ba019c8",
    ),
    "dep_d3_freeze": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256",
        "012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022",
    ),
    "dep_d3_report": (
        "xmodel/ggv-8_28-raw-to-global-M-cokernel-interface-d3-sol-20260827.md",
        "c7ea900bdf0552c50d2a61c5a8f0f41a7b06e24eccedf5e5ab9cef3946c53556",
    ),
    "dep_d3_raw": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json",
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    ),
    "dep_d3_result": (
        "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RESULT.json",
        "a1d83f3f0ec1635844a3d8c67b59ce437c8d846617ae1250f2cf2e3db4a64b3f",
    ),
    "r2_result": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json",
        "0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d",
    ),
    "r2_review": (
        "xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-hostile-review-grok-20260827.md",
        "b271a2958138d8e85c0a8cab068efd7bfa59227a56e5252eb27310a50fb11e24",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qstr(q: Q) -> str:
    return str(Q(q))


# A=Q[c]/(c^8-1), coefficient of c^i in position i.
AZERO = (Q(0),) * 8
AONE = (Q(1),) + (Q(0),) * 7


def aclean(items):
    out = [Q(0)] * 8
    for i, x in enumerate(items):
        out[i % 8] += Q(x)
    return tuple(out)


def aadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def aneg(a):
    return tuple(-x for x in a)


def amul(a, b):
    out = [Q(0)] * 8
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                out[(i + j) % 8] += x * y
    return tuple(out)


def ascale(a, q):
    return tuple(Q(q) * x for x in a)


def cpow(n):
    out = [Q(0)] * 8
    out[n % 8] = Q(1)
    return tuple(out)


def ainv(a):
    """Exact inverse in A, failing if multiplication by a is singular."""
    mat = []
    for row in range(8):
        mat.append([amul(a, cpow(col))[row] for col in range(8)] + [Q(1 if row == 0 else 0)])
    for col in range(8):
        pivot = next((r for r in range(col, 8) if mat[r][col]), None)
        assert pivot is not None, f"nonunit in A at column {col}: {a}"
        mat[col], mat[pivot] = mat[pivot], mat[col]
        scale = mat[col][col]
        mat[col] = [x / scale for x in mat[col]]
        for row in range(8):
            if row == col or not mat[row][col]:
                continue
            scale = mat[row][col]
            mat[row] = [x - scale * y for x, y in zip(mat[row], mat[col])]
    out = tuple(mat[i][-1] for i in range(8))
    assert amul(a, out) == AONE
    return out


def aencode(a):
    return [qstr(x) for x in a]


class Dag:
    def __init__(self):
        self.nodes = []
        self.intern = {}
        self.const_values = {}
        self.zero = self.const(AZERO)
        self.one = self.const(AONE)

    def _put(self, key, record):
        if key in self.intern:
            return self.intern[key]
        node_id = len(self.nodes)
        record = {"id": node_id, **record}
        self.nodes.append(record)
        self.intern[key] = node_id
        return node_id

    def const(self, a):
        a = tuple(Q(x) for x in a)
        key = ("ConstA", tuple(qstr(x) for x in a))
        node = self._put(key, {"op": "ConstA", "value": aencode(a)})
        self.const_values[node] = a
        return node

    def rational(self, q):
        return self.const(ascale(AONE, Q(q)))

    def var(self, name):
        return self._put(("Raw", name), {"op": "Raw", "slot": name})

    def is_const(self, node):
        return node in self.const_values

    def mul(self, *items):
        coeff = AONE
        rest = []
        for node in items:
            rec = self.nodes[node]
            children = rec["args"] if rec["op"] == "Mul" else [node]
            for child in children:
                if self.is_const(child):
                    coeff = amul(coeff, self.const_values[child])
                else:
                    rest.append(child)
        if coeff == AZERO:
            return self.zero
        rest.sort()
        if not rest:
            return self.const(coeff)
        if coeff != AONE:
            rest.insert(0, self.const(coeff))
        if len(rest) == 1:
            return rest[0]
        key = ("Mul", tuple(rest))
        return self._put(key, {"op": "Mul", "args": rest})

    def neg(self, node):
        return self.mul(self.rational(-1), node)

    def _split_term(self, node):
        if self.is_const(node):
            return self.const_values[node], ()
        rec = self.nodes[node]
        if rec["op"] == "Mul" and rec["args"] and self.is_const(rec["args"][0]):
            return self.const_values[rec["args"][0]], tuple(rec["args"][1:])
        return AONE, (node,)

    def add(self, *items):
        flat = []
        for node in items:
            rec = self.nodes[node]
            flat.extend(rec["args"] if rec["op"] == "Add" else [node])
        groups = {}
        for node in flat:
            coeff, base = self._split_term(node)
            groups[base] = aadd(groups.get(base, AZERO), coeff)
        terms = []
        for base, coeff in sorted(groups.items()):
            if coeff == AZERO:
                continue
            if not base:
                terms.append(self.const(coeff))
            else:
                args = list(base)
                if coeff != AONE:
                    args.insert(0, self.const(coeff))
                terms.append(self.mul(*args))
        terms.sort()
        if not terms:
            return self.zero
        if len(terms) == 1:
            return terms[0]
        key = ("Add", tuple(terms))
        return self._put(key, {"op": "Add", "args": terms})

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scale_a(self, node, a):
        return self.mul(self.const(a), node)

    def output(self):
        return self.nodes


def szero(dag):
    return [dag.zero] * (N + 1)


def sadd(dag, *series):
    assert series
    out = [dag.zero] * (N + 1)
    for item in series:
        out = [dag.add(x, y) for x, y in zip(out, item)]
    return out


def sneg(dag, a):
    return [dag.neg(x) for x in a]


def sscale_expr(dag, a, q):
    return [dag.mul(q, x) for x in a]


def smul(dag, a, b):
    out = [dag.zero] * (N + 1)
    for n in range(N + 1):
        terms = [dag.mul(a[i], b[n - i]) for i in range(n + 1)]
        out[n] = dag.add(*terms)
    return out


def spow(dag, a, k):
    out = [dag.zero] * (N + 1)
    out[0] = dag.one
    for _ in range(k):
        out = smul(dag, out, a)
    return out


def sinv(dag, a, label, unit_log):
    assert dag.is_const(a[0]), f"{label}: nonconstant series leading coefficient"
    a0 = dag.const_values[a[0]]
    a0_inv = ainv(a0)
    inv0 = dag.const(a0_inv)
    unit_log.append({"operation": "SeriesInverse", "label": label, "constant": aencode(a0), "inverse": aencode(a0_inv)})
    out = [dag.zero] * (N + 1)
    out[0] = inv0
    for n in range(1, N + 1):
        conv = dag.add(*[dag.mul(a[i], out[n - i]) for i in range(1, n + 1)])
        out[n] = dag.neg(dag.mul(inv0, conv))
    return out


def ssqrt(dag, a, root0_a, label, unit_log):
    assert dag.is_const(a[0])
    assert amul(root0_a, root0_a) == dag.const_values[a[0]]
    denom = ascale(root0_a, 2)
    denom_inv = ainv(denom)
    unit_log.append({"operation": "SeriesSquareRoot", "label": label, "oriented_root": aencode(root0_a), "two_root_inverse": aencode(denom_inv)})
    out = [dag.zero] * (N + 1)
    out[0] = dag.const(root0_a)
    inv_node = dag.const(denom_inv)
    for n in range(1, N + 1):
        inner = dag.add(*[dag.mul(out[i], out[n - i]) for i in range(1, n)])
        out[n] = dag.mul(inv_node, dag.sub(a[n], inner))
    return out


def poly_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Q(0)) + x * y
    return {i: c for i, c in out.items() if c}


def poly_pow(a, n):
    out = {0: Q(1)}
    for _ in range(n):
        out = poly_mul(out, a)
    return out


H_POLY = {0: Q(-1), 8: Q(1)}
F0_POLY = poly_pow(H_POLY, 2)
G0_POLY = poly_pow(H_POLY, 3)


def falling(i, r):
    out = 1
    for k in range(r):
        out *= i - k
    return out


class RawRows:
    def __init__(self, source, dag):
        self.source = source
        self.dag = dag
        self.by_kind_weight = {}
        for kind in ("F", "G"):
            table = {}
            for slot in source["raw_slots_through_weight_22"][kind]:
                table.setdefault(slot["weight"], []).append(slot)
            self.by_kind_weight[kind] = table

    def derivative_at_c(self, kind, weight, derivative):
        if weight == 0:
            poly = F0_POLY if kind == "F" else G0_POLY
            a = AZERO
            for i, coeff in poly.items():
                if i >= derivative:
                    a = aadd(a, ascale(cpow(i - derivative), coeff * falling(i, derivative)))
            return self.dag.const(a)
        terms = []
        for slot in self.by_kind_weight[kind].get(weight, []):
            i = slot["raw_exponents"]["x"]
            if i < derivative:
                continue
            coeff = ascale(cpow(i - derivative), falling(i, derivative))
            terms.append(self.dag.scale_a(self.dag.var(slot["slot"]), coeff))
        return self.dag.add(*terms)


def compose_total(dag, rows, kind, derivative, shift, cutoff=N):
    """Series for sum t^n P_n^(derivative)(c+shift(t))."""
    max_degree = 16 if kind == "F" else 24
    powers = [[dag.zero] * (N + 1) for _ in range(max_degree + 1)]
    powers[0][0] = dag.one
    for k in range(1, max_degree + 1):
        powers[k] = smul(dag, powers[k - 1], shift)
    out = [dag.zero] * (N + 1)
    for weight in range(cutoff + 1):
        for k in range(max_degree - derivative + 1):
            leaf = rows.derivative_at_c(kind, weight, derivative + k)
            if leaf == dag.zero:
                continue
            coeff = dag.mul(dag.rational(Q(1, math.factorial(k))), leaf)
            for tdeg in range(cutoff - weight + 1):
                term = powers[k][tdeg]
                if term != dag.zero:
                    out[weight + tdeg] = dag.add(out[weight + tdeg], dag.mul(coeff, term))
    return out


def solve_critical_section(dag, rows, unit_log):
    shift = [dag.zero] * (N + 1)
    f0xx = rows.derivative_at_c("F", 0, 2)
    assert dag.is_const(f0xx)
    f0xx_a = dag.const_values[f0xx]
    f0xx_inv_a = ainv(f0xx_a)
    f0xx_inv = dag.const(f0xx_inv_a)
    unit_log.append({"operation": "ImplicitCriticalSection", "label": "F_X(c+s,t)=0", "linear_coefficient": aencode(f0xx_a), "inverse": aencode(f0xx_inv_a)})
    equations = []
    for n in range(1, N + 1):
        known = compose_total(dag, rows, "F", 1, shift, n)[n]
        shift[n] = dag.neg(dag.mul(f0xx_inv, known))
        equations.append({"weight": n, "known_node": known, "solution_node": shift[n], "rule": "s_n=-(F0''(c))^-1*known_n"})
    return shift, equations


def series_ids(series):
    return {str(i): node for i, node in enumerate(series)}


def sparse_tx_add(a, b):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = out.get(mon, Q(0)) + coeff
        if not out[mon]:
            del out[mon]
    return out


def sparse_tx_mul(a, b):
    out = {}
    for (ta, xa), ca in a.items():
        for (tb, xb), cb in b.items():
            mon = (ta + tb, xa + xb)
            out[mon] = out.get(mon, Q(0)) + ca * cb
    return {mon: coeff for mon, coeff in out.items() if coeff}


def sparse_tx_scale(a, q):
    return {mon: Q(q) * coeff for mon, coeff in a.items() if Q(q) * coeff}


def encode_tx(a):
    return [{"t_degree": t, "X_degree": x, "coefficient": qstr(a[t, x])} for t, x in sorted(a)]


def discriminator(source):
    Htx = {(0, 0): Q(-1), (0, 8): Q(1)}
    u = sparse_tx_add(Htx, {(6, 1): Q(1), (8, 0): Q(-1, 2)})
    U = {(14, 1): Q(1), (16, 0): Q(-1, 4)}
    F = sparse_tx_add(sparse_tx_mul(u, u), U)
    expected = sparse_tx_add(
        sparse_tx_mul(Htx, Htx),
        {(6, 1): Q(-2), (6, 9): Q(2), (8, 0): Q(1), (8, 8): Q(-1), (12, 2): Q(1)},
    )
    assert F == expected
    assert not any(t in (14, 16) for t, _ in F)

    slot_by_key = {}
    for slot in source["raw_slots_through_weight_22"]["F"]:
        slot_by_key[slot["weight"], slot["raw_exponents"]["x"]] = slot
    rows = []
    leading = sparse_tx_mul(Htx, Htx)
    for (t, x), coeff in sorted(sparse_tx_add(F, sparse_tx_scale(leading, -1)).items()):
        assert (t, x) in slot_by_key
        rows.append({"slot": slot_by_key[t, x]["slot"], "weight": t, "X_degree": x, "coefficient": qstr(coeff)})
    assert (14, 1) not in slot_by_key

    # Sign mutations retain a forbidden residual at an empty raw slice.
    bad_u = sparse_tx_add(Htx, {(6, 1): Q(1), (8, 0): Q(1, 2)})
    bad_sign_F = sparse_tx_add(sparse_tx_mul(bad_u, bad_u), U)
    assert bad_sign_F != expected
    bad_U = {(14, 1): Q(1), (16, 0): Q(1, 4)}
    bad_u16_F = sparse_tx_add(sparse_tx_mul(u, u), bad_U)
    assert any(t == 16 for t, _ in bad_u16_F)
    assert not any(slot["weight"] == 16 for slot in source["raw_slots_through_weight_22"]["F"])

    return {
        "status": "PASS-U14-X-SYNTHESIZED-FROM-LEGAL-LOWER-RAW-ROWS",
        "identity": {
            "H": "X^8-1",
            "u": "H+t^6*X-(1/2)*t^8",
            "U": "t^14*X-(1/4)*t^16",
            "F_equals_u2_plus_U": encode_tx(F),
            "F_compact": "H^2+2*t^6*H*X-t^8*H+t^12*X^2",
            "legal_nonleading_raw_rows": rows,
            "cancelled_weights": {"14": "-X+X=0", "16": "1/4-1/4=0"},
            "orientation": "u=H mod t",
            "local_unit": "u_X=H'(X)+t^6, whose closed-fibre value H'(c) is a unit",
        },
        "consequence": "raw F14 support alone cannot exclude local U14=X",
        "mutations": {
            "flip_minus_half_in_u": "REJECTED: sparse identity changes",
            "flip_minus_quarter_in_U": "REJECTED: leaves a t^16/2 term where the raw F16 slice is empty",
            "delete_supporting_row": "REJECTED: sparse identity changes",
            "insert_raw_F14_X": "REJECTED: no D3 slot (14,1); it would pull back to x*y^-3",
        },
    }


def build_result(source_bytes, source):
    observed = {}
    for key, (rel, expected) in PINS.items():
        got = sha256(ROOT / rel)
        assert got == expected, (key, got, expected)
        observed[key] = {"path": rel, "sha256": got}
    assert hashlib.sha256(source_bytes).hexdigest() == PINS["dep_d3_raw"][1]
    assert source["schema"] == "GGV-8_28-D3-RAW-TO-GLOBAL-v1"

    dag = Dag()
    rows = RawRows(source, dag)
    unit_log = []
    critical, critical_equations = solve_critical_section(dag, rows, unit_log)

    U = compose_total(dag, rows, "F", 0, critical)
    Fxx = compose_total(dag, rows, "F", 2, critical)
    Fxxx = compose_total(dag, rows, "F", 3, critical)
    Fxxxx = compose_total(dag, rows, "F", 4, critical)
    half = dag.rational(Q(1, 2))
    sixth = dag.rational(Q(1, 6))
    twentyfourth = dag.rational(Q(1, 24))
    A2 = sscale_expr(dag, Fxx, half)
    A3 = sscale_expr(dag, Fxxx, sixth)
    A4 = sscale_expr(dag, Fxxxx, twentyfourth)

    Hp_a = ascale(cpow(7), 8)
    q0 = ssqrt(dag, A2, Hp_a, "q0=sqrt(F_XX(xi,t)/2), oriented by H'(c)", unit_log)
    alpha = sinv(dag, q0, "alpha=q0^-1", unit_log)
    q1 = sscale_expr(dag, smul(dag, A3, alpha), half)
    q1sq = smul(dag, q1, q1)
    q2 = sscale_expr(dag, smul(dag, sadd(dag, A4, sneg(dag, q1sq)), alpha), half)
    alpha2 = smul(dag, alpha, alpha)
    alpha3 = smul(dag, alpha2, alpha)
    alpha4 = smul(dag, alpha3, alpha)
    alpha5 = smul(dag, alpha4, alpha)
    beta = sneg(dag, smul(dag, q1, alpha3))
    gamma = sadd(
        dag,
        sscale_expr(dag, smul(dag, q1sq, alpha5), dag.rational(2)),
        sneg(dag, smul(dag, q2, alpha4)),
    )

    g0 = compose_total(dag, rows, "G", 0, critical)
    g1 = compose_total(dag, rows, "G", 1, critical)
    g2 = sscale_expr(dag, compose_total(dag, rows, "G", 2, critical), half)
    g3 = sscale_expr(dag, compose_total(dag, rows, "G", 3, critical), sixth)
    W = g0
    V = smul(dag, g1, alpha)
    Qseries = sadd(dag, smul(dag, g1, beta), smul(dag, g2, alpha2))
    Gamma = sadd(
        dag,
        smul(dag, g1, gamma),
        sscale_expr(dag, smul(dag, smul(dag, g2, alpha), beta), dag.rational(2)),
        smul(dag, g3, alpha3),
    )

    # Closed fibre controls fold to constants without assigning raw rows.
    expected_zero = dag.zero
    expected_one = dag.one
    assert U[0] == expected_zero
    assert W[0] == expected_zero
    assert V[0] == expected_zero
    assert Qseries[0] == expected_zero
    assert Gamma[0] == expected_one
    assert critical[0] == expected_zero

    factors = source["factor_registry"]
    factor_ids = [f["factor_id"] for f in factors]
    tags = {
        "algebra": "A=Q[c]/(c^8-1), projected factorwise",
        "factor_ids": factor_ids,
        "chart": "X=xi(t)+z; u=z*(q0+q1*z+q2*z^2+O(z^3))",
        "orientation": "u=H mod t",
        "determinant": "u_X(c,0)=H'(c)=8c^7",
        "deck": "ORIENTED_PLUS_H",
        "global_polynomial_automorphism_claim": False,
    }
    outputs = {
        "critical_shift_s": series_ids(critical),
        "U": series_ids(U),
        "coordinate_q0": series_ids(q0),
        "coordinate_q1": series_ids(q1),
        "coordinate_q2": series_ids(q2),
        "inverse_alpha": series_ids(alpha),
        "inverse_beta": series_ids(beta),
        "inverse_gamma": series_ids(gamma),
        "W": series_ids(W),
        "V": series_ids(V),
        "Q": series_ids(Qseries),
        "Gamma": series_ids(Gamma),
    }
    for name, table in outputs.items():
        assert list(table) == [str(i) for i in range(N + 1)], name

    dag_bytes = json.dumps(dag.output(), sort_keys=True, separators=(",", ":")).encode()
    op_census = {}
    for node in dag.nodes:
        op_census[node["op"]] = op_census.get(node["op"], 0) + 1

    result = {
        "status": "PASS-DEP-D3-FACTOR-LOCAL-CLEANUP-DAG-W22",
        "dependency": "DEP-D3",
        "scope": "generic symbolic raw 2S/3S rows with fixed H^2/H^3 leading edge; factor-local formal cleanup through weight 22",
        "pins": observed,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "raw_boundary_relations": {
            "F0": "(X^8-1)^2 (fixed; D3 weight-zero raw slots specialized accordingly)",
            "G0": "(X^8-1)^3 (fixed; D3 weight-zero raw slots specialized accordingly)",
            "positive_weight_rows": "all named D3 raw slots retained as independent leaves",
        },
        "tags": tags,
        "unit_inversions": unit_log,
        "critical_section_equations": critical_equations,
        "outputs": outputs,
        "higher_u_sidecar": {
            "typed_residual": "R_ge4=G(xi+z(u),t)-W-V*u-Q*u^2-Gamma*u^3 in A[[t,u]], ord_u>=4",
            "coefficientwise_expansion": "not needed for R2 constant-channel carrier theorem and not claimed",
            "raw_provenance": "inherited from the same G raw leaves and coordinate DAG",
        },
        "closed_fibre_checks": {"s0": 0, "U0": 0, "W0": 0, "V0": 0, "Q0": 0, "Gamma0": 1},
        "first_discriminator": discriminator(source),
        "dag": {
            "coefficient_algebra": "A=Q[c]/(c^8-1)",
            "node_count": len(dag.nodes),
            "raw_leaf_count": sum(1 for node in dag.nodes if node["op"] == "Raw"),
            "op_census": op_census,
            "allowed_ops": ["ConstA", "Raw", "Add", "Mul"],
            "canonical_compact_encoding_bytes": len(dag_bytes),
            "canonical_compact_encoding_sha256": hashlib.sha256(dag_bytes).hexdigest(),
            "storage": "certificate-sized Merkle/digest manifest; compile_cleanup_dag.py deterministically reconstructs every node before checking this result",
        },
        "firewall": {
            "global_E22_compiled": False,
            "global_H_multiple_controlled": False,
            "claims_not_made": ["Keller recurrence for a specialization", "global polynomial automorphism", "8_28 face/family exclusion", "G2-PSC", "G2-BD", "JC2"],
        },
    }
    assert result["first_discriminator"]["status"] == "PASS-U14-X-SYNTHESIZED-FROM-LEGAL-LOWER-RAW-ROWS"
    return result


def dump(obj):
    return json.dumps(obj, sort_keys=True, indent=2) + "\n"


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--print-result":
        source_path = Path(sys.argv[2])
        source_bytes = source_path.read_bytes()
        print(dump(build_result(source_bytes, json.loads(source_bytes))), end="")
        return
    if len(sys.argv) == 4 and sys.argv[1] == "--check":
        source_path, result_path = Path(sys.argv[2]), Path(sys.argv[3])
        source_bytes = source_path.read_bytes()
        expected = dump(build_result(source_bytes, json.loads(source_bytes))).encode()
        assert result_path.read_bytes() == expected
        print("PASS DEP-D3 exact cleanup DAG replay")
        return
    raise SystemExit("usage: compile_cleanup_dag.py --print-result D3_RAW | --check D3_RAW RESULT")


if __name__ == "__main__":
    main()
