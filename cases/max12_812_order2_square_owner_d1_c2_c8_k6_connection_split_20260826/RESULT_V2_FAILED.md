# V2 no-verdict: D1 primary-C2 `c=8` connection split

Date: 2026-08-26

Status: **FAILED OVER-STRONG SENTINEL; NO CELL VERDICT.**

Exact Q, `F_65519`, and `F_65521` compiled and executed the same frozen V2
source with rc zero and zero swap.  All source, inventory, grade-25/26,
moving-connection, chart-unit, root-square, and negative-control checks passed
except one:

```text
C2C8_ROOT_FABER=0.
```

V2 incorrectly demanded equality between the grade-26 fixed-root Faber
evaluation and the moving-connection analytic numerator before applying the
preregistered scheme split `D(k60) union V(k60)`.  The moving root contributes
a term proportional to the earlier grade-25 `k60*C/L` column, so this
unconditional equality is not licensed.  Consistently, the independently
compiled checks already show all of the following in every characteristic:

```text
C2C8_G25_K60_C_EXACT=1
C2C8_CONNECTION_MINUS3_OVER4=1
C2C8_D_K60_BOTH_C_CHARTS_UNIT=1
C2C8_V_K60_ROOT_SQUARES=1
C2C8_V_K60_BOTH_C_CHARTS_UNIT=1
```

Thus the only failing condition is an over-strong pre-split bridge.  It does
not refute the chamber argument, but V2 is quarantined as no-verdict because
its fail-closed validator correctly rejected the endpoint.  The repaired
client must require the root bridge only after adjoining `k60=0` and retain a
negative sentinel showing that the unconditional moving-root gap is nonzero.

The three retrieved V2 trees are frozen by `EVIDENCE_V2_FAILED.sha256`; the
source is frozen by `FREEZE_V2_FAILED.sha256`.  Neither file licenses an
emptiness claim for `c=8` or any neighboring contact.
