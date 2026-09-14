"""Fresh read-only production readiness; no rows/maps or writes."""
from pathlib import Path
import hashlib,json,os,platform,subprocess,time
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
need(platform.system()=='Linux' and Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2' and Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','host')
boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip();need(boot=='bef732b9-38e5-4a9a-8f93-77203426d2b8','boot')
expected={'construct.py':'aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264','replay.py':'06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23','baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53','run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2','REGISTRATION.md':'1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6','ROOT-GREEN.md':'12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36','authority.json':'d3a16840b13b51bb503c26416cab1fa79c316599acf1e0d4b9fb9ffb8e0e1f17'}
pins={n:sha(W/n) for n in expected};need(pins==expected,'existing pin drift')
paths={n:os.path.lexists(W/n) for n in ('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr','pilot.telemetry.json','production.claim.json','production.launch.json','production.receipt.json','engineering/rss.authority.json','engineering/ROOT-GREEN.md')};need(not any(paths.values()),'fresh output/archive path occupied')
source='/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl';source_sha=sha(source);need(source_sha=='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','source pin')
ps=subprocess.check_output(['ps','-eo','pid,ppid,pgid,lstart,stat,args'],text=True).splitlines()
user=[]
for line in ps[1:]:
    parts=line.split(None,3)
    if len(parts)==4 and parts[1]!='2':user.append(line)
print(json.dumps(dict(utc=time.time(),boot=boot,pins=pins,source_sha256=source_sha,paths=paths,processes=user,
    memory=subprocess.check_output(['free','-m'],text=True),disk=subprocess.check_output(['df','-Pk',str(W)],text=True),
    ebs=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),
    mount=subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','/'],text=True),
    executables={p:sha(p) for p in ('/usr/bin/python3','/usr/bin/prlimit')},
    old_ids_absent=all(not Path('/proc',str(p)).exists() for p in (1536,1537,1538,1541,1542,1544))),sort_keys=True))
