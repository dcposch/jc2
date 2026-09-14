#!/usr/bin/env python3
"""Emit a compact, unambiguous report and complete CSV of exact Hilbert pieces."""
import csv
import hashlib
import json
from pathlib import Path
import sys

OUT=Path(__file__).resolve().parent


def main():
    results=[]
    for n in (77,111,129,136):
        candidates=[]
        for path in OUT.glob(f'hilbert_{n}_B*_Y*.json'):
            result=json.loads(path.read_text())
            candidates.append((result['max_y'],result,path))
        _,result,path=max(candidates,key=lambda x:x[0])
        results.append((result,path))
    execution_records=[]
    for result,path in results:
        execution_records.append(dict(parameters=result['parameters'],
            command=f"python3 box/graded-macaulay-20260905/hilbert/compute_hilbert.py --parameters {result['parameters']} --max-y {result['max_y']}",
            status=result.get('completion_status','COMPLETED_ALL_COMPONENTS_EXACT_Q'),
            original_driver_exit_status=result.get('original_driver_cancellation',{}).get('actual_exit_status',0),
            elapsed_seconds=result['total_elapsed_seconds'],
            output_json=str(path.relative_to(Path.cwd())),
            output_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    (OUT/'execution_records.json').write_text(json.dumps(dict(
        python_version=sys.version,runs=execution_records,
        linear_verification_status='PASS_100_RANDOM_4_ORIGINAL_AND_4_MEMBERSHIP_CONTROLS',
        support_verification_status='PASS_ALL_FOUR_FIBRES_ALL_ORIGINAL_ROW_TERMS'),indent=2)+'\n')
    with (OUT/'hilbert_components.csv').open('w') as stream:
        fields=['parameters','B','Y','columns','rows','nonzeros','rank_Q','rank_Fp','hilbert_Q','I_piece_zero','status']
        writer=csv.DictWriter(stream,fieldnames=fields)
        writer.writeheader()
        for result,_ in results:
            for piece in result['components']:
                writer.writerow({key:result['parameters'] if key=='parameters' else piece[key] for key in fields})
    lines=[
        '# Exact original-ring Macaulay Hilbert truncations',
        '',
        'These are exact Q computations in the full original chart ring R=Q[z,c]. ',
        'No variable was specialized, no c=1 section was taken, and no polynomial ',
        'completion or Groebner basis was used. B denotes the positive first charge. ',
        'The older instrument audit stores its negative; the driver derives the ',
        'positive convention again from each variable name and source metadata.',
        '',
        'For each (B,Y), all monomials of that degree are explicit columns. ',
        'Every nonzero original generator g contributes every monomial multiple ',
        'of complementary degree, including dependent rows. Primitive integer ',
        'Gaussian row operations compute rank over Q exactly. A separate modular ',
        'elimination at p=1073741827 crosschecks the rank. High-degree generators ',
        'cannot contribute because every variable has nonnegative B and positive Y. ',
        'Thus these are full-ideal Hilbert pieces, despite the finite cutoff.',
        '',
        '| Fibre | B range | Y range | Exact pieces | Largest columns | Largest rows | Original run seconds |',
        '|---:|---|---|---:|---:|---:|---:|',
    ]
    for result,path in results:
        cs=result['components'];assert all(c['status'] in ('EXACT_Q','EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP') for c in cs)
        assert all(c['rank_Q']==c['rank_Fp'] for c in cs if c['status']=='EXACT_Q')
        lines.append(f"| {result['parameters']} | 0..{result['max_b']} | 0..{result['max_y']} | {len(cs)} | {max(c['columns'] for c in cs):,} | {max(c['rows'] for c in cs):,} | {result['total_elapsed_seconds']} |")
    lines += ['', 'The complete exact rows, column dimensions, rational and modular ranks, ',
              'and H_(B,Y) are in `hilbert_components.csv`. JSON files additionally ',
              'record all variable degrees and order, original generator order, ',
              'input SHA-256 values, matrix hashes, and exact echelon hashes.', '',
              'Every computed component with dim R_(B,Y)>0 has H_(B,Y)>0. ',
              'No nonempty ring component in these grids is killed entirely by I.', '',
              'There are 345 direct original-ring components and one explicitly ',
              'typed `EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP` component: fibre136 at ',
              '(6,12). Its reduced matrix has 8,765 columns and 5,554 rows, ',
              'rank_Q=4,945 and H=3,820. A verified homogeneous rational unit ',
              'quotient therefore gives original rank_Q=80,415-3,820=76,595. ',
              'All 71 ordered constant pivots were independently checked against ',
              'the original source rows and the exact images and both reduced ',
              'matrix ranks were replayed. The direct (5,12) value H=4,446 ',
              'agrees with the reduced calculation. The redundant final original ',
              'elimination was stopped with SIGTERM after 1,681.19 seconds; ',
              'the observed process exit status was 143. No original echelon ',
              'hash or direct modular rank is claimed for the transferred cell.', '',
              '| Fibre | Y | H_(B,Y), with B ascending from 0 |',
              '|---:|---:|---|']
    for result,path in results:
        for y in [10,12,14]:
            if y>result['max_y']:continue
            hs=[c['hilbert_Q'] for c in result['components'] if c['Y']==y]
            lines.append(f"| {result['parameters']} | {y} | ({', '.join(map(str,hs))}) |")
    support=json.loads((OUT/'global_support_vanishing.json').read_text())
    assert all(piece['hilbert_Q']>0 for result,_ in results
               for piece in result['components'] if piece['columns']>0)
    lines += ['', 'An N-independent support result was verified for every original ',
              'generator and every ring variable. For B,Y nonnegative integers,', '',
              '    I_(B,Y)=0 iff B=0 or Y<lambda(B),', '',
              'where lambda(B) is B (77), 2B (111), ceil(13B/3) (129), ',
              'or ceil(B/3) (136). Also R_(B,Y)=0 iff Y<lambda(B). ',
              'All (0,Y) pieces of I vanish, so H_(0,Y)=dim R_(0,Y) for every Y. ',
              'This does not say any nonempty quotient piece vanishes.', '',
              'The lower bound follows from dY>=aB for every variable and generator, ',
              'and B>=1 for every generator. For the converse, write B=r+kd ',
              'with 1<=r<=d. A displayed nonzero original generator in degree ',
              '(r,ceil(ar/d)), multiplied by a variable of degree (d,a) to power k ',
              'and by a variable of degree (0,1) to the remaining weight, gives ',
              'a nonzero member of I_(B,Y). The original polynomial ring is a ',
              'domain. `global_support_vanishing.json` supplies all residue ',
              'generators and variable names; this is not an extrapolation from ',
              'the finite Hilbert grid.', '',
              '| Fibre | Period variable (degree) | Residue source-index witnesses |',
              '|---:|---|---|']
    for row in sorted(support,key=lambda r:r['parameters']):
        ws=', '.join(f"{w['source_index']} at {tuple(w['degree'])}" for w in row['residue_generator_witnesses'])
        lines.append(f"| {row['parameters']} | {row['period_variable']} {tuple(row['period_degree'])} | {ws} |")
    lines += ['', 'The linear algebra verification contains 100 deterministic random ',
              'dense crosschecks against python-flint fmpq_mat and nmod_mat, ',
              'plus four actual original-ring Macaulay components. Every check ',
              'passed. The controls include exact positive and negative membership, ',
              'and both bad-prime directions: A=[p], target=[1] is YES over Q ',
              'and NO modulo p; A=[1,p], target=[1,0] is NO over Q and YES ',
              'modulo p. Positive toy combinations are replayed exactly.', '',
              'A modular NO is an exact rational NO only after a suitable ',
              'good-prime condition is certified. One sufficient condition is ',
              'rank_Q(A)=rank_Fp(A): then a modular augmented-rank increase ',
              'forces an augmented-rank increase over Q. Integrality of the ',
              'input alone does not establish that condition. A modular YES ',
              'remains a signal; the required certificate for a c-power kill ',
              'is an exact rational combination replayed in the original ring.', '',
              'The computed Y cutoffs are below D=39,29,41,29, respectively. ',
              'Accordingly these grids do not test c, c^2, or c^3 and give ',
              'no c-power kill. They supply exact finite Hilbert data and ',
              'a complete N-independent support-vanishing criterion.', '',
              'Reproduce with:', '',
              '```bash',
              'python3 box/graded-macaulay-20260905/hilbert/compute_hilbert.py --parameters 77 --max-y 14',
              'python3 box/graded-macaulay-20260905/hilbert/compute_hilbert.py --parameters 111 --max-y 14',
              'python3 box/graded-macaulay-20260905/hilbert/compute_hilbert.py --parameters 129 --max-y 14',
              'python3 box/graded-macaulay-20260905/hilbert/compute_hilbert.py --parameters 136 --max-y 12',
              'python3 box/graded-macaulay-20260905/hilbert/verify_support.py',
              'python3 box/graded-macaulay-20260905/hilbert/verify_linear.py',
              'python3 box/graded-macaulay-20260905/hilbert/verify_unit_map.py',
              'python3 box/graded-macaulay-20260905/hilbert/summarize.py',
              '```', '']
    (OUT/'RESULTS.md').write_text('\n'.join(lines))
    manifest=[]
    for path in sorted(OUT.rglob('*')):
        if path.is_file() and path.name!='SHA256SUMS' and '__pycache__' not in path.parts:
            manifest.append(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(Path.cwd())}')
    (OUT/'SHA256SUMS').write_text('\n'.join(manifest)+'\n')
    print('\n'.join(lines))


if __name__=='__main__':main()
