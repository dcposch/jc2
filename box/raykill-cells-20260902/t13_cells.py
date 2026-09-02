import sympy as sp, time, sys
from cell import build_cell
def decide(e,U,**kw):
    t=time.time(); eqs,V,info=build_cell(e,U,**kw)
    gb=sp.groebner(eqs,*V,order='grevlex')
    unit = (list(gb.exprs)==[sp.Integer(1)])
    return unit, len(eqs), len(V), time.time()-t
print("--- (1,3) controls ---")
print(" full, a=b=1        :", decide(1,3))
print(" full, a,b symbolic :", decide(1,3,params=True))
print(" wall NOT imposed   :", decide(1,3,wall=False))
print(" NEG ctrl drop EQ3  :", decide(1,3,drop={'EQ3'}))
print(" NEG ctrl drop EQ2  :", decide(1,3,drop={'EQ2'}))
print(" NEG ctrl drop EQ4  :", decide(1,3,drop={'EQ4'}))
print(" NEG ctrl drop E0   :", decide(1,3,drop={'E0'}))
print(" NEG ctrl drop T1   :", decide(1,3,drop={'T1'}))
