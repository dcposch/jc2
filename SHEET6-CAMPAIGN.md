# SHEET6 CAMPAIGN — systematic td=6 case enumeration + bash (Sigray engine)

Status: PHASE 1 COMPLETE (2026-08-07). Follow-on to SHEET6-PILOT.md. Driver:
`cases/sheet6_campaign.py` (gate PASS). HEADLINE: the mechanizable layer of the
td=6 case bash is built and run — all 6 single-pole Λ=6 entries + the td≤5
re-validation. Both (2,3)-type td=6 entries (rows 2,3) are fully excluded
conditional on H1-H4+H3; the other four reduce to ~14 case-III parametric tails
+ IV-terminals gated by H3. The bash also found 3 NEW thesis errata (E2-E4:
"no solution" claims false, giving λ=0 self-loops) and exposed that the printed
thesis td≥6 proof is incomplete without an unstated root-kill (G2) and never
treats rows 5,10 (G3). Open-case list with estimates: §6. Nothing farm-sized.

## 0a. Assembly-layer extraction (thesis pp. 37-60, needed before enumeration)

- Prop 5.8 (20): td(f,g) = Σ_{F∈Ta,pole} D_g,F·deg(p_F)/ν_F = Σ_{pole} Λ(F). With
  Prop 5.7 (Λ ≥ β ≥ 3): td=6 ⇔ ONE pole vertex with Λ=6 (rows 2,3,6,8,9,11 of table
  (23)) OR TWO pole vertices Λ=3+3 (row 1 twice). td≤5 ⇔ one vertex, Λ=td, rows
  {1,4,5,7,10}.
- Notation 9.1: Q(F) = (D_F, deg p_F, ν_F, M_F, κ̄_F), κ̄ := κ_F(1−π(F)). St 9.1:
  pole vertices have κ̄ = D_F + D_g,F. St 9.2: at root (0,y): D=d, ν=1, κ̄=1.
- Prop 9.2/St 9.5: characteristic sequence F0=pole → F_{i+1}=F_i° → (0,y), finite;
  Σ λ_{F_i} ≤ td−2 (St 9.4 via Cor 7.1). Prop 8.4 (REQUIRES Ta,pole singleton):
  M_F ≠ 1 for every F in the tree ⇒ any M=1 outcome kills the chain.
- Prop 9.3: per step G=F+c, exactly one of cases I / II / III / IV; (a)-(d) give for
  I,II: deg(p)/deg(q) = (D_G+n·deg p_G)/(i(κ̄_G+n)), i := deg(p_G)/mult(p,c);
  D_F = (D_G+n·deg p_G)/ν_G; κ̄_F = (κ̄_G+n)/ν_G ∈ N (⇒ n ≡ −κ̄_G mod ν_G);
  case III: (e)-(h) same with ν-weights; case IV (terminal (0,y)): needs (i) ν_G=κ_G,
  (j) κ̄_G < ν_G, (k) d_F = [D_G+(ν_G−κ̄_G)deg p_G]/ν_G ∈ N, (l) d_F < deg p_G,
  (m) d_F·M_G/deg p_G ∈ N. Verified (k) reproduces 9.7(iii)/9.9(iii)/9.10(iii)
  terminals exactly ((4s+3)²j/(4s+3) etc.).
- Root-pattern template (extracted from all six proofs of St 9.6-9.11; St 8.4:
  mult(p,c)=:μ | M_G, regularity ⇒ μ = max mult): μ=1 ⇒ M_F=gcd(ν,nν+1)=1 KILL.
  Case I and II(b) and III: M_F | gcd(μ−1, ·) ⇒ μ=2 gives M_F=1 KILL; μ≥3 gives
  λ_F ≥ 1 (regularity argument). Case II(a): p=(η^ν−c^ν)^μ·Π_k, deg p=(k+μ)ν,
  deg q=(k+l+1)ν+1; k>0 ⇒ l=0 (St 8.2); k=0 ⇒ l ≥ 0 free. Solve ratio eq with
  n = n0+m·ν_G. λ-rule (REVERSE-ENGINEERED, audit flag AF2 below): each of the k
  extra roots contributes max(1, D_F/i − κ̄_F); matches all six lemmas
  (9.6: λ≥2,3,2 for (A),(B),(C); k=0 ⇒ λ=0; 9.11: λ≥2,2).

