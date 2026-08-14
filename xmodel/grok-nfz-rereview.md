**VERDICT: STILL-SHORT — ordered `Z` and `θ* = min` fold findings 1–2 (pair separates at zone position 2; bound replays); the claimed commutative free zone is not a theorem, and that is where the second anagram lives; NF-Z† fail-closed is Rule-6-sound as policy and is not a check; REDUCED-WITH-PROVED-CORE is not earned.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: repaired `NF-Z.md` (status REDUCED-WITH-PROVED-CORE, post `xmodel/grok-nfz-review.md`).
Prior review: **NOT-PROVED**, findings 1–6. Authors claim all folded.
Claims under re-review: (1) the anagram pair `(3,5,7,9)` / `(3,7,5,9)` now SEPARATES under the ordered zone-word invariant (quoted replay: `α_exit = 1834803494/189` vs `2566192670/189`, separation at zone position 2); (2) `θ*` definition==use (min skeleton gap; td-7 value `1/13566`; zone bound `log2(20349/P_0)+1`); (3) the new architecture — ordered bounded interleaved zone + commutative free zone — is the free-zone commutativity claim PROVED, and if not, hunt a second anagram there; (4) NF-Z† as a per-entry finite check with FAIL-CLOSED semantics — is fail-closed genuinely sound for the compiler (no silent completeness loss)?; (5) is the status label REDUCED-WITH-PROVED-CORE earned?
Method: line-read of repaired `NF-Z.md` against the prior review, `xmodel/sol-normalform.md` §§0–4 (fat record (1.2), cylinder (2.5), NF-Z item 3, compiler rule 6), `TOWER-UNIFORM.md` + `TOWER-9-15.md` (td-7 skeleton gaps, pad-included prefix-δ, WIN), `xmodel/sol-td11-13-scope.md` §3 (entry packets and prefix menus). `python3 cases/nfz_check.py`: exit 0, **28/28 PASS** (the document still prints “25 checks”). Independent exact `Fraction` replay of the quoted pair, of the same pair interleaved with the td-7 direct skeleton, of the `θ*` / `20349` bound, and a free-zone anagram hunt. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: clear — Claim (3), and the “PROVED” half of the status. Free-zone commutativity is not a theorem. The second anagram lives there; the written reason it is harmless is a false letter-locality step plus a CONS-scope slogan.

