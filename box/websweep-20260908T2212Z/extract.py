import sys
sys.dont_write_bytecode=True
import zipfile,json,xml.etree.ElementTree as ET,re,hashlib,resource
from pathlib import Path
from html.parser import HTMLParser
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
P=Path(__file__).resolve().parent;S=P/'sources'
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t in ('p','div','li','h1','h2','h3','br','tr'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.parts.append(s)
for name in ('tao-primary.html','gao-primary.html','shaska-primary.html','arxiv-ag.html','arxiv-ac.html','arxiv-cv.html','x-octonion.html','retry-x-search.html'):
 f=S/name
 if f.exists() and f.stat().st_size:
  p=Plain();p.feed(f.read_text(errors='replace'));text='\n'.join(x.strip() for x in ''.join(p.parts).splitlines() if x.strip())
  with (P/(name+'.txt')).open('xb') as o:o.write(text.encode())
z=zipfile.ZipFile(S/'duan-package.zip');print('ZIP',[(x.filename,x.file_size) for x in z.infolist()]); owned=[]
for i in z.infolist():
 if i.file_size>3*1024*1024:continue
 if i.filename.endswith('_EN.docx') or i.filename.endswith('plane_jacobian_mesh80_spec.json') or i.filename.endswith('verify_package.py'):
  b=z.read(i.filename);dest=P/('duan-'+Path(i.filename).name)
  with dest.open('xb') as f:f.write(b)
  owned.append({'member':i.filename,'file':dest.name,'sha256':hashlib.sha256(b).hexdigest()})
  if i.filename.endswith('.docx'):
   zz=zipfile.ZipFile(dest);t=ET.fromstring(zz.read('word/document.xml'));text='\n'.join(''.join(p.itertext()) for p in t.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
   with (P/'duan-English.txt').open('xb') as f:f.write(text.encode())
with (P/'extracted-pins.json').open('xb') as f:f.write(json.dumps(owned,indent=2).encode())
