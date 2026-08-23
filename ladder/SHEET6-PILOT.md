# SHEET6 PILOT — Sigray Prop 9.1 / Stmt 9.6 machine-rederivation

Status: COMPLETE. Prop 9.1 PASS (11/11); Stmt 9.6 DISCREPANCY — thesis row (B)=(75,51) is a
p. 52 arithmetic slip (spurious, benign direction; corrected list {(21,15),(20,16)}); see §3.

### 0. SHEET6.md spec (read, §2/§7)
Pilot = Prop 9.1 (11-row multiplicity table, types (α,β) ∈ {(2,3),(3,4),(2,5),(3,5),(4,5),(5,6)})
+ Stmt 9.6: propagation from Q(G) = (j,2j,3,2,5); Diophantine
(k+2)ν/((k+1)ν+1) = (1+2n)/(5+n), n ≡ 1 (mod 3); expected exactly
deg(p,q) ∈ {(21,15),(75,51),(20,16)} + λ-classification (i)-(v). Diff vs thesis pp. 45-53.

## 1. Extraction (thesis pp. 45-53)
- [x] Prop 9.1 (pp. 45-46): "If Λ(F) ≤ 6, all possible multiplicity data for F ∈ T_a,pole" = table (23),
  11 rows, columns: type (α,β) | (D_F, D_g,F) | (deg p_F, deg p_g,F) | ν_F | Λ(F).
  Rows (verbatim): 1:(2,3),(2,3),(2,3),2,3 · 2:(2,3),(2,3),(2,3),1,6 · 3:(2,3),(4,6),(2,3),2,6 ·
  4:(2,3),(2,3),(4,6),3,4 · 5:(3,4),(3,4),(3,4),3,4 · 6:(3,4),(3,4),(3,4),2,6 · 7:(2,5),(2,5),(2,5),2,5 ·
  8:(2,5),(2,5),(6,15),5,6 · 9:(3,5),(3,5),(6,10),5,6 · 10:(4,5),(4,5),(4,5),4,5 · 11:(5,6),(5,6),(5,6),5,6.
  (Print quirk: rows 5,6 both typeset "6"; content unambiguous. Λ=6 in exactly 6 rows — SHEET6.md's "7" is off by one.)
- [x] Proof machinery: Prop 5.7 → type (α,β), 1<α<β≤6, gcd=1. St 5.2(ii) → ν_F ≤ β. "(19)" used as
  Λ(F) = D_g,F·deg(p_F)/ν_F ≤ 6 (verified: reproduces every listed bound D_g,F·deg p_F ≤ 6β and every
  "ν_F ≠ 1 / > 2 / > 3" kill, and the Λ column of all 11 rows). St 5.2(i) → (D_F,D_g,F) = a(α,β),
  (deg p_F, deg p_g,F) = b(α,β), a,b ∈ N*. St 5.2 ν-menu per (a,b): matches rule
  [ν | deg p_F and ν | deg p_g,F − 1] OR [ν | deg p_F − 1 and ν | deg p_g,F] on all 18 case-lines pp. 46-48.
  (Rule reverse-engineered from usage; §5 text check pending below.)
- [x] Stmt 9.6 (p. 51): G ∈ T_a^↘, F := G° regular over G, Q(G) = (j,2j,3,2,5), j ∈ N*
  [i.e. D_G=j, deg p_G=2j, ν_G=3, M_G=2, κ_G(1−π(G))=5]. Possibilities:
  (i) M_F=1; (ii) λ_F≥3; (iii) Q(F)=(7j,21j,7,3,5), λ_F≥2; (iv) Q(F)=(5j,20j,5,4,4), λ_F≥2;
  (v) Q(F)=((6s+3)j,(4s+2)j,2s+1,2,3s+3), λ_F=0.
- [x] Constraint system (proof, p. 52): mult(p,c) | 2. mult=2, case II(a), k≠0, l=0:
  p,q root patterns give deg p = (k+2)ν, deg q = (k+1)ν+1, and Prop 9.3(b) forces the RATIO equation
    (k+2)ν / ((k+1)ν+1) = (D_G + n·deg p_G)/(i(κ_G(1−v)+n)) = (1+2n)/(5+n),  i = deg(p_G)/M_G = j,
  with k,n ∈ N*, ν ∈ N*\{1}, and n = 3m+1 (m ∈ N) from integrality of Prop 9.3(d)
  κ_F(1−π(F)) = ((1−π(G))κ_G + n)/ν_G = (5+n)/3. Thesis claims exactly:
  (A) k=1,n=10,ν=7 → (deg p,deg q)=(21,15); (B) k=1,n=13,ν=25 → (75,51); (C) k=2,n=7,ν=5 → (20,16).
  So the pairs (21,15),(75,51),(20,16) are (deg p, deg q) of the one-variable models p_F-related p,q —
  local branch-degree data, NOT bidegrees of (f,g). Propagated Q(F) via 9.3(c),(d): D_F=(1+2n)j/3, etc.
- [x] k=0 sub-case: deg p = 2ν, deg q = (l+1)ν+1, equation 2ν/((l+1)ν+1) = (1+2n)/(5+n);
  claimed solutions l=0, ν=2s+1, n=9s+4 (s ∈ N*), M_F=2 iff l even ∧ ν odd → family (v).
- [x] §5 verified verbatim (pdftotext, thesis pp. 26-27): Notation 5.3 multiplicity data =
  {type (α,β); (D_g,F, D_F); ν_F; (deg p_F, deg p_g,F)}. St 5.2(i): deg(p_F)/deg(p_g,F) = D_F/D_g,F = α/β.
  St 5.2(ii) ACTUAL: [ν_F|α ∧ ν_F|deg(p_g,F)−1] OR [ν_F|β ∧ ν_F|deg(p_F)−1]  (α/β-divisor form, slightly
  stronger than my first guess; re-checked against all 18 proof case-lines of Prop 9.1: exact match).
  Eq (19) = Prop 5.6: Λ(F) := D_g,F·deg(p_F)/ν_F = Σ_P Λ(P) (∈ N, pole orders of g). Prop 5.7: Λ(F) ≥ β
  ⇒ under Λ ≤ 6: β ≤ 6, plus 1 < α < β, gcd(α,β) = 1 (type of normalized counterexample).
- [x] Text layer confirms printed (B): "k = 1, n = 13 and ν = 25 ... deg(p) = 75 and deg(q) = 51".
  Pre-registered hand-check BEFORE coding: (B) fails its own equation: 75·(5+13) = 1350 ≠ 51·(1+26) = 1377.
  The (k,ν) = (1,25) branch actually forces n = 12 (27n = 25·13−1 = 324), and 12 ≢ 1 (mod 3).
  To be settled by full enumeration below.

## 2. Enumeration (cases/sheet6_pilot.py)
- [x] Exact integer arithmetic; generates ALL solutions, with completeness certificates:
  Prop 9.1: sweep β ≤ 60, a,b ≤ 40, ν ≤ β (valid: ν|α ∨ ν|β ⇒ ν ≤ β; Λ ≥ abα prunes; Λ ≥ β
  asserted, so β ≤ 6 is re-derived not assumed; Λ-integrality automatic since ν|α ⇒ ν|deg p_F,
  ν|β ⇒ ν|D_g,F). Stmt 9.6 k≠0: n(kν+2) = ν(4k+9)−1 ⇒ (kν+2) | 9(k+2) ⇒ ν ≤ 25, and n ≥ 1 ⇒
  k ≤ 8; oversweep k,ν ≤ 2000 asserts the box. k=0: 2n(lν+1) = ν(9−l)−1 ⇒ l ≤ 2; l=1 parity-killed;
  l=2 ⇒ (2ν+1)|9 killed; l=0 ⇒ ν = 2s+1, n = 9s+4 infinite family, identities checked.
- [x] Results: Prop 9.1 → exactly the 11 thesis rows, no extras, no missing. **PASS.**
  Stmt 9.6 k≠0 ratio equation, unfiltered (6 solutions total):
    (k,ν,n) = (1,7,10)→(21,15) ✓mod3 · (1,25,12)→(75,51) ✗ · (2,5,7)→(20,16) ✓ ·
    (2,17,8)→(68,52) ✗ · (4,13,6)→(78,66) ✗ · (8,11,5)→(110,100) ✗
  With the thesis's own filter n = 3m+1: exactly {(21,15),(20,16)}, with propagated
  Q(F) = (7j,21j,7,3,5) and (5j,20j,5,4,4) = thesis (iii),(iv) verbatim. k=0 branch: family (v)
  ((6s+3)j,(4s+2)j,2s+1,2,3s+3), M_F=2, reproduced exactly (l=0 forced, ν odd forced).

## 3. Comparison vs expected
- [x] **Prop 9.1: PASS** (11/11 exact). **Stmt 9.6: DISCREPANCY — thesis's (B) = (75,51) is spurious.**
  ERRATUM (unrefereed thesis, p. 52), double-checked in rendered page AND pdftotext layer:
  printed "(B) k=1, n=13, ν=25 ⇒ (75,51)" fails its own equation: 75·(5+13) = 1350 ≠ 51·(1+2·13) = 1377.
  The (k,ν) = (1,25) branch forces n = 12 (27n = 324), and n = 12 ≢ 1 (mod 3), so (B) is excluded by
  the thesis's own side-condition n = 3m+1 (equivalently κ_F(1−π(F)) = 17/3 ∉ N, D_F = 25j/3 ∉ jN).
  No missing solutions — the discrepancy is one EXTRA row in the thesis, not a gap in it.
  Impact: benign-and-favorable. Stmt 9.6 is a disjunction; (B) fed possibility (ii) λ_F ≥ 3 only.
  Corrected Stmt 9.6 = {(i),(iii),(iv),(v)}: strictly stronger, so td ≤ 5/6 applications that killed
  case (ii) did harmless extra work. Thesis conclusions unaffected; SHEET6.md's expected-output line
  (and its "7 rows with Λ=6"; true count 6) should be amended to cite this erratum.

## 4. Degree-6 readiness note
- [x] Extends directly (already running): (1) the Prop 9.1 enumerator is Λ-parametric — prop91(Lmax=7)
  (the td=6 leaf table, bound td+1) already runs: **14 rows** over 9 types, adding (2,7),(3,7),(6,7);
  (4,7),(5,7) admit no rows. SHEET6 §4's 20-30-row estimate is high — good news. (2) The Diophantine
  pattern [ratio eq → closed form n(kν+c)=… → divisor-bound certificate → oversweep assert] is the
  common shape of all propagation lemmas St 9.6-9.11; RHS is always (D_G-coeff + n·degp_G-coeff)/(κ+n)
  read off Q(G) — a solve_ratio(Q_G, root-pattern) library call. (3) Q(F) propagation via Prop 9.3
  (a)-(d) implemented; (e)-(h) same shape.
- [x] Missing for td=6: (1) Prop 9.3 cases III/IV arithmetic ((e)-(m)) + St 3.16/3.18-driven derivation
  of admissible root-pattern families per (M_G,ν_G) — currently hand-read per lemma; (2) λ-bookkeeping
  (St 9.3/9.4 inequalities, Σλ ≤ td−2 = 4 budget) and Cor 7.1 generalization — genuine math, not
  enumeration (SHEET6 §6.2); (3) characteristic-sequence assembly + St 9.12-analogue termination;
  (4) foundations audit of §§3-8 remains the load-bearing risk — reinforced by the p. 52 erratum found
  here: unrefereed arithmetic does contain slips, and machine re-derivation catches them.
