#!/usr/bin/env python3
"""Bounded exact coefficient-reduction and patched-engine controls."""
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
from fractions import Fraction

root=Path('/home/ubuntu/full-j-solver-pilot-20260906')
if socket.gethostname()!='ip-172-30-0-56' or Path.cwd()!=root:
    raise SystemExit('wrong worker/root')
from flint import fmpq_mpoly,fmpq_mpoly_ctx,nmod_mpoly,nmod_mpoly_ctx
p=1073741827
names=('Hc_11_0','A3c_99_0','Hfact_0_0')
qctx=fmpq_mpoly_ctx.get(names,ordering='degrevlex')
pctx=nmod_mpoly_ctx.get(names,p,ordering='degrevlex')
pattern=re.compile(r'(^|[+-])(\d+)(?:/(\d+))?(?=\*|$|[+-])')
def rewrite(poly,strip=True):
    def sub(m):
        sign,num,den=m.groups()
        den=int(den or '1')
        if den%p==0:raise ValueError('bad denominator')
        val=int(num)%p*pow(den,-1,p)%p
        if val==0:raise ValueError('zero term')
        return sign+str(val)
    return pattern.sub(sub,re.sub(r'\s+','',poly) if strip else poly)
raw='-Hc_11_0^3 - 1/2*A3c_99_0^2 + 33075/2*Hfact_0_0 - 3/4'
q=fmpq_mpoly(raw,ctx=qctx)
ref={e:int(Fraction(str(c)).numerator)%p*pow(Fraction(str(c)).denominator,-1,p)%p for e,c in q.to_dict().items()}
actual=nmod_mpoly(rewrite(raw),ctx=pctx)
if {e:int(c) for e,c in actual.to_dict().items()}!=ref:raise SystemExit('Q-to-Fp semantic mismatch')
if '/' not in rewrite(raw,False):raise SystemExit('whitespace negative control did not fire')
if nmod_mpoly(rewrite(raw.replace('- 3/4','+ 3/4')),ctx=pctx)==actual:raise SystemExit('sign mutation accepted')
for bad in [f'1/{p}*Hc_11_0',f'{p}*Hc_11_0']:
    try:rewrite(bad)
    except ValueError:pass
    else:raise SystemExit('bad denominator/zero term accepted')
rec=json.loads((root/'binary.json').read_text())
binary=rec['binary']
results={}
for name,rows in {'unit':['x+y','x-y','x-1'],'proper':['x*y-1','y^2-x']}.items():
    inp=root/('control-'+name+'.ms')
    inp.write_text('x,y\n'+str(p)+'\n'+',\n'.join(rows)+'\n')
    out=root/('control-'+name+'.basis')
    with (root/('control-'+name+'.stdout')).open('x') as so,(root/('control-'+name+'.stderr')).open('x') as se:
        done=subprocess.run([binary,'-g','2','-t','2','-v','2','--random-seed','0','-f',str(inp),'-o',str(out)],stdout=so,stderr=se,check=True)
    data=out.read_text()
    if '#Reduced Groebner basis data' not in data:raise SystemExit('missing reduced basis header')
    match=re.search(r'\[([^\[\]]*)\]\s*:\s*\Z',data,re.S)
    if not match:raise SystemExit('incomplete smoke basis')
    polys=[s.strip() for s in match.group(1).split(',') if s.strip()]
    if name=='unit' and polys!=['1']:raise SystemExit('unit control did not produce1')
    if name=='proper' and (len(polys)!=3 or '1' in polys):raise SystemExit('proper control wrong basis')
    results[name]={'returncode':done.returncode,'basis':polys,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
(root/'smoke.json').write_text(json.dumps({'exact_rational_reduction':True,'whitespace_negative':True,'coefficient_sign_mutation':True,
    'bad_denominator_and_zero_term_rejected':True,'prime':p,'engine_controls':results},sort_keys=True,indent=2)+'\n')
(root/'smoke.PASS').write_text('EXACT_COEFFICIENT_AND_PATCHED_ENGINE_SMOKES_PASS\n')
print('ALL_SMOKES_PASS',flush=True)