- File: `NF-Z.md:94-98,157-193`; `cases/nfz_check.py:184-222`
- Claim: below `θ*` the letter action is commutative at the level of CONS. The invariant `F` keeps only “multiset-level exports” (product factor, letter-local congruence classes, endpoint if last). Caps are automatic; legality is letter-local (including “the finite-modulus residue conditions of the sub-`θ*` delta consumers”); the death-step register is CONS-unread because root-interior depth is residual. Equal `I` therefore still gives equal labels.
- How checked.

  **The second anagram, same `I`, different register.** Take the prior-review pair and push it under `θ*` by enlarging the poleward anchor, or keep the td-7 seed and append a free tail after an in-zone prefix.

  | pair | where | `Z` | `u_r` | `Π` | `F` (product, end, `u mod 2`) | `α_exit` |
  |---|---|---|---:|---:|---|---|
  | `(3,5,7,9)` vs `(3,7,5,9)` | `P_0 = 30000`, all four gaps `< 1/13566` | empty | 9 | 945 | `(945, 9, (1,1,1,1))` both | `160225018542337913710789949999/2835000` vs `11215751297330428730409149999/2835000` |
  | `(13,15,17)` vs `(15,13,17)` | after in-zone prefix `(3,5,7,9,11)` at `P_0 = 2` (`P = 20790 > 20349`) | `(3,5,7,9,11)` both | 17 | `20790 · 3315` | tail `(3315, 17, (1,1,1))` both | differ |

  These are exactly finding 1 of the last review, relocated below `θ*`. The ordered-zone repair does not touch them: `Z` agrees, `F` agrees, `τ` is the trivial `M = 1` ledger. Independent `run_word` produces different death-step tables and different `α`. The machine gate’s block E never tests a same-endpoint pair — it uses `(3,5,7)` vs `(7,5,3)` and then a separate check that the endpoints differ.

  **A coarser collision, not even an anagram.** `F` as specified (product + endpoint + letter-local classes) is coarser than a multiset of letters. At `w = 2` the cylinder class is “odd”, so

  ```
  (7,15,13)  and  (3,35,13)     Π = 1365, u_r = 13, classes (1,1,1)
  (5,21,13)  and  (3,35,13)     same
  (9,5,7)    and  (3,15,7)      Π = 315,  u_r = 7,  classes (1,1,1)
  ```

  are identified by `F` at `P_0 = 30000` (all free-zone, all legal odd letters). Distinct factorizations, distinct intermediate gaps and degrees, same written free-zone summary.

  **The letter-local step is false for prefix-δ.** Sol’s NF-Z item 3 (`sol-normalform.md:417-418`) and the fat-record tower consumer (`Θ` stores every atom’s gap / cap / prefix-δ; TOWER-UNIFORM includes every witness vertex in those loops) evaluate prefix-δ integrality `D_f · g − κ̄ ∈ ℕ` at every created atom, including free-zone pads, at the entry’s prefix-menu gaps `g`. That is a residue condition on the *ordered prefix product* `P_j`, not on a letter. Concrete hit, exact `Fraction`:

  ```
  prefix-δ at g = 7/3, w = 2 (κ̄ = 2(u+1)):
    (3,5,7) vs (5,3,7)
      P0 ∈ {2,4,8,30001,30002}:  [T,T,T] vs [F,T,T]
      P0 = 30000 (3 | P0):       [T,T,T] vs [T,T,T]   # collision, both pass
  ```

  At `P_0 = 30001` both words are free-zone (`4/90003` and `6/150005` are `< 1/13566`) and have the same `F`, and one word’s first atom fails a den-3 prefix-δ that the other passes. The same shape fires at any menu gap whose denominator does not already divide `P_0` (e.g. `g = 8/5` distinguishes `(3,5,7)` from `(3,7,5)` at `P_0 = 2`).

  This is *not* a td-7 boolean hit: the promoted Case-C menu is `{3/2, 1, 2}`, denominators `{2,1,1}`, and `P_0 = 2` makes every free-zone atom pass. Several other filed packets likewise have `P_0` divisible by the denominators that their pole-top / window arithmetic would suggest (`(3,4)` carries `P_0 ∈ {3,9}`; type `(2,3)` carries even `P_0`). So the hunt did **not** produce a CONS-boolean counterexample against a named promoted entry. It produced (i) same-`I` / different-register pairs, and (ii) a proof obligation the text discharges with a false lemma.

  **What the proof actually does.** §4(ii) is four sentences: no skeleton below `θ*` (true by definition); `k' | P_{j+1}` (true, Z2, independently replayed, 0 failures); “letter-local congruences” including sub-`θ*` delta consumers (false as stated); register unread because “root-interior depth is residual” (a CONS-scope slogan, load-bearing, and a conflation — free-zone *word* atoms are padding on the chain, not the root chart). CONS as listed in §0 still names death gaps, delta descent, death equations, and `μ`-recursion. The residual sentence is the only thing standing between the pairs above and a replay of finding 1. It is not a computation that `F` determines those predicates, and block E does not check them.

  Sol item 3 asked for every tower-gap / cap / prefix-δ predicate at every neutral vertex, “not merely their maximum under a td-7 window.” The free-zone half of `I` is a max-gap-style projection (product + endpoint + coarse classes) on an unbounded tail. That is legal only after a lemma that every CONS predicate on that tail is automatic or a function of `F`. Caps are automatic. WIN / N4 comparisons are automatic (`γ < θ* ≪ 2/5`). Prefix-δ and the exact gap / exponent atoms are not, except on entries whose menu denominators already divide the in-zone scale — a lemma that is true on some filed packets, unstated, and not what §4 writes.

  This is why the core is not proved and the status is not earned. Findings 1–2 of the last review are not “the same break still open”; they are folded in-zone and reopened below `θ*` by an unproved collapse.

### 2. Severity: clear — Claim (4). Fail-closed is the right Rule-6 policy. It is not a finite check, and it is the channel for silent loss.

