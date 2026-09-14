#!/usr/bin/env python3
"""Explicit source preservation and EBS checks; no solver or instance action."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import socket
import stat
import subprocess

host=socket.gethostname()
root=Path('/home/ubuntu/fleet-recoverable-stop-20260906')
if host not in ('ip-172-30-0-63','ip-172-30-0-56') or Path.cwd()!=root:
    raise SystemExit('wrong worker/root')
if Path('/sys/class/dmi/id/sys_vendor').read_text().strip()!='Amazon EC2': raise SystemExit('not EC2')
def need(ok,why):
    if not ok: raise SystemExit(why)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def manifest(tree):
    result={}
    for base,dirs,files in os.walk(tree,followlinks=False):
        for name in dirs+files:
            p=Path(base)/name; s=p.lstat(); rel=str(p.relative_to(tree))
            entry={'mode':stat.S_IMODE(s.st_mode)}
            if p.is_symlink(): entry.update(type='symlink',target=os.readlink(p))
            elif p.is_dir(): entry.update(type='directory')
            elif p.is_file(): entry.update(type='file',bytes=s.st_size,sha256=sha(p))
            else: raise SystemExit('unexpected special file '+str(p))
            result[rel]=entry
    return result
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host':host,
        'root':str(root),'archive':{},'retention':{}}
rootdev=Path('/').stat().st_dev
if host.endswith('-63'):
    need(sha(Path('/tmp/msolve-patched/bin/msolve'))=='da552c7c21d5339973fa6cc2157a171555af6d359ad7a4a392199702d5837530','original installed binary differs')
    for name in ('msolve-src-0101','msolve-patched'):
        src=Path('/tmp')/name; dst=root/name
        need(src.is_dir() and src.stat().st_dev==rootdev and not dst.exists(),'archive source/device/target')
        before=manifest(src)
        total=sum(e.get('bytes',0) for e in before.values())
        need(shutil.disk_usage(root).free>total+1024**3,'archive disk headroom')
        subprocess.run(['cp','-a','--',str(src),str(dst)],check=True,timeout=120)
        after=manifest(dst); original_after=manifest(src)
        need(before==after==original_after,'archive mismatch or original drift')
        record['archive'][str(src)]={'destination':str(dst),'files':before,
            'regular_bytes':total,'entries':len(before),'source_retained':True,'exact_content_and_modes_verified':True}
    paths=[Path('/home/ubuntu/t2t3-longsolve/presentations/d2-z55-source'),
           Path('/home/ubuntu/t2t3-longsolve/runs/d2-z55-msolve'),Path('/home/ubuntu/t2t3-longsolve/runs/d2-z55-singular')]
    expected={}
else:
    paths=[Path('/home/ubuntu')/name for name in ('factored-jacobian-pilot-20260906','factored-jacobian-root-replay-20260906',
       'factored-jacobian-review-20260906','full-j-solver-pilot-20260906','msolve-allocation-repair-20260906',
       'linear-c-structured-pilot-20260906','linear-c-discriminator-20260906','linear-c-root-replay-20260906','k16-gate-root-replay-20260906')]
    expected={
      '/home/ubuntu/factored-jacobian-pilot-20260906/complete_checked.sing':'50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091',
      '/home/ubuntu/factored-jacobian-pilot-20260906/complete_export.generators.jsonl':'39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f',
      '/home/ubuntu/full-j-solver-pilot-20260906/complete.slimgb.sing':'f87c0718b7df56c2b421a9d145e0e30d4e337ac2dca4a4c73d036033a55487cb',
      '/home/ubuntu/full-j-solver-pilot-20260906/complete.p1073741827.ms':'5a7f674325e9e8cb483234bd8b510f54bff387032498ed49ba76e084748517e2',
      '/home/ubuntu/msolve-allocation-repair-20260906/msolve-source/.libs/msolve':'175575870bf76a3c3a21c1660e1f6c7b8604a256fc4123643ce9711589326434'}
for p in paths:
    need(p.is_dir() and p.stat().st_dev==rootdev,'retention path missing/not on root filesystem '+str(p))
    record['retention'][str(p)]={'root_device':p.stat().st_dev,
      'mount':json.loads(subprocess.check_output(['findmnt','-J','-T',str(p)],text=True)),
      'top_files':[{'name':q.name,'bytes':q.stat().st_size} for q in p.iterdir() if q.is_file()]}
record['key_hashes']={p:sha(Path(p)) for p in expected}
need(record['key_hashes']==expected,'important input/binary hash drift')
record['df']=subprocess.check_output(['df','-B1',str(root)],text=True)
with (root/'archive-retention.json').open('x') as f: json.dump(record,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'host':host,'sha256':sha(root/'archive-retention.json'),
  'archived':{p:{k:v for k,v in item.items() if k!='files'} for p,item in record['archive'].items()},
  'retention_roots':list(record['retention']),'key_hashes':record['key_hashes'],'df':record['df']},sort_keys=True))
