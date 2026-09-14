#!/usr/bin/env python3
"""Exact identity, nonzero-leader positive, and wrong-target negative controls."""
import hashlib,json,subprocess
from pathlib import Path
import sympy as s
from remainder_backend import script_for
HERE=Path(__file__).resolve().parent
H,v,U,R,p,q=s.symbols('H v U R p q')
V=s.Rational(3,8)*U
depressed=(H**2+v)**3-(H**3+s.Rational(3,2)*v*H+V)**2+p*(H**2+v)+q
rhs=(s.Rational(3,4)*R+p)*H**2-v*U*H/8+v*R-9*U**2/s.Integer(64)+p*v+q
assert s.expand(depressed-rhs-(v*v-U*H-R)*(s.Rational(3,4)*H*H+v))==0
# s0 is a degree-11 homogeneous polynomial with the required two-point top.
# h=s0^3-s0^2+s0-1, v=s0^2, U=s0+1 gives remainder 1.
# With p=-5/8 the characteristic polynomial has actual degree 5 in s0.
s0=s.symbols('s0');hh=s0**3-s0**2+s0-1;vv=s0**2;uu=s0+1
actual=s.expand(depressed.subs({H:hh,v:vv,U:uu,p:-s.Rational(5,8),q:0}))
assert s.degree(actual,s0)==5 and actual.coeff(s0,5)==-s.Rational(1,4)
out=HERE/'remainder-controls';out.mkdir(exist_ok=True)
record={'identity':True,'univariate_Q':str(actual),'positive_degree_after_degree11_composition':55,
        'positive_leader':'-1/4','scope':'characteristic rows only; deliberately fails actual D2 source faces','cases':{}}
P='zz^8*(1+zz)^3'
names=['target_a','target_b','target_c','target_d','target_e','leader55','Z55']
for label,leader in [('positive','leader55+(1/4)'),('negative_wrong_target','leader55-1')]:
    script=script_for(h_expr=f'({P})^3-tt^11*({P})^2+tt^22*({P})-tt^33',
      D_expr=f'tt^43*({P})^2',C_expr=f'(3/8)*(tt^87*({P})+tt^98)',
      residual_strings=['target_a','target_b','target_c','target_d+(5/8)','target_e',leader],
      names=names,k=33,target=55,face_expr='zz^16*(1+zz)^6',localizer_rows=())
    path=out/(label+'.sing');path.write_text(script)
    result=subprocess.run(['Singular','-q',str(path)],text=True,capture_output=True,timeout=60)
    text=result.stdout+result.stderr;(out/(label+'.out')).write_text(text)
    errors=[line for line in text.splitlines() if line.lstrip().startswith('?')]
    assert result.returncode==0 and not errors,(label,errors,text[-1000:])
    vals=text.split('BEGIN_RESULT\n')[1].split('\nEND_RESULT')[0].strip().splitlines()
    controls=text.split('BEGIN_CONTROLS\n')[1].split('\nEND_CONTROLS')[0].strip().splitlines()
    assert vals[0]==('1' if label=='positive' else '0') and controls==['0','1'],(vals,controls)
    record['cases'][label]={'reduce_one':vals[0],'dimension':int(vals[1]),'basis_size':int(vals[2]),
       'controls':controls,'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
       'output_sha256':hashlib.sha256(text.encode()).hexdigest()}
(HERE/'remainder-backend-controls.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,sort_keys=True))
