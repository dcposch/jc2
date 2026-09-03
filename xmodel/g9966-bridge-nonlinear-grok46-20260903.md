# Nonlinear T₂, T₃ bridge rows on the (99,66) minor jets

Lane `g9966-bridge-nonlinear-grok46-20260903`.  Add-on to
`box/g9966outer-20260903/` and the charged chart driver under
`box/g9966-20260903/` (neither modified).  New drivers live in
`box/g9966bridge-20260903/`.  No ledger, `jc2-lean`, `ideation-*`, or named
in-progress lane report (`g9966-global-band`, `k16-*`, `preprocess-native`)
was read or edited.

## Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g9966-bridge-nonlinear-grok46-20260903.run.v2`, checked with
`sha256sum -c`.  All **24/24** frozen inputs `OK`.  No digest was retyped.
Manifest: `box/g9966bridge-20260903/inputs.sha256`.

Shapes of `T2`, `T3` and Tschirnhausen counts are `PRINTED` (Moh p.152,
Xu §7.3 p.10): 4 + 34 unknowns after `α₁=0` and the monic `G³−F²`,
`G⁹−F⁶`.  The bridge *rows* on the actual minor jets are emitted in two
layers.

**Linearized straight slice** `u=0`, `a=1` (D₂-remaining outer slots, remaining
`C2/C3` after major D₁, three free `h3` tails, T-coefficients).  Exact `Q*`
over `Q`, leftover `0` on every block:

| block | columns | rank | remaining | leftover |
|---|---:|---:|---:|---:|
| linearized `F,G` leaders (2.4) | 1107 | **570** | 537 | 0 |
| `T2` vanishing `t^{-35}…t^{-11}` | 1107 | **544** | 563 | 0 |
| `T2` vanishing + leader `λ p^5` | 1108 | **557** | 551 | 0 |
| `T3` vanishing (z-deg `≤40` truncation) | 1136 | **2** | 1134 | 0 |
| union `FG+T2+T3` | 1141 | **974** | **167** | 0 |

`T3` in this truncation has only three nonzero columns; `LAMBDA3` pivots on
`[t^{-25} z^{25}]` of `−R` and forces `λ=0`.  That is *not* `R` in the linear
image: it is the statement that the truncated linear `dT3` does not produce
`R`.  `FALLACY-v2 / floor-attainment`: leftover `0` is consistency of a
relaxation, never a pair.

Tschirnhausen *face* on the leading pair `(p^9,p^6)`, coefficient ideal in
`z`, three primes `32003, 104729, 1299709`, grevlex std (ring
`GF(p)[c0,a1,a0,b1,b0,λ]` and `GF(p)[c0…c8,λ]`):

```text
T2_face − λ p^5  →  (λ, b0, b1, a0, a1, c0)     size 6
T3_face − λ R    →  (λ, c8, …, c0)              size 10
```

Only the origin.  `p^5` and `R` are not in the face spans as `z`-polynomials.
The charged p-power obstruction is confirmed as a coefficient-ideal statement.
The leaders remain residuals of *subleading* jets.

Union remaining **167** on this slice.  Of a 48-column *sample* of D₁ pivots
stored in the charged `outer_order_bands.json`, 9 `B2` slots still remain
(`B2_{63,0}`…).  If those 9 are independent of the 974, a floor is **158**.
The full D₁ rank 176 is not replayed (the JSON lists a sample, not 176
column names).  Quadratic `N≥2` generators in the 167 remaining variables
were not run to a standard basis (20-minute modular jobs on the *face* ideals
completed; a 167-variable quadratic std is not a 20-minute object).

```text
COUNTING-BOUND[LINEARIZED-STRAIGHT-u=0-a=1 UNION]  dim 167, leftover 0
COUNTING-BOUND[delta=5/2 SUPPORT + SAME FACE]     T2 window slots enumerated
OPEN[QUADRATIC-N>=2 ON REMAINING 167]
TRIVIAL[u_s=1 / (16,12)]
SURVIVES[tame deg>=6 J=1] / NOT-APPLICABLE[tame two-factor leading form]
```

`(99,66)` remains `OPEN`.  Nothing here is a Keller witness.  No new
exit-price assertion.

## 0. Pages opened

