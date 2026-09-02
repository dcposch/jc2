import sympy as sp, time, sys
from cell import build_cell
def decide(tag,e,U,**kw):
    t=time.time(); eqs,V,info=build_cell(e,U,**kw)
    try:
        gb=sp.groebner(eqs,*V,order='grevlex')
        unit=(list(gb.exprs)==[sp.Integer(1)])
        print("  %-22s cell(%d,%d) eqs=%d vars=%d  UNIT=%s   %.1fs"%(tag,e,U,len(eqs),len(V),unit,time.time()-t)); sys.stdout.flush()
    except Exception as ex:
        print("  %-22s cell(%d,%d) FAILED %s"%(tag,e,U,ex)); sys.stdout.flush()
import argparse
p=argparse.ArgumentParser(); p.add_argument('which'); A=p.parse_args()
if A.which=='a': decide("full a=b=1",1,3)
if A.which=='b': decide("full a,b symbolic",1,3,params=True)
if A.which=='c': decide("wall NOT imposed",1,3,wall=False)
if A.which=='d':
    for k in ['EQ1','EQ2','EQ3','EQ4','E0','T1']:
        decide("NEG drop %s"%k,1,3,drop={k})
