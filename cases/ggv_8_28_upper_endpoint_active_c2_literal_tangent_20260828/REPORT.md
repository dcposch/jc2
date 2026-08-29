# Mathematical report: exact tangent obstruction at the frozen point

Let `A x = b` be the frozen tangent system, with 510 coefficient rows and
308 legal first-order parameters.  The target vector `b` is zero except for
the row `D22[X^0]`, where it is one.

Exact sparse elimination over `Q` gives rank 291 and reaches a contradiction
at row 494, labelled `D22[X^0]`.  Its archived left-dual witness is supported
on exactly the 19 rows

```text
D4[X^0], D5[X^0], ..., D21[X^0], D22[X^0].
```

The corresponding coefficients are

```text
1/8^18, 1/8^17, ..., 1/8, 1.
```

Before emitting the certificate, the frozen producer recomputed the witness
against the exact sparse matrix and asserted `y*A = 0` for every column and
`y*b = 1`.  Hence a solution would imply `0 = 1`, so no tangent vector in
the preregistered parameter space preserves `D0=...=D21=0` while changing
`D22[X^0]` to one.  The zero-target mutation remains consistent via the zero
tangent vector.

The three frozen modular cross-checks at 65521, 65519, and 65497 each have
rank 291 and independently reach the same contradiction row with residual
one.  These modular results corroborate but do not replace the exact-Q dual.

The exact certificate SHA-256 is
`d21fc8538e908f9a1bc6705fd9e5cf99a2c3d0be3f3b8a82318906ef817c0a8b`.
The charged command completed in 5.99 seconds wall time with 23,760 KiB
maximum RSS and zero swaps.  Final process-group census was validated and
empty.

## Scope firewall

This is a first-order obstruction only at the one frozen homogeneous point,
inside the complete specified reduced-prefix/raw-window tangent space.  It
does not establish scheme isolation, exclude nonlinear arcs or other base
points, settle the deep locus or general-`V0` landing bridge, prove a Keller
theorem, or resolve JC2.

