# Divided-linear first-residual erratum at `p=3,D=7`

This package replaces and quarantines the earlier 29-row deep-branch
producer.  It derives the missing row `u5_3+v5_2=0` from the integer
Jacobian, provides an explicit old-pass/new-fail negative control, generates
the corrected 40-variable/30-row ideal, and verifies its exact three-piece
nonreduced cover.

Replay:

```sh
python3 replay_divided_linear_carry.py
Singular -q audit_divided_linear_carry.sing
python3 generate_corrected_deep_branch_gate.py | Singular -q
COVER=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
RADICAL=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

The `RADICAL=1` check is exact but slower.  The cover pieces are localization
aids, not asserted primary or minimal components.  Scope stops before the
accepted-second-digit and next-carry equations.
