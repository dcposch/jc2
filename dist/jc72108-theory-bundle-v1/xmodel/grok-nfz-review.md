**VERDICT: NOT-PROVED — Z1/Z2 and the 11-A v₂ arithmetic stand; CONS-relative completeness does not. Same-I deep anagrams export different α; θ is defined as a min and instantiated as a max; the written σ is a state, not a monoid element. Status PROVED-RELATIVE is not earned.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `NF-Z.md` (neutral-word future quotient, claimed PROVED-RELATIVE to CONS).
Claims under review: (1) the quotient invariants `I = (τ, W_θ, u_r, Π, σ)` determine a neutral word's effect on the fat Markov record — completeness relative to CONS; (2) finiteness of the quotient for fixed entry data; (3) the core identities — α-exit `α_next = ℓ+1-γ`, the difference-denominator lemma (`k' = den(γ-difference)`, pairwise exit-denominator cancellation, `k ≥ u_j u_{j+1} ≥ 4` vs caps), forced ordered word-deaths; (4) the COROLLARY neutral-depth rigidity (`c_0 < 4` makes window-zone words tower-dead outright), with td-7 N1–N4 and the 11-A v₂ certificate as specializations — both must reproduce the promoted statements exactly; (5) relativity — is CONS exactly the promoted kernel, and does any td-11/13 census step consume something outside CONS (which would make PROVED-RELATIVE insufficient for the compiler)?
Method: line-read of `NF-Z.md` against `xmodel/sol-normalform.md` §§0–4 (fat record (1.2), cylinder (2.5), NF-Z statement, 11-A §4.3), `xmodel/grok-normalform-review.md` (fifth pair, ν=1, why fat-state enumeration cannot certify emptiness), `TOWER-UNIFORM.md` + `TOWER-9-15.md` N1–N4, `xmodel/sol-td11-13-scope.md` §§1–3 (census steps and portable kernels), `SHEET6-TEMPLATE.md` / `cases/tower_check.py` C2 and C3-N, certificate T1 rows in `cases/towers/t9_15_direct.json` and `TOWER-25-35.md`. No `nfz_check.py` exists; the three “machine-verified” identities were reconstructed in exact `Fraction` and rerun, together with `python3 cases/tower_check.py` (exit 0, `UNIFORM (17 cells): THEOREM`). No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: break — Claim (1). Completeness is false for the written `I`. Deep-zone anagrams with identical invariants export different `α` and different death-step sequences.

- File: `NF-Z.md:82-119,143-234`
- Claim: two neutral words with equal `I` (same ledger, same window-zone schema and parameters, same endpoint `u_r`, same symbolic product `Π`, same interface-monoid element) have identical labelled CONS futures. In particular the exported interface is `α_exit = ℓ'_r + 1 − γ_r`, “a function of `(u_r, Π)` — already invariants.”
- How checked.

  **Z1 does not make `α_exit` a function of `(u_r, Π)`.** The closed form is `α_next = ℓ' + 1 − γ`. Here `γ_r = (u_r+1)/(P_0 Π)` is indeed a function of `(u_r, Π)`, but `ℓ'_r` is the numerator of the *death step* at the last word vertex. Z2 itself gives the recurrence

  ```
  ℓ''/k'' = (γ' − γ) + ℓ' ,
  ```

  so `ℓ''` depends on the previous `ℓ'`. The previous `ℓ'` depends on the previous gap, and so on. The product `Π` and the last letter do not determine the ordered gap sequence, hence do not determine `ℓ'_r`.

  **Concrete pair.** At the td-7 / 11-A chain-1 seed `w = 2`, `P_0 = 2`, `θ = 2/5` as the document instantiates it:

  | word | `W_θ` | `u_r` | `Π` | `τ` | gaps | death-step `(k,ℓ)` after the pole | `α_exit` |
  |---|---|---:|---:|---|---|---|---|
  | `(3,5,7,9)` | one letter `u=3`, gap `2/3` | 9 | 945 | `M ≡ 1` | `2/3, 1/5, 4/105, 10/1890` | `(6,7), (15,98), (105,10273), (945,9707954)` | `1834803494/189` |
  | `(3,7,5,9)` | one letter `u=3`, gap `2/3` | 9 | 945 | `M ≡ 1` | `2/3, 4/21, 1/35, 10/1890` | `(6,7), (21,137), (105,14368), (945,13577738)` | `2566192670/189` |

  Written `I` agrees (window letter, endpoint, product, trivial ledger). The fifth-pair obstruction of `grok-normalform-review.md` finding 1 is *not* this pair — `(3,5,7)` vs `(5,3,7)` is correctly split by `W_θ` (`2/3` vs `3/5`). Same-window-prefix *deep anagrams* are not split. `σ` as defined in §2 is residues of `(previous letter, running product)` plus ledger position at the *end* of the word: previous letter is `u_r = 9` and the product is `945` on both sides, so the written state is the same. The theorem’s later phrase “interface-monoid element” is a different object and is not what §2 puts in `I` (finding 3).

  Independent exact replay of the recurrence, starting from the pole packet `(k_0,ℓ_0)=(2,3)`, `α_1 = 3/2` (the only packet the document uses for its running example): first death at `γ = 2/3` has `ℓ/k = 2/3 + 3/2 − 1 = 7/6`, then Z2 produces the table above. `α_exit` differs. The same split appears for `(3,5,7,11)` vs `(3,7,5,11)`, `(3,5,7,9,11)` vs `(3,7,5,9,11)`, and `(3,5,11,7)` vs `(3,11,5,7)`.

  **Why this is a CONS-visible difference, not an internal scratch value.** CONS includes mu-recursion and death equations (`NF-Z.md:48-56,277-279`). The α entering the post-word context is exactly the “exported interface” the proof names. Different `α_exit` changes every later `k_v = i_v(α − 1)` and every later death equation. Intermediate death steps `(k_j,ℓ_j)` are themselves the global ladder — Sol’s NF-Z item 3 asked for every tower-gap / cap / prefix-δ *predicate* at every neutral vertex, and the fat-record tower consumer evaluates N4 gaps, prefix-δ, and live-factor caps at every created atom (`sol-normalform.md:166-170`; `TOWER-UNIFORM.md` “pad vertices included in the max-gap/prefix-delta loops”).

  **What the proof actually does.** §1 is a field-touch table (correct as a retention audit, not a quotient). §3 is unconditional for price/E5F/H8/`M`/Z-Omega and is fine. §4 asserts that (Z1)–(Z3) collapse deep atoms to `I`. The collapse step for the exported α is a false function-of claim. No other invariant in `I` stores the ordered deep-gap path or the `ℓ'` register.

  This is why the status cannot be PROVED-RELATIVE. The identities can be true (they are) and the quotient still fails to be a CONS-complete summary.

