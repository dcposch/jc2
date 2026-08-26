# Registration: normalized `(8,12)` order-four `mu_4 != 0` coefficient curve

Date: 2026-08-25

Status: preregistered; no endpoint consumed before source/hash freeze.

## Exact input

- Producer theorem:
  `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-20260825.md`.
- Frozen sparse Faber source:
  `cases/max12_high_row_probe_20260824/shared_faber_probe.py`, SHA-256
  `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f`.
- Compiler: `compile_curve.py`; it must run on registered AWS and emit both
  the normalized tail ideal and the shifted-coefficient ideal.
- Mandatory open-set condition: saturation by `r7`.

## Preregistered verdicts

1. If either ideal containment or `[z^5]V=-2r7` fails: compiler/client
   mismatch, **NO MATHEMATICAL VERDICT**.
2. If the saturated ideal is the unit ideal, the computation is only a
   screening elimination until an independently verified rational unit
   certificate is frozen.
3. If it is nonunit, record dimension and the complete exact standard basis;
   this identifies a coefficient curve only, not a source or Keller map.
4. Timeout, OOM, missing hashes, missing saturation, or engine disagreement:
   **NO VERDICT**.

## AWS-only limits

- compile cap: `134217728 KiB`, timeout `7200 s`;
- geometry cap: `402653184 KiB`, timeout `21600 s`;
- each launch records host, remote job directory, launcher PID, caps, input
  hash, engine version, UTC times, return code, and output hashes.

Actual tags, hosts, directories, PIDs, and immutable source/input hashes are
appended only after freeze and launch.

## Compile prelaunch record

- registered tag:
  `max12_812_order4_mu4_nonzero_curve_compile_20260826T000001Z_box02`;
- registered host: Box02, instance `i-010201a5da47795c4`, current public IP
  `34.203.207.55`, expected hostname `ip-172-30-0-186`;
- remote job directory:
  `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_curve_compile_20260826T000001Z_box02`;
- payload timeout `7200 s`, memory cap `134217728 KiB`;
- the remote launcher writes its PID and a registration ledger before it
  invokes the exact compiler.  No endpoint had been consumed when this
  prelaunch record was written.

The compiler completed `rc=0` on hostname `ip-172-30-0-186`; its emitted
Singular input has SHA-256
`5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`.

## Geometry prelaunch records

The following two lanes use that byte-identical input.  They were registered
before either Singular payload began.

1. Tag `max12_812_order4_mu4_nonzero_curve_geom_20260826T000211Z_box02`;
   Box02 / `i-010201a5da47795c4` / `34.203.207.55`; remote job directory
   `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_curve_geom_20260826T000211Z_box02`;
   timeout `21600 s`; memory cap `402653184 KiB`.
2. Tag `max12_812_order4_mu4_nonzero_curve_geom_20260826T000211Z_box03`;
   Box03 / `i-0ece0b9a3b4a7512f` / `98.80.65.144`; remote job directory
   `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_curve_geom_20260826T000211Z_box03`;
   timeout `21600 s`; memory cap `402653184 KiB`.

Each remote launcher writes its actual hostname, PID, caps, UTC time, and
input hash before invoking Singular.  Box03 is an independent-host replay;
its installed Singular version is recorded rather than assumed identical.

## Modular reconnaissance prelaunch

Tag `max12_812_order4_mu4_nonzero_curve_mod32003_20260826T000738Z_box02`
is registered on Box02 in remote directory
`/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_curve_mod32003_20260826T000738Z_box02`,
with timeout `21600 s` and memory cap `402653184 KiB`.  Its input is the
byte-identical emitted characteristic-zero program with only the ring
characteristic changed from `0` to the good odd prime `32003`; the remote
input hash is recorded before launch.  This lane is **SCREENING ONLY**:
neither a unit nor a nonunit basis modulo one prime is a characteristic-zero
verdict.

