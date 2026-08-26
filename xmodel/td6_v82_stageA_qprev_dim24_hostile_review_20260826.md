# Hostile review: TD6 V82 Stage-A `Q_prev=Q`, dimension 24

Inspection only of the charged producer theorem and the frozen Stage-A
case.  No CAS, no producer execution, no `verify.py` run, no Python
hashing, no shell, no solver, no Lean, and no Flint.  Stored `PASS` /
producer-verdict strings were ignored as proof.  SHA-256 values below
are the pins recorded in `FREEZE.sha256`, `MANIFEST.sha256`,
`SOURCE.sha256`, `launch.meta`, and stdout; they were checked for
internal consistency and for byte-identity of the load-bearing tables
by direct read.  They were not recomputed.  `source.tar.gz` members
were not unpacked.  V82Q source typing was read from the V82Q stdout,
from the V82Q `source_check.stdout` file list, and from the already
extracted copy of the same all-q producer that the V78B archive pin
`cc7717b46d…` and the V82P3 payload both list as
`7e5ade2b0f8723e2ac502978fd8ea48470e57231a83c8e8c0a233f64948b695d`.

Charged surfaces and recorded pins:

- producer `xmodel/td6-v82-stageA-qprev-dim24-producer-20260826.md`,
  recorded SHA `6867c9159287ce76bdf6e4b75764bf2583aa20096b74e99cc43a7b9af629541b`
  (second line of `FREEZE.sha256`);
- case `cases/td6_c1_c2_c3_kernel_previous_pole_stageA_v82qp3_aws_20260826/`;
- `MANIFEST.sha256`, recorded SHA
  `918bd017264959c92c0b7ce4c2d9fff7538841b73f348457ddd4521e83adedb9`
  (first line of `FREEZE.sha256`, matching the charge);
- `FREEZE.sha256`, charged SHA
  `02b8da31a7af66b65f591cf674f391d3acffdb2165acba925c0beeeb0abd682a`
  (not recomputed).

Consumed as already-reviewed ancestry, not re-proved: V81C transport
kernel dimension 24, V78 22-axis FIRST zero, V82S2 `d10,d15` FIRST
zero, and the FIRST generic-surjectivity corollary.  This freeze
independently reconstructs the transport and FIRST gates as
fail-closed prerequisites of the previous/pole stage; those
reconstructions are audited here only as gates, not as a re-proof of
the FIRST theorem.

---

## Findings

**1. [Confirmed] Exact source typing is the 22 licensed q-exponents
`q2..q14,q16..q24` in the square-zero ring `E(C,V,U)[eps_e]` together
with the two dead-stretch coefficients `d10,d15` in the pole chart
`y = r^5 + d_m r^m + zeta r^{17}`, all at symbolic center `(C,V,U)`.
V82Q and V82P3 are different Dual presentations of the same previous/pole
compilers; the mismatches are typed and do not change the 24 displayed
axes or the common localization.**

V82Q stdout, on both hosts, prints

```text
producer=TD6-A3-ALL-Q-VECTOR-AD-V78B
mode=staged
q_exponents=2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24
q15_lower_target_shear_gauge_excluded=true
source_center=(C,V,U)
source_p_boundary=t^15_fixed
source_dead_stretch=0_fixed
scope_open=D(U*(C-3U^2)*B3)
V32_base_source_sha256=dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742
```

The all-q producer (SHA `7e5ade2b…`) sets
`Q_EXPONENTS = tuple(range(2, 15)) + tuple(range(16, 25))` with
`assert 15 not in Q_EXPONENTS`, and Dual `EJet` with sparse derivatives
keyed by those exponents.  `q15` is the excluded lower-target shear
gauge.  Transport is undeformed in every q-column
(`transport_matrix_all_q_derivative_zero=true`) with RHS q-derivatives
retained.  Direct q-prime omission is per-axis and dual-host identical
(e.g. `first_q2_column=221;omit=1;sha=240fe449…` on both r6d and
Box03).

