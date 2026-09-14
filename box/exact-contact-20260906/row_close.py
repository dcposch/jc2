import sys, json, itertools
from fractions import Fraction as Q
from math import gcd
sys.path.insert(0,'box/exact-contact-20260906')
from exact_contact import tower
import sibling_tower3 as S
rows={json.loads(l)['row_id']: json.loads(l) for l in open('/tmp/jc2-lane.69C0ak/inputs/roster.jsonl')}
from exact_contact import all_flat
def lcmn(v):
    a=1
    for x in v: a=a*x//gcd(a,x)
    return a
depth=int(sys.argv[1])
for rid in sys.argv[2:]:
    T=tower(rows[rid]['source']); n,m,s=T['n'],T['m'],T['s']
    print(f"=== {rid} ({n},{m}) s={s}")
    any_surv=False
    for c in all_flat(T):
        # d_true at level i = d_i / gcd(multiplicities of p_i) : the pattern may
        # itself be a perfect power, in which case Def 5.1's d_i is not maximal
        dtrue={}
        for i,(z,orb,ix) in c['pattern'].items():
            g=0
            for r in ([z] if z>0 else [])+list(orb): g=gcd(g,r)
            dtrue[i]=T['d'][i]//g
        dtrue[T['s']]=T['d'][T['s']]//gcd(T['d'][T['s']]-T['V'][T['s']],T['V'][T['s']])
        sib=[l for l in c['leaves'] if l['kind']=='major-sibling']
        base_IM=c['IM']-sum(l['IM_each']*l['copies'] for l in sib)
        base_Im=c['Im']
        pools=[]
        ok=True
        for l in sib:
            i=l['level']; rho=int(l['rho']); kap=l['kappa']
            W0=n-T['M'][i]; L=lcmn([T['delta'][j].denominator for j in range(i,s+1)])
            R=S.search(n,m,rho,kap,W0,L,dtrue[i],depth,4)
            if not R: ok=False; break
            pools.append([((a,b), l['copies']) for (a,b) in R])
        if not ok:
            print(f"   pattern {c.get('pattern')}: DEAD (a major sibling has NO admissible completion)")
            continue
        best=[]
        for combo in itertools.product(*pools) if pools else [()]:
            IM=base_IM+sum(a*k for (a,b),k in combo)
            Im=base_Im+sum(b*k for (a,b),k in combo)
            if IM.denominator==1 and IM>=Im: best.append((IM,Im))
        if best:
            any_surv=True
            print(f"   pattern {c.get('pattern')}: {len(set(best))} survivors e.g. {sorted(set(best))[:3]}")
        else:
            print(f"   pattern {c.get('pattern')}: DEAD (no completion with I_M in Z and I_M>=I_m)")
    print(f"   ROW VERDICT: {'ALIVE' if any_surv else 'DEAD (all patterns, depth<=%d)'%depth}")
    sys.stdout.flush()
