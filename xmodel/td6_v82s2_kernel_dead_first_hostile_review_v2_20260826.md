# Hostile review V2: TD6 V82S2 kernel-dead first gate and the 24-direction first kernel

Inspection only of the charged producer case, producer report, frozen V1
review charge, and the two consumed hostile reviews.  No producer
execution, no `verify.py` run, no CAS, no solver, no Lean, and no Flint.
Stored `PASS` / producer-verdict strings were ignored as proof.  Frozen
file bytes were hashed with Python `hashlib.sha256` and compared by exact
equality.  The portable archive
`archives/td6-v82s2-kernel-dead-first-shards-source-20260826.tar.gz` was
listed and selected members were read by `tarfile.extractfile`; it was
not unpacked into the tree.  Every load-bearing equality below was
re-checked outside the case checker.

Charged surfaces and immutable pins (all matched on disk):

- `cases/td6_c1_c2_c3_kernel_dead_first_v82s2_aws_20260826/FREEZE.sha256`,
  file SHA `f683d403d4b3fcdf67135834cad407b530602c6b49c60ff4ad952d1cfaada5f3`
- `xmodel/td6-c1-c2-c3-kernel-dead-first-v82s2-producer-20260826.md`,
  SHA `e18147d25c8be32f6db71eeed76be1dc50aa94ec44908ce1d9564859d7ecd757`
- frozen V1 review charge
  `xmodel/td6-v82s2-kernel-dead-first-hostile-review-prompt-20260826.md`,
  SHA `494d36a5717f0c36b18627cf12380943284384e83a2ff1b64e57055347b1bf0b`

Consumed, not re-proved:

- V81C review `xmodel/td6_v81c_dead_transport_rank_hostile_review_20260826.md`,
  SHA `dfac352887f645a9dd1f03a32b4701372b32de3a445bfd496c74109e64381ebb`,
  standalone verdict `CONFIRMED`
- V78 review `xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md`,
  SHA `a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861`,
  standalone verdict `CONFIRMED`

The seven load-bearing charges are re-audited from extracted source, the
four AWS raw outputs, the eight header-only tables, the pinned V81B/V82
parents, and the two consumed reviews.

---

## Findings

**1. [Confirmed] Exact source typing is the single dead-stretch
coefficient `d_m` for `m in {10,15}` in the pole chart**

```text
x = r^{-25},
y = r^5 + d_m r^m + zeta r^{17},
```

**differentiated at vanishing dead stretch by `j * binom(j-1,k) r^{m-5+12k}`,
then compiled through the first X-band with `qd.Dual = AxisJet` at the
symbolic A3 center `(C,V,U)`.**

The unique mathematical producer is

```text
payload/jc2/cases/td6_c1_c2_c3_kernel_dead_first_shard_v82s_20260826/replay.py
```

SHA `a344d3c211094315fa6f079e1292676ca78e8f1fbcbdfa7078a52e9e8969db90`,
pinned in the outer `SOURCE.sha256` and imported only after hash-checking
the V82 parent `537219eb8d4c4439697b537542600cc1f95851e8eda2175a9fee3bbde7c508e5`.
That parent hash-checks V81B
`cc23970873283f02e8c352006c95c393de4ad3f1a9bbf57beab6db91e79b79ad`.
`main()` refuses any `TD6_DEAD_LEVEL` outside `{10,15}` and prints
`dead_axis=dN`.  Zeta is the already present pole modulus.  No `d5`, no
`d17`, and no licensed q-jet is inserted into the first-band Dual.

`AxisJet` is defined in V81B and is byte-identical to the V81C class
(3,315 bytes).  It is `E(C,V,U)` plus a square-zero derivative dictionary
keyed by the 33 licensed axis names, with `assert axis in AXES` on
construction.  Ancestry of the Dual used at first stage is exactly

```text
V82S2 shard  --imports-->  V82  --imports-->  V81B.AxisJet
                         Dual = AxisJet
                         S,D,L,A = AxisJet(E3(field))
                         Q_PRIME = {0: AxisJet(1), 24: AxisJet(25)}
                         B = AxisJet()   # no q2
```

`insert_axis` is the only place a dead derivative is stored: each
transport parameter becomes `AxisJet(base, {dN: d_row})`.  First-band
compilation is the pinned jet-orbit `first_band_polynomials` /
`pack("X-2", ...)` with `qd.Dual` rebound to that class.  The Dual
Leibniz law is the same as V78's `EJet` (value/derivative product rule,
square-zero inverse, `__bool__` on value or derivatives).  V78 keys
derivatives by q-exponent; V82S2 keys them by axis name.  That is a
labeling difference, not a different first-order calculus.

