# Outer Theorem-1.2 bands and the T₂, T₃ bridge for the (99,66) joint chart

Lane `g9966-outer-bridge-grok46-20260903`.  Add-on to the charged chart driver
under `box/g9966-20260903/` (not modified).  New drivers live in
`box/g9966outer-20260903/`.  No ledger, `jc2-lean`, `ideation-*`, or named
in-progress lane report was read or edited.

## Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g9966-outer-bridge-grok46-20260903.run.v2`, checked with
`sha256sum -c`.  All **21/21** frozen inputs `OK`.  No digest was retyped.
Manifest: `box/g9966outer-20260903/inputs.sha256`.

The missing necessary content named by the design-gate (AUDIT delta 17(aaaa))
splits cleanly.

**(a) Outer Theorem-1.2 D₁/D₂ bands on A, B.**  These are explicit linear
vanishing rows in the invertible `t^r(w-1)^q` chart of `K_Q=t^D Q(t^{-1},w/t)`.
Theorem 1.2 is `≥`, so the equality face is **not** a row.  Exact `Q*` / `Q`-Gaussian
counts, both minor branches (the rows sit at the *first* point):

| band | A2 | A3 | B1 | B2 | total |
|---|---:|---:|---:|---:|---:|
| ambient `S(D,33)` | 1650 | 2739 | 561 | 1650 | **6600** |
| D₂ unit vanishings `3r+4q < 3(D+bound_t)` | 1386 | 2442 | 384 | 1386 | **5598** |
| D₂ remaining | 264 | 297 | 177 | 264 | **1002** |
| D₁ raw `(e,Π)` slots | 51 | 108 | 15 | 51 | **225** |
| D₁ `Q*` rank | 44 | 73 | 15 | 44 | **176** |
| D₁ dependent slots (homogeneous, not an obstruction) | 7 | 35 | 0 | 7 | 49 |

New independent outer pivots: **5774** (`5598+176`).  All **15** first-global-band
outer pivots lie among the D₂ unit rows, so they are not subtracted twice.  Union
with the charged prefix:

```text
delta=2:     6689  →  1106 after D₂  →  930 after D₁
delta=5/2, b0=0: 6687  →  1104 after D₂  →  928 after D₁
```

These are `COUNTING-BOUND` dimensions of a still-incomplete relaxation.

**(b) Effective T₂, T₃ ∈ K[f,g] bridge.**  The *shape* is PRINTED (Moh p.152,
Xu §7.3 p.10):

```text
T2 = G^3 - F^2 + c0 G^2 + (a1 F + a0) G + (b1 F + b0)     (5 unknown; 4 after Tschirnhausen)
T3 = G^9 - F^6 + sum_{i=1}^{9} alpha_i(F) G^{9-i}          (35 unknown; 34 after Tschirnhausen)
     deg alpha_i <= floor(2i/3),  leading [F^6] of alpha_9 = -1.
deg_y T2 = -mu_2 = 55,   deg_y T3 = -mu_3 = 145.
```

Chart convention: `F` = Moh `g` (deg 99), `G` = Moh `f` (deg 66), so
`T0=F`, `T1=G`, and `T_r^ψ` is a polynomial in `(G,F)`.  The rows that would
identify `T2(σ)∼p^5` and `T3(σ)∼R` / `p^{10}q_1` with the minor leaders are
**not** among those linear forms: after the monic `G^3-F^2` (resp. `G^9-F^6`)
cancellation, the Tschirnhausen span evaluated on the leading pair
`(F,G)∼(p^9,p^6)` is `span{p^{18},p^{15},p^{12},p^9,p^6,p^0}` and does not
contain `p^5`, nor a degree-40 polynomial of shape `(25,14)` or `p^{10}q_1`.
Those leaders are residuals of *subleading* `F,G` jets.  Typed

```text
OPEN[EFFECTIVE-T2-T3-BRIDGE]
```

as complete linear rows on the 7161-chart.  For the `(64,48)→(16,12)` control,
`u_s=1` and the bridge is **trivial** (one Puiseux branch; Xu Prop. 7.3 / Moh
Prop. 4.4).  Both p.208 `c_5` readings, wrapper `T·κ-1`, Groebner over
`GF(32003)` grevlex, are `[1]`.  The automorphism `(ax+y,(a-1)x+y)` survives;
its `s=3` tower, outer bands, and `T2,T3` are `NOT-APPLICABLE[degrees (1,1)]`.

