# Whole-portfolio ideation — `20260828T1707Z` — Fable 5

Lane: Fable 5 (Anthropic), exact model `claude-fable-5`, blind same-input round.
Packet: `xmodel/ideation-20260828T1707Z-packet.md`, SHA-256
`1e40e7106e2a3c16b6a6fe92e6d2387228fb1260ae5633e686b456e9f9d95f1c` — verified
before reading. All 17 custody-gate hashes verified against local files before
reading them (list in §11). No peer `20260828T1707Z` file was read or listed.
`jc2-lean` was not entered, listed, searched, read, built, modified,
status-checked, or controlled. No AWS, Singular, msolve, Sage, or Lean was
touched. Only `shasum`, file reads, and one small exact standard-library
Python check (§11) were run. This file is my only write. A model verdict is
not mathematical evidence; every new claim below is `PROVISIONAL/UNREVIEWED`.

---

## 1. Executive summary

1. **MFE composed literally on residue A: NO KILL.** The actual selected
   exit-orbit set over `U^full` is: poles 0+0, merge 0 (all p-roots are
   arrivals; the `l=1` orbit is not a direction of `T_a` at all), suffix
   vertex `(42,126,7,3,5)` contributes the single IIa `k=1` northeast orbit
   at price `lambda=2`. With `psi=2`: `2 <= 6-1-2 = 3`, slack 1. MFE
   *validates* the previously conditional shared budget; it sharpens nothing
   and cannot be refined inside `T_a` (§2.1).
2. **The resonant q-only orbit is an asymptotic-value door, not a chargeable
   exit.** At the residue-A merge, `St 9.1` gives `D_g = kappa-bar - D =
   5 - 6 = -1`: the `l=1` orbit kills the *last* polar level of `g`. Ambient
   rays in that direction have `f -> a` (order frozen at `D=6>0`) and
   plausibly `g -> b` finite: each such ray witnesses `(a,b) in A(F)`,
   Jelonek's asymptotic variety. The books have, for the first time, a
   concrete `A(F)` construction site — and a new kill route via the
   dimension of `A(F)` (§5, card 2). This explains *why* the printed theory
   is blind to the residue: p-roots are fibre doors (priced), q-only roots
   are nonproperness doors (target-side data).
3. **Likely-missed insight: the td=6 two-pole root sector is now closed
   outright**, not merely its all-`M=1` layer. At `td=6, m=2` the entries
   are forced to the unique `Lambda=3` row (`a=b=1, nu=2`), so `M=1` and
   `mu=1` are forced on both chains (MP4+MP5), and MP1 allows exactly one
   merge — so *every* root meet in that sector is all-`mu=1`, which the
   promoted theorem excludes. Mixed-`mu`/off-axis root recensus is vacuous
   at `td=6` two-pole; the entire td=6 root frontier is the single-pole
   (HIII/SF1) root-signature recensus (§10).
4. **The root identity generalizes exactly as far as an M>=2 w-transfer
   law.** (R1)–(R2) are already promoted per-edge at mixed `mu`; the first
   exact missing implication is DS2/DS3 for `M>=2` segments plus the
   jump-cell transfer `w_child = w(r+l)/(l*nu+1)` (which reproduces the
   printed suffix `w=3/2` at residue A). A hand computation finds the first
   candidate live root frame beyond td=6: entry `(a,b,nu)=(2,1,3)` at
   `Lambda=4` has `w_0=8/3` with an admissible resonant step to `2/3<1`,
   matching an `l=4` root meet inside the td=7 two-pole budget (§2.2).
5. **GGV lane: replace per-chart complement recursion by a level-wise
   Fitting atlas** with unit-cocertificate cover gates; termination in at
   most rank-many levels; every leaf ends `EMPTY`, `ENDPOINT-ZERO`, or
   `SURVIVOR` — fail closed (§2.5, card 3).
6. Avenue changes: **raise 7 narrowly** (A(F) finally has a
   books-constructed client), **raise 27 narrowly** (bilateral splice +
   van Dobben pi_1-at-infinity filter on the doubly pinned template). All
   other calls unchanged from the 17:03Z overlay; `G2-PSC` and `G2-BD`
   remain distinct obligations throughout.

---

