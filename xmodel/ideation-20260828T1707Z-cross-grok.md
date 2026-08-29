# Hostile cross-pollination — Grok — `20260828T1707Z`

Lane: Grok 4.6 (xAI), equal-standing **hostile falsifier**.  
Packet: `xmodel/ideation-20260828T1707Z-cross-packet.md`  
SHA-256 `9cc1d824e35abbd9f367f59cc94bfde2f6c93f37a099ee48238211b6bbbec8e9` — verified before any other file was used as evidence.  
This is not a proof or counterexample of JC2. A model verdict is not mathematical evidence.

---

## 0. Custody, firewall, execution

All five frozen-corpus hashes and both overlay-A/B hash blocks matched before the corresponding files were read. Overlay-C campaign hashes matched locally:

```text
dd460760df7370aba220bacdb5025c192fbb387b6dba76af72799acf16b30f26
  cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_charts_r1_20260828/RESULT.md
71cd2bcd0a0a53460c21ff3e032f699dcf5b36c3219df20ac41b7cf0c9012e83
  cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_charts_r1_20260828/CUSTODY.md
1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787
  clean terminal archive (CUSTODY.md)
33e20a4d5f8e3646d66b7ac2f646924fcfc84a2b3f3a014785a8eb3cb3d84815
  failed Q1P03 complement archive (literal REDUCER_PLACEHOLDER)
```

`jc2-lean` was not entered, listed, searched, read, built, modified, status-checked, or controlled. Canonical ledgers and all four peer reports were not modified. No AWS job was touched. No Singular, msolve, Sage, Lean, or heavy local algebra was run. The only write is this file.

Allowed checks: SHA-256; one standard-library `fractions.Fraction` script (MFE budget, `W(2)`, `W(8/3)`, `(R1)`/`(R3)`, ratio norm). Additional non-`jc2-lean` sources were read only to audit named dependencies (`L1a(b)`/`MP5`, St 9.1 domain, GGV result/custody, Prop 4.2 for `h_1`).

---

## Executive hostile verdict

Shared assumptions do not close `td=6`.

- Literal MFE on residue A is `2 <= 3`. **NO HIT.** Slack 1. A unit charge of the q-only orbit still yields `3<=3`. Every `T_a`-supported refinement is structurally blind to that orbit (Statement 3.18: `F*b` does not exist at a non-root of `p_F`).
- Overlay A’s **edgewise** mixed-root identities are GREEN and are the only root statement that survives mixed `μ`. The stronger whole-sector two-pole `td=6` closure (`ROOT-W2` / Fable §10 / this lane’s own prior on-axis mixed-`μ` emptiness) is **not** a theorem as written.
- `A47.1` is an elementary identity and survives. `A47-BUDGET` and the claimed Def-3.3 injectivity transfer do **not**. `RES-AV` as written is a Statement-9.1 domain error.
- GGV completeness is **not** licensed. Only `ENDPOINT_DEAD_ONLY_ON_D(Delta)` is. Complements remain `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`. The adapter failure is not mathematics.

Residue A is still the unique interior two-pole `td=6` necessary-condition exhibit. It is not a Puiseux forest and not a polynomial Keller map.

---

## 1. `ROOT-W2` audit — **REPAIR**

### 1.1 Claim as written (Opus §3.2)

> In the two-pole `td=6` configuration there is no root merge, for any multiplicities `μ`.

Proof skeleton: `L1a(b)` ⇒ every vertex strictly above the meet is `M=1`, single simple `ν`-orbit ⇒ `DS2`/`DS3` ⇒ `W={2}` ⇒ parent `w_G=2` ⇒ `(R2)` ⇒ `w_G<1`. Contradiction, with no `μ` hypothesis.

### 1.2 Line-by-line