V82P3 stdout, on all four lanes, prints `dead_axis=d10` or `d15`,
`source_center=(C,V,U);symbolic=true`, and
`scope=D(U*H*B3)_generic_center_square_zero_previous_pole_source_incidence`.
The shard refuses any `TD6_DEAD_LEVEL` outside `{10,15}`.  It
hash-imports V82S2 `a344d3c211…`, which hash-imports V82 `537219eb…`
and V81B `AxisJet`.  Dead stretch is inserted by `insert_axis` after
`v81.dead_lift`; first-to-previous/pole composition is
`compose_axis_forms` wholly inside `AxisJet`, with an explicit
preflight that a 33-axis `AxisJet` scale is not an `EJet`.
`H = C - 3*U**2` is the V32 identification, so `D(U*H*B3)` is the same
declared chart as V82Q's `D(U*(C-3U^2)*B3)`.

Flagged presentation mismatches, none of which is a 24-axis or
localization contradiction:

| item | V82Q | V82P3 |
|---|---|---|
| Dual | `EJet`, keys `2..14,16..24` | `AxisJet`, keys `d10` / `d15` |
| composer | `compose_forms` (`EJet`) | `compose_axis_forms` (`AxisJet` only; V82P/P2 `EJet` coercion is the typed-composition erratum, not consumed) |
| previous/pole leftover count | `dependent_count=1` | `dependent_count=0` |
| conormal table header | `… exponent …` | `… axis …` |
| empty-table SHA | `b1b1f698…` | `2c0e79ec…` |
| archive | `cc7717b46d…` (V78B staged bundle) | `1a23ceca70…` (V82P3 shard bundle) |
| process state | harvested mid-current | four independent `rc=0` |

Both presentations call the same packed compilers

```text
qd.pack("X-1", qd.compile_previous(f1,f2,g1,g2))
qd.pack("P1",  qd.compile_pole_previous(pole_f, pole_g))
parameterize(94, previous_rows)  # 38 pivots, 56 free
```

on the same first-band free module of rank `38/132`.  The first/transport
mpoly pins `ce400cca…` / `17f342d6…` and the V32 pin `dcc7003def…` are
the common source of those compilers.  The leftover-count mismatch is
Dual packing: V82Q's 22-derivative `EJet` can pack a row that is later
reduced to a zero 22-column leftover, which `solve_cert_jet` records as
one dependent row; V82P3's one-axis `AxisJet` never packs that
q-only Dual row, so it records zero dependents.  The V82Q conormal table
of that leftover is empty (Finding 2), so the extra packed row does not
cut any of the 22 q-axes.

No `d6..d9`, `d11..d14`, `d16`, `d5`, `d17`, or `q15` is claimed.

**2. [Confirmed] The V82Q previous/pole checkpoint is complete frozen
evidence.  The parent process was still live in current stage; that does
not touch the already-written previous/pole table, kernel, or stdout
block.  Rank is `38/94`, one leftover Dual row, 22-axis conormal rank
`0/22`, unit denominator, pivot-source replay, and dual-host
byte-identical table and kernel.**

Both V82Q stdouts end on the flushed line
`previous_pole_all_q_full_family_parameterization=true`.  There is no
`CURRENT_*.tsv`, no staged `PASS`, no `rc`, and stderr is the empty
byte string (`e3b0c442…`).  `launch.meta` records
`mode=staged`, `timeout_seconds=21600`, source archive `cc7717b46d…`,
r6d host `ip-172-30-0-45` tag `td6_v82q_qkernel_staged_r6d_20260826T0302Z`,
Box03 host `ip-172-30-0-249` tag
`td6_v82q_qkernel_staged_box03_20260826T0302Z`.  Harvest at this
boundary is exactly what the source does: `run_staged` writes
`PREVIOUS_POLE_{CONORMAL,KERNEL}` and prints the full-family marker
*before* composing into current.

The previous/pole block on both hosts is

