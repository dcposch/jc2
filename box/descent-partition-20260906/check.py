"""Exact local inversion controls; no roster, producer evaluator, or route import.

Only four pure functions are loaded by AST from the verified frozen instrument.
The R063 block is a consistency audit of the literal frozen report descriptor,
not an assertion that this descriptor is the omitted original roster row.
"""
from __future__ import annotations
import ast
import hashlib
import json
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
from typing import Any, Mapping

HERE = Path(__file__).resolve().parent
INPUTS = Path('/tmp/jc2-lane.X8q4dc/inputs')
source = (INPUTS / 'descend_own.py').read_text()
assert hashlib.sha256(source.encode()).hexdigest() == '3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2'
names = {'exact_int', 'prefix_gcds', 'def51_radii', 'inverse_top'}
tree = ast.parse(source)
body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
assert {n.name for n in body} == names
exec(compile(ast.Module(body=body, type_ignores=[]), '<frozen pure helpers>', 'exec'))


def leaf(n, m, H, birth, lam_f, rho):
    n, m, H, birth, lam_f, rho = map(Q, (n, m, H, birth, lam_f, rho))
    kap = rho * (H - birth) + lam_f
    if kap > 0:
        delta = H - (n + m) * kap / ((n + m) * rho - m)
        lf = lam_f + rho * (delta - birth)
        lg = n / m * lf
        contribution = -rho * lg
        assert delta == H + lf + lg
        return dict(kind='major', rho=rho, delta=delta, lam_f=lf,
                    lam_g=lg, contribution=contribution)
    assert kap < 0
    return dict(kind='minor', rho=rho, delta=birth - lam_f / rho,
                lam_f=Q(0), lam_g=Q(0), contribution=Q(0))


def transverse(N, rho, e, delta, lf, lg, u=1, v=3):
    N, rho, e, delta, lf, lg, u, v = map(Q, (N, rho, e, delta, lf, lg, u, v))
    assert delta > e > 0
    out = dict(discs=N*e, rho=rho, delta=v-u+u/e*(delta-1),
               lam_f=u/e*lf, lam_g=u/e*lg)
    assert out['discs'].denominator == 1
    out['total_roots'] = out['discs'] * rho
    out['major_sum'] = -out['discs'] * rho * out['lam_g']
    assert out['major_sum'] == u * (-N * rho * lg)
    return out


