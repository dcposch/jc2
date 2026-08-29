# SIGRAY-AUDIT.md — Section 2–6 statement audit (thesis pp. 7–30)

Source: [refs/sigray_full.pdf](../refs/sigray_full.pdf) (printed page = PDF page). Batch: 72 items, Not 2.1 through Prop 6.2. Verdicts cross-checked against the campaign's erratum catalogue E1–E11 + G1–G3 (`SHEET6-CAMPAIGN.md` §7, `SHEET6-LT-REVIEW.md` §6, `SHEET6-AF2.md`, `SHEET6-AF3.md`, `SHEET6-III.md` §5) and against usage in the promoted SHEET6 docs.

## 1. Verdict ledger (sorted by thesis page)

| id | page | verdict | note |
|---|---|---|---|
| Not 2.1 | 7 | VERIFIED | Definition well-formed: ~ is an equivalence preserving the Jacobian condition; lex-min exists; swap automorphism gives deg f ≤ deg g (used in Lem 2.1(iii)). |
| Not 2.2 | 7 | VERIFIED | Q⁺ := Q ∩ [0,∞); inclusion of 0 deliberate and consistently used (Lem 2.1's α ≠ 0 step would otherwise be vacuous). |
| Lem 2.1 | 8 | VERIFIED_WITH_NIT | Statement + proof re-derived with exact arithmetic; two [A]-citations re-proved from scratch. Nits: [A, 18.13]/[A, 19.2] are load-bearing external inputs not in repo refs; the symmetric j>l_f rectangle case is not literally covered by the printed parenthetical. |
| Not 2.3 | 9 | VERIFIED | Normalized counterexample well-defined; the "from now on" reduction is sound via Lem 2.1. |
| Not 2.4 | 9 | VERIFIED | Type (α,β) well-posed (k_f,k_g ∈ N* from Lem 2.1(i)); (iii) forces α < β. |
| St 2.1 | 9 | VERIFIED_WITH_NIT | Claim (α ≠ 1, β ≠ 1) TRUE, but printed citation "(iv)" insufficient for β ≠ 1 — needs (iii)+(iv); one-word citation repair. |
| St 3.1 | 10 | VERIFIED | No proof printed; the exactly-one-of-(i)/(ii) dichotomy and Puiseux form re-derived from scratch. |
| Def 3.1 | 10 | VERIFIED | Characteristic sequence well-defined: gcd(κ, supp) = 1 forces termination e_m = 1; β_i strictly increasing. |
| Def 3.2 | 10 | VERIFIED_WITH_NIT | Contact order O well-defined; must read 0 ∈ Q⁺ (constant terms); O(P,P) left undefined (needed by Def 3.3); stray ∞ upper-limit typo. |
| St 3.2 | 11 | VERIFIED_WITH_NIT | Proof MISSING in thesis and claim nontrivial (false for general series sets); re-derived via Galois-orbit ultrametricity + greedy anchor induction; 400-trial exact confirmation. Typos ("There exits", "THE Puiseux series"). |
| Def 3.3 | 11 | VERIFIED_WITH_NIT | ~ IS an equivalence, but reflexivity needs unstated O(P,P) = ∞ and transitivity (ultrametric inequality) is nowhere established in the thesis. |
| Not 3.1 | 11 | VERIFIED | I_P injective, π well-defined, π∘I_P = id — all re-derived. |
| Not 3.2 | 11 | VERIFIED_WITH_NIT | (0,y), (0,x) well-defined single classes; usual "independent of P" remark omitted; nonemptiness of S*_y, S*_x implicit. |
| St 3.3 | 11 | VERIFIED_WITH_NIT | Two components re-derived (cross-form O = −1 separates; rays connect each side). Nit: printed S*_{a,x}, S*_{a,y} never defined (stray subscript). |
| Def 3.4 | 11 | VERIFIED_WITH_NIT | V_a well-defined and finite; "u = α_{j,P} for some j" must be read j ≥ 1 (forced downstream) — matches campaign's H1-tier reading dependence (LT-REVIEW LR1(a)), deliberately unfiled. |
| Not 3.3 | 12 | VERIFIED_WITH_NIT | Edge structure re-derived (u* unique, F°-independence, edges biject with non-root vertices). Nits: forward reference to T_a; edge interval printed backwards (I_P([u,u*]) for I_P([u*,u])). |
| Not 3.4 | 12 | VERIFIED | ν_F P-independence PROVED here (not claimed in print; 20000-trial exact sweep) — settles SHEET6-HIII-REVIEW's parenthetical worry negatively: H5a does NOT infect ν_F. |
| Not 3.5 | 12 | GAP | κ_F NOT well-defined as printed: explicit two-branch witness gives κ_F = 4 vs 2 at the same vertex. = campaign's standing item H5a (SHEET6-III.md §5, HIII-REVIEW Front 4), documented but NOT E/G-numbered. Forced repair: jump-realization/max (Eggers-Wall) value. |
| Not 3.6 | 12 | VERIFIED_WITH_NIT | T_a well-formed; printed "T_{a,y} := T_{a,y} ∩ T_a" is circular — RHS must be the starred components of St 3.3. Cosmetic. |
| St 3.4 | 12 | VERIFIED | No proof printed; π(F) ∈ Q re-derived for all three vertex classes (V_{1,a}, V_{2,a}, roots). H5a does not affect it. |
| Not 3.7 | 12 | VERIFIED | Suitable κ exist = common multiples of the finitely many pole multiplicities; requires the Not 3.2 reading of forms (3)/(4). |
| Not 3.8 | 12 | VERIFIED | Both embedded "independent of P" claims re-derived (thesis: "easy to check"); F*c half needs only n ∈ N (n = 0 allowed). |
| St 3.5 | 13 | VERIFIED_WITH_NIT | Re-derived ((F*c)′ = F); hypothesis omits "suitable" for κ; harmless. |
| St 3.6 | 13 | VERIFIED | Re-derived with explicit witness coefficient; edge cases (n = 1, zero coefficient) check out. |
| Not 3.9 | 13 | VERIFIED_WITH_NIT | Well-posed; strict truncation j < π(F) is exactly what gives P-independence. Nits: "Ω(F)" slip for Ω(P); asymmetric unused κ-hypothesis in the x-case. |
| St 3.7 | 13 | ERRATUM | NEW. Eq (5) FALSE as printed: hypothesis κπ(F) ∈ N missing (its twin (6) carries it); exact-arithmetic counterexamples at κπ(F) ∉ Z. Corrected statement adds the hypothesis. Benign downstream: Not 3.10 hedges, all later uses impose κπ(F) ∈ N. |
| Not 3.10 | 13 | VERIFIED_WITH_NIT | Decomposition unique; d_{h,F}, p_{h,F}, h⁺_F invariant under change of suitable κ; the "Assume ... form (5)" hedge insulates it from the St 3.7 erratum. |
| Not 3.11 | 13–14 | VERIFIED_WITH_NIT | Under the canonical maximal-presentation reading, κ_F at v is (Q,j)-independent — re-derived. Nits: type slip (v names a set), existence of v tacit, formal reliance on P-dependent Not 3.5. Related but distinct from E5/H5a. |
| St 3.8 | 14 | ERRATUM | NEW. D_{h,F} ∈ Z FALSE under Not 3.5's P-presentation: explicit contact-vertex witness gives D = −1/2 ∉ Z (and ill-defined value 1 vs 2 even when integral). This UPGRADES H5a from coherence-forced convention to printed-statement-forced: only the jump/max κ_F reading makes St 3.8 true; corrected version proved in two lines (lattice argument). Not previously filed against St 3.8. |
| Not 3.12 | 14 | VERIFIED | mult(p,z) well-posed via unique factorization; degenerate p ≡ 0 never fed to it. |
| Prop 3.1 | 14–15 | VERIFIED_WITH_NIT | Counting identities (*)/(**) re-derived (unramified cover + Hensel + squarefree ⇒ distinct) and machine-checked at κ = 2, 4. Print errors: "c_j x^{-j}" must be c_j x^{-j/κ} (E5/E8-grade typo); proof cites form (4) where (3) is meant; proof terse. |
| St 3.9 | 15 | VERIFIED_WITH_NIT | (i)–(iii) re-derived and machine-checked. Its printed Proposition 3.1 hypothesis is **auxiliary-`h` dependent and load-bearing**: an exact `kappa=1` ablation gives `mult=3` but child degree 1 because `h=0` has pole order 2. The statement is sound with its full hypothesis; every consumer using a derived `h_j` must refine to an `h_j`-suitable κ/subdivision or use St 3.11. Display typos (upper limit l for n, x^{-κ}η for x^{-1/κ}η, missing /) self-repair; forward reference to Not 3.13. Opus finding `882485d6...`, Sol review `ca63eb5e...`. |
| St 3.10 | 16 | VERIFIED | No proof printed; ω, ω* monotone/continuity/slope laws re-derived via contact orders; exact spot-check passed. |
| St 3.11 | 16 | ERRATUM | NEW (the campaign's own paraphrases silently correct it). Printed (ii)'s first term lacks the prime (should be d_{h,F'}): as printed the first inequality is vacuous and the equality-propagation clause is FALSE (explicit counterexample, verified). Corrected version fully re-derived.  The lower bound, upper bound and degree inequality are independently rederived in the Proposition 6.7 review `eb37373b...`; the corrected lower bound is now load-bearing there. |
| Not 3.13 | 16 | VERIFIED_WITH_NIT | Load-bearing slip: p_F, d_F must be read p_{f−a,F}, d_{f−a,F} (literal h = f empties T_a⁻ and falsifies St 3.13). Campaign already adopts this reading (SHEET6-H3.md). |
| St 3.12 | 16 | ERRATUM | NEW. Print (600 dpi confirmed) shows the SAME identity twice — no (0,x)/(1,0) clause; even one instance false under the printed chart naming. Corrected: h⁺_{(0,y)} = h⁺_{(1,0)}, h⁺_{(0,x)} = h⁺_{(0,1)}. Consequence inequalities TRUE. SHEET6-H3.md §2a's "verbatim" quote silently corrects the print — filing amendment needed. |
| St 3.13 | 16 | ERRATUM | NEW (E12-candidate). FALSE as printed for a ≠ 0: d_{f,I(u)} freezes at 0 past the crossing (exact counterexample f = xy, a = 1) — uniqueness fails. TRUE with d_{f−a}: unique zero re-derived. Root cause = Not 3.13 slip; same one-token repair fixes Not 3.14, St 3.14, St 3.15's hypothesis. Campaign silently uses corrected reading (SHEET6-LROOT.md). |
| Not 3.14 | 16 | VERIFIED_WITH_NIT | Trichotomy trivially a partition; inherits the Not 3.13 slip — printed reading gives T_a⁻ = ∅ and an infinite T⁰ tail, breaking Not 7.1/Prop 7.5 downstream; corrected reading is the one actually used. |
| St 3.14 | 16–17 | GAP | (a) Printed reading false for a ≠ 0 (d_{f−a} repair mandatory). (b) Under the repair, all steps re-derived except (ii): "η_F = η_G" assumes the per-fiber Ω picks aligned continuations; can fail up to a root-of-unity conjugation twist for κ > 1. Repair: weaken (ii) up to twist (preserves d, deg, root multiplicities — all the campaign uses) or strengthen St 3.2. NEW. |
| St 3.15 | 17 | KNOWN_ERRATUM | = E10 (labels (i)/(iii) swapped), independently reconfirmed with exact witnesses; multiplicity clause verified modulo the swap; d_{h,H} typo. ADDITION to the filing: the hypothesis's p_F must also read p_{f−a,F} (Not 3.13 slip), else vacuous/false for deep F on fibers a ≠ 0. |
| St 3.16 | 17 | VERIFIED_WITH_NIT | No proof printed; both halves (vertex iff >1 root; η^ν root pattern) re-derived + exact confirmation. Same Not 3.13 p_{f−a} reading dependence (uncatalogued). |
| Prop 3.2 | 18 | VERIFIED | No proof printed; existence/uniqueness/κ-independence of F = G + c re-derived, incl. unstated P-independence of c. |
| St 3.17 | 18 | VERIFIED_WITH_NIT | (i)/(ii) re-derived (vertex-free segment argument + St 3.9 iteration) + exact confirmation. Nits: "π_G" undefined notation; p_{f−a} reading dependence. |
| St 3.18 | 18 | ERRATUM | NEW. Conclusion prints "…unique ν_F-th root of unity, ε such that F * c exists" — ε never occurs in the conclusion; literally false whenever ν_F ≥ 2. Corrected "F * (εc) exists" re-derived TRUE (uniqueness leans on St 3.2's coherent Ω). SHEET6-A2P-REVIEW quotes the corrected form as "verbatim" — uncatalogued; campaign usage is of the corrected form throughout. |
| Prop 4.1 | 18 | VERIFIED_WITH_NIT | Chain-rule identity and (8) dichotomy re-derived (numeric check passed). Nits: undefined "T_{κ,a}"; p_k-for-p_l display slip; hypothesis (7) not load-bearing for 4.1 itself. |
| Prop 4.2 | 19–20 | ERRATUM | **Complete repair promoted 2026-08-28** (`10bc55d5...`, Opus5 review `47f2b608...`; no-first-corner strengthening `882485d6...`, Sol review `ca63eb5e...`). Permit `l_j=0` only once, as the unique terminal constant shift `(k,l,s)=(1,0,c)`, `h_m=h_{m-1}-c`; then `d_{h_m,F}<0`, the next bracket is nonzero, `delta_m=0`, `deg p_{h_m,F}=(mu_F-1)deg p_F+1`, and `M_F` includes this terminal degree. A corner is in `T_a^nearrow`, never on a pole characteristic path. A separate ancestor induction now proves that index-zero corners are impossible for every translated `(f,g-b)`, so restore the p. 20 Remark's **statement** that (7) is automatic on `T_a^+`, replacing its circular printed justification. Fact A/Prop 4.4 uses with a derived `h_j` must refine to an `h_j`-suitable κ before invoking St 3.9; cross-multiplied Props 6.2/6.3 and Fact B remain part of the repair. Prop 4.3 remains separate; Proposition 5.1 supplies the shifted negative-side condition. Correct tuple arity to `N^m`; use `gcd(k,0)=k`. |
| Prop 4.3 | 20–21 | VERIFIED_WITH_NIT | NO proof printed; full analogue proof reconstructed and CLOSES ((7) excludes 4.2's stuck corner at j = 0; strict negativity closes j ≥ 1) — explains why (7) is hypothesized here and 4.2's missing analogue is exactly its gap. (iv)'s (f⁺_F)^μ vs (f−a)⁺_F reconciled: T_a⁻ ≠ ∅ forces a = 0. |
| Not 4.1 | 21 | VERIFIED_WITH_NIT | Well-defined via 4.2's uniqueness; ⪯ is a PREORDER, not partial order (antisymmetry fails) — downstream uses need only the preorder. Stray parenthesis typo. |
| Not 4.2 | 21 | VERIFIED_WITH_NIT | Well-posed via 4.3; dropped b-subscripts in the strict clause; duplicated "b ∈ C"; inherited off-by-one dimension tags; "preorder" not "partial order". |
| Prop 4.4 | 21–22 | VERIFIED_WITH_NIT | Proof re-derived link-by-link (T_a⁺ chain, T_a⁻ λ-interpolation) — sound. Nits: F′ never defined in the statement (= tree parent); "any F, F′ ∈ T_a⁻" overstates what is proved (neighbour version + chaining suffices for all downstream uses); minor citation/notation slips. |
| Prop 4.5 | 22–23 | VERIFIED_WITH_NIT | Proof reconstructed; rests on Lem 2.1(i)'s rectangle/corner property of the fixed normalized f — load-bearing but unstated. Print: missing ⁺ superscript in hypothesis; relies on St 3.12 whose print is garbled (see St 3.12 erratum). |
| Prop 4.6 | 23 | VERIFIED_WITH_NIT | No proof printed; (11)–(17) fully re-derived + machine-verified (295-trial exact sweep); the (12) "<" vs (15) ">" sign asymmetry confirmed correct. Nits: "Set F = T_a⁺ ∪ T_a⁻" misprints ∈; T_a⁻ case rests on 4.3(iv) not "(10)". |
| Prop 5.1 | 23–24 | ERRATUM | NEW; **complete repair promoted 2026-08-28** (`a0470416...`, Opus5 review `dc549047...`, coordinator integration `11059166...`). At a finite puncture the printed `b=0` makes (7) fail and the threshold need not exist. The unique repair is `b_P=g(P)` (and `b_P=0` at a pole), with `rho_P=d_{f-a}+d_{g-b_P}+v-1`; its first rational zero is the first nonzero leading Jacobian. The threshold is sided and never lies in `T_a^0`: it is in `T_a^+` exactly at a g-pole and in `T_a^-` exactly at a finite puncture. Thus sided `m=0` is typed at the threshold, while the unique `d_{f-a}=0` flag must use the leading-Jacobian predicate. Non-leakage proves `T_{a,pole}` and all pole masses/books unchanged and proves the source's unproved St 7.2; Prop 7.3's missing shift/(7) step is supplied. |
| Prop 5.2 | 24 | KNOWN_ERRATUM | = E10 casualty exactly as filed (LT-REVIEW §6 FILING FIX 1): statement TRUE, printed proof's last inference only reads correctly under the erroneous St 3.15 labels. Repair re-derived here inside the printed apparatus. |
| Not 5.1 | 24 | VERIFIED_WITH_NIT | Under the promoted Prop 5.1 repair, retain `(b_P,side)` with `F_P^*`. The threshold exists uniquely at every puncture, is positive, rational and never in `T_a^0`; sided `m=0` is well-typed. At g-poles `b_P=0` and the datum is literally the printed campaign object. |
| St 5.1 | 24 | VERIFIED_WITH_NIT | Proof re-derived both directions; k/l vs l/k letter-shuffle in the displayed ratio (harmless); only T_a⁺ vertices invoked, so the 5.1 gap never bites. |
| Not 5.2 | 25 | VERIFIED | T_{a,pole} remains exactly the g-pole threshold set after the Prop 5.1 repair: the promoted non-leakage theorem puts every finite-puncture threshold in T_a⁻ and every pole threshold in T_a⁺. Thus the cut is mathematical, not a consumer convention. |
| Prop 5.3 | 25–26 | ERRATUM | NEW statement-level: (ii) and (viii) ratios INVERTED — printed d_{g,F} = (k_f/k_g)d_F, correct (k_g/k_f)d_F = (β/α)d_F; proof has a second distinct slip (k_f/l_f). Forced by 4.6(11), St 5.2(i), Prop 5.7, table (23). All NINE properties are true after correction.  Its proof of (iv) also omits the genuine linear-`p`/constant-`q` bracket branch; the promoted pole degree pin `be9e4b74...` proves `alpha*deg p_(g,F)=beta*deg p_F`, hence `deg p_F>=alpha>=2`.  Campaign consumers use the corrected ratio; A3L1-REVIEW:61 quotes the print unflagged. Secondary: (vii) is not derived in print; (vi) misses ",c". |
| Prop 5.4 | 26 | ERRATUM | **Complete repair promoted 2026-08-28.** The statement is true but the printed proof never proves the `q`-half.  The deck-character projector plus zero-homogeneous-kernel proof closes it after the repaired pole degree pin: R2 `be9e4b74...`, Opus5 review `c3f0bfde...`, coordinator integration `6375bc05...`; exact checkers replay 1,788 + 943 PASS.  The abstract `alpha=1` mixer exists only on the excluded linear branch. |
| Not 5.3 | 26 | VERIFIED | Q-datum well-defined on T_{a,pole}: κ_F supplied by 5.3(iv), integrality by St 3.8, positivity by T_a⁺ + 5.3(ii) (unaffected by the 5.3 ratio erratum). |
| St 5.2 | 26 | ERRATUM | (i)'s middle ratio is INVERTED: print has `D_(g,F)/D_F=alpha/beta`; correct is `D_F/D_(g,F)=alpha/beta`, equivalently `D_(g,F)/D_F=beta/alpha`.  The degree ratio and (ii) menu are true; complete Proposition 5.4 repair `be9e4b74...` proves the formerly missing `q`-half, and exact sweeps pass. |
| Prop 5.5 | 26 | ERRATUM | NEW proof-level: all three case conclusions drop g-subscripts (case (ii, c ≠ 0) as printed literally contradicts (18)); dangling "Statement 18" citation (same class as E8). Boxed statement (18) re-derived TRUE; the iff direction needs E10-corrected St 3.15 (known co-dependence, already listed in LT-REVIEW). Corrected proof closes in full. |
| Prop 5.6 | 27 | VERIFIED_WITH_NIT | (19) re-derived exactly in all three root-pattern cases (orbit arithmetic exhaustively swept). One-line printed proof silently needs 5.3(v)/(ix) (simplicity; one puncture per continuation). |
| Prop 5.7 | 27 | VERIFIED | Λ ≥ β re-derived with the missing a,b-scaling supplied; ν_F < deg p_F needs 5.3(iv); sweep confirms bound tight (table (23) rows r5, r10). |
| Def 5.1 | 28 | VERIFIED | Generic preimage count well-posed; Keller condition forces dominance and multiplicity 1, so td ∈ N*. |
| Prop 5.8 | 28 | GAP IN SOURCE / CAMPAIGN REPLACEMENT PROMOTED | NO proof is printed for (20) (text goes straight to §6).  The source verdict remains GAP, but the every-fiber theorem is proved by the dual-reviewed relative-surface/Chau replacement `SOL-PROP58.md` and independently re-audited in `47eef092...`, which also supplies an internal positive-pole transport proof using repaired Proposition 5.1 sidedness.  Do not use the formerly proposed one-line St 3.14 + ν-invariance route: it omits pole-set, g-data and κ transport and exact η alignment can twist.  Coordinator integration `bb033a71...`. |
| Prop 6.1 | 28 | VERIFIED_WITH_NIT | Indirect proof re-derived ((16) ⟺ (17) under the hypothesis, contradicting 4.6's exclusivity; 2000-trial check). Literal broken "Notation ??" reference; T_a⁻ half tacitly needs Prop 4.3. |
| Thm 6.1 | 28 | VERIFIED_WITH_NIT | l_f < k_f re-derived (Lem 2.1(iii) + Prop 6.1 at the root). Nits: systematic chart-naming inconsistency (operative convention vs literal Not 3.2 chain — conclusion invariant); flags the St 3.12 duplicated-identity print typo. |
| Not 6.1 | 29 | VERIFIED | T↗/T↘ well-posed, disjoint, exhaust T_a⁺ by Prop 6.1; transcription exact. |
| St 6.1 | 29 | VERIFIED | One-line proof sound; Prop 6.1's dichotomy independently re-checked in both branches. |
| St 6.2 | 29 | GAP | The iff is re-derived exactly. The "in particular" clause (unproven in print) does NOT follow as stated: `H in T_a+` — required for `H in T_a^down` — is not implied (abstract failure mode `d_H <= 0`). Corrected statement: add `H in V_a cap T_a+` or weaken the conclusion to the strict inequality. Consumer sweep r1 (`d64b043c...`) conflated the one-grid-step `G*_kappa c` with the next vertex `G+c`; r2 (`581219e0...`) corrects this. Props. 6.7/6.8 are review-closed (`eb37373b...`, correction `050ccddd...`), and Lemma 6.1 is now different-model confirmed (`2fdbbee9...`, `5193e7b0...`, correction `607e0dcf...`, integration `bb033a71...`). Concrete consumers that establish the omitted positive domain may use the bridge without a provisional rider. Distinct from E5. |
| Prop 6.2 | 29–30 | ERRATUM | NEW. Hypothesis F/G swap: printed side conditions (i) G ∈ T_a⁻ / (ii) F ∈ T_a⁺ are the exact mirror of what Prop 4.4 needs; mixed-sign case admitted and the proof breaks in three places (exact witness). Corrected (i′) F ∈ T_a⁻ / (ii′) G ∈ T_a⁺: entire proof re-derived + 300k/82k-trial exact sweeps, 0 failures. Same family as E10. Thesis's only citation (Prop 6.3, G ∈ T↘ branch) satisfies (ii′) — downstream unaffected. Two benign /κ display drops also noted. |

## 2. Summary

Of the 72 items audited (thesis pp. 7–30, Not 2.1 → Prop 6.2): **21
VERIFIED, 32 VERIFIED_WITH_NIT, 13 ERRATUM, 2 KNOWN_ERRATUM, 4 GAP**.
The two KNOWN_ERRATUM items remain Statement 3.15 and Proposition 5.2, the
catalogue's E10 family.  The thirteen internally filed ERRATUM items are
Statements 3.7, 3.8, 3.11, 3.12, 3.13, 3.18, 5.2 and Propositions 4.2,
5.1, 5.3, 5.4, 5.5 and 6.2.  Proposition 5.1 entered this list after its complete forced-puncture
repair (`a0470416...`, `dc549047...`, `11059166...`). Proposition 4.2 moved
from GAP only after the complete constant-shift repair
(`10bc55d5...`) and Opus5 downstream-typing review (`47f2b608...`): the
circular p. 20 argument is deleted, but a later different-model-reviewed
ancestor induction (`882485d6...`, `ca63eb5e...`) restores its statement and
makes (7) automatic on `T_a^+` for every target shift. Facts A/B,
auxiliary-`h` κ refinement and cross-multiplication repair the downstream
`l=0` consumers.

Of the four remaining GAP verdicts, one is the campaign's known but unnumbered
H5a ambiguity in Notation 3.5.  The other three are Statement 3.14 (cross-fiber
root-of-unity twist), Proposition 5.8 (printed proof absent; separately
replaced in the campaign), and Statement
6.2 (missing `H in T_a^+` hypothesis).  The recurring Notation 3.13
`p_F/d_F -> p_{f-a,F}/d_{f-a,F}` slip still drives riders on Notation 3.14
and Statements 3.14–3.16; campaign computations use the corrected reading.
The three independent filing fixes remain: `SHEET6-H3.md` §2a and
`SHEET6-A2P-REVIEW.md` silently correct Statements 3.12/3.18 while calling
them verbatim, and `SHEET6-A3L1-REVIEW.md` quotes the inverted Proposition
5.3(ii) ratio without flagging it.

## 3. Load-bearing risk

Every ERRATUM/GAP/KNOWN_ERRATUM item is inside the campaign's trust perimeter (SHEET6-TEMPLATE.md §6 lists "Prop 3.1, St 3.7–3.18, Prop 4.1–4.6, Prop 5.1–5.8" wholesale). Grep-verified usage by promoted results, ordered by residual risk:

**Tier 1 — unproven strength actually consumed by promoted results:**
- **Prop 5.8 (20) [GAP IN SOURCE / CAMPAIGN REPLACEMENT PROMOTED]** — the enumeration bedrock `td = sum Lambda` over pole vertices is consumed by the finite-entry books.  The thesis prints no proof, but the campaign's every-fiber theorem is review-closed by `SOL-PROP58.md` / `SOL-PROP58-REVIEW.md` plus Chau 4.4.  Independent audit `47eef092...` also gives a positive-pole transport proof from repaired Proposition 5.1 sidedness.  Thus this is no longer a campaign trust risk.  The replacement repairs only mass/entry allocation, not landing, merge, suffix, or book completeness.
- **Not 3.5 / H5a [GAP] + St 3.8 [ERRATUM]** — the κ_F convention feeds Not 3.11, Not 5.3's Q-data, Prop 9.3, and the E5-corrected λ-bound engine; SHEET6-III.md's promoted tails closure (10 of 13) is explicitly conditional on H5a/H5b. The St 3.8 finding is favorable: it forces the H5a reading from the printed text, converting a standing hypothesis into a theorem-level constraint — ledger should record the upgrade. D-integrality (St 3.8, corrected) also underpins Prop 5.7 and every integer Q-datum in the §9 tables.
- **St 6.2 [GAP IN SOURCE; CONSUMER BRIDGE CLOSED]** — the climb/regularity workhorse is consumed by AF2, III, A2P, MULTIPOLE and the Statements 9.6–9.11 template.  Sweep r2 (`581219e0...`) distinguishes the microstep from the next vertex.  Repaired Proposition 6.7 puts the realizable microstep in `T_a+`; repaired Proposition 6.8 carries a down microstep to the next down vertex through a same-branch pole.  Opus5 review `eb37373b...` plus correction `050ccddd...` confirms that composition, and Lemma 6.1 is now independently closed by `2fdbbee9...`, review `5193e7b0...`, correction `607e0dcf...`.  The source omission remains, but no consumer is provisional once it supplies the positive domain.

**Tier 2 — load-bearing, but campaign already computes with the corrected form (filing fixes only):**
- **Prop 5.4 [ERRATUM — COMPLETE REPAIR]** — its `(i)/(ii)` eta-to-`nu`
  patterns source Statement 5.2(ii)'s menu, used by TDUNIFORM and AF3.
  The promoted pole degree pin plus deck-character proof (`be9e4b74...`,
  review `c3f0bfde...`, integration `6375bc05...`) supplies exactly the
  omitted `q`-half; both exact checkers pass.  This source risk is closed.
- **St 3.18 [ERRATUM]** — root ↔ direction correspondence with unique-ε continuation is core to direction pricing: III (S1/S2 c = 0 forcing), L1 (one-continuation-per-orbit exclusions), AF2 (R1), TDUNIFORM (unpriced q-orbits), A2P-REVIEW. All uses are of the corrected "F*(εc)" form; A2P-REVIEW's "verbatim" label must be fixed when filing.
- **St 3.15 = E10 [KNOWN_ERRATUM]** — value dichotomy used by LROOT's pole purity ("St 3.15 with corrected labels, E10"), Prop 5.5/5.6's (18)/(19), A3L1/A2P. Already catalogued; add the p_{f−a} hypothesis rider found here.
- **Prop 5.3 [ERRATUM]** — (v)/(vi)/(ix) drive LROOT pole purity, AF3's pattern layer, 2POLE, L1; the inverted (ii)/(viii) ratio is silently corrected in TDUNIFORM (R1). File the erratum + flag A3L1-REVIEW:61.
- **Prop 5.5 (18) [ERRATUM]** — Λ values feed the entire Λ ≤ 7 leaf table (CAMPAIGN §1), 2POLE, LROOT. Statement re-derived true; proof-level subscript drops benign; iff already listed as E10 casualty in LT-REVIEW.
- **St 3.12 [ERRATUM]** — used by Thm 6.1, Prop 4.5, LROOT root data, and H3's mult/deg transport (the promoted H3 root-kill). Consequence inequalities true; H3.md §2a's "verbatim" quote must be amended.
- **St 3.13 + Not 3.13/3.14 slip family [ERRATUM]** — LROOT (PROMOTED) places cv vertices at "the unique (St 3.13) d = 0 point" under the corrected d_{f−a} reading it already uses; file as E12 so the reading is on the ledger rather than folklore.
- **St 3.11 [ERRATUM]** — heavily used (R6 echo kills, TEMPLATE's 16 ≤ 7
  kill, LT-REVIEW:132, R1-Q2E5).  Repaired Proposition 6.7 is the first
  load-bearing use of corrected (ii)'s lower bound; Opus5 independently
  rederived both bounds and the degree inequality in `eb37373b...`.
  Consumers must use the corrected primed first term; the printed equality
  clause remains false.
- **Prop 4.2 [ERRATUM — COMPLETE REPAIR]** — towers are ubiquitous.  The
  corrected global `T_a^+` recursion admits one final `(1,0,c)` shift and
  then terminates with the exact degree and `M_F` formulas.  The p. 20
  Remark's circular proof is deleted, but its statement is restored by the
  reviewed no-first-corner induction and target translation: (7) is automatic
  on `T_a^+`.  Facts A/B, auxiliary-`h` κ refinement and cross-multiplication
  repair the downstream `l=0` consumers.  Pole characteristic paths lie in
  `T_a^searrow` and are corner-free.  Consumers must carry the complete
  repair, not merely replace `N*` by `N`; Proposition 4.3 remains separate.
- **Prop 5.1 / Not 5.1 [ERRATUM — COMPLETE REPAIR]** — use the forced centre
  `b_P=g(P)` at finite punctures, `b_P=0` at poles, and the shifted `rho_P`.
  The threshold is sided and never lies in `T_a^0`; a bounded-degree limit
  proof establishes this without Prop 4.4.  Therefore the repaired
  all-puncture definition does not leak finite thresholds into `T_{a,pole}`,
  and the printed pole book, `M/Q/Lambda` data and mass formula are unchanged.
  This also proves the source's unproved St 7.2 and closes Prop 7.3's missing
  shift/(7) step.  The unique `T_a^0` flag remains typed only by the
  leading-Jacobian predicate; Not 8.1/St 8.1 repeat that broader source slip.

**Tier 3 — used, failure mode outside campaign usage (verify-on-use guards recommended):**
- **St 3.14 [GAP]** — used by LT-REVIEW (Prop 7.3's pattern-preservation mechanism) and as the natural Prop 5.8 repair route; the conjugation-twist gap preserves d, deg, and root multiplicities — everything those uses need — but the twist must be carried explicitly if (ii) is ever used for exact leading coefficients across fibers.
- **Prop 5.2 [KNOWN_ERRATUM]** — LROOT cites its no-pole conclusion inside the E10 discussion with corrected labels; statement true, repair re-derived; no action beyond the existing FILING FIX 1.
- **Prop 6.2 [ERRATUM]** — L1 (PROMOTED) uses "(14) = the root law" only via Prop 6.3, whose branch satisfies the corrected (ii′); condition (i) is never invoked anywhere in thesis or campaign. File the swap; no downstream damage.
- **St 3.7 [ERRATUM]** — appears only in TEMPLATE's trust-perimeter listing; every actual use imposes κπ(F) ∈ N, which is precisely the missing hypothesis. Benign; file for completeness.

## 4. Supplementary audit beyond the 72-item batch

These items lie after Proposition 6.2 and do not alter the 72-item counts.

- **Prop 6.7 — ERRATUM, complete repair.**  Producer `c3d6ff92...`, Opus5 review `eb37373b...`, and
  correction `050ccddd...` establish the stated conclusion after adding
  `kappa*pi(F) in N`, completing cyclic residual equivariance, using
  corrected Statement 3.11 for the derived terminal polynomial, and closing
  the source's false `h=h_G` shortcut by a tower-prefix/two-case argument.
- **Lemma 6.1 — printed proof incomplete; complete reviewed repair.**
  The print incorrectly infers a nonzero leading Jacobian merely from
  `deg p_(g,F)=0`.  R2 `2fdbbee9...` uses a fixed-pair defect induction to
  keep every ancestor tower nonempty, transports its primitive first
  relation to an axis, and obtains `q^alpha=s*p^beta`; `deg p=1` forces
  `alpha|beta`, impossible.  Opus5 review `5193e7b0...` confirms every
  mathematical step; correction `607e0dcf...` adds the exact common-`K`
  divisibility and `f`/`f-a` positive-leading-data typing.
- **Prop 6.8 — ERRATUM, complete reviewed repair.**  Replace the false printed
  termination bound `d_(F_n)<=u-n/kappa` by
  `d_(F_n)<=d_F-n/kappa`, preserve one fixed grid, and make the final-branch
  ancestry explicit.  Opus5 confirms the repair, and the Lemma 6.1 condition
  is discharged above.  It is the load-bearing microstep-to-next-vertex
  bridge for every Statement 6.2 regularity consumer.
- **Section 7 / Corollary 7.1 — printed equality unproved; inequality
  replacement promoted.**  The literal per-puncture `delta` and Proposition
  7.5 equation `(22)` are not established; the attempted fixed-baseline
  `(22-cl)` also fails because jump/max `kappa` can change between zero and
  nonzero coefficient orbits.  The amended actual-cluster-weight proof
  `c253bd12...` passes Terra gate `727f5850...`: generic weight is the
  maximal jump baseline and every exceptional weight specializes upward by
  a one-point proper-tube comparison.  Euler integration proves exactly
  Corollary 7.1's inequality.  It does not restore either equality or MP8's
  equality-based no-charge claim.
- **Section 8 later-`M` package — complete at corrected scope.**  Source
  audit `5fc6b163...`, Opus review `fa25c8af...`, and the cyclic repair/final
  gate `37b83208...` / `a2b4d37c...` establish Statements 8.4--8.5 and the
  local divisibility package.  Corrected Proposition 8.4 is **nonroot only**;
  at `(0,y)`, `M=1` is permitted and Statement 8.5 gives divisibility alone.
- **Section 9 / Theorem 9.1 — printed proof incomplete; internal
  reconstruction promoted.**  Source audit `2763d970...` and GPT-5.5 review
  `0729a576...` repair the table label, Statement 9.3 sign, case-III
  denominators, omitted zero-charge families and literal nested `Y(F)`
  ownership.  First-separation exit sets plus the actual-weight Corollary
  7.1 close the repaired row-4 graph.  Together with pinned nonroot pole
  kills this proves `counterexample => td>=6` without root Proposition 8.4.
  It does not exclude `td=6`; Zoladek Theorem 6.12 remains the independent
  refereed source for the same lower bound.
