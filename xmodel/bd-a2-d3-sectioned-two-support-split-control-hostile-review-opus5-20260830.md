# Hostile review: D3 sectioned two-support split control

Date: 2026-08-30 UTC
Reviewer: Opus 5, fresh hostile lane, independent reconstruction
Subject: `xmodel/bd-a2-d3-sectioned-two-support-split-control-sol56-20260830.md`
Verdict: **CONFIRM_WITH_CORRECTIONS**

No counterexample to the mathematical content was found.  Every load-bearing
geometric claim reproduced, several by routes independent of the ones the
report uses.  Two software-layer corrections and two exposition gaps are
recorded; neither touches the conclusion.  This review asserts no exit price,
so no `charge_basis` line is emitted and receipt status `ABSENT` is expected.

## 0. Custody

All five charged hashes reproduced byte-exactly:

```text
dcdfaabcdaf3d8c71111a207ea75ddcb8784cf8f164051df7b2cd54b8e51d4e7  ...split-control-sol56-20260830.md
77b9188d28ad3dd9b4674971e36deb0f7c02048d541b6fcd4815ee8dad3ce3a1  ...split-control-sol56-20260830.md.artifact.json
996dffc8d3215fb099c672a4cb5ae7840403d2988e5df9b864f8bb0886179a48  ops/bd_a2_d3_sectioned_two_support_control_replay.py
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de  ...d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d  ...rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
```

Independent body recomputation of the primary report: `12539` body bytes,
body SHA-256 `6975f482e1f2eeb6d5277623951dd3c82a3a9bc3258ee00ac636169a65e01c6b`,
file bytes `12872`.  All three agree with the artifact JSON.  The literal
string `<!-- BODY-END -->` occurs twice, but only once as a standalone line;
the second occurrence is inside backticks in the seal, so the "unique
standalone" body definition is well posed and the stamp is honest.

## 1. Reverse operator, shear, section, degree cap — `CONFIRMED`

`R_u(H)=u^3 H(t;X/u,y/u,z)` obeys the composition law `R_u R_w = R_{uw}`
exactly, so the double reverse identity (0.3) holds for **general** `a,b`,
not merely for the specialization.  Verified symbolically; a first attempt
using `expand` on the difference of the composed and direct forms returned a
spurious nonzero because `expand` does not clear the rational-function
denominators introduced by the product argument — `simplify`/`cancel` give
zero.  This is a sympy normal-form artifact, not a mathematical discrepancy,
and it is worth recording because the same trap can produce a false REFUTED.

The shear identity (1.1), `t(x+(t-a-b)z)-(t-a)(t-b)z = tx-abz`, is exact, and
(0.4) follows.  The literal raw `t`-degree of every `(x,y,z)`-monomial
coefficient of `F_(a,b)` is `<= 3` for generic `a,b`, and `3` is attained, so
the closure genuinely has class `(3,3)` rather than a degenerate sub-class.
The specialization `(a,b)=(1,-1)` reproduces (0.5) exactly, with

```text
F = x^3 + t(3x^2z+y^3+yz^2) + t^2(3xz^2+2xyz) + t^3(x^2y+z^3).
```

The section (1.2) `[S:T] |-> [(a+b)S-T:0:S]` lies on `F_(a,b)` identically for
general `a,b` (verified as an identity in `S,T,a,b`), and specializes to
`[-T:0:S]`.  It is the `y=0` locus of the fibre, where `F_(a,b)` collapses to
`(x+(t-a-b)z)^3`.

**New leverage supplied by this review.**  The reverse move has an exact
invariant weight.  For a ternary cubic, `c4` and `c6` are the degree-`4` and
degree-`6` generators of the invariant ring, of weights `4` and `6`.  `R_u`
combines the substitution `diag(1/u,1/u,1)` (determinant `u^{-2}`) with the
scaling `u^3`, giving total factor `mu = u^3 * u^{-2} = u`.  Hence

```text
R_u : (c4,c6,Delta) |-> (u^4 c4, u^6 c6, u^12 Delta),
```

which is *precisely* a CFS level raise by `ord(u)`.  The shear is unimodular
and inert.  This makes the report's "reverse `(1,1)` move" terminology a
theorem rather than a naming convention, and it is what drives Section 2.

