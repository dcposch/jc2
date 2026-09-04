# D = 108 no-split descent: Prop 6.3 datum, variable map, (24,16) status

Lane `g108-nosplit-descent-grok46-20260903`.  Basis `1a3815fb`.
Task: close `OPEN[DESCENT-SUPPORT/VARIABLE-MAP]` for the no-split alternative
of the charged skeleton `(108,72; M=(−72,81,106); d=(108,36,9,1); V=(7,7))`.

## 0. Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g108-nosplit-descent-grok46-20260903.run.v2` and checked with
`sha256sum -c`; all thirteen frozen inputs under
`/tmp/jc2-lane.CG4V2L/inputs` returned `OK`.  No digest retyped.

```text
VERDICT  CONDITIONAL[D108-NOSPLIT]
CLOSED   the Prop 6.3 substitution (γ,π)-map, including the even jet
NOT CLOSED  identification of that pair with the ordinary total-degree
            two-point chart (24,16; M2'=18, V2'=7; k=4)
DEAD?    no.  The charged compiler unit is the 17(uu) δ1'=0 slice
         (first raw generator −c).  The general order chart 17(zzzz)
         kills (25,15;21;2;k=2), not this row, and reports the
         δ1'=0 instrument as INSTRUMENT-FAIL.
ROW      split branch DEAD [17(ddddd)]; no-split DESCENDS; the
         descended (γ,π) pair is not shown empty; D=108 is not
         closed at skeleton level.
RESIDUAL OPEN[ORDINARY-SUPPORT]  (= the original promotion blocker,
         after the substitution has been sourced)
```

Sol's numerical 4-tuple `(24,16; M2'=18, V2'=7; k=4)` is **correct** as
Prop 6.3 π-degrees and scaled characteristic data.  The JSON packaging
`V'=(7,2)` is `V2'=7` together with `d3'=2`, not a census `V3`.
No new exit-price assertion is made, so no `charge_basis` line is licensed.

## 1. Pages opened

`SOURCE-READ`.  Journal page `N` is PDF page `N−139`.  Images at 180 dpi
in `/tmp/g108-nosplit-pages/`.

| content | printed | image |
|---|---|---|
| Moh Prop 6.1 remainder; δ* estimate ≥ 1; top form; eq (8)–(10) `z=y−bx−e` | 193–194 | `moh-54.png`, `moh-55.png` |
| Prop 6.3 statement and proof; Prop 6.4; Cor 6.1 | 197–199 | `moh-58.png`–`moh-60.png` |
| Appendix II table; (16,12) shapes; (99,66) linear-power row | 207–209 | `moh_app-68.png`, `moh_app-69.png` |
| Xu Prop 7.3, the linear-power claim, Cor 7.5 | 10–11 | `xu-10.png`, `xu-11.png` |

Prime marks `n', m', M_i', V_i', d_i', δ_i', s', k` are labels for
descended data, never derivatives.  `p', q'` in Xu's ODE (charged
classification) are `d/dπ`.

## 2. Prop 6.3 for this row

### 2.1 Statement (`SOURCE-READ`, p.197)

Hypotheses.  `g` monic in `y` with `deg g = deg_y g = n > 1`; `δ_s = −1`;
and the logarithmic radius of the minor disc satisfies
`δ*_{s−1} ≥ v_s/u_s`.  Let `z` be (10), `y^{−1}=θ`, and view
`g, T_1^ψ, …, T_{s−1}^ψ` as elements of `k⟪θ⟫[z]`.  Then there is a
π-root `σ = Σ a_j θ^j + π θ^{v_s/u_s}` such that with `γ = θ^{1/u_s}`:

1. `ḡ(σ), T̄_1^ψ(σ), …, T̄_{s−1}^ψ(σ) ∈ k[γ, π]`;
2. they are monic in `π` of π-degrees
   `u_s n/d_s`, `u_s(−μ_1)/d_s`, …, `u_s(−μ_{s−1})/d_s`;
