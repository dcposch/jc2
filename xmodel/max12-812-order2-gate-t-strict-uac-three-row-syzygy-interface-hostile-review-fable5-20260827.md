# Hostile review: direct three-row strict unique-`AC` certificate (Sol lane)

Date: 2026-08-27
Reviewer: Fable 5 (Anthropic), adversarial exact-algebra / Faber-support desk review.
Independence: every identity, wall, and row extraction below was re-derived or
re-executed in this session with code written here.  Neither the producer's Sol
lane nor Opus5's direct-coordinate simplification was accepted as authority;
the confirmed uniform source-transport review (`…naturality-interface-hostile-
review-fable5-20260827.md`) was consumed only for the seven-formula scope of
(1.1)-total and the frozen-tail conventions, not for any purity claim.

## 0. Candidates and overall verdict

Hashes recomputed byte-exact in this session, both matching the prompt pins:

```text
2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md
56edb06f57c657534b46f1c406363de7821e240ccc1eb7d8529be7eeb2c5c3f4
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-replay-20260827.py
```

Also re-verified on disk: miner `0e94e540…/mine_support.py` (pin matches; the
replay hash-checks it before import, and `enumerate_primitives` is pure —
`require_aws` fires only in `main()`, so the import path is sound); canonical
`tails.json` byte hash `d72f774c…` with census `36+54+58+81+89+120+131=569`;
upstream `1cfa10b4…` (uniform sol) and `23007a2b…` (Opus5 a2d2 composition
review) unaltered.

| # | Mandated attack | Verdict |
|---|---|---|
| 1 | Re-expand (1.2); radical conclusion on `D(rho) ∩ (D(A0c) ∪ D(A1))`; set vs ideal; inverted factors | **PASS** — all four identities exact; radical claim proved; hypotheses sharp (§1) |
| 2 | Independent polar derivation of `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]`; simple-pole cancellation; hidden survivors | **PASS**, one **REPAIR** wording item (§2) |
| 3 | Twelve baselines + exact-`r` sub-tails; every boundary (`E`, `RA^2`, `A^3`, `a=7` tie, `k2`, targets); `(2,5,r)` split | **PASS** — classification exact at row level, all boundaries confirmed (§3) |
| 4 | Literal-row direction, source-to-total transport, replaceable vs corroborated imports | **PASS**, two **REPAIR** precision items (§4) |
| 5 | Replay audit | **REPAIR** — genuine but with a vacuous-pass hole and four smaller gaps (§5) |
| 6 | Minimal linker/schema delta | delivered (§6) |

**Overall: PASS (CONFIRMED) as scoped by the producer's own status line** — a
proved core lemma plus a mechanically derived low-band classification, which
replaces nothing until a frozen row-level linker and its independent review
exist.  Every repair below is wording, replay hardening, or schema content;
none is a mathematical error.  The strongest exact theorem, the exact contact
list, and the smallest failing identity/hypothesis are in §7.

## 1. Attack 1 — the four identities and the radical conclusion: PASS

### 1.1 Re-expansion

