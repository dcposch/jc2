# D3 sectioned one-support global control and genus-two ramification obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `adb7d06a166bd15f82203fcc1342cbb882a61764`  
Lifecycle: **EXACT GLOBAL CONTROL / CONDITIONAL PROPER-BLOCK EXCLUSION / REVIEW REQUIRED**

## 0. Verdict and scope

The corrected local degree-cap counter-control has the following
class-`(3,3)` closure:

```text
X: G=(Sx+Tz)^3+S^2*T*y^3+T^3*x^2*y=0
   in P2_[x:y:z] x P1_[S:T].                           (0.1)
```

This global surface is integral and normal, and projection

```text
pi:X -> P2_[x:y:z]                                    (0.2)
```

is finite flat of degree three.  The other projection has a section and its
smooth minimal model is the rational elliptic surface with Weierstrass generic
fibre

```text
V^2=U^3-t^4.                                          (0.3)
```

Its singular fibres are `IV*` at `t=T/S=0` and `IV` at infinity.  The only
singularities of `X` are the exact level-two point
`p_0=(T=0,[0:0:1])` and an `A_2` point
`p_infinity=(S=0,[0:1:0])`.  The exceptional boundary over `p_0` is a
rational tree, despite local geometric genus two.  Thus local normality,
solubility, raw degree three, additive reduction, and rational-forest topology
do **not** eliminate the sectioned one-support row.

The binding D3 Hodge-divisor theorem applies because `X` is rational.  It
therefore identifies this as a genuine surface-level positive control for

```text
m=1,       T=2*t_0,       D=-2*F_(t_0),       rho(Y)>=12. (0.4)
```

This does not make (0.1) an intermediate surface of a proper block.  In fact,
a complete residual component of `Ram(pi)` has normalization of genus two.
If the restriction of (0.2) over an affine target plane were globally the
second leg of an actual proper block, the promoted everywhere-defined etale
first leg would miss this curve.  Its strict transform would then be a
positive-genus boundary component, contradicting the binding morphic
rational-forest theorem.  This last conclusion is conditional on the **global
second-leg identification**; it is not an inference from abstract rationality
or from the local completed algebra.

## 1. Finite flatness, singular locus, and normality

As a binary cubic in `[S:T]`, the four coefficients of `G` are

```text
x^3,
3*x^2*z+y^3,
3*x*z^2,
z^3+x^2*y.                                            (1.1)
```

They have no common projective zero: the first forces `x=0`, the second then
forces `y=0`, and the fourth forces `z=0`.  Hence every fibre of `pi` is the
length-three zero scheme of a nonzero binary cubic.  The projective
quasi-finite map `pi` is finite.  The hypersurface `X` is Cohen--Macaulay and
the target is regular of the same dimension, so finite miracle flatness makes
`pi` locally free of rank three.

On `S=1`, put `t=T/S`.  The equation is

```text
F=(x+t*z)^3+t*y^3+t^3*x^2*y.                          (1.2)
```

For `t!=0`, let `u=x+tz`.  A singular point of the plane fibre would satisfy

```text
F_z=3*t*u^2=0,
F_x=3*u^2+2*t^3*x*y=0,
F_y=3*t*y^2+t^3*x^2=0.
```

Thus `u=0`, `xy=0`, and `3y^2+t^2x^2=0`, which has no projective solution.
Every finite nonzero fibre is smooth.  At `t=0`,

```text
F=x^3,
(F_x,F_y,F_z,F_t)=(3*x^2,0,0,3*x^2*z+y^3),            (1.3)
```

so the unique total-space singularity in this chart is `p_0`.

On `T=1`, put `s=S/T`.  Then

```text
H=(s*x+z)^3+s^2*y^3+x^2*y.                            (1.4)
```

For `s!=0` this is the preceding smooth family after `t=1/s`.  At `s=0`,
the unique singular point is `[0:1:0]`.  In the chart `y=1`, the polynomial
coordinate `w=z+sx` gives

```text
H=w^3+s^2+x^2,                                        (1.5)
```

the `A_2` rational double point.  Hence `Sing(X)={p_0,p_infinity}`.

The generic plane cubic is smooth and therefore geometrically integral, so
the primitive hypersurface is integral.  A hypersurface is `S_2`, while the
two isolated singularities give `R_1`.  Serre's criterion proves normality.

## 2. Section, minimal elliptic surface, and the exact D3 row

There is a global section of the coefficient-base projection:

```text
[S:T] |-> [x:y:z]=[-T:0:S].                           (2.1)
```

The two integral `(1,1)` CFS transformations in the corrected local report
identify the generic pointed cubic with (0.3).  This also checks the local
invariants without relying on the plane discriminant alone.  At `t=0`,

```text
ord(c4,c6,Delta)=(infinity,4,8),                       (2.2)
```

so the minimal fibre is `IV*`.  At infinity, with `s=1/t` and
`U'=s^2U,V'=s^3V`, equation (0.3) becomes

```text
(V')^2=(U')^3-s^2,                                    (2.3)
```

which is minimal of type `IV`, with orders `(infinity,2,4)`.  Thus the
minimal discriminant has degree `8+4=12`, the fundamental line has degree
one, and the relatively minimal sectioned surface over `P1` is rational.
Every smooth projective resolution of `X` has the same function field, hence
is rational as well.

Equivalently, on the original plane model the invariant sections have the
forms, up to nonzero constants,

```text
c4_plane=0,
c6_plane=S^2*T^16,
Delta_plane=S^4*T^32.                                 (2.4)
```

The orders at `T=0` are obtained from (2.2) by adding two CFS levels,
namely `(12,24)` to `(c6,Delta)`; the remaining orders at `S=0` are `(2,4)`.
There are no other singular coefficient-base fibres by Section 1.

The point `p_infinity` is Du Val and contributes no GR defect.  The point
`p_0` has exact CFS/Hodge level two.  Applying

```text
xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
```

to this integral normal rational class-`(3,3)` surface gives precisely (0.4),
including the stated Picard lower bound.  This use is a surface theorem; it
does not assert a proper block, polynomial map, or JC2 counterexample.

## 3. The level-two exceptional boundary is a rational tree

In the affine chart `z=1`, shear `X_1=x+t`.  The germ at `p_0` is

```text
f=X_1^3+t*y^3+t^3*(X_1-t)^2*y.                        (3.1)
```

For weights

```text
wt(X_1,y,t)=(7,6,3),          weighted degree=21,      (3.2)
```

its principal part and the two higher terms are

```text
f_21=X_1^3+t*y^3+t^5*y,
f-f_21=t^3*X_1^2*y-2*t^4*X_1*y,
weights(f-f_21)=29,25.                                (3.3)
```

The principal part has an isolated singularity at the affine-cone origin.
Indeed

```text
d_X f_21=3*X_1^2,
d_y f_21=t*(3*y^2+t^4),
d_t f_21=y*(y^2+5*t^4),                               (3.4)
```

and these vanish simultaneously only at the origin.  Consequently the
strict transform under the normalized weighted blowup is smooth as a stack
along its exceptional curve, apart from cyclic quotient singularities of the
coarse model.  The exceptional curve is the irreducible quasismooth curve

```text
C: X_1^3+t*y^3+t^5*y=0 in P(7,6,3).                   (3.5)
```

It is rational.  Put `r=y/t^2`.  Every degree-zero monomial has its
`X_1` exponent divisible by three, since the other weights have gcd three,
and

```text
X_1^3/t^7=-(r^3+r).                                   (3.6)
```

Thus the degree-zero function field of `C` is exactly `C(r)`.  Irreducibility
also follows because `t*y*(y^2+t^4)` is not a cube in `C(y,t)`.

Resolving a cyclic quotient point adds a Hirzebruch--Jung chain of rational
curves attached at one branch of the strict transform of `C`.  Therefore the
normalized weighted blowup followed by quotient resolution has one rational
central curve with rational-chain arms: its reduced exceptional dual graph is
a tree.  More explicitly, on the stacky `t`-chart write

```text
(X_1,y,t)=(r^7*xi,r^6*eta,r^3).
```

At `r=0` the curve is `xi^3+eta^3+eta=0`; the residual `mu_3` acts by
`(r,xi,eta)->(zeta*r,zeta^2*xi,eta)`.  Its intersections with the fixed
stratum are the three distinct smooth one-branch points
`xi=0, eta=0,+i,-i`.  The `y`-chart adds the sole point over `t=0`, again a
smooth one-branch point on the stack with cyclic coarse quotient.  The
`X_1`-chart adds none, since `[1:0:0]` does not lie on (3.5).  Thus quotient
resolution attaches four disjoint bamboos and cannot create a cycle.  This is
already a good local resolution; the higher-weight terms in (3.3) do not
alter the quasismooth exceptional intersection.  Further blowups only attach
or subdivide rational trees.  The `A_2` point at infinity separately resolves
to its usual two-vertex rational chain.

