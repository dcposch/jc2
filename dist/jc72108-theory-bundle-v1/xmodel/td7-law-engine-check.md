# td7-law-engine-check: zero-shared-reasoning verification of sol-td7-law.md

VERDICT: CONFIRMS LAW — 62/62 agreement. My independent engine (own derivation of the
reduced equation from BOOK-OFFAXIS.md R1.0; exact sympy/QQ(A) linear algebra; Sol's
proof and equations not used) finds DEAD on exactly the 56 cells with d_p | d_q and
ALIVE on exactly Sol's 6 exceptions; the six forced solutions and constants also
reproduce Sol's table verbatim.

Independent engine check of the claimed decision law (DEAD iff d_p | d_q) for the
Prop. 8.1(iv) local rigid solve on the 62 pinned td=7 off-axis class-B/C cells.
Method: normal form re-verified against BOOK-OFFAXIS.md; reduced equation re-derived
from the book's R1.0 statement (not taken from Sol); each cell decided by exact
sympy/QQ linear algebra; verdicts compared cell-by-cell against the law.

## 1. Normal-form verification (against BOOK-OFFAXIS.md)

Checked before trusting sol-td7-law.md §1; every ingredient traces to the book:

- R1.0 (§6, lines 209-224): at every vertex of T_a↘ ∩ V_a, in Prop 8.1(iv)
  (δpq′ − (1−u)p′q = ⊖p, ⊖ ≠ 0) every root of p is a SIMPLE root of q, every
  q-root off p is simple, ν ≥ 2 forces η ‖ q, and δ/(1−u) = d_p/d_q (line 219,
  St 8.2's proof p. 41).
- R2.2 (§7, lines 317-322): merge radical shape p_red = ⊖η^ε·Π_e(η^ν−c_e^ν)^{μ_e}
  ·Π_j(η^ν−d_j^ν)^{m_j} (ε = μ₀ if a 0-chain arrives); q = ⊖η·(each distinct
  nonzero p-orbit once)·(simple extras).
- P3 (§10, lines 521-549): classes B and C are "chain-2 at 0" (case III) with
  μ₀ = 1 (B, line 537) resp. μ₀ ≥ 2 (C, line 541); chain 1 is the sole nonzero
  arrival, frozen at mult 1 (line 522, (μ,w,M) = (1,2,1)); "All class A-C cells
  carry λ_merge = 0 (Σm = 0, ε = μ₀ arriving)" (line 547); d_p = 1 + ν_G (B,
  line 538) resp. d_p = μ₀ + ν_G (C, line 543).

Combining, with μ := μ₀ = d_p − ν and t := η^ν: p = ⊖η^μ(t − A), A = c^ν ≠ 0
(chain-1 orbit nonzero), no d_j factors (Σm = 0); q = ⊖η(t − A)s(t) with s the
extras product, deg s = ℓ where d_q = 1 + (ℓ+1)ν, i.e. ℓ = (d_q−1)/ν − 1, and
R1.0 forces the admissibility of s: s squarefree (q-roots off p simple), s(0) ≠ 0
(η ‖ q), s(A) ≠ 0 (the p-root orbit c is simple in q). This is exactly Sol's
normal form (1), so it DOES follow from the cited lines. μ ≥ 1, ℓ ≥ 1, d_p = μ+ν,
d_q ≡ 1 (mod ν) and M = gcd(d_p,d_q) were re-verified per cell by assertion in the
engine (all 62 pass).

## 2. Reduced equation: derivation from R1.0

Derived directly from the book's own formulation (Sol's equations (2)-(3) not used).
R1.0 states Prop 8.1(iv) as δpq′ − (1−u)p′q = ⊖p with ⊖ ≠ 0 (its proof uses
"= ⊖ ≠ 0", line 218) and δ/(1−u) = d_p/d_q (line 219); in particular 1−u ≠ 0, so
dividing by 1−u:

    ρ·p·q′ − p′·q = C·p,   ρ := d_p/d_q,   C := ⊖/(1−u) ≠ 0.        (RE0)

Insert the normal form p = η^μ(t−A), q = η(t−A)s(t), t = η^ν (pattern scalars ⊖
absorbed into C, which stays nonzero). With dt/dη = νt/η:

    p′ = η^{μ−1}[μ(t−A) + νt],
    q′ = (t−A)s + νts + νt(t−A)s′   (s′ = ds/dt).

