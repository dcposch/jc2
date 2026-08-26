# Hostile review: TD6 V81C dead-transport rank

Inspection only of the charged producer case and producer report.  No
producer execution, no `verify.py` run, no CAS, no solver, no Lean, and
no Flint.  Stored `PASS` / producer-verdict strings were ignored as
proof.  Frozen file bytes were hashed with Python `hashlib.sha256` and
compared by exact equality.  The portable archive
`archives/td6-v81c-generic-dead-transport-shards-source-20260826.tar.gz`
was listed and selected members were read by `tarfile.extractfile`; it
was not unpacked into the tree.  The nine-by-nine sentinel minor was
reconstructed from the eleven frozen generic tables independently of
`verify.py`.  Every load-bearing equality below was re-checked outside
that checker.

Charged surfaces:

- `cases/td6_c1_c2_c3_dead_transport_rank_v81c_aws_20260826/`
- `xmodel/td6-c1-c2-c3-dead-transport-rank-v81c-producer-20260826.md`

Consumed, not re-proved:

- V78B/V78C hostile review V3 (frozen copy
  `dependencies/V78BC_REVIEW.md`, byte-identical to
  `xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md`)
- V78B r6d stdout/rc (`dependencies/V78B_R6D.stdout`,
  `dependencies/V78B_R6D.rc`)
- V80B point tables, used only as specialization-hash controls

The seven load-bearing charges are re-audited from extracted source,
the pinned first-band / all-q parent modules named by the source
manifest, both AWS raw outputs, the eleven generic and eleven point
tables on each host, and the frozen V78 dependency.

---

## Findings

**1. [Confirmed] Exact source typing is the eleven pole-chart
coefficients `d6..d16` in**

```text
x = r^{-25},
y = r^5 + sum_{m=6}^{16} d_m r^m + zeta r^{17},
```

**differentiated at vanishing dead stretch, one level per shard, by
`j * binom(j-1,k) r^{m-5+12k}`, at the symbolic A3 center `(C,V,U)`
with the frozen F1 normalization `p=t^{15}`, `q=t+t^{25}`.**

The unique mathematical producer is

```text
payload/jc2/cases/td6_c1_c2_c3_q_dead_joint_transport_v81c_20260826/replay.py
```

SHA `e1d4c69b…`, pinned in `SOURCE.sha256`.  `main()` refuses any
`TD6_DEAD_LEVEL` outside `{6,...,16}` and prints `dead_axis=dN` with
ring `E(C,V,U)[eps_dN]/eps_dN^2`.  Zeta is the already present pole
modulus, not a twelfth dead-stretch coordinate.  No `d5` and no `d17`
appear.  `q15` is printed as target-shear gauge and is excluded from
the 33-axis inventory; `assert "q15" not in AXES`.

`dead_derivative_rows` walks the frozen rectangles `(f: i<=15, j<=60)`
and `(g: i<=25, j<=100)` and, for each monomial `x^i y^j` and each
zeta degree `k < j`, installs

```text
coefficient = j * C(j-1, k),
exponent    = -25 i + 5 j + (LEVEL - 5) + 12 k
```

with f-cutoff `-3` and g-cutoff `-5`.  That is the first derivative of
`x^i y^j` in `d_m` at vanishing dead stretch: the undeformed pole chart
in the pinned first-band parent (`c55e2136…`) is `x=r^{-25}`,
`y=r^5+zeta r^{17}`, and

```text
d/d(d_m) y^j |_{d=0}
  = j (r^5 + zeta r^{17})^{j-1} r^m
  = j sum_k C(j-1,k) r^{5(j-1-k)+17k+m} zeta^k,
```

which is `j C(j-1,k) r^{m-5+12k}` times the undeformed `r^{5j}`
factor.  The undeformed F0 rows in the same parent use `C(j,k)` and
`k=0..j`; the derivative correctly uses `j C(j-1,k)` and `k=0..j-1`.
The in-source positive control is the `x^2 y^3` slot
`variable = 2*61+3`, requiring coefficient `3` at `k=0` and `6` at
`k=1`; the wrong-shift key `LEVEL-4` is required not to carry `3`.

