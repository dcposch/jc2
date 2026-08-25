# Hostile review: Q8 bidegree residual bound plus rational high-contact kill

Act as an independent hostile algebraic-geometry and exact-computation
referee.  Work read-only except for the one output file named below.  Do not
browse, use a shell, access the network, or run new heavy computation.  Read
these files in full:

- `xmodel/max12-912-order3-nu-q8-sparse-bidegree-residual-bound-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-rational-contact-residual-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`
- `cases/max12_912_order3_nu_q8_sparse_bidegree_mixed_volume_aws_20260825/README.md`
- `cases/max12_912_order3_nu_q8_sparse_bidegree_mixed_volume_aws_20260825/verify.py`
- `cases/max12_912_order3_nu_q8_sparse_bidegree_mixed_volume_aws_20260825/aws_box02_horizontal_v1/result.json`
- `cases/max12_912_order3_nu_q8_sparse_bidegree_mixed_volume_aws_20260825/aws_box03_vertical_v1/result.json`
- `cases/max12_912_order3_nu_q8_contact_hensel_order16384_aws_20260825/README.md`
- `cases/max12_912_order3_nu_q8_contact_hensel_order16384_aws_20260825/replay.py`
- the three accepted `result.out` and `run.meta` files under that case's
  `aws_box02_v5/` and `dependency_linear26_order8192/` directories.

The claimed conclusion is narrow and currently provisional: conditional on
the reviewed existence of at least one H-supported source component, the
bidegree/contact chain should prove that at least one of the three rational
corrected-Q8 contacts `(0,26),(0,58),(0,67)` lies on an H-supported mod-127
source component.  Try to refute every load-bearing point:

1. Audit the `P1_w x P1_v` class convention.  Check that the horizontal and
   vertical affine-BKK calculations really give `A<=176`, `B<=550`, while the
   generic `(1,1)` calculation gives `A+B<=658`, including source
   localization, coordinate-boundary strata, generic isolatedness, and
   arbitrary-characteristic support monotonicity.
2. Check that removing at least one effective H-supported pushforward
   summand of bidegree `(21,190)` licenses
   `a<=155`, `b<=360`, `a+b<=447`.  Attack hidden assumptions about source
   degree, pushforward multiplicity, negative residual coefficients, or
   several H-supported summands.
3. Recompute the exact linear optimization of
   `I(H,R)=190*a+21*b` under those three inequalities.  Verify that the
   maximum is at `(155,292)` and equals `35582`, with no missed projective or
   common-component intersection.
4. Verify from the exact Q8 factorization that `26,58,67` are three distinct
   rational points, not three names for one residue-field orbit or a repeated
   root.
5. Check that the full relative Jacobian/localizer certificate gives one
   reduced source branch with `w` as parameter at each point, and that each
   high-order Newton lane reconstructs the same source equations and truly
   proves `ord H>=N`, rather than only a projected or off-fibre congruence.
6. Audit the use of `h_contact_order=-1` modulo `w^N`: it gives a lower bound
   `N`, not an infinite-order identity.  Ensure that the two 64-GiB failures
   and two terminated mirrors contribute nothing.
7. Under the contradiction assumption that none of the three local branches
   is H-supported, must all three contribute to the non-H residual cycle?
   Check projection-formula multiplicities, ramification, possible vertical
   components, and whether contact at three distinct plane points adds as
   `16384+16384+8192` without normalization loss.
8. Verify the strict arithmetic `40960>35582` and the exact existential
   conclusion: **at least one of these three only**.  Enforce the firewall
   against identifying it, covering the quintic orbit/all eight contacts,
   degree one, characteristic-zero no-merger, Taylor/terminal conclusions,
   maximum twelve, or JC2.

If any mixed-volume or intersection hypothesis is not established by the
listed immutable evidence, mark the composed theorem unconfirmed and name
the smallest exact repair.  Distinguish a custody/exposition omission from a
false mathematical implication.  Do not edit producer files, cases,
manifests, or canonical ledgers.

Write the complete review only to
`xmodel/max12-912-order3-nu-q8-p127-rational-contact-residual-review-grok-20260825.md`.
End with exactly one verdict token on its own line:

```text
CONFIRMED
CONFIRMED_WITH_REPAIRS
INCONCLUSIVE
REFUTED
```
