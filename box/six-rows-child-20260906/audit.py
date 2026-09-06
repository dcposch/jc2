#!/usr/bin/env python3
"""Exact child-partition audit for R025--R028 and R057--R058.

The program reads only the frozen lane inputs named in the receipt.  It
recomputes the first-support alternatives in descend_own.py lines 151--180,
enumerates the printed fixed-list child partitions with Fraction arithmetic,
and writes the JSON certificate used by the accompanying report.

No row is treated as a polynomial-pair witness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path


ROOT = Path("/home/ubuntu/jc2")
INPUTS = Path("/tmp/jc2-lane.EWXUl5/inputs")
RECEIPT = ROOT / "xmodel/six-rows-child-sum-sol56-20260906.run.v2"
ROWS = ("R025", "R026", "R027", "R028", "R057", "R058")


def frac(value):
    return value if isinstance(value, F) else F(str(value))


def show(value):
    value = frac(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def jsonable(value):
    if isinstance(value, F):
        return show(value)
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(v) for v in value]
    return value


def receipt_manifest():
    fields = {}
    for line in RECEIPT.read_text().splitlines():
        if line.startswith("charged_input_") and "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    records = []
    for i in range(1, 11):
        basename = fields[f"charged_input_{i}_basename"]
        expected = fields[f"charged_input_{i}_sha256"]
        path = INPUTS / basename
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({
            "index": i,
            "basename": basename,
            "expected_sha256": expected,
            "actual_sha256": actual,
            "ok": actual == expected,
        })
    assert all(r["ok"] for r in records)
    return records


def load_rows():
    found = {}
    with (INPUTS / "roster.jsonl").open() as handle:
        for line in handle:
            row = json.loads(line)
            if row["row_id"] in ROWS:
                found[row["row_id"]] = row
    assert tuple(sorted(found)) == ROWS
    return found


def prefix_gcds(n, M):
    answer = {1: n}
    for i in range(1, len(M) + 1):
        answer[i + 1] = gcd(answer[i], M[i])
    return answer


def own_first_support(row):
    """Verbatim arithmetic of the frozen descend_own loop, without its dependency."""
    source = row["source"]
    s = source["s"]
    M = {i + 1: int(v) for i, v in enumerate(source["M"])}
    V = {i + 2: int(v) for i, v in enumerate(source["V"])}
    d = prefix_gcds(int(source["n"]), M)
    deltas = {i + 1: frac(v) for i, v in enumerate(source["delta"])}
    assert [d[i] for i in range(1, s + 2)] == source["d"]
    us = int(source["u_s"])
    zero_values = {s: F(us)}
    choices = []
    steps = []
    for i in range(s - 1, 1, -1):
        delta = deltas[i]
        P = F(V[i + 1] * d[i], d[i + 1])
        assert P.denominator == 1
        P = P.numerator
        b = delta.denominator
        zero_ok = (P - V[i]) % b == 0
        nonzero_ok = delta > 0 and b * V[i] <= P
        step = {
            "source_index": i,
            "delta": delta,
            "P": P,
            "selected_V": V[i],
            "denominator": b,
            "zero_ok": zero_ok,
            "nonzero_ok": nonzero_ok,
            "incoming_child_V": zero_values[i + 1],
        }
        if nonzero_ok:
            vector = tuple(
                zero_values[k] if k > i else F(V[k])
                for k in range(2, s)
            )
            choices.append({"first_nonzero": i, "V_vector": vector})
        if zero_ok:
            zero_values[i] = F(d[i], d[i + 1]) * zero_values[i + 1] - delta * (P - V[i])
            step["zero_child_V"] = zero_values[i]
        steps.append(step)
        if not zero_ok:
            break
    own = row["own_child"]
    expected = tuple(F(v) for v in own["V_prime"])
    assert row["provenance"]["own_route_state"] == "NONEMPTY"
    assert len(choices) == 1 and choices[0]["V_vector"] == expected
    assert choices[0]["first_nonzero"] == own["first_nonzero_source_index"]
    return {"steps": steps, "outer_choices": choices, "retained_vector": expected,
            "charged_whole_source_route_state": row["provenance"]["own_route_state"]}


def partitions(total, maximum=None):
    """Integer partitions in descending order."""
    if maximum is None or maximum > total:
        maximum = total
    if total == 0:
        yield ()
        return
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def shifted_leaf(n, m, H, di, Mi, delta0, r, L=1):
    rho_p = F(m, di) * r
    rho_q = F(n, di) * r
    assert rho_p.denominator == rho_q.denominator == 1
    threshold_cmp = r * (n - Mi) - di
    lambda_p = F(m) * (delta0 - H) / (n - Mi)
    a = -lambda_p
    kappa = rho_p * (H - delta0) - a
    base = {
        "r": r,
        "rho_P": int(rho_p),
        "rho_Q": int(rho_q),
        "lambda_P_at_level": lambda_p,
        "kappa": kappa,
        "depth_bound_r_minus_1": r - 1,
    }
    if threshold_cmp == 0:
        return {**base, "kind": "FORBIDDEN_EQUAL_AVERAGE", "complete": False}
    if threshold_cmp < 0:
        delta_final = delta0 + a / rho_p
        A = (F(L) * delta_final).denominator
        return {**base, "kind": "minor", "delta_final": delta_final,
                "A_final": A, "I_M": F(0), "I_m_increment": delta_final - H,
                "residues": [int(rho_p) % A, int(rho_q) % A],
                "complete": r == 1}
    denominator = (n + m) * rho_p - m
    delta_final = F(H) - F(n + m) * kappa / denominator
    contribution = F(n) * rho_p * kappa / denominator
    A = (F(L) * delta_final).denominator
    residues = [int(rho_p) % A, int(rho_q) % A]
    residue_ok = all(v in (0, 1) for v in residues)
    return {**base, "kind": "major", "delta_final": delta_final,
            "A_final": A, "residues": residues, "residue_ok": residue_ok,
            "I_M": contribution, "I_m_increment": F(0),
            "complete": residue_ok}


def branch_types(n, m, H, M2, d2, delta2, P2, Q2):
    records = []
    valid = []
    for part in partitions(P2):
        if len(part) > Q2:
            continue
        leaves = [shifted_leaf(n, m, H, d2, M2, delta2, r, L=1) for r in part]
        record = {
            "multiplicities": part,
            "distinct_p_roots": len(part),
            "leaves": leaves,
            "P_root_total": sum(x["rho_P"] for x in leaves),
            "Q_root_total": sum(x["rho_Q"] for x in leaves),
            "I_M": sum((x["I_M"] for x in leaves), F(0)),
            "I_m_increment": sum((x["I_m_increment"] for x in leaves), F(0)),
            "complete": all(x["complete"] for x in leaves),
        }
        records.append(record)
        if record["complete"]:
            valid.append(record)
    assert all(x["P_root_total"] == F(m, d2) * P2 for x in records)
    assert all(x["Q_root_total"] == F(n, d2) * P2 for x in records)
    return records, valid


def code_for(part):
    codes = {
        (3, 2): "A",
        (3, 1, 1): "B",
        (2, 2, 1): "C",
        (2, 1, 1, 1): "D",
        (3, 1): "E",
    }
    return codes.get(tuple(part), "X")


def family(row):
    own = row["own_child"]
    n, m, ell = own["n_prime"], own["m_prime"], own["ell"]
    H = 1 + ell
    M = {i + 1: int(v) for i, v in enumerate(own["M_prime"])}
    d = {i + 1: int(v) for i, v in enumerate(own["d_prime"])}
    V = {i + 2: int(v) for i, v in enumerate(own["V_prime"])}
    V[4] = d[4]
    delta = {i + 1: frac(v) for i, v in enumerate(own["delta_prime"])}
    P3 = V[4] * d[3] // d[4]
    Q3 = V[4] * (n - M[3]) // d[4]
    top_candidates = [p for p in partitions(P3) if len(p) <= Q3 and V[3] in p]
    assert top_candidates == [(1, 1)]
    top_leaf = shifted_leaf(n, m, H, d[3], M[3], delta[3], 1, L=1)
    assert top_leaf["kind"] == "major"

    P2 = V[3] * d[2] // d[3]
    Q2 = V[3] * (n - M[2]) // d[3]
    candidates, valid = branch_types(n, m, H, M[2], d[2], delta[2], P2, Q2)
    selected = [x for x in valid if V[2] in x["multiplicities"]]
    selected_marked = []
    for item in selected:
        for mark in range(item["multiplicities"].count(V[2])):
            selected_marked.append({"branch": item, "selected_equal_factor_index": mark})

    complete = []
    for tower in selected_marked:
        for sibling in valid:
            major_sum = tower["branch"]["I_M"] + sibling["I_M"]
            minor_floor = F(H) + tower["branch"]["I_m_increment"] + sibling["I_m_increment"]
            complete.append({
                "selected_branch": code_for(tower["branch"]["multiplicities"]),
                "selected_multiplicities": tower["branch"]["multiplicities"],
                "selected_equal_factor_index": tower["selected_equal_factor_index"],
                "sibling_branch": code_for(sibling["multiplicities"]),
                "sibling_multiplicities": sibling["multiplicities"],
                "I_M": major_sum,
                "I_m_shifted": minor_floor,
                "xu_minor_bound_ok": major_sum >= minor_floor,
                "integral_I_M": major_sum.denominator == 1,
                "P_root_total": tower["branch"]["P_root_total"] + sibling["P_root_total"],
                "Q_root_total": tower["branch"]["Q_root_total"] + sibling["Q_root_total"],
            })
    assert all(x["P_root_total"] == m and x["Q_root_total"] == n for x in complete)
    assert all(x["integral_I_M"] for x in complete)

    flat = []
    for tower in selected_marked:
        value = tower["branch"]["I_M"] + top_leaf["I_M"]
        flat.append({
            "selected_branch": code_for(tower["branch"]["multiplicities"]),
            "selected_equal_factor_index": tower["selected_equal_factor_index"],
            "selected_subtotal": tower["branch"]["I_M"],
            "premature_top_sibling_term": top_leaf["I_M"],
            "truncated_I_M": value,
            "integral": value.denominator == 1,
        })
    assert not any(x["integral"] for x in flat)

    return {
        "n": n, "m": m, "ell": ell, "H": H, "M": M, "d": d, "V": V,
        "delta": delta, "actual_entering_stabilizer_L": 1,
        "top": {"P3": P3, "Q3": Q3, "A3": 1,
                "multiplicities": (1, 1), "both_major": True,
                "mandatory_next_level": "D2_by_Prop5.3",
                "premature_immediate_final_leaf": top_leaf},
        "D2": {"P2": P2, "Q2": Q2, "A2": 1,
               "all_candidate_patterns": candidates,
               "valid_complete_patterns": valid},
        "selected_marked_alternatives": selected_marked,
        "flat_negative_controls": flat,
        "complete_partitions": complete,
    }


# Polynomial identity controls. Coefficients are low degree first.
@dataclass(frozen=True)
class Q5:
    """Element a+b*s of Q[s]/(s^2-5), used for the C-face control."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def lift(value):
        return value if isinstance(value, Q5) else Q5(F(value), F(0))

    def __add__(self, other):
        other = self.lift(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        return Q5(self.a * other.a + 5 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __eq__(self, other):
        try:
            other = self.lift(other)
        except (TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(c, a):
    return [c * x for x in a]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def ppow(a, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def pder(a):
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def factor(root):
    return [-F(root), F(1)]


def factor5(root):
    root = Q5.lift(root)
    return [-root, Q5(F(1), F(0))]


def ode_check(P, Q, p, q, C):
    lhs = padd(pscale(P, pmul(p, pder(q))), pscale(-Q, pmul(pder(p), q)))
    return lhs == pscale(C, p)


def ode_controls():
    z = [F(0), F(1)]
    zm1 = factor(1)
    zp1 = factor(-1)
    controls = {}
    p = padd(pmul(z, z), [-1])                         # z^2-1
    q = pmul(pmul(z, p), [-3, 0, 2])                  # z(z^2-1)(2z^2-3)
    controls["top_30_20_(1,1)"] = ode_check(2, 5, p, q, 6)
    q = pmul(z, p)                                     # z(z^2-1)
    controls["top_32_24_(1,1)"] = ode_check(2, 3, p, q, -2)
    p = pmul(ppow(z, 2), ppow(zm1, 3))
    q = pmul(pmul(z, zm1), [7, -35, 25])
    controls["A_(3,2)"] = ode_check(5, 4, p, q, 21)
    p = pmul(ppow(z, 3), [15, -5, 1])
    q = pmul(pmul(z, [15, -5, 1]), zp1)
    controls["B_(3,1,1)"] = ode_check(5, 4, p, q, -105)
    root_a = Q5(F(1, 2), F(1, 2))                 # (1+sqrt(5))/2
    root_c = Q5(F(1, 2), F(-1, 10))               # (5-sqrt(5))/10
    z5 = factor5(0)
    zm15 = factor5(1)
    p = pmul(pmul(ppow(z5, 2), ppow(zm15, 2)), factor5(root_a))
    q = pmul(pmul(pmul(z5, zm15), factor5(root_a)), factor5(root_c))
    controls["C_(2,2,1)_over_Q(sqrt5)"] = ode_check(
        5, 4, p, q, Q5(F(0), F(3, 5)))
    p = pmul(ppow(z, 2), [-1, 0, 0, 1])
    q = pmul(z, [-1, 0, 0, 1])
    controls["D_(2,1,1,1)"] = ode_check(5, 4, p, q, 3)
    p = pmul(ppow(z, 3), [-4, 1])
    q = pmul(pmul(z, [-4, 1]), zp1)
    controls["E_(3,1)"] = ode_check(4, 3, p, q, 20)
    assert all(controls.values())
    return controls


PARENT_WITNESSES = {
    "R025": {"parent_I_M": 17, "selected_branch": "A", "sibling_branch": "D",
             "selection": "small/nonzero source arm, multiplicity 2"},
    "R026": {"parent_I_M": 17, "selected_branch": "D", "sibling_branch": "A",
             "selection": "large/zero source arm, multiplicity 2"},
    "R027": {"parent_I_M": 17, "selected_branch": "A", "sibling_branch": "D",
             "selection": "small/nonzero source arm, multiplicity 3"},
    "R028": {"parent_I_M": 22, "selected_branch": "B", "sibling_branch": "A",
             "selection": "large/zero source arm, multiplicity 3"},
    "R057": {"parent_I_M": 18, "selected_branch": "E", "sibling_branch": "E",
             "selection": "small/nonzero source arm, multiplicity 3"},
    "R058": {"parent_I_M": 18, "selected_branch": "E", "sibling_branch": "E",
             "selection": "large/zero source arm, multiplicity 3"},
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    manifest = receipt_manifest()
    rows = load_rows()
    result = {
        "schema": "jc2.six-rows-child-partition-audit/v1",
        "semantic_scope": "necessary numerical/face configurations, not polynomial-pair witnesses",
        "input_verification": {"ok": True, "count": len(manifest), "records": manifest},
        "ode_identity_controls": ode_controls(),
        "rows": {},
        "verdict_counts": {"SURVIVES": 0, "DEAD": 0, "UNDECIDED": 0},
    }
    expected_flat = {
        "R025": {"127/4", "107/4", "91/4"},
        "R026": {"127/4", "107/4", "91/4"},
        "R027": {"127/4", "111/4"},
        "R028": {"127/4", "111/4"},
        "R057": {"209/9"},
        "R058": {"209/9"},
    }
    for rid in ROWS:
        route = own_first_support(rows[rid])
        data = family(rows[rid])
        flat_values = {show(x["truncated_I_M"]) for x in data["flat_negative_controls"]}
        assert flat_values == expected_flat[rid]
        witness = PARENT_WITNESSES[rid]
        matching = [x for x in data["complete_partitions"]
                    if x["selected_branch"] == witness["selected_branch"]
                    and x["sibling_branch"] == witness["sibling_branch"]
                    and x["I_M"] == witness["parent_I_M"]
                    and x["xu_minor_bound_ok"]]
        assert matching
        result["rows"][rid] = {
            "own_first_support": route,
            "child": data,
            "frozen_flat_values_reproduced": sorted(flat_values),
            "parent_mapped_witness": {**witness, "matching_child_partitions": len(matching)},
            "verdict": "SURVIVES",
            "reason": "integral complete fixed-list child partition exhibited",
        }
        result["verdict_counts"]["SURVIVES"] += 1
    result["all_assertions_pass"] = True
    payload = json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
