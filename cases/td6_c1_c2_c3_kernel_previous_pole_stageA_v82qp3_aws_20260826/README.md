# TD6 V82 Stage-A previous/pole kernel composition

This immutable package composes two exact AWS calculations on the same
symbolic-center source presentation over `K=E(C,V,U)`:

- V82Q: all 22 licensed q axes
  `q2..q14,q16..q24` have zero previous/pole conormal; and
- V82P3: each of `d10,d15` has zero previous/pole conormal.

The underlying previous/pole equations have base rank `38/94`.  V82Q has one
base dependent row, but its complete 22-axis coefficient is zero.  V82P3 has
zero dependent rows after its typed source lift.  All 24 columns therefore
vanish, so the linear map on

```text
Q = span(q2..q14,q16..q24,d10,d15)
```

is zero and `Q_prev=Q` has dimension 24.

The conclusion is conditional on the common symbolic-center localization
used by the two producers.  Their conservative declared chart is
`D(U*(C-3U^2)*B3)`.  The separate V83 rank-open audit may replace this by an
explicit principal open; this package does not identify the two opens or
claim anything on a rank-drop divisor.

V82Q was still advancing through the current stage when this Stage-A
checkpoint was harvested.  Its previous/pole table and kernel were already
fully written and byte-identical on r6d and Box03; this package consumes only
that completed stage, not a final V82Q process verdict.  Both V82P3 axes
finished rc0 independently on both hosts.

This is a first-order source-incidence theorem.  It licenses computation of
the quadratic previous/pole Kuranishi map on `Q`; it is not itself a
quadratic survivor, family, full TD6, SP2, or JC2 statement.