By hand and with an independent dense five-variable exact-`Fraction` engine
(unrelated to the replay's sparse engine), with
`g1=(3/8)(A0c*C1+A1*C0c)`, `g2=(3/8)(A0c*C0c+rho^2*A1*C1)`,
`g4=(3/32)(C0c^2+rho^2*C1^2)`, `D=rho^2*C1^2-C0c^2`:

```text
C1*g2 - C0c*g1            = (3/8)*A1*(rho^2*C1^2 - C0c^2)   =  (3/8)*A1*D   EXACT
C0c*g2 - rho^2*C1*g1      = (3/8)*A0c*(C0c^2 - rho^2*C1^2)  = -(3/8)*A0c*D  EXACT
(32/3)*g4 + D             = 2*rho^2*C1^2                                    EXACT
(32/3)*g4 - D             = 2*C0c^2                                         EXACT
```

All four hold identically; the middle expansions above show every
cross-term cancellation explicitly.  Four explicit membership witnesses were
verified term-exact over `Q`:

```text
2*A1*rho^2*C1^2  = (8/3)*(C1*g2 - C0c*g1)            + (32/3)*A1*g4
2*A1*C0c^2       = -(8/3)*(C1*g2 - C0c*g1)           + (32/3)*A1*g4
2*A0c*rho^2*C1^2 = -(8/3)*(C0c*g2 - rho^2*C1*g1)     + (32/3)*A0c*g4
2*A0c*C0c^2      = (8/3)*(C0c*g2 - rho^2*C1*g1)      + (32/3)*A0c*g4
```

Hence `C0c^2` and `rho^2*C1^2` lie in `I=(g1,g2,g4)` after inverting `A0c`
alone (or `A1` alone); inverting `rho` in addition gives `C1^2 in I`, so (1.3)
holds exactly as stated.  Two sharpenings the note may keep or add:

- **Nullstellensatz-free point form.**  The set-theoretic conclusion needs no
  algebraic closure: at any `K`-point of any field `K` with `6` invertible,
  `g1=g2=g4=0`, `rho != 0`, and (`A0c != 0` or `A1 != 0`) force
  `C0c=C1=0` directly from the displayed witnesses.  So the arcwise use is
  licensed over the actual residue fields, not just geometrically.
- **Inverted factors, complete list.**  The identities (1.2) live over
  `Z[1/2,1/3]`; the localization inverts exactly `rho` and one of
  `A0c`/`A1`; nothing else — no `k`, no `J`, no leading-`C` coefficient, no
  `theta`/`eta`, no Hensel `lambda`.  "Characteristic zero" is safe but
  stronger than needed (`char != 2,3` suffices), which also licenses the
  odd-prime replay lanes; worth one schema line.

### 1.2 Set-theoretic vs ideal/unit, and sharpness

The candidate's own firewall sentence ("set-theoretic/radical … does not
assert a scheme-theoretic unit ideal before localization or radical") is
correct and required: `I` itself is not unit and not radical-trivial without
the localizations.  Both hypotheses are sharp.  Countermodel executed:
`(A1,A0c,C1,C0c,rho)=(5,0,7,0,0)` gives `g1=g2=g4=0` with `C1=7 != 0` — the
conclusion genuinely fails at `rho=0` when only `A1` is nonzero.  (At `rho=0`
with `A0c != 0` the conclusion happens to survive; the lemma correctly does
not claim that fringe, and the campaign never uses it.)  Dropping
`(A0c,A1) != (0,0)` also kills the lemma (`C0c=±i*rho*C1` solves `g4=0`
alone over a closure).  The candidate's "only `rho != 0` and
`(A0c,A1) != (0,0)` are load-bearing" survives attack: no root allocation,
Hensel series, deck split, `k10`/`J` unit, or leading-`C` inversion enters,
which I confirm against my own row builds below (no such quantity occurs in
any extracted coefficient).

## 2. Attack 2 — what literally sits in `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]`: PASS, one repair

### 2.1 Independent construction

I rebuilt all seven literal rows from scratch: the seven formulas (1.1)-total
of the uniform sol (F6=2P … F0=Rtot^2+sigma^2*N0), the 569 frozen tails
(byte hash verified before use), the three delayed load series
(`sigma^4/12/20`), and the target subtraction `-sigma^{2(12+ell)}*(0,mu2,0,
mu4,0,mu6,J/4)`, on the exact contact ideal (1.2) with all higher jets
symbolic and `p0=-2*rho^2`, `rho` symbolic.  Scalar arithmetic over
`F_p`, `p=2^61-1` (every frozen tail coefficient and every extracted
coefficient in these windows has numerator far below `p`, so a zero/equality
verdict is exact); the pipeline was anchored by reproducing, symbolically and
term-for-term, **all** of Opus5's independently published `(2,4,3)` facts:
rows identically zero at grades 0–15, `[sigma^16]Phi1 = g1`,
`[sigma^16]Phi2 = g2`, `[sigma^16]Phi4=[sigma^17]Phi4=0`,
`[sigma^18]Phi4 = g4`, and the grade-16 deflation
(rows 3,5,7 = `-(p/4), -(p^2/32), -(p^3/128)` times row 1; rows 4,6 zero).

### 2.2 Which families contribute — verified row-level law

Across every cell and probe executed (21 distinct cells — 16 positive, 5
negative — twelve of them symbolic, all numeric at two seeds; 9 tagged family
probes; full list in §3):

- **Rows 1 and 2 receive pole-one content only**, each family first at its
  polar grade (`AC` at `10+a+c`, `k10RC` at `11+r+c`, `k10A^2` at `14+2a`,
  `k10R^3` at `10+3r`, `k6C` at `17+c`, `k2R` at `22+r`), plus row 2's `mu2`
  from 28.  With condition 1 (`AC` alone at or before `G`) the two grade-`G`
  coefficients are exactly (1.1)'s `g1,g2` — verified symbolically with the
  `3/8` scalars at eight cells and numerically at all twelve baselines.
- **Row 4 (and row 6) annihilate every pole-one family identically**, loaded
  or not.  Tagged probes: `k10` at `(5,8,5)`/`(6,9,6)` (both `k10A^2` and
  `k10RC` inside the `T`-window), `k6C` inside the window at `(6,9,6)` and
  even at its tie/wall cells `(7,8,7)`, `(8,9,8)`, `k2R` at `(6,9,6)` and at
  its own tie `(9,12,9)`: in every case the tag is live in rows 1,2,3,5,7 at
  the exact predicted grade and **never** appears in row 4 within the window.
  This is the row-level content of the candidate's "moving-`P` simple-pole
  recurrence" sentence, and it held without exception.
- **Every pole-`>=2` family does reach row 4**: `C^2` at `10+2c` (the wanted
  `g4`, coefficient `3/32` verified), `RA^2` at `12+r+2a` (§3 negatives),
  `k10R^2A` at the `E` cell (`kt0`-content in `[sigma^18]Phi4`), the
  pole-three `A^3` (an `A`-degree-3 term in row 4 at 18 at `E` — reaching
  row 4, not only row 6, exactly as the `z^{-4}` reduction of a degree-3
  numerator over `L^3` predicts), and the pole-two **load** `k2A` at
  `25+a` (tag-verified in row 4 at exactly `T=34` at `(9,12,9)`).  So
  condition 2's load-agnostic "pole one except `C^2`" is exactly the right
  guard — a load-blind version would be wrong.

Hence, on any cell passing conditions 1–3, the three extracted coefficients
are literally (1.1) with `A1=az_a, A0c=ac_a, C1=ez_c, C0c=ec_c` — no hidden
higher-pole, load, target, `ell`, stage-zero, or `lambda` term survives.  The
`z`-linearity of the leading pairs is contact-independent (the model's `A`,
`C` are `z`-linear with `sigma`-series coefficients), so no parity/role swap
of `g1` vs `g2` can occur at other contacts; verified at all twelve.

**REPAIR (wording/schema).**  The sentence "Every pole-one primitive
contributes identically zero to `Phi4 = h4 + (P/2)*h2` by the exact moving-`P`
simple-pole recurrence" cites an analytic-device recurrence for which no
frozen uniform reviewed lemma exists (the `universal_hshift`/`ROW_IDENTITIES`
bridge is reviewed per chamber and per grade, not uniformly).  The candidate's
own interface already contains the correct fail-closed substitute — the
per-manifest **symbolic equality of the three extracted coefficients to
(1.1)** — which subsumes the recurrence claim for the cell at hand.  State
that the equality check, not the recurrence, is the normative gate, and label
the recurrence as motivation (here empirically confirmed at every probed
cell).  The equality duty must be symbolic over the full contact jet ring:
`g2` and `g4` carry `rho^2`-terms, so this same check rejects any relabeled
`rho=0` face bytes (which would reproduce `g1` but not `g2`, `g4`) and any
stage-zero substitution (stage-zero pairs are killed by the contact ideal, so
equality would fail against the shifted-jet row content).

## 3. Attack 3 — the twelve contacts, the sub-tails, and every wall: PASS

### 3.1 Independent re-derivation of the classification

Three mutually independent routes agree:

1. **Closed-form walls (hand).**  `RA^2` (`12+r+2a`) enters by `T_C2=10+2c`
   iff `r <= 2d-2`; `A^3` (`15+3a`) iff `a <= 2d-5` (so only `E=(1,3,·)` in
   the fan, `r`-independent); `k10R^2A` (`13+2r+a`) at baselines only at `E`;
   `k6C` ties `G` iff `a=7`, precedes iff `a>=8`; `k2R` ties `G` first at
   `(a,d)=(9,3),(10,2),(11,1)` (least tails; miner-confirmed, and `22+r <=
   10+2a+d` is the right inequality); `k2A` (`25+a`, pole 2) reaches `T_C2`
   iff `15-a-2d <= 0`; `mu2` wall `G>=28` and `mu4` wall `T_C2>=32` are
   beyond the `k6` wall for all `d<=3` (max over the twelve: `G=25`, `T=28`).
   These reproduce the twelve baselines `d=1: a=2..6; d=2: a=2..6; d=3:
   a=5,6` (with the `s_min` pattern `1` iff `a<=d`) and the sub-tail
   recoveries exactly.
2. **Independent mini-miner.**  A from-scratch reimplementation of the
   four-summand/four-atom census (my own code, no shared lines) matches the
   pinned miner's `enumerate_primitives` on **94 cells** (`a<=11`, `d<=3`,
   three `r` values each): identical family sets *and* coefficients, zero
   mismatches.  The load-bearing aggregation cancellations are real and were
   traced route-by-route: `R^2C` (`+3/4-3/4`), `R^3A` (`+3/4-3/4`), `R^4`
   (`3/8-3/4+3/8`) all vanish — without these cancellations `(2,3,2)` would
   have had a spurious pole-two `R^2C`/`R^4` at `T=16`.  The row-level checks
   below confirm no such content exists in the literal rows.
