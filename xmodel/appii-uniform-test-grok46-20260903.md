# APPII-UNIFORM TEST — Grok 4.6 — 2026-09-03

Lane `appii-uniform-test-grok46-20260903`. Cheapest test of
`CONJ[APPII-UNIFORM]` (charged `prop55k-opus5-20260903.md` §4.2, PROVISIONAL
delta 17(z)): Moh's p.210 Appendix II reduction with the **descended**
order conditions. Frozen inputs in `/tmp/jc2-lane.zyQliU/inputs`; **all 11
SHA-256 verified** by `awk` from the lane receipt plus `sha256sum -c`
before any read (stop-on-mismatch did not trigger). Moh 1983 read from
`refs/moh1983_jram340_configurations_of_roots.pdf` (`6c8847a8…`, matches),
rendered at **200 dpi** with `pdftoppm -r 200`. Journal page `N` = PDF page
`N−139`. Pages opened **as images**: `j207_pdf68-68.png` … `j211_pdf72-72.png`
in `box/appii-uniform-20260903/moh-pages/` (PDF 68–72).

Every Moh citation below is `SOURCE-READ` (page given) or typed
`SOURCE-UNVERIFIED`. Tools: `which Singular` → `/usr/bin/Singular` 4.3.2;
`which M2` → not found; sympy 1.12. Desk-scale, one core; CAS wall
under 15 min except the honest-G2 construction which was killed at 240 s
and typed `COUNTING-BOUND`.

Discipline: no canonical ledger edited; `jc2-lean` not inspected; no
`ideation-20260903T1200Z-*` file and no running lane's report opened.
Drivers in `box/appii-uniform-20260903/`.

Prime marks `n', m', M_i', V_i', d_i', δ_i', k` are **labels** for
descended data, never derivatives. `P` is Moh's descended polynomial
(Prop 6.3); `Π = n*+m*`. The remainder polynomial `δ` of p.210 eq. (3)
is named `delta` in code and marked when quoted. Singular's reserved
`p` (characteristic) is never a coefficient name (`bp, bq, br, bs, cc`).

## 0. Headline

1. **Calibration holds.** Moh's `(15,10; 11; 3; X²)` is
   `SATURATED-EMPTY` by the general routine with licensed `(c)` (the
   2,2,6 split of p.210) and the audited `γ`; Case 1 is Moh's
   contradiction; Case 2 lex `Q[a1..a12,T]`, Rabinowitsch `T a9−1`,
   Gröbner `{1}` in 0.008 s. `ERRATUM[APPII-GAMMA-B]` reproduced:
   Euclidean `γ` matches B-coefficient `−a9² a8`, not the printed
   `−a9² a10`. Frozen `moh_1510_control2.py` / `moh_1510_controls_pm.py`
   replay identically. Positive drop-one and negative toy: the kill uses
   exactly the three monomials `(2,0), (1,1), (0,2)`. `SOURCE-READ` p.210–211.
2. **Second positive control holds.** `(16,12; 13; 3; X)` in the p.209
   η-form (10 shape coefficients + `cc`) with `J = cc x`, saturate
   `cc ≠ 0`: Singular grevlex `{1}` in 0.95 s, 70 equations, 11 unknowns.
   Unsaturated 65 gens (non-trivial); drop the `(1,0)` matching of
   `J−cc x` survives (65 gens). `SOURCE-READ` p.208–209.
3. **Negative control survives every named step.** The existing pair
   `P = π⁵ − γ⁵`, `Q = P³ + aπ` has `J = −5a γ⁴` by direct
   differentiation. After the D1-centering Moh always makes (p.207:
   “choose `x, y` properly so that the π-root in `D1` is
   `σ = π t^{δ1}`”), `(a)`, `(b)`, and the `π^{-1}`-tail all hold.
   Imposing the unlicensed 2,2,6 leading form **would** exclude it
   (different support). The routine does not.
