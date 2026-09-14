#!/usr/bin/env python3
"""Exact-Q full characteristic total-degree/face instrument, corrected99.

Input manifests retain every source map and finite row.  A bounded CAS
execution remains OPEN; only parsed, controlled, complete results decide.
"""
import argparse,hashlib,json,os,signal,subprocess,time
from pathlib import Path
import sympy as sp
from normalized_backend_snapshot import normalized_script,exprS
HERE=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--timeout',type=int,default=1200)
    ap.add_argument('--emit-only',action='store_true');a=ap.parse_args()
    data=json.loads(a.input.read_text());branch=data['branch'];a.out.mkdir(parents=True,exist_ok=True)
    def poly(tab):
        return '+'.join(f'({exprS(sp.sympify(v))})*tt^{r}*zz^{q}' for r,q,v in tab) or '0'
    maps=data['maps'];sep='rho' if branch=='delta2' else 'c';inverse='Zrho' if branch=='delta2' else 'Zc'
    names=sorted(set(data['full_free_coordinates'])|{sep,inverse})
    res=[exprS(sp.sympify(v)) for _,v in data['residual_rows']]
    defs='\n'.join(f'poly {name}={poly(maps[key])};' for name,key in [('baseH','h3'),('innerC2','C2'),('innerC3','C3')])
    script=normalized_script('baseH^3+innerC2*baseH+innerC3',poly(maps['B2']),poly(maps['A3']),res,names,
        33,55,'zz^16*(1+zz)^6',leader_name='leader55',leader_inverse='Z55',localizer_rows=(inverse+'*'+sep+'-1',))
    token='print("BEGIN_BUILD_NORMALIZED");';assert script.count(token)==1
    script=script.replace(token,token+'\n'+defs)
    path=a.out/'augmented.sing';path.write_text(script)
    meta={'branch':branch,'stage':data['stage'],'status':'FULL-AUGMENTED-SCRIPT-EMITTED',
        'field':'Q','full_free_ring':['zz','tt']+names,'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
        'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'backend_sha256':hashlib.sha256((HERE/'normalized_backend_snapshot.py').read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(script.encode()).hexdigest(),'script_bytes':len(script),
        'source_finite':data['finite'],'all_source_coordinates_retained':True,
        'full_characteristic_rows':True,'all_five_target_coefficients_retained':True,
        'characteristic_degree':55,'leading_homogeneous_target':'leader55*y^15*(y-x)^40',
        'normalized_rows':{'derivedV_all':98,'upper_all':130,'digit_normalizer':162,'digit_zero_t_below':140,
            'digit_face_t':140,'digit_face':'leader55*z^16*(1+z)^6','low_normalizer':195,'low_zero_t_below':141},
        'target_subtraction':True,'new_gauges':[],'source_gauge':data['source_gauge']}
    resultpath=a.out/'result.json'
    def save():resultpath.write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    save();print(branch,data['stage'],'EMITTED',len(script),len(names),flush=True)
    if a.emit_only:return
    start=time.monotonic()
    with (a.out/'singular.out').open('w') as stream:
        proc=subprocess.Popen(['Singular','-q',str(path)],stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        timed=False
        try:rc=proc.wait(timeout=a.timeout)
        except subprocess.TimeoutExpired:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:rc=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);rc=proc.wait()
    output=(a.out/'singular.out').read_text();errors=[l for l in output.splitlines() if l.lstrip().startswith('?') or 'error occurred' in l]
    meta['run']={'seconds':round(time.monotonic()-start,3),'timeout':timed,'returncode':rc,'errors':errors[:20],
        'last_marker':next((l for l in reversed(output.splitlines()) if l.startswith(('BEGIN_','END_'))),None),
        'output_sha256':hashlib.sha256(output.encode()).hexdigest()}
    complete='BEGIN_RESULT\n' in output and '\nEND_RESULT' in output and 'BEGIN_CONTROLS\n' in output and '\nEND_CONTROLS' in output
    if complete and not errors and rc==0:
        vals=output.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].strip().splitlines()
        controls=output.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].strip().splitlines()
        assert controls==['0','1'],controls
        assert len(vals)==3 and vals[0] in ('0','1'),vals
        meta['status']='UNIT-CANDIDATE-NEEDS-INDEPENDENT-REPLAY' if vals[0]=='0' else 'EXACT-Q-PROPER-AUGMENTED-IDEAL'
        meta['run'].update(reduce_one=vals[0],dimension_with_unused_t_z=int(vals[1]),basis_size=int(vals[2]),controls=controls)
    elif timed:meta['status']='COMPUTE-BOUND-OPEN'
    elif rc!=0 and ('omalloc' in output or 'memory' in output.lower() or rc in (-6,-9,-11)):
        meta['status']='MEMORY-BOUND-OPEN'
    else:meta['status']='CAS-ERROR-OPEN'
    save();print(branch,data['stage'],meta['status'],meta['run']['last_marker'],flush=True)

if __name__=='__main__':main()
