#!/usr/bin/env python3
"""One recoverable StopInstances call after explicit frozen readiness gates."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
root=Path(__file__).resolve().parent
INSTANCES={'63':('i-07e1212591a6acae9','vol-09c6e3133f3442e56','t2t3-longsolve-sol56-20260906'),
           '56':('i-0da0cebfc97c9fd54','vol-0eb6450d18ffa89f1','coordinator-factored-jacobian-20260906')}
def need(ok,why):
    if not ok: raise SystemExit(why)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name): return json.loads((root/name).read_text())
def save(name,data):
    with (root/name).open('x') as f: json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
checks={}
for suffix,(instance,volume,owner) in INSTANCES.items():
    before=load('pre'+suffix+'.json'); now=load('ready'+suffix+'.json'); arc=load('archive'+suffix+'.json')
    need(before['boot_id']==now['boot_id'],'boot changed')
    need(now['hostname']=='ip-172-30-0-'+suffix and arc['host']==now['hostname'],'worker mismatch')
    age=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(now['utc'])).total_seconds()
    need(0<=age<180,'readiness snapshot stale')
    current={p['pid']:p for p in now['processes']}
    chain=set(); pid=now['audit_pid']
    while pid in current and pid not in chain:
        chain.add(pid); pid=current[pid]['ppid']
    services={(tuple(p['argv']),p['cgroup']) for p in before['processes']
        if p['cgroup'].startswith('0::/system.slice/') or p['argv'] in (
             ['/sbin/init'],['/usr/lib/systemd/systemd','--user'],['(sd-pam)'],
             ['/usr/bin/dbus-daemon','--session','--address=systemd:','--nofork','--nopidfile','--systemd-activation','--syslog-only'])}
    unexpected=[p for p in now['processes'] if p['pid'] not in chain and (tuple(p['argv']),p['cgroup']) not in services]
    need(not unexpected,'unexpected live process owner '+repr(unexpected))
    disks=[d for d in json.loads(now['blocks'])['blockdevices'] if d['type']=='disk']
    need(len(disks)==1 and disks[0]['serial']==volume.replace('-',''),'non-EBS/unexpected disk')
    need(all(Path(e['path']).name.startswith('eic-hostkey-') for e in now['dev_shm_top_level']),'unexpected shared-memory artifact')
    if suffix=='63':
        monitor=load('monitor-cleanup.json'); need(monitor['after']==[],'monitor still live')
        need(set(arc['archive'])=={'/tmp/msolve-src-0101','/tmp/msolve-patched'},'archive scope')
        need(all(r['exact_content_and_modes_verified'] and r['source_retained'] for r in arc['archive'].values()),'archive not verified')
    else: need(len(arc['key_hashes'])==5,'full-J/binary retention gate missing')
    checks[instance]={'owner':owner,'volume':volume,'ready_sha256':sha(root/('ready'+suffix+'.json')),
        'archive_sha256':sha(root/('archive'+suffix+'.json')),'unexpected_live_processes':unexpected,
        'snapshot_age_seconds':age,'no_instance_store_disk':True}
ids=[v[0] for v in INSTANCES.values()]
desc=json.loads(subprocess.check_output(['aws','ec2','describe-instances','--region','us-east-1','--instance-ids',*ids,'--output','json'],text=True))
actual={i['InstanceId']:i for r in desc['Reservations'] for i in r['Instances']}
need(set(actual)==set(ids),'unexpected described instance')
for suffix,(iid,vid,owner) in INSTANCES.items():
    i=actual[iid]; tags={t['Key']:t['Value'] for t in i.get('Tags',[])}
    need(i['State']['Name']=='running' and i['PrivateIpAddress']=='172.30.0.'+suffix,'state/address drift')
    need(tags.get('Owner')==owner,'owner changed')
    need(len(i['BlockDeviceMappings'])==1 and i['BlockDeviceMappings'][0]['Ebs']['VolumeId']==vid,'EBS mapping drift')
save('stop-readiness.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,
 'authorization':'ROOT recoverable STOP of exact two IDs after terminal/ownership/storage gates; never TERMINATE',
 'pre_action_describe':desc})
response=json.loads(subprocess.check_output(['aws','ec2','stop-instances','--region','us-east-1','--instance-ids',*ids,'--output','json'],text=True))
save('stop-response.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response':response,
                        'action':'StopInstances','instance_ids':ids})
print(json.dumps(response,sort_keys=True))