F1 is the frozen first-band pair: `F1_F_PATTERN = P_REDUCED^3`,
`F1_G_PATTERN = P_REDUCED^5`, f-transport `(15,60,3)` from `{15: 1}`,
g-transport `(25,100,5)` from `{1: 1, 25: 1}`.  The x-chart is
`x = C s + V s^2 + U s^3 + t s^4`.  `build_base_transport` assigns

```text
r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))
```

clears `_X_POWER_CACHE`, and asserts this center is not `(1,1,1)`
before and after `factor_transport`.  Every one of the 22 stdouts
prints

```text
symbolic_center_asserted_before_transport=true
symbolic_center_asserted_after_transport=true
symbolic_center_asserted_after_dead_column=true
base_beta=0;base_dead_stretch=0
scope=generic_center_single_dead_axis_transport_source_incidence_only
```

This is the generic A3 center, not the V80B point.  The first-band
module default `CENTER = (Q(1),Q(1),Q(1))` is overwritten before any
transport row is built.

**2. [Confirmed] All 3,470 original transport pivot rows replay on
every shard; the dead-derivative exponent shift is the formula of
Finding 1; the matrix-derivative omission control is a real negative
control, including on `d10` and `d15`; and every V80B point table is
reproduced by exact byte identity, not merely by a printed hash.**

After echelon differentiation, `dead_lift` rebuilds every pivot key of
the frozen rank-3470 transport as `A0 x' + A'_LEVEL x0 = 0` and
asserts the reconstructed form is `ZERO_FORM`.  It then asserts
`replay_count == len(pivots)` before printing.  All 22 stdout files
contain

```text
transport_rank=3470/3602;free=132
dN_original_3470_pivot_rows_replayed=true
```

The omission control separately counts rows of `A'_LEVEL` with
`A' x0 != 0` and requires the count to be positive, so a producer that
set `x'=0` and skipped `A'` cannot pass by treating a matrix-changing
direction as RHS-only or as the zero matrix.  Frozen counts are
exactly the V80B `omission_failures` vector, identical on both hosts:

| level | omission_failures | compatibility_forms | generic entries |
|---|---:|---:|---:|
| d6 | 39 | 39 | 1397 |
| d7 | 36 | 36 | 1270 |
| d8 | 32 | 32 | 1160 |
| d9 | 29 | 29 | 1008 |
| d10 | 26 | 0 | 0 |
| d11 | 23 | 23 | 736 |
| d12 | 20 | 20 | 618 |
| d13 | 16 | 16 | 515 |
| d14 | 13 | 13 | 374 |
| d15 | 10 | 0 | 0 |
| d16 | 7 | 7 | 115 |

Those numbers are positive on `d10` and `d15`, so the two empty
compatibility tables are not `A'=0`.  Derivative-only keys absent from
the base echelon are retained.  No emitted table row has kind
`base-dependent`; every nonempty table is `kind=derivative-only`.

V80B specialization is a hash-and-byte control, not a second generic
computation.  `point_table` evaluates each generic `E3` form at
`(C,V,U)=(1,1,1)` and asserts the SHA against the frozen V80B table.
Independently, each V81C `POINT_CVU111_DEAD_DN_TRANSPORT_COMPATIBILITY.tsv`
is byte-identical to the corresponding V80B
`DEAD_DN_TRANSPORT_COMPATIBILITY.tsv` on r6d for all eleven levels.
Stdout `V80B_selected_point_table_hash_reproduced=true` therefore
matches the frozen V80B bytes, not just an internal dictionary.

Generic and point tables differ on the nine nonzero columns (generic
d6 has 1397 entries, the specialized point table 1396): specialization
may kill a generic term.  Empty `d10` and `d15` are invariant under
specialization.

**3. [Confirmed] Dual-host byte custody is closed on all twenty-two
runs, and the `d10`, `d15` generic and point tables are the exact
empty header.**

`MANIFEST.sha256` has 165 paths.  Every listed file exists; every
on-disk case file is listed; all 165 content digests match.  Archive
SHA `acc26126…` matches README, `verify.py`, and the tarball bytes.
Outer `SOURCE.sha256` has 55 members; every AWS stdout prints those 55
paths as `OK` in the same order; every listed member hashes to its
pin.  Parent pins are the reviewed ones: all-q repaired `7e5ade2b…`
(V78 theorem file, imported but not executed as V78), first-band
`c55e2136…`, jet-orbit `fb138b0f…`, V32 `dcc7003d…`.

