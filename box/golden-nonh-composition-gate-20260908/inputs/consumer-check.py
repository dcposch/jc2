"""Exact scalar coefficient projections only; no degree6/10 or source pairs."""
import ast
import json
import resource
import sys
from fractions import Fraction as Q
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
def need(ok, message):
    if not ok:
        raise ValueError(message)
mode = sys.argv[1] if len(sys.argv) > 1 else 'positive'
need(mode in ('positive', 'wrong-quintic-factor', 'wrong-face-sign', 'wrong-target-factor', 'drop-resonant-target'), 'mode')
def k(a=0, b=0): return (Q(a), Q(b))
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]+3*a[1]*b[1])
def scale(a, n): return (a[0]*n, a[1]*n)
one, zero = k(1), k()
# Abstract coefficient symbols k,e: the Y10 coefficient is zero; Y5 is
# 6e + (q/2 - 5q/2)k^2 and the constant is e*k*p^(1/2).
# No P,Q, derivatives, or degree6/10 polynomial is materialized.
q = Q(4,3) if mode == 'wrong-quintic-factor' else Q(5,3)
need(6*q/2-10*Q(1,2) == 0, 'Y10 coefficient cancellation fixes quintic factor')
need(q/2-5*q/2 == Q(-10,3), 'Y5 coefficient of k squared')
need(Q(10,3)/6 == Q(5,9), 'Y5 row forces e=5k squared/9')
# Weighted source face determinant projections, no full high face expansion.
need(2*0-1*1 == -1, 'c=-a*d')
need(2*5-1*8 == 2 and 9*0-6*1 == -6, 'g9p5 face row')
need(2*10-1*15 == 5 and 9*5-6*8 == -3, 'g16p10 face row')
need(9*10-6*15 == 0, 'top face bracket cancels')
need(6*Q(12,5)+10*Q(12,5)-Q(12,5) == (0 if mode == 'drop-resonant-target' else 36), 'resonant initial bracket equals source target order36')
rows = []
for rho in (k(0,1), k(3,-1)):
    t = add(one,neg(rho)); tm1=add(t,k(-1)); a2=mul(t,tm1)
    tinv=add(k(2),neg(rho)); rinv=add(k(3),neg(rho))
    need(mul(t,t)==rho and mul(t,tinv)==one and mul(rho,rinv)==one, 'golden units in both embeddings')
    need(a2!=zero, 'nondegenerate Morse quadratic')
    # lambda^3 is a common symbolic factor; remove it only after showing
    # all coefficients homogeneous of degree3 in lambda in the prose.
    resonant=scale(mul(t,mul(tm1,tm1)),Q(5,9))
    face=scale(t,Q(5,9) if mode=='wrong-face-sign' else Q(-5,9))
    need(face==scale(mul(mul(t,mul(t,t)),rinv),Q(-5,9)), 'source c=-5lambda cubed*t/9')
    # (k/lambda)^2=(t-1)/t; c=(5/9)k^3*t^2*a.
    # Multiply by a^2 to compare without adjoining its square root.
    target_t2=t if mode=='wrong-target-factor' else mul(t,t)
    need(mul(resonant,a2)==scale(mul(mul(tm1,mul(tm1,tm1)),target_t2),Q(5,9)), 'Morse target denominator t squared*a')
    discrepancy=add(mul(tm1,tm1),one)
    need(discrepancy==scale(rho,3) and discrepancy!=zero, 'incompatible coefficients differ by unit 3rho')
    need(add(resonant,neg(face))!=zero, 'resonant/source coefficients are unequal')
    rows.append({'rho':[str(x) for x in rho], 'resonant_c_over_lambda3':[str(x) for x in resonant], 'face_c_over_lambda3':[str(x) for x in face], 'unit_discrepancy':[str(x) for x in discrepancy]})
need(not any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(Path(__file__).read_text()))), 'no gating asserts')
print(json.dumps({'status':'PASS','mode':mode,'scalar_only':True,'rows':rows},sort_keys=True))
