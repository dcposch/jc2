import sympy as s
x,B,e=s.symbols('x B e'); L=-1+x*x
G=s.Rational(3,2)*L*(L+1)-B*x
R=s.Rational(3,16)*L**2*(L*(L+2)-4*B*x)-e*x*x*(L/2+B*x)
for lc in [(-3+2*s.sqrt(6))/20,(-3-2*s.sqrt(6))/20]:
 P=lc*x**4-s.Rational(1,4)
 for k in [7,6,5]:
  q=s.Symbol('q'+str(k-4));P+=q*x**(k-4)
  f=s.Poly(s.expand(x*s.diff(P**2,x)-3*P**2+G*P-R),x).coeff_monomial(x**k)
  P=P.subs(q,s.radsimp(s.solve(f,q)[0]))
 e0=s.simplify(s.diff(P,x,2).subs(x,0)/2)
 f1=s.factor(s.diff(P,x).subs(x,0)+B)
 b0=s.solve(f1,B)[0]
 Pe=s.simplify(P.subs(B,b0)); Fe=s.simplify((x*s.diff(Pe**2,x)-3*Pe**2+G.subs(B,b0)*Pe-R.subs({B:b0,e:e0})).expand())
 print('lc',lc,'P',P,'eta',e0,'Bjet',f1,'B',b0,'residual',Fe,flush=True)
