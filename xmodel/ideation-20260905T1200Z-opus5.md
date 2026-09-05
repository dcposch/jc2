# Ideation round 20260905T1200Z — blind submission (Opus 5)

Lane `ideation-20260905T1200Z-opus5`. Desk-scale CAS only; every number below
is either cited to a banked delta or was produced in this lane and is labelled
`MEASURED-HERE`.

## 0. Provenance, blindness, and what I actually ran

Charged inputs verified mechanically before reading: the manifest was rebuilt
with `awk` from `xmodel/ideation-20260905T1200Z-opus5.run.v2`
(`charged_input_<i>_sha256=` / `_basename=`) and checked with `sha256sum -c`.
4/4 `OK`, no content mismatch:

| input | sha256 (first 16) | verdict |
|---|---|---|
| `ideation-20260905T1200Z-packet.md` | `caf32f2f2faf822f` | OK |
| `ideation-20260905T0200Z-synthesis.md` | `4695f855267b451c` | OK |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7` | OK |
| `COORDINATION.md` | `26940fc807976314` | OK |

Read after that: `AUDIT.md` deltas 17(mmmmmm)–(ssssss); `notes.md` LIVE
STATE/EVENT stream 2026-09-05T00:32Z → 09:28Z (the 09:28Z EVENT is the newest
binding entry); `xmodel/moh14-fullorder-grok46-20260905.md` (freshest sealed
Moh lane); `xmodel/k16-brcr-closedform-sol56-20260903.md` §2.3, §4;
`AUDIT.md` 17(rrrrr) EN-CURVE/FITT/B-HSOP; `box/k16brcr-20260905/…` exact tail
files; `box/moh14-charts-20260905/classes/…` chart jobs emitted before
09:29Z. `APPROACHES.md` overlay of 2026-09-03T10:45Z.

**Blindness disclosure (one line, accidental).** A repository-wide
`grep -rn "Eagon"` returned one matching line from
`xmodel/ideation-20260905T1200Z-opus5-coordinator.md`, which is a same-round
submission I was instructed not to read. The line proposed liaison / the
Eagon–Northcott resolution and the "nonzerodivisor = not in any associated
prime" framing. I did not open that file, and I flag the overlap explicitly:
the Q1 idea below reaches the associated-prime observation independently but
goes past it to a *group action*, which is the part I am claiming. Treat the
overlap as correlated, not as independent support. Subsequent greps were run
with same-round exclusions. I did not open `moh14-msolve-sol56-20260905.md`
(receipt only: `initial_status=RUNNING`, `start_utc=2026-09-05T09:29:37Z`,
8 charged inputs, no `final_status`).

**Second blindness disclosure (mine, after my results were computed).** At
write-up time I listed my persistent memory directory, saw an unfamiliar file
`k16-gamma-reduced-single-orbit.md`, and read it. It turned out to be a note
written *during this round by another lane* and to cite that lane's report.
Its content — Γ_t is generically reduced, `7/46/265` simple points on `b4 ≠ 0`
at t = 3,4,5, and at t = 3 those points form ONE **Galois** orbit over `A_3`,
so clause (ii) is all-or-nothing per orbit — is a different mechanism from
mine (Galois orbits of points vs. a `G_m` action on the incidence), and it
arrived after every number in §2 was already measured. I used none of it. I
flag it because the two are *complementary* and the coordinator should dedupe
them as one cluster with two independent mechanisms, not treat either as
confirmation of the other.

**Compute run here** (desk-scale, reproducible from the cited banked
artifacts): five Singular jobs (K16 β-collapse, t = 3–6) and three Python
passes over the 48 MB emitted Moh chart
`C_n24m16_Mm12_m2_5_ell1_s4_union_fo_u32003.sing` (exact homogeneity solve,
zero-propagation/branch census, pivot-elimination attempt). Ledger in §11.

---

## 1. Disposition vector (changes only)

| avenue / object | was | now | reason |
|---|---|---|---|
| K16 atom: nonvanishing of `T_{t,2t−1}` on the EN curve `Γ` | flagship OPEN, "needs a new idea", HOLD | **REOPEN + RAISE** | `MEASURED-HERE`: the atom collapses from a ∀ over the `d_Γ(t)` points of a curve of growing degree to **two fixed-shape 0-dimensional statements**, because `β` carries weight `t+1 ≠ 0` and `G_m` therefore acts transitively on the `β ≠ 0` slices. Verified reproducing (V0) at t=3,4,5. §2. |
| K16 `d_Γ(t)` bookkeeping (LENGTH-SPLIT, EN Hilbert numerator) | load-bearing | **LOWER to descriptive** | the collapse removes `d_Γ(t)` from the statement; §2.35 re-derives LENGTH-SPLIT as its shadow. |
| K16 resultant route | refuted / "ill-posed" | **unchanged (stay closed)**, with a note | the ill-posedness was on a non-square system; the collapse produces a square `t`-in-`t` system. Not reopening it — flagging it as the one refutation that may not transfer. |
| Moh ≤100 residual = "a solver-performance wall" (17(ssssss)) | accepted | **PARTIALLY DISPUTED → RETYPE** | `MEASURED-HERE`: the wall is *at least partly* instrument choice. The chart is exactly weighted-homogeneous; the only inhomogeneous element in the 425-generator system is the Rabinowitsch generator `T·c−1`, which every run carried. §3. |
| "78–84% of order-chart unknowns are raw-pivotable" (banked, band-engine charts) | assumed transferable | **LOWER** | `MEASURED-HERE`: on this chart, 0 of 27 pure-linear pivots survive a 1500-term cap; pivot representations run 180→8182 terms. The figure does not transfer to the s'=3 order charts. |
| receiver atlas as the unifying object | corrected to "routing object" (17(mmmmmm)) | **unchanged**, ranked lower than U-NEGATIVE | §4. |
| leak (ii) U-NEGATIVE (`V₂' > d₂'`) | named, dormant since 17(qqqqq) | **RAISE to first-rank scope leak** | It is the only one of the three surviving leaks that is an *uncharted configuration* rather than a bookkeeping obligation. No lane has ever enumerated it. §4. |
| the u_s≥2 census (1359 descended classes) as a fleet target | queued | **LOWER / DEFER** | Deploying 1000 vCPU on 1359 instances of a method that has not yet finished one of 12 residual fibres is a throughput answer to an algorithm question. §5. |
| `(H1)∧(H2) ⇒ plane JC2 for minimal counterexamples` (17(pppppp)) | promoted | **unchanged** | I re-read the argument shape and have no objection; the three named leaks are correctly kept. |
| the "6-chart fleet batch" framing of the ≤100 finish | live | **REDESIGN** | re-emit graded and branched before more fleet time. §3, §7. |

Bottleneck re-rank (proof side): **(1)** the 12 u_s=1 fibre charts, now
retyped as a *graded* emptiness problem; **(2)** the K16 atom, now retyped as
(α)+(β); **(3)** U-NEGATIVE; **(4)** route-to-state totality; **(5)** the
u_s≥2 census. Disproof side unchanged: no lane has produced a verified
`(P,Q)` with `J = c·x^ℓ`, and 17(ssssss) is explicit that `TIMEOUT` is not a
survive.

---

## 2. Q1 (K16) — the β-PENCIL COLLAPSE: a group action on `Γ` that the campaign
has been carrying without using

### 2.1 The claim

The atom, as stated across 17(rrrrr)/(uuuuu)/(hhhhhh), is:

> for every `t ≥ 3`, `T_{t,2t−1}` is a nonzerodivisor on `S_t/(G_1..G_{t−1})`
> — equivalently the top row does not vanish at any of the `d_Γ(t)` points of
> the Eagon–Northcott curve `Γ = V(I₂(N))`.

`d_Γ(t) = [C(3t+1,t−1) − C(2t,t−1)]/(t+1) = 15/2, 46, 805/3, 1548, …` — an
object of *growing* size, which is exactly why every route so far had to be
uniform-in-`t` and every uniform route failed.

**CLAIM (β-PENCIL COLLAPSE).** `Γ` is not an unstructured curve. It is the
total space of a `G_m`-equivariant pencil with a **nonzero weight on the
kernel parameter**, and therefore, modulo two banked inputs, the ∀ over
`d_Γ(t)` points is *equivalent* to two statements of fixed shape:

> **(V0) ⟺ (α) `V(C_1,…,C_{t−1}, c_0) = {0}`  ∧  (β) `1 ∈ (C_1+B_1, …,
> C_{t−1}+B_{t−1}, a_0+b_0+c_0)`.**

and **(α) is free given C-HSOP** (`V(C_1,…,C_{t−1}) = {0}` already implies
`V(C, c_0) = {0}`).

### 2.2 Derivation (three lines, all inputs banked)

1. *Finite kernel everywhere.* At a rank-one point the kernel is `(1:β)` with
   `C_r + βB_r = 0` (Sol §4.1 (4.1)). The excluded case — all `B_r = 0`, some
   `C_s ≠ 0`, kernel `(0:1)` — is empty under **B-HSOP** (`V(B) = {0}`,
   measured t = 2..8, 17(rrrrr)), so every nonzero point of `Γ` has finite `β`.
2. *The weight of `β` is `t+1`, independent of `r`.* From Sol's exact support
   table (§2.3): `#B_r = p_{t−1}(t+1+r)` and `#C_r = p_{t−1}(2t+2+r)`, i.e.
   `wt(B_r) = t+1+r`, `wt(C_r) = 2t+2+r`, so `wt(C_r) − wt(B_r) = t+1` for
   every `r`. This is Sol's own (4.11) relative twist
   `deg_P(v) − deg_P(u) = t+1` — *stated but never used as a group action*.
   `MEASURED-HERE` (Singular `deg` in the `wp(1,…,t−1)` ring):
   t = 3: `deg C_1 = 9`, `deg B_1 = 5`; t = 4: `11`, `6`; t = 5: `13`, `7`.
   Differences `4, 5, 6 = t+1`. ✓
