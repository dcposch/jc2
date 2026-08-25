# Hostile bounded review: TD6 q2-beta raw `u-h-zero` and origin V70

Referee: independent algebraic/source/custody pass of the frozen V70
repair of the V33/V69 localization debt.  Operations used: full read of
the charged surfaces; `tar` extract of the 125-KiB V69 archive into
`/tmp/jc2-td6-u-h-zero-v70-review-grok-20260825/`; independent SHA256 via
Python `hashlib`; structural inspection of stratum typing, wrapper
monkeypatches, parent complete-certificate formula, `x_power_expansion`,
`q_beta` / `q_beta'`, original-row GE, and the set-theoretic cover; short
stdlib comparison of dual-host bytes, omit diffs, operator-failure prefix,
and `verify.py`.  The two `u-h-zero` transport events and the origin
transport incompatibility are identified both from V70 stdout and by
matching already frozen trivariate `C=U=0` / origin transports of the
same matrix.  No producer execution, no CAS, solver, Lean, or other
substantive computation.  Stored PASS strings are not authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-aws-20260825.md`,
`xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-prereg-20260825.md`,
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md`,
`cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_aws_20260825/`.

Prior hostile review of the surviving open:
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-review-grok-20260825.md`, SHA-256
`706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291`,
verdict `CONFIRMED_WITH_REPAIRS`.

Producer actually executed, from frozen stderr of the repaired rc-zero
runs:

```text
timeout --signal=TERM --kill-after=120s 8h /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/replay_v70.py --stratum=u-h-zero

timeout --signal=TERM --kill-after=120s 8h /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/replay_v70.py --stratum=origin
```

Omission controls append `--omit-direct-qprime`.  The preregistration
command naming V69 `replay.py` directly is not what ran; the wrapper is.
Expanded tree basename `td6-aws-handoff-20260825-v69` matches the tarball
name.  Dual `main()`, V31 `main()`, and V33 `main()` are not called.

Import/hash pin chain executed by the repaired producer, in order:

1. V70 `replay_v70.py` (`07cf6df3…`, independently recomputed; listed in
   `V70_SOURCE.sha256`) pins and imports
   `td6_c1_c2_c3_q2_n13_raw_canonical_v69_20260825/replay.py`
   (`PARENT_SHA256=9a518a4b…`).
2. V69 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py`
   (`DUAL_SHA256=cf3f3f02…`).  Dual defines `H = C - 3*U**2`.
3. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`TRI_SHA256=1fb51264…`), then calls `tri.configure()`.
4. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
5. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256`); transport then loads
   `c1_pencil.py`, which pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

V33 `td6_c1_c2_c3_q2_n13_raw_20260825/replay.py` and V31
`td6_c1_c2_c3_q2_n13_20260825/replay.py` are in the archive and in the
recursive source checks, but they are not imported by V69 or V70.

---

## Charge 1 — Source typing

**Result: holds in source.**  The main raw branches are exactly `C=U=0`
over `Q(V)` and `C=V=U=0`, inside the fixed source-typed normalized A3
q2-beta section.  Polynomial `beta` and direct
`q_beta'=1+2 beta t+25 t^24` are retained.  The V33 `U=0,D(C)` echelon is
not specialized through `C=0`.

- V69 accepts exactly one `--stratum=` and optional `--omit-direct-qprime`.
  The wrapper then asserts `p.STRATUM in {"u-h-zero", "origin"}` before
  any GE.  Frozen argv of the theorem runs is `--stratum=u-h-zero` or
  `--stratum=origin` only.  Stdout:
  `raw_center_stratum=u-h-zero` / `origin`, `direct_qprime_retained=true`.
- Trivariate `STRATUM` is read from the same argv at import, before
  `center_coordinates()` runs.  On `"u-h-zero"` it returns
  `Rat3(0), Rat3(V), Rat3(0), "C=U=0 over Q(V)"`.  On `"origin"` it
  returns `Rat3(0), Rat3(0), Rat3(0), "C=V=U=0"`.  It does not take the
  `generic`, `u-zero`, `h-zero`, `v-zero`, `v-h-zero`, `v-cplus1-zero`,
  `v-cplus5-zero`, or `b3-param` branches.  Frozen stdout is
  `source_center=C=U=0 over Q(V)` and `source_center=C=V=U=0`.
