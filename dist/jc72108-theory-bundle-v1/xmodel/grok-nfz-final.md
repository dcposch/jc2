**VERDICT: STILL-SHORT — the quoted CE is true and unconditional commutativity is correctly withdrawn; the SD-conditional exchange theorem is FALSE in the document’s own interleaved ladder: after the last skeleton death at θ* the live-factor-cap / μ-integrality boolean at the first free atom flips on equal-I tails (323=17·19 first vs later). REDUCED-WITH-PROVED-CORE-UNDER-SD is not earned; the result is not COMPILER-SUFFICIENT.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: round-3 `NF-Z.md` (status REDUCED-WITH-PROVED-CORE-UNDER-SD, post `xmodel/grok-nfz-rereview.md`).
Prior reviews: **NOT-PROVED** (`xmodel/grok-nfz-review.md`), **STILL-SHORT** (`xmodel/grok-nfz-rereview.md`). Authors claim the open core step resolved both ways: unconditional free-zone commutativity FALSE (own CE), commutativity PROVED under SD + `den(α_entry)|P_0`, SD on every filed packet, fail-closed ordered-free-zone fallback, NF-Z† policy.
Claims under final review: (1) verify `((5,3,7,11)` vs `(5,7,3,11)` at `P_0=30002`, `g=7/3`); (2) replay the SD field-by-field proof, hunt a consumed field the case split misses; (3) does the gate actually test SD on all packets, and is SD stable for td-11/13 or a td-7 artifact?; (4) fail-closed ordered-free-zone fallback sound as policy?; (5) is REDUCED-WITH-PROVED-CORE-UNDER-SD earned, and is the result COMPILER-SUFFICIENT (per-entry SD check + fail-closed + NF-Z† policy)?
Method: line-read of round-3 `NF-Z.md` against both prior reviews, `xmodel/sol-normalform.md` §§0–4 (fat record (1.2), NF-Z item 3, compiler rule 6), `xmodel/sol-td11-13-scope.md` §§2–3 (nine entry packets, A/B/C non-port), `TOWER-UNIFORM.md` + `TOWER-9-15.md` (Case-C menu, td-7 skeleton gaps), `cases/tower_check.py` Case-C derivation. `python3 cases/nfz_check.py`: exit 0, **39/39 PASS**. Independent exact `Fraction` replay of the quoted CE, of both prior-review lattices, of the interleaved td-7 register through `{X-scale, F1, F2, F3, F4, G}` then a free tail, and of every §3.1 packet against the written SD dens. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: break — Claim (2), and the “PROVED-CORE-UNDER-SD” half of the status. The field table’s cap / μ-recursion row is false in the interleaved ladder the document itself uses. Same-`I` free tails, under SD and entry compatibility, disagree on a Sol-item-3 live-factor-cap boolean.

