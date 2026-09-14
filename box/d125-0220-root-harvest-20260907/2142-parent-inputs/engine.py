"""Two fixed engineering payloads only. No launch loop or production source read."""
import json,os,signal,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import driver as D
import exact as E
import hybrid as H
ROOT=Path('/home/ubuntu/d125-hybrid81-exact-solver-20260907')
ENG=ROOT/'engineering'
FIXTURE_SHA='d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf'
PINS={'driver.py':'ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a',
      'exact.py':'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
      'hybrid.py':'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3'}

def control_binding(a,operation,helper_sha,green_sha):
    E.need(operation in ('hybrid','alarm'),'fixed engineering operation only')
    E.need(a.get('mode')=='engineering_control','engineering authority only')
    E.need(a.get('engineering')=={'operation':operation,'helper_sha256':helper_sha,
        'fixture_sha256':FIXTURE_SHA,'root_green_sha256':green_sha},'helper/fixture/physical GREEN binding')
    E.need(len(green_sha)==64 and all(c in '0123456789abcdef' for c in green_sha),'physical GREEN digest')

def hybrid_script(data):
    E.need(E.digest(data)==FIXTURE_SHA,'fixed tiny fixture pin')
    variables,rows,labels,prefix=H.read_hybrid(data,production=False)
    E.need(len(variables)==4 and len(rows)==7,'tiny fixture shape')
    script=prefix+D.footer(variables,FIXTURE_SHA,control=True)
    E.need(not any(x in script for x in ('slimgb','std(','dim(','system(','write(','LIB ')),'control script contains solver/external command')
    E.need(len(script.encode('ascii'))<=32768,'tiny script cap')
    return script

def alarm_script():
    return 'ring R=0,(x),dp;\nint alarmspin=0;\nprint("JC2_HYBRID81_ALARM_READY");\nwhile(1){alarmspin=1-alarmspin;}\n'

def check_hybrid(data,stdout,stderr):
    E.need(E.digest(data)==FIXTURE_SHA and len(stdout)<=65536,'tiny replay bounds/pin')
    variables,rows,labels,unused=H.read_hybrid(data,production=False)
    engine,basis,cofactors=E.parse_result(stdout,stderr,variables,FIXTURE_SHA)
    E.need(cofactors is not None and len(engine)==len(cofactors)==len(rows)==7 and basis==[E.ONE],'complete actual tiny I/G/T columns')
    verdict,mapping,lifted=E.unit_certificate(rows,engine,cofactors)
    E.need(mapping==[0,1,0,1,4,0,6],'tiny zero/duplicate mapping')
    return {'status':'TINY_HYBRID_ENGINE_REPLAY_PASS','verdict':verdict,'rows':7,'engine_columns':len(engine),'cofactor_rows':len(cofactors),'mapping':mapping}

def expected_parent_argv(operation):
    E.need(operation in ('hybrid','alarm'),'fixed engineering operation only')
    return [x.encode('ascii') for x in [
        '/usr/bin/python3','-I','-B',str(ROOT/'run_capped.py'),
        '--wall-seconds','10','--cpu-seconds','10',
        '--rss-bytes','536870912','--rss-sample-seconds','0.05',
        '--term-grace-seconds','0.25','--cwd',str(ROOT),
        '--stdout-file',str(ENG/(operation+'.stdout')),
        '--stderr-file',str(ENG/(operation+'.stderr')),
        '--telemetry-file',str(ENG/(operation+'.telemetry.json')),
        '--','/usr/bin/python3','-I','-B',str(ROOT/'engine.py'),
        operation,str(ENG/(operation+'.authority.json'))]]

def payload(operation,authority_path):
    E.need(operation in ('hybrid','alarm'),'fixed engineering operation only')
    E.need(Path(__file__).resolve()==ROOT/'engine.py' and Path.cwd()==ROOT,'exact engineering code/cwd')
    E.need(Path(authority_path).resolve()==ENG/(operation+'.authority.json'),'distinct fixed authority path')
    a,authority_sha,duration=D.context(authority_path,'control')
    control_binding(a,operation,D.file_sha(__file__),D.file_sha(ENG/'ROOT-GREEN.md'))
    E.need({name:D.file_sha(ROOT/name) for name in PINS}==PINS,'fixed engineering code pins')
    E.need(os.getpid()==os.getpgrp(),'exact CAPRUN payload group leader')
    parent=Path('/proc')/str(os.getppid())
    E.need((parent/'cmdline').read_bytes().split(b'\0')==expected_parent_argv(operation)+[b''],'exact registered CAPRUN parent argv')
    # Root controller owns stdout/stderr/telemetry; only these two payload files
    # are reserved here. No external process or inherited session is created.
    for suffix in ('sing','identity.json'):
        E.need(not os.path.lexists(ENG/(operation+'.'+suffix)),'exclusive engineering payload output')
    D.arm_deadline(a,min(duration,1.0) if operation=='alarm' else duration)
    D.limits('control')
    identity={'operation':operation,'pid':os.getpid(),'pgid':os.getpgrp(),
        'start_ticks':Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],
        'host':D.observed_host(),'namespace':os.readlink('/proc/self/ns/pid'),
        'cgroup':Path('/proc/self/cgroup').read_text(),'authority_sha256':authority_sha,
        'helper_sha256':D.file_sha(__file__),'utc':time.time(),
        'timer_remaining':signal.getitimer(signal.ITIMER_REAL),'source_access':False}
    D.write_new(ENG/(operation+'.identity.json'),E.canonical(identity))
    script=hybrid_script((ENG/'tiny-engine-fixture.jsonl').read_bytes()) if operation=='hybrid' else alarm_script()
    path=ENG/(operation+'.sing');D.write_new(path,script.encode('ascii'))
    env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
    os.execve('/usr/bin/Singular',['Singular','--no-rc','-q',str(path)],env)

if __name__=='__main__':
    E.need(len(sys.argv)==3,'fixed operation and authority path required')
    payload(sys.argv[1],sys.argv[2])
