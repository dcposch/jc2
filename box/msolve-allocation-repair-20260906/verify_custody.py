#!/usr/bin/env python3
"""Short local hash/control audit; no solver invocation or remote action."""
from pathlib import Path
import hashlib
import json
root=Path(__file__).resolve().parent
evidence=root/'evidence'
custody=json.loads((evidence/'custody.json').read_text())
def need(ok,why):
    if not ok: raise SystemExit(why)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
verified=[]
for name,rec in custody['files'].items():
    candidates=[evidence/name,root/name]
    if name=='boundary-v2.c': candidates.append(root/'boundary.c')
    if name=='REGISTRATION-final.md': candidates.append(root/'REGISTRATION.md')
    found=next((p for p in candidates if p.is_file() and sha(p)==rec['sha256']),None)
    if found: verified.append(name)
    elif name not in ('boundary','REGISTRATION.md'):
        raise SystemExit('missing/drifted charged artifact '+name)
for name,digest in custody['sources'].items():
    need(sha(evidence/'source'/name)==digest,'source drift '+name)
for n in ('build','upgrade','tests-retry'):
    t=custody['terminal_stages'][n]
    need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0,'required stage '+n)
need(custody['live_registered_group_members']==[],'live group')
need(custody['build_test_elapsed_seconds']<1200,'arithmetic cap')
need(custody['max_observed_group_rss_bytes']<16*1024**3,'RSS cap')
for n in ('build','upgrade'):
    data=(evidence/(n+'.stdout')).read_text()
    need('# TOTAL: 64' in data and '# PASS:  64' in data and '# FAIL:  0' in data,'upstream test census')
result={'verified_remote_artifacts':sorted(verified),'source_files':len(custody['sources']),
        'remote_only_hashed':[n for n in custody['files'] if n not in verified],
        'custody_sha256':sha(evidence/'custody.json'),'status':'PASS'}
with (root/'local-verification-v2.json').open('x') as f:
    json.dump(result,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps(result,sort_keys=True))
