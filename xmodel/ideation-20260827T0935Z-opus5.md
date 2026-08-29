# Blind whole-portfolio ideation — Opus 5 — round `20260827T0935Z`

Date: 2026-08-27
Author: Opus 5, blind whole-portfolio ideator
Status: **BLIND SUBMISSION. NO CANONICAL LEDGER EDITED. NO AWS LAUNCHED. NO
HEAVY LOCAL ALGEBRA RUN. `jc2-lean` NOT INSPECTED OR TOUCHED.**

## 0. Custody, what I read, and what I actually executed

Verified by recomputation before reading:

```text
e871e3d71a8777ca50f7c796bf7547023a8c2ca8e2930c6a0981ddcebd6ae3db  xmodel/ideation-20260827T0935Z-packet.md
92006f6d7222a5b78f279de34d94e3e6859f2b018a7de47af54f633df229700a  APPROACHES.md
b6c8158e87e787736c6ae0fb1232b0f082236c4a91a8420d9efe9eb4129f1655  AUDIT.md
15d7ed1075317c8feaa8e278d60ada668f97ec7cc6616fe81235c9c3d20dceae  PROGRESS.md
72d789d3f7fbceff5f20b45e61799d4372869c9796f74b85bbf14fa99de1054e  COORDINATION.md
7345d4a8dda7afd9f45dd6b938a5ec0e15ff642e4809da5434ef35eb505f446d  xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-sol-20260827.md
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
8867c66a8e436107d059269e18347ef8ef01bbf8fdaa44ccec6b58fcef874944  xmodel/max12-812-order2-gate-t-strict-uac-uniform-transport-design-grok-20260827.md
```

Also read: the full 46-row master union table and consensus/dissent sections of
`APPROACHES.md` plus every overlay back to the 2026-08-23 canonical correction;
the newest `AUDIT.md` promotions; the 2026-08-27 `PROGRESS.md` day; all of
`COORDINATION.md`; `ladder/REDUCTION.md` executive verdict, `G2` terminology
correction, and gap headings; `xmodel/ideation-20260827T0635Z-synthesis-sol.md`;
`xmodel/websweep-20260826T2355Z.md`;
`xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-sol-20260827.md`
(`e3d263d5…`, the DVR criterion, including its §3 toy counterexample);
`xmodel/max12-812-order2-k00-d8-hostile-review-prompt-20260827.md`;
and the live source of
`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dehom_eliminant_v43.py`
and `…/compile_total_dvr_w30_v43.py`.

Executed (desk scale only, exact integer arithmetic in stock Python; no
Singular, no msolve, no FLINT, no AWS):

1. SHA-256 of every artifact above.
2. Exact factorization of the V43 dual denominator
   `34670334774018800828908752076800000
   = 2^23·3^11·5^5·7^5·11·19^2·23^2·37·59·157·617`.
   All factors are ordinary elimination-pivot primes; **neither selector prime
   65519 nor 65521 divides it**, so both finite-field lanes are lucky for the
   certificate denominator. The V43 report does not state this; it is a small
   independent consistency check in the producer's favour.
3. Census arithmetic: `66,076 − 1 = 66,075` matches the reported dual-unknown
   count after `Lambda(a1^6)=1`.
4. A scope census of every registered `T-a1` case directory
   (`cases/max12_812_order2_p0_total_rees_j2_a1_*`): **14 lanes, and every one
   of them is `rho=0`-scoped**, confirmed from the preregistration text of
   V28, V30, V31, V32, V33, V34, V35, V36, V37, V38, V39 and from the V43
   compiler source. No lane in the campaign has ever computed the
   general-`rho` (generic-fibre) object.

Everything mathematical below is hand algebra over frozen, already-promoted
statements. I ran no membership, rank, or Gröbner computation. Where I say a
statement is *proved*, I mean proved here by the displayed argument from
promoted inputs; where I say *predicted*, I mean unverified.

---

## 0.1 Executive summary — the one structural finding

Three of the campaign's most expensive lanes are the **same instrument**: a
monotone ladder over a filtration index, funded rung by rung, with no
termination theorem.

```text
T-a1   : exponent ladder    a1^N in J0 ,   N = 6, 7, 8, ...
K00    : (d)-adic ladder    r7 in I+(d)^n , n = 8, 9, 10, ...
AS109  : degree ladder      deg_y Q >= 2, >= 6, >= 12, ...
```

A ladder of this shape is a **decision procedure only on its negative
branch**. Its positive branch is semi-decidable and never confirmed. Two of
the three are worse than that:

- The `T-a1` exponent ladder is **guaranteed** to reach its uninformative
  positive branch, because `a1 ∈ √J0` is already promoted twice over (V42, and
  the 17-row `rho=0,a1=1` unit Gröbner basis). Every remaining rung buys at
  most one bit, there are at most `N0 − 6` bits available for an unknown `N0`,
  and the last rung buys zero.
- The `K00` `(d)`-adic ladder terminates **iff** local nonmembership holds at
  the origin. D7 and D8 both returned compatible. If local membership holds,
  D9, D10, … are all guaranteed compatible and the "first filtered obstruction
  degree" *does not exist*.

For the first two I can replace the ladder with a **single closure-escape
test**, by an elementary lemma the campaign has not applied to these objects.
For `T-a1` this collapses the entire remaining question to one Gröbner basis
whose `rho=0` twin **already runs and already passes as a control inside the
existing V43 eliminant compiler**. That is the highest expected-information-
per-unit-time item I found, by a wide margin.