- Dual’s `H = C - 3*U**2` makes `C=U=0` the same locus as `H=U=0`.  The
  stratum name `u-h-zero` is therefore the raw intersection charged by
  the V33 erratum, not a different center equation.
- V69 copies those three coordinates into `r.fb.CENTER` and clears the
  x-power cache before `build_transport`.  `x_power_expansion` is
  polynomial in `(c1,c2,c3)`:

  ```text
  coeff *= c1**a1 * c2**a2 * c3**a3
  ```

  `c1=0` drops the `C` terms, `c3=0` drops the `U` terms, and the origin
  leaves only the `t*s^4` summands.  There is no division by `C`, `V`, or
  `U` in that expansion.  A vanished-center inversion anywhere else in
  the exact arithmetic would have been `ZeroDivisionError`; both strata
  completed.
- Transport g-boundary is `{1: 1, 25: 1}` (the `t + t^{25}` skeleton).
  The `beta t^2` term enters only through `source_vector_beta`.  Direct
  `q'` is installed after a successful transport by `configure_qd(True)`:
  `qd.Q_PRIME = {0: 1, 24: 25, 1: BetaPoly([0, 2])}`, i.e.
  `1 + 2 beta t + 25 t^{24}`.  Origin never reaches `configure_qd`,
  because transport already returns; that is correct, not a dropped
  `q'`.  `--omit-direct-qprime` is absent from the theorem argv.
- Printed `q_beta=t+beta*t^2+t^25`.  `p = t^{15}` is the f-boundary
  `{15: 1}`.  F1 patterns, pole scale/data, and the licensed zero dead
  stretch remain the imported `fb` constants.
- `solve_stage` still raises `AssertionError("beta-dependent pivot:
  exceptional strata required")` if any accepted lead has
  `lead.degree != 0`.  `BetaPoly.inverse` exists only for degree 0.
- V69 rebuilds `ordered` transport rows from `build_transport` after the
  new `CENTER`.  It never loads V33 pivots, never imports V33 `replay.py`,
  and never substitutes `C=0` into a `U=0` fraction-field echelon.  The
  event fingerprint confirms a rebuild: V33/`U=0` events were
  `4804,(f,X,-1,2),193;num=(-C)` and `5380,(g,X,-1,2),1289;num=(-C)`;
  V70/`C=U=0` events are the same keys at the same rows but pivot
  columns `194/1290` and numerator `-V`.

**Defects.**  None in the typing.  Same expository nits as V33: V69
prints `ring=E(C,V,U)[beta]` after coordinates have been specialized;
the working rings are `E(V)[beta]` and the constant field.  The imported
trivariate module docstring is leftover B3-chart language.  The
`center_coordinates()` body, not that docstring, is what ran.

**Survival.**  The producer is source-typed as the raw charts `C=U=0`
over `Q(V)` and `C=V=U=0`, with polynomial `beta` and (on the first-band
leaf) direct `q_beta'`, inside the fixed normalized A3 q2 section.

---

## Charge 2 — Wrapper fidelity

**Result: holds.**  `replay_v70.py` hash-pins V69 and changes only
observability: transport-event/chart display, complete-localization
composition, and exact wrong-row controls.  Monkeypatch dispatch
separates the transport and affine-stage replay paths.

Wrapper SHA-256 `07cf6df3b4f7c5c43f02dcbc30bff118618630090cbc85bd0cb587975c303179`
pins V69 `9a518a4b877f32548d99ecfa6a9eb15650a8a301e3277991da98744bed8e5385`.
Stdout reprints `v70_parent_sha256=9a518a4b…`.  Extracted V69 `replay.py`
live-hashes to that pin.

Three patches, all after `exec_module` and before `p.main()`:

1. `p.tri.factor_transport`.  Calls the original, records
   `transport_rows` and `transport_chart`, prints every event and
   `r.transport_chart_polynomial(events)`.  Return value unchanged.
   `main` looks up `tri.factor_transport`, which is this attribute.
2. `p.parameterize`.  LCMs first-stage (or later affine-stage) row
   coefficients and RHS by the parent formula

   ```text
   denominator_lcm(coefficient for _, row, rhs in rows
                   for coefficient in list(row.values()) + [rhs])
   ```

   then calls original `parameterize`.  Origin never reaches this
   function.  `u-h-zero` does, once, with `stage="first"`.
