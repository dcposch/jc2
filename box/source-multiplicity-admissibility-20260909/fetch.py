import sys
sys.dont_write_bytecode=True
import urllib.request,json,hashlib,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
P=Path(__file__).resolve().parent
name,url=sys.argv[1:]
entry={'name':name,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as r:b=r.read(8000000);entry.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
 with (P/name).open('xb') as f:f.write(b)
 entry.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
except Exception as e:entry.update(error=str(e))
with (P/(name+'.fetch.json')).open('x') as f:json.dump(entry,f,indent=2)
print(json.dumps(entry))
