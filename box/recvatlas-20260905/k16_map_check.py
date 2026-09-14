#!/usr/bin/env python3
"""Exact K16 receiver-map controls; no basis computation or imported row files.

One foreground core.  The exceptional F3 family and REC are copied as
formulas from the hash-verified charged report.  Rational pi expressions
are required to cancel into Q[b,gamma,pi] before any Jacobian is accepted.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
x, b, tc, gamma, pi, Gamma, Pi = s.symbols("x b tc gamma pi Gamma Pi")
y = s.Rational(1, 5)
g = s.Rational(7, 125)
c = -y*g
C = x
W = -s.Rational(25, 4)*x**5 + s.Rational(5, 2)*b*x**2
B = eta = b1 = s.Integer(0)
r = b*b/4
A = 3*x**3*C*C/(4*y*y)
D = 3*b*x*C/(2*y)
K = x*x*C-y*b
rhs = (W*W+(B-2*A+D)*W+A*(A-D)/3-B*(A-D)
       -b*eta*K/(2*y)-B*eta*x+(2*r*A-4*r*(B+W))/x)
F3 = s.cancel(2*(x*W-r)*s.diff(W,x)-rhs)
assert F3 == 0

T = s.integrate(g*(5*C+3*x*s.diff(C,x))/(2*y),x)+tc
Up = s.expand(y*(2*x*s.diff(W,x)-W-B)/(3*x)
              +x*x*C*(5*C+2*x*s.diff(C,x))/(4*y)
              -b*C-b*x*s.diff(C,x)/2)
S = s.expand(g*(W+B)/x-3*g*x*x*C*C/(4*y*y)+g*b*C/(2*y)+x*C*T/y)
Faux = x*T-g*b
Y = x*S-b*T-g*B
Vp = s.cancel((y*g*b1-K*s.diff(Y,x)+s.diff(K,x)*Y+2*Up*Faux)/(2*y*x))
tc_value = s.solve(s.expand(Vp).coeff(x,4),tc)[0]
assert tc_value == 0
T,S,Faux,Y,Vp = [s.expand(f.subs(tc,tc_value)) for f in (T,S,Faux,Y,Vp)]
U,V = s.integrate(Up,x),s.integrate(Vp,x)
assert U == x**5-b*x**2/2
assert V == x**7-s.Rational(7,20)*b*x**4

xp = pi**3*(pi-gamma)+b*pi
Q = s.cancel(U.subs(x,xp)+K.subs(x,xp)/pi+y*xp/pi**2)
P = s.cancel(V.subs(x,xp)+Y.subs(x,xp)/pi+Faux.subs(x,xp)/pi**2+g*xp/pi**3)
Qp,Pp = [s.Poly(f,gamma,pi,domain=s.QQ[b]) for f in (Q,P)]
Jac = s.expand(s.diff(Q,gamma)*s.diff(P,pi)-s.diff(Q,pi)*s.diff(P,gamma))
assert Jac == y*g*(pi-gamma)
assert Qp.coeff_monomial(gamma) == 0
assert Pp.coeff_monomial(gamma) == -g
assert s.Poly(Q,pi).LC() == 1
assert s.Poly(P,pi).LC() == 1
assert s.degree(Q,pi) == 20 and s.degree(P,pi) == 28

def forbidden(f, gx, px, include_zero):
    return [{"gamma_power":i,"pi_power":j,"coefficient":str(a)}
            for (i,j),a in s.Poly(f,gx,px).terms()
            if i > 3*j and (include_zero or j>0)]

assert forbidden(Q,gamma,pi,True) == []
assert forbidden(P,gamma,pi,True) == [
    {"gamma_power":1,"pi_power":0,"coefficient":"-7/125"}]
assert forbidden(P,gamma,pi,False) == []
assert forbidden(Q,gamma,pi,False) == []

# On this cone tau=0: Gamma=gamma-pi, Pi=pi, inverse gamma=Gamma+Pi.
Qr,Pr = [s.expand(f.subs({gamma:Gamma+Pi,pi:Pi},simultaneous=True)) for f in (Q,P)]
Jr = s.expand(s.diff(Qr,Gamma)*s.diff(Pr,Pi)-s.diff(Qr,Pi)*s.diff(Pr,Gamma))
assert Jr == c*Gamma
assert s.Poly(Pr,Gamma,Pi).coeff_monomial(Gamma) == -g
assert forbidden(Pr,Gamma,Pi,True) == [
    {"gamma_power":1,"pi_power":0,"coefficient":"-7/125"}]
assert s.degree(Qr,Pi) == 15 and s.degree(Pr,Pi) == 21
assert s.Poly(Qr,Pi).LC() == -Gamma**5
assert s.Poly(Pr,Pi).LC() == -Gamma**7

# Generic formal support obstruction. The constant coefficient in pi is
# determined using finite Taylor jets; h carries gamma first at pi^3.
u0,u1,u2,u3,p10,p11,p12,p20,p21,G,BB,bb,bb1 = s.symbols(
    "u0 u1 u2 u3 p10 p11 p12 p20 p21 G BB bb bb1")
xx = pi**3*(pi-gamma+bb1)+BB*pi*pi+bb*pi
formal = (u0+u1*xx+u2*xx**2+u3*xx**3
          +(p10+p11*xx+p12*xx**2)/pi
          +(p20+p21*xx)/pi**2+G*xx/pi**3)
assert s.expand(formal).coeff(pi,0).coeff(gamma,1) == -G

# General critical-line coordinate map and monic target normalization.
tau,cs,qs,es = s.symbols("tau cs qs es",nonzero=True)
old_gamma = Gamma+(1-tau/cs)*Pi
line = cs*gamma+(tau-cs)*pi
assert s.expand(line.subs({gamma:old_gamma,pi:Pi},simultaneous=True)) == cs*Gamma
assert s.diff(old_gamma,Gamma)*s.diff(Pi,Pi)-s.diff(old_gamma,Pi)*s.diff(Pi,Gamma) == 1

# Polynomiality before descent and monicity after descent do not imply
# a <= 3*j when the truncation A(gamma) is nonzero.
yy,zz = s.symbols("yy zz")
H = (yy**3*zz-yy)**2+yy*zz
sigma = gamma**2+pi*gamma**3
Hdesc = s.cancel(H.subs({yy:1/gamma,zz:sigma},simultaneous=True))
assert Hdesc == pi*pi+gamma*gamma*pi+gamma
assert s.Poly(Hdesc,pi).LC() == 1
assert s.expand(Hdesc).coeff(pi,0) == gamma

extra_paths = [
    Path("box/k16pivot-20260903/terminal_laurent_model.py"),
    Path("box/k16T-drivers-20260903/t2_order_system.py"),
    Path("box/k16astra-20260905/moh-linear-jacobian.md"),
]
record = {
  "field":"Q; parameter b free", "generator_order":["b","gamma","pi"],
  "F3_exact":True, "REC_exact":True, "Q":str(Q),"P":str(P),
  "Q_pi_degree":20,"P_pi_degree":28,"monic_original":True,
  "Jacobian_original":str(Jac),"Jacobian_reoriented":str(Jr),
  "original_forbidden_Q":forbidden(Q,gamma,pi,True),
  "original_forbidden_P":forbidden(P,gamma,pi,True),
  "positive_pi_support_passes":True,
  "reoriented_Q_pi_degree":15,"reoriented_P_pi_degree":21,
  "reoriented_Q_leading":str(s.Poly(Qr,Pi).LC()),
  "reoriented_P_leading":str(s.Poly(Pr,Pi).LC()),
  "generic_gamma_pi0_coefficient":"-G",
  "polynomiality_countercontrol_original":str(H),
  "polynomiality_countercontrol_sigma":str(sigma),
  "polynomiality_countercontrol_descent":str(Hdesc),
  "extra_readonly_provenance":[{"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in extra_paths],
  "result":"PASS: candidate all-j receiver map fails support; no K16 kill"
}
(ROOT/"k16_map_check.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:v for k,v in record.items() if k not in {"Q","P","extra_readonly_provenance"}},indent=2))