Printed Moh page `p` is PDF page `p-139`.  Xu printed page `p` is PDF page `p`.
Images under `box/g9966bridge-20260903/pages/`; OCR under
`box/g9966bridge-20260903/text/`.

```text
moh_p150_pdf11.png / moh_pdf-11.png   p.150  {M_j,d_j}; defining equation F(f,g)
moh_p151_pdf12.png / moh_pdf-12.png   p.151  Lemma 2.1; ψ: x ↦ 0
moh_p152_pdf13.png / moh_pdf-13.png   p.152  T_r^ψ = truncation of F^{1/d_r}; Prop. 2.2
xu_pdf-09.png                         p.9    §7.1; Lemma 7.1
xu_pdf-10.png / xu_p10_s73.png        p.10   §7.2–7.3; Lemma 7.2; Prop. 7.3
xu_pdf-11.png                         p.11   Prop. 7.3 proof; Cor. 7.5
xu_pdf-12.png                         p.12   equation (7.1); start of §8
xu_pdf-13.png / xu_p13_s8.png         p.13   (8.1)(8.2); T_i(σ) display; δ=5/2 open
```

## 1. SOURCE-READ: T_r^ψ shape and Tschirnhausen

`SOURCE-READ`, Moh p.150.  Characteristic data of `(f,g)` with respect to `x`:
`M_1=−m`, then `M_2,M_3`; `d_j=gcd(d_{j−1},M_j)`; `q_1=M_1`,
`q_j=M_j−M_{j−1}`; `λ_j=∑_{i≤j} q_i d_i`; `μ_j=λ_j/d_j`.  For `(99,66)`
with `M=(−66,77,97)` this is `d=(99,33,11,1)`, `μ=(−66,−55,−145)`, matching
Xu p.13.

`SOURCE-READ`, Moh p.151–152.  `F(f,g)` is the monic degree-`n` equation of
the symbol `f` over `k[x]((g^{−1}))`.  `ψ:x↦0` specialises coefficients.
Proposition 2.1: the `d_r`-th approximate root of `F` specialises to that of
`F^ψ`.  The printed formula (p.152) is the truncation of `F^{1/d_r}`:

```text
T_r^ψ(f,g) = f^{n/d_r} + ∑_{n/d_r ≥ i > 0} α_i(0,g) f^{n/d_r − i} ∈ k[f,g]
deg_y T_r^ψ(f(x,y),g(x,y)) = −μ_r     (Prop. 2.2, M_r ≤ e)
```

Moh keeps `α_1(0,g)`.  The AM Tschirnhausen that kills the second term is a
characteristic-zero normalisation, not forced by the displayed truncation.
Both counts are recorded: 5 / 4 unknowns for `T2` after monic / after
`α_1=0`; 35 / 34 for `T3`.  Weighted bound `deg_g α_i ≤ ⌊m i/n⌋=⌊2i/3⌋`.
Leading cancellation against monic `f,g` in `y` is `[g^{m/d_r}]α_{n/d_r}=−1`.

`SOURCE-READ`, Xu §7.3 p.10: `T_i(f,g)∈K[f,g]`, `T_0=g`, `T_1=f`,
`deg T_i=−μ_i`.  Chart names: `F=` Moh `g` (deg 99), `G=` Moh `f` (deg 66),
so `T_0=F`, `T_1=G`, and

```text
T2 = G^3 − F^2 + c0 G^2 + (a1 F + a0) G + (b1 F + b0)
T3 = G^9 − F^6 + ∑_{i=1}^{9} α_i(F) G^{9−i},   [F^6] of α_9 = −1
deg_y T2 = 55,   deg_y T3 = 145
```

`SOURCE-READ`, Xu p.13.  At a principal-minor `π`-root of order `δ`,

```text
G(σ)=p^6 t^{6(−8+3δ)}+⋯,   F(σ)=p^9 t^{9(−8+3δ)}+⋯,
T2(σ)=p^5 t^{5(−8+3δ)}+⋯,   T3(σ)=q t^{13(−8+3δ)−1+δ}+⋯
```

