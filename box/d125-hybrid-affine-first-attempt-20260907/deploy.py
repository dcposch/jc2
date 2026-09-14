"""Single exclusive deployment under HYBRID-ENGINEERING-GREEN; no arithmetic."""
import base64,hashlib,json,subprocess
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');OWN=ROOT/'box/d125-hybrid-affine-first-attempt-20260907'
FILES={
 'construct.py':('box/d125-hybrid-affine-code-prep-20260907/construct.py','aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264'),
 'replay.py':('box/d125-hybrid-affine-code-prep-20260907/replay.py','06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23'),
 'baseline.py':('box/d125-hybrid-affine-code-prep-20260907/baseline.py','ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'),
 'run_capped.py':('box/full-j-solver-pilot-20260906/evidence/run_capped.py','4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'),
 'engineering/host_control.py':('box/d125-hybrid-pilot-readiness-20260907/host_control.py','3ea4ba7cd62600ba351a27640ee44815adc70fbd27e18729c180f2a550f215ba'),
 'REGISTRATION.md':('box/d125-hybrid-affine-first-attempt-20260907/REGISTRATION.md','1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6'),
 'ROOT-GREEN.md':('box/d125-0220-root-harvest-20260907/HYBRID-ENGINEERING-GREEN.md','12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36')}
payload={}
for name,(path,pin) in FILES.items():
    b=(ROOT/path).read_bytes()
    if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('local pin '+name)
    payload[name]={'sha256':pin,'base64':base64.b64encode(b).decode()}
script='files='+repr(payload)+'\n'+r'''
import base64,hashlib,json,os,platform,socket,time
from pathlib import Path
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
need(platform.system()=='Linux' and Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','EC2 host')
need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','instance')
boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip();need(boot=='bef732b9-38e5-4a9a-8f93-77203426d2b8','boot')
need(time.time()<1788759540,'GREEN dispatch window expired')
need(not os.path.lexists(W),'new workdir not absent')
source='/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl'
source_sha=sha(source);need(source_sha=='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','source byte-hash custody')
W.mkdir();(W/'engineering').mkdir()
for name,v in files.items():
    b=base64.b64decode(v['base64']);need(hashlib.sha256(b).hexdigest()==v['sha256'],'transport pin')
    with (W/name).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
pins={n:sha(W/n) for n in files};need(all(pins[n]==v['sha256'] for n,v in files.items()),'deployed hash')
print(json.dumps(dict(status='EXCLUSIVE_DEPLOYMENT_PASS',boot=boot,hostname=socket.gethostname(),utc=time.time(),pins=pins,source_sha256=source_sha,source_access='opaque hash only',authority_absent=not os.path.lexists(W/'authority.json'),construction_absent=not os.path.lexists(W/'construction.jsonl'),replay_absent=not os.path.lexists(W/'replay-result.json')),sort_keys=True))
'''
r=subprocess.run(['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=10','ubuntu@172.30.0.56','/usr/bin/python3 -I -B -'],input=script,text=True,capture_output=True)
print(json.dumps(dict(returncode=r.returncode,stdout=r.stdout,stderr=r.stderr),sort_keys=True))
raise SystemExit(r.returncode)
