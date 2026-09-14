#!/usr/bin/env python3
"""Fresh exact-host identity/control/import exec; never creates an inner PGID."""
import json, os, platform, resource, signal, sys, time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906')
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def save(path,obj):
    with Path(path).open('x') as out:
        json.dump(obj,out,sort_keys=True,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
def identity():
    need(platform.system()=='Linux','not Linux')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','not EC2')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','wrong DMI')
    ready=json.loads((ROOT/'readiness.json').read_text())
    boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    need(boot==ready['boot_id'],'boot drift')
    cwd=Path.cwd().resolve();need(cwd==ROOT or ROOT in cwd.parents,'wrong cwd')
    fields=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()
    return {'pid':os.getpid(),'pgid':os.getpgrp(),'start_ticks':fields[19],'boot_id':boot,
            'cwd':str(cwd),'cgroup':Path('/proc/self/cgroup').read_text(),
            'pid_namespace':os.readlink('/proc/self/ns/pid'),'argv':sys.argv,'utc':time.time()}
mode=sys.argv[1];ident=identity();save(mode+'.identity.json',ident)
if mode=='identity':
    print(json.dumps(ident),flush=True)
elif mode=='orphan':
    child=os.fork()
    if child==0:
        signal.signal(signal.SIGTERM,signal.SIG_IGN)
        save('orphan.descendant.json',identity())
        time.sleep(20);os._exit(0)
    print(json.dumps({'leader':os.getpid(),'child':child,'pgid':os.getpgrp()}),flush=True)
    os._exit(0)
elif mode=='import':
    import hashlib
    manifest=json.loads(Path(sys.argv[2]).read_text());item=manifest['singular']
    path=Path(item['path']);data=path.read_bytes()
    need(hashlib.sha256(data).hexdigest()==item['sha256'],'import input drift')
    need(Path.cwd()==ROOT/Path.cwd().name,'wrong import cwd')
    need(data.endswith(b';\nprint("D125_COMPLETE_LITERAL_IMPORT_ONLY");\nprint(size(I));\nquit;\n'),'not registered import-only suffix')
    import re
    need(not re.search(rb'\b(std|slimgb|groebner|eliminate|dim|solve|msolve)\s*\(',data),'forbidden algorithm')
    resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
    ready=json.loads((ROOT/'readiness.json').read_text())
    binary=Path(ready['singular_path'])
    need(hashlib.sha256(binary.read_bytes()).hexdigest()==ready['singular_sha256'],'binary drift')
    os.execv(str(binary),[str(binary),'-q',str(path)])
else: raise RuntimeError('unknown payload mode')
