import sympy as sp, time, sys
from cell import build_cell
def decide(tag,e,U,**kw):
    t=time.time(); eqs,V,info=build_cell(e,U,**kw)
    gb=sp.groebner(eqs,*V,order='grevlex')
    unit=(list(gb.exprs)==[sp.Integer(1)])
    print("  %-24s cell(%d,%2d) eqs=%3d vars=%3d  UNIT(EMPTY)=%-5s  %.1fs"
          %(tag,e,U,len(eqs),len(V),unit,time.time()-t)); sys.stdout.flush()
    return unit
decide("full",1,3)
decide("wall NOT imposed",1,3,wall=False)
for k in ['EQ1','EQ2','EQ3','EQ4','E0','T1']:
    decide("NEG control drop %s"%k,1,3,drop={k})