## 2. The seven packet questions

### 2.1 Compose MFE literally (Q1)

Ledger over `U^full` for residue A (exact data from `SHEET6-2POLE.md` §6a,
replayed in my §11 check):

- Poles `P1=P2=(2,2,2,·,5)`: `lambda=0` each (Prop 5.5 + Prop 7.2: every
  puncture above a pole has `g=infinity`; no cv flag).
- Merge `G_m=(6,12,3,2,5)`: **selected exit set empty.** MP6(a) `k=0`: every
  root of `p_{G_m}` is a chain arrival (excluded before pricing); the
  rootward continuation is excluded; the `l=1` orbit is a root of `q` only —
  by corrected St 3.18 it is not a direction (no `F*c`), carries no `T_a`
  flag, and is not in the orbit set `D_{G_m}` at all. `lambda=0` — now
  *sound* under MFE rather than asserted via the withdrawn equality.
- Suffix vertex `F=(42,126,7,3,5)`: one IIa `k=1` non-chain p-root orbit,
  northeast; AF2 price `lambda = k*max(1, ceil(D/i - kappa-bar)) =
  1*ceil(7-5) = 2`. Its St 7.3 witness is distinct from the x-side witness
  (two components, St 3.3) and unique (attachment lemma).
- Terminal: `psi = ceil(126/42)-1 = 2`.

MFE: `sum lambda^exit = 2 <= td-1-psi = 3`. **NO HIT** — slack 1. The two
robust residue-A classes survive at slack 1; the boundary classes at
`Sigma lambda = 3` survive tight. MFE's real contribution is that this
budget is now unconditional at scope (previously conditional on cross-chain
disjointness); numerically nothing changes.

**Can a sound refinement price the q-only orbit? Not inside `T_a`.** I
attempted it and it fails at the object level, instructively: the e-orbit
direction carries no fibre branch (`p(e) != 0`, Prop 3.1(**)), hence no
`V_a` vertex, no puncture, no threshold, and no `T_{a,cv}` flag — St 7.3
and (C7.1*) have nothing to attach. Any `T_a`-internal charge would revive
the quarantined `(22)`-type equality. The two sound doors are: (a) exhibit
one *additional genuine cv flag of the same fibre* forced by the resonance
— nothing visible supplies one; (b) leave `T_a` entirely and price the
orbit as target-side nonproperness data — §2.4/card 2 (`RES-AV`), which is
where I judge the real content of the orbit lives.

### 2.2 Push the root identity (Q2)

(R1)–(R2) are promoted per incoming edge at any genuine root meet,
including mixed `mu`: `X_F = D_F/i = mu_e(1-w_e)` forces `w_e < 1` at
*every* parent. I do not extend `w=l/(r+l)` beyond all-`mu=1`. The exact
first missing implication for a broader root kill is:

> **M>=2 w-transfer law (to prove).** For every `M>=2` chain segment and
> every `l>=1` jump-cell emission, the child invariant satisfies
> `w_child = w(r+l)/(l*nu+1)` (from the DS4 handshake: `kappa-bar_child =
> w*dq/Delta`, `rho_child = w/Delta`, so `w_child = w(dq-1)/(Delta*nu)`,
> which for IIa is exactly `w(r+l)/(l*nu+1)`), and `M>=2` chain steps
> conserve/contract `w` as in DS2/DS3.

Consistency check: residue A's cell `(2,3,1)` gives `w_child = 2*3/4 = 3/2`
— exactly the printed St 9.6(v) suffix conservation value (DEPTH check 5).
Since `3/2 >= 1`, the residue-A suffix can never feed a root meet; its
case-IV interior terminal is forced, independently re-derived.

