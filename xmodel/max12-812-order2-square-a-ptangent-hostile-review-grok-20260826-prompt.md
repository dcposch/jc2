You are the independent hostile referee for the moving-`p` addendum to the
generic-square high-contact `A`-prolongation in the `jc2` repository.  Work
text-only.  Do not run Singular, Sage, msolve, Lean, any package compiler, or
any substantive algebra program.  You may read files, recompute SHA-256
hashes, inspect frozen output, and verify the displayed finite identities by
hand.  Do not edit existing files.

Primary targets and required byte hashes:

```text
74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea
  cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULT.md
a2a665a4771f2941a8b64babb9fed35ddc877ce81af2e3fcf75f8a56b5ea1e94
  cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/FREEZE.sha256
380245162296ae04a2cdcc677b04d4617bd415e09665c999090bfab1741839a6
  cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULTS.sha256
657d0461778a3d2b0b0f532c0bf857e2ee71ac1b55abc869667f72d3fdabc11f
  cases/max12_812_order2_square_a_prolongation_owner_v4_ptangent_retry_20260826/compile_square_a_ptangent_v4.py
6977fbcdb9f446dd5c794a1c33438bc60e3ea14784d7269b25288515b750d09c
  cases/max12_812_order2_square_a_prolongation_owner_v4_ptangent_retry_20260826/FREEZE.sha256
322f20ae93c98fe6373cf36e2c5f359646a4de44ea14188c38a4f8b0b3df6488
  cases/max12_812_order2_square_a_prolongation_owner_v3_ptangent_20260826/compile_square_a_ptangent.py
```

Read all six targets completely, validate both named manifests and every
file they name, and also read completely:

```text
cases/max12_812_order2_square_a_prolongation_owner_v3_ptangent_20260826/REGISTRATION.md
cases/max12_812_order2_square_a_prolongation_owner_v4_ptangent_retry_20260826/REGISTRATION.md
cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/REGISTRATION.md
cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/RESULT.md
xmodel/max12-812-order2-square-a-prolongation-hostile-review-grok-20260826.md
xmodel/max12-812-order2-square-a-prolongation-design-20260826.md
```

Attack these points independently:

1. Custody.  Recompute the six pins and every manifest row.  Check the exact
   Q Box03 and `F_65521` r6d V5 tags, compiled inputs, return codes,
   validators, stdout hashes, timings, memory, and swap.  Trace the complete
   V5 -> V4 -> V3 -> owner-v2 dependency chain.  Verify that V3 failed before
   engine at an anchor spelling, V4 ran the mathematical client on both
   fields but failed only its validator prefix, and V5 changed only those
   four strings.  Do not use V3/V4 as accepted endpoints.
2. Source substitution.  Starting from the ordinary quartic coefficients,
   audit `p -> p+2*sigma*ell` in every occurrence: the leading coefficient,
   `r=((p+2sigmaell)^2+...)/4`, `n1,n0`, and every loaded source row.
   Check that this is exactly `L(sigma)=z^2+p/2+sigma*ell`,
   `K=L(sigma)^2+sigma^4 B+...`, and
   `D=L(sigma)A+sigma^4E+...` on the registered high-contact cone.
3. Complete moving receiver.  Independently derive the full sigma-grade-15
   negative receiver from the binomial expansions, including simultaneous
   changes in the numerator `D`, denominator `K`, and Laurent/Faber basis.
   Decide whether the net rational correction really is
   `ell*partial_L(h14)`, with cleared numerator
   `Delta=-12 ell L A E+12 ell B A^2-(5/2)ell k L A^2`.
   The previous hostile review §6 worried that differentiating `K` and `D`
   produces additional pieces.  Reconcile this explicitly: for example the
   denominator contribution `-3/2 ell A E/L^2` and numerator contribution
   `+3/4 ell A E/L^2` must be combined rather than counted separately.
   Quarantine the addendum if any term remains outside `Delta`.
4. Moving Faber transform.  Check the exact formula
   `g14=T(p)h14` and
   `g15=T(p)h15moving+2ell*(dT/dp)(p)h14`, including the factor two from
   `p+2sigmaell`, parity, unit diagonal, and all seven row identities as far
   as hand degree/printed rows permit.  Distinguish source replay from
   analytic insertion.
5. Separator.  Verify
   `Num14 congruent -12 B A^2 (mod L)`,
   `Delta congruent 12 ell B A^2 (mod L)`, and
   `Delta congruent -ell Num14 (mod L)`.  Then decide rigorously whether
   grade fourteen removes the moving contribution and grade fifteen still
   gives `Num15moving congruent -A^3 (mod L)`, so squarefreeness and
   `deg A<=1` force `A=0`.
6. Scope.  The only proposed extension is from fixed `p` to its first
   tangent in the already certified high-contact cone
   `ord_sigma(R)>=2`, `ord_sigma(C)>=4` on `D(p*k0)`.  Lower rays, higher
   `p` jets unless formally implied, `p=0`, fan exhaustiveness, the square
   branch, order two, `(8,12)`, maximum twelve, and JC2 remain open.

Output exactly one new report and no other file:

`xmodel/max12-812-order2-square-a-ptangent-hostile-review-grok-20260826.md`

Include a verdict table, custody chain, complete hand moving-receiver
derivation, reconciliation with the prior review's concern, strongest
surviving theorem, and exact non-claims.  If unchanged, end with exactly
`ORDER2_SQUARE_A_PTANGENT_CONFIRMED`; otherwise end with exactly one of
`ORDER2_SQUARE_A_PTANGENT_REPAIRED` or
`ORDER2_SQUARE_A_PTANGENT_QUARANTINED` and state the smallest repair.
