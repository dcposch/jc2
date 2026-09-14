#!/usr/bin/env python3
"""Bounded read-only status waits: 10 s sleeps, 30 s API-call ceilings."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import time
root=Path(__file__).resolve().parent
ids=['i-07e1212591a6acae9','i-0da0cebfc97c9fd54']
def save(name,data):
    with (root/name).open('x') as f: json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
records=[]
for i in range(12):
    result=json.loads(subprocess.check_output(['aws','ec2','describe-instances','--region','us-east-1',
        '--instance-ids',*ids,'--output','json'],text=True,timeout=30))
    actual={x['InstanceId']:x for r in result['Reservations'] for x in r['Instances']}
    if set(actual)!=set(ids): raise SystemExit('unexpected response instance')
    states={k:v['State']['Name'] for k,v in actual.items()}
    record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'states':states}
    records.append(record); save('poll-'+str(i)+'.json',record)
    print(json.dumps(record,sort_keys=True),flush=True)
    if set(states.values())=={'stopped'}:
        save('ec2-stopped.json',result)
        volumes=json.loads(subprocess.check_output(['aws','ec2','describe-volumes','--region','us-east-1',
            '--volume-ids','vol-09c6e3133f3442e56','vol-0eb6450d18ffa89f1','--output','json'],text=True,timeout=30))
        save('volumes-retained.json',volumes)
        files={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in root.iterdir() if p.is_file()}
        save('custody.json',{'schema':'RECOVERABLE_FLEET_STOP/v1','utc':record['utc'],
            'owner':'/root/model_productivity','coordinator_retains_instances':True,
            'instance_states':states,'instances':actual,'volumes':volumes,'polls':records,
            'action':'StopInstances only; no termination, tag edits, volume deletion, overwrite or source removal',
            'archive63':json.loads((root/'archive63.json').read_text()),
            'retention56':json.loads((root/'archive56.json').read_text()),
            'monitor_cleanup':json.loads((root/'monitor-cleanup.json').read_text()),
            'files':files})
        print('BOTH_STOPPED_CUSTODY_COMPLETE',flush=True)
        break
    time.sleep(10)
else: raise SystemExit('bounded observation ended before both stopped; report pending state')
