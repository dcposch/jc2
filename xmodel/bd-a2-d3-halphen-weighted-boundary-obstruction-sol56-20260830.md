# D3 one-point Halphen row: universal weighted-boundary obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `7ef0f3d9799b196dea26a82315c8ac79a0fbb00d`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Assume the promoted degree-three one-point Halphen row and local CFS gates,
literal raw coefficient-base degree three, and occurrence as the actual
normal finite incidence of a proper intermediate block.  Then **every**
remaining critical shard in

```text
m=3,                    T=2t0
```

is impossible.

The obstruction is uniform in all surviving coefficients.  At the unique
singular point, a weighted blowup extracts a complete curve whose boundary
invariant

```text
tau = sum(component normalization genera)+b1(dual multigraph)
```

equals one.  It is either a smooth genus-one curve or an irreducible rational
curve with one node, whose resolution creates a graph cycle.  The actual
everywhere-defined first leg from `A^2` misses the singular point, so the
entire extracted curve is boundary.  This contradicts the corrected morphic
rational-forest theorem.

The morphic qualification is load-bearing.  This report does not eliminate
an abstract class-`(3,3)` surface merely because it is rationally dominated,
and it does not prove that a proper block or a Keller counterexample exists.

## 1. Exact weighted face

Work in a projective chart `z=1` around the marked point and move its
coefficient-base value to `t=0`.  This chart need not be the fixed polynomial
affine chart; if the point lies on target infinity, it is boundary a fortiori.
Retain the raw expression

```text
F=x^3+tF1+t^2F2+t^3F3.
```

The promoted CFS state machine leaves only the triple-root branch.  In the
notation of that theorem its equations include

```text
q1=q2=C2=U2=0,       R2=3s^2,       C3=s^3,
s!=0,

b=Q021-sq0=3lambda,
U3+s^2ell-sM111=3lambda^2,
-s^3a+s^2V2-sR3=lambda^3,
kappa=0,             eta!=0.
```

Use analytic coordinates centered at the singular point

```text
X=x+s t,                  Y=y+lambda t.
```

Give `(X,Y,t)` weights `(5,4,3)`.  Direct expansion under all displayed CFS
relations has no term of weight below 15, and its complete weight-15 face is

```text
P15=X^3+tY^3+alpha t^2XY+eta t^5,                       (1.1)

alpha=M111-2s ell-2lambda q0,                           (1.2)
```

where `eta` is exactly the final nonzero CFS flag

```text
eta=-A2s^3-P2s^2lambda-T2s lambda^2-B2lambda^3
    +V3s^2+M3s lambda+Q3lambda^2.                       (1.3)
```

Every other term has weight at least 16.  No genericity assumption is made
on `alpha`; only the already forced principal open `eta!=0` is used.

The literal degree-three coefficient base is essential twice: it is used in
the CFS state machine and prevents an uncharged higher `t` coefficient from
altering the exact local finite presentation below.

## 2. Exceptional curve

The `(5,4,3)` weighted blowup extracts the reduced curve

```text
C_(alpha,eta): P15=0  in  P(5,4,3).                    (2.1)
```

The weighted plane is well formed.  Its degree-15 hypersurface has arithmetic
genus one; explicitly the standard Hilbert-series formula gives

```text
2p_a = 15^2/(5*4*3)
       -15(1/(5*4)+1/(5*3)+1/(4*3))
       +(gcd(15,5)/5+gcd(15,4)/4+gcd(15,3)/3)-1
     =2.
```

The geometry is more useful than the arithmetic count.  On the index cover
of the chart `t!=0`, compactification gives the projective Hesse cubic

```text
E: u^3+v^3+alpha uvw+eta w^3=0  in P^2,                (2.2)
```

with residual action

```text
(u,v,w) |-> (zeta^2u,zeta v,w),            zeta^3=1.   (2.3)
```

The coarse exceptional curve is `E/mu3`.  The only projective fixed points
of (2.3) are the three coordinate vertices; their values in (2.2) are
`1,1,eta`, so the action on `E` is free.

Put

```text
delta=alpha^3+27eta.
```

