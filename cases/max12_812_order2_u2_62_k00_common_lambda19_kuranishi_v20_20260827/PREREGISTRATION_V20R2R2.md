# V20R2R2 modular-normalization repair

Date: 2026-08-27

Status: **FROZEN AFTER R1 FAILURE AND BEFORE R2 EXECUTION.**

R2 may change only the arithmetic DAG evaluator and its fixture call:

1. accept an optional prime modulus;
2. reduce every addition and multiplication modulo that prime; and
3. add a mandatory control which evaluates the same `F_65521` fixture both
   with unreduced integer representatives and with nodewise reduction,
   requires at least one representative to differ, and requires every raw
   root reduced modulo `65521` to equal the nodewise-reduced root.

Exact-Q evaluation is unchanged.  The frozen tails, 140 DAG roots, source
columns, boundary restriction, contracted residual, syzygy identities,
Singular replays, and all prior sign/weight/restriction/contraction mutations
are unchanged.  Both R0 and R1 remain immutable and nonpromotable.  Any
further discrepancy fails closed.
