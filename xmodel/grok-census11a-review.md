**VERDICT: SOUND — the 13 newly added cells are E5-realizable on genuinely priced chain-2 arrivals, N1 bites exactly the four advertised even-μ₀ cells and no 14th, forced-ν is exactly the two equal-ν passers, and the route recount is 238 raw / 202 eq / 233 dedup / 197 eq on the nose.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `BOOK-OFFAXIS.md` §11a + `cases/td7_census_e5.py`, the E5-corrected td-7 class-B/C census (promoted Q-value+E5 book = 17 cells / 233 dedup).
Claim under review: the 13 cells added beyond the six already replayed in `xmodel/grok-gluing-preflight-review.md` are priced E5 matches, survive T1 / N1 / budget, and with the four kept old cells make the advertised 17 / 238 / 233 / 197 book; forced-ν is exactly 2 cells.
Method: did **not** re-audit the six old rows. Independent of `td7_census_e5.enumerate_book`: re-derived (I5a)–(I5d) from (I4)=(I5), inverted every `(μ₀, w)` on the filed 69-state closure (`px5.close_with_cells((3/2,2))`, budget 5), brute-forced `ν_G ≤ 400` as a completeness check (0 misses, 0 extras), reconstructed a min-cost charged path to every new arrival state via `px2.chain_steps`, replayed T1 / N1 / `px5.feasible`, and recounted raw / eq / dedup under the engine's own key. Engine itself re-run: exit 0, G1–G5 PASS.
No other repo file modified. No git.

---

## Per-new-cell table (this replay vs §11a)

`kbar_cell = 2 d_q/(d_q−d_p)` is (I5). `kbar_E5 = (μ₀ ν_G w_U − 2)/(μ₀−1)` is (I4). `w_req` is the unique E5-matching weight `(kbar_cell(μ₀−1)+2)/(μ₀ ν_G)`. “Direct” means a stored `st96`/`clean` cell in `cellmap`; “neutral only” is the engine's blanket `ν ≡ −1 (mod μ₀)`. `forced?` is whether `ν_U = ν_G` is itself a legal vertex at a priced state. Paths are min-cost from the seed `(3/2, 2)`.