- File: `NF-Z.md:211-246,248-294,267-268,279-294`; `cases/nfz_check.py:394-413,318-333`
- Claim: under SD and `den(α_entry)|P_0`, every CONS-consumed boolean on a legal single-word free tail is automatic or a function of `I`. Caps / aliveness are automatic by Lemma 4.2a (`k_j | P_j` along any order). The register is discharged by Lemma 4.2b (CONS reads it only as the next-death input or at a skeleton vertex; below `θ*` there is no skeleton).
- How checked.

  **Lemma 4.2a is a pure-word statement.** The induction is `den(α_entry)|P_0 ⇒ den(α_j)|P_{j-1}` and `k_j | P_j` along the word, with no intervening skeleton death. G7 tests exactly that (and the necessity witness `P_0=3, α=3/2, u=5, k=10 ∤ 15`). The table then applies 4.2a to free-tail caps *in the interleaved ladder*. That is the illicit step.

  **The free tail does not start from `α_entry`.** §3 threads the register in global gap order — the merge of the word’s `γ` sequence with the skeleton. `θ*` is the *minimum* skeleton competing gap, so the last pre-tail death is the skeleton vertex that attains `θ*`. Z1 gives `α_* = ℓ+1−θ*` after that death. For the td-7 direct skeleton, `θ* = 1/13566` and `17, 19 | 13566`. The numerator of `ℓ+1−1/13566` is `≡ −1 (mod 17)` and `(mod 19)`, so those primes **never cancel**: `17·19 | den(α_*)` after G, for every incoming register. Independently replayed on the real interleaving of `Z = (3,5,7,9,11)` at `P_0 = 2` with `{2/5, 1/34, 3/3230, 2/11305, 1/13566}`:

  ```
  last death G at 1/13566 → α_* has den 13566 = 2·3·7·17·19
  P after Z = 20790 = 2·3³·5·7·11     (no 17, no 19)
  ```

  The 4.2a hypothesis `den(α)|P` is therefore false at the free-zone boundary on the document’s own td-7 instance, *with SD and entry compatibility both holding*.

  **Same-`I` cap flip, exact `Fraction`.** When `Z` is nonempty the first free letter is *not* in `F` (head is stored only for entirely-free words, `NF-Z.md:127-130`). Cylinder class at `w=2` is “odd”. The tails

  | tail after `Z=(3,5,7,9,11)` | `Π_free` | end | classes | all-free | `k|P` per atom |
  |---|---:|---:|---|---|---|
  | `(323,13,15,17)` | 1070745 | 17 | all odd | yes | **`[T, T, T, T]`** (`k = 39270, …`) |
  | `(13,15,323,17)` | 1070745 | 17 | all odd | yes | **`[F, T, T, T]`** (`k = 87297210, …`) |

  are legal cylinder-(2.5) words (`323` odd, `2 | 324`, `gcd(2,323)=1`), lie entirely below `1/13566`, and have equal corrected `I` (same `τ`, same `Z`, same `u_r`, same `Π`, same `F`). The first-atom live-factor-cap boolean flips. The same flip fires for `(323,3,5,11)/(3,5,323,11)`, `(323,13,11)/(13,323,11)`, and 25 158 length-3/4 anagrams over `{3,5,…,29,323}` that share a multiset and an endpoint. Exhaustion over odds `3..29` *without* a `17·19` factor: 0 flips (both sides fail the first cap equally). The missing primes have to enter by a tail letter, and `F` does not record which letter is first.

  **This is Sol item 3, not an internal scratch value.** NF-Z item 3 (`sol-normalform.md:417-418`) demands *all* live-factor-cap predicates at every neutral vertex. CONS §0 names “aliveness with integral factor exponents” and “μ-recursion with `k_v = i_v(α−1) ∈ ℕ`”. The table’s own cap row is the consumer. The μ-boolean `P_j(α−1) ∈ ℕ` flips on the same pair (`True` after `×323`, `False` after `×13`). Lemma 4.2b cannot discharge a boolean the table listed as automatic and that Sol required as an output of the summary.

  **Why the gate is silent.** G3 runs `run_word` as a *pure* word from `α=3/2` (no skeleton) and checks only prefix-δ / descent. G7 refuses every seed with `P_0 % den(α) ≠ 0`, so it never sees a post-`θ*` register. G9’s coarse pair `(7,15,13)/(3,35,13)` does not carry `17·19`. Block E’s “automatic cap `k'|P_{j+1}`” is the *consecutive-word* Z2 identity, which does not apply to the first free death (that death follows a skeleton death, not a word death).

  **What the proof actually does.** Part (i) correctly retains the in-zone register as a function of `Z`. Part (ii) then quotes 4.2a as if the free tail inherited `den(α_*)|P`. It does not. SD kills the prefix-δ order-sensitivity (finding 2 of the last review, now a theorem plus CE). It does not kill cap / μ-integrality order-sensitivity at the `θ*` junction. That is a second consumed field, and it is the one the case split misses.

  This is why the core is not proved and the status is not earned. Findings 1–2 of the first review were folded in-zone, reopened below `θ*` as prefix-δ, and are now folded as prefix-δ under SD — and reopened again as caps at the same junction.

### 2. Severity: clear — Claim (3). G8 does not test SD on the filed packets. The written “lemma” that `den(g_top)|P_0` is weaker than the Case-C menu SD actually names. SD is structurally plausible on type-`(2,3)` inheritance and unproved on `(3,4)` / `(2,5)`.

