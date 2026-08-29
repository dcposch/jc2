# TD6 V89H13 augmented-maximal-minor pilot result

Date: 2026-08-26

Verdict: **PASS as a finite-field pivot diagnostic; the proposed 17-by-17
maximal-minor route is withdrawn.**

The frozen V89H12 quotient was evaluated independently at the good points

```text
GF(32003), (U,V)=(1,3), H=5
GF(65521), (U,V)=(2,3), H=-23.
```

At each point, all 64 deterministic dense q samples gave coefficient-matrix
rank 2 and augmented rank 3.  Every pure q axis gave ranks `(2,3)`, except
q13 and q14, which gave `(1,2)`.  Hence all 17-by-17 augmented minors vanished
in every sample and on every tested axis.  The two lanes returned rc 0 in
0.21 seconds with zero swap.  The pure-axis telemetry is byte-identical;
dense-sample tables differ only because the two primes intentionally use
different deterministic sample sequences.

This is not a proof of characteristic-zero rank or mixed-q exclusion.  It is
a decisive routing failure for the preregistered maximal-size Fitting test:
the 18-by-17 augmented matrix is far below maximal rank, so its maximal minors
cannot expose the relevant compatibility obstruction.  Exact V89H14 support
analysis supersedes the modular structural inference and identifies the
correct two-row/six-scalar split.

No unit ideal, q-chart exclusion, source point, total-Rees map, TD6 closure,
or JC2 result is claimed.  All arithmetic ran on AWS and `jc2-lean` was not
touched.