Boundary of the tool (hand computation, `PROVISIONAL`): all entries have
`w_0 = a(b(alpha+beta)-1)/(b*nu) > 1` (since `nu <= beta`, `alpha >= 2`),
and integer `w` stays `>= 2` under resonance; but non-integer `w_0` can
drop below 1: entry `(a,b,nu)=(2,1,3)` at type `(2,3)`, `Lambda=4`, has
`w_0 = 8/3` and the resonant step `Delta=8, (n,nu)=(2,7), dq=15` is
admissible (`b*Delta=24 | a*dq=30`? — no: `24 | 2*15=30` fails; the correct
check is `kappa-bar_F = w*dq/Delta = (8/3)(15/8) = 5 in Z`, which passes),
giving `w' = 2/3 < 1`, matching an `l=4` all-`mu=1` root meet within the
td=7 two-pole budget (`psi=5`, `Sigma lambda <= 1`). So td=6 was lucky
(`W={2}`); at td=7 the two-pole *root* book has a live frame and the
transfer law is what decides it. This example needs the per-edge
`n_e ≡ -kappa-bar (mod nu)` admissibility replayed before use.

### 2.3 A new global composition (Q3)

Two literal theorem interfaces; otherwise NO HIT (Riemann–Hurwitz/Euler
recombination warnings stand):

1. **RES-AV (books -> A(F)), the new mechanism** — see §5 and card 2. If it
   closes, it yields a *new global object* (the germ of the asymptotic
   curve `{(a, b(a))}`) with pinned Puiseux data, feeding Avenue 6's
   one-place machinery on the correct object for the first time; its
   moving-value branch threatens residue A with a dimension contradiction
   against Jelonek's curve theorem.
2. **Bilateral book cross-pinning (Avenue 2 ↔ 25/27), the new connection**
   — §5. Conditional on the sanctioned single-pole closure, *both*
   fibrations of a td=6 counterexample are two-pole residue A; the
   transposed template's forced data must coexist with the original's on
   one plane. First consistency check passes (`l/k = 1/3` on both sides,
   §11); the discriminating next check is matching the g-side pole entries
   against the f-side `f->infinity` / x-side data, then feeding the merged
   boundary data to the splice/`pi_1`-at-infinity filter (van Dobben
   arXiv:2608.27341 lens).

### 2.4 Attack the concrete survivor (Q4)

Ranking by information per hour:

1. **Coefficient-vs-parent H1 match at the `(2,3,1)` cell** (MULTIPOLE §8
   item 3): match the rigid merged coefficients (`a1/a2 = 2±sqrt(3)`)
   against both row-1 parents' Prop 9.3(a)–(d) edge equations and their own
   Prop 8.1(iv) identities. Finite exact solve in `Q(sqrt 3)`; the single
   most valuable H1-tier computation; kills the minimal td=6 interior cell
   or hardens it into a coefficient-complete seed. (Card 1a.)
2. **RES-AV dichotomy on the same local model** (card 1b): expand `g` along
   the `l`-orbit direction (`D_g=-1`, one cancellation from finiteness) and
   decide whether the asymptotic value `b` depends on free tail
   coefficients. Moving `b` for generic `a` contradicts `dim A(F) = 1`;
   constant `b` pins the `A(F)` germ.
3. Merged-pattern inadmissibility (2POLE L1) stays the highest-*value*
   target but has no new entry point; the two computations above are its
   cheapest concrete probes.
4. Puiseux algebraization / direct collision construction: run only after
   1–2, seeded by whichever coefficient family survives.

### 2.5 Optimize the GGV recursion (Q5)

Stop recursing on per-chart complements; they multiply without a
termination invariant. Use a **level-wise Fitting atlas** (card 3): at each
level, the certified object is a closed variety `V_k` (start: each branch);
compute the rank `r_k` and the finitely many size-`r_k` minors; the charts
`D(Delta_i)` carry the adjugate kernel + endpoint-NF-zero test; the *next
level* is the single closed set `V_{k+1} = V_k ∩ V(all size-r_k minors)` —
the honest rank-drop locus — never a per-chart complement. Termination:
rank strictly drops, bounded by 9 levels from the banked `9/104`. Gates:
(i) a cover cocertificate `1 in (minors)+I(V_k)` or explicit passage of the
residual to level `k+1`; (ii) reducer-safe pinned ambient `std` + NF replay
on every operation (the banked contract); (iii) leaf verdicts only
`EMPTY` (unit), `ENDPOINT-ZERO` (NF certificate), or `SURVIVOR` (explicit
point -> immediate K00-style escalation). AWS fanout: one 16-vCPU/128-GiB
instance per (branch, level), ≤ 6 branches and ≤ 4 live levels — well
inside the 512-vCPU quota, zero swap. This converts
`NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED` into a complete finite verdict.

