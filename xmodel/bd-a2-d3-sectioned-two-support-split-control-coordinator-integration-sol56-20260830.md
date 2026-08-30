# Binding integration: D3 sectioned two-support split representative

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator lane  
Frozen basis: `03a4d8dc557abf1e23e5a039ff5c995131935ff2`  
Disposition: **PROMOTE REPRESENTATIVE CONTROL WITH REVIEW CORRECTIONS**

## 0. Binding verdict

Promote the split two-support construction as one exact surface-level
representative of the sectioned row, and exclude this representative from
being the globally identified second leg of an actual proper block, conditional
on the already-promoted first-leg interface and morphic rational-forest
theorem.

Put

```text
F=(x+t*z)^3+t*y^3+t*(t*x+z)^2*y
```

and let `X` be its class-`(3,3)` closure in `P2_[x:y:z] x P1_[S:T]`.
Let `r:Y->X` be the minimal projective resolution.  Then:

```text
X is integral, normal, and rational;
pi:X->P2 is finite flat of degree 3;
X has four A2 points and two simple elliptic degree-three points;
m=1, T=[1]+[-1], D=-F_1-F_(-1), CFS levels=(1,1);
rho(Y)>=16;
Ram(pi)=2*C_sec+R', with g((R')^nu)=3.
```

The Opus 5 hostile review returns `CONFIRM_WITH_CORRECTIONS`.  It finds no
wrong mathematical conclusion.  Its corrections are load-bearing for the
integrated statement: the displayed tangent cubic in the producer is only
projectively equivalent to the literal tangent cone; the realized Picard
bound sharpens from the row minimum `rho(Y)>=12` to `rho(Y)>=16`; the
extraneous resultant factors must be discarded explicitly; and absolute
irreducibility is certified without the producer's invalid Singular command.

This is strictly a **representative-only** result.  It proves that the
sectioned row is nonempty at the abstract surface level and that this named
member is not an actual proper-block second leg.  It does not empty the
positive-dimensional row, classify its members, construct a polynomial map,
or prove JC2.

## 1. Frozen evidence and custody

The exact sealed producer is

```text
dcdfaabcdaf3d8c71111a207ea75ddcb8784cf8f164051df7b2cd54b8e51d4e7
  xmodel/bd-a2-d3-sectioned-two-support-split-control-sol56-20260830.md

77b9188d28ad3dd9b4674971e36deb0f7c02048d541b6fcd4815ee8dad3ce3a1
  xmodel/bd-a2-d3-sectioned-two-support-split-control-sol56-20260830.md.artifact.json
```

The artifact lifecycle independently verifies body bytes `12539`, body
SHA-256
`6975f482e1f2eeb6d5277623951dd3c82a3a9bc3258ee00ac636169a65e01c6b`,
and frozen basis `f86884a5ab78e5248977942f93547fbf25b5be8e`.

The sealed independent review is

```text
0f85980cb0dd6d35b776171aae87a0f1c4a96c58ac3848f9a432d90a29068ca6
  xmodel/bd-a2-d3-sectioned-two-support-split-control-hostile-review-opus5-20260830.md
```

Its seal verifies body bytes `30002`, body SHA-256
`b126a20364a30e4c4517289eb38f42f8b70e73c8c0cc37c451ba7d12e1103950`,
and basis `f1f10d94730606b7c5a9b3e78a362110d4ab2b6f`.  The review reproduced all
charged mathematical hashes before reconstruction and asserted no exit price.

The two promoted interfaces consumed only by the proper-block exclusion are

```text
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md

94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
```

Neither is re-derived here.

## 2. Exact representative surface theorem

The reverse-operation identity and integral shear give

```text
R_(t-b) R_(t-a) H_0
 =X^3+t*y^3+t*(t*X-(t-a)*(t-b)*z)^2*y,

X=x+(t-a-b)z,
F_(a,b)=(x+(t-a-b)z)^3+t*y^3+t*(t*x-a*b*z)^2*y.
```

The specialization `(a,b)=(1,-1)` is the displayed `F`.  Its binary-cubic
coefficients are

```text
A_0=x^3,
A_1=3*x^2*z+y^3+y*z^2,
A_2=3*x*z^2+2*x*y*z,
A_3=z^3+x^2*y.
```

They have no common projective zero, so target projection is finite; finite
miracle flatness gives rank three.  The complete singular locus consists of

```text
t= 1: [-1:0:1],             t=-1: [1:0:1],
t= 0: [0:0:1], [0:i:1], [0:-i:1],
t=inf: [0:1:0].
```

