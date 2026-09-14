#!/usr/bin/env python3
"""Fetch compact terminal evidence only; dense literal streams stay on EBS."""
import hashlib,json,subprocess
from pathlib import Path
BOX=Path(__file__).resolve().parent;OUT=BOX/'evidence';OUT.mkdir()
REMOTE='/home/ubuntu/d125-small-source-construction-pilot-20260906/'
SCP=['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes']
def get(relative):
    target=OUT/relative;target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():raise RuntimeError('refuse local overwrite')
    subprocess.run(SCP+['ubuntu@172.30.0.56:'+REMOTE+relative,str(target)],check=True,timeout=20)
    return target
custody_path=get('custody.json')
if hashlib.sha256(custody_path.read_bytes()).hexdigest()!='601643fcd066c19a24b04e22a0374c7e9fd5f106b0bfb5be43c695eb8c1b23b9':raise RuntimeError('custody pin mismatch')
custody=json.loads(custody_path.read_text());pins={}
for item in custody['artifacts_before_custody']:
    name=item['relative']
    if name.endswith(('.jsonl','.sing','.pyc')):continue
    path=get(name)
    got=hashlib.sha256(path.read_bytes()).hexdigest()
    if got!=item['sha256']:raise RuntimeError('remote evidence drift '+name)
    pins[name]=got
for case in custody['cases']:
    for leaf in ('header.json','footer.json'):
        name=case['case']+'-'+case['branch']+'/'+leaf
        path=get(name);pins[name]=hashlib.sha256(path.read_bytes()).hexdigest()
with (BOX/'pull-manifest.json').open('x') as out:
    json.dump({'files':pins,'custody_sha256':hashlib.sha256(custody_path.read_bytes()).hexdigest(),
               'dense_inputs_retained_remote':True,'all_hashes_match':True},out,sort_keys=True,indent=2);out.write('\n')
print(json.dumps({'status':'PULLED_VERIFIED','files':len(pins),'cases':[{
    'case':c['case'],'branch':c['branch'],'construction_s':c['construct_seconds'],
    'import_s':c['import_seconds'],'construct_RSS':c['construct_RSS_bytes'],'import_RSS':c['import_RSS_bytes'],
    'jsonl':c['manifest']['jsonl'],'singular':c['manifest']['singular'],
    'import_stdout':c['import_stdout'],'unused':c['manifest']['footer']['unused_variables']}
    for c in custody['cases']]}))
