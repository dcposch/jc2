#!/usr/bin/env python3
"""Audit every explicit leading homogeneous row of the production circuits."""
import hashlib,json,math,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
def audit(path,k):
    target=55 if k==33 else 63;power=15 if k==33 else 14
    leader=f'leader{target}';inverse=f'Z{target}'
    text=path.read_text();body=text.split('ideal I=\n',1)[1].split(';\nprint("ALL_ROWS_PARSED")',1)[0]
    rows=body.split(',\n');metadata=json.loads(path.with_suffix('.circuit.json').read_text())
    counts=metadata['counts'];assert len(rows)==sum(counts.values())
    start=len(rows)-counts['Q']-counts['localizers'];stop=len(rows)-counts['localizers']
    leaders=[(i,row) for i,row in enumerate(rows) if re.search(r'\b'+leader+r'\b',row)]
    unit=[(i,row) for i,row in leaders if re.search(r'\b'+inverse+r'\b',row)]
    assert len(unit)==1 and unit[0][1]==f'({inverse}*{leader}-1)'
    face=[(i,row) for i,row in leaders if not re.search(r'\b'+inverse+r'\b',row)]
    assert len(face)==power+1
    values=[]
    for i,row in face:
        assert start<=i<stop and row.count(leader)==1
        m=re.search(r'\+\(-1\)\*\(\(([0-9]+)\)\*'+leader+r'\)\)$',row)
        assert m,(path,i,row[-150:]);values.append(int(m[1]))
    assert values==[math.comb(power,j) for j in range(power+1)]
    assert [i for i,row in face]==list(range(stop-power-1,stop))
    return {'script':str(path),'script_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'target_degree':target,'normalizer':6*k-2,'target_depth':6*k-2-target,
        'whole_target':f'lambda*z^{40 if k==33 else 49}*(1+z)^{power}',
        'all_leader_occurrences_accounted_for':True,'all_binomial_coefficients_subtracted':values,
        'no_leader_in_source_or_graph_rows':True,'unit_row_retained':True,'result':'PASS'}
def main():
    cases=[(p,33) for p in sorted((HERE/'g9966/circuit-runs').glob('*/augmented.sing'))]
    cases +=[(p,36) for p in sorted((HERE/'d108').glob('d108_circuit_stage*_translated_strongfront.sing'))]
    cases +=[(p,36) for p in sorted((HERE/'d108').glob('d108_meanfree_circuit_stage*_strongfront.sing'))]
    records=[audit(p,k) for p,k in cases if p.with_suffix('.circuit.json').exists()]
    out={'result':'PASS','circuits_checked':len(records),'records':records,
      'source_necessity':'Moh Prop4.5 p169 and p172 proof; actual y-degree Prop2.2 p152',
      'scope':'emitted production circuits only; no solver verdict inferred'}
    (HERE/'target-subtraction-audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('Full target subtraction:',len(records),'circuits PASS')
if __name__=='__main__':main()
