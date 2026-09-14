#!/usr/bin/env python3
"""Tiny exact identity/jet controls; no polynomial-system solve or CAS.

The proof in the report is degree-uniform.  These controls merely detect
sign/normalization defects in its local formulas.  Checks survive python -O.
"""
import argparse
from fractions import Fraction as F
import resource

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
parser = argparse.ArgumentParser()
parser.add_argument("--mutate", action="store_true")
args = parser.parse_args()
K = 10


def require(condition, label):
    if not condition:
        raise RuntimeError("CHECK_FAILED: " + label)
    print("PASS " + label)


def const(c):
    return [F(c)] + [F(0)] * K


def add(*polys):
    return [sum((p[i] for p in polys), F(0)) for i in range(K + 1)]


def scale(c, p):
    return [F(c) * a for a in p]


def mul(p, q):
    return [sum((p[j] * q[i-j] for j in range(i+1)), F(0))
            for i in range(K + 1)]


def inv(p):
    if p[0] == 0:
        raise RuntimeError("nonunit inverse")
    q = const(1 / p[0])
    for i in range(1, K + 1):
        q[i] = -sum(p[j] * q[i-j] for j in range(1, i+1)) / p[0]
    return q


def deriv(p):
    return [(i+1) * p[i+1] for i in range(K)] + [F(0)]


def sq(p):
    return mul(p, p)


def zero(p):
    return all(c == 0 for c in p)


alpha = F(28, 3)
t = F(7, 3)
d0 = F(3, 4)
w = F(1)
require(alpha == 3*t*(t-1) and d0 == 1/(t-1), "quadratic-place-map")
x = const(alpha)
x[1] = F(1)
xi = inv(x)
W = const(0)
W[1] = w
Wp = deriv(W)


def residual(D):
    # F=R-WJ, where J is its exact differential definition.
    R = add(scale(F(1, 3), mul(x, sq(D))), scale(-1, D), const(-1))
    J = add(scale(2, Wp), scale(-1, mul(add(W, const(1)), xi)), scale(2, D))
    return add(R, scale(-1, mul(W, J)))


D = const(d0)
pivot = 2*t-1
require(residual(D)[0] == 0 and pivot != 0, "local-unit-pivot")
for j in range(1, K + 1):
    D[j] = -residual(D)[j] / pivot
require(zero(residual(D)), "formal-contact-through-order-10")

J0 = 2*w + (6*t-1)/alpha
expected_Dp = (w*J0-d0*d0/3)/(2*t-1)
require(D[1] == expected_Dp == F(1077, 1232), "exact-simple-root-contact")
R = add(scale(F(1, 3), mul(x, sq(D))), scale(-1, D), const(-1))
require(R[0] == 0 and R[1] == w*J0 == F(95, 28), "simple-R-root-not-ramified")

# Recover an actual formal square Z^2=4D/3, and A=Z/x; Z(0)=1.
Z = const(1)
target = scale(F(4, 3), D)
for j in range(1, K + 1):
    Z[j] = (target[j]-sq(Z)[j])/2
require(sq(Z) == target, "square-shape-through-order-10")
A = mul(Z, xi)
Cvalue = (5*t-2)*A[0] + 6*t*(t-1)*(2*t-1)*A[1]
Qprime = 3*(t-1)*R[1]
require(Cvalue == t*(t-1)*A[0]*Qprime == F(95, 21),
        "critical-polynomial-nonzero-at-compatible-W-root")
U = mul(mul(sq(x), x), sq(A))
require(U == scale(F(4, 3), mul(x, D)), "original-U-ring-map")
E = add(scale(2, mul(mul(x, W), Wp)), scale(-1, sq(W)),
        mul(add(scale(F(3, 2), U), const(-1)), W),
        scale(F(-3, 16), sq(U)), scale(F(3, 4), U), x)
require(zero(E), "literal-normalized-E-through-order-10")

# The fixed branch has D=-2, alpha=-3/4. R' ignores arbitrary D'.
af, df = F(-3, 4), F(-2)
require(af*df*df/3-df-1 == 0 and 2*af*df/3-1 == 0
        and df*df/3 == F(4, 3), "fixed-branch-simple-R-root")
# wJ-R' = (2/3)*(3w^2-4w-2), as coefficient vectors in w.
require([F(-4, 3), F(-8, 3), F(2)]
        == [F(2, 3)*a for a in [-2, -4, 3]], "fixed-slope-polynomial")

# Deliberate mutation is checked by the same non-assert failure mechanism.
if args.mutate:
    D[1] += 1
    require(zero(residual(D)), "mutated-D-prime-must-fail")

print("ALL_EXACT_CONTROLS_PASS")