## 2. Generic pointed cubic, invariants, Kodaira row — `CONFIRMED`

The substitution `z = tX - W` (determinant `-1`, inert) turns `H_0` into
`K = X^3 + t y (y^2 + W^2)`, and the further `(y,W) -> (p,q)` diagonalization
gives the normal form

```text
K' = X^3 + (t/2) * p q (p+q).
```

Under `(p,q) -> (alpha p, alpha q)` (determinant `alpha^2`, `mu = alpha^2`),
`K'_c` maps to `K'_{c alpha^3}`, so `S(K'_c) = c^{8/3} S(K'_1)` and
`T(K'_c) = c^4 T(K'_1)`.  Polynomiality in `c` forces `S ≡ 0`, and `T(K'_1)`
is nonzero because `X^3+pq(p+q)` is smooth (checked).  Combining with the
weight law of Section 1:

```text
c4(F) = 0 identically,
c6(F) ∝ t^4 (t^2-1)^6,
Delta(F) = -c6^2/1728 ∝ t^8 (t^2-1)^12.
```

This reproduces (1.4) **up to nonzero constants, as stated**, without any
Aronhold-formula convention risk.  I did not attempt a direct degree-12
resultant; the weight route is stronger because it is convention-free.

Independent corroboration: elimination in all three `P^2` charts shows the
plane fibre `F_t` is singular exactly for `t in {0,1,-1}` (chart `z=1` gives
`t(t-1)^5(t+1)^5`, chart `x=1` gives `(t-1)^5(t+1)^5`, chart `y=1` gives `t`),
matching the zero set of `Delta` exactly.

Weierstrass form.  On `y=1`, `H_0 = X^3+t+tW^2`, and `U=-tX`, `V=t^2W` give
`V^2-U^3+t^4 = t^3(X^3+t+tW^2)`, i.e. (1.3).  The section supplies a rational
point, so this is the curve itself, not merely its Jacobian.

Orders and Kodaira types:

| place | `(v c4, v c6, v Delta)` | CFS level | minimal type |
|---|---|---:|---|
| `t=0` | `(inf,4,8)` | `0` | `IV*` |
| `t=+1` | `(inf,6,12)` | `1` | good |
| `t=-1` | `(inf,6,12)` | `1` | good |
| `t=inf` | `(inf,2,4)` | `0` | `IV` |

The infinity orders are obtained by homogenizing to degrees `18,36`, which is
the correct normalization: the chart change `t -> 1/s` multiplies the cubic by
`s^3`, hence `c4,c6,Delta` by `s^12,s^18,s^36`.  With `v(c6)=4<6` at `t=0` and
`v(c6)=2<6` at `t=inf`, the plane model is already minimal there, so there is
**no** GR defect at `0` or `inf`.  At `t=+-1` the coordinator's exactness gate
(5.2) is satisfied through its second disjunct `v(c6)=6<12`, so the level is
exactly `1`, not `>=2`.  `Delta` degree `8+4=12`, Euler number `8+4=12`,
`chi=1`, section present: rational elliptic surface with fibres `IV*+IV`.
`X` is birational to it, hence rational.  The Hodge row (0.6) is row 1 of the
coordinator's four-row table, with `m=1` (the Weierstrass zero section exists
and neither `IV*` nor `IV` is a multiple fibre).

**Plane-model versus total-space distinction.**  These are genuinely different
and the report keeps them apart correctly:

- `t=0`: the plane fibre is the *triple line* `x^3=0` (non-reduced), but the
  total space carries only three `A2` points on it.  A triple *plane* fibre
  does not make `m=3`; the coordinator's implication runs the other way.
- `t=+-1`: the plane fibre is `X^3 ± X^2 y ± y^3` in `X=x+tz`, a binary cubic
  of discriminant `-31 != 0`, i.e. **three distinct concurrent lines** through
  `p_±`.  The total space has one triple point there.
- `t=inf`: the plane fibre is the cuspidal cubic `z^3+x^2y`; the total space
  has one `A2`.

## 3. Basepoint freeness, finite flatness, full singular locus — `CONFIRMED`

