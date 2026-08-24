# Hostile different-model review — AS109 `xy` membership gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/as109-xy-membership-gate-20260824.md`
- every file under `cases/as109_xy_membership_20260824/`
- the reviewed Hensel degree-cross and `A_infinity` parent gates
- the now-confirmed Moskowicz prime-degree source audit and hostile review

Frozen child hashes:

- report: `09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729`
- replay: `d31f47f0dcee171a2dc4ac60d6aacd098cc55596f7d5a97a0b93574216a6fc01`
- freeze: `76ce3a7b3f176f9d7aa575850e8011ce1cb70b7f88d46fc706ae0e190b857448`

Independently rerun the replay and attack exactly:

1. Rebuild the 109 Hensel sections on the target tube
   `(P,Q)=(109*S,1+109*T)`. Check the hypotheses needed for the sections,
   the congruences `sigma_a(x)=a`, `sigma_a(y)=1` modulo 109, and therefore
   the 109 distinct residues `sigma_a(xy)=a`.
2. Audit the field-degree conclusion. Prove carefully that the distinct tube
   images force `[M(xy):M]>=109`, rather than merely distinct special-fibre
   values after an illegitimate specialization. Check separability,
   localization/completion injections, and the use of the reviewed
   Hensel-to-global degree cross.
3. Check that `xy` cannot lie in the target field or target ring, and that
   this remains true after a characteristic-zero coefficient-field embedding
   into `C`. Seek a constant-extension or descent loophole.
4. Under the separately reviewed hypothesis `A_infinity=0`, verify
   `[L:M]=109`, hence `L=M(xy)`, and derive coefficient by coefficient that
   the monic minimal polynomial reduces on the named tube to
   `Z^109-Z`. Audit integrality/denominator choices and the distinction
   between a field minimal polynomial and a local integral polynomial.
5. Independently recompute trace, norm, and discriminant reductions. Decide
   whether the report correctly stops them as split-etale tautologies rather
   than claiming an obstruction.
6. Verify both controls: the degree-109 finite-free non-Keller map
   `G_p=(x+108*x^109,y)` with primitive `xy` and trivial rational deck group,
   and the cyclic Kummer control in which every nonidentity deck element moves
   `xy`. Check every displayed minimal-polynomial and deck assertion.
7. Audit the surviving univariate deck discriminator `R_tau(mu_w)=0`, its
   reduction `R_tau(Z)=Z+1`, its iteration condition, and whether any claimed
   implication silently assumes the deck action that remains unearned.
8. Enforce scope. The admissible conclusion is a sharp no-go for the
   `xy in M` bridge plus the conditional primitive-generator statement. It
   neither excludes arbitrary AS109 lifts, proves `A_infinity=0`, descends a
   deck cycle, nor resolves JC2.

Use a genuinely independent derivation or second engine wherever practical.
Try hard to find a completion/specialization error, a hidden denominator, or
a field/ring conflation. Do not edit producer/canonical files or launch AWS.

Write exactly one report file:

`xmodel/as109-xy-membership-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent algebra/replay, dependency status, exact scope, and
promotion advice.
