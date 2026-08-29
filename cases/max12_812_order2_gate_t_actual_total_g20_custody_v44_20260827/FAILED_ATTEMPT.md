# V44 failed-closed attempt

Date: 2026-08-27

The first exact-Q (`r6a`) and `F_65521` (`r6b`) executions completed the
general-`rho` grade-20 expansion and serialized all seven rows, then failed
closed at the same over-strong postcondition:

```text
terminal receiver absent from all rows:
ac15,az15,cs18,ec15,ell20,ez15,k10_16,k2,k6_8,rs18
```

Those ten variables are present at the terminal positions of the constructed
source/load series, as required, but none occurs in any grade-20 row.  The
pre-registration did not require row occurrence; it required correct source
depth.  Thus this is a validator-design failure, not a mathematical verdict
and not evidence that `ACT-TOT-G20` failed.

The attempt is preserved byte-for-byte in `failed_v1_aws_q_r6a/` and
`failed_v1_aws_p65521_r6b/`.  Both processes returned `rc=1`, emitted no
PASS banner or result manifest, used zero swap, and peaked at about 226 MiB
RSS.  The additive V44R1 successor reverses only this false postcondition:
it requires and records terminal-receiver absence while retaining every
source, prefix, face-bridge, homogeneity, parity, and row-custody gate.

No row hash from this failed attempt is promoted on its own.