All 22 `rc` files are the single byte-string `0` (shared SHA
`9a271f2a…`).  All 22 stdout files end on

```text
TD6-A3-GENERIC-DEAD-TRANSPORT-V81C-SHARD PASS
```

Hosts are distinct: r6d `ip-172-30-0-45`, Box03 `ip-172-30-0-249`.
Twenty-two PIDs and twenty-two tags
`td6_v81c_{r6d,box03}_dN_20260826T0225Z` are unique.
`/usr/bin/time -v` on stderr records `timeout 14400 bash run_v81c.sh`
and `Exit status: 0` (wall times about six to seven minutes).
`python_flint_version=0.9.0` is printed before the source check.
Launch metadata is `cap_kib=8388608`, `timeout_seconds=14400`.

For each of the eleven levels, both generic tables and both point
tables are byte-identical r6d versus Box03.  The common generic SHAs
are the `verify.py` / MANIFEST pins.

`d10` and `d15`, generic and point, both hosts, are the 38-byte header

```text
kind	key	coordinate	coefficient_exact\n
```

SHA `a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df`.
That is the SHA of those exact header bytes.  Compatibility forms `0`,
entries `0`.  Exact vanishing of leftover incidence, not vanishing of
`A'` (Finding 2).

Independence of the two hosts is the hostname/PID/path difference.
Mathematical equality is the identical table bytes.

**4. [Confirmed] The nine-row minor on original F0 source keys
`('f','F0',m-20,0)` for `m=6,7,8,9,11,12,13,14,16`, in that order, is
lower-triangular with identical nonzero diagonal; dead rank is
exactly nine with kernel `span(d10,d15)`.**

Independently assembled from the r6d generic tables (Box03 is
byte-identical), the constant-coordinate slice of those nine keys
against those nine columns is

```text
        d6   d7   d8   d9   d11  d12  d13  d14  d16
d6      D    .    .    .    .    .    .    .    .
d7      .    D    .    .    .    .    .    .    .
d8      .    .    D    .    .    .    .    .    .
d9      .    .    .    D    .    .    .    .    .
d11     *    .    .    .    D    .    .    .    .
d12     .    *    .    .    .    D    .    .    .
d13     .    .    *    .    .    .    D    .    .
d14     .    .    .    *    .    .    .    D    .
d16     *    .    .    .    *    .    .    .    D
```

`D` is the same 18-coordinate serializer

```text
(('0','1'), ('0','1'), ('0','1'), ('0','1'), ('0','1'),
 ('0','1'), ('15625/3','1'), ('0','1'), ..., ('0','1'))
```

one nonzero `E3` slot `15625/3 = 5^6/3` over denominator `1`.  Every
strictly upper-triangular slot is absent, including every
`p`-coordinate of those keys: later columns do not meet earlier
sentinel keys at all.  The six starred lower-triangular slots are
different, parameter-rich forms (30 `p`-coordinates on each), not a
second copy of `D`.  The leading `4 x 4` block is actually diagonal.
A diagonal matrix is lower-triangular; the producer’s
lower-triangular claim is therefore correct, and is the orientation
that makes the deleted-`(d10,d15)` order a triangular minor.

Those nine keys are original pole-chart F0 source keys.  Every table
row that carries them is `kind=derivative-only`: they are not among
the undifferentiated 3,470 pivot rows.  Linear independence does not
require them to have been base-transport rows.  Projecting the eleven
columns onto these nine parameter-free constant coordinates already
gives an invertible `9 x 9` matrix over `E(C,V,U)`, determinant
`(15625/3)^9 ≠ 0`.  Combined with the two identically zero columns
`d10`, `d15`, the dead block has rank exactly nine and kernel exactly
`span(d10,d15)` in the leftover-form space (constants and the 132
transport parameters, at generic `p`).

`verify.py` checks the same diagonal and the empty upper triangle; it
does not need the lower stars.  The reconstruction above does not
depend on it.

**5. [Confirmed] V78 is consumed only as the already reviewed fact
that the 22 licensed q-transport compatibility columns are zero.
V81C does not recompute them.**