Then ρpq′ − p′q = η^μ(t−A)·{(ρ−μ)(t−A)s + (ρ−1)νts + ρνt(t−A)s′} and Cp =
C·η^μ(t−A). Cancelling the nonzero polynomial η^μ(t−A):

    (ρ−μ)(t−A)s + (ρ−1)νts + ρνt(t−A)s′ = C.                        (RE)

Decision problem (the Prop 8.1(iv) rigid solve for the cell): does (RE) admit s
with deg s = ℓ EXACTLY (d_q is pinned, so s_ℓ ≠ 0; wlog monic since (s,C) may be
jointly rescaled) and C ≠ 0, with the R1.0 admissibility s squarefree, s(0) ≠ 0,
s(A) ≠ 0? Useful forced identities (t = A and t = 0 evaluations of (RE)):
C = (ρ−1)νA·s(A) = −A(ρ−μ)s(0), so C ≠ 0 already implies s(A) ≠ 0 and s(0) ≠ 0;
the engine nevertheless checks all four conditions independently. A-dependence:
η ↦ λη with λ^ν = A maps the A-instance to the A = 1 instance (s_j ↦ A^{ℓ−j}s_j,
C ↦ A·C), so solvability and admissibility are independent of the value A ≠ 0;
this was confirmed computationally (every condition value is a QQ-multiple of a
power of A — "A_monomial_ok" flag true on all 62 cells).

## 3. Cell list (reproduction)

Ran sol-td7-law.md's reproduction block verbatim: python3
cases/scratch_offaxis_pricing/px5.py (53.2 s, 1694 output lines), then the perl
extraction + sort -nu. Result: exactly 61 distinct class-C tuples (μ,d_p,d_q,ν,M),
as claimed. Added class-B (d_p,d_q,ν,M) = (3,9,2,3) with μ = d_p − ν = 1,
ℓ = (d_q−1)/ν − 1 = 3, derived the same way. Total 62 cells. Largest system:
(15,45,2,15), ℓ = 21.

## 4. Engine and decision procedure

Script: scratchpad engine.py (sympy 1.14, exact rationals, A symbolic over QQ(A)).
Per cell (μ,ν,ℓ): build monic s = t^ℓ + Σ_{j<ℓ} s_j t^j; expand (RE) − C as a
polynomial in t; require EVERY t-coefficient to vanish (the t^{ℓ+1} coefficient
vanishes identically because ρ = d_p/d_q — consistency of the deg-ℓ ansatz);
linsolve for (s_0..s_{ℓ−1}, C) over QQ(A). Outcomes observed on all 62 cells: the
system is consistent with a UNIQUE solution (asserted; no free parameters — so the
full solution set with s_ℓ ≠ 0 is one ray, and C ≠ 0 is decided on that ray).
Verdict ALIVE iff none of the four conditions fails: C ≠ 0, s(0) ≠ 0, s(A) ≠ 0,
s squarefree (gcd(s,s′) constant). Law compared: law_dead := (d_q mod d_p == 0).

Result: 56 DEAD, 6 ALIVE, 0 mismatches. Failure modes among the 56 dead: all have
forced C = 0, s(0) = 0 and s(A) = 0; 39 of them additionally have s non-squarefree
(e.g. class-B (3,9,2,3): forced s = t(t−A)², and (83,249,62,83): s = t(t−A)²).
The 6 alive cells' forced solutions (my computation, matching Sol's exception
table verbatim, incl. constants):

| cell (d_p,d_q,ν,M) | μ | ℓ | forced monic s(t) | C |
|---|---:|---:|---|---|
| (9,15,7,3)   | 2 | 1 | t − (2/3)A | −(14/15)A² |
| (10,15,7,5)  | 3 | 1 | t − (1/2)A | −(7/6)A² |
| (15,25,8,5)  | 7 | 2 | t² − (2/3)At − (1/9)A² | −(32/45)A³ |
| (15,25,12,5) | 3 | 1 | t − (2/3)A | −(8/5)A² |
| (18,27,13,9) | 5 | 1 | t − (1/2)A | −(13/6)A² |
| (39,65,32,13)| 7 | 1 | t − (2/3)A | −(64/15)A² |

All six pass all four admissibility conditions exactly.

## 5. 62-row comparison table

Sorted by (d_p,d_q,ν). "fails" lists which admissibility conditions the unique
forced solution violates (dash = none). Law column: Sol's prediction (DEAD iff
d_p | d_q).

