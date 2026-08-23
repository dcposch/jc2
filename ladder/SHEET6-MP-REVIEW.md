# SHEET6-MP-REVIEW.md — Adversarial review of SHEET6-MULTIPOLE.md (0827409), the Theorem MP synthesis

Reviewer: Claude (adversarial synthesis-grafting pass, 2026-08-12). Status:
COMPLETE. Scope: the SYNTHESIS layer only — the per-angle A1/A2 contents were
adversarially voted inside the workflow (3/3 each) and their records are NOT
in the repo; this review therefore audits (a) the doc's own provenance map
(§3 D-derivations + §9 grafting record) clause by clause, (b) whether the
grafted clauses COMPOSE, by full re-derivation at the concrete instance
(m, td) = (2, 6) against the promoted SHEET6-2POLE/SHEET6-L1 record, (c) the
six load-bearing page citations on-page, (d) the obstruction witness, (e) the
reduction/finiteness rider. Ground truth: refs/sigray_full.pdf re-read
on-page this session (pp. 26–28, 34, 38–52). Engines re-run:
cases/twopole_check.py phases 1–4 (all counts byte-match SHEET6-L1 §6:
133 / 47970 / 552 / 0 root; phase 4: 26 / 18427 / 17199 / 601 / 276 / 351,
unique residue child (ρ,ν,M,κ̄) = (1/2,3,2,5)), cases/l1_ode_check.py
(families A/B/B-η/Z/C reproduced exactly). PLUS an independent exact checker
written for this review (/tmp/mp_check.py; no shared code): MP6(d) menu,
MP7 kill, MP9 parity + log-residues, MP7 root pin, and a raised-caps
κ̄-vs-ν sweep over the M=1 chain tree. ALL CHECKS PASS.

Verdicts:
- Front 1 (clause provenance + quarantine): **CONFIRMED, two flags** (no
  §7 leak found; every MP clause has an in-doc derivation D1–D9 standing on
  printed statements + sanctioned P1/P2, so provenance risk is contained
  even where the panel record is truncated; flags in §1)
- Front 2 (composition at m = 2, td = 6): **CONFIRMED with one citation
  correction** (MP4→MP5→MP6→MP7 reproduces the promoted record exactly —
  entry row 1, μ=(1,1), the 3-shape menu clause-for-clause, merged child
  (6,12,3,2,5) unique; the MP9 root-meet td=6 citation names the wrong
  ground — kill re-established independently here, §2c)
- Front 3 (page fidelity, 6 citations): **CONFIRMED, 6/6 verbatim** (§3)
- Front 4 (obstruction half): **CONFIRMED** (witness located, re-verified,
  b_i = 1 doubly forced, and it IS the promoted residue-A object) (§4)
- Front 5 (reduction claim): **DEMOTED** — the "finite book per (m, td)"
  rider (§0, §5 of the doc) is proven only per parent frame; global
  finiteness needs an unproven chain-closure lemma, and the doc's own MP8
  shows no printed budget can supply it (§5; parameterization spec §5c)
- Front 6 (mechanization): **DONE, ALL PASS** (/tmp/mp_check.py, §6)

Net: **MP0–MP8 stand as printed. MP9 stands with its root-meet ground
corrected. Theorem O stands. The finite-book rider is the one demotion.**

## 1. Front 1 — clause provenance and quarantine integrity

Provenance map assembled from §3/§9 of the doc and checked against the
promoted sheets:

| clause | source per §9 | independent in-doc derivation | promoted-record anchor |
|---|---|---|---|
| MP0 | A1/A2 (cross) | D1: Prop 6.8 + St 3.16/3.17(i) + Prop 5.3(v) | 2POLE §1b/§1c |
| MP1 | A2 (unique-predecessor adopted) | D2: edge count Σ(r−1) = −1 + m leaves (verified: gives m−1) | 2POLE §1c(ii) at m=2 |
| MP2/MP3 | A1.T2 = A2(4); A1.T3 correction | D3: P1 + 8.3(iii) single-root + p.45 Bezout | 2POLE §1c(iii) |
| MP4 | A2(1) ⊇ A1's β-minimal | D4: (19) + St 5.2 + St 2.1 arithmetic (re-done here, §3b) | L1a(a)/A3L1 fronts 1–2 |
| MP5 | A1/A2 (k=0 manufacture in both, §9) | D5: St 8.4/8.2 + Prop 6.8 same-branch | L1a(b) |
| MP6 | A1.T4/T5 = A2(3) = A3.P4 | D6: St 3.17(i)/8.1(i)/(v) + gcd arithmetic | L1a(c) 3-shape menu |
| MP7 | A1/A2 | D7: gcd + (iv) degeneration + St 9.2(ii) | L1 §0/§4 |
| MP8 | A1.T7 = A2.Prop B | D8: (22) itemization + F*_P argument | LROOT §1–2 |
| MP9 | A1/A2 + D9's new residue closed form | D9 | L1 §4–§6, 2POLE §4b/§5b |

