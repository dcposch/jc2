#!/usr/bin/env python3
"""Independent canonical inner minor necessity ideal, without F/G expansion.

Moh p149 Thm1.2 on the coherent endpoint system gives C2,C3 orders.
The h3 leader is already exact. After those strict pole rows, K2's leader
condition is exactly face(C2)*P+face(C3)=0; no higher local H3 term can enter.
"""
import argparse,hashlib,json,time
from pathlib import Path
import sympy as sp
import engine as E
import minor_maps as MM
from source_data import SOURCE as S,jsonable


def evaluate(rows,point):
    return [(label,str(value)) for label,row in rows if (value:=sp.expand(row.xreplace(point)))!=0]


def run(branch,out):
    started=time.monotonic();h,C2,C3,free,meta=E.inner_state(branch)
    print('SOURCE_READY',branch,len(free),time.monotonic()-started,flush=True)
    cover=S['minor'][branch]['cover'];order=S['minor'][branch]['h3_order']
    floors={name:int(cover*(S['inner_normalization_degrees'][name]+power*order)) for name,power in (('C2',2),('C3',3))}
    hfloor=S['minor'][branch]['h3_local_floor'];kfloor=3*hfloor
    assert floors=={'C2':2*hfloor,'C3':kfloor}
    P,_=MM.derive_minor_face(branch);pi=sp.Symbol('zeta')
    hlocal=E.local_rows(h,branch,hfloor)
    expected={(hfloor,power[0]):value for power,value in sp.Poly(P,pi).terms()}
    assert all(sp.expand(hlocal.get(key,0)-expected.get(key,0))==0 for key in set(hlocal)|set(expected))
    local={name:E.local_rows(poly,branch,floors[name]) for name,poly in (('C2',C2),('C3',C3))}
    print('LOCAL_READY',branch,[len(local[n]) for n in local],time.monotonic()-started,flush=True)
    rows=[(f'inner_minor_{name}_s{n}_q{k}',value) for name in ('C2','C3') for (n,k),value in sorted(local[name].items()) if n<floors[name]]
    localizer=sp.Symbol('rho' if branch=='delta2' else 'c')
    residual,map1,piv1,zero=E.qstar_reduce(rows,set(free)-{localizer})
    assert all(E.substitute_map(v,map1)==0 for _,v in rows if not residual) if not residual else True
    faceC2=sum(v*pi**k for (n,k),v in local['C2'].items() if n==floors['C2'])
    faceC3=sum(v*pi**k for (n,k),v in local['C3'].items() if n==floors['C3'])
    equality=sp.Poly(sp.expand(faceC2*P+faceC3),pi)
    eqrows=[(f'inner_minor_K2_face_s{kfloor}_q{k[0]}',v) for k,v in equality.terms()]
    reduced_eq=[(label,E.substitute_map(v,map1)) for label,v in eqrows]
    residual2,map2,piv2,zero2=E.qstar_reduce(residual+reduced_eq,set(free)-set(map1)-{localizer})
    combined=dict(map1);combined.update(map2);combined=E.resolve_map(combined)
    allrows=rows+eqrows
    exact_images=[(l,E.substitute_map(r,combined)) for l,r in allrows]
    print('REDUCED',branch,len(piv1),len(piv2),len(residual2),time.monotonic()-started,flush=True)
    remaining=set(free)-set(combined)
    trial={v:sp.Integer(0) for v in remaining};trial[localizer]=sp.Integer(1);trial[sp.Symbol('jet0')]=sp.Integer(1)
    trial.update({v:sp.expand(r.xreplace(trial)) for v,r in combined.items()})
    failures=evaluate(allrows,trial)
    result={'branch':branch,'floors':floors,'k2_floor':kfloor,'source_inner_count':len(free),
       'source_incidence_pivots':len(meta['source_Qstar_pivots']),'source_h3_control':meta['h3_control'],
       'row_count':len(allrows),'strict_row_count':len(rows),'equality_row_count':len(eqrows),
       'strict_Qstar_pivots':len(piv1),'face_Qstar_pivots':len(piv2),'Qstar_pivots':len(combined),
       'row_hash':E.rows_hash(allrows),'residual_count':len(residual2),'residual_rows':[(l,str(v)) for l,v in residual2],
       'residual_hash':E.rows_hash(residual2),'map':E.encode_map(combined),
       'pivot_ledger':[{'label':p.label,'variable':str(p.variable),'coefficient':str(p.coefficient)} for p in piv1+piv2],
       'raw_rows':[(l,str(v)) for l,v in allrows],
       'native_trial_satisfies_all_rows':not failures,'native_trial_failures':failures[:20],
       'native_trial_nonzero':{str(v):str(value) for v,value in trial.items() if value!=0},
       'scope':'necessary canonical inner chart; includes no outer or Jacobian rows',
       'source':'Moh printed p149 Thm1.2; endpoint coherent system in print-audit-derivations.md section3',
       'H3_local_identity_verified':True,'K2_leader_reduction':'h3local>=hfloor,C2local>=2hfloor,C3local>=3hfloor; equality remainder=C2face*P+C3face',
       'engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
       'elapsed_seconds':time.monotonic()-started}
    out.write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
    singular=E.singular_dimension(residual2,branch,out.with_suffix('.sing'))
    dimension=-1 if singular['unit_ideal'] else len(remaining)-singular['codimension']
    result.update({'singular':singular,'dimension':dimension,'elapsed_seconds':time.monotonic()-started})
    out.write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('branch','dimension','row_count','Qstar_pivots','residual_count','elapsed_seconds')},indent=2))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--branch',required=True,choices=['delta2','delta52']);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();run(a.branch,a.out)
