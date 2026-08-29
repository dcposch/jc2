# V20R2 exact contracted-source compiler result

Date: 2026-08-27

Status: **EXACT PRODUCER PASS; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE
REVIEW.**

After the preserved R0/R1 fail-closed repairs, the registered one-core r6b
R2 lane emitted

```text
PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE.
```

It independently reconstructed all 569 frozen tails and derived:

- 140 literal equations `(Phi_i,Lambda^n)`, `1<=i<=7`, `0<=n<=19`;
- 169 labelled source columns, five boundary constants restricted to zero
  before any solve/saturation, and 164 free columns;
- named unit opens `k10[0]` and `Jdet[0]`, with `Jdet` explicitly distinct
  from collision ideals `J1,J2`;
- a deterministic 309,343-node exact-rational DAG for the literal equations;
- the exact scalar-contracted 66-generator deformation image and target; and
- exact six-row and seven-row representation controls.

The source replay freshly recomputed `Syz(r1,...,r6)`, obtained 66 generators,
proved mutual module generation with the frozen module, replayed all 87
seven-row syzygies, `h*r7=sum u_i*r_i`, `h(0)=20`, and every contracted cross
relation.  The honest residual

```text
h*Phi7-sum u_i*Phi_i
```

agreed through grade 19 with contraction first, followed by the honest
weighted parameter map.

Two exact-Q fixtures and one `F_65521` fixture independently evaluated all
140 DAG roots directly from the tails.  Mandatory mutations detected target
sign, `k6` weight/order, restriction-before-saturation, modular
representative normalization, syzygy sign, and contraction order.

R2 used 16.07 seconds wall time, 178,300 KiB maximum RSS, one core, and zero
swap.  The exact result JSON SHA-256 is
`a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15`.
The literal DAG SHA-256 is
`b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6`.

The original endpoint manifest has the self-listing defect recorded in
`EVIDENCE_MANIFEST_ERRATUM_V20R2.md`.  All 23 harvested evidence and
registration files are covered by the clean additive manifest
`HARVEST_EVIDENCE_R2.sha256`.

## Scope firewall

This is an exact source/type/compiler milestone only.  It does not solve or
cover the nonlinear constructible prefix strata, prove a compatible
`Lambda<=19` jet, prove an obstruction, exclude a formal or algebraic arc,
decide K00 closure incidence, or imply order two, maximum twelve, or JC2.

