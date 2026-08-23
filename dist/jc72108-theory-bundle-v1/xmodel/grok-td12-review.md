**VERDICT: SOUND-WITH-ERRATA — FIRST-DEATH REFUSAL kills the 8 co-scaled cells on the *enumerated* list (74 unique gaps, not the advertised 54; all refuse; the neutral lemma and the cylinder `(4ν+1)`-part both replay); the 6 spine stamps replay at the entry-tier `P/μ`; no occurring 55th unrefused first death was found. The completeness claim, three tautological gates, B1’s “gap-generic” sentence, and the fail-closed inventory are not earned as written.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-17.
Target: `BOOK-TD12.md`, `cases/td12_book.py`, and the FIRST-DEATH REFUSAL theorem (the new kill: no `M=1` carrier, no X, both poles identical `(6,1,2,5)`).
Claim under review: all 14 entry-level cells of the td-12 type-`(3,5)` book are TOWER-DEAD (6 `SPINE-DEAD-H8` + 8 `CLASH-DEAD-FIRSTDEATH`), conditional on the named fail-closed classes.
Method: line-read of the book against `xmodel/sol-tdbound-review.md` §8, `cases/book_offaxis.py:merge_cells`, `TOWER-TD11.md` §0 / OB7a, `NF-M.md` / `cases/nfm_check.py` G2–G3, `cases/td11_census.py` `menu_BB` + FC1–FC7, `SHEET6-L1.md` St 8.4/8.5, `TOWER-UNIFORM.md` H8, `px2.chain_steps`. Independent exact `Fraction` replay of the P1/Z1 packet, the 14-cell skeleton, the `{3,6}`-lattice, the 74-gap list, the neutral lemma on `u ≤ 399`, the cylinder law on `ν ≤ 399`, the td-11 BB1/BB2 menus (engine window and the `k ≤ 9, x ≤ 20, ν ≤ 200` widening), the budget-10 cutoff Dijkstra, and H8 `P/μ` at the B1 degrees. `python3 cases/td12_book.py`: exit 0, **11/11 PASS**. No other repo file modified. No git.

The 11/11 gate is not a proof of its prose labels. Three of the eleven checks are tautologies (`H1`, `F4`, `C2`).

---

## Findings (worst first)

### 1. Severity: erratum — the candidate list is 74, not 54, and completeness is list-relative. No 55th *occurring* unrefused first death was found; a missing occurring candidate would still be a hole.

