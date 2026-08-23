**VERDICT: SOUND-WITH-ERRATA — the displayed (I3)–(I5) arithmetic on the six recorded arrivals is exact and the E5 transfer to class-C zero-edges is legitimate, but the cell-level 6→2 shrink is false under the promoted E5/H5a reading the table uses: (18,27,13,9)@5 is E5-alive on a direct priced arrival, and (15,25,12,5)@3 is E5-alive on the book's own arrival law.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `xmodel/sol-gluing-design.md` §2.2 (GPT-5.6-Sol), under the promoted E5/H5a corrected reading.
Claim under review: four of the six td-7 T1-survivor cells — `(15,25,8,5)@7`, `(15,25,12,5)@3`, `(18,27,13,9)@5`, `(39,65,32,13)@7` — fail before coefficient emission, while `(9,15,7,3)@2` and `(10,15,7,5)@3` pass preflight, shrinking the td-7 book 6 → 2 by arithmetic alone.
Method: re-derive (I3)–(I5) from E5 `(g')/(h')` + R2.1 + the chain-1 freeze; exact `Fraction` replay of all six table rows; line-by-line transfer of SHEET6-III:131-147 / HIII-REVIEW:102-134 onto BOOK P3 class-C zero-edges; H5a P-value vs Q-value vs printed-forced-`ν` trichotomy against SIGRAY-AUDIT:26,37,92; silent `px5.close_with_cells` + `feasible` re-enumeration of the E5 pin `kbar=(μ0 ν_G w_U−2)/(μ0−1)` over the filed chain-2 closure; substitution of the §3 rational anchor into the 15 local LEAD-PILOT rows.
No other repo file modified. No git.

---

## Per-cell table (this replay vs Sol §2.2)

All six rows use Sol's recorded zero-arrival `(w_U, ν_U)` from §2.2/§2.3. `kbar_cell = 2 d_q/(d_q−d_p)` is (I5). `kbar_E5 = (μ0 ν_G w_U − 2)/(μ0−1)` is (I4). `kbar_BOOK = (μ0 ν_U w_U − 2)/(μ0−1)` is the mixed/px5 pin that generated the book. `req w_U` is the unique E5-matching arrival weight `(kbar_cell(μ0−1)+2)/(μ0 ν_G)`.

| cell | μ0 | recorded `(w_U,ν_U)` | `ν_G` | `kbar_cell,X` | Sol `kbar_E5` | this `kbar_E5` | `kbar_BOOK` | Sol verdict | this, *this arrival* | E5-required `w_U` | this, *cell* |
|---|---:|---|---:|---|---|---|---|---|---|---|---|
| `(9,15,7,3)` | 2 | `(1/2, 7)` | 7 | `(5, 3)` | 5 | 5 | 5 | PASS | **PASS** (match) | `1/2` (= recorded) | **PASS** |
| `(10,15,7,5)` | 3 | `(2/3, 7)` | 7 | `(6, 4)` | 6 | 6 | 6 | PASS | **PASS** (match) | `2/3` (= recorded) | **PASS** |
| `(15,25,8,5)` | 7 | `(2/21, 48)` | 8 | `(5, 3)` | `5/9` | `5/9` | 5 | REJECT | **REJECT** (match) | `4/7` (absent from chain-2 closure) | **REJECT** |
| `(15,25,12,5)` | 3 | `(1/2, 8)` | 12 | `(5, 3)` | 8 | 8 | 5 | REJECT | **REJECT** (match) | `1/3` (in closure, lam=5) | **PASS on alt arrival** |
| `(18,27,13,9)` | 5 | `(2/15, 39)` | 13 | `(6, 4)` | `5/3` | `5/3` | 6 | REJECT | **REJECT** (match) | `2/5` (in closure, lam=3, *direct* cells) | **PASS on alt arrival** |
| `(39,65,32,13)` | 7 | `(2/21, 48)` | 32 | `(5, 3)` | `29/9` | `29/9` | 5 | REJECT | **REJECT** (match) | `1/7` (absent from chain-2 closure) | **REJECT** |

Every displayed Sol number reproduces. The erratum is not arithmetic. It is the promotion of “this recorded arrival fails (I4)=(I5)” to “this cell is dead.”

