# Whole-portfolio ideation — Opus 5 — `20260828T1707Z`

Lane: Opus 5 (`claude-opus-5`), blind whole-portfolio researcher.
Packet: `xmodel/ideation-20260828T1707Z-packet.md`,
SHA-256 `1e40e7106e2a3c16b6a6fe92e6d2387228fb1260ae5633e686b456e9f9d95f1c` — **verified before reading**.
All seventeen custody hashes verified `OK`; `git rev-parse HEAD` = `418e413593120d19e15e6546eb50c985f4b1f038`.
No peer `1707Z` response was read (none existed; see §11 disclosure).
`jc2-lean` was not entered, listed, searched, read, built, modified, status-checked or controlled.
No AWS, Singular, msolve, Sage, Lean, or heavy local algebra was used.

**This report does not claim a proof or a counterexample to JC2.** It contains one
new candidate theorem (`ROOT-W2`, §3), one new decision oracle (`ROOT-REACH`, §3),
one new mechanism (`A47`, §5), and a reranking. Everything new here is
`INTERNAL-UNREVIEWED / PROVISIONAL` and requires the ordinary different-model gate.

---

## 1. Answers to the seven packet questions, in one page

| # | question | verdict |
|---|---|---|
| 1 | Compose MFE literally on residue A | **NO HIT.** `Σλ^exit = 2 ≤ td−1−ψ = 3`, slack 1 — numerically identical to the budget already recorded in `SHEET6-2POLE §6a`. MFE *hardens* the survivor: it removes the last conditionality from that budget. No sound refinement can price the resonant orbit: it carries no flag (§2). |
| 2 | Push the root identity | **HIT.** `(R2)` has **no `μ` hypothesis**. Composed with promoted `L1a(b)` + `DS2/DS3`, it excludes **every** root merge (any `μ`) in the two-pole `td=6` sector — `ROOT-W2`, §3. Generalizes to a cap-free finite oracle `ROOT-REACH` that decides 41 of the 57 on-axis `td=6` entries by arithmetic alone. First exact missing implication stated in §3.4. |
| 3 | Find a global composition | **PARTIAL HIT.** No new `td`/degree ceiling. One literal new interface: `A47`, the resonant-direction budget carried by the exact identity `J(f,h_1)=α·g^{α−1}` (§5). |
| 4 | Attack the concrete survivor | Cheapest decisive test = **`RIGID-TRANSPORT`** (Card 1, §8): the `⊖`-constant / substitution compatibility of Prop 8.1(iv) *across one chain edge*, between the two independently pinned rigid patterns. |
| 5 | Optimize the GGV recursion | **Fitting-level syzygy/module presentation, not a minor atlas** (§6). Chart complements are the wrong object; Fitting ideals are canonical, finite, totally ordered and have no complements to recurse into. |
| 6 | Re-rank proof vs disproof | The under-resourced route that can beat both backbones is **the `w`-alphabet arithmetic** (§3, §7): zero compute, cap-free, and it just produced `ROOT-W2` and `ROOT-REACH` for free. |
| 7 | Accelerate software | **`ALPHABET`**: a cap-free closure compiler replacing capped BFS engines — the exact class of instrument that produced the campaign's last two false closures (§7). |

---

## 2. Question 1 — MFE composed literally on residue A

### 2.1 The composition

Residue A's exhibit (`SHEET6-2POLE §6a`, promoted; child uniqueness from
`SHEET6-L1 §5–6`). Both poles are row 1 of table (23), type `(α,β)=(2,3)`:

```text
U^full = { P1, P2 } ∪ { G_m } ∪ { F } ∪ { (0,y) }      (shared suffix once)

P1,P2 : Q=(2,2,2,2,5)     λ^exit = 0   (Prop 5.5 ⇒ every puncture has g=∞;
                                        St 7.2 ⇒ Y(P_i)=∅ — not a budget choice)
G_m   : Q=(6,12,3,2,5)    λ^exit = 0   (k=0 merged pattern; the *other* chain's
                                        orbit is searrow and never λ-charged)
F     : Q=(42,126,7,3,5)  λ^exit = 2   (μ=2, IIa k=1 suffix step)
(0,y) : terminal, case IV, R=3;  ψ = ceil(k_f/l_f) − 1 = ceil(126/42) − 1 = 2
```

`Σ_{F∈U^full} λ_F^exit = 2`; `td − 1 − ψ = 6 − 1 − 2 = 3`. **MFE holds with slack 1.**
Machine-checked exactly (`CHECK 1`, §11). The same computation on all four
surviving IV classes (`(1/3,7,3,5)@2`, `(2/3,3s+2,3,2s+2)@2`, `(1/4,5,4,4)@2`,
`(3/4,4s+3,4,3s+3)@2`) gives `2 ≤ 3` in every case: **NO HIT ×4**, no terminal-menu
sharpening.

### 2.2 The consequential reading — MFE hardens the survivor

This is the load-bearing point and it runs against the intuitive direction.
`SHEET6-2POLE §2b.3` previously carried the shared two-pole budget as
*conditional* on an unproved cross-chain/shared-suffix disjointness lemma. MFE
proves that lemma. The exhibit's verdict therefore moves from
"CONSISTENT-EXHIBIT modulo a budget hypothesis" to
**"CONSISTENT-EXHIBIT, budget-unconditional"**. The 17:03Z promotion is, net,
a small negative for the proof side at `td=6` and should be recorded as such.

### 2.3 Can a sound refinement price the q-only resonant orbit? — **No, structurally**

The resonant orbit at `G_m` is `(η³ − b)` with `b` **not** a root of `p_{G_m}`.
By Statement 3.18 a flag `F * c` exists only at a root `c` of `p_F`. Hence the
three directions `η³ = b`:

- carry **no tree vertex** of `T_a`,
- carry **no cv-vertex** (`T_{a,cv} ⊂ T_a^0 ⊂ T_a`),
- carry **no puncture, no pole, no `λ`, and no `Y(F)` membership**.

MFE, `(C7.1*)`, `(22)`, `(22-cl)`, `δ_a`, every `λ`-rule and every `ψ`-rule are
functions on `T_a`. **Every one of them is identically blind to the resonant
orbit**, which is the sole reason `M(G_m) = gcd(6,10) = 2` instead of
`gcd(6,7) = 1`, and therefore the sole reason residue A escapes restored
Proposition 8.4. This reproduces `SHEET6-L1 §3` independently and upgrades it
from "no printed statement sees it" to "no `T_a`-supported functional can ever
see it".

**Operational consequence — stop.** Further refinement of the `λ`/exit budget
cannot kill residue A, no matter how sharp. Any charge must come from an
object living **off** `T_a`. Two such objects exist and are named in this
report: the auxiliary-`h` branch structure (`A47`, §5) and the coefficient/
substitution layer (`RIGID-TRANSPORT`, §8 Card 1). Reallocate accordingly.

---

## 3. Question 2 — pushing the root identity: `ROOT-W2` and `ROOT-REACH`

### 3.1 The observation

The 16:59Z integration derives, for a genuine (contact-zero) root merge with
lower `F=(0,y)`, upper parent `G=F+c`, `μ = mult(p_F^red,c)`:

```text
X_root = D_F/i = μ(1 − w_G)            (R1)
⇒  w_G = 1 − X_root/μ < 1              (R2)   [uses only D_F>0, i>0, μ>0]
```