3. `p.emit_stage_incompatibilities`.  Calls original V69 emit first
   (inner residual/Bezout/combination LCM, still printed as
   `{stage}_compatibility_certificate_denominator`).  Then, if there is
   a bad residual:

   - transport: `source_denominator = transport_chart ** 0` (one);
     replay via `replay_transport_combination` against original
     transport rows, RHS from `source_vector_beta`;
   - affine (`first`): `source_denominator` from the parameterize
     capture; replay via `replay_combination` against packed stage
     rows and stored RHS;
   - complete chart `monic(transport_chart * source_denominator * inner)`;
   - wrong-row: copy the combination, add `BetaPoly(1)` to the minimal
     original index, assert the perturbed identity fails.

V69 `parameterize` and `transport_beta_incompatibilities` resolve
`emit_stage_incompatibilities` as a module global at call time, so the
patch is live on both paths.  Original `emit` is bound separately and
is not re-entered.  GE, pivot choice, residual arithmetic, and V69
original-row reduction are not rewritten.

The two replay helpers are not the same function.  Affine replay uses
packed `row`/`rhs` with `pack`’s convention `RHS = -constant`.
Transport replay uses stored matrix coefficients converted by
`BetaPoly(scalar(coefficient))` and an independently rebuilt
`source_vector_beta` RHS, matching V69’s own transport residual
construction.  A monkeypatch mix-up (affine replay on origin, or
`captured["transport_source_denominator"]` on a transport stage) is
exactly the v70c operator failure; the repaired wrapper does not do
that.

Parent complete-certificate formulas in the imported trivariate
emitter, still sitting in the same `c1_c2_c3_trivariate.py`:

```text
first:      transport_chart * first_source * combination * residual
transport:  transport_chart * combination * residual
```

V70 inner LCM also includes Bezout weights and `gcd.inverse()`.  On
both frozen theorem streams that extra LCM is `(1)`, so the printed
complete charts `V^3` and `1` are the parent charts.

**Defects.**  None load-bearing.  The preregistration still quotes V69
`replay.py --stratum=u-h-zero` rather than `replay_v70.py`.  That is a
stale command, not a different algebra: the wrapper is a strict
observability shell around that same V69 file.

**Survival.**  Algebra is V69’s.  Displayed localization is the parent
complete chart.  Wrong-row controls are exact negative identities on
the same original rows.

---

## Charge 3 — `u-h-zero`

**Result: holds as dual-host producer-asserted original-row algebra on
`C=U=0,D(V)`, with an exact shared-transport fingerprint.  Ranks and
the 14-row combination were not recomputed here.**

Byte-identical mathematical stdout on Box02 and Box03, SHA-256
`2431ed0217d8d71dce2929a8581036d0e11921396dff661466288901243f4ebd`.
Both `rc` files are `0\n`.  Source-check closure on both hosts.
`source_center=C=U=0 over Q(V)`, `direct_qprime_retained=true`.

Frozen stdout:

```text
transport_rank=3470/3602
v70_transport_event_count=2
v70_transport_event[0]=4804,('f', 'X', -1, 2),194;num=(-V);den=(1)
v70_transport_event[1]=5380,('g', 'X', -1, 2),1290;num=(-V);den=(1)
v70_transport_chart_denominator=(V^2)
v70_first_source_denominator=(V)
first_rank=36/132
first_dependent_count=1
first_incompatibility[0]_row_index=13
first_incompatibility[0]_key=('X-2', 14)
first_incompatibility[0]_degree=0
first_incompatibility[0]_source_row_count=14
first_compatibility_gcd_degree=0
v70_first_inner_denominator=(1)
v70_first_complete_certificate_denominator=(V^3)
v70_first_whole_raw_stratum_empty=false
v70_first_incompatibility[0]_wrong_row_control=true
```

`factor_transport` records an event only when
`lead.numerator.total_degree() or lead.denominator.total_degree()`.
Both events have numerator `-V` and denominator `1`.  The parent chart
is the monic product of nonconstant event numerators:
`(-V)*(-V) = V^2`.  Complete localization is

```text
V^2 * V * 1 = V^3.
```

`parameterize` returns `None` as soon as `emit_stage_incompatibilities`
sees a nonzero residual, so previous/current stages and N13 are not
entered.  The PASS banner is `TD6-A3-Q2-N13-RAW-FIRST PASS`.

The transport matrix does not depend on `q_beta`.  V70’s per-250-row
pivot/event stream is byte-identical in the checkpoint numbers to the
frozen trivariate `C=U=0` transport
(`cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v12/tricenter-u-h-zero.stdout`):

