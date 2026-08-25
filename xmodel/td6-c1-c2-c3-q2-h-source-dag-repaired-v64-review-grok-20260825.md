# Hostile source/custody review: TD6 H-stratum repaired source DAG V64

Referee: independent algebraic/source-fidelity pass of the frozen V64
H-stratum claim only.  Operations used: read, search, `tar` extract of the
frozen 264 KiB archive into
`/tmp/jc2-td6-v64-review-grok-20260825/`, and independent SHA256 via
Python `hashlib`.  No producer execution, no `verify.py` run, no CAS,
solver, Lean, or other substantive computation.  Stored PASS strings are
not authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_h_source_dag_repaired_v64_aws_20260825/`.
Predecessor (immutable): V60 report `bd923e4b…`, V60 hostile review
`c9989580…`, V60 ancestry erratum `3443fcc6…`.

Producer actually executed by `run_v64.sh`:
`jc2/cases/td6_c1_c2_c3_q2_h_source_dag_repaired_v64_20260825/replay.py`
with `--stratum=h-zero`.  Expanded tree basename
`td6-aws-handoff-20260825-v64` matches the tarball name.

Import/hash pin chain executed by that producer, in order:

1. V64 `replay.py` pins and imports
   `td6_c1_c2_c3_q2_full_p12_n13_unit_raw_canonical_20260825/replay.py`
   (`PARENT_SHA256=77194c4b…`, independently recomputed) and scans pinned
   `V44_H_ZERO.stdout` (`609349a5…`).
2. That parent pins and imports
   `td6_c1_c2_c3_q2_n13_v34_20260825/replay.py` (`1743dc29…`).
3. V34 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py` (`cf3f3f02…`).
4. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`1fb51264…`), then calls `tri.configure()`.  Dual defines
   `H = C - 3*U**2`.
5. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
6. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256` as `ce400cca…`);
   pencil then pins `td6_jet_orbit_adjoint_20260824/replay.py`
   (`fb138b0f…`), which pins the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

`run_v64.sh` is the only entry that can produce this case: it execs the
V64 producer with `--stratum=h-zero`.  The generic edge-DAG and V60
producers remain in the tarball and are out of the executed path.

---

## Charge 1 — Freeze, manifest, artifacts, rc, source-check, one-host

**Result: listed custody hashes recompute.  Declared `SOURCE.sha256`
closes against `source-check.txt`.  `rc` is `0`.  One-host is a README
statement plus a single remote run path, not an in-artifact IP proof.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v64.tar.gz` | `1a2e4f6766ffe5b15b963dd6ac86c02d538eb3e6d45b27d4a5a99e3c87a7aac6` | MANIFEST, README, xmodel, `verify.py` EXPECTED |
| `aws_r6d/v64.stdout` | `14775e9ad4adfb0a20512823be01bdd48da711e30b8ac7796e094841f41edd06` | same set |
| `aws_r6d/artifacts/N13_PROOF_DAG.txt` | `ef721416a7aac4f97167003801bfe94033e0b6627942d4ba9269c5565d9a962e` | same set; also printed in stdout |
| `aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv` | `259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385` | same set; **byte-identical to the V60 ledger** |
| `aws_r6d/v64.stderr` | `7660d509151d4ce1828123a00f592fd5c91919294b7c04ff973c3f99e7be9226` | MANIFEST, EXPECTED |
| `aws_r6d/source-check.txt` | `99f932613dcc6e55507212d903de2e87c64a83550a0f6750c85cf5d76a9d4a1a` | MANIFEST, EXPECTED |
| `aws_r6d/rc` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body is `0\n` |
| `aws_r6d/start_utc` | `dfdaefba92c64e72476a7a40b9440f5780c8c4355e70182490740f5220d48dbf` | MANIFEST; body `2026-08-25T13:33:12Z` |
| `aws_r6d/end_utc` | `1999f8e196205e78a95a016f408bb40cef8a0d04098d46750ba4819ef27d06a5` | MANIFEST; body `2026-08-25T14:00:56Z` |
| `README.md` | `97b25860da3d36bf82fe0573425300fc0d540271cb326e4e1b04c3e26888b459` | MANIFEST, FREEZE |
| `verify.py` | `c23b3b1e9874d0f8c1e9a95b1c58c2207b42a8ca67a51a551250a424548804c0` | MANIFEST, FREEZE |
| `MANIFEST.sha256` | `51722a5dd366b29411487d2c7f38684172cc24332d04cc4b94772ca9cdf13222` | FREEZE |
| xmodel V64 report | `096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39` | FREEZE |
| extracted `SOURCE.sha256` | `777551c9ecff94cc98e16e8d076bffee7171e37e9690914b66d440615f9b53c7` | README “source manifest” |
| extracted V64 `replay.py` | `9d3315f9270e513436e6549d8a1c1bce2378a903e80a39611286bde4f73e9dd0` | `SOURCE.sha256`, `V64_SOURCE.sha256` |
| extracted parent raw-canonical `replay.py` | `77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef` | live `PARENT_SHA256` assert; **not** in top-level `SOURCE.sha256` |
| V60 erratum | `3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069` | xmodel V64 report |
| V60 review | `c99895806fbf7cbae8baea451856a86949c0b4049185dc5d0227425938a5d89e` | erratum, `V64_RUNBOOK.md` |
| V60 report | `bd923e4bad92e14abac9502f211821e01b1ff2b4fa08ae7aeb41fc49238e093b` | erratum |

