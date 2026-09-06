"""Exact structured-family replay; no general U_eta claim."""
from pathlib import Path
import subprocess
import sympy as s

out = Path(__file__).resolve().parent
t, A, j, U, q, v, w, z = s.symbols('t A j U q v w z')
L = -1 + A*t + t*t

def residual(P, speed):
    return s.Poly(s.expand(speed*t*s.diff(P**2,t)-3*P**2
        +s.Rational(3,2)*L*(L+1)*P
        -s.Rational(3,16)*L**3*(L+2)), t)

P = -s.Rational(1,4)+v*t*t+w*t**3+z*t**4
F = residual(P,j)
sol = {}
for row, var in [(2,v),(3,w),(4,z)]:
    pol = s.cancel(F.nth(row).subs(sol))
    sol[var] = s.factor(-pol.subs(var,0)/s.diff(pol,var))
polys=[]
for row in (5,6,7):
    num = s.fraction(s.factor(F.nth(row).subs(sol)))[0]
    if row % 2:
        assert s.rem(num,A,A)==0
        num=s.cancel(num/A)
    terms=s.Poly(num,A).terms()
    assert all(mon[0]%2==0 for mon, coefficient in terms)
    pol=s.Poly(sum(coefficient*U**(mon[0]//2)
        for mon,coefficient in terms),U,j).primitive()[1].as_expr()
    polys.append(pol)
R1=s.factor(s.resultant(polys[0],polys[1],U))
R2=s.factor(s.resultant(polys[0],polys[2],U))
common=j**8*(j-1)**2*(2*j-3)**6*(4*j-3)**2
C1=6272*j**5-12670*j**4+243*j**3+7505*j**2+1409*j-3267
C2=1792*j**5-890*j**4-8547*j**3+15481*j**2-11687*j+3267
assert s.expand(R1+common*C1)==0
assert s.expand(R2-common*C2)==0
assert s.gcd(C1,C2)==1
assert s.resultant(C1,C2,j)==669531824097600026204667144843558912

# Resonant speed j=3: retain q, the permitted x^3 coefficient of P.
P=-s.Rational(1,4)+q*t+v*t*t+w*t**3+z*t**4
F=residual(P,3)
sol={}
for row,var in [(2,v),(3,w),(4,z)]:
    pol=s.cancel(F.nth(row).subs(sol))
    sol[var]=s.factor(-pol.subs(var,0)/s.diff(pol,var))
rows=[s.Poly(s.fraction(s.factor(F.nth(row).subs(sol)))[0],A,q)
      .primitive()[1].as_expr() for row in range(5,9)]
assert list(s.groebner(rows,A,q,order='grevlex'))==[1]
emit=lambda pol:s.sstr(pol).replace('**','^')
singular='ring r=0,(A,q),dp;\nideal I='+','.join(map(emit,rows))+';\n'
singular+='ideal G=std(I);\nprint("RESONANT_QUADRATIC_BASIS");\nG;\n'
singular+='if (size(G)!=1 || G[1]!=1) { ERROR("unit ideal missing"); }\n'
# Nonempty control in the same ring: the cubic family identity is exact.
singular+='ring c=0,(b,a,x),dp;\npoly L=-b+a*x^3;\npoly P=-(L^2)/4;\n'
singular+='poly F=x*diff(P^2,x)-3*P^2+3*L*(L+b)*P/2-3*L^3*(L+2*b)/16;\n'
singular+='if(F!=0) { ERROR("cubic family control failed"); }\n'
singular+='print("CUBIC_CONTROL_PASS");\nquit;\n'
singpath=out/'structure-quadratic.sing'
singpath.write_text(singular)
proc=subprocess.run(['Singular','-q',str(singpath)],text=True,capture_output=True,check=True)
assert '?' not in proc.stdout and 'error' not in proc.stdout.lower()
assert 'CUBIC_CONTROL_PASS' in proc.stdout
lines=['EXACT_Q_ALL_PASS',
       'R1='+str(R1),'R2='+str(R2),
       'gcd(C1,C2)=1',
       'resultant(C1,C2)=669531824097600026204667144843558912',
       'Sympy resonant basis=[1]',proc.stdout.strip()]
(out/'structure-quadratic-check.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
