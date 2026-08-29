#!/usr/bin/env python3
"""Discovery-only reduction of the (6,8) residual one-forms.

Run on AWS.  We solve the two homogeneous residual invariants for A and e
on the B*d != 0 chart, substitute into the three homogeneous one-form rows,
and factor their pullbacks.
"""

import os
import platform
import socket

import sympy as s

if platform.system() != "Linux":
    raise SystemExit("refusing to run CAS discovery off Linux")
job_tag = os.environ.get("JC2_JOB_TAG", "")
if not job_tag:
    raise SystemExit("JC2_JOB_TAG is required")
print("job_tag =", job_tag)
print("hostname =", socket.gethostname())

t = s.symbols("t")
B = s.Function("B")(t)
c = s.Function("c")(t)
d = s.Function("d")(t)

e = B**2 / 9 - c * d / B
A = -s.Rational(2, 3) * B * c / d - 3 * c**2 / B**2 + s.Rational(3, 2) * d / B

def der(x):
    return s.diff(x, t)

row2_body = (
    -6 * A * B * der(e)
    -6 * A * der(B) * e
    -6 * A * c * der(d)
    -6 * A * der(c) * d
    -der(A) * B**3
    +3 * der(A) * B * e
    +3 * der(A) * c * d
    +6 * B**2 * der(d)
    +12 * B * der(B) * d
    +12 * B * c * der(c)
    +6 * der(B) * c**2
    -18 * d * der(e)
    -18 * der(d) * e
)

row1_body = (
    2 * A**2 * B * der(d)
    +2 * A**2 * der(B) * d
    +2 * A * der(A) * B * d
    -6 * A * c * der(e)
    -6 * A * der(c) * e
    -2 * der(A) * B**2 * c
    +3 * der(A) * d**2
    -3 * B**2 * der(e)
    +3 * B * c * der(d)
    +3 * B * der(c) * d
    +9 * der(B) * c * d
    +6 * c**2 * der(c)
    -18 * e * der(e)
)

row0_body = (
    -A * der(A) * B * e
    -A * der(A) * c * d
    -A * B**2 * der(d)
    -A * B * der(B) * d
    +der(A) * B * c**2
    -3 * der(A) * d * e
    +3 * B * c * der(e)
    -3 * B * d * der(d)
    -3 * der(B) * d**2
    -3 * c * der(c) * d
)

print("A =", A)
print("e =", e)
for name, expr in (("row2", row2_body), ("row1", row1_body), ("row0", row0_body)):
    reduced = s.factor(s.cancel(s.together(expr)))
    print(name, "=", reduced)

print("\nratio coordinates c=B*r, d=B*u")
r = s.Function("r")(t)
u = s.Function("u")(t)
ratio_subs = {
    c: B * r,
    d: B * u,
    der(c): der(B * r),
    der(d): der(B * u),
}
ratio_rows = []
for name, expr in (("row2", row2_body), ("row1", row1_body), ("row0", row0_body)):
    reduced = s.factor(s.cancel(s.together(expr.subs(ratio_subs))))
    ratio_rows.append(reduced)
    print(name, "=", reduced)

Bp, rp, up = s.symbols("Bp rp up")
dsubs = {der(B): Bp, der(r): rp, der(u): up}
linear_rows = [s.cancel(x.subs(dsubs)) for x in ratio_rows]
matrix = s.Matrix([[s.diff(x, v) for v in (Bp, rp, up)] for x in linear_rows])
print("det(row2,row1,row0 / B',r',u') =")
print(s.factor(s.cancel(matrix.det())))