and then *specializes* to the all-`μ=1` anatomy to get `w = l/(r+l) ∈ (0,1)`
`(R3)`, contradicting `W={2}`. **`(R3)` is not needed for the contradiction.**
`(R2)` alone already says `w_G < 1`, and it carries **no hypothesis on `μ`**
at all. Verified symbolically (`CHECK 4/5`, §11): `(R3)` is a strict special
case of `(R2)`.

### 3.2 Candidate theorem `ROOT-W2`

> **`ROOT-W2` (candidate, INTERNAL-UNREVIEWED).** In the two-pole `td=6`
> configuration (`m=2`; both poles row 1 of table (23); type `(2,3)`, forced by
> `Λ=3+3` via Prop 5.8(20)/5.7/9.1), **there is no root merge, for any
> multiplicities `μ`.**

*Proof.* (a) `L1a(b)` (PROMOTED, `SHEET6-L1 §2`, `SHEET6-A3L1-REVIEW`): every
chain vertex strictly above the meet has `M=1` and reduced pattern a **single
simple `ν`-orbit** `(dp,dq) = (ν, nν+1)`, `λ=0`. Its proof is an induction from
the pole using the third-pole argument (St 8.2 + St 8.4 + Prop 6.8) and never
uses whether the meet is interior; when the meet is `(0,y)` it covers the whole
chain.
(b) `DS2` (`SHEET6-DEPTH §3`, PROVED, machine-verified): along such an edge
`w_F = w_G · n_F/Δ_F`, `Δ_F=(n_F−1)ν_F+1`. `DS3` (`§4`): a resonant step
`n_F ≥ 2` requires `Δ_F | num(w)` with `Δ_F ≥ 3`.
(c) Entry pin (`§4`, and directly from `Q(P_i)=(2,2,2,2,5)`):
`w_0 = (κ̄ − D/deg p)/ν = (5 − 1)/2 = 2`. `num(w_0)=2` has no divisor `≥3`, so
no resonant step is admissible and `W(2) = {2}`. Every candidate parent `G` of a
root edge therefore has `w_G = 2`.
(d) A genuine root merge is Prop 9.3 case I with `F,G ∈ V_a ∩ T_a^↘`, `D_F=l_f>0`
(Thm 6.1). `(R2)` gives `w_G < 1`. But `w_G = 2`. Contradiction. ∎

*Consequences.* (i) The retracted `twopole_check.py` phase-3 zero is **restored
analytically, for all `μ`**, with no engine, no caps and no AWS census.
(ii) The two-pole `td=6` book is exactly `{residue A + its 4 IV classes}` — the
packet's open item "mixed-`μ` root-merge completeness" is closed **for `m=2`**.
(iii) The queued root-aware AWS recensus loses its `m=2` justification; its
remaining scope is `m≥3`, SF1 and off-axis.

*Exact attack surface for a hostile reviewer (please attack in this order).*
1. Does `L1a(b)`'s third-pole induction really run when the meet is `(0,y)`?
   (`(0,y)` has special status in St 8.5 and Prop 8.3(iii).) This is the single
   most fragile step.
2. Is `w_G` at the last chain vertex the same `w` that `(R2)` constrains? Both
   are `(κ̄_G − D_G/deg p_G)/ν_G`; confirm no `i`-normalization mismatch.
3. Does `(R2)` need `G ∈ V_{1,a}` (it does not, as written) or `ν_G ≥ 2`?
4. Zero-length chains: the meet is `P_i°`, parent `= P_i`, `w = 2`. Covered.
5. Negative control: exhibit an entry whose `W` **does** meet `(0,1)` and check
   the argument correctly fails there — `(a,α,β,ν) = (2,2,3,3)`, `w_0 = 8/3`,
   `W ∋ 2/3` (§3.3 table).

### 3.3 `ROOT-REACH` — a cap-free root-merge oracle

`ROOT-W2` generalizes to a decision procedure. `DS3`'s contraction makes
`W(w_0)` finite and computable; the entry pin (MP4) gives
`w_0 = a(b(α+β)−1)/(bν)`, `Λ = abαβ/ν`, and on-axis `b=1` means `M=1`, so
`DS2/DS3` apply.

> **`ROOT-REACH` (oracle).** For an on-axis entry, if `W(w_0) ∩ (0,1) = ∅` then
> **no root merge is possible on a chain from that entry**.

Because my closure ignores the per-edge congruence `n_e ≡ −κ̄_e (mod ν_e)`,
`W` is an **over-approximation**: `excluded` verdicts are sound; `not excluded`
is not a proof. Computed exactly for every on-axis `td=6` entry
(`Λ ≥ β`, `Λ ≤ td`, `1<α<β≤td`, `gcd(α,β)=1`) — 57 rows, 41 excluded:

```text
(a,α,β,ν)   Λ  w0    W(w0)                     root merge?
(1,2,3,2)   3  2     {2}                       EXCLUDED   <- the two-pole row-1 entry
(1,2,3,1)   6  4     {2,4}                     EXCLUDED
(1,2,5,2)   5  3     {2,3}                     EXCLUDED
(1,3,4,3)   4  2     {2}                       EXCLUDED
(5,3,4,12)  5  5/2   {1,3/2,5/2}               EXCLUDED   (min = 1, not < 1)
(1,4,5,4)   5  2     {2}                       EXCLUDED
(1,5,6,5)   6  2     {2}                       EXCLUDED
...
(2,2,3,3)   4  8/3   {2/3,4/3,8/3}             not excluded
(5,2,3,6)   5  10/3  {2/3,4/3,2,10/3}          not excluded
(3,2,5,5)   6  18/5  {2/5,4/5,6/5,8/5,2,12/5}  not excluded
(1,3,5,3)   5  7/3   {2/3,1,4/3,7/3}           not excluded
(2,3,5,5)   6  14/5  {2/5,4/5,6/5,8/5,14/5}    not excluded
(3,4,5,10)  6  12/5  {2/5,4/5,6/5,8/5,12/5}    not excluded
```

Full 57-row table reproduced by `/tmp/opus5_rootreach.py` (§11). **This replaces
a planned AWS census by ~0.4 s of exact integer arithmetic on 41 of 57 entries.**

### 3.4 First exact missing implications (the packet asked for these literally)

1. **Post-jump `w`-law.** `DS2/DS3` are stated only for `M=1` segments. For
   `m ≥ 3`, a chain may pass an interior jump (`M ≥ 2` child) before reaching the
   root, and `w` below that jump is uncontrolled. *Missing:* the analogue of
   `DS2` for an `M ≥ 2` segment, i.e. how `(κ̄, D/i, ν)` transforms under Prop 9.3
   (a)–(d) when `μ_e ≥ 2`. This is elementary Prop 9.3 arithmetic; it is the
   single cheapest unblocked item in the whole Sigray lane.
2. **Off-axis entries.** For `b ≥ 2` the entry has `M = b ≥ 2`, so the `w`
   recursion does not start. *Missing:* an off-axis entry-frame invariant playing
   the role of `w`. Without it, `ROOT-REACH` says nothing off-axis, and the
   packet's "off-axis root completeness" stays genuinely open.
3. **The congruence refinement.** Adding `n_e ≡ −κ̄_e (mod ν_e)` and `κ̄ ∈ ℤ` to
   the closure would turn the over-approximation into the exact reachable set and
   would likely close several of the 16 `not excluded` rows.