```text
rows=4750;pivots=1716;events=0
rows=5000;pivots=1966;events=1
rows=5250;pivots=2215;events=1
rows=5500;pivots=2465;events=2
… pivots=3465 at rows=6500;  rank 3470/3602
```

That frozen classical transport printed the same two events, the same
chart `V^2`, the same first-source `V`, the same first rank `36/132`,
the same dependent key `('X-2',14)` at packed `row_index=13`, and the
same complete chart `V^3`.  V70’s combination is 14 original q2-beta
rows rather than the classical 1-row multiplier; that is the same
pattern as V33 on `U=0,D(C)`.

`pack` keys are `(family, degree)`.  Packed degree 14 is first-J
`t^{14}`.  `source_row_count=14` is `len(combination)`.  Dependent
records start at `{row_index: 1}` and reduce through stored original
combinations of earlier pivots.  V70 then re-asserts
`sum weight_i * original_row_i` has empty matrix part and RHS equal to
the residual, and that adding `1` to the minimal original weight
destroys that identity.

There is exactly one bad residual, so `polynomial_ideal_gcd` is monic
scaling of that single generator.  Degree 0 plus monic forces `gcd = 1`
in `E(V)[beta]`.  The gcd SHA-256
`597c6860e914abbb80705004c4465829d8c400df0ae2b76bf08f23ff8b1610f0`
is the same byte string as the origin unit gcd; V69’s serializer is
`sorted-Rat3-coordinate-v1` and asserts `" object at 0x" not in`
the canonical form, so this is a content hash of the unit, not an
address.  Signs: no extra `normalizer = -1`.  `pack` uses RHS
`-constant`; affine replay is against that same convention.

This certificate inverts `V` three times and therefore excludes exactly
`C=U=0` on `D(V)`.  It does not specialize to `V=0`.
`v70_first_remaining_denominator_strata_required=true` is the correct
flag; the origin leaf is mandatory.

**Defects.**  None load-bearing.  The printed ring still names `U`.
V69’s `first_compatibility_original_row_replay=true` remains a banner;
the load-bearing replay is the V70 assert that actually ran.

**Survival.**  First-J q2-beta incompatibility on `C=U=0 ∩ D(V)` for
every beta, in this fixed section.  Complete chart `V^3`.  Not the
origin, and not a C-specialization of V33.

---

## Charge 4 — Origin

**Result: holds as dual-host producer-asserted original-row transport
algebra on `C=V=U=0`.  Rank and the 21-row combination were not
recomputed here.  The wrong-row control is a real negative identity on
the repaired wrapper; the rc-one v70c runs never reached it.**

Byte-identical mathematical stdout on Box02 and Box03, SHA-256
`90df496c59c8283c85cec26521a2b422d6ca8d658aa0e8802c968052cd505d67`.
Both repaired `rc` files are `0\n`.  Source-check closure on both hosts.
`source_center=C=V=U=0`, `direct_qprime_retained=true`.

Frozen stdout:

```text
transport_rank=3468/3602
v70_transport_event_count=0
v70_transport_chart_denominator=(1)
transport_incompatibility[0]_row_index=6460
transport_incompatibility[0]_key=('g', 'X', -19, 20)
transport_incompatibility[0]_degree=0
transport_incompatibility[0]_source_row_count=21
transport_compatibility_gcd_degree=0
v70_transport_inner_denominator=(1)
v70_transport_complete_certificate_denominator=(1)
v70_transport_whole_raw_stratum_empty=true
v70_transport_incompatibility[0]_wrong_row_control=true
TD6-A3-Q2-N13-RAW-TRANSPORT PASS
```

Rank `3468 = 3470-2` matches vanishing of the two `u-h-zero` V-pivots.
Checkpoint stream:

```text
rows=5000;pivots=1966;events=0
rows=5250;pivots=2214;events=0
rows=6500;pivots=3463;events=0
```

versus `u-h-zero` `2215` at 5250 and `3465` at 6500.  No nonconstant
transport leads, so the chart is one.  Complete localization is
`1 * 1 * 1 = 1`.  First band is correctly skipped.

