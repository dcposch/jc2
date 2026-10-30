#!/usr/bin/env python3
"""Three exact sanity cases and rational coordinate identities; not an all-n proof."""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as S

x, y, u, t, w, a, b = S.symbols('x y u t w a b')
P = x - x**3*y**5
W = x**2*y**5
def jac(f, g, v1, v2):
    return S.diff(f,v1)*S.diff(g,v2)-S.diff(f,v2)*S.diff(g,v1)
def zero(f):
    return S.cancel(f) == 0

checks = []
coeff = -S.Rational(1,2)
G = S.Integer(0)
for n in range(3):
    if n:
        coeff *= -S.Rational(5*n-2,5*n+2)
    G += coeff*(w-1)**n
    Q = y*G.subs(w,W)
    J = jac(P,Q,x,y)
    expected = 1-(5*n+3)*coeff*(W-1)**(n+1)
    grad_ideal = S.groebner([S.diff(Q,x),S.diff(Q,y)],x,y)
    checks.append({'n':n,'G':str(S.expand(G)),
                   'Jacobian_identity':zero(J-expected),
                   'Q_gradient_ideal_is_unit':list(grad_ideal)==[S.Integer(1)],
                   'G_at_zero':str(G.subs(w,0)),
                   'G_at_one':str(G.subs(w,1)),
                   'error_coefficient':str((5*n+3)*coeff)})

X=(1+u**2*t)**3/u**5
Y=u**2/(1+u**2*t)
target_P=1/(a**3*b)
target_Q=a**2*b
identities={
    'P_gradient_ideal_is_unit':list(S.groebner([S.diff(P,x),S.diff(P,y)],x,y))==[S.Integer(1)],
    'u_inverse':zero(X*Y**3-u),
    'w_inverse':zero(X**2*Y**5-(1+u**2*t)),
    'source_volume':zero(jac(X,Y,u,t)+(1+u**2*t)/u**2),
    'P_in_chart':zero(P.subs({x:X,y:Y})+t*(1+u**2*t)**3/u**3),
    'source_graded_r_inverse':zero(X*Y**2-(1+u**2*t)/u),
    'source_graded_s':zero(X**2*Y**4*(X**2*Y**5-1)-(1+u**2*t)**2*t),
    'target_a_inverse':zero(1/(target_P*target_Q)-a),
    'target_b_inverse':zero(target_P**2*target_Q**3-b),
    'target_volume':zero(jac(target_P,target_Q,a,b)+1/(a**2*b)),
}
out={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'sympy_version':S.__version__,'scope':'Exactly n=0,1,2 and displayed rational identities; all-n claims require the written proof.',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'cases':checks,'identities':identities}
out['status']='PASS' if all(r['Jacobian_identity'] and r['Q_gradient_ideal_is_unit'] for r in checks) and all(identities.values()) else 'FAIL'
print(json.dumps(out, indent=2))
