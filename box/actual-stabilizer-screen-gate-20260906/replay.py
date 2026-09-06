#!/usr/bin/env python3
"""Independent exact census and necessary whole-tree screen for the hostile gate.

No lane driver is imported by the solver.  The optional charged comparison
imports only the frozen skeleton AFTER computing this implementation's results.
Rows are (n, m, M_2..M_s, V_2..V_s), never asserted polynomial pairs.
"""
from fractions import Fraction as F
from math import gcd, lcm
from functools import lru_cache
from collections import Counter
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import time


def integral(q):
    q = F(q)
    assert q.denominator == 1, q
    return q.numerator


def data(n, m, middle):
    M = (None, -m) + tuple(middle)
    d = [None, n]
    for a in M[1:]:
        d.append(gcd(d[-1], a))
    return M, tuple(d)


def lower_radius(n, M, d, j, radius, v):
    """Def 5.1(3), ratio of its consecutive product formulas."""
    return 1 - (1 - radius) * F(n - M[j-1], n - M[j]) * F(
        v * (n - M[j]) - d[j], v * (n - M[j-1]) - d[j])


def bottom_divisibility(n, m, K, v, A):
    ng, nf = n // K * v, m // K * v
    return (ng % A == 0 and (nf - 1) % A == 0,
            nf % A == 0 and (ng - 1) % A == 0)


def characteristic_sequences(n, m):
    """Choose increasing exponents directly, with strictly dropping prefix gcds.

    Terminal M_s=n-2; d_s>=4.  No height cap or degree-100 test.
    At least one middle exponent is required by s>=3.
    """
    def extend(previous, divisor, prefix):
        if prefix:
            yield prefix + (n - 2,)
        for a in range(previous + 1, n - 2):
            child = gcd(divisor, a)
            if 4 <= child < divisor:
                yield from extend(a, child, prefix + (a,))
    yield from extend(-m, gcd(n, m), ())


def census(limit):
    for n in range(16, limit + 1):
        for m in range(2, n):
            K = gcd(n, m)
            if K < 2 or n % m == 0:
                continue
            for middle in characteristic_sequences(n, m):
                M, d = data(n, m, middle)
                s = len(M) - 1

                def descend(j, incoming, radius, L, chosen):
                    P = incoming * d[j] // d[j+1]
                    lo = d[j] // (n - M[j]) + 1
                    hi = min(P, d[j] - 1) if j == s else P
                    A = (L * radius).denominator
                    for v in range(lo, hi + 1):
                        if j < s and not (A * v <= P or (P - v) % A == 0):
                            continue
                        child_radius = lower_radius(n, M, d, j, radius, v)
                        child_L = lcm(L, radius.denominator)
                        new_chosen = (v,) + chosen
                        if j == 2:
                            A1 = (child_L * child_radius).denominator
                            if any(bottom_divisibility(n, m, d[2], v, A1)):
                                yield (n, m, middle, new_chosen)
                        else:
                            yield from descend(j - 1, v, child_radius,
                                               child_L, new_chosen)
                yield from descend(s, d[s+1], F(-1), 1, ())


