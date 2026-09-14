#!/usr/bin/env python3
"""Capture readonly worker and EC2 snapshots; explicit instance IDs only."""
from pathlib import Path
import json
import subprocess
import sys
root=Path(__file__).resolve().parent
mode=sys.argv[1]
if mode=='audit':
    ip=sys.argv[2]; label=sys.argv[3]
    if ip not in ('172.30.0.63','172.30.0.56'): raise SystemExit('wrong worker')
    with (root/'audit_worker.py').open('rb') as script:
        p=subprocess.run(['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=12',
                          'ubuntu@'+ip,'python3 -'],stdin=script,capture_output=True,check=True)
    data=json.loads(p.stdout)
    with (root/(label+'.json')).open('xb') as f: f.write(p.stdout)
    print(json.dumps({'host':data['hostname'],'utc':data['utc'],'processes':data['processes'],
                     'home_top_level':data['home_top_level'],'tmp_top_level':data['tmp_top_level'],
                     'dev_shm_top_level':data['dev_shm_top_level'],'df':data['df']},sort_keys=True))
elif mode=='ec2':
    data=json.loads(subprocess.check_output(['aws','ec2','describe-instances','--region','us-east-1',
        '--instance-ids','i-07e1212591a6acae9','i-0da0cebfc97c9fd54','--output','json'],text=True))
    with (root/(sys.argv[2]+'.json')).open('x') as f: json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
    print(json.dumps([{'id':i['InstanceId'],'state':i['State']['Name'],'tags':i.get('Tags',[]),
        'block_devices':i['BlockDeviceMappings']} for r in data['Reservations'] for i in r['Instances']],sort_keys=True))
else: raise SystemExit('unknown mode')