4. **`(R3)` beyond all-`μ=1`.** Do **not** extend `w = l/(r+l)`: it uses
   Prop 8.1(iv) top-degree cancellation at `u=0` with `(dp,dq)=(r,r+l)`. The
   correct mixed-`μ` form is `X_root = dp/dq = μ_tot/(r+l+e_0)` with
   `μ_tot = Σμ_j`, `r = #`distinct roots, `e_0 ∈ {0,1}` the `η`-factor — derivable
   from the same cancellation plus the ROOT LAW/ETA LAW of `SHEET6-L1 §1a`, but
   **not proved here**.

---

## 4. Question 3 — global composition attempts

**Ceilings: `NO HIT`.** I re-examined Riemann–Hurwitz on `ĝ`, the pole-mass
identity `td = ΣΛ(F)`, Euler/genus, terminal orbit laws, and the Jelonek/
conductor family. Each recombines to an identity the campaign already holds, or
needs an input (a bound on the Puiseux denominator `κ_i` at infinity) that `td`
provably does not control — `SHEET6-DEPTH §2 R1` is explicit that `κ_i` is not
bounded by `(m,td)`, which is the structural reason no depth cap and no cofinal
`td` ceiling has appeared in this frame. I found nothing that changes this.

**Topology at infinity: `PARTIAL`.** van Dobben de Bruyn arXiv:2608.27341 gives
a boundary-graph filter (a multiplicity-`k>1` intersection forces a non-linear
`D_{k+2}` dual graph, obstructing `A²`). That filter now has, for the first
time, a *fully pinned* input: residue A's boundary data are determined up to two
scales. See §9 (Avenue 27 `reopen`).

**One literal new interface: `A47`.** See §5.

---

## 5. New mechanism `A47` — resonant-direction budget via the auxiliary Jacobian

### 5.1 The identity

Sigray's auxiliary family (Not 8.1) has first member `h = h_1 = g^α − s_0 f^β`
(for the normalized type `(α,β)`; `(2,3)` here). With `J(f,g)=1`:

```text
J(f,h) = J(f, g^α − s_0 f^β)
       = α g^{α−1} J(f,g) − s_0 β f^{β−1} J(f,f)
       = α · g^{α−1}.                                    (A47.1)
J(h,g) = −s_0 β f^{β−1}.                                 (A47.2)
```

For `(α,β)=(2,3)`: `J(f,h) = 2g`, `J(h,g) = −3 s_0 f²`.

I searched the files I read for these identities and did not find them. The
ledgers use the `h`-family only through (i) `M_F = gcd(deg p_F, deg p_{h_j,F})`
(Not 8.1) and (ii) the *pattern* ODE Prop 8.1(iv) `δ p q′ − (1−u) p′ q = ⊖p`,
where `q` is the reduced `h`-pattern. **`h` is never treated as the second
coordinate of a map with a known, non-constant Jacobian.**

### 5.2 Why this is the right object for the resonant orbit

`q_F = p_{h,F}^red`. The resonant directions are precisely
`Res(F) := roots(q_F) \ roots(p_F)`: places where `h` degenerates and the fibre
`f = a` does not continue. By `(A47.1)` the ramification of the map `(f,h)` is
supported exactly on `{g = 0}`, with multiplicity `α−1` — for `(2,3)`, the
**reduced** curve `{g=0}`. So the resonant directions are not arbitrary: they
are constrained by the boundary behaviour of a single, explicitly known divisor.

Additionally `[ℂ(f,g):ℂ(f,h)] = 2` (as `g² = h + s_0f³` and `g ∉ ℂ(f,h)` unless
degenerate), so `td(f,h) = 2·td = 12`: a second, larger, fully determined
covering whose ramification divisor is named.

### 5.3 Literal theorem interface (`A47-BUDGET`)

> **To prove.** Let `(f,g)` be a normalized counterexample of type `(α,β)`,
> `h = g^α − s_0 f^β`, and for `F ∈ V_a` let `l_F := |Res(F)| / ν_F` be the number
> of resonant `ν_F`-orbits. Then the assignment
> `(F, b) ↦ (the branch of h at infinity through the flag F * b)`
> is **injective** on `{(F,b) : F ∈ V_a, b ∈ Res(F)}`, and
> ```text
> Σ_{F ∈ V_a} l_F · ν_F  ≤  N_∞(h) − N_∞(h ∩ f=a),          (A47-BUDGET)
> ```
> where `N_∞(h)` counts branches of `h` at infinity in the fibre-`a` sector.

The injectivity half is **already available**: it is exactly the promoted
Definition 3.3 contact-quotient/unique-attachment argument (`f55a00f5…`,
`c74fc0f9…`) applied to a different witness family. That is the reason `A47` is
cheap: the hard combinatorial half of the new inequality has just been proved
for a neighbouring purpose. What is genuinely new is the right-hand side — and
`(A47.1)` is what makes it computable, because `{g=0}` is the whole ramification
locus of `(f,h)`.

**Discriminator on residue A.** `A47-BUDGET` predicts `LHS ≥ l·ν = 1·3 = 3` at
`G_m` alone. Residue A dies iff the sector count is `< 3`. I do **not** claim it
is; I claim this is the first inequality of the right *type*, and the first one
whose two sides are both explicitly computable from pinned data.

**Comparison with repository history.** `SHEET6-L1 §7.2(i)` names precisely this
gap: *"GLOBAL accounting of the extra q-orbit: b carries branches of
`h_1 = g² − s_0 f³` with no f-branch; nothing in §§3–9 counts h_1-branches at
non-p directions — a Newton-polygon/branch budget for `h_1` at infinity is the
natural candidate and would be new mathematics in the frame."* `A47` supplies
the missing structural input to that call: the ramification identity `(A47.1)`,
plus the observation that the injectivity half is already promoted. `L2` in
`SHEET6-2POLE §6c` asked for a Bezout transport through `G_m`; `A47` is not that
— it is a count of objects the printed frame does not enumerate at all.

---

## 6. Question 5 — the fastest complete treatment of the GGV rank-chart complements

**Recommendation: Fitting-level syzygy/module presentation. Not a minor atlas,
not chart-complement recursion, not saturation/radical covers.**

The current failure mode is structural, not tactical: a nonzero-minor chart can
only ever prove a statement on a dense open of one branch, so every result
returns `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`, and each complement spawns a
fresh recursion of the same shape. A minor atlas makes that combinatorially
worse (`C(106,105)`-scale charts per level). The correct object is not "the
kernel at a point" but "the kernel as a module".

### 6.1 Design

For each branch ring `R = A/I` (pinned ambient `std(I)`, NF after every
operation — the reducer-safe adapter that closed the `q2²` trap):

1. **Fitting stratification.** Compute `Fitt_r(M)` for `r` from the certified
   generic rank downward. These are canonical, chart-free, finitely many, and
   **totally ordered** — `V(Fitt_{r}) ⊇ V(Fitt_{r−1})`. Certified ranks
   (`9/104`, `6/101`, `4/99`) say the live drop is small, so the ladder is short.
2. **One syzygy computation per stratum.** On
   `S_r := V(Fitt_r) \ V(Fitt_{r−1})` the kernel has constant rank and the
   localized syzygy module **is** the kernel. Compute generators `k_1,…,k_s` of
   `Syz(M)` over `R_r`, verifying `NF(M·k_j) = 0` for every `j`.