`build_base_transport` assigns `r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))`,
clears `_X_POWER_CACHE`, and asserts this center is not `(1,1,1)` before
and after `factor_transport`.  The first-band parent default
`CENTER = (Q(1), Q(1), Q(1))` is overwritten before any transport row is
built.  The x-chart is therefore `x = C s + V s^2 + U s^3 + t s^4`.
F1 is the frozen first-band pair: `F1_F_PATTERN = P_REDUCED^3`,
`F1_G_PATTERN = P_REDUCED^5`, f-transport `(15,60,3)` from `{15: 1}`,
g-transport `(25,100,5)` from `{1: 1, 25: 1}`.  Pole chart in that
parent is `x=r^{-25}`, `y=r^5+zeta r^{17}`.  Every one of the four
stdouts prints

```text
source_center=(C,V,U);symbolic=true
base_q=t+t^25;base_dead_stretch=0
symbolic_center_asserted_before_transport=true
symbolic_center_asserted_after_transport=true
```

Parent pins used on the executed path, all present in outer
`SOURCE.sha256` and all hashing to those pins inside the tarball:

| parent | SHA256 prefix | role |
|---|---|---|
| V82 | `537219eb…` | first-band Dual GE, `build_sections`, `column_digest` |
| V81B | `cc239708…` | `AxisJet`, transport, dead derivative/lift |
| all-q repaired (V78 theorem file) | `7e5ade2b…` | `Rat3`/`E3`/`(C,V,U)`/`tri`/`qd` |
| first-band | `c55e2136…` | pole/F1/x-chart |
| jet-orbit | `fb138b0f…` | `first_band_polynomials` / `pack` |
| V32 | `dcc7003d…` | imported by all-q, not executed as V32 |

V81C's unique producer `e1d4c69b…` is not this file.  The six functions
V82S2 actually calls from V81B — `dead_derivative_rows`, `dead_lift`,
`build_base_transport`, `base_form`, `propagate_q`, `global_q_forms` —
are byte-identical to the corresponding V81C functions, and the
`AxisJet` class is byte-identical as well.  The V81B filename is
ancestry, not a second dead-lift.

**2. [Confirmed] All 3,470 original transport pivot rows replay on
every shard; the dead-derivative exponent shift is the formula of
Finding 1; the matrix-derivative omission control is a real negative
control on both `d10` and `d15`.**

After echelon differentiation, `dead_lift` immediately strips q-jets by
`base_forms = [base_form(form) for form in q_forms]`, so calling
`propagate_q` / `global_q_forms` rather than V81C's `propagate_base` /
`global_base_forms` does not change the dead column.  It then rebuilds
every pivot key of the frozen rank-3470 transport as
`A0 x' + A'_LEVEL x0 = 0` and asserts the reconstructed form is
`ZERO_FORM`.  It asserts `replay_count == len(pivots)` before
returning.  `build_base_transport` has already asserted
`len(pivots) == 3470` and `len(pivots) + 132 == nf + ng`.  All four
stdout files contain

```text
transport_rank=3470/3602;free=132
transport_event_count=2
transport_axis_compatibility_exact_zero=true
transport_original_3470_pivot_rows_replayed=true
```

The printed replay marker is unconditional in the shard, but it is
emitted only after `dead_lift`'s `assert replay_count == len(pivots)`
and `assert not compatibility`.  A producer that skipped the 3,470-row
reconstruction would have exited nonzero.

The omission control separately counts rows of `A'_LEVEL` with
`A' x0 != 0` and requires the count to be positive, so a producer that
set `x'=0` and skipped `A'` cannot pass by treating a matrix-changing
direction as RHS-only or as the zero matrix.  Frozen counts match the
V81C `omission_failures` / derivative-row / term vector on the same two
levels, independently of V81C table bytes:

| level | derivative_rows | terms | omission_failures | compatibility |
|---|---:|---:|---:|---:|
| d10 | 3093 | 24173 | 26 | 0 |
| d15 | 3035 | 23571 | 10 | 0 |

