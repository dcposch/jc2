# Hostile different-model review — AS109 carry erratum

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2`. The committed basis is
`c17bd2542b40f3178ec619ae4a73501550555336`; all named producer artifacts are
frozen uncommitted additions on top of it.

Read in full:

- `xmodel/as109-support-gate-20260824.md`
- `xmodel/as109-support-review-grok-20260824.md`
- `xmodel/as109-support-gate-20260824-erratum.md`
- `cases/as109_support_20260824/verify_carry_erratum.py`

Frozen hashes:

- original producer: `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`
- original Grok review: `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`
- carry erratum: `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`
- carry replay: `cde7f3d467b492c0d914511b7fa609c916e40a33e6ca6c741af9be79a99d53f0`

The purpose of this follow-up is to correct your earlier claim 2, not to
re-vote by inertia. Independently rerun the carry replay and attack exactly:

1. Expand the determinant modulo `p^3` over `Z[x,y]` for
   `P=x-x^p+pA_0+p^2A_1`, `Q=y+pB_0+p^2B_1`. Verify the definitions of
   `C_1`, `K`, and `N_0`, including every sign, and decide whether corrected
   `E2` is `K+L(A_1,B_1)+N_0=0 mod p`.
2. Verify the analogous carries in the marked collision equations.
3. Recompute the five-slot countercontrol. It must pass the frozen uncarried
   `E1/E2` over `F_109` yet have
   `det J-1 = 109^2 x^108 mod 109^3`.
4. Recompute the parametric family `A_0=y^m`, `B_0=x^108y` and transported
   successor. Decide whether `C_1=0`, the second residual, and the marked
   differences vanish integrally for every `m>=1`; hence decide whether the
   unbounded-gauge/no-finite-literal-grammar stop survives.
5. Check that the Hensel nonautomorphy lemma assumes an already exact
   determinant-one map and is independent of digit carries.
6. Check that `CLOSED-SUPPORT + UNIT-L` uses the packed exact `Z_109`
   equation and is likewise unaffected, while remaining wholly conditional.
7. Scope: no enumeration ran, no lift was found, and no JC2 inference is
   available. State exactly which part of the original review is superseded.

Use exact arithmetic. Identify the smallest failing identity or missing
hypothesis if any. Do not edit any existing producer, review, replay, or
canonical file.

Write exactly one file:

`xmodel/as109-carry-erratum-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
the replay result and hashes, promotion advice, and explicit scope exclusions.
