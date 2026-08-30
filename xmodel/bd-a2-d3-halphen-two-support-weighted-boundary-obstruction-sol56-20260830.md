# D3 two-support Halphen row: weighted-boundary obstruction at the triple fibre

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent D3 audit lane  
Frozen basis: `effb538eb858ff2c51d713a91f392d90796e786e`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Maximum-safe verdict

Assume the promoted degree-three two-support Halphen row

```text
m=3,                     T=t0+t1,              t1!=t0,
plane CFS levels=(1,1),  D=-P0-F_t1,
```

and assume that its normal class-`(3,3)` incidence occurs as the actual local
normal incidence of a hypothetical proper intermediate block.  Then the row
is impossible.

The obstruction is already forced at the triple fibre `t0`.  Exact plane
level one equals the strictly-Henselian-insoluble Halphen floor one, so the
three forced CFS line moves do not drop the level.  Instead they form the
critical cycle

```text
x^3  ->  y^3  ->  C2 z^3  ->  x^3,          C2!=0.
```

At the unique total-space singular point on the central triple line, the
`(2,1,3)` weighted blowup extracts

```text
C: x^3+t(y^3+q1xy)+C2t^2=0  in P(2,1,3).                (0.1)
```

For every `q1` and every `C2!=0`, this curve has boundary invariant one.  It
is either a smooth genus-one curve or an irreducible rational curve with one
ordinary node; resolving the latter creates a graph cycle.  The actual
everywhere-defined etale first leg from `A^2` misses the singular center, so
the whole exceptional configuration is boundary.  This contradicts the
binding morphic rational-forest theorem.

The local model `x^3+t y^3+t^2z^3` is an exact normal CFS-critical control.
Thus local formal survival is nonempty.  This report neither constructs nor
rules out an abstract global two-support class-`(3,3)` surface without the
actual morphic block interface.  It proves no occurrence theorem, polynomial
map, counterexample, or conclusion about JC2 outside the charged row.

## 1. Charged hypotheses and local setup

Move `t0` to `t=0` and the central triple line to `x=0`.  Over
`R=C[[t]]`, retain the literal raw coefficient-base degree-three model

```text
F=x^3+tF1+t^2F2+t^3F3,                                  (1.1)

F1=a x^3+ell x^2y+m x^2z
   +x(q0y^2+q1yz+q2z^2)+H(y,z).                         (1.2)
```

The charged row supplies all of the following.

1. The generic ternary cubic is nonsingular and the total incidence surface
   is normal.
2. The displayed plane model has exact CFS level one at `t0`.
3. The index-three Halphen torsor is strictly-Henselian insoluble at `t0`.
   In residue characteristic zero its minimal ternary-cubic level is exactly
   one.
4. The raw coefficient-base degree is at most three.  This is used again in
   the finite-local interface in Section 6.

Normality gives `H!=0`: on the generic point of the central line,

```text
F_t |_(t=x=0)=H(y,z),                                   (1.3)
```

so `H=0` would put the whole line in the total-space singular locus.  The
second support `t1` is used only to make the Hodge length at `t0` equal to
one rather than two.  No condition at `t1` is needed after the exact local
level at `t0` has been charged.

## 2. Exact CFS three-cycle

The reduction `x^3` has singular line `x=0`, so the first CFS move is forced:

```text
E1=t^-1 F(tx,y,z).                                      (2.1)
```

It is integral, has the same level one, and has reduction `H`.  Since level
one is already the strictly-Henselian-insoluble minimal floor, `E1` is a
minimal insoluble model.  CFS Lemma 5.8 forces its nonzero reduction to be a
scalar cube of a linear form.  Over `C`, a constant change on the central
line therefore normalizes

```text
H=y^3.                                                   (2.2)
```

The singular line is now `y=0`, and the second forced move is

```text
E2=t^-1 E1(x,ty,z)=t^-2F(tx,ty,z).                      (2.3)
```

Writing

