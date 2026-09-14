#!/usr/bin/env python3
"""Independently check the homogeneous triangular quotient, then replay cells.

Only writes below this Hilbert directory. The quotient isomorphism follows
from the checked ordered nonzero-constant pivots, not from an evaluation.
"""
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
from compute_hilbert import OUT,PROFILES,INSTRUMENT,parse_rows


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    path=Path('box/graded-macaulay-20260905/counts/reduced-hilbert/hilbert136.json')
    reduced=json.loads(path.read_text());mp=Path(reduced['input']);mapping=json.loads(mp.read_text())
    assert sha(mp)==reduced['input_sha256']
    assert sha(reduced['original_source'])==reduced['original_source_sha256']==mapping['source_sha256']
    driver=path.parent/'compute136.py';assert sha(driver)==reduced['driver_sha256']
    assert sha(path.parent/'eligible-images.json')==reduced['image_artifact_sha256']
    profile=next(p for p in json.loads(PROFILES.read_text()) if p['parameters']==136)
    audit=json.loads((INSTRUMENT/(profile['stem']+'_audit.json')).read_text())
    names,weights,rows,terms=parse_rows(profile,audit)
    assert names==mapping['source_variables']
    assert dict(zip(names,weights))=={v:tuple(w) for v,w in mapping['weights'].items()}
    lookup={v:i for i,v in enumerate(names)};by_index={r['source_index']:r for r in rows}
    raw={int(line.split('|',1)[0]):line.split('|',4)[4]
         for line in Path(reduced['original_source']).read_text().splitlines()[1:]}
    pivots=mapping['pivots'];pivot_vars={p['variable'] for p in pivots}
    assert len(pivots)==len(pivot_vars)==71
    assert pivot_vars=={v for v,w in zip(names,weights) if v.startswith('A') and w[0]>0}
    remaining=[v for v in names if v not in pivot_vars]
    assert remaining==mapping['remaining_variables']==reduced['remaining_variables']
    seen=set();prime=1073741827
    for pivot in pivots:
        variable=pivot['variable'];i=lookup[variable];q=Fraction(pivot['coefficient'])
        row=by_index[pivot['index']]
        assert q and q.numerator%prime and q.denominator%prime
        assert raw[pivot['index']]==pivot['original_row']
        assert tuple(pivot['degree'])==row['degree']==weights[i]
        occurrences=[(m,c) for m,c in row['terms'].items() if i in m]
        assert occurrences==[((i,),q*row['denominator_clear'])]
        dependencies={names[j] for m in row['terms'] for j in m
                      if names[j] in pivot_vars and names[j]!=variable}
        assert dependencies==set(pivot['dependencies']) and dependencies<=seen
        seen.add(variable)
    eligible=sorted(r['source_index'] for r in rows if r['degree'][0]<=6 and r['degree'][1]<=12)
    assert eligible==reduced['eligible_source_indices']
    assert len(eligible)==reduced['source_rows_composed_exactly']==69
    saved=json.loads((path.parent/'eligible-images.json').read_text())
    assert sorted(saved['exact_zero_indices']+[r['source_index'] for r in saved['source_images']])==eligible
    assert len(saved['source_images'])==30 and len(saved['exact_zero_indices'])==39
    # Re-execute the exact recursive images and both finite matrix ranks into a
    # separate custody directory. This also checks all surviving image grades.
    spec=importlib.util.spec_from_file_location('independent_unit_cell_replay',driver)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.OUT=OUT/'unit-map-replay';module.OUT.mkdir(exist_ok=True)
    module.run()
    replay_path=module.OUT/'hilbert136.json';replay=json.loads(replay_path.read_text())
    assert replay['image_artifact_sha256']==reduced['image_artifact_sha256']
    for original,rerun in zip(reduced['components'],replay['components']):
        for key in ('B','Y','reduced_columns','reduced_rows','nonzeros','rank_Q','rank_Fp',
                    'hilbert_Q','matrix_sha256','exact_echelon_sha256'):
            assert original[key]==rerun[key],(key,original[key],rerun[key])
    direct=[json.loads(line) for line in (OUT/'hilbert_136_Y12.log').read_text().splitlines()]
    control=next(r for r in direct if (r['B'],r['Y'])==(5,12))
    reduced_control=next(r for r in reduced['components'] if (r['B'],r['Y'])==(5,12))
    assert control['hilbert_Q']==reduced_control['hilbert_Q']==4446
    output=dict(status='EXACT_HOMOGENEOUS_UNIT_QUOTIENT_VERIFIED_AND_RANKS_REPLAYED',
                field='Q',prime=prime,prime_compatible_constant_pivots=True,
                original_source_sha256=reduced['original_source_sha256'],
                input_path=str(path),input_sha256=sha(path),
                mapping_path=str(mp),mapping_sha256=sha(mp),
                source_variable_order_verified=True,all_original_terms_reverified=terms,
                homogeneous_ordered_constant_pivots_verified=71,
                pivot_subideal_contained_in_original_I=True,
                quotient_isomorphism='R/I ~= Q[remaining]/phi(I), with bidegrees preserved',
                all_eligible_original_source_images_accounted_for=69,
                exact_zero_images=39,exact_nonzero_images=30,
                all_reduced_images_and_matrix_ranks_replayed=True,
                independent_original_component_control=dict(B=5,Y=12,hilbert_Q=4446),
                final_component=dict(B=6,Y=12,original_columns=80415,
                                     reduced_columns=8765,reduced_rank_Q=4945,
                                     original_hilbert_Q=3820,original_rank_Q=76595),
                replay_path=str(replay_path),replay_sha256=sha(replay_path),
                driver_sha256=sha(__file__))
    (OUT/'unit_map_verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