3. **Literal rows.**  All twelve baselines and all four sub-tail bases were
   built as literal rows and passed the full purity battery (all rows zero
   below `G`; row 4 zero below `T_C2`; the three coefficients equal
   `g1,g2,g4`): eight cells fully symbolically (`(2,3,2)`, `(3,4,3)`,
   `(2,4,3)`, `(3,5,3)`, `(1,3,3)`, `(2,5,5)`, `(4,7,5)`, plus the anchor),
   and all sixteen positive cells numerically at two independent seeds over
   `F_{2^61-1}` (Schwartz–Zippel, per-cell failure probability `< 2^-58`).

### 3.2 Every boundary attacked, with the exact obstruction

- **`RA^2` wall, inclusive at `T`**: symbolic negatives at `(1,3,2)`
  (`r=2d-2`, enters *at* `T=16`), `(2,5,3)` (enters at 19, row 4 nonzero
  below `T`), `(2,5,4)` and `(4,7,4)` (enter exactly at `T`), numeric at
  `(3,6,4)`.  The obstruction is exactly the symmetric root-pair form of the
  `RA^2` family; at `(1,3,2)`:

  ```text
  [sigma^16]Phi4 - g4 = -(3/4)*rho^2*cs2*az1*ac1 - (3/32)*rho^2*rs2*az1^2
                        - (3/32)*rs2*ac1^2
                      = -(3/16)*( R0(rho)*A0(rho)^2 + R0(-rho)*A0(-rho)^2 ),
  R0(z)=cs2*z+rs2/4,  A0(z)=az1*z+ac1
  ```

  and the identical shape with `(cs4,rs4,az2,ac2)` at `(2,5,4)`.  This
  **confirms** that `(2,5,r=3,4)` is not direct while `r>=5` is (the `r>=5`
  cell is symbolically pure), and quantifies the candidate's "stronger
  certificate which retains the extra `RA^2` term" option.  Note the
  refinement (true at every pole-wall negative): rows 1 and 2 at `G` remain
  exactly `g1,g2` — the failure is confined to row 4.