There are exactly two strata.

### 2.1 `delta!=0`

The Hesse cubic is smooth.  Indeed, if `alpha=0`, the two affine partials can
vanish only at `(0,0)`, which is excluded by `eta!=0`.  If `alpha!=0`, a
singular point has nonzero `u,v`; multiplying the two derivative equations by
`u,v` gives `u^3=v^3`.  Write `v=zeta u`.  Then

```text
u=-alpha zeta/3,        v=-alpha zeta^2/3,
```

and the equation is `eta+alpha^3/27=0`.  The converse is direct.  Hence
`delta!=0` is precisely the smooth stratum.

The free degree-three quotient of the smooth elliptic `E` is again a smooth
genus-one curve.  Thus `C_(alpha,eta)` contributes component genus one and

```text
tau(C)=1.
```

### 2.2 `delta=0`

Put `c=-alpha/3`, so `c^3=eta!=0`.  Then

```text
E=(u+v+cw)
  (u+zeta v+zeta^2cw)
  (u+zeta^2v+zeta cw).                                  (2.4)
```

The action cyclically permutes the three lines and their three vertices.
The quotient is therefore an irreducible rational curve with one ordinary
node: its normalization is one `P^1`, while the orbit of the three vertices
becomes one identification of two normalization branches.  Resolving that
node gives a dual-graph cycle, so again

```text
tau(C)=b1=1.                                             (2.5)
```

Here `tau` always denotes the campaign boundary invariant, not the Tjurina
number.  The weighted-homogeneous surface cone is non-isolated on this
special stratum; no isolated-cone claim is used.

## 3. Quotient and higher-weight terms do not erase the obstruction

The only point of (2.1) on a weighted coordinate axis is `[0:1:0]`.  On the
`Y=1` orbifold chart its index-cover equation is

```text
u^3+v+alpha v^2u+eta v^5=0.
```

Its `v` derivative is one at the origin.  The curve is smooth on the cover,
and its one-dimensional cyclic coarse quotient is smooth.  The special
Hesse nodes lie in `t!=0`, where the residual action has trivial stabilizer.
Thus no weighted-axis singularity changes the genus or node ledger.

The normalized weighted strict transform is an integral normal surface.  It
is locally a characteristic-zero finite quotient of a hypersurface and hence
`S2`; it is regular in codimension one because the original surface is normal
off the center and the reduced exceptional curve is generically smooth.

In the smooth-Hesse case, every common resolution therefore contains a
boundary component birational to the genus-one `C`.  In the nodal case the
weight-at-least-16 terms may change the radial surface singularity at the
node, but cannot erase its two branches.  On a local index cover, parametric
Morse reduction has form

```text
uv+phi(r)=0.
```

Normality rules out `phi=0`; after a unit change `phi=r^n`.  Resolution
inserts a connected rational chain joining the two branches of the same
globally irreducible exceptional curve.  The normalization component and
that chain give two paths between the same attachment points, hence a genuine
cycle.  Equivalently, connectedness of the resolution fibre alone preserves
the cycle.  Later boundary blowups only subdivide edges or add leaves.

Thus every good resolution has a complete exceptional boundary
subconfiguration with boundary invariant one, on both strata of `delta`.

## 4. Why it is boundary in an actual proper block

The point `p=(x,y,t)=(0,0,0)` is singular: (1.1) has no ordinary linear term,
and the exact germ has the same vanishing gradient.  If `p` lies on the fixed
target line at infinity, the extracted configuration is already first-leg
boundary and the contradiction follows.  Suppose instead that `p` lies in
the polynomial target affine plane.  Then, more specifically,

```text
F(t;0,0,1)=s^3t^3,           s!=0.                      (4.1)
```

Because the raw coefficient-base degree is at most three, (4.1) makes the
projection to the affine target plane finite, after a unit normalization,
in a neighbourhood of `p`.  On the charged normal incidence occurrence this
local finite normal algebra is the local algebra of the intermediate block
surface `Y`.

For an actual proper block,

```text
A^2 --g1--> Y --g2--> A^2,
```