- File: `NF-Z.md:226-250,261-265`; `xmodel/sol-normalform.md:728-731`; `cases/nfz_check.py` (no dagger block)
- Claim: for a fixed entry, compute a cross-branch deep cap `c_x`; if the constraint system forces `k' ≤ c_x < u u'` for every consecutive deep pair, deep zones decouple-or-die and NF-Z closes; otherwise the entry stays on the exact fat record (fail-closed, Sol interface rule 6) and “no emptiness certificate may use the quotient there.” The check is finite. On every inspected promoted configuration the coupling resolved as kills.
- How checked.

  **The policy is sound for emptiness.** Sol rule 6: a run with an open obligation may emit `OPEN` / a symbolic candidate; it may **not** certify an empty panel. Leaving failed entries on the fat record, and forbidding quotient-based emptiness there, is exactly that rule. A FAIL cannot silently produce a false empty-panel certificate *if the FAIL is actually raised*.

  **It is not a check.** `c_x :=` “gcd-bound exported by each branch’s rootward exponents to the other branches’ sub-`θ*` deaths” is not an algorithm: which exponents, which gcd, over which word tails (unbounded), against which live-factor consumers. The only written success path is the td-7-shaped uniform kill `c_x < 4 ≤ u u'`. There is no “coupling is a function of `F`” success path, which is conservative (more FAILs) and does not make the PASS side well-defined. Nothing in `nfz_check.py` implements dagger. The sentence “on every configuration inspected in the promoted corpus (td-7 direct/trunk, the 16 uniform cells, 11-A) the deep coupling resolved as kills” is an inspection claim with no lattice, no log, and no gate row.

  **Silent loss is a process risk, not a math bug in the policy.** Completeness of the *finite* quotient is lost on every FAIL — words remain an unbounded cylinder, the enumerator does not terminate, emptiness cannot be certified via `I`. That loss is supposed to be loud (`NEEDS_NF_Z` / `OPEN`). It becomes silent when

  1. the check is not run and the “PROVED” single-word core is applied to an entry that has two deep words (that is a *soundness* hole: the core’s hypothesis is false and `F` is not a joint invariant of two interleaved free tails);
  2. the unmachine-checked “inspected corpus” sentence is read as a universal PASS;
  3. REDUCED-WITH-PROVED-CORE is read as ungating the neutral-word slice of the compiler.

  §7 tries to block (3) (“only per-entry where NF-Z† checks”). It cannot block (1)–(2) without an executable default-deny check. Fail-closed that is not wired is default-open.

  A compiler that implements the sketch as default-deny and refuses empty-panel certificates on FAIL is sound and incomplete, loudly. That is not what is in the repo, and it is not a proof that dagger is a “per-entry finite check.”

### 3. Severity: erratum — Claim (5) as a label, and the artifact. Findings 1–2, 4–6 of the last review are otherwise folded; the gate is 28/28, not 25; two written checks are vacuous or off-target.