| cell @ μ₀ | κ̄ | `w_req` | priced `(M,λ)` | last charged step | arrival | (I4)=(I5), `X` | T1 | N1 `gcd` | raw(eq) / dedup | forced `ν_G`? | this |
|---|---:|---|---|---|---|---|---|---:|---|---|---|
| `(21,35,17,7)@4` | 5 | `1/4` | `(4,5),(8,5)` | `pure-b l13e5` `λ=1` from `(2/13,13)` | **neutral only** | 5=5, `X=3` | alive | 1 | 2(2) / **1(1)** | no (`17≡1≢3 (mod 4)`) | **PASS** |
| `(25,35,17,5)@8` | 7 | `3/8` | `(8,4)` | `st96 l4e0k2S4x0nu5(40,16)` `λ=2` from `(3/4,4)` | direct `(5,8)` + neut. | 7=7, `X=5` | alive | 1 | 3(2) / 3(2) | no (`17≡1≢7 (mod 8)`; dir≠17) | **PASS** |
| `(26,39,19,13)@7` | 6 | `2/7` | `(7,3)` | `st96 l4e0k1S3x0nu17(119,35)` `λ=1` from `(3/4,4)` | direct `(3,7),(10,7),(17,7)` | 6=6, `X=4` | alive | 1 | 63(53) / 63(53) | no (`19≡5≢6 (mod 7)`; dir≠19) | **PASS** |
| `(27,45,22,9)@5` | 5 | `1/5` | `(5,5),(10,5)` | `pure-b l13e3` `λ=1` from `(2/13,13)` | **neutral only** | 5=5, `X=3` | alive | 1 | 2(2) / **1(1)** | no (`22≡2≢4 (mod 5)`) | **PASS** |
| `(34,51,25,17)@9` | 6 | `2/9` | `(9,4)` | `st96 l5e0k1S4x0nu13(117,27)` `λ=1` from `(2/5,5)` | direct `(4,9),(13,9)` | 6=6, `X=4` | alive | 1 | 18(17) / 18(17) | no (`25≡7≢8 (mod 9)`; dir≠25) | **PASS** |
| `(42,63,31,21)@11` | 6 | `2/11` | `(11,4)` | `st96 l7e0k1S4x0nu5(55,11)` `λ=1` from `(2/7,7)` | direct `(5,11),(16,11)` | 6=6, `X=4` | alive | 1 | 23(22) / 23(22) | no (`31≡9≢10 (mod 11)`; dir≠31) | **PASS** |
| `(50,75,37,25)@13` | 6 | `2/13` | `(13,4)` | `st96 l7e0k1S6x0nu19(247,39)` `λ=1` from `(2/7,7)` | direct `(19,13)` | 6=6, `X=4` | alive | 1 | 31(30) / 31(30) | no (`37≡11≢12 (mod 13)`; dir≠37) | **PASS** |
| `(58,87,43,29)@15` | 6 | `2/15` | `(15,5)` | `st96 l9e0k1S6x0nu7(105,15)` `λ=1` from `(2/9,9)` | direct `(7,15),(37,15)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`43≡13≢14 (mod 15)`; dir≠43) | **PASS** |
| `(66,99,49,33)@17` | 6 | `2/17` | `(17,5)` | `st96 l9e0k1S8x0nu25(425,51)` `λ=1` from `(2/9,9)` | direct `(25,17)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`49≡15≢16 (mod 17)`; dir≠49) | **PASS** |
| `(74,111,55,37)@19` | 6 | `2/19` | `(19,5)` | `st96 l11e0k1S8x0nu9(171,19)` `λ=1` from `(2/11,11)` | direct `(9,19),(47,19)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`55≡17≢18 (mod 19)`; dir≠55) | **PASS** |
| `(82,123,61,41)@21` | 6 | `2/21` | `(21,5)` | `st96 l11e0k1S10x0nu31(651,63)` `λ=1` from `(2/11,11)` | direct `(31,21)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`61≡19≢20 (mod 21)`; dir≠61) | **PASS** |
| `(90,135,67,45)@23` | 6 | `2/23` | `(23,5)` | `st96 l13e0k1S10x0nu11(253,23)` `λ=1` from `(2/13,13)` | direct `(11,23)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`67≡21≢22 (mod 23)`; dir≠67) | **PASS** |
| `(98,147,73,49)@25` | 6 | `2/25` | `(25,5)` | `st96 l13e0k1S12x0nu37(925,75)` `λ=1` from `(2/13,13)` | direct `(37,25)` | 6=6, `X=4` | alive | 1 | 1(1) / 1(1) | no (`73≡23≢24 (mod 25)`; dir≠73) | **PASS** |

Every displayed §11a number on these 13 reproduces (κ̄, `w_U`, `M_U`, λ, direct-cell list, raw(eq)). Handshake: `X` from (I3) equals `μ₀(κ̄ − ν_G w_U)` on every row (the E5 specialisation of (H6)). No 14th T1-alive N1-ok budget-fitting cell exists in the closure: independent inversion + `g≤400` brute + `feasible` produce exactly the advertised 17.

The two neutral-only cells are not arithmetic ghosts. Both arrival weights sit in the 69-state closure and are reached by a charged `pure-b` last step (λ=1) off the already-priced trunk state `(2/13,13)`. That is the same engine-neutral law the preflight review already accepted for `(15,25,12,5)@3` (empty `cellmap`, `ν ≡ −1 (mod μ₀)`). The other eleven new cells have stored direct step-cells.

---

## Findings (worst first)

### 1. Severity: clear — the census is arithmetically right; the remaining question is which H5a reading is true, and the printed record now leans at the 17-cell book

- File: `BOOK-OFFAXIS.md:742-793`; trichotomy sources `SHEET6-III.md:131-147`, `SHEET6-HIII-REVIEW.md:107-128`, `SIGRAY-AUDIT.md:26,37,92`
- Claim (correct, and now load-bearing): promoted Q-value+E5 gives 17 cells; printed `(g)/(h)` + forced `ν_G=ν_U` gives exactly 2; P-value gives no census.
- How checked. Independent forced-ν re-enumeration (arrival vertex **is** `ν_G` and legal, then T1/N1/budget): alive set = `{(9,15,7,3),(10,15,7,5)}` only. None of the 13 new cells, and neither arrival-replaced old cell, has `ν_G` legal:

  - kbar=6, `w=2/μ₀` family (`ν_G=3μ₀−2`): `ν_G ≡ −2 ≢ −1 (mod μ₀)`, and no stored direct equals `ν_G`.
  - kbar=5, `w=1/μ₀` family (`ν_G=5μ₀−3`): same modular miss (e.g. `(21,35)`: `17≡1≢3 (mod 4)`).
  - the lone kbar=7 cell `(25,35,17,5)@8`: `17≡1≢7 (mod 8)`, stored direct is `ν=5`.

  Forced-legal among T1-alive N1-ok budget-fitting cells is exactly the two equal-ν passers. Forced route recount: 51 raw / 33 eq / 49 dedup / 31 eq — §2.2's “49/31 (51/33)” figures, correctly identified as the forced-ν book, not the E5 book. The 15 promoted-only cells (13 new + 2 arrival-replaced) fail forced-ν by the *arrival law*, not by `(I4)≠(I5)`.

- What printed / promoted evidence bears on **which** reading is true (this is the material question the census reduces to):

  | reading | κ at the merge | case-III update | zero-edge matching | this census |
  |---|---|---|---|---|
  | H5a Q-value + E5 `(g')/(h')` **(promoted)** | `ν_G κ_U/ν_U` | (H5), (H6), (I4) | `ν_U` free; gate is priced `w_U` + `μ₀∣M_U` | **17 cells / 233 dedup** |
  | printed `(g)/(h)` + force `ν_G=ν_U` | equals Q-value *when* `ν` equal | printed, only on that locus | unequal `ν` illegal | **2 cells / 49 dedup** |
  | P-value / coarse | `κ_U/ν_U` | `(g)/(h)` never hold (HIII-REVIEW:112-115) | (I4) is not a theorem | **no census** (St 3.8 also fails) |

  Printed evidence that **kills P-value**: SIGRAY-AUDIT:37 (St 3.8 `D∈Z` is false under the P-presentation; witness `D=−1/2`) and :92 (this upgrades H5a from a coherence convention to a printed-statement-forced jump/max reading). P-value is not a live option for this campaign.

  Printed evidence that **favours E5-as-erratum (17 cells) over printed-formula-as-gospel (2 cells)**:
  1. Once Q-value is forced, SHEET6-III:137-143 re-derives `(g')/(h')` from `D_F=κ_F d_F`, St 3.17(ii), printed `(e)`, and `κ_F=ν_F κ_G/ν_G`. The printed denominators `ν_F` are then a subscript slip (E5). `ν` need not be equal.
  2. HIII-REVIEW:112-115: printed `(g)/(h)` hold iff `κ_F=κ_G`; under Q-value that forces `ν_F=ν_G`, and it is *impossible* under P-value. The forced-ν reading is the *other coherent* restriction of the printed formula, not a derivation from Q-value + St 3.17.
  3. HIII-REVIEW:129-134: St 9.6's printed proof (p. 53) writes `ν_F` in exactly this formula family and then plugs in `ν=3=ν_G` of the parent. The thesis itself treats the printed subscript as `ν_G`. That is independent printed support that E5 is a slip, not a domain restriction.
  4. Against: no printed *computation* in the thesis discriminates the two coherent readings (HIII-REVIEW:137). Forced-ν remains coherent if one privileges the printed tokens of `(g)/(h)` over the St 3.17 derivation and the p. 53 slip.

  Promoted evidence is unambiguous: SHEET6-III files E5 as an erratum and adopts Q-value; the campaign lives on the 17-cell book. The census is honest that every cell beyond the two equal-ν passers is conditional on that choice. The new information is that the conditionality is now *quantified* (15 cells / 184 of 233 dedup routes sit on the promoted-only side) and that the printed record, via St 3.8 + the St 9.6 slip, leans at Q+E5 rather than at forced-ν.

- This is not an erratum of §11a. The subsection records both books and does not pretend the caveat evaporated.

### 2. Severity: clear — N1 bites exactly the four advertised cells; no 14th T1-alive budget-fitting cell is N1-killed, wrongly or otherwise

- File: `BOOK-OFFAXIS.md:734-738, 778-780`; engine `td7_census_e5.py:311-323, 488-494`; N1 at `SHEET6-III.md:121-129`; L6 at `TEMPLATE-ATTACK.md:58-60` (`gcd(κ̄_V, ν_V)=1`)
- Claim: four E5-realizable T1-alive cells die by N1 alone — `(14,21,10,7)@4`, `(22,33,16,11)@6`, `(30,45,22,15)@8`, `(38,57,28,19)@10` — and T1 additionally kills three new pre-T1 κ̄=3 cells the old book never had.
- How checked. L6 and N1 are the same condition at this merge (`gcd(κ̄, ν_G)=1`). Independent inversion of the 69-state closure, then T1 then N1 then budget:

  | cell @ μ₀ | κ̄ | `w_req` | `gcd(κ̄,ν_G)` | T1 (`d_p∣d_q`?) | priced? | `feasible` routes | verdict |
  |---|---:|---|---:|---|---|---:|---|
  | `(14,21,10,7)@4` | 6 | `1/2` | **2** | no (alive) | `(4,4)` | 9 | N1-kill |
  | `(22,33,16,11)@6` | 6 | `1/3` | **2** | no | `(6,5)` | 1 | N1-kill |
  | `(30,45,22,15)@8` | 6 | `1/4` | **2** | no | `(8,5)` | 1 | N1-kill |
  | `(38,57,28,19)@10` | 6 | `1/5` | **2** | no | `(10,5)` | 1 | N1-kill |

  These four *are* the even-μ₀ members of the same `w=2/μ₀`, κ̄=6, `ν_G=3μ₀−2` family as the odd-μ₀ survivors: `gcd(6, 3μ₀−2)=2` for μ₀ even and `=1` for μ₀ odd (`3μ₀−2 ≡ 1 (mod 6)`). Next even members (μ₀=12, 14, …) need `w=1/6`, `1/7`, … — all absent from the closure. T1 does not apply: `d_p ∤ d_q` and κ̄=6 ∉ {3,4}.

  Unique T1-alive N1-fail inversion hits *before* budget: those four, plus `(6,9,4,3)@2` at `w=1` (κ̄=6, `gcd(6,4)=2`). The fifth has **0** `feasible` routes, so it never enters the book and is not an N1 bite. No 14th T1-alive budget-fitting cell has `gcd>1`. No advertised survivor has `gcd>1`.

  New pre-T1 κ̄=3 (claimed three): `(37,111,22,37)@15`, `(47,141,28,47)@19`, `(57,171,34,57)@23` — all `d_p∣d_q`, all priced, all budget-fitting, all correctly T1-killed. Identity `d_p∣d_q ⇔ κ̄∈{3,4}` re-derived (κ̄ integral >2 ⇒ `κ̄−2∣2`). T1 scope (`ℓ=(d_q−1)/ν−1 ≥ 1`, `d_q > d_p ≥ μ₀+2`) holds on every pre-filter cell. The other 30 T1-kills are DEAD56 re-hits.

  Class B is empty even pre-T1: the E5 pin `ν_G w_U=2` with `g∣2` forces the single MP2 cell `(3,9,2,3)` at `w=1`; those states are priced (λ 4/5) but admit 0 budget-fitting completions. T1-dead regardless (κ̄=3).

### 3. Severity: clear — every new-cell `(I4)=(I5)` match is a priced closure state, not an arithmetic solution; family termination at μ₀=25 is a closure bound

- File: `BOOK-OFFAXIS.md:712-732, 766-768`; inversion `td7_census_e5.py:160-198`
- Attack: the 13 matches could be Diophantine solutions whose `w_U` is not a filed chain-2 state, or the `2/(2k+1)` family could stop because of a loop cap rather than the closure.
- How checked.

  **Priced, not arithmetic.** Each of the 13 has `w_req` among the 25 distinct weights of the 69-state closure, with `μ₀∣M_U` and a reconstructed charged path from `(3/2,2)` (table). Last steps are `st96` (11 cells) or charged `pure-b` (2 cells). No path is a free M-drop onto an unpriced weight. `(I4)=(I5)` is the inversion identity

  \[
  \bar\kappa=\frac{\mu_0\nu_G w_U-2}{\mu_0-1}=\frac{2d_q}{d_q-d_p},
  \]

  and is asserted in-engine then re-checked here as exact `Fraction` equality, including the (H6) handshake `X=μ₀(κ̄−ν_G w_U)`. Cap-free inversion (I5a)–(I5d) matches a brute `ν_G≤400` scan with 0 misses and 0 extras on the whole closure (56 inversion keys = 56 brute keys) and on each of the 13 weights separately.

  **Family termination.** The last six rows are `w=2/(2k+1)`, μ₀=15..25 odd, κ̄=6, one exact-fit route (`λ_pre=5`, `bleft=0`, `ψ=1`, tot = budget = 5). Next member would be μ₀=27, `w=2/27`, `ν_G=79`, κ̄=6. The closure's minimum weight is `2/25`; `w≤2/27` is empty; `w=2/27` is absent. Stronger than claimed: inversion against *every* priced weight produces **zero** hits at μ₀≥27 (so no *other* cell sneaks in at large μ₀ on a different `w`). The inversion loops `c=1..c(g₀)` per (I5d) — finite, no `ν`-cap, no `μ₀`-cap — and the engine iterates all 69 states. `px5.NCAP=400` is not on this path. Closure-forced.

  Labelling nit, not a miss: the same closed form `(d_p,d_q,ν_G,M)=(4μ₀−2, 6μ₀−3, 3μ₀−2, 2μ₀−1)`, `w=2/μ₀`, κ̄=6 already contains `(10,15,7,5)@3` (old passer), `(18,27,13,9)@5` (old, arrival replaced), and the new μ₀=7,9,11,13 cells. §11a only tags μ₀=15..25 as “the family” because those are the exact-fit tail. All earlier odd members are in the book; all earlier even members are the N1 four. Parallel kbar=5 family `w=1/μ₀`, `ν_G=5μ₀−3` is `(9,15)@2`, `(15,25,12)@3`, `(21,35)@4`, `(27,45)@5` and stops because `w=1/6` is absent. The only new cell outside both families is the kbar=7 singleton `(25,35,17,5)@8`.

### 4. Severity: clear — route recount 238 raw / 202 eq / 233 dedup / 197 eq

- File: `BOOK-OFFAXIS.md:742-744`; engine `:297-308, 476-479`
- How checked. Silent re-collection of `px5.feasible` on the independent 17-cell book, same key `(ctx, terminal)` with `ctx` carrying `μ₀, w₂, λ, cell` and *not* `M_U` / `ν_U`:

  | | cells | raw | raw eq | dedup | dedup eq |
  |---|---:|---:|---:|---:|---:|
  | this replay | 17 | 238 | 202 | 233 | 197 |
  | §11a | 17 | 238 | 202 | 233 | 197 |

  The five collapsed records (238−233=5, all equality) are exactly the dual-`M_U` pairs of four cells — `(9,15)` (2 collisions), `(15,25,12)`, `(21,35)`, `(27,45)` — whose two states share `w`, `λ`, cell, and terminal string, so the M_U-dropping key identifies them. Per-cell raw(eq) on every new row matches the markdown table. Forced book independently 51/33 raw, 49/31 dedup. No 18th cell, no missing claimed cell.

- Nit, not a miscount: the markdown table prints *raw* for `(21,35)` and `(27,45)` as 2(2); after dedup each is 1(1). The headline uses the dedup totals. Convention is stated (`td7_census_e5.py:58-61`) and matches px5's drop of `M_U`.

### 5. Severity: nit — family-extent wording and the two weaker (neutral-only) new cells

- §11a:766-768 names only the last six rows as the `w=2/(2k+1)` family. The closed form starts at μ₀=3 (Finding 3). No cell is missing; the wording undersells how much of the new book is one family.
- `(21,35,17,7)@4` and `(27,45,22,9)@5` have empty `cellmap`. They survive on the filed arrival-law superset (honesty rider at :814-815), same as `(15,25,12)`. They are priced states with charged last steps; they are not direct-cell witnesses. An implementation that tightened arrivals to stored step-cells only would drop these two (and the old `(15,25,12)`), leaving 14 promoted cells, still not the forced-ν two.

---

## Attack-list scorecard

| # | Target | Result |
|---|---|---|
| 1 | Per-new-cell (I4)=(I5) by a priced px5 arrival, not an arithmetic solution; family termination at μ₀=25 a closure bound | Holds on all 13. Every `w_req` is a 69-state closure weight on a charged path; 11/13 have stored directs. Inversion = brute. No `w≤2/27`; no μ₀≥27 hit on any priced weight. |
| 2 | Replay T1 (`d_p∣d_q`), L6/N1, budget on the 13; verify the 4 N1 kills and that no 14th cell was wrongly N1-killed | Holds. All 13 T1-alive, N1-ok, budget-fitting. N1 four are exactly the even-μ₀ `w=2/μ₀` siblings (`gcd=2`); the only other T1-alive N1-fail inversion hit is budget-dead `(6,9,4,3)@2`. L6≡N1 here. |
| 3 | Forced-ν = exactly 2 cells, from the trichotomy; what printed/promoted evidence says about *which* H5a reading is true | Holds as a census fact. Material question: St 3.8 kills P-value; St 3.17 + the St 9.6 `ν_F`/`ν_G` slip favour E5-as-erratum (17 cells); forced-ν stays coherent only if printed `(g)/(h)` are treated as gospel. Census records both books. |
| 4 | Recount 238 raw / 233 dedup / 197 eq | Holds (and 202 raw-eq). Five collapses are dual-`M_U` identical terminals. |

---

## What remains true

- Under promoted Q-value+E5 the post-E5 class-B/C book is 17 T1-alive N1-ok budget-fitting cells, 238 raw / 233 dedup (197 eq). The 13 additions are real. Class B is empty.
- Under printed `(g)/(h)` + forced `ν_G=ν_U` the book is exactly `(9,15,7,3)@2` and `(10,15,7,5)@3`, 51 raw / 49 dedup (31 eq). That *is* §2.2's 49/31.
- `(15,25,8,5)@7` and `(39,65,32,13)@7` stay dead (`w_U=4/7`, `1/7` absent). The two arrival-replaced old cells stay alive only on the promoted reading.
- The next tier (transport / global / coefficient) is on 17 cells, of which 2 are unconditional across the coherent readings. The §11 ADDENDUM transport result for `(9,15)@2` is untouched.
- Honesty riders inherited from §10 still apply: arrival law is a superset, λ is a min-over-paths lower bound, and the census is conditional on CONJECTURE H5a + promoted E5 + P3's one-orbit classification + the P0-closed budget-5 state family.

Reproduction (this review): `python3 cases/td7_census_e5.py` (exit 0, ~51 s, G1–G5 PASS) plus a silent first-principles inversion / path reconstruction / recount that does not import the census enumerator.