Every V81C stdout prints `q_transport_columns_consumed=false`.
`main()` calls `propagate_base` / `global_base_forms` / `dead_lift` /
`write_generic_axis` / `point_table`.  It does not call `propagate_q`,
`global_q_forms`, `insert_dead_axis`, `rref`, or `write_joint`.  The
q-injection in unused `source_jet` is the V78 pattern
`('g','X',0,e) ↦ eps_{q e}` and is not on the executed path.

The frozen V78B r6d stdout (SHA `118dcb50…`, the same pin recorded in
the V78 V3 review) contains

```text
transport_rank=3470/3602
transport_active_q_columns=2,3,...,14,16,...,24
transport_all_q_source_keys_exact_and_singleton=true
transport_matrix_all_q_derivative_zero=true
transport_rhs_all_q_derivatives_retained=true
FIRST_conormal_rank=0/22
TD6-A3-ALL-Q-VECTOR-AD-P12 PASS
```

`dependencies/V78B_R6D.rc` is `0\n`.  The frozen review copy SHA
`a3599e65…` is byte-identical to
`xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md` and ends on
the standalone line `CONFIRMED`.  That review already established:
inventory `{q2,...,q14,q16,...,q24}` with `q15` gauge; transport
`3470/3602` at the same F1 / pole / symbolic center; `A'_q = 0` with
RHS q-derivatives retained; transport leftover empty
(`assert not compatibility` in V78 `propagate_jet`); first-conormal
the zero map of rank `0/22`.  V81C imports the same all-q parent
`7e5ade2b…` for `Rat3` / `E3` / `(C,V,U)` / `tri` / `r` and does not
run that parent’s `main()`.

V81C therefore does not claim a new q-column computation.  The
first-conormal vanishing is stronger than the transport-stage fact
actually used below; this review uses only the transport-stage zero
q-columns, which is what the producer states.

**6. [Confirmed] The inferred full 33-axis fraction-field transport
rank is nine, with kernel dimension 24, as a first-order concatenation
of Finding 4 with Finding 5.  It is not a one-ring V81B replay and
not a first/previous/current theorem.**

Domain is the 33 licensed source axes `q2..q14,q16..q24` plus
`d6..d16`.  At first order the mixed q-dead second derivatives are
square-zero and vanish.  The transport leftover map is the
concatenation of the 22 V78 q-columns (zero) and the 11 V81C dead
columns (rank 9, kernel `span(d10,d15)`).  Rank is nine; kernel is
the 22 q-axes plus `d10`, `d15`, dimension `33-9=24`.

This is the Jacobian column-by-column, not the unexecuted
`write_joint` path and not a 33-fold square-zero ring.  The shard
preregistration requires “the full V81B single-ring producer or a
separately reviewed exact union assembler” for joint conclusions.
The freeze assembler `verify.py` plus this review is that assembler.
Shard stdout keeps `single_axis_result_not_a_joint_kernel=true`; the
33-axis sentence lives in the freeze README / producer report /
checker, which is what this charge audits.

The leftover space is the same transport cokernel: same
`factor_transport` rank `3470/3602`, same two events, same 132 free
parameters, same F1/pole/center.  V78 leftover at transport stage is
the empty list; V81C leftover is the eleven tables.  Concatenation is
legitimate at this stage only.

**7. [Confirmed] Every advertised firewall is present as source
assertion, frozen execution trace, or consumed V78 scope.  The result
is a generic fraction-field transport source-incidence statement.**

Visible without unpacking, on all 22 traces:

```text
scope=generic_center_single_dead_axis_transport_source_incidence_only
V80B_use=specialization_control_only
q_transport_columns_consumed=false
no_joint_kernel_or_first_previous_current_or_kuranishi_claim=true
single_axis_result_not_a_joint_kernel=true
generic_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

`run_v81c.sh` refuses non-Linux and any `AWS_RUN_TAG` not matching
`td6_v81c_*`, and pins `/home/ubuntu/venvs/td6/bin/python3`.
`V81C_PREREGISTRATION.md` refuses first/previous/current, Fitting /
Kuranishi, family, TD6, SP-2, and JC2.  The producer report and case
README repeat: no denominator-cleared constructible atlas, no
first/previous/current, no nonlinear q/dead neighborhood, no family
kill, no full TD6, no SP-2, no JC2.  `verify.py` prints

```text
scope=generic_fraction_field_E(C,V,U)_transport_source_incidence_only
```

Generic-table denominators that actually occur are `{1, U, C-3U^2}`.
The sentinel diagonal has denominator `1`.  The fraction-field rank
does not need a constructible open.  V78’s `D(U(C-3U^2)B3)` is
inherited only for the consumed zero q-columns; at the generic point
of `Spec Q[C,V,U]` that divisor is already avoided.  V81A deployment
and operator-dispatch errata are retained as negative custody: neither
emitted a table.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. `run_v81c.sh` still says `REFUSED: V81A is AWS/Linux only`.  The
   tag gate is the correct `td6_v81c_*` test.  The refuse string is
   copy-paste.

2. The producer file is named `q_dead_joint_transport_v81c` and still
   contains unused `propagate_q`, `insert_dead_axis`, `rref`, and
   `write_joint`.  Executed `main()` is one dead axis.  A reader of
   the filename alone could think V81C already ran the 33-axis ring.
   The printed banners already contradict that; the unused functions
   should not be cited as executed evidence.

3. The nine sentinel keys are original F0 source keys of kind
   `derivative-only`, not undifferentiated transport rows.  “Original
   source” is accurate.  “Original row” in the sense of the 3,470
   pivot rows is not.  The triangular witness does not need the
   stronger reading.

4. The minor is sparse lower-triangular, and the leading `4 x 4` is
   diagonal.  Saying “lower-triangular” is correct; saying it as if
   every below-diagonal slot were filled would not be.

5. Stdout never prints `aws_platform=Linux`.  The wrapper refuses
   non-Linux.  A printed platform marker would match V78/V80B traces.

6. The tarball contains AppleDouble `._*` members and an unlisted
   `payload/SOURCE.sha256`.  Neither is in the outer 55-line
   `SOURCE.sha256`; neither is executed.  Harvest `r6d.sha256` /
   `box03.sha256` still carry `/tmp/td6-v81c-harvest-…` paths.

---

## Independent discharge

- **Dual-host equality** of all twenty-two generic and point tables is
  discharged by identical file bytes, identical MANIFEST SHAs, and
  identical stdout `generic_sha` / `point_sha` markers.
- **Empty `d10`,`d15`** is discharged by the 38-byte header and SHA
  `a30f8597…` on four files per host pair.
- **V80B specialization** is discharged by byte identity with the
  frozen V80B tables, not by the printed boolean.
- **Nine-by-nine minor** is discharged by direct reads of the nine
  generic tables, independently of `verify.py`.
- **V78 zero q-columns** are discharged by the frozen CONFIRMED V3
  review plus the pinned V78B stdout, not by any V81C q-propagation.
- **Exit-0 / PASS** is discharged by 22 `rc` files equal to `0` and 22
  final stdout lines.  `PASS` was not treated as an algebraic proof.

---

## Strongest exact theorem that survives

Over the generic symbolic-center field `E(C,V,U)`, at the fixed
source-typed A3 / F1 slice `p=t^{15}`, `q=t+t^{25}`, in the pole chart
`x=r^{-25}`, `y=r^5+sum_{m=6}^{16} d_m r^m + zeta r^{17}`, the eleven
pure-axis transport derivatives of the frozen rank-3470 / 132-free
echelon, formed by `j binom(j-1,k) r^{m-5+12k}` and replayed on all
3,470 original pivot rows, have the following exact generic leftover
tables, identical on two AWS hosts: `d10` and `d15` are the empty
table; the other nine columns admit a lower-triangular minor on the
original F0 keys `('f','F0',m-20,0)` for
`m=6,7,8,9,11,12,13,14,16` whose diagonal is the nonzero `E3` element
with coordinate `15625/3`.  Dead rank is exactly nine and the dead
kernel is `span(d10,d15)`.  `A'` is not the zero matrix on any of the
eleven levels.  Consuming the separately hostile-reviewed V78 fact
that the 22 licensed q-transport columns are zero, the concatenated
33-axis transport source-incidence map has rank nine and kernel
dimension 24.  This is a fraction-field transport source-incidence
theorem.  It is not a one-ring 33-fold square-zero computation, not a
denominator-cleared constructible atlas, not first/previous/current
compatibility, and not a neighborhood, family, TD6, SP-2, or JC2
theorem.

---

CONFIRMED
