# Corrected post-D10 D9/D8 F-only gate

This package replaces the quarantined post-D10 D9/D8 calculation.  It derives
the missing divided Frobenius cross-carry from the integer Jacobian, retains
all six degree-six Frobenius directions, and recomputes the vertical and
`g != 0` literal-F3 compatibility gates.

Run the complete portable replay from this directory:

```sh
./replay_all.sh
```

The full replay takes roughly two minutes on the producer machine.  It uses
Python 3 and Singular.  `generate_corrected.py` consumes the confirmed D10
generator at the repo-relative path
`../as_fonly_d7_degree10_pointwise_20260824/generate_degree10_gate.py`.

Individual checks:

```sh
python3 audit_corrected_frobenius_rows.py
python3 replay_next_carry_controls.py
python3 reconstruct_representatives.py

python3 generate_corrected.py > /tmp/vertical.sing
singular -q audit_vertical_d9_section.sing
singular -q audit_vertical_core_rank.sing
singular -q /tmp/vertical.sing

STRUCTURAL=1 python3 generate_corrected.py
ENUMERATE=1 python3 generate_corrected.py
BRANCH=g STRUCTURAL=1 python3 generate_corrected.py
BRANCH=g ENUMERATE=1 python3 generate_corrected.py
```

The literal-F3 censuses are finite exact checks.  They are not compatibility
classifications over the algebraic closure and make no all-depth, no-lift,
characteristic-zero, counterexample, or JC2 claim.