`(99,66)` remains `OPEN`.  Nothing here is a Keller witness.  No new
exit-price assertion.

## 0. Pages opened

Printed Moh page `p` is PDF page `p-139`.  Xu printed page `p` is PDF page `p`.
Images under `box/g9966outer-20260903/pages/`; OCR extracts under
`box/g9966outer-20260903/text/`.

```text
moh_p149_pdf10.png   p.149  Theorem 1.2 (quasi-approximate roots; ord h_j(σ_i) ≥ (λ/d) j)
moh_p150_pdf11.png   p.150  characteristic data {M_j,d_j}; n_j, q_j, λ_j, μ_j
moh_p151_pdf12.png   p.151  Lemma 2.1; defining equation F(f,g); ψ: x ↦ 0
moh_p152_pdf13.png   p.152  T_r^ψ = truncation of F^{1/d_r}; Prop. 2.2  deg_y T_r^ψ = -μ_r
moh_p164_pdf25.png   p.164  Prop. 4.1, D(a,b,p,q); start of the D1/D2 detector sequence
moh_p167_pdf28.png   p.167  Prop. 4.4 setup (nonsplitting at a disc; leading forms powers of a linear)
xu_p10_s73.png       p.10   §7.3: T_i(f,g) ∈ K[f,g], T0=g, T1=f, deg T_i = -μ_i; Prop. 7.3
xu_p13_s8.png        p.13   §8 (99,66) data; -μ2=55, -μ3=145; leaders at δ=2 and 5/2
```

## 1. Custody and label reversal

The 21 frozen inputs were checked as in the verdict.  Work is over
characteristic zero; exact rank is over `Q`.  The `(16,12)` saturation is over
`GF(32003)`, declared below.

`SOURCE-READ`, Moh p.149: `deg_y f=m`, `deg_y g=n`.  `SOURCE-READ`, Xu p.10
and p.13: `n=99`, `m=66`, `T0=g`, `T1=f`, principal-minor multiplicity of `f`
is `m u_s/d_s=18`.  The charged chart puts the *minor* line at `y=0` and the
*major* line at `y=x`, with

```text
chart F = Moh/Xu g,  deg 99,  minor 27,  major 72
chart G = Moh/Xu f,  deg 66,  minor 18,  major 48
```

so `(F,G)=(g_Moh, f_Moh)` and `J(F,G)=1` is `-J(f,g)` in Moh's ordered pair.
`FALLACY-v2 / flag-place-series`: the D₁/D₂ bands of this lane are at the
*first* (major) point, residue `y=x`; `u_s=3` is the complementary factor at
the *second* point.  They are not identified.

## 2. Theorem 1.2 as coefficient rows at D₁ and D₂

`SOURCE-READ`, Moh p.149 Theorem 1.2: if `f=(h)^d + ∑_{j=1}^d h_j (h)^{d-j}`
with `deg h_j < deg h = (deg f)/d` and `h` a `d`-th quasi-approximate root of
accuracy `λ`, then `ord h_j(σ_i) ≥ (λ/d) j`.  Along the major tower
`ord h = λ/d`, which is the design's `ord Q_j ≥ j·ord h`.

Chart (2.1), first point (design §2.1, now imposed):

```text
ord h2(D2) = -1,     ord h2(D1) = -1/9
F = h2^3 + A2 h2 + A3     ⇒   ord A2 ≥ 2 ord h2,   ord A3 ≥ 3 ord h2
G = h2^2 + B1 h2 + B2     ⇒   ord B1 ≥ 1 ord h2,   ord B2 ≥ 2 ord h2
```

Explicitly: at D₂, `ord A2≥-2`, `ord A3≥-3`, `ord B1≥-1`, `ord B2≥-2`; at D₁,
`ord A2≥-2/9`, `ord A3≥-1/3`, `ord B1≥-1/9`, `ord B2≥-2/9`.  The Tschirnhausen
`h2^2` term in `F` is already zero in (2.1).

Homogenize `Q∈S(D,33)` by `K_Q=t^D Q(t^{-1},w/t)` in the basis `t^r(w-1)^q`,
support `r≥0`, `0≤q<33`, `r+q≤D` (dimension `33(D+1)-33·32/2`, matching the
charged 1650 / 2739 / 561 / 1650).