| step | status | attack |
|---|---|---|
| Type pin `Λ=3+3` ⇒ `(α,β)=(2,3)`, unique table-(23) `Λ=3` row = row 1, `b=1`, `w_0=2` | **holds** | `SHEET6-2POLE` §2a; MP4. Off-axis `b≥2` cannot occur in this sector. |
| `(R1)`/`(R2)`: every genuine contact-zero root edge has `X_R=μ_e(1-w_e)`, hence `0<w_e<1`, **any** `μ_e` | **holds** | Overlay A, GREEN. Includes mixed and all-`μ≥2` edges. Do **not** extend `w=l/(r+l)` past all-`μ=1`. |
| All-`μ=1` top-cancellation `w=l/(r+l)∈(0,1)` vs `W={2}` | **holds**, already promoted | DEPTH root-scope repair; MP9 root paragraph. This kills the all-`M=1` layer only. |
| `DS2`/`DS3` on `M=1` segments: `W(2)={2}` | **holds** | Rechecked: no `Δ≥3` divides `2`. `DS2` is case-II chain arithmetic; it is **not** the root edge (case I). |
| Zero-length: pole is the parent, `w=2` | **holds** | Covered by `(R2)` directly. |
| Negative control `(a,α,β,ν)=(2,2,3,3)`, `w_0=8/3`, `W∋{2/3,4/3,8/3}` | **holds** | Rechecked. Lives at `Λ=4`, not in this sector. |
| **`L1a(b)` covers `G_m=(0,y)`** | **fails as cited** | Weakest dependency. See §1.3. |
| `L1a(c)` at the root (third-pole ⇒ `k=0`, three shapes) | **fails at `(0,y)`** | Third-pole counting at an interior merge is not Prop 6.8 at the root: extra `p`-roots at `(0,y)` are incoming chains, not a third pole of a disjoint subtree. Use MP1+MP6(a) if `μ_e=1` is already known; overlay A **forbids** inferring `A=Σμ`, `B=r+l`, `k=0` for all-`μ≥2`. |
| `ROOT-REACH` 41/57 excluded | **not a theorem** | Over-approximation (omits `n_e ≡ -κ̄ (mod ν)`). `EXCLUDED` is one-sided; `not excluded` is not a construction. Off-axis and post-jump `M≥2` are outside `DS2`/`DS3`. |

### 1.3 Exact weakest dependency

`L1a` is stated for an **interior** two-pole `(3,3)` merge (`SHEET6-L1` §0: “chains merge at an interior `G_m` in `V_{2,a}`”). Clause (b) is induction on vertices **strictly above** that interior meet. `SHEET6-L1` itself says root merges are **not** killed by that argument.

The repair path is **not** “`L1a(b)` at `(0,y)`”. It is:

1. MP4: both poles are row 1, `M=1`, `w_0=2`.
2. MP1: `m=2` has at most one merge. A genuine root meet means that unique merge **is** `(0,y)`, so every vertex except the root is strictly pre-merge.
3. MP5 / D5: induction on `K=H°` **still pre-merge** (nonroot). Statement 8.2, repaired Prop 6.7–6.8, and the same-branch pole manufacture run at those `K`, not at `(0,y)`. Prop 8.3(iii) and Statement 8.5’s root exemptions are not used.
4. Statement 8.4 at the root arrival: `μ_e | M_{H_e}=1`, so `μ_e=1`.
5. `DS3`: the parent alphabet is `W={2}`.
6. Overlay A: `w_e<1`. Contradiction.

Step 3 is the remaining narrow gate: D5(c) at the **last** pre-merge vertex (the parent of `(0,y)`). A second `p`-root at that parent is a different tree direction from the unique down-edge to the root; Prop 6.8 still manufactures a pole on that branch and makes the parent a merge, contradicting “strictly pre-merge” plus MP1. This does **not** invoke `(0,y)` special status. It is a composition, not the written `ROOT-W2` proof.

`w=2` already kills mixed `μ` at that parent (`X_R=-μ_e<0`). Mixed-`μ` is not an extra door **if** the parent carries the row-1 alphabet. That “if” is exactly the overlay-A audit target.

