#!/usr/bin/env python3
"""Render a compact report table from the preserved best-result index."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES = ['C70', 'C109', 'C127', 'C171', 'C341', 'C455',
         'R001', 'R002', 'R003', 'R004']


def code(record):
    if record is None:
        return '—'
    status = record.get('source_status') or record['status']
    if status == 'COMPLETE_TRUNCATED_NONUNIT':
        assert record['completed_homogeneous_weight'] == record['requested_cutoff']
        assert record['std_done'] and record['nf_is_zero'] == 0
        return 'C'
    if status == 'EXACT_TARGET_BOUND_BELOW_KELLER_ROW':
        assert record['completed_homogeneous_weight'] == record['requested_cutoff']
        return 'D'
    if status.startswith('OPEN_'):
        assert record['completed_homogeneous_weight'] is None
        return 'O'
    raise AssertionError((record['case'], record['N'], status))


def main():
    data = json.loads((HERE / 'best-results.json').read_text())
    records = {(r['case'], r['variant'], r['N']): r for r in data['records']}
    for case in CASES:
        for n in (1, 2, 3):
            assert (case, 'baseline', n) in records
            assert (case, 'Keller', n) in records
            assert code(records[case, 'charge0', n]) == 'C'
    lines = [
        'All **30 charge-zero target computations completed** at the listed B, with basis size 1 and `NF(s^B)=s^B`. The final replay took 19.193 seconds and peaked at 145.4 MiB; `chargezero-independent-audit.json` binds these target-component results.',
        '',
        'Cells list N=1,2,3: **C** = completed truncated nonunit at the listed B; **D** = exact target bound below the c-row, not a full basis; **O** = OPEN, no completed weight; **—** = no executed UX probe.',
        '',
        '| case | all-row baseline | with c-localizer | with c-localizer and UX |',
        '|---|---|---|---|',
    ]
    for case in CASES:
        cells = [','.join(code(records.get((case, variant, n))) for n in (1, 2, 3))
                 for variant in ('baseline', 'Keller', 'Keller+UX')]
        lines.append('| ' + case + ' | ' + ' | '.join(cells) + ' |')
    lines += [
        '',
        'R003 reuses the verified identical R002 presentation. `best-results.json` pins chosen receipts and their history; `run-summary.md` gives individual bounds, times, and memory. No class-unit certificate was obtained.',
    ]
    output = '\n'.join(lines) + '\n'
    (HERE / 'run-fragment.md').write_text(output)
    print(output)
    print('FRAGMENT_BYTES=' + str(len(output.encode())))


if __name__ == '__main__':
    main()
