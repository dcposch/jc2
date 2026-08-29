# Preregistration: V24R2 exact-Q chart properness and compatibility

Date: 2026-08-27

Status: **FROZEN BEFORE EXECUTION OR ALGEBRA.**

V24R1 proved that the frozen prior ideal localized at `k10_0*W` is the unit
ideal over `F_65521`; hence V24's two zero modular normal forms were vacuous.
That single bad-prime result does not decide the characteristic-zero ideal.

V24R2 takes the byte-frozen V24 script and changes only the coefficient
field declaration from `65521` to exact `Q`.  It keeps exactly the same 35
prior generators, the same localization generator

```text
zinv*k10_0*W - 1,
```

and the same exact grade-seven compatibility polynomials.  It computes a
tracked `liftstd(P,T)` with `option(redSB)` absent and must replay

```text
matrix(P)*T = matrix(G)
```

coefficientwise before any result is consumed.  A forced-unit mutation
`P+(1)` must reduce `1` to zero.

If `reduce(1,G)=0`, V24R2 must use `lift` and `T` to serialize an explicit
36-entry coefficient matrix `C` and replay

```text
matrix(P)*C = 1.
```

This outcome proves that the exact-Q prior prefix has no point on
`D(k10_0*W)`.  If instead `reduce(1,G)=1`, the ideal is proper and V24R2
reduces both exact compatibility polynomials.  If both reduce to zero, it
must serialize and replay a two-column coefficient matrix expressing them
in `P`; otherwise it must serialize the nonzero normal forms and the tracked
basis/transform needed to replay the standard-basis computation.

Allowed outcomes:

```text
PASS_Q_LOCALIZED_PRIOR_IDEAL_UNIT_CHART_EMPTY
PASS_Q_PROPER_C6_C7_EXACT_MEMBERS
PASS_Q_PROPER_COMPATIBILITY_NONMEMBERSHIP_NORMAL_FORMS
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

The run is one-core and bounded at 900 GiB virtual memory and six hours on
Box02.  Even an exact unit result eliminates only the normalized,
valuation-one, `k10_0!=0`, `W!=0` finite-prefix chart through grade six.  It
does not cover `W=0`, other valuation/unit strata, grades through 19, a full
jet or arc, K00 closure incidence, order two, maximum twelve, or JC2.
