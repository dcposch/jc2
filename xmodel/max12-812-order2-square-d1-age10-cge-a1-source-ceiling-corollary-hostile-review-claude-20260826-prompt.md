# Hostile review: D1 `a>=10`, `C>=a+1` source-ceiling corollary

You are the independent hostile reviewer.  Work in
`/Users/dc/code/math/jc2`.  Do not trust the corollary, producer RESULT, or
PASS markers.  Do not edit any producer, corollary, manifest, prompt, ledger,
or existing review.  Write only

```text
xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-hostile-review-claude-20260826.md
```

Finish with exactly one verdict: `CONFIRMED_CONDITIONAL`, `REPAIR`, or
`REFUTED`.  `CONFIRMED_CONDITIONAL` means the specialization is exact but
final promotion remains conditional on confirmation of the separately live
parent producer review.

## Frozen target

```text
d0ef64c39189df96654df50726fd7b65a958e0eaea67ec2204456b7bc9bf3087
  xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-20260826.md
7cdf4a707204bcd7fbbbea6e6b21aab687afef11b2a8aad7e33a864b01fac560
  xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-20260826.sha256
```

Rehash all seven manifest rows, both parent manifests, and every nested
source/evidence row needed for a finding.  The parent producer's separate
hostile review may still be live; do not mutate or silently import its
eventual report.

## Charges

1. Inspect the exact compiled source and decide whether its grade-38 relation
   is genuinely polynomial in every `Abar,Cbar,Rbar,theta,eta` jet.  Confirm
   or refute that the only localization used for the endpoint is
   `iJ*J-1`; no `A`, `C`, `R`, `theta`, or `eta` leading coefficient may be
   inverted or constrained by a Bezout/exact-contact equation.
2. Re-derive the specialization

   ```text
   theta=sigma^n, eta=sigma^s, Cbar=sigma^m*Chat,
   n,m,s>=0.
   ```

   Charge whether substitution commutes with the moving `p(sigma)` Faber
   connection, reduction modulo `sigma^39`, and the complete target rows.
   The conclusion must be a closed divisibility/source-ceiling statement,
   never density from an exact-contact open.
3. Audit the finite `C_10` ceiling mechanically.  For each `0<=m<=10`,
   compare the available shifted `Chat` coefficients with the exact remaining
   grade budget.  At `m=10`, verify that the possible grade-38 `k6*C/L`
   coefficient is still present.  At `m=11`, verify that the earliest
   `C`-dependent family is grade 39 and is zero modulo `sigma^39`, so no
   omitted `Chat` jet can enter.
4. Independently enumerate how every primitive family containing `e_C`
   copies of `C` moves under the shift.  Raising `C` must move it later by
   `m*e_C`, never reveal an excluded lower-grade family, change its pole
   order, or move a target.  Recheck that all `C`-free families are already
   within the parent's pole-three ceiling and that the first pole-four family
   `k6*A*C/L^4` moves from grade 43 to `43+m`.
5. Recheck the odd-row functional and target cancellation after the
   specialization.  Even targets must remain absent and the sole survivor
   must be `-sigma^38*J/4`; decide whether the unit ideal on `D(J)` is before
   radicals.
6. Use a hostile boundary control: lower rather than raise `C` and determine
   whether at shift `m=-5` the displayed pole-four family reaches grade 38.
   This is outside the claim, but the review should reject any silent
   extension across a source-ceiling wall.
7. Recompute the exact unique-`AC` consequence from

   ```text
   d in {1,2,3}, s=r-a>=0, a+3*s>d.
   ```

   Verify specifically that for every `a>=10` the corollary contains all
   `d=2` classes `s=0,1,>=2` and both `d=3` classes `s=0,>=1`, and state the
   first high-`a` point omitted if any.
8. Enforce the firewall.  This review may confirm only the `C>=a+1,r>=a`
   specialization after the same upstream gates, conditional on the parent
   review.  It is not another D1 fan face, a positive-load theorem, a new
   `p=0`/`k0=0` landing, a whole-square/order-two/max-12 theorem, or JC2.

Report the smallest failed substitution, first missing jet, or first omitted
fan point if one exists.
