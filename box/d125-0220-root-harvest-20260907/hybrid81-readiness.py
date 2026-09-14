"""Read-only stdin host check, only on the exact root-started retained worker."""
from pathlib import Path
import hashlib,json,os,platform,socket,subprocess,time
INSTANCE='i-0da0cebfc97c9fd54';W=Path('/home/ubuntu/d125-hybrid81-exact-solver-20260907')
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
h=dict(utc=time.time(),system=platform.system(),hostname=socket.gethostname(),vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip())
need(h['system']=='Linux' and h['vendor']=='Amazon EC2' and h['instance']==INSTANCE,'exact registered EC2 host')
h.update(ebs=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),mount=subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','/'],text=True),disk=subprocess.check_output(['df','-Pk','/home/ubuntu'],text=True),memory=subprocess.check_output(['free','-m'],text=True),processes=subprocess.check_output(['ps','-eo','pid,ppid,pgid,lstart,stat,args'],text=True),services=subprocess.check_output(['systemctl','list-units','--type=service','--state=running','--no-pager'],text=True),new_cwd_lexists=os.path.lexists(W))
need(h['ebs']=='vol0eb6450d18ffa89f1','sole retained EBS')
expected={'/usr/bin/python3':'a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223','/usr/bin/prlimit':'17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069','/usr/bin/Singular':'90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4','/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl':'b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','/home/ubuntu/d125-hybrid-affine-pilot-20260907/construction.jsonl':'4ea526b2680ef41154332be3059ae5543c2678fdf8fb6a95d02176e8eb929272'}
h['pins']={p:sha(p) for p in expected};h['source_access']='Opaque byte hashing only, no parsing/arithmetic'
need(h['pins']==expected,'physical pins')
need(not h['new_cwd_lexists'],'fresh cwd occupied')
mem={line.split(':')[0]:int(line.split()[1]) for line in Path('/proc/meminfo').read_text().splitlines()}
need(mem['MemAvailable']>=20*1024**2 and mem['SwapTotal']==0,'memory/swap readiness')
h['reader_identity']=dict(pid=os.getpid(),pgid=os.getpgrp(),start_ticks=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],namespace=os.readlink('/proc/self/ns/pid'),cgroup=Path('/proc/self/cgroup').read_text())
print(json.dumps(h,sort_keys=True))
