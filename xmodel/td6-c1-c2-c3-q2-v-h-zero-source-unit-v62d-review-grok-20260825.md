# Hostile bounded review: TD6 V62D `V=H=0,D(U)` source unit

Referee: independent algebraic/source/custody pass of the frozen V62D
rational-edge unit claim only.  Operations used: full read of the charged
surfaces, `tar` extract of the frozen archive into
`/tmp/jc2-td6-v62d-review-grok-20260825/`, independent SHA256 via Python
`hashlib`, `ast.literal_eval` of the canonical unit certificate, and short
exact structural checks of multipliers, Bezout weights, and Rat3
denominators.  No producer execution, no `verify.py` run, no CAS, solver,
Lean, or other substantive computation.  Stored PASS strings are not
authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-v-h-zero-source-unit-v62d-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_v_h_zero_source_unit_v62d_aws_20260825/`.
Scope/composition boundary only (not V62D evidence):
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-aws-20260825.md`.

Producer actually executed by `run_v62d.sh v-h-zero`:
`jc2/cases/td6_c1_c2_c3_q2_v_h_zero_combined_empty_v62d_20260825/replay.py`
with `--stratum=v-h-zero`.  Expanded tree basename
`td6-aws-handoff-20260825-v62d` matches the tarball name.  `V62.main()` is
not called.

Import/hash pin chain executed by that producer, in order:

1. V62D `replay.py` pins and imports
   `td6_c1_c2_c3_q2_full_source_glue_rational_edge_dag_v62_20260825/replay.py`
   (`PARENT_SHA256=1c888f05…`, independently recomputed) and asserts
   `--stratum=v-h-zero`.
2. That parent pins and imports
   `td6_c1_c2_c3_q2_full_p12_n13_unit_raw_rational_canonical_20260825/replay.py`
   (`7e137083…`) and scans pinned `V45_V_H_ZERO.stdout` (`61bb5fed…`).
   The V45 P12/N13 markers are an import-time gate.  They are not consumed
   by V62D's unit construction.
3. Raw-rational-canonical pins and imports
   `td6_c1_c2_c3_q2_n13_v34_20260825/replay.py` (`1743dc29…`).
4. V34 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py` (`cf3f3f02…`).
5. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`1fb51264…`), then calls `tri.configure()`.  Dual defines
   `H = C - 3*U**2`.
6. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
7. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256` as `ce400cca…`); transport
   then loads `c1_pencil.py`, which pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

`run_v62d.sh` is the only entry that can produce this case: it execs the
V62D producer with `--stratum=v-h-zero` and rejects every other mode.

---

## Charge 1 — Source typing and ring

**Result: holds in source.**  Fixed center `(c1,c2,c3)=(C,V,U)`,
`H=C-3U^2`, raw chart `V=H=0` over `Q(U)`, arbitrary `beta`, direct
`q_beta` / `q_beta'`.  No illicit specialization or extra normalization
is imposed as a center equation.

- `run_v62d.sh` accepts only `v-h-zero`.  V62D then asserts
  `sys.argv[1:]` filtered to `--stratum=` is exactly
  `["--stratum=v-h-zero"]` before import.
- Trivariate `center_coordinates()` on `STRATUM=="v-h-zero"` returns
  `Rat3(3*U**2), Rat3(0), Rat3(U), "V=H=0 over Q(U)"`.  It does not
  take the `u-zero`, `h-zero`, `v-zero`, `origin`, `b3-param`,
  `v-cplus1-zero`, or `v-cplus5-zero` branches.  `STRATUM` is read from
  the same argv at trivariate, V34, V62, and V62D load.  Dual defines
  `H = C - 3*U**2`.
- V62 `build_transport_and_rows()` (the only V62 entry V62D calls)
  asserts `not center_v and not (center_c - 3*center_u**2)` and copies
  those three coordinates into `r.fb.CENTER`.  Frozen stdout is
  `source_center=V=H=0 over Q(U)`.