- **`E`**: `[sigma^16]Phi4` carries exactly `{cs2,rs2,az1,ac1,rho}` (`RA^2`),
  and `[sigma^18]Phi4 - g4` carries 25 terms including `kt0` (`k10R^2A`) and
  one `A`-degree-3 term (`A^3`); row 6 turns on at 18.  All three predicted
  wall families leave fingerprints; raising `r` to 20 leaves the
  `r`-independent `A^3` alone (miner-instrumented), so `E` is permanently
  non-direct.  Meanwhile `E`'s rows 1,2 at `G=15` are still pure `g1,g2` —
  condition 1 holds at `E`; only condition 2 fails, on three families.
- **`a=7` tie / `a>=8` load-first**: tagged `k6` probes show first arrival in
  rows 1,2 at exactly 25 (`=G`) at `(7,8,7)` and at 26 (`<G=27`) at
  `(8,9,8)`; row 4 stays `k6`-free through `T` at both.  So the `a>=7`
  failure is confined to rows 1,2 — the mirror image of the pole walls.
- **Later `k2` walls**: miner-confirmed ties at `(9,3),(10,2),(11,1)` and a
  row-level probe at `(9,12,9)`: `k2R` arrives in rows 1,2,3,5,7 at exactly
  `31=G` and pole-two `k2A` arrives **in row 4** at exactly `34=T`.
