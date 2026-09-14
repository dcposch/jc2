#!/usr/bin/env python3
"""Independent exact-rational replay; inputs limited to frozen roster and report formulas.
Raw flat values are conditional on immediate termination of unselected major siblings.
"""
from fractions import Fraction as F
from math import gcd,lcm
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
INPUT=Path('/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl')

@lru_cache(None)
def partitions(N, minimum=1):
    if N==0: return ((),)
    out=[]
    for j in range(minimum,N+1):
        for tail in partitions(N-j,j): out.append((j,)+tail)
    return tuple(out)

def patterns(src,i,L=None):
    n,m,s=src['n'],src['m'],src['s']
    d=src['d'];V=src['V'];M=src['M'];delta=list(map(F,src['delta']))
    P=F(V[i-1]*d[i-1],d[i]);Q=P*F(n-M[i-1],d[i-1]);lo=F(d[i-1],n-M[i-1]);select=V[i-2]
    assert P.denominator==Q.denominator==1
    P,Q=int(P),int(Q)
    if L is None:L=lcm(*(x.denominator for x in delta[i:]))
    A=(L*delta[i-1]).denominator
    ans=[]
    for z in range(P%A,P+1,A):
        if z and z==lo:continue
        for parts in partitions((P-z)//A):
            if A*len(parts)+(z>0)>Q or lo in parts:continue
            # Record zero vs nonzero choice separately; equal nonzero factors are symmetric.
            for chosen in ('zero','nonzero'):
                if (chosen=='zero' and z!=select) or (chosen=='nonzero' and select not in parts):continue
                ans.append(dict(i=i,P=P,Q=Q,lo=lo,L=L,A=A,z=z,parts=parts,selected=chosen,V=select))
    return ans

def jsonable(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:jsonable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [jsonable(v) for v in x]
    return x

def read_rows():return [json.loads(l) for l in INPUT.open()]

def configs(src,i=None,L=1,picked=()):
    if i is None:i=src['s']-1
    if i<2:
        yield tuple(reversed(picked))
        return
    for p in patterns(src,i,L):
        nextL=L if p['selected']=='zero' else lcm(L,F(src['delta'][i-1]).denominator)
        yield from configs(src,i-1,nextL,picked+(p,))

def census_configs(src):
    sets=[[p for p in patterns(src,i) if not(p['A']==1 and p['z']>0)] for i in range(2,src['s'])]
    return product(*sets)

def flat_eval(src,ps,mode='sameV'):
    n,m,s=src['n'],src['m'],src['s'];d=src['d'];V=src['V'];M=src['M'];delta=list(map(F,src['delta']))
    by_i={p['i']:p for p in ps}
    def evaluate(i,mult=1):
        if i==1:
            rho=F(m*V[0],d[1]);assert rho.denominator==1
            return F(n,n+m)*rho*(1-delta[0]),F(0),[],[]
        p=by_i[i]; IM=F(0);Im=F(0);maj=[];minors=[]
        groups=([(p['z'],1,'zero')] if p['z'] else [])+[(r,p['A'],'nonzero') for r in p['parts']]
        consumed=False
        for r,num,kind in groups:
            rho=F(m*r,d[i-1]);assert rho.denominator==1
            lamabs=F(m)*(1-delta[i-1])/F(n-M[i-1]);kappa=rho*(1-delta[i-1])-lamabs
            is_selected=(r==p['V'] and kind==p['selected'] and not consumed)
            if is_selected:consumed=True
            follow=(r==p['V']) if mode=='sameV' else is_selected
            if follow:
                subIM,subIm,submaj,submin=evaluate(i-1,mult*num)
                IM+=num*subIM;Im+=num*subIm;maj.extend(submaj);minors.extend(submin)
            elif kappa>0:
                J=F(n)*rho*kappa/((n+m)*rho-m)
                IM+=num*J
                maj.append(dict(level=i,multiplicity=r,count=num*mult,rho=int(rho),kappa=kappa,W0=n-M[i-1],L=lcm(p['L'],delta[i-1].denominator) if kind=='nonzero' else p['L'],kind=kind,d=d[i-1],sameV=r==p['V'],J=J))
            else:
                assert kappa<0
                term=-kappa/rho
                Im+=num*term
                minors.append(dict(level=i,multiplicity=r,count=num*mult,rho=int(rho),delta=1+term,Im=term))
        assert consumed
        return IM,Im,maj,minors
    IM,Im,maj,minors=evaluate(s-1)
    # Class label counts any sibling distinct from chosen Galois orbit, including sameV copies.
    major_other=False;major_same=False
    for p in ps:
        consumed=False
        for r,num,kind in ([(p['z'],1,'zero')] if p['z'] else [])+[(r,p['A'],'nonzero') for r in p['parts']]:
            selected=r==p['V'] and kind==p['selected'] and not consumed
            if selected:consumed=True
            elif r>p['lo']:
                if r==p['V']:major_same=True
                else:major_other=True
    typ='T3' if major_other else ('T2' if major_same else 'T1')
    return dict(IM_flat=IM,Im_unsplit=Im+F(V[-1],src['u_s']),type=typ,major_siblings=maj,minor_packets=minors)

def run():
    from collections import Counter
    result={'schema':'independent-flat-census-replay/v1','source':str(INPUT),'semantics':'IM_flat assumes immediate termination of off-tower major siblings. Im_unsplit assumes no earlier splitting of minor packets. Neither a T3 completion nor a polynomial-pair witness is asserted.','encoding':{'patterns':'list of [level,zero_multiplicity,orbit_multiplicities,selection_kind]','flags':'[nonintegral_IM,IM_below_Im,integrality_only]'},'totals':Counter(),'by_type':{},'rows':[]}
    targets={f'R{i:03}' for i in [1,9,25,26,27,28,50,57,58]}
    detail=[]
    for row in read_rows():
        rec={'row_id':row['row_id'],'source':row['source'],'totals':Counter(),'configs':[]}
        for j,ps in enumerate(census_configs(row['source'])):
            e=flat_eval(row['source'],ps,'selected');IM,Im=e['IM_flat'],e['Im_unsplit']
            flags=[IM.denominator!=1,IM<Im,IM.denominator!=1 and IM>=Im]
            broad=[('configurations',True),('nonintegral',flags[0]),('below',flags[1]),('integrality_only',flags[2]),('surviving_flat',not flags[0] and not flags[1]),('upper_level_sibling',any(x['level']>=3 for x in e['major_siblings']))]
            typ=e['type'];result['by_type'].setdefault(typ,Counter())
            for k,v in broad:
                if v:
                    result['totals'][k]+=1;rec['totals'][k]+=1;result['by_type'][typ][k]+=1
            c={'index':j,'patterns':[[p['i'],p['z'],p['parts'],p['selected']] for p in ps],'IM_flat':IM,'Im_unsplit':Im,'type':typ,'flags':flags}
            rec['configs'].append(c)
            if row['row_id'] in targets:
                detail.append(dict(row_id=row['row_id'],index=j,patterns=ps,**e))
        result['rows'].append(rec)
    (BASE/'census_replay.json').write_text(json.dumps(jsonable(result),separators=(',',':'))+'\n')
    (BASE/'census_targets.json').write_text(json.dumps(jsonable(detail),separators=(',',':'))+'\n')
    print(json.dumps(jsonable({'totals':result['totals'],'by_type':result['by_type']}),indent=2))
    for r in result['rows']:
        print(r['row_id'],dict(r['totals']))

if __name__=='__main__':run()
