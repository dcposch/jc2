# Failed/no-verdict attempts

Date: 2026-08-26

## V1: overstrong ordinary-part equality

V1 ran under the three fresh AWS tags

```text
max12_812_order2_square_d1_tied_a1c5r2_maxpole2_q_box02_20260826T1929Z
max12_812_order2_square_d1_tied_a1c5r2_maxpole2_p65519_box03_20260826T1929Z
max12_812_order2_square_d1_tied_a1c5r2_maxpole2_p65521_r6d_20260826T1929Z
```

All engines returned `rc=0`, used about 20 MiB RSS, and produced the same
Singular stdout SHA

```text
292e1c0a0d37ff6475e58cdf03132dbab4d80ce93d2ccffdbbbfa6e6a2775475.
```

Every substantive source/root check passed: four-family census, padded
cutoff, seven literal rows, recursive source extraction, target firewall,
pole-two recurrence, both root Faber identities, derivative-row syzygy, all
four root-value charts, both exact `L` quotients, both quotient/derivative
terminals, exact unit ideals, and the omitted-`R3` negative control.

The fail-closed validator nevertheless rejected all three runs at

```text
T15_COMMON_N2=0.
```

V1 had required literal equality between the negative Laurent-tail numerator
reconstructed from the Faber rows and the full cleared numerator.  This is
too strong: the ordinary polynomial part is discarded by the Laurent/Faber
tail, so the invariant is equality modulo `L^2`.  A separate exact-Q AWS
diagnostic on the frozen V1 output gave

```text
T15_DIAG_MOD_L2=1
T15_DIAG_EXACT_QUOTIENT=1.
```

Thus this is a normalization/sentinel defect, not evidence against the
root obstruction.  V1 remains **NO VERDICT** and must never be cited as a
producer PASS.  V2 retains the discarded ordinary quotient explicitly and
changes no root functional, allocation equation, terminal, localization, or
scope.

The immutable V1 source archive has SHA

```text
e564be31b404940e59c5433382bc2f810270c6288954d569b5380236549afef1.
```

The V1 source snapshots are pinned by `FREEZE_V1_FAILED.sha256`; the three
retrieved evidence directories are named `aws_v1_failed_*`.