### 2. Severity: break — Claims (1) and (4). `θ` is defined as the *smallest* competing gap and instantiated as td-7’s *largest* non-X competing gap `2/5`. The two readings are incompatible; each one kills a different load-bearing sentence.

- File: `NF-Z.md:102-103,182-190,236-265`
- Claim: `θ` is “the smallest death gap of any non-word competing vertex, td-7 instance: `2/5`.” Window-zone letters are those with `(u_j+1)/P_j ≥ θ`. Consecutive *word* deaths obey the Z2 word formula, occur in word order, and (corollary) face the small other-branch cap `c_0`.
- How checked.

  **What `2/5` actually is.** `TOWER-UNIFORM.md` Lemma WIN: every budget-admissible competing vertex *other than the poles and X* has death gap `≤ 2/5`, and `2/5` is attained by first-charged `(C)`. So `2/5` is the *maximum* non-X competing gap, not the smallest. Deeper skeleton vertices (F1 after insertions, F2, terminals, …) have strictly smaller gaps. The framed table’s `maxgap` column is this same `2/5` / `5/14` ceiling.

  **Reading A — believe the definition (`θ = min` skeleton gap).** Then the td-7 instance is false (`θ` is tiny, not `2/5`), and the §5 claim “`W_θ`-schema at `θ = 2/5` with zone length 1” is false: every letter with gap above the deepest skeleton gap is window-zone, so zone length is not 1. The X-family is not “the” window schema.

  **Reading B — believe the instance (`θ = 2/5 =` WIN ceiling).** Then zone length 1 at `P_0 = 2` is correct (independent check: first letter `u ≥ 2` has gap `(u+1)/(2u) ≥ 1/2 > 2/5`; the second letter has gap ratio `≤ 1/2`, hence gap `≤ 3/8 < 2/5`, so it is deep). But then the deep zone still contains skeleton vertices (first-charged at `2/5`, everything below it). Consecutive *word* deaths are not consecutive *ladder* deaths: the first-charged death sits between X (`~2/3`) and the first deep letter (`≤ 3/8`). Z2’s word formula `γ_{j+1} − γ_j = (1 − u_j u_{j+1})/P_{j+1}` and the bound `k' ≥ u_j u_{j+1} ≥ 4` are for consecutive word deaths *as ladder levels*. They do not apply across an intervening skeleton death. Deep-zone “faces only congruences, not small-`i` caps” is also false on this reading: a level dying at a deep word vertex is still alive at every larger-gap skeleton vertex that has not yet died, including any charged vertex with gap in `(γ_deep, θ)`.

  **The corollary is not the td-7 kill.** Case A of the promoted three-case exhaustion is the *pole→X* death, not a word→word death. Exact replay: after `(k_0,ℓ_0)=(2,3)`, `α_1=3/2`,

  ```
  ℓ'/k' = (u+1)/(2u) + 3/2 − 1 = (2u+1)/(2u),    k' = 2u = 2 ν_X
  ```

  for every `u = 2..14`. That is the promoted “`k_1 = 2 ν_X > 2`” line. The corollary’s `k'_{j+1} ≥ u_j u_{j+1} ≥ 4` vs `c_0 = 2` is a different identity, about a second window-zone word death that the geometric decay at `θ = 2/5` already forbids (zone length 1). §5’s sentence “the kill’s `u_j u_{j+1} ≤ c_0 = 2 < 4` instance is the corollary” misidentifies the mechanism.

  There is no repair that keeps both the td-7 specialization *and* the no-intervening-skeleton half of §4. This is independent of finding 1 and already stops the ladder-completeness argument.

