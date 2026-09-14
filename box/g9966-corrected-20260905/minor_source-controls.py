#!/usr/bin/env python3
"""Independent rational image and support checks for the printed source chart."""
from pathlib import Path
import sys,json,hashlib,time
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import minor_source_engine_snapshot as e
ENGINE_SHA256=hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest()
from deep_point_scan import specialize,compose_local,local_series,polynomial_record,mul,add,scale
from fractions import Fraction as Q

def run(branch):
    start=time.monotonic()
    h,c2,c3,free,meta=e.inner_state(branch)
    assignment=dict.fromkeys(free,sp.Integer(0))
    assignment[sp.Symbol('jet0')]=assignment[sp.Symbol('rho' if branch=='delta2' else 'c')]=sp.Integer(1)
    num={name:specialize(poly,assignment) for name,poly in [('h3',h),('C2',c2),('C3',c3)]}
    residue=[(label,sp.expand(v.xreplace(assignment))) for label,v in meta['additional_rows']]
    assert all(v==0 for _,v in residue)
    hsq=mul(num['h3'],num['h3'],33)
    k2=add(mul(hsq,num['h3'],33),mul(num['C2'],num['h3'],33),num['C3'])
    wt,wz=e.S['D2_weight'];pi=sp.Symbol('pi')
    face=sum(sp.Rational(v.numerator,v.denominator)*pi**q for (r,q),v in k2.items() if wt*r+wz*q==e.S['k2_floor'])
    wanted=e.S['k2_face'].subs(sp.Symbol('beta'),1)
    assert sp.expand(face-wanted)==0
    assert all(wt*r+wz*q>=e.S['k2_floor'] for r,q in k2)
    # Independent generic substitution at D1, using exact Fraction convolution.
    cover,base,child=e.S['D1_substitution']
    d1series={(0,0):Q(1),(base,0):Q(1),(child,1):Q(1)}
    d1=compose_local(k2,cover,d1series,e.S['k2_D1_floor']-1)
    assert not d1,d1
    # Compose at actual minor series before forming powers, avoiding any large global F/G.
    cover,w=local_series(branch,assignment)
    cap=max(e.S['minor'][branch]['F_local_floor'],e.S['minor'][branch]['G_local_floor'])
    local={name:compose_local(poly,cover,w,cap) for name,poly in num.items()}
    lk2=add(mul(mul(local['h3'],local['h3'],cap),local['h3'],cap),mul(local['C2'],local['h3'],cap),local['C3'])
    lF=mul(mul(lk2,lk2,cap),lk2,cap);lG=mul(lk2,lk2,cap)
    faces={name:poly for name,poly in [('F',lF),('G',lG)]}
    failures={}
    for name,poly in faces.items():
        power,target=e.minor_pole_targets(branch)[name]
        tpoly={(power,k):Q(int(v.xreplace(assignment).p),int(v.xreplace(assignment).q)) for k,v in target.items() if v.xreplace(assignment)!=0}
        rows=add(poly,scale(tpoly,Q(-1)))
        rows={key:v for key,v in rows.items() if key[0]<=power}
        first=min((n for n,k in rows),default=None)
        failures[name]={'target_local_power':power,'first_failed_local_power':first,
                        'first_nonzero_rows':polynomial_record({key:v for key,v in rows.items() if key[0]==first})}
    mins={name:min((n for n,k in poly),default=None) for name,poly in local.items()}
    mins['K2']=min((n for n,k in lk2),default=None)
    report={'branch':branch,'status':'PASS: source incidence and major orders',
            'free_coordinates':sorted(map(str,free)), 'free_count':len(free),
            'assignment_nonzero':{str(k):str(v) for k,v in assignment.items() if v!=0},
            'assignment_other_free':'0','inner_residual_count':len(residue),
            'K2_D2_face_exact':True,'K2_D2_floor_exact':True,'K2_D1_below_rows_zero':True,
            'local_leading_orders':mins,'pole_point_failures':failures,
            'Jacobian':'identically zero at this point when all outer free coefficients are zero',
            'numeric_blocks':{name:polynomial_record(poly) for name,poly in num.items()},
            'engine_sha256':ENGINE_SHA256,
            'elapsed_seconds':time.monotonic()-start}
    (HERE/f'minor_source-point-snapshot-{branch}.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['branch','free_count','local_leading_orders','pole_point_failures','elapsed_seconds']},indent=2),flush=True)
    return report
if __name__=='__main__':
    run(sys.argv[1])
