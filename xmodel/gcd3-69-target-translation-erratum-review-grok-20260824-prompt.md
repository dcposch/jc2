# Focused hostile review: GCD3 `(6,9)` target-translation erratum

Act as a hostile different-model reviewer of the frozen erratum

`xmodel/gcd3-69-target-translation-erratum-20260824.md`

at SHA-256

`43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78`.

Verify

`cases/gcd3_69_target_translation_erratum_20260824/MANIFEST.sha256`

at SHA-256
`a00ff5c38a76a033d0b5688bb98052db75ea4a44aa307a657c4d2bba9a1d9529`
and

`cases/gcd3_69_target_translation_erratum_20260824/FREEZE.sha256`

at SHA-256
`4c3f7cb0d0c9bdc45423308a18d50aea5aaef54839c55fd1397b7a31ced21934`.

Read the frozen first common-cubic producer and its completed Grok review,
plus the frozen lower-Pfaffian successor. This review exists because the first
review did not test constant translation of the **first** target coordinate.
Do not defer to either producer or earlier review.

Write exactly one report:

`xmodel/gcd3-69-target-translation-erratum-review-grok-20260824.md`.

Do not edit any other repository file. Re-run the registered replay and make
an independent symbolic or hand derivation of each point.

1. Is `(f,g)->(f+q,g)`, `q in k`, a legal target automorphism under the exact
   frozen `(6,9)` hypotheses? Search for any explicit target-origin,
   boundary-value, integral, Kummer, monicity, or degree pin that forbids it.
   Merely preferring a normalized target value is not a prohibition.
2. Independently verify the high-row chart action
   `a0_new=a0+q`, `kappa_new=kappa-3q/2` and identity
   `g0(a0+q)+(kappa-3q/2)K=g0(a0)+kappa K`. Decide whether
   `q=2kappa/3` proves that `kappa` is not an essential modulus modulo the
   full target affine group.
3. Reconstruct the four lower first integrals and check exactly
   `I4,I3,I1` invariant,
   `I2_new-I2=3kappa q-9q^2/4`, and
   `C=(kappa^2+mu)` invariant. Check signs using simultaneous substitution.
4. Audit both reduced sheets. Verify `d_new=d+q` and invariance of
   `kappa+3d/2` on the zero-bracket sheet. On `C=0`, verify that
   `q=2kappa/3` sends the shifted DS first coordinate to `f_lambda`, leaves
   `g_lambda` and all derivatives unchanged, and therefore leaves the
   terminal ODE and nontrivial-Kummer valuation contradiction unchanged.
5. Give the exact impact on the earlier trust record. The candidate verdict
   is: the phrase "essential kappa" and the modulo-gauge variable count were
   wrong or at least pin-dependent, but no identity, invariant-fiber
   decomposition, or aligned-branch exclusion is invalidated because the
   successor treated all kappa and depends on invariant `C`. Refute this if
   any step actually fails. Cube mismatch, arbitrary `(6,9)`, and JC2 remain
   open.

Label each item `CONFIRMED`, `PARTIAL`, `REFUTED`, or `TYPE-FAIL`. State the
smallest failing identity and the cleanest canonical repair at the top and
bottom.
