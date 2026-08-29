# Result: central-vertex retirement and moving-load discriminator V11

Date: 2026-08-26 UTC

Status: **PRODUCER-TIER EXACT DUAL-AWS RESULT; HOSTILE REVIEW REQUIRED.**

## Exact computational endpoint

Both registered AWS traversals reconstructed the literal V8/V9 witness,
restored the ordinary constant-field loads

```text
kbar=Lambda^6*k,
row 3 target=Lambda^15*mu,
row 6 target=Lambda^18*nu,
row 8 target=Lambda^20*(1+tau),
```

and verified all eight full-load row covariances under
`p=-3*a^2, c=2*a^3+h`.  Specializing `(k,mu,nu)=(0,2/3,0)` recovers the
frozen 48-term polynomial exactly, with canonical SHA

```text
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0.
```

The full constant-load universal witness has 62 terms and SHA

```text
c0f1552c06650e321db954ab99788324f59e52dea94fd8e7dfbdfbb3931aeab6.
```

Relative to the fixed witness, its 14 load-sensitive terms have canonical
SHA

```text
dbd78a81294d473aa043af6e0b0c87ce8050ae3e906a20d07395143d4371d75f.
```

Their parameter counts are `k:13`, `mu:0`, `nu:1`.  The absence of `mu` is
an exact consequence of the frozen row-3 multiplier being zero, not a
sampling claim.  Every load-sensitive term lies strictly above the target
at the closed corner: the minimum margin is 1; the single `nu` term has
margin 3; the `k` terms have margins 1, 7/2, or 6.  Thus no load term changes
the 30 old non-target zero-corner face terms.  The complete 62-term corner
histogram is

```text
0:32, 1:10, 5/2:11, 3:1, 7/2:2, 5:5, 6:1.
```

The obstruction list is empty.  The exact producer endpoint is therefore

```text
EXISTING_WITNESS_FULL_CONSTANT_LOAD_UNIFORM.
```

## Central vertex and rescaled Lambda

The pinned, hostile-reviewed exceptional-support theorem has SHA

```text
a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee.
```

It identifies the reduced strict coefficient-infinity support with the
common-cubic graph `P(2,3)`.  V11 independently checks that all eight boundary
coefficients vanish at `(p,c)=(0,0)`.  Consequently this point is the affine
cone vertex and the irrelevant point for `Proj`, not a strict
coefficient-infinity leading centre.  No separate central `a=h=0`
elimination is mathematically live in this frozen associated-graded chart.

On the nonzero discriminant-zero locus, `p=-3*a^2, c=2*a^3` has `a` nonzero;
after projective normalization `a` is a unit.  Hence a positive Rees/radial
Lambda still has positive rescaled valuation `v(Lambda/a)=v(Lambda)>0`.
The nominal nonpositive-rescaled-Lambda remainder is therefore not another
point of this strict projective chart.  If it arises from an arc with
`a,h` vanishing to higher order, the chosen leading coefficient vector is
zero and the arc must be regraded at its next actual coefficient order.  It
is a chart/order issue, not a missing V10 direction.  This inference is
provisional pending the V11 hostile review and is not a global no-arc
theorem.

The later V9 hostile review consumed as ancestry is
`UNIT_AXIS_COVARIANCE_CONFIRMED`, SHA

```text
f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226.
```

## Dual custody

| Host | Tag | Worker PID | Order | JSON SHA | Elapsed / max RSS / swaps |
|---|---|---:|---|---|---|
| Box03 `98.80.65.144` | `max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_box03_forward` | 168130 | forward | `bbd712444d8b6b3392ed0c2209f99e04f9b8d740b0e7e508a63c3eabdbc93be0` | 6.46 s / 22,340 KiB / 0 |
| r6d `100.26.198.153` | `max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_r6d_reverse` | 235150 | reverse | `0c6aca31fa67b11ad939f015e0786d9e6a72cf1527051a8e437f1bcc23379bcf` | 6.40 s / 22,480 KiB / 0 |

Both workers have rc 0, empty compiler and launch stderr, exactly one
compiler PASS, successful prelaunch and post-run source checks, a `DONE`
sentinel, and no `FAILED` sentinel.  Deleting only the preregistered `tag`
and `order` fields gives identical sorted certificates of SHA

```text
a4f7c47b7f57e6dea9cecd89a74d4b7b4ac80a59abad431dfe3a64260b142477.
```

The complete harvested remote-tree manifest SHAs are

```text
ea47f554dcbf381d699449f81d74674b6bb8e6f45b7afd5b41f0cc7cfc76849b  Box03
bb0ac5f6d29afac55eebf3f45cc555cdc73cbdd6aae1a558f1f759466beba55f  r6d.
```

## Firewall

The exact uniformity statement treats `k,mu,nu` as arbitrary elements of the
constant field.  It does not treat loads that are themselves formal series.
The projective retirement applies only to this reviewed strict
coefficient-infinity associated-graded chart; regraded higher-order source
strata, another source chart, landing/accessibility, D1, and JC2 remain open.
