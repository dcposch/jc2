# Hostile review: TD6 V80B dead-stretch transport point discriminator

Inspection only of the charged producer case and producer report.  No
producer execution, no `verify.py` run, no CAS, no solver, no Lean, no
shell, and no local hash recomputation.  Stored `PASS` strings were
ignored as proof.  Frozen file bytes were read and compared as text.
The portable archive `source/source.tar.gz` was not unpacked; its
50-entry closure is the frozen `source/SOURCE.sha256` listing, the
extracted siblings under `source/`, and the 22 host execution traces.

Charged surfaces:

- `cases/td6_c1_c2_c3_dead_stretch_transport_v80b_aws_20260826/`
- `xmodel/td6-c1-c2-c3-dead-stretch-transport-v80b-producer-20260826.md`

The seven load-bearing charges are re-audited from extracted source,
the pinned parent first-band / jet-orbit modules named by the source
manifest, both AWS raw outputs, and the eleven exact compatibility
tables on each host.

---

## Findings

**1. [Confirmed] Exact source typing is the eleven pole-chart
coefficients `d6..d16` in**

```text
x = r^{-25},
y = r^5 + sum_{m=6}^{16} d_m r^m + zeta r^{17},
```

**differentiated at `d_6=...=d_16=0`, one level per shard, by the
binomial/shift formula `j * binom(j-1,k) r^{m-5+12k}`.**

`source/replay_shard.py` is the unique mathematical producer.  It
refuses any `TD6_DEAD_LEVEL` outside `{6,...,16}` and prints

```text
pole_chart=x=r^-25;y=r^5+sum(d_m*r^m,m=6..16)+zeta*r^17
```

on every frozen stdout.  Zeta is the already present pole modulus, not
a twelfth dead-stretch coordinate.  The g-transport consumed from the
pinned jet-orbit parent is the coefficient dict `{1: Q(1), 25: Q(1)}`,
so `q = t + t^{25}` with no dead-stretch slot in `q`.

`dead_derivative_rows` walks the frozen rectangles `(f: i<=15, j<=60)`
and `(g: i<=25, j<=100)` and, for each monomial `x^i y^j` and each
zeta degree `k < j`, installs

```text
coefficient = j * C(j-1, k),
exponent    = -25 i + 5 j + (LEVEL - 5) + 12 k
```

with f-cutoff `-3` and g-cutoff `-5`.  That is exactly the first
derivative of `x^i y^j` in `d_m` at vanishing dead stretch: `x^i`
contributes `r^{-25 i}`, and

```text
d/d(d_m) y^j |_{d=0}
  = j (r^5 + zeta r^{17})^{j-1} r^m
  = j sum_k C(j-1,k) r^{5(j-1-k) + 17k + m} zeta^k,
```

which is `j C(j-1,k) r^{m-5+12k}` times the undeformed `r^{5j}`
factor.  The in-source positive control is the `x^2 y^3` slot
`variable = 2*61+3`, requiring coefficient `3` at `k=0` and `6` at
`k=1`; the wrong-shift key `LEVEL-4` is required not to carry `3`.
Both banners print `true` on all 22 stdout files.

No twelfth exponent, no `d5`, and no `d17` appear as a dead direction.
Each shard injects exactly one `LEVEL`.

**2. [Confirmed] The computation is the hard-center point
`fb.CENTER = (Q(1), Q(1), Q(1))` with `beta=0`.  It is not a
calculation over the generic A3 center ring, and it does not inherit
V78's symbolic-center scope.**