**D₂.**  `t=s^3`, `w=1+π s^4`, so `t^r(w-1)^q` has exact weight `3r+4q`.
`A2=t^{-65}K_{A2}` has `ord_t = min(3r+4q)/3 - 65`; the bound `≥-2` is
`3r+4q ≥ 189`.  Strict vanishing (`Theorem 1.2` is `≥`; the equality face is
allowed) is the **unit** row `c_{r,q}=0` on every slot with `3r+4q<189`.  The
four thresholds `3(D+bound_t)` are `189,285,93,189`.  Counts in the verdict
table; every such row is a coordinate vanishing, rank equals the count,
residual `0`.

**D₁.**  Recentre `t=e^9`, `w=1+e^{12}+Π e^{13}` as in the charged `h2`
probe.  A remaining term contributes
`c_{r,q} e^{9r+12q}(1+Π e)^q`.  The bound `ord_t Q ≥ bound_t` is
`ord_e K_Q ≥ 9(D+bound_t)`, i.e. thresholds `583,879,287,583`.  After D₂,
`min 9r+12q = 3·(D2 threshold)`, so the D₁ gap is a finite window
(`e∈[567,582]` for A2/B2, `[855,878]` for A3, `[279,286]` for B1).  Exact
`Q`-Gaussian on the binomial matrix (rows `(e,j)`, columns remaining `(r,q)`)
has rank **176** of **225** raw slots.  Leftover rows reduce to `0`
(homogeneous: slot-dependencies, not a cokernel obstruction).  The same engine
replays the charged `h2` D₁ band: 7 slots, rank 7, `e`-powers
`291:1,292:1,293:1,294:2,295:2`, matching `major_h2-results.json`.

**Which `(x,y)` monomials vanish.**  The unit rows are in the `(r,q)` basis,
triangular in `x^i y^j` via `w=y/x`, `t=x^{-1}`, `r=D-i-j`.  The lowest slot
`(0,0)` is exactly `A3_{98,0}`, `A2_{65,0}`, `B2_{65,0}`, `B1_{32,0}`.  All
`r=0` slots of A2/A3/B2 lie strictly below the D₂ threshold (A2 face
`4q≤128<189`), so the entire degree-`D` face of A2, A3, B2 vanishes at D₂.
B1 is the exception: `r=0,q≥24` remains (`4·24=96≥93`).  Remaining A2/B2
support has `r≥21`; remaining A3 has `r≥53`.

**Prefix overlap.**  The 15 charged first-global-band outer pivots
(`A3_{98,0}…A3_{89,9}`, `A2_{65,0}`, `B2_{65,0}…B2_{63,0}`) all have
`3r+4q` below the D₂ threshold.  After those unit substitutions the ten
degree-162 Jacobian prefix rows become `0=0`.  They add no rank beyond D₂.

**h₃-adic D₂ on `F_j`, `G_j`.**  Expanding (2.1) in `h3`,

```text
F_1 = 0,     F_2 = 3 C2,     F_3 = 3 C3,     F_6 = 3 C3^2 + C2^3 + A2,
F_9 = C3^3 + A2 C3 + A3
G_1 = 0,     G_2 = 2 C2,     G_3 = 2 C3 + B1,  G_6 = C3^2 + B1 C3 + B2
```

(and the remaining `F_4,F_5,F_7,F_8,G_4,G_5` likewise).  Canonical `F_1=0`
is an identity of the chart, as is `G_1=0`.  Theorem 1.2 at D₂, base `h3`
(`ord h3=-1/3`), asks `ord F_j≥-j/3` and `ord G_j≥-j/3`.  The inner bounds
`ord C2≥-2/3`, `ord C3≥-1` are already in the charged 516-row tower; the
outer D₂-`h2` bounds of this lane give the rest by addition of lower bounds.
`FALLACY-v2 / floor-attainment`: products of `≥` remain `≥`; no equality is
claimed, and no extra ambient coordinates are introduced.
`DERIVED`, **0** new outer pivots.

Both minor branches receive the **same** outer D₂/D₁ rows: they constrain the
first point.

## 3. T₂, T₃ as elements of K[f,g]

`SOURCE-READ`, Moh p.150.  With `M_1=-m=-66`, `M_2=77`, `M_3=97`,

```text
d = (99, 33, 11, 1)
q = (-66, 143, 20)
λ = (-6534, -1815, -1595)
μ = λ/d = (-66, -55, -145)
```

