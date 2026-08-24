#!/usr/bin/env python3
"""Exact source/target quotient audit for the three TD6 center jets.

The audit is deliberately scoped to the frozen registered section: global
(x,y), y=s^-1, p=t^15, q=t+t^25, and the already-fixed F1/pole data.
Changing that section by a new global-domain normalization is not silently
declared a gauge here.
"""

from fractions import Fraction as Q
from hashlib import sha256


def add(left, right, scale=Q(1)):
    out = dict(left)
    for key, coefficient in right.items():
        value = out.get(key, Q(0)) + scale * coefficient
        if value:
            out[key] = value
        else:
            out.pop(key, None)
    return out


def rank(rows):
    pivots = {}
    for original in rows:
        row = dict(original)
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            for key, coefficient in pivots[pivot].items():
                value = row.get(key, Q(0)) - factor * coefficient
                if value:
                    row[key] = value
                else:
                    row.pop(key, None)
        if row:
            pivot = min(row)
            lead = row[pivot]
            pivots[pivot] = {
                key: coefficient / lead for key, coefficient in row.items()
            }
    return len(pivots)


def main():
    # At fixed global x,y, differentiating
    # x=c1*s+c2*s^2+c3*s^3+t*s^4 gives the complete chart components
    # delta t=-delta c1*s^-3-delta c2*s^-2-delta c3*s^-1.
    centers = [
        {("chart_t", -3, 0): Q(-1)},
        {("chart_t", -2, 0): Q(-1)},
        {("chart_t", -1, 0): Q(-1)},
    ]
    assert rank(centers) == 3
    assert all(min(key[1] for key in row) < 0 for row in centers)

    # A regular truncated source change has delta t in E[[s,t]], so every
    # s exponent is nonnegative.  The displayed finite spanning sample is
    # only a replay witness; disjoint Laurent support proves the general
    # statement for all regular orders.
    regular_source = [
        {("chart_t", sdegree, tdegree): Q(1)}
        for sdegree in range(4)
        for tdegree in range(7)
    ]
    assert all(key[1] >= 0 for row in regular_source for key in row)
    assert rank(regular_source + centers) == rank(regular_source) + 3

    # In the normalized boundary section, q'=1+25*t^24 is a unit.  Hence a
    # regular t-reparametrization with delta q=q'*h=0 has h=0.  This is the
    # boundary counterpart of the Laurent-support argument; p'=15*t^14.
    qprime = {0: Q(1), 24: Q(25)}
    for degree in range(7):
        h = {degree: Q(1)}
        product = {}
        for i, a in qprime.items():
            for j, b in h.items():
                product[i + j] = product.get(i + j, Q(0)) + a * b
        assert product[degree] == 1

    # The complete rectangle-preserving determinant-one target gauge list
    # for the frozen degree ordering is: two translations, reciprocal
    # scaling, and the lower shear g+=epsilon*f.  All act on (p,q), never on
    # the source chart, so their center projection is exactly zero.
    p = {15: Q(1)}
    q = {1: Q(1), 25: Q(1)}
    target = [
        {("p", 0, 0): Q(1)},
        {("q", 0, 0): Q(1)},
        add(
            {("p", 0, degree): coefficient for degree, coefficient in p.items()},
            {("q", 0, degree): coefficient for degree, coefficient in q.items()},
            Q(-1),
        ),
        {("q", 0, degree): coefficient for degree, coefficient in p.items()},
    ]
    assert rank(target) == 4
    assert all(key[0] != "chart_t" for row in target for key in row)
    assert rank(regular_source + target + centers) == rank(regular_source + target) + 3

    payload = (
        "center_laurent=-s^-3,-s^-2,-s^-1\n"
        "regular_source_s_degree>=0\n"
        "qprime_unit=true\n"
        "target_gauge_rank=4\n"
        "normalized_section_caveat=true\n"
        "centering_quotient_rank=3\n"
    )
    print("TD6-CENTERING-ORBIT-AUDIT: PASS")
    print("center_chart_tangents = -s^-3,-s^-2,-s^-1")
    print("regular_source_intersection = 0")
    print("qprime_unit_boundary_section = true")
    print("target_gauge_rank = 4")
    print("target_gauge_center_projection_rank = 0")
    print("centering_quotient_rank = 3")
    print("normalized_section_transversality_caveat = true")
    print(f"audit.sha256 = {sha256(payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
