# Hostile no-shell review: TD6 H-stratum source DAG V60

Referee: independent algebraic/source-fidelity pass of the frozen V60
H-stratum claim only.  Operations used: read, glob, and search.  No
Bash, Python, CAS, shell, or network.  No byte hash was recomputed.
Custody markers are not treated as proofs of algebra.

Claim surfaces: `xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/`.  Producer:
`/tmp/jc2-td6-v60-review.ePmK88/td6-aws-handoff-20260825-v59/jc2/cases/td6_c1_c2_c3_q2_full_source_glue_raw_edge_dag_v60_20260825/replay.py`
(expanded tree basename `...-v59/`; claimed tarball name `...-v60`; see
Finding 9).

Import/hash pin chain actually executed by that producer, in order:

1. V60 `replay.py` pins and imports
   `td6_c1_c2_c3_q2_full_p12_n13_unit_raw_canonical_20260825/replay.py`
   (`PARENT_SHA256=77194c4b…`) and scans pinned `V44_H_ZERO.stdout`
   (`609349a5…`).
2. That parent pins and imports
   `td6_c1_c2_c3_q2_n13_v34_20260825/replay.py` (`1743dc29…`).
3. V34 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py` (`cf3f3f02…`).
4. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`1fb51264…`), then calls `tri.configure()`.
5. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
6. That file imports `first_c1_c3_mpoly.py` **without** a hash pin;
   pencil then pins `td6_jet_orbit_adjoint_20260824/replay.py`
   (`fb138b0f…`), which pins the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

`run_v60.sh h-zero` is the only entry that can produce this case:
it execs the raw V60 producer with `--stratum=h-zero`.  The generic
edge-DAG producer is a different file and is out of scope.

---

## Finding 1 — Raw center typing `H=C-3U^2=0`

**Result: holds in source.**  No stronger center equation is imposed.

- `c1_c2_c3_trivariate.py` `center_coordinates()` on `STRATUM=="h-zero"`
  returns `Rat3(3*U**2), Rat3(V), Rat3(U), "C=3U^2 over Q(V,U)"`.
  It does **not** take the `v-h-zero`, `origin`, `u-zero`, or
  `b3-param` branches.
- `beta_dual/replay.py` defines `H = C - 3*U**2` as a polynomial in
  the trivariate ring.  On the h-zero chart this is identically zero
  by substitution, not by an extra output equation.
- V60 `build_transport_and_rows()` copies those three coordinates
  into `r.fb.CENTER` and prints `source_center` / `raw_center_stratum`
  from that call.  Frozen stdout is
  `source_center=C=3U^2 over Q(V,U)` and `raw_center_stratum=h-zero`.
- `B3` remains the generic polynomial
  `4*C**2*U**2 - 4*C*V**2*U + 24*C*U**4 + V**4 - 20*V**2*U**3 + 20*U**6`.
  It is not set to zero.  `P3` and `QH` appear only as emitted
  denominator factors, not as center equations.
- The two-center-cover prototype has a *bivariate* h-zero
  (`C=3U^2 over Q(U)`, V dropped).  That function is not the one V60
  calls; `tri.center_coordinates()` is.

**Defects.**  None in the center substitution itself.  The banner
`transport_chart=fraction_field_of_h-zero` is printed before transport
and already names a fraction field, not a polynomial ring.  That is
scope, not a stronger center.

**Smallest repair.**  None required for typing.  Optional: print
`H_polynomial=C-3*U^2` and `H_after_chart=0` next to `source_center`
so the identity `H=C-3U^2` is visible in stdout rather than only in
the dual import.

**Survival.**  The producer is source-typed as the raw chart `C=3U^2`
over `Q(V,U)`.

---

## Finding 2 — Arbitrary-degree original rows; row-13 ancestry

**Result: original-row preservation holds; the claimed previous-row
set is false.**  Row 13 is traced through **exactly one** previous
key, `('X-1', 14)`, plus original first rows.  `('X-1', 0)` is an
independent quadratic positive control, not an N13 previous edge.

**What is algebraically checked (not a digest).**

- Echelon stages still go through `qd.pack`, which asserts every
  nonzero monomial has length 1 (linear packer; V48 failure class).
  That packer is **not** applied to the replayed original polynomials.
- `source_records` keeps `g.clean(polynomial)` at every degree,
  including zeros and degree 2.  Raw previous/current are built that
  way from `qd.compile_previous` / `qd.compile_current` on the
  132-variable bands.
- `lift_current_key` divides the **raw** 132-variable current
  polynomial by first pivots, remaps, then divides by previous
  pivots.  It asserts remainder equality against the packed reduced
  row and replays:
  - `first_only_relation` against packed first rows, equaling
    `raw_current - embed(remainder94)`;
  - `previous_relation94` against **packed** previous rows, equaling
    `remainder94 - embed(remainder56)`.
- `lift_previous_key` divides the **raw** 132-variable previous
  polynomial by first pivots and asserts
  `source_replay(relation, first_rows) == raw_previous - embed(remainder94)`
  with `remainder94` equal to the packed previous polynomial (or `{}`
  if that key is absent from the pack).
- `divide_polynomial` itself replays `remainder + sum quotient*pivot
  == original` before returning.  That is an exact edge identity.

**What is only a banner or a digest.**

- `arbitrary_degree_original_rows_preserved=true` is printed at the
  top of `main()`, before `source_records` runs.  It is not an
  assert.
- DAG lines `previous_edge_relation_sha256=…` are canonical digests
  of objects already checked.  They do not add a second algebraic
  test.
- `previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]` is
  `sorted(previous_first_relations_by_key)`, the lift **cache**, not
  the support of row 13.

**Ancestry of current row 13.**

- `N13_left_null_support=1`, `current_rows_source_lifted_indices=[13]`,
  DAG `current_row_key=('X0', 13)`,
  `previous_reduced_nonzero_rows=1`.
- Nonzero previous multipliers are the only keys `lift_current_key`
  sends to `lift_previous_key`.  With one nonzero previous multiplier,
  row 13 uses one packed previous row.
- The extra cache key is forced earlier:

  ```text
  quadratic_previous[0] -> lift_previous_key
  quadratic_source_positive_control_key=('X-1', 0)
  ```

  Therefore the unique N13 previous edge is `('X-1', 14)`, and
  `('X-1', 0)` is the first raw quadratic previous row, lifted as a
  control.  That matches DAG
  `previous_edge_nonzero_first_rows=14` for key 0 versus `38` for
  key 14 (row 13’s own first-only support is also 38).

The claim text “reduced through exactly the previous rows
`('X-1',0)` and `('X-1',14)`” is therefore a cache dump, not the
N13 support.  Nested previous-first multiplier products are
intentionally not expanded; transitivity is the free-module edge
rule printed as `proof_rule=exact_edge_substitution_in_free_equation_module`.
That rule is a proof-representation choice, not a digest.  It does
**not** make `('X-1', 0)` an N13 edge.

**Smallest repair.**

1. Print two distinct keys:
   `N13_previous_edge_keys=[('X-1', 14)]` and
   `quadratic_source_positive_control_key=('X-1', 0)`.
2. Change xmodel/README/verify.py to demand the first list, not the
   cache union.
3. Move `arbitrary_degree_original_rows_preserved=true` to after the
   quadratic-control replay assert.

**Survival.**  Arbitrary-degree original polynomials are the objects
replayed.  Row 13’s previous original-row edge is `('X-1', 14)` then
first rows.  The two-key N13 ancestry statement does not survive.

---

## Finding 3 — Genuine direct-first P12

**Result: holds.**  P12 is `compile_x_current(...)[12]` on the
132-variable bands, reduced only through first pivots.  Live h-zero
counts match the frozen V44 h-zero objects.

- V60 looks up `raw_current_rows[('X0', 12)]` from `source_records`,
  which enumerates `qd.compile_current` without skipping zeros and
  without `qd.pack`.  That is the same compiler family V44 uses as
  `compile_current(...)[12]`, not a later-echelon `X0,t12` packed
  row.
- First-stage only: `divide_polynomial(p12_raw, first_pivots)`,
  `lift_relations`, `source_replay` against first rows, with
  `P12_previous_stage_reduction_required=false` and
  `N13_nested_multiplier_expansion_used=false`.  There is no nested
  previous-first expansion of P12.
- Exact live checks, then digest pins:
  - `len(raw_base)==2885` and
    `polynomial_digest(raw_base)==d71fd249…` (V44
    `raw_P12_base_sha256`);
  - 28 nonzero first relations and 1640 multiplier terms
    (`sum(len(relation))`);
  - tail digest `0639f8cd…` and N13-multiplier digest `aef2b851…`,
    matching V44 stdout;
  - `len(p12_remainder132)==3`, `len(tail132)==2`.
- Frozen V44 h-zero stdout: `raw_P12_term_count=2885`,
  `raw_P12_base_terms=2885`, `raw_P12_beta_degree=1`,
  `first_source_nonzero_rows=28`,
  `first_source_multiplier_terms=1640`.  The V44 banner
  `P12_compiler=genuine_2893_term_source_polynomial` is a leftover
  generic/b3 count (V60’s b3 expected base is 2893) and is **not**
  the h-zero live count.  V60 does not reprint 2893 for h-zero.

**Defects.**  `P12_old_tail_and_multiplier_objects_exactly_equal=true`
is printed after digest equality, not after a Python `==` on the V44
in-memory objects (V44 is a scanned stdout, not a live object).
That is still an exact canonical-digest comparison of the live tail
and multiplier against the reviewed hashes, because parent import
replaces `n.digest` with `canonical_digest` (coordinate form, not
object addresses).  `verify.py` never checks
`genuine_P12_term_count_control=2885`.

**Smallest repair.**  Add that term-count marker to `verify.py`.
Optionally stop pinning the V44 `genuine_2893` banner as if it were
the h-zero term count (V60 already uses 2885).

**Survival.**  P12 is the genuine direct-first object with 2,885
terms, 28 first rows, 1,640 multiplier terms, and exact V44 tail
and multiplier digests.  No giant nested-multiplier shortcut is
used for P12.

---

## Finding 4 — P12/N13 composition and residual `-k/50`

**Result: the residual identity holds in source, with a tautological
scalar step.  `k` is a frozen-A3 residue-field unit, not a hidden
`(V,U)` divisor in the ledger.**

Let `R` be the first-pivot remainder of genuine P12.  V60 asserts:

1. `P12 = first_source + R` (replay);
2. `projection(R, 0) = {(): -k/50}`;
3. `R + k/50 = beta * tail` (`beta_tail`: no constant leftover,
   and the difference equals `tail * beta`);
4. staged current value `n13 == (k/25)*beta` and
   `k * k.inverse() == E3(1)`;
5. `M := (25/k)*tail`, then `M * n13 == tail * beta`.

Step 5 is automatic from step 4 and the definition of `M`.  The
nontrivial algebra is steps 1–4.  Chaining them gives

```text
P12 - first_source - M * n13_staged = -k/50.
```

That is an exact scalar composition on the first-stage remainder
plus the staged current value.  It is **not** an expanded identity
`P12 - M*N13` against a fully substituted N13 source polynomial
in the 132-variable module.  The N13 source lift is the separate
edge DAG of Finding 2.

**Typing of `k`.**

```text
S = E3(qd.uniform.S_FIELD)
k = E3(252) - 342*S + 144*S**2 - 36*S**3
```

`S_FIELD` is the generator of the moduli field
`K = Q[S]/(F_MONIC)` inside `E = K[A]/(A^3-ALPHA)`.  `E3(...)`
embeds that via `FIELD.from_e`.  Those coordinates are constants in
the `C,V,U` chart (Rat3 constants), not polynomials in `V,U`.
Inverting `k` is inversion in the residue field `E`.  The factor
`50` is inverted in `Q`.  Neither is a new `D(V,U)` stratum.

Consistency with the leaf ledger: `N13_scalar` and `P12_unit` are
fed to the ledger; no first-label other than `current_13_weight`’s
unit `1` is needed for them.  Frozen V44 has
`N13_multiplier_denominator=(1)`.  That is evidence that `25/k`
contributes no polynomial `(V,U)` denominator.  V60 does **not**
print `e3_rat3_coordinates(k)` or factor `k`, so this is inferred
from typing plus the unit ledger, not from an emitted factorization
of `k`.

**Unreported localization?**  No extra `(V,U)` factor of `k` is
visible.  The condition `k ≠ 0` in `E` is a statement about this
frozen A3, already assumed by the q2-beta section.  Transport’s two
events are prior chart localization (`transport_chart=fraction_field_of_h-zero`)
and are not in the 16-line leaf ledger; they are not `k`.

**Smallest repair.**  Print
`k_coordinate_denominator_factor_set` from `e3_rat3_coordinates(k)`
and `k_is_residue_field_unit=true`.  Rename the glue flag to
`P12_remainder_glues_to_staged_N13_by_k_identity=true` so it is not
read as an expanded 132-variable `P12-M*N13` normal form.

**Survival.**  Residual `-k/50` is the exact beta-degree-0 first
remainder.  `k` is typed nonzero in `E`.  It does not add an
unreported `(V,U)` leaf factor.  The “glue” is scalar, not a
nested source expansion.

---

## Finding 5 — Negative controls

### One-required-edge omission

**Attacks the staged current left-null, not the previous/first DAG.**

```text
omitted_index = min(n13_weights)   # support size 1 => row 13
staged_n13_left == {(): -n13}      # algebraic
staged_without_one != {(): -n13}   # empty sum vs -n13
```

With singleton support this is exactly `n13 ≠ 0` (more precisely:
the empty combination is not `-n13`).  It does **not** drop
`('X-1', 14)` or a first-row edge and re-test.  It is not a wrapper:
the add/assert are on the reduced 56-variable current row.  It is
the wrong control for the advertised “required edge” set of size 2.

### P12 without N13

**Attacks the first-stage remainder tail, not a wrapper.**

V60 asserts `M * 0 != tail * beta`, i.e. `tail ≠ 0`.  Together with
`R = -k/50 + beta*tail` this says first rows alone do not produce
`P12 + k/50`.  V44’s parent has the stronger in-memory test
`first_source_identity != P12 - (-k/50)`.  V60 does not re-assert
that object inequality; it infers it from `len(tail)==2` and the
zero-multiplier compare.  That still hits the claimed P12/N13
scalar dependency, not merely a print wrapper.

Neither control tests omission of `('X-1', 0)` or `('X-1', 14)`.

**Smallest repair.**  Rename the first flag to
`N13_singleton_current_row_omission_negative_control=true`.  If a
previous-edge control is wanted, drop `('X-1', 14)` from
`previous_relation94` and assert the 94-variable replay fails.
Re-assert V44’s `first_source != P12 + k/50` on the live P12
objects.

**Survival.**  Both controls are exact and hit real identities.
They do not certify the two-previous-row story.

---

## Finding 6 — Sixteen denominator-ledger lines

**Result: 16 lines, factorizations reconstruct, radical is
`{U, V, P3, QH}` as claimed.**  Independent irreducibility of `P3`
and `QH` was not re-proved (no CAS).  Termwise products for the N13
path are not expanded.

Header plus 16 data rows; stdout `DAG_leaf_denominator_count=16`.
`factor_strings` uses `polynomial.factor()` with empty output for
degree 0, matching line `1`.  Hand expansion of every claimed
product:

| denominator | claimed factors | reconstructs? |
|---|---|---|
| `1` | `[]` | yes (unit) |
| `U` | `U` | yes |
| `V` | `V` | yes |
| `V*U` | `U, V` | yes |
| `V^4+8 V^2 U^3-64 U^6` | `QH` | yes, this **is** `QH` |
| `V^4-32 V^2 U^3+128 U^6` | `P3` | yes, this **is** `P3` |
| `V^4 U+8 V^2 U^4-64 U^7` | `U * QH` | yes |
| `V^4 U-32 V^2 U^4+128 U^7` | `U * P3` | yes |
| `V^4 U^2-32 V^2 U^5+128 U^8` | `U^2 * P3` | yes |
| `V^5-32 V^3 U^3+128 V U^6` | `V * P3` | yes |
| `V^5 U-32 V^3 U^4+128 V U^7` | `U V P3` | yes |
| `V^5 U^2-32 V^3 U^5+128 V U^8` | `U^2 V P3` | yes |
| `V^6 U-32 V^4 U^4+128 V^2 U^7` | `U V^2 P3` | yes; equals V44 termwise and V60 `p12_termwise_denominator` |
| `V^8-24 V^6 U^3-192 V^4 U^6+3072 V^2 U^9-8192 U^12` | `QH * P3` | yes (cross terms `-24, -192, 3072, -8192`) |
| that times `U` | `U QH P3` | yes |
| that times `V` | `V QH P3` | yes |

Over `Q`, neither `P3` nor `QH` splits as
`(V^2+s U^3)(V^2+t U^3)` (`s,t` would require `√2` or `√5`).  Flint
emitted each as a single factor; that is the source’s
normalization.  Hidden extra powers inside one key: none except
`U^2` where claimed.  The multiplicity column is leaf-occurrence
count, not algebraic multiplicity of a prime.

**Coefficient vs termwise.**  Leaves are Rat3 **coefficient**
denominators of DAG objects (weights, multipliers, selected rows,
raw/reduced rows, N13, unit, tail, multiplier, V44 clear).  V60
does not multiply multiplier×row and LCM those products except by
pinning V44’s P12 termwise denominator as
`V44_P12_termwise_clear` (multiplicity 1).
`factored_clear_scalar_expansion_required=false` is explicit: the
clearing polynomial is not expanded.

**Radical.**  Union of factor strings is exactly
`U, V, QH=V^4+8 V^2 U^3-64 U^6, P3=V^4-32 V^2 U^3+128 U^6`.
Stdout factor set matches, order `U, V, QH, P3`.

**Smallest repair.**  State in README that the radical is the
**leaf-coefficient** radical, not a termwise-product LCM of the N13
edges.  Optional: emit that LCM as one extra line.

**Survival.**  The 16-line ledger is internally exact as printed.
The open it supports is leaf support on the post-transport H=0
chart.

---

## Finding 7 — `QH` in row-13 first multipliers and previous-14

**Result: both occurrences are in the ledger.  Minimality of `QH`
is not proved.  No missing displayed factor; no hidden extra `QH`
power in a single key.**

- Standalone `QH` (381) and `QH*P3` / `U*QH*P3` / `V*QH*P3`
  (90+28+104) have `first_label=current_13_first_only_multipliers`.
  So `QH` divides row-13-to-first multiplier denominators.
- `U*QH` (14) has
  `first_label=previous_('X-1', 14)_first_multipliers`.
  So `QH` divides the previous-14-to-first edge.  Because
  first-label is first-seen, this line is the **proof** that key 14
  carries `QH`; additional standalone `QH` on that edge would have
  been absorbed into the earlier `QH` key.
- First rows in V44 are only `V*U`.  If that remains true here,
  Rat3 cancellation in a single product `multiplier * first_row`
  does not remove `QH` unless the multiplier numerator already has
  `QH`.  The **sum** of products could still cancel `QH`.  V60
  never asserts that the composed identity’s reduced denominator
  still has `QH`.
- No ledger line factors `QH` to power >1.  No extra prime appears
  beyond `{U,V,P3,QH}`.

`('X-1', 0)` does not introduce a new `QH` key.  Charging `QH`
from the quadratic control is unnecessary; charging it from row 13
and key 14 is supported.

**Smallest repair.**  Keep `QH` as an emitted leaf obligation (the
package already refuses to drop it).  Do not claim `QH` is an
essential prime of the simplified identity.  If essentiality is
wanted, reduce the composed current-13 identity modulo
`{U,V,P3}`-inverted coefficients and show a remaining `QH`
denominator.

**Survival.**  `QH` is present on the two stated edges as leaf
coefficients.  It may or may not cancel in the sum.  The
conservative charge of `QH=0` as still-open is correct; a theorem
that `D(U V P3)` already suffices is **not** proved, and a theorem
that `QH` cannot be removed is **not** proved either.

---

## Finding 8 — Logical conclusion

**Result: the written scope is the largest conclusion the source
can bear, once Finding 2 is repaired.**

Producer terminal flags:

```text
raw_stratum_fraction_field_source_identity_exact=true
raw_denominator_factor_strata_still_charged=true
whole_raw_stratum_killed=false
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