- File: `BOOK-TD12.md:50,91`; `cases/td12_book.py:136-158`
- Claim: “54 candidates swept, zero unrefused”; F3’s f-string prints `len(set(GAPS))`.
- How checked.

  Independent rebuild of the exact `GAPS` construction:

  | family | raw | unique contribution |
  |---|---:|---:|
  | seed menu `{5/21, 4/15, 5/21, 1/5}` | 4 | 3 |
  | neutrals `u ∈ {5,7,11,13,17,25}` | 6 | 5 (`u=5` is `1/5`, already the pure-b row) |
  | BB2 `(k̄, d_p)` eight-tuple | 8 | 8 |
  | cylinder `ν = 2..59` | 58 | 58 (pairwise distinct: `gcd(2ν+1, 4ν+1)=1`) |
  | BB1 `[(4,10),(2,4)]` at `i ≥ 6` | 2 | 0 (both already among the BB2 gaps `1/15`, `1/12`) |
  | **total** | **78** | **74** |

  The live gate prints “zero unrefused candidates among **74**”. The book’s “54” is a stale count (a previous `ν`-cut `2..35` plus the 20 non-cylinder raw rows is 54 before uniquing). It is not the object the machine swept.

  **Attack (1), replayed.** Every one of the 74 refuses under the book’s `refused()` (any-cap, `{3,6}`-lattice), under the stricter same-cap test `k ∣ c` for the `c` that produced the lattice, and under the reachable-from-`α_1=10/3` one-step prefix lattice. Max is `5/9` (cylinder at `ν=2`), as advertised.

  **What is not proved.** Den-refusal kills only what is enumerated. The following were checked as the natural 55th-candidate sources:

  1. *td-11 BB2 engine, including the non-authoritative `M_G ∈ {5,8,9}` cells.* The eight book pairs `{(4,20),(7,11),(8,26),(5,14),(6,15),(8,65),(4,45),(2,8)}` are exactly the unique `(k̄, d_p)` of `menu_BB(2)` in `td11_census.py` / `nfm_check.py`. Widening to `k ≤ 9`, `x ≤ 20`, `ν ≤ 200` adds no pair. Zero unrefused.
  2. *BB1.* Engine has exactly the two book cells `(10,16) M=2` (authoritative) and `(4,16) M=4` (not). Both refuse at `i_G ≥ 6`.
  3. *B1 core-strata gaps.* The cutoff Dijkstra produces **12** unique gaps, **10 of them absent from the 74**. All 10 refuse (`1/4, 1/8, 5/24, 1/14, 1/51, 4/195, 2/75, 1/40, 1/49, 1/42`). B1 never runs `refused()` on them; the book’s sentence “every core-strata gap joins the F3 refusal class (the den-criterion is gap-generic)” is **false as a universal claim** (`g ∈ {1/3, 1/2, 2/3, 5/6}` are unrefused on this lattice). It happens to be true of the 12 gaps the Dijkstra actually emitted.
  4. *Seed `px2.chain_steps(3/2, 2)`.* Six unique steps: 3 st96 (gaps `5/21, 4/15, 5/21`), 1 pure-b, 2 neutrals, 0 clean. All `k ≤ 2`, `lex = 0` — inside the td-7 dirty cap. Raising `k, lex` at the *seed* cannot add a row the existing cap missed. Descendant states with larger `num(w)` are where the inherited `k ≤ 6`, `lex ≤ 40` cap can hide a cell (named fail-closed (a), not discharged).
  5. *`ν = 1`.* The printed domain law (`TOWER-TD11.md` §0: `gcd(a,ν)=1` and `d ∣ ν+1`) admits `u=1` at `w=3/2`. Gap `(1+1)/(6·1)=1/3`, **unrefused** (`α=10/3` gives `r=8/3`, `den=3 ∣ 3`). This is exactly the integer the book’s `u ≥ 5` conjunct deletes, and it is the only odd 3-free positive integer below 5. Parked in fail-closed (c) / NF-P. Load-bearing: if `ν=1` is ever legal as a first death, the theorem is false.

  **No exhibited hole.** I did not find a geometric first-death gap that both (i) occurs on an entry-tier configuration and (ii) escapes `refused()`. I also did not find a completeness lemma. The honest statement is: *every named family, plus the 10 extra B1 gaps, plus the td-11 BB menus at proved-sup widening, refuse; `ν=1` and beyond-core dirty cells are Rule-6.*

  **Erratum to write.** Replace “54” by “74 unique (78 raw)”. State that B1’s extra 10 are an independent refused family, not members of F3. Do not call the den-criterion gap-generic.

### 2. Severity: residual — three of eleven machine rows are tautologies; they do not discharge the obligations they name.

- File: `cases/td12_book.py:160-167,153-158,253-256`
- Claim: H1 spine-death, F4 cylinder algebra, C2 certificate / frontier.
- How checked. The predicates actually evaluated:

  | row | what it evaluates |
  |---|---|
  | H1 | `all(u % 2 == 1 for u in (5,7,11,13))` and `6==6` and `3==3` |
  | F4 | `all((4*ν+1) % 2 == 1 and 4*ν+1 ≥ 9 for ν in 2..59)` |
  | C2 | `True` |
  | F2 algebraic half | congruence on the five-point sample `{5,7,11,13,25}`, `a ∈ {0,…,L-1}` only |
  | P1 `w0` | `1·(2·8−1)/(2·5)=3/2` (correct, but a single arithmetic identity) |

  F3, F1, S1, W1, B1 (no `≥ 1/2` violator), C1 (stamp counts), and the `refused()` half of F2 are real constraints. The honest machine core is those. H1, F4, and C2 do not constrain the spine 2-adic, the `(4ν+1)`-part, or the frontier claim.

### 3. Severity: residual — H1 does not prove the 6 spine stamps; the *claim* still replays at the 14-cell tier.

