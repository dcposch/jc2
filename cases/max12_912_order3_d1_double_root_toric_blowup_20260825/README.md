# D1 double-root toric blow-up wave

This package tests the remaining strict D1 double-root normal chart with the
full charged ordinary tails.  It keeps the moving cusp/axis, all six normal
coefficients, the weight-six `kbar` interaction, and the exact weight
15/18/20 targets.

`compile_toric_blowup.py` is AWS-only and emits two mathematically equivalent
but computationally independent Singular encodings.  `remote_worker.sh`
holds both phases behind sentinels and validates source hashes and terminal
markers.  See `PREREGISTRATION.md` for the exact chart and inference firewall.

No source in this directory may be run substantively on the local Mac.
