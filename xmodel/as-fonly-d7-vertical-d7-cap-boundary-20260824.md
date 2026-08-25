# AS F-only `p=3,D=7`: exact D7 cap-boundary successor

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Headline

Starting from the source-corrected and different-model-confirmed vertical D8
gate, the literal integer Jacobian gives eight degree-seven rows.  They force

```text
fua=fc=fd=R=0,
T+fb+fv*h=0,
d6_1=fa*h, d6_4=fb*h.                              (1)
```

After (1), the D8 core becomes a seven-equation scheme in the eleven
variables

```text
(P,Q,s,w,h,fa,fb,fv,X0,X1,X2).                     (2)
```

Its exact literal-F3 census is `1245/6561` compatible states and `3507`
compatible digit points.  This is a one-row shrink, not an empty gate: the
old 3-, 9-, and 729-fibre representative choices pass, while the chosen
81-fibre representative fails exactly the last equation in (1).

The geometric support has exactly thirteen global minimal components:
eight closures of the `h!=0` localized components and five genuinely new
`h=0` components.  A sixth minimal prime of the special fibre is the fibre
of one of the eight global components and is therefore not globally
minimal.  This is a minimal-prime statement only; the original seven-row
ideal, not its radical, remains the source scheme.

No next carry, recurrence, all-depth lift/no-lift, characteristic-zero,
counterexample, or JC2 conclusion is made.

## 1. Licensed source

This successor consumes the frozen source-corrected D9/D8 gate and its
different-model source review:

```text
xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md
SHA-256 9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8

xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md
SHA-256 156053c538c4c826bc0feb345d25d91f015543464e0ab9d7734ab190cd7842c4
verdict CONFIRMED/PROMOTE at exact D9/D8 source scope
```

It also consumes the independently reviewed polynomial state theorem for the
displayed D8 core:

```text
xmodel/as-fonly-d7-vertical-state-sufficiency-20260824.md
SHA-256 410235081a54470a377d8d107a1982d34d507040718b945d11ee99dc4d1e5fe4

xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md
SHA-256 6ab373bf9214c54f506cd368473aff02ed472a20e9797037f83a9745c384bc17
verdict CONFIRMED at the displayed-matrix/state-theorem tier
```

The source review explicitly says that degree seven was not examined; the
present package derives it afresh.

## 2. Integer source and the eight D7 rows

Use the corrected source notation

```text
Pmap=x-x^3+3U+9C, Qmap=y+3V+9D,
M=(U_x-x^2)D_y+C_xV_y-U_yD_x-C_yV_x,
```

and split `U=U0+UF`, `V=V0+VF`, where

```text
UF=fua*y^6+fa*x^3*y^3+fb*x^6,
VF=fc*y^6+fd*x^3*y^3+fv*x^6.
```

The replay constructs the exact integer difference

```text
[K(U0+UF,V0+VF)-K(U0,V0)]/3 mod 3                 (3)
```

before any mod-3 simplification, adds it to `M`, and compares every
coefficient with the frozen corrected generator.  It then applies only the
registered accepted-row, D9, D8, and triangular-coordinate substitutions.
The resulting rows, from `y^7` through `x^7`, are

```text
2*fua*h,
fc*h+2*fua,
fc,
d6_1+2*fa*h,
R+fd*h,
2*fd,
d6_4+2*fb*h,
T+fb+fv*h.                                         (4)
```

Thus (1) follows over a field.  Omitting (3) while retaining all later
coordinate/pivot substitutions changes all eight rows, providing a negative
source control.

## 3. Exact joint scheme

Put `fv=fvb`.  Rename the three surviving D8 source variables
`(d7_1,d7_4,d7_7)=(X0,X1,X2)`.  After (1), the seven D8 equations are

```text
e0=2P X0+2P fa s+h^3 s^3,
e1=2P X1+2P fa w+2P fb s+2P fv h s+2Q X0+2Q fa s
   +2fv h^3 s^2,
e2=2P X2+P fb fv+2P fb w+P fv^2 h+2P fv h w+2Q X1
   +2Q fa w+2Q fb s+2Q fv h s+fa fb^2+2fa fb fv h
   +fa fv^2 h^2+fv h^3 s w,
e3=2Q X2+Q fb fv+2Q fb w+Q fv^2 h+2Q fv h w
   +2fv h^3 w^2+h^3 w^3,
e4=2X0 h^3+fa h^3 s,
e5=2X1 h^3+fa h^3 w+2fa s+fb h^3 s+fv h^4 s,
e6=2X2 h^3+2fa w+2fb fv h^3+fb h^3 w+2fv^2 h^4
   +fv h^4 w.                                      (5)
```