- `B3` remains the generic polynomial
  `4*C**2*U**2 - 4*C*V**2*U + 24*C*U**4 + V**4 - 20*V**2*U**3 + 20*U**6`.
  It is not set to zero.  On this chart it specializes to `128 U^6`,
  which is a unit on `D(U)` and is not inverted as a named extra center.
- After transport, V62D calls `n.configure_qd(direct_qprime=True)`.
  That sets `qd.Q_PRIME = {0: 1, 24: 25, 1: BetaPoly([0, 2])}`, i.e.
  `q_beta' = 1 + 2*beta*t + 25*t^24` with the `beta t` term present.
  Dual's documented `q_beta = t + beta t^2 + t^25` is the same family.
  `--omit-direct-qprime` is not on the argv.  `solve_stage` raises
  `AssertionError("beta-dependent pivot: exceptional strata required")`
  if any accepted lead has `lead.degree != 0`.  Both first and previous
  stages printed `*_all_pivots_beta_independent=true` on both hosts.
- `BetaPoly.inverse` exists only for degree 0.  The only extra
  normalization in V62D is making the compatibility gcd monic in
  `E(Q(U))[beta]` and multiplying by `-1`.  That is a unit of the
  function field, not a center change.

**Defects.**  None in the typing.  Stdout prints
`raw_center_stratum=V=H=0_over_Q(U)` at the top of V62D and then
`raw_center_stratum=v-h-zero` from `build_transport_and_rows`.  Two
labels, same chart.  `transport_matrix_beta_independent=true` is a
banner printed after `assert not compatibility and
len(transport_pivots) == 3470`; the empty compatibility list is the
assert, the banner is not a second test.

**Smallest repair.**  None required for typing.  Optional: print one
stratum key, and print `H_polynomial=C-3*U^2` / `H_after_chart=0`
next to `source_center`.

**Survival.**  The producer is source-typed as the raw chart `V=0`,
`C=3U^2` over `Q(U)`, with polynomial `beta` and direct `q_beta'`.

---

## Charge 2 — Exact ranks and dependencies

**Result: holds as producer-asserted, dual-host-duplicated, and
certificate-backed facts.  Ranks were not recomputed here.**

`solve_stage` prints `rank=len(pivots)/nvariables` and
`dependent_count` from the GE it just ran, then V62D asserts:

- first: `len(first_pivots) == 38 and len(free94) == 94` and
  `not first_dependent`;
- previous: `len(previous_pivots) == 37`,
  `len(previous_dependent) == 2`, `len(bad) == 2`, and
  `[record[1] for record in bad] == [("X-1", 11), ("X-1", 13)]`,
  with `bad = [record for record in previous_dependent if record[2]]`.

So there are exactly two previous dependents, and both have nonzero
residual.  Frozen stdout on both hosts:

```text
first_v62d_rank=38/132
first_v62d_dependent_count=0
previous_pole_v62d_rank=37/94
previous_pole_v62d_dependent_count=2
previous_pole_nonzero_dependency_keys=[('X-1', 11), ('X-1', 13)]
previous_pole_actual_rank_accepted=37
```

The serialized certificate stores `bad_keys == (('X-1', 11), ('X-1', 13))`.
Residual 0 is a nonzero `beta`-degree 0 element of `E(Q(U))` whose
Rat3 coordinates are multiples of `U`.  Residual 1 is a nonzero
`beta`-degree 2 element, also with polynomial denominators `1`.

Previous GE is `n.solve_stage`, **not** V62
`parameterize_with_pivots`.  The latter asserts every dependent rhs is
zero and would refuse this stage.  V62's own `main()` still asserts
previous rank 38; that path is not executed.  V62D's `37` is an
explicit acceptance of the observed rank, not a silent reuse of V62's
38-pivot parameterization.

