#!/usr/bin/env python3
"""Finish the 136 grid using one explicitly typed exact quotient component."""
import hashlib
import json
from pathlib import Path
from compute_hilbert import OUT,PROFILES,INSTRUMENT,parse_rows


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    proof_path=OUT/'unit_map_verification.json';proof=json.loads(proof_path.read_text())
    assert proof['status']=='EXACT_HOMOGENEOUS_UNIT_QUOTIENT_VERIFIED_AND_RANKS_REPLAYED'
    assert sha(proof['input_path'])==proof['input_sha256']
    assert sha(proof['mapping_path'])==proof['mapping_sha256']
    assert sha(proof['replay_path'])==proof['replay_sha256']
    cancellation=json.loads((OUT/'original_driver_cancellation.json').read_text())
    assert cancellation['actual_exit_status']==143
    direct=[]
    for line in (OUT/'hilbert_136_Y12.log').read_text().splitlines():
        # Shell's own SIGTERM notice can follow the last JSON row.
        if not line.startswith('{'):continue
        row=json.loads(line);assert row.pop('parameters')==136
        assert row['status']=='EXACT_Q';direct.append(row)
    expected={(b,y) for b in range(7) for y in range(13)}
    assert len(direct)==90 and {(r['B'],r['Y']) for r in direct}==expected-{(6,12)}
    output=json.loads((OUT/'hilbert_136_B6_Y10.json').read_text())
    profile=next(p for p in json.loads(PROFILES.read_text()) if p['parameters']==136)
    audit=json.loads((INSTRUMENT/(profile['stem']+'_audit.json')).read_text())
    names,degrees,rows,terms=parse_rows(profile,audit)
    assert output['variable_order']==names
    counts=[[0]*13 for _ in range(7)];counts[0][0]=1
    for b,y in degrees:
        for B in range(b,7):
            for Y in range(y,13):counts[B][Y]+=counts[B-b][Y-y]
    row_count=nonzeros=0
    for row in rows:
        b,y=row['degree']
        if b<=6 and y<=12:
            multipliers=counts[6-b][12-y]
            row_count+=multipliers;nonzeros+=multipliers*len(row['terms'])
    assert counts[6][12]==80415 and row_count==146269
    reduced=json.loads(Path(proof['input_path']).read_text())
    rr=next(r for r in reduced['components'] if (r['B'],r['Y'])==(6,12))
    assert rr['hilbert_Q']==3820 and rr['rank_Q']==4945
    last=dict(B=6,Y=12,columns=80415,rows=row_count,nonzeros=nonzeros,
              rank_Q=80415-3820,rank_Fp=None,prime=1073741827,
              hilbert_Q=3820,I_piece_zero=False,
              status='EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP',
              original_matrix_rank_computed_directly=False,
              original_echelon_sha256=None,
              original_modular_rank_claimed=False,
              reduced_columns=rr['reduced_columns'],reduced_rows=rr['reduced_rows'],
              reduced_rank_Q=rr['rank_Q'],reduced_rank_Fp=rr['rank_Fp'],
              reduced_matrix_sha256=rr['matrix_sha256'],
              reduced_exact_echelon_sha256=rr['exact_echelon_sha256'],
              proof_path=str(proof_path),proof_sha256=sha(proof_path),
              method='Homogeneous exact Q unit quotient isomorphism preserves H; original rank = original columns - H',
              elapsed_seconds=rr['elapsed_seconds'])
    direct.append(last)
    output.update(max_y=12,components=direct,
                  total_elapsed_seconds=cancellation['observed_elapsed_seconds'],
                  direct_components=90,exact_unit_map_components=1,
                  original_driver_cancellation=cancellation,
                  algorithm='90 original-ring exact primitive-integer row eliminations; one exact rank via verified homogeneous rational unit-quotient isomorphism',
                  completion_status='ALL_91_COMPONENTS_EXACT_Q_WITH_ONE_UNIT_MAP_TRANSFER',
                  finalization_driver_sha256=sha(__file__),
                  no_specialization=True,no_groebner_completion=True)
    target=OUT/'hilbert_136_B6_Y12.json';target.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(path=str(target),sha256=sha(target),last_component=last),indent=2))


if __name__=='__main__':main()