## 0b. Thesis ambiguities found during extraction (beyond pilot's erratum)

- **G1 (St 9.12 label/formula tension)**: St 9.12 says single pole vertex "cannot have
  type (3)" and its proof opens "Then td(f,g) = 4". Under (20), row 3 has Λ=6 (td=6,
  not 4); row 4 has Λ=4. Table row labels are misprinted (rows 5,6 both "6"), and
  St 9.6's Q(G)=(j,2j,3,2,5) matches row 4 (j=2, M=2) and NO other row. Adopted
  reading: St 9.12 kills row **4**, "type (3)" is a label slip, (20) stands as printed.
- **G2 (St 9.12 proof terseness — load-bearing)**: printed kill mechanisms are only
  "some M_{F_j}=1 (contra Prop 8.4) or Σλ > td−2 (contra St 9.4)". But the chain
  row4 →9.6(iii) (λ=2) →9.7(iii) = case-IV terminal reaches (0,y) with Σλ = 2 ≤ 2
  and no M=1: NOT killed by the stated mechanisms. An unstated root-vertex kill must
  close it. Candidate: case IV forces d_F < deg p_F at (0,y) by its own condition
  (l), while Thm 6.1 (l_f < k_f, i.e. deg p < d at the root in the other chart) plus
  normalization forbids exactly this. Campaign runs with hypothesis **H3**: "case-IV
  terminals are killed by the root-data constraint" and reports verdicts both with
  and without H3.
