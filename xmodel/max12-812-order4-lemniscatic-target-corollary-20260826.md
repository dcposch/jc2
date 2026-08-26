# Order-four residual Kummer target is lemniscatic

Date: 2026-08-26 02:24Z

Status: **EXACT HAND COROLLARY AT TARGET-CURVE SCOPE; SOURCE PROJECTION STILL OPEN**

## Charged theorem

The immutable residual-plane theorem
`xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md`
(SHA-256
`cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756`)
and its independent `CONFIRMED` review (SHA-256
`59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a`)
prove that the normalization `X` of the exact residual plane is a
geometrically integral genus-zero curve and that, over the algebraic closure,

```text
div_X(v)=8 P_0-P_ul-P_A-6 P_B,                         (1)
```

where the four displayed places are distinct.  The nonmutating tangent
coordinate erratum has SHA-256
`26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300`
and changes none of (1).

## Lemniscatic normal form

Work over `C`.  Since `X` has genus zero, choose a coordinate `t` with

```text
t(P_ul)=0,   t(P_A)=1,   t(P_B)=infinity.
```

Then

```text
div(1/(t(t-1)))=-P_ul-P_A+2P_B.
```

Subtracting this divisor from (1) gives

```text
div(v)-div(1/(t(t-1)))=8P_0-8P_B=4(2P_0-2P_B).        (2)
```

Every degree-zero divisor on `P1_C` is principal.  Hence there are
`g in C(X)^*` and `c in C^*` such that

```text
v=c*g^4/(t(t-1)).                                     (3)
```

On the Kummer curve `Y:y^4=v`, choose a fourth root of `c` and put

```text
xi=c^(1/4)*g/y.
```

Equation (3) becomes

```text
xi^4=t(t-1).                                          (4)
```

Thus the complete normalization of `Y` is geometrically isomorphic to the
fixed `(4,4,2)` Kummer curve (4); no coefficient of the original 18-term
plane remains in its geometric isomorphism class.

## Weierstrass model and differential

Put `W=2t-1`.  From (4),

```text
W^2=1+4xi^4.                                          (5)
```

On the common dense chart define

```text
X_E=2(W+1)/xi^2,        Z_E=4(W+1)/xi^3.              (6)
```

Direct substitution using `W^2-1=4xi^4` gives

```text
Z_E^2=X_E^3-16X_E.                                    (7)
```

Conversely `xi=2X_E/Z_E` and `W=X_E*xi^2/2-1`, so (6) is birational;
smooth projective completion makes it an isomorphism.  Therefore `Y` is the
lemniscatic elliptic curve and

```text
j(Y)=1728.
```

Differentiating (5) gives `dW=8xi^3 dxi/W`.  A direct differentiation of
(6) then yields the exact pullback identity

```text
dX_E/Z_E=-dxi/W.                                      (8)
```

The left side is a nonzero regular differential on (7), so (8) supplies an
explicit nonzero regular differential on the target Kummer curve.

## Source firewall and conditional consequence

If a relevant loaded order-four source component is proved to induce a
nonconstant map `P1_x -> Y`, then pulling (8) back gives a nonzero regular
differential on `P1`.  In characteristic zero a nonconstant curve morphism is
separable, so pullback of a nonzero differential is nonzero, whereas
`H^0(P1,Omega^1)=0`.  This is the same contradiction as the genus-one gate in
a smaller explicit form.

Nothing here proves that source map is nonconstant, that every source
component dominates `Y`, that `a6` is nonzero on every component, or that the
corrected source ideal is prime.  It does not by itself eliminate the loaded
order-four leaf, maximum twelve, or JC2.