so `-μ_1=66=deg T_1`, `-μ_2=55`, `-μ_3=145`, matching Xu p.13.  `n/d_r` as
the degree in the symbol `f` is `(1,3,9)` for `T_1,T_2,T_3`.

`SOURCE-READ`, Moh p.152: `T_r^ψ` is the `d_r`-th approximate root of
`F^ψ(f,g)` (the `x↦0` specialisation of the defining equation of `f` over
`k[x]((g^{-1}))`):

```text
T_r^ψ(f,g) = f^{n/d_r} + ∑_{i=1}^{n/d_r} α_i(0,g) f^{n/d_r-i} ∈ k[f,g],
deg_y T_r^ψ(f(x,y),g(x,y)) = -μ_r     (Prop. 2.2, M_r ≤ e).
```

`SOURCE-READ`, Xu §7.3 p.10: `T_i(f,g)∈K[f,g]`, `T_0=g`, `T_1=f`,
`deg T_i=-μ_i`.  In chart names this is `T_0=F`, `T_1=G`, `T_r^ψ∈K[G,F]`.

Weighted degree in `k[g]`: `deg_g α_i ≤ ⌊m i/n⌋ = ⌊2i/3⌋`, because the
`i`-th correction in `F^{1/d_r}` has `y`-weight `m i`.  Leading cancellation
against `f^{n/d_r}` forces `[g^{m n/(n d_r)}]α_{n/d_r}=[g^{m/d_r}]α_{n/d_r}=-1`
when both are monic in `y`.  Thus

```text
T2 ≡ G^3 - F^2 + lower,     n/d2=3, m/d2=2,   target deg_y = 55 (naive 198)
T3 ≡ G^9 - F^6 + lower,     n/d3=9, m/d3=6,   target deg_y = 145 (naive 594)
```

Unknown constant coefficients after the monic leading: **5** for `T2`
(`α_1` deg `≤0`: 1; `α_2` deg `≤1`: 2; `α_3` deg `≤2`: 3; minus the
`[F^2]=-1`), or **4** if the approximate-root Tschirnhausen `α_1=0` is
imposed.  For `T3`, `∑_{i=1}^9(⌊2i/3⌋+1)=36` including leading, hence
**35** unknown, or **34** after `α_1=0`.  Moh p.152's truncation does *not*
force `α_1=0`; the two counts are recorded separately.  Principal-minor
multiplicity of `T3` is Xu's `((−μ_s−2)u_s/d_s)+1=40`.

**Face obstruction, both branches.**  At a principal-minor `π`-root, Xu §8
gives `F(σ)=p^9 t^{9(-8+3δ)}+⋯`, `G(σ)=p^6 t^{6(-8+3δ)}+⋯`, `T2(σ)=p^5 t^{5(-8+3δ)}+⋯`,
and `T3(σ)=q t^{⋯}` with `deg q=40`.  Substituting the leading pair into the
Tschirnhausen shape, `G^3-F^2` and `G^9-F^6` cancel, and the remaining span
in powers of `p` is `{p^{18},p^{15},p^{12},p^9,p^6,p^0}` (resp. multiples of
6 down from 54).  It does not contain `p^5`.  It does not contain a degree-40
polynomial of N8 shape `z^{25}(z+3ρ)^{14}(z-2ρ)` or of N9 shape `p^{10}q_1`.
Those identifications require subleading `F,G` jets (the residual of
`G^3-F^2` after the D₂/pole vanishings drop the naive degree 198).  That
residual is nonlinear in the 7161 coordinates and is not a linear add-on of
this prefix.  Linear bridge rows emitted on the chart: **0**.  Status
`OPEN[EFFECTIVE-T2-T3-BRIDGE]` for both `δ=2` and `δ=5/2`.

**`u_s=1` is trivial.**  `SOURCE-READ`, Moh p.207: the `(64,48)` parent (and
the reduced `(16,12)` of p.208) has `u_s=d_s-v_s=1`.  Xu Prop. 7.3 / Moh
Prop. 4.4 then force every `T_{i,σ}` to be a power of one linear polynomial.
There is no split leader `R` or `q_1` to identify, and no free `T3` ODE.  The
bridge adds no variables and no rows.

## 4. Union with the charged prefix; new dimensions

Charged first-global-band prefix: dimension `6689` (`δ=2`) and `6687`
(`δ=5/2`, `b0=0`), of which 15 outer `A/B` pivots and 6600 otherwise
untouched outer coordinates.  D₂ contributes `5598-15=5583` new unit pivots;
D₁ contributes 176 more, on the 1002-dimensional D₂-remaining space.  The
inner `H,C2,C3` block and the minor `h3` leaders are disjoint from these
columns.

