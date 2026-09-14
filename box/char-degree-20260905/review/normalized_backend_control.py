#!/usr/bin/env python3
"""Independent normalizer, division-map, and total-face row controls."""
import hashlib,json,subprocess,sys
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'d108'))
from normalized_backend import normalized_script

x,y,t,z=s.symbols('x y t z')
def norm(poly,degree):
    result=s.expand(t**degree*poly.subs({x:1/t,y:(1+z)/t},simultaneous=True))
    assert all(mon[0]>=0 and mon[1]>=0 for mon,_ in s.Poly(result,t,z).terms())
    return result
def divide(poly,H,var):
    q,r=s.div(s.Poly(poly,var),s.Poly(H,var))
    assert s.expand(poly-q.as_expr()*H-r.as_expr())==0
    return q.as_expr(),r.as_expr()

# Dense, nontrivial physical polynomials: all four normalized z-divisions
# must be precisely the normalization of their monic y-divisions.
k=3
H=y**3+(x+1)*y*y+(x*x-2)*y+x+3
v=(x**3+2)*y*y+(x**4-x)*y+x**5+1
U,R=divide(v*v,H,y)
P,R1=divide(v*U,H,y)
Q,R2=divide(v*R,H,y)
W,R3=divide(U*U,H,y)
Hn=norm(H,k);vn=norm(v,2*k-1)
Un,Rn=divide(vn*vn,Hn,z)
Pn,R1n=divide(vn*Un,Hn,z)
Qn,R2n=divide(vn*Rn,Hn,z)
Wn,R3n=divide(Un*Un,Hn,z)
normalizers=[('U',U,Un,3*k-2),('R',R,Rn,4*k-2),('P',P,Pn,4*k-3),
             ('R1',R1,R1n,5*k-3),('Q',Q,Qn,5*k-3),('R2',R2,R2n,6*k-3),
             ('W',W,Wn,5*k-4),('R3',R3,R3n,6*k-4)]
for name,physical,normalized,degree in normalizers:
    assert s.expand(norm(physical,degree)-normalized)==0,name

cases=[]
for k,d,P0,exponent in [(33,55,y**3*(y-x)**8,3),(36,63,y**2*(y-x)**7,4)]:
    Edegree=d-k
    quotient_power=2 if k==33 else 3
    topQ=P0**(exponent+quotient_power)
    topH=P0**exponent
    topE=P0**quotient_power
    assert s.expand(topE*topH-topQ)==0
    ed,ld=5*k-3,6*k-3
    expected_face=z**(16 if k==33 else 21)*(1+z)**6
    assert s.expand(norm(s.expand(topE),Edegree)-expected_face)==0
    cases.append({'k':k,'target':d,'normalizers':{'H':k,'v':2*k-1,'V':3*k-1,
                    'U':3*k-2,'R':4*k-2,'P':4*k-3,'R1':5*k-3,'Q':5*k-3,
                    'R2':6*k-3,'W':5*k-4,'R3':6*k-4,'upper':4*k-2,'digit':ed,'low':ld},
                  'digit_face_depth':ed-Edegree,'digit_face':str(expected_face),
                  'low_vanish_strict_t_bound':ld-(d-1),
                  'filtered_monic_face_division':True})

# Exercise the actual normalized Singular backend. The test pair has
# H=y^2, v=y, V=3/8 and Q=-y^3/8-9/64. It is a backend test only.
names=sorted(['target_a','target_b','target_c','target_d','target_e','leader3','Z3','c','Zc'])
rows=['target_a','target_b','target_c','target_d','target_e','c-1']
base=normalized_script('(1+zz)^2','tt^2*(1+zz)','(3/8)*tt^5',rows,names,2,3,'1+zz')
test_specs=[('attained_face',base,False),
            ('wrong_face',base.replace('tt^6*(1+zz)','tt^6*(zz)'),True),
            ('low_at_target_must_vanish',base.replace('poly digitDifference=','low=low+tt^6;poly digitDifference='),True),
            ('low_below_target_may_survive',base.replace('poly digitDifference=','low=low+tt^7;poly digitDifference='),False)]
backend=[]
for tag,script,unit in test_specs:
    path=HERE/f'normalized_{tag}.sing';path.write_text(script)
    proc=subprocess.run(['Singular','-q',str(path)],capture_output=True,text=True,timeout=60)
    log=proc.stdout+proc.stderr;(HERE/f'normalized_{tag}.out').write_text(log)
    assert proc.returncode==0 and not any(line.lstrip().startswith('?') for line in log.splitlines()),log
    result=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines()
    assert (result[0]=='0')==unit,(tag,result)
    assert log.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines()==['0','1']
    backend.append({'tag':tag,'unit':unit,'reduce_one':result[0],
                    'script_sha256':hashlib.sha256(script.encode()).hexdigest(),'passed':True})

record={'field':'Q','physical_y_to_normalized_z_four_divisions':True,'dense_control_k':3,
        'cases':cases,'actual_backend_controls':backend,
        'backend_sha256':hashlib.sha256((HERE.parent/'d108/normalized_backend.py').read_bytes()).hexdigest(),
        'self_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'normalized_backend_control.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