3. **One endpoint decision per stratum.** Form the generic kernel element
   `κ(t) = Σ_j t_j k_j` and reduce the quadratic endpoint
   `E = x14·x72 + x1·x97` at `κ(t)`. The coefficient ideal `E_r ⊆ R_r` of
   `E(κ(t))` in the `t`-variables decides the stratum: `E_r = 0` ⟺
   `ENDPOINT_DEAD_AT_FITTING_LEVEL_r`; `E_r ≠ 0` ⟹ a survivor with an explicit
   nonzero witness (scalable to `E=1` over `ℂ`).

There are **no complements**: the strata partition the branch by construction.

### 6.2 AWS fanout

- Phase A (6 jobs, 16 vCPU / 128 GiB, zero swap): top Fitting level on each of
  `P`, `C8P02`, `Q1P02`, `Q1P03`, `TRIPLE02`, `TRIPLE03`.
- Phase B (launched only where `Fitt_{r−1} ≠ (1)`): next level down, same shape.
  Expected `≤ 3` further levels per branch given the certified rank drops; budget
  `≤ 24` jobs total, but sequence B on A's output rather than fanning out blind.
- Reuse the existing zero-swap custody/manifest harness unchanged.

### 6.3 Proof-object gates (all mandatory, fail-closed)

- **G1** pinned ambient `std(I)`; NF after every entry/row/minor/syzygy step;
  mandatory `q2 mod (q2) = 0` negative control per job.
- **G2** explicit syzygy generators with `NF(M·k_j)=0` for all `j`, banked.
- **G3** Fitting certificate: a nonzero-NF witness for `Fitt_r ≠ 0` **and**
  exhaustive vanishing at the next size (the existing R5/r6 discipline).
- **G4** the endpoint ideal `E_r` banked in NF, with the `t`-degree census.
- **G5** planted-nonzero control: replace `E` by `E + 1` and require a nonzero
  NF. A `PASS` on the planted control is a job failure.
- **G6** strict banner `NO_VERDICT_BRANCH_OR_COMPONENT_OUTSIDE_FITTING_LEVEL_r`;
  zero swap; custody manifest replay.

### 6.4 Licensed assumption to verify first (cheap, one job)

Over a non-regular quotient ring, "localized syzygy module = kernel on the
constant-rank stratum" needs `R_r` reduced (or at least that `M` has locally
free cokernel there). **Verify this on the smallest branch (`Q1P03`, `4/99`)
before Phase A fans out.** If it fails, fall back to: present `coker(M)` and
decide `E` against `Fitt_1(coker)` — slower but assumption-free.

---

## 7. Question 7 — software: `ALPHABET`, a cap-free closure compiler

**The problem is not speed, it is caps.** Both false closures corrected today
(the silently capped `MU1` `l`-scan; the `M=1`-before-root pruning; the l-free
phase-3 menu) came from the same instrument class: a capped BFS engine that
reports absence. `ROOT-W2` and `ROOT-REACH` show the alternative: for the
`M=1` layer the reachable set is **finite by a proved contraction** (`DS3`:
`num(w)` contracts by `≥ 1/3` per resonant step), so the closure can be computed
**exactly and cap-free** by divisor enumeration.

**`ALPHABET` — exact target.** Given `(td, m, type menu, entry menu)`, emit:
1. the exact finite `w`-closure `W(w_0)` per entry, with the resonance
   certificate `Δ | num(w)`, `Δ = (n−1)ν+1`, `Δ ≥ 3` (no `NUMAX`, no `KMAX`);
2. the exact reachable jump-cell menu per `(w, r)` by solving the divisibility
   conditions of `SHEET6-DEPTH §5b` in closed form rather than scanning —
   e.g. for IIa, `gcd(lν+1, ν)=1` forces `(lν+1) | w·r·ν`, hence
   `(lν+1) | 4` at `w=2, r=2`, hence `(ν,l) = (3,1)` **uniquely**;
3. the `ROOT-REACH` verdict per entry;
4. a proof object per verdict (the divisor list actually enumerated), so a
   reviewer replays arithmetic, not a search.

**Verification gate (all five required before any consumer):**

- **V1** reproduce, cap-free, `W(2) = {2}` and `W(4) = {2,4}`, `W(3) = {2,3}`.
- **V2** reproduce the unique IIa cell `(r,ν,l) = (2,3,1)`, `M=2`, child
  `Q=(6,12,3,2,5)` at `w=2`, and independently reproduce the three integral
  solutions `{(ν,l)} = {(1,1),(1,3),(3,1)}` before the `ν≥2` filter — I verified
  all of these by hand and by exact enumeration (`CHECK 2`, §11).
- **V3** reproduce `SHEET6-L1` phase-4 counts `601` (`ν=1`), `276` (ZCH `(2,3)`),
  `351` (all landing on the unique residue child) **without caps**, and show the
  cap-free counts are equal — if they differ, the promoted book has a hole.
- **V4** emit the hostile `l = 98` root-`M1` witness with nominal `KMAX = 0`
  (the `93f98e4d…` regression).
- **V5** planted-cell negative control: inject a fabricated admissible cell and
  require `ALPHABET` to find it.

**Cost:** small; pure integer arithmetic, standard library, local, no AWS.
**Expected gain:** removes the campaign's dominant false-closure mechanism and
retires a planned AWS census. This is my nomination for item 5 of the contract.

---

## 8. Idea cards (three, as capped)

### Card 1 — `RIGID-TRANSPORT`: kill or seed residue A one level below patterns

**Exact dependencies.** Prop 8.1(iv) `δ p q′ − (1−u) p′ q = ⊖ p` (printed,
`SHEET6-L1 §1`); Cor 6.1; St 3.9 (with its **load-bearing auxiliary-`h` `κ`
rider** — `SIGRAY-AUDIT` St 3.9, Opus `882485d6…`); St 3.17(i); the two pinned
patterns:

```text
pole P_i :  p = η² − c_i²,        p_g = ⊖ η(η² − (3/2)w_i²)        [rigid, 1 scale]
merge G_m:  p = (η³−a_1)(η³−a_2), q  = η(η³−a_1)(η³−a_2)(η³−b)     [rigid, 1 scale]
            a_1/a_2 = 2 + √3,  b = (2/3)(a_1+a_2),  a_1a_2 = σ²/6, σ = a_1+a_2
suffix F :  p = (t−A)²(t−B),      q  = η(t−A)(t−B),  B = (3/2)A     [rigid, 1 scale]
```

(Closed forms re-derived exactly, `CHECK 6`, §11: `(σ/2)²(1−1/ν) = σ²(ν−1)/(4ν)`
at `ν=3` gives `a_1a_2 = σ²/6`; the ratio satisfies `r² − 4r + 1 = 0`.)

**Licensed assumptions.** The `⊖`-constants `c̃` at parent and child are both
shadows of the *same* global `J(f,g)=1`; St 3.9 pins their scaling relation up to
the (known) exponent data. Nothing beyond printed statements is assumed.

**Cheapest decisive discriminator.** Impose the actual Puiseux substitution
across **one** chain edge `G_m → P_i` (direction `c_i`, `c_i³ = a_i`) and compare
the two `c̃` constants under the pinned exponent/scale transport. This is *one
level deeper than patterns*, which is exactly what `SHEET6-L1 §7.2(ii)` says is
missing and provably not reachable from the printed statement list (`§3`).

