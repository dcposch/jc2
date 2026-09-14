#!/usr/bin/env python3
"""Symbolic row-ideal comparison, independent of the backend emitter."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
y=s.symbols('y');p,q=s.symbols('p q')
out=[]
for k in (2,3,4):
 hs=s.symbols(f'h0:{k}');vs=s.symbols(f'v0:{k}');us=s.symbols(f'u0:{k}')
 H=y**k+sum(hs[i]*y**i for i in range(k))
 v=sum(vs[i]*y**i for i in range(k));U=sum(us[i]*y**i for i in range(k))
 R=s.Poly(s.expand(v**2-U*H),y)
 RR=sum(R.nth(i)*y**i for i in range(k))
 V=s.Rational(3,8)*U
 direct=s.expand((H**2+v)**3-(H**3+s.Rational(3,2)*v*H+V)**2+p*(H**2+v)+q)
 emitted=s.expand((s.Rational(3,4)*RR+p)*H**2-v*U*H/8+v*RR-s.Rational(9,64)*U**2+p*v+q)
 assert s.expand(direct-emitted-(R.as_expr()-RR)*(s.Rational(3,4)*H**2+v))==0
 Q=s.Poly(direct,y);H2=s.Poly(s.expand(H**2),y)
 recovered={}
 for j in range(2*k-1,k-1,-1):
  image=s.Rational(4,3)*Q.nth(j+2*k)-sum(recovered[l]*H2.nth(j+2*k-l) for l in range(j+1,2*k))
  image=s.expand(image)
  assert s.expand(image-R.nth(j))==0
  recovered[j]=image
 out.append({'k':k,'all_high_remainder_rows_recovered_from_Q_rows':True,
             'selected_Q_y_degrees':list(range(4*k-1,3*k-1,-1)),
             'target_rows_unaltered_mod_remainder_rows':True,
             'generic_remainder_identity':True})
backend=HERE/'remainder_backend.py'
record={'backend_sha256':hashlib.sha256(backend.read_bytes()).hexdigest(),
        'field':'Q','tests':out,'result':'PASS',
        'theorem_scope':'generic monic degree-k divisor, v and U of y-degree below k; exact polynomial row-ideal equality'}
(HERE/'remainder-independent-review.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
