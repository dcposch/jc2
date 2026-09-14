import sys, json, itertools
from fractions import Fraction as Q
from math import gcd
sys.path.insert(0,'/home/ubuntu/jc2/box/t3-residue-20260906')
from exact_contact import tower, all_flat
from t3_closure import Closure, lcmn, ROSTER
rows={json.loads(l)['row_id']: json.loads(l) for l in open(ROSTER)}
S={}
for rid in sys.argv[1:]:
    T=tower(rows[rid]['source']); n,m,s=T['n'],T['m'],T['s']
    ncfg=0; nsurv=0; best=None; dmax=0; dbound=0; tow=0; sibinv=set()
    for c in all_flat(T):
        ncfg+=1
        dtrue={}
        for i,(z,orb,ix) in c['pattern'].items():
            gg=0
            for r in ([z] if z>0 else [])+list(orb): gg=gcd(gg,r)
            dtrue[i]=T['d'][i]//gg
        dtrue[s]=T['d'][s]//gcd(T['d'][s]-T['V'][s],T['V'][s])
        sib=[l for l in c['leaves'] if l['kind']=='major-sibling']
        base_IM=c['IM']-sum(l['IM_each']*l['copies'] for l in sib)
        pools=[]; ok=True
        for l in sib:
            i=l['level']; rho=int(l['rho']); u=m//dtrue[i]
            W0=n-T['M'][i]; L=lcmn([T['delta'][j].denominator for j in range(i,s+1)])
            C=Closure(n,m,u,dtrue[i],True,True,True,False,None)
            R=C.run(rho,l['kappa'],W0,L)
            dmax=max(dmax,C.depth_reached); dbound=max(dbound,rho//u-1); tow+=C.enum
            sibinv.add((i,l['mult'],rho,u,rho//u,rho//u-1))
            if not R: ok=False; break
            pools.append([(a,b,l['copies']) for a,(b,w) in R.items()])
        if not ok: continue
        found=False
        for combo in itertools.product(*pools) if pools else [()]:
            IM=base_IM+sum(a*k for a,b,k in combo); Im=c['Im']+sum(b*k for a,b,k in combo)
            if IM.denominator==1 and IM>=Im:
                found=True
                if best is None or (IM-Im,IM)<best[:2]: best=(IM-Im,IM,Im)
        nsurv+=found
    S[rid]=dict(n=n,m=m,s=s,configs=ncfg,surviving_configs=nsurv,
                min_margin=str(best[0]) if best else None,
                IM=str(best[1]) if best else None, Im=str(best[2]) if best else None,
                depth_searched=dmax, depth_bound=dbound, towers_enumerated=tow,
                sibling_inventory=sorted(sibinv))
    b=S[rid]
    print(f"{rid} ({n},{m}) cfgs={ncfg} surviving={nsurv} min_margin={b['min_margin']} "
          f"I_M={b['IM']} I_m={b['Im']} depth_searched={dmax} depth_bound={dbound} towers={tow}")
    print(f"     sibling roots (level,mult,rho_f,unit,r,depth_bound): {sorted(sibinv)}")
json.dump(S,open('/home/ubuntu/jc2/box/t3-residue-20260906/t3_summary.json','w'),indent=1)