- **G3 (thesis silence on rows 1,5,7,10)**: under (20), td≤5 also admits single-vertex
  rows 1 (td=3), 5 (td=4), 7 (td=5), 10 (td=5). §9 as printed bashes only row 4.
  Campaign re-bashes ALL of {1,4,5,7,10} as validation (if our engine kills them, the
  silence is benign; if not, the thesis's td≥6 claim has a gap beyond terseness).

## 0c. Standing hypotheses (all audit-flagged, inherited from unrefereed source)

- H1: Prop 9.3 case split + (a)-(m) arithmetic correct (foundations audit pending).
- H2: chain kills = {M=1 via Prop 8.4 (single-pole only), λ-budget via St 9.4,
  no-applicable-case}; AF2: λ-rule as reverse-engineered above.
- H3: case-IV (0,y)-terminals killed by root-data constraint (see G2).
- H4: regularity wlog per thesis usage; St 3.16/3.18 root patterns as templated.

## 0. Gate: pilot reproduction

**PASS** (cases/sheet6_campaign.py `gate`): Prop 9.1 11/11 rows; Stmt 9.6 corrected
pairs {(21,15),(20,16)} + erratum row (k,ν,n)=(1,25,12)→(75,51) reproduced; new
generic engine re-derives St 9.6 possibilities (iii),(iv),(v) with λ = 2,2,0 exactly.

## 1. Leaf table at Λ ≤ 7 (td = 6 bound = td+1)

**14 rows** (`table` phase; = pilot's readiness count; SHEET6.md's 20-30 estimate
high). New Λ=7 rows beyond the 11: (2,7)×1, (3,7)×1, (6,7)×1 (all with
(D,Dg)=(α,β)=(deg p,deg p_g), ν=α); (4,7),(5,7) admit none. td=6 entries use the
Λ=6 rows only: {2,3,6,8,9,11} in pilot numbering.

## 2. Q-datum extraction & configuration layer

- td = ΣΛ over pole vertices (Prop 5.8 (20)); Λ ≥ β ≥ 3 ⇒ td=6 configs =
  **6 single-pole rows × M-menu** + **one double-pole config** (row 1 + row 1, Λ=3+3).
- Entry Q per St 9.1 (κ̄ = D+D_g): row2→(ρ=1,ν=1,κ̄=5); row3→(ρ=2,ν=2,κ̄=10);
  row6→(ρ=1,ν=2,κ̄=7); row8→(ρ=1/3,ν=5,κ̄=7); row9→(ρ=1/2,ν=5,κ̄=8);
  row11→(ρ=1,ν=5,κ̄=11). M-menu per AF3: M | deg p_F (thesis-sanctioned subset:
  M | gcd(D,P)); μ | M (St 8.4). μ-admissibility needs NO deg(p)-content condition
  (the formal j-unit rescales), so the M-menu is the only entry freedom.
- **Double-pole (3,3)**: Prop 8.4 (M≠1) REQUIRES Ta,pole singleton ⇒ every M=1 kill
  is unavailable. OPEN — needs a Prop-8.4 analogue for 2 dicriticals (genuine math,
  see §6).

## 3. Propagation lemmas (St 9.6–9.11 analogues, td = 6)

### 3a. Validation on solved ground (td ≤ 5 lemmas re-derived)

Engine `validate` phase vs thesis pp. 51-59 (λ-rule AF2 used throughout):
- **St 9.6 PASS exact**: (iii) (1/3,7,3,5) λ≥2; (iv) (1/4,5,4,4) λ≥2; (v)
  (3/2,2s+3,2,3s+6) λ=0 [= thesis (v), s-shift]; I/IIb/III/μ=1 ⇒ M_F=1. Erratum
  (75,51) absent. λ values 2,2,0 match thesis exactly.
- **St 9.11 PASS exact**: self-loop (v) + (iii) (1/4,5,4,4) λ≥2 + (iv) (1/3,7,3,5)
  λ≥2, matching thesis (2φ+1)-family statement.
- **St 9.7 PASS + refinement**: thesis (iii) IV-terminal ✓, (iv) (2/3,3s+2,3,2s+2)
  λ=0 ✓; engine additionally SOLVES the thesis's λ≥1 shortcut branches (needed at
  td=6 budgets): case I → (1,1,M=2,2) λ≥2; IIb → (1,2s+2,1,·) [M=1 kill] and
  (1,2s+3,2,2s+4) λ≥1; III → (1,7,2,8) λ≥2.
- **St 9.8: DISCREPANCY (new thesis erratum E2)**: thesis claims μ=2, l=0 ⇒ M_F=1
  and "no solution with n=5m+1, l>0". TRUE for l>0, but l=0 has the solution family
  3ν=4m+1 (ν=4s+3, m=3s+2, n=15s+11) with M_F = gcd(2ν,ν+1) = **2** (ν odd), giving
  a MISSING possibility Q(F) ~ (3/4, 4s+3, M=2, 3s+3) λ=0 — same numbers as thesis
  (iv) but M=2 (the thesis's own 9.6(v) computes this gcd correctly, so 9.8's
  "M_F=1" is a slip). Engine also confirms (iv) via μ=4 (M=4 copy) ✓ and refines
  I (λ≥3, M_F=1 kill), IIb (6 residue families, M∈{1,3}), III → (1,5,3,6) λ≥3.
- **St 9.9: DISCREPANCY (E3)**: thesis claims both μ=2 and μ=4 Diophantines have
  "no solution"; both are false as printed — 3ν=4m+1 families exist for both, giving
  **λ=0 SELF-LOOPS** (3/4,4s+3,M,3s+3) → itself with M=2 (μ=2) and M=4 (μ=4).
  Benign for td≤5 (loops must exit; exits unchanged) but the lemma's possibility
  list is incomplete as printed. Also engine finds exit (1/8,5,4,2) λ≥2 (μ=2,k=2).