### 2.6 Proof vs disproof re-rank (Q6) — see §4.

### 2.7 Software (Q7) — see §7.

---

## 3. Disposition vector, avenues 1–46

Baseline is the 17:03Z overlay; "unchanged" means unchanged relative to it
(which already carries: 2 principal/raised, 1 redesigned-continue, 4
raised-narrow, 16 lowered, 25 gated-pilot, 36 raised/protected).

**Changed (2):**

| # | Avenue | Call | Reason |
|--:|---|---|---|
| 7 | Nonproperness / Jelonek `A(F)` | **raise (narrow)** | RES-AV gives the first concrete `A(F)` construction site *from the books* (the `D_g=-1` q-only orbit at the residue-A merge) plus a new kill route (dimension of `A(F)`). This resolves the old S:8-vs-Grok dissent operationally: the first experiment is now bounded and exact, not "rebuild the compactification". |
| 27 | Links at infinity / splice | **raise (narrow)** | The doubly pinned template (coefficient rigidity + prospective bilateral pin) plus the van Dobben `pi_1`-at-infinity filter give it two concrete new clients; Domrina's precedent (splice arithmetic killed the td=4 multi-dicritical case) says this layer can finish what fibre-side accounting cannot. |

**Unchanged, grouped:**

- *Core/raised, keep exactly as set:* 1 (GGV rank/Fitting redesign; card 3
  is an amendment, not a re-rank), 2 (principal proof backbone; the two new
  green theorems and §10's closure strengthen it; `G2-PSC` and `G2-BD`
  remain separate obligations and are never merged), 4 (raise-narrow:
  germ→polynomial algebraization arrow, now with a better seed), 36/K00
  (raised/protected strongest finite falsifier).
- *Typed pilots, keep gated:* 6 (one-place on `A(F)` components — becomes
  the named client of RES-AV's constant-`b` branch but is not raised until
  that lands), 25 (coupled two-coordinate: bilateral cross-pinning is the
  tree-level cousin and is filed under Avenue 2; no monodromy rerun), 26,
  31.
- *Lowered/execution-parked, keep:* 16 (HENS-CT: redesign-gated), 3
  (unchanged; its ODE rigidity is the engine of card 1), 5, 8, 9, 12, 13,
  15, 17, 20, 21, 28 (the van Dobben filter is filed under 27; BMY itself
  still NEEDS-DATA), 29, 30, 32, 33 (COSTUME), 34, 35, 37, 38, 39, 40, 42,
  43, 45, 46.
- *Char-p lane:* 19 unchanged (degree-12 partial-degree frontier; conductor
  growth quantification only). K00 is *not* Avenue 19.
- *Dead/refuted, keep closed:* 10, 11, 14 (defensive recon only), 18, 22,
  23, 24, 41, 44 (repaired membership theorem only).

No avenue is reopened.

---

## 4. Bottleneck reranking

**Proof (3):**

1. **Universal full-configuration landing** — unchanged at the top; the
   marked-first-event theorem still needs typing, totality, and provenance
   (REDUCTION Critical 4–6).
2. **Cofinal `td`/complexity ceiling + `RPMC(C)` + independent type
   control** — unchanged; no candidate mechanism appeared this round.
3. **Concrete td=6 closure** — *new at rank 3, displacing source trust*
   (Sections 5–9 are now review-closed at repaired scope; the remaining
   source items — St 6.2's omitted domain, St 3.14's twist, H5a filing —
   are riders, not walls). Content: kill residue A (card 1) and finish the
   single-pole root-signature recensus; §10 shows these are the *only*
   td=6 residues.

**Disproof (2):**

1. **K00 / full-`P6` rank-exact point plus one prolongation** — unchanged
   strongest bounded falsifier; preregistration gate then AWS.
2. **Residue-A realizability → algebraization → collision** — raised in
   quality: the seed is about to become coefficient-complete (card 1a) and
   carries a target-side invariant (`b(a)` germ, card 1b) that an actual
   construction must match; the char-p/Witt route stays third.

---

## 5. New mechanism and new connection

