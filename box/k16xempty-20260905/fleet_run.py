#!/usr/bin/env python3
"""One exact foreground Singular job on an explicitly named permitted worker."""
import argparse,hashlib,json,shlex,subprocess,time
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('host',choices=['172.30.0.7','172.30.0.18','172.30.0.28']);p.add_argument('script');p.add_argument('--timeout',type=int,default=1800);p.add_argument('--outputs',nargs='*',default=[])
a=p.parse_args();root=Path(__file__).resolve().parent
script=Path(a.script).resolve();name=script.stem
remote=f'/tmp/k16xempty-20260905-astra/{name}'
ssh=['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'-o','BatchMode=yes','-o','ConnectTimeout=10',f'ubuntu@{a.host}']
scp=['scp','-i',str(Path.home()/'.ssh/jc2-fleet'),'-o','BatchMode=yes','-o','ConnectTimeout=10']
dest=root/'fleet'/a.host/name;dest.mkdir(parents=True,exist_ok=True)
local=dest/script.name
local.write_text(script.read_text().replace(str(root),remote))
subprocess.run(ssh+[f'mkdir -p {shlex.quote(remote)}'],check=True)
subprocess.run(scp+[str(local),f'ubuntu@{a.host}:{remote}/{script.name}'],check=True)
cmd=f'cd {shlex.quote(remote)} && timeout -k 10 {a.timeout} stdbuf -oL -eL Singular --cpus=1 --threads=1 --flint-threads=1 --no-rc -q {shlex.quote(script.name)}'
start=time.time()
print(json.dumps({'phase':'start','host':a.host,'command':cmd}),flush=True)
with (dest/'stdout.log').open('w') as out,(dest/'stderr.log').open('w') as err:
    proc=subprocess.run(ssh+[cmd],stdout=out,stderr=err)
meta={'host':a.host,'command':cmd,'elapsed_seconds':time.time()-start,'returncode':proc.returncode,'script_sha256':hashlib.sha256(local.read_bytes()).hexdigest(),'cores':1}
for f in a.outputs:
    result=subprocess.run(scp+[f'ubuntu@{a.host}:{remote}/{f}',str(root/f)],capture_output=True,text=True)
    meta.setdefault('outputs',{})[f]={'returncode':result.returncode,'stderr':result.stderr}
(dest/'status.json').write_text(json.dumps(meta,indent=2)+'\n')
print((dest/'stdout.log').read_text(),end='',flush=True)
print(json.dumps(meta),flush=True)