**Defects.**  None that flip the rank claim.  The two keys are real
nonzero dependents.  What they contribute to the *unit* is Charge 3,
not Charge 2.

**Survival.**  First `38/132` with no dependents; previous/pole `37/94`
with exactly the two nonzero keys `('X-1',11)` and `('X-1',13)`.

---

## Charge 3 — Bezout/sign, raw previous, original-row unit, certificate

**Result: the reduced target is `1`; the combination is returned to
raw previous polynomials; one original-first-pivot division has
remainder `1`; the serialized certificate is a source-key multiplier
identity targeting `1`, not an echelon-row dump.  The second Bezout
weight is the zero polynomial.  That is a proof-representation fact,
not a hole in emptiness.**

### Sign and monic gcd

`polynomial_ideal_gcd` returns a monic generator and Bezout weights
with `sum weight*residual == gcd`.  V62D then asserts
`gcd.degree == 0 and gcd`.  The certificate stores gcd as the E3 unit
`(1,0,…,0)` (18 coordinates, first `('1','1')`, rest `('0','1')`).
So after monicization gcd is the constant `1`, and
`normalizer = -gcd.inverse()` is `-1`.

Packed previous polynomials reconstruct as
`source_polynomial(row, rhs)` with constant term `-rhs`.  A dependent
combination therefore replays as `{(): -residual}`.  The minus in the
normalizer is required: without it the packed combination would be
`-1`.  With it, `reduced_replay == {(): 1}` is the asserted identity.
That assert is in source; this session did not rerun it.

### The second Bezout weight is zero

Parsed certificate:

| object | content |
|---|---|
| `bad_keys` | `('X-1',11)`, `('X-1',13)` |
| residual 0 | `beta`-degree 0, 6 nonzero E3 coords, dens `1`, numerators `*U` |
| residual 1 | `beta`-degree 2, nonzero, dens `1` |
| bezout 0 | `beta`-degree 0, dens `{1, U}` |
| bezout 1 | empty `BetaPoly` |
| `normalized_reduced_weights` | 12 packed indices `0..11` |
| selected raw previous keys | `('X-1',0)` through `('X-1',11)` |

Residual 0 is a function-field unit on `D(U)` (content `U`).  Euclidean
xgcd of a unit against residual 1 therefore returns weights
`(inverse, 0)` after monicization.  The code still *runs* two-argument
Bezout; the second weight is honestly serialized as zero.  The unit is
the inverse of residual `('X-1',11)`.  Key `('X-1',13)` is a genuine
extra dependent row and is **not** in the original-row support of the
certificate.

That does not empty the previous stage any less: one function-field
unit residual is already an obstruction on `D(U)`.  The claim text
“their exact Bezout combination” overstates the arithmetic.  The
emptiness statement does not depend on residual 13.

### Raw previous, one division, original first rows

After the packed check, V62D builds `raw_previous_rows` with
`source_records` (arbitrary-degree original polynomials, zeros kept),
maps packed keys to raw keys, and forms `raw_combined` as the same
scalar weights on those raw polynomials.  Then:

```text
remainder132, quotients = g.divide_polynomial(raw_combined, first_pivots)
assert remainder132 == unit_polynomial
```

`divide_polynomial` reduces a possibly nonlinear polynomial by
normalized affine first pivots and asserts
`remainder + sum quotient*pivot == original` before returning.
`lift_relations` pushes quotients through the GE combinations of
those pivots, i.e. onto **original packed first-band row indices**,
not onto echelon pivot columns.  First multipliers are the sign flip
of that lift.  Full replay against `(first_rows, raw_previous_rows)`
is asserted equal to `{(): 1}`.

