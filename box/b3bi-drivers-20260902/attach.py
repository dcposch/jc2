import sympy as sp
X2,Zp=sp.symbols('X2 Zp')
# after three blowups of F(x,y)=(x, x y^2) at the source point [0:1:0]:
# chart (X2,Zp): u = X2^2*Zp , v = 1/Zp ; target chart at p=(u=0,v=inf):
#   U' = u/v , V' = 1/v
u=X2**2*Zp; v=1/Zp
Up=sp.simplify(u/v); Vp=sp.simplify(1/v)
print("U' =",Up," V' =",Vp)
print("dicritical g~ = {X2=0}: image (U',V') =",(Up.subs(X2,0), sp.simplify(Vp)), " -> dominates g={U'=0}")
print("neighbour B = {Zp=0}: image (U',V') =",(sp.limit(Up,Zp,0), sp.limit(Vp,Zp,0)), " -> CONTRACTED to p=(0,0)")
print("local exponent matrix of (U',V') in (X2,Zp):", sp.Matrix([[2,2],[0,1]]),
      " det =", sp.Matrix([[2,2],[0,1]]).det(), "(F finite of local degree 2 at p~ = s*mu = 1*2)")