- File: `NF-Z.md:1-27,279-294`; `cases/nfz_check.py:125-133,179-182,187-202`
- Claim: all three breaks repaired; machine gate “25 checks, exit 0”; block E demonstrates free-zone order-freeness; composition is associative; status earned.
- How checked.

  **What did fold, and was independently replayed.**

  *Finding 1, in-zone.* Quoted table matches exactly:

  ```
  (3,5,7,9): (6,7),(15,98),(105,10273),(945,9707954),  α_exit = 1834803494/189
  (3,7,5,9): (6,7),(21,137),(105,14368),(945,13577738), α_exit = 2566192670/189
  ```

  At td-7 `θ* = 1/13566` every letter of both words is in-zone (`1/189 > 1/13566`), so `Z = (3,5,7,9)` vs `(3,7,5,9)`, first difference at position 2. The fifth pair `(3,5,7)` vs `(5,3,7)` is likewise split by `Z` (`2/3` vs `3/5`). The letter action is non-commutative on `(α, ℓ')`; that is now the content of `Z`, not a defect.

  The quoted `α` values are the *pure-word* replay (no skeleton deaths), same as last review. Interleaving the td-7 direct skeleton `{2/5, 1/34, 3/3230, 2/11305, 1/13566}` makes the split louder, not quieter: after the common prefix `(X = 3, F1 = 2/5)`,

  | word | next word gaps vs `F2 = 1/34` | `α` at `F2` |
  |---|---|---|
  | `(3,5,7,9)` | `1/5` and `4/105 > 1/34` die *before* `F2` | `6421365119/34` |
  | `(3,7,5,9)` | `4/21 > 1/34`, then `1/35 < 1/34` dies *after* `F2` | `256909031/34` |

  Equal `Z` would have forced equal interleaving with a fixed skeleton; unequal `Z` is exactly the missing coordinate. This is the repaired completeness mechanism *above* `θ*`, and it works.

  *Finding 2.* `θ* := min` skeleton competing gap is now both the definition and the td-7 instance: `min{2/5, 1/34, 3/3230, 2/11305, 1/13566} = 1/13566` (`TOWER-9-15.md` vertex `G`). The `2/5` object is named WIN ceiling and is used only in §5 kill arithmetic. Case A is restored to the pole-to-X identity `k' = 2 ν_X`, `ℓ/k = (2u+1)/(2u)`, not the word–word corollary. N1 is imported; N4 is the absolute `3/8` bound, not Z3. Independently: `3/(2θ*) = 20349`; `γ ≥ θ*` forces `P_{prev} ≤ (u+1)/(θ* u) ≤ 3/(2θ*)`; the necessary condition holds on a `u = 2..79`, `P = 1..24999` scan; at `P_{prev} = 20349` only `u = 2` remains in-zone (`γ = 1/13566`); at `20350` the zone is empty. `L* = ⌊log2(20349/P_0)⌋ + 1` is `14, 13, 12` at `P_0 = 2, 4, 8`. Trunk vertex `T` at `1/158270 < 1/13566` (`TOWER-9-15.md:446`) is a *different* skeleton; the document’s instance is scoped to the direct route and is correct for that skeleton.

  *Finding 3.* Finite-state `σ` is withdrawn. The finite object is the schema set (ledgers × zone-shapes of length `≤ L*` × residue domains) with `Z`’s letters, `u_r`, `Π` as exact symbolic parameters. That is Sol’s demanded *shape*. The register is admitted integer-valued and unbounded. This is the right response to last review’s finding 3; it does not by itself make `F` a complete deep-zone coordinate (finding 1 of *this* review).

  *Findings 4–5.* CONS is named as a consumer list, not the promoted kernel. WIN and St 8.3(i)+Not 4.1 are added; sibling-`X` ties stay carved out. Compiler remains gated on NF-P/M. N1–N4 and the 11-A `v_2` certificate are attributed the way last review required. Block F replays those numbers.

  *Finding 6.* `nfz_check.py` exists. E5F is “equivalent under the pad handshake,” not “verbatim.” Z-Omega is scoped to clean-neutral rows. `τ` is the drop-value chain.

  **What the artifact still gets wrong.**

  | written | actual |
  |---|---|
  | “25 checks” (`NF-Z.md:25,280`) | **28** `check()` calls, 28/28 PASS, exit 0 |
  | block D “monotonicity” | `all(γ < θ or True for …)` is a tautology; real monotonicity is Z3 (`γ_{j+1}/γ_j ≤ 1/2`) and holds |
  | block E “free-zone anagrams have equal exports” | endpoints differ (`7` vs `3`); the same-endpoint pair that would test commutativity is not in the gate |
  | “concatenation is closed (§2)” | §2 specifies `Z(W_L · W_R) = Z(W_L) · rethreshold(Z(W_R), P_0 Π_L)` (associative on an 81-word extra lattice, and on the gate’s sample). `F` has no composition law |
  | free-zone schema finiteness | an unbounded multiset of classes is not a finite schema family unless `F` is further quotiented to a symbolic `(Π_free, class-counts or product residues, endpoint)`. That quotient is implied by the prose and not written |

  These would be editorial if finding 1 of this review were closed. They are load-bearing while commutativity is the open core step: the gate does not test the claim it is cited for.

### 4. Severity: residual — Claim (5). The status that *would* be earned, once finding 1 is a lemma and finding 2 is a gate row.

- What is actually on the page is: a proved in-zone quotient (ordered `Z`, length `≤ L*`, concatenation by re-threshold), proved Z1–Z3, a correctly renamed `θ*`, honest CONS / compiler relativity, and an identified multi-word residue. That is a real reduction from last review’s NOT-PROVED. It is **REDUCED**. The suffix **WITH-PROVED-CORE** asserts that single-word CONS-completeness — including the free-zone half — is a theorem. It is not (finding 1), and the residue is not a check (finding 2). The earned label is **REDUCED**, or **REDUCED-WITH-PROVED-IN-ZONE-CORE**, not what is printed.

---

## Attack scorecard (this round)