Those omission counts are positive, so the two empty transport leftover
tables are not `A'=0`.  The in-source positive control on the `x^2 y^3`
slot `variable = 2*61+3` still requires coefficient `3` at `k=0` and
`6` at `k=1`, and the wrong-shift key `LEVEL-4` is required not to
carry `3`.  Derivative-only keys absent from the base echelon are
retained by `dead_lift` and then required to vanish as forms; they do.

**3. [Confirmed] Both raw first-source columns are genuinely present;
the omission-zero negative control is real; first rank is `38/132`
with no dependent row; every first-stage pivot source combination is
replayed inside Dual GE.**

Dead source enters the first X-band only through the transported
sections.  `configure_base_qd` installs no dead `Q_PRIME` term and
asserts `not qd.B.derivatives`.  `column_digest` serializes every
nonzero `AxisJet.derivatives[dN]` entry of the packed first rows.
Positive counts and SHA256 values are identical on both hosts:

| axis | raw entries | raw SHA256 | omitted entries | omitted SHA256 |
|---|---:|---|---:|---|
| d10 | 1108 | `e9c830bf3bc0abbc6a91b1e38a227ac0ae61b40bbeabf4e233dce62450f730f7` | 0 | `e3b0c442…` (empty bytes) |
| d15 | 739 | `4ea40ca645ec2dd523db2b85ab67cdf1b3c82fe28eb610a5220a44deedbb66ab` | 0 | `e3b0c442…` |

The omission control compiles the same first-band polynomials from
`base_forms` (no dead jet) and requires `positive_count > 0`,
`omitted_count == 0`, and distinct digests.  A producer that never
injected `dN` into the sections would see a zero raw column and fail.
The empty omitted digest is the SHA256 of the empty byte string, which
is exactly what `column_digest` returns for a column with no lines.

`parameterize(132, first_rows)` is V82 `solve_cert` Dual GE: pivots are
chosen only on nonzero base values; already-pivoted columns, including
derivative-only coefficients, are reduced (the `lambda' A` term).
Every dependent row and every surviving pivot reconstructs its
`AxisJet` polynomial from original packed source rows and asserts
equality.  The shard then asserts

```text
len(first_pivots) == 38 and len(free94) == 94
```

and prints `first_rank=38/132`, `first_dependent_count=0`.  That is the
same undeformed first echelon as hostile-reviewed V78
(`FIRST_conormal_rank=0/22` over the same `38/132` base).  With no
dependent rows, `dependent_coordinates` is empty, so the one-axis
conormal has rank `0/1`.  The printed marker
`all_first_pivot_source_combinations_replayed=true` is unconditional in
the shard, but it is reached only if those 38 pivot-combination asserts
succeeded.  A skipped replay is a nonzero exit, not a silent empty
table.

The raw-column SHA256 values exist only in pinned stdout, not as frozen
TSV files.  Dual-host identity of those SHA256 strings is the inspectable
presence evidence.  Re-deriving the 1,108 and 739 entries would be
producer CAS, which this charge forbids.

**4. [Confirmed] All eight actual and synthetic tables are the same
header-only byte string; the `tri.ONE` reporter correction is in the
executed empty-table path; the empty-table positive control is a
separate execution; the denominator is the unit `1`; dual-host
normalized stdouts are byte-identical per axis.**

`write_table` is

```text
assert v81.tri.ONE == v81.tri.CTX.constant(1)
denominator = allq.denominator_for(values) if values else v81.tri.ONE
```

The all-q parent still has the defective empty branch
`tri.CTX(1)` inside `denominator_for`.  V82S2 never takes it: both the
synthetic control (`coordinates={}`) and the actual table
(`nonzero==0`) use `v81.tri.ONE`.  The pinned trivariate module defines

```text
ZERO, ONE = CTX.constant(0), CTX.constant(1)
```

so the runtime assert is the identification the V82S reporter lacked.
`V82S2_REPORTER_ERRATUM.md` (SHA `f0830be9…`, listed in
`SOURCE.sha256`) records that V82S reached the empty coordinate
dictionary and then died while constructing the unit denominator; V82S2
reruns the complete algebra and treats V82S stdout as
reporter-negative evidence only.  No V82S stdout is in this freeze.

The synthetic control is executed first, into
`empty_table_control/`, before transport, with `assert control_nonzero == 0`
and `assert control_denominator == v81.tri.ONE`.  The actual table is
written later, after Dual GE, with the same two asserts plus
`path.read_text() ==` the header.  All eight frozen files are exactly
the 57-byte string

