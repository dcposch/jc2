Run from `/home/ubuntu/jc2`. All source presentations and frozen inputs are read-only.

- `inputs.sha256`: receipt-derived six-input manifest; verify with `sha256sum -c`.
- `counts/exact_counts.py`: full original/native monomial, generated-row and sparse-entry counts. Two independent integer dynamic programs agree throughout each rectangle.
- `reduced/reduce_counts.py`: complete homogeneous rational-unit A-pivot maps and exact reduced counts, with optional elimination of c. Modular nonzero evaluations certify nonzero polynomial images; every zero image candidate is checked over Q.
- `counts/check_root_reduced.py`: independent verification of reduced counts, contributions and c-free generating-function identity.
- `audit/audit_minimality.py`: independent exact source linear rank and cotangent-minimality proof.
- `hilbert/compute_hilbert.py`: full-original-ring finite Macaulay ranks over Q with modular crosscheck; no Gröbner basis.
- `hilbert/sparse_linear.py`: exact integer, modular, and rational-combination row-space routines.
- `hilbert/verify_linear.py`: independent FLINT controls, including bad-prime membership traps.
- `hilbert/verify_support.py`: complete N-independent ideal-piece vanishing criterion and explicit nonzero witnesses.
- `audit/audit_hilbert.py`: counts already certified finite N=1 witnesses and full charge-zero Hilbert pieces; does not equate witness and source quotients.
- `build_report.py --seal`: render checked tables into the requested xmodel report and seal its body. Without `--seal`, emits only a lane-local draft.

Python-FLINT 0.9.0 is read from the existing package directory `box/k16xempty-20260905/linear_python`; the full environment and executable hashes are recorded in `environment.json`. No fleet machine is owned by this lane.

For every requested N=2/3 block, the explicit matrix exceeds the proposed 10^7-column cutoff. No target rank or target membership result is available. Low-degree rational ranks and exact ambient counts must not be promoted to a c-power kill. Positive certification requires an exact rational identity in the original completed ring.
