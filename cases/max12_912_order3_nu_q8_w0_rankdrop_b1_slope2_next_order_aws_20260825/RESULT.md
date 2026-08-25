# b=1 slope-two next-order finite-jet control

Box02 `std/dp` and Box03 `slimgb/block` independently regenerated the pinned
six-row source and substituted

```text
c  = c + C1*t
d4 = 1 + B1*t
d2 = 2 + (B1+Q1)*t
x5 = t
x3 = (5/3)*t + X2*t^2
x1 = U2*t^2
w  = -(4/9)*t^2 + W3*t^3.
```

Both exact-Q endpoints verified all leading coefficients vanish, printed the
same six next coefficients, and returned

```text
GNext=(1),  elimination to Q[c]=(1).
```

Thus the reviewed selected slope-two cone has no continuation through this
normalized **unramified** `ord(x5)=1` next-order ansatz, for any finite `c`,
even after allowing first jets of `c`, `d4`, and `u=d2-d4-1`.

This is finite-jet routing only.  It does not exclude ramified/mixed-order
Puiseux arcs, earlier base-coordinate drift relative to `ord(x5)`, arbitrary
rank-drop arcs, full Hsrc, coefficient infinity, Taylor/terminal realization,
trajectories, `(9,12)`, maximum twelve, or JC2.