- **Quarantine honored.** The three §7 blocks (prime-partition kill,
  RH-lemma kills, OB extension (3,5,1)/(4,7,1)) were grepped against
  MP0–MP9, §0, §5, §6, §8. No leak. The two near-misses are clean:
  (i) MP4's prime-Λ clause overlaps A3's quarantined P2 *statement*, but §9
  attributes it to A2(1) and D4 derives it in full from (19)+St 5.2(ii)
  (re-verified on-page, §3b below) — the A3-unique *partition* consequences
  (8=3+5 etc.) stay in §7. (ii) Theorem O's m-uniform escape claims
  "arithmetic existence only" (lν ≡ −1 mod m ⇒ gcd(m, lν+1) = m — trivially
  checkable) and expressly does NOT claim (iv)-solvability for m ≥ 3; A3's
  quarantined OB (which claims solvability at (3,5,1)/(4,7,1)) is cited
  only as §8 future work. Correctly firewalled.
- **Flag 1.** §4's record caveat (i) admits A2's third vote flagged one
  *unnamed* subsidiary sub-claim as failing plus one unflagged
  record-contradiction. Because the failing sub-claim is not identified, a
  reviewer cannot verify it stayed out of the graft. Containment: every MP
  clause carries a D-derivation from printed statements, and this review
  re-verified the load-bearing ones — so nothing in MP *depends* on
  unexamined A2 record content. Still, the synthesis should name the failed
  sub-claim. (Action item A1 below.)
- **Flag 2.** The A1/A2/A3 panel records are not preserved in the repo;
  provenance is auditable only through the doc itself. Acceptable given the
  D-derivations, but the record should be archived if it still exists.
- Grafting upgrades audited: A1's "M_G | gcd(r, lν+1)" → equality (D6d) —
  proved both directions here and machine-swept (§6): exact. A1.T6's
  ψ = r+l−1 vs A2(5R)'s ψ = l+1 at r = 2: identical. A1's G\* = A2's
  G_last: same object (max ∩C_i).

## 2. Front 2 — the composition re-derived at m = 2, td = 6

### 2a. Clause-by-clause against the promoted record

- **MP4 entry.** td = 6 = mβ; Λ = 3+3, Prop 9.1's 1 < α < β ≤ 6 pins
  (α,β) = (2,3); Λ_i = 3 = β is both β-minimal AND prime — b_i = 1 forced
  by either MP4 route. (deg p, deg p_g) = 1·(2,3), M = gcd(2,3) = 1 = row 1
  of (23) (re-read on-page: unique Λ=3 row, ν=2). Matches L1a(a)/2POLE §2d
  exactly. MP4's b-formula reproduces all 11 rows of (23) (b = 1 except
  rows 4, 8, 9: gcd(4,6)=2, gcd(6,15)=3, gcd(6,10)=2 — same gcds as
  A3L1-REVIEW front 2).
- **MP5 propagation.** Single simple ν-orbit, dp = ν, dq = nν+1, λ = 0,
  μ_i = 1 at arrival = L1a(b) verbatim; engine phase 4: 26 pre-merge
  shapes, all M=1/λ=0. Match.
