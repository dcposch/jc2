# Hostile different-model review — AS D7 divided-carry erratum

You are the independent different-model hostile reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`7832fb73ac887041968f9cec2dc6cba7aa0d0bcf`, with the frozen uncommitted
producer artifacts named below. Read in full:

- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md`;
- every payload in
  `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/MANIFEST.sha256`;
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/FREEZE.txt`;
- the earlier quarantined report and package only to check the retraction and
  byte-preservation ledger, never as mathematical evidence.

Frozen hashes:

- report:
  `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194`;
- manifest / freeze:
  `15eaebe76b10f27f63bf16e01efebbb623d0a7c03a7c45787aa58fd977f0736d` /
  `e1e8bd61077354d3523c9b655980fe6118164fdbb67e7ff1930db064df0643f6`;
- integer replay / independent Singular audit / corrected generator:
  `dde2c39caaaadae1a5e881c511cecc73c8842083076a01af50b950f91be59bfa` /
  `a271c47faa8fcb8f96ecc9e7b04e4305237f59ec867feb4c4d9a0e4972dc0518` /
  `41ee62190262d779e36a62183cbdf27f05273cff5ac91cbcd002e324a3facca3`.

Verify the manifest and rerun every registered command, including the slow
`RADICAL=1` and `COVER=1` modes. Those runs are regressions only. Then attack
the source and algebra independently:

1. **Integral quotient provenance.** Starting over `Z` from
   `P0=x-x^3`, `Q0=y`, `P=P0+3U`, `Q=Q0+3V`, derive the complete identity
   `det J(P,Q)-1=3L+9K`, including signs, with
   `L=U_x+V_y-x^2`. Prove precisely when `L/3` is integral on the charged
   first-digit scheme. After adding `9C,9D`, independently derive the next
   residual `L/3+K+C_x+D_y mod 3`. A mod-three bracket reconstruction alone
   is a review failure.
2. **Cartier row and falsifier.** Independently prove the basic Cartier
   coefficient of `K` vanishes but that the coefficient of `L/3` is
   `u_(p,p-1)+v_(p-1,p)`, hence `u5_3+v5_2` at `p=3,D=7`. Recompute the
   integer determinant for `U=x^3 y^2`, `V=x^2 y`; verify that it passes the
   old 29-row test yet has full residual coefficient one at `x^2y^2`.
3. **Corrected source ideal.** From coefficient arithmetic rather than copied
   generator text, independently enumerate the 40 variables and all 30
   nonzero rows: 14 first-divergence, nine degree-eight carry, six
   degree-seven carry, and the divided-linear Cartier row. Check that the six
   degree-six Frobenius coefficients remain a free factor and that no omitted
   divided term reaches the already reviewed degree-12/11 associated-top
   gate.
4. **Exact algebra.** Over `F3`, independently verify GB size 269, dimension
   18, radical GB size 44, and nonradicality of the original ideal `I`.
   Attack monomial-order and generator-order dependence. Do not infer a
   minimal-prime or primary decomposition from a radical routine.
5. **Nonreduced cover.** Reconstruct `q4`, `Q0=I:q4^infinity`,
   `B=I+(q4^2)`, `Q1=B:u5_0^infinity`, and `E=B+(u5_0^2)` from the original
   `I`. Verify both containment directions in
   `I=Q0 intersect B=Q0 intersect Q1 intersect E`, with the reported
   dimensions and GB sizes `(18,150)`, `(18,169)`, `(17,3277)`. Try to break
   the equality. Explicitly reject unsupported claims that these pieces are
   primary or minimal, and retain `E` as load-bearing.
6. **Retraction and scope.** Confirm that the old universal bracket lemma and
   degree-12/11 top gate survive, while full-residual, 29-row completeness,
   old dimension/component statistics, and old two-piece cover claims are
   retracted. Check the old frozen bytes are unchanged. Reject any inference
   about accepted second digits, the following carry, other branches, full
   D7, all-depth lifting, characteristic zero, a counterexample, or JC2.
   Decide whether the degree-ten mixed-carry system, generated componentwise
   from the original nonreduced `I`, is the smallest honest successor.

Use exact arithmetic and a genuinely independent source-identity/equation
emitter. Producer replay and prose comparison are insufficient. Do not edit
producer, case, canonical, ladder, notes, prompt, log, run, freeze, or erratum
files and do not launch AWS. Keep scratch outside tracked paths. Write exactly
one report:

`xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
checked hashes, independent identities/row data, the smallest failing identity
if any, exact promotion language, and quarantine language at both ends.
