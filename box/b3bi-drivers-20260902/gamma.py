import sympy as sp
t,x,y=sp.symbols('t x y')
X=t**2; Y=t**3*(t**2-1)
f=sp.expand(y**2-x**3*(x-1)**2)
print("param satisfies eq:", sp.simplify(f.subs({x:X,y:Y})))
F=sp.Poly(f,x,y); print("total degree:",sp.total_degree(f), " irreducible:",len(sp.factor_list(f)[1])==1)
# affine singular locus
sols=sp.solve([f,sp.diff(f,x),sp.diff(f,y)],[x,y],dict=True); print("affine sings:",sols)
# cusp at (0,0): orders of x,y in t at t=0
print("t=0: ord x =",sp.Poly(X,t).monoms()[-1][0]," ord y =",sp.Poly(sp.expand(Y),t).monoms()[-1][0])
# node at (1,0): t=+-1, tangents
for t0 in (1,-1):
    dx=sp.diff(X,t).subs(t,t0); dy=sp.diff(Y,t).subs(t,t0); print("  branch t=%s tangent dy/dx = %s"%(t0,sp.nsimplify(dy/dx)))
# places at infinity: poles of (X,Y) -> only t=infinity
print("poles of param (affine t):", sp.solve(sp.denom(sp.together(X)),t), sp.solve(sp.denom(sp.together(Y)),t))
# delta budget
pa=(5-1)*(5-2)//2
print("p_a =",pa,"  delta_cusp=1 delta_node=1  => delta_infty =",pa-2)