**New mechanism — `RES-AV` (resonant orbit = asymptotic-value door).**
At any resonant jump cell, the `l` extra q-orbits are roots of the
`g`-pattern that are not roots of the `f`-pattern: no fibre branch
continues there, so the entire `T_a` apparatus (vertices, punctures,
thresholds, cv flags, `lambda`) is structurally blind to them — that is
Theorem O. But *ambient* Puiseux rays in those directions exist, have
`ord(f-a)` frozen at `D>0` (so `f -> a`), and reduce the polar order of
`g` by construction. At the residue-A merge, St 9.1 (`kappa-bar = D +
D_g`) gives `D_g = 5-6 = -1`: the orbit cancels the *last* polar level, so
one step plausibly reaches `g -> b` finite. Every such ray witnesses
`(a,b) in A(F)`. Dichotomy: if `b` moves with the free tail coefficients
for generic `a`, then `A(F)` contains `{a} x (infinitely many values)` for
a Zariski-dense set of `a`, contradicting Jelonek's theorem that `A(F)` is
a curve; if `b` is constant, the books hand Avenue 6/7 the explicit germ of
an `A(F)` component. *Comparison with repository history:* Avenue 7's row
records "A(F) never constructed from the books" and the earlier raw
all-directions pencil defect stopped `JUMP-ONLY/TYPE-FAIL`; Sol's S9
proposed constructing asymptotic values for the smallest book but named no
site or mechanism. RES-AV supplies the exact site (`D_g=-1` q-only
orbits), the exact local model (the rigid `(2,3,1)` coefficients), and a
kill route (dimension of `A(F)`) that appears nowhere in `APPROACHES.md`,
`REDUCTION.md`, or the sheets. Honest gaps it must close: the `a`-generic
uniformity of the configuration (the books fix one fibre), the primary-text
pin of Jelonek's curve theorem for dominant plane Keller maps, and the
depth to which the merged local model determines `g`'s expansion (M-PAT
tier). My own failed sharper version is disclosed in §11.

**New connection — bilateral book cross-pinning (Avenue 2 with 25/27).**
`td` is symmetric, so the transposed fibration of a td=6 counterexample has
its own Sigray tree, its own `Lambda' = 3+3` forcing, hence (conditional on
the sanctioned single-pole closure) its own two-pole residue-A template of
type `(2,3)`. Both templates live on one plane and share its ends. First
check (passes, §11): the f-side terminal forces `(k_f,l_f;k_g,l_g) =
(126,42;189,63)` with `l/k = 1/3` on both coordinates — consistent.
Discriminating next check: the g-side template forces two row-1 f-pole
entries in *its* tree; translate them through the shared end set into
f-side `f->infinity`/x-side data and compare with the f-template's `psi=2`
x-side witness. A clash excludes td=6 modulo the sanctioned perimeter; a
match doubles the seed's rigidity and yields merged boundary data for the
splice/`pi_1`-at-infinity filter. *Comparison with history:* Avenue 25's
coupled CSP (Sol S12) couples the two fibrations at the *monodromy* level
and is gated; the transpose discriminator in REDUCTION Critical 3 conjugates
*charts of one fibration*, not the two fibrations; splice diagrams were
tried on residue-A's f-side only. Tree-level cross-pinning using the
promoted book closures is not in the record.

---

## 6. Strongest attacks to run next

- **Proof attack:** card 1a — the exact `(2,3,1)` coefficient-vs-parent
  match. It is the campaign's named single most valuable H1 computation,
  now finally cheap, and §10 means a kill there (plus the single-pole
  recensus) closes td=6's two-pole interior at coefficient level.
- **Counterexample attack:** card 1b's constant-`b` branch feeding a
  depth-limited jet construction: impose the residue-A template, the
  matched coefficients, and the `b(a)` germ as *data*, and prolong the
  Keller jet system at infinity (Avenue 4 machinery pointed at the Sigray
  template instead of branch P). Growing-depth consistency is a seed;
  low-depth inconsistency is an independent kill. K00 stays queued in
  parallel as the orthogonal falsifier.

---

## 7. Software acceleration / decisive experiment

**MFE-conformant book auditor + asymptotic-door column.** Extend the
repaired root-aware engines (before the AWS census launches) with:

