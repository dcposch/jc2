# Hostile review prompt: normalized B9 exact rational/SNF core

Audit
`xmodel/as-b9-9-12-exact-core-cokernel-producer-20260825.md` and
`cases/as_b9_9_12_exact_core_cokernel_20260825/` without trusting the
producer.

Charge independently and fail-closed:

1. regeneration of the exact all-row equation
   `E(T)=b+A*T+243*J(T)` from the pinned parent source;
2. all 276 rows, all 146 normalized coefficient variables, and the published
   hashes of `A` and `b`;
3. exact rational rank 142, augmented rank 143, and the conclusion that only
   the linear equation `A*T=-b` is rationally inconsistent;
4. right/left kernel dimensions 4/134, primitiveness and exact multiplication
   checks of the emitted bases;
5. the full Smith diagonal and 3-adic histogram, including agreement with
   finite-window ranks `85,115,127,129,129`;
6. construction of every projected P-Q term in
   `C^T(b+243*J(T))`, the count 4556, coefficient rank 68, constant content
   valuation 21, and payload hashes;
7. the strict logical firewall: a nonzero projected polynomial is a
   compatibility system, not an emptiness theorem, and no common-cubic or
   all-depth conclusion is licensed.

Do not run heavy computation locally.  Any substantive replay must run on
AWS with exact custody.  Distinguish a source-independent reconstruction
from source-identical reruns.

Write the verdict to
`xmodel/as-b9-9-12-exact-core-cokernel-review-grok-20260825.md`.
