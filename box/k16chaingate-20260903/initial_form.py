#!/usr/bin/env python3
"""Initial-form degeneration of I_{t,+} at t=4,5 for R={q_{t-1,0}, b3}.

w = 0 on R, 1 off R; in_w = terms of minimal w-degree.  Exact std+dim over
Q with H_t adjoined as a generator.  Coefficient field Q, dp order, generator
order = record residual variables then Y.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_record import load, qsym  # noqa: E402
from sing_util import clear_poly, to_sing, write_and_run  # noqa: E402


def main() -> None:
    for tv in (4, 5):
        D = load(tv)
        y, b3, H, vs = D["y"], D["b3"], D["H"], D["variables"]
        Q = qsym(D, tv - 1)
        Rset = {Q, b3}
        wv = [0 if v in Rset else 1 for v in vs]
        print("=== t=%d R={%s,b3} vars=%s w=%s ===" % (tv, Q, vs, wv))
        gens = []
        degrees = []
        for k in range(1, 2 * tv):
            e = sp.expand(D["rows"].get(k, 0))
            if e == 0:
                continue
            P = sp.Poly(e, *vs)
            best = min(sum(a * w for a, w in zip(mon, wv)) for mon, _ in P.terms())
            ini = sum(
                co * sp.prod([v**a for v, a in zip(vs, mon)])
                for mon, co in P.terms()
                if sum(a * w for a, w in zip(mon, wv)) == best
            )
            gens.append(sp.expand(ini))
            degrees.append((k, best))
        print("   w-degree per band:", ", ".join("k%d:%d" % p for p in degrees))
        allv = list(vs) + [y]
        body = [to_sing(clear_poly(g, allv), y) for g in gens]
        body.append(to_sing(clear_poly(H, allv), y))
        write_and_run(
            "initial_t%d_r1" % tv,
            [str(v) for v in vs] + ["Y"],
            body,
            timeout=600,
        )


if __name__ == "__main__":
    main()