1. a selected-exit ownership module: build `U^full`, one direction-orbit
   set per vertex, dedupe shared suffixes, price exits once, emit the MFE
   ledger `sum lambda^exit <= td-1-psi` per configuration;
2. a `D_g = kappa-bar - D` column on every jump cell, flagging
   `D_g = -1` cells as `RES-AV-APPLICABLE`.

Exact verification gate: reproduce the §6a residue-A ledger (`2 <= 3`) and
the existing St 9.6(iii)/(iv)/(v) lambda values `2,2,0` already replayed by
`sheet6_campaign.gate()`; mandatory negative control: a mutant that prices
per incoming edge or duplicates a shared-suffix vertex must be flagged
nonconforming (the integration explicitly requires this failure mode to
fail closed). Cost: one lane-day plus review; it makes every present and
future book survivor carry an automatic, sound global budget instead of a
hand ledger.

---

## 8. Idea cards (3)

**Card 1 — `RESA-LOCAL`: exact local model of the residue-A merge; match
and dichotomy.**
*Dependencies/licensed assumptions:* promoted H1 tier (Prop 9.3(a)–(d)),
Prop 8.1(i)/(iv), St 3.17/8.4, MP4–MP7, the rigid ODE facts
(`cases/l1_ode_check.py`, `a1/a2 = 2±sqrt(3)`); for part (b) additionally
M-PAT (merged q-shape, flagged unproven tier), St 9.1's identity
`kappa-bar = D + D_g` on chain vertices (verify its printed domain), and a
primary-text pin of Jelonek's `A(F)`-curve theorem.
*Cheapest decisive discriminator:* (a) finite exact solve in `Q(sqrt 3)`
matching the merged cell's pinned coefficients against both row-1 parents'
per-edge equations; (b) on the same model, first-order expansion of `g`
along the `l`-orbit: does the limit `b` depend on the first free tail
coefficient?
*Materially different outcomes:* (a) inconsistent → the unique td=6
interior cell dies at coefficient level (with §10, td=6 two-pole closes;
huge). (a) consistent → coefficient-complete seed; proceed to (b).
(b) moving `b` → dimension-contradiction route opens (needs the
`a`-uniformity lemma; if that lemma holds, residue A dies). (b) constant
`b` → explicit `A(F)` germ; hand to Avenue 6/7 and the jet-construction
lane.
*Stop/rollback:* stop if the match requires coefficient conventions beyond
H1/M-PAT or if St 9.1's domain excludes the merge; file the exact missing
statement instead of proceeding.
*Cost:* 1–2 lane-days desk algebra + one hostile review; no AWS.
*Information gain:* highest available per hour — it decides the campaign's
distinguished td=6 object either way.

**Card 2 — `BILATERAL`: transposed-fibration cross-pinning.**
*Dependencies/licensed assumptions:* td symmetry; promoted `Lambda>=beta`,
every-fibre mass replacement, MP4, table (23); the *conditional*
single-pole td=6 closure at its sanctioned perimeter {H1,H2,H4,AF2,AF3,
H5a/b,H3q} — the conclusion inherits exactly that conditionality and must
say so.
*Cheapest decisive discriminator:* derive the transposed pair's normalized
type and two forced row-1 entries; translate through the shared end set
into f-side `f->infinity` data; compare with the f-template's x-side/psi
data. Pure promoted-formula arithmetic.
*Materially different outcomes:* clash → td=6 excluded modulo the sanctioned
perimeter; match → doubled rigidity plus merged boundary data for the
splice/pi_1 filter; undetermined → names the exact missing decoration
(a sharp new sub-gap, likely a genuine two-sided landing obligation).
*Stop/rollback:* stop when the translation needs any cross-tree lemma not
derivable from promoted statements; file that lemma as the interface.
*Cost:* 1–2 lane-days + review; no AWS.
*Information gain:* high; also a template for bilateral analysis at td=7+.