`verify.py` fail-closes on `whole_raw_stratum_killed=true` and
`full_A3_beta_family_killed=true`.  xmodel/README already refuse
whole-`H`, full-A3, TD6, SP-2, landing, and JC2.

The exact statement that survives is: on the source-typed chart
`H=0` (i.e. `C=3U^2` over `Q(V,U)`), in the post-transport
fraction field, after inverting the DAG-leaf radical `U V P3 QH`,
the genuine P12 first-row identity and the singleton N13 current
row 13 (via previous `('X-1', 14)` and first rows) give residual
`-k/50`.  That is a fraction-field obstruction / exact identity on
`H=0, D(U V P3 QH)`.  It is not a whole-`H` divisor theorem, not a
cover of `V=0`, `P3=0`, or `QH=0`, not fixed-A3 globally, and not
TD6/JC2.

**Defects.**  Packaging that two previous rows are N13-required
would, if left un-repaired, overstate the DAG.  It would still not
upgrade the theorem to whole-`H`.

**Smallest repair.**  Replace “previous rows 0 and 14” by “previous
row 14, with independent quadratic control 0” in xmodel and README.
No change to the negative whole-H/TD6/JC2 claims.

**Survival.**  The scoped fraction-field conclusion survives.  The
unscoped readings named in the prompt do not, and the package
already denies them.

