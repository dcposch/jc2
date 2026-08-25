# Hostile review request: D1 weighted-infinity exceptional support

Act as an independent hostile mathematical reviewer.  Read every source named
below in full, then independently rederive or break the claimed theorem.  Do
not use the existing same-model review as evidence and do not merely summarize
the producer.

Target (immutable):

```text
de7dd223d472508e057db72a5ec466c6362b762b4ba9a50f4ff823f585e774c7  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-20260825.md
```

Required sources:

```text
cases/max12_912_order3_fibre_20260824/order3_fibre.py
cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
cases/max12_912_order3_d1_weighted_infinity_20260825/PREREGISTRATION.md
xmodel/max12-912-order3-d1-classical-degree-split-20260825.md
```

Independently attack all load-bearing bridges:

1. Does the descended `s=1` exceptional fibre really reduce, on the `t=1`
   etale sheet and its `mu_3` orbit, to `k=0` and the eight ordinary Faber
   equations `r_1=...=r_8=0`?
2. From the exact convention
   `g(z(w))=w^12-sum_(ell>=1) r_ell w^-ell`, verify or refute that eight
   vanished tails imply `deg_z(g^3-f^4)<=15`.  Check signs, the inverse-root
   indexing, possible positive Laurent terms, cancellation, and the passage
   from `w`-order back to ordinary `z`-degree.
3. Rework the Mason--Stothers argument after division by
   `D=gcd(g^3,f^4)`: pairwise coprimeness, every constant/zero edge, the
   radical-degree estimate, base-field extension, and the claimed strict
   contradiction.
4. Check the UFD conclusion `f=C^3,g=C^4`, depression of `C`, the six explicit
   graph equations, primeness/closedness, Nullstellensatz contraction, and
   the exact statement after irrelevant-ideal saturation.  Distinguish the
   affine origin from an origin-supported component and from the irrelevant
   point of `Proj`.
5. Check that the reduced exceptional divisor is precisely weighted
   `P(2,3)`, including both axes and the discriminant-zero locus.
6. Re-derive the rational ramification corollary.  In particular verify the
   `mu_n` equivariance, why `gcd(m,n)=1` changes `n|m(9-i)` to `n|(9-i)`, and
   why the only possible denominators are `1` generically, `1 or 2` on the
   `r=0` axis, and `1 or 3` on the `p=0` axis.  Check that `m` remains
   unbounded and that order-zero survival is not mistaken for a deformation.
7. Search aggressively for scope creep: this may classify reduced support
   only.  It must not imply reducedness, formal lifting, a D1 exclusion, a
   counterexample, or JC2.

Write exactly one report:

```text
xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md
```

Include the target SHA, model identity, an explicit verdict (`CONFIRMED`,
`REPAIR`, or `REFUTED`), the smallest failing identity or missing hypothesis,
an independent proof/attack, and a strict scope firewall.  Do not edit any
other file.  This is source-reading and hand derivation only: run no CAS,
solver, substantive Python, or other heavy local computation.
