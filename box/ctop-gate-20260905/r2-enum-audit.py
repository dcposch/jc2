#!/usr/bin/env python3
"""Round 2 independent replay of labelled C-TOP, with no replay JSON input until
after enumeration. This tests arithmetic and census membership, not whether the
labels describe the characteristic data of a realized child.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
import time
from collections import Counter
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
FROZEN = Path('/tmp/jc2-lane.yqyWvI/inputs')
OUT = ROOT / 'box/ctop-gate-20260905'
TREE_PATH = ROOT / 'box/centre-gate-20260903/opus5_probe.py'

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value

B = module('moh_skeleton_full_frozen', FROZEN / 'moh_skeleton_full.py')
T = module('r2_operative_tree', TREE_PATH)
assert T.B is B

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def gcds(n, Ms):
    # Evaluate each prefix afresh to avoid inheriting the previous replay's loop.
    return [reduce(gcd, [n, *Ms[:i]]) for i in range(len(Ms) + 1)]

def row(n, m, Ms, Vs):
    full = (-m, *Ms)
    d = gcds(n, full)
    ds = d[-2]
    us = ds - Vs[len(full)]
    scale = Fraction(us, ds)
    np, mp = Fraction(n) * scale, Fraction(m) * scale
    cm = [Fraction(M) * scale for M in full[:-1]]
    assert np.denominator == mp.denominator == 1
    assert all(z.denominator == 1 for z in cm)
    np, mp = int(np), int(mp)
    cm = [int(z) for z in cm]
    cv = [Vs[i] for i in range(2, len(full))]
    cd = gcds(np, cm)
    assert cd == [scale * z for z in d[:-1]]
    assert cd[-1] == us
    assert all(cd[i+1] < cd[i] for i in range(1, len(cd)-1))
    dropped = cm[-1] == np - 1
    em = cm[:-1] if dropped else cm[:]
    ev = cv[:-1] if dropped else cv[:]
    ed = gcds(np, em)
    assert len(em) >= 2
    assert not dropped or (us == 1 and gcd(ed[-1], np - 1) == 1)
    return dict(n=n, m=m, Ms=list(Ms), V={str(i): Vs[i] for i in sorted(Vs)},
                s=len(full), parent_M=list(full), parent_d=d, d_s=ds, u_s=us,
                v_s=Vs[len(full)], ell=Vs[len(full)]-us-1, n1=np, m1=mp,
                raw_sp=len(cm), raw_M=cm, raw_d=cd, raw_V=cv,
                effective_sp=len(em), effective_M=em, effective_d=ed,
                effective_V=ev, drops=int(dropped), raw_ctop_fail=cv[-1] > cd[-2],
                effective_ctop_fail=ev[-1] > ed[-2], up=gcd(np,mp)-Vs[2],
                U_NEG=Vs[2] > gcd(np,mp),
                labelled_roots_in_D1=str(Fraction(np, gcd(np,mp))*Vs[2]))

def key(r):
    return (r['n'],r['m'],tuple(r['Ms']),tuple(sorted(r['V'].items())))

def hist(rs, field):
    return dict(sorted(Counter(r[field] for r in rs).items()))

def counts(rs):
    us1 = [r for r in rs if r['u_s'] == 1]
    higher = [r for r in rs if r['u_s'] > 1]
    live = [r for r in us1 if not r['effective_ctop_fail']]
    dead = [r for r in us1 if r['effective_ctop_fail']]
    dropped = [r for r in rs if r['drops']]
    return dict(rows=len(rs), by_us=hist(rs, 'u_s'),
        raw_sp=hist(rs,'raw_sp'), effective_sp=hist(rs,'effective_sp'),
        drops=hist(rs,'drops'), drops_by_us=hist(dropped,'u_s'),
        us1=dict(rows=len(us1),raw_fail=sum(r['raw_ctop_fail'] for r in us1),
            effective_fail=len(dead),effective_live=len(live),
            fail_by_effective_sp=hist(dead,'effective_sp'),
            live_by_effective_sp=hist(live,'effective_sp'),
            live_by_raw_sp=hist(live,'raw_sp'),
            live_degree_pairs=len({(r['n'],r['m']) for r in live}),
            U_NEG=sum(r['U_NEG'] for r in us1),
            U_NEG_and_ctop_live=sum(r['U_NEG'] for r in live),
            rescued_by_drop=sum(r['raw_ctop_fail'] for r in live)),
        us_ge2=dict(rows=len(higher),raw_fail=sum(r['raw_ctop_fail'] for r in higher),
            effective_fail=sum(r['effective_ctop_fail'] for r in higher),
            U_NEG=sum(r['U_NEG'] for r in higher)),
        U_NEG=sum(r['U_NEG'] for r in rs),
        drop_cross_tab={str(k): v for k,v in sorted(Counter(
            (r['u_s'],r['raw_ctop_fail'],r['effective_ctop_fail']) for r in dropped).items())})

started=time.monotonic()
all_rows=[]
operative=[]
for n in range(16,201):
    for m,Ms,Vs in B.census(n,Kmin=2,full=True):
        parent = B.Skel(n,m,Ms,Vs)
        assert parent.windows_ok() and parent.full_ok()
        r = row(n,m,Ms,Vs)
        tree = T.Tree(n,m,Ms,gate=False,ode=True,capacity=False,passport=False,recenter=True)
        r['operative'] = tree.embeds(Vs) is not None
        all_rows.append(r)
        if r['operative']:
            operative.append(r)
    if n % 20 == 0:
        print(json.dumps(dict(n=n,census=len(all_rows),operative=len(operative),
                              seconds=round(time.monotonic()-started,3))),flush=True)

assert len({key(r) for r in all_rows}) == len(all_rows)
summary={'census':counts(all_rows), 'operative':counts(operative)}
summary=json.loads(json.dumps(summary))

# The charged replay is used only after fresh regeneration, and compared exactly.
prior=json.loads((FROZEN/'enum-replay.json').read_text())
old={key(r): r for r in prior['operative_rows']}
new={key(r): r for r in operative}
assert new.keys() == old.keys()
differences=[]
for k,r in new.items():
    if r != old[k]:
        differences.append(dict(key=str(k),fields={f:[r.get(f),old[k].get(f)]
            for f in set(r)|set(old[k]) if r.get(f) != old[k].get(f)}))
assert not differences
assert summary == prior['summary']

# Positive/negative C-TOP controls at the same characteristic-label chain.
family=[r for r in operative if (r['n'],r['m'],r['Ms']) == (96,72,[36,78,94])]
assert {tuple(r['raw_V']): r['effective_ctop_fail'] for r in family} == {
    (1,1):False,(1,3):True,(4,3):True}
moh=[row(n,m,Ms,V) for n,m,Ms,V,*_ in B.MOH_TABLE]
assert len([r for r in moh if r['u_s']==1]) == 5
assert all(not r['effective_ctop_fail'] for r in moh if r['u_s']==1)
drop_rows=[r for r in operative if r['drops']]
assert all(not r['U_NEG'] for r in drop_rows)
assert all(r['raw_ctop_fail'] for r in drop_rows)
assert all(r['raw_d'][-1] == 1 and r['effective_d'][-1] > 1 for r in drop_rows)
assert all((Fraction(r['labelled_roots_in_D1']) > r['n1']) == r['U_NEG'] for r in operative)

result=dict(schema='jc2.ctop-gate.r2-enum-audit/v1',
    limitation='All tests are of campaign labels; equality with actual child data is not established by this computation.',
    settings=prior['settings'],summary=summary,
    verification=dict(census_unique=True,parent_windows_and_full_ok=True,gcd_scaling=True,
        strict_gcd_drops=True,charged_replay_exact_row_match=True,
        charged_replay_exact_summary_match=True,moh5_us1_positive_controls=True,
        same_M_positive_and_negative_controls=True,drops_U_NEG_disjoint=True,
        dropped_effective_top_gcd_exceeds_one=True,labelled_root_count_identity=True),
    input_sha256={str(p):sha(p) for p in [FROZEN/'moh_skeleton_full.py',
        FROZEN/'enum-replay.json',TREE_PATH]},
    named_instance=family,moh_table=moh,
    drop_rescued=[r for r in drop_rows if not r['effective_ctop_fail']],
    drop_still_fails=[r for r in drop_rows if r['effective_ctop_fail']],
    operative_rows=operative,seconds=round(time.monotonic()-started,3))
(OUT/'r2-enum-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
print(json.dumps(result['verification'],indent=2),flush=True)
print('Exact charged replay comparison: PASS',flush=True)
