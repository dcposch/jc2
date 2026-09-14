import sys
sys.dont_write_bytecode=True
from pathlib import Path
import urllib.request,hashlib,json,datetime
B=Path(__file__).resolve().parent
url='https://arxiv.org/pdf/math/0608157v2'
with urllib.request.urlopen(url,timeout=20) as f:data=f.read(2000000)
if not data.startswith(b'%PDF') or len(data)>=2000000:raise RuntimeError('PDF response')
with (B/'arzhantsev-petravchuk-v2.pdf').open('xb') as f:f.write(data)
r={'url':url,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'read_scope':'Web PDF: Section2 Proposition1 and Lemmas1-2 pp3; Lemmas4-5 p5 including their proof text. Lemma4 cites external sources; those proofs not reread. Not whole13-page proof. Old theorem, targeted primary check; not a new broad sweep.'}
with (B/'primary-receipt.json').open('xb') as f:f.write((json.dumps(r,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(r))
