# Ideation round 20260905T0000Z — sealed packet (full-spectrum; COORDINATION.md)

## 1. State since the 12:00Z round (AUDIT #17 deltas (ppppp)–(dddddd); newest LIVE STATE/EVENT in notes.md binding)

PROGRAM (5/5, unchanged): JC2 along Moh's two-point M_s=n−2 line = (H1) split ⇒ joint chart inconsistent ∧ (H2) no-split ⇒ descent + theorem (T). NOT all of plane JC2 (one-place/Abhyankar–Moh is a separate program; the routing maps are the unproved interface).

MAJOR PROGRESS TODAY:
- **D=108 CLOSED at skeleton level** (17(bbbbbb)): split branch dead (17(ddddd)) + no-split K=8 row dead (exact-Q UNIT_IDEAL, 36-var reduced chart).
- **(99,66) SKELETON verdict COMPLETE for all three configurations** (split B 17(pppp), split C 17(tttt), unsplit A=case(A) 17(bbbbbb)) — the case-(A) QUALIFICATION is DISCHARGED. Necessity (17(hhhhh)) + gauges N3/N4 discharged (17(jjjjj)) + classification N2 discharged (17(sssss)). Rests on N1 only.
- **N1 = a finite kill list toward the DEGREE-WIDE (99,66) theorem** (17(cccccc)/(dddddd)): exactly 8 (1)–(13)-admissible skeletons at (99,66); 3 DEAD (S8=(8,8), S6, S5), 5 OPEN (S1,S2,S3,S4,S7 — u_s≥2 joint charts, 2271–3441 coeffs after two corner pins). If all 5 fall ⇒ NO KELLER PAIR OF DEGREES (99,66) ⇒ the published open case of Moh's ≤100 theorem RESOLVED. ERRATUM caught: 17(cccccc)'s S6 used the wrong descended Jacobian exponent (ℓ = v_s−u_s−1 is correct; k=4 ray & D=108 used it right).
- **K16 ray reduced to ONE atom** (17(ppppp)/(rrrrr)/(uuuuu)/(wwwww)): (V0)-for-all-t ⟺ CRITERION RANK ⟺ T_{t,2t−1} a nonzerodivisor on the Eagon-Northcott curve Γ ⟺ √(I₂(N)+(W_r)) = m factorwise. Length L_t = 2·binom(3t+1,t−1) derived (CI-SERIES). Coprime-leaders and degree-only routes PROVED impossible. Coefficient recursion derived (triangular, not rational in (t,r)). JC2-relevant target is the WEAKER (8.1) = τ_t ∈ radical(I_{t,+}). Four deep lanes SHARPENED without closing — needs a NEW idea. Fixed-t (T) t=1..7.
- **k=4 ray** (17(vvvvv)/(yyyyy)/(zzzzz)): case(A)=K9, D=108 no-split=K8, δ₁'=0 row=K7 unified. Composite arm (β∈k ⇒ h|J ⇒ composite) PROVED uniform/unconditional. Uniform theorem deg(g²−f³−λf)=K+6. Census members K=7,8,9 all CLOSED (pin + lower-band + guided_gb); the ALL-K uniform kill is NOT proved (degree tower saturates at c=3; residual grows ~4K/3).
- **(H1) general**: disc route (17(ooooo)) and NONRES arithmetic predicate (17(ttttt)) both REFUTED as uniform mechanisms; the killing augmented Schur/Fitting row is chart-specific. Deliverable is the census (166/296 sharpened rows); the per-row kill METHOD (top pin + exact lower-band parametrization → ~36 vars → guided_gb) is validated and generalises.
- **Tooling SHIPPED** (17(xxxxx)): box/lib/guided_gb.py (Hilbert-hinted, modular+CRT, properness-scoped, control battery) + staged_band_emitter.py, all tests pass.

RUNNING (receipts-only; do NOT open .md until final_status): g9966-n1-batch3-opus5 (building+killing the last five (99,66) skeletons S1–S4,S7).

## 2. Questions
Q1 (K16, the standing atom): a NEW idea for OPEN[K16-Q-NONVANISHING-ON-GAMMA] — prove T_{t,2t−1} is a nonzerodivisor on the Eagon-Northcott curve Γ (all t), OR prove the weaker (8.1) τ_t ∈ radical directly. The coefficient recursion, Γ's Hilbert series, and √(I₂(N)+(W_r))=m are in hand; four Gröbner/degree/resultant routes are refuted. What structural idea (a valuation on Γ, a specialization argument, an intersection-theory count, a deformation) closes it uniformly?
Q2 (degree-wide (99,66) / N1): is killing the 5 remaining skeletons S1–S4,S7 the right route, or is there a UNIFORM argument across the 8 admissible V-assignments (e.g. a single obstruction parameterised by V) that closes N1 at once? And is Moh's (1)–(13)-completeness (every degree-(99,66) pair has one of these 8 skeletons) citable, or itself a gap?
Q3 ((H1) general census): with the per-row kill method validated, what is the most efficient path through the 296-row / 166-group u_s≥2 census — a batched guided_gb sweep, a uniform pin+parametrization theorem, or the augmented-Schur-row theorem? Price it.
Q4 (the finish): does the degree-wide (99,66) closure method (enumerate admissible skeletons at a degree, kill each) generalise to a DEGREE-WIDE program for ALL two-point degrees, and does that, with K16 (H2) and the routing maps, constitute a complete proof of the two-point stratum? Challenge the framing; name the single most valuable next object.

## 3. Deliverables (per submission)
Disposition vector (changes only); Q1–Q4 with typed claims, bounded quantities, cheapest tests; three idea cards; the single first lane; continue/redesign/stop for the running lane (receipt only); one systems upgrade; OPENs raised with the collision scan (ops/open_collision.py, round/receipt-guarded). Target 25–45KB; 150 minutes; seal with <!-- BODY-END -->.

<!-- BODY-END -->
