from pathlib import Path
import hashlib,json
root=Path('box/graded-moh-20260905')
manifest=root/'resume-r2/final-custody.sha256'
exclude={manifest,root/'resume-r2/final-custody-check.log',root/'resume-r2/seal-check.log',root/'resume-r2/charge-check.log'}
files=[p for p in sorted(root.rglob('*')) if p.is_file() and p not in exclude and '__pycache__' not in p.parts]
with manifest.open('w') as out:
 for p in files:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8<<20),b''):h.update(b)
  out.write(h.hexdigest()+'  '+str(p)+'\n')
print(json.dumps(dict(files=len(files),bytes=sum(p.stat().st_size for p in files),manifest=str(manifest))))
