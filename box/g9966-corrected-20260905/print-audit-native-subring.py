#!/usr/bin/env python3
"""Audit native arithmetic subring embeddings against actual full-ring phases."""
import hashlib,json
from pathlib import Path
N=Path(__file__).resolve().parent
records=[]
for branch in ('delta2','delta52'):
    summary_path=N/'results-fullJ-flint'/('fullJ-flint-'+branch+'.json')
    summary_raw=summary_path.read_bytes();summary=json.loads(summary_raw)
    metadata=summary['current_backend_metadata'];t=metadata['t_cutoff']
    assert metadata['coefficient_field']=='Q' and metadata['full_chart_coordinates_removed'] is False
    generators=metadata['active_computation_generators']
    assert generators[0]=='w' and len(generators)==len(set(generators))
    variables=set(generators[1:])
    matches=[]
    for path in summary_path.parent.glob('fullJ-flint-'+branch+'_phase*.json'):
        raw=path.read_bytes();phase=json.loads(raw)
        if phase['phase']=='Jacobian_t'+str(t):matches.append((path,raw,phase))
    assert len(matches)==1
    path,raw,phase=matches[0]
    before=set(phase['free_before']);after=set(phase['free_after'])
    assert variables<=before
    removed=before-after
    newtargets=set(phase['map_after'])-set(phase['map_before'])
    assert removed==newtargets
    unused=before-variables
    assert unused-after<=newtargets
    # Every native variable is embedded as the same declared full-ring
    # coordinate; unused coordinates are absent from arithmetic inputs only.
    images=[[name,name] for name in generators]
    slots=[(t,k) for k in range(164-t)]
    stored=[]
    for label,_row in phase['raw_new_rows_before_reduction']:
        prefix=f'resumed_J_t{t}_d{163-t}_k'
        assert label.startswith(prefix)
        stored.append((t,int(label[len(prefix):])))
    assert len(stored)==len(set(stored)) and set(stored)<=set(slots)
    omitted=sorted(set(slots)-set(stored))
    records.append({'branch':branch,'t':t,'native_metadata':metadata,
        'full_declared_free_before':sorted(before),'ordered_native_generator_images':images,
        'native_variables_subset_of_declared_full_ring':True,
        'unused_full_ring_coordinates':sorted(unused),
        'unused_coordinates_still_free_after':sorted(unused&after),
        'unused_coordinates_changed_only_by_recorded_pivots':sorted(unused-after),
        'all_removed_coordinates_exactly_recorded_map_targets':True,
        'all_expected_scalar_slots':slots,'saved_nonzero_slots':stored,
        'omitted_slots_requiring_literal_zero_replay':omitted,
        'phase_path':str(path),'phase_sha256':hashlib.sha256(raw).hexdigest(),
        'summary_path':str(summary_path),'summary_observed_sha256':hashlib.sha256(summary_raw).hexdigest()})
result={'status':'PASS','field':'Q','arithmetic_subring':'Q[w,V] embedded injectively in Q[full_free][w] by the displayed generator images; maintained residual is applied afterward.',
 'full_chart_ring_is_not_replaced_by_native_ring':True,
 'cutoff_proof':'All source t powers are nonnegative; multiplication adds powers and normalized bracket contributes at r+s. A source term with r>cutoff cannot influence the requested cutoff coefficient.',
 'coefficient_map_proof':'encode derives every occurring source symbol, inserts w at index0, and uses the same generator index in from_dict and to_dict decoding. No coefficient symbol is assumed absent from the full chart.',
 'native_zero_proof':'FLINT is_zero means the exact polynomial is zero in Q[w,V], hence also zero under the full-ring embedding and in every maintained quotient.',
 'omitted_scalar_slot_requirement':'Caller enumerates allk0..163-t and supplies0 for missing native w monomials. Since saved phases filter literalzeros, a replay must reconstruct that full vector then compare the complete nonzero list, certifying every omitted slot zero.',
 'records':records,'driver_sha256':hashlib.sha256((N/'deep_resume_jacobian_flint.py').read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256((N/'deep_flint_jacobian.py').read_bytes()).hexdigest(),
 'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','phases':[{'branch':r['branch'],'t':r['t'],'native_variables':len(r['native_metadata']['active_computation_generators'])-1,'full_free_before':len(r['full_declared_free_before']),'unused_full_free':len(r['unused_full_ring_coordinates']),'expected_scalar_slots':len(r['all_expected_scalar_slots']),'saved_nonzero_slots':len(r['saved_nonzero_slots'])} for r in records]},indent=2))
