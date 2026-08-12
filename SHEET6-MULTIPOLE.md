# SHEET6-MULTIPOLE.md — the m-pole analogue of Prop 8.4: the maximal printed-tier kill, its exact frontier, and the honest obstruction

**Status: PROMOTED WITH ONE DEMOTION (2026-08-12, SHEET6-MP-REVIEW.md):
MP0-MP8 + Theorem O stand as printed; MP9 stands on corrected ground
(l-independent kappa<nu kill); the "finite book" rider is DEMOTED to
finite-per-parent-frame — chain-frame depth is the sole unbounded axis,
needs a closure lemma (empirically depth-invariant at td=6). Jump-book
parameterization spec: review doc final section.**
Original sYNTHESIS (judge document).** Composite of three panel angles: A1 (piecewise regularity / merge cascade, T0–T7 + obstruction O; NOT REFUTED, 3/3 adversarial votes), A2 (Euler/budget ledger, Theorem M (1)–(5) + Proposition B; NOT REFUTED, 3/3 votes — all theorem clauses explicitly listed as surviving), A3 (merge pattern algebra, Theorem MPM P1–P5 + OB; adversarial record truncated at synthesis time — its clauses cross-derived by A1/A2 are grafted at full tier, its unique clauses quarantined in §7).
**Ground truth:** refs/sigray_full.pdf (printed page = pdf page); page citations below re-read on-page by the panel this session. Prior promoted sheets: SHEET6-2POLE.md, SHEET6-L1.md, SHEET6-LROOT.md, SHEET6-TDUNIFORM.md, SHEET6-A3L1-REVIEW.md.

---

## 0. Verdict in one paragraph

The requested lemma splits along an exact seam, and both halves are now theorems. **Kill half:** for m ≥ 2 poles the printed Prop 8.4 machinery is restored *verbatim* on the shared suffix at and below the global meet G\* of the m characteristic sequences (M_F ≠ 1 there whenever G\* ≠ (0,y)), and is *supplemented* above G\* by a merge calculus: entry M-values are pinned per pole, M = 1 cascades are forced into rigid single-orbit shapes, every merge with an M = 1 arrival has fully pinned anatomy (k = 0, gcd menu), non-resonant merges (l = 0) can never break M = 1, and the entire M = 1 region is budget-transparent (Σλ = 0). **Obstruction half:** the verbatim multi-pole analogue of Prop 8.4 ("M_F ≠ 1 on pre-merge segments") is *FALSE* — M = 1 is FORCED pre-merge whenever the poles enter with b_i = 1 — and the surviving escape hatch is exactly the set of **resonant jump vertices** (merges with l ≥ 1 extra q-orbits and M = gcd-value ≥ 2), which provably pass every printed statement (machine-verified witness at td = 6, m = 2). Theorem MP below is therefore the *maximal* printed-tier statement: it reduces the multi-pole problem, for every (m, td), to a finite book of jump-vertex cells.

---

## 1. Setting and notation

(f,g) a normalized counterexample of type (α,β), 2 ≤ α < β, gcd(α,β) = 1 (Not 2.4/St 2.1, pp. 8–9; the type is global, Lemma 2.1 p. 8). T_{a,pole} = {P_1,…,P_m}, m ≥ 2.

