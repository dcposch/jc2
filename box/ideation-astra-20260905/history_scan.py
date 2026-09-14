#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
root=Path.cwd()
sys.path.insert(0,str(root/'ops'))
import open_collision
own=root/'xmodel/ideation-20260905T0200Z-astra.md'
blocked=('moh100-14rows-opus5-20260905','k16-f3abel-astra-20260905')
paths=[p for p in open_collision.banked_corpus(root,own) if not p.name.startswith(blocked) and not p.name.endswith('.prompt.md')]
paths += [root/'PROGRESS.md',root/'ladder/REDUCTION.md']
patterns={
'new_quartic':r'quartic.{0,100}Abel|Abel.{0,100}quartic|differential.compatible|lambda\s*=\s*36|69.{0,12}lambda',
'interface':r'DESCENT-CLASS-SPLIT-HALF|receiver atlas|certificate.pullback|source.to.receiver',
'finite_residue':r'90,\s*60.{0,80}45,\s*80,\s*88|twelve.{0,80}(Moh|excess)|12.{0,40}live.{0,40}rows',
}
log=[]
for name,pattern in patterns.items():
    hits=[]
    for i in range(0,len(paths),150):
        r=subprocess.run(['rg','-n','-i',pattern,*map(str,paths[i:i+150])],capture_output=True,text=True)
        if r.returncode not in (0,1):raise RuntimeError(r.stderr)
        hits.extend(r.stdout.splitlines())
    log.append(f'GROUP {name}: {len(hits)} matching lines')
    log.extend(hits)
    print(name,len(hits))
    for line in hits[:6]:print(line[:550])
(root/'box/ideation-astra-20260905/history-scan.log').write_text('\n'.join(log)+'\n')
print('Guarded corpus entries',len(paths),'Explicit receipt-only exclusions',len(blocked))