All 63 paths in extracted `SOURCE.sha256` recompute.  Frozen
`source-check.txt` is exactly those 63 names, each `: OK`.  Declared
source-check closure holds.

`aws_r6d/rc` is `0\n`.  stderr `Exit status: 0`; elapsed `27:43.09`;
RSS `674204` KiB.  README UTC interval, remote path
`/home/ubuntu/runs/td6_v64_h_repaired_r6d_20260825T1333Z`, RSS, and
exit code match the artifacts.  Stdout artifact paths use that same
directory.

**One-host.**  README states r6d `100.26.198.153`.  That IP does not
appear in stdout or stderr.  The artifacts prove a single remote path
and a single timed invocation of `./run_v64.sh`.  They do not prove
the IP.

**`verify.py` is not algebra.**  It hashes six paths, checks `rc`, then
`assert marker in out` / DAG / ledger for the repaired banners.  It
never imports `replay.py` and never divides a polynomial.  This review
does not treat its PASS string as a theorem.

**Source-check vs executed pin chain / archive inventory.**  The tarball
has 100 files; 36 are absent from `SOURCE.sha256`, including the
**executed parent** `full_p12_n13_unit_raw_canonical/replay.py`,
`V64_SOURCE.sha256` itself, unused V55–V61 producers, `run_v60.sh`, and
`jc2/cases/.../v57.../__pycache__/replay.cpython-314.pyc`.  The parent
is live-pinned in V64 `replay.py` before import, and this session
recomputed `77194c4b…`.  That is a stronger gate than a source-check
line.  It is still a declared-list hole: `SOURCE.sha256` is not an
inventory of the executed import chain or of the archive.  The parent
hash **is** recorded in unlisted `V58_SOURCE.sha256`.

**Survival.**  Freeze/manifest/artifact hashes and `rc=0` survive
independent recomputation.  Declared 63-file source-check survives.
Archive-wide inventory and in-artifact host-IP proof do not.

---

## Charge 2 — V60 load-bearing ancestry correction

**Result: genuinely implemented as live asserts, not as a renamed
cache dump.  Current row 13 traces through exactly previous key
`('X-1', 14)` plus original first rows.  `('X-1', 0)` is an independent
quadratic positive control / lift-cache entry, never an N13 previous
edge.**

V60’s false sentence was that N13 reduced through previous rows 0 and
14.  The V60 review’s required repair was: print
`N13_previous_edge_keys=[('X-1', 14)]` separately from
`quadratic_source_positive_control_key=('X-1', 0)`, demand the first
list in xmodel/README/`verify.py`, and move
`arbitrary_degree_original_rows_preserved=true` to after the quadratic
replay assert.  All three are in the V64 producer.

**What the source actually does.**

- `required_current = sorted(set(n13_weights))`.  Frozen stdout
  `N13_left_null_support=1`, `current_rows_source_lifted_indices=[13]`.
- `lift_current_key` records `selected_previous` as the keys of nonzero
  entries of `previous_relation94`.  For `key == ('X0', 13)` it
  **asserts** `selected_previous == [('X-1', 14)]`.
