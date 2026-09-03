#!/usr/bin/env python3
"""Symbolic diagonal formulas for the lean Laurent second spine.

The calculation is over Q(t,j)[d]/(3*d**2-(t+1)).  It linearizes the exact
Laurent recurrence at the homogeneous origin.  Homogeneity puts one new
elimination variable in each weight, so these diagonal derivatives are the
actual descending-weight affine pivot coefficients.
"""

from __future__ import annotations

import json
import pathlib
import csv

import sympy as sp


t, j, n, d = sp.symbols("t j n d")
q, e = 2*t + 1, 3*t + 1
y = (d+t+1)/(2*q)
g1 = e/q
g2 = e*(d+q)/(2*q**2)
g3 = e*t*(3*d+2*(t+1))/(6*q**3)


def reduce_d(expr):
    field = sp.QQ.frac_field(t, j)
    modulus = sp.Poly(3*d*d-(t+1), d, domain=field)
    numerator, denominator = sp.cancel(expr).as_numer_denom()
    numerator = sp.Poly(numerator, d, domain=field).rem(modulus)
    denominator = sp.Poly(denominator, d, domain=field).rem(modulus)
    return sp.factor((numerator*sp.invert(denominator, modulus)).rem(modulus).as_expr())


# Weight j, 1 <= j <= t-1: perturb C by s**(t-1-j).
b_j = g3*(3*t+2-3*j)/(2*y*(t-j))
d_j = (g2*(t+1-2*j)+b_j*(t+1+j))/(y*(4*t-2*j+1))
n_j = -g1*(t+j)+(j-t)*d_j+2*q*b_j
p_c_derived = reduce_d(e+n_j/(2*y)-q*d_j)

A_c = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j
       +72*t**3+144*t*t+88*t+16)
B_c = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j
       -12*t**3-20*t*t-8*t)
L_c = A_c*d+B_c
p_c_closed = 3*t*e*L_c/((t+1)*(3*t+2)**3*(4*t-2*j+1))
assert reduce_d(p_c_derived-p_c_closed) == 0

F_c = sp.factor(-(3*B_c**2-A_c**2*(t+1))/(3*t+2)**3)
F_c_positive = (
    3*n**4 + 24*n**3*t + 42*n**3
    + 66*n**2*t**2 + 146*n**2*t + 119*n**2
    + 72*n*t**3 + 238*n*t**2 + 234*n*t + 104*n
    + 27*t**4 + 134*t**3 + 223*t**2 + 136*t + 32
)
assert sp.expand(F_c.subs(j, t-n)-F_c_positive) == 0


# Weight j, t <= j <= 2t: perturb U by s**(q-j).
dq_j = 3*g3*(q-j)/(y*(4*t-2*j+1))
nq_j = (j-t)*dq_j+2*(q-j)*g2
p_q_derived = reduce_d(nq_j/(2*y)-(q-j)*g1-q*dq_j)

A_q = 12*t*t+16*t+4-j*(3*t+4)
B_q = 2*(t+1)*(j-t)
L_q = A_q*d+B_q
p_q_closed = -3*t*e*(q-j)*L_q/(
    (t+1)*q*(3*t+2)**2*(4*t-2*j+1)
)
assert reduce_d(p_q_derived-p_q_closed) == 0

F_q = sp.factor(-(3*B_q**2-A_q**2*(t+1))/((t+1)*(3*t+2)**2))
F_q_positive = n**2+4*n*t+6*n+4*t*t-3
assert sp.expand(F_q.subs(j, q-n)-F_q_positive) == 0


# Last high pivot (weight 2t+1) is the b2 coefficient.
p_b2 = reduce_d(g3*d/(2*y))
assert reduce_d(p_b2-g3*d/(2*y)) == 0

print("LAURENT_PIVOT_FORMULAS_PASS")
print("C_WEIGHT_PIVOT_NUMERATOR=", sp.factor(L_c))
print("C_WEIGHT_NORM_FACTOR=", sp.factor(-(3*t+2)**3*F_c))
print("C_WEIGHT_POSITIVE_AT_j=t-n=", F_c_positive)
print("Q_WEIGHT_PIVOT_NUMERATOR=", sp.factor(L_q))
print("Q_WEIGHT_NORM_FACTOR=", sp.factor(-(t+1)*(3*t+2)**2*F_q))
print("Q_WEIGHT_POSITIVE_AT_j=q-n=", F_q_positive)
print("B2_PIVOT=", p_b2)


