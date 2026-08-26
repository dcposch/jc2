# Preregistration: 24-column hQ filtered lift

Date: 2026-08-26 UTC

Reconstruct the exact frozen V7 witness from the charged ordinary-tail rows,
the reviewed q2 correction, the V6 scalar h correction, and the V7 scalar
h-squared correction.  Require the exact V7 witness SHA before solving.

Let `E_i(0)` be the complete h-zero specialization of row `i`.  Form exactly
the 24 preregistered multiplier columns

```text
h*q_j*E_i(0),  i=1,...,8,  q_j in {q2,q1,q0}.
```

At h-degree one project onto the disjoint union of the previously cancelled
Q-R and `(R^2 or Q^3)` grades and the next `Q^2 R` grade.  Solve the complete
exact rational system on that union.  Including the first two zero targets
prevents a new hQ correction from silently destroying earlier cancellations.
If inconsistent, emit and verify a left-cokernel functional.  If solvable,
add the 24-term-supported correction to the eight multipliers, verify the
complete projected residual is zero, emit the full exact polynomial identity,
and recompute its exact eta threshold.

Run source-identical forward/reverse arithmetic traversals on two registered
AWS hosts under explicit caps.  This test is complete only for the stated 24
columns and three projected grades.  It does not prove multiplier-support
completeness, an h-adic lift, moving-source/load covariance, the whole fan,
D1, or JC2.