- After the N13 lifts,
  `n13_previous_edge_keys` is the sorted union of
  `current_previous_edge_keys` over N13 support only, then
  `assert n13_previous_edge_keys == [('X-1', 14)]`.
- `('X-1', 0)` is forced earlier, independently:

  ```text
  quadratic_previous[0] -> lift_previous_key
  quadratic_source_positive_control_key=('X-1', 0)
  quadratic_source_positive_control_exact=true
  ```

  That insert populates `previous_first_relations_by_key` before N13.
  The cache print
  `previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]` is
  therefore still a cache union, now immediately followed by
  `N13_previous_edge_keys=[('X-1', 14)]` and
  `quadratic_control_is_not_N13_edge=true`.

**Reconciliation of every DAG previous-edge line.**  The DAG still
emits, from `sorted(previous_first_relations_by_key)`:

```text
previous_edge_key=('X-1', 0)
previous_edge_nonzero_first_rows=14
previous_edge_key=('X-1', 14)
previous_edge_nonzero_first_rows=38
```

Those two blocks describe **every lifted previous original row**, i.e.
the quadratic control plus the N13 previous edge.  They are not N13
support.  Support is the later lines

```text
N13_previous_edge_keys=[('X-1', 14)]
quadratic_control_key=('X-1', 0)
quadratic_control_is_not_N13_edge=true
```

Row 13’s own first-only support is 38, matching previous-14’s first
support and not previous-0’s 14.  xmodel, README, and `V64_RUNBOOK.md`
state the one-edge N13 trace.  They do not repeat V60’s two-edge N13
prose.

**Packaging nits, not ancestry reversal.**

- DAG `quadratic_control_key=('X-1', 0)` is a string literal, not
  `f"quadratic_control_key={quadratic_key}"`.  Frozen stdout’s live
  print of `quadratic_source_positive_control_key` is `('X-1', 0)`, so
  this run is consistent.  A future first-quadratic-row change could
  desync the DAG line without failing the N13 assert.
- `quadratic_control_is_not_N13_edge=true` is a constant print after
  `assert n13_previous_edge_keys == [('X-1', 14)]`, not
  `quadratic_key not in n13_previous_edge_keys`.  For this frozen run
  the assert already excludes key 0 from N13 support.
- The early banner
  `arbitrary_degree_original_rows_preserved=pending_live_control` is
  replaced after the quadratic replay by `=true`.  `verify.py` looks
  for the later string.

**Survival.**  The V60 load-bearing correction survives in source.
`('X-1', 0)` is not an N13 previous edge.

---

## Charge 3 — Source replay logic (not digests)

**Result: arbitrary-degree original rows are the replayed objects.
Every selected current and previous edge is replayed against original
rows.  The staged left-null relation is an exact 56-variable identity.
Transitivity in the free equation module is the licensed representation
of the unexpanded DAG.**

- `source_records` keeps `g.clean(polynomial)` at every degree,
  including zeros.  Raw previous/current come from
  `qd.compile_previous` / `qd.compile_current` on the 132-variable
  bands, **not** from `qd.pack`.
- Echelon stages still go through `qd.pack` in
  `td6_jet_orbit_adjoint_20260824/replay.py`, which asserts
  `len(monomial) == 1` (the V48 linear-packer failure class).  That
  packer is not applied to the replayed original previous/current
  polynomials.  First-band rows are linear, so packing them does not
  drop quadratic source terms.
- Parent `divide_polynomial` reduces by normalized affine pivots and
  **replays** `remainder + sum quotient * pivot == original` before
  returning.  That is an exact edge identity, not a digest.
- `lift_current_key` divides the **raw** 132-variable current
  polynomial by first pivots, remaps, then divides by previous pivots.
  It asserts remainder equality against the packed reduced row and
  replays:
  - `first_only_relation` against first rows, equaling
    `raw_current - embed(remainder94)`;
  - `previous_relation94` against packed previous rows, equaling
    `remainder94 - embed(remainder56)`.
- `lift_previous_key` divides the **raw** 132-variable previous
  polynomial by first pivots and asserts
  `source_replay(relation, first_rows) == raw_previous - embed(remainder94)`
  with `remainder94` equal to the packed previous polynomial.
