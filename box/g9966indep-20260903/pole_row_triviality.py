import sys; sys.path.insert(0,'box/g9966indep-20260903')
import indep_engine as E
from ring import *
for BR in ('delta2','delta52'):
    br=E.Branch(BR); K3f=E.build_K3(12)
    el=E.Elim(forbidden={br.leadvar})
    for lab,p in E.leader_rows(br,K3f): el.feed(lab,p)
    if BR=='delta52': el.feed('x',var('Hc_11_0'))
    K3=E.series_subst(E.build_K3(E.NT), el.sub)
    K2,_,_,_=E.build_K2(K3); B1,_=E.build_B1(E.NT)
    KF,KG=E.build_KFKG(K2,B1)
    base=4 if BR=='delta2' else 8
    print('---',BR,'raw (unreduced) pole rows')
    for st in range(0,9 if BR=='delta52' else 5):
        m=base+st; out=[]
        for nm,S in (('F',KF),('G',KG)):
            d=E.split_z(br.sub_series(S,m).get(m,{}),br.zvar)
            for e,c in sorted(d.items()):
                if c: out.append('%s_%s^%d[%d terms]'%(nm,br.zvar,e,len(c)))
        print('  stage%d local power %d : %s'%(st,m, out if out else 'ALL IDENTICALLY ZERO'))