The three points over zero and the point at infinity are `A2` rational double
points.  The points over `t=+-1` have multiplicity three and smooth
projectivized tangent cone.  One ordinary blowup resolves each, with
exceptional curve a smooth plane cubic of genus one, self-intersection `-3`,
and discrepancy `-1`.  The isolated singular locus and hypersurface
Cohen--Macaulay property give `R1+S2`, hence normality.  The smooth generic
plane cubic gives integrality, and the associated elliptic surface gives
rationality.

The pointed generic cubic has minimal Weierstrass equation

```text
V^2=U^3-t^4.
```

The plane invariants, up to nonzero constants, are

```text
c4=0,
c6=t^4*(t^2-1)^6,
Delta=t^8*(t^2-1)^12.
```

The minimal fibres are `IV*` at zero and `IV` at infinity; at `t=+-1` the
given plane model has exact CFS level one above good reduction.  Thus the
associated relatively minimal elliptic surface is rational with a section,
and the class-`(3,3)` surface realizes exactly

```text
m=1,
T=[1]+[-1],
D=-F_1-F_(-1),
local CFS levels=(1,1).
```

The target discriminant is

```text
Disc_[S:T](F)=-y^2*B_10,
```

where the factor `y^2` is the tame different of the totally ramified section
curve `C_sec`, and `B_10` is the residual degree-ten branch form.  On the
dense residual ramification chart the normalization is birational to

```text
P(q,t)=9*q^7*t+12*q^6*t^2+q^6+4*q^5*t^3+9*q^4*t^2
       +8*q^3*t^3+4*q^2*t^4+4*t^6=0.
```

This curve is absolutely irreducible.  Its Newton polygon has four interior
lattice points; its only toric boundary defect is one ordinary node.  Hence

```text
Ram(pi)=2*C_sec+R',             g((R')^nu)=4-1=3.
```

The ramification degree count `12=2+10` and the omitted-locus audit leave no
additional residual component.

## 3. Binding review corrections

### 3.1 The tangent cone is projectively equivalent, not literally equal

In literal local coordinates `X=x-x_0`, `Y=y`, `T=t-a`, the two tangent
cones are

```text
TC_+ = X^3+X^2*Y+3*X^2*T-2*X*Y*T+3*X*T^2
       +Y^3+Y*T^2+T^3,

TC_- = X^3-X^2*Y+3*X^2*T+2*X*Y*T+3*X*T^2
       -Y^3-Y*T^2+T^3.
```

If

```text
C_a(U,V,W)=U^3+a*V^3+a*(a*U-W)^2*V,
```

then the exact identities are

```text
TC_+ =  8*C_(+1)((X+T)/2, Y/2, T),
TC_- = -8*C_(-1)(-(X+T)/2, -Y/2, T).
```

The substitutions are invertible linear transformations, so the producer's
smooth-cubic and one-blowup conclusions are correct.  Only its phrase "is
exactly" is replaced by "is projectively equivalent to".

### 3.2 The realized Picard bound is at least sixteen

The four-row theorem supplies the universal row minimum `rho(Y)>=12`; that
inequality was true but non-sharp for this witness.  Here the relatively
minimal rational elliptic surface has Picard number ten.  Over each of the two
level-one defects, the inverse minimalization contains three `(-1)`-curves:

```text
Y_(+-1)=L'_1+L'_2+L'_3+E_(+-1),
E.(L'_1+L'_2+L'_3)=3,
(L'_i)^2=-1.
```

The six contractions therefore give the binding representative estimate

```text
rho(Y)>=10+3+3=16.
```

No claim of equality is needed.

### 3.3 Resultant artifacts are discarded explicitly

After removing the section and putting `x=1`, `z=(u-1)/t`, `u=q*y`, the
two residual equations `A=B=0` give

```text
Res_y(A,B)=t^2*(t-1)^2*(t+1)^2*P(q,t).
```

The three displayed base factors are not residual ramification components:

1. At `t=+-1`, `A` specializes to
   `y^2*(q^3+q^2+1)` at `t=1` and
   `y^2*(q^3-q^2-1)` at `t=-1`; `B` has one factor `y`, and the only common
   root is `y=0`, the section already divided out.
2. At `t=0`, both equations become `(q*y-1)^2`.  Their apparent common root
   makes `z=(q*y-1)/t` equal to `0/0`, outside this chart transformation.
   Directly, the original equation on `x=1,t=0` is `A_0=1`, so there is no
   point of `X` there.