As a consistency check, the Newton/weighted geometric-genus count has exactly
the two positive lattice points

```text
(i,j,k)=(1,1,1),(1,1,2),
7*i+6*j+3*k <= 21,                                    (3.7)
```

so `p_g(p_0)=2`.  This is an explicit warning that a rational-tree dual graph
does not imply a rational surface singularity.

## 4. A complete genus-two ramification component

For the finite map `pi`, adjunction gives

```text
K_X=B|_X,                    Ram(pi) ~ (3*A+B)|_X,      (4.1)
```

where `A` and `B` are the hyperplane classes from `P2` and `P1`.  Its degree
over the coefficient base is

```text
(3*A+B)*B*(3*A+3*B)=9.                                (4.2)
```

The curve

```text
C_0: y=0,        S*x+T*z=0                             (4.3)
```

is the section (2.1).  At its generic point the binary cubic is a cube, so
the ramification index is three and `C_0` occurs in the different with
coefficient two.

Now work densely on `S=x=1`, with `t=T/S`, and put

```text
u=1+t*z,                 q=u/y.                        (4.4)
```

Away from `C_0`, the equations `F=F_t=0` imply

```text
3*u^2+2*t*y^3=0,
y=-3*q^2/(2*t),
u=-3*q^3/(2*t),
z=(u-1)/t.                                             (4.5)
```

Substitution leaves the irreducible Laurent curve

```text
P(q,t)=9*q^7+9*t*q^4+4*t^5=0.                         (4.6)
```

Its closure in `X` is a complete irreducible ramification component `R'`.
The parametrizing formulas (4.5) are birational onto their image.  One exact
irreducibility check is obtained by setting `a=u`: the same curve is
birational to

```text
a^4*(3-2*a)^3=-12*t^8.                                (4.7)
```

On the dense torus the two birational directions are

```text
a=-3*q^3/(2*t),               q=2*t^3/(a*(3-2*a)).     (4.7a)
```

Over `C(a)`, the right side is not a square because it has order three at
`a=3/2`; hence the degree-eight Kummer polynomial is irreducible.

The normalization genus is two.  For (4.7), the degree-eight map to the
`a`-line has the following branch ledger:

```text
a=0:       valuation 4,    4 points of index 2, contribution 4;
a=3/2:     valuation 3,    1 point  of index 8, contribution 7;
a=infinity: valuation -7,  1 point  of index 8, contribution 7. (4.8)
```

Riemann--Hurwitz gives

```text
2*g-2=8*(-2)+(4+7+7)=2,             g(R'^nu)=2.        (4.9)
```

Independently, the Newton polygon of (4.6) has vertices
`(7,0),(4,1),(0,5)`, area four and six boundary lattice intervals, hence two
interior lattice points.  Its full polynomial and each edge truncation are
torus-nondegenerate, so the toric genus formula again gives two.

For reference, the target binary-cubic discriminant factors as

```text
Disc_[S:T](G)=-y^2*B_10,

B_10=27*x^10+54*x^6*y^2*z^2+36*x^4*y^5*z+4*x^2*y^8
     +27*x^2*y^4*z^4+4*y^7*z^3.                       (4.10)
```

The doubled line is the image of `2*C_0`; `R'` is the residual generic simple
ramification component.  Its coefficient-base degree is seven, as is also
forced by (4.2) after removing `2*C_0`.

## 5. Conditional proper-block obstruction

Assume, in addition to the exact surface statements above, that for some
affine target plane `A2 subset P2` the restriction

```text
Y=pi^(-1)(A2) -> A2                                    (5.1)
```

is globally the finite second leg of an actual proper block.  The promoted
block interface then supplies

```text
V=g1(A2) subset Y_sm minus Ram(pi),
g1:A2 -> V everywhere-defined and surjective.          (5.2)
```

Take a projective resolution `W->X` which is an isomorphism over `V`, then
blow up the boundary to strict SNC.  Every point of `R'` over the affine
target is missed by (5.2), while every point over target infinity is outside
`Y`; hence the complete strict transform of `R'` is a boundary component.
Because the birational map is a morphism toward `X`, this strict transform is
not contracted.  In an SNC boundary it is the smooth normalization and has
genus two.  This contradicts

```text
xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md,
```

which forces every boundary component to be rational.

