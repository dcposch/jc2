#!/usr/bin/env python3
"""Independent gauge identities; no assertion of the Xu prolongation licence."""
import importlib.util
import json
from pathlib import Path
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / 'box/g9966-d2-precise-20260905/band_engine.py'
spec = importlib.util.spec_from_file_location('g9966_gauge_import', ENGINE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)

x, y, a, b, j, u, v, c, pi, H, C = S.symbols('x y a b jet0 u v c pi Hc_11_0 C')
raw, variables = m.h3_template()
# This basis conversion is independent of the engine's series conversion:
# t^r (w-1)^q t^-11 -> x^(11-r-q) (y-x)^q.
hxy = S.expand(sum(coef*x**(11-r-q)*(y-x)**q for (r,q),coef in raw.items()))
on_major = S.expand(hxy.subs(y,x))
assert on_major == H
after_diagonal_at_origin = S.expand(hxy.subs({x:a,y:a}, simultaneous=True))
assert after_diagonal_at_origin == H

# Restore H in the precise branch map, and compute its first minor correction.
hmap, free, centre = m.h3_branch_map('delta52')
hmap[H] = H
changed = {key:m.substitute_map(value,hmap) for key,value in raw.items()}
rows = m.local_rows(changed, 'delta52', 22, exact_only=False)
p = pi*(pi**2-c)
lead = S.expand(sum(value*pi**power for (order,power),value in rows.items() if order==21))
A0 = S.expand(sum(value*pi**power for (order,power),value in rows.items() if order==22))
d = u**2-j**2*u+2*j*v
assert S.expand(lead-p) == 0
assert S.expand(A0-(H-d*S.diff(p,pi))) == 0

# Conditional calculation: IF D_s(Q,h)+2s^2h^4=0 has polynomial B1,
# its first extension imposes H=0 independently of q1's additive constant.
I = S.integrate(p**3,pi)
primitive = 2*d*p**4 - 8*H*I + C
assert S.expand(S.diff(primitive,pi)+8*p**3*A0) == 0
at_zero = primitive.subs(pi,0)
mod_second_factor = S.rem(primitive.subs(C,0), pi**2-c, pi)
assert at_zero == C
assert S.expand(mod_second_factor-H*c**5/S.Integer(5)) == 0

summary = {
    'status':'PASS',
    'h3_restricted_to_centered_major_line':str(on_major),
    'h3_after_residual_diagonal_translation_at_origin':str(after_diagonal_at_origin),
    'H_is_not_source_translation_normalization':True,
    'minor_leader':str(p),
    'minor_A0':str(S.factor(A0)),
    'minor_A0_identity':'Hc_11_0 - (u^2-jet0^2*u+2*jet0*v)*p_prime',
    'conditional_ODE_primitive':str(primitive),
    'conditional_ODE_remainder_mod_pi2_minus_c':str(mod_second_factor),
    'conditional_ODE_caveat':'This calculation does not prove that the global approximate h3 satisfies the prolonged Xu equation.',
    'pristine_endpoint_max_t':{
        branch:max(max(m.stage_spec(branch,i)['jacobian']['t_power'] for i in range(stage+1)),
                   m.stage_spec(branch,stage)['pole_local_power'] if branch=='delta2'
                   else (m.stage_spec(branch,stage)['pole_local_power']+1)//2,4)
        for branch,stage in [('delta2',4),('delta52',8)]
    },
}
assert set(summary['pristine_endpoint_max_t'].values()) == {8}
print(json.dumps(summary,indent=2,sort_keys=True))
