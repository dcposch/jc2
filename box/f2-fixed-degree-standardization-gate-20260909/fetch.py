import sys
sys.dont_write_bytecode=True
import json,hashlib,urllib.request,datetime,subprocess,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
B=Path(__file__).resolve().parent;R=Path('/home/ubuntu/jc2')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for src,name,url in [
 ('box/source-multiplicity-admissibility-20260909/ggv-v3.pdf','ggv-1401.1784v3.pdf','https://arxiv.org/pdf/1401.1784v3'),
 ('box/source-multiplicity-admissibility-20260909/ggv-v3.txt','ggv-1401.1784v3.txt','https://arxiv.org/pdf/1401.1784v3'),
 ('box/d108-published-case-interface-20260906/ggvh-algorithms-1708.07936v1.pdf','gghv-1708.07936v1.pdf','https://arxiv.org/pdf/1708.07936v1'),
 ('box/d108-published-case-interface-20260906/ggvh-algorithms-1708.07936v1.txt','gghv-1708.07936v1.txt','https://arxiv.org/pdf/1708.07936v1')]:
 p=R/src;q=B/name
 with q.open('xb') as f:f.write(p.read_bytes())
 if sha(q)!=sha(p):raise RuntimeError('copy drift')
 rows.append({'source':src,'url':url,'path':name,'sha256':sha(q),'bytes':q.stat().st_size})
url='https://serdica.math.bas.bg/index.php/serdica/article/download/300/153/862'
try:
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=15) as r:data=r.read(3000000);status=r.status
 if not data.startswith(b'%PDF'):raise RuntimeError('not PDF')
 p=B/'makar-limanov-serdica-2025.pdf'
 with p.open('xb') as f:f.write(data)
 z=subprocess.run(['pdftotext','-layout',str(p),str(B/'makar-limanov-serdica-2025.txt')],capture_output=True,timeout=10,check=True)
 rows.append({'url':url,'status':status,'path':p.name,'sha256':sha(p),'bytes':len(data),'text_sha256':sha(B/'makar-limanov-serdica-2025.txt')})
except Exception as e:rows.append({'url':url,'error':str(e)})
with (B/'source-pins.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':rows},f,indent=2)
print(json.dumps(rows,indent=2))