- Only nonzero previous multipliers call `lift_previous_key`.  With
  the row-13 assert above, the N13 previous original-row edge is
  exactly key 14.
- Staged left-null: `staged_n13_left == {(): -n13}` on the reduced
  56-variable current row.  DAG
  `staged_left_sha256` equals `staged_target_sha256` and
  `remainder56_sha256`.
- Nested previous-first multiplier products are intentionally not
  expanded.  The certificate is
  `proof_rule=exact_edge_substitution_in_free_equation_module`.
  That is a proof-representation choice, not a digest, and it does
  not make `('X-1', 0)` an N13 edge.

DAG digest lines (`previous_edge_relation_sha256=…` and kin) hash
objects already checked.  They add no second algebraic test.

**Survival.**  The unexpanded DAG is licensed as exact edge
substitution in the free equation module.  It is not a fully expanded
132-variable normal form of `current_13`.

---

## Charge 4 — Repaired controls as live assertions

**Result: all five charged controls are live mathematical asserts,
not print wrappers.**

1. **Omission of previous row 14.**  For current `('X0', 13)`, the
   unique nonzero `previous_relation94` slot is zeroed and
   `source_replay(omitted_relation, previous_rows) != previous_target`.
   That is the V60-requested previous-edge control.  The later print
   `N13_previous_edge_14_omission_negative_control=true` occurs only
   after this assert (the producer would abort otherwise).
2. **Omission of singleton current row 13.**
   `omitted_index = min(n13_weights)` (support size 1 ⇒ 13);
   `staged_n13_left == {(): -n13}` and
   `staged_without_one != {(): -n13}`.  Renamed
   `N13_singleton_current_row_omission_negative_control`.  With
   singleton support this is `n13 ≠ 0` in the reduced module.  It is
   no longer advertised as a two-previous-row “required edge” test.
3. **Independent quadratic control.**  First raw quadratic previous
   row is lifted and replayed against first rows **before** N13.
   `quadratic_source_positive_control_exact=true` follows that
   replay, then
   `arbitrary_degree_original_rows_preserved=true`.
4. **Frozen-unit `k`, no center-coordinate denominator.**
   `k = E3(252) - 342*S + 144*S**2 - 36*S**3` in the residue field
   `E`.  The producer collects
   `factor_strings(coordinate.denominator)` over
   `tri.e3_rat3_coordinates(k)`, asserts the set empty, prints
   `k_coordinate_denominator_factor_set=[]` and
   `k_is_frozen_residue_field_unit=true`, and already has
   `k * k.inverse() == E3(1)`.  This is the V60-requested typing
   emission, not an inference from the unit ledger alone.
5. **Live P12-without-N13 negative object.**  Two asserts:
   `scale_polynomial(n13_multiplier, 0) != tail * beta` (tail ≠ 0),
   and
   `p12_first_source != P12 - (-k/50)` on the live first-stage
   objects (V44’s in-memory inequality, which V60 only inferred).
   DAG
   `P12_without_N13_live_source_object_negative_control=true`.

**Survival.**  The five controls hit the identities they name.

---

## Charge 5 — Genuine P12, counts, residual, no previous-stage shortcut

**Result: holds.  P12 is `compile_current(...)[12]` on the 132-variable
bands, reduced only through first pivots.  Live h-zero counts match
pinned V44.  Composition with staged N13 is the exact residual
`-k/50`.  Previous-stage reduction of P12 is not used.**

- Lookup is `raw_current_rows[('X0', 12)]` from `source_records` of
  `qd.compile_current`, with no `qd.pack` and no skip of zeros.
- First-stage only: `divide_polynomial(p12_raw, first_pivots)`,
  `lift_relations`, `source_replay` against first rows.
  `P12_previous_stage_reduction_required=false`,
  `N13_nested_multiplier_expansion_used=false`.
- Live checks, then digest pins:
  - `len(raw_base)==2885` and
    `polynomial_digest(raw_base)==d71fd249…` (V44
    `raw_P12_base_sha256`);
  - 28 nonzero first relations and 1640 multiplier terms;
  - tail digest `0639f8cd…` and N13-multiplier digest `aef2b851…`;
  - `len(p12_remainder132)==3`, `len(tail132)==2`;
  - `projection(remainder, 0) == {(): -k/50}`.
