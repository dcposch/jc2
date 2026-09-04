# Ideation round 20260904T1200Z — blind submission (Opus 5)

Lane `ideation-20260904T1200Z-opus5`; basis `bb2a1a78`; packet
`ideation-20260904T1200Z-packet.md` (sha256 `1ee8e07b…`).

## 0. Provenance, verification, and what is new here

All four charged inputs verified mechanically: the manifest was generated from
`xmodel/ideation-20260904T1200Z-opus5.run.v2` with `awk` on the
`charged_input_<i>_sha256=` / `_basename=` lines and checked with
`sha256sum -c` — 4/4 OK, no retyping. Read in order: packet, 00:00Z synthesis,
FALLACY-v2, COORDINATION (§§ full-spectrum, OPEN authoring rules), then
AUDIT 17(tttt)–(ooooo), the newest `notes.md` LIVE STATE/EVENT block
(11:36Z), the APPROACHES overlays (2026-09-04T08:56Z and 2026-09-03 10:45Z).
The running lane `k16-hsop-length-allt-opus5` was checked by receipt only
(`initial_status=RUNNING`, no `final_status`); its `.md` was **not** opened and
its live box directory `box/k16hsop-20260903/` (files written 11:31–12:02Z)
was **not** read.

Four things were computed or read from primary source inside the lane budget;
they change three of the four answers:

1. **`L_t` is the weighted Bézout number of the tail system** — an identity,
   not an independent theorem. Proving "length = `L_t`" *is* proving `dim 0`.
   The `2^{t−2}` resultant surcharge follows in one line from the same
   bookkeeping. (§3, PROVED-HERE, arithmetic replayed t = 3..12.)
2. **Case (A) of (99,66) — the last scope hole in the flagship — is one
   elementary lemma away from closing.** The banked branch-A system, with the
   suspect standalone `−c` row *deleted*, has residual locus exactly
   `{bp = bq = br = 0}` (exact over Q, dim 11, controls pass); on that stratum
   `β` is a constant, `α = 0`, and `f = h²+2β`, `g = h³+3βh` are both
   polynomials in `h`, so `J ≡ 0`. The `−c` row was *right* there. (§4,
   MEASURED + PROVED-HERE.)
3. **The (H1) census is arithmetically stratified 129 / 48.** The (99,66)
   pivot closed form's non-vanishing (`11 ∤ 3n`, 17(hhhhh)) generalises to a
   skeleton predicate; it holds on 129 of the 177 `u_s > 1` groups and fails on
   exactly 48, and **every** failing group has `D ≥ 144`. The entire live
   frontier (99, 105, 108, 112, 117, 120) is non-resonant. (§5, MEASURED, the
   banked 1420/310/177 controls reproduced.)
4. **N2 cannot be closed by the source read the packet hopes for.** Xu §8
   *declares* "the denominator of order δ ≤ u_s = 3" as one of his two tools
   and never proves or cites it (the string "denominator" occurs exactly twice
   in the whole paper, both times as an assumption). Moh p. 188 has the
   conjugation/coprimality block that is the only plausible source. (§4,
   source read.)

Artifacts banked: `box/nonres-20260904/` (scan + log),
`box/caseA-20260904/` (six Singular scripts, six `.out`, `artifacts.sha256`).
Every Singular run below is sub-second, char 0, with the four controls
(`CONTROL_EMPTY_PASS`, `CONTROL_NONEMPTY_PASS`, `CTRL_UNIT = −1`,
`CTRL_ORIGIN = 0`) printed; per the lane-CAS rule the `.out` files were
grepped for markers rather than trusting exit status.

## 1. Disposition vector over the APPROACHES rows (changes only)

| row | change | reason |
|---|---|---|
| 32 (off-diagonal collision ideal / Fitting) | **RAISE** (mechanism, not program) | The Fitting/rank formulation is now the *exact* object on both halves: for K16 the tail is `dim 0` iff `Fitt₀ = I₂(M)` is m-primary for an explicit `2 × (2t−2)` matrix (§3); for (H1) the missing uniform statement is itself a Fitting/Schur row (17(ooooo)). The row's own client (`I:Δ = I + (det A)`) stays where it is; what rises is the *technique*. |
| 43 (Ritt decomposition / composite coordinates) | **REOPEN as a stratum-closer** | Previously scored 3 ("collapses to GGV after Aut-reduction"). But the residual stratum of the branch-A chart is exactly the *composite* locus `f, g ∈ k[h]`, and one line of Ritt/functional-dependence kills it (§4). Composite-locus arguments are the natural closers of every unsplit terminal chart, not a program. |
| 6 (Abhyankar–Moh one-place / coordinate recognition) | **RAISE** (already raised 2026-09-03; reaffirmed) | The `h`-tower normal form `f = h^q + …`, `g = h^e + …` is the object every terminal chart is written in; the case-(A) kill is an AM-style statement about `B₂`. |
| 3 (vertex-gap / strip ODEs / residue functional) | **RAISE** | The ladder law `c(p,k) = ±[eA(K−p) − n(k−k₀)]` (17(iiiii)) plus the pivot closed form `9(99−3n−11i)` is a *residue functional* on the Jacobian band; §5 turns its non-vanishing into a skeleton-level arithmetic predicate that is decidable for free on the whole census. This is the row that owns the (H1) theorem route now that disc is refuted. |
| 20 (reduction mod p / p-curvature formalism) | **unchanged as a route, RAISE as an instrument** | The minimal compute change unblocking OPEN[FULL-BASIS-TIMEOUT] is modular Gröbner + rational reconstruction + *exact* char-0 verification of the cofactors (§5.6) — bookkeeping under row 20's banner, not the refuted formalism. |
| 1 (GGV corner families / degree farm, reopened as RECEIVER) | **unchanged**, but re-scoped | The receiver is only licensed for `u_s = 1` (Prop 6.3). The `u_s ≥ 2`-unsplit configurations are *not* receiver clients today (§6). |

Everything else `unchanged`. In particular I do **not** lower K16 (row-less;
it is the (H2) prototype) despite the fixed-`t` exhaustion — §3 gives it a new
object, not a new computation.

## 2. Bottleneck reranking

1. **Case (A) of (99,66)** — the cheapest closable item in the campaign and
   *load-bearing for the banked headline*: one elementary lemma plus one
   chart-necessity check (§4).
2. **N2 = GAP[DEN(δ) ≤ u_s]** — from "literature, presumed closable" to
   "unproved anywhere we can find"; the exhaustiveness of the A/B/C
   configuration list rests on it (§4.6).
3. **The `u_s ≥ 2`-unsplit class** — no sourced engine, zero closed instances
   before today; this is the third configuration Q4 asks about (§6).
