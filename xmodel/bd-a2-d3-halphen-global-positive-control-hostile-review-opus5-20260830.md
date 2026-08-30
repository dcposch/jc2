# Hostile review: D3 Halphen global positive control and ramification obstruction

Date: 2026-08-30 UTC
Reviewer: Opus 5, fresh hostile reviewer, independent reconstruction
Reviewed basis: `effb538eb858ff2c51d713a91f392d90796e786e`
Exit price: **none asserted** (`charge_basis` deliberately omitted; receipt `ABSENT`)

## 0. Custody

All seven charged files hash byte-exactly as specified. The primary report's
seal verifies independently: taking the body as every byte through and
including its unique standalone end-of-body marker line gives `7859` bytes with
SHA-256 `47791910632b8985b9d6bebc116c0bfc2fc0575222fcb590431b24b9ac3739cd`,
matching both the seal block and the artifact manifest (`file_bytes` 8191
confirmed on disk). Exactly one such marker precedes the seal.

I read only the seven charged files. I did not read any sibling review,
prompt, log, or receipt; I did not inspect, list, search, stat, build, modify
or control `jc2-lean`; I modified no repository file except by creating this
single report. All computation below is my own reconstruction, run under
`uv run --with sympy==1.14.0`; where I reuse a route I say so.

## 1. Binary-cubic coefficients, finiteness, degree, miracle flatness

`CONFIRMED`.

Expanding `(Sx+Tz)^3+T*S^2*y^3+T^3*x^2*z` in `[S:T]` reproduces (1.1) exactly:

```text
S^3   : x^3
S^2T  : 3x^2z+y^3
ST^2  : 3xz^2
T^3   : z^3+x^2z = z(z^2+x^2)
```

The triangular implication is correct as stated (the third coefficient is not
needed). I strengthened it to a radical certificate rather than a chain of
words: a Groebner basis of the coefficient ideal in `C[x,y,z]` is
`[z^4, x^3, y^3-3z^3, x^2z+z^3, xz^2]`, so `x^3` and `z^4` lie in the ideal,
and `y^12 = (y^3)^4 == 81 z^12` lies in `(z^4)`. Hence the radical is
`(x,y,z)` and there is no common projective zero. `pi` is finite.

Miracle flatness is applied correctly, but with two hypotheses supplied by the
reader rather than stated:

- `X` is a nonzero effective divisor in the smooth 3-fold `P^2 x P^1`, hence
  locally cut by one nonzerodivisor, hence Cohen--Macaulay **and pure of
  dimension two**. Purity is what makes `dim O_{X,p} = 2` at *every* point,
  which the local criterion needs; the report says only "the hypersurface is
  Cohen--Macaulay".
- The fibre-dimension-zero hypothesis is carried by the word "finite", proved
  immediately above. That is legitimate but implicit.

With those, `O_{P^2}` regular of dimension 2, `O_X` CM, fibre dimension 0 give
flatness (Matsumura 23.1). Degree three: the leading coefficient `x^3` is not
identically zero, so the generic fibre is three points with multiplicity;
flatness then upgrades this to length three on every fibre. `pi_*O_X` is
locally free of rank 3.

## 2. Total-space singular locus, `D4`, integrality, normality

`CONFIRMED`. I found no reducible connected divisor and no hidden singular
curve; I re-derived the locus by elimination rather than by the report's
`r`-substitution, and the two answers agree.

Euler's relation holds (`x F_x + y F_y + z F_z = 3F`), so the singular locus is
`V(F_x,F_y,F_z,F_t)`. Working chart-by-chart in `P^2` to avoid the irrelevant
ideal, Groebner bases give:

```text
chart S=1 (t finite):  z=1 -> [ -3t^4+12t^2+24tx+12x^2+y^3, xy^3,
                                3t^4+8t^3x-y^3, y^5, ty^2, t^5 ]  -> {(0,0,0)}
                       y=1 -> [1]        x=1 -> [1]
chart T=1 (u=S/T):     y=1 -> [x^2+3z^2, xz, z^3, u]              -> {(0,0,0)}
                       z=1 -> [1]        x=1 -> [1]
```

So `Sing(X)` is exactly the two points `([0:0:1],t=0)` and `([0:1:0],u=0)`.
Zero-dimensional; no singular curve anywhere. The report's finite derivative
reduction is also correct in detail: with `y=0`, `z=1`, `x=t(r-1)`,