- Pinned V44 h-zero stdout (hash `609349a5…`):
  `raw_P12_term_count=2885`, `raw_P12_base_terms=2885`,
  `first_source_nonzero_rows=28`,
  `first_source_multiplier_terms=1640`,
  `remainder_base_is_minus_k_over_50=true`,
  `N13_multiplier_denominator=(1)`.  The leftover V44 banner
  `P12_compiler=genuine_2893_term_source_polynomial` is the generic/b3
  count.  V64 never reprints 2893 for h-zero; it prints
  `genuine_P12_term_count_control=2885`, which `verify.py` now demands.
- Glue: `R - M * n13_staged == {(): -k/50}` with
  `M = (25/k)*tail` and `n13 == (k/25)*beta`.  Printed as
  `P12_remainder_glues_to_staged_N13_by_k_identity=true`.  This is
  **not** an expanded 132-variable `P12 - M*N13` against a fully
  substituted N13 source polynomial.  The N13 source lift is Charge 3.
- `P12_old_tail_and_multiplier_objects_exactly_equal=true` remains a
  canonical-digest comparison against scanned V44 hashes, not Python
  `==` on a live V44 object.  Parent import still replaces `n.digest`
  with `canonical_digest`.

**Survival.**  Genuine direct-first P12 with 2,885 terms, 28 first
rows, 1,640 multiplier terms, residual `-k/50`, no previous-stage
reduction of P12.

---

## Charge 6 — Denominator ledger / radical `{U, V, P3, QH}`

**Result: 16 lines, claimed products reconstruct by hand, radical is
exactly `{U, V, P3, QH}` as a coefficient-leaf support plus the pinned
V44 P12 termwise clear.  No missing displayed `k` or selected-edge
factor.  Not a termwise-product LCM of the N13 path.  `QH`
essentiality is not proved.**

Header plus 16 data rows; stdout `DAG_leaf_denominator_count=16`.
Ledger SHA256 equals V60’s, as expected: V64 still lifts the same two
previous original rows (control 0 + edge 14) and the same P12/N13
leaves.  Hand reconstruction of every claimed product (no CAS):

| denominator | claimed factors | reconstructs? |
|---|---|---|
| `1` | `[]` | yes (unit) |
| `U` | `U` | yes |
| `V` | `V` | yes |
| `V*U` | `U, V` | yes |
| `V^4+8 V^2 U^3-64 U^6` | `QH` | yes; this **is** `QH` |
| `V^4-32 V^2 U^3+128 U^6` | `P3` | yes; this **is** `P3` |
| `V^4 U+8 V^2 U^4-64 U^7` | `U * QH` | yes |
| `V^4 U-32 V^2 U^4+128 U^7` | `U * P3` | yes |
| `V^4 U^2-32 V^2 U^5+128 U^8` | `U^2 * P3` | yes |
| `V^5-32 V^3 U^3+128 V U^6` | `V * P3` | yes |
| `V^5 U-32 V^3 U^4+128 V U^7` | `U V P3` | yes |
| `V^5 U^2-32 V^3 U^5+128 V U^8` | `U^2 V P3` | yes |
| `V^6 U-32 V^4 U^4+128 V^2 U^7` | `U V^2 P3` | yes; equals V44 termwise and `p12_termwise_denominator` |
| `V^8-24 V^6 U^3-192 V^4 U^6+3072 V^2 U^9-8192 U^12` | `QH * P3` | yes (cross terms `-24, -192, 3072, -8192`) |
| that times `U` | `U QH P3` | yes |
| that times `V` | `V QH P3` | yes |

Union of factor strings is exactly
`U, V, QH=V^4+8 V^2 U^3-64 U^6, P3=V^4-32 V^2 U^3+128 U^6`.
Stdout `DAG_leaf_denominator_factor_set` matches, order
`U, V, QH, P3`.  DAG labels
`denominator_support_kind=leaf_coefficient_radical_plus_V44_P12_termwise_clear`
and `factored_clear_scalar_expansion_required=false`.

**Where the factors sit.**

- Standalone `QH` and `QH*P3` / `U*QH*P3` / `V*QH*P3` have
  `first_label=current_13_first_only_multipliers`.