### 1.4 Disposition

**`REPAIR`.** Do not `PROMOTE` Opus’s writeup, Fable §10, or this lane’s prior on-axis mixed-`μ` emptiness as a whole-sector theorem.

Repaired statement, still unreviewed as a composition:

> In the two-pole `td=6` sector, every genuine contact-zero root meet receives two row-1 `M=1` parents with `W={2}`, by MP4+MP1+MP5(D5 at nonroot `K`)+St 8.4; overlay A then excludes the meet for every `μ`.

`REJECT` any claim that mixed-`μ` / off-axis / SF1 / `m≥3` / `td≠6` root completeness is closed. Overlay A’s census (all-`b=1` through `td=12`) is diagnostic; off-axis/mixed completeness remains open at that scope. Cancel only the `m=2` `td=6` root recensus **after** a different-model check of D5 at the last pre-merge parent.

---

## 2. Residue-A extra-charge proposals — visibility test

MFE composition (all four peers, overlay B): poles `0+0`, merge `0`, suffix `2`, `ψ=2`, cap `3`. **NO HIT.** Overlay B is exact: for the `R3` terminal the witness weight is only known to be 2 or 3; for `R4` it is exactly 2. The q-only resonant orbit is not a p-root, not a tree direction, not a cv witness. No factor 6 or 7 is licensed. Ordinary `T_a`-supported `λ` refinements cannot price it.

Geometric test used below: a proposal **sees** the orbit if it produces, from promoted statements, an actual object (flag, branch, module generator, or ramification component) supported on `Res(G_m)=roots(q)\roots(p)` and distinct from the suffix witness. Renaming “the extra factor of `deg q`” fails.

| proposal | sees `Res(G_m)`? | verdict |
|---|---|---|
| Simultaneous coefficient / parent H1 match | No. Operates on edge equations and the rigid ratio `a1/a2=2±√3`. | **Keep as cheapest discriminator.** Incompatibility kills the cell; compatibility seeds algebraization. Does not charge the orbit. |
| `MERGE-DIFFERENT` (Sol) | No. Conjectural length of a local different at a `V2` merge, plus an unproved injection into actual flags. | **Conjecture.** Stop if the length is Euler/conductor under new names, or if global finiteness of `C[x,y]` over `C[f,g]` is assumed. Even a proved length-1 extra is only `3<=3`. |
| `RES-AV` (Fable) | **No.** | **`REJECT` as stated.** St 9.1 is a **pole** identity: `κ̄=D+D_g` at pole vertices (`SHEET6-CAMPAIGN`, `SHEET6-2POLE` §2a). Applying it at the merge `Q=(6,12,3,2,5)` to get `D_g=5-6=-1` is a domain error. Independently: Jelonek `dim A(F)=1` applies to a polynomial map, not to a Q-exhibit; `a`-generic uniformity is unproved; `D_g=-1` even if it were legal would still be a simple pole of `g` (`g→∞`), not `(a,b)∈A(F)`. The word “plausibly” in Fable §5 is the tell. |
| `Q-GHOST` (this lane, blind round) | No. Translated-pair hope via Prop 5.1. | **Conjecture, not a charge.** Card C of the blind report already admitted +1 may not kill. Retain only as a named client of Prop 5.1 **after** a rigid germ exists. |
| `A47-BUDGET` (Opus) | Identity yes; budget no. | Identity **survives** (§3). Budget **`REJECT` until the transfer is proved.** Unique-attachment (Def 3.3 / MFE) is for flags that exist in `T_a^*`. `Res(F)` directions have no `F*b` (St 3.18). Citing the MFE attachment lemma “verbatim” on non-flags is the `(22)` failure mode. Opus Card 2 already names this stop. |
| Coefficient-complete seed-to-jet (Sol/Opus `RIGID-TRANSPORT`) | No. One level below patterns. | **Keep as the disproof endgame**, gated on H1 compatibility. Not a geometric sighting of the orbit. |
| Parent-swap / inversion (Sol missed insight) | No. | **Cheap test, not a theorem.** `(2+√3)(2-√3)=1` is true. The poles are labelled by distinct `c_i`; unordered-merge-over-`Q` is an extra hypothesis. Run it inside the H1 matcher as a check, never as an assumed equality. |

