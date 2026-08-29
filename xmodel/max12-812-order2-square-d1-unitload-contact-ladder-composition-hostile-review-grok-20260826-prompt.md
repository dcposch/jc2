# Hostile review: unit-load D1 `d=1` contact-ladder composition

You are the independent hostile reviewer. Work in
`/Users/dc/code/math/jc2`. Review the frozen audit and all named constituents;
do not trust their summaries. Do not edit any producer, audit, prompt, ledger,
or existing review. Write only

```text
xmodel/max12-812-order2-square-d1-unitload-contact-ladder-composition-hostile-review-grok-20260826.md
```

Finish with exactly one verdict: `CONFIRMED`, `CONFIRMED_CONDITIONAL`,
`REPAIR`, or `REFUTED`. A conditional verdict is allowed because the frozen
`a>=10` producer's separate hostile review is still live; state the condition
precisely.

## Target and fan authority

```text
52ab6ce6a9628dfc019d1e99aa2deba8af9a6f467f23f2821ff1f30109a56d85
  xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-audit-20260826.md
c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d
  xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md
```

## Constituent custody

```text
17c3baa20232dad9dd1356c8e903a863a44480344d81d8aa587216414aad0a61
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/RESULT.md
9c53eecf7aa3a1fbc75012d9566a2d564e7a39da7e9011c6d5fd63cd53431920
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/FREEZE.sha256
49264a8d6ae24724ee1005dfac9b4602946f2f3b7a77c0512df237369470f254
  cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/EVIDENCE.sha256
e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335
  xmodel/max12-812-order2-square-d1-finite-band-a2-a5-hostile-review-grok-20260826.md

f3c987b630a2895defabcc1043768497f2e8caad538f58122bb4e17b317c0a9c
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/RESULT.md
b2a38e4f5c38166789c5d73ecae989c30ed8168c5fc6a58fc3058eb5535e1ad5
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/FREEZE.sha256
eb0058746a406c9d36c11d00c97884e7e937f93cf693763401aa957c432990ee
  cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/EVIDENCE.sha256
3e601cf34eb23270daa067794087155b7179607d27af01f84a60624447f949e3
  xmodel/max12-812-order2-square-d1-load-transition-a6-a7-v2-hostile-review-grok-20260826.md

3d847561946751c68a081db55f2f514b3808c22f7ac6e236fcbff10911ab1ce6
  xmodel/max12-812-order2-square-d1-a8-k6-mu2-v3-promotion-20260826.md
b5944e1582a2df9ff37224bd7c5875520321f0ee0998c63c8ceeeedfbb66bba2
  xmodel/max12-812-order2-square-d1-a8-k6-mu2-v3-hostile-review-grok-20260826.md
dfabe08283e8fe9cb1ea6cef28a9eac6a4728d0f7c482e8c642b2835798d0459
  xmodel/max12-812-order2-square-d1-a9-full-composition-promotion-20260826.md
8524bd1e20ecfc3931df5c9df9e88f6673de5a7f348b015954884acdddd558eb
  xmodel/max12-812-order2-square-d1-a9-full-composition-hostile-review-grok-v3-20260826.md

60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b
  cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/PRODUCER_FREEZE.sha256
```

Rehash all named files and every source/evidence manifest row.

## Charges

1. Recompute the unit-load lower hull from the five candidate weights and
   prove or disprove that the normalized integral unique-`AC`, `d=1` cell is
   exactly `a>=2,c=a+1,r>=a`. Charge strict versus closed inequalities,
   equality faces, the `RA2` exception, and the meaning of integral
   `ord_sigma`. Give the first omitted `(a,c,r)` if any.
2. Verify that the intervals `{2,3,4,5}`, `{6,7}`, `{8}`, `{9}`, and
   `{a>=10}` partition the cell with no gap. Check that `k10` versus its
   leading jet `k0` is the same unit-load open and that the `D(J)` tail may
   be restricted to `D(p*k0*J)`.
3. Audit `r>a` in every finite band: leading-section `eta=0`, next-R-jet
   timing, exact-contact hypotheses, and the homogeneous `a>=10` tail.
4. Audit every lower-load transition: no early `k6` at `a<=5`; complete
   `k60/k61` timing at `a=6,7`; exhaustive `D(k60)/V(k60)` at `a=8`;
   exhaustive `k60,k60_1` scheme split and DVR intermediate sections at
   `a=9`; all `k10_6,k6_10,k2_6` values at `a>=10`.
5. Charge the common upstream hypotheses and theorem types. Arcwise
   set-theoretic bands and scheme-theoretic later bands may compose to
   arcwise emptiness, but not automatically to reduced scheme structure.
6. The `a=2..5` and `a=6,7` hostile reviews are CONFIRMED, but no standalone
   promotion artifacts were found. Rehash their exact review SHAs and decide
   explicitly whether a single final composition promotion may import these
   reviewed results directly, or whether two narrow promotion artifacts must
   be written first. Treat this as lifecycle rigor, not automatically as a
   mathematical defect.
7. Independently inspect the frozen `a>=10` producer enough to decide whether
   the composition is at least conditional on its separate review. Do not
   import a producer PASS as already promoted.
8. Verify the residual list. This composition must not be called whole D1:
   `d=2,3`, `C2/R3/RC/A2` and equality faces, the `a=1` charts, positive-order
   `k10`, `p=0`, `k0=0`, zero/infinity, terminal/Taylor/lifecycle, and global
   landing remain outside unless separately promoted.

State the narrowest legitimate composition theorem and the exact lifecycle
steps required before promotion.
