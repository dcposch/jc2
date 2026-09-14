#!/usr/bin/env python3
"""Check only frozen leading faces and the tiny GGV Euler auxiliary."""
import json
from pathlib import Path
import resource
import time
import sys
import sympy as S
root=Path(__file__).resolve().parent
data=json.loads((root/'source_interface.json').read_text())
started=time.monotonic()
X,W,Z=S.symbols('X W Z')
def require(ok,why):
    if not ok:raise ValueError(why)
def jac(p,q):return S.expand(S.diff(p,X)*S.diff(q,W)-S.diff(p,W)*S.diff(q,X))
maps=data['source_maps']
for key,rows in maps.items():
    require(max(r['X'] for r in rows)==8,'x degree bound')
    require(max(4*r['X']-r['W'] for r in rows)==4,'weight bound')
lead=[r for r in maps['h'] if r['X']==8]
require(len(lead)==1 and lead[0]['W']==28 and S.sympify(lead[0]['coefficient'])==1,'unique leading x slot')
face=S.expand(sum(S.sympify(r['coefficient'])*X**r['X']*W**r['W'] for r in maps['h'] if 4*r['X']-r['W']==4))
H=X*(X*W**4-1)**7
require(S.expand(face-H)==0,'weight face mismatch')
# The small one-variable recurrence constructs [E,H]=H; [E/m,H^m]=H^m.
coef=[S.Integer(1)]
for n in range(1,5):coef.append(S.factor(-(20-4*n)*coef[-1]/(4*n+1)))
g=sum(c*Z**i for i,c in enumerate(coef))
require(S.expand((16*Z+1)*g-4*Z*(Z-1)*S.diff(g,Z)-1)==0,'Euler coefficient recurrence')
E=S.expand(X*W*(X*W**4-1)*g.subs(Z,X*W**4))
require(jac(E,H)==S.expand(H),'Euler bracket mismatch')
terms=S.Poly(E,X,W).terms()
require(all(4*i-j==3 for (i,j),c in terms),'Euler weight mismatch')
require(max(j for (i,j),c in terms)==21 and max(i for (i,j),c in terms)==6,'Euler endpoint mismatch')
# The final major-edge shift alpha=1 is fixed, not the source separation parameter c.
xx,yy=S.symbols('x y')
swapped=yy*(yy*xx**4-1)**7
require(S.expand(swapped.subs(yy,yy+xx**-4)-xx**28*yy**8-xx**24*yy**7)==0,'major edge cut mismatch')
result={'status':'EXACT_FIXED_EDGE_AND_AUXILIARY_PASS','map_scope':'NO full lower-boundary factor/cancellation transport claimed',
 'all_source_x_degree_bound':8,'all_source_weight_4_minus1_bound':4,
 'h_x_lead':'X^8 W^28','h_weight_face':'X(XW^4-1)^7',
 'after_A_equals_X_plus_W':'h face=A(AB^4-1)^7; h A-leading=A^8 B^28',
 'F_total_degree':108,'G_total_degree':72,'F_A_degree':24,'G_A_degree':16,
 'F_A_lead':'A^24 B^84','G_A_lead':'A^16 B^56',
 'F_weight_face':'[A(AB^4-1)^7]^3','G_weight_face':'[A(AB^4-1)^7]^2',
 'GGV_standard_pair_conditions_at_actual_Keller_points':True,'GGV_global_minimality_claimed':False,
 'Euler_g':str(g),'Euler_auxiliary_E':str(E),'Euler_identity':'J(E,H)=H; J(E/m,H^m)=H^m',
 'Euler_weight':3,'Euler_endpoint':[6,21],'Euler_swapped_endpoint':[21,6],
 'Euler_endpoint_ratio_to_8_28':'3/4','fixed_major_cut_lambda4':1,
 'fixed_major_cut_result':'x^28 y^8+x^24 y^7',
 'seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
target=root/'edge_interface.json'
if '--verify' in sys.argv:
    recorded=json.loads(target.read_text())
    require({k:v for k,v in recorded.items() if k not in ('seconds','peak_rss_kib')}=={k:v for k,v in result.items() if k not in ('seconds','peak_rss_kib')},'replay mismatch')
else:
    require(not target.exists(),'no overwrite')
    target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