---

## Finding 9 — Manifest, freeze, paths, hashes, endpoint

**Result: hash **strings** are internally consistent across the
case files I was allowed to read.  No SHA256 was recomputed from
bytes.  `verify.py` is a custody/marker gate, not an algebraic
replay.  Endpoint fields in stderr/rc match README.**

String cross-checks (not recomputations):

| object | digest prefix | where the same hex appears |
|---|---|---|
| claimed source tar | `78dae78e…` | xmodel, README, `verify.py` EXPECTED, `MANIFEST.sha256`, `aws_run/ARCHIVE.sha256` body |
| stdout | `d029a06d…` | same set |
| DAG | `95161169…` | same set; also printed in stdout |
| ledger | `259605ae…` | same set; also printed in stdout |
| stderr | `91b7c192…` | EXPECTED + MANIFEST |
| `ARCHIVE.sha256` file | `bbbb4572…` | EXPECTED + MANIFEST |
| V44 h-zero stdout | `609349a5…` | V60 producer, `V60_SOURCE.sha256`, V60 stdout `parent` pin |
| raw-canonical parent | `77194c4b…` | V60 producer, `V58_SOURCE.sha256`, V60 stdout |
| V60 producer | `7e7ac7d2…` | `V60_SOURCE.sha256` only |
| README | `eb6dc3a8…` | MANIFEST + FREEZE |
| verify.py | `a2b48cfc…` | MANIFEST + FREEZE |
| xmodel | `bd923e4b…` | FREEZE only |
| MANIFEST | `afeaaf4e…` | FREEZE only |

