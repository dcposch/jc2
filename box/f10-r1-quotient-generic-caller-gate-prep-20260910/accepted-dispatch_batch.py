"""One registered GENERIC compatibility batch. Existing supervisor unchanged.
RLIMIT_FSIZE is inherited BEFORE exec of the exact existing CAPRUN argv.
No new PGID is created by this caller; CAPRUN owns its recorded child PGID.
"""
import sys
sys.dont_write_bytecode = True
import os, json, hashlib, socket, resource, subprocess, time, datetime
from pathlib import Path
# DISABLED without a fresh root-written, externally pinned registration.
ROOT = Path(__file__).resolve().parent
REGISTRATION = ROOT / 'dispatch.registration.json'
INSTANCE = JOB = DEADLINE = AGGREGATE = None
registration = None
fixed_files = {}
first_math = None
records = []

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def exclusive(path, obj):
    with Path(path).open('x') as f:
        json.dump(obj, f, sort_keys=True, indent=2); f.write('\n')

def require(ok, reason):
    if not ok: raise RuntimeError(reason)

def filelimit():
    resource.setrlimit(resource.RLIMIT_FSIZE, (16777216,16777216))

def quiet(pgid):
    live=[]
    for item in Path('/proc').iterdir():
        if not item.name.isdigit(): continue
        try:
            raw=(item/'stat').read_text(); fields=raw[raw.rfind(')')+2:].split()
            if int(fields[2])==pgid and fields[0]!='Z': live.append(int(item.name))
        except (FileNotFoundError,ProcessLookupError,PermissionError): pass
    return live