3. *Transitivity.* The incidence `Γ̃ = V(C_r + βB_r) ⊂ A^{t−1} × A¹_β` is
   stable under the `G_m` action with weights `(1,2,…,t−1; t+1)`. Because
   `wt(β) = t+1 ≠ 0`, `G_m` acts **transitively on the set of nonzero `β`
   values**: every orbit with `β ≠ 0` meets the slice `β = 1`. Hence
   `Γ̃ ∖ {0} = (β = 0 stratum) ⊔ G_m·(β = 1 slice)`, and the two clauses
   above are exactly the two strata.
   The `β`-axis `{p = 0}` ⊂ `Γ̃` is harmless: `b_0, c_0` have positive weight
   so `Q̂|_{p=0} = a_0β²`, and `a_0` is a **unit** (banked TAIL-SPLIT,
   17(rrrrr)), so `Q̂ ≠ 0` there for `β ≠ 0`.

`Q_t = a_0β² + b_0β + c_0` with `wt(a_0) = 0`, `wt(b_0) = t+1`,
`wt(c_0) = 2t+2` (support table; homogeneity of `Q_t` is then automatic).
Clause (α) is the `β = 0` stratum (`Q_t = c_0`), clause (β) the `β = 1`
slice (`Q_t = a_0+b_0+c_0`), and (β) is a Nullstellensatz emptiness, i.e. a
unit-ideal test — the dehomogenisation-by-1 form the campaign already knows
is ~100× cheaper than a `c^N ∈ I` test.

### 2.3 MEASURED-HERE

Exact over `A_t = Q[yy]/(H_t)` at t = 3, 4 (`H_3 = 588y²−336y+44`,
`H_4 = 972y²−540y+70`); modular at t = 5 with `p = 32003` and t = 6 with
`p = 32027`, both chosen so that `H_t` stays **irreducible** (`A_5 = Q(√2)`,
`A_6 = Q(√21)`; Singular accepts the `minpoly` with no zero-divisor warning).
A first t = 6 attempt at `p = 32003` hit `H_6` reducible — a product algebra,
not a field — and was discarded and rerun; FALLACY-v2 *sat()/ring* discipline,
recorded because the discarded run happened to give the same `vdim`. Forms
taken verbatim from `box/k16brcr-20260903/explicit_tail_t{3,4,5,6}_exact.txt`.

| t | TEST A `dim(C)`, `vdim` | ∏(2t+2+r)/(t−1)! | TEST B `β=1` slice | CTRL-B `dim(B)`,`vdim` | CTRL `dim(I₂(N)+W)` |
|---|---|---|---|---|---|
| 3 (exact) | `0`, **45** | `9·10/2 = 45` ✓ | `reduce(1,·)=0`, `dim −1` (inconsistent) | `0`, `15` = `5·6/2` ✓ | `0` ✓ (banked (V0) t=3) |
| 4 (exact) | `0`, **286** | `11·12·13/6 = 286` ✓ | inconsistent, 25 ms | `0`, `56` = `6·7·8/6` ✓ | `0`, 63 ms ✓ |
| 5 (mod 32003) | `0`, **1820** | `13·14·15·16/24 = 1820` ✓ | inconsistent, 4 ms | `0`, `210` ✓ | `0`, 5 ms ✓ |
| 6 (mod 32027) | `0`, **11628**, 40 ms | `15·16·17·18·19/120 = 11628` ✓ | *running at seal* | `0`, `792` = `C(12,5)` ✓ | — |

Three things to read off:

- **The collapse reproduces the banked verdict.** (V0) is true at t = 3,4,5
  (control column) and (α)∧(β) is true at t = 3,4,5. No disagreement.
- **C-HSOP holds and is *exactly* Bézout.** `vdim(C)` equals the weighted
  Bézout number `∏_{r}(2t+2+r)/(t−1)!` on the nose at t = 3,4,5,**6** —
  45, 286, 1820, 11628, four for four, no excess intersection. So `C_1,…,C_{t−1}` is a regular sequence of the generic
  length, the exact analogue of the banked B-HSOP (`vdim(B) = ∏(t+1+r)/(t−1)!`,
  also exact here: 15, 56, 210). This is a *Koszul* statement with a closed-form
  length — the shape that has yielded to the campaign's leading-form machinery
  three times.
