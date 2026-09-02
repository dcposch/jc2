cd /tmp/raykill
python3 - <<'PY'
import sympy as sp, time, sys
from cell import build_cell
for (e,U) in [(1,5),(2,6),(3,9),(1,7),(2,8),(4,12),(1,9),(3,11)]:
    t=time.time()
    try:
        eqs,V,info=build_cell(e,U)               # normS deliberately OFF
        gb=sp.groebner(eqs,*V,order='grevlex')
        unit=(list(gb.exprs)==[sp.Integer(1)])
        print("cell(%d,%2d) eqs=%3d vars=%3d  UNIT(EMPTY)=%-5s  %.1fs"%(e,U,len(eqs),len(V),unit,time.time()-t))
    except Exception as ex:
        print("cell(%d,%2d) ERROR %s"%(e,U,ex))
    sys.stdout.flush()
PY