- File: `BOOK-TD12.md:55-56`; `td12_book.py:160-167`; attack (4) and the mixed-μ half of (5)
- Claim: arrivals `(1,2)` / `(2,1)` give `6Π_1 = 3Π_2` i.e. `Π_2 = 2Π_1`; the `w=3/2` letter domain forces `v_2(Π)=0` on both chains; `0=1` unsat. Co-scaled `(1,1)` / `(2,2)` inhabit (empty stacks pass) and fall to F3.
- How checked.

  **Empty-prefix arithmetic is correct.** Both poles have `P=6`. H8 `= P/μ` at `(μ_1,μ_2)=(1,2)` is `6Π_1 = 3Π_2`. Domain law at `w=3/2`: `gcd(3,u)=1` and `2 ∣ u+1`, i.e. `u` odd and `3 ∤ u`. Every such `u < 80` is odd (including the `u=1` NF-P edge). Empty stacks: `Π=1`, `v_2(1)=0` both sides, `0=1`. Neutral prefixes stay at `w=3/2` and stay odd. The 6 mixed-μ *empty/neutral* routes are spine-dead.

  **The gate does not check this.** See finding 2.

  **Current-state / even-multiplier routes.** The core contains `(3,1)`, reached by the seed pure-b (`λ=3`). At `w=3` the domain law admits even letters (`ν=2` is legal). Necessary 2-adic for H8 after multipliers `m_i = d_p/ℓ` is `1 + v_2(m_1) + v_2(Π_1) = v_2(m_2) + v_2(Π_2)` on `(1,2)`. The seed `(20,16)` step has `m=10`, `v_2=1`, so the *necessary* condition can hold. It is not sufficient: H8 also demands `P_1/μ_1 = P_2/μ_2`. At the B1 degrees

  ```
  seed 6, (20,16)→60, (21,15)→63, (7,5)→21, pure-b→12, neut-drop→12
  ```

  the only H8 hits with `μ ∣ M_current` are *same-state co-scaling* and one mixed current-state pair `((2/3,3), μ=3)` against `((2,1), μ=1)`. The latter has `μ=3`, which is not an entry-level `μ ∣ b=2` assignment — it is fail-closed (d). **No entry-level `(1,2)` / `(2,1)` pair inhabits H8 after one-sided charged steps at the audited degrees.**

  So the blanket `SPINE-DEAD-H8` stamp on all 6 mixed-μ cells is correct at the 14-cell tier, and is not a live-cell escape. It is not what H1 tested, and it is not proved for current-state `μ` beyond `{1,2}` (correctly Rule-6).

  **Erratum to write.** Replace H1 by: the domain law at `w=3/2` (every legal `u` odd); empty/neutral `(1,2)` gives `v_2` mismatch; one-step B1 degrees give no H8 hit for `μ ∈ {1,2}` across distinct states; current-state `μ=3` is (d).

### 4. Severity: residual — F4 does not prove the cylinder law; the law is nevertheless true.

- File: `BOOK-TD12.md:47-50`; `td12_book.py:153-158`; attack (2)’s sibling
- Claim: gap `(2ν+1)/(4ν+1)`; the `(4ν+1)`-part of `den(α−1+g)` survives every cap `∣ 6`.
- How checked.

  The gate only tests that `4ν+1` is odd and `≥ 9`. That is true of every odd integer `≥ 9` and does not mention a death residue.

  Independent algebra, lattice `α = a/L` with `L ∈ {3,6}`:

  ```
  r = (4aν + a − 2Lν) / (L(4ν+1)).
  gcd(num, 4ν+1) = gcd(Lν, 4ν+1) = gcd(L, 4ν+1) ∈ {1,3}
  ```

  (`ν` is coprime to `4ν+1` because `4ν+1 − 4ν = 1`; `4ν+1` is odd). The surviving odd factor is `(4ν+1)/gcd(L,4ν+1) ≥ 9/3 = 3`. It equals 1 only if `4ν+1 ∣ L`, impossible for `ν ≥ 2`. The only case in which the leftover can be a bare `3` (hence a possible `3 ∣ 3` escape) is `4ν+1 ∈ {3,9}`, i.e. `ν=2`. Explicit check on the full `{3,6}`-lattice at `ν=2`: every `r > 0` has `den ∈ {9,18}`, none dividing `{1,2,3,6}`. (The extra `3` from `L` remains after cancelling one `3` from `9`.) Sweep `ν = 2..399` on both `refused()` and the strict same-cap test: **zero escapes**, including the `ν ≡ 2 (mod 3)` slice where `3 ∣ (4ν+1)`.

  F3’s finite cylinder lattice to `ν=59` is therefore a corollary, not the proof. The one-line “`(4ν+1)`-part survives” is true after the `ν=2` residual is written down. F4 as a machine row does not write it down.

