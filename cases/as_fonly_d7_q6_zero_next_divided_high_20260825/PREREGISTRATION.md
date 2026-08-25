# Q6 zero-branch next divided high carry

Use the cumulative canonical branch

```text
Q9: x23=x30=1;
Q8: zero restored vector;
Q7: zero C6,D6,W5,Z5 vector;
Q6: zero H7,J7 vector.
```

Reconstruct the exact integer determinant through the fourth digit.  Write
`G4=F/3+N+T+div(H,J)` for the already-accepted fourth-digit row and form
the recursive next-order residual

```text
R = G4/3 + S(U,V;H,J) + Rmix(C,D;W,Z),
Rmix = Cx Zy + Wx Dy - Cy Zx - Wy Dx,
```

with `H=J=0` on this point.  For degrees 12 down to 7, assert every prior
division over the integers and compare `R mod 3` coefficientwise with the
literal `(det-1)/243 mod 3`.  The first nonzero degree above six is a
pointwise cap-boundary obstruction because a cap-seven fifth digit has
divergence degree at most six.

This tests one cumulative branch only.  It does not classify the Q7/Q6
kernels unless the first obstruction is proved independent of them.