```text
C2=[z^3]F2,
```

direct coefficient extraction gives

```text
(E2)_0=z^2(q2x+C2z).                                    (2.4)
```

Again `E2` is an integral level-one model equivalent to the generic torsor,
so it is minimal and strictly-Henselian insoluble.  Its reduction cannot be
zero: if `q2=C2=0`, then every coefficient of `E2` is divisible by `t`, and
dividing by `t` produces an integral equivalent model of level zero,
contradicting the minimal floor one.  Lemma 5.8 therefore makes (2.4) a
nonzero cube.  A cubic `z^2(q2x+C2z)` is a nonzero cube exactly when

```text
q2=0,                     C2!=0.                         (2.5)
```

Its singular line is `z=0`.  The third forced move returns the original
model exactly:

```text
t^-1 E2(x,y,tz)=t^-3F(tx,ty,tz)=F,                      (2.6)
```

by spatial homogeneity of degree three.  Unlike the promoted length-two row,
this cycle is not a minimisation contradiction: the present plane model is
already minimal.  It is the forced critical cycle for every survivor of the
two-support Halphen row.

This argument also bypasses the broader first-jet invariant disjunction.
Exact minimal insolubility makes the first transverse cubic itself a cube,
so the double-root branch never arises in this row.

## 3. Exact weighted face at the singular center

The only zero of `F_t=y^3` on the central line is

```text
p=([0:0:1],t=0).
```

All spatial derivatives vanish there, so `p` is singular.  Work in `z=1`
with local coordinates `(x,y,t)` centered at `p`, and give them weights

```text
w(x)=2,                    w(y)=1,                    w(t)=3.  (3.1)
```

Conditions (2.2) and (2.5) imply that there is no term below weight six and
that the complete weight-six face is

```text
P=x^3+t(y^3+q1xy)+C2t^2.                                (3.2)
```

Indeed, the only possible lower term was `t q2 x`, of weight five, and
`q2=0`.  The other terms of `tF1` have weight at least seven, every nonconstant
term of `t^2F2(x,y,1)` has weight at least seven, and `t^3F3` has weight at
least nine.  The unit coefficient `C2` makes (3.2) an exact face, not a
closure specialization.

## 4. Exceptional curve and its two exhaustive strata

The `(2,1,3)` weighted blowup extracts the reduced projective curve

```text
C={P=0} subset P(2,1,3).                                (4.1)
```

The weighted plane is well formed.  Its two quotient coordinate points are
`[1:0:0]` and `[0:0:1]`; equation (3.2) takes the nonzero values `1` and
`C2` there, respectively.  Thus `C` avoids both quotient points.  It passes
through the ordinary weight-one point `[0:1:0]`, where the derivative with
respect to `t` is one.  At every point with `y=0` on `C`, both `x` and `t`
are nonzero and `P_t=2C2t` is nonzero.  Hence every possible singularity of
`C` lies in the ordinary affine chart `y=1`.

Complete the weighted square by setting

```text
T=t+(y^3+q1xy)/(2C2),               W=2C2T.
```

On `y=1`, the curve becomes

```text
W^2=h(x),               h(x)=(1+q1x)^2-4C2x^3.          (4.2)
```

Its cubic discriminant is

```text
Disc_x(h)=-16C2(q1^3+27C2).                             (4.3)
```

There are exactly two cases.

### 4.1 The open stratum `q1^3+27C2!=0`

The cubic `h` has three distinct finite roots.  Together with the branch at
infinity, (4.2) is a smooth connected double cover of `P^1` branched at four
points, hence `C` is a smooth genus-one curve.  Equivalently, (4.1) is a
smooth anticanonical degree-six curve in `P(1,2,3)`.  It contributes component
genus one to every resolved boundary.

### 4.2 The equality stratum `q1^3+27C2=0`

Because `C2!=0`, this equality forces `q1!=0`.  Substitution
`C2=-q1^3/27` gives the exact factorization