```text
key\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact\n
```

SHA256 `68b4a3a151d2eb15e04b6bb1b0bb6e5656423289e4dca1260844476105ea6692`.
That is emptiness of leftover first-stage incidence, not emptiness of
the raw column (Finding 3).  Printed denominator state on all four
lanes is `first_axis_denominator_factor=(1, [])`.  The accompanying
`first_axis_denominator_radical_subset_U_H_B3=true` is vacuous on a
degree-zero unit; `factors_only_allowed` accepts degree zero.

After replacing only hostname, registered run tag, and absolute run
root, the two host stdouts are byte-identical per axis.  Independently
recomputed normalized SHA256 values:

| axis | normalized stdout SHA256 |
|---|---|
| d10 | `a586c3b473f5cff53939dc5a682ab1da45aff6c3e541f148c2aa39e0fdb24c15` |
| d15 | `359df41d98d795657a08cf02b4175602d0d1e711f851da3c9c87524119397245` |

Independence of the two hosts is the hostname/PID/path difference
(r6d `ip-172-30-0-45`, Box03 `ip-172-30-0-249`).  Mathematical equality
is the identical table bytes and the identical normalized stdout.

**5. [Confirmed] Manifest, archive, and raw-output custody close on
the four lanes.  The only unpinned relevant bytes are the actual host
launcher (not the algebra) and the unfrozen raw-column TSV (Finding 3).**

`MANIFEST.sha256` has 48 paths and file SHA `7f1eefc70d50db24023f1eb79037c8ae4ff1df2a45d2a8bee30a4f34c5f0224a`,
which is the first FREEZE line.  Every listed local file exists; every
on-disk case file other than `FREEZE.sha256` and `MANIFEST.sha256`
itself is listed; all 48 content digests match, including the two
charged xmodel files.  Archive SHA
`1def8eb0d2e84451a3112c3d3679dde879706bb361267b32f2fbe4b9c6467545`
matches README, `verify.py`, both `registration.meta` files, and the
tarball bytes.  Outer `SOURCE.sha256` has 62 members; every AWS stdout
prints those 62 paths as `OK` in the same order; every listed member
hashes to its pin.  The two tar files not in that list are
`./SOURCE.sha256` itself and `./payload/SOURCE.sha256` (the older
parent payload manifest, which omits V82S/V81B/V82 because those live
in the outer list).  Neither is executed.  There are no AppleDouble
`._*` members.

All four `rc` files are the single byte-string `0\n` (shared SHA
`9a271f2a…`).  All four stdout files end on the standalone line
`TD6-A3-KERNEL-DEAD-FIRST-SHARD-V82S PASS`.  `/usr/bin/time -v` on
stderr records `timeout 14400 bash run_v82s.sh` and `Exit status: 0`
on every lane (wall times 14:50–16:03).  `python_flint_version=0.9.0`
is printed before the source check.  Four PIDs and four tags
`td6_v82s_v2_{r6d,box03}_d{10,15}_20260826T0320Z` are unique.
`run_v82s.sh` refuses non-Linux and any `AWS_RUN_TAG` not matching
`td6_v82s_*`, and pins `/home/ubuntu/venvs/td6/bin/python3`.
`RESULTS.sha256` on each lane pins that lane's stdout, stderr, and rc.

The archived `launch_v82s_host.sh` is not the script that wrote the
frozen `launch.meta`: it emits tags `td6_v82s_{host}_dN_20260826T0253Z`
and a three-field meta, while the frozen meta has `td6_v82s_v2_…T0320Z`
plus `cap_kib=8388608` and `timeout_s=14400`.  The executed algebra is
still `run_v82s.sh` as timed on stderr, with the pinned shard producer.
That launcher mismatch is unpinned orchestration, not unpinned
mathematics.  Raw first-source TSV files are likewise unpinned
(Finding 3); their SHA256 values are pinned in stdout.

`PASS` was not treated as an algebraic proof.  Exit-0 is the four `rc`
files and the four time-record exit statuses.

**6. [Confirmed] The composed implication is exact: the reviewed V81C
rank-nine transport kernel `Q22 + d10 + d15`, the reviewed V78 q-first
zero, and the V82S2 d10/d15 first zero together say that exactly those
24 transport-kernel directions survive the first gate.  This is
first-order column concatenation, not a 24-fold one-ring first-stage
run and not a previous/pole/current theorem.**