- **MP6 menu at r = 2.** IIa: (2ν,(l+2)ν+1), M = gcd(2, lν+1); ZCH:
  (ν+1,(l+1)ν+1), M = gcd(ν+1, l); I: (2, 2+l), M = gcd(2, l). All three
  reduce EXACTLY to L1a(c)'s menu (checked by hand: (l+1)ν+1 ≡ −l mod ν+1;
  gcd(2,2+l) = gcd(2,l)) and machine-swept (§6). Match, including the
  equal-quotient i = 2 (exhibit's i₀ = P_i/μ_i = 2, realized absolutely).
- **MP7 + MP9 interior meet.** M = gcd(2, lν+1) = 2 iff l, ν both odd
  (parity swept §6); l = 0 → M = 1 → MP2 kill; ν = 1 killed by D9's
  log-obstruction (even l) + MP2 (odd l). Survivor menu IIa(l odd, ν ≥ 3
  odd)/ZCH(gcd(ν+1,l) ≥ 2) = L1 §0's post-L1b state; reach then pins the
  unique in-caps cell (r,ν,l) = (2,3,1), n = (5,5), dp/dq = 6/10 → merged
  child Q = **(6,12,3,2,5) @ Σλ = 0** — engine re-run this session:
  351 parent pairs, every depth, single residue child (1/2,3,2,5),
  byte-matching L1 §6 and 2POLE §6a. deg p_full = i·dp = 2·6 = 12,
  M = gcd(6,10) = 2, κ̄ = (5+5)/2 = 5. **The MP machinery reproduces the
  promoted record exactly; no mismatch found.**
- **MP8.** Σλ = 0 through pre-merge + merge = 2POLE §5a's min-spend-0;
  witness total Σλ = 2 ≤ 6−1−2 = 3 (St 9.4 (25) at ψ = 2, on-page). Match.
- **D9's log-obstruction upgrade** (all even l at ν = 1, beyond L1's engine
  caps): the residue identity C(−n, n−1) = (−1)^{n−1}C(2n−2, n−1) ≠ 0 and
  the partial-fraction residue of p^{−n} were re-verified exactly for
  n = 2..12 (§6), against L1's l=2 value ∓2/(a₁−a₂)³. The claim is sound:
  LHS (s·p^{−l/2})′ is a derivative, residue-free; RHS has nonzero simple
  residues; c′ = 0 forced, contra ⊖ ≠ 0. The η-variant cap flag (l ≤ 4)
  correctly survives as the doc states.

### 2b. MP1/MP3 at m = 2

Σ(r−1) = 1: exactly one merge, r = 2, G\* = G_m; escape set = the two
pre-merge segments = 2POLE §1c(iii). Consistent.

### 2c. The one composition flaw: MP9's root-meet citation

MP9 (root meet) claims "Empty at td = 6 by reach (2POLE §5b phase 3)". Two
problems with that citation: (i) phase 3's printed grounds fail for the
very family MP9 leaves open — ground (i)'s searrow failure and the ratio
rigidity (2+k)/(k+2) = 1 both presuppose the *l-free* I-like root pattern
(dq = k+2); with l ≥ 1 extras dq = 2+l, the searrow test passes and the
ratio is 2/(2+l) ≠ 1 — indeed MP9 itself proves l = 1 *locally solvable*;
(ii) the engine's phase-3 MENU is l-free (`dp, dq = mu1+mu2+k, k+2`,
twopole_check.py:253), so it never enumerated the l ≥ 1 root family at all.
**The kill is nevertheless real and was re-established here on an
l-INDEPENDENT ground:** the terminal edge into (0,y) is Prop 9.3 case (I)
(root merge ⇒ (0,y) ∈ V_{2,a}, case (IV) hypothesis fails — 2POLE
§1c(ii)), and (d) with child κ̄ = 1 (St 9.2(iii), on-page) forces
n_e = ν_e − κ̄_e ≥ 1, i.e. **κ̄ < ν at both parents, whatever the pattern
shape**. Independent raised-caps sweep (/tmp/mp_check.py check 5: ν ≤ 48,
l ≤ 8, depth ≤ 8 vs the engine's 24/4/6): 50 reachable M=1/λ=0 chain
shapes from the row-1 entry, **zero with κ̄ < ν**. So td = 6 root meets
with μ = (1,1) are reach-dead. Required fix: MP9's citation should read
"κ̄ < ν unreachability along M=1/λ=0 chains (Prop 9.3(d) at child κ̄ = 1;
engine sweep)", and the phase-3 root menu should gain the l-family before
any reuse at general td (where the doc correctly marks the residual OPEN).
Same tier as before (H1 + capped sweep) — no tier change, no new survivor.

## 3. Front 3 — page fidelity (all six re-read on-page this session)

