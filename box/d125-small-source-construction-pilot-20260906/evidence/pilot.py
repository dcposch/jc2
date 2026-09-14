#!/usr/bin/env python3
"""One registered sequential construction/import batch; stops on first problem."""
import datetime, hashlib, json, math, os, re, subprocess, sys, time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906')
INSTANCE='i-0da0cebfc97c9fd54'
REG='82d2db220affc538e5076707061a8b38c57b736a178dcb8c6d368ba5760e918c'
PINS={'exporter_sha256':'9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703',
      'baseline_sha256':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
      'normalization_gate_sha256':'cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d',
      'lift_contract_sha256':'433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
      'lift_gate_sha256':'4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122'}
RUNNER='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as src:
        for block in iter(lambda:src.read(1048576),b''):h.update(block)
    return h.hexdigest()
def save(path,obj):
    with Path(path).open('x') as out:
        json.dump(obj,out,sort_keys=True,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def pins():
    need(Path.cwd()==ROOT and ROOT.resolve()==ROOT,'wrong exact task cwd')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()==INSTANCE,'wrong instance')
    need(sha(ROOT/'REGISTRATION.md')==REG,'registration drift')
    need(sha(ROOT/'run_capped.py')==RUNNER,'runner drift')
    for name in ('exporter','baseline'):need(sha(ROOT/(name+'.py'))==PINS[name+'_sha256'],'code drift')
def group_absent(pgid):
    for _ in range(30):
        lines=subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines()
        group=[line for line in lines if int(line.split()[1])==pgid]
        if not group:return True
        time.sleep(.1)
    return False
JOBS=[]
def job(label,cwd,argv,cap,cpu,rss,expected='NORMAL_EXIT'):
    command=[sys.executable,str(ROOT/'run_capped.py'),'--cwd',str(cwd),'--wall-seconds',str(cap),
             '--cpu-seconds',str(cpu),'--rss-bytes',str(rss),'--term-grace-seconds','.25',
             '--stdout-file',str(cwd/(label+'.stdout')),'--stderr-file',str(cwd/(label+'.stderr')),
             '--telemetry-file',str(cwd/(label+'.telemetry.json')),'--']+argv
    start=utc();run=subprocess.run(command,capture_output=True,text=True)
    record={'label':label,'cwd':str(cwd),'command':command,'runner_rc':run.returncode,
            'runner_stdout':run.stdout,'runner_stderr':run.stderr,'start_utc':start,'end_utc':utc()}
    tele=json.loads((cwd/(label+'.telemetry.json')).read_text());record['telemetry']=tele
    record['group_absent']=group_absent(tele['pgid']) if tele['pgid'] else False
    JOBS.append(record);save(cwd/(label+'.receipt.json'),record)
    need(record['group_absent'],'job process group remains')
    need(tele['status']==expected and tele['error'] is None,'cap/runner status mismatch '+label)
    need(run.returncode==(124 if expected=='WALL_TIMEOUT' else 0),'job failed '+label)
    need(expected!='NORMAL_EXIT' or tele['child_returncode']==0,'child failed '+label)
    return record