4. **G2, honest support: `COUNTING-BOUND`.** Inputs
   `(15,10; M₂'=4; V₂'=1; X⁴)`, `d₂'=5`, `n*=3`, `m*=2`,
   `δ₁'=5/4`, `δ₂'=−1/2` (closed form, charged Φ). Order support:
   14 free in `h` + 27 in `β` + `c` = **42**, matching the charged
   `descent-radii` count. `(c)` is **not licensed** (`δ₂' ≠ −1`;
   inverse-Prop-6.3 2,2,6 is the `(75,50)→(15,10; V₂=3)` geometry).
   Construction of identity (3) in 41 parameters did not return in
   240 s / 1 core; Gröbner not reached.
5. **G2 slices empty; this is the METHOD, not a frontier theorem.**
   Newton-tight 12-unknown slice: `SATURATED-EMPTY` (`T cc−1`, `{1}`,
   0.10 s). Order-`h` (14) + Moh-pattern `β` (4) + (3) + `J=cc x⁴`:
   `SATURATED-EMPTY` (`{1}`, 0.66 s, 81 eqs, 19+`T` vars); unsaturated
   103 gens; drop `(4,0)` survives. Unlicensed 2,2,6 + (3) empties
   because (3) does not see `k` — it is Moh's Case 2, **wrong shape**.
   G2 is a `D = 105` descendant and `D = 105` is already TREE-empty
   (AUDIT delta 17(p), provisional, **not consumed**). A G2-slice kill
   proves the **method** of Appendix II under descended radii, not a
   new existence theorem on the frontier.
6. **`CONJ[APPII-UNIFORM]` at this instance remains `CONJ`.** Calibration
   and the fail-closed family hold; the honest G2 system is not solved;
   `(c)` does not generalise by copying 2,2,6. What *does* generalise
   is named in §6.

No exit-price assertion is made, so no `charge_basis` line is due.

## 1. SOURCE-READ, pp.207–211

**p.207.** Prop A.5: `D=c ≠ 0` ⇒ `p·q` simple roots. Descended table
`(16,12; 13; 3; δ=(−1,1/4); X)`, `(15,10; 11; 3[2]; δ=(−1, 1/2[4/3]); X²)`.
“Choose `x, y` properly so that the π-root in `D1` is `σ = π t^{1/4}`.”

**p.208.** `(16,12)`: `h` the 4th approximate root, `deg_y h=4`,
`ord α_i(σ) ≥ i(−1/4)`, `ord h(σ) ≥ −1/4`. Shapes (1)–(5):
`h = y³(y−x)+b₁ y³+b₂ y²+b₃ y+b₄`. **Sign of (a):** Moh's bound is
`≥ i(−δ₁)`. At `σ=π t^{δ₁}`, `ord(x^i y^j)=−i+δ₁ j`, so
`ord h ≥ −δ₁` ⇔ `i ≤ δ₁(j+1)`. The CONJ phrase “`≥ i·δ₁'`” names
that signed quantity, not the positive `5/4`. The routine implements
Moh. `SOURCE-READ`.

**p.209.** η-reduction to 10: `β₂β₃=γ h+γ*`, `β₂³=δ h²+δ*`,
`g = h⁴+(4/3)(β₂ h²+β₃ h)+(2/9)(β₂³+2γ)−(4/81)δ+a₂ h²`.

**p.210.** `(15,10; 11; 3)`: `f=h²+2β`,
`g=f^{3/2}+a f^{−1/2}+b f^{−6/10}+c(x³+d)f^{−9/10}+⋯`.
Polynomiality forces `(3) β³=(3γ+a)h²+ε h+δ` with `deg ε,δ<4`.
Inverse Prop 6.3 ⇒ “three subdiscs which contains 2, 2, 6 of roots
`f`”; with `δ₁=1/2` this licenses `h_top=y³(y²−x²)`.

**p.211.** Printed `γ` has B-coeff `−a₉² a₁₀`. From `A y ≡ −a₈` and
`A² ≡ (a₆x+a₇)A − a₈ B (mod h)` it is `−a₉² a₈`:
`ERRATUM[APPII-GAMMA-B]`. Case 1 `a₉=0` is Moh's contradiction. Case 2
printed `a₁₀=0` does not close; audited `a₈=0`,
`a₆=−2a₁₁/a₉`, `a₇=−2a₁₂/a₉` plus (3) do.

