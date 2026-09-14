"""Publish completed preparation and freeze exact owned custody; no launch."""
import datetime, hashlib, json, pathlib, subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z'
report=R/'xmodel/ideation-20260909T0040Z-prep-astra.md'
token='fe01992ce3e308abeeff888e0939553c3efcae525751596c7abe0972592a6c37'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
results=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B',str(R/'ops/artifact_finalize.py'),phase,'--final',str(report)]
 if phase!='verify': argv+=['--token',token]
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,check=True)
 results.append(dict(argv=argv,stdout=p.stdout,stderr=p.stderr,rc=p.returncode))
with (B/'publication.json').open('x') as f: json.dump(results,f,indent=2); f.write('\n')
owned=[p for p in sorted(B.rglob('*')) if p.is_file()]+[report,pathlib.Path(str(report)+'.artifact.json')]
entries=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in owned]
custody=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),owner='/root/model_productivity',status='TERMINAL_PREP_ONLY_NO_INVITATION',writers='IDLE after this final exclusive custody write; no further input writes',entries=entries)
with (B/'custody.json').open('x') as f: json.dump(custody,f,indent=2); f.write('\n')
for p in owned+[B/'custody.json']: p.chmod(0o444)
print(json.dumps(dict(report_sha256=sha(report),transaction_sha256=sha(pathlib.Path(str(report)+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'PINS.json'),manifest_sha256=sha(B/'MANIFEST.json'),prompts={s:sha(B/(s+'.prompt.md')) for s in ['coordinator','astra','fable5','sol56']},owned_pins=len(entries),writers='IDLE',launch_performed=False)))
