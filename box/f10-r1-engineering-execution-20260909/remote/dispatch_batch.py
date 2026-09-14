"""One owned engineering batch. No solver or supervisor replacement.
RLIMIT_FSIZE is inherited BEFORE exec of the exact existing CAPRUN argv.
No new PGID is created by this caller; CAPRUN owns its recorded child PGID.
"""
import sys
sys.dont_write_bytecode = True
import os, json, hashlib, socket, resource, subprocess, time, datetime
from pathlib import Path
ROOT = Path('/home/ubuntu/f10-r1-exact-artifact-validation-20260909')
INSTANCE = 'i-08d2a40f272ee9fa2'
JOB = 'f10-r1-exact-artifact-validation-20260909'
DEADLINE = datetime.datetime(2026,9,9,12,53,tzinfo=datetime.timezone.utc).timestamp()
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

def run(name, script, trailing, operation='check', wall=30, cpu=25, rss=2147483648, defect=None, mathematical=False):
    global first_math
    if mathematical:
        now=time.time()
        if first_math is None: first_math=now
        hard=min(DEADLINE, first_math+360)
        require(now+wall+2 < hard, 'insufficient remaining mathematical budget')
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
    files={str(ROOT/n):digest(ROOT/n) for n in ['builder.py','checker.py','execution_gate.py','run_capped.py',
             'probe.py','precision.py','dispatch_batch.py','admissibility.md','frontier.json']}
    files['/usr/bin/python3']=digest('/usr/bin/python3')
    if operation=='check': files[str(trailing[0])]=digest(trailing[0])
    spec={'schema':'F10-R1-REGISTERED/v1','enabled':True,'job_tag':JOB,'operation':operation,
          'instance_id':INSTANCE,'hostname':socket.gethostname(),'admissibility_sha256':digest(ROOT/'admissibility.md'),
          'runner_path':str(ROOT/'run_capped.py'),'cwd':str(ROOT),'caps':caps,
          'stdout_file':str(ROOT/(name+'.stdout')),'stderr_file':str(ROOT/(name+'.stderr')),
          'telemetry_file':str(ROOT/(name+'.telemetry.json')),'parent_argv':parent,'child_argv':child,'file_sha256':files}
    if defect=='disabled': spec['enabled']=False
    if defect=='wronghost': spec['hostname']='NOT-THE-REGISTERED-HOST'
    if defect=='argv': spec['parent_argv']=parent+['EXTRA']
    if defect=='cap': spec['caps']=dict(caps,rss_bytes='1')
    if defect=='missing-input': del spec['file_sha256'][str(trailing[0])]
    exclusive(auth,spec)
    namespace=os.readlink('/proc/self/ns/pid')
    started=time.time()
    with (ROOT/(name+'.caller.stdout')).open('x') as out, (ROOT/(name+'.caller.stderr')).open('x') as err:
        process=subprocess.Popen(parent,stdin=subprocess.DEVNULL,stdout=out,stderr=err,cwd=ROOT,
                                 preexec_fn=filelimit, start_new_session=False)
        require(os.readlink(f'/proc/{process.pid}/ns/pid')==namespace,'caller PID namespace mismatch')
        caller_stat=Path(f'/proc/{process.pid}/stat').read_text()
        rc=process.wait()
    telemetry=json.loads((ROOT/(name+'.telemetry.json')).read_text())
    require(not quiet(telemetry['pgid']), 'owned live PGID after CAPRUN')
    for filename,want in files.items(): require(digest(filename)==want,'source/input changed')
    record={'name':name,'returncode':rc,'started_utc':datetime.datetime.fromtimestamp(started,datetime.timezone.utc).isoformat(),
            'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'namespace':namespace,
            'caller_pid':process.pid,'caller_stat':caller_stat,'authority_sha256':digest(auth),
            'telemetry_sha256':digest(ROOT/(name+'.telemetry.json')),'mathematical':mathematical,
            'first_math_epoch':first_math,'remaining_group_live':[]}
    records.append(record); exclusive(ROOT/(name+'.dispatch.json'),record)
    if defect:
        require(rc!=0 and telemetry['status']=='NORMAL_EXIT','gate refusal was not ordinary nonzero exit')
        require(not Path(trailing[1]).exists(),'postauthorize sentinel written by rejected authority')
    elif name=='dummy-descendant':
        require(rc==125 and telemetry['resource']=='rss','dummy did not exercise RSS cap')
        term=telemetry['termination']
        require(term['term_sent'] and term['kill_sent'] and term['cleanup_complete'] and term['leader_reaped'], 'dummy cleanup failed')
        require(telemetry['max_observed_group_rss_bytes']>rss,'descendant RSS not measured')
        lines=[json.loads(x) for x in (ROOT/(name+'.stdout')).read_text().splitlines()]
        require(len(lines)==2 and all(x['namespace']==namespace for x in lines),'dummy namespace/custody missing')
        require(all(x['pgid']==telemetry['pgid'] for x in lines),'descendant escaped recorded PGID')
        require(all(x.get('result')=='MATCH' for x in telemetry['identity_checks']), 'TERM/KILL identity not matched')
    else:
        require(rc==0 and telemetry['status']=='NORMAL_EXIT','cap/failure: STOP, no retry')
    return record

