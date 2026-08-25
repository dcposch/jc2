# AS F-only vertical state-sufficiency gate

This portable package checks the exact adjugate/remainder criterion for the
corrected vertical D8 `7 x 5` affine system in the map-only `p=3,D=7` tower.

Run:

```sh
./replay_all.sh
```

The replay takes about 2.5 minutes on the producer machine.  It first verifies
the formal matrix identities without external packages, then exhausts all
`3^13=1,594,323` corrected literal-F3 assignments and compares the state
criterion against direct Gaussian solvability.

The source matrix and inhomogeneous column are loaded from the frozen corrected
producer at the repo-relative path
`../as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py`.
That producer's different-model review was still active when this package was
frozen, so the present source-to-AS interpretation remains conditional on that
review.  The matrix theorem and finite equivalence replay are exact for the
displayed input.

This is a literal-F3 state compression, not an algebraic-closure
classification, an all-depth theorem, a lift/no-lift result, or a JC2 claim.
