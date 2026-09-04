#!/usr/bin/env python3
"""Q-PLANE on charged exact records t=3,4,5.

S = {b4 = q_{2,0} = ... = q_{t-2,0} = 0}, residual (q_{t-1,0}, b3).
Ring: Q[q_{t-1,0}, b3, Y] with H_t(Y) adjoined (finite fibre; dim unchanged).
Map: names as in the JSON; y = q_{2t+1,1}; coefficients reduced modulo H_t.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_record import load, qsym  # noqa: E402
from sing_util import clear_poly, to_sing, write_and_run  # noqa: E402

HERE = Path(__file__).resolve().parent


def A_red(co, y, H):
    Hp = sp.Poly(H, y)
    e = sp.together(sp.expand(co))
    n, de = sp.fraction(e)
    n = sp.Poly(sp.expand(n), y).rem(Hp).as_expr()
    de = sp.expand(de)
    if de.has(y):
        inv = sp.invert(sp.Poly(de, y), Hp).as_expr()
        n = sp.expand(n * inv)
        de = 1
    return sp.expand(sp.Poly(sp.expand(n / de), y).rem(Hp).as_expr())


def main() -> None:
    for tv in (3, 4, 5):
        D = load(tv)
        y, b3, H = D["y"], D["b3"], D["H"]
        x = qsym(D, tv - 1)
        killed = {D["b4"]}
        for j in range(2, tv - 1):
            killed.add(qsym(D, j))
        zero = {v: 0 for v in killed}
        print("=== t=%d S kills %s residual (%s, b3) ===" % (tv, sorted(map(str, killed)), x))
        gens = []
        live = []
        for k in range(1, 2 * tv):
            e = sp.expand(D["rows"].get(k, 0).subs(zero))
            if e == 0:
                continue
            gens.append(clear_poly(e, [x, b3, y]))
            P = sp.Poly(e, x, b3)
            mons = []
            for mon, co in P.terms():
                co = A_red(co, y, H)
                if co == 0:
                    continue
                N = sp.resultant(sp.Poly(H, y), sp.Poly(sp.expand(co), y))
                N = sp.factor(sp.expand(N))
                mons.append("x^%d b3^%d Res=%s (zero=%s)" % (mon[0], mon[1], N, N == 0))
            live.append("k=%d : %s" % (k, "; ".join(mons) if mons else "0 after A_t reduction"))
        for line in live:
            print("   ", line)
        body = [to_sing(g, y) for g in gens] + [to_sing(clear_poly(H, [x, b3, y]), y)]
        write_and_run(
            "plane_t%d_r1" % tv,
            [str(x), "b3", "Y"],
            body,
            timeout=600,
        )


if __name__ == "__main__":
    main()