- **Target walls**: schedule re-verified in the builds (`mu2` at 28 active in
  the `(6,9,6)` window without touching `Phi4[28]`; `mu4` at 32 outside all
  twelve windows, max `T=28`).  The guard `G<28`, `T_C2<32` is the right
  inclusive-exclusive convention.

One completeness point the note leaves implicit and should state: the
sub-tail memberships are **monotone in `r`** (every family grade is
nondecreasing in `r` at fixed windows, and no family enters a window as `r`
grows), so checking the base `r` of each recovered sub-tail certifies all
larger `r`; and the recovery list `{(1,2): r>=3; (2,3),(3,3),(4,3): r>=5}` is
**complete** — the remaining non-direct cells cannot be recovered by raising
`r` (`E` via `A^3` and `a>=7` via `k6C` are `r`-independent).

## 4. Attack 4 — direction, transport, and what is replaceable: PASS, two repairs

- **No reversed map.**  The certificate is a coefficient identity plus a
  pointwise field-arithmetic contradiction on the contact locus; emptiness of
  total arcs follows through the reviewed direction only (finite-jet
  factorization under the uniform naturality (1.5)); no `Spec` map is run
  backwards.  The three extracted coefficients are the same polynomials on
  the total side and the D1 side under the shift — that is (1.5), consumed
  within its confirmed formula-level scope.
