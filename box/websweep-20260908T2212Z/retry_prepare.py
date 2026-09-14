import sys
sys.dont_write_bytecode=True
import json
from pathlib import Path
P=Path(__file__).resolve().parent
rows=[]
for n in (1,2,3,4):
    receipts=P/f'batch{n}-receipts.json'
    if receipts.exists():
        bad={r['file'].split('/')[-1] for r in json.loads(receipts.read_bytes()) if r['error'] or r['status']!=200}
        rows += [('retry-'+a,b) for a,b in json.loads((P/f'batch{n}.json').read_bytes()) if a in bad]
    else: rows += [('retry-'+a,b) for a,b in json.loads((P/f'batch{n}.json').read_bytes())]
for i in range(0,len(rows),12):
    with (P/f'retry{i//12+1}.json').open('xb') as f:f.write(json.dumps(rows[i:i+12],indent=2).encode())
print({'retry_count':len(rows)})