with `deg p=3`, `deg q=40`.  At `δ=2`: orders `−12,−18,−10,−25` and
`q=R=z^{25}(z+3a)^{14}(z−2a)`.  At `δ=5/2`: orders `−3,−9/2,−5/2,−5` in `t`
(`s^{−6},s^{−9},s^{−5},s^{−10}`) and `q=p^{10}q_1`, `q_1=−2∫p^3`.
Equation (7.1) is `∂(T_s(σ),g(σ))/∂(t,π)=−J·(T_s)_f(σ)\,t^{−2+δ}`.  Identity
(8.2) and the face ODE `2p R'−25 p' R=5 p^{14}` hold identically over `Q`
(driver `controls_bridge.py`).

## 2. Minor jets of F, G at the second point

Minor line `y=0`.  D₂-remaining outer coordinates are *not* `x^i y^j` poles:
`t^r(w−1)^q` pulls back as `x^{D−r−q}(y−x)^q`.  At `δ=2`, `u=0`,

```text
x^{D−r−q}(y−x)^q = (−1)^q t^{r−D} (1 − z t^3)^q
```

so the `k=0` t-order is `r−D`.  Remaining A3 starts at `t^{−45}`, *more
singular* than `F_lead=t^{−18}`.  Those slots must cancel in (2.4) before
`T2` is matched.  They are genuine subleading-to-the-top jets.

`k=0` order ranges of D₂-remaining slots, and the multiplier that lands them
in `G³−F²` (`h2∼t^{−6}`, `F0∼t^{−18}`, `G0∼t^{−12}`):

| block | D₂ remain | `k=0` min | T2 shift | T2 window `k=0` slots |
|---|---:|---:|---:|---:|
| A3 | 297 | −45 | −18 | 94 |
| A2 | 264 | −44 | −24 | 46 |
| B2 | 264 | −44 | −24 | 46 |
| B1 | 177 | −32 | −30 | 15 |

Inner after major D₁: 68 `C2` + 31 `C3` = **99**, plus free `h3` tails
`c_7_4, c_10_1, c_11_0`.  Charged joint inner+centre after the common-`h3`
leader is 104 (includes `u,ρ`).

At `δ=5/2`, `u=v=0`, `x=s^{−2}`, `y=π s^5`:
`x^{D−r−q}(y−x)^q=(−1)^q s^{−2(D−r)}(1−π s^7)^q`, `h2∼s^{−3}`.  T2 window
`s^{−18}…s^{−5}` is hit by 14+9+9+3 `k=0` slots of A3/A2/B2/B1.

Which chart coefficients appear at t-order `e` of `F(σ)` (straight slice):
every remaining `(r,q)` of A3 with `r−98+3k=e` for some `k≤q`; of A2 after
multiplying by `h2_0`; of `H,C2,C3` through `h2=h3^3+C2 h3+C3`; similarly
`G` from B1, B2 and `h2`.  Lists: `jet_support.json` (counts and samples)
and the `Q*` pivot heads in `residual_linear.json` (explicit first-fired
slots, e.g. `A3_{81,11}` at `(t,z)=(−35,18)`).

## 3. Residuals of T₂(G,F) and T₃(G,F); emitted rows

Write `F=p^9 t^{−18}+∑_{k≥1} f_k t^{−18+k}`, `G=p^6 t^{−12}+∑_{k≥1} g_k t^{−12+k}`
after (2.4), at `δ=2`.  Let `N` be the exponent above the face `t^{−36}` of
`G³−F²`.  The bridge rows are the coefficients of `t^{−36+N}` in

```text
T2(σ) = G³ − F² + c0 G² + (a1 F + a0) G + (b1 F + b0)
```

as polynomials in `z`:

```text
[t^{−36+N}] T2
  = ∑_{i+j+k=N} g_i g_j g_k − ∑_{i+j=N} f_i f_j
    + c0 ∑_{i+j=N−12} g_i g_j
    + a1 ∑_{i+j=N−6}  f_i g_j
    + a0 g_{N−24} + b1 f_{N−18} + b0 δ_{N,36}
```

Impose `[t^{−36+N}] T2 = 0` for `N=1,…,25` and `= λ p^5` at `N=26`
(`t^{−10}`).  `b0` first appears at `N=36` (order `0`), after the leader:
it is not a T2-leader unknown on this branch.  Tschirnhausen entry:
`a1` at `N=6` (`t^{−30}`), `c0` at `N=12` (`t^{−24}`), `b1` at `N=18`,
`a0` at `N=24` (`t^{−12}`).

