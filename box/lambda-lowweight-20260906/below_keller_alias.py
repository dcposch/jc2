#!/usr/bin/env python3
"""Exact target bounds when Tc-ss^(n+m) lies above the positive cutoff."""
import json
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
count=0
for case in json.loads((HERE/'run_cases.json').read_text()):
    for N in (1,2,3):
        B=N*case['W']+3
        if B>=case['n']+case['m']:continue
        source=HERE/f'{case["id"]}.charge0.N{N}.json'
        d=json.loads(source.read_text())
        assert d['run_complete'] and d['nf_is_query']==1 and d['basis_size']==1
        out={'case':case['id']+'.keller','N':N,'W':case['W'],'cutoff':B,
             'status':'EXACT_TARGET_BOUND_BELOW_KELLER_ROW','source_receipt':source.name,
             'completed_homogeneous_weight':B,'keller_row_weight':case['n']+case['m'],
             'keller_row_selected':False,'keller_localizer':True,
             'coefficient_field':'Q','new_variable':'T of positive weight 1',
             'proof':'Tc-ss^(n+m) has degree greater than B. Positive-degree multipliers cannot use it through B. Adjoining the unused T preserves target membership. The charge-zero component of the remaining ideal is the principal actual-leader localizer tested in the source receipt.',
             'map':'Original variables, Z and ss map identically; T is adjoined freely.',
             'jacobian_rows_sha256':d['rows_sha256'],'lambda_sha256':d['lambda_sha256'],
             'component_std_done':True,'full_std_done':False,'std_done':False,
             'wall_seconds':0,'peak_rss_bytes':None,
             'source_normal_form':'ss^B','claim_scope':'No homogeneous unit certificate of weight at most B; no survivor or attainment claim.'}
        runner.persist_small(HERE/f'{case["id"]}.keller.N{N}.json',json.dumps(out,indent=2)+'\n')
        count+=1
print('BELOW_KELLER_TARGET_BOUNDS='+str(count))