3. `J_{γ,π}(ḡ(σ), T_1^{−ψ}(σ)) = −(u_s/b) γ^{v_s−u_s−1}`.

Prop 6.4 (p.198): if in addition `u_s=1`, then `δ*_{s−1} ≥ v_s` automatically.
Cor 6.1 (p.199): for `u_s=1` (the `d_s=3` case of the corollary) the
characteristic data scale as `{M_i/d_s, d_i/d_s}` and the Jacobian is a
nonzero *constant* (here `k=v_s−2=0`).

`ERRATUM[PROP63-JAC-SIGN]` (charged, not re-opened): the last display of
the p.198 proof is the reciprocal `−u_s/(b γ^{v_s−u_s−1})`.  Statement (3)
and the p.207 Jacobian column are what is meant.  After a nonzero scalar
rescaling the target is `J = c γ^k`, `c≠0`, with `k=v_s−u_s−1`.

### 2.2 The three hypotheses, instantiated

Parent skeleton (`DERIVED`, `Skel(108,72,[81,106],{2:7,3:7})` from the
frozen `moh_skeleton_full.py`):

```text
n=108, m=72, s=3
M=(−72,81,106), d=(108,36,9,1), V=(7,7)
δ=(3/8, 1/4, −1),  A1=2, A2=4, L1=4, L2=1
windows_ok=true, full_ok=true, cond1011(j=2)=(true, by10), cond1213=by13
u3=d3−V3=2, v3=7, d3=9, v3/u3=7/2
minor threshold d3/(n−M3)=9/2:  u3=2 is minor, v3=7 is major
```

The specific `V=(7,7)` assignment is present in `census(108,Kmin=16,full=True)`
(a second assignment `V3=6` at the same `M` is a different row and is not
this client).

- `g` monic, `deg=deg_y=108>1`: gauge of the census row.
- `δ_s=−1`: Def 5.1(3) at `M_s=n−2`.
- `δ*_{s−1} ≥ 7/2`: **not** automatic (`u_s=2`, Prop 6.4 N/A).  Licensed
  only on the no-split alternative, §2.3.

### 2.3 Why no-split gives `δ* ≥ 7/2`

`SOURCE-READ`, Xu p.10–11 Prop 7.3: if `σ1` is the π-root of *order 1* for
the principal-minor roots of `f`, then `T_{0,σ1}(π),…,T_{s,σ1}(π)` are
powers of a common linear polynomial, and the proof claims
`p(π)=(π−a)^{u_s}`.  If not, a root `b≠a` extends to a final minor π-root
of some split order `δ0`, and every probe of order `1<δ<δ0` is a
distribution detector.

