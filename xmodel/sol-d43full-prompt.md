You are GPT-5.6 Sol, IMPLEMENTATION lane (own it end-to-end). Repo:
/Users/dc/code/math/jc72108. This is THE single most decision-relevant compute
in the campaign: decide the FULLY-RECONSTRUCTED graph-preserving D43 residue-A
family ideal, which the truth test (xmodel/sol-truth.md §2.3, §3) identified as
the discriminating target for CONJECTURE A-SCALE (the G2 crux). Char 0 / mod p.

READ FIRST: xmodel/sol-truth.md (§2.3, §3), the prior D43 lane's self-notes in
notes.md (~08:35 entry) and cases/d43_graph_final_report.json, and the existing
engines cases/d43_graph_family.py, cases/d43_nf_certificate.py, cases/d25_reduce.py,
cases/d43_family2.py. SHEET6-DIRECTIONB.md §10.6-10.8.

THE EXACT GAP TO CLOSE. The prior lane's 175-row object (34 parked + 52 compat +
89 rung-26..42 graph rows) was an OVERAPPROXIMATION: it reintroduced the D23/D25
coordinates eliminated by the parked quotient as INDEPENDENT variables WITHOUT
their earlier reconstruction graph. Its algebraic points failed 94 older D23/D25
reconstruction residuals (bands 6..24). So it is NOT the true survivor family.

TASK. Build the FULLY-RECONSTRUCTED family system that imposes SIMULTANEOUSLY:
  (a) the D23/D25 reconstruction graph (the ~94 residual equations the
      overapproximation dropped -- restore them from the D25 certificate /
      d25_reduce reconstruction, so the reintroduced coords are graph-bound), AND
  (b) the rung-26..42 reconstruction graph (the 89 rows already built), AND
  (c) the 34 parked rows.
Then DECIDE EMPTY / NONEMPTY family-wide at both banked primes (105337, 105673),
using ONLY the exact-slice / linear-witness / certificate route (NO full-file
msolve -- it segfaults at rung 39-40; small subsystems and exact pivot
certificates only, as in d43_graph_family.py and the D25 certificate replay).

DECISION SEMANTICS:
  - If EMPTY (the D23/D25 graph cuts the dim-81 overapproximation to empty):
    that is the FIRST DEPTH KILL at fixed Sigray scale B=84. Produce an exact
    emptiness certificate (unit-pivot DAG / linear-combination witness of 1 in
    the ideal), replayable, at both primes. This is pro-A-SCALE at B=84.
  - If NONEMPTY: extract an explicit witness and run it through the FULL
    survivor gate (all D21/D23/D25 reconstruction residuals + rung graph +
    the s9_nu_ge_43 / floor checks). A witness passing the FULL gate = the
    residue-A carrier survives to depth 43 at B=84 = a live A-SCALE
    counterexample signal; then report its ell+ (floor context: D75 is the
    first Newton-certification depth). If the witness FAILS some gate, say
    exactly which -- the family may still be an over/under-approximation.

DELIVERABLE (write xmodel/sol-d43full.md AND emit reusable engine + certificate
JSON under cases/): the constructed system's exact census (row/var counts,
byte-exact regressions vs banked sources), the EMPTY/NONEMPTY verdict with its
certificate or witness, all gates with pass/fail counts, and an HONEST scope
label (INTERNAL / UNREVIEWED / MOD-p as appropriate). If you cannot fully decide
in one pass, report exactly how far the exact-slice route got and the precise
residual subsystem that remains, so the next lane resumes cleanly. Do NOT claim
a verdict the certificate does not support. No git operations. No msolve source
changes. Terse, technical, exact arithmetic.
