#!/usr/bin/env python3
"""Independent exact-Q controls. Inputs: frozen roster, Xu's printed cases.

No producer code imported. rho always counts smaller-polynomial f roots.
All contact equalities below are for the displayed unsplit branches.
"""
from fractions import Fraction as F
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
INPUT = Path('/tmp/jc2-lane.QKyQBy/inputs')

def major(n, m, rho, a, delta0):
    kappa = rho*(1-delta0)-a
    delta = 1-F(n+m)*kappa/((n+m)*rho-m)
    lg = F(n,n+m)*(delta-1)
    J = -rho*lg
    lf = -a+rho*(delta-delta0)
    assert delta == 1+lf+F(n,m)*lf
    assert J == F(n*rho)*kappa/((n+m)*rho-m)
    assert J == F(m,n+m)*F(n*rho,m)*(1-delta)
    return {'rho_f':rho, 'rho_g':F(n*rho,m), 'kappa':kappa,
            'delta':delta, 'lambda_f':lf, 'lambda_g':lg, 'I_M':J}

def minor(rho, a, delta0):
    delta = delta0 + a/rho
    assert delta > 1
    return {'rho_f':rho, 'delta':delta, 'I_m_term':delta-1}

def calc(row, z, rs):
    s=row['source']; n=s['n']; m=s['m']
    d=s['d'][1]; delta0=F(s['delta'][1]); a=F(m)*(1-delta0)/(n-s['M'][1])
    A=delta0.denominator
    leaves=[]; im=F(s['v_s'],s['u_s']); IM=F(0)
    for r,count in ([(z,1)] if z else [])+[(r,A) for r in rs]:
        rho=F(m*r,d); assert rho.denominator==1
        kappa=rho*(1-delta0)-a
        if kappa>0:
            leaf=major(n,m,int(rho),a,delta0); IM+=count*leaf['I_M']
        else:
            leaf=minor(int(rho),a,delta0); im+=count*leaf['I_m_term']
        leaf.update({'multiplicity':r,'orbit_count':count}); leaves.append(leaf)
    return {'row':row['row_id'],'pattern':{'z':z,'orbits':rs},
            'n':n,'m':m,'delta0':delta0,'abs_lambda_f0':a,
            'leaves':leaves,'I_M':IM,'I_m_unsplit':im,'margin':IM-im}

def main():
    rows={r['row_id']:r for r in map(json.loads,(INPUT/'roster.jsonl').read_text().splitlines())}
    specs=[('Xu6.1i','R002',0,[2,2],8,4),('Xu6.1ii','R002',0,[2,1,1],4,6),
           ('Xu6.2i','R001',0,[2,1],4,5),('Xu6.2ii','R007',1,[5],10,4),
           ('R009_alpha','R009',0,[2,1],8,8),('R009_beta','R009',16,[2],F(1592,79),3),
           ('R050_alpha','R050',1,[4,1],8,8),('R050_beta','R050',5,[4],F(123,11),3)]
    out={}
    for name,rid,z,rs,IM,im in specs:
        a=calc(rows[rid],z,rs)
        assert a['I_M']==IM,(name,a)
        assert a['I_m_unsplit']==im,(name,a)
        out[name]=a
    # Trace/valuation convention: a full orbit can be integral when its per-disc term is not.
    assert out['R009_alpha']['leaves'][0]['I_M']==F(1,2)
    out['metadata']={'normalization':'I=-ord_t resultant; x=t^-1; no cover division',
                     'orientation':'deg_y f=m, deg_y g=n; f is smaller roster member',
                     'all_assertions_passed':True}
    out['metadata']['derivative_controls']={}
    for name in ('R009_alpha','R050_alpha'):
        v=out[name]; src=rows[v['row']]['source']; m=src['m']
        e=sum(l['orbit_count'] for l in v['leaves'])
        ider=F(m)+(e-1)*v['abs_lambda_f0']
        for leaf in v['leaves']:
            if 'lambda_f' in leaf:
                ider-=leaf['orbit_count']*(leaf['rho_f']-1)*leaf['lambda_f']
        rp=F(m*src['u_s'],src['d'][-2]);dp=F(src['v_s'],src['u_s'])
        bound=F(m-1)+(rp-1)*(dp-1)
        norm=F(m)+rp*(dp-1)-ider
        for leaf in v['leaves']:
            if 'I_m_term' in leaf:
                bound+=leaf['orbit_count']*(leaf['rho_f']-1)*leaf['I_m_term']
                norm+=leaf['orbit_count']*leaf['rho_f']*leaf['I_m_term']
        assert ider==bound and norm==v['I_M']
        out['metadata']['derivative_controls'][name]={'I_f_fy':ider,'Xu4_7_bound':bound,'norm_reconstruction':norm}
    (OUT/'controls.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
    print(json.dumps({k:(str(v['I_M']),str(v['I_m_unsplit'])) for k,v in out.items() if k!='metadata'}))

if __name__=='__main__': main()