```text
previous_pole_all_q_rank=38/94
previous_pole_all_q_dependent_count=1
previous_pole_all_q_pivot_source_replay=true
PREVIOUS_POLE_conormal_coordinate_count=0
PREVIOUS_POLE_conormal_rank=0/22
PREVIOUS_POLE_conormal_kernel_dimension=22
PREVIOUS_POLE_denominator_factor=(1, [])
PREVIOUS_POLE_conormal_sha256=b1b1f6980b03fb5ea4695ba82eb3fc628db410e1fc7932161c2a1ca29352cb30
PREVIOUS_POLE_kernel_sha256=ef4d3be85c40e12582c80963eb36e9e3ff843ec4c239679d0060ff873c4905bb
previous_pole_all_q_full_family_parameterization=true
```

`parameterize` prints `pivot_source_replay=true` only after every packed
row, pivot or leftover, has been reconstructed from original source
rows.  `conormal_table` on an empty coordinate dictionary writes a
header-only TSV and the identity kernel of the 22-space.  Direct read:
both hosts' `PREVIOUS_POLE_CONORMAL.tsv` are the single header line
`compatibility\tkey\tcoordinate\texponent\tcoefficient_sha256\tcoefficient_exact`.
Both hosts' `PREVIOUS_POLE_KERNEL.exact.tsv` are 22 data lines, keys
`2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24` in order,
each a single nonzero unit coefficient with digest `d698d748…` and
`e3_exact` of `E3(1)`.  That is the identity basis of `ker(0: K^{22}->0)`,
not an 18-dimensional family: the 18-tuple is the trivariate encoding of
the scalar `1`.  FIRST tables/kernels share these SHAs because FIRST is
likewise a header-only empty 22-column table with the same identity
kernel; that is required, not a copy of one stage onto the other.

The one leftover Dual row has empty 22-axis coordinates, so it does not
obstruct `Q_prev`.  `full_family_parameterization=true` is the branch
taken only when `dependent_obstruction_coordinates` is empty; a nonempty
previous/pole conormal would have printed
`current_stage_skipped_due_previous_obstruction=true` and would not have
written this kernel.

**3. [Confirmed] All four V82P3 lanes are dual-host `rc=0`.  Raw
previous/pole columns are nontrivial and dual-host identical by SHA.
Typed composition and omission controls pass.  Pivot combinations are
replayed inside `solve_cert`.  Final conormal tables are header-only
zeros with unit denominators.**

Four `rc` files are the single byte-string `0\n` (shared recorded SHA
`9a271f2a…`).  Four `/usr/bin/time -v` stderrs record
`timeout 14400 bash run_v82p.sh` and `Exit status: 0`.  `run_v82p.sh`
refuses non-Linux, any tag not matching `td6_v82p_*`, and any level
other than `10|15`; it hash-checks `SOURCE.sha256` before exec.  Tags
`td6_v82p_v3_{r6d,box03}_d{10,15}_20260826T0340Z` are unique.
Hosts are `ip-172-30-0-45` and `ip-172-30-0-249`.  Both
`registration.meta` files pin archive `1a23ceca70…`.

Every lane prints, before any previous/pole algebra:

```text
empty_previous_pole_table_positive_control=true
axisjet_composition_boundary_preflight=true
```

The control writes the header-only table into `empty_table_control/`
with `assert control_denominator == v81.tri.ONE` and
`assert ONE == CTX.constant(1)` (V82P2 reporter erratum).  The preflight
composes a nontrivial one-variable square-zero `AxisJet` form against a
directly constructed expected answer and asserts the result is `AxisJet`
and not `EJet`.  Then:

```text
transport_rank=3470/3602;free=132
transport_conormal_exact_zero=true
transport_original_3470_pivot_rows_replayed=true
first_conormal_exact_zero=true
first_raw_source_omission_control=true
all_first_pivot_source_combinations_replayed=true
all_previous_pole_input_forms_axisjet_typed=true
previous_pole_rank=38/94
previous_pole_dependent_count=0
previous_pole_axis_conormal_rank=0/1
previous_pole_axis_conormal_coordinate_count=0
previous_pole_axis_denominator_factor=(1, [])
previous_pole_axis_table_sha256=2c0e79ec04b6e8cfc4da5ca71454e2b27aac9ad2fa20a13a97b3066947f76400
all_previous_pole_pivot_source_combinations_replayed=true
```

