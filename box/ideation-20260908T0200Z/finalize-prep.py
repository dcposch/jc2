import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,subprocess
R=Path('/home/ubuntu/jc2');B=Path(__file__).resolve().parent
manifest=json.loads((B/'MANIFEST.json').read_bytes())
for x in manifest['inputs']:
    if hashlib.sha256((R/x['snapshot']).read_bytes()).hexdigest()!=x['sha256']:raise RuntimeError('snapshot changed '+x['snapshot'])
    if x['scope']=='whole' and x['source']!='owned packet':
        if hashlib.sha256((R/x['source']).read_bytes()).hexdigest()!=x['sha256']:raise RuntimeError('source changed '+x['source'])
vectors=[]; normalized=[]
for lane in ('coordinator','astra','fable5','sol56'):
    p=B/(lane+'.prompt.md');raw=p.read_bytes()
    vectors.append(subprocess.run(['sed','-n','s/^charged_input=//p',str(p)],check=True,stdout=subprocess.PIPE).stdout)
    normalized.append(raw.replace(('20260908T0200Z-'+lane+'.md').encode(),b'20260908T0200Z-LANE.md'))
    if b'{{LANE_INPUTS}}' not in raw:raise RuntimeError('missing placeholder')
    if any(z.startswith(b'charge_basis') for z in raw.splitlines()):raise RuntimeError('exit-price declaration')
if len(set(vectors))!=1 or len(set(normalized))!=1:raise RuntimeError('lane contracts differ')
report=R/'xmodel/ideation-20260908T0200Z-prep-astra.md'
files=sorted(p for p in B.rglob('*') if p.is_file())+[report,Path(str(report)+'.artifact.json')]
entries=[]
for p in files:
    data=p.read_bytes();entries.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
record={'status':'TERMINAL PREP ONLY','all_writers_idle':True,'invitations':0,'root_blind_read':False,'root_blind_sealed':'NOT CHECKED; REQUIRED BEFORE INVITATIONS','all_four_contracts_identical_except_report_target':True,'literal_lane_parser_verified':True,'full_current_source_pins_verified':True,'entries':entries}
with (B/'custody.json').open('xb') as f:f.write((json.dumps(record,indent=2,sort_keys=True)+'\n').encode())
print(json.dumps({'status':'PASS','entries':len(entries),'custody_sha256':hashlib.sha256((B/'custody.json').read_bytes()).hexdigest(),'prompts':{lane:hashlib.sha256((B/(lane+'.prompt.md')).read_bytes()).hexdigest() for lane in ('coordinator','astra','fable5','sol56')}}))
