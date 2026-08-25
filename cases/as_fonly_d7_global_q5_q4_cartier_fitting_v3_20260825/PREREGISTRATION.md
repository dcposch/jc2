# Corrected whole-Q5 Q4 Cartier/Fitting source split V3

Consume V2 analyzer SHA-256
`dd779edff09d5a7c17a1ac79f6b688879da4cf6993d8263a6f06b65755e864aa`.
Its AWS V2 run failed closed because it preregistered 76 restoration-dependent
equalities, while exact assertion-DAG inspection found 63.  Do not reinterpret
the missing thirteen equations as absent: preserve every restoration-independent
assertion as a separately hashed predecessor constraint block.

The V3 discriminator makes only the exact 76-to-63 source correction and adds
custody for the independent assertion block.  It must:

1. prove whole-cube affineness of all 63 assertions involving the 30 Q6/Q5
   restoration digits;
2. retain and hash every independent assertion and its complete dependency set;
3. exhaust the 79 compatible structural bases and all six Frobenius controls
   for coefficient-matrix rank/Fitting strata, without dividing by a pivot or
   radicalizing;
4. record the exact Q4 `[x^2 y^2]` Cartier expression and dependencies;
5. make no zero-locus emptiness or downstream Q3/Q2/Q1 inference.

The result is a source-first compiler checkpoint for the global obstruction
lane.  All substantive execution is AWS-only.