**Lemma 2.1 tail at `(m*,n*)=(2,3)`.** `g=η̃^{−15}+Σ g_j η̃^j`,
`η̃=f^{−1/10}`: `J=c x^k` ⇔ `g_j∈k` for `j<9` and `deg_x g_9=k+1`.
The term `a η̃⁵=a f^{−1/2}` has `5<9`, so `a∈k` for every `k`,
including G2's `k=4`. Identity (3) with `a` constant is the correct
`(2,3)`-tail at G2; the `x`-dependent term is `J=c x^k` itself.

## 2. The general routine

`box/appii-uniform-20260903/appii_reduce.py`.

**Inputs.** `n', m', M₂', V₂', k` and the closed-form radii
`δ₂' = −(k+1)/R`, `δ₁' = (k+1)(Π U₂' − R)/(R(Π V₂' − 1))`,
`R = n'−M₂'−1`, `Π = n*+m*`, `U₂' = d₂'−V₂'`, `d₂' = gcd(n',m')`.
The four charged values (p.207 two rows, G2, control family) match
this formula with zero free parameters.

**Outputs.** The polynomial system in the coefficients of `h` and of
the `α_i, β_i` after:

- **(a)** D1 order: monomial `x^i y^j` of a weight-`w` coefficient is
  allowed iff `i ≤ δ₁'(j+w)`, together with `tot(h)=deg_y h = d₂'`,
  `deg_x h ≤ U₂'`, `tot(β) ≤ m'`, `deg_x β ≤ U₂' m'/d₂'`. Monic leader
  `y^{d₂'}` is kept.
- **(b)** `deg_y α_i, β_i < d₂'`; second-level `deg_y γ < d₂'`,
  `deg_y ε,δ < d₂'−1`; from (3), `deg_y γ ≤ d₂'−3` (= 2 when `d₂'=5`).
- **Tail.** For `(m*,n*)=(2,3)`: Euclidean `β² = α h + γ`; (3) as
  “`h²`-quotient of `β³`, minus `3γ`, is a constant in `(x,y)`”.
  For `(3,4)`: the p.209 display (η-form of `g`).
- **(c)** only when licensed. 2,2,6 (`h_top = y^{V₂}(y²−x²)`) is
  licensed solely for `(15,10; 11; 3; k=2)` (Moh p.210: inverse
  transform of degrees 50 and 75). Two-point Lemma 5.3
  (`δ₂' = −1` ⇒ more than one point at infinity) licenses
  `y^{V₂}(y−x)^{U₂}` (the `(16,12)` printed form is the `U₂=1` case)
  and is **not** the inverse-6.3 2,2,6 split. If `δ₂' ≠ −1`, (c) is
  refused and the support is order-only.

**`sat()` discipline (FALLACY-v2).** Every emptiness claim names the
ring, generator order, coefficient field `Q`, the Rabinowitsch
generator, and both controls. The returned object is the Gröbner
basis of that *component*. Engine: Singular `std` / `groebner`,
`option(redSB)`, grevlex (`dp`) unless the 12-variable lex Case 2.

## 3. Positive controls

### 3.1 `(15,10; 11; 3; X²)` — `SATURATED-EMPTY`

`(c)` licensed. `h_free` = 8 monomials of p.211 (5); Moh-pattern `β`
(6) is the order support at `δ₁=1/2`. Euclidean `γ`:

| formula | reproduced |
|---|---|
| printed `α = a₉² B + 2 a₉ a₁₀` | True |
| printed `γ` (B-coeff `−a₉² a₁₀`) | **False** |
| audited `γ` (B-coeff `−a₉² a₈`) | **True** |

`ERRATUM[APPII-GAMMA-B]` **CONFIRMED**.

