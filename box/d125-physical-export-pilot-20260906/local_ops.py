#!/usr/bin/env python3
"""Scoped transport/metadata only. Never computes the production ideal locally."""
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
SSH=['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=12','ubuntu@172.30.0.56']
mode=sys.argv[1]
if mode=='audit':
    with (HERE/'audit_worker.py').open('rb') as f:
        p=subprocess.run(SSH+['python3 -'],stdin=f,capture_output=True,timeout=60)
    with (HERE/'readiness.stdout').open('xb') as f:f.write(p.stdout)
    with (HERE/'readiness.stderr').open('xb') as f:f.write(p.stderr)
    if p.returncode: raise SystemExit(p.stderr.decode())
    d=json.loads(p.stdout)
    print(json.dumps({k:d[k] for k in ('status','host','instance_id','boot_id','mount','free_disk_bytes','source_pins','singular_path','singular_sha256','suspects')},sort_keys=True))
elif mode=='ec2':
    p=subprocess.run(['aws','ec2','describe-instances','--region','us-east-1','--instance-ids','i-0da0cebfc97c9fd54','--output','json'],capture_output=True,check=True)
    with (HERE/'ec2.json').open('xb') as f:f.write(p.stdout)
    d=json.loads(p.stdout)['Reservations'][0]['Instances'][0]
    print(json.dumps({'id':d['InstanceId'],'state':d['State']['Name'],'ip':d['PublicIpAddress'],'tags':d['Tags'],'ebs':d['BlockDeviceMappings']},sort_keys=True))
elif mode=='deploy':
    ready=json.loads((HERE/'readiness.stdout').read_text())
    if ready['status']!='READY_READONLY':raise SystemExit('not ready')
    remote='/home/ubuntu/d125-physical-export-pilot-20260906'
    subprocess.run(SSH+['mkdir -- '+remote],check=True)
    repo=HERE.parent.parent
    files=[HERE/n for n in ('authority.json','payload.py','orphan_control.py','controls.py','readiness.stdout')]
    files += [repo/'box/d125-physical-exporter-20260906'/n for n in ('exporter.py','test_exporter.py')]
    files += [repo/'box/full-j-solver-pilot-20260906/evidence/run_capped.py']
    files += [repo/'xmodel'/n for n in json.loads((HERE/'authority.json').read_text())['source_hashes']]
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    with (HERE/'deployment.json').open('x') as f:json.dump(manifest,f,sort_keys=True,indent=2);f.write('\n')
    subprocess.run(['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes',*[str(p) for p in files],str(HERE/'deployment.json'),'ubuntu@172.30.0.56:'+remote+'/'],check=True)
    print(json.dumps(manifest,sort_keys=True))
elif mode=='stage':
    stage=sys.argv[2]
    if stage not in ('controls','construct','import'):raise SystemExit('unknown stage')
    remote='/home/ubuntu/d125-physical-export-pilot-20260906'
    if stage=='controls':
        command='cd '+remote+' && exec /usr/bin/python3 controls.py remote'
        seconds=50
    else:
        wall,rss=(600,8589934592) if stage=='construct' else (300,17179869184)
        command=('cd '+remote+' && exec /usr/bin/python3 run_capped.py --wall-seconds '+str(wall)+
                 ' --rss-bytes '+str(rss)+' --cwd '+remote+' --stdout-file '+remote+'/'+stage+'.stdout'+
                 ' --stderr-file '+remote+'/'+stage+'.stderr --telemetry-file '+remote+'/'+stage+'.telemetry.json'+
                 ' -- /usr/bin/python3 '+remote+'/payload.py '+stage)
        seconds=wall+30
    with (HERE/(stage+'.launch.json')).open('x') as f:json.dump({'ssh_argv':SSH+[command],'timeout':seconds},f,sort_keys=True,indent=2);f.write('\n')
    p=subprocess.run(SSH+[command],capture_output=True,timeout=seconds)
    with (HERE/(stage+'.ssh.stdout')).open('xb') as f:f.write(p.stdout)
    with (HERE/(stage+'.ssh.stderr')).open('xb') as f:f.write(p.stderr)
    with (HERE/(stage+'.ssh.rc')).open('x') as f:f.write(str(p.returncode)+'\n')
    print(json.dumps({'stage':stage,'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()},sort_keys=True))
    raise SystemExit(p.returncode)
elif mode=='guard-controls':
    cases=[('wrong_host',[sys.executable,str(HERE/'payload.py'),'construct'],'wrong Linux hostname'),
           ('wrong_cwd',SSH+['cd /home/ubuntu/d125-physical-export-pilot-20260906/remote-controls && /usr/bin/python3 ../payload.py construct'],'wrong cwd/symlink')]
    outcomes={}
    for label,argv,error in cases:
        p=subprocess.run(argv,capture_output=True,text=True,timeout=10)
        with (HERE/(label+'.stdout')).open('x') as f:f.write(p.stdout)
        with (HERE/(label+'.stderr')).open('x') as f:f.write(p.stderr)
        if not (p.returncode!=0 and error in p.stderr):raise RuntimeError((label,p.returncode,p.stderr))
        outcomes[label]={'returncode':p.returncode,'rejected':True,'expected_error':error}
    with (HERE/'guard-controls.json').open('x') as f:json.dump(outcomes,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps(outcomes,sort_keys=True))
elif mode=='harvest':
    remote='/home/ubuntu/d125-physical-export-pilot-20260906'
    subprocess.run(['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes',str(HERE/'harvest.py'),'ubuntu@172.30.0.56:'+remote+'/harvest.py'],check=True)
    p=subprocess.run(SSH+['cd '+remote+' && exec /usr/bin/python3 harvest.py'],capture_output=True,timeout=45)
    with (HERE/'harvest.stdout').open('xb') as f:f.write(p.stdout)
    with (HERE/'harvest.stderr').open('xb') as f:f.write(p.stderr)
    if p.returncode:raise RuntimeError(p.stderr.decode())
    subprocess.run(['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','ubuntu@172.30.0.56:'+remote+'/evidence.tar',str(HERE/'evidence.tar')],check=True)
    expected=json.loads(p.stdout)['archive_sha256']
    if hashlib.sha256((HERE/'evidence.tar').read_bytes()).hexdigest()!=expected:raise RuntimeError('archive transfer hash')
    print(p.stdout.decode())
else: raise SystemExit('unknown operation')
