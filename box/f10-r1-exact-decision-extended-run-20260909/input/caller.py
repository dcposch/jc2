"""UNEXECUTED disabled-until-root-registered exact decision caller.
Existing CAPRUN is the sole supervisor. No new inner PGID; no retry.
"""
import sys
sys.dont_write_bytecode = True
import os, json, time, datetime, hashlib, socket, resource, subprocess
from pathlib import Path

ARTIFACT='168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
CAPRUN='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
HELPER='cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6'
PROBE='02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7'
FLAGS=['--no-rc','--no-stdlib','--no-shell','-q','-t']

def require(ok,message):
    if not ok: raise RuntimeError(message)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exclusive(p,data):
    with Path(p).open('x') as f: json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
def filelimit(): resource.setrlimit(resource.RLIMIT_FSIZE,(16777216,16777216))
def quiet(group):
    live=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit(): continue
        try:
            raw=(p/'stat').read_text(); f=raw[raw.rfind(')')+2:].split()
            if int(f[2])==group and f[0]!='Z': live.append(int(p.name))
        except (FileNotFoundError,ProcessLookupError,PermissionError): pass
    return live
def timestamp(value):
    require(type(value) is str and value.endswith('+00:00'),'explicit UTC cutoff required')
    return datetime.datetime.fromisoformat(value).timestamp()

