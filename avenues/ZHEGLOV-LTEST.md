# ZHEGLOV-LTEST: Falsification test of Lemma "L:polynomials" (arXiv:2410.06959 v5)

Status: COMPLETE 2026-08-04. NOT REFUTED — 640/640 instances pass (see Verdict).

## 1. Lemma statement (exact + plain terms)
Source: DC5.tex lines 1721-1731 (label `L:polynomials`). Exact statement:

> Suppose g̃ ∈ ℂ[x] is a polynomial with more than one root. Suppose deg_x(g̃)=l̃,
> and d̃, z̃, A ∈ ℕ satisfy z̃=(A−1)d̃. Then there exists a solution H ∈ ℂ[x] of
>   c̃·g̃^A = H′·g̃ − ((z̃+1)/d̃)·H·g̃′,  c̃ ∈ ℂ*        (E:difeq*0)
> only if l̃/d̃ ∈ ℕ and l̃/d̃ > 1. In this case deg_x(H) = l̃(z̃+1)/d̃.

Plain terms. Fix a complex polynomial g̃ of degree l̃ with **at least 2 distinct
roots** ("one root" means g=(1+αx)^l per line 1804). Fix integers A,d̃ ≥ 1 with
z̃=(A−1)d̃ ∈ ℕ; DC5.tex:377 defines ℕ = positive integers, so z̃≥1 forces **A≥2**.
Let λ=(z̃+1)/d̃ = A−1+1/d̃. Claims:
- (N) If d̃∤l̃, or l̃=d̃, then NO pair (H∈ℂ[x], c̃≠0) satisfies E:difeq*0.
- (D) If a solution exists (hence d̃|l̃, l̃/d̃≥2), then deg H = λl̃ = l̃(A−1)+l̃/d̃.
Note: the lemma does NOT claim existence; (N) is its load-bearing content.
Used at lines 2041 (kills case via l/d<1), 2198, 2301 (forces deg_y(H) and d/l=d_2)
— the S4 case-exhaustion engine.

## 2. Hypothesis enforcement in random tests
- "more than one root": g̃ built as c·∏(x−r_i)^{m_i} with ≥2 *distinct* rationals
  r_i (sampled without replacement, asserted pairwise distinct), Σm_i = l̃.
