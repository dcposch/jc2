#!/usr/bin/env python3
"""Independent exact support-cardinality audit, using only the Python stdlib.

Run on a worker with --root pointing at a repository-shaped input directory.
No polynomial identity is inferred from a zero specialization. Every potential
nonzero row site is bounded above by support arithmetic; every such row must
evaluate NONZERO at the displayed deterministic finite-field specialization.
Consequently the same rows are nonzero over Q. A zero witness aborts the proof.
Series dictionaries retain zero-valued entries, so numerical cancellation can
never silently shrink the support upper bound.
"""
import argparse
import ast
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re

P = 1000000007
SPECS = {
    "99-delta2": (
        "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
        "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea",
        33, 55, 3, 145, 40, 15, 105, 40, "rho", "Zrho", "leader55", "Z55"),
    "99-delta52": (
        "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
        "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46",
        33, 55, 3, 145, 40, 15, 105, 40, "c", "Zc", "leader55", "Z55"),
    "108-free-mean": (
        "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
        "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814",
        36, 63, 4, 227, 49, 14, 176, 51, "c", "Zc", "leader63", "Z63"),
}


def digest_lines(values):
    return hashlib.sha256("".join(str(x) + "\n" for x in values).encode()).hexdigest()


def add(*tables):
    answer = {}
    for table, scalar in tables:
        for site, value in table.items():
            answer[site] = (answer.get(site, 0) + scalar * value) % P
    return answer


def mul(left, right, cap=None):
    answer = {}
    for (r, z), a in left.items():
        for (s, w), b in right.items():
            if cap is None or r + s <= cap:
                site = (r + s, z + w)
                answer[site] = (answer.get(site, 0) + a * b) % P
    return answer


def shift(table, dr=0, dz=0, scalar=1, cap=None):
    return {(r + dr, z + dz): scalar * value % P
            for (r, z), value in table.items()
            if cap is None or r + dr <= cap}


def power(table, exponent, cap=None):
    answer = {(0, 0): 1}
    for _ in range(exponent):
        answer = mul(answer, table, cap)
    return answer


def split_top(expression):
    pieces = []
    start = depth = 0
    for i, c in enumerate(expression):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            assert depth >= 0
        elif c == "+" and depth == 0:
            pieces.append(expression[start:i])
            start = i + 1
    assert depth == 0
    pieces.append(expression[start:])
    return [x for x in pieces if x]