def main():
    require(len(sys.argv)==2 and sys.flags.isolated and sys.flags.dont_write_bytecode,'caller -I -B ROOT_REGISTRATION')
    registration=Path(sys.argv[1]).resolve(strict=True); registered_hash=sha(registration)
    reg=json.loads(registration.read_text())
    require(reg.get('schema')=='F10-EXACT-DECISION-ROOT/1' and reg.get('enabled') is True,'root registration disabled')
    require(reg.get('compatibility_confirmed') is True,'installed engine compatibility unconfirmed')
    require(reg.get('mode') in ['validate','decide'],'explicit bounded lane mode')
    root=Path(reg['cwd']); require(root.is_absolute() and Path.cwd()==root,'exact cwd')
    require(reg['job_tag'].startswith('f10-r1-exact-decision-') and str(root)=='/home/ubuntu/'+reg['job_tag'],'exclusive job path')
    instance=Path('/sys/devices/virtual/dmi/id/board_asset_tag').read_text().strip()
    require(Path('/sys/devices/virtual/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','not AWS')
    require(instance==reg['instance_id'] and instance.startswith('i-'),'wrong instance')
    require(socket.gethostname()==reg['hostname'] and socket.gethostname()!='math-hq','wrong hostname')
    deadline=timestamp(reg['math_deadline_utc']); task_deadline=timestamp(reg['task_deadline_utc'])
    require(time.time()<deadline<=task_deadline,'expired/inverted root clocks')
    require(type(reg.get('engine_version')) is str and reg['engine_version'],'installed version missing')
    engine=Path(reg['engine_path']).resolve(strict=True)
    require(str(engine)==reg['engine_path'] and reg['file_sha256'].get(str(engine))==reg['engine_sha256'],'exact engine pin')
    fixed={'exact.json':ARTIFACT,'run_capped.py':CAPRUN,'execution_gate.py':HELPER,'probe.py':PROBE}
    for name,want in fixed.items(): require(sha(root/name)==want,'fixed input/helper pin '+name)
    require(reg['admissibility_sha256']=='02952e1b804ce553c4bd8abf63daab1357cba5a19f78b1abe38ba6c933b0910a' and
            sha(root/'admissibility.md')==reg['admissibility_sha256'],'exact admissibility input')
    for name in ['caller.py','engine.py','certificate.py','semantic_tests.py','probe.py','execution_gate.py','run_capped.py','exact.json','admissibility.md']:
        require(str(root/name) in reg['file_sha256'],'missing root source pin '+name)
    require('/usr/bin/python3' in reg['file_sha256'],'missing interpreter pin')
    for p,want in reg['file_sha256'].items(): require(sha(p)==want,'root source changed')
    if reg['mode']=='decide':
        validation=Path(reg['semantic_validation_path']).resolve(strict=True)
        require(reg['file_sha256'].get(str(validation))==reg['semantic_validation_sha256']==sha(validation),'pinned semantic validation missing')
        previous=json.loads(validation.read_text())
        require(previous['status']=='PASS-DESIGNED-SEMANTICS' and previous['artifact_sha256']==ARTIFACT and
                previous['certificate_sha256']==sha(root/'certificate.py') and
                previous['tests_sha256']==sha(root/'semantic_tests.py'),'semantic validation/source mismatch')
    records=[]; first_math=None

    def run(name,script,args,wall,cpu,rss=2147483648,defect=None,mathematical=False):
        nonlocal first_math
        now=time.time(); hard=task_deadline
        if mathematical:
            if first_math is None: first_math=now
            hard=min(deadline,first_math+690,task_deadline)
        require(now+wall+15<hard,'insufficient remaining registered budget')
        require(sha(registration)==registered_hash,'root registration changed')
        auth=root/(name+'.authority.json')
        child=['/usr/bin/python3','-I','-B',str(root/script),str(auth),*map(str,args)]
        caps={'wall_seconds':str(wall),'cpu_seconds':str(cpu),'rss_bytes':str(rss),
              'rss_sample_seconds':'0.05','term_grace_seconds':'0.25'}
        parent=['/usr/bin/python3','-I','-B',str(root/'run_capped.py'),
                '--wall-seconds',str(wall),'--cpu-seconds',str(cpu),'--rss-bytes',str(rss),
                '--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',str(root),
                '--stdout-file',str(root/(name+'.stdout')),'--stderr-file',str(root/(name+'.stderr')),
                '--telemetry-file',str(root/(name+'.telemetry.json')),'--',*child]
        files=dict(reg['file_sha256']); files[str(registration)]=registered_hash
        if name=='verify':
            for generated in ['engine.receipt.json','input.sing','singular.stdout','singular.stderr']:
                files[str(root/generated)]=sha(root/generated)
        spec={'schema':'F10-R1-REGISTERED/v1','enabled':True,'job_tag':reg['job_tag'],'operation':'check',
              'instance_id':instance,'hostname':reg['hostname'],'cwd':str(root),
              'admissibility_sha256':reg['admissibility_sha256'],'runner_path':str(root/'run_capped.py'),
              'caps':caps,'stdout_file':str(root/(name+'.stdout')),'stderr_file':str(root/(name+'.stderr')),
              'telemetry_file':str(root/(name+'.telemetry.json')),'parent_argv':parent,'child_argv':child,
              'engine_path':str(engine),'engine_sha256':reg['engine_sha256'],'engine_version':reg['engine_version'],
              'engine_argv':[str(engine),*FLAGS,str(root/'input.sing')],
              'file_sha256':files,'root_registration_sha256':registered_hash,'hard_cutoff_epoch':str(hard)}
        if defect=='disabled': spec['enabled']=False
        if defect=='wronghost': spec['hostname']='NOT-REGISTERED'
        if defect=='argv': spec['parent_argv']=parent+['EXTRA']
        if defect=='cap': spec['caps']=dict(caps,rss_bytes='1')
        if defect=='missing-input': del spec['file_sha256'][str(args[0])]
        exclusive(auth,spec); namespace=os.readlink('/proc/self/ns/pid')
        with (root/(name+'.caller.stdout')).open('x') as out,(root/(name+'.caller.stderr')).open('x') as err:
            process=subprocess.Popen(parent,stdin=subprocess.DEVNULL,stdout=out,stderr=err,cwd=root,
                                     preexec_fn=filelimit,start_new_session=False)
            caller_stat=Path('/proc/'+str(process.pid)+'/stat').read_text()
            require(os.readlink('/proc/'+str(process.pid)+'/ns/pid')==namespace,'CAPRUN namespace mismatch')
            rc=process.wait(); returned=time.time()
        telemetry=json.loads((root/(name+'.telemetry.json')).read_text())
        require(not quiet(telemetry['pgid']),'owned PGID remains live')
        for p,want in files.items(): require(sha(p)==want,'post-run input changed')
        record={'name':name,'returncode':rc,'caller_pid':process.pid,'caller_stat':caller_stat,'namespace':namespace,
                'authority_sha256':sha(auth),'telemetry_sha256':sha(root/(name+'.telemetry.json')),
                'first_math_epoch':first_math,'hard_cutoff_epoch':hard,'returned_epoch':returned,
                'mathematical':mathematical,'remaining_group_live':[]}
        records.append(record); exclusive(root/(name+'.dispatch.json'),record)
        require(returned<hard,'late return: INCONCLUSIVE')
        if defect:
            require(rc!=0 and telemetry['status']=='NORMAL_EXIT' and not Path(args[1]).exists(),'authority refusal failed')
        elif name=='dummy':
            require(rc==125 and telemetry['status']=='RESOURCE_CAP' and telemetry['resource']=='rss','dummy cap not exercised')
            t=telemetry['termination']; require(all(t[k] for k in ['term_sent','kill_sent','cleanup_complete','leader_reaped']),'dummy cleanup')
            require(telemetry['max_observed_group_rss_bytes']>rss,'descendant RSS not sampled')
            events=telemetry['identity_checks']
            require([(e.get('stage'),e.get('result'),e.get('signal')) for e in events]==[
                ('before-term','MATCH',None),('before-term-send','SENT',15),
                ('before-kill','MATCH',None),('before-kill-send','SENT',9)],'dummy identity sequence')
            for e in events:
                if e['result']=='MATCH':
                    require(e.get('observed_pid')==telemetry['pid']==telemetry['pgid']==e.get('observed_pgid') and
                            e.get('observed_start_identity')==telemetry['start_identity'],'dummy PID/start mismatch')
                else: require(type(e['signal']) is int,'signal type')
            lines=[json.loads(x) for x in (root/'dummy.stdout').read_text().splitlines()]
            require(len(lines)==2 and all(x['namespace']==namespace and x['pgid']==telemetry['pgid'] for x in lines),'dummy descendant binding')
        else: require(rc==0 and telemetry['status']=='NORMAL_EXIT','cap/failure: INCONCLUSIVE')

    try:
        for defect in ['disabled','wronghost','argv','cap','missing-input']:
            run('gate-'+defect,'probe.py',[root/'exact.json',root/(defect+'.sentinel'),'plain'],5,3,defect=defect)
        run('valid','probe.py',[root/'exact.json',root/'valid.sentinel','plain'],5,3)
        require((root/'valid.sentinel').read_text()=='POSTAUTHORIZE\n','valid sentinel')
        run('dummy','probe.py',[root/'exact.json',root/'dummy.sentinel','descendant'],5,3,33554432)
        exclusive(root/'preflight.PASS.json',{'records':records,'status':'PASS'})
        if reg['mode']=='validate':
            run('semantics','semantic_tests.py',[root/'exact.json',root/'semantic-validation.json'],30,25,mathematical=True)
            exclusive(root/'batch.FINAL.json',{'records':records,'status':'VALIDATION-ONLY-NO-DECISION'})
            return
        run('engine','engine.py',[root/'exact.json',root/'engine.receipt.json'],600,550,mathematical=True)
        run('verify','certificate.py',[root/'exact.json',root/'engine.receipt.json',root/'decision.json'],60,50,mathematical=True)
        verdict=json.loads((root/'decision.json').read_text())['verdict']
        require(verdict in ['VERIFIED-UNIT','VERIFIED-PROPER'],'unrecognized terminal decision')
        exclusive(root/'batch.FINAL.json',{'records':records,'verdict':verdict,'root_registration_sha256':registered_hash})
    except BaseException as e:
        exclusive(root/'batch.STOP.json',{'records':records,'status':'INCONCLUSIVE','error':type(e).__name__+': '+str(e)})
        raise

if __name__=='__main__': main()
