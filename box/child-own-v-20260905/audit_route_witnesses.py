#!/usr/bin/env python3
"""Independent arithmetic check of all saved necessary-tree witnesses.

Does not import own_v_routes or establish coefficient/pair realization.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def main():
    data = json.loads((HERE / "full-source-routes.json").read_text())
    counts = Counter()
    for row in data["rows"]:
        n, m, M = row["n"], row["m"], [None] + row["M"]
        s = len(row["M"])
        d = [None, n]
        for value in M[1:]:
            d.append(gcd(d[-1], value))

        def radius(i, high):
            f = F(n - M[i], n - M[s] - 1)
            for k, value in zip(range(i + 1, s + 1), high):
                f *= F(value * (n - M[k]) - d[k], value * (n - M[k - 1]) - d[k])
            return 1 - f

        def check(node, j, high, L, danger, need=None, first=None):
            counts["node_occurrences"] += 1
            if j == 1:
                assert not danger
                delta = radius(1, high)
                A = (L * delta).denominator
                V = high[0]
                ns, ms = n // d[2], m // d[2]
                assert ((ns * V) % A == 0 and (ms * V - 1) % A == 0 or
                        (ms * V) % A == 0 and (ns * V - 1) % A == 0)
                assert node == dict(V2=V, delta1=str(delta), A1=A, centre_L=L)
                assert first is None
                counts["bottom_occurrences"] += 1
                return
            delta = radius(j, high)
            A = (L * delta).denominator
            P = F(high[0] * d[j], d[j + 1])
            Q = F(high[0] * (n - M[j]), d[j + 1])
            assert P.denominator == Q.denominator == 1
            z, orbits = node["z"], node["orbits"]
            lo = F(d[j], n - M[j])
            assert node["j"] == j and F(node["delta"]) == delta
            assert node["centre_L"] == L and node["A"] == A
            assert node["danger"] == danger and node["P"] == P and node["Q"] == Q
            assert z >= 0 and all(r > 0 for r in orbits)
            assert z + A * sum(orbits) == P
            assert int(z > 0) + A * len(orbits) <= Q
            assert not z or P != Q * z
            assert all(P != Q * r for r in orbits)
            assert z > lo or any(r > lo for r in orbits)
            removable = delta.denominator == 1 and delta <= 0

            def next_node(child, v, zero, selected=False):
                newL = L if zero else lcm(L, delta.denominator)
                newdanger = danger and (zero or removable)
                newfirst = first if selected and (zero or removable) else None
                tail = need[1:] or None if selected else None
                check(child, j - 1, (v,) + high, newL, newdanger, tail, newfirst)

            if z > lo:
                assert node["zero_major_child"] is not None
                next_node(node["zero_major_child"], z, True)
            else:
                assert node["zero_major_child"] is None
            children = node["nonzero_major_children"]
            assert set(map(int, children)) == {r for r in orbits if r > lo}
            for r in set(orbits):
                if r > lo:
                    next_node(children[str(r)], r, False)
            if need is None:
                assert node["mode"] == "free" and node["selected_child"] is None
            else:
                mode = node["mode"]
                value = need[0]
                assert value > lo
                if mode == "zero":
                    assert value == z and (first is None or j > first or removable)
                    next_node(node["selected_child"], value, True, True)
                else:
                    assert mode == "nonzero" and value in orbits
                    assert first is None or j == first and delta > 0
                    next_node(node["selected_child"], value, False, True)

        for kept in row["kept"]:
            V = row["V"]
            check(kept["witness"], s - 1, (V[-1],), 1, True,
                  tuple(reversed(V[:-1])), kept["first_nonzero"])
            counts["root_witnesses"] += 1
            counts["dropped_witnesses"] += bool(row["drops"])
            if not row["drops"]:
                counts["remaining_witnesses"] += 1
                counts["remaining_us1" if row["u_s"] == 1 else "remaining_us_gt1"] += 1
    result = dict(status="PASS", count_type="DETERMINED", counts=counts,
                  scope="saved necessary-tree arithmetic and every mandatory major continuation; no realization claim")
    (HERE / "route-witness-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