Raw previous/pole axis columns, dual-host identical:

| axis | raw entries | raw SHA-256 |
|---|---:|---|
| d10 | 1115 | `86e61fc847d09005e00be42eb6cda44312a50ffb4b396ac9195ddaedfeeadfb6` |
| d15 | 980 | `90e13af111cdda4febadd57ccb6a583b650d5ccca25c473775bb68603e0b99b2` |

Those SHAs exist only in pinned stdout, not as frozen TSVs.  Dual-host
identity of the strings is the inspectable presence evidence.  An
axis-omitted first-band column is required empty and distinct from the
positive first-band column before previous/pole is reached.  A producer
that composed base forms rather than axis forms would emit a zero raw
previous/pole column and would not print these counts.

`all_previous_pole_pivot_source_combinations_replayed=true` is an
unconditional print in the shard, but it is reached only after
`v82.parameterize` / `solve_cert` has reconstructed every leftover and
every surviving pivot from original packed rows.  A skipped replay is a
nonzero exit, not a silent empty table.

Direct read: all eight actual and control tables
(`D10`/`D15` × table × control × two hosts) are the same header-only
string
`compatibility\tkey\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact`.
That is emptiness of leftover previous/pole incidence, not emptiness of
the raw column.  `previous_pole_kernel_is_not_a_current_or_nonlinear_kernel=true`
is printed on every lane.

**4. [Confirmed] Vanishing of `L_prev` on the 24 displayed basis axes
implies `Q_prev = Q` of dimension 24.  No 24-column one-ring previous/pole
run is required.  The argument is first-order Dual-linearity on a named
basis, the same concatenation already used at transport and FIRST.**

Let `K = E(C,V,U)` and

```text
Q = span_K(q2..q14, q16..q24, d10, d15).
```

These 24 names are distinct square-zero coordinates: 22 `EJet`
exponents plus two `AxisJet` dead axes.  They are linearly independent
by construction of the Duals (`assert exponent in Q_EXPONENTS`,
`assert axis in AXES`).  Dimension 24 is that basis count, not a
computed 24-column rank.

`L_prev` is the K-linear leftover map of the packed previous X-band
plus pole equations after the rank-38 first-stage parameterization.
Square-zero Dual arithmetic has `eps_i eps_j = 0`, so there are no
first-order mixed q-dead cross terms.  V82Q evaluates `L_prev` on the
22 q-basis vectors jointly and gets the zero 22-column.  V82P3
evaluates `L_prev` on `d10` and on `d15` separately and gets the zero
1-column twice.  Concatenation of empty columns is the zero map
`Q -> C_prev`.  Therefore `ker(L_prev|Q) = Q` and `dim_K Q_prev = 24`.

This is the same first-order column concatenation as the already
reviewed transport kernel (V81C) and FIRST kernel (V78+V82S2 corollary).
A joint 24-axis Dual would only recompute bilinear `eps_q eps_d`
products that are identically zero at this order.  The V82Q joint 22-run
already is the q-block of that Dual; adding `d10,d15` one axis at a time
does not create a new linear relation among the 24.

What is *not* proved: that a 24-column Dual GE of previous/pole would
select the same 38 base pivots if dead and q jets were present
simultaneously in one Dual object.  Base pivots are chosen only on
nonzero undeformed values (`coefficient.value`), so Dual jets do not
change the undeformed 38/94 echelon.  Both presentations already report
that same undeformed rank.

**5. [Confirmed] Same-open firewall holds.  `D(U*(C-3U^2)*B3)` is a
conservative declared chart, not the intrinsic previous/pole rank-open.
The theorem is the intersection of the echelons' actual domains of
definition with whatever principal open V83 later emits, and it is
silent on every rank-drop fibre.**