- **St 9.10: DISCREPANCY (E4)**: thesis μ=3 eq "no solution" false — 2ν=3m+1 family
  (ν=3s+2, m=2s+1) exists with M_F=3 ⇒ λ=0 SELF-LOOP (2/3,3s+2,3,2s+2)→itself.
  (Thesis 9.10's printed (iv) row — the (12s+9,16s+12,4s+3,4,3s+3) copy from 9.9 —
  is NOT produced by its own proof body, which derives only (i)-(iii); label chaos.)
- Parametric-III limitation: for parametric nodes (9.9/9.10 shapes) case III has no
  s-free reduction (κ̄ parametric, ρ concrete) ⇒ flagged OPEN, handled per-s (§6).

### 3b. New td = 6 cases

Engine solves the propagation Diophantines generically per node (no per-lemma hand
work): branches {IIa k>0, IIa k=0, I, IIb, III} × μ | M, with per-cell exact m/ν
solves, family detection (collinear + residue-split mod ≤ 12), s-free reduction of
parametric families via linear-form cancellation (PIT-certified ×24 samples), and
s-shift re-parametrization when the s≥0 window blocks the congruence. The td=6
runs traverse ≈ 30-90 solved propagation steps per entry (loops deduped by shape) —
consistent with SHEET6.md's 150-400 estimate summed over entries. Representative
new (not-in-thesis) lemma content, entry row 6 = (3,4),ν=2,M=3 (κ̄=7):
μ=3 IIa_k k=1 → (1/3,4,3,3) λ≥3; IIa_0 self-family (3,3s+2,3,9s+9) λ=0;
I → (1,1,2,3) λ≥3; III k=1 ν-family (1/2, 45+54t, 2, 23+27t) λ≥1 → IV-capable.

## 4. λ-budget & assembly (Σλ ≤ td−2 = 4)

BFS over chains (Prop 9.2 characteristic sequence), state = (Q-shape, Σλ):
- kills: child M_F=1 (Prop 8.4; single-pole only), Σλ > 4 (St 9.4/9.5), and every
  λ≥1-costing branch is pruned unsolved when remaining budget < 1 (I/IIa_k/IIb/III
  all cost λ ≥ 1 per AF2+ceil; only IIa_0 (k=0) is free).
- λ uses ceil(D_F/i − κ̄_F) per extra root (κ_H(π(H)−1) ∈ N, St 9.4 proof line).
- loops (revisited shape at ≥ λ): closed off first visit; sequences are finite
  (Prop 9.2) so λ=0 self-loops (which DO exist — E2-E4) cannot save a chain.
- IV-terminals recorded, killed iff H3. Depth cap 7 (no frontier hits at cap).

## 5. Verdict table

td ≤ 5 validation chains (single pole, budget Λ−2; `bash5` phase):

| entry (row, Q) | M | verdict | residue |
|---|---|---|---|
| r1 td3 (2,3) ρ=1,ν=2,κ̄=5 | 2 | **EXCLUDED** (H1-H4; no IV hit, no H3 needed) | — |
| r4 td4 (2,3) ρ=1/2,ν=3,κ̄=5 | 2 SANC | **EXCLUDED mod H3** (5 IV-terminals) | thesis's St 9.12 case, now mechanical |
| r4 td4 | 4 ext | 2 III-tails (λ0/λ1) | superset branch only |
| r5 td4 (3,4) ρ=1,ν=3,κ̄=7 | 3 | 1 III-tail (λ0) at (2,3s+2,3,6s+6) | thesis silent on this row (G3) |
| r7 td5 (2,5) ρ=1,ν=2,κ̄=7 | 2 | **EXCLUDED** (no IV possible) | — |
| r10 td5 (4,5) ρ=1,ν=4,κ̄=9 | 2 | 1 III-tail (λ2); 4 IV mod H3 | thesis silent (G3) |
| r10 td5 | 4 | 4 III-tails; 20 IV mod H3 | thesis silent (G3) |