The antecedent (5.1) is essential.  A local completed-algebra match, a finite
jet, a rational map from `A2`, or abstract rationality of `X` does not license
this exclusion.  Thus (0.1) is simultaneously a sharp positive control for
the global D3 surface row and a negative control for the actual proper-block
interface.

## 6. Exact desk replay

```bash
python3 - <<'PY'
import math
import sympy as s

S,T,x,y,z,t,a,b,q,X=s.symbols('S T x y z t a b q X')
G=s.expand((S*x+T*z)**3+S**2*T*y**3+T**3*x**2*y)
coeff=[s.expand(G).coeff(S,3-i).coeff(T,i) for i in range(4)]
assert coeff == [x**3,3*x**2*z+y**3,3*x*z**2,x**2*y+z**3]

F=s.expand(G.subs({S:1,T:t}))
assert F == s.expand((x+t*z)**3+t*y**3+t**3*x**2*y)
closed=[s.expand(s.diff(F,v).subs(t,0)) for v in (x,y,z,t)]
assert closed == [3*x**2,0,0,3*x**2*z+y**3]

# Target discriminant.
B10=(27*x**10+54*x**6*y**2*z**2+36*x**4*y**5*z
     +4*x**2*y**8+27*x**2*y**4*z**4+4*y**7*z**3)
assert s.factor(s.discriminant(F,t)) == -y**2*B10

# Dense residual ramification calculation, with a=u/x and b=y/x.
fab=a**3+t*b**3+t**3*b
ram=3*a**2*(a-1)+t*b**3+3*t**3*b
assert s.expand(ram-fab) == 2*a**3-3*a**2+2*t**3*b
aval=-s.Rational(3,2)*q**3/t
bval=-s.Rational(3,2)*q**2/t
P=9*q**7+9*t*q**4+4*t**5
assert s.factor(fab.subs({a:aval,b:bval})) == -3*q**2*P/(8*t**3)

# Full torus nondegeneracy: the coefficient matrix for
# P, q*dP/dq, t*dP/dt in (q^7,t*q^4,t^5) is nonsingular.
M=s.Matrix([[9,9,4],[63,36,0],[0,9,20]])
assert M.det() == -2592
vertices=[(7,0),(4,1),(0,5)]
area2=abs(sum(vertices[i][0]*vertices[(i+1)%3][1]
              -vertices[i][1]*vertices[(i+1)%3][0]
              for i in range(3)))
boundary=sum(math.gcd(abs(vertices[i][0]-vertices[(i+1)%3][0]),
                      abs(vertices[i][1]-vertices[(i+1)%3][1]))
             for i in range(3))
assert (area2,boundary,(area2-boundary+2)//2) == (8,6,2)

# Weighted principal part and its positive lattice-point ledger.
f21=X**3+t*y**3+t**5*y
assert s.groebner([s.diff(f21,v) for v in (X,y,t)],X,y,t).is_zero_dimensional
points=[(i,j,k) for i in range(1,4) for j in range(1,4)
        for k in range(1,8) if 7*i+6*j+3*k <= 21]
assert points == [(1,1,1),(1,1,2)]
print('D3_SECTIONED_GLOBAL_CONTROL_RAMIFICATION_PASS')
PY
```

Expected output:

```text
D3_SECTIONED_GLOBAL_CONTROL_RAMIFICATION_PASS
```

The replay verifies the polynomial identities, discriminant, dense
ramification equation, nondegeneracy determinant, Newton genus ledger and
weighted principal-part count.  The report layer invokes finite miracle
flatness, `S_2+R_1`, weighted quotient resolution, Kummer
Riemann--Hurwitz, the classification of minimal elliptic fibres, and the two
named binding campaign theorems.

## 7. Maximum-safe conclusion

The raw-degree-three exact-level-two local counter-control globalizes to a
finite flat integral normal rational class-`(3,3)` surface in the sectioned
one-support row.  Both singular-resolution boundaries are rational trees, so
no universal local rational-forest closure is available.  This particular
global presentation nevertheless has a complete genus-two residual
ramification component and therefore cannot be the globally identified
second leg of an actual proper block with the promoted morphic first leg.
The surface construction and the conditional block exclusion are separate;
neither constructs a Keller map nor resolves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15960`.
- Body SHA-256:
  `cc63787378346bba5055b573186fe30b709340c968bd2cf465afc5729d962a73`.
- Frozen basis: `adb7d06a166bd15f82203fcc1342cbb882a61764`.