the promoted block theorem gives that `g1` is an everywhere-defined dominant
étale morphism and

```text
g1(A^2) subset Y_sm minus NonEt(g2).
```

Since `p` is singular, it is outside the open image
`V=g1(A^2)`.  Every divisor centered over `p`, including the entire weighted
exceptional configuration above, lies in the resolved boundary of `V`.
Apply the corrected morphic rational-forest theorem directly to the
surjective morphism `g1:A^2 -> V`: every resolved boundary component must be
rational and its dual multigraph a forest.  Sections 2--3 give the opposite.

This argument does not say that `g1` is birational, finite, proper or an open
immersion; its generic degree may be at least two.  It also does not use an
arbitrary rational map from `A^2`, for which the rational-forest statement is
false.

## 5. Uniform row elimination and control

The proof used no specialization of `alpha`.  It therefore excludes both
intrinsic first-jet shards `q0=0` and `q0!=0`, every value of their remaining
higher coefficients, and both Hesse strata.  Conditional on actual
proper-block occurrence, the complete promoted row

```text
triple fibre F0=3P0,       defect T=2t0,
exact local CFS level 2,   pushed discrepancy -4P0
```

is empty.

For the sharp positive control

```text
F=(x+tz)^3+t y^3+t^3x^2z,
```

one has `alpha=0,eta=1`.  Its exceptional curve is already smooth elliptic.
Thus the control realizes the local CFS/surface coefficient conditions but
fails the actual map-side boundary interface at the cheapest possible local
place.  A more expensive global ramification computation is unnecessary for
this exclusion.

## 6. Executable replay

The exact symbolic replay is

```text
2601681db842d66ce5cc479c4304ab684b983b634cad5f7995b8b9b5c25b340a
  ops/d3_halphen_weighted_boundary_replay.py
```

With SymPy 1.14.0 under
`uv run --with sympy==1.14.0`, ordinary, `-O` and `-OO` outputs are
byte-identical, 599 bytes, SHA-256

```text
a5d5ec6b3abcca9d83edf45f04ff5ca81376f257d4ae0970004f5155041a150c.
```

The mutation `--mutate-t5-sign` exits one with
`FAIL:weighted face identity failed`.  The replay has zero AST `assert`
nodes.  It derives (1.1)--(1.3), the weight gap, arithmetic genus, Hesse
discriminant candidate, triangle factorization, residual line cycle, fixed-
point ledger and weighted-axis regularity.  The resolution and proper-block
interface arguments are mathematical inputs proved above, not software
outputs.

## 7. Exact dependencies and price

The promoted local dependency is

```text
e5d55d5efd1203bedce54021f8c84d1229fd905cdab31184f22153376d9b87f7
  xmodel/bd-a2-d3-halphen-local-gates-coordinator-integration-sol56-20260830.md
e0999f46bded42a598a0c389269857d25ef76365ec3b7d947196a67b3a632ae6
  its artifact manifest
```

The one-point four-row input is

```text
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
```

The corrected morphic boundary theorem is

```text
d49a44ce65f13f0aba35e0a034923a1362594ba8a21fef27c63cc866ec7b667a
  xmodel/bd-a2-rational-forest-morphic-correction-sol56-20260830.md
d14702bb98d3fd347a9b96ffaa531fefd55aad28df58d37601f6336bfb29029f
  its artifact manifest
```

The actual-first-leg placement also consumes the promoted intermediate-block
structure theorem: `Y` normal affine, `g2` finite flat, `g1` everywhere
étale/open/dominant, and `g1(A^2)` disjoint from `Sing(Y)` and the non-étale
support of `g2`.

This packet is review-gated.  Even after promotion it closes only the
one-point index-three Halphen row in the degree-three proper-block surface
classification.  The other three Hodge rows, other block degrees,
non-occurrence of blocks, and JC2 remain open.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11732`.
- Body SHA-256:
  `2fc2cd21ca8e4dd6c6d667ce4d37123cc2be2884c883601a252223f757140bee`.
- Frozen basis: `7ef0f3d9799b196dea26a82315c8ac79a0fbb00d`.
