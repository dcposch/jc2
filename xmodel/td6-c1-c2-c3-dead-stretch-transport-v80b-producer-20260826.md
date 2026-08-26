# TD6 V80B dead-stretch transport point discriminator — producer report

Verdict: **PASS at one source-typed point, with an explicit scope correction.**

Two independent AWS executions of the eleven exact transport shards agree
level by level.  The producer is specialized by the literal assignment
`fb.CENTER=(1,1,1)` and has `beta=0`; it is therefore not a computation over
the generic A3 center ring.

At `(C,V,U)=(1,1,1), beta=0`, `d10` and `d15` have zero transport
compatibility tables.  Each other pure dead-stretch axis is inconsistent.  A
common displayed residual value `0|(15625/3)*S^0|0` occurs at shifted source
keys, but common values can cancel in linear combinations.  No joint-axis,
block, generic-center, neighborhood, family, full-TD6, or SP-2 conclusion is
licensed.

The full exact vector, source archive, controls, emitted tables, both AWS raw
outputs, and lightweight custody verifier are frozen in
`cases/td6_c1_c2_c3_dead_stretch_transport_v80b_aws_20260826/`.

Next gate: rebuild a single symbolic-center square-zero source problem with
all 22 licensed q directions and all 11 dead-stretch directions together;
compute its exact linear map/kernel (including `d10,d15`) before any
rank-stratified Fitting/Kuranishi successor.