- **(β) is where the content sits**, and it is now a statement about a
  Bézout-bounded *finite* scheme (`V(C+B)`, whose finiteness follows from
  C-HSOP because the top-weight part of `C_r + B_r` is `C_r`), not about a
  curve of growing degree.

### 2.35 The identity that says the collapse is the right decomposition

The two Bézout numbers measured above are not arbitrary. In binomial form,
`∏_{r=1}^{t−1}(2t+2+r)/(t−1)! = C(3t+1, t−1)` and
`∏_{r=1}^{t−1}(t+1+r)/(t−1)! = C(2t, t−1)`, so `MEASURED-HERE` reads

> `vdim(C_1,…,C_{t−1}) = C(3t+1, t−1)` = 45, 286, 1820, 11628 at t = 3,4,5,6
> `vdim(B_1,…,B_{t−1}) = C(2t, t−1)` = 15, 56, 210, 792 at t = 3,4,5,6

— and these are **exactly the two binomials in the banked Eagon–Northcott
degree formula** `d_Γ(t) = [C(3t+1,t−1) − C(2t,t−1)]/(t+1)` (17(rrrrr),
Sol (4.10)), and exactly the two terms of the banked LENGTH-SPLIT
`L_t = 2C(3t+1,t−1) = 2C(2t,t−1) + (2t+2)·d_Γ(t)`. Rewriting:

> **`d_Γ(t) = [vdim(C) − vdim(B)] / (t+1)`**, and
> **`L_t = 2·vdim(C)`.**

So the banked length theorem *is* the statement that the curve degree is the
excess of the `C`-hsop over the `B`-hsop, divided by the twist `t+1` — which
is precisely `wt(β)`. The LENGTH-SPLIT, which has been carried as a numerical
consistency identity, is the shadow of the `G_m` decomposition. That is the
strongest evidence I have that (α)/(β) is the *natural* decomposition of this
object rather than an ad-hoc rewriting, and it is also the connection between
two previously separate avenues (the length/EN-numerator bookkeeping and the
nonzerodivisor atom). Cross-check: at t = 6, `[11628 − 792]/7 = 1548`, the
banked `d_Γ(6)`. ✓

### 2.4 Why this is new, and what it does not do

Every prior route (coprime-leaders, degree-only, exact square, resultant,
linked quartic, socle law) attacked `Γ` as a curve and needed a uniform-in-`t`
identity because `d_Γ(t) → ∞`. The `G_m` action deletes that growth: after the
collapse there is no growing object in the statement, only two systems of `t`
forms in `t−1` variables. The socle law (17(oooooo)) is untouched and
consistent with this — it says there is no uniform fixed-power identity for
`τ_t ∈ √I`; the collapse does not produce one, it replaces the target.

Honest limits: (i) the collapse is conditional on **B-HSOP** (measured to
t = 8, not proved for all `t`) and on `a_0` being a unit (banked exactly to
t = 5); state both as hypotheses. (ii) It reduces, it does not prove: (β) at
general `t` is still open. (iii) `MEASURED-HERE` at t = 5 is modular, hence a
signal, not a char-0 promotion (FALLACY-v2). (iv) FALLACY *floor/attainment*:
I am claiming an **equivalence** with named hypotheses, not a bound.

### 2.5 Cheapest decisive test (bounded quantity + instrument + gate + clock)

**QUANTITY.** Decide whether `vdim(C_1,…,C_{t−1}) = ∏_{r=1}^{t−1}(2t+2+r)/(t−1)!`
holds at `t = 6,7,8`, and whether the `β = 1` slice ideal `= (1)` at those `t`.
**INSTRUMENT.** Singular in `ring (p, yy),(b4,q2_0..q_{t−1}_0), wp(1..t−1)`
with `p` chosen so `H_t` stays irreducible; the forms are already banked
(`explicit_tail_t{6,7,8}_exact.txt`, t = 6 exists; t = 7,8 need one
`brcr` re-emit). **GATE.** `dim = 0 ∧ vdim = Bézout` and `reduce(1,slice) = 0`.
**CLOCK.** t = 6 modular started here (running at seal); t = 7,8 ≤ 30 min
including the emit. If the Bézout identity holds at every `t` tested, promote
**C-HSOP-BEZOUT** as a lemma candidate and put the whole K16 ray on (β) alone.

---

## 3. Q2 (Moh ≤100 finish) — the wall is partly instrument, and I can show it

### 3.1 If msolve returns UNIT: that is not yet the finish. Two named gaps.

**Gap 1 — a modular UNIT is not a characteristic-zero kill, and the gap is
real, not pedantic.** `1 ∈ I ⊗ F_p` does **not** imply `1 ∈ I ⊗ Q`: the
one-line counterexample is `I = (px − 1) ⊂ Z[x]`, which is the unit ideal mod
`p` and has the honest rational zero `x = 1/p`. The grok46 lane already types
this correctly ("a unit here is a signal, not a char-0 kill"), and Stage B
(exact-`Q` on a certificate subset) *was never reached*. So the promotion
obligation is explicit:

> a `UNIT` verdict is promoted only by an exact cofactor vector
> `1 = Σ f_i g_i` over `Q`, verified by exact multiplication.

The *search* for that vector is expensive; the *verification* is one
polynomial multiplication pass. The right pipeline is therefore: solve mod
several primes → reconstruct the cofactors by CRT + rational reconstruction →
verify exactly. This is the only step that is genuinely embarrassingly
parallel in the whole Moh finish, and it is the one nobody has built (§9).

