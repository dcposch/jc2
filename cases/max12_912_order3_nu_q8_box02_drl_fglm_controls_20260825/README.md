# Selected-Q8 Box02 DRL/FGLM/elimination controls

Date: 2026-08-25

This is the hardened `msolve` 0.10.1 control package for the selected-Q8
fixed modular fibre.  It consumes the pinned source-honest generator and runs
one of three independently tagged routes:

- `drl`: the full reduced degree-reverse-lexicographic basis (`-g 2`);
- `fglm`: the zero-dimensional finite-field parametrization path;
- `elim`: the two-block basis eliminating the first seven variables and
  retaining `v`.

Every lane records `--random-seed`, exact input/source hashes, engine version,
host, UTC endpoints, resource caps, and all stdout/stderr bytes.  An `elim`
output is not evidence until `run_verify.sh` reconstructs the original eight
rows, standardizes the candidate basis in Singular, and reduces every original
generator to zero.  The separately observed `msolve` 0.6.5 discrepancy—block
elimination produced a degree-473 shape set while DRL/FGLM returned `[1]`, and
the shape set failed original-row reduction—is a mandatory negative control.

Suggested Box02 shards:

```sh
run_msolve.sh REPO OUT q8_p89_w1_drl_v1  89  1 drl  8 0 14400
run_msolve.sh REPO OUT q8_p89_w1_fglm_v1 89 1 fglm 8 0 14400
run_msolve.sh REPO OUT q8_p89_w2_drl_v1  89  2 drl  8 0 14400
run_msolve.sh REPO OUT q8_p89_w2_fglm_v1 89 2 fglm 8 0 14400
run_msolve.sh REPO OUT q8_p127_w1_elim_v1 127 1 elim 8 0 14400
run_verify.sh REPO VERIFY_OUT q8_p127_w1_elim_verify_v1 ELIM_LANE 1800 33554432
```

Each algebra lane is capped at 4 hours / 128 GiB; each verifier at 30 minutes
/ 32 GiB.  All runs are modular, fixed-fibre controls.  They do not establish
generic degree preservation, characteristic-zero lifting, selected component
grouping, a trajectory, `(9,12)`, maximum twelve, or JC2.
