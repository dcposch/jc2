"""Exact arithmetic for CHILD-INTEGRALITY; no repository imports or search caps.

The general algorithm and its geometric certification obligations are in the
report.  This file implements its fixed-characteristic numerical outer screen
for the three frozen controls, plus the pure own-data arithmetic.  It does not
claim to execute the unavailable OwnVRouteTree dependency of descend_own.py.
"""
from __future__ import annotations

import ast
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path

ROOT = Path('/tmp/jc2-lane.rbo6IG/inputs')
OUT = Path(__file__).resolve().parent

# Execute only the named pure functions from the verified frozen instrument.
names = {'exact_int', 'prefix_gcds', 'characteristic_mu', 'def51_radii', 'inverse_top'}
tree = ast.parse((ROOT / 'descend_own.py').read_text())
pure = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)]
                 + [x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name in names],
                 type_ignores=[])
env = {'Q': F, 'gcd': gcd}
exec(compile(ast.fix_missing_locations(pure), str(ROOT / 'descend_own.py'), 'exec'), env)
integer = env['exact_int']


@lru_cache(None)
def partitions(total, lower=1):
    if total == 0:
        return ((),)
    return tuple((a,) + tail for a in range(lower, total + 1)
                 for tail in partitions(total - a, a))


def factor_shapes(P, Q, A, selected=None):
    """All orbit multiplicities passing these necessary numerical conditions."""
    for z in range(P + 1):
        if (P - z) % A:
            continue
        for mult in partitions((P - z) // A):
            if bool(z) + A * len(mult) > Q:
                continue
            parts = ([z] if z else []) + list(mult)
            if any(F(a) == F(P, Q) for a in parts):
                continue
            if selected is not None and selected not in parts:
                continue
            yield z, mult


def signature_screen(n, m, Mtuple, Vtuple, H, final_galois=False):
    """Finite outer signatures.  Minor subtrees are zero-contribution sinks.

    These controls have a full characteristic chain and an initial centre of
    stabilizer 1. Geometry establishing that these inputs cover actual children
    is a proof obligation, not an assertion established by running this code.
    """
    M = dict(enumerate(Mtuple, 1))
    d = env['prefix_gcds'](n, M)
    s = len(M)
    V = dict(enumerate(Vtuple, 2))
    V[s + 1] = d[s + 1]
    radii = env['def51_radii'](n, M, d, V, H)
    assert M[1] == -m and d[s + 1] == 1

    # Each tuple entry records (kind, f-root count, radius, g-root count, L).
    def canonical(entries):
        return tuple(sorted(entries, key=str))

    @lru_cache(None)
    def visit(r, P, delta, lam, L, selected_path):
        nf, ng = integer(F(m * P, d[r])), integer(F(n * P, d[r]))
        assert lam == F(delta - H, n - M[r])
        if r == 1:
            A = (L * delta).denominator
            if final_galois and not ((nf % A == 0 and ng % A == 1 % A)
                                     or (ng % A == 0 and nf % A == 1 % A)):
                return frozenset()
            return frozenset({(('major', nf, delta, ng, L),)})
        Q = integer(F(P * (n - M[r]), d[r]))
        A = (L * delta).denominator
        answer = set()
        for z, mult in factor_shapes(P, Q, A, V[r] if selected_path else None):
            groups = ([(z, 1, L)] if z else []) + [
                (a, A, lcm(L, delta.denominator)) for a in mult]
            choices_of_selected = [i for i, (a, _, _) in enumerate(groups)
                                   if selected_path and a == V[r]] if selected_path else [None]
            for distinguished in choices_of_selected:
                child_sets = []
                for i, (a, copies, Ln) in enumerate(groups):
                    rho, rhoq = integer(F(m * a, d[r])), integer(F(n * a, d[r]))
                    kappa = m * lam + rho * (H - delta)
                    if kappa < 0:
                        options = {(('minor-sink', rho, H - kappa / rho, rhoq, Ln),)}
                    else:
                        assert kappa > 0
                        W = n - M[r - 1]
                        nd = H - F(W) * kappa / (W * rho - m)
                        assert nd > delta and nd < H
                        nP = integer(F(a * d[r - 1], d[r]))
                        options = visit(r - 1, nP, nd, F(nd - H, W), Ln,
                                        selected_path and i == distinguished)
                    child_sets.append([item * copies for item in options])
                for combination in product(*child_sets):
                    sig = canonical(tuple(x for group in combination for x in group))
                    assert sum(x[1] for x in sig) == nf
                    assert sum(x[3] for x in sig) == ng
                    answer.add(sig)
        return frozenset(answer)

    Ptop = integer(F(V[s + 1] * d[s], d[s + 1]))
    sigs = visit(s, Ptop, radii[s], F(radii[s] - H, n - M[s]), 1, True)
    sums = sorted({sum((F(n, n + m) * row[1] * (H - row[2])
                        for row in sig if row[0] == 'major'), F(0)) for sig in sigs})
    return {'n': n, 'm': m, 'H': H, 'M': M, 'd': d, 'V': Vtuple, 'radii': radii,
            'signature_count': len(sigs), 'sums': sums,
            'signatures': sorted(sigs, key=str), 'final_galois': final_galois}


def classify(sums, *, exhaustive=True):
    if not exhaustive:
        return 'SET-VALUED'
    return 'SURVIVES' if any(x.denominator == 1 for x in sums) else 'DEAD'


def main():
    source_M = {1: -112, 2: 140, 3: 160, 4: 166}
    source_d = env['prefix_gcds'](168, source_M)
    source_V = {2: 3, 3: 21, 4: 3, 5: source_d[5]}
    source_delta = env['def51_radii'](168, source_M, source_d, source_V)
    assert source_delta == {1: F(3, 4), 2: F(3, 10), 3: F(1, 5), 4: F(-1)}
    zero_values, route_steps = {4: F(1)}, []
    vectors = set()
    for i in (3, 2):
        P = integer(F(source_V[i + 1] * source_d[i], source_d[i + 1]))
        den = source_delta[i].denominator
        zero_ok = (P - source_V[i]) % den == 0
        nonzero_ok = source_delta[i] > 0 and den * source_V[i] <= P
        route_steps.append({'i': i, 'P': P, 'zero_ok': zero_ok, 'nonzero_ok': nonzero_ok})
        if nonzero_ok:
            vectors.add(tuple(zero_values[k] if k > i else F(source_V[k]) for k in (2, 3)))
        if not zero_ok:
            break
        zero_values[i] = F(source_d[i], source_d[i + 1]) * zero_values[i + 1] - source_delta[i] * (P - source_V[i])
    assert vectors == {(F(3), F(7))}
    inverted = env['inverse_top'](112, 4, 56, 1, 3, F(3, 10), 12, (3,))
    assert [g['roots'] for g in inverted['inverse_groups']] == [10, 6, 6, 6]

    controls = {
        'R063': (42, 28, (-28, 35, 40), (3, 7), 2),
        'R009': (48, 32, (-32, 37), (2,), 2),
        'R050': (49, 14, (-14, 46), (4,), 2),
    }
    output = {'schema': 'jc2.child-integrality-lemma/v1',
              'lemma': {'name': 'CHILD-INTEGRALITY', 'status': 'PROVED_CONDITIONAL',
                        'hypotheses': ['reduced parent Keller data', 'licensed descent',
                                       'finite correlated own-data cover',
                                       'complete final-major signature cover with printed local hypotheses'],
                        'conclusion': 'all complete sums nonintegral, or certified empty cover, implies no realizing polynomial pair',
                        'r063': 'DEAD', 'six_other_rows': 'OPEN[TRANSPORT-EXHAUSTION]',
                        'transport': "I'_M = u_s I_M on actual mapped major roots"},
              'scope': 'exact finite numerical outer screen; report supplies geometric hypotheses',
              'frozen_pure_functions': sorted(names),
              'R063_source': {'M': source_M, 'd': source_d, 'V': source_V,
                              'delta': source_delta, 'route_steps': route_steps,
                              'outer_V_vectors': sorted(vectors), 'inverse_top': inverted},
              'controls': {}}
    for name, args in controls.items():
        ungated = signature_screen(*args)
        gated = signature_screen(*args, final_galois=True)
        output['controls'][name] = {'ungated': ungated, 'galois_filtered': gated,
                                    'integrality_screen': classify(ungated['sums'])}
    assert output['controls']['R063']['ungated']['sums'] == [F(71, 4)]
    assert output['controls']['R063']['galois_filtered']['sums'] == []
    assert output['controls']['R009']['galois_filtered']['sums'] == [F(8)]
    assert output['controls']['R050']['galois_filtered']['sums'] == [F(8)]
    assert classify([F(1, 2), F(8)]) == 'SURVIVES'
    assert classify([F(71, 4), F(3, 2)]) == 'DEAD'
    assert classify([], exhaustive=False) == 'SET-VALUED'
    assert classify([]) == 'DEAD'
    # Fractional packet contributions can add to an integer; never filter singly.
    assert classify([F(1, 2) + F(3, 2)]) == 'SURVIVES'
    # Corrected (4.4) side bound allows a critical root closer to a g-root.
    q = [F(-2), F(2)]
    beta_distances = [F(-2), F(3)]
    assert sum(q) == 0 and sum(beta_distances) != 0
    assert min(sum(beta_distances) - a for a in beta_distances) >= -2
    output['logical_controls'] = 'passed: finite union, missing cover, empty certified cover, total-sum-only, side-bound cancellation'
    output['six_rows'] = {name: {'output': 'SET-VALUED', 'reason': 'OPEN[TRANSPORT-EXHAUSTION]'}
                          for name in ('R025', 'R026', 'R027', 'R028', 'R057', 'R058')}
    (OUT / 'checks.json').write_text(json.dumps(output, indent=2, default=str) + '\n')
    print(json.dumps({name: {k: list(map(str, data[k]['sums'])) for k in ('ungated', 'galois_filtered')}
                      for name, data in output['controls'].items()}, indent=2))


if __name__ == '__main__':
    main()
