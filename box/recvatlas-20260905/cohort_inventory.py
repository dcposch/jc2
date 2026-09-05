#!/usr/bin/env python3
"""Exact read-only replay and typed atlas inventory of the 296-row cohort.

This is arithmetic/interface coverage, never a new skeleton emptiness claim.
The broad receiver map is the finite coefficient map proved in the parent
report, conditional on Moh Proposition 6.3's licensed radius branch.  The
original source's complementary split branch is retained as UNASSIGNED.
"""
from __future__ import annotations

import collections
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/recvatlas-20260905/cohort'
FROZEN = Path('/tmp/jc2-lane.MMCkx9/inputs')


def read_json(relative):
    path = ROOT / relative
    read_paths.append(path)
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def histogram(items):
    return dict(sorted(collections.Counter(items).items()))


def source_interface(r):
    n, m, u, v = r['n'], r['m'], r['u_s'], r['V_s']
    ds = u + v
    np, mp = Fraction(n * u, ds), Fraction(m * u, ds)
    assert np.denominator == mp.denominator == 1
    s = skeleton.Skel(n, m, r['M'], {int(i): j for i, j in r['V'].items()})
    assert s.d[r['s']] == ds
    assert s.windows_ok() and s.full_ok()
    assert s.delta[r['s']] == -1
    mprime = [Fraction(t * u, ds) for t in [-m] + r['M'][:-1]]
    assert all(t.denominator == 1 for t in mprime)
    terminal_anchor = np - mprime[-1] - 1
    ell = v - u - 1
    assert ell >= 0
    key = [int(np), int(mp), ell, r['V']['2']]
    record = {
        'row_key': r['row_key'],
        'source': {
            'n': n, 'm': m, 's': r['s'], 'M2_to_Ms': r['M'], 'V': r['V'],
            'd': s.d, 'delta': {str(i): str(d) for i, d in s.delta.items()},
            'u_s': u, 'v_s': v, 'd_s': ds,
        },
        'conditional_descendant': {
            'coarse_key': key, 'n_prime': int(np), 'm_prime': int(mp),
            'ell': ell, 'M_prime_including_M1': list(map(int, mprime)),
            'V_prime': {i: j for i, j in r['V'].items() if int(i) < r['s']},
            'height': len(mprime), 'terminal_anchor': str(terminal_anchor),
            'terminal_radius_if_inherited_formula_applies': str(-Fraction(ell + 1, terminal_anchor)),
        },
        'literal_wedge_k1': {
            'status': 'UNASSIGNED',
            'reason': 'NO_PROVED_NECESSARY_FORWARD_WEDGE_SUPPORT_PULLBACK',
            'additional_exponent_mismatch': ell != 1,
            'arithmetic_exponent_candidate_only': ell == 1,
        },
        'licensed_radius_branch': {
            'hypothesis': f'delta_star_(s-1) >= {v}/{u}',
            'source': 'Moh 1983 printed p.197 Proposition 6.3; printed p.198 proof',
            'status': 'ASSIGNED_CONDITIONAL_BROAD_MONOMIAL_RECEIVER',
            'map_schema': 'COEFFICIENT_EXTRACTION_NEGATIVE_LAURENT_ROWS_V1',
            'A_gamma_exponents': list(range(v)),
            'source_substitution': {
                'X': f'beta*(gamma^(-{u})-e-A(gamma)-pi*gamma^{v})',
                'Y': f'gamma^(-{u})',
                'localization_row': 'b*beta-1',
            },
            'receiver_support_caps': {
                'P_gamma_degree': v * n, 'P_pi_degree': int(np),
                'Q_gamma_degree': v * m, 'Q_pi_degree': int(mp),
                'exact_pi_degrees_or_monicity_imposed': False,
            },
            'receiver_localization': 'c*rho-1',
            'map_generator_images': {
                'p_ij': '[gamma^i*pi^j] F(X(gamma,pi),Y(gamma,pi))',
                'q_ij': '[gamma^i*pi^j] G(X(gamma,pi),Y(gamma,pi))',
                'c': f'-{u}*beta',
                'rho': f'-b/{u}',
            },
            'source_necessary_rows': [
                'b*beta-1',
                'all coefficient rows of J_XY(F,G)-1',
                'all negative-gamma Laurent coefficient rows of both substituted polynomials',
                f'all coefficient rows above pi-degree {int(np)} for F and {int(mp)} for G',
            ],
            'receiver_generator_pullback': 'chain rule plus explicit negative/high Laurent coefficient cofactors; not invariant matching',
            'receiver_emptiness': 'NONEMPTY',
            'receiver_nonempty_control': {
                'P': 'pi', 'Q': f'pi+gamma^{ell+1}',
                'c': -(ell+1), 'rho': str(-Fraction(1,ell+1)),
            },
        },
        'complementary_source_branch': {
            'hypothesis': f'delta_star_(s-1) < {v}/{u}',
            'status': 'UNASSIGNED_SPLIT_OBLIGATION',
            'reason': 'Moh Proposition 6.4 automatic radius applies only to u_s=1; every cohort row has u_s>=2',
        },
        'source_emptiness_from_this_atlas': False,
    }
    assert v*n >= ell+1 and v*m >= ell+1
    assert int(np) >= 1 and int(mp) >= 1
    return record