- File: `NF-Z.md:33-39,332-347`; `cases/nfz_check.py:415-423`; `xmodel/sol-td11-13-scope.md:174-175,260-303`; `cases/tower_check.py:707-716`
- Claim: SD holds on every filed packet (td-7 menu `{1,3/2,2}`, type `(2,3)` even degrees, 13-2d `7/3` with `P_0∈{3,9}`, 11-B `7/2` with `P_0∈{2,6}`), “machine-checked (gate block G)”. The structural reason is `g_top=(α+β)/α` with `α | b·α = P_0`.
- How checked.

  **What G8 actually runs.** Four hardcoded divisibilities:

  ```
  dens({1,3/2,2}) | {2}
  2 | {2,4,6,10}
  3 | {3,9}
  2 | {2,6}
  ```

  It does not load `t9_15_direct.json`, does not walk the nine §3.1 rows, does not derive a prefix menu, and does not check `den(α_entry)|P_0` per packet. It is an inspection claim typed in as arithmetic, not a corpus gate.

  **The prefix menu is not the pole top.** td-7 Case C is the legal `(k,ℓ)` in the window `(gap(X), 5/2)` under the cap `k|2`:

  ```
  {(1,2),(2,3),(2,5)}  →  g = ℓ/k − 1/2 ∈ {3/2, 1, 2}
  ```

  (`tower_check.py:707-716`; `TOWER-UNIFORM.md:208-209`). Prefix-δ is evaluated at *those* gaps, on every created atom. `sol-td11-13-scope.md:174-175` says the displayed A/B/C (and that menu) is td-7-packet-specific: type `(2,5)`, type `(3,4)`, resonant X, or another cap “needs a new exhaustion.” The authors’ “`den(g_top)|P_0`” lemma is true and strictly weaker: `g_top` is one number, the menu is a finite set of `(k,ℓ)` gaps.

  **Packet-by-packet against the written dens** (`sol-td11-13-scope.md:292-302`):

  | ID | type | `[M@w;p]` | written SD check | actual menu | SD as defined |
  |---|---|---|---|---|---|
  | 11-A | `(2,3)` | `[1@2;2]+[2@3;4]` | `2\|{2,4}` | certified `{1,3/2,2}` on the local pair | **holds** (dens `{1,2}\|` even `P_0`) |
  | 11-C, 13-3, 13-4 | `(2,3)` | even `p` | same | inherit the td-7 local pair | **plausible** (same menu on that pair; nested hierarchies can change the clash, `sol-td11-13-scope.md:188-189`) |
  | 13-2a | `(2,3)` | `[1@2;2]+[5@8/5;10]` | `2\|{2,10}` | second seed `w=8/5` is not the td-7 packet | **unknown** (if the menu gains `8/5`, `5\|10` still holds; if it gains something else, not checked) |
  | 13-2b | `(2,3)` | `[2@3/2;4]+[3@7/3;6]` | `2\|{4,6}` | all off-axis; one seed is `(7/3,3)` | **unknown** |
  | 13-2c | `(2,3)` | `[2@3/2;4]+[1@6;2]` | `2\|{4,2}` | plus a `6→2` resonance | **plausible** on the `(3/2,2)` seed |
  | 13-2d | `(3,4)` | `[1@2;3]+[3@5/3;9]` | `3\|{3,9}` (= `den(7/3)`) | **uncomputed** `k\|3` exhaustion (`sol-td11-13-scope.md:378`) | **not tested** |
  | 11-B | `(2,5)` | `[1@3;2]+[3@4/3;6]` | `2\|{2,6}` (= `den(7/2)`) | **uncomputed** type-`(2,5)` exhaustion | **not tested** |

  Entry compatibility is worse: G8 never checks it. Lemma 4.2a’s own necessity witness is `P_0=3, α=3/2`. That is the shape of 13-2d’s first packet `[1@2;3]` *if* that packet inherited the td-7 `α_1=3/2` — and port obligation 1 of `sol-td11-13-scope.md:203-206` is exactly “do not infer `(k_0,ℓ_0), α_1` from type `(2,3)`.” Unknown, and not a gate row.

  **td-7 artifact or compiler-stable?** The *mechanism* (menu gaps are `ℓ/k+1−α` under a cap that shares prime factors with `P_0`) is not a td-7 accident; it is why `{1,3/2,2}` has dens `{1,2}` on every even type-`(2,3)` packet. That is the majority of the td-11/13 target (11-A/C, 13-2c/3/4, the local pair inside 13-2a). It is **not** a proof for 11-B or 13-2d, and G8 does not become one by writing the pole-top dens down. Finding 1 already shows that even on the packet where SD *does* hold (td-7, menu certified, `P_0=2`), SD is not a sufficient commutativity hypothesis. Stability of SD is therefore secondary: the compiler target’s best packet fails the theorem for a different field.