Case 1 `a₉=0`: `α=0`, `γ=β²`, `deg_y β³ = 3 < 5`. (3) forces
`3γ+a=0` so `γ` constant; (4) needs `deg_y ε=4`. Contradiction.
Moh's Case 1, reproduced.

Case 2 audited: `a₈=0`, `a₆=−2a₁₁/a₉`, `a₇=−2a₁₂/a₉`. Five
non-constant monomials of `c₂−3γ` (same as charged control2). Ring
`Q[a1..a12,T]`, lex, `T a9−1`. Gröbner `{1}` in **0.008 s**. Drop-one:
`(2,0),(1,1),(0,2)` non-trivial (5 gens); `(1,0),(0,1)` still `{1}`.
Negative `a9=1,a10=2,a11=3`: 4 gens. Kill uses exactly that triple.
Frozen replay: EMPTY, audited True, printed-gamma False.

### 3.2 `(16,12; 13; 3; X)` — `SATURATED-EMPTY`

Printed p.208 `h = y³(y−x)+b₁ y³+b₂ y²+b₃ y+b₄` (Lemma 5.3, `U₂=1`,
`SOURCE-READ`, not 2,2,6). p.209 η-form: `β₂ = bp A + bq`,
`β₃ = br A + bs B + bt`, plus `a₂`, plus `cc`. 11 unknowns.
`J − cc x = 0` expands to 70 equations.

```text
  MAIN     : saturate cc != 0  ->  EMPTY  [1]
             ring Q[b1..b4, bp,bq,br,bs,bt, a2, cc, T], grevlex, T*cc-1
             0.95 s  (J built 10.7 s)
  UNSAT    : 65 gens, not {1}          [cc=0 lives]
  POSITIVE : drop (1,0) matching       -> NON-TRIVIAL (65)
  NEGATIVE : cc=1, no J eqs            -> NON-TRIVIAL (T-1, cc-1)
```

The 17-coefficient raw p.208 shape was not needed (η-form already
empty). Moh's “reduced to 10, then compute” is this job.

## 4. Negative control — `SURVIVES`

Family A of the charged `control_pairs.py`:
`P = π⁵ − γ⁵`, `Q = P³ + a π`, `(n',m')=(15,5)`, `k=4`, `d₂'=5`,
`n*=3`, `m*=1`, `M₂'=9`, `V₂'=1`, `δ' = (−1, 11/3)`,
`J = −5 a γ⁴`. Direct differentiation in `(γ,π) = (x,y)`:

```text
  J(P,Q) = −5 a x^4     (exact; c = −5a).
```

This pair is **not** a Prop 6.3 descendant; it is a native
monomial-Jacobian witness that PROP 5.5(k) must not kill, and that
the Appendix II routine must not kill either.

`m*=1` ⇒ `P = h` (no `β_i`). Unshifted `h = y⁵ − x⁵` fails the raw
order bound at `σ = π t^{11/3}` because the common part is not in
`k((t))` — the same phenomenon as charged prop55k §3.4. After
D1-centering `Y = π − γ` (Moh p.207 “choose `x,y` properly”):

```text
  h = (Y+x)⁵ − x⁵ = Y⁵ + 5 x Y⁴ + 10 x² Y³ + 10 x³ Y² + 5 x⁴ Y
  monomials (0,5),(1,4),(2,3),(3,2),(4,1)
  (a)  i ≤ (11/3)(j+1)  on each: holds
  deg_x h = 4 = U₂'
  tail Q − h³ = a(Y+x)     polynomial, deg_y = 1 < 5     (b) holds
  (a) on α₃ = a(Y+x), weight 3: holds
  shifted J = −5 a x⁴      still the monomial
```

Every named step of `(a)`, `(b)`, and tail cancellation **SURVIVES**.
The 2,2,6 leading form `{y⁵, −x² y³}` is a different support; applying
it would exclude this existing pair. It is **not** applied. The
routine does not over-constrain.

## 5. G2 — with and without `(c)`

Closed form on `(15,10; 4; 1; k=4)`: `R=10`, `δ₂'=−1/2`, `δ₁'=5/4`,
`d₂'=5`, `n*=3`, `m*=2`, `U₂'=4`. Matches charged Φ and the
`descent-radii` §4.2 value independently.

