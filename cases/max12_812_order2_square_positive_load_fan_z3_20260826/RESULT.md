# Positive-load square fan enumeration: exact navigation result

Status: **authoritative computation for the seven preregistered forms only;
known incomplete as a full source fan and usable for navigation only.  It is
not a theorem of fan exhaustiveness, emptiness, order two, maximum twelve, or
JC2.**

The frozen V2 enumerator tested all 1,016 candidate active-set/boundary pairs:
the `2^7-1` nonempty active sets for the seven preregistered affine weight
forms, times the eight zero/positive boundary assignments for `a,r,c`.  On AWS Box02 with
`z3-solver==4.13.3.0` it found:

- 80 feasible active-set/boundary cells;
- 936 candidate active-set/boundary pairs reported UNSAT by Z3;
- 39 distinct active minimizer sets among the feasible cells;
- maximal active-set size four, attained by five boundary cells.

Every one of the 80 feasible cells has a rational witness.  A separate
dependency-free checker evaluates the affine forms with Python `Fraction`,
checks all active equalities, all inactive strict inequalities, and all
zero/positive domain conditions.  It passed both on AWS and after evidence
download.  The result JSON SHA-256 is
`26325958ca5bb5f2b119e7d5b02c52709c701c915167a84c82fecee7d5fa6180`.

The five maximal cells are represented by:

| Active forms | Zero boundary | `(a,c,q,r)` witness |
|---|---|---|
| `AC,C2,kR3,kRC` | none | `(4,4,1/2,5/2)` |
| `AC,RA2,A3,kA2` | none | `(1/2,6,3/2,7/2)` |
| `AC,RA2,A3,kA2` | `a=0` | `(0,5,1,3)` |
| `AC,RA2,kR3,kA2` | none | `(7/4,25/4,1/2,5/2)` |
| `AC,kR3,kRC,kA2` | none | `(17/2,13,1/2,7)` |

## Exact scope and use

The feasible witnesses are exact certificates for those 80 cells.  The 936
UNSAT answers are solver-derived navigation data, not independently certified
infeasibility proofs.  More strongly, a post-run source audit has identified
lower-load terms absent from the seven-form input: terms arising from the
`k6*f^(3/4)` contribution can enter a shifted unique-`AC` face for large
contact (already at `a>=7` in the audited `d=1` scaling), and `k2` support may
enter later.  Thus the seven forms are now known not to exhaust all source
corrections.  The computation may be used to shard and prioritize exact-source
clients only after the missing load-derived forms are added or separately
stratified; it may not be cited to close the square branch or any mathematical
avenue.

V1 is retained only as a custody-negative control.  V2 is authoritative;
source custody is recorded in `FREEZE_V2.sha256`, execution metadata in
`AWS_LAUNCH_METADATA.md`, and downloaded evidence in `EVIDENCE_V2.sha256`.
