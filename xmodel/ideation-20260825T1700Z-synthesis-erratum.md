# Erratum to the `20260825T1700Z` synthesis — common-cubic V2

Status: **retraction of post-cutoff solver evidence; no mathematical
promotion is changed**  
Parent synthesis: `xmodel/ideation-20260825T1700Z-synthesis.md`, SHA-256
`a1cd2be8eb99e4ef19338c60d3d3d7721905afcb5268c8f68919ca2df20d74e2`

The synthesis correctly labelled the normalized B9 common-cubic `UNSAT` as
provisional pending independent source/formula audit.  That audit found a
decisive encoding error, so every conditional family-death inference from
that V2 formula is now refused.

In
`cases/as_b9_9_12_common_cubic_3p11_20260825/emit_common_cubic.py`, SHA-256
`ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556`,
the constructor

```text
bv(value) = value mod 177147
```

was used both for residue constants and for the raw positive modulus itself.
Consequently `bv(177147)` emitted zero.  All 407 remainder gates used a zero
divisor, and every intended bound `h_i<177147` became `h_i<0`.  The latter is
already contradictory.  The invalid V2 SMT has SHA-256
`182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604`;
deterministic bit-blasting reduces it to the trivial unsatisfiable CNF
`p cnf 0 1`, SHA-256
`69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`.
Thus the instant Boolector, Z3, and CaDiCaL/DRAT outcomes are encoding
negative controls, not evidence that a common-cubic locus is empty.

The reviewed normalized first nonlinear family at result SHA-256
`984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539`
is unaffected.  A V3 emitter separates residue constants from raw positive
modulus constants and audits every constructor call.  Two independent V3
emissions now agree byte-for-byte on the nontrivial formula SHA-256
`5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563`.
Its AWS solvers are still running; no corrected SAT or UNSAT verdict is
recorded here.

The strategic core-first decision remains unchanged.  The corrected lesson
is stronger software discipline: a proof-carrying emitter must type residue
constants and modulus/divisor constants separately, fail closed on every
zero divisor, assert nontrivial variable/equation counts before solver
launch, and retain a small known-SAT arithmetic control.  Until the V3 source
and formula are independently reviewed and a model or checked certificate is
replayed, the charged normalized family remains live.

Canonical nonmutating erratum:
`xmodel/as-b9-9-12-common-cubic-v2-zero-divisor-erratum-20260825.md`,
SHA-256
`cb07f729ca3a8cf32b07d7c8e4ed2cc9cf178750f21a06bb38342eb4dea4722c`.
Nothing in V2 proves an inverse-limit obstruction, family death,
characteristic-zero statement, counterexample, maximum-12 theorem, or JC2.
