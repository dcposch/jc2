import sys, time
sys.path.insert(0, "../lib"); sys.path.insert(0, ".")
sys.path.insert(0, "lib"); sys.path.insert(0, "cases")
from jc import SystemA
from emit import CASES, FIX
from reduce3 import Cascade3
from chartelim import two_chart, leaf_to_msolve

DIRS = [(2,1),(3,1),(1,1),(4,1),(1,2),(3,2),(5,2),(1,0),(2,3),(0,1)]
for name in ["reg_9_27", "reg_7_21"]:
    spec = CASES[name]
    best = None
    for d in DIRS:
        S = SystemA(name, spec["cornersP"], spec["cornersQ"], spec["rhs"],
                    nonvanish="nonorigin", fix_ones=FIX[name])
        C = Cascade3(S, level_dir=d)
        t0 = time.time()
        st = C.run()
        dt = time.time() - t0
        nb = len(C.bvars)
        mx = max((len(c) for c in C.eqs), default=0)
        print(f"{name} dir={d}: {st}, {len(C.alive)} vars ({nb} b left), "
              f"maxterms {mx} ({dt:.0f}s)", flush=True)
        score = (st != "reduced", nb, len(C.alive), mx)
        if best is None or score < best[0]:
            best = (score, d, C)
    _, d, C = best
    print(f"{name}: BEST dir={d}", flush=True)
    if best[0][0] is False and len(C.bvars) <= 6:
        G, Cm, info = two_chart(C)
        for tag, L in (("G", G), ("C", Cm)):
            nv, ne = leaf_to_msolve(L, f"systems/{name}_chart{tag}.p65521.ms", 65521)
            print(f"  {name}_chart{tag}: {nv} vars, {ne} eqs", flush=True)
