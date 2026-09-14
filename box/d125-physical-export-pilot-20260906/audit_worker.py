#!/usr/bin/env python3
"""Read-only readiness audit for the one explicitly registered EC2 worker."""
import hashlib,json,os,platform,subprocess,time
from pathlib import Path

def run(argv):
    p=subprocess.run(argv,capture_output=True,text=True,timeout=20)
    if p.returncode: raise RuntimeError((argv,p.returncode,p.stderr))
    return p.stdout
def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()
def need(ok,text):
    if not ok: raise RuntimeError(text)

host=platform.node();instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip()
need(platform.system()=='Linux' and host=='ip-172-30-0-56' and instance=='i-0da0cebfc97c9fd54' and vendor=='Amazon EC2','UNREGISTERED HOST')
pins={
 '/home/ubuntu/full-j-solver-pilot-20260906/run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2',
 '/home/ubuntu/factored-jacobian-pilot-20260906/complete_checked.sing':'50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091',
 '/home/ubuntu/factored-jacobian-pilot-20260906/complete_export.generators.jsonl':'39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f'}
actual={p:digest(p) for p in pins}
need(actual==pins,'CUSTODY PIN DRIFT')
blocks=json.loads(run(['lsblk','-J','-b','-o','NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL']))
disks=[d for d in blocks['blockdevices'] if d['type']=='disk']
need(len(disks)==1 and disks[0]['serial']=='vol0eb6450d18ffa89f1','EBS mismatch/extra disk')
mount=run(['findmnt','-T','/home/ubuntu','-n','-o','SOURCE,FSTYPE,TARGET']).strip()
need(mount.split()==['/dev/nvme0n1p1','ext4','/'],'unexpected task filesystem')
mem={line.split(':')[0]:int(line.split()[1])*1024 for line in Path('/proc/meminfo').read_text().splitlines() if len(line.split())>=3 and line.split()[1].isdigit()}
need(mem['MemAvailable']>32*1024**3,'insufficient memory')
fs=os.statvfs('/home/ubuntu');free=fs.f_bavail*fs.f_frsize
need(free>4*1024**3,'insufficient EBS free space')
processes=run(['ps','-eo','pid,ppid,pgid,stat,rss,etimes,args','--sort=-rss'])
suspects=[]
for line in processes.splitlines()[1:]:
    parts=line.split(None,6)
    if len(parts)<7: continue
    pid,ppid,pgid,stat,rss,age,argv=parts
    if any(s in argv for s in ('Singular','msolve','run_capped.py','factored-jacobian','linear-c-','d125-physical-export-pilot')):
        suspects.append(line)
need(not suspects,'unexpected campaign/autostart arithmetic')
singular=run(['sh','-c','command -v Singular']).strip()
result={'utc':time.time(),'audit_pid':os.getpid(),'host':host,'instance_id':instance,'vendor':vendor,
 'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'cgroup':Path('/proc/self/cgroup').read_text(),
 'pid_namespace':os.readlink('/proc/self/ns/pid'),'mount':mount,'blocks':blocks,'free_disk_bytes':free,
 'memory':mem,'processes':processes,'suspects':suspects,'source_pins':actual,'singular_path':singular,
 'singular_sha256':digest(singular),'singular_version':run([singular,'--version']),
 'python_version':run(['/usr/bin/python3','--version']),'status':'READY_READONLY'}
print(json.dumps(result,sort_keys=True,indent=2))