- **C_i** = characteristic sequence of P_i: F_0 = P_i, F_{j+1} = F_j°, terminating at (0,y) (Prop 8.4's construction pp. 44–45; Prop 9.2 p. 50; ° per Not 3.3 p. 12, branch-independent and deterministic).
- **U** := ∪_i C_i, the **chain tree**, partially ordered with root (0,y) at the bottom, poles at the top.
- **r(G)** := #{H ∈ Va ∩ Ta& \ {(0,y)} : H° = G} (in-degree). **Merge vertex**: r(G) ≥ 2. **G\*** := max(∩_i C_i), the global meet (= "G_last"; nonempty since (0,y) ∈ every C_i). **G_i** = first (highest) merge vertex of C_i; **pre-merge segment of C_i** = vertices of C_i strictly above G_i.
- At a merge G with arriving edges from H_e = G + c_e: **μ_e** := mult(p_G^{red}, c_e), **r** = number of arriving bundles, **ν** = ν_G, **l** = number of extra simple ν-orbit families of q_G off the roots of p_G, **k** = number of non-chain roots of p_G.
- **Regularity** = Not 9.2 (p. 48); M_F = gcd(deg p_F, deg p_{h_0,F},…) per Not 8.1 (p. 39); reduced pattern (p,q), i = deg p_F / M\*_F, identity **(iv)**: δpq′ − (1−u)p′q = ⊖p (Prop 8.1, pp. 39–41); λ_F, Y(F), ψ per Not 9.3/St 9.3/9.4 (p. 49); budget Σλ ≤ td − 1 − ψ (St 9.4 (25)–(26), p. 49); Euler identity (22) (Prop 7.5, p. 38).

---

## 2. THEOREM MP (m-pole piecewise kill + merge calculus; hypothesis perimeter §4)

Let T_{a,pole} = {P_1,…,P_m}, m ≥ 2, any td.

**MP0 (chain-completeness).** Ta& ∩ Va \ {(0,x),(0,y)} = U \ {(0,y)}; U is a finite tree under F ↦ F° rooted at (0,y), and its leaves are exactly P_1,…,P_m (no pole has a chain predecessor).

**MP1 (merge counting and localization).** Σ_{G ∈ U, r(G) ≥ 2} (r(G) − 1) = m − 1; hence ≤ m − 1 merge vertices, each with r(G) ≤ m. Not 9.2-regularity fails **exactly** at merge vertices. No merge vertex lies strictly below G\*, and r(G\*) ≥ 2. Every suffix vertex (≤ G\*, ≠ G\*) has a *unique* Ta& ∩ Va predecessor.

**MP2 (restored kill, general m).** If G\* ≠ (0,y), then **M_F ≠ 1 for every F ∈ U with F ≤ G\*** (trunk and G\* itself). The printed Prop 8.4 proof (pp. 44–45) runs verbatim; the singleton hypothesis is needed only above the last merge.

**MP3 (exact escape set).** The vertices escaping MP2 are exactly {F ∈ U : F > G\*}: ALL strict ancestors of G\* — pre-merge segments, inter-merge segments, and merge vertices above G\*. (Not merely "the first vertex above each merge": the M = 1 contradiction is manufactured only at (0,y), so no per-segment rerun of Prop 8.4 exists.)

**MP4 (entry pin; td- and m-uniform).** At every pole, (deg p_{P_i}, deg p_{g,P_i}) = b_i(α,β) and **M_{P_i} = b_i = deg p_{P_i}/α**. Moreover b_i = 1 (hence M_{P_i} = 1) is FORCED when Λ(P_i) = β (β-minimal pole) and when Λ(P_i) is prime. In particular at the minimal m-pole degree td = mβ, ALL entries have M = 1.

**MP5 (forced M = 1 propagation — the naive analogue is false, maximally).** If M_F = 1 at a pre-merge vertex of C_i (e.g. F = P_i when b_i = 1), then every C_i-vertex from F down to the last pre-merge vertex has reduced pattern a single SIMPLE ν-orbit (dp = ν, dq = nν + 1, n ≥ 1), M = 1, λ = 0, no ray of T_a separating there; the chain arrives at G_i with μ_i = 1. M = 1 likewise propagates down every merge-free segment (Prop 8.3(i)) and through every M = 1-emitting merge.

**MP6 (merge anatomy).** No merge vertex is a pole vertex. At a merge G with at least one arriving μ_e = 1 (automatic for any M = 1-ancestry arrival, since μ_e | M_{H_e} by St 8.4):
 (a) **k = 0**: every root of p_G carries an incoming chain; no non-chain roots, searrow or northeast; the roots are exactly the r arriving directions;
 (b) **equal-quotient law**: deg p_{H_e} = i·μ_e with one common i ≥ 2 for all e;
 (c) **q-shape** [P2]: q = η·rad(p)·Π_{s=1}^{l}(η^ν − b_s^ν) for ν ≥ 2 (η-factor absorbed at ν = 1), all q-roots simple;
 (d) **gcd menu**: dq ≡ 1 (mod ν), hence **gcd(M_G, ν_G) = 1** always; with no 0-chain, **M_G = gcd(Σ_e μ_e, (r+l)ν + 1)**, so M_G | Σ_e μ_e ≤ Σ_e M_{H_e} (subadditivity). All-μ=1 families: **IIa**: (dp,dq) = (rν, (r+l)ν+1), M_G = gcd(rν,(r+l)ν+1) **= gcd(r, lν+1)**; **ZCH** (one chain at the 0-direction): (dp,dq) = ((r−1)ν+1, (r−1+l)ν+1), M_G = gcd((r−1)ν+1, l); **I** (ν = 1): (dp,dq) = (r, r+l), M_G = gcd(r, l). Corollary: outside ZCH, **M_G | r ≤ m**;
 (e) **λ_G = 0**: no northeast direction exists and the l extras carry no tree vertex.

**MP7 (no-resonance kill and jump existence).** l = 0 at an all-M=1 merge forces M_G = 1 (IIa: gcd(r,1)) or is impossible outright (ZCH and ν = 1: q = p forces p′ = const ≠ 0 in (iv), i.e. deg p = 1 — contradiction). Hence an all-M=1 merge either emits M = 1 (cascade continues) or is a **resonant jump**: l ≥ 1 and 2 ≤ M_G ≤ r(G) ≤ m in the non-0-chain families. Consequently: if all entries have M = 1 (forced at td = mβ, or all Λ_i prime, by MP4), then either G\* ≠ (0,y) and at least one resonant jump vertex with the full MP6 anatomy exists at or above G\*, or G\* = (0,y) and the **root merge** itself has the all-μ=1 anatomy at ν = 1 (St 9.2(ii)) with k = 0, l ≥ 1, M = gcd(r,l), and the top-cancellation pin **k_f = (r+l)·l_f**, ψ = r+l−1 in St 9.4.

**MP8 (budget transparency — the obstruction's mechanism).** On the pure M=1 forest {F ∈ U : M ≡ 1 at F and at every U-vertex above F} and at every all-M=1 merge vertex (including jumps): Y(F) = ∅ and λ_F = 0. Itemizing the Euler equality (22) (Prop 7.5, p. 38) for m poles: pole clusters, chain paths, M=1 segments, and μ=1-arrival merges all contribute identically zero rows. Hence **no refinement or re-partition of any printed budget** (St 9.4/9.5 (25)–(26) p. 49, Cor 7.1 p. 39, identity (22)) can charge M=1 pre-merge ancestry even one unit, for any m and any td. The only printed per-pole cost is Λ-mass: td = ΣΛ_i ≥ mβ ≥ 3m (Props 5.7/5.8), i.e. m ≤ td/3.

**MP9 (m = 2, b = (1,1) sharpening; td-uniform).** Both chains are M=1/λ=0 single-simple-orbit to the meet, μ = (1,1).
 (Interior meet, G\* ≠ (0,y)): M_{G\*} = gcd(2, lν+1) must equal 2 (else MP2 kills), forcing l odd ≥ 1 and ν odd. ν = 1 is impossible: l even contradicts (iv) by the exact log-obstruction (all even l — upgrades SHEET6-L1 §4 beyond engine caps), l odd gives M = 1, killed by MP2. Survivors: exactly **IIa(l odd, ν ≥ 3 odd), M = 2** or **ZCH with gcd(ν+1, l) ≥ 2** — at total pre-merge + merge spend 0. [Cap flag: the ν = 1 variant with an η-factor in q is excluded only for l ≤ 4.]
 (Root meet, G\* = (0,y)) [+H1 for the last clause]: l = 0 impossible (q = p gives 0 = ⊖p ≠ 0 in (iv)); l even impossible (same log-obstruction, ν = 1 by St 9.2(ii)); residual: l odd, locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2 ≠ 0, exact), with k_f = (2+l)·l_f, ψ = l+1, and l ≤ td − 2 (Σλ = 0 in St 9.4 (25)); Prop 9.3(d) with child data (ν,κ̄,D) = (1,1,l_f) forces **κ̄ < ν at both parents** (the case-IV corner, 2POLE §4b). Empty at td = 6 by reach (2POLE §5b phase 3); OPEN at general td.

**OBSTRUCTION O (honest half; sharp).** The verbatim multi-pole analogue of Prop 8.4 is FALSE at printed tier: at td = 6, m = 2, both poles are row 1 of table (23) (p. 46) with M_P = gcd(2,3) = 1 *forced*, all pre-merge vertices have M = 1 *forced* (MP5), and the resonant jump (r,ν,l) = (2,3,1) with M = 2 solves the printed identity Prop 8.1(iv) *exactly* with rigid coefficients (a₁/a₂ = 2±√3; cases/l1_ode_check.py; SHEET6-L1 §5, SHEET6-2POLE §6a, machine-verified), at Σλ(pre-merge ∪ merge) = 0, passing every located printed constraint. The L1 §3 blind spot is r-uniform: the l extra q-orbits sit at non-roots of p, carry no tree vertex, no puncture, no cv vertex, no λ, no pole — nothing printed sees them except deg q. At pattern level the escape is m-uniform: for every m, choosing lν ≡ −1 (mod m), ν odd, gives M_{G\*} = m at spend 0 (arithmetic existence only; r-edge H1 ratio-consistency unverified for m ≥ 3). Hence the MP7 residual is irreducible from the printed statement list, and MP0–MP9 is the exact printed-tier frontier.

---

## 3. Derivation

All page numbers: refs/sigray_full.pdf, printed page = pdf page. The printed inventory used is listed once: St 2.1/Not 2.4 (pp. 8–9); Not 3.3 (p. 12); St 3.9 (p. 15); St 3.16 (p. 17); Prop 3.2/St 3.17/3.18 (p. 18); Prop 4.2 (p. 19); Prop 5.1/Not 5.1–5.2 (pp. 23–25); Prop 5.3 (p. 25); St 5.2 (p. 26); Props 5.5–5.8 (pp. 26–28); Thm 6.1 (p. 28); Not 6.1/St 6.1–6.2 (p. 29); Props 6.7/6.8 (pp. 33–34); Not 7.1/St 7.1–7.3 (p. 35); Prop 7.2 (p. 36); Prop 7.5 (22) (p. 38); Cor 7.1, Not 8.1, St 8.1, Prop 8.1 (pp. 39–41); St 8.2–8.5 (pp. 41–43); Cor 8.1, Props 8.2–8.4 (pp. 43–45); table (23) (p. 46); Not 9.1–9.2, St 9.1–9.4 (pp. 48–49); Prop 9.2 (p. 50).

### D1 (MP0)
(⊇) Each C_i ⊆ Ta& ∩ Va: the printed Prop 8.4 proof line (p. 45) "From Propositions 6.7 and 6.8, we obtain F_0,…,F_n ∈ Ta&" applies from F_0 = P_i — nothing in the construction uses |T_{a,pole}| = 1 (2POLE §1b); poles are in Ta& (d > 0 and deg p ≥ 2 by Prop 5.3(iv)–(v) + St 3.16), and Va-membership descends via Not 3.3(i).
(⊆) Any H ∈ Ta& ∩ Va \ {(0,x),(0,y)} has deg p_H ≥ 2 (St 3.16: p has more than one root). Prop 6.8 (p. 34, verbatim: "there exist P, u, v: F = I_P(u), v ≥ u, I_P(v) ∈ T_{a,pole}" — the pole lies above H on the SAME branch) gives I_P(v) = P_s. Not 3.3's ° enumerates every Va-vertex of I_P([0,v)) in decreasing order, branch-independently; H is one of them, so H ∈ C_s.
Leaves: a chain predecessor H of P_j would give deg p_H = mult(p_{P_j}, c) ≥ 2 (St 3.17(i) + St 3.16), contradicting squarefreeness of p_{P_j} (Prop 5.3(v)). So poles have in-degree 0; every non-pole U-vertex is some F°; leaves(U) = {P_1,…,P_m}. ∎

### D2 (MP1)
U is a finite tree: every vertex except (0,y) has the unique out-edge F → F° (Not 3.3 deterministic). Counting edges: Σ_G (r(G) − 1) = −1 over all of U with r = 0 exactly at the m leaves, so Σ_{r ≥ 2}(r − 1) = m − 1. By D1 the Not 9.2-predecessor set of G equals its U-predecessor set, so regularity ⇔ r(G) = 1. No merge strictly below G\*: below the meet all chains coincide (° deterministic; Not 3.3 betweenness excludes side entries from ≥ G\*); r(G\*) ≥ 2 by maximality of G\*. Unique-predecessor at suffix vertices (A2's complement): a second predecessor H′ of a suffix vertex S would, by St 3.16 + Prop 6.8, lie under some pole P_j; C_j visits H′ and continues to S (Prop 3.2 determinism), yet C_j also passes through G\* and reaches S through the trunk — a characteristic sequence is a simple descending path and cannot contain two predecessors of one vertex. Contradiction. ∎

### D3 (MP2, MP3)
Take F ≤ G\*, M_F = 1, G\* ≠ (0,y). Every step of the descent from F is regular (D2), so Prop 8.3 (p. 44, under the P1 reading of its hypothesis) applies inductively: M = 1 all the way down, with 8.3(ii) at interior steps and 8.3(iii) at (0,y): p_{(0,y)} = (η−c)^k, a single root ((0,y) is not a merge since G\* ≠ (0,y), and a second root direction would violate D2's unique-predecessor claim). The printed Bezout endgame (p. 45) then runs verbatim: St 8.1 combination at H = F_{n−1}, (k,l) = w(k_f,l_f) via Cor 6.1 + Prop 6.3; the k-computation's deg = mult steps are valid precisely because every p_{h_j,(0,y)} is evaluated at the single root (this is where 8.3(iii) is load-bearing); k = 1, l = l_f/k_f ∈ ℕ contradicting Thm 6.1 (l_f < k_f, p. 28). Nothing mentions |T_{a,pole}|. — Escape exactness: for F > G\*, the arrival step into the first merge at latest G\* is non-regular (D2), Prop 8.3 is inapplicable there, and since the contradiction lives only at (0,y), no vertex above G\* is killed by this route; conversely all F ≤ G\* are killed. ∎

### D4 (MP4)
Poles have m_F = 0 (Prop 5.1(i) + Not 5.1/5.2), so the h-family is {g} (Prop 4.2) and M_{P_i} = gcd(deg p_{P_i}, deg p_{g,P_i}) (Not 8.1). St 5.2(i): deg p/deg p_g = α/β at poles, so (deg p, deg p_g) = b_i(α,β) and M_{P_i} = b_i·gcd(α,β) = b_i = deg p_{P_i}/α. (Check: reproduces all 11 rows of table (23), p. 46, and St 9.6's printed M = 2 = gcd(4,6).) β-minimal: Λ(P) = a b αβ/ν (Prop 5.6 (19)) = β forces ν = abα; St 5.2(ii): ν | α ⇒ ab = 1 ⇒ b = 1; ν | β ⇒ abα | β with gcd(α,β) = 1 ⇒ α = 1, contra St 2.1. Prime Λ: case ν | α: Λ = ab(α/ν)β divisible by β ≥ 3, so Λ = β and a = b = α/ν = 1; case ν | β: Λ = abα(β/ν) divisible by α ≥ 2, so Λ = α < β ≤ Λ (Prop 5.7) — empty. Since the type (α,β) is global (Lemma 2.1), this is per-vertex, valid at every td — repairing the Λ = td-dependence of SHEET6-TDUNIFORM §2. ∎

### D5 (MP5)
Downward induction from an M = 1 pre-merge vertex H, K = H° still pre-merge: (a) St 8.4 (p. 42) at the pair (K, H = K + c): mult(p_K^{red}, c) | M_H = 1 — the chain orbit is simple. (b) St 8.2 (p. 41) at that μ = 1 arrival: deg q_K > deg p_K; then for every root c′ of p_K, deg q·mult(p,c′) ≥ deg q > deg p, so every root is searrow — **no northeast roots exist at K at all**. (c) A non-chain root c′ would give the tree vertex K ∗ εc′ (St 3.18; the 0-root always continues) with, by St 3.9(iii) + St 3.17(i) + Prop 8.1(i) + the St 6.2 computation (p. 29), K ∗ εc′ ∈ Ta& and deg p = i·mult(p^{red}, εc′) ≥ i ≥ 2; Prop 6.8 then manufactures a pole above it **on that branch** — necessarily one of the m poles of T_{a,pole} (this consumes no pole budget, which is why it scales to every m, replacing L1a's m=2-only third-pole counting); that pole's chain visits K through direction c′ (Not 3.3/Prop 3.2), making K a merge vertex — contradiction with K strictly pre-merge. So p_K = single simple ν-orbit, dp = ν. (d) Root law + eta law [P2] (exact order/residue counting on (iv): at a p-root of mult μ, mult(q) = 1 forced; off-p q-roots simple; η-residue b ≡ 1 mod ν): dq = nν + 1, M_K = gcd(ν, nν+1) = 1 — verbatim the thesis's own step in St 9.6's proof (p. 52). (e) λ_K = 0: no direction in Ta% exists (b); the q-extras at non-roots of p have no tree continuation (St 3.18). (f) No ray separates: all full-pattern roots lie in one ν-orbit with a unique continuing representative (St 3.18; Prop 5.6's proof, p. 27). At the merge arrival: St 8.4 at (G_i, H_i) gives μ_i = 1. ∎

### D6 (MP6)
Merge ≠ pole: an arriving direction has full multiplicity deg p_{H_e} ≥ 2, contradicting Prop 5.3(v) squarefreeness. Let some μ_j = 1. (a) k = 0: exactly the D5(c) manufacture, now read at G — every root of p_G supports, via Prop 6.8's same-branch pole, an incoming chain of one of the m poles; the roots of p_G are precisely the r arriving directions, in distinct ν-orbits (St 3.18: one continuation per orbit). (b) Equal-quotient: deg p_{H_e} = mult(p_G^{full}, c_e) = i·μ_e (St 3.17(i) + Prop 8.1(i): p^{full} = ⊖p^i); with μ_j = 1, i = deg p_{H_j} ≥ 2. (c) q-shape by root/eta laws [P2] as in D5(d). (d) Arithmetic: dq = (r+l)ν + 1 ≡ 1 (mod ν) forces gcd(M_G, ν) = 1 (Prop 8.1(v): M_G = gcd(dp, dq)); with dp = (Σμ_e)ν, any common divisor is coprime to ν hence divides Σμ_e: M_G = gcd(Σμ_e, (r+l)ν+1) | Σμ_e ≤ ΣM_{H_e} (St 8.4). All-μ=1 IIa: d | (r+l)ν+1 ⇒ gcd(d,ν) = 1 ⇒ (d | rν ⇔ d | r), and (r+l)ν+1 ≡ lν+1 (mod d): **gcd(rν,(r+l)ν+1) = gcd(r, lν+1)** exactly (A1's "divides" upgraded to A2/A3's equality; elementary both ways). ZCH: dp = (r−1)ν+1, difference lν, coprimality to ν gives M = gcd((r−1)ν+1, l). ν = 1: q = p·s, M = gcd(r, r+l) = gcd(r,l). (Machine-swept: r ≤ 9, ν ≤ 12, l ≤ 12, mixed μ-vectors; reproduces every recorded engine cell — (2,3,1) → 2; ZCH (2,2,3) → 3; ν=1 (2,l=2) → 2.) (e) λ_G = 0 as in D5(e). ∎

### D7 (MP7)
l = 0 kills: IIa: M = gcd(r,1) = 1. ZCH/ν=1: l = 0 forces q = p, and (iv) becomes (δ−1+u)pp′ = ⊖p, i.e. p′ = const ≠ 0, i.e. deg p = 1 — below ν+1 resp. 2 ≤ r: impossible. Cascade: Prop 8.3(i) propagates M = 1 down merge-free segments (regular steps, D2); at an M = 1-emitting merge the cascade continues (M_G = 1 known by direct gcd; steps below regular until the next merge). If the cascade reaches G\* with M = 1 and G\* ≠ (0,y), D3 gives the contradiction — so some merge at or above G\* breaks M = 1: a jump, with the D6 anatomy, and (all entries M = 1 ⇒ the FIRST break is an all-μ=1 merge) the resonance l ≥ 1 and 2 ≤ M ≤ r ≤ m outside ZCH. Entry forcing is D4. Root merge: (0,y) ∈ Ta& (d = l_f < k_f = deg p_{(0,y)}, Thm 6.1 read as the Ta&-inequality at π = 0), so D6 applies at (0,y) with ν = 1 (St 9.2(ii)); top-cancellation of (iv) (St 8.2's proof computation, forced since dq ≥ 2, u = 0, δ = l_f/i) gives l_f = i·r/(r+l) and k_f = i·r, hence **k_f = (r+l)·l_f** and ψ = ⌈k_f/l_f⌉ − 1 = r+l−1 (St 9.4). Prop 8.3(iii) fails (r ≥ 2 roots): no M = 1 kill at the root merge. ∎

### D8 (MP8)
Claim: every branch P ∈ Ra\R̄a through the pure M=1 forest or an all-M=1 merge has F\*_P ∈ T_{a,pole}. Ascend along P: at segment vertices the full pattern is a single simple orbit (D5), at all-M=1 merges all roots are chain roots (D6a), at poles the branch either separates above (where deg p = 1 by St 3.17(i) + Prop 5.3(v), and St 3.16 excludes Va-membership there and above) or continues along the defining branch (Prop 5.3(ix)). So P passes through a pole vertex Q₀, and since m_F is a vertex invariant, F\*_P = Q₀ ∈ T_{a,pole}. St 7.2 (p. 35) then bans cv vertices on P; Y(F) = ∅ (literally when M = 1 holds from the pole down: every ray through the segment reaches P_i, g(P) = ∞ by Prop 5.5, no cv vertex by Prop 7.2; under the E9/H2 branch-at-F reading for mid-segment onset); λ_F = 0 (St 9.3 (24)). Ledger itemization of the equality (22), extending SHEET6-LROOT §1 to m poles: (i) pole clusters carry zero cv mass (Prop 5.5 + Prop 7.2, per pole); (ii) chain paths carry none (T_{a,cv} ⊂ T_a^0 = {d = 0}, Not 7.1, while d > 0 down to d_{(0,y)} = l_f > 0); (iii) M=1 pre-merge sub-segments: identically zero rows (D5(f)); (iv) μ=1-arrival merges: zero rows (D6e) — the l q-extras are exhibited EMPTY ledger rows; (v) the x-side keeps its ≥ ψ cost (St 9.4's proof, p. 49). Since (22) is an Euler-characteristic *equality*, no re-partition or refinement of the printed counting frame can price these objects: "≥ 1 unit per M=1 occurrence" is structurally false at every m, td. The only remaining per-pole cost is td = ΣΛ_i ≥ mβ (Props 5.7/5.8): m ≤ td/3. ∎

### D9 (MP9)
m = 2, b = (1,1): D5 forces both chains M=1/λ=0 single-orbit, μ = (1,1) at the meet. Interior meet: r = 2 in D6d, M = gcd(2, lν+1); M = 1 is killed at G\* by D3, so M = 2, i.e. lν odd: l odd ≥ 1 (l = 0 gives gcd(2ν, 2ν+1) = 1), ν odd. ν = 1: (iv) reduces to 2ps′ − l p′s = c′ ≠ 0 (ρ = 2/(2+l), L1 §4's reduction re-derived); l even: divide by p^{(l+2)/2} — (s·p^{−l/2})′ = (c′/2)p^{−(l+2)/2}, whose partial-fraction residue at each root is C(−n, n−1)(a₁−a₂)^{1−2n} with n = (l+2)/2 and C(−n,n−1) = (−1)^{n−1}·C(2n−2, n−1) ≠ 0 for ALL n ≥ 2 (exact; machine-verified n = 2..6) — a log term, so no rational s exists unless c′ = 0, contra ⊖ ≠ 0. This holds at ALL even l, td-uniformly (upgrading L1b beyond its engine caps). l odd gives M = gcd(2, 2+l) = 1, killed. Survivors: IIa(l odd, ν ≥ 3 odd) / ZCH(gcd(ν+1,l) ≥ 2) — exactly the L1 §3 blind-spot family, spend 0. Root meet: ν = 1 (St 9.2(ii)); l = 0: root law gives q = p and (iv) reads 0 = ⊖p ≠ 0 — impossible; l even: the same log-obstruction (u = 0 changes nothing); l odd: locally solvable at l = 1 (s = t − (a₁+a₂)/2, c′ = −(a₁−a₂)²/2, machine-verified exact), no M = 1 kill (Prop 8.3(iii) fails: two predecessors); printed pins: k_f = (2+l)l_f (D7 at r = 2), ψ = l+1 admissible, Σλ = 0 ⇒ l ≤ td−2 (St 9.4 (25)); [+H1] Prop 9.3(d) with child (ν,κ̄,D) = (1,1,l_f) gives 1 = (κ̄_i + n_i)/ν_i, n_i ≥ 1, so κ̄_i ≤ ν_i − 1 at both parents. td = 6: empty by reach (2POLE §5b phase 3). ∎

---

## 4. Honest hypothesis perimeter

**Sanctioned hypotheses (all clauses):**
- **P1** — Prop 8.3's hypothesis read as Not 9.2-regularity (known printed typo; sanctioned SHEET6-2POLE §1b). Load-bearing in D3, D7.
- **P2** — root/eta laws as exact order/residue computations on the printed identity Prop 8.1(iv) (derivation in D5(d)/D6(c); promoted tier per SHEET6-A3L1-REVIEW). Load-bearing in D5–D7, D9.
- **P3** — y-side convention: characteristic sequences terminate at (0,y) as printed (Prop 9.2 p. 50; (0,x) ∈ Ta% per St 9.4's proof p. 49).
- **P4** — entry pin chain: Not 8.1 + Prop 5.1(i)/Not 5.1–5.2 + St 5.2(i) + St 2.1 (D4).

**Clause-local hypotheses:**
- **E9/H2** (branch-at-F reading of λ): needed in MP8 only for *mid-segment* M = 1 onset; when M = 1 holds from the pole down, Y(F) = ∅ holds in the literal Not 9.3 reading.
- **H1** (Prop 9.3(a)–(d) printed-step arithmetic): used only in MP9's root-residual κ̄ < ν clause.

**Engine caps (flagged, not closed):** the ν = 1 interior-merge variant with an η-factor in q (legal only at ν = 1) is excluded only for l ≤ 4 (cases/l1_ode_check.py families B/B-η).

**Open, stated, NOT claimed:** mixed merges with all μ_e ≥ 2 obey only MP6(b)/(d)-subadditivity (k = 0 needs some μ_e = 1; the l ≥ 1 forcing does not apply) — possible only for m ≥ 3 downstream of an earlier jump; the m ≥ 3 pattern-level escape (M = m via lν ≡ −1 mod m) is arithmetic existence only, r-edge H1 ratio-consistency unverified; the root-merge endgame at general td is open (closed at td = 6, m = 2); jump vertices are unkillable at printed tier (witness O — this is a theorem-grade negative, not a gap in the proof).

**Record caveats:** (i) A2's third adversarial vote flagged one *subsidiary* (non-load-bearing) sub-claim as failing and one unflagged record-contradiction; the vote explicitly lists all Theorem M clauses (1)–(4), (5I), the conditional content of (5R), and Prop B as surviving, and every A2 clause grafted here is cross-derived by A1 or so listed. (ii) A3's adversarial votes were truncated in the synthesis input; A3 clauses P1/P3/P4 are independently derived by A1/A2 and grafted at full tier; A3-unique kills are quarantined in §7.

---

## 5. The obstruction half, stated precisely

**Theorem O.** No printed-tier argument can prove M_F ≠ 1 on pre-merge segments (it is false: MP5 forces M = 1 there whenever b_i = 1, which is itself forced at td = mβ and at prime Λ_i), and no printed-tier argument can exclude resonant jump vertices: the cell (r,ν,l) = (2,3,1), M = 2 at td = 6, m = 2 solves Prop 8.1(iv) exactly with rigid coefficients (a₁/a₂ = 2±√3), passes Prop 8.1(iv)-(v), St 8.2/8.4, the root/eta laws, all located budget statements (Σλ = 2 ≤ 3 globally, 0 through the merge), and the entry pins — machine-verified (cases/l1_ode_check.py; SHEET6-2POLE §6a full hand-verified exhibit, every datum absolute). The blind spot is structural and r-uniform: the l extra q-orbits are invisible to every printed statement except deg q (SHEET6-L1 §3). Combined with MP8 (spend 0), the residual is irreducible: **MP0–MP9 is the maximal printed-tier kill**, and the multi-pole problem reduces, for each (m, td), to the finite book of resonant jump cells pinned by MP6/MP7 + the equal-quotient law + Prop 9.3's per-edge ratio equations (pp. 50–51), with entries pinned by MP4.

---

## 6. Refuted attempts (one line each)

1. **Verbatim m-pole Prop 8.4** ("M_F ≠ 1 on pre-merge segments"): FALSE — MP5 proves M = 1 is *forced* there whenever b_i = 1; witnessed forced at td = 6 (row 1 of table (23), M = gcd(2,3) = 1).
2. **Per-segment piecewise restoration** ("rerun the printed induction on each pre-merge segment; only the first vertex above each merge escapes"): wrong — the contradiction is manufactured only at (0,y), so ALL strict ancestors of G\* escape, including inter-merge segments (MP3).
3. **Budget kill** ("each M = 1 occurrence costs ≥ 1, so ≤ td−2 occurrences"): structurally false — the region contributes identically zero rows to the Euler *equality* (22) and Σλ = 0 there; no re-partition of any printed budget can charge it (MP8/Prop B).
4. **λ_root ≥ 1 transported to m poles** (the LROOT-style 8→4 route): dead — λ = 0 is forced at all-M=1 merges and at the root merge (MP8, generalizing SHEET6-LROOT §2 to all m).
5. **Non-resonant jump** (M ≥ 2 at a merge with l = 0): impossible — l = 0 forces M = 1 (IIa) or contradicts Prop 8.1(iv) outright (ZCH, ν = 1) (MP7).
6. **ν = 1 interior jump at m = 2**: dead at all l — even l by the exact log-obstruction (all l, beyond L1b's caps), odd l by M = 1 + MP2; only the η-factor subvariant remains cap-limited (l ≤ 4).
7. **Killing the jump vertex itself from printed statements**: impossible — the (2,3,1) M = 2 cell is a consistent exhibit solving every located printed constraint (Theorem O).
8. **Λ = td pin transport** (TDUNIFORM §2 verbatim at multi-pole): fails as stated (Λ(P_i) < td); rescued only by the per-pole β-minimal/prime-Λ argument via the *global* type (MP4/D4).

---

## 7. Supplementary kills at A3 tier (quarantined pending recorded adversarial confirmation)

From Theorem MPM (pattern-algebra angle; statement complete in the panel record, votes truncated at synthesis). These sharpen the jump book but are NOT counted in Theorem MP:
- **Prime-partition kill (P2):** Λ(P_i) prime forces a_i = b_i = 1, β = Λ(P_i), ν_i = α | Λ(P_i) − 1; hence no counterexample has two pole vertices with distinct prime Λ-parts (e.g. two-pole partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 excluded outright), and a prime part p forces p | Λ_j for every other part unless ν_j = p, p | b_jα − 1, Λ_j = a_j b_j α.
- **RH-lemma kills (P5):** n_q − 1 ≤ D_min for searrow reduced patterns; saturated IIa cells with (lν+1) | r die (e.g. (3,2,1), (4,3,1), (5,4,1)); ν = 1 merges with gcd(r,l) ≥ 2 and (r | l or l | r) die (reproves L1b uniformly, extends to all r; no ν = 1 emission of M ≥ 2 for r ≤ 3); full-M ZCH cells (M = (r−1)ν+1) die; IIa l = 1 exists iff (ν+1) ∤ r, with a rigid one-scale closed form.
- **OB extension:** cells (3,5,1) M = 3 and (4,7,1) M = 4 solve Prop 8.1(iv) with admissible coefficients (machine-verified per A3) — candidate m = 3, 4 consistent exhibits.
**Action:** re-referee these three blocks (their derivation exists in the panel record through P2 case analysis; the machine check /tmp/mpm_check.py is session-local and must be rebuilt under cases/).

---

## 8. The sharpest remaining gap, and the concrete next step

**The gap.** Everything printed now funnels into a single residual object: the **resonant jump vertex** — an all-M=1 merge with l ≥ 1 extra simple q-orbits, M = gcd(r, lν+1) ≥ 2 (or its ZCH/mixed analogues), spend 0, whose l extras no printed statement can see (Theorem O). For m = 2 this is exactly IIa(l odd, ν ≥ 3 odd, M = 2) / ZCH(gcd(ν+1,l) ≥ 2) at an interior meet, plus the root-meet l-odd residual; for m ≥ 3 the cells lν ≡ −1 (mod m) exist at pattern level but their *reachability* (r-edge ratio consistency) is untested. The kill, if one exists, must come from the H1 layer that the printed statements stop short of: matching the rigid (iv)-coefficients of a jump cell against the per-edge Prop 9.3(a)–(d) ratio equations of ALL r incoming chains simultaneously — a computation never yet run for any cell (the l = 1 rigidity a₁/a₂ = 2±√3 shows the coefficients are fully pinned, so the match is a finite check per cell).

**Concrete next step (ordered, engine-able):**
1. **Build the r = 3 jump-cell reachability check**: extend cases/l1_ode_check.py + cases/twopole_check.py to r = 3 incoming edges; impose Prop 9.3(a)–(d) per-edge (H1 tier) plus the equal-quotient law and entry pin at the cell (r,ν,l) = (3,5,1), M = 3, in the minimal m = 3 configuration td = 3β. Outcome either way is decisive: a ratio-inconsistency kills the first m ≥ 3 escape cell and gives the template for the whole book; consistency produces the m = 3 exhibit and sharpens Theorem O to m ≥ 3.
2. **Close the m = 2 root-merge residual at td = 7, 8** (l odd, k_f = (2+l)l_f, both κ̄ < ν) by the reach method of 2POLE §5b phase 3 — the only MP9 clause still td-bounded.
3. **Run the coefficient-vs-ratio match for the td = 6 cell (2,3,1)**: the exhibit's pinned pattern coefficients against both parents' Prop 9.3 edge data — the single most valuable H1-tier computation, since this cell is the minimal consistent example anchoring the entire obstruction.
4. **Promote §7**: referee the A3 prime-partition and RH kills; if confirmed, they delete the partitions 8 = 3+5, 10 = 3+7, 12 = 5+7 and all saturated cells from the book before any engine run.

---

## 9. Cross-consistency notes (grafting record)

- A1.T2 = A2(4) (restored kill; A2's unique-predecessor argument adopted into D2/D3 as the cleaner single-root justification at (0,y)). A1.T4/T5 = A2(3) = A3.P4 (merge anatomy; independent derivations agree cell-by-cell). A1.T5's "M_G | gcd(r, lν+1)" upgraded to A2/A3's equality (elementary proof in D6d). A1.T6's root pin ψ = r+l−1 ⟷ A2(5R)'s ψ = l+1 at r = 2: consistent. A1.T7 = A2.Prop B (budget transparency; A2 adds the Euler-equality itemization, A1 adds the F\*_P ∈ T_{a,pole} branch argument — both used in D8). A1's G\* = A2's G_last (max ∩C_i). A2(1) prime-Λ pin subsumes A1's β-minimal pin; both in MP4.
- Escape-set adjudication: A1.T3's correction (ALL strict ancestors of G\* escape) supersedes any "first-vertex-above-merge" phrasing; A2(2)'s "pre-merge segment" forcing and A2.P3's inter-merge propagation condition are compatible refinements.
- The k = 0 manufacture (D5c/D6a) is the load-bearing novelty in both A1 and A2, derived independently with the same printed chain (St 6.2 computation + St 3.9(iii)/3.17(i)/8.1(i) + Prop 6.8 same-branch); its no-pole-budget character is what makes Theorem MP m-uniform.

## 10. Reproduction

- Printed ground truth: refs/sigray_full.pdf pp. 8–9, 12–19, 23–29, 32–36, 38–46, 48–52 (all re-read on-page by the panel).
- Machine checks: cases/l1_ode_check.py (jump-cell rigidity, families incl. B/B-η caps); cases/twopole_check.py (2POLE §5 phases); cases/lroot_ledger.py (ledger itemization template for D8); gcd sweeps r ≤ 9, ν ≤ 12, l ≤ 12 + mixed μ-vectors and the log-obstruction residues C(−n, n−1), n = 2..6 (panel sessions; A3's /tmp/mpm_check.py to be rebuilt under cases/ per §7).
- Prior sheets: SHEET6-2POLE.md §§1–6, SHEET6-L1.md §§0–7, SHEET6-LROOT.md §§1–5, SHEET6-TDUNIFORM.md §§1–8, SHEET6-A3L1-REVIEW.md.