#!/usr/bin/env python3
"""Certify R003=R002 as polynomial presentations and reuse bounded results."""
import gzip,hashlib,json
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent

def certify():
    cases={c['id']:c for c in json.loads((HERE/'run_cases.json').read_text())}
    a,b=cases['R002'],cases['R003']
    keys=['n','m','K','e','q','ell','W','variables','rows_sha256','coefficient_coordinate_sha256']
    for key in keys: assert a[key]==b[key],key
    def formula(c):
        p=runner.ROOT/c['lambda_path'];return gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
    assert formula(a)==formula(b)
    receipt={'source':'R002','receiver':'R003','status':'EXACT_IDENTICAL_PRESENTATION',
             'coefficient_field':'Q','verified_identical_fields':keys,
             'coefficient_map':'Every coefficient variable maps identically in the printed ordered list; Z,ss and T map identically.',
             'variables':a['variables'],'jacobian_rows_sha256':a['rows_sha256'],
             'lambda_raw_sha256':a['lambda_sha256'],
             'image_checks':'Full ordered coefficient row bytes and full decompressed leader bytes agree; all weights and localizer exponents agree.'}
    runner.persist_small(HERE/'R003-R002-identity.json',json.dumps(receipt,indent=2)+'\n')
    return cases

def alias():
    certify()
    identity_sha=hashlib.sha256((HERE/'R003-R002-identity.json').read_bytes()).hexdigest()
    for source in sorted(HERE.glob('R002*.N*.json')):
        if '.charge0.' in source.name:continue # independently executed for R003
        d=json.loads(source.read_text());prior=d['status']
        target=HERE/source.name.replace('R002','R003',1)
        if target.exists():
            old=json.loads(target.read_text())
            assert old['status'] in ('REUSED_IDENTICAL_PRESENTATION','EXACT_TARGET_BOUND_BELOW_KELLER_ROW'),target
        d.update(case=d['case'].replace('R002','R003',1),status='REUSED_IDENTICAL_PRESENTATION',source_status=prior,
                 source_receipt=source.name,identity_receipt='R003-R002-identity.json',
                 source_receipt_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                 identity_receipt_sha256=identity_sha,
                 source_wall_seconds=d.get('wall_seconds'),wall_seconds=0,
                 source_peak_rss_bytes=d.get('peak_rss_bytes'),peak_rss_bytes=None,
                 note='No second expensive CAS run: exact ordered presentation identity, not a name-based or numerical extrapolation.')
        for key in ('runner_pid','process_pid','process_group'):
            if key in d:d['source_'+key]=d.pop(key)
        runner.persist_small(target,json.dumps(d,indent=2)+'\n')

if __name__=='__main__':alias()
