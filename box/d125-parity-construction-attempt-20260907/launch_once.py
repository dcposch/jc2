"""Single root-authorized argv-only dispatch, supplied to SSH stdin."""
import datetime,hashlib,json,os,socket,subprocess,sys,time
from pathlib import Path
W=Path('/home/ubuntu/d125-parity-compression-pilot-20260907')
BOOT='1a830d1e-1fa2-47f3-98bc-8c26c8cb8453'
PINS={'construct.py':'22173cc6a9217a90a8537081a1229b01e58017990b728291285e8cfc01a332a2',
      'replay.py':'2dbb7464fd7b59e361f34b5a705cc7359b98001bf570a80fc77f441e029c2a17',
      'baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
      'qpoly.py':'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
      'run_once.py':'d164af0b576fd7d8f7e3c3a294da8211df996595677aeac75267d2bf9546d40f',
      'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'}
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    with Path(p).open('x') as f:json.dump(v,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def ident(pid):
    p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    return dict(pid=pid,pgid=int(s[2]),start_ticks=s[19],boot=BOOT,cgroup=(p/'cgroup').read_text(),
                namespace=os.readlink(p/'ns/pid'),argv=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode())
os.chdir(W)
need(time.time()<datetime.datetime(2026,9,7,3,55,tzinfo=datetime.timezone.utc).timestamp(),'launch window closed')
need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54' and
     Path('/proc/sys/kernel/random/boot_id').read_text().strip()==BOOT,'host/boot mismatch')
need(socket.gethostname()=='ip-172-30-0-56','hostname mismatch')
need({k:sha(W/k) for k in PINS}==PINS,'code pins')
reg=sha(W/'REGISTRATION.md');need(reg=='9435f425ddd135846480dd1cdb08674de3b376803a1f73e93804a546c5b5d107','registration')
need(sha('/usr/bin/python3')=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223' and
     sha('/usr/bin/prlimit')=='17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069','binary pins')
for name in ['authority.json','construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr','pilot.telemetry.json']:
    need(not(W/name).exists(),'exclusive path already exists '+name)
save(W/'pilot-pre.json',dict(controller=ident(os.getpid()),hostname=socket.gethostname(),pins=PINS,
     registration=reg,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
     actual_total=[75,125],partial_u=[15,25],partial_v=[60,100],finite_support=True,
     memory=subprocess.check_output(['free','-m'],text=True),disk=subprocess.check_output(['df','-Pk',str(W)],text=True)))
dispatched=time.time();expiry=dispatched+300
a=dict(schema='jc2.d125-parity-construction-authority/v1',root_green=True,construction_only=True,mode='slice',
       job='d125-parity-construction-attempt-astra-20260907',boot_id=BOOT,code_sha256=PINS,
       source_sha256='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac',
       symmetry_sha256='9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12',
       symmetry_gate_accepted=True,symmetry_gate_sha256='3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d',
       registration_sha256=reg,expires_unix=expiry,
       caps=dict(wall_seconds=300,cpu_seconds=300,address_bytes=4294967296,output_bytes=134217728,
                 polynomial_terms=100000,multiply_pairs=1000000,retained_terms=1000000,coefficient_bits=4096))
save(W/'authority.json',a)
cmd=['/usr/bin/prlimit','--fsize=134217728:134217728','--core=0:0','--','/usr/bin/python3','-I','-B',str(W/'run_capped.py'),
     '--wall-seconds','300','--cpu-seconds','300','--rss-bytes','4294967296','--rss-sample-seconds','0.05',
     '--term-grace-seconds','0.25','--cwd',str(W),'--stdout-file',str(W/'pilot.stdout'),
     '--stderr-file',str(W/'pilot.stderr'),'--telemetry-file',str(W/'pilot.telemetry.json'),'--',
     '/usr/bin/python3','-I','-B',str(W/'run_once.py'),str(W/'authority.json')]
with (W/'pilot-runner.stdout').open('xb') as out,(W/'pilot-runner.stderr').open('xb') as err:
    p=subprocess.Popen(cmd,cwd=W,stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=True)
    launch=dict(argv=cmd,runner=ident(p.pid),controller=ident(os.getpid()),hostname=socket.gethostname(),
                authority_sha256=sha(W/'authority.json'),dispatch_unix=dispatched,expires_unix=expiry)
    save(W/'pilot.launch.json',launch)
    payload=None
    for _ in range(100):
        for entry in Path('/proc').iterdir():
            if not entry.name.isdigit():continue
            try:
                s=(entry/'stat').read_text().rsplit(') ',1)[1].split()
                argv=(entry/'cmdline').read_bytes()
                if int(s[1])==p.pid and str(W/'run_once.py').encode() in argv:payload=ident(int(entry.name));break
            except (FileNotFoundError,ProcessLookupError):continue
        if payload is not None:break
        time.sleep(.01)
    save(W/'pilot.payload-identity.json',dict(payload=payload,expires_unix=expiry))
    print(json.dumps(dict(status='DISPATCHED_ONCE',runner=launch['runner'],payload=payload,expires_unix=expiry)),flush=True)
    rc=p.wait()
save(W/'pilot-runner.result.json',dict(runner_rc=rc,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
     runner_absent=not Path('/proc',str(p.pid)).exists(),authority_sha256=sha(W/'authority.json')))
print(json.dumps(dict(status='RUNNER_TERMINAL',runner_rc=rc)),flush=True)
