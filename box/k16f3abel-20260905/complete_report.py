#!/usr/bin/env python3
"""Record completed outcomes and fill report status sections; never seals."""
from datetime import datetime, timezone
import json
from pathlib import Path

root=Path(__file__).resolve().parent
workspace=root.parent.parent
receipt=dict(line.split('=',1) for line in
    (workspace/'xmodel/k16-f3abel-astra-20260905.run.v2').read_text().splitlines() if '=' in line)
full=json.loads((root/'controls_t8_guided.log').read_text())
slice_result=json.loads((root/'slice_t8_guided.log').read_text())
for result in (full,slice_result):
    assert result['verdict']=='INCONCLUSIVE_TIMEOUT', 'A different result needs mathematical review.'
    assert result['certificate']['accepted_run_count']==0
    run=result['certificate']['runs'][0]
    assert run['timed_out'] and run['main']['dimension'] is None

status=r'''The direct t=8 reconstruction was generated afresh modulo p=32003,
at d=31750 (so d^2=3), equivalently y=11288. All sixteen w pivots and
the B pivot were nonzero. The leading and automatic low rows passed.
The fifteen residuals were checked monomial by monomial for weights
32,31,...,18 in the ring with variable weights (1,2,3,4,5,6,7,9).
The reconstructed B, eta, and product have weights 17,16,33. All rows
vanish at the origin. Independent positive dimension-zero and negative
positive-dimensional controls passed before the main basis calls.

Two one-core foreground jobs used the frozen guided_gb policy and
fixed wall timeouts. Their completed outcomes are:

| homogeneous ideal in R_8 modulo p | wall limit | completed outcome |
|---|---:|---|
| J_8=(E2,...,E16) | 1800 seconds | INCONCLUSIVE_TIMEOUT |
| J_8+(b), the b=0 slice | 900 seconds | INCONCLUSIVE_TIMEOUT |

Both stopped inside the standard-basis computation. Neither returned
an accepted basis or a dimension. The wrappers reaped the CAS
processes and returned typed timeout records; their wrapper exit
codes are not mathematical results. No t=8 full or slice assertion,
and no length or nilpotence assertion, is promoted from these runs.
The logs and complete guided result objects are saved in
`controls_t8_guided.log` and `slice_t8_guided.log`, with the emitted
scripts and captured stdout/stderr in their corresponding directories.
No predicted Hilbert series was used as a proof or a basis hint.

For a future successful replay, the exact promotion gate is as
follows. Work over the local domain obtained from Z[d]/(d^2-3) at
the prime (32003,d-31750), inverting the fixed scalar denominators,
y, and the actual high pivots. Their nonzero residues were checked,
so the modular direct recurrence is the reduction of the
characteristic-zero recurrence over this local domain. The rows are
homogeneous in positive weights, and the b=0 slice is homogeneous
as well. An accepted dimension-zero special fibre would have empty
weighted projectivization. The latter is proper over the local
domain: one may take a standard graded Veronese to see properness.
Its closed image could not contain the generic point while omitting
the closed point. Thus empty special projective fibre would imply
empty generic projective fibre and a zero-dimensional homogeneous
characteristic-zero cone. Extension to the algebraic closure covers
both embeddings of this irreducible quadratic field. This argument
would promote dimension zero only, not the measured modular length.

That antecedent did not occur in either completed run. In particular
no inhomogeneous Rabinowitsch ideal was tested modulo p and then
incorrectly promoted by this properness argument.'''

end=datetime.now(timezone.utc)
start=datetime.fromisoformat(receipt['start_utc'].replace('Z','+00:00'))
elapsed=(end-start).total_seconds()
assert elapsed<=180*60,elapsed
completion=(
    'All lane-owned CAS jobs have finished and been reaped. The two t=8 '
    'timeouts are recorded as inconclusive; all accepted exact controls and '
    'universal identity checks completed. Final mathematical review found no '
    'load-bearing gap in the stated partial results after the recorded '
    'notation corrections. The report was completed within the 180-minute '
    'budget and is sealed only after the artifact and process audit. '
    'Final verdict: PARTIAL; the all-t theorem remains OPEN.')
path=root/'report_remainder.md'
text=path.read_text()
assert text.count('COMPUTATION_STATUS_PENDING')==1
assert text.count('COMPLETION_STATUS_PENDING')==1
text=text.replace('COMPUTATION_STATUS_PENDING',status)
text=text.replace('COMPLETION_STATUS_PENDING',completion)
path.write_text(text)

outcomes={
    'lane':'k16-f3abel-astra-20260905',
    'verdict':'PARTIAL',
    'all_t_atom':'OPEN[K16-8.1-RADICAL]',
    'whole_ray_theorem_promoted':False,
    'full_cone_exact_controls':[
        {'t':2,'d':-1,'dimension':1,'length':None,'product_in_ideal':True},
        {'t':2,'d':1,'dimension':0,'length':12,'product_in_ideal':True},
        {'t':3,'field':'Q[d]/(3d^2-4)','dimension':0,'length':66,'product_in_ideal':False,'product_square_in_ideal':True},
        {'t':4,'field':'Q[d]/(3d^2-5)','dimension':0,'length':338,'product_in_ideal':False,'product_square_in_ideal':True}],
    'coincident_root_exact_slices':{'indices':[11,26,47],'both_split_factors':True,'all_b':True},
    't2_negative_control_correction':'B*eta is forced zero; V0 fails on the free b-axis.',
    't8_full':full,'t8_bzero':slice_result,
    'all_lane_jobs_finished':True,'final_audit_pass':False,
    'mathematical_reviews_passed':True,
    'core_limit':5,'cas_cores_per_job':1,
    'start_utc':receipt['start_utc'],'completion_utc':end.isoformat(),
    'elapsed_seconds':round(elapsed,3)}
(root/'run_outcomes.json').write_text(json.dumps(outcomes,indent=2)+'\n')
print(json.dumps({'verdict':'PARTIAL','elapsed_seconds':round(elapsed,3),'statuses_filled':True}),flush=True)