```text
27h(x)=(q1x+3)^2(4q1x+3).                               (4.4)
```

The double and simple roots are distinct, and

```text
h''(-3/q1)=-2q1^2/3!=0.                                 (4.5)
```

Thus the singularity is an ordinary node, never a cusp or triple-root
specialization.  The curve is irreducible because the remaining linear
factor in (4.4) is not a square in `C[x]`.  Its normalization is rational and
the node identifies two distinct normalization branches.

Consequently the exceptional curve has campaign boundary invariant

```text
tau=sum genera+b1(dual multigraph)=1                    (4.6)
```

on both strata: component genus one in Section 4.1, and one graph cycle after
resolving the node in Section 4.2.

## 5. Higher terms and resolution-cycle persistence

The weighted strict transform is integral because it is the closure of the
integral punctured surface.  It is `S2`: in weighted charts it is a
hypersurface, or a characteristic-zero finite cyclic quotient of one.  It is
regular in codimension one.  Away from the exceptional divisor this follows
from normality of the original surface near its isolated center; at the
generic point of the exceptional divisor it follows from generic smoothness
of the reduced curve (4.1).  The curve avoids both quotient points.  Hence
the weighted strict transform itself is normal.  No normalization of the
exceptional curve is being performed.

In the smooth stratum, the genus-one exceptional prime therefore persists
birationally on every common resolution.  In the nodal stratum, the node is
in the ordinary `y`-chart.  Write the weighted blowup there as

```text
x=r^2X,                    y=r,                    t=r^3T.
```

After division by `r^6`, the strict-transform equation is

```text
P(X,1,T)+r*(higher terms)=0.                             (5.1)
```

At the node, `P(X,1,T)` has a nondegenerate quadratic part.  Parametric Morse
reduction therefore puts (5.1) in the exact analytic/formal form

```text
uv+phi(r)=0.                                             (5.2)
```

If `phi=0`, the strict transform is singular along the curve `u=v=0`; away
from `r=0` the weighted blowdown is an isomorphism, so the original surface
would have a codimension-one singular locus.  Normality excludes this.
Thus, after absorbing a unit,

```text
phi(r)=r^n,                     n>=1.                    (5.3)
```

For `n=1` the surface is smooth and an ordinary boundary blowup at the node
makes the strict transform of the globally irreducible rational curve meet
the new exceptional curve in two points, yielding two parallel graph edges.
For `n>=2`, (5.2) is an `A_(n-1)` surface singularity; its resolution chain
joins the two local branches of that same global exceptional curve.  The
chain plus the global strict transform is a cycle.  This explicit
`uv+r^n` argument, rather than connectedness alone, proves persistence.
Later boundary blowups only subdivide the cycle or attach trees.

## 6. Finite-local identification and the actual morphic boundary

If `p` lies on the fixed target line at infinity, every divisor over it is
first-leg boundary a fortiori.  Suppose `p` lies in the polynomial target
affine plane.  At the target point `(x,y)=(0,0)`, literal raw base degree at
most three and (2.5) give

```text
F(t;0,0,1)=C2t^2+C3t^3=t^2(C2+C3t),          C2!=0.     (6.1)
```

Thus the local equation is `t`-regular of exact order two.  Weierstrass
preparation writes it, in the completed or analytic local ring, as a unit
times a monic degree-two polynomial in `t`.  Equivalently, the projective
incidence projection is quasi-finite at `p` and finite after shrinking the
target neighbourhood.  This is only a local finiteness statement; it makes
no claim that an arbitrary projective incidence is globally finite.

Under the charged occurrence hypothesis, this finite normal incidence germ
has the same function field as the intermediate block.  By uniqueness of
integral closure it is the local germ of the actual normal affine
intermediate surface `Y`.

For a hypothetical proper block,

```text
A^2 --g1--> Y --g2--> A^2,
```