**Gap 2 — the class logic is conjunctive and there are 12 obligations, not 6.**
`class dead ⟺ every fibre UNIT`. From the grok46 per-class table the fibre
counts are `1 + 1 + 2 + 3 + 3 + 2 = 12`, with unknown counts 77, 88, 126, 155,
248, 333, 378, … So the finish is **12 certificates**, and one non-unit fibre
collapses it. The asymmetry matters for scheduling: partial UNIT signals on
"several fibres" (the packet's phrasing) are worth much less than the count
suggests.

**Paper-grade statement, if all 12 land.** Not a new theorem about JC2 — a
*repair of a published one*:

> **THEOREM (conditional on the 12 certificates).** Moh's Theorem 1.1 (no
> plane Keller counterexample of degree ≤ 100) holds with no residual case.
> Chain: Moh (1)–(13) sieve → the promoted whole-tree screen (17(r)/(hh)/(ll))
> and the Xu screen → 658 → 20 → 14 → 12 rows in 6 descended classes → the
> `Φ_eff` s'=3 compiler (17(nnnnnn), `δ'_i = (ℓ+1)·Def 5.1(3)` after the
> p.174 drop, validated 5/5 against Appendix II p.207 and against
> `order_basis_full.closed_form`) → the full Theorem-1.2 D1 order chart with
> `B_safe` → emptiness certificate per fibre. Independently, the published
> open case `(99,66)` is closed degree-wide by 17(ffffff).

Dependencies to state, not hide: `B_safe` not `B_tight`; the 17(ssssss)
correction (the order chart *is* the complete necessary object at `u_s = 1`;
pole/Jacobian/incidence rows are `u_s ≥ 2` machinery and 17(rrrrrr)'s call for
them was withdrawn); and that this is the **two-point stratum**, which by
17(pppppp) covers all *minimal* plane Keller counterexamples but still carries
the U-NEGATIVE and routing leaks.

### 3.2 If msolve stalls: the structural route — and a measured reason the stall
is avoidable

I took the smallest already-full chart —
`box/moh14-charts-20260905/classes/C_n24m16_Mm12_m2_5_ell1_s4/jobs/…_union_fo_u32003.sing`
(class `C_n24m16_Mm12_m2_5_ell1_s4`, `K = 8`, 77 unknowns, 425 generators,
48 MB, the one that burned 11.2 GB / 58 min on an r7i without returning a
basis) and measured its structure.

**(A) The chart is exactly weighted-homogeneous.** `MEASURED-HERE`: parse all
424 non-Rabinowitsch generators, form the homogeneity equations
`Σ_f (n_f(m) − n_f(m₀))·W_f = Σ(i+j)(m) − Σ(i+j)(m₀)` over every monomial pair,
and solve exactly over `Q`:

- 1,155,984 equations, **rank 6, zero inconsistent rows**;
- unique solution `w(X_{i,j}) = W_X − i − j` with
  `W_h = W_{A1} = 8 = K`, `W_{A2} = W_{B2} = 16 = 2K`, `W_{A3} = 24 = 3K`,
  and `w(c) = 37 = 5K − 3`;
- `T` is a free family — i.e. **`T·c − 1` is the only inhomogeneous element in
  the entire system**;
- independent confirmation: after substituting the two weight-zero variables,
  Singular reports `HOMOG 1` on the 397-generator ideal in the
  `wp(w_1,…,w_75)` ring.

**(B) The grading is non-negative with exactly two weight-zero unknowns.**
Weight multiset over the 77 unknowns: `0:2, 1:4, 2:4, 3:2, 4:2, 5:2, 6:2,
7:2, 8:4, …, 23:2, 37:1(=c)`. The two weight-zero unknowns are `h_1_7` and
`A1_1_7`.

**(C) One generator is a variable.** `I[420] = −16·A1_1_7`. Zero-propagation
forces `A1_1_7 = 0` in one round and drops the system 425 → 397 generators.
`c` is *not* forced to zero, and no contradiction appears — so this is a
simplification, not a kill.

**(D) The chart carries a free three-way case split.** After (C) the ideal
still contains the pure monomial `−8·A2_1_7·B2_1_7·h_1_7^13`, so
`V(I) = {A2_1_7=0} ∪ {B2_1_7=0} ∪ {h_1_7=0}`. `MEASURED-HERE` branch sizes:
`A2_1_7=0` → 388 gens; `B2_1_7=0` → 375; **`h_1_7=0` → 209 gens** (a 47%
reduction from one substitution). Second-level splits exist in every branch.
`std` is being asked to discover this split implicitly, in an ungraded `dp`
ring, on 78 variables.

**(E) The consequence — a complete kill certificate that needs no
saturation.** Set `A1_1_7 = 0` (forced) and `h_1_7 = 1` (the lead
normalisation; the `h_1_7 = 0` branch is the separate 209-generator problem).
Because both are **weight-zero**, this substitution *preserves the grading*.
What remains is a weighted-homogeneous ideal `I₀` in **75 unknowns, all
weights ≥ 1**, with `w(c) = 37 > 0`. For a positively graded ideal:

> `dim V(I₀) = 0 ⟹ V(I₀) = {0} ⟹ c ≡ 0 on the chart ⟹ the fibre is dead.`

So `dim(std(I₀)) == 0` is a **complete kill certificate** — no `T`, no
Rabinowitsch generator, no saturation — and it is computable by a *graded*,
degree-by-degree standard basis whose memory is bounded per degree and which
can be truncated. This is exactly the banked homogeneous-cone recipe ("test
dim-0, not the inhomogeneous `[1]`; `dim > 0` is not failure"), and it has
never been applied to these six charts. Conversely `dim > 0` is not a survive;
it hands back the smaller question "does some positive-dimensional component
avoid `V(c)`", on a system that has by then been reduced.

**(F) Honest negative — the pivot route does not work here.** I tried the
banked pivot-reduction recipe: all 27 unknowns with a pure-linear occurrence
were tested as pivots, cheapest-first. **0 of 77 unknowns eliminated** at a
1500-term cap; the pivot representations run from 180 terms (`A2_1_4`) to
8182 terms (`A3_2_0`), and every substitution blew the cap on some generator.
The banked "78–84% raw-pivotable" figure is a band-engine number and does
**not** transfer to the s'=3 order charts. I am reporting this because it kills
an obvious-looking cheap idea before someone spends a lane on it.

**(G) Status of the confirming run.** A graded `std` of the 397-generator,
75-unknown, positively weighted ideal (`wp`, `p = 32003`, no `T`) was launched
here; at seal it had printed `NGENS 397` and `HOMOG 1` and was still running.
So I claim the *structure* as measured and the *speedup* as untested. That is
the honest split, and it is precisely the experiment the first lane should own.

### 3.3 The structural route for `u_s = 1`, independent of any chart

Worth stating because it is the only route that would make the charts
unnecessary. At `u_s = 1` the Prop 6.3 descent is the substitution
`y = γ^{−u_s} = γ^{−1}` (banked: the descent is an explicit substitution, `J`
a `γ`-monomial), and the descended degree is `n' = (n/d_s)·u_s = n/d_s`. So at
`u_s = 1` the descent is a **strict degree drop by the factor `d_s`**: every
one of the 12 rows descends to degree `n/d_s ≤ 50`. If the descended datum
were a legitimate smaller instance of the ≤100 statement, all 12 would die by
Moh's own induction with no Gröbner basis at all. The reason they do not is
nameable: the descended object is a monomial-Jacobian pair in `k[γ,π]`, not a
polynomial Keller pair, so the induction hypothesis does not literally apply.
That missing bridge — "descended datum ⟹ legitimate smaller instance" — is a
single lemma, and it is worth an hour before any more compute. Raised as
`OPEN[US1-DESCENT-INDUCTION]` (§10).

---

## 4. Q3 (coverage) — the binding sub-gap is *totality of route-to-state*, and
it is not the top-ranked leak

### 4.1 Is coverage a finite check or a uniform theorem? Neither — it is an
induction, and that is good news

The packet asks whether coverage is "a finite check per degree, or a uniform
theorem". It is a third thing: a **well-founded induction along the descent**,
with the finite atlas as the *step* and `s' = 2` / `u_s = 1` as the *base*.
The obligation decomposes into three, only one of which is hard:

- **(T1) Totality of first-separation.** Every charged source branch has a
  defined first-separation datum. This is exactly what the 296 explicit
  `UNASSIGNED` split branches of the atlas (17(mmmmmm)) measure — 132/132
  cohort keys carry an INTERFACE theorem, 296 branches carry no assignment.
  **(T1) is the binding sub-gap.**
