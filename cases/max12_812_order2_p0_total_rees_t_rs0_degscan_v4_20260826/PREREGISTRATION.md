# Preregistration: repaired degree-scan streaming `T-rs-0`

Date: 2026-08-26

Status: **NAVIGATION-ONLY SOFTWARE ACCELERATOR. NO REES, CHART,
MOVING-`p`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

This is the fail-closed successor to V3.  V3 found and rewrote exactly all
581 intended dependency statements, then stopped before Singular because its
final substring check also matched the unrelated rho deck-invariance check.
V4 changes only that compiler postcondition: after requiring seven literal
old statements and seven literal new degree statements for each of the exact
76+7 frozen atom names, it rejects any surviving old dependency statement.

The resulting Singular program is otherwise emitted byte-for-byte by the
frozen row-streaming V2 compiler.  It changes only

```text
subst(Phi,x,0)-Phi != 0
```

to the exact canonical-polynomial test `deg(Phi,x)>0` in those 581 locations.
All source formulae, rows, quotient extraction, retained coefficients,
controls, term counts, Delta calculation, and the frozen V2 validator remain
unchanged.

V4 runs at the same two good primes alongside V2.  It is accepted only if
both V4 outputs agree with one another and with completed V2 custody.  It may
accelerate manifest discovery but cannot replace exact-Q plus a fresh-prime
validation or prove a Rees/chart theorem.