**Combine.** The only sound combination is sequential, not additive: H1 match (kill or pin) → if pinned, `RIGID-TRANSPORT` / jet lift **and** a separately proved off-`T_a` object (`A47` branch count or a genuine translated threshold). Do not sum conjectural +1’s against slack 1. Do not spend a round squeezing MFE.

---

## 3. `A47` identity — survives; first missing implication

### 3.1 The identity is elementary and correct

Prop 4.2: `h_0=g`, `h_{j+1}=h_j^{k_j}-s_j f^{l_j}`. At type `(α,β)` the first step is `h_1=g^α-s_0 f^β`. With `J(f,g)=1` and `J(f,f)=0`,

```text
J(f,h_1) = α g^{α-1} J(f,g) - s_0 β f^{β-1} J(f,f) = α g^{α-1}.     (A47.1)
J(h_1,g) = -s_0 β f^{β-1}.                                          (A47.2)
```

For `(2,3)`: `J(f,h_1)=2g`, `J(h_1,g)=-3 s_0 f^2`. Bilinear Jacobian; no Sigray lemma required. `SHEET6-L1` §7.2(i) already named the missing `h_1`-branch budget; it did not record `(A47.1)`.

### 3.2 What the identity does **not** imply

- `(f,h_1)` is not a Keller pair (`J=2g` is not a nonzero constant). Sigray hypotheses do not transport.
- Field degree `[C(f,g):C(f,h_1)]=2` does not license a Sigray tree of `(f,h_1)` with `td=12`.
- Ramification of `(f,h_1)` supported on `{g=0}` does not enumerate branches of `h_1` at `Res(G_m)`.
- `N_∞(h)` is not a function of the pinned `Q`-data.

### 3.3 First exact missing implication (the packet’s item 3)

```text
(A47.1)  =/=>  A47-BUDGET.
```

The first missing implication is:

> Each resonant `ν_F`-orbit `b ∈ Res(F)` determines a unique branch of `h_1` at infinity in the fibre-`a` sector, the assignment is injective on `{(F,b): b∈Res(F)}`, and those branches are disjoint from the branches of `h_1` already accounted for by actual `p_F`-roots / pole punctures.

Until that implication exists, `A47` is an identity plus a slogan. Computing `N_∞` without it is not a budget.

---

## 4. Fastest complete GGV route — hybrid; completeness **REJECT**

### 4.1 What is licensed

Overlay C, RESULT `dd460760…`: six rank-2 charts, 95 pivots replayed, bordered identities and lifts NF-zero, all endpoint coefficients vanish, every `I+(Delta)` proper. Classification: `ENDPOINT_DEAD_ONLY_ON_D(Delta)`. Complements: `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`. Strict banner: `ROOT_CHARTS_COMPLETE_COMPLEMENTS_COMPONENTWISE`. Not a stratum, radical, reduced-scheme, existence, or nonexistence verdict.

Failed complement pilot `33e20a4d…`: `REDUCER_PLACEHOLDER` survived generation; Singular rc0 with parser diagnostics; 95-pivot marker correctly rejected the run. **Not evidence about the mathematics.**

### 4.2 Attack on the four designs

- **Unstructured per-chart complement chains** (live R2, unrepaired): honest remaining object, but no termination invariant other than “hope the remainder becomes `(1)`”. Combinatorial split on generating sets of minors.
- **Minor atlas** (Grok blind): worst combinatorics (`C(106,k)`-scale). Reject as the primary compute.
- **Level-wise Fitting closed sets** (Fable): correct termination invariant (rank drops, ≤9 levels from `9/104`). Computing all size-`r` minors of a `106×105` matrix over the quotient is a Groebner-class job the chart method was invented to avoid. Do not launch from scratch.
- **Fitting syzygy / module presentation** (Opus, Sol): canonical, no complements. Over a non-regular quotient, “localized syzygy = kernel on the constant-rank stratum” needs reducedness or locally free cokernel (Opus §6.4). Unverified. A full syzygy of `coker M` is not the fastest next hour.