- `U*QH` has `first_label=previous_('X-1', 14)_first_multipliers`.
  First-label is first-seen; current-13 leaves are ingested before
  previous-key leaves, so this line is the proof that key 14 carries a
  `QH` factor not already recorded from row 13.
- No `previous_('X-1', 0)_…` first_label.  The quadratic control
  introduces no new radical key.
- `k` contributes no `(V,U)` factor (Charge 4).  V44
  `N13_multiplier_denominator=(1)` is consistent with `25/k` adding
  no polynomial denominator.
- First rows on the V44 pin are `V*U` only.  Selected first-row and
  first-multiplier leaves are in the ledger.  Unused (zero-multiplier)
  first rows are not.  Pivot denominators of unused rows are outside
  the selected-edge leaf design.

Independent irreducibility of `P3` and `QH` over `Q` was not re-proved
(no CAS).  Flint emitted each as a single factor.  No ledger line
factors `QH` to power >1.  No extra prime appears.

The **sum** of products `multiplier * row` could still cancel `QH`.
V64 never asserts that the composed identity’s reduced denominator
still has `QH`.  Conservatively charging `QH=0` as open is correct;
neither `D(U V P3)` sufficiency nor `QH` essentiality is proved.

**Survival.**  Complete as a coefficient-leaf plus V44 termwise-clear
radical on the post-transport H=0 chart.  Not a fully expanded N13
termwise LCM.

---

## Charge 7 — Licensed scope

**Result: the written scope is the largest conclusion the source can
bear.**

Producer terminal flags:

```text
raw_stratum_fraction_field_source_identity_exact=true
raw_denominator_factor_strata_still_charged=true
whole_raw_stratum_killed=false
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
full_unused_previous_current_row_audit_complete=false
```

`verify.py` fail-closes on `whole_raw_stratum_killed=true` and prints
`whole_H_cover_complete=false`.  xmodel/README/`V64_RUNBOOK.md` refuse
whole-H, whole-fixed-A3, TD6, SP-2, landing, and JC2, and refuse a
`QH`-essentiality theorem.

Center typing is the raw chart `C=3U^2` over `Q(V,U)`:
`tri.center_coordinates()` on `STRATUM=="h-zero"` returns
`Rat3(3*U**2), Rat3(V), Rat3(U)`.  Dual `H = C - 3*U**2` is then
identically zero by substitution.  `B3` remains the generic polynomial
and is not set to zero.  `P3` and `QH` are emitted denominator factors,
not center equations.  Transport banner
`transport_chart=fraction_field_of_h-zero` already names a fraction
field (two transport events), not a polynomial ring.

The exact statement that survives is: on the source-typed chart
`H=0` (`C=3U^2` over `Q(V,U)`), in the post-transport fraction field,
after inverting the DAG-leaf radical `U V P3 QH`, the genuine P12
first-row identity and the singleton N13 current row 13 (via previous
`('X-1', 14)` and first rows) give residual `-k/50`.  That is a
fraction-field obstruction / exact identity on
`H=0, D(U*V*P3*QH)` inside the fixed source-typed A3 q2-beta section.

It is **not** a whole-`H` divisor theorem, not a cover of `U=0`,
`V=0`, `P3=0`, or `QH=0`, not unused-row completeness, not fixed-A3
globally, and not TD6 / SP-2 / landing / JC2.

---

## Separate verdicts

**Mathematical identity.**  Holds in source, as a post-transport
fraction-field identity: genuine P12 through 28 original first rows
with residual `-k/50` against staged N13, and current row 13 through
previous original row `('X-1', 14)` and original first rows, with
`k` a frozen A3 residue-field unit.

**Ancestry/source.**  The V60 two-edge N13 claim is repaired.  Row 13
has exactly one previous original-row edge, `('X-1', 14)`.
`('X-1', 0)` is a separate quadratic positive control.  Arbitrary-degree
original rows are preserved and replayed.  The DAG’s two
`previous_edge_key` blocks are the lift-cache dump and are restricted
by the later `N13_previous_edge_keys` line.

**Factor-ledger.**  16-line coefficient-leaf ledger plus pinned V44
termwise clear; radical exactly `{U, V, P3, QH}`.  No missing displayed
selected-edge or `k` denominator.  Not an N13 termwise-product LCM.
`QH` essentiality unproved.