```text
F_x/t^2 = 3r^2+2t^2(r-1),   F_z/t^3 = 3r^2+t^2(r-1)^2,
difference = t^2(r-1)(r-3),  F_t/(3t^2) = r^2+t^2(r-1)^2,
```

`F_x/t^2 = 3` at `r=1`; at `r=3` vanishing forces `t^2=-27/4` where
`F_t/(3t^2) = 9-27 = -18 != 0`. The report leaves implicit that `F_t` must also
vanish for a *total-space* singularity; that is the operative step, and it is
correct. Note the `r=3, t^2=-27/4` locus is exactly the two cuspidal fibres of
section 2 -- fibre-singular, total-space-smooth. This is precisely the
flag/place separation FALLACY-v2 asks for, and the report gets it right.

**`D4`.** The report's justification ("three distinct tangent lines, so the
standard `D4` suspension") states the right criterion but omits the
determinacy step. I supplied it. The germ at `[0:1:0]` in the chart `y=1` is

```text
u^3x^3 + 3u^2x^2z + u^2 + 3uxz^2 + x^2z + z^3.
```

With weights `wt(u)=1/2, wt(x)=wt(z)=1/3` the weighted-degree census is

```text
wdeg 1  : u^2, x^2z, z^3        wdeg 3/2 : 3uxz^2
wdeg 2  : 3u^2x^2z              wdeg 5/2 : u^3x^3
```

The principal part `u^2+z^3+x^2z` is quasi-homogeneous of weighted degree one
with isolated singularity (Jacobian GB `[z^3, x^2+3z^2, xz, u]`, Milnor basis
`{1,x,z,z^2}`, `mu=4`), i.e. it *is* `D4`. Every remaining monomial has
weighted degree `> 1`, and the local-algebra basis has maximal weighted degree
`2/3 < 1`, so the germ is right-equivalent to its principal part exactly. `D4`
is a rational double point, hence normal and Gorenstein. Confirmed.

**Integrality.** The report's route (ample `(3,3)` divisor hence connected;
reducible or nonreduced would force a positive-dimensional singular locus) is
valid: `O(3,3)` is ample on `P^2 x P^1` and an effective ample divisor on a
projective variety of dimension `>= 2` is connected. I add two independent
confirmations that do not depend on that step: (i) `F` is irreducible as a
polynomial (`factor_list` returns a single factor of multiplicity one, in both
the bihomogeneous and the affine chart); (ii) every component of `X` dominates
`P^1` for dimension reasons, and the generic fibre of `pr_2` is a plane cubic
with `Delta = -27t^24(4t^2+27)^2 != 0`, hence smooth and irreducible.

**`S2 + R1`.** `S2` from the hypersurface/CM property; `R1` because the
singular locus is two points, codimension two on a surface. Serre gives
normality. Confirmed.

## 3. Shifted weighted face and what it imports

`CONFIRM_WITH_CORRECTIONS`. The arithmetic is exact; the citation label is
mis-typed by lifecycle.

Setting `z=1` and `X_1=x+t` gives exactly (1.4):

```text
X_1^3 + t y^3 + t^3 X_1^2 - 2 t^4 X_1 + t^5.
```

For weights `(5,4,3)` on `(X_1,y,t)` the full weight census is `{15, 17, 19}`;
there is **no** term of weight below 15, and the exact weight-15 face is
`X_1^3 + t y^3 + t^5`. This equals the weighted-boundary packet's

```text
P15 = X^3 + tY^3 + alpha t^2 X Y + eta t^5
```

at `alpha = 0, eta = 1`, so the report's numerals are right.

Two corrections:

1. **Lifecycle.** The `(alpha, eta)` normal form (1.1)--(1.3) exists only in
   `bd-a2-d3-halphen-weighted-boundary-obstruction-sol56-20260830.md`, whose
   lifecycle is `EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED`
   -- **not promoted**. What *is* promoted is the control family itself, at
   `bd-a2-d3-halphen-local-gates-coordinator-integration-sol56-20260830.md:158-176`
   (section 3, "Sharp positive control"), whose critical flag is written
   `kappa=0, eta!=0`, and where `alpha` never appears. The phrase "the already
   promoted sharp critical local control `alpha=0,eta=1`" fuses a promoted
   object with an unreviewed coordinate system. Retype as: *the promoted
   control family, whose weight-15 face is `(alpha,eta)=(0,1)` in the
   provisional weighted-boundary normal form*.
