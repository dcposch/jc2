You are the hostile independent reviewer of one explicit algebraic-geometry
certificate in the plane Jacobian-conjecture campaign.  Work from the named
bytes, not from any prior verdict or summary.  Do not run Singular, Sage,
msolve, Lean, or substantive exact Python locally.  A new heavy replay, if
you judge one indispensable, must be preregistered and run on AWS; normally
the frozen AWS output is enough for this review.

Target:
`xmodel/max12-812-order4-lemniscatic-explicit-param-certificate-20260826.md`

Required target SHA-256:
`949fc476be7be24ea19ac3bc8a18e5ee17e415d0909bc35064b9e0a523042729`

Frozen V3 source manifest:
`cases/max12_812_order4_lemniscatic_target_20260826/FREEZE_V3.sha256`

Registered endpoint and retrieved evidence:

```text
cases/max12_812_order4_lemniscatic_target_20260826/REGISTRATION_V3.md
cases/max12_812_order4_lemniscatic_target_20260826/aws_v3/
```

Charged predecessor/review/erratum and the separately confirmed
coordinate-free corollary are pinned in the target.  Rehash every charged
file you use.  Treat V1 and V2 as immutable NO VERDICT controls.

Independently attack every load-bearing step:

1. Inspect the full V3 input and output.  Verify source/archive custody,
   clean return code, absence of Singular diagnostics, every required
   sentinel, and that the final PASS is not fallthrough.  Check that the
   cleared `D^3 P(q(T),5184/D)` expression really matches the full charged
   residual polynomial.
2. Check the birationality argument: derive the complete divisor/degree of
   `q` on the charged normalization, compare it with `T^2(T-1)`, and ensure
   that extension to and factorization through the normalization is valid.
3. Recompute all five named places, their `q,v` values/valuations, and both
   branch factorizations.  Distinguish the other finite preimages of
   `q=-4/27` and `q=484/9261` from the top-boundary pole places.
4. Recompute
   `S=24(T-1)/(3T-2)` and
   `(1/v)/(S(S-1))=(3T-2)^8/124416`, including the constant, signs, and all
   points at infinity.  Verify that
   `xi=c/((3T-2)^2 y)`, `c^4=124416`, gives exactly
   `xi^4=S(S-1)` over the algebraic closure.
5. Independently check the Weierstrass map, rational inverse, smooth
   completion, `j=1728`, and the differential identity/regularity.
6. Enforce the firewall.  This target arithmetic must not be promoted to a
   source exclusion without componentwise nonconstant `(q,y)` projection,
   exact `dim(J)=1`, and the independent `a6` chart audit.

Write the review only to
`xmodel/max12-812-order4-lemniscatic-explicit-param-review-grok-20260826.md`.
Include the recomputed target SHA, the smallest failing identity or
hypothesis if any, and end with exactly one verdict token on its own line:
`CONFIRMED`, `REPAIR`, or `REJECTED`.  Do not edit the target, case sources,
AWS evidence, nested repositories, or top-level campaign files.