First-band rows are affine: `first_band_polynomials` uses
`nr.affine_polynomial`, and `qd.pack` asserts every nonconstant
monomial has length 1.  Pack here is a format change, not the V48
linearization of genuine quadratics.  Previous rows used in the
certificate are `source_records`, not packed 94-variable rows.
Stdout `source_selected_previous_max_degree=2` is consistent with
keeping a quadratic original previous row.  Certificate previous
multipliers are scalars (the combined weights).  Certificate first
multipliers are linear in the 132 jet variables, 13 nonzero, with
`beta`-degrees `0..12`.  That is the shape of quotients of a higher-
degree raw polynomial by affine first pivots.

`individual_previous_edge_lifts_used=false` is accurate: V62D does
not call `lift_previous_key`.  The one-division construction is the
identity.

### Serialized certificate versus echelon

Schema `TD6-A3-Q2-V-H-ZERO-COMBINED-EMPTY-SOURCE-v1`.  Fields include
`bad_keys`, residuals, Bezout, gcd, normalized packed weights,
`first_keys`, `first_multipliers`, `raw_previous_keys`,
`raw_previous_multipliers`, and `target`.  Parsed:

- `first_keys` = `('X-2', 0)` through `('X-2', 37)` (38 original
  first-band keys, matching 38 first-stage pivots);
- `raw_previous_keys` = `('X-1', 0)` through `('X-1', 39)` plus
  `('P1', 0)` through `('P1', 13)` (54 source records);
- 13 nonzero first multipliers on `('X-2', 0)`–`('X-2', 12)`;
- 12 nonzero previous multipliers on `('X-1', 0)`–`('X-1', 11)`;
- `target == {(): E3-unit 1}`.

The certificate does not store the original row polynomials.  It is a
multiplier certificate against named source keys, replayable only by
rebuilding those rows from the same producer.  That is a
representation choice, not an echelon substitution.  Pivot *digests*
in the certificate (`be44a0b7…`, `cee166ca…`) are canonical hashes of
factor tuples; they are not the identity.

Stdout `first_v62d_pivot_digest=675d11c7…` /
`previous_pole_v62d_pivot_digest=b8b7292c…` come from V34
`digest = sha256(repr(value))` inside `solve_stage`, which was **not**
replaced when raw-rational-canonical set `n.digest = canonical_digest`.
The two published pivot-digest families are therefore different hashes
of related objects.  Custody nit, not an ancestry gap.

**Defects.**  Prose that treats both residuals as load-bearing Bezout
inputs is false as arithmetic.  The identity that is actually
serialized is residual-11 inverse plus one raw first-pivot division.
That is still a source identity targeting `1`.

**Smallest repair.**  Print `bezout_second_weight_is_zero=true` and
state that residual `('X-1',13)` is a genuine extra dependent not used
in the unit.  Optional: store min selected previous degree, not only
max.

**Survival.**  Original-row unit on first+raw-previous holds in the
asserted construction; certificate target is `1` on source keys.

---

## Charge 4 — No current / N13 / P12; omission controls

**Result: the V62D theorem construction uses none of current, N13, or
P12.  Both omission controls are meaningful.  The V62 parent still
pins a V45 P12/N13 stdout at import; that is a source-graph impurity,
not a smuggled row in the unit.**

V62D `main()` never calls `qd.compile_current`, never reads current
row 13, never constructs P12, and never calls `lift_current_key`.
Banners `current_stage_used=false`, `P12_used=false`, `N13_used=false`
match the executed body.  V62 `main()` — the file that *does* use
those objects — is not invoked.

The V62 *module* still asserts V45 markers
`P12_N13_polynomial_unit_identity_exact=true` and
`combined_unit_residual_is_minus_k_over_50=true` at import.  V62D
cannot start without that pinned V45 file.  That is packaging, not
`P12` or `N13` appearing in the first+previous identity.

Omission controls, in source:

```text
assert nonzero_first and nonzero_previous
omitted_first[nonzero_first[0]] = {}
assert source_replay(...) != unit_polynomial
omitted_previous[nonzero_previous[0]] = {}
assert source_replay(...) != unit_polynomial
```