Coefficients (2.1) reproduce exactly.  The triangular basepoint argument is
correct: `A_0=0 => x=0`; then `A_3 = z^3 => z=0`; then `A_1 = y^3 => y=0`.
Hence `pi` is projective with length-three fibres, so finite; `X` is a
hypersurface in a smooth fourfold hence Cohen–Macaulay, `P^2` is regular of
the same dimension, so miracle flatness gives locally free rank three.

I did **not** accept the report's reduction of the singular-locus audit to
four base values.  Instead I solved the full Jacobian system by brute force in
all six affine charts `(S=1,T=1) x (x=1,y=1,z=1)`.  The complete singular set
is exactly (2.3) and nothing else:

```text
t=+1: [-1:0:1]      t=-1: [1:0:1]
t=0 : [0:0:1], [0:i:1], [0:-i:1]
t=inf: [0:1:0]
```

No missing chart, no unlisted fibre singularity.  (The report's reduction is
also sound in principle: flatness plus fibre smoothness at a point implies
total-space smoothness there, so singularities can only sit over `0,±1,inf`.)

Integrality: `G` has no vertical factor because `F(t_0)` retains the `x^3`
term for finite `t_0` and equals `z^3+x^2y != 0` at infinity; the generic
fibre is a smooth plane cubic over `C(t)`, hence geometrically integral, so
`G` is irreducible and reduced.  `S_2` from hypersurface CM, `R_1` from the
codimension-two isolated singular set, Serre gives normality.  All `CONFIRMED`.

## 4. Tangent cones and blowup — `CONFIRM_WITH_CORRECTIONS`

Deriving the tangent cones directly from `F` with no reverse-move
interpretation, both defect points have multiplicity exactly three (no linear
or quadratic terms) with

```text
TC_+ = X^3 + X^2 Y + 3X^2 T - 2XYT + 3XT^2 + Y^3 + YT^2 + T^3,
TC_- = X^3 - X^2 Y + 3X^2 T + 2XYT + 3XT^2 - Y^3 - YT^2 + T^3,
```

in the local coordinates `X=x-x_0`, `Y=y`, `T=t-a`.  Both are projectively
smooth plane cubics (full three-chart Groebner Jacobian test, unit ideal in
every chart).

**Correction.**  The report's (3.1) states that the tangent cone "is exactly"
`X^3+a y^3+a(aX-tau)^2 y`.  In the literal `(x,y,z,t)` coordinates it is not;
the raw cones above differ from (3.1) by the linear part of the *unit* reverse
move that the report removes one sentence earlier.  The exact equivalences are

```text
a=+1:  TC_+ = 8 * C_{+1}( (X+T)/2, Y/2, T ),
a=-1:  TC_- = -8 * C_{-1}( -(X+T)/2, -Y/2, T ),
```

both verified as identities.  These are invertible linear substitutions
(determinants `1/4` up to sign), so (3.1) is correct as a statement about the
germ up to analytic isomorphism and the smoothness conclusion is untouched;
the wording "is exactly" should read "is projectively equivalent to".  The
same slack appears in the charged replay, which tests `C_plus = X^3+Y^3+
(X-2q)^2 Y` — yet another rescale (`tau = 2q`) of the same cubic.  Harmless,
but three different representatives are in circulation for one object.

The resolution claim is correct.  A multiplicity-`m` germ whose projectivized
tangent cone is smooth is an ordinary `m`-fold point: in a blowup chart the
strict transform is `f_m(1,u,v) + X_1(...)`, whose differential along `E` is
`df_m`, nonzero by smoothness of the cone.  So one ordinary blowup resolves
each germ, `E_± ≅ C_±` is a smooth plane cubic of genus one with `E_±^2 = -3`,
and each point is a simple elliptic singularity of degree three with
discrepancy exactly `-1`.  These are the only non-Du-Val points, and
`D = -F_1 - F_{-1}` follows because the fibre of `S` over `t=±1` is smooth and
`E_±` maps isomorphically onto it.

**Sharpness note.**  `ord_{E}(t-1) = 1`, so the `Y`-fibre over `t=1` is
`L'_1+L'_2+L'_3+E_1` with `E_1.(sum L'_i) = -E_1^2 = 3`, `L'_i.L'_j = 0` and
`L'^2_i = -1`.  Three `(-1)`-curves are contracted over each defect, so
`rho(Y) >= 10+6 = 16` for this surface.  The report's `rho(Y) >= 12` is the
coordinator's row bound and is correct, but this witness does not exhibit the
bound's sharpness.

