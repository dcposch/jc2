You are Grok, adversarial verifier for a Jacobian-Conjecture campaign. Repo:
/Users/dc/code/math/jc72108. Read xmodel/sol-d43full.md in full plus
cases/d43_full_final_report.json and (skim) cases/d43_full_family.py. This is
the campaign's sharpest fixed-scale depth-kill test; the claim is that the FULLY
graph-preserving residue-A D43 family is NONEMPTY mod p at B=84. A PRIOR D43
lane was later found to be an OVERAPPROXIMATION (it dropped the D23/D25
reconstruction graph). Your job: determine whether THIS one is genuinely the
complete family or ALSO drops a constraint, and whether the NONEMPTY verdict is
sound. Write to xmodel/grok-d43full-review.md.

ADVERSARIAL CHECKS:
  1. COMPLETENESS (the key question). The system is claimed to be 34 parked + 95
     old-graph rows (bands 6-24) + 89 late-graph rows (bands 26-42) = the true
     graph-preserving family in 184 vars. Is this the COMPLETE constraint set for
     a genuine graph-preserving D43 survivor, or is a constraint class still
     missing (as in the prior overapproximation)? Specifically: are the 95 "old
     graph" rows really the full D21/D23/D25 reconstruction graph (not a subset)?
     Is the 184-variable union ring correct (no coordinate reintroduced without
     its graph)? Check the census/hash-regression logic in the report. If a
     constraint class is still missing, the NONEMPTY verdict is on an
     overapproximation again -- flag it precisely.
  2. WITNESS SOUNDNESS. The witness is a 184-coordinate mod-p point claimed to
     satisfy all 218 generators + pass the 18-check survivor/floor gate. Is the
     gate the FULL survivor gate, or are decisive checks omitted (e.g. is
     s9_nu_ge_43 actually testing nu>=43, is the ell+>=37 floor check real)? Is
     the exact-slice -> full-replay logic valid (do the decoded 101-pivot points
     truly force all 184 rows zero, or only the sliced rows)? Any way the
     "NONEMPTY" is an artifact of an under-constrained slice?
  3. SCOPE HONESTY. The doc claims this does NOT disprove A-SCALE (unbounded B),
     does NOT lift to char-0, does NOT algebraize. Confirm those disclaimers are
     correct and not hiding a stronger (or weaker) result. Is "the fixed-B=84
     carrier survives to D43" the right reading, or is there residual doubt?

Output: verdict on completeness [COMPLETE / STILL-OVERAPPROX / UNSURE with the
specific missing class], verdict on the witness [SOUND / ARTIFACT / GAP], and a
one-line honest reading of what the NONEMPTY result does and does not establish.
Be a hostile referee; the campaign has been burned by an overapproximation once.
Terse, technical.
