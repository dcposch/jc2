# Selected-Q8 projective-specialization length lemma

Date: 2026-08-25  
Status: **PRODUCER-EXACT CONDITIONAL LEMMA; saturated-boundary endpoint pending**

## 1. Exact global construction

Let `k=F_127`, let `S=A1_w`, and write the eliminated localized selected-Q8
source in the seven internal affine coordinates

```text
(u,c,d2,d4,x1,x5,v),
x3=(v+2)x5,            u=inv*x5,
u*x5*v=1.
```

This is the same localized source as the full presentation.  Indeed
`v*x5=x3-2x5` and
`inv*x5*(x3-2x5)=1` imply that `v` and `x5` are units; hence
`u=inv*x5` has inverse change `inv=u/x5`, and its localizer becomes exactly
`u*x5*v=1`.

Embed the seven-dimensional affine internal chart into `P7` with homogenizing
coordinate `t`.  Homogenize each source polynomial in the internal variables
only, leaving `w` as a base coordinate, to obtain an ideal `J`.  Define the
global projective closure by

```text
C = J:t^infinity = eliminate(J+(z*t-1),z).              (1)
```

The order in (1) is load-bearing: saturation is performed over `k[w]` before
any specialization of `w`.

## 2. Conditional endpoint

Assume the exact saturated AWS calculation proves that, after setting
`w=25,t=0`, every one of the seven standard projective charts

```text
u=1, c=1, d2=1, d4=1, x1=1, x5=1, v=1
```

has unit ideal.  These charts cover `P6` at infinity, so the special fibre of
the global closure has no geometric boundary point.  Unit ideals over
`F_127` exclude points after algebraic closure as well.

Also consume the frozen full affine fixed-fibre calculation at `w=25`:

```text
dim X_25=0,       length(X_25)=190.                     (2)
```

The coordinate change above identifies that full fibre with the affine chart
of (1).

## 3. Properness and the length upper bound

Let `f:Xbar->S` be the projective morphism defined by `C`.  On `D_+(t)`,
global saturation changes no equation, so `Xbar` restricts to the original
affine localized source.  The assumed empty boundary over `25` and (2) imply
that the entire projective fibre `Xbar_25` is zero-dimensional of scheme
length `190`.

Upper semicontinuity of fibre dimension gives an open neighbourhood `U` of
`25` on which every fibre is zero-dimensional (or empty).  Thus
`f^{-1}(U)->U` is projective and quasi-finite, hence finite.  Localize at the
DVR

```text
R=k[w]_(w-25).
```

The finite morphism is represented by a finite `R`-algebra `M`.  Write its
finite-module structure as a free part of rank `r` plus `R`-torsion.  Then

```text
length_(k(w))(M tensor_R k(w)) = r
                            <= dim_k(M/(w-25)M)
                             = 190.                     (3)
```

No flatness is assumed.  Embedded or nilpotent generic structure contributes
to `r` and is counted in (3); vertical and torsion components supported at
`w=25` contribute only to the special fibre and can only increase its length.
Properness prevents a `w`-dominant component from avoiding the fibre by
escaping to infinity.

The original generic affine localized algebra is the `t!=0` open part of the
generic projective fibre.  Its finite length is therefore at most the total
generic length `r`, so (3) gives

```text
generic localized source length <=190.                 (4)
```

## 4. Pairing with the reviewed H component

The reviewed mod-127 component theorem and geometric integrality of the monic
`v`-degree-190 curve `H` independently give a generic source contribution of
at least `190`.  Combining that lower bound with (4) forces generic length
exactly `190`.  The separate conditional generic-length lemma then yields:

- multiplicity one and source degree one over `H`;
- a unique `w`-dominant geometric localized component; and
- all eight full corrected-Q8 contacts on that component.

This conclusion remains conditional until the saturated-boundary endpoint is
complete and frozen.

## 5. Saturation/base-change firewall

One must not specialize before saturating.  For example, the affine family

```text
(w-25)x-1=0
```

has empty affine fibre at `w=25`, while its global projective closure has an
infinite point above `25`.  Homogenizing the already specialized empty fibre
would erase exactly that escape.  The live AWS producer uses (1) first and
only then imposes `w=25,t=0`.

This lemma concerns one chosen projective closure.  A raw unsaturated
homogenization with apparent `t=0` components supplies neither a positive nor
a negative result; those components may be removed by (1).

## 6. Scope

Even a passing endpoint proves a characteristic-127 generic length,
degree-one, and all-contact statement only.  It does not by itself prove
regularity of every projective coordinate at every boundary, the repaired
characteristic-zero no-merger and integral-section hypotheses, identity with
the primitive-grouping/infinity components, Taylor realization, terminal
dynamics, a rational trajectory, maximum twelve, or JC2.
