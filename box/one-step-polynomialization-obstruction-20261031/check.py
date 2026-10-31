"""Exactly the three fixed-map identities authorized by CREMONA2355."""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as S

u, v = S.symbols('u v')
P = u**4 + u*v
Q = 3*v**2 + 12*u**3*v + 8*u**6
checks = {
    'Jacobian_6v2': S.expand(S.diff(P,u)*S.diff(Q,v)-S.diff(P,v)*S.diff(Q,u)-6*v**2)==0,
    'cusp_pullback_v3_times_9v_plus_8u3': S.expand(Q**2-64*P**3-v**3*(9*v+8*u**3))==0,
    'simultaneous_sign_deck_symmetry': all(S.expand(f.subs({u:-u,v:-v}, simultaneous=True)-f)==0 for f in (P,Q)),
}
out = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'status':'PASS' if all(checks.values()) else 'FAIL',
       'scope':'Three polynomial identities for one previously reviewed map only; no field-degree/Galois/polynomialization or JC2 verification.',
       'sympy_version':S.__version__,
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'checks':checks}
print(json.dumps(out))