**Materially different outcomes.** (a) **Incompatible** ⇒ residue A dies ⇒ with
`ROOT-W2` the whole two-pole `td=6` book is empty ⇒ `td=6` is excluded modulo the
still-unmodeled tiers (`π`-positivity, absolute-degree realizability, `h`-family
realizability). (b) **Compatible** ⇒ the campaign holds explicit exact Puiseux
coefficients at three consecutive levels of a hypothetical counterexample — the
strongest counterexample seed in the repository's history, and the direct input
to Avenue 4 algebraization.

**Stop / rollback.** Stop if the transport turns out to have `≥ 2` free scales
per edge (then it is vacuous and the constants absorb); stop if St 3.9's `κ`
rider cannot be discharged with a common `h`-suitable `κ` for `f−a`, `g` and
`h_1`. Roll back by deleting the card; nothing else consumes it.

**Cost.** Exact algebra over `ℚ(√3)`; hours of reasoning + a small exact script.
**No AWS.** Review: one different-model hostile pass.

**Expected information gain.** Highest in the portfolio: it is the *only*
remaining discriminator for the last `td=6` configuration, and both outcomes are
campaign-moving.

---

### Card 2 — `A47-BUDGET`: charge the resonant orbit from the `h`-side

**Exact dependencies.** `(A47.1) J(f,h_1) = α g^{α−1}` (§5.1, elementary, exact);
the promoted Definition 3.3 contact-quotient / unique-attachment lemma
(`f55a00f5…`, `c74fc0f9…`); Not 8.1; Prop 8.1(i)/(iv); the ROOT/ETA laws
(`SHEET6-L1 §1a`).

**Licensed assumptions.** That the injectivity argument of the MFE attachment
lemma transfers verbatim from cv-witnesses to `h`-branch witnesses — plausible
because it is a statement about `T_a^*` alone, but **must be re-proved, not
cited**: the witnesses live at flags `F * b` that do not exist in `T_a`, so the
attachment must be argued in the ambient `T_a^*`/`R̄_a` presentation.

**Cheapest decisive discriminator.** Compute `N_∞`, the number of branches of
`h_1` at infinity in the fibre-`a` sector, from the pinned entry data
(`(α,β)=(2,3)`, `Λ=3+3`, `td=6`), and compare with `Σ l_F ν_F ≥ 3` for
residue A.

**Materially different outcomes.** (a) `N_∞ < 3` ⇒ residue A dies and, unlike
Card 1, the argument is *structural* — it would generalize to every `l ≥ 1`
merge and close `L1` outright (the "HIGHEST-VALUE TARGET" of
`SHEET6-2POLE §6c`). (b) `N_∞ ≥ 3` ⇒ no kill, but the campaign gains a new
budget functional off `T_a`, which is the only kind that can ever bite here (§2.3).

**Stop / rollback.** Stop if the attachment argument does not transfer to
non-flag directions (then the count double-charges and the inequality is unsound
— this is exactly the `(22)`/`(22-cl)` failure mode and must not be repeated).
Stop if `N_∞` cannot be pinned without a landing theorem.

**Cost.** Reasoning-only first pass; no AWS. Review: one different-model pass,
with the "does it double-charge?" attack made explicit.

**Expected information gain.** High but riskier than Card 1: it can close the
whole `l ≥ 1` family rather than one configuration, but its main hypothesis may
not transfer.

---

### Card 3 — `ROOT-W2` / `ROOT-REACH` promotion

**Exact dependencies.** `(R1)/(R2)` (PROMOTED 16:59Z, `d534f083…`); `L1a(b)`
(PROMOTED, `SHEET6-L1 §2`); `DS2`/`DS3` (PROVED, `SHEET6-DEPTH §3–4`); the MP4
entry pin; table (23) row 1 forced by Prop 5.8(20)/5.7/9.1.

**Licensed assumptions.** None beyond the above. In particular **no** engine
output, no cap, no AWS census, and no use of `(R3)`.

**Cheapest decisive discriminator.** Already executed (§11 `CHECK 3/4`, §3.3
table). What remains is a targeted different-model hostile review of the five
attack points in §3.2, of which point 1 (`L1a(b)` at `G_m = (0,y)`) is the only
genuinely fragile one.

**Materially different outcomes.** (a) Confirmed ⇒ the two-pole `td=6` root
sector is closed for all `μ`, the retracted phase-3 zero is restored
analytically, the `m=2` root recensus is cancelled, and `ROOT-REACH` becomes a
standing cap-free instrument. (b) `L1a(b)` fails at the root ⇒ the promoted
`SHEET6-L1` result itself narrows, which is *more* important to know than the
new theorem.

**Stop / rollback.** If refuted, delete `ROOT-W2`; `ROOT-REACH` survives as a
*sufficient* condition wherever `M=1` chain structure is independently certified.
Nothing downstream is built on either yet.

**Cost.** One reviewer, bounded. **No compute.**
**Expected information gain.** Immediate and certain-ish: it either banks a
result or exposes a hole in a promoted one.

---

## 9. Contract item 1 — disposition vector for all 46 avenues

Baseline = the 17:03Z / 16:22Z / 14:00Z / 12:24Z overlay stack in `APPROACHES.md`.
`G2-PSC` and `G2-BD` are kept strictly distinct throughout and are obligations,
not avenues.

**Changed (6):**

| # | avenue | call | reason |
|---|---|---|---|
| 3 | Vertex-gap / strip ODEs / residue functional `R_{k,d2}` | **raise** | Prop 8.1(iv) `δpq′−(1−u)p′q = ⊖p` **is** a strip/residue-ODE of exactly this family, and the campaign has been solving it cell-by-cell ad hoc (`l1_ode_check.py`). Avenue 3's own proposed extension — depth-three Ore/resultant composition — is precisely the instrument needed for the chain-composite transport that Card 1 requires. The connection was never made; the avenue is currently unassigned. |
| 4 | Formal-germ certification + algebraization | **raise** | Residue A is now coefficient-rigid at **three** consecutive levels up to one scale each (`a_1/a_2 = 2+√3`; `b = (2/3)σ`; `B = (3/2)A`). Avenue 4's prolongation machinery finally has a *seeded* target instead of a blind `l+/e+ ≥ 37` window. |
| 7 | Nonproperness / Jelonek `A(F)` | **raise** | The resonant orbit is a direction along which `g²/f³ → s_0`, i.e. a **pinned predicted asymptotic direction**. Avenue 7's recorded blocker was "`A(F)` was never constructed from the books"; there is now one explicit candidate datum to verify rather than a compactification to rebuild. |
| 25 | Fiber monodromy / dessins / Hurwitz passports | **lower** | Dominated. Residue A is now pinned at the coefficient level, which is strictly finer than any passport; the 169-passport census returned no kill; L5 still supplies no coupled two-coordinate inertia (12:24Z adjudication §3.2 item 4 unchanged). Spending here buys information the coefficient layer already contains. |
| 27 | Links at infinity / splice diagrams / plumbing | **reopen** | Three independent inputs landed since it was parked: (i) the promoted Definition 3.3 contact-quotient facts (rootward closure, unique attachment, no remerging) are the exact combinatorial statements splice arguments need; (ii) residue A's boundary data are pinned; (iii) van Dobben arXiv:2608.27341 supplies a concrete `D_{k+2}` non-linear-dual-graph obstruction. The realizability question is finite for the first time. |
| 31 | Integrality / ZMT / Rees valuations | **raise** | `A47-BUDGET` is literally a valuation/branch-counting client on one pinned configuration — i.e. Sol's S16 experiment ("Rees valuations of one complete boundary book") with a concrete object at last, and with `(A47.1)` naming the divisor to count against. |

