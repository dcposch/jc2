# D3 Halphen global positive control and ramification obstruction

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `effb538eb858ff2c51d713a91f392d90796e786e`  
Lifecycle: **EXACT GLOBAL CONTROL / CONDITIONAL FIRST-LEG EXCLUSION**

## 0. Decision

The bihomogeneous closure of the promoted local critical control,

```text
X: (Sx+Tz)^3+T*S^2*y^3+T^3*x^2*z=0
   in P2_[x:y:z] x P1_[S:T],                         (0.1)
```

is an integral normal class-`(3,3)` surface.  Projection to the first factor
is finite flat of degree three.  Its only total-space singularities are the
marked level-two point over `T=0` and one `D4` point over `S=0`.  Thus this is
a genuine global surface control for the local D3 Halphen survivor, rather
than merely a finite formal jet.  This statement does not by itself identify
the full GR divisor, prove rationality or certify occurrence in the promoted
four-row theorem.

The control nevertheless cannot be an actual proper block.  On a dense
target chart, a component of the ramification divisor has normalization the
connected cyclic cubic cover

```text
y^3 = -3*q^2*(2*q^2+3)^4 / (4*(q^2+1)).              (0.2)
```

It is branched at six points and has genus four.  In an actual block the
everywhere-defined etale first leg lands in the complement of the second-leg
ramification divisor.  The complete genus-four closure would therefore be a
boundary component, contradicting the corrected morphic rational-forest
theorem.  This provides an independent global failure mode for the sharp
control; the universal weighted exceptional-curve obstruction remains the
stronger family-wide theorem.

## 1. Finite normal global closure

Regard (0.1) as a binary cubic in `[S:T]`.  Its four coefficients are

```text
x^3,
3*x^2*z+y^3,
3*x*z^2,
z^3+x^2*z.                                             (1.1)
```

They have no common projective zero: the first forces `x=0`, the second then
forces `y=0`, and the fourth forces `z=0`.  Hence

```text
pi:X -> P2_[x:y:z]
```

is finite.  The hypersurface is Cohen--Macaulay and the target is smooth of
the same dimension, so finite miracle flatness gives flatness; the generic
degree is three.

On `S=1`, write `t=T/S`.  The equation is

```text
F=(x+t*z)^3+t*y^3+t^3*x^2*z.                          (1.2)
```

At `t=0`, its only total-space singular point is `[x:y:z]=[0:0:1]`.
For `t!=0`, `F_y=3*t*y^2` forces `y=0`, and `z=0` is impossible.  Put
`z=1`, `x=t*(r-1)`.  The scaled `x`- and `z`-derivatives are

```text
3*r^2+2*t^2*(r-1),
3*r^2+t^2*(r-1)^2,
```

whose difference is `t^2*(r-1)*(r-3)`.  The first expression is nonzero at
`r=1`; at `r=3` its vanishing requires `t^2=-27/4`, where the scaled base
derivative is `-18`.  Thus there is no other finite-chart singularity.

On `T=1`, put `u=S/T`.  At `u=0`, the derivative equations have the unique
solution `[x:y:z]=[0:1:0]`.  In the chart `y=1` the local equation begins

```text
u^2+z^3+x^2*z + terms of ordinary degree at least four. (1.3)
```

The cubic `z*(z^2+x^2)` has three distinct tangent lines, so (1.3) is the
standard `D4` suspension.  The singular locus is therefore precisely the two
points above.  The `(3,3)` divisor is ample and hence connected.  If it were
reducible, distinct components would meet and their intersection would lie in
the singular locus; if it were nonreduced it would be singular along a
component.  Either case would give a positive-dimensional singular locus, so
`X` is integral.  As a hypersurface it is `S2`, and its isolated
singular locus gives `R1`, so `X` is normal.

At the marked finite point, setting `z=1` and `X_1=x+t` gives

```text
X_1^3+t*y^3+t^3*X_1^2-2*t^4*X_1+t^5.                 (1.4)
```

For weights `(5,4,3)` on `(X_1,y,t)`, the exact weight-15 face is
`X_1^3+t*y^3+t^5`.  This is the already promoted sharp critical local
control `alpha=0,eta=1`; it does not turn global closure into a polynomial
map or prove the row's global occurrence theorem.