controls = {}
for name, n, m, M, V, birth, z, rs in [
    ('R009', 192, 128, {1:-128, 2:148, 3:190}, {2:2, 3:3, 4:2}, Q(5,16), 0, (2,1)),
    ('R050', 196, 56, {1:-56, 2:184, 3:194}, {2:4, 3:3, 4:2}, Q(1,4), 1, (4,1)),
]:
    d = prefix_gcds(n, M)
    parent_radii = def51_radii(n, M, d, V)
    assert parent_radii[2] == birth
    inv = inverse_top(n, d[3], d[2], 1, 3, birth, z, rs)
    np, mp = n//4, m//4
    Mc = {1:M[1]//4, 2:M[2]//4}
    dc = prefix_gcds(np, Mc)
    child_radii = def51_radii(np, Mc, dc, {2:V[2], 3:1}, 2)
    child_birth = 3 - 1/birth
    assert child_radii[2] == child_birth
    records = []
    for group in inv['inverse_groups']:
        rho = group['roots'] * Q(m,n)
        rec = leaf(np, mp, 2, child_birth,
                   mp*(child_birth-2)/(np-Mc[2]), rho)
        records.append(dict(group=group, leaf=rec))
    total = sum(r['leaf']['contribution'] for r in records)
    assert total == 8
    assert sum(r['leaf']['rho'] for r in records) == mp
    controls[name] = dict(source=dict(n=n,m=m,M=M,V=V,d=d,radii=parent_radii),
                          child=dict(n=np,m=mp,M=Mc,d=dc,radii=child_radii),
                          inverse_top=inv, child_packets=records, I_M=total)

controls['R009']['transverse_major'] = transverse(16,4,Q(5,16),Q(19,24),Q(-1,12),Q(-1,8))
controls['R009']['transverse_minor'] = transverse(16,2,Q(5,16),Q(21,16),0,0)
controls['R009']['regular_minor'] = dict(discs=1,rho=2,delta=3,lam_f=0,lam_g=0)
controls['R009']['principal_image'] = dict(chart='gamma=0',discs=1,rho=32,radius_gamma=0)
controls['R050']['transverse_major'] = transverse(4,8,Q(1,4),Q(19,28),Q(-1,14),Q(-1,4))
controls['R050']['transverse_minor'] = transverse(4,2,Q(1,4),2,0,0)
controls['R050']['endpoint_minor'] = dict(source_discs=1,source_rho=2,source_delta=2,
                                         child_discs=1,child_rho=4,child_delta=Q(5,2),
                                         lam_f=0,lam_g=0)
controls['R050']['principal_image'] = dict(chart='gamma=0',discs=1,rho=14,radius_gamma=0)
assert 32-controls['R009']['transverse_major']['total_roots']-controls['R009']['transverse_minor']['total_roots'] == 2
assert 14-controls['R050']['transverse_major']['total_roots']-controls['R050']['transverse_minor']['total_roots']-4 == 0

# Exhaust the possible effective child characteristics from the literal descriptor.
# d2=14; d3 is a proper divisor >1.  P2 = 7*14/d3 = 5+3*A.
candidates = []
for M2 in range(-27,41):
    d3 = gcd(14,M2)
    if not 1 < d3 < 14:
        continue
    P = Q(7*14,d3)
    A = (P-5)/3
    if A.denominator != 1 or A <= 0:
        continue
    for M3 in range(M2+1,41):
        if gcd(d3,M3) != 1:
            continue
        Mc = {1:-28,2:M2,3:M3}
        dc = prefix_gcds(42,Mc)
        rc = def51_radii(42,Mc,dc,{2:3,3:7,4:1},2)
        # Since V3=d3 and p3 has degree d3, the selected p3 is all zero;
        # the incoming centre at level 2 has stabilizer 1, not den(delta3).
        if rc[2].denominator != A:
            continue
        candidates.append(dict(M=Mc,d=dc,radii=rc,A=A,P=P))
assert [c['M'][3] for c in candidates] == [36,37,38,39,40]
assert all(c['M'][2] == 35 and c['radii'][2] == Q(-1,3) for c in candidates)

child_r063_major = leaf(42,28,2,Q(-1,3),Q(-28,3),6)
child_r063_zero = leaf(42,28,2,Q(-1,3),Q(-28,3),10)
assert 3*child_r063_major['contribution'] + child_r063_zero['contribution'] == Q(71,4)

parents = []
for c in candidates:
    Ms = {1:-112,2:140,3:4*c['M'][3],4:166}
    ds = prefix_gcds(168,Ms)
    # Exhaust the first-support alternatives of the frozen recurrence, keeping
    # only the descriptor's child V3=7.  No route-tree completion is asserted.
    possible = []
    for V3 in range(1,22):
        if V3*(168-Ms[3]) <= ds[3]:
            continue
        Vs = {2:3,3:V3,4:3,5:2}
        rr = def51_radii(168,Ms,ds,Vs)
        if not rr[3] < rr[2] < rr[1] < 1 or rr[1] <= 0:
            continue
        e3 = rr[3]
        if e3 > 0 and e3.denominator*V3 <= 21 and V3 == 7:
            possible.append((V3,'nonzero'))
        if (21-V3) % e3.denominator == 0 and 7-e3*(21-V3) == 7:
            possible.append((V3,'zero'))
    assert possible == [(21,'zero')]
    Vs = {2:3,3:21,4:3,5:2}
    rr = def51_radii(168,Ms,ds,Vs)
    assert rr[2] == Q(3,10)
    # P2=42, A2=10, selected multiplicity=3; another orbit of multiplicity
    # 1 leaves a zero of multiplicity 2, precisely the forbidden threshold.
    patterns = []
    for extras in [(),(1,)]:
        mults = (3,)+extras
        zero = 42-10*sum(mults)
        if zero < 0 or zero == 2:
            continue
        patterns.append((zero,mults))
    assert patterns == [(12,(3,))]
    maj = leaf(168,112,1,Q(3,10),Q(-14,5),6)
    zer = leaf(168,112,1,Q(3,10),Q(-14,5),24)
    im = 10*maj['contribution'] + zer['contribution']
    assert im == Q(1035,59) and im != 19
    assert zer['delta'].denominator == 59
    assert 24 % 59 not in (0,1) and 36 % 59 not in (0,1)
    projection = inverse_top(168,4,56,1,3,Q(3,10),12,(3,))
    assert projection['inverse_groups'][0]['V'] == 5
    parents.append(dict(M=Ms,d=ds,V=Vs,radii=rr,first_support=possible,
                        level2_pattern=patterns[0],selected_final=maj,
                        zero_final=zer,I_M=im,projection=projection))

r063 = dict(type='LITERAL_FROZEN_DESCRIPTOR_CONSISTENCY_AUDIT_NOT_ROSTER_IDENTIFICATION',
            child_candidates=candidates, child_major=child_r063_major,
            child_zero=child_r063_zero, child_flat_I=Q(71,4),
            inferred_parents=parents, inferred_parent_I=Q(1035,59),
            reported_parent_I=19, compatible_with_reported_parent_I=False,
            inferred_full_source_route='EMPTY_BY_FORCED_ZERO_FINAL_GALOIS_FAILURE',
            child_zero_galois=dict(centre_stabilizer=1,increment=24,rho_f=10,rho_g=15,passes=False),
            row_verdict='OPEN_MISSING_CORRECT_FROZEN_R063_ROW_AND_FULL_PATTERN')
assert child_r063_zero['delta'].denominator == 24
assert 10 % 24 not in (0,1) and 15 % 24 not in (0,1)

# Negative controls: using only the shift and retaining source packet counts
# does not transport the sum; using the orbit count and valuation both does.
negative_controls = dict(
    R009_kept_16_discs_at_child_radius=16*4*Q(3,5)*(2-Q(4,3)),
    R050_kept_4_discs_at_child_radius=4*8*Q(7,9)*(2-Q(5,7)),
    general_cover=transverse(16,4,Q(5,16),Q(19,24),Q(-1,12),Q(-1,8),u=2,v=5),
)
assert negative_controls['R009_kept_16_discs_at_child_radius'] == Q(128,5)
assert negative_controls['R050_kept_4_discs_at_child_radius'] == 32
assert negative_controls['general_cover']['major_sum'] == 16

def plain(obj):
    if isinstance(obj,Q):
        return str(obj)
    if isinstance(obj,dict):
        return {str(k):plain(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):
        return [plain(v) for v in obj]
    return obj

result = dict(schema='jc2.descent-partition/v1',controls=controls,
              R063_literal_descriptor=r063,negative_controls=negative_controls,
              major_transport='I_M(child)=u_s*I_M(parent) on actual mapped major orbits',
              full_packet_bijection=False,ledger_edits=False)
(HERE/'checks.json').write_text(json.dumps(plain(result),indent=2)+'\n')
print('PASS: R009=8, R050=8; orbit transport; u=2 scaling; R063 descriptor inconsistency.')