`base_transport_forms` assigns `fb.CENTER = (Q(1), Q(1), Q(1))` and
clears `fb._X_POWER_CACHE` before `qd.build_transport_rows()`.  The
imported first-band module (jet-orbit's `fb`) already declares

```text
CENTER = (Q(1), Q(1), Q(1))
```

and `x_power_expansion` reads that name, so `fb.CENTER = ...` is an
attribute assignment onto the same module global.  The first-band
docstring hard-wires the x-chart as `x = s + s^2 + s^3 + t s^4`.  The
V80B assignment is therefore a restatement of an already specialized
point, not a generic-center computation that was later evaluated at
`(1,1,1)`.

`beta=0` is the transport section, not a Dual-number leftover.  Jet-orbit
`build_transport_rows` builds g from `{1: Q(1), 25: Q(1)}` only.  The
parent's `B = Dual(0,1)` and `source_rhs(..., 2): B` belong to the
parent's own q2-adjoint `main()`; V80B keeps Dual constants only long
enough to take `.value` and retain homogeneous Q-directions (the
parent comment: "The transport matrix is constant").  The q2-base
sibling's module-level `B = Q(1)` is never the g-transport dict that
V80B calls.  Every stdout scope line is

```text
scope=transport_source_incidence_at_fixed_A3_zero_dead_stretch
```

The producer report's scope correction is required, and it matches the
source.

**3. [Confirmed] Every shard replays all 3,470 original pivot rows of
the differentiated equation, and the matrix-derivative omission
control is a real negative control, including on the two consistent
levels.**

After echelon differentiation, `derivative_lift` rebuilds every pivot
key of the frozen rank-3470 transport as

```text
A0 x' + A'_LEVEL x0  =  0
```

and asserts the reconstructed form is `ZERO_FORM`.  All 22 stdout
files print `differentiated_original_pivot_rows_replayed=3470` together
with `transport_rank=3470/3602;free=132`.  The producer also asserts
`pivot_replays == len(pivots)` before printing.

The omission control does not trust that replay.  It separately counts
rows of `A'_LEVEL` with `A' x0 != 0` and requires the count to be
positive, so a producer that set `x'=0` and skipped `A'` cannot pass
by treating a matrix-changing direction as RHS-only or as the zero
matrix.  Frozen counts are exactly the vector column
`omission_failures`:

| level | omission_failures |
|---|---|
| d6 | 39 |
| d7 | 36 |
| d8 | 32 |
| d9 | 29 |
| d10 | 26 |
| d11 | 23 |
| d12 | 20 |
| d13 | 16 |
| d14 | 13 |
| d15 | 10 |
| d16 | 7 |

Those numbers are positive on `d10` and `d15` as well, so the two
zero compatibility tables are not `A'=0`.  Every stdout also prints
`dead_stretch_matrix_derivative_omission_negative_control=true`.

Derivative-only keys absent from the base echelon are retained (the
`derivative-only` branch).  No emitted table row has kind
`base-dependent`; that branch exists in source and was not taken on
this point.

**4. [Confirmed] All eleven levels on both hosts are exit-0 / final-line
`PASS`, and the eleven exact compatibility tables are byte-identical
across r6d and Box03.**

`MANIFEST.sha256` records the same SHA for each pair

```text
evidence/{r6d,box03}/dN/evidence/DEAD_DN_TRANSPORT_COMPATIBILITY.tsv
```

N=6..16.  Those SHA strings are copied into
`DEAD_TRANSPORT_11_VECTOR.tsv` column `compatibility_table_sha256` and
into both hosts' `transport_compatibility_table_sha256=` markers.
Every `rc` file is the single byte-string `0` (all 22 share MANIFEST
SHA `9a271f2a…`).  Every stdout ends on

```text
TD6-A3-DEAD-STRETCH-TRANSPORT-V80B-SHARD PASS
```

Hosts are distinct: r6d `ip-172-30-0-45`, Box03 `ip-172-30-0-249`.
PIDs differ.  Run tags are
`td6_v80b_dead_{r6d,box03}_20260826T0137Z_dN`.  Direct reads of the
tables agree on the load-bearing prefix: header-only for `d10` and
`d15`; on every inconsistent level the first data line is the same
`derivative-only` constant on both hosts.

Independence of the two hosts is the hostname/PID/path difference.
Mathematical equality is the identical table SHA, the identical
content digest, and the identical vector row.

**5. [Confirmed] At this point `d10` and `d15` have the exact zero
compatibility table.  Each of the other nine pure axes is affine-
inconsistent, with the same first residual SHA, at a level-shifted
source key.**

`d10` and `d15` on both hosts:

```text
transport_compatibility_forms=0
transport_compatibility_table_entries=0
transport_compatibility_affine_consistent=true
transport_compatibility_digest=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The digest is the SHA of the empty byte string.  The emitted TSV is
the header line `kind\tkey\tcoordinate\tcoefficient_exact\n` only, SHA
`a30f85978…`, identical for `d10` and `d15` and across hosts.  This is
exact vanishing of leftover incidence on the 132-dimensional base
transport space, not vanishing of `A'` (Finding 3).  For these two
levels `dead_derivative_only_row_keys=0`: every derivative key already
sits in the base record set and reduces to zero.

The other nine levels have `consistent=false`, affine rank `0/132`,
`first_inconsistency_index=0`, and

```text
transport_compatibility_first_inconsistency_sha256=
0458f40e62da3f7fc5d841ab77d1d10a1215791299991bba2285073d090cccda
```

The first TSV row on each of those nine, on both hosts, is a
parameter-free constant

```text
derivative-only    ('f', 'F0', LEVEL-20, 0)    constant    0|(15625/3)*S^0|0
```

| level | first key | forms | entries |
|---|---|---|---|
| d6 | `('f','F0',-14,0)` | 39 | 1396 |
| d7 | `('f','F0',-13,0)` | 36 | 1269 |
| d8 | `('f','F0',-12,0)` | 32 | 1159 |
| d9 | `('f','F0',-11,0)` | 29 | 1007 |
| d11 | `('f','F0',-9,0)` | 23 | 735 |
| d12 | `('f','F0',-8,0)` | 20 | 617 |
| d13 | `('f','F0',-7,0)` | 16 | 514 |
| d14 | `('f','F0',-6,0)` | 13 | 373 |
| d16 | `('f','F0',-4,0)` | 7 | 115 |

The next line is always a different key (for d6/d16, `('f','F0',
LEVEL-20, 5)` with constant `-31250`), so the first obstruction has no
p-column and cannot be absorbed into the 132 free transport
parameters.  That is a pure-axis inconsistency at this point.

**6. [Confirmed] Equal displayed nonzero scalars are not a common
linear form.  They can sit at shifted keys, and overlapping keys carry
unequal forms.  No joint-axis, dead-stretch-block, generic-A3,
neighborhood, family, full-TD6, or SP-2 exclusion is licensed.**

The common first residual `0|(15625/3)*S^0|0` occurs at nine distinct
keys `LEVEL-20`.  Direct reads of the tables show:

- `('f','F0',-14,0)` occurs only in the two `d6` tables;
- `('f','F0',-13,0)` occurs only in the two `d7` tables;
- `('f','F0',-12,0)` occurs only in the two `d8` tables;
- `('f','F0',-9,0)` occurs in `d11` as that parameter-free `15625/3`
  constant **and** in `d6` as a different, parameter-rich form whose
  constant is not `15625/3`;
- `('f','F0',-4,0)` occurs in `d16` as `15625/3` **and** in `d6` and
  `d11` as two further, mutually different parameter-rich forms.

So a common displayed scalar is not a common cokernel coordinate, and
an overlapping key is not an equal column.  Linear combinations of
those columns are therefore not readable from "nine axes failed with
the same first number."  `d10` and `d15` are exact zero columns at
this point, so any joint kernel that was later formed would contain at
least those two axes.  The 22 licensed q-directions are absent.  The
center is `(1,1,1)`, not generic A3.

The producer did not freeze a joint 11-column matrix or its kernel.
Even a triangular reading of the earliest unique keys would still be a
point-scope, q-free, first-order observation, not a licensed block
theorem.  The next-gate sentence in the producer report (one
symbolic-center 33-axis source problem) is the correct successor.
Nothing in the tables licenses a neighborhood, a family, generic A3,
full TD6, or SP-2.

**7. [Confirmed] Source / archive / manifest / hash custody is closed
on the inspectable freeze, V80A is a deployment-negative erratum, and
every advertised firewall is present as source assertion or as a
frozen execution trace.**

Closure, as frozen, is:

- `source/SOURCE.sha256`: 50 entries.  Extracted
  `PREREGISTRATION.md`, `replay_shard.py`, and
  `V80A_DEPLOYMENT_ERRATUM.md` carry the same SHA strings as their
  archive members.  Parent jet-orbit is pinned
  `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`,
  matching the workspace jet-orbit `MANIFEST.sha256` and the V80A
  erratum's corrected pin (the V80A typo was the tenth hex digit
  `a` versus `e`).
