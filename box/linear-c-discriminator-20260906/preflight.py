#!/usr/bin/env python3
"""Small exact source-independence and highest-J-face controls; no solve.

The top-face parametrization is a statement about field points/reduced loci,
not an isomorphism of the original possibly nonreduced coefficient algebra.
This script does not certify the remaining Jacobian rows or a counterexample.
"""
import hashlib
import json
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json'

def require(value, message):
    if not value:
        raise ValueError(message)

raw = SOURCE.read_bytes()
require(hashlib.sha256(raw).hexdigest() == '778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea', 'source hash')
data = json.loads(raw)
require(data['residual_rows'] == [], 'source residuals changed')
maps = {name: [(r, z, S.sympify(expr)) for r, z, expr in rows]
        for name, rows in data['maps'].items()}
symbols = {name: set().union(*(expr.free_symbols for _, _, expr in rows))
           for name, rows in maps.items()}
cvars = symbols['A3']
require(len(cvars) == 192, 'C coordinate count')
require(not cvars.intersection(set().union(*(symbols[n] for n in ('h3','C2','C3','B2')))), 'C occurs in h or D')
require(all(S.Poly(expr, *sorted(cvars, key=str)).total_degree() <= 1 for _, _, expr in maps['A3']), 'C not linear')
require(cvars <= {expr for _, _, expr in maps['A3'] if isinstance(expr, S.Symbol)}, 'C source injection lacks identity slots')

# Physical coordinates (x,z), z=y-x, have determinant-one change of variables.
x, z = S.symbols('x z')
aa, bb, cc = S.symbols('aa bb cc')
htop = (x+z)**9*z**24
ell = aa*x*x+bb*x*z+cc*z*z
dtop = x*x*(x+z)**5*z**25*ell
ctop = S.Rational(3,8)*x**4*(x+z)*z**26*ell**2
require(S.cancel(S.Rational(3,4)*dtop**2-2*htop*ctop) == 0, 'highest-face parametrization')
def jac(f, g):
    return S.diff(f,x)*S.diff(g,z)-S.diff(f,z)*S.diff(g,x)
highest = S.Rational(3,2)*dtop*jac(htop,dtop)+2*htop*jac(ctop,htop)
require(S.expand(highest) == 0, 'highest Jacobian row')
require(S.Poly(S.expand(dtop),x,z).total_degree() == 34, 'D degree')
require(S.Poly(S.expand(ctop),x,z).total_degree() == 35, 'C degree')
require(all(i+j == 34 and 25 <= j <= 32 for i,j in S.Poly(S.expand(dtop),x,z).monoms()), 'D source top support')
require(all(i+j == 35 and 26 <= j <= 32 for i,j in S.Poly(S.expand(ctop),x,z).monoms()), 'C source top support')
bad = x**9*z**25
require(S.rem(bad**2, (x+z)**9, x) != 0, 'negative divisibility control')
print(json.dumps({'status':'PASS', 'C_parameters':192, 'C_linear_injective_and_independent':True,
                  'highest_J_face_parametrization':True, 'negative_divisibility_control':True,
                  'full_J_or_properness_claim':False}, sort_keys=True))