td = 6 campaign (single pole, budget 4; `bash`/`report` phases):

| entry (row, Q) | M | verdict | open residue (distinct shapes) |
|---|---|---|---|
| r2 (2,3) ρ=1,ν=1,κ̄=5 | 2 SANC | **EXCLUDED mod H3** (2 IV: (1/3,7,3,5), (2/3,3s+2,3,2s+2), both λ=4) | none |
| r3 (2,3) ρ=2,ν=2,κ̄=10 | 2 SANC | **EXCLUDED mod H3** (same 2 IV shapes) | none |
| r6 (3,4) ρ=1,ν=2,κ̄=7 | 3 SANC | mod H3 + 2 III-tails | (2/3,3s+2,3,2s+2)@λ3, (3,3s+2,3,9s+9)@λ0 |
| r8 (2,5) ρ=1/3,ν=5,κ̄=7 | 2 SANC | mod H3 (7 IV) + 2 III-tails | (2/9,9s+8,3,2s+2)@λ3, (8/9,9s+8,3,8s+8)@λ2 |
| r8 | 3,6 ext | more III-tails (1 and 15) | superset |
| r9 (3,5) ρ=1/2,ν=5,κ̄=8 | 3 SANC | mod H3 (15 IV) + 1 III-tail | (3/2,6s+5,3,9s+9)@λ0 |
| r9 | 2,6 ext | 3 and 21 tails | superset |
| r11 (5,6) ρ=1,ν=5,κ̄=11 | 5 SANC | mod H3 (26 IV) + 8 III-tails | μ∈{3,4,5}, shapes in report |
| 2-pole (r1+r1, Λ=3+3) | — | **OPEN** (Prop 8.4 unavailable) | needs 2-dicritical M≠1 analogue |

All s≤5 instances of every tail were chased to death (kills/loops only); IV-terminal
counts are before applying H3. No computation exceeded minutes; nothing farmed
(systems/sheet6/ not needed — remaining opens are lemma-sized mathematics, not
compute).

## 6. Remaining open cases (with size estimates)

1. **H3 / root-vertex kill (BLOCKING, math)**: prove that a characteristic sequence
   ending at (0,y) via case IV contradicts normalization (candidate: case IV (l)
   forces d < deg p at the root; Thm 6.1 gives deg p < d at (0,x); chart-matching
   argument needed). Without it, EVERY IV-terminal above (≈ 100 shapes, all pinned
   with explicit Q-data) is a survivor-candidate. The td≤5 proof needs this too
   (G2), so it is an audit item on solved ground first. Est: days (expert), or
   agent-audit of thesis §§2-4 charts.
2. **Case-III s-tails (~15 distinct shapes, listed in §5/report)**: for parametric
   nodes, RATIO_III = μ(ρ+m)/(κ̄(s)+m) is never s-free; per-s instances (s ≤ 5) all
   die, s ≥ 6 unproven. Each shape is one two-variable-per-s Diophantine family
   m = [κ̄(s)(μ+kν) − μρ(1+kν)]/[kν(μ−1)]; closure = symbolic divisor-bound in s.
   Est: 1-2 agent-hours per shape, mechanizable; top targets (reachable at λ=0):
   (3,3s+2,3,9s+9) [r6], (4/3,3s+2,3,4s+4) [r8-ext], (2,5s+4,5,10s+10) [r11].
3. **Case-III structural admissibility**: St 3.16/3.18 may forbid III at many of
   these nodes (thesis handles III only via λ≥1 shortcut; the ν_F-vs-Puiseux-jump
   side conditions are unextracted). Extracting them could kill all III-tails at
   once. Est: thesis §3 close-read, 0.5-1 day.
