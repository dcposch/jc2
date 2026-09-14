#!/usr/bin/env python3
"""Harvest each declared terminal file and hash-verify local custody."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

root=Path(__file__).resolve().parent
evidence=root/'evidence'
pre=json.loads((evidence/'pre.json').read_text())
post=json.loads((evidence/'post.json').read_text())
storage=json.loads((root/'storage.json').read_text())
def need(ok,why):
    if not ok: raise SystemExit(why)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def values(text):
    return {line.split(':',1)[0]:line.split(':',1)[1].strip() for line in text.splitlines() if ':' in line}
def kib(text,key): return int(values(text)[key].split()[0])*1024
need(pre['hashes']==post['hashes'],'source/input drift')
need(post['group_members']==[],'registered group not empty')
for name,job in post['jobs'].items():
    dest=evidence/name; dest.mkdir()
    for rel,record in job['files'].items():
        need('/' not in rel and record['bytes']<1024*1024,'unexpected large/nested terminal artifact')
        source=job['run_dir']+'/'+rel
        subprocess.run(['scp','-q','-i','/home/ubuntu/.ssh/jc2-fleet',
            'ubuntu@172.30.0.63:'+source,str(dest/rel)],check=True)
        need(sha(dest/rel)==record['sha256'],'terminal artifact drift '+source)
    for line in job['postflight'].splitlines():
        digest,path=line.split(None,1)
        if path in post['hashes']: need(post['hashes'][path]==digest,'postflight input mismatch')
        else: need(sha(dest/Path(path).name)==digest,'postflight output mismatch')
    need(job['caprun']['start_identity']=='boot='+pre['boot_id']+';start_ticks='+str(pre['parents'][str(job['caprun']['pgid'])]['start_ticks']),
         'terminal leader identity differs from pre-stop snapshot')
need(post['jobs']['d2-z55-msolve']['files']['basis.ms']['bytes']==0,'unexpected msolve basis requires review')
sg=post['jobs']['d2-z55-singular']['stdout']
need(sg=='ALL_ROWS_PARSED\nBEGIN_STD\n\nhalt 1\n','unexpected Singular result requires review')
signals=[json.loads(line) for line in (evidence/'signal-actions.jsonl').read_text().splitlines()]
need({s['pid'] for s in signals}=={20597,20637} and all(s['signal']=='SIGTERM' for s in signals),'signal scope')
memory={'pre_utc':pre['utc'],'post_utc':post['utc'],
 'solver_pre_RSS_bytes':{pid:kib(r['status'],'VmRSS') for pid,r in pre['targets'].items()},
 'solver_pre_swap_bytes':{pid:kib(r['status'],'VmSwap') for pid,r in pre['targets'].items()},
 'pre_MemAvailable_bytes':kib(pre['meminfo'],'MemAvailable'),
 'post_MemAvailable_bytes':kib(post['meminfo'],'MemAvailable'),
 'pre_SwapTotal_bytes':kib(pre['meminfo'],'SwapTotal'),'post_SwapTotal_bytes':kib(post['meminfo'],'SwapTotal'),
 'pswpin_delta':post['swap_counters']['pswpin']-pre['swap_counters']['pswpin'],
 'pswpout_delta':post['swap_counters']['pswpout']-pre['swap_counters']['pswpout']}
files={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in root.rglob('*') if p.is_file()}
result={'schema':'DEGREE99_LONGSOLVE_OPERATOR_STOP/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'owner':'/root/model_productivity','instance':'i-07e1212591a6acae9','private_ip':'172.30.0.63',
 'authorization':'ROOT GREEN: stop only solverPIDs20597/20637, preserve wrappers/files, no instance action',
 'reason':'METHOD_ONLY: externally closed actual degree99; no named open client for remaining16h',
 'signals':signals,'terminal_group_members':[],'memory':memory,'storage':storage,
 'jobs':{n:{'run_dir':j['run_dir'],'runner_rc':int(j['runner_rc']),
             'caprun_status':j['caprun']['status'],'wall_elapsed_seconds':j['caprun']['wall_elapsed_seconds'],
             'classification':'OPERATOR_STOP / NO_COMPLETED_RESULT','output_hashes':j['files']}
         for n,j in post['jobs'].items()},
 'preserved_input_and_instrument_hashes':post['hashes'],
 'retained_roots':post['retained_roots_unmodified'],
 'no_instance_state_or_tag_mutation':True,'all_source_input_output_files_retained':True,
 'new_worker_custody_directory':'/home/ubuntu/degree99-longsolve-stop-astra-20260906',
 'files':files}
with (root/'custody.json').open('x') as f: json.dump(result,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'custody_sha256':sha(root/'custody.json'),'memory':memory,
    'terminal_pgids':[20596,20636],'classification':'OPERATOR_STOP / NO_COMPLETED_RESULT'},sort_keys=True))