**Linearity.**  After T-coefficients are fixed: `N=0` is the monic identity;
`N=1` is linear in `(f_1,g_1)` hence linear in the chart jets that first
appear there; `N≥2` contains `g_1^2`, `f_1^2` (quadratic) and from `N=3`
cubics.  Sequentially in `N` (Newton–Puiseux), each slice is affine in the
*new* jets `f_N,g_N`, with polynomial inhomogeneity in previous jets.
Simultaneous system on the 7161-chart: nonlinear for `N≥2`.  T-coefficients
enter bilinearly (T-coeff × jet products).

`T3` analogously from `G^9−F^6+∑ α_i(F) G^{9−i}`, face at `t^{−108}`,
target `N` such that `t^{−25}` (`δ=2`) / `s^{−10}` (`δ=5/2`).  Face
Tschirnhausen orders are multiples of 6 in `t`; `−25≡2 (mod 3)` at `u=0`
and `−25≡5 (mod 6)` as a face weight, so `R` is not a face value.

Unknowns on the linearized slice: 1102 chart names (D₂-remaining A/B +
remaining C + 3 `h3` tails) + 5 T2 Tschirnhausen + 34 T3 `α_{i,m}` = 1141.
Raw T2 vanishing labels: `25×41=1025` `(t,z)` slots; rank 544.  Raw T3
vanishing labels in the z-cap: 3362; rank 2 (truncation: `G0^8` has z-degree
144, dropped).  Equations after `Q*`: 974 independent linear rows, leftover
0, remaining 167.

## 4. Union with the 930 / 928 relaxation; Q* and modular bases

The charged outer-bridge space is 930 (`δ=2`) / 928 (`δ=5/2`, `b0=0`):
826 D₁-reduced outer + 104 inner+centre.  This lane's linearized union is
on the *larger* D₂-remaining outer (1002) plus inner 99 plus 3 `h3` plus
T-coefficients, at `u=0,a=1`.  It is not a change of the 7161 ring, and it
does not replay all 176 D₁ rows (only a 48-column sample of stored D₁
pivots: 9 still free, all in `B2`).

`Q*` leftover 0: the linearized bridge does not kill the slice.  Dimension
**167**.  Floor **158** if the 9 remaining sampled D₁ `B2` columns are
independent.  Relative to 930 this is a different ring (D₁ not fully
imposed; T-coefficients adjoined; `u=0` slice).  It is a counting bound of
a still-incomplete relaxation: quadratic `N≥2` in the 167, the unranked
remainder of `IJ`, and the full D₁ block.

Modular standard bases, three primes, grevlex, all `rc=0` well under 20
minutes, `OMP_NUM_THREADS=1`:

* Face `T2−λp^5` coefficient ideal: std `=(λ,b0,b1,a0,a1,c0)` on
  `32003`, `104729`, `1299709`.  Origin only.  Not `[1]`.
* Face `T3−λR` (G-powers `k=0…8`): std `=(λ,c8,…,c0)`, size 10, same three
  primes.  Origin only.
* Linear leftover of the 974-row union: empty, so std in the remaining 167
  is `(0)`.  No kill certificate.

`sat()` wrapping: rings are declared (`Q` for `Q*`; `GF(p)[…]` grevlex for
std).  Positive control: base `F0=h3^9`, `G0=h3^6` on the resolved `h3`
leader has `F_lead=p^9`, `G_lead=p^6` identically.  Negative: the face std
contains `λ`, so `λ=1` is impossible on the face.  Wrapper not used (no
Jacobian scalar in this ring).

Next system: sequential Newton `N=2` (quadratic in the first subleading
jets) on the 167 remaining coordinates, together with the 9 leftover
sampled D₁ `B2` columns and the unranked Jacobian face at
`[x^{135} y^{27}]`.  An empty localized ideal there would be a finite
necessary-condition kill of *this slice of this branch*, not of `(99,66)`.

## 5. Controls

**(16,12), `u_s=1`.**  `SOURCE-READ`, Moh p.207–208: the `(64,48)` parent
and the reduced p.208 chart have `u_s=1`.  Xu Prop. 7.3 / Moh Prop. 4.4:
`T_{i,σ}` are powers of one linear polynomial.  No split leader `R` or
`q_1`.  Bridge rows added: **0**.  Unknowns added: **0**.  Status
`TRIVIAL[u_s=1] / SATISFIED`.  Charged Groebner over `GF(32003)` of both
`c_5` readings remains `[1]` (not replayed; charged `controls.json`).

