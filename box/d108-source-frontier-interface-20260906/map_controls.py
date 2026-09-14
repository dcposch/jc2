#!/usr/bin/env python3
"""Exact partial-map, source-residual independence, and transverse-port controls."""
import copy
import json
from pathlib import Path
import resource
import time
import sys
import sympy as S
root=Path(__file__).resolve().parent
data=json.loads((root/'source_interface.json').read_text())
started=time.monotonic()
X,W,x,y,ell2,ell3,ell4,b=S.symbols('X W x y ell2 ell3 ell4 target_b')
def req(ok,why):
    if not ok:raise ValueError(why)
def zero(p):return S.expand(p)==0
def parse(text):return S.sympify(text,locals={'X':X,'W':W,'x':x,'y':y})
def jac(p,q):return S.expand(S.diff(p,x)*S.diff(q,y)-S.diff(p,y)*S.diff(q,x))
packet={'hline':data['line']['h'],'Dline':data['line']['D'],'Cline':data['line']['C'],
 'residuals':[r['expression'] for r in data['residual_rows']],
 'inversion_exponent':4,'target_Q_sign':-1,
 'pre_small_P':[[-1,0],[0,0],[56,16],[48,14]],
 'pre_small_Q':[[2,1],[0,0],[84,24],[72,21]],
 'pre_extra_P':[32,8],'pre_extra_Q':[48,12]}
def verify(p):
    c_names=set(data['C_identity_slots'])
    resid=[parse(e) for e in p['residuals']]
    req(len(resid)==14,'residual census')
    req(not any({str(s) for s in r.free_symbols}&c_names for r in resid),'C coordinate entered residual source ideal')
    K,j0,j1,j2=S.symbols('K2c_3_26 jet0 jet1 jet2')
    L=-K+8*j0*j1-8*j2
    req(zero(resid[0]-L**2),'first residual is not square of axis-leading obstruction')
    h,D,C=map(parse,(p['hline'],p['Dline'],p['Cline']))
    G=S.expand(h**2-b*h/3+D)
    req(S.degree(G,X)==2 and G.coeff(X,2)==1,'monic quadratic transverse restriction failed')
    beta=S.diff(C,X);gamma=C.subs(X,0)
    req(zero(C-beta*X-gamma),'C restriction not affine linear')
    A96,A86,A91=S.symbols('A3c_96_8 A3c_86_16 A3c_91_12')
    req(zero(beta-(S.Rational(2,7)*A96+S.Rational(3,35)*A86+S.Rational(8,35)*A91)),'C line functional mismatch')
    beta_new=S.Symbol('beta')
    change=S.Rational(7,2)*beta_new-S.Rational(3,10)*A86-S.Rational(4,5)*A91
    req(zero(beta.subs(A96,change)-beta_new),'fixed rational C coordinate transport failed')
    const_name='A3c_107_0'
    const_rows=[r for r in data['source_maps']['C'] if const_name in r['names']]
    req(len(const_rows)==1 and const_rows[0]['X']==const_rows[0]['W']==0 and zero(parse(const_rows[0]['coefficient'])-S.Symbol(const_name)),'C constant has a nonconstant tail')
    exponent=p['inversion_exponent']
    nx=x**exponent*y-x**-1+ell2*x**2+ell3*x**3+ell4*x**4
    nw=x**-1
    req(zero(jac(nx,nw)-x**2),'partial coordinate-map Jacobian factor mismatch')
    # Genuine polynomial Keller control F=X+W²,G=W, not a D108 source point.
    P=nw;Q=p['target_Q_sign']*(nx+nw**2)
    req(zero(jac(P,Q)-x**2),'ordered target-pair Jacobian sign mismatch')
    transform=lambda q:[-q[0]+exponent*q[1],q[1]]
    req(set(map(tuple,map(transform,p['pre_small_P'])))=={(0,0),(1,0),(8,14),(8,16)},'small P polygon map mismatch')
    req(set(map(tuple,map(transform,p['pre_small_Q'])))=={(0,0),(2,1),(12,21),(12,24)},'small Q polygon map mismatch')
    req(transform(p['pre_extra_P'])==[0,8] and transform(p['pre_extra_Q'])==[0,12],'large-branch extra vertex map mismatch')
    return {'all14residuals_C_independent':True,'C_constant_column_exactly1':True,
      'C_constant_claim_scope':'raw physical Jacobian and14source residuals ONLY, not complete T2/T3 rows',
      'first_residual_exact_L_squared':str(L**2),'G_line':str(G),
      'beta':str(beta),'C_A96_reconstruction':str(change),
      'partial_map_X':str(nx),'partial_map_W':str(nw),'map_Jacobian':'x^2',
      'valid_Keller_control':'F=X+W^2,G=W; P=map(G),Q=-map(F)',
      'both_terminal_polygon_maps_exact':True,'full_source_to_GGHV_map':'GAP_LOWER_POLYGON_AND_EDGE_FACTOR_TRANSPORT'}
result=verify(packet)
controls=[]
def reject(label,fn):
    bad=copy.deepcopy(packet);fn(bad)
    try:verify(bad)
    except ValueError as e:controls.append({'mutation':label,'status':'REJECTED_BY_ACTUAL_CHECKER','reason':str(e)})
    else:raise ValueError('mutation escaped:'+label)
reject('introduce C constant into source residual',lambda p:p['residuals'].__setitem__(1,p['residuals'][1]+'+A3c_107_0'))
reject('alter first residual square',lambda p:p['residuals'].__setitem__(0,p['residuals'][0]+'+1'))
reject('replace transverse h slope -1 by -2',lambda p:p.__setitem__('hline',p['hline']+'-X'))
reject('inversion x^4*y changed to x^3*y',lambda p:p.__setitem__('inversion_exponent',3))
reject('target Q sign reversed',lambda p:p.__setitem__('target_Q_sign',1))
reject('wrong large-branch extra P vertex',lambda p:p.__setitem__('pre_extra_P',[33,8]))
result.update({'controls':controls,'status':'EXACT_PARTIAL_INTERFACE_AND_PORTABILITY_CONTROLS_PASS',
 'seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
target=root/'map_controls.json'
if '--verify' in sys.argv:
    recorded=json.loads(target.read_text())
    req({k:v for k,v in recorded.items() if k not in ('seconds','peak_rss_kib')}=={k:v for k,v in result.items() if k not in ('seconds','peak_rss_kib')},'replay mismatch')
else:
    req(not target.exists(),'no overwrite')
    target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