I also found one concrete fail-open software defect (§6.2) and one attractive
cross-avenue bridge that I built and then **refuted myself** (§4.2), which I
report because the refutation is the useful part.

---

## 1. Disposition vector over the numbered avenue inventory

`unchanged` unless a reason is given. Six changes out of 46; I have
deliberately resisted label inflation, because a disposition vector whose
entries mostly move is not information.

| # | Avenue | Disposition | Reason (only where changed) |
|--:|---|---|---|
| 1 | GGV corner farm / degree farm | unchanged | |
| 2 | Sheet ladder / Eggers–Wall / Sigray | unchanged | |
| 3 | Vertex-gap / strip ODEs / `R_{k,d2}` | unchanged | |
| 4 | Formal-germ certification, D-series | unchanged | |
| 5 | Jung–van der Kulk degree descent | unchanged | |
| 6 | Abhyankar–Moh / one-place | unchanged | |
| 7 | Nonproperness / Jelonek `A(F)` | **raise** | The sweep's Jelonek result (bounded-degree automorphism locus Zariski **closed**, plus a component dichotomy) is the first external result in the ledger that changes the *search* calculus rather than a special class. Closedness makes the counterexample locus **open**, hence dense in whichever component it meets. That is a structural statement about the campaign's own bounded-degree world and nobody owns it. See §4.1. |
| 8 | Formal-inverse combinatorics (BCW tree) | unchanged | |
| 9 | Lee–Li Conjecture E | unchanged | |
| 10 | HC4 ⇒ JC2 | unchanged | `NO LEVERAGE` stands. |
| 11 | Mathieu / GMC / Zhao ladder | unchanged | refuted |
| 12 | Face isolation / p-adic multinomials | unchanged | |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | `End(A_1)` / Zheglov audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged | |
| 17 | BCW / Druzkowski / Yagzhev | unchanged | |
| 18 | Graded / equivariant / GIT symmetry | **reopen (structural input only, not a CE hunt)** | Shaska closes it as a counterexample class, and that closure stays. But every campaign chart system is `sigma`-weighted-homogeneous by construction, so every campaign solution generates a `G_m` orbit whose `t→0` limit is a graded datum. Shaska then says that limit is an automorphism. That is a usable *structural* fact — it is exactly the piece that pairs with row 7 — and it is currently filed only under "closed". Reopen with the tight scope "limit/degeneration lemma", not "search for a graded CE". |
| 19 | Char-p CEs + Witt lifting (AS109) | **lower (rank on critical path; no theorem withdrawn)** | The `deg_y` floor sequence 2 → 6 → 12 is an unbounded floor-raising ladder with no termination theorem, and the campaign's own avenue-19 note already says every fixed simultaneous map/gauge cap eventually fails. Every promoted AS109 statement stands; what should drop is its share of critical-path capacity relative to the two lanes where a one-shot decision now exists. Fund it capped and explicitly labelled as buying negative information only. |
| 20 | Reduction mod p / p-curvature | unchanged | |
| 21 | p-adic injectivity / Hensel | unchanged | |
| 22 | Diophantine integral points / heights | unchanged | |
| 23 | Analytic global inverse | unchanged | |
| 24 | Real JC / Pinchuk | unchanged | |
| 25 | Fiber monodromy / passports | unchanged | |
| 26 | Primitive-monodromy `td` bound | unchanged | |
| 27 | Links at infinity / splice diagrams | unchanged | |
| 28 | Log surfaces / BMY | unchanged | |
| 29 | LND / Hamiltonian completeness | unchanged | |
| 30 | Affine-surface classification / ML | unchanged | |
| 31 | Integrality / ZMT / **Rees valuations** | **raise (narrow, opportunistic)** | S16's proposed experiment ("Rees valuations of one complete boundary book") was scored 6 when the campaign had no Rees machinery. It now builds, freezes, and saturates Rees algebras and their standard charts every day. The experiment's cost has collapsed while its score was never revisited. This is an unforced synergy, not a new idea. |
| 32 | Off-diagonal collision ideal | unchanged | |
| 33 | Global symplectic / action residues | unchanged | `COSTUME` stands. |
| 34 | 2D tangent-sweep / pole removal | unchanged | |
| 35 | Descent of dim ≥ 3 CEs | unchanged | |
| 36 | Guided CE search / sparse supports | **raise** | Its recorded low rank rests on "above the cutoff CEs form a thin locus". If Jelonek's closedness is as summarized, that premise is **false**: the CE locus is open, hence dense in its component, hence a *generic* point of that component. The correct target then becomes component enumeration of `K_D`, not random sampling — a different and much better-posed problem. See §4.1, including its limits. |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical geometry | unchanged | |
| 39 | Cohomological cluster | unchanged | |
| 40 | Free-associative / NC Jacobian | unchanged | |
| 41 | Naive scaling deformation | **reopen (lemma-only; still dead as a route)** | The row's content — `F_t = t^{-1}F(tx)` degenerates to the linear part — is now load-bearing input for §4.1/§4.2 and is the exact reason my own `G_m`-purity bridge in §4.2 is **false**. It should be retrievable as a lemma rather than filed as a dead end, precisely so the next ideator does not rebuild the bad bridge. |
| 42 | Markus–Yamabe | unchanged | |
| 43 | Ritt decomposition | unchanged | |
| 44 | Moskowicz "no prime td" | unchanged | Closed as proof input; the repaired membership theorem is already carrying the AS109 floor. |
| 45 | Differential Galois / Liouvillian | unchanged | |
| 46 | Lean / AI formal certification | unchanged | Not inspected this round by instruction. |