**Hypothesis audit (the part the prompt asks to be precise about).**  Putting
`E_±` in the boundary requires, and only requires, the promoted interface
(4.1) of the rational-forest coordinator:

```text
A2 --g1--> Y --g2--> A2,   V = g1(A2) subset Y_sm minus Ram(g2),
g1 : A2 -> V everywhere-defined, surjective, etale.
```

The chain is: `V subset X_sm`, so the minimal resolution `r` is an isomorphism
over `V`; take a smooth projective `W` containing `V` with SNC boundary `B`;
then `E_± subset B` because `E_±` is complete and disjoint from `V`; boundary
blowups only subdivide, so a genus-one component survives; the morphic theorem
forces `tau(B)=0`, contradiction.  Crucially this uses the **morphic** theorem.
Mere rational domination is refuted by the coordinator's own `P^2 minus E`
counterexample, and the report says so explicitly in §0 and §3.  I confirm the
report never leans on rational domination, abstract rationality, or a local
algebra match.  The report does *consume* (4.1) without restating why `V`
avoids `Ram(g2)`; that is a legitimate consumption of a promoted result, but
it is a live external dependency, not something this report establishes.

## 5. Ramification, `P`, and genus three — `CONFIRMED`

Target discriminant.  With the standard binary-cubic discriminant,

```text
Disc_[S:T](F) = -y^2 * B_10,   deg B_10 = 10,   B_10 squarefree, Q-irreducible,
```

reproducing (5.1) exactly including sign.  On `y=0` the binary cubic is
`(Sx+Tz)^3`: totally ramified, tame, different exponent `e-1 = 2`, matching
the `y^2`.  The section maps isomorphically onto the line `y=0`.

Elimination.  With `x=1`, `z=(u-1)/t`, `u=qy`, one gets
`t F = y A` and `t^2 F_t = y B`, and

```text
Res_y(A,B) = t^2 (t-1)^2 (t+1)^2 * P,
P = 9q^7t + 12q^6t^2 + q^6 + 4q^5t^3 + 9q^4t^2 + 8q^3t^3 + 4q^2t^4 + 4t^6,
```

reproducing (5.3) exactly.

**Gap closed.**  The report does not justify discarding `t^2(t-1)^2(t+1)^2`.
It is discardable, and here is the reason.  The two leading `y`-coefficients
`q^3t+q^2+t^2` and `3q^3t+q^2+t^2` vanish simultaneously only at `(0,0)`, so
away from the origin the resultant vanishes exactly where a common root
exists.  At `t=±1`, `A` degenerates to `y^2 *(q^3±q^2±1)` and `B` to
`y*(...)`, so the only common root is `y=0` — the already-removed section.  At
`t=0`, `A=B=(qy-1)^2`, whose common root `y=1/q` has `z=(qy-1)/t = 0/0`, an
indeterminacy of the chart map; and independently `t=0` cannot lie on `X` over
`x != 0` because `A_0 = x^3 != 0`.  Both factors are therefore extraneous.

**Birational, not merely dominant.**  `A,B` are quadratic in `y`, and
`L = b_2 A - a_2 B` is exactly linear in `y` with

```text
lead_y(L) = q t (3q^4t + 2q^3t^2 - q^3 - 2q^2t + 3qt^2 - 2t^3),
gcd(P, lead_y(L)) = 1.
```

So `lead_y(L)` does not vanish identically on `P=0`, and `y` — hence `z` — is a
rational function of `(q,t)` on the curve.  The transfer is birational.

**Absolute irreducibility, certified independently.**  The report's Singular
check is not usable (see §7), so I supplied a certificate.  `P` is irreducible
over `Q` and squarefree (sympy).  In the chart `q=1/r`, `t=w/r`,

```text
r^8 P = w(2w+3)^2 + r^2(4w^6+4w^4+8w^3+9w^2+1),
```

