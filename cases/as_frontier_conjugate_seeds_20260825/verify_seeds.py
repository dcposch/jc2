#!/usr/bin/env python3
"""Exact controls for two tame right-composed AS max-y=12 residue seeds."""

from collections import Counter, defaultdict
from sympy import Poly, expand, symbols

x, y, s, t = symbols("x y s t")


def jacdet(f, g, a=x, b=y):
    return expand(f.diff(a) * g.diff(b) - f.diff(b) * g.diff(a))


def mod3(poly):
    return Poly(expand(poly), x, y, modulus=3).as_expr()


def eval3(poly, a, b):
    return int(Poly(poly, x, y, modulus=3).eval({x: a, y: b})) % 3


def check_seed(name, m, k, orient):
    u = x + y**m
    v = y + u**k
    bdet = jacdet(u, v)
    assert bdet == 1

    # Displayed inverse in independent target variables s,t.
    iy = t - s**k
    ix = s - iy**m
    assert expand(ix.subs({s: u, t: v}, simultaneous=True) - x) == 0
    assert expand(iy.subs({s: u, t: v}, simultaneous=True) - y) == 0
    assert expand(u.subs({x: ix, y: iy}, simultaneous=True) - s) == 0
    assert expand(v.subs({x: ix, y: iy}, simultaneous=True) - t) == 0

    raw_p = expand(u - u**3)
    raw_q = expand(v)
    assert expand(jacdet(raw_p, raw_q) - (1 - 3 * u**2)) == 0

    if orient == "raw":
        p, q = raw_p, raw_q
    elif orient == "swap_sign":
        p, q = raw_q, expand(-raw_p)
    else:
        raise AssertionError(orient)

    dyp = Poly(p, y).degree()
    dyq = Poly(q, y).degree()
    tdp = Poly(p, x, y).total_degree()
    tdq = Poly(q, x, y).total_degree()
    lcp = Poly(p, y).LC()
    lcq = Poly(q, y).LC()
    assert (name, dyp, dyq) in (("G9", 9, 12), ("G8", 8, 12))
    assert lcp in (-1, 1) and lcq in (-1, 1)
    assert mod3(jacdet(p, q) - 1) == 0

    fibres = defaultdict(list)
    for a in range(3):
        for b in range(3):
            fibres[(eval3(p, a, b), eval3(q, a, b))].append((a, b))
    sizes = Counter(len(points) for points in fibres.values())
    assert sum(len(points) for points in fibres.values()) == 9
    assert max(len(points) for points in fibres.values()) == 3
    assert len(fibres) == 3
    assert sizes == Counter({3: 3})

    print(
        f"{name}: m={m} k={k} orient={orient} "
        f"deg_y=({dyp},{dyq}) total_deg=({tdp},{tdq}) "
        f"lead_y=({lcp},{lcq}) detB={bdet} "
        f"det_raw=1-3*u^2 fibres={sorted(sizes.items())}"
    )


check_seed("G9", 3, 4, "raw")
check_seed("G8", 4, 2, "swap_sign")
print("PASS-AS-MAX12-RIGHT-COMPOSED-SEEDS")
print(
    "scope=finite-field residue seeds only; no mod9 lift, all-depth branch, "
    "counterexample, Q8/TD6 landing, maximum12 theorem, or JC2"
)