Row index `6460` is the original index in `ordered`, not an echelon
slot.  V69 `transport_source_combination` starts at `{row_index: 1}`
and reduces through original combinations of earlier transport pivots.
`source_row_count=21` is `len(combination)`.  The same original row,
key, rank, zero events, 21-row ancestry, unit residual, complete
denominator one, and plus-one negative control already appear on the
frozen trivariate origin
(`cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v14/origin.stdout`),
where `ancestor_count=21` and `source_row_count=21` agree.  V70’s
residual SHA is a BetaPoly content hash, not the classical vector hash;
the locus is the same.

Source sign: V69 rebuilds the transport residual as
`sum weight * source_vector_beta(key)` and asserts it equals the
propagated incompatibility.  V70’s transport replay uses that same
formula and asserts equality with the stored residual.  The positive
assert would have aborted on a sign/RHS mismatch.  It did not.

Wrong-row control: the repaired wrapper copies the combination, adds
`BetaPoly(1)` to `min(combination)`, and asserts nonempty matrix or
changed RHS.  If the minimal original row were the zero row, both
disjuncts would fail and the process would abort.  The banner
`v70_transport_incompatibility[0]_wrong_row_control=true` is therefore
behind a successful negative identity, not an unconditional print.
The v70c operator-failure streams are an exact 48-line prefix of the
repaired origin stdout: they contain the unit obstruction through
`transport_beta_root_stratum_required=false` and then die on
`KeyError: 'transport_source_denominator'` before any V70 complete
or wrong-row line.  Those rc-one streams are not theorem evidence.

**Defects.**  None load-bearing.

**Survival.**  Raw transport incompatibility at original row 6460 /
`('g','X',-19,20)` on `C=V=U=0` for every beta, complete chart one,
in this fixed section.

---

## Charge 5 — Controls and custody

**Result: listed hashes recompute; source-check closure holds for the
declared manifests; repaired runs are rc zero and dual-host
byte-identical; the portable V69 archive contains the executed pin
chain; omission controls reproduce both obstructions as residuals and
charts, not as identical first-band ancestry; only the repaired
rc-zero wrapper is theorem evidence.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `source/td6-aws-handoff-20260825-v69.tar.gz` | `9e89808cca9d24ec5182466b40e53d612317a4f03c70053a9c490e957ab51f38` | MANIFEST, README, xmodel, prereg |
| `source/replay_v70.py` | `07cf6df3b4f7c5c43f02dcbc30bff118618630090cbc85bd0cb587975c303179` | MANIFEST, V70_SOURCE, xmodel |
| `source/V70_SOURCE.sha256` | `6aed38de4ac1642b9351dd688793fdce0b98b5dc2b7b3e25d3ebc9c81c9d5986` | MANIFEST, xmodel |
| `source/RUNBOOK.md` | `4118ba8bfd46de5a382293bb78be1fbe9c6b22ab501fc86d69b3484a6f60e486` | MANIFEST, V70_SOURCE as `V70_RUNBOOK.md` |
| extracted V69 `replay.py` | `9a518a4b877f32548d99ecfa6a9eb15650a8a301e3277991da98744bed8e5385` | V69_SOURCE, V70_SOURCE, wrapper pin |
| extracted `V69_SOURCE.sha256` | `fe39baefa6bcec511646397b5060ee8a4d555d17c2310b40b0035ff5931900ac` | V70_SOURCE, prereg “outer source manifest” |
| `evidence/u-h-zero/*/u-h-zero.stdout` | `2431ed0217d8d71dce2929a8581036d0e11921396dff661466288901243f4ebd` | MANIFEST, README, xmodel, verify.py |
| `evidence/origin/*/origin.stdout` | `90df496c59c8283c85cec26521a2b422d6ca8d658aa0e8802c968052cd505d67` | MANIFEST, README, xmodel, verify.py |
| `evidence/controls/u-h-zero-omit-box02/u-h-zero-omit.stdout` | `4a31f5273149fd886ecc2a40435b309d01d75941160c6c0b983cf8ca7fbabb43` | MANIFEST, xmodel |
| `evidence/controls/origin-omit-box02/origin-omit.stdout` | `6005d4ad35ac6262e027c246de5823ba35d1446329f8d5630c6f309073b88a3a` | MANIFEST, xmodel |
| theorem `rc` files | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body `0\n` |
| operator-failure `rc` | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` | MANIFEST; body `1\n` |
| README | `0b1c755cb84fdeab02937d04aa35a1cf11178139ee658702b224ec4bc228533a` | MANIFEST |
| `MANIFEST.sha256` | `8008772785dc927a8048dfc9199d45409e84604fdd3c301e59ba71a3ae2fd40b` | FREEZE |
| `DEPENDENCIES.sha256` | `b7eb702e1075ed725cfe81ac85305732a03ae09c9aa057fdfc04c8abb3fd4830` | MANIFEST |
| `verify.py` | `f0526ff26ef7308224e359fbd34f61dfd04514c74fff2d724aefe09b6726720a` | MANIFEST |
| xmodel AWS report | `9013ec370a4d5651c08afa921a0b56e799651f1f490908208221240baddd8c45` | FREEZE |
| prereg | `899c6df7438c9572a503b5a8039d110323ee9a35c8d13bddf5eb7aeb44f61cae` | FREEZE, DEPENDENCIES, MANIFEST via case |
| erratum | `df74697606e1b6d64fac91fdce0f063046f5cd77385114321de507da94c842bd` | FREEZE, DEPENDENCIES |
| prior V33 review | `706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291` | DEPENDENCIES, erratum |

All 109 MANIFEST paths recompute.  All 4 FREEZE paths recompute.  All 5
DEPENDENCIES targets recompute.  All 31 `SOURCE.sha256` members, all 3
`V31_SOURCE.sha256` members, both `V33_SOURCE.sha256` members, all 6
`V69_SOURCE.sha256` members, and all 4 `V70_SOURCE.sha256` members
recompute against the extracted tree plus the case-bundled wrapper and
runbook.

Source-check stdout on the theorem runs: 31/31 `: OK` (base), 3/3
(V31), 2/2 (V33), 6/6 (V69), 4/4 (V70).  `verify.py` prints
`TD6-Q2-BETA-U-H-ZERO-V70 VERIFY PASS`.  The extracted V69 tree has the
declared members plus the unlisted manifest files themselves; the V70
files are added at extract time as the runbook states, and are what
the theorem stderr executed.

Supervisor PIDs match the AWS tags: `191766` / `82534` (`u-h-zero`
Box02/Box03) and `191774` / `82542` (origin).  Wall times ~11 s and
~16 s, RSS ~77 MiB and ~62 MiB, both far under the stated 12-GiB cap.
Stderr is `/usr/bin/time -v` plus, on the failed runs, the KeyError
traceback.  Host IPs `34.203.207.55` and `98.80.65.144` do not appear
in stdout or stderr.

**Omission controls.**  Both ran on Box02 only, rc zero, repaired
wrapper.  `direct_qprime_retained=false`.

- Origin omit is byte-identical to the theorem origin stream except
  that flag.  Residual SHA, 21-row certificate SHA, rank, and complete
  denominator one all match.  Transport does not call `configure_qd`,
  so this is the expected identity, not a second test of `q'`.
