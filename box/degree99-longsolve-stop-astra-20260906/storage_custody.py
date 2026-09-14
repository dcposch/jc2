#!/usr/bin/env python3
"""Read-only EC2/EBS metadata for the sole authorized worker."""
from pathlib import Path
import datetime
import json
import subprocess
root=Path(__file__).resolve().parent
def aws(*args):
    return json.loads(subprocess.check_output(['aws','ec2',*args,'--region','us-east-1','--output','json'],text=True))
data=aws('describe-instances','--instance-ids','i-07e1212591a6acae9')
instances=[i for r in data['Reservations'] for i in r['Instances']]
if len(instances)!=1 or instances[0]['InstanceId']!='i-07e1212591a6acae9':
    raise SystemExit('unexpected instance')
instance=instances[0]
volumes=[m['Ebs']['VolumeId'] for m in instance['BlockDeviceMappings'] if 'Ebs' in m]
if volumes!=['vol-09c6e3133f3442e56']: raise SystemExit('unexpected EBS mapping; review required')
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'instance':{k:instance.get(k) for k in ('InstanceId','State','RootDeviceName','RootDeviceType','BlockDeviceMappings','Tags','PrivateIpAddress','InstanceType','Placement')},
 'volumes':aws('describe-volumes','--volume-ids',*volumes),
 'actions':'read-only describes; no stop/termination/retag'}
with (root/'storage.json').open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps(out,sort_keys=True))
