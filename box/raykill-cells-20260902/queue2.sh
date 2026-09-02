cd /tmp/raykill
python3 - <<'PY'
import sympy as sp, time, sys
from cellp import build_primed
for (e,U) in [(1,5),(1,7),(2,8),(1,9),(2,10),(3,11),(4,14)]:
    t=time.time()
    try:
        eqs,V,info=build_primed(e,U)
        gb=sp.groebner(eqs,*V,order='grevlex')
        unit=(list(gb.exprs)==[sp.Integer(1)])
        print("PRIMED cell(%d,%2d) eqs=%3d vars=%3d  UNIT(EMPTY)=%-5s  %.1fs"%(e,U,len(eqs),len(V),unit,time.time()-t))
    except Exception as ex:
        print("PRIMED cell(%d,%2d) ERROR %s"%(e,U,ex))
    sys.stdout.flush()
PY
