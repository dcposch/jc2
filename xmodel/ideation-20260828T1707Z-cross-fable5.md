# Cross-pollination synthesis — Fable 5 — `20260828T1707Z`

Lane: Fable 5 (Anthropic), exact model `claude-fable-5`, cross-review round
(deliberately unblinded). Cross-packet
`xmodel/ideation-20260828T1707Z-cross-packet.md` verified at
`9cc1d824e35abbd9f367f59cc94bfde2f6c93f37a099ee48238211b6bbbec8e9` before
reading. All five frozen-corpus hashes and all five overlay hashes verified
by `shasum -a 256` and matched exactly (list in §7.6). All four peer
reports and all overlay files were read in full. `jc2-lean` was not
entered, listed, searched, read, built, modified, status-checked, or
controlled. No AWS, Singular, msolve, Sage, or Lean was touched; no heavy
local CAS was run. Only hashing, file reads, and hand-replayed exact
arithmetic were used. This file is my only write. A model verdict is not
mathematical evidence; every new claim here is `PROVISIONAL/UNREVIEWED`.

**Custody drift disclosure (affects Charge 1).** `ladder/SHEET6-L1.md`
currently hashes `69e6e4c1c359381c01941f641c5c7f364f95342411c8e90ed7d4aa27965f38fc`,
not the `9697f10a…` Opus 5 recorded in his blind report. The worktree is
dirty and the file has changed since his read. I re-checked that the
content he consumed is still present (status header `COMPLETE + PROMOTED`;
Lemma L1a in §2 with clause (b); the §7 item 2(i) `h_1`-branch-budget gap
paragraph), but any promotion consuming `SHEET6-L1` must re-pin the hash.

---

## 0. Verdicts in five lines

1. `ROOT-W2` / td=6 two-pole root closure: **REPAIR** — true at the
   claimed scope, but by a different (stronger-perimeter) proof than
   Opus 5 wrote; the `L1a(b)` step is both fragile and avoidable (§1).
2. The six residue-A proposals reduce to **two independent tests, run as
   one two-stage composition**: source-side coefficient match, then
   target-side ghost-ray dichotomy. RES-AV, Q-GHOST, and A47 are three
   costumes of the same geometric object; MERGE-DIFFERENT as printed
   targets a provably flag-free region and is DOA unless retargeted
   off-tree (§2).
3. `A47`'s identity is verified exact; its first missing implication is
   precisely RES-AV's convergence step — the two cards are one card (§3).
4. GGV: **hybrid** — keep the held single-node complement-recursion gate,
   then reorganize level-wise (Fitting), with the merged fail-closed
   contract G0–G7 and the existing "one full node passes" fanout trigger
   (§4).
5. Three connections extracted (§5); 6-hour queue with stop rules and a
   60/40 proof/disproof split (§6); full ledger (§7).

---

## 1. Charge 1 — line-by-line audit of `ROOT-W2` and the td=6 two-pole root closure

