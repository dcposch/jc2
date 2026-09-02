import sympy as sp, time, sys
from cell import build_cell
def decide(tag,e,U,**kw):
    t=time.time(); eqs,V,info=build_cell(e,U,**kw)
    gb=sp.groebner(eqs,*V,order='grevlex')
    unit=(list(gb.exprs)==[sp.Integer(1)])
    print("  %-30s cell(%d,%2d) eqs=%3d vars=%3d  UNIT(EMPTY)=%-5s  %.1fs"
          %(tag,e,U,len(eqs),len(V),unit,time.time()-t)); sys.stdout.flush()
import sys
w=sys.argv[1]
if w=='pos':
    decide("POS ctrl: only T1+E0",1,3,drop={'EQ1','EQ2','EQ3','EQ4'})
    decide("POS ctrl: only EQ3",1,3,drop={'EQ1','EQ2','EQ4','E0','T1'})
    decide("POS ctrl: only EQ1+EQ4",1,3,drop={'EQ2','EQ3','E0','T1'})
    decide("POS ctrl: only EQ2+T1+E0",1,3,drop={'EQ1','EQ3','EQ4'})
if w=='15':  decide("full",1,5,normS=True)
if w=='17':  decide("full",1,7,normS=True)
if w=='28':  decide("full",2,8,normS=True)
if w=='26':  decide("full",2,6)
if w=='39':  decide("full",3,9)