Certificate support of those first nonzero slots is
`('X-2', 0)` (103-term linear first multiplier, `beta`-degree 12) and
`('X-1', 0)` (nonzero scalar previous multiplier).  If either omitted
row were the zero polynomial, the replay would be unchanged and the
assert would fail.  Dual-host `rc=0` therefore proves both omitted
edges were used.  The controls do **not** claim every one of the 13+12
edges is independently essential, and they do not omit key 13 (zero
multiplier; omitting it would not break the identity).

**Defects.**  None load-bearing.  The V45 pin should not be required
to state a previous-stage unit.

**Survival.**  No current/N13/P12 row is in the theorem.  The two
omission controls are non-vacuous for the edges they actually drop.

---

## Charge 5 — Denominator completeness; radical `{U}`

**Result: every charged source multiplier/coefficient and every
normalized first/previous pivot/lead that the producer ledgers has
Rat3 polynomial denominator in `{1} ∪ {U^k}`.  The same is true of
every Rat3 denominator in the serialized certificate.  Constant-field
`Q^*` coefficients exist and are units.  No omitted nonunit was
found.  The identity is a function-field statement on `D(U)`, not a
polynomial-ring statement on the whole line `V=H=0`.**

Source-ledger inputs: `normalizer`, `reduced_bezout`,
`reduced_weights`, first multipliers, selected first rows, previous
multipliers, selected raw previous rows.

Pivot-ledger inputs: every coefficient of each normalized first and
previous pivot (row, rhs, and GE combination), pre-normalization
leads, previous residuals, and Bezout weights.

`leaf_denominator_ledger` walks `tri.e3_rat3_coordinates` and records
`coordinate.denominator`.  `factor_strings` returns `[]` for degree-0
polynomials, so constant denominators do not appear in
`*_factor_set`; they would still appear as TSV keys.  Frozen TSVs:

Source (`02d29ba2…`):

```text
1        488820  normalizer
U        1078    reduced_bezout
U^2      674     reduced_weights
U^3      408     reduced_weights
U^4      228     reduced_weights
U^5      126     reduced_weights
U^6      54      reduced_weights
U^7      12      first_multipliers
```

Pivot (`bacdf7a6…`):

```text
1        68662   first_normalized_pivots
U        108     first_normalized_pivots
U^2      163     first_normalized_pivots
U^3      133     first_normalized_pivots
U^4      78      first_normalized_pivots
U^5      39      previous_normalized_pivots
U^6      9       previous_normalized_pivots
```

Union of leaf factor sets is `['U']`.  Walk of every `(numerator,
denominator)` string pair in the canonical certificate, ignoring four
schema/hash strings, yields only `1, U, U^2, …, U^7`.  Bezout 0
introduces `U`; first multipliers introduce `U^7`.  Residual 0 has
polynomial denominator `1` and numerator content `U`; its inverse is
exactly the `U` in Bezout 0.

Integer/Q coefficients such as `25` and
`10317125787295556` sit in Rat3 *numerators*.  Over `Q` they are
units of `Q[U]_{(U)}`.  They are not missing nonunits.

`divide_polynomial` performs no inversion (pivots are already
normalized to lead 1).  `gcd.leading.inverse()` is already multiplied
into the Bezout weights.  Pivot lead inverses are in the normalized
pivot ledger.  Serialization uses the same E3 coordinate split as the
ledgers.

Function-field versus localization: residual 0 is a multiple of `U`,
hence a unit in `E(Q(U))` and a nonunit in `E[U]`.  V62D claims
emptiness only on `D(U)` and prints
`whole_V_H_zero_edge_empty=false` and
`raw_denominator_factor_strata_still_charged=true`.  That gap is
scoped, not hidden.

`verify.py` only checks that `U` / `U^7` (source) and `U` / `U^6`
(pivot) appear as TSV rows and that substrings `V`, `P3`, `QH` do
not.  It is not an algebraic completeness proof.  The TSV bodies and
the certificate walk are.

