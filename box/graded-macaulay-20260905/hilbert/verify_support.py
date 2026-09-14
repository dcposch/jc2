#!/usr/bin/env python3
"""Certify a global, N-independent criterion for vanishing ideal pieces."""
import json
from pathlib import Path
from compute_hilbert import OUT, PROFILES, INSTRUMENT, parse_rows, sha

SLOPES = {77: (1, 1), 111: (2, 1), 129: (13, 3), 136: (1, 3)}


def main():
    result = []
    for profile in json.loads(PROFILES.read_text()):
        n = profile['parameters']
        if n not in SLOPES:
            continue
        a, d = SLOPES[n]
        audit = json.loads((INSTRUMENT / (profile['stem'] + '_audit.json')).read_text())
        names, weights, rows, terms = parse_rows(profile, audit)
        # Lower support inequality for both ring monomials and generators.
        assert all(d*y >= a*b for b,y in weights)
        assert all(d*r['degree'][1] >= a*r['degree'][0] for r in rows)
        assert all(r['degree'][0] >= 1 for r in rows)
        zero_fill = next(name for name,w in zip(names,weights) if w == (0,1))
        period = next(name for name,w in zip(names,weights) if w == (d,a))
        witnesses = []
        for residue in range(1,d+1):
            weight = (a*residue+d-1)//d
            generator = next(r for r in rows if r['degree'] == (residue,weight))
            ring_variable = next(name for name,w in zip(names,weights) if w == (residue,weight))
            assert generator['terms']
            witnesses.append(dict(residue=residue,degree=[residue,weight],
                                  source_index=generator['source_index'],
                                  row_terms=len(generator['terms']),
                                  ring_residue_variable=ring_variable))
        result.append(dict(parameters=n,stem=profile['stem'],slope_numerator=a,
                           slope_denominator=d,
                           exact_vanishing_criterion=f'B=0 or Y<ceil({a}*B/{d})',
                           domain='B,Y nonnegative integers',
                           nonvanishing_criterion=f'B>=1 and Y>=ceil({a}*B/{d})',
                           ring_nonvanishing_criterion=f'Y>=ceil({a}*B/{d})',
                           all_ring_variables_satisfy_lower_inequality=True,
                           all_original_generators_satisfy_lower_inequality=True,
                           all_original_generators_have_positive_B=True,
                           all_direct_row_terms_reverified=terms,
                           zero_charge_fill_variable=zero_fill,
                           period_variable=period,period_degree=[d,a],
                           residue_generator_witnesses=witnesses,
                           direct_rows_sha256=sha(audit['rows_path']),
                           proof='For B=r+kd with 1<=r<=d, multiply the displayed nonzero original generator of degree (r,ceil(ar/d)) by period_variable^k and zero_charge_fill_variable^(Y-ceil(aB/d)). This is a nonzero original-ring element of I_(B,Y) because Q[z,c] is a domain. Conversely every monomial multiple of an original generator has B>=1 and dY>=aB.'))
    target = OUT / 'global_support_vanishing.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
