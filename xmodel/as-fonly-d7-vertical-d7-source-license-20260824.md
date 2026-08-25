# AS F-only `p=3,D=7`: full-`E1` source license for the D7 rows

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Result

This supplemental gate closes the sole source-scope gap in the frozen D7
cap-boundary producer.  In the charged vertical normal form, the exact
integer residual at order 27 is

```text
(det J-1)/27 = E1+M+3N,
E=L/3+K+C_x+D_y=3E1.                              (1)
```

At total degree seven, the replay proves directly over the integers that

```text
[E1]_7=[K/3]_7=[single-Frobenius K/3]_7.          (2)
```

Consequently the full degree-seven residual is exactly the `M+KFdiv` row
used by the frozen cap-boundary package.  After its registered accepted-row,
D8-pivot, and triangular-coordinate substitutions, the eight rows are

```text
2*fua*h,
fc*h+2*fua,
fc,
d6_1+2*fa*h,
R+fd*h,
2*fd,
d6_4+2*fb*h,
T+fb+fv*h.                                        (3)
```

Thus there is no mathematical source correction to the frozen D7 rows.  The
earlier freeze remains byte-preserved; this gate supplies the independent
full-`E1` license that its report did not spell out.

## Exact degree argument

Write the charged first digit as `U=U0+UF,V=V0+VF`, with
`deg(U0),deg(V0)<=4`, no degree-five layer, and homogeneous degree-six
Frobenius pieces `UF,VF`.  The current digit `C,D` has degrees six and seven.
The integer replay obtains

```text
deg(L/3)<=5,
deg(C_x+D_y)<=6,
deg K(U0,V0)<=6.                                  (4)
```

Every derivative of `UF,VF` is divisible by three.  The double-Frobenius
Poisson product is divisible by nine, so its quotient by three is zero
modulo three.  Therefore the only degree-seven part of `E/3` is the exact
single-Frobenius cross in (2).  This is a degree statement about the full
integer source, not an extrapolation from the reviewed D9/D8 generator.

The replay also constructs `M` once with `U,V` including all six Frobenius
directions and once with `U0,V0`; the two are equal modulo three because the
extra derivatives are three-divisible.  It then builds `[E1+M]_7` and only
afterward compares it to the frozen formula as a regression.

Deterministic internal hashes are

```text
[E1]_7:    c5e95b5ee9aeccfd44ce54e35a974cc65cf8fee23e9b15791ef2a24e900d428e
[E1+M]_7: 4cf87c8cd85756803b3fafea92618d65fe8d6629d68d8d8b95aa79b700c3dfb3
```

## Licensed and consumed artifacts

The predecessor source review is consumed at its exact D9/D8 scope:

```text
xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md
SHA-256 156053c538c4c826bc0feb345d25d91f015543464e0ab9d7734ab190cd7842c4
verdict CONFIRMED; degree seven explicitly excluded
```

The supplemented producer is

```text
xmodel/as-fonly-d7-vertical-d7-cap-boundary-20260824.md
SHA-256 3576de6cfba306230477fe7955e2ae159cc3dd241b4613b96d0ff57a05bbbfad
```

This source-license gate does not independently re-review the subsequent
seven-row census or 13-component stratified decomposition.  It licenses only
their eight source rows and the forced substitutions derived from them.

## Refusal scope

No lower residual, new order-27 digit, next divided carry, recurrence,
all-depth lift/no-lift, characteristic-zero, counterexample, or JC2 result is
claimed.  The finite census and component theorem retain the exact scope and
review status of their separate frozen producer.