Handshake cross-check at the recorded arrivals, same `kbar_cell`:

| cell | `X` from (I3) | `X` from E5 (H6) `μ0(kbar_cell − ν_G w_U)` | `X` from BOOK `μ0(kbar_cell − ν_U w_U)` |
|---|---:|---:|---:|
| `(9,15)` | 3 | 3 | 3 |
| `(10,15)` | 4 | 4 | 4 |
| `(15,25,8)` | 3 | `89/3` | 3 |
| `(15,25,12)` | 3 | `−3` | 3 |
| `(18,27)` | 4 | `64/3` | 4 |
| `(39,65)` | 3 | `41/3` | 3 |

Only E5 (H6) disagrees, and only on the four recorded unequal-`ν` arrivals. BOOK `X` matches (I3) on all six, as it must: those arrivals were generated from the BOOK pin.

---

## Findings (worst first)

### 1. Severity: clear — cell-level 6→2 is false under the E5/H5a reading the table uses

- File: `xmodel/sol-gluing-design.md:20-25,47-48,511-561`
- Claim: four *cells* fail before emission; after the gate the book is the two equal-characteristic cells only; endpoint census 49/31 (dedup) and 51/33 (raw); default policy “emit no msolve job for them.”
- How checked: (I4) does not contain `ν_U`. The E5 pin of a class-C cell is

  \[
  \bar\kappa=(\mu_0\nu_G w_U-2)/(\mu_0-1),
  \]

  a condition on `(μ0, ν_G, w_U)`, not on the mixed-engine pair `(w_U, ν_U)` that `px5.py:244` used to *generate* the recorded book (`kb = Fr(mu0 * nu2 * w2 - 2, mu0 - 1)`). Re-solving the filed chain-2 closure (`close_with_cells((3/2,2))`, 69 states) for that E5 pin, then running the filed `feasible` budget test:

  | cell | recorded arrival | E5-required `w_U` | in closure? | arrival kind | `feasible` routes (eq) | N1 `gcd(kbar,ν_G)` |
  |---|---|---|---|---|---:|---|
  | `(9,15,7,3)@2` | `w=1/2` | `1/2` | yes, lam=4 | same law as sixcells (ν=7) | 4 (4) | 1 |
  | `(10,15,7,5)@3` | `w=2/3` | `2/3` | yes, lam=2 | direct `(4,3),(7,3)` | 47 (29) | 1 |
  | `(15,25,8,5)@7` | `w=2/21` | `4/7` | **absent** | — | 0 | — |
  | `(15,25,12,5)@3` | `w=1/2` | `1/3` | yes, lam=5 | engine-neutral `ν≡2 (mod 3)` | 2 (2) | 1 |
  | `(18,27,13,9)@5` | `w=2/15` | `2/5` | yes, lam=3 | **direct** `(2,5),(7,5),(12,5)` | 37 (33) | 1 |
  | `(39,65,32,13)@7` | `w=2/21` | `1/7` | **absent** | — | 0 | — |

  The `(18,27)` counterexample is not a superset artifact. State `(w,M)=(2/5,5)` is reached by the charged step

  ```text
  (2/3, 3) --λ=1 st96 l3e0k1S2x0nu7(35,15)--> (2/5, 5)
  ```

  which is the same trunk edge the §3 / sixcells `(9,15)` witness already uses. Direct cells `(ν,M)∈{(2,5),(7,5),(12,5)}` are stored by `close_with_cells`. `μ0=5` divides `M=5`. E5 arithmetic at this arrival is the identity

  \[
  \bar\kappa^{\rm E5}=(5\cdot13\cdot\tfrac25-2)/4=6=\bar\kappa^{\rm cell},\qquad
  X=5(6-13\cdot\tfrac25)=4.
  \]

  Trunk `w_{\rm tr}=(6-4/18)/13=4/9`, `ψ=1`, budget `5`; `lam_pre=3` fits, including the direct terminal that §2.3 already lists for this cell. N1: `gcd(6,13)=1`.

  `(15,25,12)` is weaker (empty `cellmap`, only the engine's blanket `ν_H≡−1\pmod{μ0}` law) but it is the *same* arrival law that accepts the `(9,15)` lead cell (whose `(1/2,2)` `cellmap` is also empty, because `H2` is a clean-neutral not tagged `st96`/`clean`). Charged pure-b predecessors of `(1/3,3)` exist. At `w_U=1/3`:

  \[
  \bar\kappa^{\rm E5}=(3\cdot12\cdot\tfrac13-2)/2=5=\bar\kappa^{\rm cell}.
  \]

  Direct terminal `w=2/5`, `ψ=1`, `lam_pre=5=6−ψ`. N1: `gcd(5,12)=1`.

  `(15,25,8)` and `(39,65)` have no E5-required `w_U` in the priced closure with `μ0∣M`. Those two *cell* kills stand.

- Why this is an erratum, not a nit: §0.2, §2.2's implementation policy, and the 49/31 census all treat the four *cells* as gone. Emitting no job for `(18,27)` would drop 37 E5-valid completions of a T1-surviving, N1-legal, budget-fitting cell. The honest statement of the displayed table is: **four recorded mixed-engine arrivals fail (I4)=(I5); two of those four cells remain E5-realizable.** Under E5 the recorded book does not shrink 6 → 2.

- The other coherent reading (printed `(g)/(h)` + forced `ν_G=ν_U`) *does* kill all four cells: a silent equal-`ν` re-enumeration of the same closure returns only `(9,15)` and `(10,15)` as T1-alive N1 budget-fitting cells. Sol's sentence at :547-548 (“the same four *records* are rejected”) is true of records. The surrounding cell-level language is not.

### 2. Severity: clear — even granting only the recorded six, the E5-corrected class-C menu was not re-solved

- File: `xmodel/sol-gluing-design.md:541-561,1304,1394-1405`
- Claim (implicit in “these are the two surviving cells only”): the E5 gate applied to the existing book *is* the E5 book.
- How checked: the generator's class-C step pins `kbar` from `(μ0, ν_U, w_U)` and then searches `ν_G`. E5 pins `kbar` from `(μ0, ν_G, w_U)` and does not use `ν_U` at all. Those are different Diophantine problems. A bounded E5 re-scan (`ν_G≤80`, engine arrival predicate, filed `feasible`) already produces further T1-alive N1 budget-fitting cells with *direct* stored arrivals, among them

  `(25,35,17,5)@8`, `(26,39,19,13)@7` (63 raw / 53 eq), `(34,51,25,17)@9`, `(42,63,31,21)@11`, `(50,75,37,25)@13`,

  plus a `w=2/(2k+1)` family. This list is a *superset* (engine-neutral arrivals, `ν_G` cap) and is not offered as a new certified book. It is offered as a proof that “49/31, two cells only” is not an E5 theorem. An implementation that rejects the four recorded cells and emits only `(9,15)` and `(10,15)` is not running the E5 menu.

- Suggestion: Stage 0 must re-run class-C generation with the E5 pin before any rejection manifest is treated as a census. Until that re-run, the only proved E5 statements are: the six *recorded arrivals* have the table's verdicts; `(18,27)` and `(15,25,12)` have other priced E5 arrivals; `(15,25,8)` and `(39,65)` have none in the filed closure.

### 3. Severity: clear — the E5 transfer to td-7 class-C zero-edges is legitimate (attack 2 fails as posed)

- File: `xmodel/sol-gluing-design.md:260-276,511-525`; sources `SHEET6-III.md:131-147`, `SHEET6-HIII-REVIEW.md:102-134`, `BOOK-OFFAXIS.md:293-315,541-546`, `SHEET6-DEPTH.md:253-277`
- Attack: §2.2 applies E5, “a td=6 pole-to-merge template formula,” to td=7 class-C merges; transfer is the likeliest break.
- How checked, line by line.

  **(T1)** E5 is the corrected Prop. 9.3 `(g)/(h)` for *any* case-III step. SHEET6-III:136-147 re-derives it from `D_F=κ_F d_F`, St. 3.17(ii), printed `(e)`, and H5a `κ_F=ν_F κ_G/ν_G`. No pole hypothesis, no td hypothesis, no locked-tail identity `κ̄=ρ(ν+1)`. The tail closed forms at III:149-157 are *not* used in §2.2. The other E5 in the repo (TEMPLATE `w_i^4`) is not cited and is not this formula. The “td=6 pole-to-merge template” characterization is the wrong object for what §2.2 actually imports.

  **(T2)** Class-C is defined as chain-2 at 0, `μ0≥2`, case III, `ν_G≥2` (`BOOK-OFFAXIS.md:541-546`). DEPTH §5c is the same classification: 0-direction ⇒ the chain-2 pole has coefficient 0 at `π(G)`, while `ν_G≥2` puts `G∈V_{1,a}`, so the 0-edge is case III. All six recorded arrivals have `ν_U≥2`, so the parent is itself `V_{1,a}` and can sit at an `α_j`. This is the Prop. 9.3 case-III parent.

  **(T3)** Name translation. Thesis: `G=F+c`, `F` new/shallower, `G` parent/deeper. Design: `L`/`G` rootward = shallower = merge = thesis `F`; `U` poleward = deeper = chain-2 parent = thesis `G`. Then `(h')` `κ̄_F=(ν_F κ̄_G+n)/ν_G` becomes design (H5) `κ̄_G=(ν_G κ̄_U+n_e)/ν_U`. Checked.

  **(T4)** (H6) `X_G=μ0(κ̄_G−ν_G w_U)` is not printed in SHEET6-III; it is (H5)+(H8)+the definition of `w_U`. Let `w_U=(κ̄_U−ρ_U)/ν_U`. Then

  \[
  \bar\kappa_G-\nu_G w_U=(n+\nu_G\rho_U)/\nu_U.
  \]

  (H5) on `D` and `ρ_U=D_U/\deg p_U` give `X_G=(\deg p_U/i_G)\,(n+ν_G ρ_U)/ν_U`. (H8) / St. 3.17(i) + Prop. 8.1(i) is `deg p_U^{\rm full}=i_G μ0`, hence (H6). Independently verified on the §3 ledger: `i_G μ0=22610·2=45220=` full `f`-degree of `H2`.

  **(T5)** (I3) is R2.1 case I/II at the frozen chain-1 edge `(μ,w)=(1,2)` (P3:521-524). Independent of E5 and of H5a. Combined with (H6) this is (I4). Calling (I4) “the E5-required value” is slightly fat — it is E5 plus the chain-1 freeze — but the identity is correct.

  **(T6)** (I5) is (I3) plus `X/κ̄=d_p/d_q`. Independent of E5. Reproduces every table `kbar_cell`.

  **(T7)** H5a's double realization at a case-III vertex is exactly the class-C merge: `P` is the 0-chain (non-jump at `π(G)`), `Q` is the nonzero chain-1 (the jump). The promoted scope of H5a *is* this vertex. Not a td=6-only convention.

- Result: the transfer, as a local case-III update, is sound. The failure in Finding 1 is a different wrong-object (recorded mixed arrival versus cell), not “E5 cannot leave td=6.”

### 4. Severity: clear — H5a dependence is inside promoted scope; the P-value reading kills (I4), not the two passers' chain-1 data

- File: `xmodel/sol-gluing-design.md:50-56,545-550`; `SHEET6-III.md:131-147,223-242`; `SHEET6-HIII-REVIEW.md:102-128`; `SIGRAY-AUDIT.md:26,37,92`
- Attack: does the kill depend on H5a beyond its promoted scope? What fails if H5a is read the other way?
- How checked.

  Promoted H5a is the jump/max (Q) value at a doubly realized vertex. Printed Not 3.5 is a GAP (`SIGRAY-AUDIT.md:26`). St. 3.8 upgrades that GAP: only jump/max makes `D∈Z` (`:37`), and `:92` records the upgrade to a printed-statement-forced reading. Sol cites `:26,92` as if both were the GAP; `:92` is the upgrade note. Citation slop, not a hidden axiom.

  Three readings, not two:

  | reading | `κ` at the merge | case-III update | (I4) | recorded four | `(9,15)`, `(10,15)` |
  |---|---|---|---|---|---|
  | H5a / Q-value + E5 `(g')/(h')` (promoted) | `ν_G κ_U/ν_U` | (H5), (H6) | theorem | those *arrivals* fail; two *cells* live (F1) | pass, `ν_G=ν_U` so E5=BOOK |
  | printed `(g)/(h)` + force `ν_G=ν_U` (other coherent) | equals Q-value *when* `ν` equal | printed, only if `ν_F=ν_G` | not used; unequal `ν` illegal | four *cells* die (no equal-`ν` arrival in closure) | pass |
  | P-value / coarse (the actual “other way” to read Not 3.5) | `κ_U/ν_U` | `κ̄_G=κ̄_U/ν_U+n/(ν_U ν_G)` | **not derived** | (I4)≠(I5) is not a theorem | chain-1 still pins `kbar_cell∈{5,6}`; zero-edge matching needs a different `n` |

  HIII-REVIEW:112-128: printed `(g)/(h)` hold iff `κ_F=κ_G`; the only Not 3.5 values are P (`κ_G/ν_G`) and Q (`ν_F κ_G/ν_G`); `κ_F=κ_G` forces `ν_F=ν_G` under Q and is impossible under P. The mixed engine (`ν_U` free, printed denominator) “corresponds to neither Notation 3.5 value.”

  If H5a is read the P-way, *exactly* this fails:

  1. (H5), (H6), (I4) are not theorems. The table column `bar_kappa_E5` is meaningless.
  2. The four recorded REJECTS, *as* `(I4)≠(I5)`, evaporate. So do the two recorded PASSES *as* `(I4)=(I5)`.
  3. Printed `(g)/(h)` cannot be salvaged by forcing `ν` equal, because P-value never gives `κ_F=κ_G`.
  4. N1's proof (III:121-129) uses the jump index; integer `κ̄` and `gcd(κ̄,ν)=1` at the merge are not guaranteed from the zero-edge.
  5. St. 3.8 is false as printed (audit witness `D=−1/2`). That is why the campaign does not live on this reading.
  6. The mixed/px5 formula is *still* not the P-value update. Reading H5a the other way does not rehabilitate the old engine.

  The kill of the four *recorded arrivals* under the promoted reading is inside H5a scope (the merge is the doubly realized case-III vertex). It is not a silent extension. The *cell-level* 6→2 shrink is not an H5a-scope issue; it is Finding 1.

  Distinctive content of H5a in (I4) is the factor `ν_G` rather than `ν_U`. When `ν_G=ν_U` the swap is invisible, which is why the two passers (and the §3 pilot) do not test it.

### 5. Severity: clear — `(9,15)@2` passing preflight is compatible with dual-certified transport and with LEAD-PILOT SAT

- File: `xmodel/sol-gluing-design.md:538,719-1071`; `xmodel/sol-sixcells.md:49-143`; `xmodel/grok-sixcells-review.md` (VERDICT SOUND)
- Claim (consistency, attack 4): the preflight PASS at `(9,15)@2` must not contradict the dual-certified transport survival or the §3 SAT.
- How checked.

  Preflight PASS is `ν_G=ν_U=7`, so (I4)=(I5)=5 and E5=BOOK. sixcells :124-135 closes the zero-edge by R2.1 `X=2(5−7/2)=3`, which is the equal-`ν` special case of (H6). The hostile sixcells review independently substituted every displayed `(p,q)` and replayed both completions. No tension: the transport tier used the reading-independent special case.

  §3.2: case-III edge `G→H2` has E5 raw `n=7` and `ν_G=ν_H=7`, “so E5 and BOOK coincide.” The pilot therefore does not exercise the `ν`-swap. It does exercise the same cell that preflight accepts.

  Rational anchor of §3.6 (`A=c=S_r=1` and the displayed remaining values): all 15 local LEAD-PILOT rows evaluate to `0` over `Q`

  | row | value |
  |---|---|
  | `2 B_{p1}−3 A_{p1}` | 0 |
  | `C_{p1}−3 A_{p1}^2` | 0 |
  | `11306 C_n+11305 A_n` | 0 |
  | `−14 A_g+21 B_g` | 0 |
  | `−7 A_g B_g−5 C_g` | 0 |
  | `4 C_h+7 A_h` | 0 |
  | `3 C_{f3}+10 A_{f3}` | 0 |
  | `2 B_{f2}−3 A_{f2}` | 0 |
  | `10 C_{f2}−51 A_{f2}^2` | 0 |
  | `Sig_{f1}−3 A_{f1}` | 0 |
  | `Pi_{f1}−3 A_{f1}^2` | 0 |
  | `4 C_{f1}+15 A_{f1}^3` | 0 |
  | `2 U_{p2}+3 A_{p2}` | 0 |
  | `8 V_{p2}−3 A_{p2}^2` | 0 |
  | `8 C_{p2}−9 A_{p2}^3` | 0 |

  Guards in (P13) are the claimed nonzero rationals. SAT over `Q` of this prefix is compatible with preflight PASS. A preflight REJECT of `(9,15)` would have been a contradiction; it does not occur.

  Limitation, not a break: SAT of the equal-`ν` pilot does not corroborate the four recorded kills, because those kills are exactly the content of the `ν_G` vs `ν_U` swap, which the pilot never sees. Sol does not claim otherwise.

### 6. Severity: nit — three labelling / citation slips that do not move a verdict

- `(I4)` is introduced as “the E5-required value.” It is E5 (H6) plus chain-1 (I3). The algebra is right; the name attributes a merge-gluing corollary to E5 alone.
- `SIGRAY-AUDIT.md:92` is cited next to `:26` as the GAP record. `:26` is the Not 3.5 GAP; `:92` is the St. 3.8 upgrade that *forces* jump/max. The CONJECTURE H5a flag is still honest (printed Not 3.5 remains a GAP); the upgrade is undersold.
- DEPTH §5c and BOOK R2.1 case-III still write `κ̄_G−X=ν_e w_e` / `X=μ0(κ̄_G−ν_e w_e)` with `ν_e=ν_U`. Sol says so (`:274-276`, rider at `:1172-1173`) and replaces that row. Not a silent override of a promoted theorem: SHEET6-III E5 is the later promoted correction of exactly those denominators.

---

## Attack-list scorecard

| # | Target | Result |
|---|---|---|
| 1 | Replay §2.2 arithmetic from promoted E5 and H5a, exact, cell by cell | Holds on every displayed entry. All six `(kbar_cell, kbar_E5, verdict)` triples match. (I3), (I5), (H6) re-derived. |
| 2 | Wrong-object: E5 as td=6 pole-to-merge template applied to td=7 class-C | Transfer of `(g')/(h')` is legitimate (Finding 3, T1–T7). The actual wrong-object is evaluating E5 on mixed-engine recorded arrivals and concluding *cell* death (Findings 1–2). |
| 3 | H5a beyond promoted scope; what fails the other way | Kill of the four *recorded arrivals* is inside H5a scope. P-value reading undefines (I4) and evaporates those REJECTS-as-stated; it also breaks St. 3.8. Printed+force-`ν` still kills the four *cells*. Cell-level 6→2 under E5 is not an H5a issue. |
| 4 | `(9,15)@2` PASS vs dual-certified transport and LEAD-PILOT SAT | Compatible. Equal-`ν` special case; 15 local pilot rows vanish at the rational anchor. SAT does not test the `ν`-swap. |

---

## What remains true

- Under the displayed arrivals, four mixed-engine completions are E5-inconsistent and two are E5-consistent. That is a proved numerical contradiction on those six pairs, conditional on H5a/E5.
- `(15,25,8,5)@7` and `(39,65,32,13)@7` are not E5-realizable from any priced chain-2 state in the filed closure. Those two cells *do* die by arithmetic.
- Under printed `(g)/(h)` + forced `ν_G=ν_U`, the cell-level shrink 6 → 2 holds.
- `(9,15)@2` remains a demonstrated transport + local-T1 + LEAD-PILOT survivor, and its preflight PASS is the same identity the rest of the document already uses.

The implementation consequence of the erratum: do not stamp `UNSOUND-FOR-VERDICT` / no-job on `(18,27)` or `(15,25,12)` as cells; stamp it on the *recorded* `(w_U,ν_U)` pairs. Re-run class-C generation with the E5 pin before publishing a post-E5 census.
