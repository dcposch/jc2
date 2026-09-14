import datetime, hashlib, json, pathlib, subprocess
root=pathlib.Path('/home/ubuntu/jc2')
own=root/'box/ideation-20260909T0310Z-astra'
prompt=root/'box/ideation-20260909T0310Z-prep/root-invite-astra.prompt.md'
manifest=root/'box/ideation-20260909T0310Z-prep/ROOT-FINAL-MANIFEST.json'
final=root/'xmodel/ideation-20260909T0310Z-astra.md'
if final.exists() or list(final.parent.glob('.'+final.name+'.partial-*')) or (final.parent/('.'+final.name+'.artifact-lease.json')).exists():
    raise SystemExit('own output collision')
m=json.loads(manifest.read_text())
r=subprocess.run(['sed','-n','s/^charged_input=//p',str(prompt)],capture_output=True,text=True,check=True,timeout=30)
paths=r.stdout.splitlines()
expected=[e['path'] for e in m['entries']]+[str(manifest.relative_to(root))]
if paths!=expected or len(paths)!=32 or len(set(paths))!=32:
    raise SystemExit('charged vector mismatch')
pins=[]
for path in paths:
    b=(root/path).read_bytes(); digest=hashlib.sha256(b).hexdigest()
    e=next((e for e in m['entries'] if e['path']==path),None)
    if e and (digest!=e['sha256'] or len(b)!=e['bytes']):
        raise SystemExit('charged drift '+path)
    pins.append({'path':path,'sha256':digest,'bytes':len(b)})
record={'actual_start_utc':'2026-09-09T03:30:40Z','verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'freeze_utc':m['freeze_utc'],'deadline_utc':'2026-09-09T04:20:00Z','entries':pins,
        'prompt_sha256':hashlib.sha256(prompt.read_bytes()).hexdigest(),'sed_count':32,
        'collision':'ABSENT','mathematical_subprocesses':0,'peer_reads':False}
with (own/'input-pins.json').open('x') as f: json.dump(record,f,indent=2)
print(json.dumps({'verified_utc':record['verified_utc'],'pins':32,'collision':'ABSENT','prompt_sha256':record['prompt_sha256']}))