```text
outer ambient                                      6600
D₂ unit rank                                       5598     remaining 1002
D₁ Q* rank                                          176     remaining  826
h3/h2 + minor-h3 + centre after charged leaders     104 / 102
joint after outer D₂+D₁                    104+826 = 930  (δ=2)
                                           102+826 = 928  (δ=5/2, b0=0)
```

Driver: `box/g9966outer-20260903/outer_order_bands.py`, field `Q`, zero-point
positive control, leftover D₁ rows identically zero, `h2` D₁ replay, prefix-15
containment.  Both branches share the outer rows.

This is a counting bound of a relaxation that still omits the unranked
remainder of `IJ` and the effective-root jet identification.

## 5. Controls

**(16,12).**  `SOURCE-READ`, Moh p.208: 17-coefficient approximate-root chart,
already the order-truncated tower (outer bands present as support rules).
`u_s=1`, bridge trivial.  Both readings of the repeated `c_5` (printed:
`α_3=c_5 A+c_5 B+c_7`; compiler: distinct `c_6`, `α_1=0`) were built in the
same ring: 17 coefficients, Jacobian scalar `κ`, wrapper `T·κ-1`, **77**
coefficient rows of `J-κ`.  Groebner over `GF(32003)`, grevlex, is `[1]` for
both.  Wrapper controls in `Q[κ,T]`: `<κ, Tκ-1>=[1]`, `<κ-1, Tκ-1>≠[1]`.
The order-spine identity
`(20z-10/3)(27/10-27z/5)-1=-2(54z^2-36z+5)` holds over `Q`.  Ring, wrapper,
and both controls declared.  Verdict:
`SATURATED-EMPTY[P208-ANSATZ / GF(32003)]`.  Calibration of the method, not a
`(99,66)` emptiness.  `OPEN[PRINTED-C5-EMENDATION]` remains for general reuse.

**Automorphism.**  `F=ax+y`, `G=(a-1)x+y` has `J≡1` identically over `Q`,
inverse `x=F-G`, `y=aG-(a-1)F`.  Shared ansatz `Ax+y`, `Cx+y` reduces to the
single row `A-C-1`; slice `A=2` is the witness `(2x+y,x+y)`.  The plumbing
does not falsely kill it.  `NOT-APPLICABLE[s=3 tower, outer D₁/D₂, T2/T3;
degrees (1,1)]`.  `SURVIVES[UNIVERSAL-GLOBAL-CHECKS]`.

## 6. Complete row inventory of the joint chart

Typed against chart (2.1), ambient 7161 (plus branch centres).

| block | type | rows / rank | notes |
|---|---|---|---|
| fixed tops `in h3=P`, `in h2=P^3`, `in F=P^9`, `in G=P^6` | PRINTED | gauge, not rows | torus slice `a=1` |
| Tschirnhausen `no h3^2` in `h2`, `no h2^2` in `F` | PRINTED | identities of (2.1) | char-0 AM normalisation |
| major `h3` D₂ face + `h2` D₂ + first `h2` D₁ | PRINTED (charged) | 516 ambient → rank 396, dim 120 | `H,C2,C3` only |
| outer A,B D₂ Thm-1.2 | **DERIVED, this lane** | **5598** unit, rank 5598 | first point; both branches |
| outer A,B D₁ Thm-1.2 gap | **DERIVED, this lane** | 225 slots, **rank 176** | after D₂; leftover 49 dependent |
| h₃-adic `F_j,G_j` D₂ | DERIVED | 0 new outer pivots | implied by chart + D₂-`h2`; `F_1=G_1=0` identities |
| `δ=2` common-`h3` leader | PRINTED (charged) | 18 pivots on `H` | N8 face `p=z^2(z+3ρ)` |
| `δ=5/2` common-`h3` + reduced `T3` ODE through `s^{28}` | PRINTED (charged) | 20 leader + ODE | reduced ODE is *not* `T3∈K[F,G]` |
| first direct FG/J prefix | PRINTED (charged) | 16 rows, rank 15 | ⊂ outer D₂; Jacobian prefix becomes `0=0` after D₂ |
| T₂, T₃ *shape* in `K[F,G]` | PRINTED (Moh p.152, Xu p.10) | 5 / 35 unknown constants | `G^3-F^2`, `G^9-F^6` plus Tschirnhausen |
| T₂, T₃ *π-root identification* with `H` and `R` / `q_1` | **OPEN[EFFECTIVE-T2-T3-BRIDGE]** | 0 linear rows | face span misses `p^5` and deg-40 `R` |
| remainder of `IJ` (`deg≤162` minus 10 contiguous) | OPEN | ≤13,366−10 | next monomial `[x^{135}y^{27}]` |
| Moh unprinted 11-variable minor system | OPEN | — | p.210; not exhibited |