### 5.1 `(c)` is not licensed

`δ₂' = −1/2 ≠ −1`: Lemma 5.3, one point at infinity, leading form a
power of a single linear form, **not** `y^{V}(y−x)^{U}` and **not**
`y³(y²−x²)`. The 2,2,6 split of p.210 is the inverse-Prop-6.3 geometry
of the **`(75,50)`** parent (`d_s=5`, `v_s=4`, descended `V₂=3`,
`u'=2`, `δ₂'=−1`). G2's parent is `(105,70)` with `d_s=7`, `u_s=1`,
`v_s=6` (charged compiler: `M=(28,103)`, `V₂=1`, `V₃=6`). Copying
2,2,6 onto G2 is an unlicensed assumption. Typed
`OPEN[G2-INVERSE-SPLIT]`: a derived subdisc list for that parent is
not produced here. The V₂'-count (Def 5.1(1)) gives 2 roots of `P` in
`D₁` and 8 in the complement; that is a **floor** on the split, not
the 2,2,6 triple.

Without `(c)`: 14 free monomials of `h` (the charged list: `y⁴, xy⁴,`
`y³,xy³,x²y³, y²,…,x³y², y,xy,x²y, 1,x`) and 27 of `β`
(`i≤(5/4)(j+2)`, `j≤4`, `i+j≤10`, `i≤8`). Plus `c`: **42**, matching
charged `descent-radii` §4.3.

### 5.2 Honest support: `COUNTING-BOUND`

`tail_m2n3` on 14+27 symbols (cubic identity (3)) ran **> 240 s / 1
core** without returning generators; the job was killed. Exact
counts: **41 unknowns** without `c`, **42** with `c`. What exceeds
one core: **construction** of the cubic system in sympy, before any
Gröbner. Equation count not obtained. Typed `COUNTING-BOUND`.
Cheapest unblock: emit (3) by monic `y`-division inside Singular
(not sympy `expand`), or first the quadratic `(7)` (`deg_y γ ≤ 2`).

### 5.3 Slices, labelled as slices

**Unlicensed 2,2,6 + (3).** Same Case 2 as §3.1. Empties (`{1}`,
0.36 s) because (3) does not see `k`. Moh's `(15,10)` shape, not
G2's. Wrong-shape kill.

**(3) only, 14 of `h` + Moh-pattern `β` (18 unk).** The 4-span
`β=bp A+bq y+br x+bs` is a **slice** at `δ₁'=5/4`. Saturate `bp≠0`:
**SURVIVES**, 42 gens, 0.09 s. Point
`h=y⁵+2x y⁴+x² y³+3y²+2x y` satisfies (3); differentiation gives
`J=27(x+y)(7x+5y)`, not `c x⁴`. So (3) alone does not exclude
G2-shaped data; `J=c x^k` is load-bearing here.

**(3)+`J=cc x⁴`, 19 unk.** Ring
`Q[14 h-free, bp,bq,br,bs, cc, T]`, grevlex, `T cc−1`. 81 eqs.

```text
  MAIN     : sat cc!=0 -> EMPTY [1]     0.66 s
  UNSAT    : 103 gens, not {1}           0.02 s
  POSITIVE : drop (4,0) of J−cc x^4 -> NON-TRIVIAL (103)
  NEGATIVE : cc=1, no J -> NON-TRIVIAL (T-1, cc-1)
```

`SATURATED-EMPTY` **on this slice**, not on G2.

**Newton-tight 12-unk** (`h=y⁵+aa x² y` + y-poly `+ ee x`, Moh `β`,
`J=cc x⁴`): grevlex `{1}` in 0.10 s, 30 eqs. Slice: Newton leading
term, not the 14-monomial order support.

## 6. Verdict on `CONJ[APPII-UNIFORM]`

At this instance the conjecture is **not proved and not refuted**.