2. The coefficient symbols underlying `alpha` and `eta` (`M111`, `Q021`, `A2`,
   `V3`, ...) are defined in **neither** charged file. The numerals `0` and `1`
   are therefore verifiable only through the face identity above, which is what
   I checked; I could not audit `alpha = M111-2s*ell-2*lambda*q0` symbolically.

On the reviewer's standing warning: the report does **not** infer global row
occurrence from this germ. Sections 0, 1, 2 and 5 all disclaim it explicitly
("does not turn global closure into a polynomial map or prove the row's global
occurrence theorem"). That is correct and load-bearing.

The specialisation is also self-consistent downstream: at `(alpha,eta)=(0,1)`,
`delta=alpha^3+27eta=27 != 0`, and the Hesse cubic is the Fermat cubic
`u^3+v^3+w^3` -- smooth (Jacobian GB `[u^2,v^2,w^2]`), genus one.

## 4. `c4, c6, Delta` in both charts and the checksum

`CONFIRMED`, re-derived by a route independent of the report's Hessian pencil.

The unimodular substitution `x = w - tz` (determinant one) turns the fibre into

```text
w^3 + t y^3 + t^3 w^2 z - 2 t^4 w z^2 + t^5 z^3,
```

i.e. `t*y^3 + A(w,z)` with `A` a binary cubic and `y` occurring *only* cubed.
Every fibre is therefore a `mu_3`-cyclic cover of `P^1` totally ramified at the
three roots of `A`, so every fibre carries an order-three automorphism with
fixed points: **`j == 0` structurally**, which is the real reason `c4 == 0`. No
invariant-convention argument is needed for that clause.

Binary discriminants:

```text
disc(A)     = -t^10 (4t^2+27)          disc(A_inf) = -(27u^2+4)
A_inf(w,x)  = w^3 + w x^2 - u x^3      (from z = w - ux on the T=1 chart)
```

Using `c6 = -216 * lambda^2 * disc(binary part)` -- the convention pinned by
the promoted gate identity `[t^4]c6 = -216 Disc_binary(G)` at
`...local-gates-coordinator-integration...md:51` -- with `lambda = t` and
`lambda = u^2` respectively:

```text
c6      = 216 t^12 (4t^2+27)        c6_inf      = 216 u^4 (27u^2+4)
Delta   = -27 t^24 (4t^2+27)^2      Delta_inf   = -27 u^8 (27u^2+4)^2
```

exactly (2.1) and (2.2). The two charts are consistently normalised: since
`infinity_form = affine / t^3`, the weight-6 scaling predicts
`c6_inf = t^-18 c6 = 216 u^4(27u^2+4)`, which is what both computations give.
`Delta = (c4^3-c6^2)/1728` is *not* an independent check once `c4=0`.

Minimal-valuation ledger, recomputed:

```text
t=0            ord(c6)=12, ord(Delta)=24 -> twist k=2 -> (0,0)   [the "level two"]
4t^2+27=0 (x2) ord(c6)=1,  ord(Delta)=2  -> k=0       -> (1,2)
t=infinity     ord(c6)=4,  ord(Delta)=8  -> k=0       -> (4,8)
checksum: 0 + 2*2 + 8 = 12
```

The two roots of `27u^2+4` in the infinity chart are the *same* two places as
`4t^2+27`; there is no double count.

**What follows.** The Jacobian of the generic fibre over `C(t)` is isotrivial
with `j = 0`; its minimal Weierstrass model over `P^1` has
`deg Delta_min = 12`, hence `chi = 1`, hence the *Jacobian* elliptic surface is
a rational elliptic surface, with Kodaira types `II + II + IV*` (Euler numbers
`2+2+8=12`, consistent) and good reduction at `t=0`. The `IV*` is independently
corroborated: the fibre over `u=0` is the three concurrent lines `z(z^2+x^2)`
(type `IV`, three components) meeting at the `D4` point, and a `D4` resolution
contributes four more curves -- `3+4 = 7 = ` the `E~6` count.

**What does not follow.** Nothing about `X`'s own relative minimal model,
Kodaira dimension, rationality, GR trace or multiplicity index. Concretely,
`pr_2: X -> P^1` has the *non-reduced* fibre `3*{x=0}` over `t=0`, so it admits
no section at all and is not the Jacobian fibration; the checksum is a
statement about the Jacobian, not about `X`. The report's hedge ("compatibility
data, not a standalone proof of the surface's relative minimal model,
multiplicity index or GR trace") is exactly right, and I did not find any place
where it is quietly exceeded.

## 5. Ramification elimination, rationality, Kummer function, Riemann--Hurwitz

`CONFIRMED`, and strengthened at the three points the reviewer flagged
(sublocus, multiple cover, valuation at infinity).

In the target chart `z=1`, `F = (1+x^2)t^3 + 3xt^2 + (3x^2+y^3)t + x^3`, and

```text
F - t F_t = -2t^3x^2 - 2t^3 - 3t^2x + x^3 = (x+t)^2(x-2t) - 2t^3x^2,
```

exactly (3.1). Three facts the report asserts and the replay does not check:

1. **The elimination is exact, not merely a containment.** A lex Groebner
   basis of `(F, F_t)` in `C[y,x,t]` has `y`-free part generated by precisely
   this quintic. So `(F,F_t) cap C[x,t] = (B)`; the ramification curve
   dominates all of `B`.
2. **`B` is irreducible** (`factor_list` returns one factor, multiplicity one).
   Equivalently, in `x = t(r-1)` coordinates `B` becomes
   `t^3 (r^2(r-3) - 2t^2(r-1)^2)`, and `r^2(r-3)/(2(r-1)^2)` is not a square in
   `C(r)` because `(r-3)` has odd multiplicity.
3. **The parametrization is birational, degree one -- not a multiple cover and
   not a proper sublocus.** `q = x t/(x+t)` is an exact rational inverse of
   `r = 2q^2+3, x = rq, t = rq/(r-1)`, and on `B` the locus `x+t=0` reduces to
   `-2t^5 = 0`, i.e. the single point `(0,0)`. So the inverse is defined on a
   dense open of `B`.

Kummer function, derived (not assumed) from `F_t = 0`:

```text
y^3 = -3((x+t)^2 + x^2t^2)  --param-->  -3 q^2 (2q^2+3)^4 / (4(q^2+1)),
```

exactly (0.2). I additionally checked the lift against `F` itself, not only
`F_t`: `F(x(q), t(q))` with `y^3` substituted vanishes identically. Complete
divisor of the Kummer function on `P^1_q`, including infinity:

```text
q=0              ord  2   (2 mod 3)      1 place
2q^2+3 = 0       ord  4   (1 mod 3)      2 places
q^2+1 = 0        ord -1   (2 mod 3)      2 places
q=infinity       ord -8   (1 mod 3)      1 place
                 degree of divisor = 2+8-2-8 = 0   (consistency)
```

Supports pairwise disjoint (distinct irreducible factors, and `infinity`
separate). No valuation is `0 mod 3`, so the function is not a cube in `C(q)`
and the cyclic cubic cover is connected; all six places are totally ramified.
Tame Riemann--Hurwitz in characteristic zero:

```text
2g-2 = 3(-2) + 6*(3-1) = 6,   g = 4,
```

cross-checked against the closed form `g = (n-1)(r-2)/2 = 2*4/2 = 4`.

**Genuine component.** `disc_t(F)` factors as `-z * (irreducible degree-11
form)`; I verified both the factorization and the irreducibility. So the branch
divisor in `P^2` is the line `z=0` plus one irreducible degree-11 curve, and
the ramification divisor in `X` has exactly two components: the rational curve
`{z=0} x {S=0}` (which does lie in `X`, and carries the `D4` point) and the
genus-four `R` above. `R` is a full component, not a sublocus. Nothing escapes
to `t=infinity` over the chart `z=1`: a double root at `[S:T]=[0:1]` would need
`1+x^2 = 0` and `3x = 0` simultaneously.

Finally, the marked singular point is `q=0` on this component (`x=t=y=0`),
which is consistent with the promoted block theorem's `Sing(Y) subset R`.

## 6. Proper-block consequence under the corrected morphic forest theorem

`CONFIRM_WITH_CORRECTIONS`. The conclusion holds; the report's three-sentence
argument omits three steps the reviewer asked about, all of which I checked and
all of which go the report's way.

Inputs used, and only these: the promoted block-structure theorem
(`block-descent-structure-coordinator-integration-sol56-20260830.md:63-71`),
giving `g1(A^2) subset Y_sm minus R` and `Sing(Y) subset R`; and the corrected
morphic theorem (`bd-a2-rational-forest-morphic-correction-sol56-20260830.md`
sections 2--3), applied to `V = g1(A^2)` directly. The report explicitly
disclaims abstract rational domination ("No assertion based only on abstract
rational domination is used"), which is the exact hypothesis the correction
packet retracted. That is respected.

The three supplied steps:

1. **One completion suffices, and no contraction can occur.** The theorem
   quantifies over *every* strict-SNC completion, so it is enough to exhibit
   one containing the curve. Take a resolution `rho: W -> X` that is an
   isomorphism over the smooth `V`, then blow up further until `D := W minus
   rho^{-1}(V)` is SNC. Because `rho` is a birational *morphism*, the strict
   transform of `R-bar` is a curve, never a point; contraction cannot erase the
   genus. The report says "on a common SNC completion ... is therefore
   boundary" without noting that the direction of the birational map is what
   forbids contraction.
2. **Normalization.** SNC forces components smooth, so the boundary component
   is the *normalization* of `R-bar`, of genus exactly 4 -- the report's
   "strict transform" is loose but harmless, since either reading gives
   `tau(D) >= 4 > 0` against `tau(D) = 0`.
3. **Target infinity / chart independence.** The report fixes `z=1` without
   comment. The conclusion is chart-independent: `pi(R-bar)` is the
   *irreducible degree-11* branch curve, not a line, so `R-bar` meets
   `pi^{-1}(P^2 minus L)` for every line `L`, and the genus-four component
   survives in `Y` for any affine target chart. Worth stating, since the
   companion weighted-boundary packet handles the analogous case explicitly
   and this one does not.

Disjointness `R-bar cap V = empty` is exact: `R-bar cap Y = R` (closed in `Y`),
`R cap V = empty` by the block theorem, and `R-bar minus R` lies over `z=0`,
outside `Y`. `V` is smooth quasi-projective and `g1: A^2 -> V` is a surjective
everywhere-defined morphism, so the theorem's hypotheses are met verbatim.

**Correction on antecedent strength (this is the substantive one).** The report
requires the *global* identification "`(0.1)` restricted over an affine target
plane **is** the second leg", i.e. `Y ~= pi^{-1}(A^2)` and `g2 ~= pi` globally.
The companion weighted-boundary route needs only the *local* algebra
identification at the marked point (its section 4). A global identification is
a far stronger and far less likely antecedent, so the exclusion proved here is
correspondingly narrower. The report's section 5 wording ("this specific global
control cannot occur as an actual proper intermediate block") is accurate;
section 0's shorthand "the control ... cannot be an actual proper block"
conflates a surface with a sandwich and should be aligned to section 5.

## 7. Replay reproduction, guards, and what is not executable

`CONFIRM_WITH_CORRECTIONS`. Reproduction is exact; one section-4 sentence
overstates what the script derives.

Reproduced under `uv run --with sympy==1.14.0`:

```text
ordinary / -O / -OO :  1148 bytes, identical
SHA-256             :  ee77940abb31d00eb90880a75f5cbec708e0b7f445757fa96ddde62963650c20
```

matching the report exactly (its "1,148-byte" count includes the trailing
newline emitted by `print`; a shell `$( )` capture strips it and shows 1147).
Source hash `be9551b7...b65485` re-verified. AST census: `Assert` nodes `0`,
`Raise` nodes `2`, `require` calls `31`; guards are `RuntimeError`, so they
survive `-O`/`-OO` -- the claim is sound, not merely nominal. Mutation
`--mutate-kummer-denominator` exits `1` with exactly
`FAIL:ramification Kummer function drifted`; an unknown argument also exits `1`.

Two notes on guard quality:

- The mutation is intercepted at line 240 by a comparison of one hardcoded
  literal against another, before reaching the genuine derivation guard. I
  checked separately that the derivation guard *would* also catch it: with
  `q^2+2`, `F_t` on the parametrized curve evaluates to
  `3q^2(2q^2+3)^4 / (4(q^2+1)(q^2+2)) != 0`. So the receipt is sound, but the
  displayed failure demonstrates literal drift, not derivation sensitivity.
- The `require` at line 224 checks only that the parametrization *lands on*
  `B`. It does not check dominance, degree one, or the stated inverse
  `q = xt/(x+t)`. That is exactly the "parametrized sublocus or multiple cover"
  hole; I closed it by hand in section 5, but the script does not.

**Not executable / report-layer.** Beyond the four the report already lists
(miracle flatness, `S2+R1`, the `D4` tangent-cone criterion,
Riemann--Hurwitz), the following are also *not* software outputs:

```text
- the entire (1.4) shift and the (5,4,3) weight-15 face: absent from the script
- integrality (ampleness => connected; components meet in Sing)
- irreducibility of B; exactness of the elimination ideal; birationality of (3.2)
- connectedness of the Kummer cover (no valuation 0 mod 3)
- the branch ledger itself: branch_valuations_mod_3 is a hardcoded dict and
  branch_points = 1+2+2+1 a hardcoded sum; ord at q=infinity is never computed.
  Only the three pairwise gcds are derived.
- minimal_fibre_valuations and minimal_discriminant_degree = 12: hardcoded
- proper_block_rational_forest_compatible = False: a hardcoded assertion
- the whole section 3 block interface
```

Correction: section 4's "The replay derives ... the Kummer branch ledger" is
false as written. It derives the Kummer *function* and the disjointness of the
three finite supports; the ledger, the valuation at infinity, the genus input
and the discriminant-degree checksum are asserted literals. Replace "derives"
with "derives the Kummer function and support-disjointness; the branch ledger
and minimal-valuation checksum are declared".

## 8. Price

`CONFIRM_WITH_CORRECTIONS`. The report's own pricing is close to right; one
lifecycle tag is missing and one antecedent distinction is unstated.

```text
Global surface control            EARNED, unconditional, exact.
                                  X is integral normal (3,3), pi finite flat
                                  of degree 3, Sing(X) = two named points.
                                  The promoted local D3 Halphen germ is
                                  realised by an actual projective surface,
                                  not merely by a formal jet. Nothing about
                                  occurrence in the four-row theorem.

Proper-block exclusion, this one  EARNED but CONDITIONAL on the *global*
control                           identification Y ~= pi^{-1}(A^2), g2 ~= pi,
                                  plus two imported theorems. It is one
                                  negative control, not a family statement.

Universal D3 row obstruction      NOT EARNED HERE, and the packet that claims
                                  it is PROVISIONAL / review-gated. Section 0's
                                  "the universal weighted exceptional-curve
                                  obstruction remains the stronger family-wide
                                  theorem" must carry that tag.

A map                             NOTHING. No Keller map, no polynomial map,
                                  no etale first leg, no primitivity. The
                                  report says so and I found no leak.

JC2                               NOTHING.
```

Shared-risk note the report does not make: both this obstruction and the
universal weighted-boundary obstruction rest on *the same two* imported
theorems -- the corrected morphic rational-forest theorem and the block
structure theorem. The two routes are independent in their geometry (a global
genus-four ramification curve versus a local genus-one exceptional curve) but
**not** independent in their premises. A single defect in the forest theorem
kills both.

## 9. Maximum-safe theorem

Everything below is unconditional except clause (vi), whose antecedent is
stated in full.

> Let `X subset P^2_[x:y:z] x P^1_[S:T]` be `(Sx+Tz)^3 + T S^2 y^3 + T^3 x^2 z
> = 0`. Then:
>
> (i) `X` is an integral normal surface of class `(3,3)`;
> (ii) `pr_1: X -> P^2` is finite, flat and surjective of degree three;
> (iii) `Sing(X)` consists of exactly two points: `([0:0:1], T=0)`, whose germ
>       is the promoted CFS level-two critical control with exact `(5,4,3)`
>       weight-15 face `X_1^3 + t y^3 + t^5` (no term of lower weight; next
>       weights 17 and 19), and `([0:1:0], S=0)`, an analytic `D4` rational
>       double point;
> (iv) every fibre of `pr_2` is a `mu_3`-cover of `P^1`, so `c4 == 0`; in the
>      normalization pinned by `[t^4]c6 = -216 Disc_binary(G)`,
>      `c6 = 216 t^12 (4t^2+27)` and `c6 = 216 u^4 (27u^2+4)` in the two
>      coefficient-base charts, with `Delta = -c6^2/1728`, minimal valuation
>      ledger `(0,0), (1,2), (4,8)` and minimal discriminant degree 12; the
>      *Jacobian* fibration is a rational elliptic surface with types
>      `II + II + IV*`. `pr_2` itself has the non-reduced fibre `3*{x=0}` over
>      `T=0` and hence no section; no conclusion about `X`'s own relative
>      minimal model, rationality or GR trace is available;
> (v) the branch divisor of `pr_1` is `{z=0}` union one irreducible degree-11
>     curve; the ramification divisor has exactly two components, a rational
>     one over `{z=0}` and an irreducible `R-bar` whose normalization is the
>     connected cyclic cubic cover `y^3 = -3q^2(2q^2+3)^4/(4(q^2+1))` of
>     `P^1_q`, totally ramified at exactly six places (`q=0`; `2q^2+3=0`;
>     `q^2+1=0`; `q=infinity`), of genus four;
> (vi) if `pi^{-1}(A^2)` for some affine chart `A^2 subset P^2` were the second
>      leg `g2` of an actual proper block `A^2 -> Y -> A^2`, then `R-bar` would
>      be disjoint from `V = g1(A^2)` and, on a resolution of `X` that is an
>      isomorphism over `V` with SNC boundary, would contribute a genus-four
>      boundary component, giving `tau >= 4` against `tau = 0` from the
>      corrected morphic rational-forest theorem. Hence this control is not the
>      middle surface of an actual proper block.

No claim of row occurrence, global attainment, map construction or JC2.

## 10. Cheapest useful successor

**Hostile-review the single shared premise: section 2 of the morphic
rational-forest correction packet.** Specifically the chain

```text
bar-P_1(U) = p_g(X) + tau(D) - rank(partial),   rank(partial) <= q(X),
tau(D)     = sum_i g(D_i) + b_1(Gamma_D),
```

on a *reduced strict-SNC* boundary, including: whether `b_1` of the **dual
multigraph** (multi-edges, two components meeting twice) is counted correctly;
whether `rank(partial) <= q(X)` is the right bound in the direction used;
and whether logarithmic pullback along the generically finite `F` really
injects when `B` is only made SNC after boundary blowups.

Why this and not more geometry: it is desk work with no CAS, it costs one
reviewer, and it is the *only* premise both live D3 exclusions share. The same
packet has already retracted one false strengthening of exactly this theorem
(the rational-map extension, killed by `U = P^2 minus E`), so the residual
error rate there is demonstrably nonzero, and a defect would simultaneously
void this global control's section 3 and the universal weighted-boundary
obstruction's section 4.

Second choice, if a producer lane is free instead: re-state clause (vi) under
the *local* incidence antecedent used by the weighted-boundary packet rather
than the global identification, and determine whether the genus-four curve is
still reachable. If it is not -- and I expect it is not, since genus is not a
germ invariant -- that fact should be recorded, because it is the precise
reason this route cannot be promoted to a family-wide theorem.

## 11. Verdict summary

```text
1  binary-cubic coefficients / finite / degree 3 / miracle flatness  CONFIRMED
2  singular locus, D4, integrality, S2+R1, normality                 CONFIRMED
3  shifted weighted face and its import          CONFIRM_WITH_CORRECTIONS
4  c4, c6, Delta, minimal-valuation checksum                         CONFIRMED
5  ramification elimination, rationality, Kummer, Riemann--Hurwitz   CONFIRMED
6  proper-block consequence via morphic forest   CONFIRM_WITH_CORRECTIONS
7  replay reproduction, guards, executability    CONFIRM_WITH_CORRECTIONS
8  pricing                                       CONFIRM_WITH_CORRECTIONS
```

No item is `REFUTED` and no item is `GAP`. I sought a counterexample at each of
the four places the packet is most exposed -- a hidden singular curve, a
reducible or nonreduced `(3,3)` divisor, a parametrized sublocus or multiple
cover masquerading as a ramification component, and a contraction that erases
the genus -- and each attempt failed against an exact certificate. The
corrections above are scope, lifecycle and executability repairs; none of them
touches the mathematics of the two headline conclusions.

This review makes no exit-price assertion. No `charge_basis` line is emitted;
receipt status `ABSENT` is expected.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28018`.
- Body SHA-256:
  `c8d62de1a530d46e90415d9695814f8c4a00a23ba9c99a0152e54924219f8fa2`.
- Frozen basis: `44ac698b0c2061b986e46895cb64ea5c5b441e0c`.
