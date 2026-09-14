import json,collections
from math import gcd
rows=json.load(open('/home/ubuntu/jc2/box/split-window-gate-20260905/crosswalk-310.json'))
def ds(n,M):
    d=[n]
    for j in range(len(M)): d.append(gcd(d[-1],abs(M[j])))
    return d                      # d[0]=d_1, d[j]=d_{j+1}
out=collections.Counter(); rowsout=[]
for r in rows:
    n=r['n']; M=r['M']; V={int(k):v for k,v in r['V'].items()}; s=r['s']; us=r['u_s']
    d=ds(n,M); d_s=d[s-1]; d_sm1=d[s-2]
    assert d_s==r['d_s'] if 'd_s' in r else True
    sp_=s-1
    Vsp=V[sp_] if sp_ in V else None
    if Vsp is None: out['no V_{s-1} (s\'=1)']+=1; continue
    dxsp=d_sm1*us//d_s if (d_sm1*us)%d_s==0 else None
    if dxsp is None: out['non-integral d\'']+=1; continue
    kills = Vsp>dxsp
    out['CTOP kills' if kills else 'CTOP holds']+=1
    rowsout.append(dict(n=n,m=r['m'],M=M,s=s,u_s=us,V_sprime=Vsp,d_sprime=dxsp,ctop_kill=kills,
                        forced=(r.get('n_surv',0)==0)))
print('counterfactual (C-TOP) on the 310 operative u_s>=2 rows:',dict(out))
forced=[x for x in rowsout if x['forced']]
print('of the 233 descent-forced:',collections.Counter(x['ctop_kill'] for x in forced))
json.dump(rowsout,open('/home/ubuntu/jc2/box/child-top-us2-20260905/ctop310.json','w'),indent=0)