### 3. Severity: break — Claim (1). `σ` is defined as a finite *state* and invoked as a *monoid element*. Neither object, as written, computes `k'` or `ℓ'`. The explicit modulus `m*` is not a consumer-complete interface.

- File: `NF-Z.md:94-110,201-219,290-297`
- Claim: every deep-zone integrality/cap condition “reads only: the previous letter’s residues mod `m*`, the running product’s residues mod `m*`, and the ledger position.” That data is `σ`, size `≤ (m*)² · |divisor poset of M_0|`. The word’s deep-zone effect is an element of the finite transition monoid those letters generate. If a computed `m*` failed to stabilize the congruence moduli, the entry degrades fail-closed — “excluded by the explicit modulus formula.”
- How checked.

  **State vs element.** §2’s tuple puts `σ` equal to the interface *state*. The theorem quotes the *monoid element*. These are not interchangeable: many words induce different transformations (or different paths) that send one start state to the same end state. Finding 1’s anagrams are exactly such a pair for the written state. A transformation-monoid element is finite (`|Q|^|Q|` functions on a finite `Q`) and would distinguish some anagrams, but it still does not store `α` or the exact death-step numerators — those are rationals, not residues.

  **`k'` is not a residue.** Z2 gives `k'_{j+1} = P_{j+1} / gcd(u_j u_{j+1} − 1, P_{j+1})`. `P_{j+1} = P_0 Π_{j+1}` carries arbitrary prime factors from unbounded letters. `m*` is a single entry-computable integer (`lcm(d, a, divisors of M_0, den(ρ_x), c_x, P_0)`). Residues of `(u_j, Π)` modulo a fixed `m*` do not determine `gcd(u_j u_{j+1}−1, P_{j+1})` once a prime `p ∤ m*` divides an earlier letter. The cap test `k' | c_x` is therefore not a finite-modulus condition on the written state. The document’s own “not observed in any inspected instance, and excluded by the explicit modulus formula” is circular: the formula is what is in question, and there is no inspected-instance log (finding 6).

  **`m*` misses ladder-prefix denominators.** Prefix-δ at `g ∈ {3/2, 1, 2}` (td-7) or at the type-`(3,4)` / `(2,5)` pole tops `7/3`, `7/2` (`sol-td11-13-scope.md:262-303`) is a residue condition on `P_j` modulo `den(g)`. Those denominators are not in the printed `m*` list unless they happen to already divide `a`, `d`, or `P_0`. Fail-closed is the right policy; “excluded by the formula” is not a proof that the formula is complete.

  Sol’s NF-Z (`sol-normalform.md:407-425`) required the monoid to be *exhibited* and proved closed. What is written is a state-space sketch plus “closure of residue arithmetic mod `m*`.” That is the right *shape*, not an exhibition, and the state space as specified does not carry the consumer (finding 1).

