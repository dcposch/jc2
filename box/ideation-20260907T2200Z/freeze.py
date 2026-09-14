"""One bounded mechanical copy of explicitly named common packet inputs."""
from pathlib import Path
import hashlib,json,os
R=Path('/home/ubuntu/jc2');B=Path(__file__).parent;S=B/'snapshots';S.mkdir(exist_ok=False)
names=['APPROACHES.md','AUDIT.md','PROGRESS.md','notes.md','COORDINATION.md','ladder/REDUCTION.md','history/APPROACHES-before-20260906-cleanup.md','xmodel/ideation-20260906T1435Z-synthesis.md','xmodel/websweep-20260907T0735Z-astra.md','xmodel/d125-pure-uniform-discriminator-astra-20260907.md','xmodel/d125-pure-uniform-gate-fable5-20260907.md','xmodel/d125-exceptional-pure-gate-fable5-20260907.md','xmodel/d125-arc-closure-interface-astra-20260907.md','box/websweep-20260907T0735Z/sources/furter-proof.typ','box/websweep-20260907T0735Z/sources/furter-primary-author.pdf','FALLACY-v2.md']
for n in names:
 if not (R/n).is_file():raise RuntimeError('missing '+n)
if len({Path(n).name for n in names})!=len(names):raise RuntimeError('duplicate basename')
pins={}
for n in names:
 data=(R/n).read_bytes();p=S/Path(n).name
 with p.open('xb') as f:f.write(data)
 os.chmod(p,0o444);pins[n]={'snapshot':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
p=B/'packet.md';pins['packet']={'snapshot':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()};os.chmod(p,0o444)
with (B/'MANIFEST.json').open('x') as f:json.dump({'basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','inputs':pins},f,sort_keys=True,indent=2);f.write('\n')
os.chmod(B/'MANIFEST.json',0o444);print(json.dumps({'inputs':len(pins),'manifest_sha256':hashlib.sha256((B/'MANIFEST.json').read_bytes()).hexdigest(),'packet_sha256':pins['packet']['sha256']}))
