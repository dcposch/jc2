"""Benchmark: Cascade3 (and generation) under JC_BACKEND=python vs flint.

Usage:  python3 cases/bench_fastcoef.py <case> <backend> [--gen-only]
  <case>    reg_9_24_c3 | open_8_28_c2 | open_8_28_c1 | moh_48_64
  <backend> python | flint

Prints one summary line:
  BENCH case backend gen=..s cascade=..s status=.. elims=N core="stats"
Reduced cases are built torus-normalized (emit.FIX), matching probe3/parity.
moh_48_64 is the unreduced (48,64) family pair of cases/unreduced.py.
"""
import os
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "lib"))
sys.path.insert(0, os.path.join(BASE, "cases"))

def main():
    name, be = sys.argv[1], sys.argv[2]
    gen_only = "--gen-only" in sys.argv
    os.environ["JC_BACKEND"] = be
    from jc import SystemA
    from reduce3 import Cascade3

    t0 = time.time()
    if name == "moh_48_64":
        mm, nn, a, b = 3, 4, 4, 12
        rP = [(0, 0), (mm * a, 0), (mm * a, mm * b), (0, mm * b)]
        rQ = [(0, 0), (nn * a, 0), (nn * a, nn * b), (0, nn * b)]
        S = SystemA(name, rP, rQ, (0, 0), nonvanish="nonorigin",
                    fix_ones=[("P", (mm * a, mm * b))])
    else:
        from emit import CASES, FIX
        spec = CASES[name]
        S = SystemA(name, spec["cornersP"], spec["cornersQ"], spec["rhs"],
                    nonvanish="nonorigin", fix_ones=FIX[name])
    tg = time.time() - t0
    print(f"# {name} {be}: generated ({S.stats()}) in {tg:.1f}s", flush=True)
    if gen_only:
        print(f"BENCH {name} {be} gen={tg:.1f}s cascade=SKIPPED", flush=True)
        return
    t0 = time.time()
    C = Cascade3(S)
    st = C.run(verbose=("-v" in sys.argv))
    tc = time.time() - t0
    print(f"BENCH {name} {be} gen={tg:.1f}s cascade={tc:.1f}s status={st} "
          f"elims={len(C.elim)} core=\"{C.stats()}\"", flush=True)

if __name__ == "__main__":
    main()
