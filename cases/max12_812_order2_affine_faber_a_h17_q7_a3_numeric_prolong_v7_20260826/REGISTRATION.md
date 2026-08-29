# Registration: H17/q7/a3 numeric formal prolongation

Date: 2026-08-26

Status: preregistered exact-Q/good-prime formal-recursion control.

## Purpose

Test the all-orders implicit-function mechanism beyond the frozen
grade-51 face on the simplest `D(X)` specialization.  This is a
coefficient-recursion producer, not a Taylor/global realization.

Use the complete frozen seven ordinary tails and set

```text
E=M=a3=X0=1,
Y0=R0=R1=S1=0,
lambda=s^17, a=s^3, X=s^7,
```

with every free positive jet zero.  Retain the full affine load graph and
take `mu6=0` and source determinant `j=1`, whose effective row-7 target is
`s^57/4`.

At recursion index `n`, solve the coefficient of `s^n` in

```text
(s^-48 P1, s^-48 P3, s^-48 P6,
 s^-48 P2, s^-48 P4, s^-51 K, s^-51 H)
```

for the new coefficients of

```text
(S0bar,Ybar,d2,dm,d4,d6,kappa).
```

Here `K=E*H3+H5` and
`H=2E^2P3+16EP5+64P7-(E^3/2)P1` are the exact frozen row
combinations.  The engine must reconstruct all seven source rows from
`tails.json`; it may not consume V6 reduced equations.

## Hard controls

- Every row is zero below weight 48 and both `K,H` are zero below 51 for
  each candidate coefficient evaluation.
- The new-coefficient map is affine and its matrix is constant through all
  25 recursion indices.
- Its exact-Q determinant is `45/2^19`; the good-prime determinant is its
  coefficient reduction and is nonzero.
- The constant solution is

  ```text
  S0=Y=0, d2=1/2, dm=-7/64, d4=3/32,
  d6=-10, kappa=8/5.
  ```

- The unit source determinant first affects recursion index six.  The
  engine emits all dependent coefficients through index 24 and verifies
  every transformed equation through that index.
- Any missing hash, nonlinear new coefficient, changed matrix, wrong
  initial solution, or residual is a fail-closed stop.

Exact Q is evidence and F65521 is a software control.  A PASS proves only
one normalized numeric formal branch through the tested order.  It does
not prove the general IFT theorem, rational/algebraic termination,
strict-source or total-Rees access, either Taylor family, order two,
maximum twelve, or JC2.
