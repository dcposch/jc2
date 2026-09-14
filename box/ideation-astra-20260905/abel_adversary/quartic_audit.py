#!/usr/bin/env python3
"""Exact desk algebra; no imported lane artifacts and no promotion by sampling."""
import sympy as s
x,W,Wp,y,b,B,eta=s.symbols('x W Wp y b B eta')
C=s.symbols('C')
r=b*b/4; K=x*x*C-y*b; z=x*W-r; zp=W+x*Wp
A=3*x**3*C*C/(4*y*y); D=3*b*x*C/(2*y)
R=W*W+(B-2*A+D)*W+A*(A-D)/3-B*(A-D)-b*eta*K/(2*y)-B*eta*x+(2*r*A-4*r*(B+W))/x
F=2*(x*W-r)*Wp-R
Q=-B*x+3*K*(K+y*b)/(2*y*y)
H=2*x*zp-3*z+Q
Psi=3*K**3*(K+2*y*b)/(16*y**4)-3*B*x*K*K/(4*y*y)-b*eta*x*x*K/(2*y)-B*eta*x**3
assert s.cancel(z*H-Psi-x*x*F)==0
print('ALL_B_PRODUCT_IDENTITY_PASS: z H - Psi = x^2 F3_residual')
k,zz,zzp=s.symbols('K z zp')
QQ=-B*x+3*k*(k+y*b)/(2*y*y)
PP=3*k**3*(k+2*y*b)/(16*y**4)-3*B*x*k*k/(4*y*y)-b*eta*x*x*k/(2*y)-B*eta*x**3
root_identity=s.expand((zz*(2*x*zzp-3*zz+QQ)-PP).subs(k,0))
assert root_identity==zz*(2*x*zzp-3*zz-B*x)+B*eta*x**3 or s.expand(root_identity-zz*(2*x*zzp-3*zz-B*x)-B*eta*x**3)==0
print('ROOT_UNIT_IDENTITY_PASS: mod K, z(2xz_prime-3z-Bx)=-B eta x^3')
u=s.symbols('u')
P=3*x*u**4+6*b*u**3-12*B*u*u-8*b*eta*u-16*B*eta
assert s.expand(PP.subs(k,y*x*u)-x**3*P/16)==0
print('QUARTIC_PENCIL_PASS')
w,L,ch,v,rr=s.symbols('w lambda chi v r')
phi=s.Rational(16,3)*L*w**4+s.Rational(8,3)*L*w**3+4*w*w-2*w
p_normal=s.factor(P.subs({x:b*b*ch/B,u:B*v/b,eta:L*B*B/(b*b)}))
assert s.factor(p_normal-3*B**3*v**4/(b*b)*(ch-phi.subs(w,1/v)))==0
print('DIMENSIONLESS_QUARTIC_PASS')
centered=s.expand(phi.subs(w,rr-s.Rational(1,8)))
assert s.expand(centered-(s.Rational(16,3)*L*rr**4+(4-L/2)*rr**2+(L/12-3)*rr+s.Rational(5,16)-L/256))==0
print('CENTERED_QUARTIC:',centered)
Delta=3*L*L-69*L-32
critical_disc=s.factor(s.discriminant(s.diff(phi,w),w))
assert critical_disc==s.Rational(4096,3)*L*Delta
print('CRITICAL_POINT_DISC:',critical_disc)
branch=256*ch**3*L**2+(9*L**3-336*L**2+384*L)*ch**2+(-24*L**2+660*L+144)*ch-4*L**2+132*L+36
res=s.factor(s.resultant(phi-ch,s.diff(phi,w),w))
assert s.expand(res+s.Rational(65536,81)*L**2*branch)==0
print('CRITICAL_VALUE_RESULTANT: -(65536/81) lambda^2 times R_lambda(chi)')
print('R_lambda:',branch)
branch_disc=s.factor(s.discriminant(branch,ch))
assert branch_disc==432*L**3*(L-36)**2*Delta**3
print('CRITICAL_VALUE_DISC:',branch_disc)
assert s.expand(centered.subs(L,36)-(192*rr**4-14*rr**2+s.Rational(11,64)))==0
assert s.expand(branch.subs(L,36)-36*(12*ch+1)**2*(64*ch-11))==0
print('LAMBDA36_COMPOSITION_PASS: Phi_36=192(r^2)^2-14r^2+11/64; r=w+1/8')
print('LAMBDA36_BRANCH_VALUES: -1/12 (double in R), 11/64 (simple in R)')
# The prescribed leading balance is an identity on the normalizer.
t,d=s.symbols('t d')
omega=3*(2*d-1)/(4*y*y*(4*t+1))
lead=(4*t+1)*omega**2+3*omega/(2*y*y)-3/(16*y**4)
assert s.factor(lead-3*(3*d*d-t-1)/(4*y**4*(4*t+1)))==0
print('LEADING_BALANCE_PASS: identity modulo 3d^2-t-1')
# Origin recurrence includes arbitrary C collisions; through n=3 is automatic.
c0,c1,c2,c3,a3,a4,a5=s.symbols('c0 c1 c2 c3 a3 a4 a5')
cc=c0+c1*x+c2*x*x+c3*x**3
kk=x*x*cc-y*b
zjet=-b*b/4-B*x+eta*x*x+a3*x**3+a4*x**4+a5*x**5
qjet=-B*x+3*kk*(kk+y*b)/(2*y*y)
pjet=3*kk**3*(kk+2*y*b)/(16*y**4)-3*B*x*kk*kk/(4*y*y)-b*eta*x*x*kk/(2*y)-B*eta*x**3
jet=s.Poly(s.expand(zjet*(2*x*s.diff(zjet,x)-3*zjet+qjet)-pjet),x)
assert all(jet.nth(j)==0 for j in range(4))
assert s.diff(jet.nth(4),a4)==-b*b/2
assert s.diff(jet.nth(5),a5)==-b*b
print('ORIGIN_FORMAL_PASS: coefficients x^0..x^3 automatic; z3 free; diag z_n = -(b^2/2)(n-3), n>=4')
print('FIRST_TRUNCATION_OBSTRUCTION:',s.factor(jet.nth(4)))
# Squarefree compatibility criterion controls; no K16 claim about mutated Psi.
za=x*x+x+1; qa=x*x+2*x+3
ha=2*x*s.diff(za,x)-3*za+qa
psia=za*ha
assert s.gcd(za,s.diff(za,x))==1
condition=lambda p:s.rem(2*x*s.diff(za,x)**2+qa*s.diff(za,x)-s.diff(p,x),za,x)
assert condition(psia)==0
assert condition(za*(ha+1))!=0
print('SQUAREFREE_FACTOR_POSITIVE_NEGATIVE_PASS')
zc=x*x; qc=x*x; hc=2*x*s.diff(zc,x)-3*zc+qc
pc=zc*(hc+x)
assert s.rem(2*x*s.diff(zc,x)**2+qc*s.diff(zc,x)-s.diff(pc,x),zc,x)==0
assert pc!=zc*hc
print('COLLISION_NEGATIVE_CONTROL_PASS: first residue condition alone accepts z=x^2, discrepancy x')
# True K16 normalizer at t=11, d=2, y=7/23, omega=529/980.
# Preserve all stated degrees and leading data but change actual Psi.
t0=11; y0=s.Rational(7,23); om0=s.Rational(529,980)
z0=om0*x**24+x*x-x-s.Rational(1,4)
k0=x**12-y0
q0=-x+3*k0*(k0+y0)/(2*y0*y0)
h0=2*x*s.diff(z0,x)-3*z0+q0
p0=3*k0**3*(k0+2*y0)/(16*y0**4)-3*x*k0*k0/(4*y0*y0)-x*x*k0/(2*y0)-x**3
pmut=s.expand(z0*h0)
gap=s.Poly(s.expand(pmut-p0),x)
assert s.degree(pmut,x)==s.degree(p0,x)==48
assert s.LC(s.Poly(pmut,x))==s.LC(s.Poly(p0,x))
assert gap.nth(4)==1
assert all(gap.nth(j)==0 for j in range(4))
assert s.rem(s.Poly(p0,x),s.Poly(z0,x))!=0
print('DEGREE_ONLY_NEGATIVE_PASS: t11 actual normalizer, b=B=eta=1, C=x^10, same degree48/lead; mutated-minus-true coefficient x4=1')
print('TRUE_PSI_DIVISIBILITY_REMAINDER_DEGREE:',s.degree(s.rem(p0,z0,x),x))
print('ALL_CHECKS_PASS')