**Custody.**  Freeze, manifest, artifact, `rc`, and declared
`SOURCE.sha256`/`source-check.txt` hashes recompute.  Executed parent
`77194c4b…` is live-pinned and independently hashed but omitted from
top-level `SOURCE.sha256`.  Host IP is README-only.  `verify.py` is a
marker gate.

**Exact licensed scope.**
`H=0, D(U*V*P3*QH)` inside the fixed source-typed A3 q2-beta section,
with
`P3=V^4-32 V^2 U^3+128 U^6` and
`QH=V^4+8 V^2 U^3-64 U^6`.
The four factor strata remain separate source-rebuild obligations.

---

## Repairs implemented relative to V60; remaining gaps

V60-requested repairs that are now live: split N13 previous-edge keys
from the quadratic control; previous-14 omission control; renamed
singleton-current omission; live P12-without-N13 object inequality;
`k` coordinate-denominator factor set; `genuine_P12_term_count_control=2885`;
`P12_remainder_glues_to_staged_N13_by_k_identity`; leaf-support kind
label; `arbitrary_degree_original_rows_preserved=true` after the
quadratic replay; extraction basename `...-v64` matching the tarball.

Remaining gaps (none of them reverses the licensed identity):

1. Top-level `SOURCE.sha256` omits the executed parent
   `full_p12_n13_unit_raw_canonical/replay.py` and 35 other archive
   members (unused producers, `V64_SOURCE.sha256`, a V57 `__pycache__`
   `.pyc`).  The parent is live-pinned.
2. `first_c1_c3_mpoly.py` is still imported without a hash pin (file
   is in `SOURCE.sha256`).
3. DAG still dumps unlabeled `previous_edge_key=('X-1', 0)` before the
   N13-restriction lines; `quadratic_control_key` on the DAG is a
   string literal.
4. `verify.py` remains a custody/marker gate, not an algebraic replay.
5. Host `100.26.198.153` is not in stdout/stderr.
6. `QH` may cancel in the summed identity; essentiality is not proved.
7. Unused previous/current rows are not audited
   (`full_unused_previous_current_row_audit_complete=false`).
8. P12/N13 “glue” is scalar on the first-stage remainder plus staged
   N13, not an expanded 132-variable `P12-M*N13` normal form.

---

## Commands and hashes used

Extract (read-only; producer not executed):

```bash
mkdir -p /tmp/jc2-td6-v64-review-grok-20260825
tar -xzf cases/td6_c1_c2_c3_q2_h_source_dag_repaired_v64_aws_20260825/archives/td6-aws-handoff-20260825-v64.tar.gz \
  -C /tmp/jc2-td6-v64-review-grok-20260825
```

Independent SHA256: Python `hashlib.sha256(path.read_bytes()).hexdigest()`
over every MANIFEST path, FREEZE path, charged xmodel file, extracted
`SOURCE.sha256` member, extracted V64 producer, extracted parent, and
the 36 unlisted archive files.  No `verify.py` execution.

Principal hashes:

```text
1a2e4f6766ffe5b15b963dd6ac86c02d538eb3e6d45b27d4a5a99e3c87a7aac6  source archive
14775e9ad4adfb0a20512823be01bdd48da711e30b8ac7796e094841f41edd06  v64.stdout
ef721416a7aac4f97167003801bfe94033e0b6627942d4ba9269c5565d9a962e  N13_PROOF_DAG.txt
259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385  DAG_LEAF_DENOMINATORS.tsv
777551c9ecff94cc98e16e8d076bffee7171e37e9690914b66d440615f9b53c7  SOURCE.sha256
9d3315f9270e513436e6549d8a1c1bce2378a903e80a39611286bde4f73e9dd0  V64 replay.py
77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef  parent raw-canonical replay.py
609349a53624531c1617104e2998ecf057192fea45bbe0ab41d7c2f24a1daf81  V44_H_ZERO.stdout
096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39  xmodel V64 report
3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069  V60 erratum
c99895806fbf7cbae8baea451856a86949c0b4049185dc5d0227425938a5d89e  V60 hostile review
```

CONFIRMED