and at `(r,w)=(0,0)` — the point `[1:0:0]` — the curve passes with
`d/dw = 9 != 0`, so `[1:0:0]` is a **smooth `Q`-rational point**.  If `P` had
`k>=2` absolute factors they would be transitively permuted by
`Gal(Qbar/Q)`, so any `Q`-point would lie on all of them and be singular.
Hence `k=1`: `P` is absolutely irreducible.  This also upgrades the report's
"exact absolute factorization ... finds one factor" from an unusable software
appeal to a proved statement.

**Newton polygon.**  Support `{(0,6),(2,4),(3,3),(4,2),(5,3),(6,0),(6,2),(7,1)}`;
convex hull vertices exactly `(0,6),(6,0),(7,1),(5,3)` as in (5.4); `2*Area =
16`, `Area = 8`; boundary lattice intervals `10`; interior lattice points `4`
(Pick: `8 = 4 + 10/2 - 1`).  All four numbers confirmed.

**Nondegeneracy.**  `P` has no singular point in the torus (Groebner with
`aux*q*t-1`).  Three edge truncations are nondegenerate:
`q^6+9q^4t^2+8q^3t^3+4q^2t^4+4t^6`, `q^6(9qt+1)`, `4t^3(q^5+t^3)`.  The fourth,
on the edge `(7,1)-(5,3)`, is `q^5 t (3q+2t)^2` — exactly (5.5) — and is
degenerate.

**The node.**  In the chart `q=1/r,t=w/r` with `v=w+3/2`, the local expansion
has **zero constant and zero linear term** and quadratic part

```text
961 r^2 / 16 - 6 v^2,
```

of rank two — exactly (5.6), an ordinary node with `delta = 1`.  (I checked
the vanishing of the linear term explicitly; a double intersection with the
line at infinity would otherwise be consistent with a smooth tangency point,
and the report does not state this check.)  The other boundary point on that
divisor, `w=0`, is smooth (`d/dw = 9`).

**No other boundary singularity.**  The outer normals are `(-1,-1)`, `(1,-1)`,
`(1,1)`, `(3,5)`, all four cones of determinant `2`, so `X_Delta` has four
`A1` points at the torus-fixed points.  Vertex truncations are monomials, so
`Cbar` avoids all of them; a smooth toric refinement adds only rays interior
to cones, whose faces are vertices, so `Cbar` meets no new divisor.  `Cbar`
therefore lies in the smooth locus, meeting the boundary in `6+1+1+1` points of
which only the node is singular.  The node lies in the open orbit of the ray
`(1,1)`, over which `X_Delta -> P^2` is an isomorphism, so the `P^2`-chart
computation of the node is legitimate.

```text
g(R'^nu) = #interior(Delta) - delta = 4 - 1 = 3.
```

**Independent second route to genus three.**  In `P^2`, `deg P = 8`, so
`p_a = 21`.  The origin is an *ordinary* six-fold point: the degree-six form is
the `(0,6)-(6,0)` edge truncation, which is squarefree with nonzero `q^6` and
`t^6` coefficients, hence six distinct lines, `delta = 15`.  At `[0:1:0]` the
germ is `rho^2 * u(sigma) + sigma^5 (3sigma+2)^2` with `u(0)=4`, i.e. `A_4`,
`delta = 2`.  `[1:0:0]` is smooth.  With the node,

```text
21 - 15 - 2 - 1 - 0 = 3.
```

Two structurally independent computations agree.  (This also explains why the
toric picture is the right one: the `A_4` and the six-fold point are artifacts
of the `P^2` compactification and are separated by `X_Delta`.)

**No lost component, no base factor.**  `X` is Gorenstein with
`K_X = O(0,1)|_X` and `pi^* K_{P^2} = O(-3,0)|_X`, so the ramification divisor
is `R = O(3,1)|_X` and, with `h^3=0`, `f^2=0`, `h^2 f = 1`,

```text
R . h = (3h+f).h.(3h+3f) = 12.
```

The section contributes `2 * 1 = 2`, leaving exactly `10` for the residual —
which matches `deg B_10 = 10` with `pi|_{R'}` birational.  There is no room for
an extra component.  I separately excluded residual components over each
omitted locus: over `x=0` the binary cubic is `T(A_1 S^2 + A_3 T^2)` with three
distinct roots generically; over `t=0` the fibre is the line `x=0` and `T=0` is
a simple root wherever `A_1 != 0`; over `t=±1` the three concurrent lines are
Galois-conjugate (`X^3+X^2+1` and `X^3-X^2-1` are `Q`-irreducible) so a common
line would force `F(t=±1) | F_t(t=±1)`, which is false; over `y=0` the fibre is
a single totally ramified point, the section.  No lost component, no base
factor, no boundary singularity, no delta defect.