Both producers invert Dual-GE leading coefficients.  The conormal /
kernel denominators frozen here are the unit `(1, [])`.  On a degree-zero
unit, `factors_only_allowed` is vacuous and
`denominator_radical_subset_U_H_B3=true` does not identify the 38 pivot
minors.  Those minors are not listed in this freeze.  V83 is not an
artifact of this case (no V83 table, open, or review is charged).  The
producer's conservative declaration is therefore the only localization
this package may claim, and only as a declared outer bound:

```text
theorem domain ⊆ D(U*(C-3U^2)*B3) ∩ (V83 principal open, when emitted)
                         ∩ {points where the frozen 38/94 echelon is defined}.
```

Anything V83 later lists as a rank-drop factor is raw-fibre debt and is
outside this theorem.  Identifying the declared chart with “the”
intrinsic FIRST or previous/pole rank-38 open would be a scope
violation.  The two Dual presentations print the same allowed-factor
alphabet `{U, H=C-3U^2, B3}` and the same unit leftover denominator, so
they do not introduce a second chart.

**6. [Confirmed] Previous/pole is a consistent first-order target on
`Q`.  The current system is already inconsistent at the undeformed base
and is not computed in this freeze.  The theorem licenses
`Sym^2(Q_prev) -> C_prev` and proves no quadratic vanishing, family, or
persistence.**

V82Q `full_family_parameterization=true` plus empty 22-column conormal,
and V82P3 `dependent_count=0` plus empty 1-column conormals, are the
consistency of `L_prev|Q = 0`.  Current is the next composition in
`run_staged`: `compose_forms` of the 56 previous-free parameters into
`qd.compile_current`, which the source itself asserts is
base-inconsistent (`assert base_inconsistent`, P12 unit remainder).
That current block is not in this freeze.  The already-reviewed V78 P12
remainder `-k/50` is a unit on the same undeformed base; V82Q prints
`dual_base_ideal_already_unit=true` at start.  Those facts distinguish
the targets.  They are not a current-stage theorem of this package.

Every V82P3 lane prints
`no_current_second_order_family_or_TD6_claim=true`,
`previous_pole_kernel_is_not_a_current_or_nonlinear_kernel=true`,
`generic_family_killed=false`, `whole_TD6_killed=false`,
`SP2_killed=false`, `JC2_resolved=false`.  V82Q's result-use line is
`tangent_conormal_and_source_support_discriminator_only`.  A quadratic
Kuranishi matrix on `Q_prev` is licensed because the linear map vanishes
on a 24-dimensional space; its vanishing, its Fitting rank, and any
nonlinear family are not proved.

**7. [Confirmed] Manifest, freeze, and source-custody pins close on
the Stage-A harvest disclosure.  No missing load-bearing evidence was
found.  No case repair is required.**

`FREEZE.sha256` contains exactly two lines: the charged manifest pin of
`MANIFEST.sha256`, and the charged producer pin.  `MANIFEST.sha256` lists
200 paths covering `README.md`, `verify.py`, both V82Q trees (launch,
stdout, empty stderr, `source_check.stdout`, `source.tar.gz`, four
FIRST/PREVIOUS_POLE outputs), and both V82P3 trees (registration,
`source.tar.gz`, extracted source, four lanes of rc/stdout/stderr/
wrapper/RESULTS/tables/controls).  Recorded content SHAs match across
hosts for every load-bearing table, kernel, and source archive:

```text
V82Q table    b1b1f698…   (r6d = Box03, FIRST = PREVIOUS_POLE)
V82Q kernel   ef4d3be8…   (r6d = Box03, FIRST = PREVIOUS_POLE)
V82Q source   cc7717b46d… (r6d = Box03 = V78B archive pin)
V82P3 table   2c0e79ec…   (all eight actual and control files)
V82P3 source  1a23ceca70… (r6d = Box03)
```

