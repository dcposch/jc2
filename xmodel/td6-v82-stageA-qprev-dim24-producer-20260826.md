# TD6 V82 Stage-A producer theorem: `Q_prev=Q`, dimension 24

Date: 2026-08-26

Status: **PRODUCER-EXACT; DUAL AWS; HOSTILE REVIEW PENDING.**

## Theorem (strict scope)

On the common symbolic-center source presentation over `K=E(C,V,U)` and on
the common localization where the reviewed transport/FIRST/previous-pole
echelons are defined, let

```text
Q = span_K(q2..q14,q16..q24,d10,d15).
```

The exact previous/pole linear compatibility map restricts to zero on `Q`.
Consequently

```text
Q_prev = ker(L_prev|Q) = Q,       dim_K Q_prev = 24.
```

The producers conservatively declare `D(U*(C-3U^2)*B3)`.  This theorem does
not identify that declared chart with the intrinsic FIRST rank-38 open.  If
V83 emits additional pivot/minor factors, the theorem is read on the
intersection with V83's explicit principal open; every rank-drop factor stays
raw-fibre debt.

## Exact evidence

The 22-axis V82Q run gives base previous/pole rank `38/94`, one base dependent
row, and an exactly empty conormal table:

```text
PREVIOUS_POLE_conormal_rank=0/22
PREVIOUS_POLE_conormal_kernel_dimension=22
PREVIOUS_POLE_denominator_factor=(1, [])
table SHA  b1b1f6980b03fb5ea4695ba82eb3fc628db410e1fc7932161c2a1ca29352cb30
kernel SHA ef4d3be85c40e12582c80963eb36e9e3ff843ec4c239679d0060ff873c4905bb
source SHA cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579
```

Both r6d and Box03 wrote byte-identical tables and kernels.  The current-stage
continuation was still live at harvest; only the already completed and fully
written previous/pole checkpoint is consumed here.

The V82P3 dead-stretch shards independently finish rc0 on both hosts.  For
`d10`, the raw previous/pole column has 1,115 nonzero pre-elimination entries,
SHA `86e61fc...`; for `d15`, 980 entries, SHA `90e13af...`.  After exact
source-replayed elimination each has conormal rank `0/1`, zero coordinates,
and unit denominator.  Their common header-only table SHA is
`2c0e79ec04b6e8cfc4da5ca71454e2b27aac9ad2fa20a13a97b3066947f76400`.
The byte-identical source archive SHA is
`1a23ceca70fa65b7907e301972356db899b28f1a5ff7e91f52d397fede2b24a6`.

Because the compatibility map is `K`-linear and all 24 basis columns vanish,
the composition conclusion is exact; no one-ring recomputation is needed for
logical completeness.

## Controls and refusal scope

- all 3,470 original transport pivot rows replay;
- all 38 FIRST and 38 previous/pole pivot combinations replay;
- q direct-source omission controls and dead raw-source omission controls are
  nontrivial;
- typed `AxisJet` composition preflight passes for each dead axis;
- the empty-table reporter positive control uses the actual field unit;
- symbolic centers remain `(C,V,U)`.

This theorem is first-order and fixed-presentation only.  It licenses the
quadratic map `Sym^2(Q_prev)->C_prev`; it does not assert that the quadratic
map vanishes, that a nonlinear family exists, or that TD6/SP2/JC2 is resolved.