| object | `(a)(b)`+tail | + licensed `(c)` | + `J=c x^k` | verdict |
|---|---|---|---|---|
| Moh `(15,10;11;3;X²)` | empties at Case 2 | licensed, used | not needed | **SATURATED-EMPTY** (calibration) |
| Moh `(16,12;13;3;X)` | η-form of `g` | Lemma 5.3 `y³(y−x)`, printed | empties | **SATURATED-EMPTY** (calibration) |
| Family `π⁵−γ⁵`, `P³+aπ` | survives | 2,2,6 would kill; not applied | holds by construction | **SURVIVES** (fail-closed) |
| G2 honest 14+27 | construction >240 s | not licensed | not reached | **COUNTING-BOUND** |
| G2 Moh-`β` slice | survives (J≠cx⁴ points) | — | empties | SATURATED-EMPTY **slice** |
| G2 Newton slice | — | — | empties | SATURATED-EMPTY **slice** |
| G2 unlicensed 2,2,6 | empties (no `k`) | wrong shape | — | SATURATED-EMPTY **wrong shape** |

**What generalises** (not a theorem). **(a)** `i≤δ₁'(j+w)` via Φ is
uniform in `k`. **(b)** remainder degrees are Euclidean, uniform.
**Tail (3) for `(2,3)`:** `a` stays a constant for every `k`
(`5<m'−1`); uniform as an *identity*, not as a *kill* (G2 Moh-`β`
slice leaves `J≠cx⁴` points). **(c) does not generalise** by copying
2,2,6 (parent-specific; `δ₂'=−1` required). **`J=c x^k` is
load-bearing** once (3) does not empty.

**Not claimed:** any kill or genuine-pair survival of G2 as a whole;
any consumption of AUDIT 17(p); any proof of (T). G2 is a `D=105`
descendant; `D=105` is already TREE-empty on that provisional
screen. A slice-emptying tests the **method**, not a frontier theorem.

## 7. Bounded quantities and OPEN accounting

| item | bounded quantity | cheapest test | status |
|---|---|---|---|
| Moh `(15,10; V₂=3)` | 5 monomials of `c₂−3γ`; 12+`T` vars | lex `{1}` 0.008 s + pos/neg | **SATURATED-EMPTY**; ERRATUM confirmed |
| Moh `(16,12)` | 70 eqs, 11+`T` vars (η-form) | grevlex `{1}` 0.95 s + pos/neg | **SATURATED-EMPTY** |
| Family `π⁵−γ⁵` | 1 pair, 5 shifted monomials of `h` | order check + `J` by hand | **SURVIVES** `(a)(b)` tail |
| G2 honest support | 14+27+`c` = 42 | Singular `y`-division of (3) | **COUNTING-BOUND**; construction >240 s |
| G2 Moh-`β` + `J` slice | 81 eqs, 19+`T` | grevlex `{1}` 0.66 s | SATURATED-EMPTY **slice** |
| G2 Newton slice | 30 eqs, 12+`T` | grevlex `{1}` 0.10 s | SATURATED-EMPTY **slice** |
| `OPEN[G2-HONEST-GB]` | 41 (no `c`) / 42 (with `c`) | emit (3) in Singular, not sympy | typed OPEN |
| `OPEN[G2-INVERSE-SPLIT]` | 1 split of 10 `f`-roots | Newton–Puiseux on a generic `(105,70)` image | typed OPEN |
| `OPEN[A-PRIME-ONE]` | charged, `≤ 4.3%` rows `k≤8` | untouched | OPEN |
| `OPEN[COMMON-PART-LATTICE]` | charged | untouched | OPEN |
| `OPEN[MINOR-DICHOTOMY]` | `u_s>1` | untouched | OPEN |
| `CONJ[APPII-UNIFORM]` | datum (a)(b)(c)+tail, uniform in `k` | this lane | remains **CONJ** |

No `OPEN` was filled by cap or analogy. The 240 s kill on honest G2
is reported as `COUNTING-BOUND`, not as emptiness.

## 8. FALLACY-v2

