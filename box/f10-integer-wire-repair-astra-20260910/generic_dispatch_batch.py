"""One registered quotient/remainder GENERIC batch. Existing supervisor unchanged.
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
armed = False
plan = None

REFUSALS = {
    'disabled': 'no active registered authority',
    'wronghost': 'not the registered AWS host',
    'argv': 'full parent argv differs from registered capped runner',
    'cap': 'registration is not the exact required CAPRUN argv',
    'missing-input': 'checker input artifact must be explicitly hash-registered',
}

def absent(paths):
    require(not any(os.path.lexists(p) for p in paths), 'output exists, including symlink')

def fixed_barrier(auth=None, authority_sha=None):
    for filename, want in fixed_files.items():
        # Retain the registered interpreter spelling /usr/bin/python3, which
        # may be an OS symlink. The registered content digest is authoritative.
        require(Path(filename).is_file() and digest(filename) == want,
                'original fixed input changed before/after dispatch')
    if auth is not None:
        require(auth.is_file() and not auth.is_symlink()
                and auth.stat().st_mode & 0o777 == 0o444
                and digest(auth) == authority_sha, 'frozen authority changed')

def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate metadata JSON key')
            result[key] = value
        return result
    def forbidden(value):
        raise RuntimeError('nonfinite metadata JSON')
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs, parse_constant=forbidden)

def generic_outputs():
    output = str(ROOT/'generic.receipt.json')
    paths = [output]
    for name, _ in plan['positive_cases']:
        paths.extend((output+'.'+name+'.input.json', output+'.'+name+'.candidate.json'))
    paths.extend(output+'.'+name+'.negative.json' for name, _ in plan['negative_cases'])
    return paths


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
    suffixes=('.authority.json','.stdout','.stderr','.telemetry.json','.caller.stdout',
              '.caller.stderr','.dispatch.json','.prelaunch.json','.sentinel')
    absent([ROOT/(name+suffix) for suffix in suffixes])
    if mathematical: absent(generic_outputs())
    spec={'schema':'F10-R1-REGISTERED/v1','enabled':True,'job_tag':JOB,'operation':operation,
          'instance_id':INSTANCE,'hostname':socket.gethostname(),'admissibility_sha256':digest(ROOT/'generic.plan.json'),
          'runner_path':str(ROOT/'run_capped.py'),'cwd':str(ROOT),'caps':caps,
          'stdout_file':str(ROOT/(name+'.stdout')),'stderr_file':str(ROOT/(name+'.stderr')),
          'telemetry_file':str(ROOT/(name+'.telemetry.json')),'parent_argv':parent,'child_argv':child,'file_sha256':files,
          'generic_only':True,'univariate_acceptance':None,
          'generic_plan_sha256':digest(ROOT/'generic.plan.json'),
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
    fixed_barrier(auth, authority_sha)
    prelaunch={'name':name,'authority_sha256':authority_sha,
               'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'fixed_file_sha256':dict(fixed_files),'parent_argv':parent,'child_argv':child,
               'hard_cutoff_epoch':hard,'first_math_epoch':first_math}
    exclusive(ROOT/(name+'.prelaunch.json'),prelaunch)
    (ROOT/(name+'.prelaunch.json')).chmod(0o444)
    prelaunch_sha=digest(ROOT/(name+'.prelaunch.json'))
    with (ROOT/(name+'.caller.stdout')).open('x') as out, (ROOT/(name+'.caller.stderr')).open('x') as err:
        # The last prospective source check is ORIGINAL fixed_files, including
        # the plan even for missing-input. No posthoc hash substitutes for it.
        absent([ROOT/(name+s) for s in ('.stdout','.stderr','.telemetry.json','.sentinel')])
        if mathematical: absent(generic_outputs())
        fixed_barrier(auth, authority_sha)
        require(time.time()+wall+15 < hard, 'budget consumed during prospective pin checks')
        started=time.time()
        process=subprocess.Popen(parent,stdin=subprocess.DEVNULL,stdout=out,stderr=err,cwd=ROOT,
                                 preexec_fn=filelimit, start_new_session=False)
        require(os.readlink(f'/proc/{process.pid}/ns/pid')==namespace,'caller PID namespace mismatch')
        caller_stat=Path(f'/proc/{process.pid}/stat').read_text()
        rc=process.wait()
        returned=time.time()
    telemetry=read_json(ROOT/(name+'.telemetry.json'))
    require(not quiet(telemetry['pgid']), 'owned live PGID after CAPRUN')
    fixed_barrier(auth, authority_sha)
    require(digest(ROOT/(name+'.prelaunch.json'))==prelaunch_sha, 'prelaunch record changed')
    record={'name':name,'returncode':rc,'started_utc':datetime.datetime.fromtimestamp(started,datetime.timezone.utc).isoformat(),
            'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'namespace':namespace,
            'caller_pid':process.pid,'caller_stat':caller_stat,'authority_sha256':authority_sha,
            'prelaunch_checked_utc':prelaunch['checked_utc'],
            'prelaunch_sha256':prelaunch_sha,
            'prospective_fixed_inputs':len(fixed_files),
            'telemetry_sha256':digest(ROOT/(name+'.telemetry.json')),'mathematical':mathematical,
            'first_math_epoch':first_math,'hard_cutoff_epoch':hard,'returned_epoch':returned,
            'admission_margin_seconds':15,'remaining_group_live':[]}
    records.append(record); exclusive(ROOT/(name+'.dispatch.json'),record)
    require(returned < hard, 'return at/after original stored hard cutoff: NONDECISION')
    if defect:
        require(rc!=0 and telemetry['status']=='NORMAL_EXIT','gate refusal was not ordinary nonzero exit')
        require(not os.path.lexists(trailing[1]),'postauthorize sentinel written by rejected authority')
        require(REFUSALS[defect] in (ROOT/(name+'.stderr')).read_text(),
                'gate refusal did not match its exact expected reason')
    elif name=='dummy-descendant':
        require(Path(trailing[1]).read_bytes()==b'POSTAUTHORIZE\n','dummy valid gate sentinel')
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
    global registration, INSTANCE, JOB, DEADLINE, AGGREGATE, fixed_files, armed, plan
    require(len(sys.argv)==2 and len(sys.argv[1])==64
            and all(c in '0123456789abcdef' for c in sys.argv[1]),
            'external ROOT registration SHA256 required')
    require(REGISTRATION.is_file() and not REGISTRATION.is_symlink()
            and digest(REGISTRATION)==sys.argv[1], 'externally pinned registration changed')
    registration=read_json(REGISTRATION)
    require(registration.get('schema')=='F10-QUOTIENT-GENERIC-DISPATCH/v1'
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
    require(type(AGGREGATE) is int and AGGREGATE==240,'fixed aggregate cap required')
    require(registration['file_size_limit_bytes']==16777216,'file cap changed')
    require(registration['profiles']=={
        'probe':{'wall_seconds':5,'cpu_seconds':3,'rss_bytes':2147483648},
        'dummy':{'wall_seconds':5,'cpu_seconds':3,'rss_bytes':33554432},
        'generic':{'wall_seconds':180,'cpu_seconds':170,'rss_bytes':2147483648}},
        'exact finite generic profiles')
    for limits in registration['profiles'].values():
        require(set(limits)=={'wall_seconds','cpu_seconds','rss_bytes'},'profile fields')
        require(all(type(v) is int and v>0 for v in limits.values()),'explicit positive integer caps')
    require(registration['profiles']['dummy']['rss_bytes']==33554432,'dummy must retain its reviewed RSS cap')
    known={
      'generic_controls.py':'259990f7f226e0509a18f8a230f9bbc66b1241c2ab09f511fa4134110f6a1717',
      'solver.py':'4e9bb9d28c60360b39629d059b42778744c7d43c5677b52fb8351e3405e4d3f4',
      'generic.plan.json':'ce193898e3114f1db018b86e6ebe0b2ea4fdac5f65296dee76245f94da0b964a',
      'checker.py':'bb4263e1149eb1ba03d2dc47f5db339df6b05829280730ccf6c8420e0bc07045',
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
    fixed_files=dict(supplied); fixed_files[str(REGISTRATION)]=sys.argv[1]
    fixed_barrier()
    plan=read_json(ROOT/'generic.plan.json')  # Literal hash above is authoritative.
    absent([ROOT/name for name in ('preflight.PASS.json','batch.PASS.json','batch.STOP.json')])
    absent(generic_outputs())
    armed=True
    for defect in ['disabled','wronghost','argv','cap','missing-input']:
        run('gate-'+defect,'probe.py',[ROOT/'generic.plan.json',ROOT/('gate-'+defect+'.sentinel'),'plain'],'probe',defect=defect)
    run('gate-valid','probe.py',[ROOT/'generic.plan.json',ROOT/'gate-valid.sentinel','plain'],'probe')
    require((ROOT/'gate-valid.sentinel').read_bytes()==b'POSTAUTHORIZE\n','valid gate failed')
    run('dummy-descendant','probe.py',[ROOT/'generic.plan.json',ROOT/'dummy-descendant.sentinel','descendant'],'dummy')
    exclusive(ROOT/'preflight.PASS.json',{'status':'PASS','records':records,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    generic=run('generic','generic_controls.py',[ROOT/'generic.receipt.json'],
        'generic',operation='build',mathematical=True)
    require((ROOT/'generic.receipt.json').is_file()
            and not (ROOT/'generic.receipt.json').is_symlink(),'regular generic receipt required')
    receipt_sha=digest(ROOT/'generic.receipt.json')
    receipt=read_json(ROOT/'generic.receipt.json')
    require(set(receipt)=={'schema','status','scope','execution','engine','harness_sha256',
                         'solver_sha256','positives','negatives'}, 'complete generic summary fields')
    require(receipt['schema']=='F10-GENERIC-CONTROLS/v1'
            and receipt['status']=='ALL-12-GENERIC-CONTROLS-VERIFIED-NO-SOURCE-ACCEPTANCE'
            and receipt['scope']=='synthetic rank-seven fixtures only; no actual-source decision or acceptance',
            'genuine generic receipt scope')
    require(receipt['execution']=={'job_tag':JOB,'hostname':registration['hostname'],
             'instance_id':INSTANCE,'authority_sha256':generic['authority_sha256']}
            and receipt['engine']==environment
            and receipt['harness_sha256']==known['generic_controls.py']
            and receipt['solver_sha256']==known['solver.py'], 'generic runtime/source binding')
    positives,negatives=receipt['positives'],receipt['negatives']
    require(type(positives) is list and len(positives)==8
            and type(negatives) is list and len(negatives)==4,'complete ordered control inventory')
    artifacts=[]
    def bound_artifact(pin, expected):
        require(type(pin) is dict and set(pin)=={'path','sha256'}
                and pin['path']==str(expected), 'literal generic sidecar binding')
        require(expected.is_file() and not expected.is_symlink(), 'regular generic sidecar required')
        raw=expected.read_bytes()
        require(hashlib.sha256(raw).hexdigest()==pin['sha256'],'generic sidecar hash mismatch')
        # Harness embeds hashes, not sizes. Record observed byte counts, never
        # pretend a missing embedded size was checked. No fixture JSON parsing.
        artifacts.append(dict(pin, bytes=len(raw)))
    for result,(name,branch) in zip(positives,plan['positive_cases']):
        require(type(result) is dict and set(result)=={'id','status','input','certificate','check'}
                and result['id']==name and result['status']=='VERIFIED-SYNTHETIC-ONLY',
                'positive ordered name/status/fields')
        expected=({'branch':'UNIT','checked_coordinates':217,'multipliers':9,'multiplier_degree_bound':25}
                  if branch=='UNIT' else {'branch':'SEPARATOR','checked_columns':1638,'target_coordinates':217})
        check=result['check']
        require(type(check) is dict and check==expected
                and all(type(check[k]) is int for k in expected if k!='branch'),
                'complete independent verifier count/branch receipt')
        bound_artifact(result['input'],ROOT/('generic.receipt.json.'+name+'.input.json'))
        bound_artifact(result['certificate'],ROOT/('generic.receipt.json.'+name+'.candidate.json'))
    for result,(name,reason) in zip(negatives,plan['negative_cases']):
        require(type(result) is dict and set(result)=={'id','status','fixture','exception_class','reason'}
                and result['id']==name and result['status']=='EXPECTED-REFUSAL'
                and result['exception_class']=='ValueError' and result['reason']==reason,
                'changed-object ordered name/exact predicate')
        bound_artifact(result['fixture'],ROOT/('generic.receipt.json.'+name+'.negative.json'))
    fixed_barrier(ROOT/'generic.authority.json',generic['authority_sha256'])
    require(digest(ROOT/'generic.receipt.json')==receipt_sha,'generic receipt changed during readback')
    require(time.time()<generic['hard_cutoff_epoch'],'generic validation after original hard cutoff')
    exclusive(ROOT/'batch.PASS.json',{'status':'QUOTIENT-GENERIC-ENGINEERING-PASS-NOT-ACTUAL-SOURCE',
        'records':records,'generic_plan_sha256':known['generic.plan.json'],'artifacts':artifacts,
        'receipt_sha256':receipt_sha,'receipt_bytes':(ROOT/'generic.receipt.json').stat().st_size,
        'first_math_epoch':first_math,'end_epoch':time.time(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})

try:
    main()
except BaseException as exc:
    if armed:
        exclusive(ROOT/'batch.STOP.json',{'status':'STOP-NONDECISION','error':type(exc).__name__+': '+str(exc),
            'records':records,'first_math_epoch':first_math,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    raise
