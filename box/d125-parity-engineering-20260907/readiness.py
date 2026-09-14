import hashlib,json,os,platform,socket,subprocess,time
from pathlib import Path
work=Path('/home/ubuntu/d125-parity-compression-pilot-20260907')
out=dict(utc=time.time(),system=platform.system(),hostname=socket.gethostname(),
         vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
         instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
         boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
         work_absent=not work.exists(),
         binaries={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['/usr/bin/python3','/usr/bin/prlimit']},
         disk=subprocess.check_output(['df','-Pk','/home/ubuntu'],text=True),
         memory=subprocess.check_output(['free','-m'],text=True),
         ebs=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),
         mount=subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','/'],text=True),
         ubuntu_processes=subprocess.check_output(['ps','-u','ubuntu','-o','pid,pgid,lstart,args'],text=True))
if not(out['system']=='Linux' and out['vendor']=='Amazon EC2' and out['instance']=='i-0da0cebfc97c9fd54'
       and out['boot']=='1a830d1e-1fa2-47f3-98bc-8c26c8cb8453' and out['work_absent']
       and out['ebs']=='vol0eb6450d18ffa89f1'
       and out['binaries']['/usr/bin/python3']=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223'
       and out['binaries']['/usr/bin/prlimit']=='17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069'):
    raise ValueError('fresh readiness mismatch')
print(json.dumps(out,sort_keys=True))