- `source/source.tar.gz` is listed in `MANIFEST.sha256` as
  `6312e21a…`, the same pin `verify.py` names.
- `MANIFEST.sha256` has 119 paths: vector, README, `VERIFY.stdout`,
  `verify.py`, five `source/` files, and 110 evidence files (11 levels
  × 2 hosts × `{pid,rc,stderr,stdout,tsv}`).  `FREEZE.sha256` hashes
  that manifest plus the producer report plus this review's prompt.
- `verify.py` is a custody/table-equivalence reader.  It does not
  rebuild `A'` or rerun GE.  Frozen `VERIFY.stdout` is

  ```text
  TD6 V80B POINT-DISCRIMINATOR CUSTODY PASS
  scope=(C,V,U)=(1,1,1);beta=0;pure_axes_only
  joint_or_generic_claim=false
  ```

Firewalls actually visible without unpacking the tarball:

- Linux / registered-tag / source-closure: every stdout begins
  `aws_platform=Linux`, a host-specific `aws_hostname`, a unique
  `aws_run_tag`, then 50 `SOURCE.sha256` `OK` lines in the same order
  as the frozen manifest, including `./run_v80_shard.sh`,
  `./run_v80_one.sh`, and `./launch_v80_host.sh`.  Every stderr timed
  command is `bash ./run_v80_shard.sh`.