## 6. Does either curve give a control-specific contradiction? — `CONFIRMED, but surface-specific`

Both witnesses work, conditionally on the two promoted coordinator theorems:

- `E_±`: complete, genus one, disjoint from `V subset X_sm`, hence a
  positive-genus boundary component.  Contradiction with `tau(B)=0`.
- `R'`: complete and irreducible with `g(R'^nu) = 3`.  Its points over the
  affine target lie in `Ram(g2)` and are excluded by (4.1); its points over the
  target line at infinity are not in the domain of `g2 : Y -> A^2` at all.
  Either way `R' ∩ V = empty`.  Making the boundary SNC replaces `R'` by its
  normalization, still genus three.  Same contradiction.

Two qualifications the report should carry:

1. The report calls these "two independent reasons".  They are two independent
   *witnesses*; both route through the **same** theorem (`tau(D)=0` from the
   morphic rational-forest correction).  A single failure of that theorem would
   remove both.  This is not a fallacy in the report's sense, but the
   independence is weaker than the phrasing suggests.
2. The exclusion is about **this surface** as a globally identified second leg.
   It does not empty the sectioned row.  The row is a positive-dimensional
   family (the coordinator itself flags (5.3) as finite-dimensional, not a
   finite orbit set), and nothing here forbids some other row-1 surface whose
   defect germs and ramification are more favourable.  The report's §0 and §7
   are correctly scoped; I found no over-claim.

## 7. Replay — `CONFIRM_WITH_CORRECTIONS`

**Charged standalone script — clean.**  `ops/bd_a2_d3_sectioned_two_support_control_replay.py`
has **0** AST `assert` nodes and 17 `require()` calls.  Ordinary, `-O` and
`-OO` runs produce byte-identical JSON and exit `0`.

Because a passing replay proves nothing unless its gates are live, I
fault-injected six mutations into the real checked quantities (not just the
three built-in negative controls) and confirmed each fails with the correct
label under **both** plain and `-O`:

| mutation | label raised |
|---|---|
| `t(tx+z)^2 y -> t(tx+2z)^2 y` | `bihomogeneous dehomogenization` |
| `t^4 -> t^5` in Weierstrass | `generic Weierstrass identity` |
| `u = t-1 -> t-2` | `two reverse CFS moves and shear` |
| `A_3 += y^3` | `binary-cubic coefficient expansion` |
| `C_plus -> X^3+Y^3` | `smooth plus tangent cubic` |
| `y^3+y -> y^3-y` | `t=0 transverse polynomial` |

The script's own three mutation gates (deleted `z^3` creating the basepoint
`[0:0:1]`; `q` deleted from the tangent cone; perturbed double-reverse factor)
also fire correctly.  No vacuous-pass hole.

**Correction 1 — the §6 desk replay fails open.**  Unlike the `ops/` script,
the in-report §6 heredoc uses **11 bare `assert` statements**.  It reproduces
`D3_SECTIONED_TWO_SUPPORT_SPLIT_CONTROL_PASS` as printed.  But I falsified two
of its inputs simultaneously — `H_0` (`z -> 7z`) and the elimination
polynomial (`4t^6 -> 5t^6`) — and under `python3 -O` it still printed the PASS
banner with exit `0`, while plain `python3` correctly raised.  Any consumer
running the published block under `-O` gets an unconditional pass.  This is the
fail-open pattern already flagged for the sectioned-output contract; the
`ops/` script is the correct model and §6 should be rewritten to match it.

**Correction 2 — the Singular absolute-factorization check is vacuous.**  The
report instructs `list L=absFactorize(P); size(L);` and states "The expected
factor count is `1`."  In Singular 4.4.1, `absFactorize` returns a **ring**
carrying a list `absolute_factors`, not a list of factors.  Probing it:

```text
absFactorize(q2+t2)        -> size(L) = 1   (2 absolute factors)
absFactorize(q2-t2)        -> size(L) = 1   (2 rational factors)
absFactorize(q3+q2+qt+t2)  -> size(L) = 1   (absolutely irreducible)
```

`size(L)` is `1` for every input, reducible or not.  The check cannot fail and
therefore certifies nothing.  Correct usage is
`def S = absFactorize(P); setring(S); absolute_factors;` and then inspecting
`size(absolute_factors[1])`.  Separately, `absFactorize(P)` did **not**
complete within a 120 s local budget, so I did not reproduce it at all; per
the no-heavy-CAS instruction I stopped there and substituted the smooth
`Q`-rational-point certificate of §5, which settles the claim rigorously
without a CAS.  **The mathematical claim is true; only the published check is
worthless.**

**Residual-resultant check — reproduced.**  `Res_y(A,B) = t^2(t-1)^2(t+1)^2 P`
reproduced exactly, independently of the §6 block.

**Hand proof versus software output.**  Software (either replay) covers only:
the dehomogenization and coefficient identities; the triangular basepoint
steps; the double-reverse-plus-shear identity; the Weierstrass identity (1.3);
the `t=0` transverse polynomial and its simple roots; the infinity-chart
identity and its determinant; projective smoothness of the two tangent cubics;
the resultant identity; the Newton-polygon arithmetic; the torus/edge
Groebner nondegeneracy tests; and the node's quadratic factorization.

Everything else is hand proof and was re-derived here rather than accepted:
finite ⟹ miracle flatness ⟹ rank three; irreducibility of `G` and hence
integrality; `S_2 + R_1` ⟹ normality; the reduction of the singular-locus
audit and its brute-force replacement; the splitting lemma converting the
verified 2-jets into `A_2` (the replay supplies only the inputs); the ordinary
multiple point ⟹ one blowup resolves; simple elliptic ⟹ genus one and
discrepancy `-1`; Tate's table for `IV*`/`IV` and rationality of the elliptic
surface; the CFS exactness gate; the different exponent `2` on the section; the
extraneity of `t^2(t±1)^2`; the birationality of the transfer; absolute
irreducibility; the toric genus formula with delta correction and the `P^2`
adjunction cross-check; the ramification degree count `R.h = 12 = 2 + 10`; and
the entire proper-block exclusion, which consumes two promoted coordinator
theorems that are not charged to this review.  The report's own §6 self-
declaration is accurate as far as it goes but omits the splitting lemma,
Tate's table, and the extraneous-factor argument.

## 8. Price — narrow

| claim | status |
|---|---|
| Abstract surface-level attainment of the sectioned row | **ACHIEVED** |
| Actual proper-block occurrence for **this** surface | **EXCLUDED**, conditional on (4.1) + morphic rational forest |
| Family-wide row theorem | **NOT ACHIEVED**, and not claimed |
| Polynomial map | none |
| JC2 | none |

Precisely what is now attained: there exists an integral, normal, rational
class-`(3,3)` hypersurface in `P^2 x P^1`, with a section, whose target
projection is finite flat of degree three, realizing row 1 of the D3 four-row
table with `m=1`, `T=[1]+[-1]`, exact CFS levels `(1,1)`, `D=-F_1-F_{-1}` and
`rho(Y) >= 16`.  Row 1 is therefore nonempty at the surface level.  This is a
`FULL_ACTUAL` surface witness but a `REPRESENTATIVE`-only statement about the
row: it is one member of a positive-dimensional family, and its own exclusion
from proper-block occurrence transfers to no other member without new work.

## Maximum-safe theorem

