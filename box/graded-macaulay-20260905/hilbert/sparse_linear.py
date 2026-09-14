#!/usr/bin/env python3
"""Finite sparse row-space arithmetic, with no polynomial completion.

The primitive-integer echelon algorithm gives exact Q ranks.  Its only row
operations are scaling by nonzero rational constants and row subtraction.
The optional Fraction implementation records a combination of original rows.
"""
from fractions import Fraction
from functools import reduce
from math import gcd


def primitive(row):
    row = {k: int(v) for k, v in row.items() if v}
    if row:
        d = reduce(gcd, map(abs, row.values()))
        if row[min(row)] < 0:
            d = -d
        if d != 1:
            row = {k: v // d for k, v in row.items()}
    return row


class IntegerRowSpace:
    """Exact Q row space using integer rows and primitive fraction-free steps."""
    def __init__(self):
        self.pivots = {}
        self.input_rows = 0
        self.elimination_steps = 0

    @property
    def rank(self):
        return len(self.pivots)

    def reduce(self, row):
        row = primitive(row)
        while row:
            key = min(row)
            if key not in self.pivots:
                break
            pivot = self.pivots[key]
            a, b = row[key], pivot[key]
            d = gcd(a, b)
            a, b = a // d, b // d
            row = {k: b * v for k, v in row.items()}
            for k, v in pivot.items():
                value = row.get(k, 0) - a * v
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
            row = primitive(row)
            self.elimination_steps += 1
        return row

    def add(self, row):
        self.input_rows += 1
        row = self.reduce(row)
        if row:
            self.pivots[min(row)] = row
            return True
        return False

    def contains(self, row):
        return not self.reduce(row)


class ModularRowSpace:
    def __init__(self, prime):
        self.p = prime
        self.pivots = {}

    @property
    def rank(self):
        return len(self.pivots)

    def reduce(self, row):
        p = self.p
        row = {k: v % p for k, v in row.items() if v % p}
        while row:
            key = min(row)
            if key not in self.pivots:
                break
            a = row[key]
            for k, v in self.pivots[key].items():
                value = (row.get(k, 0) - a * v) % p
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
        return row

    def add(self, row):
        row = self.reduce(row)
        if row:
            key = min(row)
            inverse = pow(row[key], -1, self.p)
            self.pivots[key] = {k: v * inverse % self.p for k, v in row.items()}
            return True
        return False

    def contains(self, row):
        return not self.reduce(row)


def rational_combination(rows, target):
    """Return exact input-row combination for target, or None.

    Intended for identified small supports, not to attach large dense histories
    to every Macaulay pivot.  Replays the returned identity before returning.
    """
    pivots = {}
    for i, original in enumerate(rows):
        row = {k: Fraction(v) for k, v in original.items() if v}
        history = {i: Fraction(1)}
        while row:
            key = min(row)
            if key not in pivots:
                v = row[key]
                pivots[key] = ({k: a / v for k, a in row.items()},
                               {k: a / v for k, a in history.items()})
                break
            prow, phistory = pivots[key]
            coefficient = row[key]
            for destination, source in ((row, prow), (history, phistory)):
                for k, v in source.items():
                    value = destination.get(k, 0) - coefficient * v
                    if value:
                        destination[k] = value
                    else:
                        destination.pop(k, None)
    row = {k: Fraction(v) for k, v in target.items() if v}
    answer = {}
    while row:
        key = min(row)
        if key not in pivots:
            return None
        prow, phistory = pivots[key]
        coefficient = row[key]
        for k, v in prow.items():
            value = row.get(k, 0) - coefficient * v
            if value:
                row[k] = value
            else:
                row.pop(k, None)
        for k, v in phistory.items():
            answer[k] = answer.get(k, 0) + coefficient * v
    replay = {}
    for i, a in answer.items():
        for k, b in rows[i].items():
            replay[k] = replay.get(k, 0) + a * b
    replay = {k: v for k, v in replay.items() if v}
    assert replay == {k: Fraction(v) for k, v in target.items() if v}
    return {k: v for k, v in answer.items() if v}


def controls(prime=1073741827):
    cases = [
        ('positive_exact', [{0: 2, 1: 3}, {0: 4, 1: 5}], {0: 1}, True, True),
        ('negative_exact', [{0: 1, 1: 1}], {0: 1}, False, False),
        ('bad_prime_modular_NO', [{0: prime}], {0: 1}, True, False),
        ('bad_prime_modular_YES', [{0: 1, 1: prime}], {0: 1}, False, True),
    ]
    results = []
    for name, rows, target, expected_q, expected_p in cases:
        q, p = IntegerRowSpace(), ModularRowSpace(prime)
        for row in rows:
            q.add(row)
            p.add(row)
        yes_q, yes_p = q.contains(target), p.contains(target)
        assert (yes_q, yes_p) == (expected_q, expected_p), name
        combination = rational_combination(rows, target)
        assert (combination is not None) == yes_q
        results.append(dict(name=name, prime=prime, Q_rank=q.rank, Fp_rank=p.rank,
                            Q_member=yes_q, Fp_member=yes_p,
                            Q_combination=None if combination is None else
                            {str(k): str(v) for k, v in combination.items()},
                            exact_identity_replayed=combination is not None))
    return results


if __name__ == '__main__':
    import json
    print(json.dumps(controls(), indent=2))