## 7. Next system for the decider lane

The cheapest genuinely new *linear* test on this add-on is already ranked:
the D₁ gap is closed as a `Q*` block.  The exact next joint system is
therefore the charged continuation, now on the D₂-reduced outer space of
**1002** `A,B` coordinates (826 after D₁):

* degree-162 Jacobian at `[x^{135} y^{27}]` and the contiguous face;
* pole rows `F_{(95,*)}` / `G_{(62,*)}` (branch-2 exponents `-77/-50`,
  branch-52 `-181/-118`);
* the D₁ gap rows of this lane (already available as a sparse binomial
  matrix, rank 176).

An empty localized ideal there would be a valid finite necessary-condition
kill of *that branch* inside chart (2.1).  A nonempty result remains a
counting bound.  Closing `OPEN[EFFECTIVE-T2-T3-BRIDGE]` is a different,
nonlinear job: write the residual of `T2(G,F)` (resp. `T3`) on the actual
minor jets of `F,G` and match `p^5` and `R` / `p^{10}q_1`.  Until that is
done, the minor `T3` ODE still constrains a free object.  Only after a full
specialisation is recomposed into polynomials and `F_x G_y-F_y G_x` is
checked identically as `1` may it be called a Keller pair.

## 8. FALLACY-v2

Flag/place/series: D₁/D₂ radii `(4/9,1/3)` are the major tower of Moh's `g`;
they are not the principal-minor split order `δ∈{2,5/2}` and not `δ*`.
First-point `v_s=8` is not identified with second-point `u_s=3`.
Carrier/attainment: dimension 930 / 928 is a relaxation floor, never a pair
and never `FULL_ACTUAL_EXIT`.  Floor/attainment: Theorem 1.2 is `≥`; face
equalities of `h3`/`h2` are exact because those *leading forms are fixed*,
not because a lower bound was promoted; the outer A,B faces are deliberately
*not* rows.  h₃-adic bounds are implied as inequalities, not as equalities.
`sat()`: `(16,12)` declares `GF(32003)` grevlex and both wrapper controls in
`Q[κ,T]`; the `(99,66)` prefix uses `Q` Gaussian with an explicit leftover-zero
check and the charged `h2` replay.  Prime marks: `p',R'` are `d/dz` where
quoted from the charged face ODE; Xu `p'` is `d/dπ`.  Variable/ring map:
`F=Moh g`, `G=Moh f`, `K_Q=t^D Q(t^{-1},w/t)`, `t=s^3` at D₂ and `t=e^9` at
D₁, `T_r^ψ∈k[G,F]`, all stated; matching names were not treated as proof.
Raw remainder: D₁ leftover rows were reduced to `0` in the declared
`Q`-matrix; the 49 dependent slots are not an inconsistency.  No new
exit-price assertion, so no `charge_basis` line.

## 9. Reproduction

```text
python3 box/g9966outer-20260903/outer_order_bands.py
python3 box/g9966outer-20260903/t2t3_bridge.py
python3 box/g9966outer-20260903/controls.py      # ~105 s, GF(32003) Groebner
python3 box/g9966outer-20260903/driver.py
```

Python 3, SymPy 1.12.  Order bands <3 s.  Bridge <1 s.  `(16,12)` ~105 s.
No Singular.  The charged driver under `box/g9966-20260903/` was not
modified.  Artifacts:
`box/g9966outer-20260903/{driver.py,outer_order_bands.py,t2t3_bridge.py,controls.py,results.json,outer_order_bands.json,t2t3_bridge.json,controls.json,inputs.sha256,artifacts.sha256,pages/,text/}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19457`.
- Body SHA-256:
  `b9118232414b4dfef9c2767afc03922373d2eeff0b7341f3375c6a441b7e90f3`.
- Frozen basis: `205316b028444eb1b94e195efb88a1244ec55395`.