| attack | result |
|---|---|
| (1) quoted pair `α_exit` values | **true.** `1834803494/189` vs `2566192670/189`; steps match the last review’s table |
| (1b) pair now separates under ordered `Z` | **true.** At `θ* = 1/13566` both words are entirely in-zone; first difference at position 2 (`5` vs `7`) |
| (1c) interleaving with the td-7 skeleton still separates | **true**, and the `F2 = 1/34` slot sees different in-zone prefixes |
| (2) `θ*` definition == td-7 instance | **true.** `min = 1/13566`, WIN ceiling `2/5` is a different object |
| (2b) zone bound `log2(20349/P_0)+1` | **true.** `3/(2θ*) = 20349`; necessary condition holds; `L*(P_0=2) = 14` |
| (3) free-zone commutativity proved | **no.** Same-`I` anagrams and same-`F` distinct factorizations exist; letter-locality of prefix-δ is false; unread-register is a CONS slogan |
| (3b) a CONS-boolean hit on a named promoted entry | **not found.** td-7 menu dens divide `P_0`; several other packets look the same. The hole is a missing lemma, not a named-entry refutation |
| (4) NF-Z† fail-closed sound for emptiness | **policy yes** (Sol rule 6). **Not a check.** Silent loss if the core is applied without a default-deny run |
| (5) REDUCED-WITH-PROVED-CORE earned | **no.** REDUCED yes; PROVED-CORE no |
| `python3 cases/nfz_check.py` | exit 0, **28/28 PASS** (document: 25) |
| Z1 / Z2 / Z3 / 11-A `v_2` / N2–N4 / Case A | **still true** (gate blocks A, F; unchanged content) |

---

## What folded from `xmodel/grok-nfz-review.md`

| last review | this revision |
|---|---|
| 1. deep anagrams collide under written `I`; `α_exit` is not a function of `(u_r, Π)` | **Folded above `θ*`** by putting the ordered zone word in `I`. **Reopened below `θ*`** as finding 1 here |
| 2. `θ` defined as min, instantiated as WIN max `2/5` | **Folded.** One definition, one instance, WIN renamed, Case A restored |
| 3. `σ` is a state, invoked as a monoid, computes neither `k'` nor `ℓ'` | **Folded** by withdrawal. Schema-set finiteness is the right shape; `F` does not inherit a completeness theorem |
| 4. CONS ≠ promoted kernel; compiler still gated on NF-P/M | **Folded** in §0 and §7 |
| 5. N1–N4 not exact restatements; corollary is not the td-7 kill | **Folded** in §5 |
| 6. no `nfz_check.py`; “verbatim” / blanket Z-Omega / `τ`-positions | **Mostly folded.** Gate exists (28/28). Residual artifact issues in finding 3 |

Last review’s repair bar was: (i) put the `ℓ'` register or the ordered death-step word into `I`, *or prove it is a function of the existing fields*; (ii) one `θ`; (iii) a modulus that computes every CONS predicate, or stop claiming one; (iv) honest relativity. (ii)–(iv) are done. (i) is done in the interleaved zone and is an assertion, not a proof, in the free zone.

---

## What may be treated as proved, today

1. Z1, Z2 (including `k' ≥ u u' ≥ 4` and `k' | P_{j+1}`), Z3. Template `α_3 = 1003/42`. Gate block A.
2. The ordered interleaved-zone word `Z` of length `≤ L* = ⌊log2(3/(2θ* P_0))⌋ + 1` is a CONS-complete summary of everything at gaps `≥ θ*`: equal `Z` implies equal interleaving with a fixed skeleton, equal register through that range, equal `α` at every skeleton vertex. The pair `(3,5,7,9)` / `(3,7,5,9)` is the separating example. Concatenation of `Z` by re-threshold is well-defined and associative on the scanned lattices.
3. `θ* = min` skeleton competing gap, td-7 direct instance `1/13566`, WIN ceiling `2/5` a distinct object, zone bound `20349`, Case A = pole-to-X `k' = 2ν_X`.
4. Non-ladder consumers (price 0, E5F equivalent to the pad closed form under the handshake, H8 reads `P_0 Π`, Z-Omega on clean-neutral rows only, `τ` as drop-value chain).
5. 11-A `v_2(2Π) = 1` vs `≥ 3`; N2/N3/N4 *numbers*; CONS is a consumer list; compiler still gated on NF-P/M; sibling-`X` ties carved out.
6. Fail-closed + Sol rule 6 is the right *interface* for any multi-word residue. The residue itself is not proved and not gated.

Everything else — CONS-complete free-zone summaries, a lemma that prefix-δ / gap / exponent atoms below `θ*` are functions of `F`, an executable NF-Z† check, ungating any compiler entry — stays `OPEN`.

A third-round repair that would earn REDUCED-WITH-PROVED-CORE would have to (i) *prove* that every CONS predicate on `{γ < θ*}` is a function of the written `F` (in particular, that every prefix-δ denominator in CONS already divides the in-zone scale, or else put the necessary prefix residues into `F` and drop “commutative”), (ii) put the same-endpoint free-zone anagrams and the den-3 prefix-δ lattice into `nfz_check.py`, (iii) replace NF-Z† with a default-deny algorithm that is a gate row, and (iv) print 28.