### 4. Severity: clear — Claim (5). CONS is not the promoted kernel. PROVED-RELATIVE, even if it had closed, does not ungate the td-11/13 compiler. No census step was found that reads a *new kind* of neutral-word field outside CONS; the 11-A loud object is not a neutral word.

- File: `NF-Z.md:48-56,275-285`; `xmodel/sol-normalform.md:86-178,407-425`; `xmodel/sol-td11-13-scope.md:1-8,60-117,158-256,334-355`; `TOWER-UNIFORM.md:46-58`; `xmodel/grok-normalform-review.md:138-167`
- Claim: the theorem is relative to CONS, enumerated as Sol’s fat-record §1.2 checklist plus the TOWER-UNIFORM ladder calculus (Prop 4.2, Prop 8.1(i)–(v), Cor 6.1, St 3.9/3.17(i)/3.11(i), E5F, H8, N1–N4, P0/P1). A future consumer outside CONS re-opens the §1 audit.
- How checked.

  **CONS is a consumer list, not a kernel.** The promoted *kernel* in `sol-td11-13-scope.md:165-175` is the td-agnostic column: L-A’s `M=1` uncharged, `M=1` absorption, tower-N1, N4’s gap formula, base E5F, N2’s gcd identity, N3’s cap-intersection principle. Those are proved lemmas. CONS is the list of predicates that *read* a word. Identifying them is a type error. CONS as written is essentially the fat-record §1.2 consumers plus the ladder predicates; that is a fair *consumer* description and is *not* “exactly the promoted kernel.”

  Gaps vs the TOWER-UNIFORM trust set: H5a Q+E5 is present only via E5F; St 8.3(i)+Not 4.1 (single global ladder, ties) is not named; BOOK R1.0–R2.2 is present only as P0/P1; WIN is not named in §0 and is only implicit in “death gaps.” Simultaneous deaths (13-4 sibling X ties, `sol-td11-13-scope.md:385-390`) are unhandled.

  **Compiler gate.** `sol-normalform.md` STATUS and `notes.md:450-452`: the finite-census build is GATED on NF-Z/P/M. NF-Z-relative, had it closed, would replace cylinder-(2.5) words by `I`. It would not discharge:

  | census step (`sol-td11-13-scope.md`) | consumes a neutral word? | in CONS? |
  |---|---|---|
  | entry L6 / BOOK-N1 | letter domain | yes |
  | priced chain graph `(w,M,λ,P,ν,ρ,κ̄, last cell, arrivals)` | endpoint + product | yes, via `I` *if* completeness held |
  | merge cell (zero-slot, `μ\|M`, partitions, `ε`, cases I–IV) | only through frame / `P` / `M` | yes |
  | **Prop 8.1(iv) on the cell’s actual multi-factor `p`** | arrival `(p,q)` of a pad is Z-Omega; the *merge* ODE is multi-orbit | **NF-M, not NF-Z** |
  | Q+E5 / E5F `n = ν_U κ̄_G − ν_G κ̄_U` | endpoint frame | yes (§3) |
  | shared `λ` budget / P1 | word has price 0 | yes |
  | insertion closure, N2/N3 regenerated per state | computes `m*`, `c_x` (entry data) | consumer *type* in CONS |
  | global window / nested TERM / multi-pole composition | word gaps vs skeleton / sibling gaps | word side in CONS; sibling is skeleton |
  | **state-changing clean resonance (11-A `5/8`)** | **not a (2.5) letter** (`Δ=3, n=2`) | **NF-P** |
  | `ν=1` insertions | excluded by §0 / §6 | NF-P, as the document says |
  | chart / jet / milestone-2 gluing | admitted outside | outside |

  So: no td-11/13 *word* consumer of a genuinely new field was found beyond CONS’s listed predicates. The loud 11-A object is a *resonance*, not a neutral word; §5’s v₂ certificate is an H8 projection of the *surrounding* (2.5) words and does not bring the resonance into NF-Z. PROVED-RELATIVE is therefore insufficient to ungate the compiler even as a slogan — NF-P and NF-M remain, and (findings 1–3) the NF-Z slice itself is not proved. That matches Sol’s own three-lemma split (`sol-normalform.md:403-405,487-494`) and grok-normalform finding 4.

  Fat-state enumeration remains complete and infinite without this document (`grok-normalform-review.md` finding 5). Nothing here changes that.

