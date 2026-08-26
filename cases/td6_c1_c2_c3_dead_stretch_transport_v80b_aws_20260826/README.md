# TD6 V80B dead-stretch transport point discriminator

This immutable package records two-host exact transport calculations for the
eleven pole-chart directions

`y = r^5 + sum(d_m r^m, m=6..16) + zeta r^17`.

## Exact scope

The producer explicitly executes `fb.CENTER = (1, 1, 1)` before rebuilding
the frozen rank-3470 transport echelon.  The base q deformation is also zero.
Consequently every statement here is restricted to

`(C,V,U)=(1,1,1), beta=0, d_6=...=d_16=0`.

This is a source-typed point discriminator, not a result over the generic A3
center ring.  It does not inherit V78's symbolic-center scope.

## Result

Both AWS hosts returned exit 0 and byte-identical compatibility tables for
every level.  At this one point:

* `d10` and `d15` produce the exact zero transport-compatibility table;
* each of `d6,d7,d8,d9,d11,d12,d13,d14,d16` is inconsistent as a pure axis;
* the first displayed residual on each inconsistent axis is the same nonzero
  scalar `0|(15625/3)*S^0|0` (at a level-dependent source key).

Identical nonzero constants can cancel in linear combinations.  Therefore the
nine pure-axis failures do **not** prove a nine-axis or dead-stretch-block
exclusion.  In particular, this package does not compute the joint kernel,
does not include interaction with the 22 q axes, and implies no neighborhood,
family, generic-center, full-TD6, or SP-2 statement.

The next licensed gate is one symbolic-center, 33-axis source replay (22 q
directions plus all 11 dead-stretch directions) followed by its exact joint
kernel/conormal and rank-stratified Fitting/Kuranishi analysis.

## Controls and custody

For each level the producer:

* differentiates the original pole-source rows using
  `j*binom(j-1,k) r^(m-5+12k)`;
* replays all 3,470 differentiated original pivot rows;
* includes derivative-only rows absent from the base echelon;
* requires a matrix-derivative omission control to fail;
* emits an exact compatibility TSV and hashes it.

The source archive and its 50-entry source-closure manifest are under
`source/`.  Raw stdout, stderr, exit status, PIDs, and emitted compatibility
tables from r6d and Box03 are under `evidence/`.  `verify.py` is a lightweight
custody/table-equivalence verifier; it does not rerun the algebra.

The earlier V80A deployment failed only because of a mistyped dependency hash
and is retained as a deployment-negative erratum in `source/`.
