# Corrected-Q8 rank-drop line: slope-three candidate and unramified obstruction

Date: 2026-08-25  
Status: **PRODUCER-EXACT; REVIEW PENDING**

## Scope

This report uses only the hash-pinned six divided source rows
`(e1,e3,e5,e7,e2,e4)` near the finite unloaded overlap.  It identifies the
first selected weighted candidate on the exceptional normal-rank value and
excludes its continuation only in the unramified chart `x5=t`.  Arbitrary
ramification, earlier coefficient drift, full selected saturation,
coefficient infinity, Taylor/terminal realization, and trajectories remain
charged.

## Exact weighted candidate

Write

```text
d4=b,
d2=b+1+Q1*t,
x5=z*t+Z2*t^2,
x3=z*t+X2*t^2,
x1=U2*t^2,
w=W*t^3.
```

After substituting into the original six rows, taking precisely the
preregistered upper/lower coefficients, and saturating by `z`, two
independent exact-Q AWS engines prove that the resulting ideal is exactly

```text
b-1,
U2,
3*Q1-(3*c-1)*z,
3*(X2-Z2)+z^2,
9*W-2*z^3.
```

Thus slopes one and two do not exhaust the normal geometry: a genuine
leading slope-three candidate exists, necessarily at

```text
(d2,d4)=(2,1),
Q1=(c-1/3)z,
X2-Z2=-z^2/3,
W=2z^3/9.
```

Since `z!=0`, both `w` and the leading selected factors `x5` and
`x3-2*x5` are nonzero in the punctured chart.

## Exact next-row obstruction in the unramified chart

Normalize `x5=t` and substitute

```text
c_src=c+C1*t,
d4=1+B1*t+B2*t^2,
d2=2+(B1+c-1/3)*t+(B2+Q2)*t^2,
x3=t-t^2/3+X3*t^3,
x1=U3*t^3,
w=2*t^3/9+W4*t^4.
```

With `A=C1-Q2`, the exact `t^3` coefficients of `e1,e5,e7` generate the
same ideal as

```text
9*(A+U3)+c+1,
-26*c-27*B1+9*(A+U3)-15,
83*c+81*B1+18*(A+U3)-58.
```

The first two give `B1=-c-16/27`; reducing the third gives exactly `-108`.
The ideal is therefore unit.  The slope-three candidate has no ordinary
power-series continuation with `ord(x5)=1`.

This is not yet a general ramified-arc exclusion.  If `ord(x5)>1`, changes
in `c,d4,d2-d4-1` can occur before the first `x5` term and are not licensed
by the normalization above.  The separately running full `b=1` selected
saturation is the decisive arbitrary-ramification gate.

## Exact endpoints

Accepted V3 endpoints:

```text
Box02 std/dp:
  input  303590394dd4df74c46cf6cf09c50beab32141703a740098c187f07774f47d82
  stdout 598a2e9c1f02b48101e9c4d8c77208af9134603ef219be1363ff17b2c3eff4a8

Box03 slimgb/block:
  input  45da37167d5624219feeb40f9227d95c6e166c3c1ee5e30275c6a0a4010a57de
  stdout f31cc2861dfc6458b15dc2776ef6c6f9d5f5efa6edcd97802665fac080f2576c
```

Both print `leading_ideal_identity=1`,
`actual_expected_ideal_identity=1`, `continuation_unit=1`, and
`third_residual=-108`, without banned diagnostics.  The AWS-only replay
returns

```text
Q8_W0_RANKDROP_SLOPE3_CONTINUATION_V3_REPLAY_PASS
```

with stdout SHA256
`8da3e2ec282a5688e020180a286413287ce53f94f478a330f9e93946208cf05b`.
V1 and V2 are retained as fail-closed controls: V1 had invalid ideal syntax;
V2 correctly proved the continuation obstruction but compared the leading
chart before removing the excluded `z=0` component.