1. **Prop 6.8 (p. 34)**: verbatim "Set F ∈ Ta&. Assume deg(p_F) ≠ 1. Then
   there exist P ∈ R̄_a\R_a, u,v ∈ Q⁺ with (i) F = I_P(u); (ii) v ≥ u;
   (iii) I_P(v) ∈ T_{a,pole}." Same P, parameter above u — the same-branch
   pole manufacture MP0/D5(c)/D6(a) uses. CONFIRMED (note the hypothesis
   deg p_F ≠ 1: every MP application supplies deg p ≥ 2 via St 3.16/3.17(i)).
2. **Not 8.1 (p. 39)**: M_F := gcd(deg p_F, deg p_{h_0,F},…,deg p_{h_m,F}),
   h_i per Prop 4.2 (h_0 = g). CONFIRMED (with m_F = 0 at poles this is
   exactly D4's pin).
3. **Prop 8.1 (pp. 39–41)**: F ∈ Ta&, u = π(F), i := deg(p_F)/M*_F ∈ N*;
   (i) (ξ^δp)^i = ⊖f_F⁺ (so p_full = p^i — D6(b)'s ground); (iv)
   δpq′ − (1−u)p′q = ⊖p; (v) M_F = gcd(deg p, deg q); proof line
   deg(p) = M*_F. CONFIRMED, exactly as used in D5–D9.
4. **St 8.4 (p. 42)**: F, G ∈ V_a ∩ Ta&, G = F + c ⇒ mult(p, c) | M_G —
   p at the lower vertex, M at the upper: precisely MP's μ_e | M_{H_e}.
   CONFIRMED. (St 8.2's searrow test and St 8.5's V_{2,a} exemption also
   confirmed on the same pages.)
5. **Prop 7.5 (22) (p. 38)**: td = 1 + Σ κ_{F_i}(π(F_i)−1) + Σ_a δ_a,
   proved "by calculating the Euler characteristics of C² via its subsets"
   — an EQUALITY, as MP8's itemization requires; Prop 7.4's δ_a ≥ 0
   adjacent. CONFIRMED.
6. **St 9.4 (25)–(26) (p. 49)**: pairwise-different F_i ∈ V_a ∩ Ta&, ψ ∈ N
   with ψl_f < k_f ⇒ Σλ ≤ td−1−ψ; proof routes the ψ cost through a
   T_{a,cv} ∩ T_{a,x} vertex (the x-side row MP8(v) keeps). CONFIRMED,
   including the exact ψ-admissibility MP7/MP9 use (ψ = r+l−1 satisfies
   ψl_f < k_f = (r+l)l_f strictly).

Extras verified while on-page: Prop 8.3's printed hypothesis is indeed
self-contradictory as printed (take H = F) — P1's regularity reading (Not
9.2, p. 48, verbatim) is necessary and correctly flagged, not silently
assumed; Prop 8.4's proof (pp. 44–45) matches D3 step-for-step (the
deg = mult line at (0,y) is where 8.3(iii) is load-bearing, as claimed);
table (23) row 1 (p. 46); Prop 5.6 (19), Prop 5.7's two-case proof, Prop
5.8 (20) (pp. 27–28) — D4's Λ = abαβ/ν arithmetic and both forcing cases
re-derived and CONFIRMED; St 5.2 (p. 26); Thm 6.1 (p. 28); Prop 9.2
(p. 50); Prop 9.3(a)–(m) (pp. 50–51); St 9.6's proof zoo (p. 52) — the
mult = 1 step D5(d) cites is verbatim ("deg(q) = nν+1 … M_F = 1"), and the
l = 0 arguments all pass through k ≠ 0 northeast roots, exactly the blind
spot Theorem O claims.

## 4. Front 4 — the obstruction half

- **Witness located**: carried by the doc via cases/l1_ode_check.py
  (family A) + SHEET6-2POLE §6a (hand exhibit) + SHEET6-L1 §5 (closed
  forms). **Re-verified this session**: family A at ν = 3 returns
  top_cancel, c̃ = −9/5 ≠ 0, roots distinct/nonzero, b = 2σ/3 not a root;
  closed form a₁a₂ = σ²(ν−1)/4ν, b = σ(ν+1)/2ν ⇒ a₁/a₂ = 2±√3 at ν = 3.
  Exact, machine-verified, matching every recorded datum.
- **Consistency with MP4**: td = 6, m = 2 forces Λ_i = 3 = β, which is
  simultaneously β-minimal and prime — b_i = 1 forced by both MP4 routes;
  row 1 of (23) confirmed on-page. So "M = 1 forced pre-merge" is exactly
  MP4 + MP5 at this instance, and the FALSE verbatim analogue is witnessed
  where claimed.
