#!/usr/bin/env python3
"""Completion audit; exact custody and integer certificates, bounded output."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re

root = Path(__file__).resolve().parent
report = root.parent.parent/'xmodel/k16-f3abel-astra-20260905.md'

def mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out

def add(a,b):
    out = [0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i] += x
    for i,x in enumerate(b): out[i] += x
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sealed', action='store_true')
    args = ap.parse_args()
    checks = {}
    for line in (root/'inputs.sha256').read_text().splitlines():
        digest, path = line.split(None,1)
        assert hashlib.sha256(Path(path.strip()).read_bytes()).hexdigest() == digest
    checks['frozen_hashes'] = 10
    expectations = {
        'controls_t2_d-1.log':('GB_DONE dim=1 vdim=-1','target_nf=0\n','target2_nf=0\n'),
        'controls_t2_d1.log':('GB_DONE dim=0 vdim=12','target_nf=0\n','target2_nf=0\n'),
        'controls_t3.log':('GB_DONE dim=0 vdim=66','target2_nf=0\n'),
        'controls_t4.log':('GB_DONE dim=0 vdim=338','target2_nf=0\n'),
        'controls_t2_certificate.log':('EXACT_IDENTITY_PASS','T2_CERTIFICATES_DONE'),
        'infinity_structure.log':('INFINITY_AND_LOCAL_STRUCTURE_DONE',),
        'rootcover_identities.log':('_PASS',),
        'controls_uniform_identities.log':('B2_AXIS_NORM_PASS',),
    }
    for name,markers in expectations.items():
        data=(root/name).read_text()
        for marker in markers: assert marker in data,(name,marker)
        assert not re.search(r'FAIL|Traceback|error occurred|div\. by 0',data),name
        if name in ('controls_t3.log','controls_t4.log'):
            nf=next(line.partition('=')[2] for line in data.splitlines() if line.startswith('target_nf='))
            assert nf!='0',name
    checks['exact_control_logs'] = len(expectations)
    for t,m in ((11,2),(26,3),(47,4)):
        for sign in ('plus','minus'):
            name=f'rigidity_coincident_t{t}_d{sign}{m}.log'
            data=(root/name).read_text()
            assert 'GCD 1 USED_ROWS' in data,name
            assert 'INTEGER_BEZOUT_IDENTITY_EXACT_PASS' in data,name
            assert 'NO_NORMALIZED_SOLUTION_ON_SHIFTED_COINCIDENT_ROOT_SLICE' in data,name
            assert 'Traceback' not in data and 'FAIL' not in data,name
    checks['exact_split_factor_logs'] = 6
    for sign in ('plus','minus'):
        obj=json.loads((root/f'rigidity_coincident_t11_d{sign}2_certificate.json').read_text())
        a,b,c=map(int,obj['f_coefficients_descending'])
        A,B,C=map(int,obj['g_coefficients_descending'])
        Delta=a*B-A*b; eps=a*C-A*c
        N=a*eps*eps-b*eps*Delta+c*Delta*Delta
        assert Delta==int(obj['Delta']) and eps==int(obj['epsilon']) and N==int(obj['N']) and N
        ell=[b*Delta-a*eps,a*Delta]
        lhs=add(mul(add([Delta*Delta],[A*v for v in ell]),[c,b,a]),
                [-v for v in mul([a*v for v in ell],[C,B,A])])
        assert lhs==[N,0,0,0]
    checks['integer_certificates_independently_verified'] = 2
    text=report.read_text()
    assert 20000<=len(text.encode())<=45000
    assert '_PENDING' not in text
    assert '**PARTIAL.' in text and 'OPEN[K16-8.1-RADICAL]' in text
    assert 'at every geometric point' in text
    outcomes=json.loads((root/'run_outcomes.json').read_text())
    assert outcomes['all_lane_jobs_finished'] is True
    if args.sealed:
        assert outcomes['final_audit_pass'] is True
    # Inspect only processes whose command lines identify this lane's CAS drivers.
    live=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit(): continue
        try:
            cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (OSError,ProcessLookupError): continue
        if str(root) not in cmd and 'box/k16f3abel-20260905/' not in cmd: continue
        if 'python3 ' in cmd and 'final_audit.py' not in cmd:
            live.append((proc.name,cmd))
        if 'Singular ' in cmd:
            live.append((proc.name,cmd))
    assert not live,live
    checks['lane_cas_jobs_remaining'] = 0
    lines=text.splitlines(keepends=True)
    markers=[i for i,line in enumerate(lines) if line.strip()=='<!-- BODY-END -->']
    if args.sealed:
        assert len(markers)==1
        body=''.join(lines[:markers[0]+1]).encode()
        tail=''.join(lines[markers[0]+1:])
        assert f'Body bytes: `{len(body)}`' in tail
        assert hashlib.sha256(body).hexdigest() in tail
        checks['sealed_body_bytes']=len(body)
        checks['sealed_body_sha256']=hashlib.sha256(body).hexdigest()
    else:
        assert not markers
    checks['status']='PASS'
    checks['sealed']=args.sealed
    if not args.sealed:
        outcomes['final_audit_pass']=True
        (root/'run_outcomes.json').write_text(json.dumps(outcomes,indent=2)+'\n')
    (root/'artifact_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,sort_keys=True),flush=True)

if __name__=='__main__': main()