**Byte hashes not recomputed (complete list).**  Every digest
above, plus `V60_RUNBOOK.md` `a3def0a6…`, `run_v60.sh`
`76cdc7d5…`, V44 b3 stdout `a33dc711…`, generic V60 replay
`a6f735a1…`, all `SOURCE.sha256` / `V34` / dual / trivariate /
pencil / jet-orbit / q2-compiler / moduli pins, `start_utc`
`0c54db53…`, `end_utc` `3288e249…`, `rc` `9a271f2a…`, and the
DAG/ledger **contents** as bytes.  A no-shell session cannot
honestly confirm any of them.

**Path / endpoint.**

- `aws_run/rc` is `0\n`; stderr `Exit status: 0`; elapsed
  `27:52.03`; RSS `674212` KiB.  README matches.
- `start_utc` / `end_utc` are `2026-08-25T12:29:27Z` /
  `2026-08-25T12:57:19Z`.  README matches.
- Stdout artifact paths use
  `/home/ubuntu/runs/td6_v60_h_raw_r6d_20260825T1231Z/`.  README
  run path matches.
- `ARCHIVE.sha256` body names
  `/home/ubuntu/stage/td6-aws-handoff-20260825-v60-78dae78e.tar.gz`.
- README host `100.26.198.153` does not appear in stdout/stderr.
  Not a contradiction; also not an in-artifact proof of host.
