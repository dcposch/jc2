# V26R1F exact leading-base Fitting prepass

Lifecycle: `PROVISIONAL_ROLLBACK_TAG_OPUS5_PENDING`.

This is an exact producer result with a frozen two-process replay.  It is not
canonically promoted.  The upstream V24R6R1 claim identifying this as the
honest `W=0` descendant has only the internal same-family Sol Ultra audit
`f9d2afcb...`; its independent Opus5 cross-audit and adjudication are pending.
Promotion and deeper descendants are therefore forbidden.  The intrinsic
six-variable rank-locus computation below does not use `W` or its syzygy once
the frozen matrix and base generators have been compiled, so its exact
algebraic content remains independently useful even if the descendant label
is rolled back.

## Exact statement

Work in

`R = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]`.

Let `A` be the frozen `7 x 7` grade-seven newest-variable matrix in
`ATLAS_EXACT_POLYNOMIALS.json`.  Let

`B = (G2_row1,G2_row2,G2_row3,G2_row4,G2_row5,G2_row7,F10)`.

These are the six nonzero literal grade-two rows `(1,2,3,4,5,7)` plus the
quartic `F10`; the sixth logical row is zero and is not silently substituted
for literal row 7.  Then, exactly over `Q`:

1. every `6 x 6` minor of `A` is zero;
2. the list of `5 x 5` minors is nonzero;
3. `J = B + I_5(A)` is a proper ideal; and
4. `dim(R/J) = 3`.

Consequently the closed rank-`<=4` locus of `A` survives on the six-variable
leading base and has affine dimension three.  Equivalently, the affine scheme
`Spec(R/J)` is nonempty (and remains nonempty after algebraic field extension).

This does not assert that a rational point was found, that the rank-exactly-5
stratum is nonempty, that any point satisfies the full prior ideal `P6`, or
that it extends to later grades or to an honest arc.

## Exact replay

The producer preflight computed a proper standard basis, normal form of `1`
equal to `1`, dimension `3`, nine normalized generators, and first nonzero
minor index `1`.  The tracked producer then serialized a nine-generator basis
`Graw` and a `9 x 9` transform `T`.

The fresh replay verifies entrywise:

- `matrix(J)*T = matrix(Graw)`, so `(Graw) subset (J)`;
- after recomputing `G=std(Graw)`, every generator of `J` has zero normal form
  modulo `G`, so `(J) subset (Graw)`;
- only this freshly recomputed standard basis is used to rederive
  `NF_G(1)=1` and `dim(R/G)=3`;
- deleting a nonzero transform entry destroys the tracked identity;
- adjoining `1` forces the unit ideal; and
- deleting the preregistered nonzero `I5(A)` entry fires the negative control.

All matrix and ideal zero tests are entrywise.  The replay emits no Singular
standard-basis warning.  Runtime was 2.17 seconds on one Box02 core, maximum
RSS 527,804 KiB, and swap usage zero.

## Supersession history

- R1B failed before algebra because Singular does not define direct
  `ideal==ideal`; no result.
- R1C reached the proper/dimension markers but falsely rejected an all-zero
  multi-column matrix by comparing it with scalar zero; no result.
- R1D fixed matrix checks, but its serialized replay used an untagged basis
  and printed `G is no standard basis`; producer evidence only, no theorem.
- R1E recomputed the standard basis but falsely rejected a multi-entry zero
  ideal by comparing it with scalar zero; no theorem.
- R1F uses fully entrywise checks and supersedes R1D/R1E.  The failed runs are
  retained as infrastructure evidence only.

## Custody

- R1F result: `f455c7b2177eb260df2ebfa97f174381591792683c80fdeb779f1184f6e6d70e`
- AWS evidence manifest: `f012cc1ad1b1e01ad2dbd93b718861951852c9ee9cda0fd87ddeb58983646e17`
  (all entries replayed on the producing AWS host)
- portable harvest manifest: `HARVEST_REPLAY_R1F.sha256`, SHA-256
  `a9933ef5779411e7508b48c926506744ec47d5f67637658e16eeebd748545e9f`
  (all 18 harvested entries replayed locally)
- R1F source freeze: `3d04cc180e653736d4d0cf677b942f62894f02877a4a8a86804769286aaaaa06`
- standard basis: `c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0`
- tracked transform: `2961912705a81fe6ccd6007bcf190acd88da7c5f02bf58acd3fdc2ce33c87f70`
- held atlas compiler result: `f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97`
- rollback-tagged W=0 release bridge:
  `a3564e5874b96dc70eee5a92926024ef2d536650e01c75166835f83d7aac2e73`

The producing evidence manifest records absolute AWS paths.  The additive
portable harvest manifest changes no evidence bytes and removes that custody
inconvenience.

## Firewall

No full-`P6` grade-seven compatibility, rank-atlas coverage, later-grade,
Lambda-jet, source-reachability, `Jdet`, arc, closure, counterexample, or JC2
conclusion follows.  Until the Opus5 V24R6R1 cross-audit is adjudicated, even
the interpretation as the `W=0` descendant is rollback-tagged and may not be
promoted.