### 5. Severity: clear — the neutral lemma is true; the one-line proof has no quantifier slip on the stated domain. The `u ≥ 5` conjunct is load-bearing.

- File: `BOOK-TD12.md:47-49`; `td12_book.py:127-135`; attack (2)
- Claim: for `u` odd, `3 ∤ u`, `u ≥ 5`, `den(a/L − 1 + (u+1)/(6u))` carries the `u`-part; `u` coprime to 6 forces `den ∤ 6`; the whole tower is refused.
- How checked.

  Put the residue over `6u` (legal because `L ∣ 6`):

  ```
  r = [a u (6/L) + (u+1) − 6u] / (6u).
  num = a u (6/L) − 5u + 1 ≡ 1 (mod u).
  ```

  So `gcd(num, u) = 1`. After reduction, `den = 6u / gcd(num, 6u)` is still divisible by `u`. The domain `u` odd, `3 ∤ u`, `u ≥ 5` forces `gcd(u,6)=1` and `u ≥ 5`, so some prime of `u` divides `den` and that prime does not divide 6. Hence no cap `c ∣ 6` is divisible by `den`.

  **Quantifier slips hunted, not found on the stated domain.**

  - The identity is linear in `a` and independent of the range `range(L)` vs `range(2L)`. Confirmed on `u = 5..399` odd 3-free, both `L`, `a = 0..2L−1`: zero failures.
  - `refused()` on the same rectangle: zero escapes.
  - Off-domain: `u=1` gives `g=1/3`, unrefused (finding 1.5). `u` even or `3 ∣ u` still refused on the samples I ran (`u ∈ {2,3,4,6,8,9,15,21,27}`); those are excluded by the domain law at `w=3/2`, not by the lemma.
  - The gate’s algebraic half samples five `u` and `a ∈ range(L)` only, and tests `gcd(num % u + u, u) == 1` — a congruence check, not `u ∣ den`. The `refused()` half of F2 on `{5,7,11,13,17,25}` is the actual kill check. The *lemma* is the algebra above, not the sample.

  **The one-line writeup hides the `u=1` edge, not a slip inside `u ≥ 5`.** Write the domain as “odd, `3 ∤ u`, `gcd(u,6)=1`, `u ≥ 5`” and name `u=1` as the NF-P rider. Do not say “`num ≡ 1 (mod u)` so `u ∣ den`” without the “put over `6u`, `L ∣ 6`” preamble — that is the only place a reader can lose a factor.

### 6. Severity: clear — `α_1 = 10/3` and the `{3,6}`-lattice both derive from the entry data.

- File: `BOOK-TD12.md:12-19,45-46`; `td12_book.py:54-62,120-126`; attack (3)
- Claim: type `(3,5)` gives `(k_0,ℓ_0)=(3,5)`, `g_top=8/3`, `α_1=10/3`; `den(α_1)=3 ∣ p=6`; prefix steps with `k ∣ c` keep `den ∣ lcm(3,c) ∈ {3,6}`.
- How checked.

  Promoted P1/Z1 (same law as `tower_td11.py:239-246`):

  ```
  (k_0, ℓ_0) = (α, β) = (3, 5),
  g_top = (α+β)/α = 8/3,
  α_1 = ℓ_0 + 1 − g_top = 5 + 1 − 8/3 = 10/3
       = β(α−1)/α = 5·2/3 = 10/3.
  ```

  Entry packet: poles `2 × (Λ,a,b,ν) = (6,1,2,5)`, `M=b=2`, `p = bα = 6`, `w_0 = a(b(α+β)−1)/(bν) = 15/10 = 3/2`, L6 `gcd(a(α+β),ν)=gcd(8,5)=1`, budget `td−2=10`. All identities replay. `den(10/3)=3 ∣ 6`.

  Lattice: start at `10/3`, iterate `α ← α + ℓ(k−1)/k` for `k ∣ c`, `c ∈ {1,2,3,6}`. Reachable denominators:

  | cap `c` | reachable dens | `lcm(3,c)` |
  |---|---|---|
  | 1 | `{3}` | 3 |
  | 2 | `{3,6}` | 6 |
  | 3 | `{1,3}` | 3 |
  | 6 | `{1,2,3,6}` | 6 |

  All divide the predicted `lcm`. Cap `c=1` cannot leave `10/3` (`k=1` only); the third-lattice sweep in `refused()` is a conservative superset (the OB7a pattern). F1 itself only tests *one* step from `α_1` and accepts any den in `{1,2,3,6}`; the real lattice work is the `refused()` sweep, which is the right (larger) object.

