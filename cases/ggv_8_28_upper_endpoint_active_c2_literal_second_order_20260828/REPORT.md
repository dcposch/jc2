# Mathematical report: relaxed second-order obstruction

At the frozen point, the tangent matrix `A` has shape 510-by-308, rank 291,
and a 17-dimensional kernel.  The producer computed an exact kernel basis,
independently replayed every kernel vector, included the forced `S^2`, `SZ`,
`S^3`, and `c2*S` prefix-curvature terms, and formed the 153 quadratic
columns corresponding to symmetric products of kernel coordinates.

After treating those 153 products as independent variables, the relaxed
second-order equation has matrix

```text
[A | Q] : Q^461 -> Q^510.
```

Exact elimination over `Q` shows that `[A|Q]` still has rank 291 and that
the affine target is inconsistent at row 494, `D22[X^0]`.  Thus none of the
quadratic columns enlarges the image in a way that defeats the endpoint
obstruction.

The exact left dual has support on the 19 rows `D4[X^0]` through
`D22[X^0]`, with coefficients

```text
1/8^18, 1/8^17, ..., 1/8, 1.
```

Before writing the certificate, the frozen producer replayed this witness
against every one of the 461 columns and asserted `y*[A|Q]=0` and `y*b=1`.
Therefore the relaxed affine system would imply `0=1`.  Since genuine
second-order directions additionally satisfy the omitted Veronese rank-one
relations, they form a subset of this already-empty relaxation; no legal
second-order lift exists at this base point.  The zero-target system remains
consistent at `v=w=0`.

The frozen modular checks at 65521, 65519, and 65497 each independently give
rank 291 and the same `D22[X^0]` contradiction with residual one.  They are
corroboration; the conclusion rests on the exact-Q dual.

The charged run completed in 15.09 seconds wall / 15.07 seconds user with
28,068 KiB maximum RSS, zero swaps, and an empty validated final process
census.  The exact certificate SHA-256 is
`19ffd4ebd99a608a345e489c2810a6bae14e9a97fa6ec3552dafeef4ba573832`.

## Scope firewall

This excludes order-two lifts only at the one frozen homogeneous point and
inside the preregistered legal parameter space.  It does not exclude higher
ramified arcs, arcs based at other points, the general deep `A|V0` locus,
unrestricted branch P, landing, Keller pairs, or JC2.