**Unchanged (40).** Grouped by current standing, with no merging of any pair:

- *Principal / active, unchanged:* **1** (GGV corner farm — see §7 lane call:
  redesign inside the avenue, rank unchanged), **2** (Sigray sheet ladder —
  remains the principal proof backbone; the frontier moves *within* it from
  `λ`-budgets to coefficient transport, which is a redirection, not a rank
  change), **36** (guided CE search / K00 clients — protect; residue A now
  supplies a structured support template, again a redirection inside the avenue).
- *Held down by an executed negative or an explicit backend fact:* **16**
  (D-module/holonomic index — HENS-CT timed out before creative telescoping;
  stays lowered), **26** (primitive-monodromy `td` bound — `A_d/S_d` wall stands),
  **28** (log surfaces/BMY — still `NEEDS-DATA`; no licensed GRR endpoint),
  **32** (collision ideal — three-generator presentation is still injectivity),
  **33** (symplectic primitives — `COSTUME`), **35** (dim-≥3 descent — Picard
  obstruction `ℤ/(d−2)`), **38** (tropical), **39** (cohomological cluster).
- *Recon / defensive only:* **5** (Jung–van der Kulk), **6** (Abhyankar–Moh),
  **8** (formal inverse), **13** (Dixmier DC(2)), **14** (End(A₁)/Zheglov),
  **15** (spectral surfaces / commuting PDOs), **17** (BCW/Družkowski/Yagzhev),
  **20** (reduction mod p / p-curvature), **21** (p-adic injectivity/Hensel),
  **22** (Diophantine/heights), **23** (analytic global inverse), **24**
  (real JC/Pinchuk), **29** (LND/Hamiltonian completeness — I independently
  re-derived `D_f(g)=1`, i.e. `g` is a slice of `J(f,·)`; this *confirms* the
  ledger's own "LND-ness with a slice is essentially the conjecture again" and
  moves nothing), **30** (affine-surface/ML), **34** (2D tangent-sweep/pole
  removal), **37** (finite-field census), **40** (free-associative lift),
  **43** (Ritt decomposition), **45** (differential Galois/Liouvillian),
  **46** (Lean/AI certification — rigor layer only).
- *Closed / refuted, remain so:* **9** (Lee–Li Conjecture E — no reduction to a
  finite check), **10** (HC4 ⟹ JC2 — exact `NO LEVERAGE` verdict stands),
  **11** (Mathieu/GMC/Zhao ladder — refuted), **12** (face isolation / p-adic
  multinomials), **18** (graded/GIT — Shaska 2026), **41** (naive scaling
  deformation — falsified by the dim-3 CE), **42** (Markus–Yamabe — arrow points
  the wrong way), **44** (Moskowicz — `REFUTED-AS-PROOF`, only the repaired
  membership theorem retained).
- *Unchanged, live but expensive:* **19** (char-`p` + Witt — the degree-twelve
  bounded frontier is the only live sub-target; see the lane call in §12).

Count check: 6 changed + (3 principal + 8 held-down + 20 recon/defensive +
8 closed/refuted + 1 live-but-expensive) = 6 + 40 = 46, each avenue exactly once
(verified programmatically). None omitted; `G2-PSC` and `G2-BD` never merged.

---

## 10. Contract items 2–4 — bottleneck reranking and the two attacks

### 10.1 Three principal **proof** bottlenecks (reranked)

