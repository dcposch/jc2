# Preregistration — exact rational/SNF core of normalized B9

Consume the source-pinned normalized determinant equation

```text
E(T) = b + A*T + 243*J(T)
```

with 276 source rows and 146 coefficient variables.  Over the integers and
rationals, compute:

1. `rank_Q(A)` and the full Smith diagonal with its 3-adic valuation profile;
2. primitive integer bases of the rational right kernel and left kernel,
   with exact two-sided multiplication checks;
3. `rank_Q([A|-b])`, rational solvability of `A*T=-b`, and denominators of a
   particular solution if one exists;
4. the exact projected polynomial `C^T(b+243*J(T))`, including its constant,
   every P-Q quadratic coefficient, coefficient rank, support, and valuation
   histogram.

This is a structural diagnostic of one normalized coefficient box over one
fixed B9 parent.  A nonzero projected polynomial is a compatibility system,
not by itself an emptiness theorem; solving image coordinates may still be
necessary.  Heavy execution is AWS-only.
