"""Family-farm prerequisite: Generator A on UNREDUCED standard (m,n)-pair data.
Support(P) in m*rect[(0,0),(a,0),(a,b),(0,b)], Support(Q) in n*rect, corners
m(a,b), n(a,b) attained, [P,Q] = 1 (alpha-scaling absorbs the constant).
Torus left after bracket normalization: x->Lx, y->y/L -> fix ONE corner.
Measure: system size, cascade behavior under a swell cap.
"""
import sys, time
sys.path.insert(0, "../lib"); sys.path.insert(0, "lib")
from jc import SystemA
from reduce3 import Cascade3

def family(mm, nn, a, b):
    rectP = [(0,0),(mm*a,0),(mm*a,mm*b),(0,mm*b)]
    rectQ = [(0,0),(nn*a,0),(nn*a,nn*b),(0,nn*b)]
    return rectP, rectQ

for (mm, nn, a, b, tag) in [(3, 4, 4, 12, "moh_48_64")]:
    rP, rQ = family(mm, nn, a, b)
    t0 = time.time()
    S = SystemA(tag, rP, rQ, (0, 0), nonvanish="nonorigin",
                fix_ones=[("P", (mm*a, mm*b))])
    print(f"{tag}: {S.stats()} gen={time.time()-t0:.0f}s", flush=True)
    t0 = time.time()
    C = Cascade3(S, level_dir=(2, 1))
    st = C.run()
    print(f"{tag}: cascade {st}; {C.stats()} ({time.time()-t0:.0f}s)", flush=True)