### 7. Severity: residual — the five `(2,2)` cells are the printed-tier MIXED divisor-skeleton, not the geometric merge book. St 8.4/8.5 do not close the extra `M_G`.

- File: `BOOK-TD12.md:17-18,55-57`; `td12_book.py:64-84,219-236`; `book_offaxis.py:108-147`; attack (5)
- Claim: `(2,2)×5` stamped `CLASH-DEAD-FIRSTDEATH`; skeleton matches `sol-tdbound-review` §8; μ-assignment by St 8.4/8.5.
- How checked.

  Independent enumeration `μ_i ∣ 2`, `M_G ∣ (μ_1+μ_2)`, interior ⇒ `M_G ≥ 2` (MP2):

  | arrivals | root | interior | total | class in `merge_cells([2,2])` |
  |---|---:|---:|---:|---|
  | `(1,1)` | 3 | 0 | 3 | MP6 |
  | `(1,2)` | 3 | 0 | 3 | MP6 |
  | `(2,1)` | 3 | 0 | 3 | MP6 |
  | `(2,2)` | 3 | 2 | **5** | **MIXED** |
  | | 9 | 5 | **14** | 11 orbits under pole swap |

  `book_offaxis.merge_cells([2,2])` returns exactly 14, split `9 MP6 + 5 MIXED`. Matches §8 and S1.

  **St 8.4** (`SHEET6-L1.md:85-86`; `mult(p,c) ∣ M_G` at the deeper vertex): leaf arrival `μ ∣ b_i = 2`, so `μ ∈ {1,2}`. Complete at the *entry* parent. This is why there are not more μ-assignments in the 14.

  **St 8.5** (`M_G ∣ M_F` for `G = F° ∉ V_{2,a}`): the merge *is* in `V_{2,a}`. St 8.5’s hypothesis fails. This is the BOOK-OFFAXIS-REVIEW Step-2 error, not newly invented. You cannot use St 8.5 to force `M_G ∣ 2` at these cells.

  **MP6 `M_G ∣ Σ μ_e`** is R2.2(D), valid only at `ε=0=k` (`td11_census.py` v2, the whole point of the 159 vs 411 split). The five `(2,2)` cells are *all-`μ ≥ 2` MIXED*: extra NE roots (`k ≥ 1`) are legal, and the engine BB2 menu realises `M_G ∈ {1,2,4,5,8,9}`. The values `5,8,9` do **not** divide 4. They are not extra rows of the 14-cell skeleton; they are extra geometric realisations of the `(2,2)` arrival class. The book does the right thing with their *gaps* — `(8,65)`, `(4,45)`, `(2,8)`, `(6,15)` are in F3 and refuse — but the stamp table’s “`(2,2)×5`” is the divisor skeleton, not the geometric book.

  Co-scaling at seed: `6/2 · Π_1 = 6/2 · Π_2` ⇒ `Π_1=Π_2`, empty stacks inhabit. Those five cells (and the three `(1,1)`) correctly fall to first-death refusal. The new arrival structure is handled by importing the td-11 BB2 menu, not by St 8.4/8.5.

  **Erratum to write.** Cite St 8.4 for `μ ∣ 2` only. Say St 8.5 does not apply at the merge. Say MP6 `| Σμ` only at `ε=0=k`. Record that the F3 BB2 list is the geometric completeness rider for the five MIXED cells (and that this rider is the td-11 FC7 menu, not re-proved here).

### 8. Severity: residual — fail-closed classes are the right *shape* and miss two named td-11 riders; FC4-D / FC5-D are cited, not re-derived.