**Automorphism degrees (1,1).**  `F=ax+y`, `G=(a−1)x+y`, `J≡1` over `Q`.
`NOT-APPLICABLE[T2/T3 of degrees 55,145]`.  `SURVIVES`.

**Degrees ≥6, two distinct linear factors.**  128 compositions
`β∘α` with `α=(x,y+x^k)`, `β=(x+y^ℓ,y)`, `k,ℓ∈{2,3,4,5}`, and eight
`GL_2(Z)` of nonzero determinant: **0** hits with two distinct linear
factors in `in(F)` or `in(G)`.  Explicit witness
`β∘α`, `k=2,ℓ=3`: `deg(F,G)=(6,2)`, `in F=x^6`, `in G=x^2`, `J=1`.
`SURVIVES[J=1 / tame deg≥6]`.  A polynomial coordinate has one point at
infinity in `P^2`; triangular automorphisms are coordinates.
`NOT-APPLICABLE[tame two-factor]`.  `FALLACY-v2`: no fill by analogy.

The degenerate two-point top `F=P^9`, `G=P^6`, `P=y^3(y−x)^8` has two
linear factors and degrees `(99,66)`, but `J=0` and `G^3−F^2≡0`, which is
not `∼p^5`.  The bridge does not hold vacuously of every two-point pair.

Source identities over `Q`: face ODE and Xu (8.2) hold; `deg(−2∫p^3)=10`.

## 6. FALLACY-v2

Flag/place/series: D₁/D₂ radii `(4/9,1/3)` are the major tower of Moh `g`;
they are not the principal-minor split `δ∈{2,5/2}`.  First-point `v_s=8` is
not second-point `u_s=3`.  Carrier/attainment: dimension 167 is a
relaxation floor, never a pair, never `FULL_ACTUAL_EXIT`.  Floor/attainment:
`Q*` leftover 0 is consistency, not `T2(σ)=p^5 t^{−10}` as a polynomial
identity of a Jacobian pair; Theorem 1.2 was not re-used as equality.
`sat()`: face std rings `GF(p)[…]` grevlex declared; the origin ideal is
not `[1]`; both wrapper-free.  Prime marks: `p',R'` are `d/dz`; Xu `p'` is
`d/dπ`.  Variable/ring map: `F=` Moh `g`, `G=` Moh `f`, pullback
`x^{D−r−q}(y−x)^q`, slice `u=0,a=1`, `T_r^ψ∈k[G,F]`, all stated.  Raw
remainder: union leftover rows `0` in the declared `Q`-matrix.  T3 z-cap
40 is a truncation, not a proof that `dT3=0`.  No new exit-price
assertion, so no `charge_basis` line.

## 7. Reproduction

```text
python3 box/g9966bridge-20260903/jet_support.py          # support tables
python3 box/g9966bridge-20260903/residual_linear.py      # ~186 s, Q*
python3 box/g9966bridge-20260903/residual_d52.py
python3 box/g9966bridge-20260903/controls_bridge.py
python3 box/g9966bridge-20260903/face_span_qstar.py
python3 box/g9966bridge-20260903/d1_intersect_and_mod.py
python3 box/g9966bridge-20260903/driver.py
# modular, three primes, ≤20 min each:
Singular -q --no-rc box/g9966bridge-20260903/work/face_lin_p32003.sing
Singular -q --no-rc box/g9966bridge-20260903/work/t3_lin_p32003.sing
# (repeat p104729, p1299709)
```

Python 3, SymPy 1.12, Singular 4.3.2.  Charged drivers under
`box/g9966-20260903/` and `box/g9966outer-20260903/` were not modified.
Artifacts:
`box/g9966bridge-20260903/{jet_support.py,residual_linear.py,residual_d52.py,controls_bridge.py,face_span_qstar.py,d1_intersect_and_mod.py,driver.py,*.json,work/,pages/,text/,logs/,inputs.sha256,artifacts.sha256}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15645`.
- Body SHA-256:
  `54dcc5a93d6faab332fa8979338746bfcd951e20ebcfe5d5ce7ad1ddcafa316f`.
- Frozen basis: `8f7d0815fac29adfc554d97d55f02673594c0783`.
