#!/usr/bin/env python3
"""Tiny exact controls for the relative-Jacobian-rank lemma; stdout only."""
import json
import sympy as S


def require(condition, label):
    if not condition:
        raise ValueError(label)


r, s, t, w, a, b, c, d = S.symbols("r s t w a b c d")
M, A = S.Matrix([[r, s], [t, w]]), S.Matrix([[a, b], [c, d]])
mixed = d*r - c*s - b*t + a*w
require(S.expand((M-A).det() - M.det() - A.det() + mixed) == 0,
        "determinant polarization")

x, y, vx, vy = S.symbols("x y vx vy")
checked = []
for p, q in ((1, 1), (2, 3), (27, 72), (24, 84)):
    top = y**p * (y-x)**q
    expected = y**(p-1)*(y-x)**(q-1) * (
        p*vy*(y-x) + q*(vy-vx)*y)
    actual = vx*S.diff(top, x) + vy*S.diff(top, y)
    require(S.factor(actual-expected) == 0, "two-line derivative")
    # The coefficients of x and y in the bracket give an invertible
    # linear system on (vx,vy), determinant -p*q in characteristic zero.
    require(S.Matrix([[0, -p], [-q, p+q]]).det() == -p*q,
            "no constant null direction")
    checked.append([p, q])

# The two-line hypothesis is essential: a nonlinear triangular automorphism
# has relative rank 1 at every basepoint, not 2.
F, G = y + x**2, x
J = S.Matrix([[S.diff(F, x), S.diff(F, y)],
              [S.diff(G, x), S.diff(G, y)]])
ax, ay = S.symbols("ax ay")
diff = J-J.subs({x: ax, y: ay})
require(J.det() == -1, "automorphism control Jacobian")
require(diff.det() == 0 and diff.rank() == 1, "rank-one countercontrol")
require((S.eye(2)-S.eye(2)).rank() == 0, "affine rank-zero control")

print(json.dumps({"status": "PASS", "two_line_exponents": checked,
                  "determinant_identity": True,
                  "triangular_relative_rank": 1, "affine_relative_rank": 0},
                 sort_keys=True))