- `u-h-zero` omit matches rank `3470/3602`, events `-V,-V`, chart
  `V^2`, first rank `36/132`, residual SHA
  `b302c4764091027f86d1129a66df5fbc5a39ee92c6e6e76dd880234bb5bb378a`,
  inner `(1)`, and complete `V^3`.  It does **not** match ancestry:
  `source_row_count` is `1` rather than `14`, and
  `source_certificate_sha256` differs.  `verify.py` does not check
  that field.  The control therefore shows that the unit first-J
  obstruction, its key, and the `V^3` chart survive deletion of the
  direct `2 beta t` slot; it does not show that the 14-row q2-beta
  syzygy survives.  That is the correct scope of an omission control
  and is not a broader theorem.

**Operator-failure vs theorem.**  v70c origin at `2026-08-25T16:35Z`
used a shorter wrapper whose emit looked up
`captured["transport_source_denominator"]` on every stage.  Transport
never goes through `parameterize`, so that key is absent.  Stderr:

```text
KeyError: 'transport_source_denominator'
```

with `p.main()` at line 146.  The repaired wrapper has `p.main()` at
line 176 and uses `transport_chart ** 0` on the transport stage.  The
48 mathematical lines printed before the KeyError are an exact prefix
of the repaired origin stdout, including rank `3468/3602`, row 6460,
key `('g','X',-19,20)`, degree 0, 21-row combination, and unit gcd.
Those lines are V69 emit, not a V70 complete certificate.  Only the
later rc-zero runs print wrong-row and complete denominator one, and
only those are theorem evidence.  A packaging nit: operator-failure
`source-v70.stdout` is the same 4/4 OK stream as the repaired
`V70_SOURCE.sha256` check, so it authenticates the v70d wrapper, not
the executed v70c file.  The traceback, not that source-check, is the
v70c witness.

