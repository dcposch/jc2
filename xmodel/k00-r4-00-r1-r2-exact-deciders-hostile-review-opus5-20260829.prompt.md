# Hostile review: exact R4-00 R1/R2 grade-19 deciders

You are Opus 5, the independent hostile reviewer for two typed-open residual
cells in the plane Jacobian-conjecture campaign.  Write only
`xmodel/k00-r4-00-r1-r2-exact-deciders-hostile-review-opus5-20260829.md`.

Read `COORDINATION.md` and `ops/FLEET.md` completely before acting.  Do not
inspect, list, search, stat, build, modify, or control `jc2-lean`; use only
scoped git commands excluding it.  Do not edit any canonical ledger.  Heavy
or uncertain algebra/CAS is AWS-only.  Seconds-scale exact standard-library
reconstruction is allowed locally.  Preserve theorem/review separation and
use `apply_patch` for the report.

Pinned producer custody:

```text
4bd52f063289aa6dbd22b393ebec35cd90024b4ea2031a2fd21f227a5de65042
  xmodel/k00-r4-00-r1-r2-exact-deciders-sol56-20260829.md
  body: 6e420952b432f6d22d676c98431cd7bc8842fe4c9ce8c28dca54828813862083
a6e2b54fa0ca8ef3f96144d11c776a09d42175761be302745d02b8b14367ce79
  cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829/FULL_DECIDER_FREEZE.sha256
0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3
  xmodel/k00-r4-00-entry-solve-fable5-20260829.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

First verify the sealed producer full hash and body seal, then verify every
entry in `FULL_DECIDER_FREEZE.sha256`.  Treat the frozen packet JSON and
certificates as claims to attack, not as the oracle for the literal source.
The target producer claim is exact field-valued finite-jet emptiness of
CELL-R2 and both conjugate CELL-R1 branches through grade 19, because the
literal rows allegedly satisfy

```text
Jdet_0 = -(s1/64) G1,14 -(s/64) G1,15
          -(5/256) G1,19 -(3/32) G3,19 -(1/2) G5,19 - 4 G7,19.
```

Required hostile attacks:

1. Independently rebuild the seven literal affine rows from all 569 frozen
   tails and the compiler's actual normalization, load shifts, target signs,
   and `Lambda^20` truncation.  Do not use the predecessor prose, producer
   builder, serialized packet polynomials, or numerical probes as an oracle.
   Audit all relevant grade slots and check the source hashes/census.
2. Recheck the logical reductions that precede the full packets: grade-12
   cone forcing as a field-valued statement, the grade-13 `T` ladder, and
   grade-14 forcing of `A7=B7=0`.  Confirm that all omitted rows/variables are
   exactly zero, absorbable, or already forced; detect any accidental radical
   or scheme-theoretic strengthening.
3. Audit CELL-R2 literally: `p=6uz+5*kappa*s`,
   `q=-6vz+5*kappa*t`, `D=p^2+64q^2`, the `D*kappa` open, the union open
   `(s,t)!=(0,0)`, every retained grade-14..19 row, and the `Jdet_0` open.
   Audit CELL-R1 separately for epsilon `+1` and `-1`: the substitutions
   `p=8*epsilon*ii*q`, `ii^2+1=0`, `q*kappa!=0`, conjugation, signs, the same
   union open, and `Jdet_0!=0`.
4. Derive or refute the six-row `Jdet_0` identity directly from your clean-room
   rows.  Separately translate the frozen primitive normalizations and check
   each route's cofactor vector.  Explain why a unit identity with
   `1-Jdet_0*jinv` does or does not establish exact characteristic-zero
   emptiness.  Do not promote an `msolve` characteristic-zero `[1]`; modular
   output, if any, is screening only.
5. Launch a fresh reviewer-owned Singular process on an audited campaign AWS
   host and replay each sealed R2/R1+/R1- cofactor against the original ordered
   generators.  This must be a new process, not trust in producer stdout or
   the producer replay receipt.  Record host, UTC, PID/PGID, versions, input
   and output hashes, resource envelope, exit status, and replay receipt.
   Box02/Box03 carry three long-lived base diagnostics; do not stop, signal, or
   alter PIDs `448323/448356/448357/448359` on Box02 or
   `379369/379402/379403/379405/379465/379498/379500/379502` on Box03.
   Re-audit load/memory/swap before launching the seconds-scale review replay.
6. Run negative controls: mutate a used literal source coefficient or target
   sign and require the clean-room identity to fail; mutate a used packet row
   or cofactor and require the fresh replay to fail; attack the sign of the
   `Jdet` localizer.  State which mutations were detected and which evidence
   is independent of producer code.
7. Decide whether the result is a new implication of the frozen literal
   source, a packet/compiler/source error, or a producer error.  If any source
   or cell-serialization error appears, stop promotion and document the first
   precise discrepancy with an exact witness.  Do not wait for or consume the
   base-locus jobs as theorem evidence.

Give a crisp `CONFIRM`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REJECT`
verdict for each of R2, R1+, and R1-, plus one promotion recommendation.
State the maximum safe scope: normalized frozen support, field-valued finite
jets through grade 19 only.  Do not infer arcs, compatible infinite jets,
convergence, polynomial-map attainment, other supports/valuations, a
counterexample, or JC2.  End with standalone `<!-- BODY-END -->`; do not add
a seal block.