def run(name, script, trailing, profile, operation='check', defect=None, mathematical=False):
    global first_math
    limits=registration['profiles'][profile]
    wall,cpu,rss=(limits[k] for k in ('wall_seconds','cpu_seconds','rss_bytes'))
    hard = DEADLINE
    require(time.time()+wall+15 < hard, 'insufficient remaining task budget')
    if mathematical:
        now=time.time()
        if first_math is None: first_math=now
        hard=min(DEADLINE, first_math+AGGREGATE)
        require(now+wall+15 < hard, 'insufficient remaining mathematical budget')
    auth=ROOT/(name+'.authority.json')
    child=['/usr/bin/python3','-I','-B',str(ROOT/script),str(auth),*map(str,trailing)]
    caps={'wall_seconds':str(wall),'cpu_seconds':str(cpu),'rss_bytes':str(rss),
          'rss_sample_seconds':'0.05','term_grace_seconds':'0.25'}
    parent=['/usr/bin/python3','-I','-B',str(ROOT/'run_capped.py'),
            '--wall-seconds',caps['wall_seconds'],'--cpu-seconds',caps['cpu_seconds'],
            '--rss-bytes',caps['rss_bytes'],'--rss-sample-seconds','0.05',
            '--term-grace-seconds','0.25','--cwd',str(ROOT),
            '--stdout-file',str(ROOT/(name+'.stdout')),'--stderr-file',str(ROOT/(name+'.stderr')),
            '--telemetry-file',str(ROOT/(name+'.telemetry.json')),'--',*child]
    files=dict(fixed_files)
    for path in trailing:
        candidate=Path(str(path))
        if candidate.is_file():
            filename=str(candidate.resolve())
            if filename in files:
                require(digest(candidate)==files[filename], 'fixed trailing input changed')
            else:
                files[filename]=digest(candidate)
    for suffix in ('.authority.json','.stdout','.stderr','.telemetry.json','.caller.stdout','.caller.stderr','.dispatch.json'):
        require(not (ROOT/(name+suffix)).exists(), 'operation output already exists')
    spec={'schema':'F10-R1-REGISTERED/v1','enabled':True,'job_tag':JOB,'operation':operation,
          'instance_id':INSTANCE,'hostname':socket.gethostname(),'admissibility_sha256':digest(ROOT/'generic.plan.json'),
          'runner_path':str(ROOT/'run_capped.py'),'cwd':str(ROOT),'caps':caps,
          'stdout_file':str(ROOT/(name+'.stdout')),'stderr_file':str(ROOT/(name+'.stderr')),
          'telemetry_file':str(ROOT/(name+'.telemetry.json')),'parent_argv':parent,'child_argv':child,'file_sha256':files,
          'generic_only':True,'generic_plan_sha256':digest(ROOT/'generic.plan.json'),
          'python_flint':registration['python_flint']}
    if defect=='disabled': spec['enabled']=False
    if defect=='wronghost': spec['hostname']='NOT-THE-REGISTERED-HOST'
    if defect=='argv': spec['parent_argv']=parent+['EXTRA']
    if defect=='cap': spec['caps']=dict(caps,rss_bytes='1')
    if defect=='missing-input': del spec['file_sha256'][str(trailing[0])]
    exclusive(auth,spec)
    auth.chmod(0o444)  # cooperative frozen per-operation authority; no concurrent writer
    authority_sha=digest(auth)
    namespace=os.readlink('/proc/self/ns/pid')
    started=time.time()
    with (ROOT/(name+'.caller.stdout')).open('x') as out, (ROOT/(name+'.caller.stderr')).open('x') as err:
        process=subprocess.Popen(parent,stdin=subprocess.DEVNULL,stdout=out,stderr=err,cwd=ROOT,
                                 preexec_fn=filelimit, start_new_session=False)
        require(os.readlink(f'/proc/{process.pid}/ns/pid')==namespace,'caller PID namespace mismatch')
        caller_stat=Path(f'/proc/{process.pid}/stat').read_text()
        rc=process.wait()
        returned=time.time()
    telemetry=json.loads((ROOT/(name+'.telemetry.json')).read_text())
    require(not quiet(telemetry['pgid']), 'owned live PGID after CAPRUN')
    for filename,want in files.items(): require(digest(filename)==want,'source/input changed')
    require(digest(auth)==authority_sha, 'frozen authority changed')
    record={'name':name,'returncode':rc,'started_utc':datetime.datetime.fromtimestamp(started,datetime.timezone.utc).isoformat(),
            'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'namespace':namespace,
            'caller_pid':process.pid,'caller_stat':caller_stat,'authority_sha256':authority_sha,
            'telemetry_sha256':digest(ROOT/(name+'.telemetry.json')),'mathematical':mathematical,
            'first_math_epoch':first_math,'hard_cutoff_epoch':hard,'returned_epoch':returned,
            'admission_margin_seconds':15,'remaining_group_live':[]}
    records.append(record); exclusive(ROOT/(name+'.dispatch.json'),record)
    require(returned < hard, 'return at/after original stored hard cutoff: NONDECISION')
    if defect:
        require(rc!=0 and telemetry['status']=='NORMAL_EXIT','gate refusal was not ordinary nonzero exit')
        require(not Path(trailing[1]).exists(),'postauthorize sentinel written by rejected authority')
    elif name=='dummy-descendant':
        require(rc==125 and telemetry['status']=='RESOURCE_CAP' and telemetry['resource']=='rss','dummy did not exercise RSS cap')
        term=telemetry['termination']
        require(term['term_sent'] and term['kill_sent'] and term['cleanup_complete'] and term['leader_reaped'], 'dummy cleanup failed')
        require(telemetry['max_observed_group_rss_bytes']>rss,'descendant RSS not measured')
        lines=[json.loads(x) for x in (ROOT/(name+'.stdout')).read_text().splitlines()]
        require(len(lines)==2 and all(x['namespace']==namespace for x in lines),'dummy namespace/custody missing')
        require(all(x['pgid']==telemetry['pgid'] for x in lines),'descendant escaped recorded PGID')
        expected_events = [
            ('before-term', 'MATCH', None),
            ('before-term-send', 'SENT', 15),
            ('before-kill', 'MATCH', None),
            ('before-kill-send', 'SENT', 9),
        ]
        events = telemetry['identity_checks']
        observed_events = [(x.get('stage'), x.get('result'), x.get('signal')) for x in events]
        require(observed_events == expected_events, 'unexpected dummy identity/signal sequence')
        for event in events:
            if event['result'] == 'MATCH':
                require(event.get('observed_pid') == telemetry['pid'] == telemetry['pgid'] == event.get('observed_pgid')
                        and event.get('observed_start_identity') == telemetry['start_identity'],
                        'dummy MATCH identity inconsistent with registered leader')
            else:
                require(type(event.get('signal')) is int, 'dummy signal is not an exact integer')
    else:
        require(rc==0 and telemetry['status']=='NORMAL_EXIT','cap/failure: STOP, no retry')
    return record