Domain of the transport statement is the 33 licensed source axes
`q2..q14,q16..q24` plus `d6..d16`.  V81C, already CONFIRMED, gives
transport leftover rank nine with kernel `span(Q22, d10, d15)` of
dimension 24, as the concatenation of V78's 22 zero q-transport columns
and V81C's 11 dead columns (rank 9, kernel `span(d10,d15)`).  V82S2
re-obtains the two zero dead transport columns with the same
derivative-row, term, and omission counts as V81C, then advances those
two columns through the first X-band.

At first order the mixed q-dead second derivatives are square-zero and
vanish.  The first-stage leftover map, restricted to the 24-dimensional
transport kernel, is the concatenation of

- V78's 22 licensed q-first columns, rank `0/22`, empty header
  `b1b1f698…`, first rank `38/132`;
- V82S2's two dead-first columns, rank `0/1` each, empty header
  `68b4a3a1…`, first rank `38/132`.

Both first-stage computations are Dual GE on `pack("X-2",
first_band_polynomials(f1,g1))` over the same undeformed 132-parameter
space, the same F1/pole/center, and isomorphic square-zero Duals.
Empty columns concatenate to the zero map of rank `0/24` on that
24-dimensional space.  Therefore every transport-kernel direction has
zero first-stage leftover, and no larger linear space is claimed:
the nine nonzero dead transport columns are outside this kernel and
are not asserted to die or survive at first stage.

V82S2 does not recompute V78's q-first columns.  After `propagate_q` it
strips q-jets by `base_form` before `insert_axis` and compiles a
one-axis Dual.  The joint 33-axis first-stage path in the V82 parent
(`cumulative_table`, `configure_qd` with all `Q_PRIME`, V82 `main`) is
not executed; V82 `main` even refuses tags that are not `td6_v82_*`
without the extra `s`, and is never called.  The V82S preregistration
requirement that single-axis results be assembled by exact row keys is
vacuous here: both actual tables have zero data rows, so the `{d10,d15}`
union is the same header.  Assembling that empty 2-column table with
V78's empty 22-column first conormal is the 24-column statement.

This is the Jacobian column-by-column, the same assembler pattern V81C
review already accepted at transport stage.  It is not a one-ring
24-fold square-zero first-stage computation.  Shard stdout keeps
`no_joint_previous_current_second_order_or_family_claim=true` and
`transport_first_kernel_is_not_a_previous_or_current_kernel=true`.
The 24-direction sentence lives in the freeze README / producer report
/ checker as a composition, which is what this V2 charge audits.  The
producer file still labels the composition producer-tier pending V81C
review; V81C is now CONFIRMED, so that caveat is stale prose, not a
remaining algebraic gap.

**7. [Confirmed] Every advertised firewall is present as source
assertion, frozen execution trace, or consumed V78/V81C scope.  The
result is a generic fraction-field square-zero transport-plus-first
source-incidence statement on fixed source-typed A3.**

Visible without unpacking, on all four traces:

```text
scope=D(U*H*B3)_generic_center_square_zero_first_source_incidence
no_joint_previous_current_second_order_or_family_claim=true
transport_first_kernel_is_not_a_previous_or_current_kernel=true
generic_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

The first-conormal denominator is the unit `1`, so the first-stage
statement is actually over the generic point of `Spec Q[C,V,U]`, not
merely on `D(U H B3)`.  V78's open `D(U(C-3U^2)B3)` is inherited only
for the consumed zero q-columns; at the generic point that divisor is
already avoided.  `verify.py` prints
`scope=generic_fraction_field_fixed_A3_square_zero_transport_first_only`;
that string was not used as proof.

Refused implications, all of which are absent from the executed path:

- previous / pole / current compatibility (V78 staged mode is not run;
  V82S2 never calls `compile_current`);
- a denominator-cleared constructible atlas (denominator is `1`);
- second-order or nonlinear q/dead neighborhood (square-zero Dual, no
  `eps_i eps_j`);
- a family, full TD6, SP-2, or JC2 theorem;
- first-stage statements about the nine nonzero dead transport axes.

V81A deployment and math-harness errata remain in the tarball as
negative custody and are not executed.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. The archived `launch_v82s_host.sh` still writes V82S-era tags
   `…T0253Z` and a three-field `launch.meta`.  The frozen V82S2 meta has
   `v2` tags `…T0320Z`, `cap_kib`, and `timeout_s`.  The timed command
   on stderr is still `timeout 14400 bash run_v82s.sh`.  Pin the actual
   host launcher, or stop shipping the stale one as if it were the
   freeze driver.

2. Raw first-source columns are attested only by stdout SHA256, not by
   frozen TSV.  Dual-host identity of those SHA256 values is enough for
   presence.  Emitting the digest file would make Finding 3 reconstructible
   without CAS.

3. `payload/SOURCE.sha256` is an unlisted tar member and does not name
   the V82S/V81B/V82 producers.  The executed check is the outer
   62-line list, which does name them.  The inner file is leftover
   payload packaging.

4. The producer report still says the 24-direction composition remains
   producer-tier until V81C review.  V81C is CONFIRMED.  That sentence
   is stale.

5. `transport_original_3470_pivot_rows_replayed=true` and
   `all_first_pivot_source_combinations_replayed=true` are unconditional
   prints after callee asserts.  They are not independent evidence.
   The asserts are the evidence; the prints are banners.

6. V82 parent still contains unused joint 33-axis first-stage code and
   still inherits `denominator_for([]) -> tri.CTX(1)`.  Executed
   `main()` is the V82S2 shard.  A reader of `q_dead_joint_first_fitting_v82`
   alone could think this freeze already ran the 33-axis first ring.

7. Stdout never prints `aws_platform=Linux`.  The wrapper refuses
   non-Linux.  A printed platform marker would match V78 traces.

---

## Independent discharge

- **Dual-host equality** of both axes is discharged by identical table
  bytes, identical MANIFEST SHAs, and independently recomputed
  normalized stdout SHA256 values.
- **Header-only actual and synthetic tables** are discharged by the
  57-byte header and SHA `68b4a3a1…` on all eight files.
- **`tri.ONE` correction** is discharged by the executed ternary in
  `write_table`, the trivariate definition `ONE = CTX.constant(1)`, and
  the in-process assert, not by erratum prose.
- **Transport 3,470-row replay and `A'` omission** are discharged by
  V81B `dead_lift` source, which is byte-identical to reviewed V81C, and
  by the matching V81C derivative-row / term / omission counts on
  `d10` and `d15`.
- **First-stage `38/132` and pivot-combination replay** are discharged
  by V82 `solve_cert` source plus the asserted pivot/free counts.
- **V78 q-first zero** is discharged by the frozen CONFIRMED V3 review,
  not by any V82S2 q-propagation into the first band.
- **V81C rank-nine kernel `Q22+d10+d15`** is discharged by the frozen
  CONFIRMED V81C review.
- **Exit-0** is discharged by four `rc` files equal to `0\n` and four
  time-record exit statuses.  `PASS` was not treated as an algebraic
  proof.

---

## Strongest exact theorem that survives

Over the generic symbolic-center field `E(C,V,U)`, at the fixed
source-typed A3 / F1 slice `p=t^{15}`, `q=t+t^{25}`, in the pole chart
`x=r^{-25}`, `y=r^5+d_m r^m+zeta r^{17}` for `m in {10,15}`, the
first-stage Dual conormal of each dead-stretch axis `d_m`, formed from
the transported derivative `j binom(j-1,k) r^{m-5+12k}` after replaying
all 3,470 original transport pivot rows, compiled through
`qd.Dual = AxisJet` and `pack("X-2", first_band_polynomials(f1,g1))`,
is the zero map of rank `0/1`.  First rank is `38/132`.  The raw
first-source columns are nonzero (1,108 entries for d10, 739 for d15)
and vanish under the section-omission negative control.  Both actual
tables and both separately executed empty-table positive controls are
the header-only byte string of SHA256 `68b4a3a1…`.  The denominator is
the unit `1`.  Identical on two AWS hosts.

Consuming the separately hostile-reviewed V81C fact that the 33-axis
transport source-incidence map has rank nine and kernel
`span(q2..q14,q16..q24,d10,d15)`, and the separately hostile-reviewed
V78 fact that the 22 licensed q-first columns are zero, the
concatenated first-stage leftover map vanishes on that 24-dimensional
transport kernel.  Exactly those 24 directions survive the first gate.
This is a fraction-field square-zero transport-plus-first
source-incidence theorem.  It is not a one-ring 24-fold square-zero
computation, not a denominator-cleared constructible atlas, not
previous/pole/current compatibility, and not a neighborhood, family,
TD6, SP-2, or JC2 theorem.

---

CONFIRMED