`SOURCE-READ`, Moh p.193 after Prop 6.1: the proposition does not specify
`δ*_{r−1}`; it only gives `δ*_{r−1} ≥ 1`.  That is the floor at which
Prop 7.3 applies.  The detector ceiling is independent: Prop 6.1's order
identity `ord g(σ)=(n/d_s)(u_s δ − v_s)` is negative iff `δ < v_s/u_s=7/2`
(charged classification, calibrated on Xu's printed `(99,66)` orders).

Dichotomy, `DERIVED` from those two facts plus N5 (`den δ ≤ u_s=2`) and
the charged classification 17(ssss):

```text
window for a genuine principal-minor split:  1 < δ < 7/2, den ≤ 2
candidates: 3/2, 2, 5/2, 3
SURVIVES: only δ=3, partition [1,1]     now DEAD [17(ddddd)]
complement: no split in (1, 7/2)
  ⇒ the u_s=2 minor roots have not separated below 7/2
  ⇒ δ*_{2} ≥ 7/2 = v_s/u_s
  ⇒ Prop 6.3's third hypothesis holds on this alternative
```

`FALLACY-v2 / flag-place-series`: the split order `δ=3`, the combined minor
radius `δ*`, and the major radii `(3/8,1/4,−1)` are three objects.  The
ceiling `7/2` (on detector `δ`, from `ord g<0`) is not identified with the
floor `V_s/u_s=7/2` (on a final `δ_σ`).  They coincide numerically here;
the no-split implication uses the detector ceiling as a lower bound on
`δ*`, not an attainment.

This is `DESCEND-WITH-MODIFIED-HYPOTHESIS` in the classification's language:
the premise is the complementary alternative to a now-empty split window,
not a proof that every pair with this skeleton has `δ* ≥ 7/2`.  On the
alternative, Prop 6.3 runs.

## 3. The descended datum

Scale `u_s/d_s=2/9`, drop the old top level `M_s` (`DERIVED`, matching the
frozen `descent_engine.py` derivation and Sol §7):

```text
n' = 2·108/9 = 24
m' = 2·72/9  = 16          (= u_s (−μ1)/d_s, since μ1=M1=−m)
M' = (−16, 18)             M_i' = (u_s/d_s) M_i for i=1,2
d' = (24, 8, 2)            d1'=n', d2'=gcd(24,−16)=8, d3'=gcd(8,18)=2
V2'= 7                     inherited parent V2 (p.207 / p.209 control)
u2'= d2'−V2' = 1
k  = v_s−u_s−1 = 4
s' = 2                     one dropped top level
```

Parent semigroup (Moh p.150 recipe, charged classification's calibration):
`q=(−72,153,25)`, `λ=(−7776,−2268,−2043)`, `−μ=(72,63,227)`.  Prop 6.3(2)
π-degrees:

```text
ḡ :     u_s n/d_s      = 24
T̄1:    u_s (−μ1)/d_s  = 16
T̄2:    u_s (−μ2)/d_s  = 14
```

Descended semigroup on `M'=(−16,18)`, `d'=(24,8,2)`:
`q'=(−16,34)`, `λ'=(−384,−112)`, `−μ'=(16,14)`.  The `T̄2` π-degree is
exactly `−μ2'`.  Characteristic height `n'−M2'=6=k+2`; two-point index
`R=n'−M2'−1=5=k+1`.  Jet height of the substitution is `v_s=7`.

Jacobian, statement (3): `J_{γ,π}(ḡ, T1^{−ψ}) = −(2/b) γ^4`.  After a
nonzero scalar rescaling this is Sol's `J(f',g')=c x^4`, `c≠0`.

**Sol comparison.**  The 4-tuple `(24,16; M2'=18, V2'=7; k=4)` matches.
Corrections of packaging, not of the 4-tuple:

* JSON `V'=(7,2)` is `(V2', d3')`, not a Moh `V=(V2,V3)` of a census
  row.  There is no sourced `V3'` at `s'=2`.
* `d3'=2≠1`: the scaled last `d4=1·2/9` is not integral, so the
  descended characteristic tower is truncated at gcd 2.  That is the
  `u_s>1` scaling, not a census-complete `{M_i}` with `M_s=n−2`.
* `V2'=V2` is not in Prop 6.3's statement.  It is `SOURCE-INFERRED` from
  the p.207 `u_s=1` table (three-fold `V2` match) and from Moh p.209's
  printed linear-power row `(27,18; V2=8)` at parent `V2=8`.  Both printed
  `u_s>1` and `u_s=1` instances keep `V2`.

Φ closed form on the 4-tuple (charged descent-radii rule, Lemma 5.1 with
`deg_x` of the Jacobian slot equal to `k+1`):

```text
K=8, e=3, q=2, u'=1, R=5, Π=5
δ2' = −(k+1)/R = −1
δ1' = (k+1)(Π u' − R)/(R(Π V2' − 1)) = 0
B   = V2' δ1' + u' δ2' = −1
```

Φ as a *geometric* theorem was proved in the charged radii lane on the five
`u_s=1` rows of p.207.  The same closed form hits Moh p.209's printed
`(δ2,δ1)=(−1,0)` on the `u_s=3` linear-power row (control §6).  For this
row it is recorded as the closed-form evaluation of the 4-tuple, not as a
new geometric measurement.

## 4. Variable map

Two maps.  Only the first is Prop 6.3.  Matching the names `(x,y)` after
a rename is not a map (`FALLACY-v2 / variable-ring map`).

### 4.1 Map I — Prop 6.3 substitution (`SOURCE-READ`, pp.194, 197–198)

**Rings.**  Source: the parent pair in `k[y,z]` after (10)
`z = y − b x − e` (`b≠0`, `e` the common constant of the minor expansion
(9)).  Coefficient field `k=ℚ`.  Target: `k[γ,π]`, generators in that
order, `π` the monic variable of Prop 6.3(2).

**Substitution.**  `θ=y^{−1}`, `γ=θ^{1/u_s}=θ^{1/2}=y^{−1/2}`.  The
inversion lemma (6.2) plus `δ*≥7/2` makes the coefficients below
`θ^{7/2}` common, so

```text
y  = γ^{−2}
x  = (1/b) [ θ^{−1} + Σ_{i=1}^{3} c_i θ^i + higher in θ ]
σ  = (c0−e) + Σ_{i=1}^{3} c_i θ^i + π θ^{7/2}
   = a0 + a1 γ^2 + a2 γ^4 + a3 γ^6 + π γ^7
```

(`i < v_s/u_s = 7/2` forces `i∈{1,2,3}`; `θ^i=γ^{2i}`.)  This is Sol's
strict-below/at-level jet.  The odd strict-below exponents `{1,3,5}` are
**forced to vanish**; they are not seven free odd/even terms.

**Image.**  Prop 6.3(1) is the image check: the Laurent substitution of
`g, T1^ψ, T2^ψ` lands in `k[γ,π]`.  Negative γ-powers cancel.  Prop 6.3
does **not** name `h3, h2, C2, C3, C4, A2, A3, B1, B2`.  Those are parent
chart coordinates.  Their individual images are not asserted to lie in
`k[γ,π]`; only the assembled `ḡ(σ), T̄1(σ), T̄2(σ)` are.

**Which parent coefficients become descended coefficients.**  Write
`g=Σ c_{ab} y^a z^b` in the Prop 6.2 box
`(deg_y, deg_z)=(v_s,u_s)·(deg)/d_s = (84,24)` for `g` and `(56,16)` for
`f` (charged classification §3).  Then

```text
ḡ(σ) = Σ c_{ab} γ^{−2a} (a0+a1 γ^2+a2 γ^4+a3 γ^6+π γ^7)^b
```

After cancellation of negative powers, each nonnegative `(γ,π)`-coefficient
of `ḡ` (resp. `T̄1`) is a polynomial in the parent `(y,z)`-coefficients of
`g` (resp. `f`) and in the jet `(a0,a1,a2,a3)` together with `b`.  The
Tschirnhausen identities `F=h2^3+A2 h2+A3`, `G=h2^2+B1 h2+B2` remain
polynomial identities in the parent; they do not by themselves give a
descended Tschirnhausen tower in `k[γ,π]`.

**Forced on the target.**

```text
monic:     [π^{24}] ḡ = 1,  [π^{16}] T̄1 = 1,  [π^{14}] T̄2 = 1
Jacobian:  all coefficients of J_{γ,π}(ḡ, T̄1) except the γ^4 slot vanish;
           that slot equals −2/b, or c after rescaling
jet:       odd strict-below coefficients of σ vanish
leading:   y^{84} z^{24} |_{y=γ^{−2}, z=σ} = π^{24} + lower π
           (γ^{−168}(π γ^7)^{24} = π^{24}), so the corner saturates monicity
```

**Not forced by Prop 6.3.**

```text
deg_γ ḡ ≤ 24                         (total degree = π-degree)
odd powers of γ in ḡ itself          (π γ^7 is odd; odd k produce odd γ)
the Appendix-II shape
  h = y^7(y−x) + Σ_{j=0}^{7} h_j y^j
vanishing of mixed x^i y^j in h below the top face
```

A raw bidegree-box envelope (`DERIVED`, exact scan of
`0≤a≤84`, `0≤b≤24`, `a+b≤108`): the π^k summand of `y^a z^b` has
γ-degree `≤ −2a+6b+k`, maximum **168** at `(a,b,k)=(0,24,24)`.  The corner
monomial alone has maximum 0.  Without a theorem that only the corner and
total-degree `≤24` terms survive, the descended pair is a polynomial in
`(γ,π)` of π-degree 24 whose γ-degree is only bounded by 168.  Moh's
coefficient counts `C(n'+2,2)+C(m'+2,2)` that force total degree = π-degree
are printed only for the three `u_s=1` rows of p.207 (charged m2-descent
§3.3).  They are not printed for `u_s=2`.

### 4.2 Map II — ordinary total-degree `(x,y)` chart (`NOT SOURCED`)

The charged compiler (frozen `descent.json`) works in a different ring

```text
Q[h0,…,h7, bp,bq,br,bs, c, T]     ordering dp
h = y^8 − x y^7 + Σ_{j=0}^{7} h_j y^j
β = bp A + bq y + br x + bs
f = h^2 + 2β,   g = h^3 + 3β h + (3/2)α
target J_{x,y}(f,g) = c x^4,  wrapper T c − 1
26 exact rows, split 18+8 over h-adic levels 0 and 1
```

This is the rename `(γ,π)↦(x,y)` plus the two-point leading form
`y^{V2'}(y−x)^{u'}` for `h` of `y`-degree `K=8`, plus the deletion of every
mixed `x^i y^j` in `h` below the top face.  Prop 6.3 supplies none of those
three steps.  Cor 6.1 supplies the rename and the total-degree count only
for `u_s=1`.  Appendix II p.208 supplies the `h=y^3(y−x)+Σ b_j y^j` shape
only for the printed `(16,12)` pair.

`OPEN[DESCENT-SUPPORT/VARIABLE-MAP]` as charged is therefore answered by
splitting: Map I is sourced; Map II is not.  The residual is
`OPEN[ORDINARY-SUPPORT]`.

## 5. The descended (24,16) 4-tuple: census, family, banked status

**Height.**  `n'−M2'=6=k+2`, `R=5=k+1`.  The two-point condition of
AUDIT 17(pp) is `R=k+1` (not `R=1`).  `s'=2` as a count of kept `M_i`,
not as a census `s` with `M_s=n−2`.

**Not a census row.**  `census(24, Kmin=2, full=True)` is empty.
The `(1)–(7)` list at `(n,m)=(24,16)` has 28 assignments, all with
`M_s=n−2=22`, never `M2=18`.  A Keller census row has constant Jacobian
and `M_s=n−2`; the descended object has `J=c γ^4` and `M2'=18≠22`.
GGV/`K≥16` does not apply at `gcd(24,16)=8`.  17(zzzz)'s parenthetical
that treated `(25,15)` as a census `u_s>1` row is already withdrawn
(`ERRATUM[2515-FILING]`); the same trap is avoided here.

**Family.**  Not the `K=16` ray of descendants `(12t+4, 8t+4)`:
`t=1` gives `(16,12)`, `t=2` gives `(28,20)`, and `t=5/3` gives
`(24, 52/3)`, not `(24,16)`.  The 4-tuple is the `K=8` member of the
two-point ray

```text
(n',m')=(3K, 2K),  V2'=K−1,  u'=1,  k=4,  M2'=3K−6,  R=k+1,  (δ2',δ1')=(−1,0)
K=7:  (21,14; 15; 6; k=4)     parent (147,98) in the two-point list
K=8:  (24,16; 18; 7; k=4)     parent (168,112) in the two-point list;
                              also the D=108 no-split datum
K=9:  (27,18; 21; 8; k=4)     parent (189,126); also Moh p.209 branch A
                              from (99,66)
```

Same `e=3, q=2` tower combinatorics as the parent (`n/d2=3, m/d2=2`),
scaled by `2/9`.

**Banked status (AUDIT / APPROACHES, consumed not re-argued).**

| tag | what it says about this 4-tuple |
|---|---|
| 17(pp) | SATURATED-EMPTY on the A/B chart, 13 unknowns / 26 equations |
| 17(uu) | those three `k=4` “kills” are **slices**: at `δ1'=0` the batch rule deletes every `x`-term of `h` below the top face, `J` cannot produce `x^k`, first generator is `−c`, and `T c−1` closes trivially |
| 17(bbb), 17(lll), 17(hhh) | the three `δ1'=0` rows stay OPEN / COUNTING-BOUND on honest and R3 charts; `(168,112)` is in the OPEN 10 of the 17-group list |
| 17(zzzz) | general order chart: banked validation rows and `(25,15;21;2;k=2)` are `[1]`; the `δ1'=0` row `(21,14;15;6;k=4)` is **INSTRUMENT-FAIL** (`deg_x J0=2<k=4`), not promoted |

The charged compiler is the same A/B enlargement (`h=y^7(y−x)+Σ h_j y^j`,
13 unknowns, 26 rows) with the same smoking gun Sol records: first raw
row `−c`, lift `1=(−T)(−c)−(T c−1)`, raw dimension 10, localized dimension
`−1`.  That is 17(uu)'s slice, not a theorem about Map I's pair.  Even if
Map II were sourced, this diagnostic would not promote.

So: the descended 4-tuple is **not** banked DEAD, **not** killed by
17(zzzz), and the compiler unit does **not** become a kill once Map I is
sourced.

## 6. Controls

Foreground, exact `Fraction` arithmetic against the frozen skeleton;
no Singular rerun (the charged `descent.json` already records the
compiler diagnostic, and 17(uu) already classifies it).

**(64,48)→(16,12), Appendix II.**
`Skel(64,48,[52,62],{2:3,3:3})` has `d=(64,16,4,2)`, `u_s=1`, `v_s=3`,
`d_s=4`.  Prop 6.4 supplies `δ*≥3` automatically; Prop 6.3 applies
unconditionally.  Scale `1/4`: `(n',m',M2',V2',k)=(16,12,13,3,1)`.
Φ `=(−1,1/4)`, matching p.207.  Map II *is* sourced here: Moh p.207
counts `244=C(18,2)+C(14,2)`, and p.208 prints
`h=y^3(y−x)+b1 y^3+b2 y^2+b3 y+b4`.  The Appendix-II kill of this row
is banked; this lane only replays the descent arithmetic.  The control
shows what D=108 is missing: a printed total-degree count and a printed
`h`-shape.

**(99,66) no-split / branch A.**
`Skel(99,66,[77,97],{2:8,3:8})` has `d=(99,33,11,1)`, `u_s=3`, `v_s=8`,
`d_s=11`, `v_s/u_s=8/3`.  Scale `3/11`:
`(n',m',M2',V2',k)=(27,18,21,8,4)`, Φ `=(−1,0)`.  This is Moh p.209's
printed linear-power row, **byte-for-byte** the same 4-tuple.  It is the
`K=9` neighbour of the D=108 datum on the ray of §5.  Banked 17(tt)
kills the A/B *predecessor* of that printed row (14 unknowns, first
generator `−c`).  This lane replays the descent numbers and does not
re-promote 17(tt); it notes that the A/B predecessor is the same shape
17(uu) later typed as a slice on the isomorphic `(189,126)` descendant.
Moh p.209 *does* print ordinary degrees `(27,18)` for the linear-power
`u_s>1` case — a source instance of Map II at `(99,66)`, not a general
theorem, and not transferable to D=108 by analogy.

**Leading-form monicity (hand).**  Parent corner `y^{84} z^{24}`
substitutes to `γ^{−168}(π γ^7)^{24}=π^{24}`.  The π-leading coefficient
is 1 without any total-degree hypothesis.  That is Map I, clause “monic”.

## 7. FALLACY-v2 audit

*Flag/place/series.*  Major radii, split order `δ=3`, combined `δ*`,
substitution jet, and ordinary `(x,y)` support are separate.  Strict-below
jet exponents `{0,2,4,6}` are not identified with at-level `π γ^7`, nor
with the Appendix-II lower terms of `h`.
*Per-ray / carrier / attainment.*  No exit is claimed.  `δ*≥7/2` is a
lower bound on the no-split alternative, not `FULL_ACTUAL_EXIT` and not
attainment of `δ*=7/2`.  Φ's `(−1,0)` on the 4-tuple is a closed-form
evaluation, not a measured geometric radius of a D=108 pair.
*Pole/interior.*  Unused.
*Floor/attainment.*  The γ-degree envelope 168 is a floor on the *unknown*
γ-degree, not an identification with 24.  Equality `deg_γ=24` would need
a theorem covering every omitted term of the box; none is sourced.
*`sat()` wrapping.*  No saturation is run here.  The charged compiler's
localized unit is cited only as a diagnostic already classified by 17(uu);
its ring `Q[h0..h7,bp,bq,br,bs,c,T]`, wrapper `T c−1`, and raw/empty/point
controls live in the frozen `descent.json` and are not re-used as a kill.
*Raw remainder degree.*  Unused.
*Variable/ring map.*  Map I is declared (rings, generator order,
coefficient field, substitution, image check).  Map II is declared as
absent.  Parent block names `h3,h2,A2,…` are not treated as descended
coordinates.
*Prime label/derivative.*  As §1.
*Merge-free / target-arrival.*  Not touched.
No gap is filled by cap or by transferring 17(tt), Appendix II, or
17(zzzz).  No `charge_basis` line.

## 8. Dependency chain and residual

```text
(108,72; M=(−72,81,106); V=(7,7); u3=2, v3=7)
    │
    ├─ split in (1, 7/2): only δ=3 [1,1]
    │     DEAD[D108/delta3/DECLARED-NECESSARY-JOINT-CHART]   17(ddddd)
    │
    └─ no split in (1, 7/2):  δ* ≥ 7/2
          Prop 6.3 (not 6.4) applies
          Map I:  (y,z)  —(γ=y^{−1/2}, σ=even jet + π γ^7)→  k[γ,π]
          π-degrees (24,16,14), J = c γ^4, M2'=18, V2'=7, k=4
          Map II (ordinary total-degree two-point chart): NOT SOURCED
          A/B compiler unit: 17(uu) slice, not a kill
          17(zzzz) does not hit this 4-tuple
          (24,16;18;7;k=4) banked OPEN on the δ1'=0 ray
```

The no-split alternative is therefore **conditional descent to a
monomial-Jacobian pair in `k[γ,π]`**, not a skeleton-level death.
The whole D=108 row remains open on that pair.

```text
TYPED[D108-NOSPLIT]
  hypothesis   δs=−1 and δ*≥7/2 on the complement of the empty split window
  conclusion   ḡ, T̄1, T̄2 ∈ k[γ,π], monic of π-degrees 24,16,14,
               J = −(2/b) γ^4  (statement (3); scalar c γ^4 after rescaling)
  datum        (24,16; M2'=18, V2'=7; k=4; d'=(24,8,2); s'=2; u'=1)
               Sol 4-tuple CONFIRMED; V'=(7,2) is (V2', d3')
  map I        y=γ^{−2}, σ=a0+a1 γ^2+a2 γ^4+a3 γ^6+π γ^7     SOURCED
  map II       ordinary total-degree / A/B two-point chart     NOT SOURCED
  family       (3K,2K) u'=1 k=4 δ1'=0 at K=8; NOT (12t+4,8t+4)
  census       not a row (census(24,full)=∅; (1)–(7) has Ms=22)
  banked       OPEN on the δ1'=0 ray; 17(zzzz) N/A; compiler = 17(uu) slice
  residual     OPEN[ORDINARY-SUPPORT]
  whole row    split DEAD ∧ no-split CONDITIONAL; no REPRESENTATIVE
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21395`.
- Body SHA-256:
  `722d8d39c2b703e7d0518f1412efcdbfeb75ad3479ef692baab7b02ee56282cc`.
- Frozen basis: `1a3815fb22ee0c174fc2f228d16673dff7d954ac`.
