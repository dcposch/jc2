#!/usr/bin/env python3
"""Independent all-row term-pair audit; no dense exponent vectors or solver."""
import hashlib
import json
from pathlib import Path
import re
import socket
import time

root=Path('/home/ubuntu/full-j-solver-pilot-20260906')
source=Path('/home/ubuntu/factored-jacobian-pilot-20260906/complete_export.generators.jsonl')
if socket.gethostname()!='ip-172-30-0-56' or Path.cwd()!=root:raise SystemExit('wrong worker/root')
p=1073741827
inverse={1:1}
def term(token):
    sign=-1 if token.startswith('-') else 1
    token=token.lstrip('+-')
    first,sep,rest=token.partition('*')
    if first[0].isdigit():
        n,slash,d=first.partition('/')
        num,den=int(n),int(d) if slash else 1
        if den not in inverse:inverse[den]=pow(den,-1,p)
        return sign*num*inverse[den]%p,rest
    return sign%p,token
started=time.monotonic(); rows=total=0; stream=hashlib.sha256()
with source.open() as sf,(root/'complete.p1073741827.ms').open() as mf,(root/'modular.rows.tsv').open('x') as table:
    header=json.loads(next(sf))
    if next(mf).strip().split(',')!=header['variables'] or int(next(mf))!=p:raise SystemExit('header/order changed')
    for raw in sf:
        row=json.loads(raw)
        if row['type']=='complete':
            if mf.read().strip():raise SystemExit('trailing modular rows')
            footer=row;break
        line=next(mf).strip()
        if rows:
            if not line.startswith(','):raise SystemExit('missing row delimiter')
            line=line[1:]
        src=''.join(row['polynomial'].split())
        a=re.findall(r'[+-]?[^+-]+',src)
        b=re.findall(r'[+-]?[^+-]+',line)
        if len(a)!=len(b) or len(a)!=row['terms']:raise SystemExit('term count changed')
        for aa,bb in zip(a,b):
            qa,ma=term(aa);qb,mb=term(bb)
            if qa==0 or qa!=qb or ma!=mb or '/' in bb:raise SystemExit('coefficient or monomial mismatch')
        table.write(str(rows)+'\t'+row['label']+'\t'+str(len(a))+'\t'+hashlib.sha256(line.encode()).hexdigest()+'\n')
        rows+=1;total+=len(a);stream.update(raw.encode())
    if (rows,total)!=(1629,11299180) or stream.hexdigest()!=footer['generator_stream_sha256']:raise SystemExit('incomplete full stream')
result={'status':'ALL_ROWS_COEFFICIENT_AND_MONOMIAL_IDENTITY_PASS','rows':rows,'terms':total,'variables':600,
        'prime':p,'denominators':sorted(inverse),'source_generator_stream_sha256':stream.hexdigest(),
        'elapsed_seconds':time.monotonic()-started,'native_micro_control':'smoke.json','no_rows_or_terms_removed':True}
(root/'modular.audit.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True),flush=True)
