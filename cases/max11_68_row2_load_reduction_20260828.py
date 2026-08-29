#!/usr/bin/env python3
"""Discovery-only expansion of the (6,8) translated row-two load."""

import os
import platform
import socket

import sympy as s

if platform.system() != "Linux":
    raise SystemExit("refusing to run CAS discovery off Linux")
if not os.environ.get("JC2_JOB_TAG"):
    raise SystemExit("JC2_JOB_TAG is required")
print("job_tag =", os.environ["JC2_JOB_TAG"])
print("hostname =", socket.gethostname())

x = s.symbols("x")
l, alpha, beta, gamma, delta, epsilon, zeta, eta = s.symbols(
    "l alpha beta gamma delta epsilon zeta eta"
)
A, B, c, d, e = [s.Function(name)(x) for name in ("A", "B", "c", "d", "e")]
D = A * B / 3 + d
C0 = A**2 / 3 + c
E = A**3 / 27 + A * c / 3 + e

Sl = 35*l*A**2/72 + 7*l*c/6 + alpha*B + 5*beta*A/6 + delta
Tl = 7*l*A*B/36 + 7*l*D/6 + alpha*A**2/3 + alpha*c + 5*beta*B/6 + 2*gamma*A/3 + epsilon
Ul = 35*l*A**3/432 + 7*l*A*c/12 + 7*l*B**2/72 + 7*l*e/6 + alpha*D + 5*beta*A**2/24 + 5*beta*c/6 + 2*gamma*B/3 + delta*A/2 + zeta
Vl = -7*l*A**2*B/432 + 7*l*A*D/36 + 7*l*B*c/36 + alpha*A**3/27 + alpha*A*c/3 + alpha*e - 5*beta*A*B/36 + 5*beta*D/6 + gamma*A**2/9 + 2*gamma*c/3 + delta*B/2 + epsilon*A/3 + eta

row = (
    Ul*s.diff(C0, x) + 2*Tl*s.diff(D, x) + 3*Sl*s.diff(E, x)
    - 3*B*s.diff(Vl, x) - 2*C0*s.diff(Ul, x) - D*s.diff(Tl, x)
)
row = s.expand(row)
for parameter in (l, alpha, beta, gamma, delta, epsilon, zeta, eta):
    coefficient = s.factor(s.diff(row, parameter))
    if coefficient != 0:
        print(parameter, "=", coefficient)
remainder = s.factor(row.subs({p: 0 for p in (l, alpha, beta, gamma, delta, epsilon, zeta, eta)}))
print("remainder =", remainder)

Qdef = B*e + c*d - B**3/9
residual_row2_body = (
    -6*A*B*s.diff(e, x) - 6*A*s.diff(B, x)*e
    - 6*A*c*s.diff(d, x) - 6*A*s.diff(c, x)*d
    - s.diff(A, x)*B**3 + 3*s.diff(A, x)*B*e
    + 3*s.diff(A, x)*c*d + 6*B**2*s.diff(d, x)
    + 12*B*s.diff(B, x)*d + 12*B*c*s.diff(c, x)
    + 6*s.diff(B, x)*c**2 - 18*d*s.diff(e, x)
    - 18*s.diff(d, x)*e
)
incidence_rewrite = (
    -6*A*s.diff(Qdef, x) + 3*s.diff(A, x)*Qdef
    - 2*A*B**2*s.diff(B, x) - s.Rational(2, 3)*s.diff(A, x)*B**3
    + 6*s.diff(B**2*d, x) + 6*s.diff(B*c**2, x)
    - 18*s.diff(d*e, x)
)
print("incidence identity difference =", s.factor(s.expand(residual_row2_body - incidence_rewrite)))
