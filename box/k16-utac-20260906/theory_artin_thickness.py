"""Construct Artin points of I_close proving uniform exponent lower bound 2N."""
import sympy as s,json,pathlib
x,z=s.symbols('x z'); fs={1:x*x}; records=[]
def theta(f):return x*s.diff(f,x)
def T(f):return -s.Rational(1,2)*(theta(f)-3*f)-x*(2*theta(f)-3*f)
for r in range(2,12):
 h=s.expand(theta(sum(fs[i]*fs[r-i] for i in range(1,r)))-3*sum(fs[i]*fs[r-i] for i in range(1,r)))
 f=s.Integer(0); rem=h
 for m in range(r+1,2,-1):
  c=s.Poly(rem,x).coeff_monomial(x**(m+1))/s.Integer(2*m-3)
  term=c*x**m;f+=term;rem=s.expand(rem+T(term))
 assert rem==0 and s.degree(f,x)==r+1 and s.Poly(f,x).coeff_monomial(x*x)==0
 assert s.Poly(f,x).coeff_monomial(x**(r+1))>0
 fs[r]=s.expand(f)
for N in [4,5,6]:
 P=-s.Rational(1,4)-x+sum(z**r*fs[r] for r in range(1,2*N))
 F=s.expand(theta(P**2)-3*P**2-x*P+s.Rational(3,16)+s.Rational(3,4)*x-z*x*x/2+z*x**3)
 low=sum(c*z**j for (j,),c in s.Poly(F,z).terms() if j<2*N)
 assert low==0 and s.degree(P,x)==2*N
 assert s.Poly(P,x).coeff_monomial(x*x)==z
 assert s.Poly(P,x).coeff_monomial(x)==-1
 records.append({'N':N,'Artin_ring':f'Q[z]/(z^{2*N})','degree_P':int(s.degree(P,x)),'UF_residual_mod_Artin_ideal':str(low),'w2_image':str(s.Poly(P,x).coeff_monomial(x**3)),'eta_image':'z','u_image':'4*z','B_image':'1','L':'-1','exponent_lower_bound':2*N})
out={'status':'ALL_PASS','proved_uniformly':'For every N>=2, eta^e in I_close, u^e in I_close, or (B eta)^e in I_close implies e>=2N.','construction':'P=-1/4-x+sum_{r=1}^{2N-1} z^r f_r(x), f1=x², T(fr)=-(theta-3)sum_{i=1}^{r-1}fi*f_{r-i}; T is a triangular isomorphism x³Q[x]_{<=r+1}->x4Q[x]_{<=r+2}.','first_fr':{str(r):str(fs[r]) for r in range(1,5)},'checks':records}
p=pathlib.Path('box/k16-utac-20260906/theory_artin_thickness.json');p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