### 3. Severity: residual — Claim (4). Fail-closed + ordered free zone is the right Rule-6 policy for SD-fail *and* (now) for the cap hole. It is still not a check. Applying the commutative core on an SD-pass entry is the soundness channel.

- File: `NF-Z.md:40-48,322-330,381-414`; `xmodel/sol-normalform.md:728-731`
- Claim: entries failing SD keep an ordered free zone (equivalently `F` enriched by the ordered chain of prefix residues mod `lcm(menu dens)`) and stay fail-closed on the exact fat record. Multi-word deep coexistence is POLICY NF-Z† (default-deny, Sol rule 6), not a check. The commutative free zone is used only on SD-pass, single-word entries.
- How checked.

  **Policy for emptiness is still sound.** Rule 6: an open obligation may emit `OPEN` / a symbolic candidate; it may not certify an empty panel. Leaving SD-fail and multi-word entries on the fat record, and forbidding quotient-based emptiness there, is exactly that rule. The ordered-free-zone enrichment is the *right missing datum for prefix-δ* (an unbounded word over a finite residue alphabet). It does not by itself give a finite quotient, which is why fail-closed is required. That package is honest and is what the last review asked for on dagger.

  **It does not cover finding 1.** The missing datum for the cap boolean is not a prefix residue mod `lcm(menu dens)`. Menu dens for td-7 are `{1,2}`; the cap flip is mod `{17,19} =` the odd primes in `den(θ*)`. An SD-pass, single-word, type-`(2,3)` entry is exactly the case the architecture *uses the commutative core on*. That is a soundness hole, not an incompleteness: `I` is not a joint invariant of two legal free tails, and a compiler that trusts the theorem will identify them.

  **Silent loss remains a process risk.** Completeness of the finite quotient is lost on every FAIL, loudly, if FAIL is actually raised. It becomes silent when (1) the commutative core is applied to an entry whose free tails disagree on a Sol-item-3 boolean (finding 1 — this is now the live instance of last review’s soundness channel), (2) G8 is read as a universal SD PASS, (3) REDUCED-WITH-PROVED-CORE-UNDER-SD is read as ungating the neutral-word slice. §7 blocks (3) in prose (“only per entry where SD and single-word”). It cannot block (1) while the theorem is false.

  A compiler that implements default-deny on *any* free-zone identification — SD or not — and refuses empty-panel certificates on FAIL is sound and incomplete, loudly. That is a stricter policy than what is written, and it is the policy finding 1 forces.

### 4. Severity: residual — Claim (1) as an artifact, and the status label. The CE is true. The rest of the round-3 repair is real. The earned label is still REDUCED, not WITH-PROVED-CORE-UNDER-SD, and not COMPILER-SUFFICIENT.

