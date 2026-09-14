#!/usr/bin/env python3
"""Independent fresh census replay; no precomputed JSON is an input to the screen.
Frozen enumerator from /tmp lane; operative Tree read from campaign code.
The labelled descent is independently recomputed with integer division and gcd.
Counts below audit that algorithm, not identification with any actual child.
"""
import sys
sys.dont_write_bytecode = True
import hashlib, importlib.util, json, time
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
ROOT = Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/ctop-gate-20260905'
FROZEN = Path('/tmp/jc2-lane.RbaPkU/inputs/moh_skeleton_full.py')
TREE = ROOT / 'box/centre-gate-20260903/opus5_probe.py'

def imp(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod

B = imp('moh_skeleton_full_frozen', FROZEN)
P = imp('ctop_gate_operative_tree', TREE)
assert P.B is B  # Tree's own import resolves to the charged frozen module.

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def chain(n, M):
    d = [n]
    for z in M:
        d.append(gcd(d[-1], z))
    return d

def labels(n, m, Ms, V):
    parentM = [-m, *Ms]
    parentd = chain(n, parentM)
    s = len(parentM)
    ds = parentd[-2]
    us = ds - V[s]
    assert n*us % ds == m*us % ds == 0
    assert all(M*us % ds == 0 for M in parentM[:-1])
    np, mp = n*us//ds, m*us//ds
    rawM = [M*us//ds for M in parentM[:-1]]
    rawV = [V[i] for i in range(2, s)]
    rawd = chain(np, rawM)
    # Check scaling from actual gcd calculations, not a replacement assignment.
    assert rawd == [d*us//ds for d in parentd[:-1]]
    assert rawd[-1] == us
    effM = rawM[:]
    effV = rawV[:]
    drops = 0
    while len(effM) >= 2 and effM[-1] == np-1:
        effM.pop(); effV.pop(); drops += 1
    effd = chain(np, effM)
    assert len(effM) >= 2
    return dict(n=n,m=m,Ms=list(Ms),V={str(i): V[i] for i in sorted(V)},
        s=s,parent_M=parentM,parent_d=parentd,d_s=ds,u_s=us,v_s=V[s],ell=V[s]-us-1,
        n1=np,m1=mp,raw_sp=len(rawM),raw_M=rawM,raw_d=rawd,raw_V=rawV,
        effective_sp=len(effM),effective_M=effM,effective_d=effd,effective_V=effV,
        drops=drops,raw_ctop_fail=rawV[-1]>rawd[-2],
        effective_ctop_fail=effV[-1]>effd[-2],
        up=gcd(np,mp)-V[2],U_NEG=(V[2]>gcd(np,mp)),
        labelled_roots_in_D1=str(F(np,gcd(np,mp))*V[2]))

def hist(rs, name):
    return dict(sorted(Counter(r[name] for r in rs).items()))

def summary(rs):
    us1 = [r for r in rs if r['u_s']==1]
    us2 = [r for r in rs if r['u_s']>=2]
    fail = [r for r in us1 if r['effective_ctop_fail']]
    live = [r for r in us1 if not r['effective_ctop_fail']]
    return dict(rows=len(rs),by_us=hist(rs,'u_s'),
        raw_sp=hist(rs,'raw_sp'),effective_sp=hist(rs,'effective_sp'),
        drops=hist(rs,'drops'),drops_by_us=hist([r for r in rs if r['drops']],'u_s'),
        us1=dict(rows=len(us1),raw_fail=sum(r['raw_ctop_fail'] for r in us1),
            effective_fail=len(fail),effective_live=len(live),
            fail_by_effective_sp=hist(fail,'effective_sp'),live_by_effective_sp=hist(live,'effective_sp'),
            live_by_raw_sp=hist(live,'raw_sp'),
            live_degree_pairs=len({(r['n'],r['m']) for r in live}),
            U_NEG=sum(r['U_NEG'] for r in us1),U_NEG_and_ctop_live=sum(r['U_NEG'] for r in live),
            rescued_by_drop=sum(r['raw_ctop_fail'] and not r['effective_ctop_fail'] for r in us1)),
        us_ge2=dict(rows=len(us2),raw_fail=sum(r['raw_ctop_fail'] for r in us2),
            effective_fail=sum(r['effective_ctop_fail'] for r in us2),
            U_NEG=sum(r['U_NEG'] for r in us2)),
        U_NEG=sum(r['U_NEG'] for r in rs),
        drop_cross_tab={str(k):v for k,v in sorted(Counter((r['u_s'],r['raw_ctop_fail'],r['effective_ctop_fail']) for r in rs if r['drops']).items())})

started=time.monotonic()
census=[]; operative=[]; progress=[]
for n in range(16,201):
    for m,Ms,V in B.census(n,Kmin=2,full=True):
        r=labels(n,m,Ms,V)
        census.append(r)
        tree=P.Tree(n,m,Ms,gate=False,ode=True,capacity=False,passport=False,recenter=True)
        op=tree.embeds(V) is not None
        r['operative']=op
        if op: operative.append(r)
    if n%20==0:
        p=dict(n=n,census=len(census),operative=len(operative),seconds=round(time.monotonic()-started,3))
        progress.append(p);print(json.dumps(p),flush=True)

summary_out={'census':summary(census),'operative':summary(operative)}
# Sanity controls that do not assume the headline screen numbers.
keys=[(r['n'],r['m'],tuple(r['Ms']),tuple(sorted(r['V'].items()))) for r in census]
assert len(set(keys))==len(keys)
assert all(r['raw_d'][-1]==r['u_s'] for r in census)
assert all(r['effective_sp']>=2 for r in operative)
assert not any(r['effective_ctop_fail'] and not r['raw_ctop_fail'] for r in operative if r['drops'])
assert all((F(r['labelled_roots_in_D1'])>r['n1'])==r['U_NEG'] for r in operative)
printed=[]
for n,m,Ms,V,*_ in B.MOH_TABLE:
    r=labels(n,m,Ms,V)
    r['operative']=P.Tree(n,m,Ms,gate=False,ode=True,capacity=False,passport=False,recenter=True).embeds(V) is not None
    printed.append(r)
assert all(r['operative'] for r in printed)
assert all(not r['effective_ctop_fail'] for r in printed if r['u_s']==1)

# Comparison against prior JSON is diagnostic only and occurs after independent regeneration.
prior_path=ROOT/'box/scopeleaks-20260905/scope_enum.json'
prior=json.loads(prior_path.read_text())['operative_rows']
def key_old(r): return (r['n'],r['m'],tuple(r['Ms']),tuple(sorted((int(k),v) for k,v in r['V'].items())))
def key_new(r): return (r['n'],r['m'],tuple(r['Ms']),tuple(sorted((int(k),v) for k,v in r['V'].items())))
prior_by={key_old(r):r for r in prior}; fresh_by={key_new(r):r for r in operative}
match_fields=[]
for k in prior_by.keys()&fresh_by.keys():
    a,b=prior_by[k],fresh_by[k]
    for field in ('n1','m1','u_s','v_s','ell','up'):
        if a[field]!=b[field]:match_fields.append([str(k),field,a[field],b[field]])
    if a['sp']!=b['raw_sp'] or [int(F(z)) for z in a['Mp']]!=b['raw_M'][1:] or a['Vp']!=b['raw_V']:
        match_fields.append([str(k),'label_vectors'])
comparison=dict(prior_rows=len(prior),fresh_rows=len(operative),
    prior_only=len(prior_by.keys()-fresh_by.keys()),fresh_only=len(fresh_by.keys()-prior_by.keys()),
    field_discrepancies=match_fields)
inputs=[FROZEN,TREE,ROOT/'box/scopeleaks-20260905/scope_enum.py',ROOT/'box/scopeleaks-20260905/depth.py',ROOT/'box/child-data-20260905/test12_childdata.py',ROOT/'box/child-data-20260905/test2-partition.log']
output=dict(schema='jc2.ctop-gate.enum-independent/v1',settings=dict(nlo=16,nhi=200,Kmin=2,full=True,gate=False,ode=True,capacity=False,passport=False,recenter=True),
    caution='Reproduces labels and numerical predicates only. Own-child characteristic-data identification is not assumed proved.',
    input_sha256={str(p):sha(p) for p in inputs},prior_diagnostic=dict(path=str(prior_path),sha256=sha(prior_path),comparison=comparison),
    summary=summary_out,controls=dict(unique_census_rows=True,gcd_scaling_all_census=True,moh_six_operative=True,moh_five_us1_screen_live=True),
    moh_table=printed,named_instance=[r for r in operative if (r['n'],r['m'],r['Ms'])==(96,72,[36,78,94])],
    rescued_by_drop=[r for r in operative if r['u_s']==1 and r['raw_ctop_fail'] and not r['effective_ctop_fail']],
    operative_rows=operative,progress=progress,seconds=round(time.monotonic()-started,3))
(OUT/'enum-replay.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(summary_out,indent=2),flush=True)
print('PRIOR_DIAGNOSTIC '+json.dumps(comparison),flush=True)
print('WROTE '+str(OUT/'enum-replay.json'),flush=True)