def main():
    global registration, INSTANCE, JOB, DEADLINE, AGGREGATE, fixed_files
    registration=json.loads(REGISTRATION.read_text())
    require(registration.get('schema')=='F10-GENERIC-COMPATIBILITY-DISPATCH/v1'
            and registration.get('enabled') is True and registration.get('generic_only') is True,
            'DISABLED: fresh ROOT generic-only registration required')
    require('univariate_acceptance' not in registration and 'normalized_acceptance' not in registration,
            'generic batch cannot carry source acceptance')
    require(sys.flags.isolated and sys.flags.dont_write_bytecode, 'require caller Python -I -B')
    require(Path.cwd()==ROOT and str(ROOT)==registration['cwd'], 'wrong remote cwd')
    INSTANCE=registration['instance_id']; JOB=registration['job_tag']
    require(Path('/sys/devices/virtual/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','wrong vendor')
    require(Path('/sys/devices/virtual/dmi/id/board_asset_tag').read_text().strip()==INSTANCE,'wrong physical instance')
    require(socket.gethostname()==registration['hostname'] and socket.gethostname()!='math-hq','wrong host')
    require(registration['exclusive_no_concurrent_authority_writer'] is True, 'authority freeze contract missing')
    for key in ('mathematical_deadline_utc','task_deadline_utc'):
        stamp=registration[key]
        require(isinstance(stamp,str) and stamp.endswith('+00:00'),'explicit UTC deadline required')
    DEADLINE=min(datetime.datetime.fromisoformat(registration[key]).timestamp()
                 for key in ('mathematical_deadline_utc','task_deadline_utc'))
    AGGREGATE=registration['aggregate_wall_seconds']
    require(type(AGGREGATE) is int and AGGREGATE>0,'explicit aggregate cap required')
    require(registration['file_size_limit_bytes']==16777216,'file cap changed')
    require(set(registration['profiles'])=={'probe','dummy','compatibility'},'exact finite generic profiles')
    for limits in registration['profiles'].values():
        require(set(limits)=={'wall_seconds','cpu_seconds','rss_bytes'},'profile fields')
        require(all(type(v) is int and v>0 for v in limits.values()),'explicit positive integer caps')
    require(registration['profiles']['dummy']['rss_bytes']==33554432,'dummy must retain its reviewed RSS cap')
    known={
      'compatibility.py':'aaec1e2c56d7d4e77f7cf040a86371b813744368c9272b4f5cbe629af18af38b',
      'generic.plan.json':'1fe704aaaa125dc8d40d5915ea74ae651277ba3f2336ab76579adc104fc305e5',
      'checker.py':'122842e5cf38a0eab2585c7e894c1ca9d9758dd643830d5447800642554fdf69',
      'evidence.py':'cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767',
      'algebra.py':'7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc',
      'execution_gate.py':'cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6',
      'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2',
      'probe.py':'02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7'}
    supplied=registration['file_sha256']
    environment=registration.get('python_flint'); package=registration.get('python_flint_files')
    require(type(environment) is dict and set(environment)=={'version','module_file','module_sha256'}
            and type(environment['version']) is str and environment['version'],'installed FLINT metadata required')
    require(type(package) is dict and bool(package),'ROOT-pinned FLINT/native file closure required')
    require(package.get(environment['module_file'])==environment['module_sha256'],'module/closure binding')
    base={str(ROOT/n) for n in [*known,'dispatch_batch.py']} | {'/usr/bin/python3'}
    require(not (base & set(package)),'package pins must not replace task/interpreter pins')
    require(all(str(Path(p).resolve(strict=True))==p for p in package),'absolute resolved package pins')
    require(set(supplied)==base | set(package),'exact generic runtime input vector')
    for n,want in known.items():
        require(supplied[str(ROOT/n)]==want,'frozen generic runtime pin altered')
    for path,want in package.items():
        require(supplied[path]==want,'installed package pin altered')
    for filename,want in supplied.items():
        require(isinstance(want,str) and len(want)==64 and digest(filename)==want,'runtime source/interpreter pin')
    fixed_files=dict(supplied); fixed_files[str(REGISTRATION)]=digest(REGISTRATION)
    for name in ('compatibility.receipt.json','preflight.PASS.json','batch.PASS.json','batch.STOP.json'):
        require(not (ROOT/name).exists(),'exclusive job output already exists')
    for defect in ['disabled','wronghost','argv','cap','missing-input']:
        run('gate-'+defect,'probe.py',[ROOT/'generic.plan.json',ROOT/('gate-'+defect+'.sentinel'),'plain'],'probe',defect=defect)
    run('gate-valid','probe.py',[ROOT/'generic.plan.json',ROOT/'gate-valid.sentinel','plain'],'probe')
    require((ROOT/'gate-valid.sentinel').read_text()=='POSTAUTHORIZE\n','valid gate failed')
    run('dummy-descendant','probe.py',[ROOT/'generic.plan.json',ROOT/'dummy-descendant.sentinel','descendant'],'dummy')
    exclusive(ROOT/'preflight.PASS.json',{'status':'PASS','records':records,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    run('compatibility','compatibility.py',[ROOT/'generic.plan.json',ROOT/'compatibility.receipt.json'],
        'compatibility',mathematical=True)
    receipt=json.loads((ROOT/'compatibility.receipt.json').read_text())
    require(receipt.get('status')=='GENERIC-COMPATIBILITY-PASS-NOT-ACTUAL-SOURCE'
            and receipt.get('generic_only') is True,'genuine generic receipt scope')
    require(receipt.get('generic_plan_sha256')==known['generic.plan.json']
            and receipt.get('harness_sha256')==known['compatibility.py']
            and receipt.get('checker_sha256')==known['checker.py'],'genuine generic receipt source binding')
    require(receipt.get('counts')=={'verifier_calls':12,'positives':5,'negatives':7,
            'flint_matrix_constructors':2,'flint_rref_calls':2,'flint_fmpq_constructors':23},
            'finite generic compatibility counts')
    exclusive(ROOT/'batch.PASS.json',{'status':'GENERIC-COMPATIBILITY-ENGINEERING-PASS-NOT-ACTUAL-SOURCE',
        'records':records,'generic_plan_sha256':known['generic.plan.json'],
        'receipt_sha256':digest(ROOT/'compatibility.receipt.json'),
        'first_math_epoch':first_math,'end_epoch':time.time(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})

try:
    main()
except BaseException as exc:
    exclusive(ROOT/'batch.STOP.json',{'status':'STOP-NONDECISION','error':type(exc).__name__+': '+str(exc),
        'records':records,'first_math_epoch':first_math,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    raise