- **The witness IS the promoted residue-A object**: same merged child
  (6,12,3,2,5) @ Σλ = 0, same pattern p = (t−a₁)(t−a₂)|_{t=η³},
  q = η·p·(t−b), same suffix (42,126,7,3,5) with B = (3/2)A, same case-IV
  terminal R = 3, ψ = 2, slack 1. Confirmed identical to 2POLE §6a/§7.3.
- Located-constraint pass re-checked: Prop 8.1(iv)–(v), St 8.2 (10 > 6
  both edges), St 8.4 (μ = 1 | 1), root/eta laws, St 9.4 budget, entry
  pins. Theorem O's "solves every located printed constraint" stands.

## 5. Front 5 — the reduction claim (the review's main deliverable)

### 5a. What is actually proven

Finitely many at printed tier, per (m, td): types and entries (D4:
partitions td = ΣΛ_i, Λ_i ≥ β; finitely many (a_i,b_i,ν_i) per Λ_i via
(19) + St 5.2(ii)); tree shapes (MP1: ≤ m−1 merges, Σ(r−1) = m−1, r ≤ m);
merge-local anatomy (MP6: μ⃗ = 1 at all-M=1 merges, k = 0, family ∈
{IIa, ZCH, I}, M from the gcd menu, M | r ≤ m outside ZCH, gcd(M,ν) = 1);
root cells (ν = 1, l ≤ td−2 via ψ = r+l−1 and (25) — finite per td). At H1
tier, the per-edge Prop 9.3 equations make (l, n_e, ν) **finite per parent
frame**: for the all-μ=1 IIa jump, cross-multiplying (b) gives
ν·(rκ̄_e − (r+l)ρ_e − l·n_e) = ρ_e + n_e, so n_e ≤ (rκ̄_e − (r+l)ρ_e −1)/l,
l ≤ (r(κ̄_e − ρ_e) − 1)/(ρ_e + 1), and each admissible (l, n_e) DETERMINES
ν. This is real and enumeration-ready.

### 5b. What is NOT proven: the demotion

The frames themselves are generated from the finitely many entries by the
H1 chain-step map, and **nothing bounds the generation depth**: κ̄ evolves
by κ̄′ = (κ̄+n)/ν (Prop 9.3(d)) and demonstrably GROWS along admissible
M=1/λ=0 chains (the engine's own parent list at td = 6 contains κ̄ = 5, 6,
8, 10; my raised-caps sweep reached 50 frames and was cap-, not
constraint-, terminated). At pattern level the survivor menu is already
infinite (IIa: all l odd, ν ≥ 3 odd). Worse, the doc's own **MP8 proves
no printed budget can charge the M=1 region — so no printed statement can
bound pre-merge chain depth either**: the obstruction half structurally
undermines the reduction half's finiteness. Empirically the merged-child
datum was depth-invariant at td = 6 (351/351 pairs, one child), which
suggests a *child-invariance/closure lemma* exists — but none is stated or
proved in MP0–MP9, §5, or the quarantined §7. **Demotion: §0's "reduces
… to a finite book of jump-vertex cells" and Theorem O's "the finite book"
are theorem-grade only in the per-frame sense; globally the book is
finitely *generated* (finite alphabet, finite branching per frame) with
unbounded frame depth, conditional on an unproven closure lemma or a
cap-stability protocol.** notes.md's "finite-book at every level"
(2026-08-12 entry) inherits this demotion.