- File: `BOOK-TD12.md:61-70`; `td12_book.py:245-252`; `td11_census.py:721-746`; attack (6)
- Claim: KEEP-AS-POSSIBLY-LIVE (a) budget-10 beyond-core, (b) Q+E5/E5F, (c) `ν=1`/NF-P, (d) current-state arrivals / FC4-D, (e) post-merge / FC5-D with cylinder emission `w=6`.
- How checked.

  Mapping onto the td-11 inventory:

  | td-11 | td-12 named? | status here |
  |---|---|---|
  | FC1-R beyond-core | (a), and correctly notes the fleet lane is budget-9 | OPEN, as it must be |
  | FC2 complement sweep | **not named** | the 10 extra B1 gaps are a fragment of this; not discharged |
  | FC3 Q+E5/E5F | (b) | OPEN, same as td-11 |
  | FC4 current-state / sync dichotomy | (d), “pattern applies” | cited, not re-proved at these constants; the one B1 H8 hit at `μ=3` is exactly this class |
  | FC5 post-merge emission | (e) | the cylinder law `w = k̄(d_q−1)/(ν d_q) = 6` is an identity: `k̄=3(2ν+1)`, `d_q=2ν+1` ⇒ `w=6` constant. The *emission number* replays; the “joins (a)” closure is a citation of FC5-D |
  | FC6 `ν=1` / NF-P | (c) | OPEN, and load-bearing (`g=1/3` unrefused) |
  | FC7 loop bounds / menu completeness | **not named** | F3’s BB2 eight-tuple and the `ν ≤ 59` cylinder cut *are* an FC7 claim |

  Two-word deep families: the td-11 DIE-horn does not port (there is no X that dies first). First-death of the *earliest* large-gap vertex still applies — empty-prefix merge is the cylinder/`5/9` or a BB discrete; pure-neutral prefixes make the first letter (`≤ 1/5`) the first death, refused by F2. I do not demand a new named class, but the DIE-horn citation would be false here.

  Nested inner merges: `r=2`, one two-leaf hierarchy. No 11-C-style nested layer. Correctly absent.

  Inherited `px2` dirty caps (`k ≤ 6`, `lex ≤ 40`) sit in (a), not in a named menu-completeness rider.

  C2’s frontier sentence (“live frontier is `{residue-A}` plus the unadjudicated above-bound entries”) is a `True` check. It is the right *prose* consequence if the 14 cells die at this tier; it is not a machine fact.

  **Erratum to write.** Add FC2 (complement / extra core gaps) and FC7 (BB2 / cylinder loop bounds are the td-11 proved sups, cited not re-proved). Keep (c) visibly load-bearing. Do not say FC4-D “applies” without the one-line at these constants (sync ⇒ same refusal lattice; no-sync ⇒ spine at current `P/μ`; current `μ=3` is the witness that (d) is inhabited).

### 9. Severity: residual — B1’s Dijkstra is real for `gap ≥ 1/2` and wrong as a completeness instrument.

- File: `td12_book.py:172-217`; `BOOK-TD12.md:35,63-64`
- Claim: budget-10 cutoff from `(3/2,2)@6`, 6 core states below deg 94, zero steps at gap `≥ 1/2`; every core-strata gap joins F3.
- How checked.

  Independent rerun: 6 states

  ```
  (3/2, 2), (3/2, 1), (3, 1), (2, 1), (3/4, 4), (2/3, 3)
  ```

  zero `gap ≥ 1/2`, 12 unique gaps, 10 not in F3, all refused (finding 1). The “6 states” is the *degree-aware* cutoff (pole degree 6, child degree `deg · m` integral, cut at 94), not the priced `(w,M)` closure (69 states at budget 5 from the same seed, `sol-tdbound-review` §8). Different object; the book does not claim 69.

  **The else-branch hardcodes `(r,m)=(3/2, 2)` for every non-clean non-st96 tag** (neutrals and pure-b). A genuine `n=1` letter has multiplier `ν`, not 2. Neutral descendants at `deg = 6ν` for `ν ∈ {5,7,11,…}` are dropped from the heap. Their *gaps* are already in F2, so this does not create an unrefused first death. It does mean “6 core states” is an undercount of the degree-aware core, and B1 cannot be cited as a sweep of core-strata first deaths.

  No-X at the seed is independently true: menu max `4/15 < 1/2`, no clean row (`D3n2ν2` fails `den(w) ∣ d_q` because `5 ⧸ 2`), pole-adjacent M-drop `≤ 1/5`. The td-7/td-11 “X dies first” pattern correctly does not apply.