1. **Universal, provenance-preserving landing / coverage** *(unchanged at #1)*.
   Now with a sharper decomposition: for the all-`b=1` layer, `ALPHABET` +
   `ROOT-REACH` are a cap-free finite landing instrument. The residual walls are
   (a) post-jump (`M ≥ 2`) segments and (b) off-axis (`b ≥ 2`) entries, for which
   no `w`-analogue exists (§3.4 items 1–2).
2. **Coefficient-level (Puiseux/ODE) transport between adjacent flags**
   *(NEW at #2; previously buried as "H4 / realizability, the same tier open for
   every survivor")*. It is promoted to #2 because it is now the **unique**
   remaining obstacle for the last `td=6` configuration, and because
   `SHEET6-L1 §3` shows that no printed statement and (by §2.3) no `T_a`-supported
   functional can substitute for it. It displaces "source-trust integration",
   which is now largely discharged (Prop 5.4, 6.7/6.8, Lemma 6.1, the
   every-fibre 5.8 replacement, `(C7.1*)`, and §9 are all review-closed; only
   Statement 6.2's omitted domain remains, and consumers establish it).
3. **`RPMC(C)`, independently sourced type control, and a cofinal `td`/complexity
   ceiling** *(unchanged; nothing this round moved it)*. `SHEET6-DEPTH §2 R1`
   remains the structural explanation: `td` does not bound the Puiseux
   denominator `κ_i` at infinity.

### 10.2 Two principal **disproof / counterexample** bottlenecks (reranked)

1. **Puiseux algebraization of residue A** *(NEW at #1)*. It is now the most
   pinned counterexample seed in campaign history: complete `Q`-data on a
   four-vertex chain, patterns rigid up to one scale at three of them, a
   budget that is now unconditional (§2.2), and the root alternative closed by
   `ROOT-W2` (§3). The remaining arrow is germ-to-polynomial.
2. **K00 / full-`P6` rank-exact point plus one prolongation** *(was #1, now #2)*.
   It has capped twice without a verdict (`K00_V27_P6R4=RESOURCE_CAP_NO_VERDICT`)
   and gained no new structure this round. Retain and protect, but it is no
   longer the most specific seed the campaign holds.

*Note on the dropped third:* "a deep GGV survivor beyond the first-order
obstruction" is demoted out of the top two, because the endpoint lane now
produces death on `D(Δ)` only and every complement is explicitly
`NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`. It returns if §6's Fitting recursion
finds a survivor stratum.

### 10.3 Strongest proof attack to run next

**`RIGID-TRANSPORT`** (Card 1), preceded by the free win of banking `ROOT-W2`
(Card 3). Rationale: residue A is the entire remaining `td=6` obligation; §2.3
proves the budget layer can never reach it; §3 removes its root alternative; and
Card 1 is the cheapest instrument that operates at the only layer that can bite.

### 10.4 Strongest counterexample / falsification attack to run next

**Seeded two-level germ construction.** Take the pinned data
(`a_1/a_2 = 2+√3`, `b = (2/3)σ`, `B = (3/2)A`, `Q`-chain
`(2,2,2,2,5) → (6,12,3,2,5) → (42,126,7,3,5) → (0,y)`), build the Puiseux germ
explicitly, and prolong with Avenue 4's `DEPTH-STAB` machinery with **two free
scales** instead of a blind window. Immediately cross-filter the resulting
boundary with van Dobben's `D_{k+2}` criterion (Avenue 27, `reopen`) — a
boundary graph failing that criterion falsifies the seed cheaply, and one that
passes is the first structurally credible counterexample template the campaign
has produced.

---

## 11. Contract item 8 — one likely-missed insight, and its cheapest test

> **The campaign has been queueing an AWS root census for a question that four
> lines of arithmetic already answer.** `(R2)` — the promoted `w_G < 1` at any
> root case-I edge — carries **no `μ` hypothesis**. The 16:59Z integration
> immediately specializes to `(R3)` (all-`μ=1`) and then records mixed-`μ` root
> completeness as open. But `(R2)` composed with `L1a(b)` (chains are `M=1`) and
> `DS2/DS3` (`W(2)={2}`) already closes the entire two-pole `td=6` root sector,
> for all `μ`, with no engine.

**Cheapest test — already executed:** `CHECK 3` (closure `W(2)={2}`, cap-free)
and `CHECK 4` (`w_G = 1 − X_root/μ < 1` for all `μ ≥ 1`, `X_root > 0`) below,
plus the 57-row `ROOT-REACH` table. Total cost ≈ 0.5 s. What remains is a
bounded different-model hostile review of the five attack points in §3.2 — of
which only point 1 (does `L1a(b)`'s third-pole induction survive when the meet
is `(0,y)`?) is genuinely fragile.

**Secondary missed insight (corollary of §2.3):** every further sharpening of
the `λ`/exit/`ψ` budget is provably incapable of touching residue A. Cheapest
test: the one-line St 3.18 observation that `F * b` does not exist at a non-root
of `p_F`. This should be recorded as a **stop rule**, not merely as a remark in
`SHEET6-L1 §3`.

---

## 12. Contract item 7 — `continue` / `redesign` / `stop` for every major lane

| lane | call | reason |
|---|---|---|
| **Pure Sigray / exact-pair** | **continue** | Principal backbone. Reallocate inside it: from `λ`-budgets (dead end, §2.3) to coefficient transport (Card 1) and to the `w`-alphabet (§3, §7). |
| **Hybrid `G2-PSC`** | **stop** | No current consumer; the pure route bypasses it; the transport functor is not in sight. Stopping it does **not** touch `G2-BD`. |
| **`G2-BD` (post-residue-A bounded delay)** | **continue as a named obligation only** | It becomes live only if residue A survives Card 1. Do not merge it with `G2-PSC` in any summary. |
| **Arbitrary-`Q` / rank-drop GGV** | **redesign** | Replace the chart/complement recursion with the Fitting-level syzygy/module design of §6. Do not build a minor atlas. |
| **λ-nonzero / raw-window GGV** | **redesign** | Stop face-order marching (orders four and five are regular; order six is not licensed). Target the all-order row-ideal invariance theorem or the complete raw-window/endpoint incidence. |
| **LF40** | **stop** | Capped at row zero with an empty-ideal display; the `29 vs 36` predictor is retracted; no theorem and no consumer. |
| **K00 / order-two / TD6** | **continue, hard-budgeted** | Disproof bottleneck #2 (§10.2). Two `RESOURCE_CAP_NO_VERDICT` events mean the next run needs a compression preregistration, not more capacity. |
| **D43** | **stop unless a consumer is re-declared** | A ~185 GB long tail builder with no result and no named consumer in the current frontier. Re-declare or terminate; do not let it hold capacity by inertia. |
| **Artin–Schreier / char-`p`** | **redesign** | Stop the AS109 exact-lift clone (correction `y`-degree `≥ 12` forced; the zero-tail Artin section is raw-dead at `D22`). Keep only a cheap characterization of the bounded degree-twelve frontier. |
| **HENS-CT** | **stop** | Timed out inside generic multivariate `annihilator_of_composition` before creative telescoping, with no candidate. Do not rerun without a structural adapter **and** a named client; neither exists. |
| **External intelligence** | **continue** | Next broad sweep due 2026-08-29 05:24Z. Add two targeted watches: Eggers–Wall/contact-tree combinatorics, and Jelonek `A(F)` structure theorems (both now have live clients: §5, Avenue 7/27/31). |

---

## 13. Contract item 9 — epistemic ledger

### 13.1 Promoted facts I consumed (not re-derived unless stated)

`(R1)/(R2)/(R3)` root-meet theorem (`d534f083…`, `b8d6e686…`, `656c257e…`);
MFE selected-exit inequality with the pole-endpoint repair (`c74fc0f9…`,
`f55a00f5…`, `9f4526f2…`); actual-weight `(C7.1*)` (`c253bd12…`, `727f5850…`);
Section 9 `counterexample ⇒ td ≥ 6` (`2763d970…`, `0729a576…`); corrected
Proposition 8.4 (nonroot only) and Statement 8.5; Propositions 5.4, 6.7, 6.8,
Lemma 6.1, the every-fibre Proposition 5.8 replacement; Proposition 5.1 forced-
puncture repair and non-leakage; the no-first-constant-corner theorem;
`L1a`/`L1b`/`L1-zch` and the `L1-IIa` local counterexample (`SHEET6-L1`,
`SHEET6-A3L1-REVIEW`); `DS1–DS4` chain-depth closure (`SHEET6-DEPTH`); the
reducer-safe quotient ranks `9/104`, `6/101`, `4/99`.

### 13.2 Provisional inputs I used as such

The unpinned file `ladder/SHEET6-L1.md` (SHA-256
`9697f10aa646536927c73c6cc67804a2b62df9dfd8e9c1f42bdb38617bfb4adb`, recorded
status "COMPLETE + PROMOTED"). It is **not** in the packet's custody table; I
read it because it is the only file containing Prop 8.1(iv), the `L1a` lemma,
the ODE rigidity closed forms, and the `§7.2` statement of the missing global
`h`-count — all load-bearing for §3, §5 and Card 1. Its promotion status is
asserted by the file itself and I did not independently verify the review chain.
**If `SHEET6-L1` is not currently promoted, `ROOT-W2` loses step (a) and Card 1
loses its pinned patterns.**

### 13.3 Conjectures / new and unreviewed

`ROOT-W2` (§3.2); `ROOT-REACH` as an oracle (§3.3); the mixed-`μ` root form
`X_root = μ_tot/(r+l+e_0)` (§3.4 item 4, **derived sketch only, not proved**);
`A47-BUDGET` (§5.3, an interface, not a theorem); the `c̃`-transport
discriminator (Card 1, may be vacuous); the §6 Fitting-localization claim (needs
the reducedness check of §6.4).

### 13.4 Failed attempts, honestly recorded

- I looked for a new `td` / degree / conductor ceiling from Riemann–Hurwitz, the
  pole-mass identity, Euler/genus and terminal orbit data. **`NO HIT`** — all
  recombine to identities the campaign holds, for the reason in §4.
- I checked whether MFE sharpens residue A's terminal menu. It does not: all
  four IV classes sit at `Σλ=2 ≤ 3`. **`NO HIT` ×4.**
- I re-derived `D_f(g) = J(f,g) = 1`, i.e. `g` is a slice of the derivation
  `J(f,·)`, hoping for a fresh Avenue 29 handle. This is exactly the ledger's own
  recorded position ("LND-ness with a slice is essentially the conjecture
  again"). **No advance; avenue 29 stays `unchanged`.**
- My first pass at the jump-cell menu at `w=2`, `r=2` produced three integral
  solutions `(ν,l) ∈ {(1,1),(1,3),(3,1)}` and I briefly believed the promoted
  "unique IIa cell" claim was incomplete. It is not: the two `ν=1` cells are the
  `I`-family, killed by `L1b`. Recorded because a reviewer will hit the same
  intermediate state.

### 13.5 Hidden assumptions I am aware of

- `ROOT-W2` assumes `L1a(b)`'s induction covers the case `G_m = (0,y)`. The
  `SHEET6-L1` text asserts (b) for "every chain vertex strictly above `G_m`"
  without restricting `G_m`, and its proof mechanism (third-pole via Prop 6.8)
  does not obviously use interiority — but `(0,y)` is special in St 8.5 and
  Prop 8.3(iii), so this is the review point.
- The `ROOT-REACH` closure omits the per-edge congruence `n_e ≡ −κ̄_e (mod ν_e)`,
  making `W` an over-approximation. `EXCLUDED` verdicts are sound in that
  direction; `not excluded` is not a proof.
- `ROOT-REACH` applies only to on-axis (`b=1`) entries, because `b ≥ 2` means
  `M ≥ 2` at entry and the `DS2/DS3` recursion never starts.
- I did not verify the type/entry enumeration constraints (`Λ ≥ β`, `Λ ≤ td`,
  `1<α<β≤td`, `gcd(α,β)=1`) against the printed source; I took them from
  `SHEET6-2POLE §2a` and `ladder/REDUCTION.md §0`.

### 13.6 Checks actually run (all local, pure Python standard library)

Two scripts, `/tmp/opus5_1707_checks.py` and `/tmp/opus5_rootreach.py`
(exact `fractions.Fraction` and integer arithmetic only; no CAS, no network):

```text
CHECK 1  MFE on residue A: sum lambda^exit = 2 <= td-1-psi = 3, slack 1;
         psi = ceil(126/42)-1 = 2.                                   PASS
CHECK 2  IIa cell uniqueness at w=2, r=2: integral solutions are
         (nu,l) in {(1,1),(1,3),(3,1)}; with nu>=2 the unique cell is
         (nu,l)=(3,1), M=gcd(6,10)=2, kappabar=5, D/i=3.             PASS
         (hand proof: gcd(l*nu+1,nu)=1 => (l*nu+1)|4 => l*nu in {0,1,3})
CHECK 3  Closure W(2) under DS2/DS3 = {2}; no value < 1 reachable;
         entry pin w0=2 agrees with Q(P_i)=(2,2,2,2,5).              PASS
CHECK 4  (R2): w_G = 1 - X_root/mu < 1 for all mu>=1, X_root>0.      PASS
CHECK 5  (R3) is a strict special case of (R2): X=r/(r+l) =>
         w=l/(r+l) in (0,1) for all r>=2, l>=1.                      PASS
CHECK 6  Residue-A merge ODE closed forms: (sigma/2)^2(1-1/nu)
         = sigma^2(nu-1)/(4nu); at nu=3, a1a2=sigma^2/6, b=2sigma/3;
         ratio satisfies r^2-4r+1=0, i.e. r = 2+sqrt(3).             PASS
ROOT-REACH  57 on-axis td=6 entries enumerated; 41 EXCLUDED, 16 not.  RUN
```

No check failed. Nothing here required AWS, Singular, msolve, Sage or Lean.

### 13.7 Contamination

**None, with one filename-only exposure disclosed in full.**

At the time I began, `xmodel/` contained only the four `1707Z` *prompt* files and
the packet — no peer response existed. I listed the directory (filenames only) to
identify my own assigned prompt, which the packet permits by naming "your
assigned prompt" as a readable input. I read
`xmodel/ideation-20260828T1707Z-opus5-prompt.md` and no other `1707Z` file except
the packet.

**Disclosed exposure.** After this report was fully written and first hashed, a
closing `git status --porcelain` (run to confirm I had made exactly one write)
printed the names `xmodel/ideation-20260828T1707Z-grok.md` and
`xmodel/ideation-20260828T1707Z-sol-ultra.md`, which two peers had landed while I
was working. **Filenames only; no byte of either file was read, at any point.**
The exposure occurred strictly after my mathematics, verdicts, dispositions and
rankings were sealed, so it cannot have affected independence, and I did not fail
closed. Recorded here because the packet requires disclosure of accidental
contamination whether or not it is material. No peer content, verdict, or
conclusion was available to me at any stage.

### 13.8 Exact scope of this report

Everything new here is `INTERNAL-UNREVIEWED / PROVISIONAL`. `ROOT-W2` is a
candidate theorem in the two-pole `td=6` row-1 sector only; it says nothing about
`m ≥ 3`, off-axis entries, SF1, interior merges, or `td ≠ 6`. `ROOT-REACH` is a
sufficient condition for on-axis entries only, computed from an
over-approximating closure. `A47` is an interface with one unproved transfer
step. `(A47.1)`/`(A47.2)` are exact identities and are the only unconditional
new mathematics in this report. Nothing here proves or disproves JC2, excludes
`td=6`, restores printed `(22)`, `(22-cl)`, literal `δ_a`, fixed or cross-fibre
`κ`, equality/slack, or MP8's no-refinement claim. A model verdict is not
mathematical evidence.

### 13.9 Files read

*Packet-pinned, read in full:* `COORDINATION.md` (roles/gates portion),
`xmodel/ideation-20260828T1149Z-synthesis.md`,
`xmodel/websweep-20260828T0524Z.md`,
`xmodel/sigray-sections7-9-coordinator-integration-sol-ultra-20260828.md`,
`xmodel/sigray-sheet6-depth-root-meet-coordinator-integration-20260828.md`,
`xmodel/sigray-multipole-selected-orbit-attachment-coordinator-integration-20260828.md`,
`ladder/SHEET6-2POLE.md`.
*Packet-pinned, read substantially:* `APPROACHES.md` (all six 2026-08-28
overlays, the 06:23Z block, the full 46-row master table, §§2–4; older
superseded overlays sampled by heading), `AUDIT.md` (current corrections,
lines 1–470), `PROGRESS.md` (the whole 2026-08-28 day), `notes.md` (head 180,
tail 260, plus targeted lane greps), `ladder/REDUCTION.md` (frontier overlay +
executive verdict + §0), `ladder/SHEET6-DEPTH.md` (lines 1–330),
`ladder/SIGRAY-AUDIT.md` (verdict ledger, first 60 rows),
`ladder/SHEET6-MULTIPOLE.md` (supersession box + preview),
`xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md`
(§§0–3), `xmodel/sigray-rootaware-engine-cap-repair-hostile-rereview-gpt5-20260828.md`
(§§0–3).
*Not packet-pinned:* `ladder/SHEET6-L1.md` (hash recorded in §13.2),
`xmodel/ideation-20260828T1707Z-opus5-prompt.md`, and directory listings of
`xmodel/`, `ladder/`, `cases/`.

---

## 14. Ranked execution order (by expected information gain per wall-clock hour)

1. **`ROOT-W2` hostile review** (Card 3) — bounded, no compute, either banks a
   theorem or exposes a hole in a promoted one. Cancel the `m=2` root recensus
   pending the verdict.
2. **`RIGID-TRANSPORT`** (Card 1) — the only remaining discriminator for the last
   `td=6` configuration; both outcomes are campaign-moving.
3. **`ALPHABET` cap-free compiler** (§7) — small, local, removes the campaign's
   dominant false-closure mechanism; gates V1–V5.
4. **GGV Fitting/syzygy redesign** (§6) — start with the §6.4 reducedness check
   on `Q1P03`, then Phase A on six branches.
5. **`A47-BUDGET` first pass** (Card 2) — reasoning-only; if the attachment
   argument transfers, it closes `L1` outright.
6. **Post-jump `w`-law** (§3.4 item 1) — elementary Prop 9.3 arithmetic; unblocks
   `ROOT-REACH` for `m ≥ 3`.
7. **Seeded germ + van Dobben boundary filter** (§10.4) — the counterexample lane,
   now seeded rather than blind.

New work may run provisionally and reversibly during review; promotion and
expensive fanout remain review-gated, per `COORDINATION.md`.