### 4.3 Decision: hybrid

Keep the **mutation-gated complement recursion** as the compute (it is already built; Q1P03 is the pilot; substitution-only repair is the live adapter). Impose **Fitting rank-drop** as the cover invariant: a child is `V(Fitt_r)`, not an arbitrary extra minor. A module presentation of `coker M` is the **verification object** after a node passes, not the first AWS job.

Do not saturate/radicalize first. Do not primitive-clear cofactors. Do not treat dense-open death as a branch kill.

### 4.4 Fail-closed proof-object contract (all mandatory)

**G0** frozen hashes: RESULT `dd460760…`, CUSTODY `71cd2bcd…`, archive `1fe30b1c…`; successor consumes only those six exact `I+(Delta)` bases.  
**G1** pinned ambient `std(J)`; NF after every matrix entry, elimination, and kernel coordinate; `q2 mod (q2)=0` negative control.  
**G2** 95-pivot marker present; no `REDUCER_PLACEHOLDER` / `TODO`; injected-placeholder mutation must reject **before** Singular starts.  
**G3** rank witness: nonzero-NF minor plus exhaustive next-size vanishing at the claimed rank.  
**G4** adjugate right kernel: `NF(M·k_j)=0`; all 11 residual rows and 106 original rows replay.  
**G5** complete pullback of `E=x14*x72+x1*x97`, including cross terms, after `Delta^2` clearing; planted `E+1` must be nonzero-NF (a `PASS` on the plant is a job failure).  
**G6** `I+(Delta)` properness certificate, or unit-saturation “empty/nilpotent chart” skip with the saturation explicit.  
**G7** complement tagged `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED` until its own node closes; remainder unit before any whole-stratum banner; zero swap.

### 4.5 AWS fanout trigger

**No fanout until one full exact Q1P03 node passes G0–G7.** That is already the live policy; it is correct. After that pass: the other five branches in parallel, one 16-vCPU/128-GiB zero-swap worker each. Split a branch only on a mathematically distinct Fitting jump. Cap 12 workers before review. Campaign caps unchanged (512 vCPU, ≤1 TiB, zero swap required). Fail closed on adapter/parser/swap/NF mismatch; do not reuse `33e20a4d…`.

---

## 5. At most three new connections (peers × overlays only)

1. **Overlay-A edgewise `w_e<1` × MP5 at nonroot parents × unique `Λ=3` row.** This is the actual content of `ROOT-W2`. It is not a new identity. The mixed-`μ` door in two-pole `td=6` is not a different anatomy; it is the question whether a row-1 `M=1`, `W={2}` parent reaches the root. Overlay A already named that audit; the peers stated the conclusion without recording the nonroot-only scope of `L1a(b)`/`MP5`.

2. **St 9.1 pole-only × every extra-charge proposal.** Fable’s `D_g=-1` is the sharpest false sighting: a pole formula evaluated at a merge. The same mistake, in milder form, is treating Def 3.3 attachment, Prop 5.1 punctures, or MFE witnesses as if they could see `Res(G_m)`. Overlay B plus St 3.18 already say they cannot. The only new exact object off `T_a` is `(A47.1)`.

3. **Overlay-C complement recursion × Fitting termination invariant.** Completeness claims from any peer (Fable’s “finite complete verdict”, Opus’s “no complements”, Sol’s six-way atlas) overstate what `dd460760…` licenses. The adapter failure does not choose the architecture. The hybrid of §4 is the connection: live compute plus Fitting as the cover bound, fanout gated on one exact node.

