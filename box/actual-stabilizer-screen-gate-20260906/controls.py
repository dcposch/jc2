#!/usr/bin/env python3
"""Certificate checks use the full product formula, independent of DP recurrences.

Also clarify the frozen report's 'L=1 always' ancillary control and record
the five p.207 bottom-residue controls in their nonunit-Jacobian scope.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path
import json
from replay import Screen, selected_trace


def rowtuple(row):
    return row[0], row[1], tuple(row[2]), tuple(row[3])


def validate(row, tree):
    n, m, middle, target = rowtuple(row)
    M = {i: a for i, a in enumerate((-m,) + middle, 1)}
    s = len(M)
    d = {1: n}
    for i in range(1, s+1):
        d[i+1] = gcd(d[i], M[i])

    def visit(node, high, L, dangerous, selected):
        j = node['level']
        term = F(n - M[j], n - M[s] - 1)
        for k in range(j+1, s+1):
            term *= F(high[k] * (n - M[k]) - d[k],
                      high[k] * (n - M[k-1]) - d[k])
        delta = 1 - term
        A = (L * delta).denominator
        assert (node['delta'], node['L'], node['A']) == (str(delta), L, A)
        if j == 1:
            assert not dangerous
            a, b = n // d[2] * high[2], m // d[2] * high[2]
            assert (a % A, b % A) in {(0, 1 % A), (1 % A, 0)}
            return 1
        P = high[j+1] * d[j] // d[j+1]
        Q = high[j+1] * (n - M[j]) // d[j+1]
        z = node['zero']['V'] if node['zero'] else 0
        assert P == node['P'] and Q == node['Q']
        assert z + A * sum(f['V'] for f in node['orbits']) == P
        assert bool(z) + A * len(node['orbits']) <= Q
        assert (P-z) % A == 0
        factors = ([(node['zero'], True, node['zero_selected'])] if z else [])
        factors += [(f, False, f['selected']) for f in node['orbits']]
        majors = marks = bottom_count = 0
        for factor, zero, marked in factors:
            v = factor['V']
            assert v >= 1 and P != Q * v
            major = v * (n-M[j]) > d[j]
            assert major == factor['major']
            majors += major
            marks += marked
            if marked:
                assert selected and v == target[j-2]
            if major:
                L2 = L if zero else lcm(L, delta.denominator)
                danger2 = dangerous and (zero or delta.denominator == 1 and delta <= 0)
                bottom_count += visit(factor['child'], {**high, j: v},
                                      L2, danger2, marked)
            else:
                assert 'child' not in factor and not marked
        assert majors and (marks > 0 if selected else marks == 0)
        return bottom_count
    return visit(tree, {s: target[-1]}, 1, True, True)


class InternalOne(Screen):
    """Force L=1 only at internal nodes; retain the final selected update."""
    def next_L(self, L, radius, zero):
        return L if zero else lcm(L, radius.denominator)

    @lru_cache(None)
    def solve(self, j, high, L, dangerous, selected):
        return super().solve(j, high, 1 if j >= 2 else L, dangerous, selected)

    def run(self):
        try:
            return super().run()
        finally:
            Screen.solve.cache_clear()


def selected_only(row):
    """Selected-factor relaxation; no sibling existence test."""
    engine = Screen(rowtuple(row), 'actual')
    n, m, _, target = engine.row
    def walk(j, high, L, danger):
        radius = engine.radius(j, high)
        A = (L*radius).denominator
        if j == 1:
            a, b = n//engine.d[2]*high[0], m//engine.d[2]*high[0]
            return (not danger and (a%A, b%A) in {(0, 1%A), (1%A, 0)})
        P = high[0]*engine.d[j]//engine.d[j+1]
        Q = high[0]*(n-engine.M[j])//engine.d[j+1]
        v = target[j-2]
        if P == Q*v:
            return False
        for zero in (True, False):
            if ((P-v)%A != 0 if zero else A*v > P):
                continue
            L2 = L if zero else lcm(L, radius.denominator)
            danger2 = danger and (zero or radius.denominator == 1 and radius <= 0)
            if walk(j-1, (v,)+high, L2, danger2):
                return True
        return False
    try:
        return walk(engine.s-1, (target[-1],), 1, True)
    finally:
        engine.radius.cache_clear()


def main():
    directory = Path(__file__).parent
    result = json.loads((directory/'results.json').read_text())
    leaves = sum(validate(w['row'], w['tree']) for w in result['witnesses'])
    internal_one = [r for r in result['coarse_rows']
                    if InternalOne(rowtuple(r), 'actual').run() is not None]
    # These are child bottom checks only: J=x^ell, ell=1 or 2, so parent
    # Prop 5.6 is deliberately not applied.  All five rows are read from p.207.
    p207 = [
        (16, 12, 13, 3, '-1', '1/4', 1),
        (21, 14, 16, 2, '-1/2', '7/6', 1),
        (21, 14, 18, 5, '-1', '1/3', 1),
        (15, 10, 11, 3, '-1', '1/2', 2),
        (15, 10, 11, 2, '-1', '4/3', 2),
    ]
    child_checks = []
    for n,m,M2,v,delta2,delta1,ell in p207:
        readings = []
        for zero in (True, False):
            L = 1 if zero else F(delta2).denominator
            A = (L*F(delta1)).denominator
            a, b = n//gcd(n,m)*v, m//gcd(n,m)*v
            readings.append(dict(C2_zero=zero, L=L, A=A,
                                 bottom_pass=(a%A,b%A) in {(0,1%A),(1%A,0)}))
        assert any(c['bottom_pass'] for c in readings)
        child_checks.append(dict(row=[n,m,M2,v], ell=ell, readings=readings,
                                 scope='BOTTOM_RESIDUES_ONLY_NOT_PARENT_SCREEN'))
    excess = []
    for e in result['excess100']:
        row = rowtuple(e['row'])
        assert Screen(row, 'actual').run() is None
        assert Screen(row, 'coarse').run() is not None
        excess.append(dict(row=row, selected_only_actual=selected_only(row)))
    delta_checks = []
    printed_delta1 = {
        (64,48,(52,62),(3,3)): '9/16',
        (84,56,(64,82),(2,3)): '16/21',
        (84,56,(72,82),(5,3)): '7/12',
        (75,50,(55,73),(3,4)): '1/2',
        (75,50,(55,73),(2,4)): '1/3',
        (99,66,(77,97),(8,8)): '4/9',
    }
    for row, printed in printed_delta1.items():
        engine = Screen(row, 'actual')
        computed = str(engine.radius(1, row[3]))
        engine.radius.cache_clear()
        delta_checks.append(dict(row=row, printed=printed, computed=computed,
                                 agrees=printed == computed))
    assert [c['computed'] for c in delta_checks if not c['agrees']] == ['2/3']
    answer = dict(certificates_checked=len(result['witnesses']),
                  represented_bottom_certificates=leaves,
                  force_L1_all_nodes=result['counts']['one'],
                  force_L1_internal_nodes_only=len(internal_one),
                  p207_child_bottom_checks=child_checks, p202_delta1_checks=delta_checks,
                  excess100=excess,
                  selected_only_excess=sum(e['selected_only_actual'] for e in excess))
    (directory/'controls.json').write_text(json.dumps(answer,separators=(',',':'))+'\n')
    print(json.dumps(answer, indent=2))


if __name__ == '__main__':
    main()
