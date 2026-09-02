import sympy as sp, time, random
from cell import build_cell
random.seed(7)
eqs,V,info = build_cell(1,3)
tt=[v for v in V if str(v)=='tt'][0]
# plant a random rational point; shift every generator so the point is a zero
pt={}
for v in V:
    if v is tt: continue
    pt[v]=sp.Rational(random.randint(-4,4) or 1, random.randint(1,3))
pt[[v for v in V if str(v)=='kappa'][0]]=sp.Rational(3,2)
for nm in ['S2','Q3','R2']:
    w=[v for v in V if str(v)==nm]
    if w: pt[w[0]]=sp.Rational(random.randint(1,4))
sat=[e for e in eqs if tt in e.free_symbols][0]
rest=[e for e in eqs if tt not in e.free_symbols]
lead=sp.prod([pt[v] for v in V if str(v) in ('S2','Q3','R2','kappa')])
pt[tt]=1/lead
shift=[sp.expand(e - e.subs(pt)) for e in rest]+[sp.expand(sat)]
assert all(sp.simplify(g.subs(pt))==0 for g in shift), "planted point is not a zero"
print("planted control: %d generators, %d vars, planted point verified a zero"%(len(shift),len(V)))
t=time.time(); gb=sp.groebner(shift,*V,order='grevlex')
print("  PLANTED ideal is unit? ", list(gb.exprs)==[sp.Integer(1)], " (%.1fs)"%(time.time()-t))
t=time.time(); gb2=sp.groebner(eqs,*V,order='grevlex')
print("  TRUE    ideal is unit? ", list(gb2.exprs)==[sp.Integer(1)], " (%.1fs)"%(time.time()-t))