V82Q `source_check.stdout` lists the V78B payload members as `OK` and
stops at `./run_v78b.sh: OK`; it does not include V82/V82P files, which
V82Q does not execute.  V82P3 stdout lists the outer `SOURCE.sha256`
members as `OK` in the same order as the pinned list, including
`V82P3_TYPED_COMPOSITION_ERRATUM.md` (`ed53eeea…`) and V82S2 parent
`a344d3c211…`.  `RESULTS.sha256` on each P3 lane pins that lane's
stdout, stderr, and rc against the AWS absolute paths.

Disclosed, not defective: V82Q has no process `rc` because current was
still running; the previous/pole files are complete and dual-host
identical.  Raw previous/pole columns are stdout-pinned, not frozen
TSVs (same custody shape as the CONFIRMED V82S2 first-stage raw
columns).  `verify.py` is a string/custody checker, not a proof; it
was not executed.  Unlisted `__pycache__` members exist under extracted
source trees and are not in `MANIFEST.sha256`; they are not executed
and are not load-bearing.

Producer wording that was *not* used as evidence: `PRODUCER-EXACT`,
`DUAL AWS`, shard `PASS` lines, and `TD6-V82-STAGE-A-QPREV-DIM24-VERIFY PASS`.

No smallest required repair of this freeze.  The separate V83 rank-open
atlas is missing from this package by design (Finding 5), not as a
hole in the Stage-A linear statement.

---

## Exact theorem scope

On the common symbolic-center source presentation over `K = E(C,V,U)`,
on the common localization where the frozen transport, FIRST, and
previous/pole Dual-GE echelons are defined, intersected with
`D(U*(C-3U^2)*B3)` and with V83's explicit principal open when that
open is emitted, let

```text
Q = span_K(q2..q14, q16..q24, d10, d15).
```

The previous/pole linear compatibility map `L_prev` vanishes on this
basis.  Consequently

```text
Q_prev := ker(L_prev|Q) = Q,     dim_K Q_prev = 24.
```

This is a first-order, fixed-presentation, square-zero source-incidence
statement.  It licenses computation of the quadratic previous/pole
Kuranishi map `Sym^2(Q_prev) -> C_prev` on the same open.  It does not
assert that this quadratic map vanishes, that a nonlinear family
exists, that current-stage leftover vanishes, that TD6, SP-2, or JC2 is
resolved, or that anything holds on a V83 rank-drop fibre.

---

## Falsifiers

Any one of the following would retract the theorem:

1. A nonempty previous/pole conormal coordinate on any of the 24 axes,
   or a kernel row whose support is not a single licensed axis with
   unit coefficient.
2. `previous_pole` rank other than `38/94`, or FIRST rank other than
   `38/132`, on either presentation.
3. Dual-host disagreement of V82Q table/kernel bytes, of V82P3 table
   bytes, or of the printed raw-column SHAs `86e61fc8…` / `90e13af1…`.
4. A V82P3 lane with `rc != 0`, failed `AxisJet` preflight, failed
   empty-table `ONE` control, empty raw previous/pole column, or
   nonunit leftover denominator.
5. Appearance of `q15`, `d5`, `d17`, or any dead axis other than
   `d10,d15` in the claimed kernel.
6. A first-order mixed q-dead term that survives square-zero Dual
   arithmetic, or a demonstration that Dual-GE base pivots differ
   between the EJet and AxisJet presentations.
7. A leftover denominator factor, or a V83 pivot/minor factor, that is
   then treated as inverted rather than as rank-drop debt.
8. Any reading of this freeze as a current-stage, quadratic-persistence,
   family, full-TD6, SP-2, or JC2 theorem.

---

## Smallest next proof-grade experiment

Exact previous/pole quadratic Kuranishi map
`Sym^2(Q_prev) -> C_prev` on this 24-space, on the same symbolic-center
presentation and the same conservative open, Dual-linear in the typed
`EJet`/`AxisJet` source already frozen here, with dual-host empty-or-
explicit tables, unit-or-allowed denominators, original-row pivot
replay, and a hard firewall against current-stage mixing.  V83's
explicit principal open is a parallel localization audit, not a
substitute for that quadratic map.

---

CONFIRMED