After that preregistered screen returned a nonunit dimension-one basis, tag
`max12_812_order4_mu4_nonzero_curve_mod32003_minass_20260826T000843Z_box02`
was registered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
again with timeout `21600 s` and cap `402653184 KiB`.  It uses the exact same
mod-32003 definitions and saturated ideal, then calls `minAssGTZ`.  Component
data from one prime are reconnaissance only and cannot certify the
characteristic-zero decomposition.

A second-good-prime screening lane was preregistered independently as
`max12_812_order4_mu4_nonzero_curve_mod65521_20260826T000929Z_box02`,
in the same-named Box02 job directory, with the same `21600 s` / `402653184
KiB` limits.  Its sole edit is ring characteristic `65521`.  Agreement of
dimension or basis size across the two primes remains reconnaissance, not a
Q-level result.

## Exact modular-standard-basis race

Tag `max12_812_order4_mu4_nonzero_curve_modstdQ_20260826T001116Z_box02`
was preregistered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
with timeout `21600 s` and cap `402653184 KiB`.  It remains over `Q`; its only
mechanical changes are loading Singular's installed `modstd.lib` and replacing
the three direct `std` calls by `modStd` with the default `exactness=1`.
The installed library documents that this performs modular reconstruction and
a final exact standard-basis test.  All ideal-equivalence, lead-relation, and
`r7`-saturation checks remain unchanged.  Missing PASS sentinels, library
errors, or disagreement with the direct-Q lanes mean **NO VERDICT**.

## Deck-quotient genus reconnaissance

Tag `max12_812_order4_mu4_nonzero_curve_quotgenus_mod32003_20260826T001547Z_box02`
was preregistered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
with timeout `21600 s` and cap `402653184 KiB`.  Starting from the already
registered mod-32003 saturated prime component, it adjoins
`X=a6^2`, `Y=a5^2*a6`, eliminates `a0,...,a6`, and asks Singular's
`normal.lib` for the geometric genus of the resulting affine quotient curve.
The invariants generate the generic fixed field for
`(a5,a6)->(-i*a5,-a6)`: adjoining `a6` and then `a5` has generic degree four.
This is a one-prime reconnaissance gate only.  A positive modular genus is
not promoted until the elimination is birationally/source checked and a
characteristic-zero quotient model is reconstructed and reviewed.

Post-run quarantine: this quotient-genus input failed open after switching
rings (`PA` was out of scope), produced undefined `QE`/`Q` errors, and then
printed the default integer `QUOTIENT_GENUS=0`.  That token is **INVALID AND
MUST NOT BE CONSUMED**.  The lane is preserved as a negative control; there
is no quotient-genus verdict.

## Exact modular-saturation race

Tag `max12_812_order4_mu4_nonzero_curve_modsatQ_20260826T001729Z_box02`
was preregistered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
with timeout `21600 s` and cap `402653184 KiB`.  It remains over `Q`, loads
the installed `modstd.lib` and `moddiq.lib`, uses exact `modStd` for the two
presentation bases, and replaces direct `sat(Itail,(r7))` by
`modSat(Itail,(r7))`.  The installed `moddiq.lib` documents modular rational
reconstruction plus final exact saturation membership tests.  The original
two-way ideal check, lead identity, nonunit/dimension output, and full basis
remain.  Any missing PASS, exact-test failure, or disagreement with the two
direct-Q controls is **NO VERDICT**.

## Exact plane-model elimination

After the exact modular-saturation lane returned a nonunit dimension-one
Q-basis, tag
`max12_812_order4_mu4_nonzero_curve_planeQ_20260826T001904Z_box02` was
preregistered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
with timeout `21600 s` and cap `402653184 KiB`.  It uses the same exact
tail/coefficient checks and `modSat`, but the block order
`(dp(a0,...,a4),dp(a5,a6))`; it eliminates `a0,...,a4`, prints the exact
plane ideal in `(a5,a6)`, and factors its generator over Q.  A nonprincipal
elimination, failed source check, failed saturation, or factorization error
is **NO VERDICT**.  Birationality of the projection is a separate gate.
