"""Exact normalized degree 2/3 UF classification, no charged code or ray data."""
import sympy as s,json,pathlib
x,a,B,e=s.symbols('x a B e')
records=[]
for m,leadings in [(2,[(-3+2*s.sqrt(6))/20,(-3-2*s.sqrt(6))/20]),(3,[s.Rational(-1,4),s.Rational(1,12)])]:
 L=-1+x**m+(a*x*x if m==3 else 0)
 G=s.Rational(3,2)*L*(L+1)-B*x
 R=s.Rational(3,16)*L**2*(L*(L+2)-4*B*x)-e*x*x*(L/2+B*x)
 for lc in leadings:
  assert s.simplify((4*m-3)*lc**2+s.Rational(3,2)*lc-s.Rational(3,16))==0
  P=lc*x**(2*m)-s.Rational(1,4)
  for k in range(4*m-1,2*m,-1):
   q=s.Symbol('q');P+=q*x**(k-2*m)
   f=s.Poly(s.expand(x*s.diff(P**2,x)-3*P**2+G*P-R),x).coeff_monomial(x**k)
   v=s.radsimp(s.solve(f,q)[0]);P=P.subs(q,v)
  jets=[s.diff(P,x).subs(x,0)+B,s.diff(P,x,2).subs(x,0)/2-e]
  subst=s.solve(jets,[B,e],dict=True)[0]
  F=s.Poly(s.expand(x*s.diff(P**2,x)-3*P**2+G*P-R),x)
  residual={str(k):str(c) for k in range(4*m+1) if (c:=s.factor(s.simplify(F.coeff_monomial(x**k).subs(subst))))!=0}
  row={'degree_L':m,'leading_P':str(lc),'B':str(s.factor(subst[B])),'eta':str(s.factor(subst[e])),'residual_coefficients':residual}
  if m==2:
   assert set(residual)=={'4'} and s.simplify(s.sympify(residual['4']))!=0
   row['conclusion']='No polynomial solution of exact degree 2.'
  else:
   equations=jets+[c for c in F.all_coeffs() if c]
   gb=list(s.groebner(equations,B,e,a,order='lex'))
   expected=[B,e-s.Rational(9,10)*a,a*a] if lc==-s.Rational(1,4) else [s.Integer(1)]
   assert gb==expected
   row['groebner_Q_B_eta_a_lex']=list(map(str,gb))
   row['conclusion']='Reduced locus B=eta=a=0.' if lc==-s.Rational(1,4) else 'No polynomial solution.'
  records.append(row)
z=s.symbols('z')
f=48281373*z*z-392411136*z-49433741312;g=1986398181*z*z-16122815232*z-3806398081024
resultant=s.resultant(f,g,z);assert resultant!=0
out={'status':'ALL_PASS','field':'characteristic zero; algebraic closure for normalization','normalization':'x scaling makes leading L=1; L(0)=-1, L1=0, P0=-1/4, P1=-B,P2=eta','cases':records,'positive_degree3_resultant_absolute_factorization':str(s.factorint(abs(int(resultant)))),'uniform_low_degree_conclusion':'All solutions with deg L<=3 are L=-1,P=-1/4-Bx or L=-1+a x^3,P=-L^2/4 (the two families meet at a=B=0).'}
p=pathlib.Path('box/k16-utac-20260906/theory_low_degree.json');p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