### 5. Severity: erratum — Claim (4). The N1–N4 *conclusions* used by the td-7 kill reproduce; the written specializations are not exact restatements, and the corollary is not among them. The 11-A v₂ certificate *does* reproduce Sol §4.3.

- File: `NF-Z.md:247-273`; `TOWER-9-15.md:515-538`; `cases/tower_check.py:988-1034`; `xmodel/sol-normalform.md:507-606`; `xmodel/sol-td11-13-scope.md:170-173,337-355`
- Claim: “td-7 (TOWER-UNIFORM N1–N4 falls out)”; “11-A (the 2-adic certificate) … Sol §4.3 verbatim.”
- How checked.

  Promoted N1–N4 were replayed from `tower_check.py` C3-N (five certificate suites, all PASS) and independently on the same lattices.

  | item | promoted statement | NF-Z §5 | exact? |
  |---|---|---|---|
  | **N1** | state-preserving zero-cost ⇒ `n=1` via `(n−1)(ν−1)≥1`; clean `(ℓ ν, ν+1)` with `gcd(ℓ,ν+1)=M` | “N1 is the cylinder membership itself” | **conclusion assumed, not derived.** Cylinder (2.5) *is* `n=1`. The identity that *forces* `n=1` is imported, not fallen-out. `M_j = gcd(ℓ_j, u_j+1)` is in §0. |
  | **N2** | at pre-F1 `(3/2,2)`, `gcd(ℓ,ν+1)=2` forces `ν` odd, so `P_pre` odd | `d=2 \| u+1` ⇒ `u` odd = “the `v_2(Π)=0` projection” | **conclusion yes, derivation different.** Vertex integrality `d\|u+1` also forces `u` odd at this `w`, even for `ℓ=1` M-drops. `v_2(Π)=0` is the used consequence. Lattice: `gcd(ℓν,ν+1)=gcd(ℓ,ν+1)` holds; `gcd(ℓ,ν+1)=2 ⇒ ν` odd holds. |
  | **N3** | joint cap `gcd(4, 2 P_pre)=2` from pole exponent 4 and `i_{F1}=2 P_pre`, both alive at X | “window-zone aliveness cap with first-letter exponent `P_0=4` and other-branch cap `2 P_pre`” | **gcd=2 yes.** Aliveness-at-X and “any shape `iℓ=4`” not restated in §5 (the general §4 aliveness paragraph is the intended carrier). Independent: `gcd(4,2P)=2` for every odd `P`. |
  | **N4** | gap `(ν+1)/(D_prev ν)`, `ℓ`-free; `D_prev≥4 ⇒ ≤ 3/8 < 2/5`; charged gaps shrink; `gap(X)` and WIN untouched | “`γ_j`-decay bound anchored at `P_0≥4`” | **the `3/8` number yes; the name no.** Decay is Z3’s ratio `≤ 1/2`. N4 is an absolute gap bound for one insertion. Charged-gap shrinkage and “window untouched” are not in §5. Identity `4ν−8≥0` holds for `ν≥2`. |
  | X-schema | chain-1 family `gap=(u+1)/(2u)`, three-case A/B/C | “single parametric letter `X` … `W_θ` at `θ=2/5`, zone length 1; three-case exhaustion = emptiness of that automaton” | **shape yes, metaphor yes.** Zone length 1 at `θ=2/5` replays (finding 2, reading B). A/B/C is not literally automaton emptiness. |
  | corollary as the kill | — | “`u_j u_{j+1} ≤ c_0=2<4` is the corollary” | **no** (finding 2). |

  **11-A v₂, Sol §4.3 verbatim — yes.** Independent replay:

  - BOOK-N1 at `w=2`: `gcd(2,u)=1` ⇒ `u` odd. Every product of such letters has `v_2(Π)=0`, so `v_2(P_1)=v_2(2Π)=1`. Checked on all words of length `1..4` over `{3,5,7,9,11}`.
  - Resonance `(Δ,n,ν)=(3,2,2)` from `(w,M,P)=(3,2,4)`: `P'=8`, `v_2=3`; any (2.5)-prefix product `A` gives `P_2=8AB` with `B` odd, hence `v_2≥3`. Checked on `A=1..19`.
  - Equal quotient needs `P_1=P_2`, impossible at `p=2`. Certificate text `H8_EQUAL_QUOTIENT_VP_MISMATCH { prime: 2, arrivals: [(μ=1, v_p=1), (μ=1, v_p≥3)] }` is the object in `sol-normalform.md:593-606`.

  Minor sloppiness: §5 calls this “the `p=2` component of `σ`.” In §2 the 2-adic data is a *`Π`-projection*, not `σ`. The pad-scaling `5/8 → ≤5/16` is promoted 11-A content and is *not* claimed as an NF-Z specialization; it replays (`A≥2 ⇒ 5/(8A) ≤ 5/16`) and is not needed for the H8 certificate. The `ν=1` degree-preserving hole from grok-normalform finding 2 is correctly left outside this paper.