The two leading `y`-coefficients vanish simultaneously only at `(q,t)=(0,0)`,
and the penultimate subresultant is linear in `y` with leading coefficient
coprime to `P`.  Thus no component is lost, and the transfer from the residual
ramification curve to `P=0` is birational.

### 3.4 Absolute irreducibility uses the smooth rational point

The accepted certificate does not use Singular absolute factorization.  The
review first checks exact irreducibility of `P` over `Q`.  In the chart
`q=1/r`, `t=w/r`, its degree-eight closure is

```text
r^8*P=w*(2*w+3)^2
      +r^2*(4*w^6+4*w^4+8*w^3+9*w^2+1).
```

At `(r,w)=(0,0)`, corresponding to `[1:0:0]`, the derivative with respect to
`w` is `9`.  This is a smooth `Q`-rational point.  If a `Q`-irreducible curve
had at least two geometric components, Galois would permute them transitively;
a rational point on one would lie on all of them and would therefore be
singular.  The smooth rational point rules this out.  This is the binding,
CAS-free upgrade from rational to absolute irreducibility.

## 4. Evidence correction: only the standalone replay is live

The producer's embedded Section 6 Python block contains eleven bare `assert`
statements.  Under `python3 -O` those checks disappear, and even deliberately
falsified inputs can print the PASS banner.  That embedded block is
**non-evidence**.

The producer's Singular command is also non-evidence.  In Singular 4.4.1,
`absFactorize(P)` returns a ring containing `absolute_factors`, not a factor
list.  Consequently `size(L)` for

```text
list L=absFactorize(P);
```

returns `1` for reducible and irreducible controls alike.  The command cannot
certify absolute irreducibility, and the attempted correct absolute
factorization did not finish inside the review's desk budget.  Section 3.4
supplies the mathematical replacement.

The separately charged replay remains clean:

```text
996dffc8d3215fb099c672a4cb5ae7840403d2988e5df9b864f8bb0886179a48
  ops/bd_a2_d3_sectioned_two_support_control_replay.py
```

It has zero AST `Assert` nodes and seventeen live `require()` calls.  Fresh
ordinary, `-O`, and `-OO` executions are byte-identical, with output SHA-256

```text
fa9f6be4ac6a9391b672362355a5d9538c835b399c52584ed659bccbba7fa501
```

The review also fault-injected six checked quantities and saw the appropriate
named failure under plain and optimized execution; all three built-in mutation
gates fire.  The replay checks the finite coefficient, reverse-move,
Weierstrass, local-Jacobian, infinity-chart, and tangent-cubic identities.  It
does not prove finite miracle flatness, normality, Tate classification,
absolute irreducibility, the genus formula, or the proper-block exclusion;
those remain the reviewed mathematical arguments above.

The sealed producer and review are left byte-untouched.  This integration
supersedes only their evidentiary interpretation and incorporates the review's
mathematical repairs.

## 5. Proper-block consequence and exact scope

Assume the promoted interface

```text
A2 --g1--> Y_block --g2--> A2,
V=g1(A2) subset (Y_block)_sm minus Ram(g2),
g1:A2->V everywhere-defined, surjective, and etale,
```

and the promoted morphic rational-forest theorem.  If this named `X` were the
global second leg, its minimal resolution would be an isomorphism over `V`.
Each complete elliptic exceptional curve `E_+`, `E_-` is disjoint from `V`
and survives as a positive-genus component in every smooth SNC boundary.
Likewise the complete normalized residual ramification curve of genus three
is disjoint from `V`: its affine-target points are ramification points and its
points over target infinity are outside the affine second leg.  Either type of
curve contradicts the morphic rational-forest conclusion `tau(boundary)=0`.

These are two geometric witnesses, but both consume the same promoted
rational-forest theorem; they are not independent of that common dependency.
The conclusion is exactly

```text
this surface is a FULL_ACTUAL abstract surface witness;
this surface is excluded as an actual proper-block second leg;
the row-wide proper-block question remains OPEN.
```

The cheapest family-wide successor is to analyze every exact-CFS-level-one
defect in rows 1 and 3.  One must not infer discrepancy `-1` merely from the
pushed divisor, because relative minimalization can discard exceptional
components; one must also account for minimally elliptic cusp configurations
whose good SNC resolution may be a rational tree.  Until those two risks are
closed, this representative cannot be promoted to a row theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12383`.
- Body SHA-256:
  `d92ad1f2014ef0eb333a974971da21d5338ff3dae48eba4a903e136a481d36b1`.
- Frozen basis: `03a4d8dc557abf1e23e5a039ff5c995131935ff2`.