class Screen:
    def __init__(self, row, mode, danger=True, ode=True):
        self.row, self.mode, self.use_danger, self.ode = row, mode, danger, ode
        self.n, self.m, middle, self.target = row
        self.M, self.d = data(self.n, self.m, middle)
        self.s = len(self.M) - 1

    @lru_cache(None)
    def radius(self, j, high):
        radius = F(-1)
        assert len(high) == self.s - j
        for k in range(self.s, j, -1):
            radius = lower_radius(self.n, self.M, self.d, k, radius,
                                  high[k - j - 1])
        return radius

    def next_L(self, L, radius, zero):
        if self.mode == 'one':
            return 1
        return L if self.mode == 'actual' and zero else lcm(L, radius.denominator)

    @lru_cache(None)
    def solve(self, j, high, L, dangerous, selected):
        radius = self.radius(j, high)
        A = (L * radius).denominator
        if j == 1:
            div = bottom_divisibility(self.n, self.m, self.d[2], high[0], A)
            if (self.use_danger and dangerous) or not any(div):
                return None
            return dict(level=1, delta=str(radius), L=L, A=A,
                        V=high[0], bottom12=div[0], bottom13=div[1])
        P = integral(F(high[0] * self.d[j], self.d[j+1]))
        Q = integral(F(high[0] * (self.n - self.M[j]), self.d[j+1]))
        target_v = self.target[j-2]

        def factor(v, zero, mark=False):
            if self.ode and P == Q * v:
                return None
            major = v * (self.n - self.M[j]) > self.d[j]
            if not major:
                return dict(V=v, major=False) if not mark else None
            danger2 = dangerous and (zero or
                        (radius.denominator == 1 and radius <= 0))
            child = self.solve(j-1, (v,) + high, self.next_L(L, radius, zero),
                               danger2, mark)
            return None if child is None else dict(V=v, major=True, child=child)

        # A coin has mass v (one whole A-orbit), cost one orbit and two bits:
        # some major exists; the distinguished source path is present.
        nonzero = {}
        for v in range(1, P // A + 1):
            witness = factor(v, False)
            if witness is None:
                continue
            marked = factor(v, False, True) if selected and v == target_v else None
            nonzero[v] = (witness, marked)

        for b in range(P % A, P + 1, A):
            zero = factor(b, True) if b else None
            if b and zero is None:
                continue
            zero_marked = (factor(b, True, True)
                           if selected and b == target_v else None)
            zero_choices = [(zero, bool(zero and zero['major']))]
            if zero_marked is not None:
                zero_choices.append((zero_marked, 3))
            slots = (Q - bool(b)) // A
            mass = (P - b) // A
            if slots < 0:
                continue
            for z_witness, initial in zero_choices:
                dp = {(0, int(initial)): (0, ())}
                for total in range(1, mass + 1):
                    for v, (witness, marked) in nonzero.items():
                        if v > total:
                            break
                        options = [(int(witness['major']), witness, False)]
                        if marked is not None:
                            options.append((3, marked, True))
                        for oldflag in range(4):
                            prev = dp.get((total-v, oldflag))
                            if prev is None or prev[0] >= slots:
                                continue
                            for bits, wit, is_marked in options:
                                flag = oldflag | bits
                                new = (prev[0]+1, prev[1]+((v, is_marked),))
                                old = dp.get((total, flag))
                                if old is None or new[0] < old[0]:
                                    dp[total, flag] = new
                required = 3 if selected else 1
                answer = dp.get((mass, required))
                if answer is not None and answer[0] <= slots:
                    orbits = [dict(**nonzero[v][int(marked)], selected=marked)
                              for v, marked in answer[1]]
                    return dict(level=j, delta=str(radius), L=L, A=A, P=P, Q=Q,
                                zero=z_witness, zero_selected=initial == 3,
                                orbits=orbits)
        return None

    def run(self):
        try:
            return self.solve(self.s-1, (self.target[-1],), 1, True, True)
        finally:
            # Method caches have self keys; clear between rows to bound memory.
            self.solve.cache_clear()
            self.radius.cache_clear()


# Transcription from p.202 image, not imported MOH_TABLE.  Ineffective n-1
# columns are omitted.  Bracket alternatives expand to separate source rows.
PRINTED = {
    (64, 48, (52, 62), (3, 3)),
    (84, 56, (64, 82), (2, 3)),
    (84, 56, (72, 82), (5, 3)),
    (75, 50, (55, 73), (3, 4)),
    (75, 50, (55, 73), (2, 4)),
    (99, 66, (77, 97), (8, 8)),
}


def digest(rows):
    return hashlib.sha256(json.dumps(sorted(rows), separators=(',', ':')).encode()).hexdigest()


def selected_trace(witness):
    trace = []
    while witness:
        node = {k: witness[k] for k in ('level', 'delta', 'L', 'A')}
        if witness['level'] == 1:
            node.update({k: witness[k] for k in ('V', 'bottom12', 'bottom13')})
            trace.append(node)
            break
        node.update(P=witness['P'], Q=witness['Q'],
                    b=witness['zero']['V'] if witness['zero'] else 0,
                    orbit_v=[o['V'] for o in witness['orbits']])
        chosen = witness['zero'] if witness['zero_selected'] else next(
            o for o in witness['orbits'] if o['selected'])
        node['selected_zero'] = witness['zero_selected']
        node['selected_V'] = chosen['V']
        trace.append(node)
        witness = chosen['child']
    return trace


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=200)
    ap.add_argument('--inputs', type=Path, default=Path('/tmp/jc2-lane.rMB50I/inputs'))
    ap.add_argument('--compare-charged', action='store_true')
    ap.add_argument('--output', type=Path, default=Path(__file__).with_name('results.json'))
    args = ap.parse_args()
    started = time.monotonic()
    rows = sorted(census(args.limit))
    assert len(rows) == len(set(rows))
    print('Independent census:', len(rows), flush=True)
    actual, coarse, one, witnesses = set(), set(), set(), []
    excess_witnesses = []
    for index, row in enumerate(rows):
        cw = Screen(row, 'coarse').run()
        aw = Screen(row, 'actual').run()
        if cw is not None:
            coarse.add(row)
        if aw is not None:
            actual.add(row)
            assert cw is not None, row
            witnesses.append(dict(row=row, selected_trace=selected_trace(aw), tree=aw))
        if row[0] <= 100 and cw is not None and aw is None:
            excess_witnesses.append(dict(row=row, selected_trace=selected_trace(cw)))
        if Screen(row, 'one').run() is not None:
            one.add(row)
        if (index+1) % 4000 == 0:
            print('Screened', index+1, 'coarse', len(coarse), 'actual', len(actual), flush=True)
    assert actual <= coarse and one <= actual
    actual100 = {r for r in actual if r[0] <= 100}
    if args.limit >= 100:
        assert actual100 == PRINTED, (actual100 - PRINTED, PRINTED - actual100)
    comparison = None
    if args.compare_charged:
        spec = importlib.util.spec_from_file_location('frozen_control', args.inputs / 'moh_skeleton_full.py')
        control = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(control)
        other = {(n, m, tuple(M), tuple(V[j] for j in sorted(V)))
                 for n in range(16, args.limit+1)
                 for m, M, V in control.census(n, Kmin=2, full=True)}
        comparison = dict(own=len(rows), charged=len(other),
                          own_only=len(set(rows)-other), charged_only=len(other-set(rows)))
        assert set(rows) == other, comparison
    roster = []
    for line in (args.inputs / 'roster.jsonl').read_text().splitlines():
        item = json.loads(line)
        source = item['source']
        # Schema is inspected explicitly, never inferred from arrival indices.
        n, m = source['n'], source['m']
        row = (n, m, tuple(source['M'][1:]), tuple(source['V']))
        roster.append(dict(id=item['row_id'], row=row, actual=row in actual, coarse=row in coarse))
    result = dict(schema='actual-stabilizer-hostile-gate/v1', limit=args.limit,
                  type='NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR',
                  census_count=len(rows), census_sha256=digest(rows),
                  charged_census_comparison=comparison,
                  counts=dict(actual=len(actual), coarse=len(coarse), one=len(one),
                              lost=len(coarse-actual), gained=len(actual-coarse)),
                  counts100=dict(census=sum(r[0]<=100 for r in rows), actual=len(actual100),
                                 coarse=sum(r[0]<=100 for r in coarse)),
                  actual_by_height=dict(Counter(len(r[2])+1 for r in actual)),
                  coarse_by_height=dict(Counter(len(r[2])+1 for r in coarse)),
                  printed202=sorted(PRINTED), printed_set_equality=actual100 == PRINTED,
                  actual_rows=sorted(actual), coarse_rows=sorted(coarse),
                  excess100=excess_witnesses, witnesses=witnesses, roster=roster,
                  elapsed_seconds=round(time.monotonic()-started, 3))
    args.output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({k: result[k] for k in ('census_count', 'counts', 'counts100',
                     'actual_by_height', 'coarse_by_height', 'charged_census_comparison',
                     'elapsed_seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