- File: `NF-Z.md:1-56,200-246,449-478`; `cases/nfz_check.py` G4–G6
- Claim: unconditional commutativity FALSE; SD-core PROVED; status earned; 39 checks; compiler-sufficient via per-entry SD + fail-closed + NF-Z†.
- How checked.

  **Claim (1), independently replayed — true.**

  ```
  P_0 = 30002 (3 ∤ P_0), w = 2, g = 7/3, θ* = 1/13566:
    (5,3,7,11): all four gaps < θ*; prefix-δ [F,T,T,T]
    (5,7,3,11): all four gaps < θ*; prefix-δ [F,F,T,T]
  τ trivial, Z empty, head 5, endpoint 11, Π = 1155, classes (all odd).
  ```

  Both `D_f = w P_j` and `D_f = P_j` agree (`gcd(3,4)=1`). The last review’s lattice `(3,5,7)/(5,3,7)` at `g=7/3` is `[T,T,T]` vs `[F,T,T]` on `P_0 ∈ {2,4,8,30001,30002}` and both-pass at `P_0=30000`. The den-5 flip `g=8/5` at `P_0=2` distinguishes `(3,5,7)` from `(3,7,5)`. G6’s residue-class commutator (`d_eff ∈ {2,3,5}`: `d|P_0` forces constant-TRUE, `d ∤ P_0` admits a flip for every modulus) replays. Unconditional free-zone commutativity is FALSE. That half of round 3 is earned, and it is the first time the authors have found their own obstruction.

  **What otherwise folded**, and was independently replayed (unchanged from the last review, plus the new honest bits):

  *In-zone ordered `Z`.* Pair `(3,5,7,9)/(3,7,5,9)` at `P_0=2`: steps and `α_exit` match both prior reviews; `Z` separates at position 2. Interleaving with the td-7 skeleton still separates (this review’s register trace: after the common `u=3` at `2/3`, the two words are not even the object — the *new* object is a same-`Z` tail).
  *`θ* = min`.* `1/13566` vs WIN `2/5`; zone bound `20349`; Case A = pole-to-X `k'=2ν_X`.
  *Finite-state `σ` withdrawn; `τ` drop-values; CONS is a list; compiler gated on NF-P/M; sibling-`X` carved out; N1 imported; N4 is the `3/8` bound; 11-A `v_2`.*
  *NF-Z† is policy, not a check.* The “inspected corpus / `c_x` is a finite check” sentences are withdrawn. Correct.
  *Head in `F` for entirely-free words.* Necessary for E5F; does not save finding 1 (the flip is on a *tail* after nonempty `Z`).
  *Gate is 39/39, count printed.* Block D’s tautology is gone. G4–G6 contain the CE and the last review’s lattices.

  **The status that would be earned**, once finding 1 is a lemma (or the free zone is fail-closed even under SD) and finding 2 is a real menu-deriving gate row: **REDUCED-WITH-PROVED-IN-ZONE-CORE**, plus an honest SD-*necessary*-not-sufficient sentence. What is printed asserts that single-word CONS-completeness below `θ*` is a theorem under SD. It is not (finding 1). COMPILER-SUFFICIENT would additionally require that a per-entry SD check be a sound enablement of the commutative quotient. It is not: the enablement condition can hold and the identification is still wrong.

---

## Attack scorecard (this round)

| attack | result |
|---|---|
| (1) quoted CE `(5,3,7,11)` vs `(5,7,3,11)` at `P_0=30002`, `g=7/3` | **true.** `[F,T,T,T]` vs `[F,F,T,T]`; equal `I`; both all-free |
| (1b) last review’s `g=7/3` and `g=8/5` lattices | **true**, both normalizations |
| (1c) G6: `d\|P_0` ⇒ prefix-δ constant-TRUE | **true** on `d_eff ∈ {2,3,5}` |
| (2) SD-conditional field table complete | **no.** Cap / μ-integrality at the first free atom after the last skeleton death is order-sensitive under SD |
| (2b) Lemma 4.2a applies to interleaved free tails | **no.** Pure-word lemma; `17·19 \| den(α_*)` after G |
| (2c) same-`I` CONS-boolean hit under SD, on the td-7 packet | **yes.** `(323,13,15,17)` vs `(13,15,323,17)` after `Z=(3,5,7,9,11)` |
| (2d) 4.2b discharges the register | **values, if the booleans are automatic.** The booleans are not |
| (3) G8 tests SD on every filed packet | **no.** Four hardcoded dens; no menu derivation; no `den(α)\|P_0` |
| (3b) SD stable for td-11/13, or a td-7 artifact | **plausible on type `(2,3)` inheritance; unproved on 11-B / 13-2d.** Secondary: SD holds on td-7 and the theorem still fails |
| (4) fail-closed ordered-free-zone / NF-Z† sound for emptiness | **policy yes** (Rule 6). **Does not cover finding 1.** Commutative core on an SD-pass entry is the soundness channel |
| (5) REDUCED-WITH-PROVED-CORE-UNDER-SD earned | **no.** REDUCED yes; in-zone core yes; free-zone core under SD no |
| (5b) COMPILER-SUFFICIENT (per-entry SD + fail-closed + dagger) | **no.** SD-pass is not a sound enablement |
| `python3 cases/nfz_check.py` | exit 0, **39/39 PASS** (document matches) |
| Z1 / Z2 / Z3 / 11-A `v_2` / N2–N4 / Case A / `θ*` / `20349` | **still true** |

---