OUT.mkdir(parents=True, exist_ok=True)
read_paths = []
prior = read_json('box/ideation-astra-20260905/cohort/cohort-compression.json')
provenance = read_json('box/h1nonres-20260903/summary.json')
source_path = ROOT / 'box/xufloor-20260903/results.json'
source_digest = digest(source_path)
assert source_digest == provenance['provenance']['screen_snapshot']['sha256']
assert source_digest == prior['source_sha256']
source = read_json('box/xufloor-20260903/results.json')
us1 = [r for r in source['rows'] if r['phase']=='us_eq_1']
assert len(us1)==1110 and all(r['u_s']==1 for r in us1)
us1_audit = {
    'source_path': str(source_path), 'source_sha256': source_digest,
    'cohort': 'all snapshot rows with phase=us_eq_1; before the stored Xu boolean filter',
    'rows': len(us1),
    'ell_histogram': histogram(r['V_s']-r['u_s']-1 for r in us1),
    'ell1_rows': sum(r['V_s']-r['u_s']-1==1 for r in us1),
    'fable_671_over_1110_reproduced': True,
    'screened_variants': {},
}
assert us1_audit['ell1_rows']==671
for screen in ['xu_ok_promoted','xu_ok_candidate']:
    variant=[r for r in us1 if r[screen]]
    us1_audit['screened_variants'][screen]={
        'rows':len(variant),
        'ell_histogram':histogram(r['V_s']-r['u_s']-1 for r in variant),
        'ell1_rows':sum(r['V_s']-r['u_s']-1==1 for r in variant),
    }
(OUT/'us1-residue-audit.json').write_text(json.dumps(us1_audit,indent=2)+'\n')
spec = importlib.util.spec_from_file_location('frozen_moh_skeleton', FROZEN/'moh_skeleton_full.py')
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)
rows = [r for r in source['rows'] if r['phase']=='us_gt_1' and r['xu_ok_candidate']]
assert len(rows)==296
assert sorted(r['row_key'] for r in rows)==prior['selected']['original_keys']
records = [source_interface(r) for r in rows]
groups = collections.defaultdict(list)
for record in records:
    groups[tuple(record['conditional_descendant']['coarse_key'])].append(record)
assert len(groups)==132
for old_group in prior['selected']['quadruple_members']:
    new_group = groups[tuple(old_group['key'])]
    assert sorted(r['row_key'] for r in new_group)==old_group['original_keys']