## 2. Coefficient-base checks

Direct Hessian-pencilling in the finite coefficient-base chart gives

```text
c4=0,
c6=216*t^12*(4*t^2+27),
Delta=-27*t^24*(4*t^2+27)^2.                          (2.1)
```

At coefficient-base infinity the corresponding formulas are

```text
c4=0,
c6=216*u^4*(27*u^2+4),
Delta=-27*u^8*(27*u^2+4)^2.                           (2.2)
```

Removing the exact level-two factor at `t=0` leaves invariant valuations
`(ord(c6),ord(Delta))=(0,0)`.  The two roots of `4*t^2+27` have `(1,2)`,
and infinity has `(4,8)`.  The resulting minimal discriminant-degree checksum
is twelve.  These reproduce and extend the earlier hostile review's global
control audit.  They are compatibility data, not a standalone proof of the
surface's relative minimal model, multiplicity index or GR trace.

## 3. Exact ramification component

Restrict the finite projection to the target chart `z=1`.  Ramification of
the binary cubic is cut out on `X` by `F=F_t=0`.  Eliminating `y^3` by
`F-t*F_t` gives the integral rational base curve

```text
(x+t)^2*(x-2*t)-2*t^3*x^2=0.                          (3.1)
```

It has the birational parametrization

```text
r=2*q^2+3,
x=r*q,
t=r*q/(r-1),
q=x*t/(x+t).                                          (3.2)
```

Substitution in `F_t=0` yields (0.2).  Modulo three, the valuations of its
Kummer function are

```text
q=0:                         2,
the two roots of 2*q^2+3:    1,
the two roots of q^2+1:      2,
q=infinity:                  1.                       (3.3)
```

The supports are pairwise disjoint.  Since at least one valuation is not
divisible by three, the cubic Kummer cover is connected.  All six listed
places are totally ramified, and Riemann--Hurwitz gives

```text
2*g-2 = 3*(-2)+6*(3-1)=6,
g=4.                                                       (3.4)
```

This is the normalization genus of the complete projective closure of that
ramification component.  If (0.1), restricted over an affine target plane,
were the second leg of an actual proper block, the first-leg image would be
smooth and disjoint from ramification.  On a common SNC completion the
strict transform of this complete curve is therefore boundary.  Its positive
genus contradicts the morphic rational-forest theorem.  No assertion based
only on abstract rational domination is used.

## 4. Replay and custody

The exact replay is

```text
be9551b7a19d0cf72e8c1f189771b92c78496cf111b578925b65c56957b65485
  ops/d3_halphen_global_control_replay.py
```

Under `uv run --with sympy==1.14.0`, ordinary, `-O`, and `-OO` modes return
byte-identical 1,148-byte canonical JSON with SHA-256

```text
ee77940abb31d00eb90880a75f5cbec708e0b7f445757fa96ddde62963650c20.
```

The source has zero AST `assert` nodes.  Mutation
`--mutate-kummer-denominator` exits nonzero with

```text
FAIL:ramification Kummer function drifted
```

The replay derives polynomial identities, singular-locus certificates,
invariants, parametrization and the Kummer branch ledger.  It invokes standard
finite miracle flatness, `S2+R1`, the `D4` tangent-cone criterion and
Riemann--Hurwitz at the report layer.  It does not prove a block exists, build
an etale first leg, construct a Keller map, prove primitivity, or resolve JC2.

## 5. Maximum-safe conclusion

The local critical survivor has a finite flat integral normal global
class-`(3,3)` closure with exactly the two stated singularities.  Its dense
ramification component has normalization genus four.  Consequently this
specific global control cannot occur as an actual proper intermediate block
with the promoted everywhere-defined etale first leg.  The computation is a
sharp positive control for surface/local realizability and a negative control
for the block interface; it neither proves that every local survivor attains
a global surface nor replaces the universal weighted-boundary obstruction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7859`.
- Body SHA-256:
  `47791910632b8985b9d6bebc116c0bfc2fc0575222fcb590431b24b9ac3739cd`.
- Frozen basis: `effb538eb858ff2c51d713a91f392d90796e786e`.