### 6. Severity: erratum — Claim (3) as *artifact*, and several written asides. The three identities hold; they were not found as a checked-in script. A few surrounding sentences are false or oversized.

- File: `NF-Z.md:147-191,124-140,36-46,323-333`
- Claim: “The three load-bearing identities were machine-verified during construction (exact `Fraction`)” — α-exit on the td=6 template (`α_3 = 1003/42` both ways); `den(1/5−2/3)=15=P_2/gcd(u_1 u_2−1, P_2)` at `P_0=2`, word `(3,5)`; td-7/11-A specializations against the promoted gate. E5F offset “verbatim” the pad closed form. Z-Omega is “what NF-M consumes for neutral letters,” and “the promoted N/X rows are instances.”
- How checked.

  **There is no `nfz_check.py`.** §8 names it as future work. The existing machine gate is `cases/tower_check.py`, which checks the *template recursion* `α ← α+(k−1)ℓ/k` (C2: `α = (0, 3/2, 25/6, 1003/42)`) and N1–N4 as td-7 lemmas (C3-N), not Z1’s closed form, not Z2’s word formula, and not NF-Z §5 as a specialization harness. Reconstructed exact `Fraction` checks, all PASS:

  | identity | result |
  |---|---|
  | Z1 algebra `α+(k−1)ℓ/k = ℓ+1−γ` on the lattice `α=p/q`, `gcd(k,ℓ)=1` | **true** identically (death equation `ℓ/k = γ+α−1`) |
  | Z1 at F_s level-2: `23+1−5/42 = 1003/42` equals the recursion | **true**; template gaps `(5/2, 5/6, 5/42)` match C2 |
  | Z2 `den(γ'−γ+ℓ') = den(γ'−γ)` | **true** (`ℓ'` integer) |
  | word formula `γ_{j+1}−γ_j = (1−u_j u_{j+1})/P_{j+1}` | **true**; `(3,5)` at `P_0=2` is `1/5−2/3 = −7/15`, `den=15=30/gcd(14,30)` |
  | `gcd(uv−1,u)=gcd(uv−1,v)=1` for `u,v=2..39` | **true** |
  | `k' = P_2/gcd(uv−1,P_2) = uv P_0/gcd(uv−1,P_0) ≥ uv ≥ 4` on `P_0∈{1,2,3,4,6,8,9,10}`, `u,v=2..15` | **true**, 0 failures |
  | Z3 `γ_{j+1}/γ_j = (v+1)/(v(u+1)) ≤ 1/2` for `u,v≥2` | **true**; equality only at `(2,2)` |
  | N1–N4 lattices (finding 5) | **true** |
  | 11-A `v_2` (finding 5) | **true** |
  | `python3 cases/tower_check.py` | exit 0, `UNIFORM (17 cells): THEOREM` |

  Z1’s template check is a check of a *general* ladder identity at a *charged* vertex `F_s`, not at a word vertex. That is valid for Z1 (Z1 never uses price or `w`-preservation — §7 is right about that) and does not touch Z2’s word formula.

  **E5F “verbatim”.** §3 writes `n = u_r κ̄_G − ν_G w(u_r+1)` (the general law (1.5) / printed `(h')`) and says this *is* the pad closed form `n = ((u+1)X − μ_0 κ̄_G)/μ_0` “verbatim.” They are equivalent under the pad handshake, not the same formula. Numerical check at the frozen m=23 pad `(ν,κ̄)=(45,4)`: both give `n=2`. The citation is the right lemma, the word “verbatim” is wrong.

  **Z-Omega.** Clean one-orbit `C = −u A/(u+1)` matches the certified N row `11306 C + 11305 A = 0` and the (25,35) X row `26C+25A=0`. It does *not* match the merge/dirty rows the certificates also call N-adjacent (`C = −14/15 A²` at the merge, H2 `C=−7/4 A`). “N/X rows are instances” is true for the clean-neutral rows and false as a blanket. The reduced `(p,q)=(t−A, t−A)` in the N row is the one-orbit solve; the surrounding “`q = η(t−A)`” is the same family in a different chart.

  **Finiteness leak in the written `τ`.** “M-ledger … with letter positions of drops”: if the drop *index* is stored and the word is an unbounded deep `M`-drop (or a late drop on a long `M>1` word), there are infinitely many ledgers. The intended object is the drop-*value* chain in the divisor poset, with current position already in `σ`. Schema-set finiteness (finite drop-patterns × finite window-zone *shapes* × finite residue domains × finite `σ`) is the right NF-Z shape and survives after that repair; `Π` and the zone/endpoint letters stay exact symbolic parameters. Window-zone *length* is finite on either reading of `θ` (a fixed skeleton has a positive min gap, so the log bound is finite). Deep-zone length is unbounded and was never claimed finite except via the monoid.

  **Concatenation.** The semigroup story (ledgers in the divisor poset, `Π` multiplies, window zones re-truncate under `P ↦ P·Π_left`) is well-typed *as an interface*. It cannot be a completeness-preserving operation until `I` is complete (finding 1).

