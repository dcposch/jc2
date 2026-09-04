#!/usr/bin/env python3
"""Remaining r=1 terminal scalars A3,A4,A6,A7,A8 (not needed for (3.6))."""
from __future__ import annotations

import json
import time
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sq_engine as S  # noqa: E402
from sq_engine import E, b3, c1, c2, c3, c4, d, red, spine, t, x  # noqa: E402
from qplane_core import dnorm, is_high, roots_1_40  # noqa: E402


def main():
    S.set_r(1)
    core = json.loads((HERE / "qplane_core_r1.json").read_text())
    T0 = time.time()
    O = spine(has_b1=True)
    print("# spine %.1fs" % (time.time() - T0), flush=True)
    SOL = {
        c1: sp.sympify(core["c"]["c1"], locals={"d": d, "t": t}),
        c2: sp.sympify(core["c"]["c2"], locals={"d": d, "t": t}),
        c3: sp.sympify(core["c"]["c3"], locals={"d": d, "t": t}),
        c4: sp.sympify(core["c"]["c4"], locals={"d": d, "t": t}),
    }
    want = {
        "A3": (E(1, 0, 2), (2, 1)),  # t+2, x^2 b3
        "A4": (E(1, 0, 0), (1, 2)),  # t, x b3^2
        "A6": (E(0, 0, 5), (4, 0)),  # 5, x^4
        "A7": (E(0, 0, 3), (3, 1)),  # 3, x^3 b3
        "A8": (E(0, 0, 1), (2, 2)),  # 1, x^2 b3^2
    }
    Phi = O["Phi"]
    rows = {}
    for name, (key, mon) in want.items():
        t1 = time.time()
        v = red(Phi[key].subs(SOL))
        P = sp.Poly(v, x, b3)
        terms = {m: red(c) for m, c in P.terms()}
        extra = [m for m in terms if m != mon]
        co = terms[mon]
        Nn, den = dnorm(co)
        Nf, rts = roots_1_40(Nn)
        rows[name] = {"N": str(Nf), "roots": rts, "extra": str(extra), "den": str(den)}
        print("%s extra=%s roots=%s N=%s (%.1fs)" % (name, extra, rts, Nf, time.time() - t1), flush=True)
    (HERE / "qplane_rest_r1.json").write_text(json.dumps(rows, indent=2, sort_keys=True))
    print("# elapsed %.1fs" % (time.time() - T0), flush=True)


if __name__ == "__main__":
    main()