**Defects.**  None load-bearing.  `verify.py` is a weak substring
gate.

**Survival.**  Radical support of the stated localization is `{U}`.

---

## Charge 6 — Independent custody

**Result: listed hashes recompute; `SOURCE.sha256` is 111/111 closed
against Box02 `source-check.txt`; `rc=0` twice; the three proof
artifacts agree byte-for-byte; stdout differs only in the three
absolute artifact paths.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v62d.tar.gz` | `6d568ff6e77dc764c2ddae6b5be1c6b8baa75e47e364ac15f83d6e4aaaa52e42` | MANIFEST, README, xmodel, `verify.py` EXPECTED, both host archive stamps |
| `aws_box02/v62d.stdout` | `50a143c637b0344b2ea8dc7d4f67ae85c4afe497b6d3fecb59a1d94665980a76` | same set |
| `aws_r6d/v62d.stdout` | `db4e566e4dfb51d6bffe66fc271fb3e19d9b7b4c5c5b1d7657d1789a305dd1bf` | same set |
| unit certificate (both hosts) | `6d672e839c84b518909ea70161761f929d249fa4251fa5852bde9f896c1572a1` | MANIFEST, README, xmodel, stdout, EXPECTED; **byte-identical**, 3322974 bytes |
| source denominator ledger (both) | `02d29ba2f0112a5f2d83b1973d86e4350ae04203df1496a9f598c599c8d8426a` | same |
| pivot denominator ledger (both) | `bacdf7a6869cb50f118c4a77fa646815963f9782be5bf0f387dc676361f8b034` | same |
| extracted `SOURCE.sha256` | `bed1c3b9b705189702cdc9177340955ddafb813ecd8449032960da5da959e91e` | README |
| extracted V62D `replay.py` | `d4fbc690fce9baa3095aab0e6af9747a7a95cf3bad7905a7fe92e56be284448d` | `SOURCE.sha256`, `V62D_SOURCE.sha256` |
| extracted V62 parent `replay.py` | `1c888f0589fccbce12ae6870767928285ff83bbfbf8e1f7b19889a01ac1a9218` | live `PARENT_SHA256`; stdout `parent_v62_sha256`; `V62D_SOURCE.sha256` |
| extracted `run_v62d.sh` | `ac8475787ee090b0b42ecd552437b85664a32342998fc294de9b6be1779adb1b` | `V62D_SOURCE.sha256` |
| README | `103f49fd483d64ff916c7e5398d3b75c612e54f14ac1f24f2e2c32cc2dfcaf8d` | MANIFEST, FREEZE |
| `verify.py` | `60f751cda391e0fe0081ac4a9d2cbe99f58dd147cefde609b6bf944dcc0aa57f` | MANIFEST, FREEZE |
| `MANIFEST.sha256` | `a35040ee57baabe6e33260ea012ffb3e5c90513d0022b4cd746fd6f87c018120` | FREEZE |
| xmodel V62D report | `52736b96b9b7fab88ae277e00039cb67ffbce7b2c1e976c31b3f7d897adc6322` | FREEZE |
| Box02 `rc` / r6d `rc` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body `0\n` |

All 24 MANIFEST paths recompute.  All four FREEZE paths recompute.
All 111 `SOURCE.sha256` members recompute.  Box02 `source-check.txt`
is exactly those 111 names, each `: OK`.  The extracted tree has 112
files: the 111 listed members plus `SOURCE.sha256` itself.

Stdout line lists have length 79.  After dropping the three prefixes
`source_certificate_path=`, `source_denominator_ledger_path=`,
`pivot_denominator_ledger_path=`, the lines are equal.  The three raw
diffs are the Box02 versus r6d absolute artifact directories named in
README.

Box02: start `2026-08-25T13:54:31Z`, end `2026-08-25T14:17:23Z`,
RSS `556892` KiB, `Exit status: 0`, command
`timeout 21600 ./run_v62d.sh v-h-zero`.  r6d: start
`2026-08-25T14:13:25Z`, end `2026-08-25T14:30:00Z`, RSS `555196` KiB,
same exit and command.  Preflight on Box02 is the V62D preflight
branch (`PREFLIGHT PASS`, empty stderr).  r6d has no preflight or
source-check artifacts; README claims 111/111 only for Box02.

**Hosts.**  README states Box02 `34.203.207.55` and r6d
`100.26.198.153`.  Those IPs do not appear in stdout or stderr.  The
artifacts prove two remote paths and two timed invocations of
`./run_v62d.sh v-h-zero`.  They do not prove the IPs.

**`verify.py` is not algebra.**  It hashes seven paths, checks `rc`,
filters three path prefixes, asserts banners, checks 111 `: OK`
lines, and looks for `U` / `U^7` / `U^6` TSV rows.  It never imports
`replay.py` and never divides a polynomial.

**Survival.**  Freeze/manifest/artifact hashes, dual `rc=0`, 111/111
declared source-check, byte-identical proof artifacts, and the
three-path stdout claim all survive independent recomputation.

---

## Charge 7 — Scope

**Result: the strongest statement the artifact can support is
emptiness of the fixed source-typed A3 q2-beta family on the rational
edge `V=H=0,D(U)`.  V62D does not cover `U=0`, whole H, whole A3,
TD6, SP-2, landing, or JC2.  The separate U-zero theorem is named
only as a later union leaf.**

Stdout and xmodel both print:

```text
function_field_rational_edge_empty=true
raw_denominator_factor_strata_still_charged=true
whole_V_H_zero_edge_empty=false
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

