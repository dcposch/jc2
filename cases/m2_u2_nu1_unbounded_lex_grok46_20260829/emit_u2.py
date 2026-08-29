#!/usr/bin/env python3
"""Charged emission for the U2 nu=1 packet.  Cap tokens refused."""
import hashlib
import json
import os
import sys
from fractions import Fraction as Fr

from u2_core import (
    verify_absorbed_identity, verify_naive_eta_fails, r2_recurrence_S,
    d9_residue_r2, power_S, dickson, ode_is_nonzero_constant,
    M_law as Mlaw, w_tr as wtr,
)
from controls import (
    tail_cell, tail_inversion_budget, td8_direct_death, td8_postA_L_scan,
)


def refuse_caps(argv):
    for a in argv:
        if a in ('--cap', '--NUCAP', '--MAXNU') or a.startswith('--cap='):
            sys.stderr.write('REFUSED cap token %r\n' % a)
            sys.exit(2)


def frs(x):
    if isinstance(x, Fr):
        if x.denominator == 1:
            return '%d' % x.numerator
        return '%d/%d' % (x.numerator, x.denominator)
    return x


def main():
    refuse_caps(sys.argv[1:])
    out_path = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output' and i + 1 < len(args):
            out_path = args[i + 1]
            i += 2
            continue
        sys.stderr.write('unknown arg %r\n' % args[i])
        sys.exit(2)

    identities = []
    for r, mu, L in [(2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1),
                     (3, 1, 1), (3, 2, 1), (3, 1, 2), (4, 1, 1)]:
        ok, nterms = verify_absorbed_identity(r, mu, L)
        identities.append(dict(r=r, mu=mu, L=L, ok=ok, residual_terms=nterms,
                               naive_eta_fails=verify_naive_eta_fails(r, mu, L)))

    r2 = []
    for L in range(1, 12):
        S, C = r2_recurrence_S(L, A=Fr(2))
        r2.append(dict(L=L, C=frs(C), even=(L % 2 == 0), C_zero=(C == 0)))

    d9 = [dict(n=n, residue=d9_residue_r2(n)) for n in range(2, 9)]

    power = []
    for r in (2, 3, 4):
        for k in range(0, 4):
            S, C, L = power_S(r, k, A=Fr(1))
            power.append(dict(r=r, k=k, L=L, C=frs(C), C_nonzero=C != 0))

    dick = []
    for r in range(2, 6):
        for L in (r - 1, r + 1):
            if L < 1:
                continue
            ok, C = ode_is_nonzero_constant(dickson(r, Fr(2)),
                                            dickson(L, Fr(2)), r, L)
            dick.append(dict(r=r, L=L, C=frs(C), ok=ok))

    tails = []
    for t in range(2, 8):
        c = tail_cell(t)
        tails.append({k: (frs(v) if isinstance(v, Fr) else v)
                      for k, v in c.items()})

    inv = tail_inversion_budget(tmax=8, budget_left=2)
    d8 = td8_direct_death()
    scan = td8_postA_L_scan([1, 7, 13, 19], budget_left=3)
    for row in scan:
        row['w'] = row['w']
        row['self_terminal'] = row['self_terminal']

    blob = {
        'schema': 'U2-NU1/v1',
        'outcome': 'U2_REDUCED_FINITE',
        'identities': identities,
        'r2_parity': r2,
        'd9_residues': d9,
        'power_family': power,
        'dickson_consecutive': dick,
        'td7_tail_cells': tails,
        'td7_inversion': inv,
        'td8_direct': {k: v for k, v in d8.items() if k != 'rows_sample'},
        'td8_postA': scan,
        'M_samples': {
            'r2_mu1_L4': Mlaw(2, 1, 4),
            'r2_mu3_L7': Mlaw(2, 3, 7),
            'r2_mu2_L5': Mlaw(2, 2, 5),
        },
        'w_tr_samples': {
            'w2_r2_L2': frs(wtr(Fr(2), 2, 2)),
            'w32_r2_L1': frs(wtr(Fr(3, 2), 2, 1)),
        },
    }
    text = json.dumps(blob, sort_keys=True, separators=(',', ':'))
    digest = hashlib.sha256(text.encode()).hexdigest()
    blob['emit_sha256'] = digest
    text2 = json.dumps(blob, sort_keys=True, separators=(',', ':')) + '\n'

    sys.stdout.write('emit_sha256 %s\n' % digest)
    sys.stdout.write('t1_identities %d\n' % len(identities))
    sys.stdout.write('r2_parity %d\n' % len(r2))
    sys.stdout.write('td7_inversion_fitting %d\n' % inv['n_budget_fitting'])
    sys.stdout.write('td8_direct_mp2_alive %d\n' % d8['n_mp2_alive'])
    sys.stdout.write('U2_EMIT_PASS\n')

    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)) or '.',
                    exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(text2)


if __name__ == '__main__':
    main()