VDB-K remains `NO HIT` (no Sigray-to-SNC translation lemma). Bilateral fibration pinning inherits the single-pole closure’s hypothesis perimeter and is not a new theorem.

---

## 6. Ranked 6-hour queue

Proof / disproof split: **4 h proof, 2 h disproof**, same H1 object in both columns. Do **not** spend any of the six hours on MFE `+1`, L3, `RES-AV`, mixed-`μ` AWS recensus for `m=2`, a from-scratch Fitting syzygy, or generic HENS-CT.

| # | hours | task | split | stop rule |
|--:|---|---|---|---|
| 1 | 0–1 | One-page repaired `ROOT-W2`: D5 at the last pre-merge parent of `(0,y)`, St 8.4 at arrival, overlay A. Different-model hostile on that paragraph only. | proof | Stop and **`REJECT` the whole-sector claim** if Prop 6.8’s same-branch pole needs `(0,y)` or a nonroot-only hypothesis that the parent fails. Keep the edgewise theorem regardless. |
| 2 | 1–4 | Two-parent H1 / `RIGID-TRANSPORT` of residue A over `Q(√3)`: both case-II parent equations plus Prop 8.1(iv) at `(r,ν,l)=(2,3,1)`, ratio `r^2-4r+1=0`. Include parent-swap action as a **check**, not a symmetry. | 2 h proof / 2 h disproof | Stop if the matcher uses M-PAT beyond the exhibit’s two-orbit searrow rule, transports `κ` across fibres, or cannot replay `(6,10)` and `z^2-4z+1` by substitution. Incompatibility: cell dies (proof). Compatibility: pin the germ and **do not claim `td=6` excluded**. |
| 3 | 4–5 | Record `(A47.1)` as an identity. Attempt the §3.3 implication at `G_m` only: does any promoted statement produce **one** `h_1`-branch through the extra `q`-root? | proof | Stop at the first count of a non-flag. Do not emit `A47-BUDGET`. |
| 4 | 5–6 | GGV: **do not compute locally.** Confirm Q1P03 mutation-gated successor is the only live AWS node; no fanout. If H1 returned compatible, write the two-scale jet-lift spec (Avenue 4 client) as the disproof carry. | monitor / disproof spec | Stop the GGV lane on placeholder, swap, NF mismatch, or any banner stronger than `ENDPOINT_DEAD_ONLY_ON_D(Delta)` without a unit remainder. |

K00 / full-`P6` stays **protected on separate capacity**, not inside this six-hour critical path. External sweep remains due `2026-08-29 05:24Z`.

If item 1 `REJECT`s the whole-sector claim, the `td=6` two-pole root menu reopens only as “all-`M=1` dead; mixed-`μ` still needs D5 at the parent”; do not relaunch an `m=2` engine census.

---

## 7. Epistemic ledger

### Promoted facts (quoted at scope)

- Overlay A, GREEN: every genuine contact-zero searrow parent edge satisfies `X_R=μ_e(1-w_e)=A/B`, `w_e=1-A/(μ_e B)`, `0<w_e<1`. If some `μ_e=1`, repaired MP6 root anatomy applies. For all-`μ≥2`, do not infer `A=Σμ`, `B=r+l`, `k=0`, no northeast roots, or `B>A`.
- All-`μ=1` root layer at `td=6,m=2` empty via `W={2}` (DEPTH / MP9). Root `M=1` remains legal.
- MFE inequality GREEN at selected-exit/shared-inequality scope after the pole-endpoint truncation repair. Inequality only; no `(22)`, `(22-cl)`, fixed `κ`, equality/slack, MP8 no-refinement, root census, or `td=6` exclusion.
- Residue A Q-records, suffix cost 2, `ψ=2`: necessary-condition exhibit, not a realizable forest.
- GGV: `ENDPOINT_DEAD_ONLY_ON_D(Delta)` on six charts; complements open.
- `(A47.1)`/`(A47.2)`: elementary identities, this report.

### Provisional / repaired