- deg=l̃: by construction; leading coeff c random nonzero rational, asserted ≠0.
- d̃,z̃,A ∈ ℕ={1,2,...}: A≥2, d̃≥1 chosen; z̃:=(A−1)d̃≥1 computed, asserted ≥1.
  (A=1 ⇒ z̃=0 ∉ ℕ under the paper's convention: excluded entirely.)
- c̃∈ℂ*: equation is linear in (H,c̃); a solution with some c̃≠0 exists iff one
  with c̃=1 exists (scale H by 1/c̃). We solve T(H)=g̃^A, T(H):=H′g̃−λHg̃′.
- ℂ vs ℚ data: T is a ℚ-linear map once g̃∈ℚ[x]; solvability of a ℚ-coefficient
  linear system is field-independent (rank), so exact ℚ Gaussian elimination
  decides ℂ-solvability for that g̃. Degree-of-solution functionals (leading
  coeffs) are also ℚ-linear, so achievable degrees over ℂ = over ℚ.
- Completeness in deg H: if deg H=h≠λl̃, lead coeff of T(H) is (h−λl̃)·lc(H)·lc(g̃)≠0
  so deg T(H)=h+l̃−1, forcing h=(A−1)l̃+1; else h=λl̃ (needs d̃|l̃). So any solution
  has h ≤ Dmax=max((A−1)l̃+1, ⌊λl̃⌋); we solve with unknown deg ≤ Dmax+2.
- Kernel: T(H)=0 ⇒ H=c·g̃^λ, polynomial only if d̃=1; solver computes kernel
  dimension and the full set of achievable solution degrees, not just one solution.

## 3. Test design
Script: `tests/ltest_polynomials.py` (stdlib only, Fraction arithmetic).
Per instance: build g̃, A, d̃; assemble (Dmax+3)×(Dmax+l̃) exact linear system
T(H)=g̃^A; Gauss-eliminate over ℚ; record solvable?/kernel dim/solution degrees.
PASS criteria: regime with l̃/d̃∉ℕ or l̃/d̃=1 → unsolvable. Regime d̃|l̃, l̃/d̃≥2 →
unsolvable (vacuous pass, counted separately) or all solution degrees = λl̃.
Controls (not counted): one-root g̃=(x−α)^l̃, l̃≠d̃ — must be SOLVABLE with
deg H=(A−1)l̃+1 (validates solver against a known solvable family).
Regimes: R1 l̃=d̃; R2 l̃>d̃, d̃∤l̃; R3 l̃<d̃; R4 d̃|l̃, l̃/d̃≥2. Small params:
l̃∈2..6, d̃∈1..6, A∈2..4; roots/multiplicities random incl. clustered (multiple
roots with m_i>1) and boundary cases.

## 4. Results (2026-08-04, seeds 72108 and 20260804, 320 lemma instances each)
| Regime | claim tested | seed 72108 | seed 20260804 |
|---|---|---|---|
| R1 l̃=d̃ (l̃=2..6, A=2..4) | (N) unsolvable | 80/80 pass | 80/80 pass |
| R2 l̃>d̃, d̃∤l̃ (12 pairs to (8,5)) | (N) unsolvable | 80/80 pass | 80/80 pass |
| R3 l̃<d̃ (12 pairs to (5,7)) | (N) unsolvable | 80/80 pass | 80/80 pass |
| R4 d̃\|l̃, l̃/d̃≥2 (11 pairs, incl. d̃=1) | (D) deg=λl̃ if solvable | 80/80 pass | 80/80 pass |
| One-root controls (known answers) | solver validation | 24/24 | 24/24 |

**TOTAL: 640 lemma instances, 640 pass, 0 fail. No refutation candidate.**
R4 non-vacuous hits: 3+6=9 instances genuinely solvable with ≥2 distinct roots
(e.g. l̃=4,d̃=2,A=3,mults[3,1]: unique solution, deg=10=λl̃ exactly as claimed;
also (6,2) mults[3,3], (8,4) mults[3,5],[1,7], (6,2)[1,5]). Degree formula exact
in all 9. Remaining R4 = vacuous passes (unsolvable, which the lemma permits).
Solvability empirically depends only on (mults,d̃,A), consistent with affine
covariance of the ODE (2 distinct roots normalize to {0,1}).
Runtime ~1s per seed; script exits nonzero on any failure or control failure.

## 5. What was / was not tested
Tested: l̃≤9, d̃≤7, A∈{2,3,4} (A∈{2,3} for l̃≥8), 2..6 distinct rational roots
(pool: |num|≤9, den≤5), multiplicities random incl. clustered; all three
parameter shapes actually used by the paper (line 2041 uses R3-shape l̃/d̃<1;
lines 2198/2301 use the divisibility forcing d/l=d_2, i.e. R1/R2 exclusion +
R4 degree formula). Both lemma claims (N) and (D); (D) non-vacuously 9 times.
NOT tested: larger parameters; irrational/complex root configurations with ≥3
distinct roots (2-root cases reduce to ℚ by affine covariance; for ≥3 roots the
moduli (cross-ratios) were sampled only at random rational points — a failure
locus that is a proper subvariety avoiding ℚ-generic points would be missed;
note the solvable locus is Zariski-closed, so generic failure is excluded);
the lemma's own inductive proof (lines 1733-1802) was not audited line-by-line.
Latent letter-issue (never triggered): if d̃ divides every multiplicity of a
SOLVABLE instance, ker T = span(∏(x−r_i)^{λm_i}) ≠ 0 would give solutions of
degree < λl̃, breaking claim (D) as literally stated; no such solvable instance
arose (all 640 draws consistent). Reading-sensitivity: "more than one root"
must mean DISTINCT roots (confirmed by line 1804 and the proof's setup); under
a with-multiplicity reading the lemma is false (controls are counterexamples).

## Verdict
**NOT REFUTED — corroborated.** 640/640 exact-rational random instances satisfy
both the nonexistence claim (N) and the degree claim (D) of L:polynomials,
including 9 non-vacuous solvable cases matching deg H = l̃(z̃+1)/d̃ exactly.
The cheapest falsification target of DC5 (per ZHEGLOV-SCOPE T1) survives.
Small positive confidence update for the S4 case-exhaustion engine; the
expert-gated risks (R1 S6 endgame, R2, R4 per ZHEGLOV-SCOPE) are untouched.
Next per audit plan: T2 (symbolic replay of S6 Steps 4-7).

Artifacts: `tests/ltest_polynomials.py` (stdlib-only, deterministic, exits
nonzero on any failure); run: `python3 tests/ltest_polynomials.py [seed]`.