4. **Two-pole (3,3) configuration**: Prop 8.4's M≠1 kill assumes one dicritical.
   Needs either a 2-pole analogue (each pole vertex row 1: Q=(1,2,2,5)-shape) or a
   different obstruction. Genuine math; no analogue in thesis. Est: unknown; this
   is the td=6 analogue of the Domrina-Orevkov multi-dicritical split.
5. **AF2 λ-rule audit**: reverse-engineered (matches all six lemmas + ceil from
   St 9.4-integrality); needs derivation from St 9.3 (24). Est: hours.
6. **AF3 entry-M menu**: M | gcd(D,P) sanctions rows as thesis does (row-4 usage);
   superset runs (M | P) add only more III-tails, no new survivors. Justifying the
   sanction (or bashing the superset tails) closes it.
7. **μ-completeness at entries**: μ | M with M from the menu; if pole-vertex M can
   exceed deg p_F divisors (j-rescaling), larger μ become possible. All μ ≥ 7
   branches die instantly in spot checks (ratio > deg-bound), but a uniform μ-bound
   lemma (Λ ≤ 6 forces μ ≤ 6) should be extracted from §5. Est: hours.

## 7. Corrections / errata found

- **E1 (pilot)**: St 9.6 row (B) (75,51) spurious (p. 52 slip); corrected statement
  strictly stronger. [SHEET6-PILOT.md]
- **E2 (St 9.8, p. 55)**: "l=0 ⇒ M_F=1" false for the μ=2 pattern (gcd(2ν,ν+1)=2
  for odd ν); the 3ν=4m+1 family (ν=4s+3, m=3s+2) exists ⇒ missing possibility
  Q(F)~(3/4,4s+3,2,3s+3), λ=0.
- **E3 (St 9.9, p. 56)**: both "no solution" claims (μ=2 and μ=4) false; the same
  3ν=4m+1 family gives λ=0 self-loops (M=2 and M=4 resp.).
- **E4 (St 9.10, p. 57)**: μ=3 "no solution" false (2ν=3m+1 family, ν=3s+2 ⇒
  M_F=3 self-loop); also printed possibility (iv) is not derived in the proof body.
- **G1**: St 9.12 "type (3)"/"td=4" label inconsistency; adopted reading = row 4
  under Prop 5.8 (20) as printed. **G2**: St 9.12's stated kill set (M=1, budget)
  cannot kill its own IV-terminals — an unstated root-kill (our H3) is load-bearing.
  **G3**: thesis §9 silent on td≤5 rows 1,5,7,10; rows 1,7 close mechanically
  (above), rows 5,10 need the same III-tail closure as td=6 — so the thesis's
  td ≥ 6 proof is INCOMPLETE as printed even modulo its errata (rows 5,10 = td 4,5
  are independently covered by Orevkov/Domrina/Żołądek, so JC-td≤5 stands
  regardless, but "independent reproof" needs qualification in RECON/SHEET6).
- **SHEET6.md §4 amendments**: Λ=6 row count is 6 (not 7); Λ≤7 table is 14 rows
  (not 20-30); the td=6 configuration layer is 6 single-pole entries + 1 double,
  not "7 partition shapes" (Λ ≥ 3 kills the rest).

## 8. Reproduction

    cd cases && python3 sheet6_campaign.py gate      # pilot + engine gate (asserts)
    python3 sheet6_campaign.py table                 # 14-row Lambda<=7 table
    python3 sheet6_campaign.py validate              # St 9.6-9.11 re-derivation
    python3 sheet6_campaign.py bash5                 # td<=5 chains (validation)
    python3 sheet6_campaign.py bash --budget 4       # td=6 campaign
    python3 sheet6_campaign.py report                # deduped digest (this doc's §5)

Runtime: seconds per phase except bash/report (~2-3 min). Exact arithmetic
throughout (int/Fraction); no floats, no Groebner, no msolve needed at this layer.