**Card 3 — `FITTING-ATLAS`: complete GGV endpoint recursion.**
*Dependencies/licensed assumptions:* banked reducer-safe NF contract and
the six rank certificates; frozen matrix and endpoint `x14*x72+x1*x97`;
no radical/saturation shortcuts (set-cover only).
*Cheapest decisive discriminator:* level-1 cover cocertificate
`1 in (size-r minors) + I(branch)` per branch; if it fails, the residual
closed set *is* the next level — no verdict is lost either way.
*Materially different outcomes:* all leaves `EMPTY`/`ENDPOINT-ZERO` → the
lambda-zero fixed-face family is endpoint-dead completely (retire it);
any `SURVIVOR` point → immediate escalation to the K00-style prolongation
pipeline (counterexample side).
*Stop/rollback:* fail closed on any custody, NF-control, swap, or cap
event; hard cap at 9 levels (rank bound); every level's verdict is
independent, so partial progress banks.
*Cost:* ≤ 24 AWS jobs at 16 vCPU/128 GiB, days; review of the atlas gate
design first.
*Information gain:* converts the standing `NO_VERDICT` complements into a
finite complete verdict for the whole recursion.

---

## 9. Lane calls

| Lane | Call | Note |
|---|---|---|
| Pure Sigray / exact-pair | **continue** | principal backbone; next: cards 1–2, the M>=2 w-transfer law, landing typing |
| Hybrid `G2-PSC` | **continue (minimal)** | typed interface only; no census; `G2-PSC` stays a distinct unproved obligation, never merged with `G2-BD` |
| Arbitrary-Q / rank-drop GGV | **continue (amended)** | adopt the Fitting-atlas recursion (card 3); no per-chart complement chains |
| Lambda-nonzero / raw-window GGV | **continue** | recurrence/row-ideal invariance or complete raw-window/endpoint incidence; order six stays banned |
| LF40 | **redesign** | repeated `RESOURCE_CAP_NO_VERDICT` on identical engines; no identical relaunch; park until a genuinely different frozen presentation (e.g. stratified/localized) exists |
| K00 / order-two / TD6 | **continue** | protected falsifier; preregistered BASE4/LOW-KILL; the single-pole root-signature recensus on r6d is now the *whole* td=6 root frontier (§10) |
| D43 | **continue (maintenance)** | only as an Avenue-4 algebraization client; no new heavy runs licensed |
| Artin–Schreier | **continue** | degree-12 partial-degree frontier and conductor-growth quantification only |
| HENS-CT | **redesign** | structural adapter + named client before any rerun; no generic `annihilator_of_composition` path |
| External intelligence | **continue** | next broad sweep due 2026-08-29 05:24Z; add (i) primary-text pin of Jelonek's `A(F)`-curve theorem for plane Keller maps, (ii) van Dobben follow-up/citations |

---

## 10. Likely-missed insight and its cheapest test

