"""v3 probe: torus-normalized system -> cascade pre-reduction -> msolve core."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from jc import SystemA
from emit import CASES, FIX

def build_core(name):
    from reduce import Cascade
    spec = CASES[name]
    S = SystemA(name + "_v3", spec["cornersP"], spec["cornersQ"], spec["rhs"],
                nonvanish="nonorigin", fix_ones=FIX[name])
    C = Cascade(S)
    status = C.run()
    print(f"{name}: {status}; {C.stats()}")
    return C, status

if __name__ == "__main__":
    names = sys.argv[1:] or ["reg_9_24_c3"]
    outdir = os.path.join(os.path.dirname(__file__), "..", "systems")
    for name in names:
        C, status = build_core(name)
        if status == "EMPTY":
            print(f"  -> {name} discarded at cascade level (no solver needed)")
            continue
        for p in (65521, 1048573):
            nv, ne = C.write_msolve(os.path.join(outdir, f"{name}_v3.p{p}.ms"), p)
        nv, ne = C.write_msolve(os.path.join(outdir, f"{name}_v3.q.ms"), 0)
        print(f"  -> emitted core: {nv} vars, {ne} eqs")