Charge 5 is why `whole_V_H_zero_edge_empty` is false: the unit
residual is a multiple of `U`.  The separately frozen U-zero report
(`xmodel/td6-c1-c2-c3-q2-beta-u-zero-aws-20260825.md`) is a different
producer, a different archive (`71845755…`), and a first-J
incompatibility on the whole divisor `U=0`.  V62D's producer text
does not import that case.  README/xmodel mention it only as a later
composition leaf.  A union of the two leaves would be a later theorem;
it is not this one.

V62D never claims whole H (the H-stratum is a different chart), never
varies the A3 section, and never mentions landing or JC2 except to
deny them.

**Defects.**  None.  Scope matches the localization.

**Survival.**  Emptiness on `V=H=0,D(U)` inside the fixed A3 q2-beta
family, and nothing stronger.

---

## Attempted flips that did not kill the theorem

- **Sign error.**  Packed combination produces `-residual`;
  `normalizer = -1` after monic gcd `1` is the correct flip to `+1`.
- **Beta-dependent pivot.**  `solve_stage` aborts on `lead.degree != 0`.
  Residual 0 is `beta`-degree 0, so the obstruction is not a
  `beta`-root stratum.
- **Function-field versus localization.**  Real: residual 0 has
  content `U`.  Already charged; whole-line emptiness is denied.
- **Raw/echelon ancestry.**  Final replay is original first-band
  (affine pack) plus `source_records` previous, not packed previous
  rows.  Certificate keys are `(X-2,*)` / `(X-1,*)` / `(P1,*)`.
- **Omitted nonunit denominator.**  Certificate walk and both ledgers
  have radical `{U}` only.  `Q^*` coefficients are units.
- **Incomplete source archive.**  Executed pin chain is in
  `SOURCE.sha256` and live-hashed.  111/111 closed.
- **Vacuous omission control.**  Dual `rc=0` plus `!= 1` asserts on
  used nonzero edges.
- **Scope overreach.**  Not present in the charged surfaces.

---

## Leftover nits (not load-bearing)

1. Second Bezout weight is zero; prose “their Bezout combination”
   overstates the arithmetic.  Residual `('X-1',13)` is unused in the
   unit.