key_records = [{
    'coarse_key': list(key), 'source_count': len(members),
    'row_keys': sorted(r['row_key'] for r in members),
    'literal_wedge_k1': 'UNASSIGNED',
    'broad_receiver_on_licensed_radius_branch': 'ASSIGNED_WITH_COEFFICIENT_MAP',
    'complementary_split_branches': 'UNASSIGNED',
    'descendant_exponent_is_one': key[2]==1,
    'common_broad_receiver': {
        'P_gamma_degree': max(r['source']['v_s']*r['source']['n'] for r in members),
        'Q_gamma_degree': max(r['source']['v_s']*r['source']['m'] for r in members),
        'P_pi_degree': key[0], 'Q_pi_degree': key[1], 'ell': key[2],
        'ring_generator_order': 'c,rho,p_ij lex(i,j),q_ij lex(i,j), all i,j in the declared support rectangles',
        'coefficient_field': 'QQ',
        'ideal': 'all gamma,pi coefficients of J(P,Q)-c*gamma^ell; c*rho-1',
        'localization': 'c is invertible through rho; source b is invertible through beta',
        'exact_pi_degrees_or_monicity_imposed': False,
        'support_completeness': 'rectangles enlarge the full substituted supports; no inherited decoration is identified',
    },
} for key,members in sorted(groups.items())]
for key_record in key_records:
    for record in groups[tuple(key_record['coarse_key'])]:
        record['licensed_radius_branch']['receiver_common_coarse_key']=key_record['coarse_key']
        record['licensed_radius_branch']['receiver_common_support_caps']=key_record['common_broad_receiver']
        record['licensed_radius_branch']['source_ring_generator_order']=(
            'b,beta,e,a_0,...,a_(v-1),f_rs lex(r,s) with r+s<=n,g_rs lex(r,s) with r+s<=m'
        )
        record['licensed_radius_branch']['source_chart_kind']=(
            'NEW_NECESSARY_OVERAPPROXIMATION; no existing terminal coefficient chart is identified'
        )

pilots=[]
for record in records:
    r=record['source']
    if (r['n'],r['m'],r['M2_to_Ms'],r['V']) in [
        (126,84,[-14,63,124],{'2':5,'3':10,'4':5}),
        (126,84,[112,119,124],{'2':5,'3':10,'4':5}),
        (144,120,[132,138,142],{'2':5,'3':5,'4':4}),
    ]:
        pilots.append(record)
assert len(pilots)==3

summary={
    'scope':'Measured auxiliary sharpened cohort, not newly promoted universal census; maps licensed by radius branch only',
    'source_rows':len(rows), 'coarse_keys':len(groups),
    'literal_wedge_k1_certified_keys':0, 'literal_wedge_k1_UNASSIGNED_keys':132,
    'literal_wedge_k1_certified_rows':0, 'literal_wedge_k1_UNASSIGNED_rows':296,
    'broad_receiver_licensed_branch_certified_keys':132,
    'broad_receiver_licensed_branch_certified_rows':296,
    'complementary_split_UNASSIGNED_rows':296,
    'source_rows_killed':0,
    'ell_histogram_keys':histogram(k[2] for k in groups),
    'ell_histogram_rows':histogram(r['conditional_descendant']['ell'] for r in records),
    'ell1_rows':sum(r['conditional_descendant']['ell']==1 for r in records),
    'ell1_keys':sum(k[2]==1 for k in groups),
    'ell1_uv_histogram':{
        str(k):v for k,v in sorted(collections.Counter(
            (r['source']['u_s'],r['source']['v_s']) for r in records
            if r['conditional_descendant']['ell']==1).items())
    },
    'source_snapshot_sha256':source_digest,
    'exact_controls':{
        'membership_matches_previous_296_row_audit':True,
        'all_132_keys_and_members_match_previous_audit':True,
        'all_296_rows_pass_frozen_skeleton_conditions_7_to_13':True,
        'all_ds_equal_u_plus_v_and_terminal_delta_minus_one':True,
        'all_broad_receiver_nonempty_controls_fit_support':True,
        'all_source_and_receiver_denominators_declared':True,
    },
}
for name,value in [('inventory.json',{'summary':summary,'keys':key_records,'sources':records}),
                   ('summary.json',summary),('pilot-interfaces.json',pilots)]:
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n')
read_paths.extend(ROOT/p for p in [
    'box/ideation-astra-20260905/cohort/cohort_compression.py',
    'box/ideation-astra-20260905/cohort/README.md',
    'box/ideation-astra-20260905/cohort/SHA256SUMS',
])
(OUT/'new-read-inputs.sha256').write_text(''.join(f'{digest(p)}  {p}\n' for p in sorted(set(read_paths))))
print(json.dumps(summary,indent=2))