### 7. Severity: clear — Claim (2), residual. The *shape* of a finite symbolic quotient is right and is what Sol asked for. It is not a theorem until `I` is complete.

- File: `NF-Z.md:112-119,221-234`; `xmodel/sol-normalform.md:407-425`
- Claim: the invariant set is finite as a schema set, with `Π` and zone/endpoint letters retained as exact symbolic parameters over finite residue-class domains; concatenation is closed.
- How checked.

  Sol asked for finitely many symbolic summary schemas, exact parameter domains, and a closed concatenation, determining endpoint+E5F, scale/H8, every tower predicate at every neutral vertex, and attachment of the remaining skeleton. The *datatype* in §2 is that object. Cylinder (2.5) domains really are finite unions of residue classes modulo `lcm(ℓ,a,d)` (`sol-normalform.md:262-265`). `M`-drops really traverse a finite poset. A finite-state letter action really generates a finite monoid.

  What is missing is exactly Sol item 3: the tower predicates at *every* neutral vertex, not a max-gap-plus-product (the fifth pair) and not a final `(u_r, Π, σ_state)` (finding 1’s anagrams). Depth / N1–N4 / the 11-A 2-adic do not fill that hole (`grok-normalform-review.md` finding 4). This document does not change the necessity of a genuine NF-Z; it does not supply one.

---

## Attack scorecard

