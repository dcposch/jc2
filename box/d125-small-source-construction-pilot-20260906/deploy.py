#!/usr/bin/env python3
"""Exact one-worker read-only readiness, then fresh-directory deployment."""
import hashlib,json,subprocess
from pathlib import Path
BOX=Path(__file__).resolve().parent
CAMPAIGN=BOX.parents[1]
REMOTE='/home/ubuntu/d125-small-source-construction-pilot-20260906'
SSH=['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=10',
     '-o','StrictHostKeyChecking=yes','ubuntu@172.30.0.56']
def save(name,obj):
    with (BOX/name).open('x') as f:json.dump(obj,f,sort_keys=True,indent=2);f.write('\n')
run=subprocess.run(['aws','ec2','describe-instances','--instance-ids','i-0da0cebfc97c9fd54',
                    '--output','json'],capture_output=True,text=True,check=True,timeout=30)
aws=json.loads(run.stdout);instance=aws['Reservations'][0]['Instances'][0]
if instance['State']['Name']!='running' or instance['PrivateIpAddress']!='172.30.0.56':raise RuntimeError('wrong AWS state')
if {t['Key']:t['Value'] for t in instance['Tags']}.get('Owner')!='coordinator-factored-jacobian-20260906':raise RuntimeError('owner drift')
if [b['Ebs']['VolumeId'] for b in instance['BlockDeviceMappings']]!=['vol-0eb6450d18ffa89f1']:raise RuntimeError('EBS drift')
save('aws-state.json',aws)
source=r'''
import hashlib,json,os,platform,shutil,subprocess
from pathlib import Path
root=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906')
if root.exists():raise RuntimeError('fresh remote directory already exists')
vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip()
instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
if platform.system()!='Linux' or vendor!='Amazon EC2' or instance!='i-0da0cebfc97c9fd54':raise RuntimeError('DMI mismatch')
mount=subprocess.check_output(['findmnt','-T','/home/ubuntu','-n','-o','SOURCE,FSTYPE,TARGET'],text=True).split()
serial=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip()
if mount!=['/dev/nvme0n1p1','ext4','/'] or serial!='vol0eb6450d18ffa89f1':raise RuntimeError('not exact EBS')
disk=shutil.disk_usage('/home/ubuntu')
if disk.free<2*1024**3:raise RuntimeError('insufficient bounded output space')
singular=shutil.which('Singular')
if not singular:raise RuntimeError('Singular missing; no installation authority')
print(json.dumps({'system':platform.system(),'hostname':platform.node(),'instance_id':instance,'vendor':vendor,
'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'mount':mount,'ebs_serial':serial,
'disk':dict(zip(('total','used','free'),disk)),'meminfo':Path('/proc/meminfo').read_text(),
'processes':subprocess.check_output(['ps','-eo','pid,ppid,pgid,stat,rss,args'],text=True),
'timers':subprocess.check_output(['systemctl','list-timers','--all','--no-pager'],text=True),
'singular_path':singular,'singular_sha256':hashlib.sha256(Path(singular).read_bytes()).hexdigest(),
'singular_package':subprocess.check_output(['dpkg-query','-W','singular'],text=True)}))
'''
ready_run=subprocess.run(SSH+['python3 -'],input=source,capture_output=True,text=True,check=True,timeout=30)
ready=json.loads(ready_run.stdout);save('readiness.json',ready)
subprocess.run(SSH+['mkdir '+REMOTE],check=True,timeout=15)
inputs={'REGISTRATION.md':BOX/'REGISTRATION.md','payload.py':BOX/'payload.py','pilot.py':BOX/'pilot.py',
        'readiness.json':BOX/'readiness.json','run_capped.py':CAMPAIGN/'ops/run_capped.py',
        'frontier_gate.py':CAMPAIGN/'ops/frontier_gate.py',
        'exporter.py':CAMPAIGN/'box/d125-small-source-exporter-prep-20260906/exporter.py',
        'baseline.py':CAMPAIGN/'box/d125-small-source-exporter-prep-20260906/baseline.py'}
pins={}
for name,path in inputs.items():
    pins[name]=hashlib.sha256(path.read_bytes()).hexdigest()
    subprocess.run(['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes',
                    '-o','StrictHostKeyChecking=yes',str(path),'ubuntu@172.30.0.56:'+REMOTE+'/'+name],check=True,timeout=30)
check=subprocess.run(SSH+['cd '+REMOTE+' && sha256sum '+' '.join(inputs)],capture_output=True,text=True,check=True,timeout=30)
actual={line.split()[1]:line.split()[0] for line in check.stdout.splitlines()}
if actual!=pins:raise RuntimeError('deployed pin mismatch')
save('deployment.json',{'root':REMOTE,'pins':pins,'all_match':True})
print(json.dumps({'status':'DEPLOYED_UNEXECUTED','boot':ready['boot_id'],'disk_free':ready['disk']['free'],'pins':pins}))