---

## 2. Reranked bottlenecks

### 2.1 Proof side

| Rank | Bottleneck | Change | Why |
|--:|---|---|---|
| 1 | **Generic-`rho` fibre of the ordered `T-a1` frozen system on `D(a1)`** | **new #1** | §3 proves this single question decides `K+(rho)=(1)` outright, given the already-promoted `rho=0` half. It was previously mis-stated as "which exponent `N`". Cost: one Gröbner basis. |
| 2 | **K00 local membership at the origin** | up from "one of three parallel obligations" | §5.2 reduces it to one 6-variable colon ideal, and its answer also decides whether the `(d)`-adic ladder can ever terminate. |
| 3 | Source/landing coverage outside strict unique-`AC` | unchanged (structurally #1) | Still the largest hole, and still the one with **no decisive instrument at all**. Everything else on this list is instrumented. |
| 4 | Terminal/Taylor receiver and the collision-to-`[6,2]` pullback | unchanged | Blocked on a map that does not exist, not on compute. `H_K00` is the right discriminator. |
| 5 | `G2-PSC` | unchanged | Untouched for weeks. Not currently attackable. |
| 6 | **Cofinal degree/type control (absolute `td`/degree ceiling)** | **up** | Even a perfect landing theorem leaves `REDUCTION.md` gap CRITICAL 7 intact. No lane targets it. It is the only gap on this list that is *fatal to the architecture* rather than to a chart. |
| 7 | Ramified `rho=0` deck/square fibre; six staged Rees charts | unchanged | Note that §3's decision and the naturality interface of §6.3 both live on `D(rho)` and are **orthogonal** to this. |

### 2.2 Counterexample side

| Rank | Bottleneck | Why |
|--:|---|---|
| 1 | AS109 has no termination theorem in either direction | Floors rise; no ceiling, no construction. This is the defining symptom of a necessary-condition mill and it is now the *third* one in the portfolio. |
| 2 | Nobody constructs `A(F)` for the campaign's own objects | Avenue 7's obstruction ("computing `A(F)` is the compactification problem again") is stated for arbitrary Keller pairs. The campaign now has explicit frozen chart systems; `A(F)` for *those* is not the same problem. Unowned. |
| 3 | The char-p tower's limit is restricted-analytic, and neither polynomiality nor its negation is instrumented | Both directions stalled at the same place. |
| 4 | Component structure of `K_D` unknown | This is what makes §4.1 currently unusable, and it is the cheapest thing to change on this side. |
| 5 | **No obstruction-witness lane anywhere in the portfolio** | Every live lane tries to prove emptiness. Not one is trying to *build* a surviving point of a live chart and see what it is. §5.3 argues the same Card-A run supplies one for free. |

---

## 3. New mechanism, and the theorem that decides `T-a1`

### 3.1 The Escape Lemma

Elementary and standard; the novelty claimed is only its application here.

> **Escape Lemma.** Let `R` be Noetherian, `I ⊆ R` an ideal, `f ∈ R`, `m ⊂ R`
> maximal, `A = R_m`. Then
>
> ```text
> f in I·A   <=>   (I : f) not contained in m   <=>   (I : f) + m = (1).
> ```
>
> Moreover, since every ideal of a Noetherian local ring is `m`-adically closed
> (Krull), `f in I + m^n for all n  <=>  f in I·A`.

**Corollary (ladder hygiene).** A monotone ladder testing `f ∈ I + m^n`
terminates **iff** `f ∉ I·A`. If `f ∈ I·A` the ladder is infinite and every
rung reports "compatible" forever. Therefore: *a filtration ladder is a
decision procedure only for its negative branch.* Never fund a ladder whose
positive branch is the hypothesis you are trying to establish, without either
a termination proof or an escape reformulation in hand.

### 3.2 Theorem (`T-a1`): the exponent is irrelevant; the generic fibre decides

Notation exactly as in the promoted design `e3d263d5…` and its erratum
`d322d417…`. `S = Q[rho, X]`, all `x ∈ X` of positive `sigma` weight,
`wt(rho)=0`; `J ⊆ S` the frozen ordered-`a1` rows; `K = J : a1^infinity`;
`sp : rho ↦ 0`; `J0 = sp(J)`; `wt(a1) = 5`. Write `D = Q[rho]_(rho)` and
`E = K ∩ Q[rho]`, the `sigma`-weight-zero part of `K`.

> **Theorem A.**
>
> 1. `K + (rho) = (1)`  ⟺  `E ⊄ (rho)`  ⟺  `a1 ∈ √(J·D[X])`.
> 2. **Given `a1 ∈ √J0`** (promoted: V42 `5d4c42ff…` / review `a4f6b931…`, and
>    independently the 17-row `rho=0,a1=1` unit Gröbner basis),
>
>    ```text
>    K + (rho) = (1)   <=>   E != 0   <=>   a1 in sqrt( J (x) Q(rho)[X] ),
>    ```
>
>    i.e. **the frozen system has no point with `a1 != 0` over an algebraic
>    closure of `Q(rho)`.** No exponent `N` appears anywhere in the criterion.

*Proof.* (1) `K` is `sigma`-homogeneous and `rho` is the only weight-zero
variable, so taking weight-zero parts, `K+(rho)=(1)` iff some `U ∈ E` has
`U(0) != 0`, iff `E ⊄ (rho)`. Clearing denominators identifies
`a1^N U(rho) ∈ J` with `U(0) != 0` and `a1^N ∈ J·D[X]`; this is exactly the
promoted equivalence (2)⇔(3) of `e3d263d5…`, restated as a localization.

(2) Let `Y = V(K) = closure(V(J) ∩ D(a1))`, and let `C` be any irreducible
component of `Y`. Because `J` is homogeneous, `K` and every `C` are
`sigma`-cones, and `C = closure(C ∩ V(J) ∩ D(a1))`, so **`a1` does not vanish
identically on `C`**.

`E != 0` says the `rho`-image of `Y` is not dense in `A^1`, hence (each `C`
irreducible) `rho` is *constant* on each `C`, say `C ⊆ {rho = rho_C}`.
Now `K+(rho) != (1)` would mean `Y ∩ {rho=0} != ∅`, i.e. some `rho_C = 0`,
i.e. `C ⊆ V(J) ∩ {rho=0} = V(J0)`. But `a1 ∈ √J0` makes `a1` vanish on all of
`V(J0)`, hence on `C` — contradicting the previous paragraph. So
`E != 0 ⟹ K+(rho)=(1)`. The converse is immediate from (1). Finally
`E != 0` iff the closure of `V(J) ∩ D(a1)` misses the generic point of the
`rho`-line, i.e. iff the generic fibre is empty on `D(a1)`. ∎

Everything above holds verbatim with `t = rho^2` and `m = (t)`, which is the
ring the V43 compilers actually build (`total_to_t`), because `t` also has
`sigma` weight zero and the rows are even.

### 3.3 Consistency with the campaign's own toy counterexample

The design's §3 toy is `S = Q[rho,f,x]`, `J = (f − rho^2 x)`, `wt(f)=wt(x)=1`.
There `f ∈ J0 = (f)`, so the `rho=0` half holds, yet no certificate exists.
Theorem A predicts exactly this: over `Q(rho)` the variety `{f = rho^2 x}`
contains `(f,x) = (rho^2, 1)` with `f != 0`, so the generic fibre is
**nonempty** on `D(f)` and `E = J ∩ Q[rho] = 0`. The theorem reproduces the
known obstruction and identifies it as a **horizontal component** — a solution
family moving with `rho`. This is a positive control on Theorem A itself.

### 3.4 What follows immediately

- **The `N`-ladder is not the question.** V38 (`N ≥ 6`) and V43 (`N != 6`) are
  correct and I do not dispute a line of either. But they measure the minimal
  exponent in `J0`, a quantity that Theorem A shows is not needed, and that we
  already know is finite. The planned weight-35 / `N=7` extension buys at most
  one bit at roughly `(35/30)^k` the cost, from a bit-budget of unknown and
  possibly small size.
- **Asymmetric monotonicity, in favour of Theorem A.** Adding grade-20 rows
  enlarges `J`, so it *preserves* `K+(rho)=(1)` and *preserves* generic
  emptiness, but it can *destroy* a nonmembership floor. The ladder's negatives
  are prefix-fragile; Theorem A's positive is prefix-monotone. The campaign is
  currently buying the fragile kind.
- **The `rho=0` multiplier extraction that hit the 192-GiB cap is not needed.**
  It computes an explicit exponent. Theorem A never uses one.

---

## 4. New cross-avenue connection (7 ⊗ 36 ⊗ 18 ⊗ 41), and one I refuted

### 4.1 The connection I believe

From the sweep: Jelonek (arXiv:2607.20597) proves the bounded-degree
automorphism locus `A_D` is **Zariski closed** in the constant-Jacobian
parameter space `K_D`, with a component dichotomy.

Then `K_D ∖ A_D` is **open**. An open subset of a Noetherian space is dense in
every irreducible component it meets. Hence:

> **If a plane Keller counterexample of degree ≤ D exists, it is a *generic*
> point of its irreducible component of `K_D`; the automorphisms inside that
> component form a proper closed subset.**

This directly contradicts the premise recorded against avenue 36 — "above the
cutoff the space is enormous and CEs form a thin locus". If Jelonek's theorem
is as summarized, the counterexample locus is **not** thin; it is dense in
whichever component it inhabits. The reason the search fails is therefore
*not* thinness. It is that we cannot sample from a component of `K_D` — the
Keller condition itself is the hard variety.

That reframes the target: **enumerate or bound the irreducible components of
`K_D`** (avenue 7's territory), rather than sample points (avenue 36's). And it
gives avenue 36 a genuine, falsifiable prediction to test at small `D` where
`K_D` is computable: *every component of `K_D` that contains one automorphism
consists generically of automorphisms.*

Row 18 contributes the other end: since `K_D` carries the `G_m` action
`F_t = t^{-1}F(t·x)` (Jacobian and degree bound both preserved), every point
has a `t→0` limit which is weighted-homogeneous, and Shaska makes that limit an
automorphism. So `A_D` is nonempty in every `G_m`-stable component and
`A_D` meets the closure of every orbit.

**Caveats, stated plainly.** I have no web access this round and have read only
the sweep's one-line summary of Jelonek. I have not seen the statement of the
component dichotomy, the precise parameter space, or whether `K_D` is taken
reduced or with its natural scheme structure. Every sentence above is
conditional on that summary being faithful. It should be checked against the
paper before any capacity moves.

### 4.2 The bridge I built and then refuted — report the refutation

I first tried to prove: *`G_m`-stable components of `K_D` contain no
counterexample*, arguing that the `t→0` limit is graded (Shaska ⟹ an
automorphism), the limit lies in the same closed irreducible component, and a
"pure component" dichotomy would then force the whole component into `A_D`.

**This is false, and avenue 41 is the refuter.** The dimension-three
counterexample deforms to its linear part: a counterexample and an
automorphism sit in one `G_m`-orbit closure. `A_D` being *closed* says only
that the limit point lies in `A_D`; it says nothing about the orbit. So
"component purity" in that strong form cannot be what the dichotomy asserts,
and my bridge collapses.

I record this because the bridge is attractive, is reachable from the same
three rows, and will be rebuilt by someone next round unless the refutation is
filed. It is also the reason I marked avenue 41 `reopen (lemma-only)`.

---

## 5. Strongest proof attack and strongest falsification attack

### 5.1 Strongest proof attack — the generic-`rho` decision (Card A)

Decide `a1 ∈ √(J ⊗ Q(rho))` for the frozen ordered-`a1` system. By Theorem A
this closes `K + (rho) = (1)` outright, i.e. **the honest ordered `T-a1` total
chart**, without any exponent, any DVR module, any weight-35 Macaulay dual, and
without the 192-GiB multiplier extraction. Details in §6.1 and Card A.

It is the strongest attack because the `rho=0` half is already promoted, the
instrument already exists in the repository, and the answer is binary.

### 5.2 Second proof attack — K00 in one colon (Card B)

At `C6 = 1`, in `Q[d0,…,d5]`, with `I = (r1,…,r6)`, `m = (d0,…,d5)`,
`A = Q[d]_m`, the Escape Lemma gives

```text
r7 in I·A   <=>   (I : r7) + m = (1)   <=>   some element of (I : r7)
                                             has nonzero constant term.
```

This is **one colon ideal in six variables**. It needs no local ordering, no
Mora tangent-cone algorithm, and no `G = I*T` transform replay — which is
exactly what V11 and V13 failed, and which the ledger correctly classifies as
software evidence rather than a local-membership verdict. It also decides the
`(d)`-adic ladder's fate: local membership ⟹ the ladder is infinite and D9,
D10, … are guaranteed compatible; local nonmembership ⟹ a finite first
obstruction degree exists and the ladder is the right way to find it.

The promoted global nonmembership `r7 ∉ I` over `Q[C6,C6^{-1},d]` and at
`C6=1` is fully consistent with either answer, since the local multiplier is
allowed a denominator with nonzero constant term. Nothing here disturbs the
two promoted V8/V9 statements.

### 5.3 Strongest falsification attack — the *same* run, read the other way

If the Card-A generic fibre is **nonempty**, then:

- **no `a1^N U(rho^2)` certificate exists at any `N`**, so the entire
  total-`T-a1` certificate programme — V43, the `N=7` weight-35 seed, the DVR
  syzygy, and the `rho=0` lift/`lp`/high-memory retries — is dead in one step
  rather than one rung at a time; and
- the computation hands back an **explicit obstruction: a horizontal component,
  a family of solutions of the frozen 59-row system moving with `rho`, with
  `a1 != 0`.**

That witness is the first object of its kind on the total chart, and it is
exactly the shape of a candidate source arc. It is therefore also the only
counterexample-side asset this round can generate for free. §2.2 rank 5 notes
that the portfolio currently has no obstruction-witness lane at all; this run
creates one as a by-product.

**Maximal-information property:** Card A is the rare experiment whose two
outcomes are both decisive and both large. That is why it dominates.

### 5.4 A cheaper falsification aimed at Card A itself

Before trusting Card A, falsify Theorem A on the campaign's own data: run the
generic-fibre test on the design's §3 toy (`J = (f − t x)`), where Theorem A
predicts `E = 0` and a nonempty generic fibre. A pipeline that reports
"closed" on the toy is broken. This is a mandatory negative control and costs
seconds.

---

## 6. Software acceleration / decisive experiment

### 6.1 The experiment is a two-token edit to a script that already runs

`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dehom_eliminant_v43.py`
already emits, for the seventeen selected cascade rows dehomogenized at
`a1 = 1`:

```text
ideal I0=subst(I,t,0); ideal G0=std(I0); poly specialnf=reduce(1,G0);
if (specialnf!=0) { print("FAIL_V43_TOTAL_DEHOM_SPECIAL_CONTROL"); quit; }
print("V43_TOTAL_DEHOM_SPECIAL_UNIT=1");
```

That control **is** the statement `a1 ∈ √J0'` for the selected sub-ideal, and it
**passes today**. The decisive experiment is the same three lines with `t`
alive:

```text
// (a) free Monte-Carlo preflight, minutes, over a large prime:
ideal It0 = subst(I, t, t0);            // t0 random nonzero
reduce(1, std(It0));                    // 0  =>  generic fibre empty (whp)

// (b) the exact, rigorous version — one Groebner basis over a function field:
ring Rq = (0,t),(<active vars>),dp;
ideal I  = <the same seventeen dehomogenized rows>;
reduce(1, std(I));                      // 0  =>  V(t)*1 = sum h_i T_i,
                                        //        so E != 0, so the chart closes
```

Soundness of restricting to the seventeen selected rows: they generate
`J' ⊆ J`, so `E' ⊆ E`; `E' != 0 ⟹ E != 0`. And the `t=0` control already
establishes `a1 ∈ √J0'` for that same sub-ideal. **Card A is therefore fully
self-contained on the seventeen rows** and does not even consume V42. If the
seventeen rows are not enough (`E' = 0`), escalate to all 59; that is a strict
enlargement and can only help.

Monte-Carlo semantics, stated exactly: if the generic fibre is nonempty, its
`rho`-image contains a dense open, so a random `t0` lands in it with
probability one; an empty fibre at random `t0` is therefore overwhelming but
**not** proof, and the exact certificate must come from (b) or from the
`eliminate` phase. A *nonempty* fibre at random `t0` likewise indicates a
horizontal component but must be confirmed at a second `t0` or over `Q(t)`.

### 6.2 A concrete fail-open defect in the existing eliminant lane

Same file, the outcome predicate:

```text
if ((unitfactor==0)&&(candidate!=0)&&(subst(candidate,t,0)!=0))
{ unitfactor=candidate/subst(candidate,t,0); }
...
if (unitfactor==0) { print("V43_TOTAL_DEHOM_OUTCOME=no-unit-eliminant"); quit; }
```

`unitfactor` is set only from an eliminant generator with **nonzero constant
term in `t`**. Consequently the two mathematically different outcomes

```text
E' = 0                (generic fibre nonempty  -> chart does NOT close)
E' != 0 but E' ⊆ (t)  (generic fibre empty     -> chart DOES close, by Thm A)
```

are **conflated into the single token `no-unit-eliminant`**, and the run quits.
Under Theorem A the second case is a **positive** result being reported as a
failure, because the `t=0` special control that upgrades `E' != 0` to
`E' ⊄ (t)` is already being computed three lines earlier and is simply not used
for that purpose.

Fix (small, and it is a strict widening of what the lane can conclude):

1. emit `V43_TOTAL_DEHOM_ELIMINANT_NONZERO = (size(E)>0 && E != 0)`;
2. branch on that flag, not on `unitfactor`;
3. when `E' != 0` and `E' ⊆ (t)`, *require* the already-passing special control
   and record the conclusion as `chart-closes-by-escape`, citing Theorem A;
4. keep `unit-eliminant` as the stronger, self-contained outcome when it occurs.

I have **not** run this lane and cannot say which branch it would take; the
defect is in the reporting logic, which is readable from source alone.

### 6.3 Two smaller software points

- **Ladder-hygiene preflight (extends the 0635Z shared gate).** Before funding
  rung `n+1` of any monotone ladder, require one of: (i) a termination proof;
  (ii) an exhibited escape reformulation (§3.1); or (iii) an explicit
  registration that the rungs are bought for negative information only, with a
  rung budget and a stop condition. Applied today this would cap `T-a1`
  weight-35, hold K00 D9, and put a budget on the AS109 degree floors.
- **The naturality interface (`1cfa10b4…`) has one fail-open control gap.**
  Its §3 rightly warns that raw valuations of the unreduced `F_i` can
  *over*predict the finite-jet ceiling. The opposite direction is unguarded:
  formula (3.2) maximizes over the *licensed* primitive inventory, so a
  **missing** primitive silently *under*predicts, and no listed mutation
  control detects it. Add a mandatory two-sided check — recompute (3.2) from
  raw `F_i` valuations as an upper bound, require
  `max_f^raw ≥ max_f^licensed`, and require a registered cancellation
  certificate for any gap. Separately, note the scope reality: §2's shifted-jet
  map is invertible only on `D(rho)`, so this whole interface is **orthogonal**
  to the two `rho = 0` obligations that dominate the critical path. It is a real
  compute saving, not critical-path progress.

---

## 7. Idea cards

### Card A — `T-A1-GENERIC-FIBRE` (top pick)

- **Claim to decide.** `a1 ∈ √(J' ⊗ Q(t))` for the seventeen selected
  dehomogenized rows; equivalently `E' != 0`.
- **Dependencies.** Theorem A §3.2 (proved here from promoted inputs); the
  promoted DVR criterion `e3d263d5…` / `98003865…`; the already-passing `t=0`
  special control inside `compile_total_dehom_eliminant_v43.py`. It does **not**
  depend on V43's `N=6` result, on V38, or on the V42 cascade.
- **Cheapest discriminator.** `reduce(1, std(subst(I,t,t0)))` at random
  `t0 != 0` over `F_65521` — the same shape as a control that already passes.
  Minutes. Then the exact `ring Rq=(0,t),…; reduce(1,std(I))` for the
  certificate.
- **Both outcomes.**
  - `0` (unit): with the `t=0` control, **`K+(rho)=(1)`; the honest ordered
    `T-a1` total chart closes.** Certificate is `V(t)·1 = Σ h_i T_i|_{a1=1}`,
    small and replayable. Cancel weight-35/`N=7`, the DVR syzygy, and the
    `rho=0` multiplier lift.
  - nonzero: a horizontal obstruction component exists; **no certificate at any
    `N`**; the whole total-`T-a1` certificate programme is dead, and the run
    yields an explicit `rho`-moving witness to parametrize (§5.3).
- **Mandatory controls.** (i) the design's §3 toy `J=(f−tx)` must return
  *nonempty* (§5.4); (ii) the `t=0` control must still pass; (iii) a corrupted
  row (drop or perturb `Tg19_7`) must flip the verdict; (iv) two independent
  `t0`; (v) exact `Q(t)` before any promotion.
- **Stop condition.** Stop if the exact `Q(t)` basis has not terminated in six
  hours *and* two independent `t0` disagree; report the `t0` evidence and the
  smallest failing identity. Do not escalate to all 59 rows before the 17-row
  run has an answer.
- **Expected information gain.** Highest in the portfolio. It converts a top-3
  campaign gap from an open ladder into a binary answer for the cost of one
  Gröbner basis, and both branches are large. Rough estimate: hours, versus a
  ladder of unknown length at superlinear cost per rung.
- **Non-claims.** Closing the frozen ordered `T-a1` chart proves nothing about
  the terminal receiver, source/landing coverage, `G2-PSC`, `G2-BD`, the
  ramified `rho=0` fibre, Gate T, order two, maximum twelve, or JC2.

### Card B — `K00-COLON-ESCAPE`

- **Claim to decide.** `r7 ∈ (r1,…,r6)·Q[d0,…,d5]_(d)`.
- **Dependencies.** The Escape Lemma; the frozen unloaded tails and the K00
  transverse chart at `C6=1` (already reconstructed and hostile-reviewed for
  V8/V9, `6c4ebd6d…`). Independent of V10/D8 and of the quarantined V11–V13.
- **Cheapest discriminator.** `quotient(ideal(r1..r6), ideal(r7))` in
  `Q[d0..d5]`, then test whether any reduced generator has nonzero constant
  term. Six variables; minutes.
- **Both outcomes.**
  - escapes `m` (local membership): the `(d)`-adic ladder is **infinite**; D9,
    D10, … are guaranteed compatible and buy nothing. Stop the ladder; the
    "first filtered obstruction degree" does not exist and must be removed from
    the obligation list. Redirect to mixed `Lambda^19` / load / `mu` / `Jdet`
    reachability, which is the genuinely open part.
  - stays in `m` (local nonmembership): a finite first obstruction degree
    exists, the ladder is the right instrument, and the colon additionally
    bounds where to look — run D9+ with a target rather than blindly.
- **Controls.** Reproduce the promoted global nonmembership `r7 ∉ I` from the
  same freshly emitted rows; confirm the colon result is stable under the
  registered `C6=1` Kummer normalization; verify against the promoted D7/D8
  compatibility (local membership must be *consistent* with, not implied by,
  those); run a planted positive control (`r7' = r1·u` with `u(0) != 0`).
- **Stop condition.** Stop at two hours or on any disagreement between the
  colon result and reviewed V8; report the smallest failing identity.
- **Expected information gain.** High. One small computation retires or
  redirects an open-ended ladder and answers a registered obligation
  ("genuine local membership") directly.
- **Non-claims.** Decides local membership at the K00 origin only. No formal
  membership, no closure-first incidence, no Taylor realizability, no receiver,
  no Gate T / order two / maximum twelve / JC2.

### Card C — `LADDER-HYGIENE-GATE`

- **Claim to establish.** Every monotone ladder in the portfolio carries either
  a termination proof, an escape reformulation, or a registered
  negative-information-only budget.
- **Dependencies.** §3.1; the 0635Z shared fail-closed gate, which this extends
  rather than replaces.
- **Cheapest discriminator.** Apply it retroactively today to the three known
  ladders (`T-a1` exponent, K00 `(d)`-adic, AS109 `deg_y`) and see whether the
  classification is decision-relevant. It already is for two of the three.
- **Both outcomes.** If the gate reclassifies existing lanes, install it. If it
  reclassifies nothing, it costs a day and is dropped — that itself is
  informative about whether the pathology is systemic or coincidental.
- **Stop condition.** One engineering day; do not let it grow into a framework.
- **Expected information gain.** Moderate but compounding, and it is the only
  item here that prevents recurrence rather than fixing one instance.
- **Non-claims.** Process only. No mathematical content beyond §3.1.

---

## 8. Hidden assumptions exposed

1. **"Raising the exponent floor is progress."** It is progress only until the
   floor meets the (known-finite, unknown-size) special exponent, after which
   the ladder reports a guaranteed positive that means nothing. The criterion
   does not contain `N`. (§3.2)
2. **"`no-unit-eliminant` is a failure."** Only `E' = 0` is a failure. A nonzero
   `t`-divisible eliminant is a *success* given the special control that the
   same script already computes. (§6.2)
3. **"There is a first filtered obstruction degree."** Only if local
   nonmembership holds. Two consecutive compatible rungs are weak evidence the
   other way. (§5.2)
4. **"Nonmembership floors are stable."** They are not. Adding grade-20 rows can
   only *destroy* a nonmembership and can only *preserve* an emptiness. The
   campaign is buying the fragile kind of result. (§3.4)
5. **"CEs form a thin locus" (avenue 36's recorded objection).** Under
   Jelonek's closedness the CE locus is open, hence dense in its component.
   The objection may be simply false. (§4.1)
6. **"`G_m`-degeneration to a graded limit constrains the orbit."** It does not
   — closedness of `A_D` constrains the limit only. My own bridge; refuted by
   avenue 41. (§4.2)
7. **Finite-jet ceilings derived from a *licensed* primitive inventory are
   fail-open against a missing primitive.** Only the over-prediction direction
   is currently guarded. (§6.3)
8. **Ring-identity assumption inside Card A.** Theorem A assumes
   `sp(J_total) = J0` literally, with `ez9` a genuine spectator. That is exactly
   what `98003865…` promotes and what `reconstruct_rows()` enforces via its
   byte-exact `rho`-zero frozen bridge over all 70 rows — but Card A must
   re-assert it, not inherit it.
9. **Selected-subset asymmetry.** The seventeen-row lane is sound for the
   *positive* branch only (`E' != 0 ⟹ E != 0`). A negative on seventeen rows is
   inconclusive and must escalate to all 59 before any "no certificate"
   conclusion is drawn. This asymmetry is not currently written down in the
   lane's scope.

---

## 9. Lane dispositions: continue / redesign / stop

| Lane | Verdict | Reason |
|---|---|---|
| `T-a1` total-rho DVR / weight-35 `N=7` seed | **redesign** | Superseded by Card A. Hold the launch; the criterion has no `N`. |
| `T-a1` `rho=0` multiplier extraction (192-GiB lift / `lp` / high-mem retry) | **stop** | Computes an exponent Theorem A never uses. |
| `T-a1` total-rho selected eliminant | **continue, with the §6.2 predicate fix** | This is the right instrument; its success test is strictly too strong and its outcome tokens conflate two different answers. |
| `T-a1` raw `rho=0` prefix work (V38/V39/V42 successors) | **stop as a critical path; keep as promoted inputs** | Its job is done: it supplies `a1 ∈ √J0`, the half Theorem A needs. |
| K00 filtered Macaulay ladder (D8 review, D9+) | **redesign** | Finish the D8 hostile review already in flight, then hold D9 until Card B returns. D8 review is cheap and independently valuable. |
| K00 local-order Singular route (V11/V13, quarantined) | **redesign** | Replace the local ordering entirely with the global colon of Card B. The `G=I*T` transform replay is not needed for the question being asked. |
| K00 closure-first `H_K00` incidence | **continue** | Independent of both ladders and aimed at a genuine open gap (the receiver). |
| Generic-square `(2,3,≥2)`, `(2,4,≥3)` contact transports + hostile reviews | **continue** | Reviews are live and cheap; both are the repaired shifted-root pattern. |
| `ACT-TOT-G20` / V44R1 for `(2,5,≥3)` | **redesign** | If the naturality interface survives review, serial grade custody is unnecessary; demote V44R1 from critical path to a control on the interface. |
| Uniform contact-shift naturality interface + linker | **continue** | Highest leverage in that family. Add the §6.3 two-sided finite-jet control. Keep the `D(rho)`-only scope firewall explicit — it is orthogonal to the `rho=0` gaps. |
| AS109 `n=6` arithmetic Newton corner | **continue, capped and relabelled** | Sound work, but register it as a floor-raising ladder with no termination theorem, a rung budget, and a stop condition. |
| TD6 H19R2 | **continue** | Cheap, independent, already synchronized; do not disturb. |
| Web-sweep clock (`2026-08-28T00:00Z`) | **continue** | Unchanged. But see §4.1: the Jelonek statement should be re-pulled and read in full, not from the one-line summary, before any capacity moves on avenues 7/36. |
| `jc2-lean` | **untouched** | Not entered, read, built, status-inspected, or modified. |

---

## 10. Novelty caution and global non-claims

**Novelty, labelled cautiously.** The Escape Lemma is textbook. The
`eliminate`-based instrument for `T-a1` **already exists** in the repository,
and the campaign already lists a "total-rho selected eliminant" lane. What I
claim as new is: (i) **Theorem A**, which upgrades that lane from one of four
parallel exponent-hunting attempts into the *complete decision procedure*, and
shows the exponent is not part of the question; (ii) the observation that its
required output is `E != 0`, strictly weaker than the `unit-eliminant` the code
tests for, together with the concrete conflation defect at §6.2; (iii) the
random-`t0` preflight and the toy negative control; (iv) the colon
reformulation of K00 local membership as a replacement for the `(d)`-adic
ladder; (v) the observation that three separate lanes share one ladder
pathology; and (vi) the Jelonek genericity reading against avenue 36's recorded
"thin locus" premise. The coordinator's history/priority checksum should test
each of these six separately — several may have prior art I could not see.

**Non-claims.** Nothing in this submission proves or disproves JC2, Gate T,
order two, maximum twelve, `G2-PSC`, `G2-BD`, source/landing coverage, the
terminal or Taylor receiver, the ramified `rho=0` deck/square fibre, or any
cofinal degree/type bound. Theorem A is a statement about the frozen
grade-through-19 ordered `T-a1` chart and nothing else; even a positive Card A
closes only that chart. No promoted claim is contradicted; the only claim I
assert is defective is the *reporting logic* at §6.2, and the only claim I
withdraw is my own bridge at §4.2. I ran no heavy algebra, launched no AWS,
edited no canonical ledger, and touched no campaign artifact other than this
file.
