# Exact `p`-elimination on the order-three double-B saturation

This case preserves the corrected nine-variable characteristic-zero
`msolve 0.10.1` elimination run retaining only `p`.  The output is one
primitive integer polynomial of degree 630 with 71 nonzero terms, all powers
`p^(9*k)`, and a nonzero constant term.

Run `python3 verify_result.py` from the repository root.  The verifier
regenerates the source input, checks all frozen hashes and reconstruction
telemetry, and parses the complete polynomial.  As usual, identification of
the reported elimination basis with the source ideal is the CAS engine trust
boundary until an independent transformation/membership certificate lands.

