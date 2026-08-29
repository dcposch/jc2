# Preregistration: V20R2 contracted mixed-source compiler

Date: 2026-08-27

Status: **FROZEN BEFORE COMPILER EXECUTION OR ALGEBRA.**

V20 R0 is retained as a noncomputational design failure: its proposed
`EXTENDS/DOES_NOT_EXTEND` test in the uncontracted vector cokernel is
tautological.  `DESIGN_ERRATUM_V20R1.md` is the only live design.

## Charged source/type milestone

This producer compiles the exact common source through `Lambda^19` and the
correct parameter-contracted deformation complex.  It does not solve the
resulting nonlinear constructible-stratum problem.

It must independently reconstruct from the frozen 569-tail source:

```text
r_i(d), a_i^k10(d), a_i^k6(d), a_i^k2(d),  i=1,...,7,
```

on normalized K00 (`C6=1`), distinguish the Jacobian parameter `Jdet` from
collision ideals `J1,J2`, and replay the V14R1 relation

```text
h*r7=sum_i u_i*r_i,  h(0)=20.
```

It must consume and replay the complete 66-generator six-row syzygy module
and 87-generator seven-row control module.  For every six-row generator
`s`, it serializes the seven coordinates `Gamma(s)` and its contracted form
`<p,Gamma(s)>`.  It serializes `K(w)` and verifies

```text
D_p=<p,K(w)>,
Q_p=B/(I, <p,Gamma(s)> : s in S6).
```

For every seven-row generator `v`, it must replay the polynomial cross
relation before and after contraction.  A weight/sign mutation must fail.

## Literal finite source

The compiler derives rather than assumes the source census:

```text
169 labelled coefficients before boundary restriction,
164 free coefficients after k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0.
```

It emits a deterministic arithmetic DAG for every one of the 140 literal
coefficient equations `(Phi_i,Lambda^n)`, `i=1,...,7`, `0<=n<=19`, together
with the complete column map and the two unit opens `k10[0],Jdet[0]`.
The DAG is built directly from the frozen tails and exact rational K00
coordinate map; no raw-row substitute or literal K00 evaluation is allowed.

An independent evaluator must compare all 140 DAG roots against direct
tail-series evaluation on deterministic exact and `p=65521` fixtures.  It
must also compare

```text
h*Phi7-sum_i u_i*Phi_i
```

with the honestly weighted specialization of `D_p` through grade 19.  One
target-sign mutation and one load-weight mutation must both be detected.

## Frozen inputs and gates

The source compiler hashes all of:

- the 569-tail JSON and its canonical semantic digest;
- the exact normalized row prelude;
- V14R1 `h,u_i` and all 87 seven-row syzygies;
- the V21R1 serialized and freshly recomputed 66-row modules; and
- V20 R0 preregistration plus the V20R1 design erratum.

V21R1's local-nonmembership theorem may be recorded only as a provisional
dependency until its different-model hostile review passes.  The source/type
milestone itself does not depend on that theorem.

All computation runs on a registered AWS lane.  Source and input trees are
read-only after a SHA-256 freeze.  Missing inputs, source drift, failed
identity, fixture disagreement, mutation survival, timeout, OOM, or engine
diagnostic is `NOT_TYPED_OR_SOURCE_DRIFT`/`RESOURCE_CAP_NO_VERDICT`.

## Allowed endpoint and scope

The only successful endpoint is

```text
PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE
```

It proves exact typing and compilation only.  It does not prove existence or
nonexistence of a compatible jet, cover any nonlinear prefix strata, exclude
an arc, decide closure incidence, or imply order two, maximum twelve, or
JC2.
