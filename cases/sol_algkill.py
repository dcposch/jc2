#!/usr/bin/env python3
"""Exact small checks for xmodel/sol-algkill.md.

Default mode verifies the orbit-contact/Hensel margins behind the bounded
algebraization theorem and the six-slot row/variable census.  ``--row24``
also rebuilds the exact frozen-background Row-24 first-occurrence symbol
(about 25 seconds on the development machine).

No numerical approximation and no solver are used.
"""

from __future__ import annotations

import argparse
import hashlib
import pickle
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
sys.path.insert(0, str(CASES))


P = 105337
R3 = 795
A1 = 50630
A2 = 10114
BETA = 24069
W1 = 7210
W2 = 1
MU = 55070                         # 2*MU^2 = 3 (mod P)


def prime_factors(n: int) -> set[int]:
    out = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root(p: int) -> int:
    fac = prime_factors(p - 1)
    return next(g for g in range(2, p)
                if all(pow(g, (p - 1) // q, p) != 1 for q in fac))


def twist(series: dict[int, int], k: int, zeta: int) -> dict[int, int]:
    return {m: c * pow(zeta, k * m, P) % P for m, c in series.items()}


def orbit(name: str, series: dict[int, int], size: int, zeta: int):
    # A 21-orbit has even support, hence twists k and k+21 agree.
    assert size in (21, 42)
    if size == 21:
        assert all(m % 2 == 0 for m in series)
    return [(name, k, twist(series, k, zeta)) for k in range(size)]


def contact(a: dict[int, int], b: dict[int, int]) -> int:
    levels = sorted(set(a) | set(b))
    return next(m for m in levels if a.get(m, 0) != b.get(m, 0))


def contact_table(roots, orbit_name: str) -> Counter:
    tables = []
    for i, (name, _k, a) in enumerate(roots):
        if name != orbit_name:
            continue
        tables.append(Counter(contact(a, b) for j, (_n, _l, b)
                              in enumerate(roots) if j != i))
    assert tables and all(t == tables[0] for t in tables)
    return tables[0]


def hmargin(table: Counter, e: int) -> tuple[int, int, int]:
    d = sum(level * count for level, count in table.items())
    ell = max(table)
    q = e - d
    assert q > ell
    return d, ell, q


def check_contacts() -> None:
    assert R3 * R3 % P == 3
    assert pow(A1, 3, P) == (3 + R3) % P
    assert pow(A2, 3, P) == (3 - R3) % P
    assert 2 * pow(BETA, 7, P) % P == 3
    assert 2 * MU * MU % P == 3
    g = primitive_root(P)
    zeta = pow(g, (P - 1) // 42, P)
    assert pow(zeta, 42, P) == 1
    assert all(pow(zeta, d, P) != 1 for d in (1, 2, 3, 6, 7, 14, 21))

    f_roots = []
    f_roots += orbit("P1", {12: 1, 32: A1, 37: W1}, 42, zeta)
    f_roots += orbit("P2", {12: 1, 32: A2, 37: W2}, 42, zeta)
    f_roots += orbit("B", {12: BETA, 56: 1, 57: 1}, 42, zeta)
    assert len(f_roots) == 126
    assert len({tuple(sorted(s.items())) for _, _, s in f_roots}) == 126
    f_expected = {
        "P1": Counter({12: 114, 32: 10, 37: 1}),
        "P2": Counter({12: 114, 32: 10, 37: 1}),
        "B": Counter({12: 120, 56: 4, 57: 1}),
    }
    for name, want in f_expected.items():
        got = contact_table(f_roots, name)
        assert got == want, (name, got, want)
    assert hmargin(f_expected["P1"], 43 * 42) == (1725, 37, 81)
    assert hmargin(f_expected["B"], 43 * 42) == (1721, 57, 85)

    h1, h2 = MU * W1 % P, MU * W2 % P
    g_roots = []
    g_roots += orbit("Gp1", {12: 1, 32: A1, 37: h1}, 42, zeta)
    g_roots += orbit("Gp2", {12: 1, 32: A2, 37: h2}, 42, zeta)
    g_roots += orbit("G0p1", {12: 1, 32: A1}, 21, zeta)
    g_roots += orbit("G0p2", {12: 1, 32: A2}, 21, zeta)
    g_roots += orbit("GB42", {12: BETA, 55: 1}, 42, zeta)
    g_roots += orbit("GB21", {12: BETA, 56: 1}, 21, zeta)
    assert len(g_roots) == 189
    assert len({tuple(sorted(s.items())) for _, _, s in g_roots}) == 189
    g_expected = {
        "Gp1": Counter({12: 171, 32: 15, 37: 2}),
        "Gp2": Counter({12: 171, 32: 15, 37: 2}),
        "G0p1": Counter({12: 171, 32: 15, 37: 2}),
        "G0p2": Counter({12: 171, 32: 15, 37: 2}),
        "GB42": Counter({12: 180, 55: 8}),
        "GB21": Counter({12: 180, 55: 6, 56: 2}),
    }
    for name, want in g_expected.items():
        got = contact_table(g_roots, name)
        assert got == want, (name, got, want)
    assert hmargin(g_expected["Gp1"], 64 * 42) == (2606, 37, 82)
    assert hmargin(g_expected["GB42"], 64 * 42) == (2600, 55, 88)
    assert hmargin(g_expected["GB21"], 64 * 42) == (2602, 56, 86)

    # Adding S^42 Y^2 and S^63 Y^2 makes the two relations x-primitive
    # while leaving every D23 coefficient (levels <= 54) unchanged.
    assert 42 * 42 + 2 * 12 - 1725 == 63 > 54
    assert 42 * 42 + 2 * 12 - 1721 == 67 > 54
    assert 63 * 42 + 2 * 12 - 2606 == 64 > 54
    assert 63 * 42 + 2 * 12 - 2600 == 70 > 55
    assert 63 * 42 + 2 * 12 - 2602 == 68 > 56
    print("PASS algebraization contacts: f q=(81,85), g q=(82,88,86)")
    print("PASS primitive repair margins: f >=63, g >=64, all beyond D23")


def check_growth_law() -> None:
    # In six successive absolute tail levels there are four ordinary
    # P/G tails at every level and two extra G0 tails at even levels.
    for lo in range(38, 80):
        count = sum(4 + (2 if m % 2 == 0 else 0)
                    for m in range(lo, lo + 6))
        assert count == 30

    # Exact C6 grading: Row_k eta^q requires k = 2(q+1) mod 6, so
    # every odd row is absent.  This check deliberately makes no
    # all-depth eta-degree claim: off-direction eta*t^20 insertions can
    # raise the degree later in the pure-y window.
    for k in range(6, 42):
        allowed = [q for q in range(190)
                   if (k - 2 * (q + 1)) % 6 == 0]
        if k % 2:
            assert not allowed
        else:
            assert allowed
    print("PASS six-slot census: 30 new tails; exact odd-row/grading law")

    # Replay the exact supports already banked in the transient D21/D23
    # states when they are available.  This is an optional guard only.
    for path in (Path("/tmp/directionb_tails_D21.pkl"),
                 Path("/tmp/directionb_tails_D23.pkl")):
        if not path.exists():
            continue
        import r1_experiment  # noqa: F401 -- needed by pickle
        state = pickle.loads(path.read_bytes())
        for k, comp in state["byk"].items():
            assert k % 2 == 0
            assert all((k - 2 * (q + 1)) % 6 == 0 for q in comp)
        print(f"PASS banked grading replay: {path.name}")


def check_row24() -> None:
    from fractions import Fraction as Fr
    import directionb_strike as D
    import directionb_window as W
    import r1_experiment as R

    D.fresh_registry()
    R.VDEG_CAP = 25
    R.build_generators(57)             # dry registry/name pass
    front = tuple(v["name"] for v in R.VARS
                  if v["name"][:2] in ("tf", "tg")
                  and int(v["name"].rsplit("_", 1)[1]) in (51, 56))
    want_front = ("tf1_51", "tf1_56", "tf2_51", "tf2_56",
                  "tg1_51", "tg1_56", "tg2_51", "tg2_56",
                  "tg01_56", "tg02_56")
    assert front == want_front, front
    _orbs, jf, jg = D.build_frozen(25, front, "ALGKILL")
    rows = D.jrows(jf, jg, 25)
    comp = {q: v for (q, k), v in rows.items() if k == 24 and v}
    assert sorted(comp) == list(range(2, 27, 3))
    assert not any(v for (q, k), v in rows.items() if k in (21, 23))
    vids = {v["name"]: i for i, v in enumerate(R.VARS)}

    # Raw exact digest (all 9 eta rows x 10 first-occurrence columns).
    serial = []
    for q in sorted(comp):
        for name in front:
            ring = comp[q].get((vids[name],), {})
            serial.append((q, name, tuple(sorted(
                (rk, repr(c)) for rk, c in ring.items()))))
    payload = repr(serial).encode()
    assert len(serial) == 90 and len(payload) == 10800
    digest = hashlib.sha256(payload).hexdigest()
    assert digest == \
        "ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29", \
        (digest, len(payload))

    # Exact rank over the etale algebra on all sign branches and hostile
    # nonzero pole-scale fibers.  First occurrence makes this the full
    # symbol: no older free can enter a frontier coefficient.
    ranks = []
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        for w1, w2 in ((Fr(1), Fr(1)), (Fr(2), Fr(3)),
                       (Fr(1, 5), Fr(7))):
            erows = []
            for q in sorted(comp):
                row = {}
                for col, name in enumerate(front):
                    c = W.ring_to_E(comp[q].get((vids[name],), {}),
                                    s1, s2, w1, w2)
                    if c:
                        row[col] = c
                erows.append(row)
            rank, piv, _ech, leftover = W.erank_units(erows, len(front))
            assert rank == 4 and not leftover
            assert [front[c] for c in piv] == \
                ["tf1_51", "tf1_56", "tf2_51", "tf2_56"]
            ranks.append(rank)
    assert ranks == [4] * 12
    print("PASS Row24: eta={2,5,...,26}, exact frontier rank 4/10 (12 fibers)")
    print("PASS Row24 digest:", digest)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--row24", action="store_true",
                    help="also rebuild the exact D25 Row-24 symbol")
    args = ap.parse_args()
    check_contacts()
    check_growth_law()
    if args.row24:
        check_row24()


if __name__ == "__main__":
    main()