**At `td=6, m=2`, the entire root-merge sector is closed — the mixed-`mu`
and off-axis root riders are vacuous there.** Chain: (i) `Lambda_1 +
Lambda_2 = 6` with `Lambda_i >= beta >= 3` forces `(3,3)`, `beta=3`,
`alpha=2`; (ii) the unique `Lambda=3` row of table (23) is `(a,b,nu) =
(1,1,2)` (replayed exactly in §11), so both entries have `b=1`, `M=1`
forced (MP4); (iii) MP5 propagates `M=1` down both pre-merge chains, so by
St 8.4 every arrival has `mu=1`; (iv) MP1 gives exactly one merge vertex at
`m=2`, so no jump can precede a root meet, and off-axis entries do not
exist; hence (v) every root meet in the sector is all-`mu=1`/all-`M=1` —
exactly what the promoted case-I theorem excludes via `W={2}`. The current
canonical wording ("mixed-`mu` root-merge completeness awaits the corrected
AWS recensus", SHEET6-2POLE supersession box) therefore concedes more than
necessary at td=6: the recensus matters for the *single-pole* HIII/SF1 root
children and for `td>=7`, not for the td=6 two-pole root sector.
**Cheapest test:** a one-page composition note citing MP1/MP4/MP5/St 8.4
plus the promoted root theorem, with the row-uniqueness assertion machine-
checked (my §11 script does it), submitted to ordinary different-model
hostile review. If it passes, the td=6 frontier statement simplifies to:
interior residue A + single-pole root recensus, full stop.

---

## 11. Epistemic ledger

**Model.** Fable 5 (`claude-fable-5`), blind lane; sole write is this file.

**Custody.** Packet hash verified (header). All 17 custody hashes verified
by `shasum -a 256` and matched: `APPROACHES.md`, `AUDIT.md`,
`COORDINATION.md`, `PROGRESS.md`, `notes.md`, `ladder/REDUCTION.md`,
`ladder/SIGRAY-AUDIT.md`, `ladder/SHEET6-2POLE.md`,
`ladder/SHEET6-MULTIPOLE.md`, `ladder/SHEET6-DEPTH.md`, the 1149Z
synthesis, the 0524Z websweep, and the four coordinator/hostile reports.

**Files read (relevant portions of large files).** All five small xmodel
reports and the websweep in full; `SIGRAY-AUDIT.md`, `SHEET6-DEPTH.md`,
`SHEET6-MULTIPOLE.md`, `SHEET6-2POLE.md`, `COORDINATION.md` in full;
`APPROACHES.md`: full 17:03Z→06:23Z overlays, the complete 46-row master
table, consensus/dissent, provenance; `REDUCTION.md`: frontier overlay,
executive verdict, conventions, and the full gap list; `PROGRESS.md`: the
complete 2026-08-28 day; `notes.md`: all 2026-08-28 events from 12:38Z
through the 17:03Z LIVE STATE; `AUDIT.md`: the current correction block
(top ~120 lines) and section headings. Targeted greps for `LF40`, `D43`,
`SF1` to identify lanes.

**Checks run.** One exact standard-library Python check (`/tmp`, no CAS):
td=6 `Lambda` forcing and table-(23) row uniqueness at `Lambda=3`; DEPTH
entry invariant `w_0=2` and empty resonance set; `w=l/(r+l)` numbers; the
full §6a residue-A ledger (merge/suffix Q-data, per-edge ratios, gcds,
case-IV clauses, `psi=2`, budget `2<=3`); `(k_g,l_g)=(189,63)` and the
bilateral `1/3` ratio; positivity/`<1` of the mixed-`mu` per-edge root form.
Output: `ALL CHECKS PASS`. The §2.2 `8/3 -> 2/3` step and the `D_g=-1`
identity were checked by hand only.

**Failed attempts (disclosed because they shaped conclusions).** (1) I
first tried to price the q-only orbit *inside* `T_a` via St 7.3: the
e-child flag has `deg p = 0`, frozen `d>0`, hence formally "nearrow", and a
mass argument seemed to force a third pole vertex (`td>=9`). Both steps
collapse on the object-level reading: `T_a` (and thresholds, punctures, cv
flags, `T_{a,pole}` mass) attaches to fibre-relevant rays only, and no
fibre branch enters the e-subtree. The surviving, weaker mechanism is
ambient (`RES-AV`). This failure is why card 1b is phrased target-side.
(2) An earlier draft of §2.2's sub-1 example used `(a,b,nu)=(1,2,2)` with
`w'=1/2`; its `kappa-bar` integrality fails (`17/4`), so it was replaced by
the `8/3 -> 2/3` example, itself still `PROVISIONAL`.

**Hidden assumptions in my new material.** St 9.1's identity
`kappa-bar = D + D_g` applied at the merge vertex (cited from
SHEET6-2POLE §2a/DEPTH §1; printed domain to be verified); M-PAT tier for
the merged local model; `a`-generic uniformity of the residue-A
configuration (unproved; needed only by RES-AV's moving-`b` kill);
Jelonek's `A(F)`-curve theorem (to be pinned in primary text); the
bilateral card inherits the single-pole closure's sanctioned hypothesis
perimeter; the §10 composition consumes only promoted statements but is
itself unreviewed.

**Contamination.** None. No `xmodel/ideation-20260828T1707Z-*` file other
than the packet was read or listed. Background: my persistent auto-memory
index (prior JC2 review sessions) was present in context; it contains no
peer 1707Z content and nothing from it was used as evidence.

**Scope.** This is a strategy submission. It promotes nothing, edits no
canonical file, launches no compute, and asserts no theorem. Conjectures:
RES-AV soundness and both card-1 outcomes; the §2.2 transfer law; the
bilateral pin. Promoted facts consumed are exactly the packet's §2 news
plus the promoted sheets/audit entries cited inline. Failed approaches and
their reasons are recorded above so the campaign does not pay for them
twice.
