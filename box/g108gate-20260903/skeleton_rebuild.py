#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


INPUT = Path("/tmp/jc2-lane.66ch7X/inputs/moh_skeleton_full.py")


def load_module():
    spec = importlib.util.spec_from_file_location("moh_skeleton_full_frozen", INPUT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {INPUT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frac(value):
    return str(value)


def main() -> None:
    moh = load_module()
    skel = moh.Skel(108, 72, [81, 106], {2: 7, 3: 7})
    census_hits = [
        {"m": m, "Ms": list(Ms), "V": {str(k): v for k, v in sorted(V.items())}}
        for (m, Ms, V) in moh.census(108, Kmin=16, full=True)
        if m == 72 and tuple(Ms) == (81, 106) and V == {2: 7, 3: 7}
    ]
    payload = {
        "source": str(INPUT),
        "row": {
            "n": skel.n,
            "m": skel.m,
            "M": [skel.M[i] for i in range(1, skel.s + 1)],
            "d": [skel.d[i] for i in range(1, skel.s + 2)],
            "V": [skel.V[i] for i in range(2, skel.s + 1)],
            "s": skel.s,
            "K": skel.K,
            "e": skel.e,
            "dd": skel.dd,
            "u": frac(skel.u),
            "delta": {str(i): frac(skel.delta[i]) for i in range(1, skel.s + 1)},
            "A": {str(i): skel.A(i) for i in range(1, skel.s)},
            "L": {str(i): skel.L(i) for i in range(1, skel.s)},
            "div9": {
                str(i): {
                    "TRI": skel.div9(i)[0],
                    "SQ": skel.div9(i)[1],
                    "A": skel.div9(i)[2],
                    "Q": skel.div9(i)[3],
                }
                for i in range(2, skel.s)
            },
            "cond1011": {
                str(i): {
                    "ok": skel.cond1011(i)[0],
                    "by10": skel.cond1011(i)[1],
                    "by11": skel.cond1011(i)[2],
                }
                for i in range(2, skel.s)
            },
            "cond1213": {
                "ok": skel.cond1213()[0],
                "by12": skel.cond1213()[1],
                "by13": skel.cond1213()[2],
            },
            "windows_ok": skel.windows_ok(),
            "full_ok": skel.full_ok(),
            "q": frac(skel.q()),
        },
        "census_full_hits": census_hits,
        "census_full_hit_count": len(census_hits),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