- Repaired `ROOT-W2` composition of §1.4: high-confidence, **not** promoted. Weakest remaining sentence is D5 at the last pre-merge parent.
- `ROOT-REACH` as a one-sided on-axis `M=1` filter.
- H1 / `RIGID-TRANSPORT` outcomes.
- Live GGV complement-recursion adapter (substitution-only, mutation-gated).

### Conjectures (not theorems)

`MERGE-DIFFERENT`; `Q-GHOST`; VDB-K translation; post-jump `M≥2` `w`-law; mixed-`μ` formula `X_root=μ_tot/(r+l+e_0)` (Opus sketch); inversion-symmetry kill; bilateral fibration pin; `A47-BUDGET`.

### Failed / rejected this round

- MFE kill of residue A; any `T_a` price of the q-only orbit; unit merge charge as a kill (`3<=3`).
- `ROOT-W2` as written; `L1a(b)` at `(0,y)`; `L1a(c)` third-pole at the root; whole-sector mixed-`μ`/off-axis completeness; `ROOT-REACH` as a census replacement.
- `RES-AV` as stated (St 9.1 domain error; Jelonek on a non-map).
- `A47-BUDGET` injectivity transfer from Def 3.3.
- GGV completeness, dense-open death as a branch kill, adapter failure as mathematics.
- Printed `(22)`, literal `δ_a`, `(22-cl)`, cross-fibre `κ`, MP8 no-refinement, l-free phase-3 root census, case-IV labelling of genuine root merges.

### Hidden assumptions explicitly rejected

- `w=l/(r+l)` beyond all-`μ=1`.
- Q-exhibit realizability, Puiseux algebraization, global finiteness, landing, `RPMC(C)`, cofinal `td` ceiling.
- `G2-PSC` merged with `G2-BD`.
- A q-only factor is a selected exit, cv flag, or `A(F)` point.

### Checks run

- Packet and all frozen/overlay hashes in §0: match.
- Overlay-C RESULT/CUSTODY/archive and failed complement archive: match.
- `python3` `fractions.Fraction`: MFE `2<=3`; `W(2)={2}`; `W(8/3)={2/3,4/3,8/3}`; `(R1)` at `w=2` gives `X=-μ`; `(R3)` is a special case of `(R2)` on four `(r,l)` pairs; `(2+√3)(2-√3)=1`.
- Hand: `(A47.1)` bilinearity; St 9.1 pole-only vs merge `D=6`, `κ̄=5`.

No mathematical command failed. `shasum` emitted a locale fallback warning.

### Contamination and scope

Peers were **deliberately unblinded** by the packet. Prior independent `1707Z` grok report was not reread as evidence; its Q-GHOST and on-axis mixed-`μ` claims are attacked above. No other `1707Z` cross-output was read. `jc2-lean` untouched. Scope: adversarial synthesis of the seven charged items at freeze `2026-08-28T17:35Z`. Not a 46-avenue survey.

### Files read (dependency-gated beyond the packet-mandated set)

Packet-mandated: this packet; the four unblinded reports; overlay A; overlay B’s four primary reports (coordinator integration, Sol MFE producer, GPT-56 repair, Fable hostile).  
Dependency-gated: `ladder/SHEET6-L1.md` §§0–3,7–8; `ladder/SHEET6-A3L1-REVIEW.md` Front 4; `ladder/SHEET6-MULTIPOLE.md` MP1/MP5–MP9 and D5–D9; `ladder/SHEET6-DEPTH.md` DS2–DS3 and root-scope repair; `ladder/SHEET6-2POLE.md` supersession and §2a; `ladder/SHEET6-CAMPAIGN.md` St 9.1 sentence; GGV `RESULT.md`/`CUSTODY.md`/`PREREGISTRATION.md` (complements R2); Prop 4.2 repair for `h_1`.  
Not entered: `jc2-lean`. Not written except this file.

### Model

Grok 4.6, xAI. Hostile falsifier under the cross-packet. Retain only what survived the attacks above.