- **(T2) Hypothesis preservation.** The descended datum lies in the atlas
  domain. This is finite per depth and is what the `Φ_eff` compiler already
  computes (`δ'_i = (ℓ+1)·Def 5.1(3)`, validated at `s'=2` against Appendix II
  5/5).
- **(T3) Termination.** The descent law `u_s = d_s − V_s`,
  `n' = (n/d_s)·u_s`, `ℓ = v_s − u_s − 1` gives `n' < n` whenever
  `d_s ≥ 2` and `u_s < d_s`. So `n` is a candidate well-founded measure and
  the whole termination obligation is the **finite arithmetic check**
  "`d_s = 1` or `u_s = d_s` never occurs on an admissible datum". That is a
  one-pass census over the banked enumeration, not a theorem.

So coverage is neither an infinite verification nor a single uniform theorem:
it is (T1) plus two checks. FALLACY *target/arrival index*: (T1) is about
`nu_U`-side (incoming) data and must not be conflated with the fixed `nu_G`
the atlas keys on — that conflation is exactly how "132/132 keys" gets misread
as coverage.

### 4.2 Where I challenge the coordinator framing

The packet says the source→receiver coverage "is the real all-degree gap". I
half-agree and rank it **second**. The leak I would rank first is
**U-NEGATIVE (`V₂' > d₂'`)**, from the 17(qqqqq)(5) scope correction, kept
open by 17(pppppp). The difference is categorical:

- coverage/(T1) is a **bookkeeping obligation of known shape** — we know what
  the objects are (296 named branches), we know what a discharge looks like
  (an assignment with certificate pullback), and the atlas machinery exists;
- U-NEGATIVE is a **third configuration nobody has charted**. It is not a
  hard case of the two-point program; it is *outside* it. No lane has
  enumerated how many rows are U-NEGATIVE, at any degree.

A gap you have never counted outranks a gap you have itemised — and the fix
is cheap: U-NEGATIVE has a census-shaped cheapest test (§10), so one lane-hour
either closes it by enumeration or promotes it to a flagship. It is exactly
the kind of item the 2026-09-03 cheapest-test amendment was written for.

---

## 5. Q4 (leverage) — I reject the question as posed

The packet offers four deployments: the u_s≥2 census (1359 classes), the s'>2
residual, K16 t=8..11 verification, the coverage proof. All four are
throughput answers, and the evidence says throughput is not the binding
constraint:

1. The smallest residual chart — **77 unknowns** — consumed 11.2 GB and 58
   minutes on a 247 GB r7i without returning a basis, while carrying an
   *exactly verifiable* grading that no run used and an inhomogeneous
   generator that no run needed (§3.2). A thousand vCPU running that same
   configuration produces a thousand copies of the same `TIMEOUT`.
2. Gröbner basis computation is not embarrassingly parallel. The fleet's
   genuine parallel clients are (i) **independent primes** for CRT cofactor
   reconstruction, (ii) **independent branches** of an explicit case split
   (the chart hands us a free 3-way split, §3.2(D)), (iii) **independent
   graded pieces**. None of these exist in the current job shape.
3. K16 t=8..11 "verification" was sized against the curve formulation. If the
   β-collapse survives t = 6,7, that job shrinks to two `t`-form systems in
   `t−1` variables and may not need the fleet at all. Sizing a fleet job
   against a formulation you are about to replace is the expensive error.
4. The u_s≥2 census (1359 classes) is a *multiplier* on a kill method. We do
   not yet have a method that has finished **one** of the 12 residual fibres.
   Multiplying an unfinished method by 1359 is how a campaign converts
   compute budget into a larger pile of `TIMEOUT`s. Defer until one fibre
   certificate exists.
5. The coverage proof is not a compute job at all (§4).

**Answer.** The single highest-value deployment is the **re-emission and
re-solve of the 12 residual fibres in graded, branched, certificate-producing
form** — because it is the only candidate that (a) can *finish* something,
(b) has real parallel structure (branches × primes), and (c) produces the
artifact the paper needs (an exact cofactor or a `dim = 0` certificate) rather
than a verdict string. Second: the U-NEGATIVE census (one lane-hour, decides a
scope leak). Third: K16 (β)-clause at t = 6,7,8. The 1359-class census is
fourth and should not be scheduled until (a) lands.

Two further framing corrections:

- The packet says the Moh residual kill "= theorem (T) = emptiness of the FULL
  descended monomial-Jacobian D1 ORDER chart". That is right, and I want to
  keep it right: emptiness means *no point with `c ≠ 0`*. In the graded
  formulation that is `c ∈ √I₀`, and `dim V(I₀) = 0` is a **sufficient**
  certificate, not an equivalent one. Do not let the graded reformulation
  slide into "dim > 0 ⟹ survives" (FALLACY *floor/attainment*).
- "partial shows UNIT `[1]` modular signals on several fibres + correct
  NONUNIT controls" (packet, on the running lane): correct controls are
  necessary and not sufficient. Per §3.1 Gap 1, no number of modular units is
  a char-0 kill without the rational cofactor. I would not let the phrase
  "MSOLVE is BREAKING this" into a synthesis without that rider.

---

## 5.5 Strongest proof attack and strongest falsification attack

**Strongest proof attack (this round).** Clause (β) of the β-collapse, at
general `t`. After §2 the entire K16 ray is: *the finite scheme
`V(C_1+B_1,…,C_{t−1}+B_{t−1})`, of Bézout length `≤ C(3t+1,t−1)` (its
top-weight parts are the `C_r`, whose hsop property gives properness), misses
the hypersurface `a_0 + b_0 + c_0 = 0`.* Every ingredient is now finite and
closed-form: the length is a binomial, the top-weight parts are the `C_r`
whose leading coefficients `λ_{C_r}(t)` are banked in closed form
(`support_leaders_compact.tsv`), and `a_0` is a unit. The attack is: compute
the `β = 1` slice's *leading system* (top-weight parts `C_r`, plus `c_0`) and
show that any common solution of the full inhomogeneous system would have to
degenerate into a zero of the leading system, which C-HSOP forbids. This is
the standard "no solutions at infinity ⇒ the perturbation cannot create one"
argument, and it is available only after the collapse.