**Claim under audit** (Opus 5 §3.2; anticipated by Grok §1.2 and my own
blind §10; flagged by overlay A as "high-confidence promotion candidate"
pending "a narrow audit of `L1a(b)`/whether every such root meet receives
a certified row-1 `M=1`, `W={2}` branch"): *in the two-pole td=6
configuration there is no genuine root merge, for any multiplicities μ.*

I performed the audit overlay A asked for, against the current sheets.

### 1.1 Step-by-step

- **(Step 0) Sector definition.** `SHEET6-2POLE` §5 phase 3 defines the
  root sector as "root merges = meet at `(0,y)`", i.e. the two pole
  chains' characteristic paths meet first at the root. Confirmed.
- **(Step 1) Row forcing.** `Λ_1+Λ_2 = 6`, `Λ_i ≥ β ≥ 3` forces `(3,3)`,
  type `(2,3)`; the unique `Λ=3` row of table (23) is `(a,b,ν)=(1,1,2)`,
  so `b=1` at both entries. Machine-checked in my blind round (§11 script,
  row-uniqueness); consistent across all four reports. HOLDS.
- **(Step 2) Chain structure without `L1a(b)`.** MP4 (`b=1 ⟹ M=1` at
  entry, promoted) plus MP5 (promoted, verbatim: every chain vertex down
  to "the last pre-merge vertex" has a single SIMPLE ν-orbit, `M=1`,
  `λ=0`, *"no ray of `T_a` separating there; the chain arrives at `G_i`
  with `μ_i = 1`"*). Crucially, `SHEET6-DEPTH` §1's promoted segment
  setting explicitly includes segments "ending at the last vertex before a
  merge vertex `G` (`r(G) ≥ 2`) **or before `(0,y)`**" — the pre-root
  chain is inside the DS perimeter by its own wording. **`L1a(b)` is not
  needed.** This removes Opus 5's self-identified most fragile step (does
  `L1a(b)`'s third-pole induction survive when the meet is `(0,y)`?) and
  the dependency on the since-mutated `SHEET6-L1` file.
- **(Step 3) w-alphabet.** DS1–DS3 (H1 tier, promoted): entry
  `w_0 = (κ̄ − ρ)/ν = (5 − 1)/2 = 2`; a resonant step needs
  `Δ | num(w) = 2` with `Δ ≥ 3` — impossible; `W(2) = {2}` (DEPTH §4,
  machine check 2). Every chain vertex, at any depth, has `w = 2`. HOLDS.
- **(Step 4) Normalization match (Opus 5's attack point 2).** RESOLVED:
  DEPTH §1 defines `w_F := (κ̄_F − ρ_F)/ν_F` with `ρ_F = D_F/deg(p_F)`
  (full pattern degree); overlay A defines
  `w_e = (κ̄(H_e) − D_{H_e}/deg(p_{H_e}))/ν_{H_e}`. Same formula, same
  object. No i-normalization mismatch.
- **(Step 5) Root-edge law.** Overlay A (GREEN, hostile-confirmed): at a
  genuine contact-zero root merge, **every actual searrow parent edge** is
  Prop 9.3 case I with `X_R = μ_e(1−w_e)`, `0 < w_e < 1` — no hypothesis
  on `μ`, no `V_{1,a}` or `ν ≥ 2` rider (Opus 5's attack point 3 resolved
  by the overlay's promoted form). The chain's arrival edge is such an
  edge with `w_e = 2`. Contradiction. HOLDS, with one glue paragraph to
  write (below).
- **(Step 6) μ-generality is free twice over.** (i) Edgewise: Step 5 does
  not care what `μ_e` is. (ii) Structurally: `μ_e | M_{H_e} = 1` at the
  arrival (MP5's rider; at the root the divisibility is the Statement 8.5
  root clause per the packet's corrected-Section-8 wording — Grok cited
  St 8.4 here, a citation-level nuance to fix), so with one `μ_e = 1`
  present, overlay A licenses "full repaired MP6 root anatomy": the meet
  is in fact **all-`μ=1`**, and even the already-promoted (R3)/`W={2}`
  sentence recorded in DEPTH §5d/§6 kills it. Mixed-`μ` cannot occur at a
  chain-fed td=6 root meet at all.
- **(Step 7) The configuration Opus 5's statement silently includes.**
  "No root merge, for any μ" must also exclude a hypothetical `V_2` root
  merge *after* an interior merge (post-merge suffix meeting a pole-free
  fibre direction at `(0,y)`). MP1's budget does not forbid it (the
  pole-free subtree is not in `U`), and the suffix is `M=2`, outside
  DS2/DS3. It is excluded anyway, by the **already-promoted terminal
  transport**: in the interior-merge branch, `SHEET6-2POLE` (§1, lines
  74–76; §6a exhibit datum "single root", `deg p_{(0,y)} = 126`) uses
  Prop 8.3(ii) to force `p_{(0,y)}` single-rooted, so `(0,y) ∉ V_{2,a}`
  and no root merge exists in that branch. This is *shared debt* with the
  promoted exhibit (its ψ-transport already leans on it), not new debt;
  but the promotion note must cite it, and a hostile reviewer should
  re-pin Prop 8.3(ii)'s printed hypothesis at the `M≥2` suffix.

### 1.2 Verdict and weakest dependency

**REPAIR.** The theorem is true at its claimed scope, but promote the
repaired composition, not Opus 5's write-up:

> **ROOT-W2′.** td=6, m=2 (m=3 is impossible: `mβ ≤ td`): both entries
> row 1. (Interior-merge branch): Prop 8.3(ii) single-rooted terminal ⟹
> no root merge. (Root-meet branch): MP4+MP5 make both arrivals `M=1`,
> `μ=1` chains with DS-invariant `w=2` (DS1–DS3, `W(2)={2}`); overlay A's
> edgewise case-I law forces `w_e < 1` at every actual searrow parent
> edge — contradiction. Hence no genuine root merge, any `μ`. ∎

**Exact weakest dependency:** the one-paragraph glue that the last chain
vertex is an *actual searrow parent edge* of `(0,y)` in overlay A's exact
sense — i.e. `H_e = (0,y) + c_e` with `H_e ∈ V_a ∩ T_a^searrow` and `c_e`
a root of `p_{(0,y)}^red`. All three ingredients are promoted (MP0 puts
chain vertices in `Ta& ∩ V_a`; Prop 3.1(**) makes the pole branch's
coefficient at height 0 a pattern root; Not 3.3's descent makes `H_e` the
last chain vertex), but the sentence is written nowhere. Second-weakest:
Prop 8.3(ii) at the `M≥2` suffix (shared with the promoted exhibit).
Both are bounded, citation-level checks — hence REPAIR, not REJECT.

**Consequences if the repair passes hostile review:** the retracted
phase-3 zero is restored analytically for all `μ`; the m=2 root recensus
is cancelled (its remaining scope: single-pole HIII/SF1 root children,
off-axis, `m≥3` — consistent with overlay A's td≤12 census note and its
BOOK-OFFAXIS td=7 root-subcase kill); the td=6 two-pole book is exactly
{residue A + its IV classes}. It does **not** touch `td=7` (first live
root frame `(a,α,β,ν)=(2,2,3,3)`, `w_0=8/3 → 2/3` — found independently
by Opus 5's ROOT-REACH table and my blind §2.2, same frame, same missing
`M≥2`/post-jump w-law), does not exclude `td=6` (residue A stands), and
does not license ROOT-REACH's `not excluded` rows as reachable.

---

## 2. Charge 2 — the residue-A proposals, compared and combined

Setting (promoted exhibit + overlay B): merge `Q=(6,12,3,2,5)`, reduced
`(dp,dq)=(6,10)`, rigid ratio `a_1/a_2 = 2±√3` (`z²−4z+1`), one q-only
`ν=3` orbit at direction `b`; suffix selected-exit cost 2; `ψ=2` (R3
terminal) or `ψ=3` (R4); MFE `2 ≤ 3` with slack 1 (R3) and exactly-2
tight (R4). Overlay B: no factor 6 or 7 licensed; ordinary
`T_a`-supported λ-refinements cannot price the orbit.

### 2.1 Does each proposal see the orbit geometrically, or rename it?

| Proposal | Sees the orbit as | Verdict |
|---|---|---|
| Coefficient/parent match (Sol §3, Grok Card A, my Card 1a) | a load-bearing unknown in the two per-edge Prop 9.3 systems + Prop 8.1(iv) | **Geometric/algebraic — real.** Tests source-side consistency; does not charge the orbit. |
| `RIGID-TRANSPORT` (Opus 5 Card 1) | the same, one level deeper (⊖-constant transport under actual Puiseux substitution across one edge) | **Real; same family.** Sequence after the pattern-level match — it is the depth-2 checkpoint of the same computation, not a separate test. Risk: ≥2 free scales per edge makes it vacuous (his own stop rule). |
| `MERGE-DIFFERENT` (Sol interface + Card B) | a length-`l+1` different/conductor module whose non-pole summands "inject into pairwise-distinct actual cv flags attached at or above the merge" | **DOA as printed.** The at-or-above-merge region is provably cv-flag-free: MP5's verbatim "no ray of `T_a` separating there" on both chains, Prop 5.5/7.2 (every puncture above a pole has `g=∞`; cv rays need `g` finite), and MP6(a)/(e) (`k=0`; the `l` extras carry no tree vertex). The conjectured injection has an empty target. Under the opposite ("rootward") reading the target is the suffix component, where the injected flag must be proved distinct from the already-counted suffix witness — unproved, and even then `+1` is insufficient (below). The length computation itself is a real local object; its only viable budget targets are off-tree (h-branches / `A(F)` data), i.e. it collapses into A47/RES-AV. |
| `RES-AV` (my blind §5) | ambient ghost rays: `f→a` frozen (`D=6>0`), `D_g = κ̄−D = −1`, one further cancellation plausibly gives `g→b′` finite; `(a,b′) ∈ A(F)`; kill via Jelonek `dim A(F)=1` if `b′` moves | **Genuinely geometric; the only target-side object on the table.** Named dependencies: St 9.1's `κ̄=D+D_g` domain at the merge, M-PAT depth, `a`-uniformity, primary-text Jelonek pin. |
| `Q-GHOST` (Grok §4, Card C) | a shift `b` making the direction "a finite-puncture threshold of `(f,g−b)`, hence a genuine vertex of a translated tree" | **Rename in its stated form.** `T_a` is built on the fibre `f=a`; shifting `g` changes decorations (κ, cv population) but cannot create a vertex in a direction carrying no fibre branch (Prop 3.1(**)); the structural-blindness result (Opus 5 §2.3, my disclosed failed attempt, overlay B) applies to the shifted pair too. Its sound residue: the shift value *is* RES-AV's asymptotic `b′`, and the honest place the ghost becomes a vertex is the **other fibration's** tree at the fibre `g=b′` — see connection C2. Grok's own stop rules would trigger. |
| `A47-BUDGET` (Opus 5 §5, Card 2) | `l_Fν_F` h₁-pattern roots vs a count `N_∞(h)` of h₁-branches at infinity, powered by `J(f,h_1)=αg^{α−1}` | **Identity real and new (§3); budget is the pattern-level shadow of RES-AV.** Its missing first implication *is* RES-AV's convergence step (§3); injectivity must be re-proved (flags `F*b` do not exist in `T_a` — Opus 5 concedes); RHS needs a landing-free pin. |
| Seed-to-jet lifting (Sol falsification attack, my Card 1b→jet, Opus 5 §10.4) | consumer of the matched coefficients + `b′(a)` germ | **Not an independent test** — the endgame stage, correctly sequenced last by all four reports. |

### 2.2 Do they combine into one genuinely stronger geometric test? — Yes, as a two-stage composition

The six proposals are not six independent chances. They reduce to **two
independent tests that compose**, and the composition is strictly
stronger than any component:

> **Stage 1 (source side — pins the model).** The simultaneous two-parent
> coefficient match at `(2,3,1)` over `ℚ(√3)`: both per-edge Prop 9.3
> systems against one common child, both conjugate ratios, h-family as
> check, swap symmetry as check only (Sol's §6 inversion observation —
> `(2+√3)(2−√3)=1` — is a free discriminator to log, not to assume);
> then, on a surviving solution, Opus 5's ⊖-constant transport across one
> chain edge as the depth-2 checkpoint. Kill ⟹ with §1's ROOT-W2′, the
> entire on-axis two-pole td=6 book closes at coefficient level.
>
> **Stage 2 (target side — the ghost-ray dichotomy, run only on the
> matched model).** Expand `g` and `h_1` along the q-only direction.
> The RES-AV dichotomy: **moving `b′`** (depends on a free tail
> coefficient, generic `a`) ⟹ `A(F)` contains a vertical set over dense
> `a` — contradiction with Jelonek's curve theorem (needs the
> `a`-uniformity lemma + primary pin) — residue A dies; **constant `b′`**
> ⟹ the campaign holds an explicit `A(F)` germ `(a, b′(a))`, and then and
> only then: (i) A47's LHS→branch assignment becomes well-defined with
> the level pinned at `c* = b′² − s_0a³` (the h₁-limit along the ghost
> ray — one line from `h_1 = g² − s_0f³`, `f→a`, `g→b′`); (ii) A47.1
> says the ghost sector is `(f,h_1)`-unramified iff `b′ ≠ 0` — a free
> dichotomy on the computed value; (iii) Q-GHOST's shift is instantiated
> at `b = b′` on the transposed fibration (connection C2); (iv) any
> merge-different length computation must inject into these off-tree
> objects or be dropped.

Why the composition is stronger than the parts: Stage 2 without Stage 1
has free tail coefficients, making the moving-vs-constant question
ill-posed (my blind Card 1b understated this); Stage 1 without Stage 2
can only kill, never charge; A47 without RES-AV has no well-defined left
side; Q-GHOST without the transposed reading has no vertex to create;
merge-different without retargeting has no injection target. And the
composed test is **non-budget**, which matters because the budget wall is
now proved three ways: overlay B (no factor 6/7; refinements cannot
price), the +1 arithmetic (Grok §1.1/Sol: `3≤3` still survives R3), and
the structural blindness of every `T_a`-supported functional. One honest
nuance overlay B adds that the blind round missed: a proved +1 charge
*would* kill the ψ=3 R4 boundary classes (their cap is exactly 2) while
leaving the R3 class — Opus 5's blanket "2 ≤ 3 ×4" misstates the R4 cap;
his NO-HIT conclusion survives (`2 ≤ 2` holds, tight).

---

## 3. Charge 3 — the A47 identity, verified; first missing implication

**Verification (elementary, exact; no CAS needed).** With
`h = g^α − s_0 f^β` and `J(f,g) = 1`, bilinearity and the chain rule give

```text
J(f,h) = J(f, g^α) − s_0 J(f, f^β) = α g^(α−1) J(f,g) − 0 = α g^(α−1),
J(h,g) = J(g^α, g) − s_0 J(f^β, g) = 0 − s_0 β f^(β−1) J(f,g) = −s_0 β f^(β−1).
```

For `(α,β)=(2,3)`: `J(f,h)=2g`, `J(h,g)=−3s_0f²`. **CONFIRMED.** The
degree statement `[ℂ(f,g):ℂ(f,h)]=2` (via `g² = h + s_0f³`, `g ∉ ℂ(f,h)`
in the nondegenerate case), hence `td(f,h)=2·td`, is standard
multiplicativity — also fine. These identities are unconditional; I found
no prior occurrence in the files I read (Opus 5's search claim stands).

**First exact missing implication** (in order; the budget is unusable
until (i) exists):

> **(i) Ghost landing / well-definedness = RES-AV's convergence step.**
> *For a resonant orbit `(F,b)` (root of `q_F`, not of `p_F`), prove that
> the ambient rays in direction `b` carry an actual branch at infinity of
> a pinned h₁-level curve — equivalently, compute whether the next-order
> cancellation along `b` converges and to which level `c*`.* Without it,
> `Σ l_Fν_F` counts pattern roots, not geometric objects, and the
> assignment `(F,b) ↦ (h-branch)` has no target. On the matched residue-A
> model, `c* = b′² − s_0a³` — so implication (i) for A47 *is literally
> the Stage-2 RES-AV computation*. One computation discharges both cards.

Then (ii) injectivity: the promoted Definition-3.3 attachment lemma must
be *re-proved* for h-witnesses in the ambient `T_a^*`/`R̄_a` presentation
(the flags `F*b` do not exist in `T_a`; citing `f55a00f5…` is not
enough — its Lemma 3.1 is quantified over selected exits with tree
children); the double-charge failure mode of `(22)`/`(22-cl)` is the
attack to run first. Then (iii) a computable right side: `N_∞(h)` in the
fibre-`a` sector pinned without a landing theorem. A kill needs the
sector count `< 3` (`l·ν = 3` at `G_m`); no one has computed it; do not
assume either direction.

---

## 4. Charge 4 — fastest complete GGV route

**Decision: hybrid.** (a) Keep the held, mutation-gated substitution-only
repair of the q1p03 complement-recursion pilot as the **single gate
node** — it is built, its failure was adapter-level only (a literal
`REDUCER_PLACEHOLDER` surviving generation; Singular rc0 with parser
diagnostics; the 95-pivot marker gate correctly failed closed before any
mathematical inference — treat that as the fanout gate *working*, not as
evidence about the mathematics). (b) After one full node passes, do not
continue per-chart complement chains: reorganize **level-wise Fitting**
(my blind §2.5 / Opus 5 §6 agree on the object): the next object after a
chart layer is the single closed set cut by *all* size-`r` minors (the
honest rank-drop locus), so the tree has at most rank-many levels
(`9/104` banks ≤ 9) instead of unbounded chart branching (Sol's per-chart
recursion and Grok's minor atlas both lack a termination invariant at
scale; Grok's own `C(106,105)`-scale worry applies). (c) Do **not** bet
the lane on the syzygy=kernel shortcut until Opus 5's §6.4 reducedness
check passes on the smallest branch (`Q1P03`, `4/99`) — one cheap job; on
failure, fall back to the assumption-free `coker(M)` presentation +
Fitting decision (Opus 5's fallback = Grok's "module presentation as the
proof object"). No saturation/radical shortcuts; no primitive-clearing of
cofactors.

**Fail-closed proof-object contract (merged G0–G7, all mandatory):**

- **G0** frozen custody: pinned `M` (106×105), `E = x14*x72 + x1*x97`,
  95-pivot list, ambient `std(I)` hash; generated scripts must pass a
  placeholder-token scan (the `REDUCER_PLACEHOLDER` class) and a parser-
  diagnostic scan even at rc0.
- **G1** pinned ambient standard basis; NF replay after every operation;
  `q2 mod (q2) = 0` negative control per job (the banked reducer-safe
  contract).
- **G2** rank certificate per level: nonzero-NF witness + exhaustive
  next-minor vanishing.
- **G3** kernel certificate: explicit generators with `NF(M·k_j) = 0`.
- **G4** endpoint decision banked in NF: the literal pullback of `E`
  (coefficient ideal in the kernel parameters), with degree census.
- **G5** planted controls: `E+1` must give nonzero NF (a PASS on the
  planted control is a job failure); the 95-pivot replay marker must be
  present (the gate that caught the placeholder).
- **G6** leaf discipline: verdicts only `EMPTY` (unit-ideal certificate),
  `ENDPOINT_DEAD_AT_LEVEL_r`, `SURVIVOR` (explicit witness → K00-style
  escalation), or `NO_VERDICT_…`; per-level cover accounting (cover
  cocertificate `1 ∈ (minors)+I`, or explicit passage of the residual to
  the next level — either way no verdict is lost); dense-open death never
  promoted to component death; every complement explicitly tagged until
  its own level closes.
- **G7** zero swap; custody manifests; independent replay before any
  promotion.

**AWS fanout trigger:** exactly the packet's — held until **one full
exact node passes G0–G7 end-to-end plus its independent mutation gate**;
then Phase A = the six branches (`P`, `C8P02`, `Q1P02`, `Q1P03`,
`TRIPLE02`, `TRIPLE03`) at 16 vCPU/128 GiB zero-swap each; further splits
only on mathematically distinct Fitting levels; ≤ 12 workers before
review (well inside 512 vCPU). Scope guard: everything here decides the
one frozen matrix/endpoint family; it closes or seeds Avenue-1 material
only, and licenses nothing beyond `ENDPOINT_DEAD_ONLY_ON_D(Delta)` until
complements close.

---

## 5. Charge 5 — three genuinely new connections (visible only after unblinding)

- **C1 — The ghost-ray unification (RES-AV = A47's missing half; the
  h₁-limit tie).** My blind RES-AV and Opus 5's A47 were built
  independently; read together, A47's first missing implication is
  exactly RES-AV's convergence computation, and the h₁-level A47 must
  count at is pinned by RES-AV's output (`c* = b′² − s_0a³`), while
  A47.1 adds the one exact global fact nobody else has (ramification of
  `(f,h_1)` is `{g=0}`, so the ghost sector is `(f,h_1)`-unramified iff
  `b′ ≠ 0`). One Stage-2 computation discharges or kills both proposals
  simultaneously. Not in any single report or in `APPROACHES.md`.
- **C2 — Bilateral cross-pinning at the asymptotic fibre.** Grok's
  Q-GHOST shift value, made sound, is RES-AV's `b′`; my blind BILATERAL
  card ran the transposed fibration at a generic prescribed fibre. The
  composition: run the g-side tree at the *canonical* fibre `g = b′` —
  the two trees of a td=6 counterexample are coupled through the point
  `(a,b′) ∈ A(F)`, and the transposed template must land a genuine
  branch/vertex structure where the f-side tree is structurally blind.
  This converts Q-GHOST from an unsound in-tree mechanism into a
  checkable instance of promoted-formula arithmetic, and gives the
  constant-`b′` branch of Stage 2 a second, independent budget (the
  g-side tree's own MFE). Conditional on the same sanctioned perimeter as
  BILATERAL; inherits RES-AV's named dependencies.
- **C3 — The `L1a(b)`-free root closure and the td=7 convergence.**
  Overlay A's edgewise law + MP4/MP5's riders + DEPTH §1's pre-root
  segment setting close the td=6 two-pole root sector for all `μ` without
  Opus 5's fragile step and without the mutated `SHEET6-L1` (§1). The
  same synthesis shows Opus 5's ROOT-REACH row `(2,2,3,3)` (`w_0 = 8/3`,
  `W ∋ 2/3`) and my blind §2.2 example are the *same* first live root
  frame at td=7, blocked by the *same* missing lemma — the post-jump/
  `M≥2` w-transfer law (Opus 5 §3.4 item 1 = my §2.2), for which my
  candidate closed form `w_child = w(r+l)/(lν+1)` already reproduces the
  promoted DS4 handshake values (`κ̄=5, ρ=1/2, w=3/2` at the residue-A
  cell). Merge the two work items into one lemma with that consistency
  gate; it is the single cheapest unblocked Sigray item after Stage 1.

---

## 6. Charge 6 — ranked 6-hour execution queue

Resource split: **≈60% proof / ≈40% disproof** (items 1–2 proof-side;
item 3's constant-`b′` branch, item 5, and any Stage-1 survivor
hardening are disproof-side). Desk work only, except item 5's single AWS
node; any elimination exceeding standard-library exact arithmetic goes to
AWS, not local.

1. **[0:00–1:00] File ROOT-W2′** (§1.2) for different-model hostile
   review: the repaired composition + the two glue paragraphs (searrow-
   parent glue; Prop 8.3(ii) shared-debt flag) + the St 8.5-vs-8.4 root
   citation fix. Cancel the m=2 root recensus scope pending the verdict.
   *Stop rule:* if the searrow-parent glue or the root divisibility fails
   re-derivation against the printed source, revert to "root sector
   open", keep the recensus, record the exact failing citation.
2. **[1:00–3:30] Stage 1, pattern level:** simultaneous two-parent
   Prop 9.3 match at `(2,3,1)` over `ℚ(√3)`, both conjugate ratios, one
   common child; swap/inversion logged as checks only. Exact
   standard-library arithmetic; provenance per equation. *Stop rules:*
   any equation requiring M-PAT beyond the exhibit's recorded anatomy or
   an unproved convention ⟹ file the missing statement and halt; unit
   ideal/incompatible ratios ⟹ halt and draft the kill packet for
   hostile review (do not self-promote).
3. **[3:30–5:00] Stage 2, first order (only on a Stage-1-consistent
   model;** otherwise spend the block hardening the Stage-1 kill packet):
   expand `g` and `h_1` along the ghost direction; decide moving-vs-
   constant `b′` at first order; record `c*` and the `b′ = 0?` A47.1
   dichotomy. *Stop rules:* St 9.1's `κ̄ = D + D_g` domain fails at the
   merge ⟹ halt RES-AV and file; required depth exceeds the pinned model
   ⟹ file the exact M-PAT-tier statement needed; no in-`T_a` charge may
   be written under any outcome.
4. **[5:00–5:30] Write (no proof attempt)** the A47 well-definedness
   lemma statement (§3(i)–(iii)) and the C2 bilateral-at-`b′` derivation
   plan, each with its dependency list and fail-closed clauses.
5. **[5:30–6:00] GGV gate check:** read the mutation-gate result of the
   substitution-only repair; if green, authorize the single q1p03 node
   under G0–G7; fanout only on a full pass. *Stop rule:* any
   placeholder-token hit, marker absence, or NF-control failure ⟹ fail
   closed; no relaunch without an adapter diff review.

Below the line (explicitly deferred): MFE/λ refinements (proved
threefold-insufficient — overlay B, +1 arithmetic, structural blindness);
merge-different as printed (§2.1, DOA); any `w=l/(r+l)` use beyond
all-`μ=1`; ROOT-REACH `not excluded` rows as evidence; the post-jump
w-law proof (next session's item, after C3's merge); ALPHABET compiler
build (worthy, but not a 6-hour item; its V1–V5 gates are endorsed).

---

## 7. Charge 7 — epistemic ledger

### 7.1 Promoted facts consumed (at their exact scopes, no wider)

- MFE at selected-exit/shared-inequality scope with the pole-endpoint
  truncation repair (`c74fc0f9…`, `f55a00f5…`, `9f4526f2…`,
  `86b491ad…`); `(C7.1*)`; the attachment Lemma 3.1(1)–(3).
- Mixed-root-window edgewise theorem, overlay A GREEN: `X_R = μ_e(1−w_e)`,
  `0 < w_e < 1` per actual searrow parent edge; its `μ=1`-present MP6
  root anatomy; its scope firewall for all-`μ≥2` (nothing here infers
  `A=Σμ`, `B=r+l`, `k=0`, or `B>A` there).
- (R1)/(R2); all-`μ=1` (R3) `w=l/(r+l)`; row-1 alphabet `W={2}`;
  DS1–DS4 + Chain-Depth Closure at DEPTH's recorded H1 tier and stated
  perimeter (no `M≥2` suffix law, no depth cap claim).
- MP0–MP7 at `SHEET6-MULTIPOLE`'s recorded scopes, including MP5's
  no-separating-ray and `μ_i=1` arrival riders, MP6(a)/(e).
- Corrected Section 8 scope: Prop 8.4 nonroot-only; root `M=1` legal;
  root divisibility via Statement 8.5.
- The §6a residue-A exhibit as a Q-level necessary-condition object
  (never as a realizable forest); its rigid ODE ratio `2±√3`; ψ-transport
  `ψ = ceil(k_f/l_f) − 1`.
- GGV: six reducer-safe rank certificates (`9/104`, `6/101`, `4/99`) as
  rank certificates only; overlay C: all six exact endpoint charts
  `ENDPOINT_DEAD_ONLY_ON_D(Delta)`, every complement open; frozen hashes
  `dd460760…`/`71cd2bcd…` (archive `1fe30b1c…`), failed-pilot archive
  `33e20a4d…`.
- Overlay B: selected-exit weights 0/0/2, `ψ=2` (R3) with witness weight
  ∈ {2,3}, `ψ=3` (R4) exactly 2; no factor 6/7 licensed.

### 7.2 Provisional claims (used as such, promotion-gated)

ROOT-W2′ (§1 — REPAIR verdict, hostile review pending); the two-stage
combined test design (§2.2); the h₁-limit tie `c* = b′² − s_0a³` (one
line, but on the unproved RES-AV convergence); C2's bilateral-at-`b′`;
C3's merged w-law item with the candidate closed form; the G0–G7 merged
contract; TRIPLE02/03 completions and the q1p03 substitution repair
(mutation gate pending); `SHEET6-L1` content at its current (drifted)
hash.

### 7.3 Conjectures (no evidence yet)

RES-AV convergence and its dichotomy; A47-BUDGET (both halves); Q-GHOST
in any form (sound only as C2); merge-different length ≥ `l+1`;
Sol's swap/inversion obstruction; the post-jump `w`-transfer law; any
`td=6` exclusion, landing totality, `RPMC(C)`, cofinal ceiling. `G2-PSC`
and `G2-BD` remain distinct open obligations; nothing here touches
either.

### 7.4 Failed / dead (do not revive)

The in-`T_a` pricing of the ghost orbit (three independent proofs of
impossibility; overlay B confirms); merge-different's skyward injection
(empty target region — new finding, §2.1); printed `(22)`, `(22-cl)`,
literal `δ_a`, fixed/cross-fibre `κ`, equality/slack, MP8 no-refinement;
the l-free phase-3 root census; the q1p03 adapter as previously
generated (placeholder survived; archive `33e20a4d…`) — adapter failure,
not mathematics; Matysiak (unsound); naive dim-2 descent of the 3D CE.

### 7.5 Discrepancies found across the corpus (none verdict-critical)

1. `SHEET6-L1.md` hash drift vs Opus 5's recorded pin (header of this
   file); quoted content re-verified present.
2. Opus 5 cites "St 7.2" for pole `λ=0`; the sound citation is Prop 5.5
   + Prop 7.2 (St 7.2 is the known-unproved sidedness statement; the
   promoted MFE package explicitly does not use it).
3. Opus 5's "`2 ≤ 3` in every case" misstates the R4-class cap; overlay B
   gives `ψ=3`, cap 2, tight. NO-HIT conclusion unaffected; the R4
   classes are the ones a +1 charge would kill.
4. The packet's pole datum `Q=(2,2,2,2,5)`: MP4's format gives
   `(2,2,2,1,5)` (fourth slot `b_i = 1` = `M`); the printed fourth slot 2
   conflicts with row-1 `b=1`. Nothing consumes it (`w_0` uses slots
   1,2,3,5); my blind report dotted the slot. Fix at next canonical edit.
5. Grok's root-meet mixed-`μ` argument cites St 8.4 where the packet's
   corrected-Section-8 wording puts root-scope divisibility under St 8.5
   — handled in ROOT-W2′.

### 7.6 Files read and checks run

All ten pinned files read in full after hash verification: the
cross-packet, the 1707Z packet, the four peer reports, overlays A/B/C
primaries (`aaa4d179…`, `86b491ad…`, `9f4526f2…`, `f55a00f5…`,
`c74fc0f9…`). Dependency reads (unpinned, current worktree, disclosed):
`ladder/SHEET6-DEPTH.md` (§§1–9), `ladder/SHEET6-MULTIPOLE.md` (MP
statements, §§5–6, 9), `ladder/SHEET6-2POLE.md` (supersession box, §§0–6
via targeted search), `ladder/SHEET6-L1.md` (status, L1a, §7, residue
table). Checks: `shasum -a 256` on all pinned files; hand-replayed exact
arithmetic only — `w_0=(5−1)/2=2`; `W(2)={2}` (no `Δ≥3` divides 2);
merge child `κ̄=2·10/4=5`, `D/i=3`, `ρ=1/2`, `w=(5−1/2)/3=3/2`;
`ψ=ceil(126/42)−1=2`; MFE `0+0+2=2≤3`; `z²−4z+1` roots `2±√3`, product
1; `(2,2,3,3)`: `w_0=2(5−1)/3=8/3`, `Δ=8=(2−1)·7+1` gives `2/3`,
`Δ=4=(2−1)·3+1` gives `4/3` — matching both peers' tables; the A47
derivation in §3. No script was run; no engine, no AWS, no network, no
`jc2-lean`. Failed attempts: none operational; the substantive negative
findings (merge-different's empty target; Q-GHOST's in-tree failure) are
recorded in §2.1 with their proofs.

### 7.7 Contamination and scope

This round is deliberately unblinded; one peer report
(`ideation-20260828T1707Z-fable5.md`) is my own blind submission, and two
overlay files (`f55a00f5…`, `aaa4d179…` inputs) include my earlier
hostile review — I have treated my own prior claims with the same
adversarial standard as peers' (two of my blind claims are downgraded
here: Card 1b's dichotomy was understated as ill-posed without Stage 1;
my §10 closure lacked the variant of §1.1 Step 7). Persistent auto-memory
was present as background; no memory content was used as evidence.
This report promotes nothing, edits no canonical file, launches no
compute, and asserts no theorem. Everything new requires the ordinary
producer / different-model hostile review / coordinator-promotion gates.