the binding block-structure theorem makes `g1` everywhere defined, dominant,
quasi-finite and etale.  An etale morphism from the smooth source can meet
only `Y_sm`; since `p` is singular, `p` is outside the open image

```text
V=g1(A^2).
```

Every exceptional divisor centered over `p`, including the complete
configuration in Sections 4--5, is therefore boundary in a smooth SNC
completion of `V`.  Apply the corrected morphic rational-forest theorem to
the surjective morphism `g1:A^2->V`.  Its boundary components must all be
rational and its boundary dual graph must be a forest.  The smooth stratum
has a genus-one component and the equality stratum has a cycle, a
contradiction in both cases.

No birationality, properness, finiteness or surjectivity of `g1:A^2->Y` is
asserted or needed.  The theorem is applied to its actual image `V`.  An
arbitrary dominant rational map from `A^2` would not suffice.

## 7. Exact local control and occurrence firewall

The diagonal model

```text
F_control=x^3+t y^3+t^2z^3                              (7.1)
```

realizes the forced local cycle exactly:

```text
x^3 -> y^3 -> z^3 -> x^3.
```

Its three nonzero coefficient valuations are `0,1,2` in the CFS critical
order, so it is the standard critical ternary cubic: minimal, strictly-
Henselian insoluble and of level one in residue characteristic zero.  The
insolubility is also immediate from valuations: the three summands in a
putative point have valuations in distinct residue classes modulo three, so
the minimum cannot occur twice.  The generic cubic is smooth.

The total surface germ is normal.  Its only singular point over `t=0` is
`p`; a hypersurface with isolated singular locus is `R1` and `S2`.  Here
`q1=0,C2=1`, so (4.3) is nonzero and the weighted exceptional curve is
smooth elliptic.

This control proves only local/formal nonemptiness at `t0`.  It does not add
the distinct second support `t1`, construct an abstract global class-`(3,3)`
Halphen surface, or provide the actual affine-plane first leg.  The present
theorem prices the failure precisely at that last morphic interface.

## 8. Replay and dependencies

The desk-scale symbolic replay is

```text
204acc292db6d2c1874dd741a637b6a21e5c16c5c49c60389062b3874f7525cc
  ops/d3_halphen_two_support_weighted_boundary_replay.py
```

Under `uv run --with sympy==1.14.0`, ordinary, `-O`, and `-OO` outputs are
byte-identical, 547 bytes, with SHA-256

```text
d3a35f87dc841f0cdc4a6d613281999982ccea3d7813f2f4a6f07605eba07700.
```

The mutation `--mutate-discriminant-sign` exits one at the discriminant
check.  The script contains zero Python AST `assert` nodes.  It derives both
forced reductions and the exact three-cycle, extracts the complete weighted
face, checks square completion, derives (4.3)--(4.5), verifies avoidance of
the two quotient coordinate points, and checks the diagonal control cycle.
The imported CFS, normality, resolution and morphic-boundary arguments remain
mathematical inputs proved above, not software outputs.

Exact promoted dependencies are

```text
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
e5d55d5efd1203bedce54021f8c84d1229fd905cdab31184f22153376d9b87f7
  xmodel/bd-a2-d3-halphen-local-gates-coordinator-integration-sol56-20260830.md
d49a44ce65f13f0aba35e0a034923a1362594ba8a21fef27c63cc866ec7b667a
  xmodel/bd-a2-rational-forest-morphic-correction-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The classical local input is Cremona--Fisher--Stoll, especially Theorem 3.5,
Theorem 4.3, Definition 5.1, Lemmas 5.2--5.4 and 5.8, and Proposition 5.6.
The row elimination is conditional on the promoted D3 surface theorem and
actual normal morphic-block occurrence.  It should be hostile-reviewed before
binding promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15664`.
- Body SHA-256:
  `ac96f63883a5c9bd5a6e90b4c5ab9068c61c684031a80c4588a3cda7e8bb57a8`.
- Frozen basis: `effb538eb858ff2c51d713a91f392d90796e786e`.
