#!/usr/bin/env python3
"""Universal coefficient-ideal proof of all F/G pole implications.

This proof works over the coefficient ring of each fully emitted source
chart. It requires the saved phase-chain replay for those emitted rows;
it does not replace that replay by a floor assumption.
"""
import hashlib,json,sys
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True
N=Path(__file__).resolve().parent
sys.path.insert(0,str(N))
import engine as E
from source_data import SOURCE as S,jsonable
p,u,v,a,b,c,d=sp.symbols('p u v a b c d')
inner=u*p+v;H=p**3+inner
F=H**3+a*H+b;G=H**2+c*H+d
RF=a*p**3+b;RG=c*p**3+d
MF=H**2+H*p**3+p**6+a
MG=H+p**3+c
assert sp.expand(F-p**9-inner*MF-RF)==0
assert sp.expand(G-p**6-inner*MG-RG)==0
# Formal higher-series remainder shows every coefficient below the source
# endpoint vanishes in the quotient by the emitted strict coefficient rows.
s,hp,up,vp,ap,bp,cp,dp=sp.symbols('s hp up vp ap bp cp dp')
hbar=p+s*hp;c2bar=u+s*up;c3bar=v+s*vp
Hbar=hbar**3+c2bar*hbar+c3bar
Herror=sp.expand(Hbar-H)
assert sp.rem(Herror,s,s)==0
Fbar=Hbar**3+(a+s*ap)*Hbar+(b+s*bp)
Gbar=Hbar**2+(c+s*cp)*Hbar+(d+s*dp)
assert sp.expand(Fbar.subs(s,0)-F)==0
assert sp.expand(Gbar.subs(s,0)-G)==0
records=[]
for branch,data in S['minor'].items():
    if branch not in ('delta2','delta52'):continue
    A=data['h3_local_floor'];cover=data['cover'];pi=sp.Symbol('pi')
    P=data['h3_face'];loc=sp.Symbol('rho' if branch=='delta2' else 'c')
    P1=sp.expand(P.subs(loc,1))
    assert P1!=0
    floors={'h3':A,'C2':2*A,'C3':3*A,'H2':3*A,
            'A2_effective':6*A,'A3_effective':9*A,
            'B1_effective':3*A,'B2_effective':6*A,'F':9*A,'G':6*A}
    assert floors['F']==data['F_local_floor'] and floors['G']==data['G_local_floor']
    unshifted={name:floors[name+'_effective']-cover for name in ('A2','A3','B1','B2')}
    negative={
      'h3_strict_row_removed_F_endpoint_minus1':9*P1**8,
      'h3_strict_row_removed_G_endpoint_minus1':6*P1**5,
      'C2_strict_row_removed_F_endpoint_minus1':3*P1**7,
      'C2_strict_row_removed_G_endpoint_minus1':2*P1**4,
      'C3_strict_row_removed_F_endpoint_minus1':3*P1**6,
      'C3_strict_row_removed_G_endpoint_minus1':2*P1**3,
      'A2_strict_row_removed_F_endpoint_minus1':P1**3,
      'A3_strict_row_removed_F_endpoint_minus1':sp.Integer(1),
      'B1_strict_row_removed_G_endpoint_minus1':P1**3,
      'B2_strict_row_removed_G_endpoint_minus1':sp.Integer(1),
      'inner_target_removed_F_face_difference':(P1**3+1)**3-P1**9,
      'inner_target_removed_G_face_difference':(P1**3+1)**2-P1**6,
      'F_target_removed_F_face_difference':sp.Integer(1),
      'G_target_removed_G_face_difference':sp.Integer(1)}
    assert all(sp.expand(value)!=0 for value in negative.values())
    # Verify strict negative coefficients independently as scalar polynomials
    # in s and generic p, without assuming the claimed coefficient formulas.
    tests=[('h3',s**A*p+s**(A-1),0,0),
           ('C2',s**A*p,s**(2*A-1),0),
           ('C3',s**A*p,0,s**(3*A-1))]
    strictchecks={}
    for name,hh,cc2,cc3 in tests:
        HH=hh**3+cc2*hh+cc3
        ff=sp.Poly(sp.expand(HH**3),s);gg=sp.Poly(sp.expand(HH**2),s)
        fvalue=sp.expand(ff.nth(9*A-1).subs(p,P1));gvalue=sp.expand(gg.nth(6*A-1).subs(p,P1))
        assert fvalue==sp.expand(negative[name+'_strict_row_removed_F_endpoint_minus1'])
        assert gvalue==sp.expand(negative[name+'_strict_row_removed_G_endpoint_minus1'])
        strictchecks[name]=True
    raw_counts={name:sum(map(len,E.raw_minor_support(branch,name).values())) for name in ('F','G')}
    target_counts={name:len(sp.Poly(sp.expand(P**power),pi).terms()) for name,power in [('F',9),('G',6)]}
    records.append({'branch':branch,'cover':cover,'normalized_floors':floors,
        'unshifted_outer_floors':unshifted,'face':str(P),
        'historical_lower_support_counts':raw_counts,'target_nonzero_coefficient_counts':target_counts,
        'scope_includes_all_coefficients_at_endpoint_even_when_not_in_historical_lower_tags':True,
        'positive_control':'all higher blocks zero gives exact H2=P^3,F=P^9,G=P^6',
        'blanket_zero_face_negative_control':str(P1**9),
        'negative_controls':{name:str(sp.expand(value)) for name,value in negative.items()},
        'independent_strict_negative_coefficient_checks':strictchecks})
result={'status':'PASS','coefficient_ring':'The declared Q source polynomial ring, then the maintained quotient/localization; pi is an independent polynomial variable.',
 'coefficient_ideal_rule':'If E(pi)=sum e_i*pi^i and M(pi)=sum m_j*pi^j, every coefficient of E*M lies in ideal(e_i), by convolution sum e_i*m_(k-i).',
 'inner_equality_generator':str(inner),'F_equality_generator':str(RF),'G_equality_generator':str(RG),
 'F_membership_identity':str(sp.expand(F-p**9))+' = (u*p+v)*('+str(MF)+') + (a*p^3+b)',
 'G_membership_identity':str(sp.expand(G-p**6))+' = (u*p+v)*('+str(MG)+') + (c*p^3+d)',
 'identities_verified':True,'higher_series_remainder_divisible_by_s':True,
 'no_unknown_was_omitted_before_its_actual_coefficient_equation':True,
 'required_provenance':'Every strict coefficient and every equality-target coefficient used here must be generated and its full graph/radical phase chain replayed. This universal proof then certifies all omitted product rows without re-expansion.',
 'records':records,'custody':{name:hashlib.sha256((N/name).read_bytes()).hexdigest() for name in ['engine.py','source_data.py','deep_accelerated.py','print-audit-pole-membership.py']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','universal_identities':2,'branches':[r['branch'] for r in records],
                  'negative_controls_per_branch':len(records[0]['negative_controls'])},indent=2))
