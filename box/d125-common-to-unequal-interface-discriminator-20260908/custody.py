import sys
sys.dont_write_bytecode=True
import pathlib,hashlib,json
root=pathlib.Path('/home/ubuntu/jc2')
box=pathlib.Path(__file__).resolve().parent
report=root/'xmodel/d125-common-to-unequal-interface-discriminator-astra-20260908.md'
source=root/'xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md'
files=[source,report,*sorted(box.glob('*.py')),box/'replay.json',box/'witness.json']
files.extend(sorted(report.parent.glob('.'+report.name+'.transaction*')))
rows=[]
for p in files:
    raw=p.read_bytes(); rows.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
if rows[0]['sha256']!='7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413':raise RuntimeError('source changed')
with (box/'custody.json').open('xb') as f:f.write((json.dumps({'status':'TERMINAL','owner':'/root/nonemptiness_certificate','all_writers_idle':True,'no_remote_jobs':True,'entries':rows},sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({'custody_sha256':hashlib.sha256((box/'custody.json').read_bytes()).hexdigest(),'entries':len(rows),'report_sha256':rows[1]['sha256']}))