def fixed_reduce(expr, value, yy):
    qq = 2*value+1
    HH = sp.Poly(
        12*qq*qq*yy**2-12*qq*(value+1)*yy+(value+1)*(3*value+2),
        yy, domain=sp.QQ,
    )
    numerator, denominator = sp.cancel(expr).as_numer_denom()
    numerator = sp.Poly(numerator, yy, domain=sp.QQ).rem(HH)
    denominator = sp.Poly(denominator, yy, domain=sp.QQ).rem(HH)
    return sp.factor((numerator*sp.invert(denominator, HH)).rem(HH).as_expr())


checked_records = []
here = pathlib.Path(__file__).resolve().parent
for record_path in sorted(here.glob("terminal_laurent_t*.json")):
    record = json.loads(record_path.read_text(encoding="utf-8"))
    if "high_pivots" not in record:
        continue
    value = int(record["t"])
    yy = sp.Symbol("q%d_1" % (2*value+1))
    dd = 2*(2*value+1)*yy-(value+1)
    for item in record["high_pivots"]:
        variable = item["variable"]
        if variable.startswith("C"):
            index = int(variable[1:])
            formula = p_c_closed
        elif variable.startswith("q"):
            index = int(variable[1:].split("_")[0])
            formula = p_q_closed
        elif variable == "b2":
            index = 0
            formula = p_b2
        else:
            raise AssertionError(variable)
        specialized = fixed_reduce(
            formula.subs({t: value, j: index, d: dd}), value, yy
        )
        measured = fixed_reduce(sp.sympify(item["coefficient"]), value, yy)
        left = sp.Poly(specialized, yy, domain=sp.QQ)
        right = sp.Poly(measured, yy, domain=sp.QQ)
        ratio = sp.Rational(left.LC(), right.LC())
        if not (left-ratio*right).is_zero:
            raise AssertionError((record_path.name, variable, specialized, measured))
    checked_records.append(record_path.name)

print("FIXED_RECORD_ASSOCIATES_PASS=", ",".join(checked_records))


# Exact finite specialization table requested by the lane.  The primitive
# associate is useful for comparing records made with different rational row
# normalizations; the resultant belongs to the actual displayed coefficient.
table_path = here / "laurent_pivots_t2_t6.tsv"
with table_path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "t", "family", "index", "variable", "coefficient_in_A_t",
        "primitive_linear_associate", "resultant_H_coefficient",
    ])
    for value in range(2, 7):
        yy = sp.Symbol("y")
        qq = 2*value+1
        HH = sp.Poly(
            12*qq*qq*yy**2
            - 12*qq*(value+1)*yy
            + (value+1)*(3*value+2),
            yy, domain=sp.QQ,
        )
        dd = 2*qq*yy-(value+1)
        entries = []
        for index in range(1, value):
            entries.append(("C", index, "C%d" % index, p_c_closed))
        for index in range(value, 2*value+1):
            entries.append(("Q", index, "q%d" % index, p_q_closed))
        entries.append(("B", 2*value+1, "b2", p_b2))
        for family, index, variable, formula in entries:
            coefficient = fixed_reduce(
                formula.subs({t: value, j: index, d: dd}), value, yy
            )
            poly = sp.Poly(coefficient, yy, domain=sp.QQ)
            _, primitive = sp.polys.polytools.primitive(poly.as_expr(), yy)
            primitive = sp.Poly(primitive, yy, domain=sp.QQ).clear_denoms()[1]
            primitive = sp.primitive(primitive.as_expr(), yy)[1]
            if sp.Poly(primitive, yy).LC() < 0:
                primitive = -primitive
            resultant = sp.factor(sp.resultant(HH.as_expr(), coefficient, yy))
            if resultant == 0:
                raise AssertionError((value, family, index, coefficient))
            writer.writerow([
                value, family, index, variable, sp.sstr(coefficient),
                sp.sstr(sp.expand(primitive)), sp.sstr(resultant),
            ])

print("FINITE_PIVOT_TABLE=", table_path.name)