- Parent pin, LEVEL range, binomial/wrong-shift controls, omission
  control, 3470-row replay: Finding 1--3.
- `pole_chart_determinant=-25*r^-9_independent_of_dead_stretch=true`:
  structural.  With `x=r^{-25}` and `y=r^5+...+zeta r^{17}`,
  `det d(x,y)/d(r,zeta) = (-25 r^{-26}) r^{17} = -25 r^{-9}`,
  independent of every `d_m`.  The first-band parent already normalizes
  the pole ODE to that determinant.
- `fixed_section_square_zero_no_family_firewall=true` on every stdout.
- Preregistration: AWS-only, fail closed on non-Linux or missing
  registered tag, "A nonzero incidence form is not a dead-stretch
  kill", no TD6/SP-2/JC2 inference.
- V80A: deployment-negative only; no shard reached transport
  construction; not consumed as mathematics.

The launcher bodies live only inside `source.tar.gz`.  They were not
unpacked.  Their refuse branches are evidenced by the 22 matching
preambles and by preregistration, not by a line-read of
`run_v80_shard.sh`.  That is the same execution-trace standard the
freeze itself records; it is not a missing endpoint.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. Stdout never prints `CENTER=(1,1,1)` or `beta=0` as markers.
   Both are load-bearing in source (`fb.CENTER = (Q(1), Q(1), Q(1))`
   and g-transport `{1:1, 25:1}`).  `verify.py` only string-matches the
   CENTER assignment.  A printed point marker would make the scope
   correction visible in the AWS logs.

2. The imported jet-orbit parent still carries Dual `B = Dual(0,1)` in
   `source_rhs`.  V80B projects `.value` and does not run the parent's
   adjoint `main()`.  Harmless here; a V80-local `source_rhs` with
   `{1: Dual(1), 25: Dual(1)}` would make the beta=0 section
   syntactically local.

3. Equal first residuals on shifted keys, plus unique earliest keys
   for `d6,d7,d8`, can tempt a triangular 9-axis reading at this one
   point.  The producer correctly refuses to license it.  The refusal
   should keep citing the missing joint matrix and the missing 22 q
   axes, not the slogan that equal scalars "can cancel," which is true
   of linear algebra in general and is not an exhibited kernel vector
   among the nine inconsistent columns.

4. `run_v80_shard.sh` / `launch_v80_host.sh` are archive-only.  A
   future freeze that also extracts those wrappers would let a
   no-unpack review read the `uname` / tag refuse branches directly.

---

## Independent discharge

- **Dual-host equality** of the eleven exact tables is discharged by
  identical MANIFEST SHAs, identical stdout `table_sha256` / content
  digest markers, and identical table prefixes on r6d versus Box03.
- **Exit-0 / PASS** is discharged by 22 `rc` files equal to `0` and 22
  final stdout lines.  `PASS` was not treated as an algebraic proof.
- **Point scope** is discharged by the first-band `CENTER` global, the
  V80B assignment, and the `{1,25}` g-transport dict, not by report
  prose.

---

## Strongest exact theorem that survives

At the source-typed A3 point `(C,V,U)=(1,1,1)` with `beta=0` and
vanishing dead stretch, in the pole chart
`x=r^{-25}`, `y=r^5+sum_{m=6}^{16} d_m r^m + zeta r^{17}`, the eleven
pure-axis transport derivatives of the frozen rank-3470 / 132-free
echelon, formed by `j binom(j-1,k) r^{m-5+12k}` and replayed on all
3,470 original pivot rows, have the following exact tables, identical
on two AWS hosts: `d10` and `d15` leave the zero compatibility table;
each of `d6,d7,d8,d9,d11,d12,d13,d14,d16` is affine-inconsistent as a
pure axis, with first leftover a parameter-free nonzero constant
`0|(15625/3)*S^0|0` at key `('f','F0',m-20,0)`.  `A'` is not the zero
matrix on any of the eleven levels.  This is a point discriminator on
pure dead-stretch axes.  It is not a joint 11-axis kernel, not an
interaction with the 22 q-directions, not a generic-center statement,
and not a neighborhood, family, TD6, SP-2, or JC2 theorem.

---

CONFIRMED
