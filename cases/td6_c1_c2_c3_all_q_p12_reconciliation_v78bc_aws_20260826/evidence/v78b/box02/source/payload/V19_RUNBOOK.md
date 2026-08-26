# TD6 V19 raw B3 birational discriminator

This bundle performs substantive exact arithmetic only on AWS.  It rebuilds
transport, the first affine band, genuine P12, and the original-row source
relation after an exact birational parametrization of the raw divisor

```text
B3=4C0^2U0^2-4C0V0^2U0+24C0U0^4+V0^4-20V0^2U0^3+20U0^6=0.
```

With independent chart variables `t,w`, put

```text
x=C0/U0^2=(-5t^2+20t-4)/(t-2)^2,
y=V0^2/U0^3=16t/(t-2)^2,
U0=w^2/y,  V0=w^3/y,  C0=xw^4/y^2.
```

The producer executable-checks `b(x,y)=0`, the original `B3` identity, both
inverse formulas, the line-intersection factorization, a plus-one negative
control, the `t=2` projective-infinity/base-point statement, and descent from
an unused third sentinel variable.  This is a parametrization, not a source
scaling or gauge normalization.  The only missed affine conic base point is
`(x,y)=(-5,0)`, which lies on the separately raw-closed `V0=0` divisor.

Run either or both deterministic first-pivot orders:

```sh
bash run_v19.sh ARCHIVE RUN_DIR PYTHON ascending EXPECTED_ARCHIVE_SHA256
bash run_v19.sh ARCHIVE RUN_DIR PYTHON reverse-first EXPECTED_ARCHIVE_SHA256
```

A successful calculation ends in
`TD6-C1-C2-C3-B3-BIRATIONAL-DISCRIMINATOR PASS`.  Promotion requires reading
the emitted `B3_expected_minus_k_over_50`, `B3_parameterized_open_killed`,
and complete certificate-chart factorization.  PASS alone never licenses a
whole-B3, three-center-family, SP2, or JC2 claim.
