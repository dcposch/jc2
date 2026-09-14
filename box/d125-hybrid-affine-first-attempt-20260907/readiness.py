"""Read-only host/custody snapshot, supplied by stdin only after root RUNNING."""
from pathlib import Path
import hashlib,json,os,platform,socket,subprocess,time
INSTANCE='i-0da0cebfc97c9fd54'
WORK=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
SOURCE=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl')
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
host=dict(utc=time.time(),system=platform.system(),hostname=socket.gethostname(),
          vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
          instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
          boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip())
need(host['system']=='Linux' and host['vendor']=='Amazon EC2' and host['instance']==INSTANCE,'wrong host; stop before custody reads')
host.update(ebs=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),
            mount=subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','/'],text=True),
            disk=subprocess.check_output(['df','-Pk','/home/ubuntu'],text=True),
            memory=subprocess.check_output(['free','-m'],text=True),
            processes=subprocess.check_output(['ps','-eo','pid,ppid,pgid,lstart,stat,args'],text=True),
            executables={p:sha(p) for p in ('/usr/bin/python3','/usr/bin/prlimit')},
            work_lexists=os.path.lexists(WORK),
            production_paths={n:os.path.lexists(WORK/n) for n in ('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr','pilot.telemetry.json','authority.json','ROOT-GREEN.md')},
            source_file=dict(path=str(SOURCE),bytes=SOURCE.stat().st_size,access='stat only; no content read'),
            reader_identity=dict(pid=os.getpid(),pgid=os.getpgrp(),start_ticks=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],cgroup=Path('/proc/self/cgroup').read_text(),namespace=os.readlink('/proc/self/ns/pid')))
need(host['ebs']=='vol0eb6450d18ffa89f1','EBS mismatch')
need(host['executables']=={'/usr/bin/python3':'a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223','/usr/bin/prlimit':'17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069'},'executable drift')
print(json.dumps(host,sort_keys=True))
need(not host['work_lexists'] and not any(host['production_paths'].values()),'new workdir/output already present; retain snapshot, no deployment')
