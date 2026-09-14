#!/usr/bin/env python3
"""Enumerate standard monomials of the saved exact bases, integer arithmetic."""
from pathlib import Path
from collections import Counter,deque
import re,json
p=Path(__file__).resolve().parent
ans={}
for tag,t in [('t2p',2),('t3',3),('t4',4)]:
    vs=['b4']+[f'u{i}' for i in range(2,t)]+['b3']
    wt=list(range(1,t))+[t+1]
    s=(p/f'{tag}_plus_basis.txt').read_text()
    s=re.sub(r'\([^()]*\)','c',s)
    lms=[]
    for f in s.strip().split(','):
        term=re.split(r'[+-]',f.strip().lstrip('-+'))[0]
        lm=[]
        for v in vs:
            m=re.search(r'\b'+v+r'\b(?:\^(\d+))?',term)
            lm.append(int(m.group(1) or 1) if m else 0)
        assert any(lm),(tag,f[:100],term)
        lms.append(tuple(lm))
    minimal=[m for m in lms if not any(n!=m and all(a<=b for a,b in zip(n,m)) for n in lms)]
    for i in range(t): assert any(m[i]>0 and sum(m)==m[i] for m in minimal)
    start=(0,)*t; seen={start}; queue=deque([start])
    while queue:
        m=queue.popleft()
        for i in range(t):
            n=list(m);n[i]+=1;n=tuple(n)
            if n in seen or any(all(a<=b for a,b in zip(lm,n)) for lm in minimal): continue
            seen.add(n);queue.append(n)
    hist=Counter(sum(a*b for a,b in zip(m,wt)) for m in seen)
    ans[tag]={'variables':vs,'weights':wt,'basis_size':len(lms),'minimal_leaders':minimal,'length':len(seen),'top_degree':max(hist),'hilbert':dict(sorted(hist.items()))}
    print(tag,'length',len(seen),'top_degree',max(hist),'top_value',hist[max(hist)],flush=True)
(p/'exact_hilbert.json').write_text(json.dumps(ans,indent=2)+'\n')
print('HILBERT_COMPLETE',flush=True)