| # | class | (d_p,d_q,nu,M) | mu | ell | my verdict | fails (of C!=0, s(0)!=0, s(A)!=0, sqfree) | law: d_p|d_q -> DEAD | match |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | B | (3,9,2,3) | 1 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 2 | C | (5,10,3,5) | 2 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 3 | C | (5,15,2,5) | 3 | 6 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 4 | C | (7,21,2,7) | 5 | 9 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 5 | C | (7,21,4,7) | 3 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 6 | C | (7,21,5,7) | 2 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 7 | C | (8,16,3,8) | 5 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 8 | C | (8,16,5,8) | 3 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 9 | C | (9,15,7,3) | 2 | 1 | ALIVE | - | ALIVE | yes |
| 10 | C | (9,27,2,9) | 7 | 12 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 11 | C | (10,15,7,5) | 3 | 1 | ALIVE | - | ALIVE | yes |
| 12 | C | (11,22,7,11) | 4 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 13 | C | (11,33,2,11) | 9 | 15 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 14 | C | (11,33,4,11) | 7 | 7 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 15 | C | (11,33,8,11) | 3 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 16 | C | (12,36,5,12) | 7 | 6 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 17 | C | (12,36,7,12) | 5 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 18 | C | (13,26,5,13) | 8 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 19 | C | (14,28,3,14) | 11 | 8 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 20 | C | (14,28,9,14) | 5 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 21 | C | (15,25,8,5) | 7 | 2 | ALIVE | - | ALIVE | yes |
| 22 | C | (15,25,12,5) | 3 | 1 | ALIVE | - | ALIVE | yes |
| 23 | C | (15,45,2,15) | 13 | 21 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 24 | C | (15,45,4,15) | 11 | 10 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 25 | C | (15,45,11,15) | 4 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 26 | C | (17,34,11,17) | 6 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 27 | C | (17,51,10,17) | 7 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 28 | C | (18,27,13,9) | 5 | 1 | ALIVE | - | ALIVE | yes |
| 29 | C | (18,36,5,18) | 13 | 6 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 30 | C | (18,36,7,18) | 11 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 31 | C | (19,57,8,19) | 11 | 6 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 32 | C | (19,57,14,19) | 5 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 33 | C | (20,40,13,20) | 7 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 34 | C | (22,66,13,22) | 9 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 35 | C | (23,46,15,23) | 8 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 36 | C | (26,52,17,26) | 9 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 37 | C | (27,81,10,27) | 17 | 7 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 38 | C | (27,81,16,27) | 11 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 39 | C | (27,81,20,27) | 7 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 40 | C | (28,56,11,28) | 17 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 41 | C | (29,58,19,29) | 10 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 42 | C | (32,64,9,32) | 23 | 6 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 43 | C | (32,64,21,32) | 11 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 44 | C | (32,96,19,32) | 13 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 45 | C | (35,105,26,35) | 9 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 46 | C | (38,76,15,38) | 23 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 47 | C | (38,76,25,38) | 13 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 48 | C | (39,65,32,13) | 7 | 1 | ALIVE | - | ALIVE | yes |
| 49 | C | (42,126,25,42) | 17 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 50 | C | (43,129,32,43) | 11 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 51 | C | (44,88,29,44) | 15 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 52 | C | (50,100,33,50) | 17 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 53 | C | (51,153,38,51) | 13 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 54 | C | (52,156,31,52) | 21 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 55 | C | (56,112,37,56) | 19 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 56 | C | (62,124,41,62) | 21 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 57 | C | (62,186,37,62) | 25 | 4 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 58 | C | (67,201,50,67) | 17 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 59 | C | (68,136,45,68) | 23 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 60 | C | (74,148,49,74) | 25 | 2 | DEAD | C,s(0),s(A) | DEAD | yes |
| 61 | C | (83,249,62,83) | 21 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |
| 62 | C | (99,297,74,99) | 25 | 3 | DEAD | C,s(0),s(A),sqfree | DEAD | yes |

## 6. Timing

- Cell-list reproduction: px5.py 53.2 s wall (1694 lines); perl extraction < 0.1 s.
- Engine (all 62 cells, symbolic A, exact QQ(A) linsolve + admissibility checks):
  0.5 s compute, 2.8 s wall including uv/sympy startup. sympy 1.14, python 3.14.
- Hand cross-checks: recurrence solution of (RE) for (5,10,3) [dead: forced
  s = t(t−A), C = 0] and (9,15,7) [alive: s = t − 2A/3, C = −14A²/15] agree with
  the engine. Total session ~2 min of compute.

Verification date: 2026-08-13. Engine + raw JSON verdicts in session scratchpad
(engine.py, engine.out, td7-C-cells.txt); nothing outside this file was modified
in the repo.