def audit(tag, root, salt):
    path, expected_sha, k, d2, n2, d3, z2, p2, z3, p3, sep, zsep, lam2, zlam2 = SPECS[tag]
    source = root / path
    raw = source.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected_sha, str(source)
    data = json.loads(raw)
    assignments = {}
    denominators = set()

    def variable(name):
        if name not in assignments:
            token = f"t2t3-hostile-count-v1:{salt}:{tag}:{name}".encode()
            assignments[name] = 1 + int.from_bytes(hashlib.sha256(token).digest(), "big") % (P - 1)
        return assignments[name]

    def evnode(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value % P
        if isinstance(node, ast.Name):
            return variable(node.id)
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -evnode(node.operand) % P
            if isinstance(node.op, ast.UAdd):
                return evnode(node.operand)
        if isinstance(node, ast.BinOp):
            a = evnode(node.left)
            if isinstance(node.op, ast.Pow):
                assert isinstance(node.right, ast.Constant)
                assert type(node.right.value) is int and node.right.value >= 0
                return pow(a, node.right.value, P)
            b = evnode(node.right)
            if isinstance(node.op, ast.Add):
                return (a + b) % P
            if isinstance(node.op, ast.Sub):
                return (a - b) % P
            if isinstance(node.op, ast.Mult):
                return a * b % P
            if isinstance(node.op, ast.Div):
                assert not any(isinstance(x, ast.Name) for x in ast.walk(node.right))
                assert b, "denominator vanishes modulo P"
                denominators.add(b)
                return a * pow(b, -1, P) % P
        raise AssertionError(ast.dump(node))

    def ev(expression):
        return evnode(ast.parse(str(expression).replace("^", "**"), mode="eval").body)

    def table(rows):
        answer = {}
        for r, z, expression in rows:
            site = (int(r), int(z))
            assert site not in answer
            answer[site] = ev(expression)
        return answer

    def text_table(expression):
        rows = []
        for piece in split_top(expression):
            match = re.fullmatch(r"\((.*)\)\*tt\^(\d+)\*zz\^(\d+)", piece)
            assert match
            coefficient, r, z = match.groups()
            rows.append((r, z, coefficient))
        return table(rows)

    if tag.startswith("99-"):
        maps = data["maps"]
        h3, c2, c3, D, C = [table(maps[key]) for key in ("h3", "C2", "C3", "B2", "A3")]
        h = add((power(h3, 3), 1), (mul(c2, h3), 1), (c3, 1))
        residuals = [ev(expression) for _, expression in data["residual_rows"]]
        frozen_names = data["full_free_coordinates"]
        recurrence = ["t3eq", "t3_fq"]
    else:
        h, D, C = [text_table(data[key]) for key in ("h_expr", "D_expr", "C_expr")]
        residuals = [ev(expression) for expression in data["residual_strings"]]
        frozen_names = data["names"]
        recurrence = ["t3eq", "t3_fgq", "t3_fq2"]
    semantic = sorted(set(frozen_names) | {zsep}) + recurrence + ["lambda3", "Z3"]
    assert len(semantic) == len(set(semantic))
    for name in semantic:
        variable(name)
    assert set(assignments) == set(semantic)

    inv = lambda n: pow(n, -1, P)
    a, b, c, d = [variable("target_" + letter) for letter in "abcd"]
    H = add((h, 1), ({(k, 0): b}, -inv(6)))
    v = add((D, 1), ({(2*k-1, 0): (a*inv(3) + b*b*inv(18)) % P}, 1))
    V = add((C, 1), (shift(D, k), -b*inv(4)),
            ({(3*k-1, 0): (a*b*inv(12) + b**3*inv(54) - c*inv(2)) % P}, 1))
    assert min(r for r, _ in V) >= 1
    U = shift(V, -1, scalar=8*inv(3))
    R = add((mul(v, v), 1), (mul(U, H), -1))
    Rlow = {site: value for site, value in R.items() if site[1] < k}
    upper = {site: value for site, value in R.items() if site[1] >= k}
    lead = 6*k-2-d2
    defect = n2*d2-d3
    cap = lead+defect
    HH = mul(H, H, cap-min(r for r, z in Rlow))
    vU = mul(v, U, cap-1)
    pp = (d+b*c*inv(2)-(a+b*b*inv(4))**2*inv(3)) % P
    Q = add((mul(Rlow, HH, cap), 3*inv(4)),
            (shift(mul(vU, H, cap-1), 1), -inv(8)),
            (shift(mul(v, Rlow, cap-1), 1), 1),
            (shift(mul(U, U, cap-2), 2), -9*inv(64)),
            (shift(HH, 4*k-2, scalar=pp, cap=cap), 1),
            (shift(v, 4*k-1, scalar=pp, cap=cap), 1))
    strict2 = {site: value for site, value in Q.items() if site[0] < lead}
    Qjet = {(r-lead, z): value for (r, z), value in Q.items() if r >= lead}
    assert all(z <= d2-r for r, z in Qjet), "additional T2 support rows required"
    target2 = {z: math.comb(p2, z-z2)*variable(lam2) % P for z in range(z2, d2+1)}
    face2sites = {z for r, z in Qjet if r == 0} | set(target2)
    face2 = {z: (Qjet.get((0, z), 0)-target2.get(z, 0)) % P for z in face2sites}
    ht = {site: value for site, value in h.items() if site[0] <= defect}
    F, G = power(ht, 3, defect), power(ht, 2, defect)

    def t3_table(qjet):
        if n2 == 3:
            return add((power(qjet, 3, defect), 1),
                       (mul(F, G, defect), variable("t3eq")),
                       (shift(mul(F, qjet, defect-11), 11), variable("t3_fq")))
        return add((power(qjet, 4, defect), 1),
                   (mul(F, power(G, 2, defect), defect), variable("t3eq")),
                   (shift(mul(mul(F, G, defect-9), qjet, defect-9), 9), variable("t3_fgq")),
                   (shift(mul(F, power(qjet, 2, defect-18), defect-18), 18), variable("t3_fq2")))

    T3 = t3_table(Qjet)
    strict3 = {site: value for site, value in T3.items() if site[0] < defect}
    target3 = {z: math.comb(p3, z-z3)*variable("lambda3") % P for z in range(z3, d3+1)}
    face3sites = {z for r, z in T3 if r == defect} | set(target3)
    face3 = {z: (T3.get((defect, z), 0)-target3.get(z, 0)) % P for z in face3sites}
    assert max(face3sites) <= d3
    rows = []
    for label, values in (("source_residual", dict(enumerate(residuals))),
                          ("T2_upper", upper), ("T2_strict", strict2),
                          ("T2_face", face2), ("T3_strict", strict3),
                          ("T3_face", face3)):
        rows += [(label, str(site), value) for site, value in sorted(values.items())]
    rows.append(("T3_recurrence", "coefficient", (variable("t3eq")+pow(variable(lam2), n2, P)) % P))
    rows += [("inverse", x, (variable(x)*variable(y)-1) % P)
             for x, y in ((zlam2, lam2), ("Z3", "lambda3"), (zsep, sep))]
    failed = [(block, site) for block, site, value in rows if value == 0]
    assert not failed, f"No conclusion from zeros; choose another salt: {failed[:30]}"
    counts = dict(sorted(Counter(block for block, site, value in rows).items()))

    # The old graph adjoins even the absent T2 face coefficients as variables.
    # Their formal products generate additional raw T3 slots, whose images are
    # identically zero once those graph variables are recursively substituted.
    graph_Qjet = dict(Qjet)
    for z in range(d2+1):
        graph_Qjet.setdefault((0, z), 0)
    graph_T3 = t3_table(graph_Qjet)
    graph_raw = dict(counts)
    graph_raw["T2_face"] = d2+1
    graph_raw["T3_strict"] = sum(r < defect for r, z in graph_T3)
    graph_raw["T3_face"] = d3+1
    return {
        "case": tag, "input_sha256": expected_sha,
        "proof_type": "SUPPORT_UPPER_BOUND_EQUALS_ALL_NONZERO_SPECIALIZATION_LOWER_BOUND",
        "prime": P, "salt": salt,
        "semantic_variables": len(semantic), "semantic_order_sha256": digest_lines(semantic),
        "nonzero_generator_counts": counts, "nonzero_generator_total": len(rows),
        "old_graph_raw_counts": graph_raw, "old_graph_raw_total": sum(graph_raw.values()),
        "old_graph_identically_zero_images": sum(graph_raw.values())-len(rows),
        "actual_direct_raw_counts": dict(counts, T2_face=d2+1, T3_face=d3+1),
        "specialization_assignments": dict(sorted(assignments.items())),
        "specialization_values_sha256": digest_lines(f"{b}\t{s}\t{v}" for b, s, v in rows),
        "checked_nonzero_values": len(rows), "zero_witness_values": len(failed),
        "source_constant_denominators_mod_p": sorted(denominators),
        "series_support_counts": {"h":len(h), "D":len(D), "C":len(C),
                                  "R":len(R), "Rlow":len(Rlow), "Q":len(Q),
                                  "Qjet":len(Qjet), "T3":len(T3)},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--case", choices=sorted(SPECS), action="append")
    parser.add_argument("--salt", default="0")
    args = parser.parse_args()
    assert P > 1 and all(P % d for d in range(2, math.isqrt(P)+1)), "prime check"
    for tag in args.case or SPECS:
        print(json.dumps(audit(tag, args.root, args.salt), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