def main():
    require(Path.cwd()==ROOT,'wrong remote cwd')
    require(Path('/sys/devices/virtual/dmi/id/board_asset_tag').read_text().strip()==INSTANCE,'wrong physical instance')
    require(socket.gethostname()=='ip-172-30-0-72','refuse math-hq or wrong host')
    require(digest('/usr/bin/python3')=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223','interpreter pin')
    require(digest(ROOT/'admissibility.md')=='02952e1b804ce553c4bd8abf63daab1357cba5a19f78b1abe38ba6c933b0910a','admissibility pin')
    require(digest(ROOT/'frontier.json')=='f9d1fddcef51ecdb10ad01eeb59551809eb31a964d41202072d3fe27388b0e34','frontier pin')
    require(digest(ROOT/'builder.py')=='2dcba70d4f14080535c4a58f06bfd50ba4949148e819a6827ab9326828d314b8','builder pin')
    require(digest(ROOT/'checker.py')=='e2970c71774607e211ecc7e0f001a0dc02d02410e303ca58cf7c17ab77b9f545','checker pin')
    require(digest(ROOT/'execution_gate.py')=='cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6','gate pin')
    require(digest(ROOT/'run_capped.py')=='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2','CAPRUN pin')
    for defect in ['disabled','wronghost','argv','cap','missing-input']:
        run('gate-'+defect,'probe.py',[ROOT/'frontier.json',ROOT/('gate-'+defect+'.sentinel'),'plain'],wall=5,cpu=3,defect=defect)
    run('gate-valid','probe.py',[ROOT/'frontier.json',ROOT/'gate-valid.sentinel','plain'],wall=5,cpu=3)
    require((ROOT/'gate-valid.sentinel').read_text()=='POSTAUTHORIZE\n','valid gate failed')
    run('dummy-descendant','probe.py',[ROOT/'frontier.json',ROOT/'dummy-descendant.sentinel','descendant'],wall=5,cpu=3,rss=33554432)
    exclusive(ROOT/'preflight.PASS.json',{'status':'PASS','records':records,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    run('build','builder.py',[ROOT/'exact.json'],operation='build',wall=60,cpu=50,mathematical=True)
    for mode in ['full','u-zero','dropped-constant','u-zero-dropped-constant','upper-coefficient','guard','leading-top']:
        run('check-'+mode,'checker.py',[ROOT/'exact.json',ROOT/('check-'+mode+'.receipt.json'),mode],mathematical=True)
    run('precision','precision.py',[ROOT/'exact.json',ROOT/'precision.receipt.json'],mathematical=True)
    exclusive(ROOT/'batch.PASS.json',{'status':'ENGINEERING-PASS-NOT-IDEAL-DECISION','records':records,
              'first_math_epoch':first_math,'end_epoch':time.time(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})

try:
    main()
except BaseException as exc:
    exclusive(ROOT/'batch.STOP.json',{'status':'STOP-NONDECISION','error':type(exc).__name__+': '+str(exc),
        'records':records,'first_math_epoch':first_math,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    raise
