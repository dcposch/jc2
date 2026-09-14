"""Pin prepared prompt and terminal local evidence; never submit a lane."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
def pin(p):return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
charged={}
for line in (HERE/'prompt.txt').read_text().splitlines():
    if line.startswith('charged_input='):
        name=line.split('=',1)[1];charged[name]=pin(ROOT/name)
expected={'engine.py':'a87debfce5ca01817c03c2b180fd514d8e45269b1173c6f4a562255883188ae5',
          'ERRATUM.md':'bd312311284fc9617533f349f90306940b4bd105272434ef3627b00b4822a3c1',
          'driver.py':'ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a'}
for name,p in charged.items():
    if Path(name).name in expected and p['sha256']!=expected[Path(name).name]:raise RuntimeError('charged new scope drift')
probe_pids=[]
for mode in ('normal','optimized'):
    result=json.loads((HERE/(mode+'.stdout')).read_bytes())
    if result['status']!='PASS' or result['outcome_count']!=33:raise RuntimeError('replay incomplete')
    for probe in result['probes']:
        pid=probe['events'][0]['pid'];probe_pids.append(pid)
        if Path('/proc',str(pid)).exists():raise RuntimeError('probe identity remains')
owned={str(p.relative_to(HERE)):pin(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name!='PINS.json'}
value={'status':'FROZEN_PREP_ONLY_IDLE','submitted':False,'production_authority':False,
       'charged_inputs':charged,'owned':owned,'all_timed_probe_pids_absent':probe_pids,
       'caller_gate_report_sha256':'46a6304811af423042f29d9a8f4c3022189d648286e7770d02ae59d478615fac'}
with (HERE/'PINS.json').open('xb') as f:f.write(json.dumps(value,sort_keys=True,indent=2).encode()+b'\n')
print(json.dumps({'manifest':pin(HERE/'PINS.json'),'prompt':pin(HERE/'prompt.txt'),
      'harvest':pin(HERE/'HARVEST.md'),'replay':pin(HERE/'replay-results.json'),'probe_pids_absent':probe_pids},sort_keys=True))