No cv-flag/place/series; no per-ray charge; no exit price (no
`charge_basis` line); no pole identity. **Floor/attainment:** the
V₂'-count 2+8 on G2 is Def 5.1(1), not a derived inverse-6.3 split.
**`sat()`:** every emptiness names ring, grevlex/lex, field `Q`,
Rabinowitsch, unsaturated non-triviality, a drop-one positive, and a
toy negative. **Remainder degree:** `sympy.div` in `y` by a monic;
`β²−α h−γ=0` checked on (15,10). **Ring map:** Prop 6.3 `(γ,π)` vs
Appendix II `(x,y)` and remainder-`γ` never identified; coeffs
`bp,bq,br,bs,cc` avoid Singular `p`. **Prime marks:** labels.
Controls are not promoted (family survived; G2 empties are slices /
wrong shape). AUDIT 17(p) provisional, not consumed.

## 9. Typed block

```text
LANE         appii-uniform-test-grok46-20260903 (Grok 4.6)
SOURCE       Moh 1983 at 200 dpi: pp.207-211 (PDF 68-72)
GATE         hashes 11/11; Singular 4.3.2; M2 absent; sympy 1.12
PROVED-HERE  (15,10;11;3;X^2) SATURATED-EMPTY; ERRATUM[APPII-GAMMA-B]
             (B-coeff -a9^2 a8); Case 2 lex {1} 0.008s; pos/neg match.
PROVED-HERE  (16,12;13;3;X) eta-form SATURATED-EMPTY, {1} 0.95s,
             70 eqs / 11+T; unsat 65; drop (1,0) survives.
PROVED-HERE  Control pi^5-gamma^5, P^3+a pi SURVIVES (a)(b) tail
             after D1-centering; J=-5 a gamma^4 by differentiation.
TYPED        G2 honest 14+27+c=42 COUNTING-BOUND (construction >240s).
TYPED        G2 slices SATURATED-EMPTY (Newton 12; Moh-beta 19+J;
             unlicensed 2,2,6). Slices/wrong shape, not G2.
             G2 is a D=105 descendant; D=105 already TREE-empty
             (AUDIT 17(p) provisional, not consumed). Slice kill
             proves the METHOD, not a frontier theorem.
CONJ         CONJ[APPII-UNIFORM] remains CONJ. (a)(b) and (2,3)-tail
             identity generalise in k; (c) does not; J load-bearing
             on G2 once (3) does not empty.
OPEN         OPEN[G2-HONEST-GB]; OPEN[G2-INVERSE-SPLIT];
             charged A-PRIME-ONE, COMMON-PART-LATTICE, MINOR-DICHOTOMY
             untouched.
```

## 10. Drivers

```text
box/appii-uniform-20260903/appii_reduce.py     general (a)(b)(c)+tail
box/appii-uniform-20260903/run_all.py          closed form, 1510, family, G2 counts
box/appii-uniform-20260903/run_1612.py         (16,12) eta-form + J
box/appii-uniform-20260903/run_g2_generic.py   honest 14+27 (killed, COUNTING-BOUND)
box/appii-uniform-20260903/results/*.json      certificates
box/appii-uniform-20260903/moh-pages/          pdftoppm -r 200, PDF 68-72
  Frozen replay: /tmp/jc2-lane.zyQliU/inputs/moh_1510_control2.py
                 /tmp/jc2-lane.zyQliU/inputs/moh_1510_controls_pm.py
```

Pages: `pdftoppm -r 200 -f $p -l $p` on PDF pages 68–72. Reruns deterministic; no seeds.

## COLLISIONS

`P` polynomial vs `Π=n*+m*`; `k` exponent vs field; `δ` radius vs p.210 remainder;
`A` denominator vs the polynomial `A(x,y)` of `h=yA+a₈`; Singular `p` vs `bp`;
Prop 6.3 `γ` vs remainder `γ`. Never identified.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20432`.
- Body SHA-256:
  `3cb235849570660319cc2d58378f92606c7435f1edd93323ef5a21a1bc334b47`.
- Frozen basis: `7e667dd2a537174540070064c2520fbff96c327d`.