The replay reconstructs (5) symbolically from the frozen D8 matrix and
column after the independently derived substitutions (1); the displayed
rows are not an untyped hand transcription.

## 4. Component support

Over `F3(h)`, the last three rows of (5) solve `X` uniquely.  Eliminating it
leaves four equations in `(P,Q,fa,fb,fv,s,w)`.  Direct `minAssGTZ` gives
exactly eight minimal primes: six of dimension three over `F3(h)` and two of
dimension four.  Their graph closures have global dimensions four and five.
The complete bases, including the large generic component, are emitted by
the portable Singular replay.

At `h=0`, direct `minAssGTZ` on the ten-variable special fibre gives the
following six minimal primes (restore `h` to every displayed ideal):

```text
H1=(X0,fa,wX1-fvX1-sX2,wfb-fbfv+X2,sfb+X1),
H2=(X2,X1,X0,fb,w,s),
H3=(X1,X0,w,s,Q,fa fb^2+P fb fv-P X2),
H4=(X0,w,s,P,fb fv-X2,Q fv X1-fa fb X2,fa fb^2-Q X1),
H5=(fa,Q,P),
H6=(fb,w,s,Q,P).                                  (6)
```

Their dimensions are

```text
6,4,4,4,7,5.                                       (7)
```

In particular, `H2` is

```text
(X2,X1,X0,fb,w,s).                                 (8)
```

After restoring `h`, (8) is exactly the special fibre of the global prime

```text
(s,w,fb+h*fv,X0,X1,X2).                            (9)
```

The two global dimension-five closures are exactly (9) and
`(s,fa,fv-w,X0,X1,X2)`.  Neither is contained in `H3` or `H4`, as checked
by nonzero ideal remainders.  A global dimension-four prime cannot be
strictly contained in a dimension-four prime supported on `h=0`.
The primes `H1,H5,H6`, of dimensions `6,7,5`, cannot strictly contain any
localized closure, whose global dimension is at most five.  Therefore,
without assuming a direct full-ring decomposition, the global support is
exactly the eight localized closures plus `H1,H3,H4,H5,H6`: thirteen
minimal components, with dimension histogram

```text
dimension 4: 8, dimension 5: 3, dimension 6: 1, dimension 7: 1.
```

The case also preregisters three optional direct eleven-variable
minimal-associated-prime runners (SL/subsystem and two characteristic-set
orders).  They are independent regressions of the proved stratified count;
their completion is not consumed by this freeze.

## 5. Literal-F3 census

Regard (5) as seven affine equations in `X0,X1,X2`.  Exhausting all
`3^8=6561` assignments to `(P,Q,s,w,h,fa,fb,fv)` gives

```text
(rank A,rank[A|b])   states
(0,0)                    87
(0,1)                   156
(3,3)                  1158
(3,4)                  5160.                       (10)
```

Hence there are `1245` compatible base states.  Counting each kernel gives
`87*27+1158=3507` compatible digit points.  By `h`, the state/point counts
are

```text
h=0: 831 / 3093,
h=1: 207 / 207,
h=2: 207 / 207.                                    (11)
```

At `h=0`, the rank-zero compatible bases are exactly

```text
P=Q=0 and [fa=0 or (fb=s=w=0)].                    (12)
```

The two pieces in (11) contain `81` and `9` points with a three-point
overlap, hence `87`.  They are the literal-F3 footprints of the dimension
seven and dimension five boundary components.

The projection histogram (number of compatible `(fa,fb,fv,X)` points over
each `(P,Q,s,w,h)`) is

```text
0:60, 1:44, 2:4, 3:24, 5:8, 7:4,
9:64, 11:12, 15:10, 27:4, 243:8, 405:1.            (13)
```

The state and full-point stream SHA-256 values are recorded in the freeze.

## 6. Controls and refusal scope

Four frozen corrected-D8 representatives are evaluated before any cleared
or radical equation.  The 3-, 9-, and 729-fibre choices satisfy (4) and (5).
The chosen 81-fibre point fails only

```text
T+fb+fv*h=1.                                       (14)
```

Thus this row genuinely shrinks the accepted set but does not kill it.  The
already reconstructed 9- and 729-fibre integer maps remain terminal at the
following carry because of their degree-eight residual; their present-row
survival does not overturn that pointwise fact.

The finite census is literal `F3`, not an algebraic-closure count.  The
minimal-prime computation describes geometric support but does not replace
the original ideal by its radical and makes no primary/nonreduced claim.
Nothing here advances a surviving point through the next divided carry.