2. V62 parent import pins V45 P12/N13 stdout.  Unused by V62D algebra.
3. `first_c1_c3_mpoly.py` is imported without a hash pin (file is in
   `SOURCE.sha256`).
4. Stdout pivot digests use V34 `repr` digest; certificate pivot
   digests use canonical digest.
5. Duplicate `raw_center_stratum` keys (`V=H=0_over_Q(U)` then
   `v-h-zero`).
6. `verify.py` is a custody/marker gate, not an algebraic replay.
7. Host IPs are README statements, not in-artifact.
8. r6d has no `source-check.txt` / preflight pair.
9. Several `*_original_row_replay=true` / `*_beta_independent=true`
   banners are printed by `solve_stage` / `build_transport_and_rows`
   after the asserts they summarize, not as a second test.
10. V62 `main()` still asserts previous rank 38; that path is not
    this theorem.
11. The certificate does not contain the original row polynomials.

---

## Commands and hashes used

Extract (read-only; producer not executed):

```bash
mkdir -p /tmp/jc2-td6-v62d-review-grok-20260825
tar -xzf cases/td6_c1_c2_c3_q2_v_h_zero_source_unit_v62d_aws_20260825/archives/td6-aws-handoff-20260825-v62d.tar.gz \
  -C /tmp/jc2-td6-v62d-review-grok-20260825
```

Independent SHA256: Python `hashlib.sha256(path.read_bytes()).hexdigest()`
over every MANIFEST path, FREEZE path, charged xmodel file, extracted
`SOURCE.sha256` member, V62D producer, V62 parent, and the executed
pin chain.  Certificate structure via `ast.literal_eval` of the
canonical repr.  No `verify.py` execution.

Principal hashes:

```text
6d568ff6e77dc764c2ddae6b5be1c6b8baa75e47e364ac15f83d6e4aaaa52e42  source archive
50a143c637b0344b2ea8dc7d4f67ae85c4afe497b6d3fecb59a1d94665980a76  Box02 stdout
db4e566e4dfb51d6bffe66fc271fb3e19d9b7b4c5c5b1d7657d1789a305dd1bf  r6d stdout
6d672e839c84b518909ea70161761f929d249fa4251fa5852bde9f896c1572a1  COMBINED_PREVIOUS_SOURCE_UNIT.txt
02d29ba2f0112a5f2d83b1973d86e4350ae04203df1496a9f598c599c8d8426a  COMBINED_SOURCE_UNIT_DENOMINATORS.tsv
bacdf7a6869cb50f118c4a77fa646815963f9782be5bf0f387dc676361f8b034  FIRST_PREVIOUS_PIVOT_DENOMINATORS.tsv
bed1c3b9b705189702cdc9177340955ddafb813ecd8449032960da5da959e91e  SOURCE.sha256
d4fbc690fce9baa3095aab0e6af9747a7a95cf3bad7905a7fe92e56be284448d  V62D replay.py
1c888f0589fccbce12ae6870767928285ff83bbfbf8e1f7b19889a01ac1a9218  V62 parent replay.py
7e1370834460e2bc3123631825f04cb04a0b457a14449985635f3d0af86f8dd1  raw-rational-canonical parent
1743dc294ca3e3f7f8c1cc1a471d340fc2a1ac7e39d29eddf7e025327578a5c6  n13 v34
cf3f3f028b99771a156a422d73a99eefdc9f04fbdc0698d8e8baf962efa4cf7f  beta dual
1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea  trivariate
61bb5fedba625711115ed7665a6ed23f37a54b0cff44356ecac0be717668ed4e  V45_V_H_ZERO.stdout
52736b96b9b7fab88ae277e00039cb67ffbce7b2c1e976c31b3f7d897adc6322  xmodel V62D report
a35040ee57baabe6e33260ea012ffb3e5c90513d0022b4cd746fd6f87c018120  MANIFEST.sha256
```

CONFIRMED