- Expanded tree given for this review is
  `/tmp/jc2-td6-v60-review.ePmK88/td6-aws-handoff-20260825-v59/`.
  Basename says **v59**; claimed archive name says **v60**.  The
  tree does contain `V60_SOURCE.sha256`, `run_v60.sh`, and the V60
  producer.  Without a hash of the tarball and of the expanded
  `replay.py`, this session cannot prove the tree is the frozen
  v60 archive.

**`verify.py` is not algebra.**  It hashes six paths, checks `rc`,
then `assert marker in out` for banners including
`previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]` and
`combined_unit_residual_is_minus_k_over_50=true`.  It checks that
`P3` and `QH` strings occur in the ledger and that two labels
exist.  It never imports `replay.py`, never divides a polynomial,
and never checks 2885 terms.

**Smallest repair.**  Record the expanded-tree basename next to the
tarball name, or extract to a `...-v60/` directory.  Split verify
markers as in Finding 2.  Do not cite `verify.py` PASS as algebraic
confirmation.

**Survival.**  Internal hex agreement is good.  Independent
byte-level custody and independent algebra are both unproved in
this session.

---

## Survival statement

The frozen V60 producer, if it ran as written, is a source-typed
h-zero (`C=3U^2` over `Q(V,U)`) exact identity in the post-transport
fraction field: genuine P12 reduces through 28 original first rows
(2,885 terms, 1,640 multiplier terms, V44 tail and multiplier
digests), staged N13 is `(k/25)beta` with residual `-k/50`, and
current row 13 lifts through previous original row `('X-1', 14)`
and original first rows.  The emitted leaf radical is
`U V P3 QH`, with `QH` actually present on the row-13 first
multipliers and on the row-14 previous-to-first edge.  That is at
most an exact fraction-field obstruction on `H=0, D(U V P3 QH)`.

It does **not** survive as: a two-previous-row N13 DAG including
`('X-1', 0)`; a whole-`H` theorem; a cover of `V=0`, `P3=0`, or
`QH=0`; a proof that `QH` is essential; a global fixed-A3 theorem;
TD6; SP-2; landing; or JC2.  Byte hashes were not recomputed.
Custody markers do not prove the arithmetic.

Required repairs are packaging and control-naming (Findings 2, 4,
5, 8, 9), not a different center or a different P12 object.

CONFIRMED_WITH_REPAIRS