## What folded from `xmodel/grok-nfz-rereview.md`

| last review | this revision |
|---|---|
| 1. free-zone commutativity not a theorem; prefix-δ letter-locality false; same-`I` anagrams; unread-register is a slogan | **Prefix-δ half folded** by CE + SD. **Cap half reopened** as finding 1 here. 4.2b is now a CONS-list computation, but it rests on the false cap row |
| 2. NF-Z† is not a check; silent loss if the core is applied without default-deny | **Relabelled as policy.** Correct, and not enough (finding 3) |
| 3. “25 checks”; tautological monotone row; block E tests different endpoints; `F` has no composition law | **Folded as artifact.** 39 printed; D is real Z3; `F` has a written composition law; block E still uses `(3,5,7)/(7,5,3)` but G1/G3/G9 are the same-endpoint rows |
| 4. earned label is REDUCED, not WITH-PROVED-CORE | **Still.** The new suffix UNDER-SD does not make the free-zone half a theorem |

Last review’s repair bar for WITH-PROVED-CORE was: (i) prove every CONS predicate on `{γ<θ*}` is a function of `F` (in particular prefix-δ, *or* put the residues in `F` and drop “commutative”), (ii) put the same-endpoint anagrams and the den-3 lattice into the gate, (iii) replace NF-Z† with a default-deny algorithm that is a gate row, (iv) print 28. (ii) and the count are done (39). (iii) was correctly weakened to policy. (i) was done for prefix-δ and **not** for live-factor caps.

---

## What may be treated as proved, today

1. Z1, Z2 (consecutive *word* deaths in one run, including `k' ≥ uu' ≥ 4` and `k'|P_{j+1}`), Z3. Template `α_3 = 1003/42`. Gate block A.
2. The ordered interleaved-zone word `Z` of length `≤ L* = ⌊log2(3/(2θ* P_0))⌋+1` is a CONS-complete summary of everything at gaps `≥ θ*`. Concatenation by re-threshold is well-defined and associative on the scanned lattices.
3. `θ* = min` skeleton competing gap; td-7 direct instance `1/13566`; WIN ceiling `2/5` a distinct object; zone bound `20349`; Case A = pole-to-X `k'=2ν_X`.
4. Unconditional free-zone commutativity is **false**. The CE `(5,3,7,11)/(5,7,3,11)` at `P_0=30002`, `g=7/3`, and the last review’s den-3 / den-5 lattices, are theorems. SD is *necessary* for prefix-δ to be order-free. G6’s residue-class direction (`d|P_0 ⇒` constant-TRUE) is a theorem on the scanned moduli.
5. Non-ladder consumers (price 0, E5F equivalent to the pad closed form under the handshake, H8 reads `P_0 Π`, Z-Omega on clean-neutral rows only, `τ` as drop-value chain). Head must sit in `F` when `Z=∅`.
6. 11-A `v_2(2Π)=1` vs `≥3`; N2/N3/N4 *numbers*; CONS is a consumer list; compiler still gated on NF-P/M; sibling-`X` ties carved out; NF-Z† is Rule-6 policy, not a check.
7. Fail-closed + ordered free zone is the right *interface* for SD-fail and for multi-word residue. It is also, after finding 1, the right interface for SD-pass free tails, until the cap boolean is actually a function of `I`.

Everything else — CONS-complete free-zone summaries under SD, Lemma 4.2a as an interleaved statement, SD as a corpus theorem, ungating any compiler entry via a per-entry SD check — stays `OPEN`.

A fourth-round repair that would earn REDUCED-WITH-PROVED-CORE-UNDER-SD (and, with the existing fail-closed / dagger policy, COMPILER-SUFFICIENT) would have to (i) *prove* that every Sol-item-3 cap / μ-integrality boolean below `θ*` is a function of the written `F` in the *interleaved* ladder (in particular, put `P_j mod den(θ*)` — or the first free letter, or the ordered free word — into `I`, or fail-close the free zone even under SD), (ii) put the `(323,…)/(13,…,323,…)` pair and a post-skeleton 4.2a row into `nfz_check.py`, (iii) replace G8 with a menu-deriving per-entry check (Case-C analog, plus `den(α_entry)|P_0`) rather than four hardcoded dens, and (iv) keep the CE and the policy language, which are the parts of round 3 that survived.
