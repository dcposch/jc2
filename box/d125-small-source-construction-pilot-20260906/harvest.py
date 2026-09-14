#!/usr/bin/env python3
"""Read only this terminal pilot tree; retain compact fresh final custody."""
import hashlib,json,os,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906')
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for data in iter(lambda:f.read(1048576),b''):h.update(data)
    return h.hexdigest()
def save(path,obj):
    with path.open('x') as out:json.dump(obj,out,sort_keys=True,indent=2);out.write('\n')
if Path.cwd()!=ROOT or Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()!='i-0da0cebfc97c9fd54':raise RuntimeError('wrong custody host/cwd')
terminal=json.loads((ROOT/'terminal-jobs.json').read_text())
controller=json.loads((ROOT/'controller.identity.json').read_text())
groups={j['telemetry']['pgid'] for j in terminal['jobs']};groups.add(controller['pgid'])
processes=subprocess.check_output(['ps','-eo','pid=,ppid=,pgid=,stat=,rss=,args='],text=True).splitlines()
remaining=[line for line in processes if int(line.split()[2]) in groups]
if remaining:raise RuntimeError('owned group not absent '+repr(remaining))
artifacts=[];cases=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file():artifacts.append({'path':str(path),'relative':str(path.relative_to(ROOT)),
                                       'bytes':path.stat().st_size,'sha256':sha(path)})
for case in ('unequal','common_3','common_4'):
    for branch in ('rational','golden'):
        directory=ROOT/(case+'-'+branch);result_path=directory/'case.result.json'
        if not result_path.exists():continue
        result=json.loads(result_path.read_text());manifest=result['manifest'];jsonl=directory/manifest['jsonl']['path']
        with jsonl.open('rb') as f:
            header=json.loads(f.readline());last=None
            for line in f:last=line
        footer=json.loads(last)
        if footer!=manifest['footer'] or sha(jsonl)!=manifest['jsonl']['sha256']:raise RuntimeError('terminal stream drift')
        save(directory/'header.json',header);save(directory/'footer.json',footer)
        cases.append({'case':case,'branch':branch,'header':header,'manifest':manifest,
                      'import_stdout':(directory/'import.stdout').read_text(),
                      'import_stderr':(directory/'import.stderr').read_text(),
                      'construct_seconds':result['constructor_telemetry']['wall_elapsed_seconds'],
                      'construct_RSS_bytes':result['constructor_telemetry']['max_observed_group_rss_bytes'],
                      'import_seconds':result['import_telemetry']['wall_elapsed_seconds'],
                      'import_RSS_bytes':result['import_telemetry']['max_observed_group_rss_bytes'],
                      'construct_pgid':result['constructor_telemetry']['pgid'],
                      'import_pgid':result['import_telemetry']['pgid']})
custody={'status':'ALL_OWNED_GROUPS_ABSENT','utc_epoch':time.time(),'instance_id':'i-0da0cebfc97c9fd54',
        'private_ip':'172.30.0.56','boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        'EBS':'vol-0eb6450d18ffa89f1','retention':'ROOT RETAINS RUNNING INSTANCE; NO STOP OR TERMINATE BY LANE',
        'validated_absent_pgids':sorted(groups),'remaining_owned_processes':remaining,
        'post_meminfo':Path('/proc/meminfo').read_text(),'artifacts_before_custody':artifacts,'cases':cases,
        'batch':json.loads((ROOT/'batch.result.json').read_text()) if (ROOT/'batch.result.json').exists() else None,
        'failure':json.loads((ROOT/'failure.json').read_text()) if (ROOT/'failure.json').exists() else None,
        'mathematical_verdict':'NONE: construction and import-only instrument telemetry'}
save(ROOT/'custody.json',custody)
print(json.dumps({'status':custody['status'],'cases':len(cases),'pgids':sorted(groups),
                  'batch_seconds':None if custody['batch'] is None else custody['batch']['arithmetic_batch_seconds'],
                  'custody_sha256':sha(ROOT/'custody.json')}))