**Strongest falsification attack.** Not on K16 — on the Moh finish. The chart
`C_n16m12_M6_13_ell3_s3` fibre `V4_3` (155 unknowns, 243 rows, target `x^3`)
is the one the grok46 lane flagged as having "`x`-directions present" and
which never returned any verdict at any degree bound. Take it graded (§3.2),
take the branch with the *largest* surviving generator drop, and search for an
`F_p` point with `c ≠ 0` by randomized specialisation of the free
positive-weight directions after the graded reduction. A single verified
`(P,Q)` with `J = c·x^3`, `c ≠ 0`, would falsify theorem (T) on a `u_s = 1`
row and would be the first honest positive signal above `D = 100` — worth more
than another `TIMEOUT`. The campaign has run this only as "low-support slices
die" (6-, 10-, 12-parameter), which is the *wrong end*: those slices are the
ones a survivor would not live in ("a survive, if any, needs the rich
coefficient space" — grok46's own words). The graded reduction is what makes
the rich space searchable.

## 6. Three idea cards

### CARD 1 — `K16-BETA-COLLAPSE` (NEW)

- **Target obstruction.** The K16 atom: `T_{t,2t−1}` a nonzerodivisor on `Γ`
  / `(V0)` for all `t`.
- **Mechanism.** A `G_m` action, not an identity. `wt(β) = t+1 ≠ 0` makes the
  `β ≠ 0` locus of the incidence a single orbit family, so the ∀ over
  `d_Γ(t)` points splits into the `β = 0` stratum and the `β = 1` slice.
- **Object.** `(α) V(C_1..C_{t−1}, c_0) = {0}` (free given C-HSOP) and
  `(β) 1 ∈ (C_r + B_r, a_0+b_0+c_0)`.
- **Dependencies.** B-HSOP (measured t ≤ 8, 17(rrrrr)); `a_0` a unit (banked
  TAIL-SPLIT); Sol's support table `wt(B_r)=t+1+r`, `wt(C_r)=2t+2+r`; the
  exact tail files `explicit_tail_t*_exact.txt`.
- **Cheapest discriminator.** t = 6,7,8: `dim/vdim` of `(C_r)` against
  `∏(2t+2+r)/(t−1)!`, and `reduce(1, ·)` on the `β = 1` slice. ≤ 30 min
  including one `brcr` re-emit for t = 7,8. Partially executed here: clause
  (α) lands at t = 6 in 40 ms; clause (β) at t = 6 was still running at seal,
  which is itself informative — (β) is the expensive half, confirming that the
  content of the atom now sits entirely in the `β = 1` slice.
- **Interpretation.** *Bézout identity holds and slice inconsistent at every
  `t` tested* → promote C-HSOP-BEZOUT as a lemma candidate; the whole K16 ray
  becomes clause (β) alone, and the uniform target is a finite-scheme
  avoidance rather than a curve nonvanishing. *Bézout fails at some `t`* →
  C-HSOP has excess intersection there; clause (α) becomes live and is itself
  a new, sharper handle (an excess component is a *named* object). *Slice
  consistent at some `t`* → (V0) is FALSE at that `t`, which would be a major
  negative result and immediately checkable against the banked control.
- **Stop condition.** If the `β = 1` slice at t = 6 neither returns nor admits
  a modular verdict in 30 min, stop and report the collapse as a
  reformulation only (it is still worth banking: it removes `d_Γ(t)` from the
  statement).
- **Expected information gain.** High. Either it retires the "growing curve"
  framing that has defeated seven lanes, or it produces the first *located*
  failure (an excess component / a consistent slice) in the whole K16 ray.

### CARD 2 — `MOH14-GRADED-BRANCHED-KILL` (NEW instrument on a KNOWN target)

- **Target obstruction.** Emptiness of the 12 full descended D1 order charts
  (theorem (T) for the `u_s = 1` rows) — the Moh ≤100 finish.
- **Mechanism.** Change the *system*, not the engine: drop `T·c−1` (the only
  inhomogeneous element, `MEASURED-HERE`), substitute the forced weight-zero
  unknowns, normalise the remaining weight-zero unknown, take the explicit
  monomial case split, and decide `dim = 0` by a graded standard basis.
- **Dependencies.** The emitted charts (banked, pre-09:29Z); `builder_fix.py`
  (17(rrrrrr)); the weight inference (§9 upgrade); the lead normalisation
  `lead(h) = y^K` to license `h_1_7 = 1` — **this must be discharged, not
  assumed**, and the `h_1_7 = 0` branch (209 generators) run regardless.
- **Cheapest discriminator.** The 77-unknown chart already prepared here:
  graded `wp` `std` of 397 generators in 75 unknowns mod 32003, with a
  degree-truncated fallback. If it returns `dim`, we have the first real
  verdict on any residual fibre. ≤ 1 lane-hour.
- **Interpretation.** *`dim = 0`* → fibre DEAD; that is a complete certificate
  modulo the `h_1_7` branch and modular→rational promotion, and the method
  then runs on the other 11. *`dim > 0`* → NOT a survive; extract the
  components and ask whether any avoids `V(c)` — a much smaller question on a
  reduced system. *Still `TIMEOUT`* → the wall is genuinely the solver, and
  17(ssssss)'s typing is vindicated; then msolve/CRT is the only route and the
  fleet sizing is justified.
- **Stop condition.** Two graded attempts (full, then branch-split) per fibre;
  then hand to msolve with the graded generators (which msolve also prefers).
- **Expected information gain.** Very high and *cheap*. Any of the three
  outcomes is decisive about the nature of the wall, which is currently the
  campaign's biggest unforced uncertainty.

### CARD 3 — `US1-DESCENT-INDUCTION` (NEW mechanism, KNOWN rows)

- **Target obstruction.** The same 12 rows, without any chart.
- **Mechanism.** At `u_s = 1` the Prop 6.3 descent `y = γ^{−1}` is a strict
  degree drop `n → n/d_s ≤ 50`. Ask whether the descended datum is a
  legitimate instance of the ≤100 statement at the smaller degree; if so all
  12 die by Moh's own induction.
- **Dependencies.** Moh Prop 6.3/6.4 (read the page image — banked note: the
  descent is an explicit substitution and `J` is a `γ`-monomial, so
  `π`-degree screens are vacuous); the descent law closed form
  (`u_s = d_s − V_s`, `n' = (n/d_s)u_s`, `ℓ = v_s−u_s−1`); Prop 6.3 radius
  dichotomy (at `u_s = 1`, `δ* ≥ v_s/u_s` is *automatic* — 17(gggggg)).
- **Cheapest discriminator.** For the 12 rows, compute `(n/d_s, m/d_s)` and
  test whether the descended pair satisfies Moh's (1)–(13) as a *degree-`n'`*
  datum. If any row's descended datum is (1)–(13)-inadmissible at degree
  `n' ≤ 50`, that row dies immediately by the ≤100 induction hypothesis.
  ≤ 45 min with the banked enumerator.
- **Interpretation.** *Some rows die* → the chart batch shrinks below 12 and
  the fleet job shrinks with it. *No row dies but the descended data are
  legitimate instances* → the missing bridge lemma is the whole finish, and it
  is a *reading* task (Moh's induction structure), not a compute task. *The
  descended data are not instances at all* → bank the reason; that reason is
  the precise content of the `s' ≥ 3` program artifact
  (`OPEN[MOH-PROGRAM-ARTIFACT]`, 17(jjjjjj)).
- **Stop condition.** One lane; if the bridge lemma needs a hypothesis Moh
  does not supply, stop and report the hypothesis.
- **Expected information gain.** Medium-high, and it is the only card that
  could make the compute unnecessary. Cheap enough to run beside Card 2.

---

## 7. The single first lane

**`moh14-graded-branched-kill-opus5`** (Card 2). One lane, ≤ 1 lane-hour on
math-hq, no fleet.

Scope: the two already-full charts with the smallest unknown counts
(`Mm12`/77 and `M2_9 V3_8`/88). Deliverables: (i) the weight vector inferred
and cross-checked against the compiler's declared `K` for both charts; (ii)
the graded ideal with `T·c−1` removed and the forced weight-zero unknowns
substituted, with a **replay gate** (the graded ideal must reduce the original
generators to zero after re-homogenisation); (iii) a `dim` verdict or an
honest `TIMEOUT` with the degree reached; (iv) if `dim = 0`, the rational
promotion attempt; (v) the `h_1_7 = 0` branch run separately and its
normalisation discharged, not assumed.

Why this and not Card 1: Card 2 is on the *finishable* target and all three
of its outcomes are decisive; Card 1's cheapest test is 30 minutes and queues
as a second lane. Why not defer to msolve: msolve is a different **engine** on
the *same* system, this lane changes the **system** — independent, and the
results cross-check, which is what a `TIMEOUT`-only history needs.

Explicitly not launched now, with reasons: the 1359-class census (§5, premature);
the coverage proof (not compute); K16 t=8..11 in the old formulation (§5.3).

---

## 8. Running lane: `moh14-msolve-sol56` — CONTINUE, with a rider (receipt only)

Receipt state only: `initial_status=RUNNING`, `start_utc=2026-09-05T09:29:37Z`,
`basis=15fc16a9`, 8 charged inputs, no `final_status`. I did not read the
report.

**CONTINUE** to its existing budget — it is cheap, it is the first msolve
data point the campaign has, and a fast-solver baseline is worth having
regardless of outcome. **Do not extend it** and do not queue follow-on fleet
capacity against it before Card 2 reports.

Rider for whatever it returns:

1. Any `UNIT` must be typed `MODULAR-SIGNAL` until an exact rational cofactor
   is produced and verified (§3.1 Gap 1). "msolve is breaking this" is not yet
   a promotable sentence.
2. Its verdicts are per fibre; the class logic is conjunctive over 12 fibres
   (§3.1 Gap 2). A synthesis line of the form "k of 6 classes closed" needs
   the fibre denominator beside it.
3. If it stalls, the correct next step is **not** a bigger box: it is the
   graded system (§3.2), which is a strictly smaller problem in strictly fewer
   variables with no Rabinowitsch generator.

---

## 9. Systems upgrade (one, independent of the mathematical proposal)

**UPGRADE — `ops/chart_grading.py`: a mandatory pre-solve grading gate.**

Rotation slot: *reproducibility / decisive-experiment quality*.

Problem, evidenced: six charts were emitted, dispatched to a 247 GB
big-memory tier, and burned hours of fleet time in an ungraded `dp` ring —
while the generator set was **exactly weighted-homogeneous** and carried a
free three-way case split and a variable-valued generator. Nothing in the
pipeline looked. The information needed to see it costs about ten seconds per
chart.

Smallest useful implementation (one file, ~120 lines, no new dependencies):

1. **Infer.** Parse the emitted generators, build the homogeneity equations
   over the variable families, and solve exactly (rational Gaussian
   elimination). Emit the weight vector, the rank, and the count of
   inconsistent rows.
2. **Report.** Weight-zero variables; generators that are a single variable
   (forced zeros); generators that are a single monomial (free case splits);
   the family-constant identities (here `W = (K, K, 2K, 3K, 2K)`,
   `w(c) = 5K−3`), cross-checked against the compiler's declared `K`.
3. **Gate.** If a grading exists and the job's ring is ungraded, **refuse**
   and print the `wp` ring line and the substitution list; allow an explicit
   `--ungraded-ack` override that is recorded in the manifest.
4. **Record.** Write the grading into the chart manifest so downstream
   verdicts can be replayed and so `GG__DIM`/`UNIT` labels can be audited
   against the ring they were computed in.

Smallest useful test: run it on all 6 emitted class charts and diff the
recovered `W` against the compiler's `K` per class; the prototype run in this
lane (1,155,984 equations, rank 6, 0 inconsistent, agreeing with Singular's
`homog(I) = 1`) is the regression fixture. Measured benefit if the gate had
existed: it would have blocked the ungraded 58-minute/11.2 GB r7i run.
Regression risk: low — it is read-only and advisory except for the refusal,
which is overridable. Opportunity cost: under an hour.

Second-best candidate, recorded and not chosen: the CRT cofactor-lift helper
(§3.1). It is the right long-run instrument and the natural sequel; the
grading gate goes first because it changes the system the cofactors would be
computed for.

---

## OPENS RAISED (section 10)

**OPEN[K16-BETA-COLLAPSE]** — the `G_m` reduction of the K16 atom to two
0-dimensional clauses.
QUANTITY: decide whether `(V0) ⟺ (α) ∧ (β)` holds for every `t ≥ 3`, i.e.
whether `V(C_1..C_{t−1}, c_0) = {0}` and the `β = 1` slice ideal `= (1)`,
given B-HSOP and `a_0` a unit.
CHEAPEST TEST: Singular `dim`/`vdim` + `reduce(1,·)` on the banked
`explicit_tail_t*_exact.txt` forms in `wp(1..t−1)`, at `t = 6,7`; gate is
`dim = 0 ∧ vdim = ∏(2t+2+r)/(t−1)!` and `reduce(1, slice) = 0`; ≤ 30 min.

**OPEN[C-HSOP-BEZOUT]** — the `C_r` are a regular sequence of generic length.
QUANTITY: decide whether `vdim(C_1,…,C_{t−1}) = ∏_{r=1}^{t−1}(2t+2+r)/(t−1)!`
for all `t ≥ 3` (verified `= 45, 286, 1820` at `t = 3,4,5`, exact at `t=3,4`).
CHEAPEST TEST: same instrument at `t = 6,7,8`; gate is equality of the two
integers; ≤ 20 min. Already `= C(19,5) = 11628` at `t = 6` (40 ms, `p=32027`)
here, so the open question starts at `t = 7`. A proof route is a leading-form/initial-ideal argument of
the same shape that settled B-HSOP.

**OPEN[MOH14-GRADED-DIM]** — the graded emptiness certificate for the residual
fibres.
QUANTITY: decide whether `dim V(I₀) = 0` for the 75-unknown positively graded
ideal `I₀` of chart `C_n24m16_Mm12_m2_5_ell1_s4` (and its 11 siblings), where
`I₀` is the chart with `T·c−1` removed, `A1_1_7 = 0`, `h_1_7 = 1`.
CHEAPEST TEST: graded `std` in `wp(w_1..w_75)` mod 32003, with a degree
truncation; gate is `dim(std) = 0` (a complete kill) or the degree reached at
timeout; ≤ 1 lane-hour. Launched here; unfinished at seal.

**OPEN[MOH14-LEAD-NORMALISATION]** — the licence for `h_1_7 = 1`.
QUANTITY: decide whether the chart's weight-zero unknown `h_1_7` is bounded
away from 0 by the emitter's `lead(h) = y^K` gate, i.e. whether the branch
`h_1_7 = 0` is empty or must be solved separately (it has 209 generators, at
most 73 unknowns).
CHEAPEST TEST: read the `builder_fix.py` normalisation and the `lead(h)=y^K`
gate, then run the 209-generator branch graded; gate is a written derivation
plus a `dim` verdict; ≤ 30 min.

**OPEN[US1-DESCENT-INDUCTION]** — the bridge from a descended `u_s=1` datum to
a smaller instance.
QUANTITY: decide whether each of the 12 rows' descended datum, of degree
`n' = n/d_s ≤ 50`, is a legitimate instance of Moh's ≤100 induction
hypothesis; equivalently bound the number of the 12 rows that survive the
(1)–(13) sieve *at the descended degree* (currently `≤ 12`, unknown, plausibly
`< 12`).
CHEAPEST TEST: run the banked (1)–(13) enumerator on the 12 descended data;
gate is admissibility at degree `n'`; ≤ 45 min.

**OPEN[U-NEGATIVE-CENSUS]** — the size of the uncharted third configuration.
QUANTITY: bound the number of `D ≤ 200` admissible rows with `V₂' > d₂'`
(U-NEGATIVE); currently unmeasured, so the bound is `≤` the full 1,420-row
census.
CHEAPEST TEST: one pass of the banked skeleton enumerator with the `V₂' > d₂'`
predicate; gate is the count; ≤ 1 lane-hour. If the count is `0` at `D ≤ 200`
the leak closes by enumeration in that range and coverage becomes the top
scope gap; if it is large, U-NEGATIVE is a flagship and the "plane JC2 for
minimal counterexamples" reading of 17(pppppp) needs its caveat strengthened.

**OPEN[MODULAR-UNIT-PROMOTION]** — the standing promotion rule.
QUANTITY: decide whether each fibre's modular `UNIT` lifts, i.e. whether an
exact cofactor vector with `1 = Σ f_i g_i` over `Q` exists with cofactor
degree `≤ D` for some `D` reached in budget.
CHEAPEST TEST: CRT + rational reconstruction of the cofactors from ≥ 3 primes,
then exact verification by multiplication; gate is the exact identity `= 1`;
verification is seconds, reconstruction is the cost. This is the promotion
obligation for every `UNIT` the running lane may report.

### COLLISION SCAN

`ops/open_collision.py` output is appended below the seal marker in
`xmodel/ideation-20260905T1200Z-opus5.collisions.md` and reproduced in §11.
The scanner's corpus guard excludes same-round submissions automatically.
Collision hits are review candidates, never closures.

## 11. Run ledger (what finished, what did not) and collision block

`MEASURED-HERE` results are only worth what their runs are, so here is the
honest state at seal.

| run | status at seal |
|---|---|
| K16 β-collapse, t = 3, exact over `A_3` | **COMPLETE** — `dim(C)=0 vdim=45`; slice inconsistent; control `dim(I₂(N)+W)=0` |
| K16 β-collapse, t = 4, exact over `A_4` | **COMPLETE** — `vdim=286`; slice inconsistent (25 ms); control 63 ms |
| K16 β-collapse, t = 5, mod 32003 | **COMPLETE** — `vdim=1820`; slice inconsistent (4 ms); control `dim=0` (5 ms) |
| K16 β-collapse, t = 5, exact over `A_5` | **UNFINISHED** (rational coefficient blow-up; the modular run stands in) |
| K16 β-collapse, t = 6, mod 32027 (`H_6` irreducible) | **PARTIAL** — clause (α) `vdim=11628` (40 ms), `vdim(B)=792`; clause (β) still running. A first attempt at `p=32003` was discarded (`H_6` reducible there). |
| Moh chart homogeneity solve (1,155,984 eqs) | **COMPLETE** — rank 6, 0 inconsistent |
| Moh chart zero-propagation / branch census | **COMPLETE** — `A1_1_7 = 0` forced; 3-way split; `h_1_7=0` → 209 gens |
| Moh chart pivot elimination (27 candidates, cap 1500) | **COMPLETE, NEGATIVE** — 0/77 eliminated |
| Moh graded `std` (397 gens, 75 unknowns, `wp`, mod 32003) | **UNFINISHED** — printed `NGENS 397`, `HOMOG 1`, then still computing |

Two consequences on the record. The structural claims of §2 and §3.2 do not
depend on the two unfinished runs — homogeneity, the weight vector, the forced
zero, the case split, the failed pivots and the `t = 3,4,5` verdicts are all
complete. But the *speed* claim implicit in §3.2 — that the graded system is
easier than the saturated one — is **not demonstrated**, and I do not assert
it; that is the first lane's job (§7). If the graded `std` also times out,
§3.2 still delivers the split, the forced zero and a saturation-free
certificate criterion, and 17(ssssss)'s "solver wall" typing is vindicated.

**COLLISION BLOCK.** `ops/open_collision.py` was run on the unsealed report
(`--root .`, exit 0). Verbatim output is in
`xmodel/ideation-20260905T1200Z-opus5.collisions.md`. Summary:
`status: CANDIDATES`; 7 OPENs extracted; hits on
`OPEN[C-HSOP-BEZOUT]` (3 candidates — the most relevant is
`k16-hsop-length-allt-opus5-20260903`, whose banked lengths 90, 572, 3640,
23256 are **exactly `2 × ` my `vdim(C)` values**, which is the §2.35 identity
and is a genuine, deliberate overlap, not a duplicate result),
`OPEN[U-NEGATIVE-CENSUS]` (many low-precision lexical hits on "negative", none
about `V₂' > d₂'`), and `OPEN[MODULAR-UNIT-PROMOTION]` (hits on the banked
PROMOTION LEMMA 17(iiii) — that lemma is about DVR properness and is the
*right* neighbour to read before building the CRT lift). `NONE` for
`OPEN[K16-BETA-COLLAPSE]`, `OPEN[MOH14-GRADED-DIM]`,
`OPEN[MOH14-LEAD-NORMALISATION]`, `OPEN[US1-DESCENT-INDUCTION]`. The scanner's
corpus guard excluded same-round submissions. Hits are review candidates,
never closures.

## 12. Summary for the coordinator

The K16 atom is not a curve problem: `β` carries weight `t+1`, `G_m` acts
transitively on the nonzero-`β` slices, and `(V0)` collapses to two
0-dimensional clauses, one of them free — verified against the banked verdicts
at t = 3,4,5 (and the free clause at t = 6), with the banked LENGTH-SPLIT
falling out as `d_Γ(t) = [vdim(C) − vdim(B)]/(t+1)`.
The Moh ≤100 residual is not purely a solver wall: the 77-unknown chart is
exactly weighted-homogeneous, `T·c−1` is its only inhomogeneous element, one
generator is a variable, another is a monomial giving a free three-way split,
and in graded form `dim = 0` is a complete kill certificate needing no
saturation.
So the highest-value deployment is the graded, branched,
certificate-producing re-solve of the 12 residual fibres — not the 1359-class
census — and no modular `UNIT`, on any number of fibres, is the ≤100 finish
until an exact rational cofactor is reconstructed and verified.

<!-- BODY-END -->
