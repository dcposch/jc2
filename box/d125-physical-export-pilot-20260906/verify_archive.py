#!/usr/bin/env python3
"""Verify/extract this owned terminal metadata archive; no production arithmetic."""
import hashlib,json,os,tarfile
from pathlib import Path,PurePosixPath
HERE=Path(__file__).resolve().parent
archive=HERE/'evidence.tar'
claimed=json.loads((HERE/'harvest.stdout').read_text())
def need(ok,s):
    if not ok:raise RuntimeError(s)
def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
need(digest(archive)==claimed['archive_sha256'],'archive hash')
out=HERE/'evidence';out.mkdir()
with tarfile.open(archive,'r') as tar:
    members=tar.getmembers();names=set()
    for member in members:
        path=PurePosixPath(member.name)
        need(member.isfile() and not path.is_absolute() and '..' not in path.parts and member.name not in names,'unsafe archive member')
        names.add(member.name)
    tar.extractall(out,filter='data')
custody=json.loads((out/'custody.json').read_text())
need(digest(out/'custody.json')==claimed['custody_sha256'],'custody hash')
retained=[];checked=[]
for rec in custody['all_artifacts']:
    name=rec['relative']
    if name in ('complete/literal.jsonl','complete/import.sing'):
        need(not (out/name).exists(),'dense input unexpectedly copied')
        retained.append(rec);continue
    p=out/name
    need(p.is_file() and p.stat().st_size==rec['bytes'] and digest(p)==rec['sha256'],'artifact mismatch '+name)
    checked.append(name)
for p in out.rglob('*'):
    if p.is_file():os.chmod(p,0o444)
result={'status':'PASS','checked_small_artifacts':len(checked),'retained_remote_dense_artifacts':retained,
        'custody_sha256':claimed['custody_sha256'],'archive_sha256':claimed['archive_sha256'],
        'no_production_arithmetic_local':True}
with (HERE/'archive-verification.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(result,sort_keys=True))