- **Analytic-only `H` rows: rejected by design.**  Condition 4 and the §4
  manifest field ("rows are analytic auxiliaries without a reviewed bridge …
  reject") match the standing licensed pattern.  My §2 repair strengthens
  this: the symbolic-equality duty is the operative bridge check.
- **Stage-zero and `rho=0` relabel rejection**: both are caught by the same
  symbolic-equality duty (§2.2); note that `g1` alone would *not* catch a
  `rho=0` relabel (it is `rho`-free) — `g2`/`g4` carry the detection.  The
  linker must therefore check all three, never a subset.  **REPAIR: state
  this explicitly in the interface.**
- **Replaceable vs corroborated.**  Today: nothing is replaced; every one of
  the twelve cells already sits under a promoted/reviewed chamber endpoint,
  so the lemma adds corroborating second proofs and no new coverage.  After
  the frozen linker + hostile review, the clean replacements are: the four
  `d=1` `a=2..5` root-allocation certificates; the `a=6` **half** of the
  `a=6,7` endpoint (the artifact itself must survive for `a=7`); the five
  `d=2` `a=2..6` endpoints (including `B22`, where Opus5's §6.4(b) instance
  already exists); and the two `d=3` `a=5,6` endpoints.  Permanently
  corroboration-only (endpoint retained for the residual locus): the
  `(1,2)` endpoint (retained for exact `r=2`), and the `B23`-type `d=3`
  `a=2,3,4` endpoints (retained for `r` = floor..4; the direct lemma covers
  only `r>=5`).  Untouched: `E`, `a=7,8,9`, the `a>=10` ceiling, `(8,3)`
  (confirmed-but-unpromoted — bind by hash, not filename), and every equality
  face.  **REPAIR: the note's replacement list is correct but should say
  explicitly that the split endpoints (`a=6,7`; `(1,2)`; `d=3` `a=2,3,4`)
  can never be retired wholesale by this lemma.**

## 5. Attack 5 — replay audit: REPAIR

What the replay genuinely does (verified by rerun, 0.04 s PASS, and by my
instrumentation): recomputes the four syzygies with its own exact sparse
engine (not transcription); hash-pins the miner before import (no
`shared_faber_probe`-style unpinned-import gap; the import executes no side
effects); mechanically recomputes the twelve-contact classification and the
four sub-tail bases from the miner rather than from a table; and its
`expected` set matches the note's §2 list.  Tuple convention is a uniform
`(a,d,r)` throughout the replay — no `(1,3,2)`-style collision inside the
code.  No stale hash: both pins match disk.

Defects, in decreasing order of importance:

1. **Vacuous-pass hole (no positive control).**  All four `checks` entries
   are built exclusively from `add`/`scale`/`mul`; I demonstrated that
   sabotaging `mul` to return `{}` makes every check empty, so
   `any(checks)` stays falsy and the syzygy section prints PASS.  A one-line
   mutation control (e.g. assert that `C1*g2 - C0c*g1 - (3/8)*A1*D` with a
   deliberately wrong sign is *nonzero*) closes it.  The same applies to the
   classification half: a sabotaged `eligible` that always returns
   `(False, …)` would fail the positive twelve but a sabotaged miner import
   returning an empty inventory would make `initial` empty and every cell
   ineligible — caught by the twelve, fine; the syzygy half has no such
   protection.
2. **Negative controls do not assert their reasons.**  I verified each fires
   for the claimed cause (E `r=20`: sole bad pole is `A^3` with coefficient
   `-1/16`; `B23` `r=3/4`: sole bad pole `RA^2`, `-3/8`, grades 19/20;
   `a=7`: `initial = {AC, k6C}` both at 25; `(1,3,2)`: three bad poles
   `RA^2@16`, `k10R^2A@18` (`-5/32`), `A^3@18`).  The replay should assert
   the reason (family signature), not bare ineligibility, or a future miner
   regression could keep the controls green for the wrong cause.
3. **No strict-cell membership predicate.**  `eligible` never checks
   `a+3s>d` / strict `AC`-minimality; I verified by hand that all sixteen
   tested tuples are in-cell, but the linker/replay should refuse out-of-fan
   tuples.
4. **`C^2` presence is assumed, not asserted.**  The lemma needs the `C^2`
   family present at `T_C2` with coefficient `3/8`; this is automatic in the
   model (single atom route, no cancellation) and row-verified here, but the
   miner's own `main()` asserts it and the replay dropped that check.
5. **Scope extension unflagged.**  The pinned miner is the reviewed `d=2,3`
   *baseline* census; the replay reuses its pure function for `d=1` and
   exact-`r` cells.  Mathematically sound (the function is
   contact-parametric; my 94-cell independent cross-check and the `d=1` row
   checks confirm it), but the manifest/schema must name the extension, and
   the replay's `pad=0` calls silently drop the miner's own `pad` sentinel
   (redundant — `count > budget//cost` already implies grade overflow — but
   that argument should be recorded once).

None of these defects invalidates a printed conclusion; every printed line of
the replay is true and was independently reproduced here.

## 6. Attack 6 — minimal reviewed linker/schema delta before replacement

The smallest delta that makes the direct lemma able to replace a
chamber-specific root allocation, beyond the candidate's own §4 list:

1. **Per-manifest symbolic equality as the normative gate** (§2 repair): the
   linker computes `[sigma^G]Phi1, [sigma^G]Phi2, [sigma^{T_C2}]Phi4` from
   the schema-normative seven formulas + pinned tails on the contact ideal,
   all jets symbolic, `rho` symbolic, and checks term-exact equality to
   (1.1) — all three, never a subset.  This one duty subsumes the pole-one
   cancellation claim, and rejects stage-zero pairs, `rho=0` face relabels,
   analytic-only `H` rows, and any inventory omission, in one check.
2. **Strict-cell predicate** in the manifest validator (§5.3).
3. **`C^2`-at-`T_C2` presence check** with coefficient `3/8` (§5.4).
4. **Inventory dual-derivation or scope-extended review**: either a second
   independent enumeration (as done here) inside the linker, or a one-time
   review note extending the miner's reviewed scope to `d=1` and exact-`r`
   calls, plus the recorded redundancy argument for `pad=0` (§5.5).
5. **`r`-monotonicity lemma** recorded once, so base-`r` sub-tail checks
   certify the whole tail (§3.2).
6. **Syzygy-engine positive control** in the frozen replay/linker (§5.1),
   and reason-asserting negative controls (§5.2).
7. **Convention and binding hygiene** (inherited): declare `(a,d,r)` vs
   `(a,c,r)` per artifact — the note itself has one unlabeled `(2,3,>=3)`
   in §3 that is `(a,d,r)` while §2 uses `(a,c,r)` for the same cell (the
   exact Opus5-documented trap; one-word fix) — and bind endpoint statuses
   to promotion-artifact hashes, never filename patterns.
8. **Field hypothesis line**: `2,3` invertible suffices for (1.2)/(1.3);
   record it so finite-field replay lanes are licensed by the schema.

With these, the twelve replacements of §4 become mechanical; without item 1
the lemma must not replace anything, exactly as the candidate itself says.

## 7. Strongest exact surviving theorem, contact list, smallest failure

**Theorem (three-row direct certificate; survives this review).**  Let `k`
be a field with `6` invertible.  In variables `A1, A0c, C1, C0c, rho` the
four syzygies (1.2) hold identically, and at any point with `rho != 0` and
`(A0c, A1) != (0,0)`, `g1=g2=g4=0` forces `C0c=C1=0`.  Consequently, for
every strict unique-`AC` contact `(a,c,r)` satisfying, over the window
`[0, T_C2=10+2c]`: (i) `AC` is the unique polar primitive at or before
`G=10+a+c`; (ii) every other primitive through `T_C2` except `C^2` has pole
one; (iii) `G<28`, `T_C2<32`; and (iv) a reviewed literal-row bridge with
term-exact equality of `[sigma^G]Phi1, [sigma^G]Phi2, [sigma^{T_C2}]Phi4`
to (1.1) under `A1=az_a, A0c=ac_a, C1=ez_c, C0c=ec_c` — the three literal row
coefficients contradict exact leading `C` given exact leading `A` on
`D(rho)`, with no root allocation, Hensel series, deck split, load unit, or
further localization.  Conditions (i)–(iii) hold, verified here at row level,
exactly at:

```text
baselines (a,c,r):  (2,3,2) (3,4,3) (4,5,4) (5,6,5) (6,7,6)      [d=1]
                    (2,4,3) (3,5,3) (4,6,4) (5,7,5) (6,8,6)      [d=2]
                    (5,8,5) (6,9,6)                              [d=3]
exact-r sub-tails:  (1,3,r>=3);  (2,5,r>=5) (3,6,r>=5) (4,7,r>=5) [monotone in r]
```

and fail at every attacked boundary: `(1,3,2)`, `(2,5,3)`, `(2,5,4)`,
`(3,6,4)`, `(4,7,4)` (the `RA^2` wall, inclusive at `T_C2`), `E=(1,4,r)`
(all `r`; `A^3` pole three plus `RA^2` and `k10R^2A` at the least tail),
`a=7` (`k6C` tie at `G`), `a>=8` (load-first), with the later `k2` and
target walls beyond.  In particular `(2,5,r=3,4)` is **not** direct and
`(2,5,r>=5)` **is** — confirmed symbolically.

**Smallest failing identity/hypothesis.**  At the lemma level: `rho != 0`
(countermodel `(5,0,7,0,0)`).  At the fan level: condition (ii) at
`(1,3,2)`, where the single family `RA^2` adds exactly
`-(3/16)*(R0(rho)*A0(rho)^2 + R0(-rho)*A0(-rho)^2)` (three terms) to
`[sigma^16]Phi4`, so `Phi4[T] != g4` while `Phi1[G]=g1`, `Phi2[G]=g2` still
hold — the minimal, boundary-inclusive failure of the pattern.

## 8. Firewalls — all preserved

Nothing here or in the candidate asserts or implies: a strict-fan cover, any
statement on the ramified fibre `rho=0`, any equality face (including the
`AC=R3` face at `ord(R)` below the strict cell), positive-order leading
loads, `V(k)`, the six staged Rees charts, the terminal/Taylor receiver,
either global `G2` obligation, Gate T, order two, maximum twelve, `(8,12)`,
JC2, or a counterexample.  The candidate's closing denial list is complete;
the twelve replacements create no new emptiness theorem and leave every
endpoint lifecycle label untouched.

## 9. Execution record

Desk scale only: pure-Python exact `Fraction` and `F_{2^61-1}` symbolic /
dual-number-tagged truncated-series checks, throwaway harnesses under
`/tmp/uac3row_review/` (`harness_fast.py` `f51dc67f…`, `harness_numeric.py`
`009f01fb…`, `audit_miner.py` `0c53ad6a…`; ≈80 s total compute).  Producer
replay rerun: PASS in 0.04 s, output lines all reproduced independently.  One
harness bug of mine (an `a=8` probe expected the `k6C` arrival at 25 instead
of `17+c=26`) was found and fixed during the session; it was a defect of my
expectation table, not of the candidate.  No AWS, no heavy CAS, no web sweep,
no canonical-ledger edit, no `jc2-lean` access; no campaign artifact touched
other than writing this file.  Campaign inputs consumed by the executable
checks: `tails.json` (byte-pinned) and the pinned miner's pure
`enumerate_primitives` (cross-checked against an independent
reimplementation, 94 cells, zero mismatches).

**PASS (CONFIRMED as scoped: core lemma proved, classification exact,
replacement conditional on the frozen linker and its independent review;
repairs are §2 wording, §4 precision, §5 replay hardening, §6 schema
content).**