| attack | result |
|---|---|
| (1) same `I` ⇒ same CONS future | **false.** Deep anagrams `(3,5,7,9)` vs `(3,7,5,9)` (and three further pairs) have identical written `I` and different `α_exit` / death-step sequences |
| (1b) `α_exit` is a function of `(u_r, Π)` | **false.** `ℓ'_r` carries the whole previous `ℓ'` register |
| (1c) `σ` as written is the monoid Sol asked to be exhibited | **no.** §2 is a state; the theorem says “element”; neither computes `k'`/`ℓ'`/`α` |
| (2) finite schema set for fixed entry data | **shape yes; τ-positions leak; not a theorem until `I` is complete** |
| (3a) Z1 `α_next = ℓ+1−γ` | **true**, algebraically and at the td=6 template `1003/42` |
| (3b) Z2 den lemma + word formula + `k' ≥ uv ≥ 4` | **true** on the scanned lattice; applies to consecutive *ladder* deaths, not automatically to consecutive *word* deaths |
| (3c) Z3 forced ordered word-deaths, ratio `≤ 1/2` | **true** as a gap comparison; “exactly one death at own gap” is the standard `κ̄/D_f = (u+1)/P` identity for neutrals |
| (4a) corollary `c_0<4` is the td-7 kill | **no.** td-7 Case A is `k' = 2ν_X` after the pole, not word–word `k' ≥ uv` |
| (4b) N1–N4 fall out exactly | **conclusions used by the kill yes; N1 assumed not derived; N4 misnamed as decay** |
| (4c) 11-A v₂ certificate = Sol §4.3 | **yes**, exact; `v_2(2Π)=1` vs `v_2≥3` |
| (5a) CONS = promoted kernel | **no** (consumers ≠ lemmas) |
| (5b) some td-11/13 census step reads a word field outside CONS | **no new word-field found.** 11-A `5/8` is a resonance (NF-P). Multi-factor merge ODE is NF-M. Compiler stays gated on all three |
| machine-check artifact for the three identities | **absent.** Reconstructed `Fraction` checks pass; `tower_check.py` is the N1–N4 / template gate, not an NF-Z harness |

---

## What may be treated as proved, today

1. Z1 is an identity: if `ℓ/k = γ+α−1`, then `α+(k−1)ℓ/k = ℓ+1−γ`. Template value `α_3 = 1003/42` both ways.
2. Z2’s denominator cancellation: `den(γ'−γ+ℓ') = den(γ'−γ)`, and for consecutive *word* letters `γ_{j+1}−γ_j = (1−u_j u_{j+1})/P_{j+1}` with `k' = P_{j+1}/gcd(u_j u_{j+1}−1, P_{j+1}) ≥ u_j u_{j+1} ≥ 4`.
3. Word gaps are strictly ordered with ratio `≤ 1/2` (`=` only at `(u,u')=(2,2)`). Neutral death gap equals the vertex’s own `(u+1)/P`.
4. Cylinder (2.5) domains, BOOK-N1, and the td-7 N2/N3/N4 *numbers* (`u` odd, `gcd(4,2P_pre)=2`, gap `≤ 3/8` at `D_prev≥4`).
5. The 11-A pole-adjacent `5/8` family is merge-dead by `H8_EQUAL_QUOTIENT_VP_MISMATCH` at `p=2`. That one-prime projection does not need a global NF-Z (`sol-normalform.md:602-606`, unchanged).
6. Non-ladder consumers in §3 (price 0, E5F affine in `u_r`, H8 reads `P_0 Π`, Z-Omega one-orbit `C=−uA/(u+1)` for genuine clean neutrals) factor through `(u_r, Π, τ)` as claimed.
7. The fifth pair `(3,5,7)` vs `(5,3,7)` is distinguished by `W_θ`. Max-gap + product remains an illegal projection.

Everything else — CONS-complete summaries, a finite deep-zone monoid that actually carries α and the death-step register, the corollary as a uniform kill, `nfz_check.py`, ungating the compiler — stays `OPEN`. NF-P and NF-M are untouched.

A repair that would be worth a second review would have to (i) put the `ℓ'` register (or the ordered window-plus-deep death-step word) into `I`, or prove it is a function of the existing fields, (ii) pick one definition of `θ` and rewrite Z2/caps/§5 to match, (iii) exhibit `σ` as a monoid element on a modulus that computes every CONS predicate, including `k' | c_x`, and (iv) keep the relativity sentence honest: CONS is a consumer list, the compiler still needs NF-P/M, and the 11-A `5/8` resonance is not a (2.5) letter.
