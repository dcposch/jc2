# Result: weighted triple-root two-chart discriminator V10

Date: 2026-08-26 UTC

Status: **PRODUCER-TIER EXACT DUAL-AWS RESULT; HOSTILE REVIEW REQUIRED.**

## Exact endpoint

Use the weighted blow-up of `(a,h)=(0,0)` with

```text
wt(a)=1,  wt(h)=3.
```

Both AWS traversals reconstruct the same frozen 48-term V9 universal witness
of canonical SHA

```text
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0.
```

The ordinary charged source rows have exact weights

```text
row i: 12+i,  i=1,...,8,
```

so in particular the fixed target weights are 15, 18, and 20.

### The a-chart

Put `h=a^3*s` and normalize

```text
ell=wt(Lambda)-wt(a)>0.
```

For every one of the 48 terms, the coefficient of the axis valuation is
exactly zero.  The closed-corner margins have histogram

```text
margin 0:   32 terms,
margin 5/2: 11 terms,
margin 5:    5 terms.
```

The two distinguished zero-margin terms are the target and its positive
`tau` split.  Each of the other 30 zero-margin terms has a positive slope in
at least one of the open variables `u,v,eta,T,H`; hence every non-target face
term is strictly above the target in the registered open cell.  This is the
full finite-axis-valuation cone `wt(h)>=3 wt(a)` for the literal frozen V8
witness, not a check at one h grade.

For the residual cubic

```text
p=-3,  c=2+s,
```

the exact discriminant is

```text
-27*s*(s+4),
```

with canonical SHA

```text
a736793f95de15cd74b09ab6762ad56bdecee0b0dc6b9c65f569fc81d6a38dad.
```

Its two double-root values are `s=0` and `s=-4`.

### The h-chart

After adjoining a cubic root, put

```text
h=t^3,  a=t*b.
```

The residual cubic is

```text
z^3-3*b^2*z+(2*b^3+1),
```

and its exact discriminant is

```text
-27*(4*b^3+1),
```

with canonical SHA

```text
dca78309aeb09bf43aa2990ece43dfcb6a05bf7d11489090582f4be5d3b7c19f.
```

The checked ordinary homogeneity gives the exact scaling bridge
`row i -> t^(12+i) row i`, including target weights 15, 18, and 20.  Under
positive rescaled Lambda, the pinned reviewed squarefree order-20 theorem
therefore excludes the open residual locus `4*b^3+1 != 0` in this frozen
ordinary source.  On the exceptional divisor `4*b^3+1=0`, the overlap
coordinate is `s=b^(-3)=-4`.  The opposite-axis change

```text
a'=-a,  h'=h+4*a^3
```

preserves `p=-3a^2` and `c=2a^3+h`, so this exceptional direction is exactly
the `s=-4` a-chart boundary already identified above.

The V9 result and freeze consumed by the V10 source closure are exact.  The
separate later hostile V9 review is `UNIT_AXIS_COVARIANCE_CONFIRMED`, SHA

```text
f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226.
```

That later review is useful external ancestry, but the present V10 endpoint
remains provisional until its own different-model hostile review closes.

## Dual custody

| Host | Tag | Worker PID | Order | JSON SHA | Elapsed / max RSS / swaps |
|---|---|---:|---|---|---|
| Box03 `98.80.65.144` | `max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_box03_forward` | 165189 | forward | `ac7be9dce50c261117c37c8ddba9c477b0560d8a6363acd4adc52a8dedabf3dd` | 11.87 s / 22,368 KiB / 0 |
| r6d `100.26.198.153` | `max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_r6d_reverse` | 232475 | reverse | `9aaa0d14f93b168f12df60aa825bc58c3af03ad7e293cc47a54ebd60c96cf2ab` | 11.93 s / 21,932 KiB / 0 |

Both workers have rc 0, empty compiler stderr, exactly one compiler PASS,
successful source-closure checks, a `DONE` sentinel, and no `FAILED`
sentinel.  Deleting only the preregistered `tag` and `order` fields gives
identical sorted certificates of SHA

```text
25910f14424f0a021b00bf3d440b506b05aafc5c0980ee94beefe58608d5e12b.
```

The complete harvested remote-tree manifests have SHAs

```text
de2a59a2afa835dee1d8e444ee3fd2a4f26f60b44b370ed08a4dfebf0fd1f852  Box03
98f5ec6348349a310a9ea4f03ba0087a84d7951f0ab12f26de23b9eb2d620e57  r6d.
```

## Firewall

This is a directional weighted-blow-up result in the frozen ordinary
common-cubic source, with fixed loads in the V8 witness.  It requires
positive rescaled Lambda and the exact reviewed ancestry stated above.  It
does not cover the arc with `a=h=0` identically, nonpositive rescaled Lambda,
moving loads in the V8 witness, another source chart, or a global landing or
accessibility theorem.  It proves neither D1 nor JC2.

