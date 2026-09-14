import json,pathlib,collections,hashlib
root=pathlib.Path('box/graded-moh-20260905')
out=[]
for f in sorted((root/'instrument').glob('*/custody.json')):
 d=json.loads(f.read_text()); vv=d['source_ring']['variables']; groups=collections.defaultdict(set)
 for v in vv:
  if v=='c':continue
  z,b,a=v.rsplit('_',2);groups[z].add((int(b),int(a)))
 missing=[]
 for block,S in groups.items():
  for b,a in S:
   for aa in range(a):
    if (b,aa) not in S and not (b==aa==0 and block in ('A3','A4','B2','B3')):
     missing.append((block,b,a,aa))
 out.append(dict(stem=f.parent.name,source_custody_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),closed_for_constant_y_translation=not missing,missing_directions=missing))
(root/'resume-r2/translation-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for a in out: print(a['stem'],a['closed_for_constant_y_translation'],'missing',len(a['missing_directions']))
