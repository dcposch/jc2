# Hostile review: D3 two-support Halphen weighted-boundary obstruction

Date: 2026-08-30
Reviewer: GPT-5.5 hostile review pass
Scope: local repository reads were limited to the nine charged files and this
single output report path.  No sibling prompt, log, receipt, uncharged xmodel
report, Git state, canonical ledger, or `jc2-lean` path was inspected or
modified.  The CFS theorem-interface check used the primary arXiv source
`https://arxiv.org/abs/0908.1741`.

Receipt status `ABSENT` is expected.  No exit-price assertion is made.

## Custody

All charged SHA-256 hashes match exactly:

```text
9b232811376194277d4916bc7e42216740c9b9a80430800b1fb6ffba0cf91218
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-obstruction-sol56-20260830.md
c5936d24d784f1a6088d42992f41fcdb05c7b14e158abc56c82d8027154ad6b4
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-obstruction-sol56-20260830.md.artifact.json
204acc292db6d2c1874dd741a637b6a21e5c16c5c49c60389062b3874f7525cc
  ops/d3_halphen_two_support_weighted_boundary_replay.py
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
be42d2cf894d92928978935381028dbf5ae7ba1d3598a3474d7c1460a7b6dee9c
  xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md
94e56bdd79bbcc579a845ca271f89f0d1169c21fb872a9a9fd9f481a06c716cc
  xmodel/bd-a2-d3-halphen-cfs-state-machine-hostile-review-gpt55-20260830.md
e5d55d5efd1203bedce54021f8c84d1229fd905cdab31184f22153376d9b87f7
  xmodel/bd-a2-d3-halphen-local-gates-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The producer artifact JSON records body SHA-256
`ac96f63883a5c9bd5a6e90b4c5ab9068c61c684031a80c4588a3cda7e8bb57a8`
and full SHA-256 matching the charged obstruction file.  The replay source is
4954 bytes.

## Itemized Audit

1. **CONFIRM_WITH_CORRECTIONS: theorem interface.**

The exact plane level-one input is imported, not derived in the obstruction
packet.  The Hodge/four-row integration lists the row
`m=3, T=t0+t1, t1!=t0` with exact local CFS levels `(1,1)`
(`xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md:31`)
and states that the local CFS level equals the local Hodge/GR length exactly
(`...hodge-level-divisor-coordinator-integration-sol56-20260830.md:201`).
The obstruction restates the row hypotheses at
`xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-obstruction-sol56-20260830.md:62`.

The minimal floor-one claim is CFS plus strict-Henselian insolubility.  CFS
Theorem 3.5 says that a non-singular degree-3 model insoluble over `K^sh` has
minimal level at least one, and exactly one in residue characteristic not
dividing three.  Here the residue characteristic is zero.  Therefore the charged
plane model has level equal to the minimal floor and is minimal.

CFS Theorem 4.3 applies to each singular-line move only after the following
hypotheses are kept visible: generic non-singularity, `v(F)=0`, positive level,
integrality after the displayed move, and the displayed singular line in the
reduction.  These hold for `F`, for `E1` after `H!=0`, and for `E2` after the
zero-reduction case is excluded.  CFS Lemma 5.8 then applies because the moved
models remain `K`-equivalent to the same strictly-Henselian-insoluble torsor and
are minimal of level one.

The zero second reduction is handled correctly.  If `q2=C2=0`, then every
coefficient of `E2=t^-2 F(tx,ty,z)` is divisible by `t`.  Dividing by `t` gives
an integral `K`-equivalent model of level zero, since scalar division by the
uniformizer lowers the ternary-cubic level by one.  That contradicts the
floor-one theorem.  Correction for promotion: the theorem statement should name
generic non-singularity, strict-Henselian insolubility, and the scalar level-drop
convention explicitly; they are not consequences of the displayed coefficient
form or of the replay.

2. **CONFIRMED: raw three-cycle derivation.**

Start with the raw spatially homogeneous model

```text
F=x^3+tF1+t^2F2+t^3F3,
F1=a x^3+ell x^2y+m x^2z+x(q0y^2+q1yz+q2z^2)+H(y,z).
```

Normality forces `H!=0`; otherwise `F_t` vanishes generically along the central
line and the surface has a codimension-one singular locus
(`...weighted-boundary-obstruction-sol56-20260830.md:73`).  The first line move
`E1=t^-1F(tx,y,z)` has reduction `H`.  Since `E1` is again minimal,
strictly-Henselian-insoluble and level one, CFS Lemma 5.8 forces the nonzero
reduction to be a scalar cube.  Over `C`, a constant change on the central line
normalizes it to `H=y^3`.

The second line move has central reduction

```text
(E2)_0=z^2(q2x+C2z),        C2=[z^3]F2.
```

It is nonzero by item 1.  This cubic is a scalar cube if and only if the linear
factor `q2x+C2z` equals a nonzero scalar multiple of `z`, hence

```text
q2=0,       C2!=0.
```

There is no hidden stabilizer or scalar-cube exception: the residue field is
algebraically closed of characteristic zero, `C2` has a cube root, and
`q2*x*z^2` with `q2!=0` has two distinct linear factors.  The third move is

```text
t^-1E2(x,y,tz)=t^-3F(tx,ty,tz)=F,
```

using only spatial homogeneity of all `Fi`.  The exact cycle is
`x^3 -> y^3 -> C2 z^3 -> x^3`; after a residue scalar normalization it is
`x^3 -> y^3 -> z^3 -> x^3`.

3. **CONFIRMED: weighted-order computation.**

At `p=([0:0:1],t=0)`, set `z=1` and use weights

```text
w(x)=2,       w(y)=1,       w(t)=3.
```

The terms of weight below six are exhausted as follows.  The central term
`x^3` has weight six.  In `tF1`, the only possible lower term is `t*q2*x`, of
weight five, and item 2 gives `q2=0`.  The weight-six terms in `tF1` are exactly
`t*y^3` and `t*q1*x*y`.  The other `tF1` terms have weights seven or higher:
`t*m*x^2`, `t*q0*x*y^2`, `t*ell*x^2*y`, and `t*a*x^3`.

In `t^2F2(x,y,1)`, the constant `z^3` coefficient gives `C2*t^2`, of weight
six.  Every nonconstant term has at least one `x` or `y`, hence weight at least
seven.  Finally `t^3F3` has weight at least nine.  Therefore the complete face is

```text
P=x^3+t(y^3+q1xy)+C2t^2,
```

with no omitted lower or equal-weight term.

4. **CONFIRMED: curve in `P(2,1,3)`.**

The weighted exceptional curve is

```text
C={x^3+t(y^3+q1xy)+C2t^2=0} subset P(2,1,3).
```

The weighted plane is well formed.  Its only quotient coordinate points are
`[1:0:0]` and `[0:0:1]`, and the equation takes values `1` and `C2` there, so
`C` avoids them.  The point `[0:1:0]` is ordinary and has `P_t=1`.  If `y=0`
on `C`, then both `x` and `t` are nonzero and `P_t=2C2t!=0`; thus there is no
singularity at infinity or on a quotient locus.  All curve singularities lie in
the ordinary affine chart `y=1`.

On `y=1`, completing the square with

```text
W=2C2t+(1+q1x)
```

gives

```text
W^2=h(x),       h(x)=(1+q1x)^2-4C2x^3.
```

The cubic discriminant is

```text
Disc_x(h)=-16C2(q1^3+27C2).
```

If `q1^3+27C2!=0`, then `h` has three distinct finite roots.  Together with the
single branch point at infinity, the projective double cover has four branch
points and genus one.  Equivalently, this is a smooth anticanonical degree-six
curve in the smooth locus of `P(2,1,3)`.

If `q1^3+27C2=0`, then `q1!=0` and

```text
27h(x)=(q1x+3)^2(4q1x+3).
```

The double and simple roots are distinct, and
`h''(-3/q1)=-2q1^2/3!=0`.  The affine singularity is therefore an ordinary
node, not a cusp or triple-root specialization.  The polynomial `h` is not a
square in `C[x]`, so `W^2-h(x)` is irreducible.  The normalization is rational,
and the node identifies two distinct branches.  No additional weighted-projective
singularity modifies the boundary invariant.

Thus the exceptional contribution has `tau=1` in both strata: component genus
one in the smooth stratum, and one graph cycle after resolving the irreducible
nodal rational curve.

5. **CONFIRMED: weighted strict transform and cycle persistence.**

The weighted strict transform is local-hypersurface in the weight-one chart and
a finite cyclic quotient of such a hypersurface in the weight-two and
weight-three charts.  In characteristic zero the quotient groups are linearly
reductive, so the local rings are `S2`.  Away from the exceptional divisor the
weighted blowdown is an isomorphism.  At generic points of the exceptional curve
the reduced face is smooth, and the curve avoids the quotient points.  The
singular point in the equality stratum is isolated on the surface.  Hence
Serre's criterion gives normality of the weighted strict transform.

At the nodal point, the relevant chart is the ordinary `y`-chart

```text
x=r^2X,       y=r,       t=r^3T.
```

After division by `r^6`, the strict-transform equation is

```text
P(X,1,T)+r*(higher terms)=0.
```

The quadratic part of `P(X,1,T)` at the node is nondegenerate.  The formal or
analytic Morse lemma over `C[[r]]` puts the equation in the form

```text
uv+phi(r)=0.
```

If `phi=0`, the strict transform is singular along `u=v=0`, a codimension-one
singular locus on the surface, contradicting normality.  Hence
`phi` is nonzero; since `phi(0)=0`, after absorbing a unit it is `r^n` with
`n>=1`.  For `n=1`, the surface is smooth and resolving the self-node gives a
new exceptional curve meeting the strict transform of the globally irreducible
rational curve in two points, i.e. two parallel graph edges.  For `n>=2`, the
`A_(n-1)` chain resolves `uv+r^n=0` and joins the two local branches of the same
global component.  Retaining parallel edges, the resolved boundary graph has a
cycle for every `n`.

6. **CONFIRM_WITH_CORRECTIONS: actual-block identification.**

The finite-local step is correct and deliberately local.  At the affine target
point `(x,y)=(0,0)`,

```text
F(t;0,0,1)=C2t^2+C3t^3=t^2(C2+C3t),       C2!=0.
```

Weierstrass preparation makes the completed local incidence finite of degree
two over a sufficiently small target neighborhood.  This proves local
quasi-finiteness and local finiteness after shrinking, not global finiteness of
the projective incidence.

Under the charged occurrence hypothesis, this finite normal incidence germ has
the same function field as the intermediate block.  Then uniqueness of integral
closure identifies it with the local germ of the actual normal affine surface
`Y`.  This is the right ring-theoretic bridge, but it is conditional on actual
occurrence; a finite germ with the same displayed equation is not by itself an
abstract global row, a block, or a polynomial map.

The block-structure integration supplies

```text
A^2 --g1--> Y --g2--> A^2,
g1(A^2) subset Y_sm minus Ram(g2),
```

with `g1` everywhere defined, quasi-finite, etale and open
(`xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md:61`,
`...block-descent-structure-coordinator-integration-sol56-20260830.md:67`).
Since the center `p` is singular on `Y`, `p` is outside
`V=g1(A^2)`.  Every exceptional divisor over `p` is therefore boundary in a
smooth completion of `V`.

The morphic rational-forest theorem applies to `g1:A^2->V`, not to a merely
rational map and not to all of `Y`
(`xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md:18`,
`...rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md:27`).
It forbids positive-genus boundary components and boundary graph cycles,
retaining parallel edges.  Items 4 and 5 therefore contradict the actual morphic
block interface.  Correction for promotion: keep the occurrence hypothesis and
the passage to `V=g1(A^2)` in the theorem statement; the weighted local model
alone does not trigger the forest theorem.

7. **CONFIRMED: diagonal local control and occurrence firewalls.**

The diagonal model

```text
F_control=x^3+t y^3+t^2z^3
```

has the exact cycle `x^3 -> y^3 -> z^3 -> x^3`.  Its nonzero coefficient
valuations are `0,1,2` in the CFS critical ternary-cubic pattern.  CFS critical
models are strictly-Henselian-insoluble and minimal; in residue characteristic
zero their minimal level is one.  The valuation proof of insolubility is also
direct: the three term valuations are in distinct classes modulo three, so a
putative projective solution has a unique lowest-valuation summand.

The generic cubic is smooth because the three partial derivatives force
`x=y=z=0`.  The total local surface at `z=1` has an isolated singularity:
`F_x=3x^2`, `F_y=3ty^2`, and `F_t=y^3+2t` vanish simultaneously only at
`x=y=t=0`.  Hence the hypersurface germ is normal.  With `q1=0,C2=1`, the
weighted exceptional curve is in the smooth genus-one stratum.

This is a sharp negative control against any claim that CFS minimization and raw
base degree three alone eliminate the row.  It is only a local or formal germ.
It does not add the distinct support `t1`, prove a global class-`(3,3)` surface,
identify an actual intermediate block, define a Keller map, or make any
assertion about JC2.

8. **CONFIRM_WITH_CORRECTIONS: replay.**

The replay was run with SymPy 1.14.0 through `uv run --with sympy==1.14.0
--no-project` in ordinary, `-O`, and `-OO` modes.  The three outputs are
byte-identical:

```text
bytes: 547
SHA-256: d3a35f87dc841f0cdc4a6d613281999982ccea3d7813f2f4a6f07605eba07700
sympy_version: 1.14.0
```

The output records:

```text
line_move_1_reduction: y**3
line_move_2_reduction: C2*z**3 + q2*x*z**2
line_move_3_returns_input: true
weighted_face: C2*t**2 + q1*t*x*y + t*y**3 + x**3
weierstrass_discriminant: -16*C2*(27*C2 + q1**3)
nodal_second_derivative: -2*q1**2/3
orbifold_coordinate_values: ["1", "C2"]
```

The AST guard is real: the source has zero `ast.Assert` nodes, and optimization
does not remove checks.  The mutation
`--mutate-discriminant-sign` exits nonzero with
`FAIL:Weierstrass discriminant failed`.

The software proves only desk-scale coefficient algebra: line-move expansions,
the exact spatial-homogeneity cycle, weighted-face extraction, square completion,
discriminant and nodal-factorization identities, quotient coordinate avoidance,
and the diagonal control cycle.  It does not prove the Hodge/GR level theorem,
strict-Henselian insolubility, CFS Theorem 3.5, CFS Theorem 4.3, CFS Lemma 5.8,
normality of the weighted strict transform, the formal Morse reduction, graph
cycle persistence, Weierstrass/integral-closure actual-block identification, the
block-structure theorem, or the morphic rational-forest theorem.

## Overall Verdict

**CONFIRM_WITH_CORRECTIONS.**  I found no counterexample to the claimed
elimination of the actual-morphic row

```text
m=3, T=t0+t1, t1!=t0, exact local levels (1,1).
```

The mathematical obstruction is coherent under the stated actual-occurrence
hypothesis.  The corrections are scope and interface corrections: the theorem
must explicitly retain generic non-singularity, exact level one, strict-
Henselian-insoluble floor one, normality, actual local incidence with the
intermediate block, and application to the open image `V=g1(A^2)`.  The local
weighted model by itself is not an occurrence theorem.

## Maximum-Safe Theorem

Let `R=C[[t]]`, and let

```text
F=x^3+tF1+t^2F2+t^3F3
```

be the raw degree-three spatially homogeneous local model of the charged
two-support triple-fibre row at `t0`, with smooth generic ternary cubic, normal
total incidence germ, exact CFS level one, and strictly-Henselian-insoluble
minimal floor one.  Assume further that this normal local incidence is the
actual local normal incidence of a hypothetical proper intermediate block.

Then the first two CFS line moves force

```text
H=y^3,       q2=0,       C2=[z^3]F2 != 0,
```

and the third move returns the exact cycle

```text
x^3 -> y^3 -> C2 z^3 -> x^3.
```

At the unique singular center over the central triple line, the `(2,1,3)`
weighted blowup has complete face

```text
x^3+t(y^3+q1xy)+C2t^2.
```

Its exceptional curve in `P(2,1,3)` has boundary invariant one for every
`q1` and every `C2!=0`: either it is smooth of genus one, or it is irreducible
rational with one ordinary node whose resolution creates a dual-graph cycle.
Because the actual etale first leg from `A^2` misses the singular center, this
configuration lies in the boundary of `V=g1(A^2)`, contradicting the morphic
rational-forest theorem.  Therefore the charged actual-morphic row cannot occur.

This theorem does not rule out local formal controls, abstract nonmorphic
global Halphen surfaces, an unproved global occurrence class, a polynomial map,
a counterexample, or JC2.

## Cheapest Successor

Promote only the maximum-safe theorem above, then package three small interface
lemmas for independent review:

1. the level-one CFS critical-cycle lemma with the zero-second-reduction division
   step stated explicitly;
2. the weighted-boundary lemma proving `tau=1` for the face curve and persistence
   through `uv+r^n`;
3. the actual-block transfer lemma from local Weierstrass finiteness and integral
   closure to boundary inside `V=g1(A^2)`.

No heavy CAS is indicated.  The remaining risk is not coefficient algebra; it is
the actual-occurrence interface that identifies the finite local incidence with a
proper intermediate block.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17323`.
- Body SHA-256:
  `ee5660318bda0d013bfd4258d8157f1eb05936a22a095f26bd28e9ff345fe566`.
- Frozen basis: `5775cfc63803dbb99b6d4574f8e91e201790f3c0`.