def main():
    pins();ready=json.loads((ROOT/'readiness.json').read_text())
    fields=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()
    save(ROOT/'controller.identity.json',{'pid':os.getpid(),'pgid':os.getpgrp(),
         'start_ticks':fields[19],'cwd':str(Path.cwd()),'utc':utc(),'argv':sys.argv})
    need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==ready['boot_id'],'boot drift')
    mount=subprocess.check_output(['findmnt','-T',str(ROOT),'-n','-o','SOURCE,FSTYPE,TARGET'],text=True).split()
    need(mount==['/dev/nvme0n1p1','ext4','/'],'not registered EBS mount')
    serial=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip()
    need(serial=='vol0eb6450d18ffa89f1','wrong EBS serial')
    front=subprocess.run([sys.executable,str(ROOT/'frontier_gate.py'),'--total-degrees','75','125',
                          '--purpose','frontier','--tag','d125-small-source-construction-pilot-20260906'],
                          capture_output=True,text=True)
    save(ROOT/'frontier.json',{'rc':front.returncode,'stdout':front.stdout,'stderr':front.stderr})
    need(front.returncode==0 and json.loads(front.stdout)['overall_verdict']=='NOT_CLOSED_BY_THIS_GATE','frontier gate')
    control=ROOT/'controls';control.mkdir()
    normal=job('identity',control,[sys.executable,str(ROOT/'payload.py'),'identity'],10,5,512*1024**2)
    ident=json.loads((control/'identity.identity.json').read_text())
    need(ident['pid']==normal['telemetry']['pid'] and ident['pgid']==normal['telemetry']['pgid'],'caller PID/PGID mismatch')
    orphan=job('orphan',control,[sys.executable,str(ROOT/'payload.py'),'orphan'],1,5,512*1024**2,'WALL_TIMEOUT')
    desc=json.loads((control/'orphan.descendant.json').read_text())
    need(desc['pgid']==orphan['telemetry']['pgid'],'descendant escaped group')
    need(orphan['telemetry']['termination']['kill_sent'] and
         orphan['telemetry']['termination']['leader_reaped'] and
         orphan['telemetry']['termination']['cleanup_complete'],'descendant cap cleanup failed')
    save(ROOT/'regression.json',{'status':'PASS','identity':normal,'orphan':orphan,'descendant':desc})
    print('FRESH_REGRESSION_PASS',flush=True)
    deadline=time.monotonic()+600;batch_start=utc();results=[]
    sequence=[(c,b) for c in ('unequal','common_3','common_4') for b in ('rational','golden')]
    for case,branch in sequence:
        pins();remaining=math.floor(deadline-time.monotonic())-2;need(remaining>0,'combined budget exhausted')
        cap=min(180,remaining);directory=ROOT/(case+'-'+branch);directory.mkdir()
        auth={'schema':'jc2.d125-small-source-authority/v1','root_green':True,'construction_only':True,
              'job_id':'d125-small-source-pilot-20260906/'+case+'/'+branch,'registration_sha256':REG,
              'instance_id':INSTANCE,'working_directory':str(directory),'case':case,'branch':branch,
              'deadline_utc':(datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(seconds=cap)).isoformat(),
              'caps':{'wall_seconds':cap,'cpu_seconds':cap,'as_bytes':8*1024**3,
                      'aggregate_output_bytes':256*1024**2},'pins':PINS}
        save(directory/'authority.json',auth)
        build=job('construct',directory,[sys.executable,str(ROOT/'exporter.py'),'--authority',str(directory/'authority.json'),
                   '--case',case,'--branch',branch,'--singular-import-only'],cap,cap,8*1024**3)
        need((directory/'construct.stderr').stat().st_size==0,'construction stderr nonempty')
        name='client-'+case+'-'+branch;manifest_path=directory/(name+'.manifest.json')
        manifest=json.loads(manifest_path.read_text());footer=manifest['footer']
        need(manifest['status']=='CONSTRUCTION_AND_SAME_FORMULA_REPLAY_COMPLETE','incomplete replay')
        expected={'unequal':(269,803),'common_3':(295,816),'common_4':(371,816)}[case]
        need((manifest['variables'],footer['counts']['rows'])==expected,'variable/row counts')
        need(footer['counts']['jacobian']==660 and footer['counts']['polynomiality']==105,'full row classes')
        need(manifest['identity']['pid']==build['telemetry']['pid'] and
             manifest['identity']['pgid']==build['telemetry']['pgid'],'constructor identity mismatch')
        for key in ('jsonl','singular'):
            item=manifest[key];path=directory/item['path']
            need(path.stat().st_size==item['bytes'] and sha(path)==item['sha256'],'output pin mismatch')
        remaining=math.floor(deadline-time.monotonic())-2;need(remaining>0,'combined budget exhausted')
        cap=min(60,remaining)
        imported=job('import',directory,[sys.executable,str(ROOT/'payload.py'),'import',str(manifest_path)],cap,cap,8*1024**3)
        stdout=(directory/'import.stdout').read_text();stderr=(directory/'import.stderr').read_text()
        match=re.fullmatch(r'\s*D125_COMPLETE_LITERAL_IMPORT_ONLY\s+(\d+)\s*',stdout)
        need(not stderr and match is not None,'import parser diagnostics/marker failure')
        for key in ('jsonl','singular'):need(sha(directory/manifest[key]['path'])==manifest[key]['sha256'],'post-import drift')
        result={'case':case,'branch':branch,'manifest':manifest,'import_size_diagnostic':int(match.group(1)),
                'constructor_telemetry':build['telemetry'],'import_telemetry':imported['telemetry'],
                'remaining_batch_seconds':deadline-time.monotonic()}
        save(directory/'case.result.json',result);results.append(result)
        print(json.dumps({'case':case,'branch':branch,'status':'CONSTRUCTION_IMPORT_PASS',
                          'counts':footer['counts'],'jsonl_bytes':manifest['jsonl']['bytes']}),flush=True)
    save(ROOT/'batch.result.json',{'status':'ALL_SIX_CONSTRUCTION_IMPORT_COMPLETE','start_utc':batch_start,
         'end_utc':utc(),'arithmetic_batch_seconds':600-(deadline-time.monotonic()),'results':results})
try:main()
except BaseException as error:
    save(ROOT/'failure.json',{'error':repr(error),'utc':utc(),'jobs':JOBS,'no_retry':True})
    raise
finally:
    save(ROOT/'terminal-jobs.json',{'jobs':JOBS,'utc':utc(),'all_recorded_groups_absent':all(j['group_absent'] for j in JOBS)})