> Let `F = (x+tz)^3 + t y^3 + t(tx+z)^2 y` and let `X subset P^2 x P^1` be its
> class-`(3,3)` closure.  Then `X` is integral, normal and rational; the
> projection `pi : X -> P^2` is finite flat of degree three; `X` has exactly
> six singular points, namely three `A_2` over `t=0`, one `A_2` over
> `t=inf`, and two simple elliptic points of degree three over `t=±1` whose
> minimal resolution has exceptional curve a smooth plane cubic with
> self-intersection `-3` and discrepancy `-1`.  Its plane invariants are
> `c4 = 0`, `c6 ∝ t^4(t^2-1)^6`, `Delta ∝ t^8(t^2-1)^12`; the associated
> minimal elliptic surface is the rational elliptic surface with fibres
> `IV* + IV` and a section.  Hence `X` realizes the sectioned row `m=1`,
> `T=[1]+[-1]`, `D = -F_1 - F_{-1}`, exact local CFS levels `(1,1)`, with
> `rho(Y) >= 16`.  The ramification divisor of `pi` is
> `2 C_sec + R'` with `C_sec` the section over the line `y=0` and `R'`
> irreducible, birational to the absolutely irreducible curve
> `9q^7t+12q^6t^2+q^6+4q^5t^3+9q^4t^2+8q^3t^3+4q^2t^4+4t^6 = 0`, whose
> normalization has genus three.
>
> Consequently, **assuming** the promoted proper-block interface
> `V = g1(A^2) subset Y_sm minus Ram(g2)` with `g1` an everywhere-defined
> surjective etale morphism from `A^2`, and the promoted morphic
> rational-forest theorem, this `X` cannot be the globally identified second
> leg of an actual proper block: either exceptional elliptic curve, or the
> genus-three normalized ramification component, is a positive-genus boundary
> component of any smooth SNC completion of `V`.

Everything before "Consequently" is unconditional and was verified here.  The
conditional clause consumes two promoted theorems that this review did not
re-derive and could not inspect.

## Cheapest useful successor

Promote the observation from row structure to row theorem.  The coordinator's
rows `1` and `3` both have `b_t = 1` at each of two distinct defect base
points, i.e. **discrepancy exactly `-1`**: the defect germs are Gorenstein log
canonical but not canonical, hence simple elliptic or cusp.  A simple elliptic
germ contributes a genus-one boundary component; a cusp contributes a cycle of
rational curves, and the coordinator's own parallel-edge accounting already
makes a two-edge cycle fatal.  Both are forbidden by the morphic
rational-forest theorem *independently of any particular equation*.

The successor is therefore: **prove that at every exact-CFS-level-one defect
point of a row-1 or row-3 surface, the discrepancy is exactly `-1` and the
exceptional locus of the minimal good resolution has a positive-genus component
or a cycle.**  Success empties rows `1` and `3` of actual proper-block
occurrence for all class-`(3,3)` second legs at once, which is a genuinely
universal statement, and the present surface becomes its witness rather than
its content.

Two risks must be priced, not capped:

1. `h_*` can discard exceptional components, so `b_t = 1` in `D = h_* Delta`
   does not immediately force minimal discrepancy `-1` on `X`; a component of
   discrepancy `< -1` contracted by `h` must be excluded.  Doing this needs the
   coordinator's §4 blowup induction run in the reverse direction.
2. Laufer's classification of minimally elliptic germs includes exceptional
   sets that are a rational curve with a **cusp**, whose SNC resolution is a
   tree of rational curves and is *not* forbidden.  That case must be ruled out
   separately, or the theorem restricted.

Rows `2` and `4` (`b >= 2`) are strictly worse singularities and should follow,
but they are a separate obligation and must not be assumed by analogy.  If
either risk cannot be discharged, the correct output is typed `OPEN` for the
row theorem while the single-surface result of this review stands unchanged.

## Execution and scope disclosures

- All computation was local sympy plus three short Singular probes.  No AWS.
- `Singular absFactorize(P)` did **not** complete within 120 s and was
  abandoned per the no-heavy-CAS instruction; §5 supplies a CAS-free proof of
  the same claim instead.  The report's stated Singular check was additionally
  shown to be non-discriminating, so it is not evidence either way.
- I did not read, list, or execute anything under `jc2-lean`, and read no
  sibling external-model prompt, log, report, or receipt.
- No charged input, ledger, Git state, or unrelated file was modified; this
  review wrote exactly one file.
- The two coordinator theorems consumed by the conclusion were read as charged
  inputs but were **not** re-derived; the exclusion in §6 is conditional on
  them.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30002`.
- Body SHA-256:
  `b126a20364a30e4c4517289eb38f42f8b70e73c8c0cc37c451ba7d12e1103950`.
- Frozen basis: `f1f10d94730606b7c5a9b3e78a362110d4ab2b6f`.
