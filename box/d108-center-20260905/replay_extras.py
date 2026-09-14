#!/usr/bin/env python3
from pathlib import Path
import json,sys
from math import comb
from collections import defaultdict
import sympy as sp
from replay_incidence import eng,template,incidence,OUT

def reduce_case(tag,h,hv,extra=()):
    rows=incidence(h)+list(extra);res,subs,piv,zeros=eng.qstar_reduce(rows,hv)
    c,Zc=sp.symbols('c Zc');gens=[v for _,v in res]+[Zc*c-1];rv=sorted(set().union(*(v.free_symbols for v in gens)),key=str);gb=sp.groebner(gens,*rv,order='grevlex')
    datum={'tag':tag,'h3_coordinate_count':len(hv),'extra_rows':[(l,str(v)) for l,v in extra],'template':{f'{r},{q}':str(v) for (r,q),v in sorted(h.items())},'pivots':[{'row':p.label,'variable':str(p.variable),'coefficient':str(p.coefficient),'resolved_value':str(subs[p.variable])} for p in piv],'zero_rows':zeros,'residual':{k:str(v) for k,v in res},'ring_variables':list(map(str,rv)),'coefficient_field':'QQ','groebner_basis':list(map(str,gb.exprs)),'localized_unit':list(gb.exprs)==[sp.Integer(1)]}
    (OUT/(tag+'.json')).write_text(json.dumps(datum,indent=2)+'\n');print(json.dumps({k:datum[k] for k in ('tag','h3_coordinate_count','localized_unit','groebner_basis')}),flush=True)
    return datum

h,hv=template(5,35);H53,H54=sp.symbols('Hc_5_3 Hc_5_4')
reduce_case('physical35_H53_fixed',h,hv,[('fixed_H53',H53+sp.Rational(7,4))])
reduce_case('physical35_face_fixed',h,hv,[('physical_face_coefficient',H53+H54+sp.Rational(7,4))])
h,hv=template(6,43);H81=sp.Symbol('Hc_8_1');h[8,1]=H81;hv.append(H81)
reduce_case('minimal_t8z',h,hv)

# A concrete point verifies every original common-h3 incidence row.
t,z,w,pi,s=sp.symbols('t z w pi s');K=z**7*(1+z)**2-t**8*z
row_witness={v:0 for v in hv};row_witness.update({H81:-1,sp.Symbol('jet1'):0,sp.Symbol('jet2'):0,sp.Symbol('c'):1})
images={l:str(sp.expand(v.subs(row_witness))) for l,v in incidence(h)}
assert set(images.values())=={'0'}
major=sp.expand(K.subs({t:s**4,z:pi*s**5}));minor=sp.expand(K.subs(z,pi*t**4-1))
assert sp.Poly(major,s).terms()[-1][0][0]==35
assert sp.Poly(sp.expand(minor-t**8*(1-pi**2)),t).terms()[-1][0][0]>=9
(OUT/'rational-witness.json').write_text(json.dumps({'K3':str(K),'major_t_s4_z_pi_s5':str(major),'minor_w_pi_t4':str(minor),'incidence_row_images':images,'localization_c':1,'localization_Zc':1,'localization_wrapper_image':0,'claim':'Rational point of necessary common-h3 incidence only; not a Jacobian pair.'},indent=2)+'\n')

# Exact certificate for original weight(4,6) with relative constant-y minor jet.
data=json.loads((OUT/'relative_minor_jet0.json').read_text());res={k:sp.sympify(v) for k,v in data['residual'].items()};j0,j1,j2,c,Zc=sp.symbols('jet0 jet1 jet2 c Zc');A=j1*(j1+j0**2)
R=res['minor_n7_pi1'];S=res['minor_n8_pi1'];T=res['minor_n8_pi0'];L=sp.cancel((T+A*S/2+c)/R);assert sp.denom(L).is_Rational
identity=sp.expand(Zc*L*R-Zc*T-Zc*A*S/2-(Zc*c-1));assert identity==1
(OUT/'relative-jet0-certificate.json').write_text(json.dumps({'coefficient_field':'QQ','coefficients':{'minor_n7_pi1':str(Zc*L),'minor_n8_pi0':str(-Zc),'minor_n8_pi1':str(-Zc*A/2),'Zc*c-1':'-1'},'expanded_identity':str(identity),'unused_residuals':['minor_n6_pi0','minor_n7_pi0']},indent=2)+'\n')
print('rational witness and relative-jet0 exact certificate: PASS',flush=True)
