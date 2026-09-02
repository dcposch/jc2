# Hostile review lane: CUSP-A-VOID — line-by-line gate on "case (A) is empty at every degree"

The charged producer report (Opus 5, cusp-a-n8-gate) claims, at EVERY
degree N >= 2 and H2-free for Chain I: THEOREM NO-CUSP-PREIMAGE
(F^{-1}(cusp) is empty; E = F^{-1}(A_F) is smooth), THEOREM CUSP-A-VOID
(chi(E) = 1 forces an A^1 component whose image lies in
A_F minus cusp = C^*: contradiction), THEOREM PERIPHERAL-RANK, THEOREM
MERIDIAN-SPAN (kappa*j <= a), THEOREM CUSP-A-VOID-II, COROLLARY
CUSP-A-KAPPA, kappa | a, and the identity chi(E) = nu - Sigma^*. It also
CORRECTS the coordinator's charge premise ("E has a cusps") and FLAGS an
apparent conflict with MPRIME Prop 6.1 as quoted ("unique unibranch cusp,
K_p = a-1, a_p = 1"). This is a promotion candidate of the highest weight:
composed with banked SMOOTH-KILL it would say the non-properness set of a
noninvertible Keller map is never homeomorphic to C, and under H2 it
deletes case (A) from the all-degree residual.

Your task: a hostile, line-by-line, different-model gate. For EVERY
displayed theorem: CONFIRMED / GAP / REFUTED, citing the exact line, with
the repair if one exists. Mandatory checks:
(1) properness of F over C^2 minus A_F from Jelonek's definition of the
    non-properness set, and surjectivity of F onto that complement;
(2) the section-of-a-covering argument in NO-CUSP-PREIMAGE: basepoints,
    orbits vs components, and that the full preimage of a small punctured
    ball is the restricted covering;
(3) local-to-global surjectivity of pi_1 at the cusp of x^p = y^q via the
    weighted C^*-action — state precisely the homotopy equivalence used
    and whether the cusp point c must be the origin of the cone
    (Lin–Zaidenberg normalisation vs the actual A_F);
(4) chi additivity, N-fold covering multiplicativity, chi(A_F) = 1;
(5) "no nonconstant morphism A^1 -> C^*" and that F restricted to a
    component is nonconstant (no contracted curves under an étale map);
(6) the (G-C) identity and the Riemann–Hurwitz bookkeeping at infinity;
(7) THE CROSS-CHECK: MPRIME Prop 6.1 (charged) — is its a_p = 1 / K_p
    ledger a statement about E (then it and NO-CUSP-PREIMAGE cannot both
    stand — decide which) or about the dicritical map to A_F (then no
    conflict)? Resolve it explicitly;
(8) Chain II's group theory (PERIPHERAL-RANK, MERIDIAN-SPAN, the
    conjugacy of meridian lifts, the Seifert/base-orbifold genus-0 claim)
    against the measured tables;
(9) the composed consequence with SMOOTH-KILL: its exact hypotheses and
    whether the composition is legitimate at banked typings;
(10) SUCC-1: does the mechanism extend to ANY singular point c of A_F at
    which rho(Loc_c) is transitive on the N sheets (the (B3) cusp, where
    the cage records a_{p_0} = 1, is the test case: is it consistent)?
Report a typed verdict block (CONFIRMED / GAP / REFUTED per claim;
promotion recommendation; exact scope of what may be recorded).
No CAS beyond desk-scale sympy; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/cusp-a-void-review-gpt55-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/cusp-a-n8-gate-opus5-20260902.md
charged_input=xmodel/case-a-sweep-grok46-20260902.md
charged_input=xmodel/homcover-transfer-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
2a1717aec9999608b13e3de9432d841d5746152e0b5590a87430d6a69215c459  {{LANE_INPUTS}}/cusp-a-n8-gate-opus5-20260902.md
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  {{LANE_INPUTS}}/case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
```
