import json, ast, sys
from fractions import Fraction as F
from math import gcd
sys.path.insert(0,'.')
IN='/tmp/jc2-lane.4VL5oJ/inputs/'
d52=json.load(open(IN+'full-tree-ode-excess-witnesses.json'))
d14=json.load(open(IN+'full-tree-polynomial-ode-excess-witnesses.json'))
def chain(w):
    out=[]
    while isinstance(w,dict) and 'j' in w:
        out.append((w['j'], w['delta'], w.get('selected_mode')))
        w=w.get('selected_child')
    return out,w
n_z0=0; killed=0; mismatch=[]; integral_other=[]
for k,w in d52.items():
    ch,bot=chain(w)
    z0=any(dl=='0' and md=='nonzero' for (_,dl,md) in ch)
    kil = k not in d14
    if z0: n_z0+=1
    if kil: killed+=1
    if z0!=kil: mismatch.append((k,z0,kil,ch))
    for (j,dl,md) in ch:
        fr=F(dl)
        if fr.denominator==1 and fr!=0: integral_other.append((k,j,dl,md))
print('rows(52-excess ODE)=',len(d52),' POLY+ODE excess=',len(d14))
print('delta0-nonzero-edge rows =',n_z0)
print('POLY-killed rows        =',killed)
print('mismatch                =',len(mismatch))
print('integral non-zero radii on selected chains =',len(integral_other), integral_other[:5])
# radii inventory on the 52 selected chains
from collections import Counter
c=Counter()
for k,w in d52.items():
    ch,_=chain(w)
    for (j,dl,md) in ch:
        if j>=3: c[dl]+=1
print('intermediate (j>=3) radii multiset:',dict(sorted(c.items(), key=lambda kv:-kv[1])))
# the 14 survivors: any integral radius anywhere?
bad=[]
for k,w in d14.items():
    ch,_=chain(w)
    for (j,dl,md) in ch:
        if F(dl).denominator==1: bad.append((k,j,dl,md))
print('integral radii on the 14 POLY+ODE chains:',bad)