**Defects.**  None that touch the repaired theorem.  Custody nits are
collected below.

**Survival.**  Freeze/manifest/archive/source hashes, dual-host rc-zero
identity of both theorem streams, 36/36 declared V69 members plus the
V70 wrapper pin, and “the portable bundle contains the V69 ancestry
that ran” all survive independent recomputation.  Omission is a
residual/chart control, not a second 14-row certificate.

---

## Charge 6 — Cover logic

**Result: the three raw pieces are an exact constructible cover of
`V(U)` in this fixed source-typed A3 q2-beta section.  V70 therefore
restores a whole raw-`U=0` theorem here, and nothing stronger.**

Write `A^3` with coordinates `(C,V,U)`.  The set-theoretic identity

```text
V(U) = [V(U) ∩ D(C)] ∪ [V(C,U) ∩ D(V)] ∪ V(C,V,U)
```

holds, and the three pieces are disjoint:

- `U=0` and `C ≠ 0` is the erratum-corrected, hostile-reviewed V33
  theorem (`CONFIRMED_WITH_REPAIRS`): first-J emptiness on `U=0 ∩ D(C)`
  for every beta, transport chart `C^2`, complete parent chart `C^3`.
- `C=U=0` and `V ≠ 0` is V70 `u-h-zero`: first-J emptiness on
  `C=U=0 ∩ D(V)`, complete chart `V^3`.
- `C=V=U=0` is V70 origin: transport emptiness, complete chart one.

Every point of the plane `U=0` is in exactly one piece.  Each piece is
a source rebuild, not a specialization of another piece’s echelon.
Each incompatibility is beta-degree 0 with monic gcd 1, so there is no
beta-root leftover on any piece.  The union is therefore emptiness of
the raw divisor `U=0` in this fixed normalized A3 q2-beta section.

It is not a single fraction-field identity over `E(C,V)`.  It is not
a repair of the separately quarantined staged-N13 denominators: both
V70 leaves return before previous/current/N13, and the erratum’s
quarantine of N13 exceptional-curve and rational-line parameter-zero
endpoints is untouched.  It is not whole `H=0` (`C=3U^2` still has
the open `U ≠ 0`), not whole `B3=0`, not fixed-A3, not another TD6
modulus, not TD6, not SP-2, not landing, and not JC2.  Stdout of every
repaired run prints

```text
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

Those denials are correct.  V64 on `H=0,D(U*V*P3*QH)`, V62D on
`V=H=0,D(U)`, and the older beta-zero trivariate atlas remain outside
this charge, as the erratum already stated.

**Defects.**  None in the cover, once V33 is taken in its repaired
scope `U=0,D(C)` rather than the withdrawn whole-divisor sentence.

**Survival.**  Whole raw `U=0` in this fixed q2-beta section, as the
three-piece union above, and nothing stronger.

---

## Attempted flips that did not kill the supported theorem

- **Hidden denominator factors.**  `u-h-zero` events are exactly `-V,-V`
  with denominator 1; parent chart multiplies those numerators to
  `V^2`; first-source LCM is `V`; inner residual/Bezout/combination LCM
  is 1; flint `factor()` of the complete chart is `(1, [(V, 3)])`.
  Origin has zero events and inner 1.  A dropped C-factor cannot occur
  on `C ≡ 0`: it would have been a zero divisor and a crash.  Same for
  `U`.
- **V33 echelon specialized through `C=0`.**  V70 rebuilds transport
  after setting `CENTER`.  Event keys stay at rows 4804/5380 but the
  pivot columns move `193/1289 → 194/1290` and the numerator `C → V`.
  That is a different matrix, not a substitution into V33’s chart.
- **Source-row versus echelon ancestry.**  Combinations are stored on
  original indices from `{row_index: 1}` through recorded original
  combinations of earlier pivots.  V70 replays against those original
  rows.  Origin row 6460 is the original `ordered` index; classical
  origin lists the same 21 original keys.
- **Wrapper monkeypatch mix-up.**  Transport and affine paths bind
  different replay helpers and different source-denominator rules.
  The mix-up is exactly v70c, which is preserved as rc-one evidence
  and is not the theorem source.
- **Wrong sign / RHS convention.**  Affine `pack` uses `-constant`;
  affine replay uses that stored RHS.  Transport residual is
  `source_vector_beta`, replayed the same way.  Positive asserts
  would have failed on a sign error.
- **Beta specialization.**  Pivot leads are forced degree 0; residuals
  are degree 0; gcd degree 0.  No beta-root leaf.
- **Q-prime omission as a broader theorem.**  Omit reproduces both
  unit obstructions and both complete charts.  On `u-h-zero` it
  replaces the 14-row syzygy by a 1-row one.  That is a control, not
  a second main certificate, and it is not used to drop `q'`.