### 5c. The jump-book parameterization, as handed to the enumeration engine

    BOOK(m, td), m ≥ 2, 3m ≤ mβ ≤ td:
    E. Entry layer (printed; finite): type (α,β), 2 ≤ α < β, gcd = 1,
       mβ ≤ td; partition td = Σ_{i=1..m} Λ_i, Λ_i ≥ β (Props 5.7/5.8);
       per pole (a_i, b_i, ν_i): Λ_i = a_i b_i αβ/ν_i, ν_i | α or ν_i | β
       (St 5.2(ii) + (19)); entry datum Q(P_i) = (D = a_iα, deg p = b_iα,
       ν_i, M = b_i, κ̄ = a_i(α+β)), λ = 0. b_i = 1 forced if Λ_i = β or
       Λ_i prime (MP4).
    T. Tree layer (printed; finite): rooted trees, m leaves, merge
       vertices G with r(G) ≥ 2, Σ(r−1) = m−1, no merge below G*.
    C. Chain layer (H1; the unbounded direction): per edge, step frames
       (ρ, ν, κ̄, M) evolve by Prop 9.3(a)–(d) with n ≥ 1,
       n ≡ −κ̄ (mod ν); M = 1 segments are forced single-simple-orbit,
       λ = 0 (MP5); depth cap OR closure lemma REQUIRED here.
    J. Jump cells (printed anatomy + H1 reach; finite per frame):
       family ∈ {IIa: (dp,dq) = (rν,(r+l)ν+1), M = gcd(r, lν+1);
       ZCH: ((r−1)ν+1,(r−1+l)ν+1), M = gcd((r−1)ν+1, l);
       I: (r, r+l), M = gcd(r,l)}; constraints: μ_e | M_{H_e} (= 1 on
       all-M=1 ancestry), k = 0, common i ≥ 2 with deg p_{H_e} = iμ_e,
       l ≥ 1, M ≥ 2, gcd(M,ν) = 1, M | r ≤ m outside ZCH; per-edge reach:
       dp/dq = μ_e(ρ_e+n_e)/(κ̄_e+n_e), n_e ≥ 1, n_e ≡ −κ̄_e (mod ν_e),
       common child (κ̄, D, i) — bounds n_e, l and determines ν per frame
       (§5a). Coefficient layer: Prop 8.1(iv) rigid solve (à la
       l1_ode_check families A/Z), then the §8-item-3 coefficient-vs-ratio
       match (never yet run).
    R. Root cells (printed + H1; finite per td): ν = 1, all-μ=1, l odd,
       l ≤ td−2, k_f = (r+l)l_f, ψ = r+l−1, both parents κ̄ < ν (Prop
       9.3(d) at child κ̄ = 1 — l-independent, §2c), Prop 9.3 case (I).
    S. Suffix (printed): restored M ≠ 1 kill (MP2) + single-pole engine +
       St 9.4: Σλ ≤ td − 1 − ψ over the union, shared suffix once.

## 6. Front 6 — mechanization (/tmp/mp_check.py, exact, no shared code)

(1) MP6(d) identities on r ≤ 9, ν ≤ 12, l ≤ 12 + mixed μ-sums to 3r:
IIa/ZCH/I gcd equalities, gcd(M,ν) = 1, M | r, M | Σμ — all exact both
directions. (2) MP7: gcd(rν, rν+1) = 1 at l = 0, all cells; ZCH/I l = 0
degree degeneration. (3) MP9 parity: gcd(2, lν+1) = 2 ⇔ l, ν odd — swept.
(4) Root pin: k_f = (r+l)l_f and ψ = r+l−1 on a grid i ≤ 19, r ≤ 7,
l ≤ 11. (5) Log-obstruction: C(−n,n−1) closed form + exact Laurent residue
of p^{−n}, n = 2..12. (6) The κ̄ < ν sweep of §2c. ALL PASS. (§7's action
item — rebuilding A3's /tmp/mpm_check.py under cases/ — remains open and is
NOT covered by this file.)

## 7. Required fixes (none demote MP0–MP8)

1. **MP9 root-meet citation** → replace "(2POLE §5b phase 3)" by the κ̄ < ν
   ground of §2c; add the l-family to the phase-3 root menu before any
   general-td reuse (latent enumeration gap, currently masked by the κ̄ < ν
   filter at td = 6).
2. **§0/§5 finiteness rider** → reword per §5b: "finitely generated book;
   finite per parent frame; global finiteness conditional on chain-depth
   closure (empirically depth-invariant at td = 6)". Add the closure lemma
   to §8's next steps — it is arguably the cheapest high-value target: the
   351-pair child-invariance suggests it is provable at H1 tier.
3. **Name A2's failed subsidiary sub-claim** in §4 caveat (i), or archive
   the panel record; quarantine §7 already handles A3 correctly.
4. Cosmetic: doc §1 cites Not 8.1 at "p. 39" correctly, but 2POLE §2c says
   "p. 38" — fix in 2POLE, not here.

## 8. Reproduction

    cd cases && python3 twopole_check.py   # phases 1-4; byte-matches L1 §6
    python3 l1_ode_check.py                # witness families; ~5 s
    python3 /tmp/mp_check.py               # this review's checker; ~2 s
    # PDF: pp. 26-28, 34, 38-52 re-read on-page for §3.