---

## Attack card (the six requested)

| # | attack | result |
|---|---|---|
| (1) | 54-candidate completeness | **List is 74, not 54.** All 74 refuse. BB2 eight-tuple = td-11 engine, widening empty. 10 extra B1 gaps refuse and are not in the list. `ν=1` is the unique small-`u` unrefused gap and is fail-closed (c). No occurring 55th unrefused first death found. Completeness is not a lemma. |
| (2) | Neutral lemma, one-line quantifier slip | **Holds** on the stated domain. `num ≡ 1 (mod u)` ⇒ `u ∣ den` after putting over `6u` with `L ∣ 6`; `gcd(u,6)=1` ⇒ `den ∤ 6`. Sweep `u ≤ 399` empty. The slip is the unwritten `u=1` edge (`g=1/3` unrefused), not a broken congruence. |
| (3) | `α_1=10/3` and the `{3,6}`-lattice | **Confirmed.** P1/Z1 and the iterated prefix dens both replay. `refused()` sweeps the OB7a superset, which is the right direction for a kill. |
| (4) | 6 spine stamps, `Π_2=2Π_1`, `v_2` | **Claim replays at the 14-cell tier; H1 does not prove it.** Empty/neutral `(1,2)` is `0=1`. B1 degrees give no mixed-μ H8 hit for `μ ∈ {1,2}`. Even letters at `(3,1)` only co-scale at `μ=1`. |
| (5) | Five MIXED `(2,2)` cells vs St 8.4/8.5 | **Skeleton 5 is right; St 8.5 does not apply; MP6 `∣ Σμ` is not the geometric book.** Extra `M_G ∈ {5,8,9}` gaps are in F3 and refuse. Arrival structure is the td-11 BB2 menu, not a new St 8.4 deduction. |
| (6) | Conditional classes complete? | **Shape yes, inventory short.** (a)–(e) match FC1/3/6/4/5. FC2 and FC7 are unnamed. FC4-D/FC5-D are citations; the cylinder `w=6` identity is the one number that actually replays. `(c)` is load-bearing. |

---

## What survives

- The structural observation is correct and should stay in the lead: both poles are identical `M=2` seeds, there is no `M=1` L-A carrier, the seed menu max is `4/15 < 1/2`, and the promoted clash apparatus (X dies first, CAP-DEN on an X-family) does not apply.
- FIRST-DEATH REFUSAL is the right replacement *shape*: `k = den(α−1+g)` on the `{3,6}`-lattice against caps `{1,2,3,6}`. It is the general den-criterion of the td-11 block-2 repair (not Lemma CAP-DEN), correctly named this time.
- The 14-cell skeleton matches `merge_cells([2,2])` and `sol-tdbound-review` §8.
- The 8 co-scaled cells die on the enumerated list. The 6 mixed-μ cells die by H8 at the entry tier. I did not resurrect a cell.
- The certificate is already labelled conditional. That label is the only reason this is not an emptiness-certificate overclaim in the td-11-§10 sense.

The last below-bound filed entry is therefore **adjudicated at the entry/merge-cell tier, with the errata above**. The bound `td ≤ mn` did not protect it; that observation in `BOOK-TD12.md` §5 / `TDBOUND.md` is unchanged by this review.

---

## Reproduction

```bash
python3 cases/td12_book.py     # 11/11, exit 0; F3 prints 74 not 54
```

Independent work in this review: exact `Fraction` rebuild of the 74-list, the neutral lemma on `u ≤ 399`, the cylinder law on `ν ≤ 399` including the `ν=2` residual, `menu_BB` at the td-11 engine window and at `k ≤ 9, x ≤ 20, ν ≤ 200`, the budget-10 cutoff Dijkstra and its 10 extra gaps, H8 at the six B1 degrees, and `merge_cells([2,2])`. No other repo file modified. No git.