- **Nonportable digests.**  V69 replaced the address-bearing V33
  `repr(E3)` serializer.  Dual-host stdout is byte-identical,
  including residual/gcd/combination SHAs.
- **Failed-run contamination.**  Operator-failure origin is an exact
  mathematical prefix of the repaired stream, then KeyError, rc 1,
  stored under `evidence/operator-failure/`.  Theorem evidence is the
  later v70d rc-zero pair.
- **Incomplete union.**  The three pieces partition `V(U)`.  Each is
  empty of solutions in this section.
- **Whole-H / B3 / A3 / TD6 / SP-2 / JC2 / staged N13.**  Denied by
  producer flags, by the erratum quarantine, and by the fact that V70
  never varies those moduli or reaches N13.

## Attempted flip that would have killed a stronger claim, and did not
apply

- **Hidden V denominator on `u-h-zero` treated as whole `C=U=0`.**
  Real if anyone said the complete chart was 1 or that `V=0` was
  included.  V70 does not say that.  It prints `V^3` and
  `whole_raw_stratum_empty=false`, and it ran origin as a separate
  leaf.

---

## Leftover nits (not load-bearing)

- Preregistration command still names V69 `replay.py` rather than
  `replay_v70.py`.  Actual stderr is the wrapper.
- Host IPs are README/xmodel-only.
- `PYTHONHASHSEED=0` is required by the prereg and README but is not
  visible in `time -v` command strings.  Canonical dual-host identity
  does not depend on proving that env bit.
- Run tags `T1636Z` versus evidence `start_utc=2026-08-25T16:40:14Z`.
- Operator-failure `source-v70.stdout` authenticates the repaired
  wrapper, not the executed v70c file.  The traceback does.
- `first_c1_c3_mpoly.py` is imported without a live hash pin.
- V31 is archived and checked but not executed.
- Printed ring still names `C,V,U` after specialization.
- Trivariate module docstring is B3-chart leftover.
- V69 `*_compatibility_original_row_replay=true` is still a banner;
  V70’s corresponding lines are asserted.
- `verify.py` does not recompute MANIFEST/FREEZE and does not notice
  the omit 14-row versus 1-row ancestry split.
- Omission controls are single-host.
- `raw_fraction_field_not_complete_stratum=true` remains an
  unconditional V69 banner.

---

## Survival statement

The frozen V70 producer, if it ran as written on the repaired wrapper,
is a source-typed pair of raw certificates in the fixed normalized A3
q2-beta section:

- `C=U=0` over `Q(V)`: transport rank `3470/3602`, events `-V,-V`,
  chart `V^2`, first-source `V`, first rank `36/132`, unique original
  dependent `('X-2',14)`, 14-row original combination, beta-degree 0,
  monic gcd 1, complete parent-style denominator `V^3`.  Exact
  obstruction on `C=U=0 ∩ D(V)`.
- `C=V=U=0`: transport rank `3468/3602`, no nonconstant events,
  original row 6460 / `('g','X',-19,20)`, 21-row original ancestry,
  beta-degree 0, monic gcd 1, complete denominator one, wrong-row
  control passed.  Exact obstruction at the origin, already in
  transport.

Together with the erratum-corrected V33 theorem on `U=0 ∩ D(C)`, these
are the three pieces of

```text
V(U) = [V(U) ∩ D(C)] ∪ [V(C,U) ∩ D(V)] ∪ V(C,V,U).
```

That restores emptiness of the raw divisor `U=0` in this fixed
q2-beta section.  It does **not** survive as: a single chart with
denominator 1; a specialization of V33 through `C=0`; a staged-N13
repair; a `U ≠ 0` result; whole `H=0`; whole `B3=0`; whole A3; other
TD6 moduli; TD6; SP-2; landing; or JC2.

No theorem-scope repair is required.  The nits above are custody and
expository only.

CONFIRMED