4. **K16 all-`t`** — retargeted from a length identity (a tautology given
   `dim 0`) to a maximal-rank statement (§3).
5. **(H1) uniform row** — the ladder/non-resonance route (§5), with a measured
   129/48 stratification of the census.
6. OPEN[FULL-BASIS-TIMEOUT] as engineering (§5.6), demoted: the case-(A)
   experiment shows the killing content sits on a low-dimensional linear
   stratum that is cheap to find directly.

## 3. Q1 (K16) — the length statement is a tautology; the right all-`t` object is a maximal-rank statement

### 3.1 The framing is wrong, and provably so

The packet asks whether `L_t = 2·binom(3t+1, t−1)` is "provable for all `t` by
a Gröbner-free structural argument". It is not an independent statement.

The cone ring is, from the frozen emitter
(`box/k16hilb-20260903/emit_preexpanded_cone_job.py`, docstring lines 9–12,
read directly):

```
(b4, q2_0, …, q(t−1)_0, b3),  wp(1, 2, …, t−1, t+1)
```

— `t` variables, weights `1, 2, …, t−1` and `t+1` (note: **no weight-`t`
variable**). The tail rows `T_{t,t..2t−1}` are `t` weighted-homogeneous forms
of weights `2t+2, 2t+3, …, 3t+1` (17(wwww) Theorem TOPTAIL gives the row of
index `2t−1−r` weight `2t+2+r`, `r = 0..t−1`). Therefore

> **PROVED-HERE (three lines).** `∏(row weights) / ∏(variable weights)
> = ∏_{d=2t+2}^{3t+1} d / ((t−1)!·(t+1)) = L_t`. That is *exactly* the
> function `predicted_tail_length(t)` in Card A's emitter. So `L_t` is the
> weighted **Bézout number** of the tail system.

Consequence, in a weighted polynomial ring (Cohen–Macaulay) with `#rows =
#variables`, all weighted-homogeneous:

> **TFAE for every `t`:** (i) `V(tail) = {0}`; (ii) the tail is an hsop;
> (iii) the tail is a regular sequence; (iv) `dim_k S_t/(tail) = L_t`.

`(i)⇒(ii)` is the definition of a system of parameters at the vertex;
`(ii)⇔(iii)` is CM; `(iii)⇒(iv)` is the graded Koszul resolution;
`(iv)⇒(i)` is finiteness. **There is no route to (iv) that is cheaper than
(i).** Card A's `t = 5, 6` "length = `L_t`" measurements (17(mmmmm)) are
therefore `dim 0` measurements re-labelled — excellent controls, zero
independent leverage. The `Q1` half that asks for a "weighted-Fröberg" proof of
the length is asking for a proof of `dim 0` under another name, and a
weighted-Fröberg argument cannot supply it: Fröberg is a *generic*-coefficient
statement and these rows are anything but generic (the negative control
`t = 2, y = 1/5` fails `dim 0` with the same weights — 17(kkkkk) — so no
weight-only argument can be valid).

### 3.2 The `2^{t−2}` surcharge, derived rather than measured

Res_{b₃} of two `b₃`-quadratics of weights `w₀ = 2t+2` and `w_r = 2t+2+r` in a
variable of weight `t+1` has weight `2w_r + 2w₀ − 4(t+1) = 4t+4+2r`, matching
17(wwww). So the resultant system `R_1..R_{t−1}` lives in
`B = k[b4, q2_0, …, q(t−1)_0]`, weights `1..t−1`, and its weighted Bézout
number is

```
B_t = ∏_{r=1}^{t−1}(4t+4+2r) / (t−1)!  =  2^{t−1} ∏_{d=2t+3}^{3t+1} d / (t−1)!
L_t = (2t+2)·∏_{d=2t+3}^{3t+1} d / ((t−1)!(t+1))  =  2·∏_{d=2t+3}^{3t+1} d / (t−1)!
⇒  B_t / L_t = 2^{t−2}   for every t ≥ 3.
```

Replayed exactly `t = 3..12`: `B_t = 180, 2288, 29120, 372096, 4775232,
61529600, …` — these are *Grok's measured weighted Bézout numbers* from the
00:00Z round (§2 of the synthesis: 180, 2288, 29120, 372096) and Opus V3's
measured ratio, now both a one-line identity. This is `KNOWN` as a number and
`NEW` as a derivation.

### 3.3 The sharpest provable statement I can offer: a maximal-rank / Fitting reformulation

TOPTAIL gives `a₀ = α_t`, a nonzero **constant** (weight 0). So
`Q₀ := T_{t,2t−1} = α_t b₃² + b₀ b₃ + c₀` is monic-up-to-a-unit in `b₃`, and

```
R := S_t/(Q₀)  is a FREE B-module of rank 2, basis {1, b₃}
                (graded: B ⊕ B(−(t+1))).
```

Reduce the remaining `t−1` tail rows: `Q_r ≡ λ_r + μ_r b₃ (mod Q₀)` with
`λ_r, μ_r ∈ B` of weights `2t+2+r` and `t+1+r`. The ideal they generate in `R`
is generated **as a `B`-module** by the `2(t−1)` elements `Q_r, b₃Q_r`, so

```
S_t/(tail) = coker( M : B^{2t−2} → B ⊕ B(−(t+1)) ),   M = [ (λ_r,μ_r) | b₃·(λ_r,μ_r) ]
```

and `Fitt₀(coker M) = I₂(M)`, the ideal of `2×2` minors. Hence:

> **REFORMULATION (PROVED-HERE modulo TOPTAIL's `a₀` unit).** For every `t ≥ 3`:
> `V(tail) = {0}` **iff** the `2 × (2t−2)` matrix `M` over `B` (`t−1`
> variables) has rank 2 at every point off the origin, i.e. `I₂(M)` is
> `m`-primary.

This is strictly better than both current objects:

* against the square resultant system `R_1..R_{t−1}`: `V(R) = {0}` is only
  *sufficient*, and the gap is exactly the `2^{t−2}` surcharge — `V(R)` is
  where each `Q_r` shares *some* root with `Q₀`, `V(I₂(M))` is where they all
  share *the same* root: `2^{t−1}` root-assignments, of which the 2 "all-same"
  ones are the true locus. The surcharge is a *root-matching multiplicity*, not
  an elimination cost, and the Fitting ideal removes it exactly.
* against the tail itself: one fewer variable, and — decisively — the target
  becomes a **maximal-rank statement**, which is the class of statement that
  degeneration arguments actually prove. To show `rank M = 2` off the origin it
  suffices to exhibit a weight vector `w` on `B` such that the initial forms
  `in_w(M)` already have `I₂` `m`-primary (upper-semicontinuity of rank under
  flat degeneration), or to exhibit `t−1` minors forming an hsop of `B`. Both
  are *finite combinatorial* certificates, both are Gröbner-free, and both are
  per-`t` uniform if the spine recursion for `(λ_r, μ_r)` is triangular.

This also explains 17(xxxx)'s "initial-form-upgrade failure at `t = 4, 5`":
that test degenerated the *tail*, whose degeneration must control `b₃` too.
Degenerating `M` only has to control `B`.

### 3.4 Which all-`t` target? — answer

**Neither of the packet's two, as stated. Rank of `M`.** Ranking:

* the length identity: a tautology (§3.1) — **STOP asking for it separately**;
* `Z-EMPTY_t` via the linear-form Jacobian (17(kkkkk)): this is the *right
  logical target* (it is what `(V0)` really needs) but it is a strictly
  *larger* system (cone + one more generator `T^hom_{t,0}`), so it inherits
  every computational problem the tail has and adds one row. Keep it as the
  statement; do not attack it directly.
* `I₂(M)` `m`-primary: same content as the tail, one fewer variable, no
  surcharge, and a proof shape (rank/degeneration) that exists.

**Cheapest test (≈ 25 lane-minutes, desk scale).** Build `M` at `t = 3, 4, 5`
from the banked pre-expanded cone rows: reduce `Q_1..Q_{t−1}` mod `Q₀` in
`B[b₃]` (division by a unit-leading quadratic — no Gröbner), form `I₂(M)`,
check (a) `dim = 0` in `t−1` variables at `t = 3, 4, 5` (must agree with the
known cone results), (b) `deg V(R_1..R_{t−1}) / deg V(I₂(M)) = 2^{t−2}` as a
positive control on §3.2, (c) negative control `t = 2, y = 1/5` must **not**
give `m`-primary. Gate: all three, both fibres at split `t`. If (a) passes at
`t = 5` in seconds where the tail needs 33 s, the object is also cheaper and
`t = 7, 8` become reachable — but that is a bonus; the point is the proof
shape.

## 4. Q2 ((99,66) unsplit + paper-grade) — case (A) decided structurally, not by compute; and N2 is worse than the packet thinks

### 4.1 The source, read (Moh p. 209, PDF page 70)

Extracted from the text layer directly (`pdftotext -f 70 -l 71`), so this is a
primary read, not a relay:

> "In the fourth case there are complications. First, there are two
> possibilities according to the distribution of the roots of `g(y)` in the
> minor disc … The polynomial `g_σ(π)` is either a power of a linear polynomial
> or the 9-th power of a cubic polynomial with precisely two roots. **For the
> first possibility the data can be transformed to** `n = 27, m = −M₁ = 18,
> M₂ = 21, V₂ = 8, δ₂ = −1, δ₁ = 0, Jacobian X⁴`. The above mentioned method
> can be used to reduce the number of coefficients to 10."

So 17(jjjjj)'s description of case (A) is **exactly** Moh's, including
`Jacobian X⁴` and the count 10 — and Moh does **not** print the ten equations.
Also confirmed on the same page: the "above mentioned method" is the p. 208–209
reduction with `deg γ* < deg h = 4`, `deg δ* < deg h² = 8` — i.e. the same
approximate-root-tower reduction Opus V6 identified. Since `(27, 18)` with
`deg h = 9` means `(deg_h g, deg_h f) = (3, 2)`, case (A) is a `d' = 2,
e' = 3` two-point chart — which is precisely the chart the banked driver builds
(`box/moh9966-20260903/moh9966_branch_driver.py:90`, `tp.d2e3_ab_system`).

### 4.2 What the banked branch-A system actually contains (MEASURED, exact over Q)

`box/moh9966-20260903/systems/branch_A_linear_AB_Q.sing` is 47 lines. Its ideal
begins

```
ideal I = -c,
          -48*br^2,
          6*bq^2 + 12*bq*br + 54*br^2,
          … (26 more) …,
          T*c-1;
```

The first generator is the bare `−c` and the last is the Rabinowitsch
`T·c − 1`; those two alone give `1 ∈ I`. So the banked
`MAIN_SATURATED_EMPTY` at 17(tt) carries **no information whatsoever** — the
QUALIFICATION's diagnosis is right, and it is visible on line 15 of the script.

I ran the **strictly weaker** system: the same 28 rows with `−c` deleted, same
ring, same localisation, char 0 (`box/caseA-20260904/branch_A_drop_minusc_Q.sing`,
`.out`; wall 0.00 s, 11 MB):

```
MAIN_START equations=28 unknowns=14 char=0 DROPPED_ROW_minus_c
MAIN_DONE basis_size= 14 ; MAIN_NONTRIVIAL ; DIM 11
CTRL_RAW_DIM_no_localisation 12 ; CTRL_UNIT −1 ; CTRL_ORIGIN 0
CONTROL_EMPTY_PASS ; CONTROL_NONEMPTY_PASS
```

and then identified the locus (`branch_A_radical_Q.sing`, `.out`):
`bp³, bq³, br³` all reduce to 0 in `G` (so `(bp,bq,br) ⊆ √I`), `bs` and `c` do
not; `dim V(bp,bq,br) ∩ {c ≠ 0} = 11 = dim V(I)`; and `V(bp,bq,br) ∩ {c ≠ 0}`
is irreducible. Hence, set-theoretically and exactly,

> **MEASURED[BRANCH-A-RESIDUAL].** After deleting the suspect `−c` row, the
> banked branch-A system's localised solution locus is **exactly**
> `{bp = bq = br = 0, c ≠ 0}` — 11 free dimensions (`h_0_0..h_0_8`, `bs`, `c`).

Confirming from the other side: localising at `bp`, at `bq`, at `br`, at
`bp·bq·br`, or at `c·br` instead of at `c` makes the same 28 rows a **unit
ideal** over Q — `basis_size 1`, `dim −1`, all four controls pass, five
independent runs, each sub-second
(`box/caseA-20260904/branch_A_loc_{bp,bq,br,bpbqbr,c_and_br}.out`).

### 4.3 The residual stratum dies by one line, and it is chart-free

In this chart (`build_beta_ab`, `twopoint_order_batch.py:154`)
`β = bp·A + bq·y + br·x + bs` with `A = (h − h|_{y=0})/y`, and the pair is

```
f = h² + 2β ,   g = h³ + 3β h + (3/2) α ,   α := quo_y(β², h).
```

Verified symbolically (sympy, three `β`'s, exact):

> **PROVED-HERE[BRANCH-A-JACOBIAN-IDENTITY].**
> `J(f,g) = 3h·J(h,α) − 6β·J(h,β) + 3J(β,α)` identically
> (the `h²` term cancels — that is what the depressed `3β/2β` normalisation
> buys). In particular **if `β ∈ k` then `α = 0` and `J ≡ 0`.**

`bp = bq = br = 0` is exactly `β ∈ k`. So on the residual stratum `f` and `g`
are both polynomials in `h` (`f = h²+2bs`, `g = h³+3bs·h`), the pair is
**composite**, and `J ≡ 0 ≠ c`. Two further facts make this robust:

* it is *chart-free*: for Moh's normal form `f = h² + B₂`, `g = h³ + A₂h + A₃`
  with `deg h ≥ 1`, expanding gives
  `J = h²[2J(h,A₂) − 3J(h,B₂)] + h[2J(h,A₃) + J(B₂,A₂)] − A₂J(h,B₂) + J(B₂,A₃)`,
  so `B₂ ∈ k ⇒ h | J ⇒ J` is not a nonzero constant. No chart, no order basis,
  no gauge is used — only the shape Moh prints on p. 209.
* it is *not* the trivial `α = 0` condition: the control `β = x² − y` has
  `α = 0` but `J ≠ 0`. The kill needs `β` constant, nothing weaker.

### 4.4 Verdict on case (A), typed

> **CONDITIONAL[CASE-A-DEAD].** Case (A) = `(27,18; M₂=21, V₂=8, δ₂=−1,
> δ₁=0; Jacobian X⁴)` admits no Keller pair **provided** every branch-A Keller
> pair's `B₂` lies in the four-dimensional span `⟨A, y, x, 1⟩` charted by
> `d2e3_ab_system`. Proof: if `B₂` is constant, §4.3 (unconditional); if not,
> §4.2's unit ideal (exact, Q, five localisations, controls).

The residual obligation is now a *single, bounded, named* one — and it is much
smaller than OPEN[FULL-ORDER-BASIS]:

> **OPEN[BRANCH-A-BETA-SPAN]** — decide whether the branch-A `B₂` (Moh's
> `γ*`, `deg γ* < deg h = 9`) is charted by `⟨A, y, x, 1⟩`, or rerun the
> chart with the full `deg_y B₂ < 9` coefficient space.
> *Bounded quantity:* the dimension of the necessary `B₂`-space (4 vs ≤ 9·(…)).
> *Cheapest test:* rebuild `d2e3_ab_system` with `β` a general polynomial of
> `y`-degree `< deg h` (adds ≤ 8 unknowns to a 14-unknown ring), rerun the
> five localisations. Singular, ~10 min including controls.

The direction of the logic is FALLACY-safe: deleting a row *enlarges* the
locus, so a unit ideal on the enlarged system still kills anything inside it,
and the `β ∈ k` half needs no chart. Not claimed: that the 28 rows are
necessary — that is OPEN[BRANCH-A-BETA-SPAN] plus the standing chart-necessity
obligation.

### 4.5 A second, necessity-clean instrument exists and should be preferred

`box/minor-residue-20260903/charts/moh1612_kill.sing` (Card B) kills the
`(16,12)` chart by a **direct Jacobian coefficient test**: build `f`, `g` from
Moh's explicit p. 208 tower, compute `J = f_x g_y − f_y g_x`, set every
non-constant coefficient to zero, localise at the constant with Rabinowitsch,
`dim −1 / GB 1 / reduce(1) = 0`, with `CTRL_RAW_DIM 11` and both degenerate
controls. That instrument **has no order-basis obligation at all** — it imposes only
"`J(f,g)` is a nonzero constant" on an explicit parametrisation, i.e. the
definition of a Keller pair, so it is immune to the `δ₁' = 0` / `−c` /
FULL-ORDER-BASIS pathology that has demoted three results (17(ggggg),
17(fffff), the case-(A) 17(tt)).

**Recommendation:** for every *small* terminal chart (case (A): 10
coefficients; the descended `(24,16; k=4)`; the `(25,15)` 4-tuple), run the
direct-Jacobian instrument first and the order chart second. This converts
OPEN[FULL-ORDER-BASIS] from a blocker into a cross-check for the cases where
the direct chart is small enough to write down.

### 4.6 N1 / N2 — the packet's hope is refuted for N2

Xu §8 read directly (`pdftotext`; §8 begins at line 1037 of the text layer):

* Xu's data (8.1) is `n = 99, m = 66, M₂ = 77, M₃ = 97, V₃ = 8, V₂ = 8,
  δ₂ = 1/3, δ₁ = 4/9`, `deg p(π) = u₃ = 3` — **independently confirming
  ERRATUM[9966-TUPLE-IN-17tttt]** from primary source (`M = (−66,77,97)`,
  `V = (8,8)`, `u₃ = 3`).
* Xu writes: "Our tools are two constrains: one is that **the denominator of
  order δ ≤ u_s = 3**; another is equation 7.1." The string `denominator`
  occurs **exactly twice** in the entire paper (lines 1060 and 1089) — both
  times *using* the constraint. **Xu neither proves nor cites it.**
* Xu also says of Moh's p. 209 trichotomy: "We can not find materials to
  support these claims in his paper", and reports emailing Moh in Jan 2016.
  He proves (ii) and (iii) and leaves (i) open at `δ = 5/2`.

Therefore:

> **REFUTED[N2-BY-SOURCE-READ].** `GAP[DEN(δ) ≤ u_s]` cannot be discharged by
> reading Xu §8 — Xu assumes it. And it is load-bearing: the campaign's
> *exhaustiveness* of `δ ∈ {2, 5/2}` (17(nnn)/(rrr)/(sss)) uses `den(δ) ≤ u_s`
> together with the ceiling `δ < v_s/u_s = 8/3`. Without it the configuration
> list is not finite and THEOREM 8.1 has no case analysis.

The only plausible source located: **Moh p. 188** (PDF page 49), the
conjugation block — "The conjugations of `k((t^A))` over `k((t))` show us that
if the reduced denominator `A` of `δ` is not a factor of `deg g_σ(π) = n*V₂`
then `π` is a factor of `g_σ(π)` … we must have `A | n*V₂` and `A ∤ m*V₂`, or
`A ∤ n*V₂` and `A | m*V₂`. Moreover we always have `A | (n*+m*)V₂ − 1`."
Three exact divisibility constraints on the reduced denominator.

> **OPEN[DEN-DELTA-FROM-MOH-P188]** — derive `den(δ) ≤ u_s` (or the weaker
> statement the exhaustiveness argument actually needs) from Moh p. 188's three
> divisibility constraints, or exhibit a skeleton where they permit
> `den(δ) > u_s`.
> *Bounded quantity:* the set of `A` admitted by `A | n*V₂ XOR A | m*V₂` and
> `A | (n*+m*)V₂ − 1` at the `(99,66)` minor level; decide whether it is
> `⊆ {1..u_s}`.
> *Cheapest test:* pin `n*, m*, V₂` at the level Moh's p. 188 induction is at
> (a half-page source read), then enumerate divisors — 30 lane-minutes,
> arithmetic only, no CAS.

N1 (`a Keller pair of degrees (99,66) has some census skeleton`) is untouched
by this and remains a genuine Moh §§5–6 read; I have no new evidence on it and
do not recommend spending the first lane there.

## 5. Q3 ((H1) theorem vs census) — there is one uniform route left, and it is arithmetic; plus the census is 129 + 48, not 177

### 5.1 Why disc was always the wrong candidate, and what shape the right one has

17(ooooo)'s refutation is structural, not incidental: a discriminant is a
*nondegeneracy* certificate, and nondegeneracy makes the interpolation block
**invertible**, hence its equations solvable. No discriminant can be the reason
a system is inconsistent. The right type is the opposite: a quantity *nonzero
exactly when an inhomogeneous row survives elimination*. One such object is
already in the ledger.

### 5.2 The ladder pivot is that object, and its non-vanishing is arithmetic

17(hhhhh) proved the closed form for the joint `Q*` pivots at (99,66),
**unifying both branches**:

```
|coeff| = 9·(99 − 3n − 11i),   1 ≤ n ≤ 8,   never 0 because 11 ∤ 3n.
```

Reading the constants against the gated skeleton `d = (99,33,11,1)`,
`V = (8,8)`, `u₃ = 3`: `9 = n/d_s`, `99 = n`, `3 = u_s`, `11 = d_s`, and the
band index runs `1 ≤ n ≤ v_s = 8`. So the closed form is

```
|coeff| = (n/d_s)·( n − u_s·j − d_s·i ),      1 ≤ j ≤ v_s,
```

and since `d_s | n` always (the divisor chain `d_1 = n`, `d_{i+1} | d_i`), the
vanishing condition collapses to `d_s | u_s·j`. Define the skeleton predicate

> **NONRES(S) :≡ `d_s ∤ u_s·j` for all `1 ≤ j ≤ v_s`.**

Because `u_s := d_s − V_s`, i.e. `d_s = u_s + v_s`, we have
`gcd(d_s, u_s) = gcd(u_s, v_s) =: g` and

```
NONRES(S)  ⟺  d_s/g > v_s  ⟺  u_s > (g−1)·v_s.       (asserted and checked
                                                       elementwise in the driver)
```

This is the type the missing (H1) theorem needs: a *coprimality* reason for an
elimination pivot never to die. It is the same shape as Fable's Lemma INJ
(kernel iff `d₃ | n`) and as the ladder law `c(p,k) = ±[eA(K−p) − n(k−k₀)]` —
three independent derivations pointing at one divisibility.

### 5.3 MEASURED: the whole `u_s > 1` census, stratified

`box/nonres-20260904/nonresonance_scan.py` (read-only; imports the frozen
`moh_skeleton_full` / `full_tree_partition` from
`box/anchor-gate-20260903/`), degrees `D = 48..200`, `Kmin = 16`, full
(1)–(13) census, POLY∧ODE filter. Banked controls reproduced **exactly**:
`POLY_ODE_rows = 1420`, `u_s>1 rows = 310`, `u_s>1 groups = 177`.

| | groups |
|---|---|
| `u_s > 1` groups total | **177** |
| NONRES holds | **129** |
| NONRES fails | **48** |
| distinct `(u_s, v_s)` cells | 19 |

Failing cells (all of them): `(u_s,v_s) = (2,4)×34, (2,6)×7, (2,8)×3,
(3,6)×1, (3,9)×1, (4,8)×1, (5,10)×1`. Two measured facts about the failure set:

* every failing cell has `u_s | v_s` — equivalently the Prop-6.1 minor ceiling
  `v_s/u_s` is an **integer**. On this census, `NONRES ⟺ gcd(u_s,v_s) = 1 ⟺
  v_s/u_s ∉ Z`. (Also measured: `u_s < v_s` in all 19 cells, so the Prop-6.1
  floor never suffices on this stratum — consistent with why it is the hard
  one.)
* every failing group has **`D ≥ 144`**: the resonant degrees are exactly
  `144` (11 groups), `180` (14), `192` (22), `200` (1). Verified at the live
  frontier: `(99,66)` `d=(99,33,11,1)`, `v_s=8`, `u_s=3`, `g=1` → NONRES;
  `D=108` `d=(108,36,9,1)`, `v_s=7`, `u_s=2`, `g=1` → NONRES; both `D=120`
  groups NONRES.

> **CLAIM[CENSUS-NONRESONANCE] (MEASURED, controls reproduced).** 129 of the
> 177 `u_s>1` census groups — and **all** groups of degree `< 144` — satisfy
> the (99,66) pivot non-vanishing condition as a pure skeleton predicate.

### 5.4 What this buys, and the honest limit

It does **not** prove MINOR-EMPTY. What it does:

* it identifies the *only* uniform theorem still standing and gives it a
  precise statement: **OPEN[LADDER-NONRESONANCE-ROW]** — "for every fully
  specified admissible `u_s ≥ 2` split datum with NONRES, the joint elimination
  reaches a Jacobian-band row whose pivot is `(n/d_s)(n − u_s j − d_s i)` with
  `1 ≤ j ≤ v_s`". The *non-vanishing* is then free (§5.2/5.3). Only the
  *existence and reachability* of the row is at issue — which is exactly the
  "uniform Schur/Fitting row" 17(ooooo) named, but now with its hard half
  (why is the residue nonzero?) already answered on 129/177 of the stratum;
* it prices the census honestly: the batch is **not** 177 undifferentiated
  groups. If the ladder row transfers, 129 groups close by one theorem and 48
  need a second argument — and those 48 are all at `D ≥ 144`, i.e. entirely
  outside everything the campaign is currently computing;
* it makes a falsifiable prediction: **`D = 108` and every `D < 144` client
  must die by a Jacobian-band pivot of the stated form.** `D = 108`'s split
  branch died at *stage 0 on incidence*, not on a Jacobian band (17(ddddd)) —
  so either the ladder row is present but not needed there, or the mechanism is
  not uniform. **Cheapest test:** re-run the `D = 108` δ=3 elimination without
  the incidence block and see whether a band pivot of the predicted shape
  `(n/d_s)(n − u_s j − d_s i) = 12·(108 − 2j − 9i)` appears. If it does, the
  ladder is uniform across a client that dies by another route — strong
  evidence. If no such row exists, OPEN[LADDER-NONRESONANCE-ROW] is refuted for
  free and the census is the only (H1) deliverable. ~40 lane-minutes on the
  banked `box/g108band-20260903/` driver.

### 5.5 Census or theorem? — answer

**Commit to the census, but run the ladder test first because it is cheap and
it re-prices the census.** Concretely: the honest (H1) deliverable is the
census (17(ooooo) is right), but a census of 177 groups with a corrected,
timing-out engine is not obviously finishable, whereas a census of 48 groups
plus one theorem is. The `D = 108` ladder test above decides which of those two
you are buying, in under an hour.

### 5.6 The minimal compute change for OPEN[FULL-BASIS-TIMEOUT]

Three, in increasing cost, all standard and none yet in the engine:

1. **Modular Gröbner + rational reconstruction + exact char-0 verification of
   the cofactors.** Today a "kill" over Q means running `std` over Q for
   1800 s. Instead: run `std` mod `p` (seconds), extract the representation
   `1 = Σ hᵢ gᵢ` mod `p` (`lift`), rationally reconstruct the `hᵢ`, then
   **verify `Σ hᵢ gᵢ = 1` exactly over Q by polynomial arithmetic**. The
   verification is a multiplication, not a Gröbner basis: milliseconds. A
   successful lift is a complete char-0 certificate; a failed lift costs one
   more prime. This is the single highest-leverage engineering change and it
   removes the "modular ≠ char 0" caveat that has qualified a dozen results.
2. **Stratify by the shape parameters before eliminating.** The case-(A)
   experiment (§4.2) is the template: the full system's content split into
   *a unit ideal on `{(bp,bq,br) ≠ 0}`* and *an 11-dimensional linear stratum
   handled by one line of mathematics*. Both pieces are sub-second; the
   undivided system was worthless. Concretely: for each chart, localise
   successively at the leading/shape parameters, and treat the complementary
   strata by hand. Expected gain: the timing-out systems are timing out on the
   *degenerate* strata, which are exactly the ones where a structural argument
   is available.
3. Only then: better term orders / `degrevlex` + FGLM, or targeted
   saturation — the usual last resorts, not before (1) and (2).

## 6. Q4 (the finish) — the framing is wrong in one specific place, and today's work found the missing configuration

### 6.1 Right as a statement, wrong as a plan

`(H1) ∧ (H2)` is a genuine dichotomy — a skeleton either carries a split of
the principal minor roots or it does not — and I do not reopen the Q4
trichotomy the 00:00Z round buried. But (H2) is two different things and only
one of them has an engine.

The packet defines (H2) as "`u_s = 1`, **or** `u_s ≥ 2 without a split`" and
assigns it one engine: "a source-licensed descent (Prop 6.3/6.4) lands it in a
monomial-Jacobian order chart of lower degree". But Prop 6.3 is sourced at
`u_s = 1` — 17(iiiii) says so explicitly ("Moh's `(16,12)` is the Prop 6.3
descent of `(64,48)` with `u_s = 1`"), and the `D = 108` no-split descent was
banked CONDITIONAL precisely because the descended `(γ,π)` pair "is NOT
identified with the ordinary total-degree two-point chart" (17(fffff)).

The `u_s ≥ 2`-unsplit class is **not** a Prop 6.3 client. Case (A) shows what
it is instead: Moh transforms `(99,66)` case (A) to `(27,18)`, and
`27 = (n/d_s)·u_s = 9·3`, `18 = (m/d_s)·u_s = 6·3` — this is the **minor**
reduction (Prop 6.1 read with `V_r = u_s`), not the `u_s = 1` descent. Different
map, different license, different receiver.

> **FRAMING CORRECTION.** The program is really a **trichotomy of engines**:
> **(H1)** `u_s ≥ 2` split → joint two-point system inconsistent;
> **(H2a)** `u_s = 1` → Prop 6.3/6.4 descent to a monomial-Jacobian order
> chart (sourced; one worked instance, `(16,12)`);
> **(H3)** `u_s ≥ 2` unsplit → minor reduction by `u_s` to
> `((n/d_s)u_s, (m/d_s)u_s)` (**no sourced license, and until today zero
> worked instances**).
> Calling (H3) a sub-case of (H2) hides that its engine does not exist.

This matters at scale: **every one of the 177 `u_s > 1` census groups admits
the unsplit configuration a priori** — "`g_σ` is a power of a linear
polynomial" is always formally possible. So the (H1) census, even if completed,
closes only the *split* configurations and leaves an (H3) obligation at every
group. The (99,66) headline needed a QUALIFICATION the day after promotion for
exactly this reason. If (H3) has no engine, the two-half program is a reduction
of the split half, not of plane JC2.

The good news is §4: (H3)'s first instance closes, and it closes by a
*composite/functional-dependence* argument (`f, g ∈ k[h] ⇒ J ≡ 0`), not by a
descent. That suggests the (H3) engine is not a descent at all but a
**Ritt/composite-locus** argument — which is why I reopen row 43. Conjecturally
(and this is the shape I would try next): *in the unsplit configuration the
minor reduction forces the low tower coefficient `B₂` into a space so small
that either `B₂` is constant (composite, `J ≡ 0`) or a bounded coefficient
system is inconsistent.* Case (A) is exactly that dichotomy, made explicit.

### 6.3 The single most valuable next object

**The unsplit-configuration lemma, stated uniformly.** Not case (A) alone —
case (A) is the instance that makes it concrete and it is the first lane
(§8) — but the statement:

> for a `u_s ≥ 2` skeleton in the unsplit configuration, with minor reduction
> to `(n', m') = ((n/d_s)u_s, (m/d_s)u_s)` and `(deg_h g, deg_h f) = (e', q')`,
> the low coefficient `B₂` is either constant — in which case `h | J` and the
> pair is composite — or lies in an explicitly bounded space on which the
> Jacobian coefficient system is inconsistent.

It is the only object that is *load-bearing for the banked flagship*, it is
the missing third engine (§6.2), it has one worked instance as of today, and
its hard half is a Jacobian identity rather than a Gröbner basis — so it does
not compete for the exhausted compute budget.

Second place: OPEN[LADDER-NONRESONANCE-ROW] (§5), because its cheapest test is
under an hour and its outcome re-prices the entire (H1) census.

## 7. Three idea cards

### Card A — `caseA-unsplit-kill` (NEW; depends on nothing running)

*Target obstruction.* The QUALIFICATION on 17(tttt): case (A) `(27,18; δ₁=0)`
open, so the flagship (99,66) verdict covers only configurations B and C.

*Mechanism.* Two-branch dichotomy on `B₂` (§4.3 + §4.2), plus the
necessity-clean direct-Jacobian instrument (§4.5) as the independent gate.

*Cheapest discriminator.* (i) Rebuild `d2e3_ab_system` for the `(27,18)` row
with `β` a **general** polynomial of `y`-degree `< deg h` instead of
`⟨A,y,x,1⟩`; rerun the five localisations `{bp…}→{all β-coefficients not all
zero}`. (ii) Independently, port `moh1612_kill.sing` to `(27,18)`: `h` of
degree 9 with Moh's p. 209 top form, `f = h² + B₂`, `g = h³ + A₂h + A₃`,
`J = f_xg_y − f_yg_x`, all non-constant coefficients `= 0`, Rabinowitsch on the
constant. Gate: `dim −1`, `GB = 1`, `reduce(1) = 0`, plus
`CTRL_RAW_DIM > 0`, `CTRL_UNIT = −1`, `CTRL_ORIGIN = 0`, plus a positive
control (a tame automorphism of the right degrees must survive).

*Interpretation.* Both empty → **CONFIRMED[CASE-A-DEAD]**, the QUALIFICATION
lifts, and the (99,66) skeleton verdict is unqualified (still conditional on
N1/N2). (i) empty, (ii) not → the chart is over-restricted; report the gap.
(ii) not empty → case (A) survives the necessity-clean test: the first positive
signal in the program, and the headline stays restricted to B and C.

*Stop condition.* 90 minutes, or the direct chart exceeding 25 unknowns.

*Expected information gain.* High and asymmetric — it closes the flagship scope
hole or produces the campaign's first survivor.

### Card B — `k16-fitting-rank` (NEW; converges with the running hsop lane)

*Target obstruction.* OPEN[K16-HSOP-LENGTH] / OPEN[B4-GLOBAL] at `t = 7, 8`;
fixed-`t` Gröbner exhausted (17(mmmmm), 17(kkkkk)).

*Mechanism.* §3.3: `dim 0 ⟺ I₂(M)` `m`-primary for the explicit
`2 × (2t−2)` matrix over `B`; then prove maximal rank off the origin by a
weight degeneration of `M` (semicontinuity), not of the tail.

*Cheapest discriminator.* Build `M` at `t = 3,4,5` by dividing `Q_1..Q_{t−1}`
by the unit-leading quadratic `Q₀` (no Gröbner); check `I₂(M)` is `m`-primary
and that `deg V(R)/deg V(I₂(M)) = 2^{t−2}`; negative control `t = 2, y = 1/5`
must fail. Then search weight vectors `w` on `B` (a `t−1`-dimensional
polytope, tiny) for one with `in_w` already `m`-primary.

*Interpretation.* `m`-primary at `t = 3,4,5` plus a uniform `w` → an all-`t`
proof by degeneration. No uniform `w` → the object is still right and
`t = 7, 8` may now be in budget. Not `m`-primary where the tail is `dim 0` →
my reduction is wrong; report and stop.

*Stop condition.* 60 minutes; abandon if TOPTAIL's `a₀ = α_t` is
fibre-dependent (then `Q₀` is not unit-leading).

*Expected information gain.* Medium-high: the only Gröbner-free proof shape
proposed for the all-`t` statement.

### Card C — `ladder-row-transfer` (NEW; decides the (H1) census price)

*Target obstruction.* OPEN[UNIVERSAL-MINOR-EMPTY-DISCRIMINANT] is refuted;
17(ooooo) leaves "the uniform Schur/Fitting row" unproved and unnamed.

*Mechanism.* §5.2: name it as the Jacobian-band ladder row with pivot
`(n/d_s)(n − u_s j − d_s i)`, whose non-vanishing is the coprimality
`d_s ∤ u_s j` — measured to hold on 129/177 groups and on every group of
degree `< 144`.

*Cheapest discriminator.* Re-run the `D = 108` `δ = 3` elimination with the
common-`h₃` incidence block **removed** (`box/g108band-20260903/`), and look
for a Jacobian-band pivot of the predicted shape `12·(108 − 2j − 9i)`,
`1 ≤ j ≤ 7`. Positive control: the same search at (99,66) must return the
banked `9·(99 − 3n − 11i)` ladder.

*Interpretation.* Row present at a client that dies by another route → the
ladder is uniform; escalate to proving its existence and the census drops to
the 48 resonant groups. Absent → the ladder is (99,66)-specific, the OPEN
closes negative, and the campaign commits to the full 177-group census with no
theorem route.

*Stop condition.* 45 minutes / 1800 s cap.

*Expected information gain.* High per minute; the negative outcome is as
valuable as the positive.

## 8. The single first lane

**`caseA-unsplit-kill` (Card A).** It is the only item that is simultaneously
(a) load-bearing for a *banked* headline, (b) already 80% done inside this
submission (the `β ∈ k` branch is unconditional; the other branch is a
unit ideal in the banked chart), (c) the first instance of the missing third
engine (§6.2), and (d) cheap — sub-second Singular runs on a ≤ 22-unknown
ring. Owner: any lane with Singular; the two scripts to start from are
`box/caseA-20260904/branch_A_loc_br.sing` and
`box/minor-residue-20260903/charts/moh1612_kill.sing`.

Runner-up, if two lanes are available: Card C (`ladder-row-transfer`), because
its outcome re-prices the whole (H1) census before anyone commits a week to it.

## 9. Running lane — `k16-hsop-length-allt-opus5` (receipt only)

Receipt at the time §§1–8 were written:
`initial_status=RUNNING`, **no `final_status`** → still running; `.md` not
opened, box dir not read. **Post-hoc, at seal time:** the collision scan
(§12, run last) returned a hit that revealed the lane sealed at 12:03:36Z
(`final_status=DONE`) with `CRITERION RANK`, an `(t−1)×2` matrix rank
criterion. I have **not** opened its report; I record only what the scanner
printed, because the convergence is evidence: §3.3 was derived blind and
independently arrives at a rank criterion on essentially the same matrix (mine
carries the extra `b₃·Q_r` columns, which is what encodes their "kernel with
nonzero first coordinate" clause as a determinantal condition, and is why my
version is a single Fitting ideal rather than a two-clause criterion). Two
independent derivations landing on the rank of that matrix is the strongest
signal in this round that it is the right object. My recommendation as
written stands as a *harvest gate* rather than a lane instruction:

> **REDESIGN (do not stop) — as written blind; now: CONTINUE the successor.**
> Its stated target, "the hsop/complete-intersection **length** identity
> `L_t = 2·binom(3t+1,t−1)` proved combinatorially", is a tautology given
> `dim 0` (§3.1): the length is the weighted Bézout number `∏(2t+2..3t+1) /
> ((t−1)!(t+1))` and equals it *iff* the rows are an hsop. So if the lane
> returns "length identity proved" without an independent `dim 0` argument, the
> result is vacuous and must be typed so at harvest. **Redesign at the next
> launch** onto `I₂(M)` (Card B), and at harvest apply this gate: *does the
> report prove `V(tail) = {0}`, or only that the CI length would be `L_t`?*
> Only the former is a result.

This is a recommendation about the *target*, made without reading the lane's
findings. On the scanner's evidence the gate passes: the lane reports an
exact `⟺` reduction, not a length identity.

## 10. Systems upgrade (one; independent of the mathematical proposals)

Rotation slot: **reproducibility / claim propagation.**

> **UPGRADE[INSTRUMENT-FAIL SENTINEL].** Add to the chart emitters (and to
> `box/preflight.py` as a hard gate) a check that fails closed when an emitted
> ideal contains a **standalone generator in the localised variable** — i.e.
> when some generator `g` and the Rabinowitsch generator `T·g − 1` are both in
> the ideal, or more generally when a single generator divides the localiser.
> Such a system is `(1)` for a reason that carries no mathematical content.

Smallest useful test: run the sentinel over the banked `box/*/systems/*.sing`
corpus and count hits. I ran the manual version of exactly this check today and
it found the `−c` row in `branch_A_linear_AB_Q.sing` on sight (§4.2). Three
banked results have already been demoted for this single defect — 17(ggggg)
((25,15)), 17(fffff) (`D = 108` no-split), and the case-(A) QUALIFICATION — at
a cost of roughly two lane-days of downstream work each. The check is ten lines
and it would have fired on all three at emission time. Expected benefit:
prevents the recurrence of the campaign's most expensive class of error;
regression risk: nil (fails closed only on ideals that are already vacuous).

## 11. Ledger note (not an OPEN)

At harvest, retype the length half of the K16 hsop-length ledger entry: it is a
tautology (§3.1), so the live content of that entry is `dim 0` / Z-EMPTY.

## OPENS RAISED (each with its bounded quantity and cheapest test)

1. **OPEN[BRANCH-A-BETA-SPAN]** — QUANTITY: the dimension of the necessary
   `B₂`-space for the `(27,18)` branch-A chart (charted 4 = `⟨A,y,x,1⟩`, vs
   the source bound `deg_y B₂ < deg h = 9`); decide whether the charted span is
   an over-approximation. CHEAPEST TEST: rebuild `d2e3_ab_system` with general
   `β`, rerun the five localisations; Singular, ~10 min incl. controls.
2. **OPEN[DEN-DELTA-FROM-MOH-P188]** — QUANTITY: decide whether Moh p. 188's
   constraints (`A | n*V₂` XOR `A | m*V₂`, and `A | (n*+m*)V₂ − 1`) bound the
   reduced denominator `A` of `δ` by `u_s`. CHEAPEST TEST: pin `n*, m*, V₂` at
   the level of Moh's p. 188 induction (half-page source read), enumerate the
   admitted divisors at the (99,66) minor level; arithmetic only, ~30 min.
3. **OPEN[LADDER-NONRESONANCE-ROW]** — QUANTITY: decide whether every fully
   specified admissible `u_s ≥ 2` split datum's joint elimination contains a
   Jacobian-band row with pivot `(n/d_s)(n − u_s j − d_s i)`, `1 ≤ j ≤ v_s`.
   CHEAPEST TEST: Card C — re-run `D = 108` `δ=3` without the incidence block
   and search for `12·(108 − 2j − 9i)`; `box/g108band-20260903/`, ~45 min.
4. **OPEN[K16-FITTING-RANK]** — QUANTITY: decide whether `I₂(M)` is
   `m`-primary in `B` (`t−1` variables) for all `t ≥ 3`, equivalently whether
   the `2 × (2t−2)` matrix `M` has rank 2 off the origin. CHEAPEST TEST: build
   `M` by division at `t = 3,4,5` (no Gröbner), test `dim 0` and the
   `2^{t−2}` degree ratio; ~25 min.
5. **OPEN[H3-UNSPLIT-ENGINE]** — QUANTITY: exhibit (or refute) a uniform
   license for the minor reduction `((n/d_s)u_s, (m/d_s)u_s)` in the
   `u_s ≥ 2`-unsplit configuration, and bound the resulting low-coefficient
   space `B₂`. CHEAPEST TEST: replay the reduction on a second unsplit
   configuration — the `D = 108` skeleton (`d_s = 9`, `u_s = 2` →
   `(24, 16)`) — and check whether Moh's p. 209 method reproduces the same
   `f = h^{q'} + B₂` shape; source read + sympy, ~40 min.

## 12. Collision scan

`ops/open_collision.py` (round/receipt-guarded, 94af4672) run on this report
before sealing; exit 0, block reproduced verbatim below. The single hit is a
*convergence*, not a closure: it is the `k16-hsop-length-allt-opus5` seal that
landed at 12:03:36Z while this submission was being written (see §9).

## COLLISIONS

status: CANDIDATES

- `OPEN[BRANCH-A-BETA-SPAN]` (report:774): NONE

- `OPEN[DEN-DELTA-FROM-MOH-P188]` (report:779): NONE

- `OPEN[LADDER-NONRESONANCE-ROW]` (report:784): NONE

### OPEN[K16-FITTING-RANK]

- `AUDIT.md:17730` — - CRITERION RANK (EXACT iff, the reduction): with N the (t−1)×2 matrix of rows (C_r, B_r), V(J_t^tail) = {0} ⟺ (i) V(B_1..B_{t−1}, C_1..C_{t−1}) = {0} AND (ii) every p ≠ 0 with rank N(p) = 1 whose kernel has nonzero first coordinate has ...
- `notes.md:21060` — ## 2026-09-04T12:05Z EVENT — `k16-hsop-length-allt-opus5` sealed (40KB): MAJOR structural reduction. K16 (V0)-for-all-t ⟺ CRITERION RANK: (i) the b₃-coefficients B_r,C_r have no common zero AND (ii) a non-vanishing of the eliminants W_r ...

- `OPEN[H3-UNSPLIT-ENGINE]` (report:794): NONE

## 13. Artifacts banked with this submission

* `box/nonres-20260904/nonresonance_scan.py`, `.log` — §5.3; read-only,
  imports the frozen census modules from `box/anchor-gate-20260903/`;
  reproduces the banked controls 1420 / 310 / 177.
* `box/caseA-20260904/` — §4.2/4.3: `branch_A_drop_minusc_Q.sing`,
  `branch_A_radical_Q.sing`, `branch_A_loc_{bp,bq,br,bpbqbr,c_and_br}.sing`,
  the matching `.out` files, and `artifacts.sha256`. All char 0, all
  sub-second, all with the four controls printed.
* Source reads (no artifact): Moh p. 209 (PDF 70) and p. 188 (PDF 49);
  Xu §8 (text layer, lines 1037–1110).

No canonical ledger was edited; `jc2-lean` was not inspected; no lane report of
this round was read.

<!-- BODY-END -->
