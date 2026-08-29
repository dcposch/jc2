# Hostile review V2: TD6 V84R2 q2--q5 quadratic previous/pole block

Inspection only of the charged producer report and the frozen V84R2
pilot case.  No producer execution, no AWS relaunch, no Flint, no CAS,
no solver, no Lean, and no local Mac Dual GE.  Stored `PASS` /
`quadratic_*_control=true` strings were ignored as proof.  Frozen file
bytes were hashed with Python `hashlib.sha256` and compared by exact
equality.  The portable archive
`cases/td6_c1_c2_c3_qdead_previous_pole_k2_pilot_v84r2_aws_20260826/source/source.tar.gz`
was listed and selected members were read by `tarfile`; it was not
unpacked into the tree.  Every load-bearing equality below was
re-checked outside the producer checker.

The first adapter attempt (V1, target
`xmodel/td6-v84r2-k2-q2q5-zero-hostile-review-20260826.md`) is
delivery-negative: it vanished after a CLI header and produced no
report.  That attempt is not consumed.

Charged surfaces and immutable pins (all matched on disk):

```text
4a6e81d7eb2045c6733c0588a605a003148ac3275d3458f67d5c9cf59293e8d2
  cases/.../FREEZE.sha256
096557b26f8004c7b7d90f5d132572eb4c1c3fe6a9b2561a1fa3b2f5e9e1e1c8
  cases/.../MANIFEST.sha256
caf1cee14950ec7f75765c5bbaf5e306123be9c482281d5a14981996dd60226c
  xmodel/td6-v84r2-k2-q2q5-zero-producer-20260826.md
71934436bf932284f136d7742b398208504ef59bc07f29969bad91e6bf32abc3
  source/source.tar.gz
dd2c05c92b3828493eabde9427487e940d3c838cecbc47dceb6c9c2562d40ee3
  payload/.../qdead_previous_pole_k2_shard_v84r2_20260826/replay.py
```

Consumed as already-reviewed linear ancestry, not re-proved:

- V81C transport rank `3470/3602` (`dfac352887f645a9…`, `CONFIRMED`)
- V78 first-stage 22-q zero (`a3599e65f88015f6…`, `CONFIRMED`)
- V82S2 `d10,d15` first kernel (`3f62b23d43e134ee…`, `CONFIRMED`)
- V82 Stage-A `Q_prev = Q` of dimension 24 (`b47b613f8ee7c64e…`)

V84 is a typed-source deployment negative.  V84R is a failed-control
negative.  Neither is a mathematical predecessor of this table.

What was not recomputed: the rank-3470 transport factorization, Dual
GE on the 132- and 94-variable quadratic jets, first-band and
previous/pole compilation, and the numerical vanishing of the ten
quadratic pairings.  Those are attested by two independent AWS runs of
the pinned source, byte-identical exact tables, and fail-closed
asserts in that source.  This review reconstructs what that source
must emit and what an empty table is allowed to mean.

---

## Findings

**1. [Confirmed] `MANIFEST.sha256` and `FREEZE.sha256` close, the
source archive and inner `V84R2_SOURCE.sha256` close, both `rc` files
are exit zero, raw streams differ only in registered host/tag/path
text, and both exact tables and both denominator files are
byte-identical.**

All 23 `MANIFEST.sha256` members hash-match on disk.  The walk of the
case directory has no extra files and no missing listed files.
`FREEZE.sha256` pins `MANIFEST.sha256` and the producer report; both
pins match.  Inner `V84R2_SOURCE.sha256` (86 members) matches the
extracted archive byte-for-byte, including the executed producer
`replay.py` `dd2c05c92b…`.  Case-dir copies of `run_v84r2.sh`,
`launch_v84r2_pilot_host.sh`, `V84R2_PREREGISTRATION.md`,
`V84R_FAILED_CONTROL_ERRATUM.md`, and `V84R2_SOURCE.sha256` equal the
archive members.

Both `rc` files are the single byte-string `0\n`, SHA
`9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
Both stderr files are `/usr/bin/time -v` custody of
`timeout 21600 bash run_v84r2.sh` with `Exit status: 0`, zero swap,
and RSS `431068` / `431624` KiB.  After replacing hostname, run tag,
and run-root path by placeholders, the two stdout files are
byte-identical.  They differ on disk only in those registered custody
fields, as claimed.

Emitted tables, both hosts, byte-identical:

```text
b93bed47384146af9d18c44cc51897aa95455094fa55cec51470d2ea3cc737ab
  K2_BLOCK_0_0.exact.tsv   (93 bytes, one newline)
8041f53d2bb2b7e92f9e047d2ca6bad668bac36b5f2a1e0a146cec71be70af43
  K2_BLOCK_0_0.denominator.factor.txt   (8 bytes)
```

The exact table is exactly the header line plus newline:

```text
stage	compatibility	key	coordinate	axis_left	axis_right	coefficient_sha256	coefficient_exact
```

The denominator file is exactly `(1, [])\n`.  Direct read, not a
producer-printed SHA.  Both hosts record flint `0.9.0` and
`sha256sum -c V84R2_SOURCE.sha256` OK on all 86 members before any
algebra.

Registration meta on both hosts pins archive
`71934436bf932284f136d7742b398208504ef59bc07f29969bad91e6bf32abc3`,
cap `8388608` KiB, stamp `20260826T0540Z`, and tags
`td6_v84r2_k2_{r6d,box03}_block_0_0_20260826T0540Z`.  Launcher and
`main()` both refuse non-Linux, non-EC2, and any tag not starting
`td6_v84r2_k2_`.  Block env is hardcoded `(0,0)`.

**2. [Confirmed] The licensed q2--q5 source singletons are the unique
X-boundary rows `('g','X',0,j)` for `j=2,3,4,5`, each with coefficient
one, and every other licensed axis is omitted from this shard.
Typed `qd.source_rhs(key).value` is the Dual source base; the failed
V84R equality against `scalar(row_rhs)` is a presentation mismatch
outside the X boundary.  X-boundary equality is retained and
asserted.**

Import chain, each step hash-pinned before exec:

```text
V84R2 dd2c05c92b…
  -> V82P  fbe3879a714a…
    -> V82S  a344d3c21109…
      -> V82   537219eb8d4c…
        -> V81B  cc2397087328…
          -> all-q 7e5ade2b0f87…
            -> qd = jet-orbit adjoint fb138b0f59e6…
```

`Q_LEVELS = range(2,15) + range(16,25)` (22 exponents, `15` excluded).
V84R2 then restricts to the 24-kernel `Q_AXES + (d10,d15)` and splits
it into six 4-axis blocks.  Block `(0,0)` is `AXES[0:4] = (q2,q3,q4,q5)`.
`TARGET_PAIRS` is the 10 unordered pairs including diagonals, then
sorted by `AXES.index`.  `QuadJet` construction `assert`s every linear
axis in `ACTIVE_AXES` and every quadratic pair in `TARGET_PAIR_SET`.
q6--q14, q16--q24, d10, d15, and q15 cannot enter this ring.

Authoritative Dual source, jet-orbit adjoint `source_rhs`, after
`configure_qd` has rebound `Dual`, `B`, `Q_PRIME`, `R3/R5`, `POLE_*`:

```text
('g','X',0,j) |-> {1: Dual(1), 2: B, 25: Dual(1)}.get(j, Dual(0))
('f','X',0,j) |-> Dual(1) if j==15 else Dual(0)
F1 / F0      |-> R3/R5 and POLE_F/POLE_G over E(C,V,U)
```

`typed_source_jet` then does three things.

1. `base = QuadJet.coerce(qd.source_rhs(key)).value`, typed `E3`.
2. On every X-boundary row, `assert base == scalar(rhs)` against the
   legacy transport-row RHS.  That is the retained V84R equality, now
   licensed only where both presentations are in `Q`.
3. On `('g','X',0,j)` with `qj` active, inject `derivatives[qj] = E3(1)`,
   returning `OldAxisJet` (square-zero), not `QuadJet`.  Omitting that
   singleton is required to change the jet.  Each active q-axis occurs
   on exactly one such row (`seen_boundary == {q2:1,q3:1,q4:1,q5:1}`).

For `j=2`, Dual `B = QuadJet.direction("q2")` already carries linear
coefficient one, and the code asserts `raw.linear[q2] == E3(1)` before
using the injected singleton.  For `j=3,4,5`, `source_rhs` returns
`Dual(0)` (no linear); the singleton is purely the injection.  That is
the same typing as reviewed V81B/V78 `source_jet` /
`source_vector_jet`, which inject `E3(1)` on every
`('g','X',0,j)` for `j` in `Q_LEVELS` and take the Dual value as base.

Why V84R's global `raw.value == scalar(row_rhs)` is not authoritative.

The reviewed all-q transport source is `r.t.source_vector(key)`, and
that adapter is `cp.source_rhs(key) = E(qd.source_rhs(key).value)`
projected to 18 `Rat2` coordinates.  Its `.value` is Dual-typed.  The
transport triple's third component `rhs` is the first-band
`build_transport` stored RHS (univariate F1/F0 patterns at
`CENTER=(C,V,U)`).  Those two objects agree on X-boundary `{0,1}` and
need not be Python-equal on F1/F0, where Dual uses `S,D,L,A` in `E`
and the stored row uses the univariate pattern.  V84R compared them
on every row and died before any K2 table.  V84 compared
`qd.source_rhs` after `Dual=QuadJet` with the old `source_vector`
adapter and died in `Fraction`.  V84R2 keeps the Dual `.value` and
cross-checks the legacy scalar only on X.  That is the smallest repair
that restores the reviewed Dual source, not a new source.

q15 never appears: `assert "q15" not in AXES`, `Q_PRIME` is initialized
`{0: 1, 24: 25}` and then only active licensed levels, so `Q_PRIME[14]`
is unset.

**3. [Confirmed] Diagonal quadratic slots are Taylor coefficients
(`x^2` stores `1`, not `2`).  Mixed slots use the polarized product
`xy+yx`.  `QuadJet.inverse` includes the second-order term
`a^{-3}(linear)^2` (diagonal) or `2 a^{-3} lin_i lin_j` (mixed), and
asserts `self * inverse == 1`.  Direct q-prime variation is
`Q_PRIME[j-1] = direction(qj, j)`.  q15 target shear is excluded.**

`QuadJet.__mul__` for a registered pair:

```text
diagonal:   value += lin_i * lin_i          # coeff 1
mixed:      value += lin_i*lin_j + lin_j*lin_i   # coeff 2
```

Preflight, for `TARGET_PAIRS[0] = (q2,q2)` on this block:

```text
(x**2).quadratic[(q2,q2)] == 1
((x+x)**2).quadratic[(q2,q2)] == 4
```

Classical second derivative of `x^2` is `2`; the stored coefficient is
the Taylor coefficient of `eps^2` in `(1+eps)^2`.  Mixed-block
preflights (split-twice product `= 2`, pair-swap) are in source and
are not reached on a diagonal first pair; the mixed product formula
in `__mul__` is still the one executed for `q2:q3`, …, `q4:q5`.

Inverse second term, for `unit = QuadJet(2, {q2:3, q2:5}, {(q2,q2):7})`
the code asserts `unit * unit.inverse() == 1`.  Expansion of
`1/(a+b)` through degree two is `-a^{-2} b_2 + a^{-3} b_1^2`, which is
exactly the stored formula.

Direct q-prime: `configure_qd` sets

```text
Q_PRIME[0] = 1
Q_PRIME[j-1] = direction(qj, j)   for j in {2,3,4,5}
Q_PRIME[24] = 25
```

`first_band_polynomials` multiplies `f1[i]` by `Q_PRIME.get(degree-i)`.
That is `q' = 1 + 2 q2 t + 3 q3 t^2 + 4 q4 t^3 + 5 q5 t^4 + 25 t^{24}`
truncated to the active block.  `compile_previous` rebinds
`base.Q_PRIME` to this same dictionary before `compile_x_previous`.
q15 is not a key.

Dead second-matrix Taylor/mixed formula (`comb(j,2)` vs `j(j-1)`) is
in source and is not executed on this q-only block.  It is not needed
for the charged ten pairs: q-axes do not vary the transport matrix.

**4. [Confirmed] Original-row source-combination ancestry is fail-closed
at transport, FIRST, and previous/pole.  For this block the transport
quadratic target is empty (q does not vary the matrix).  FIRST has
38 pivots, 0 dependents, 94 free.  Previous/pole has 38 pivots, 1
dependent, 56 free.  The only emitted denominator is the unit of the
empty table.**

Transport.  `v81.build_base_transport` sets `CENTER = (C,V,U)`,
clears the x-power cache, factors the 3602-variable system, and
asserts rank `3470` with `free = 132` and two recorded events.  Both
stdouts print the same pivot ladder and `transport_rank=3470/3602;free=132`.
`propagate_q_typed` zips original rows with factorization records,
`assert source_key == key`, subtracts `pivot_rhs[old] * scalar(factor)`,
and `assert not compatibility`.  Linear q-forms are then
`v81.global_q_forms` on those 3470 pivots.

Quadratic transport target, `second_transport_target`, is nonempty
only for pairs involving a `d*`-axis.  All ten charged pairs are q-q,
so both hosts print

```text
pair=qi:qj;transport_target_rows=0;transport_quadratic_compatibilities=0
```

for every pair.  That is not an empty-serializer inference: the target
dict is empty by source, `lift_order` is skipped, and
`transport_quadratic` therefore contributes nothing.  q-variation of
the affine RHS is first-order `OldAxisJet` only; the second variation
of a q-q transport pair is identically zero.

FIRST.  Sections are `x_chart_coefficient` composed with `QuadJet`
forms.  `qd.pack("X-2", first_band_polynomials(f1,g1))` is Dual GE'd
by `solve_cert` / `parameterize(132, ...)`.  Pivots are chosen only on
`coefficient.value`.  Every surviving pivot and every dependent is
replayed from original packed rows:

```text
replay == source_polynomial(row, rhs)
```

`assert len(first_pivots)==38 and len(free94)==94 and not first_dependent`.
Both hosts: `first_rank=38/132;dependent=0`.

Previous/pole.  First forms are composed into previous X-band and pole
previous, packed, Dual GE'd on 94 variables.  Same original-row
replay.  `assert len(previous_pivots)==38 and len(free56)==56`.  Both
hosts: `previous_pole_rank=38/94;dependent=1`.

`all_*_source_combinations_replayed=true` are unconditional prints
after those asserts.  The asserts are the evidence; the prints are
banners.  A skipped replay is a nonzero exit, not a silent empty
table.

Denominators.  Transport quadratic compatibilities are empty.  FIRST
dependents are empty.  Previous/pole contributes only if the one
dependent row has a nonzero quadratic coefficient.  `write_table` on
an empty `values` uses `v81.tri.ONE` (the V82P2 empty-table unit,
`CTX.constant(1)`), whose `factor()` is `(1, [])`.  That is the
denominator of the zero table, not a factorization of a hidden
nonzero coefficient.

Varying matrices: q-axes do not vary the transport matrix (reviewed
Stage-A fact, reconstructed here as empty `second_transport_target`).
They do vary FIRST and previous/pole through `Q_PRIME` and through
`QuadJet` products of section forms.  Dead first/second matrix
variation (`dead_derivative_rows`, `dead_second_rows`) is present in
source and is not reached on block `(0,0)`.  The charged ten pairs
do not require it.

**5. [Confirmed] `dependent=1` with a header-only table means the one
previous/pole leftover row is zero at order 0 and 1 and pairs to zero
with all ten charged axes at order 2.  A header-only serializer that
dropped nonzero slots is incompatible with the registered-slot control
together with `dependent_quadratic` / `write_table`.  A dropped or
wrong source singleton fails closed before any table.**

`parameterize` records every Dual-GE leftover in `previous_dependent`.
`dependent_quadratic` then, for that unique leftover,

```text
for every coefficient in row values and rhs:
    assert not coefficient.value
    assert not coefficient.linear
    emit every truthy quadratic[(left,right)]
```

Order 0 and order 1 of the leftover are required zero.  Order 2 is
emitted iff a registered pair has nonzero `E3` coefficient.  `values`
is that dict.  `write_table` walks `values` and writes one TSV row per
key; it has no "if empty, write header anyway" branch that would
discard keys.  Header-only therefore means `values` was empty, hence
all ten pairings of the leftover are the zero `E3`.

Attack on a silent empty serializer.

- Registered nonzero slot: `assert QuadJet.second((q2,q2)) != QuadJet()`
  before any compilation.  `__bool__` is `value or linear or quadratic`.
  A registered quadratic coefficient is truthy.  `dependent_quadratic`
  inserts truthy `E3` values.  `write_table` would emit them.  The
  control is a ring/serializer contract, not a second write of a fake
  table.  It is enough to reject the V82P-style "always header"
  reporter: that reporter would still be reachable only if `values`
  were empty or if `QuadJet.second` were indistinguishable from zero,
  and the latter is asserted false.
- Omitted source: `typed_source_jet(..., omit_boundary=(qj,))` is
  required `!=` the true jet, and `seen_boundary` must be exactly the
  four active q-axes each once.  Wrong source (missing singleton,
  extra linear on a non-q2 Dual RHS, or unregistered axis) is an
  `AssertionError` before Dual GE.  The q2 Dual-`B` agreement is an
  additional wrong-source check.

This is not "the previous/pole system has no leftover."  Linear
Stage A already has a previous/pole leftover of rank `38/94`.  The
claim is that this leftover's quadratic pairing with
`Sym^2 span(q2,q3,q4,q5)` is zero.

**6. [Confirmed] The terminal string `...V84 PASS` is a custody
leftover.  It does not block the theorem.**

The V84R2 patch against V84R changes five executed sites: docstring,
`typed_source_jet` (typed base + X-boundary-only equality), the two
new stdout flags, tag prefix `td6_v84r2_k2_`, and
`producer=...V84R2`.  It does not change the last print,

```text
TD6-A3-QDEAD-PREVIOUS-POLE-K2-SHARD-V84 PASS
```

Every identifying surface except that one line is V84R2: producer
banner, AWS tags, `run_v84r2.sh`, preregistration, archive SHA,
`replay.py` path, and both registration metas.  The string is not
used as a mathematical predicate.  Same bytes would be emitted by a
one-line rename.  Custody repair only.

**7. [Confirmed] Scope is exactly the ten pairs in
`Sym^2 span(q2,q3,q4,q5)`, through previous/pole, on the common
generic principal open of the fixed source-typed A3 presentation.
No inference to the other 290 pairs, current, rank-drop fibres,
formal integrability, a nonlinear family, TD6, SP-2, landing, or
JC2 is licensed.**

`BLOCKS` is six 4-axis blocks of the 24-kernel.  Unordered block pairs:
6 diagonal blocks of 10 pairs and 15 off-diagonal blocks of 16 pairs,
`60+240=300=binom(24+1,2)`.  This freeze runs only `(0,0)`.  The
other 290 pairs are not computed.

Executed path never calls `compile_current`.  Dead axes are inactive.
`raw_rank_drop_denominator_fibres_remain_debt=true` is a banner, but
the source also never clears V83's `R38=0` fibre: Dual GE is on the
generic principal open (`CENTER=(C,V,U)`, no denominator localization
beyond the unit of a zero table).  `QuadJet` is truncated at degree
two, so it is not a nonlinear lift and not a family.  Printed scope
and `no_current_family_TD6_SP2_or_JC2_claim=true` match the executed
path; those strings were not used as proof.

Refused implications, all absent from the executed path:

- any of the other 290 pairs, including every pair that uses
  `q6,...,q14,q16,...,q24,d10,d15`;
- current-row compatibility;
- rank-drop fibres / a constructible atlas of the complement of the
  generic open;
- a nonlinear neighborhood, a formal-integrability statement, or a
  family;
- the 21-block union, all of K2, TD6, SP-2, landing, or JC2.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. Terminal PASS still says `V84`.  Rename it, or stop treating the
   last line as a version tag.

2. Case README PIDs `233537` / `166617` do not match freeze `pid`
   files `233528` / `166608`.  The freeze files are the launcher
   wrapper PIDs.  Pin those.

3. Inner tarball `README.md` is leftover V82P4 current-adjoint prose.
   The executed check is `V84R2_SOURCE.sha256`.  The inner file is
   packaging.

4. `linear_specialization_reproduces_stage_A_zero=true` is an
   unconditional print.  The actual linear specialization evidence is
   Dual-GE ranks `38/132` dependent `0` and `38/94` dependent `1` with
   leftover value and linear parts asserted zero.  Do not cite the
   print.

5. Inner `payload/SOURCE.sha256` and the V82P4-era `SOURCE.sha256` are
   unlisted as freeze members except via the archive hash.  The
   executed list is the 86-line `V84R2_SOURCE.sha256`.

---

## Strongest exact theorem that survives

On the fixed source-typed A3 presentation at symbolic center `(C,V,U)`,
after the rank-3470 transport and the rank-38 FIRST elimination with
no FIRST leftover, the unique previous/pole leftover of the rank-38/94
system has vanishing quadratic pairing with every unordered pair in

```text
Sym^2 span(q2, q3, q4, q5).
```

The common exact table is the 93-byte header
`b93bed47384146af9d18c44cc51897aa95455094fa55cec51470d2ea3cc737ab`
and the common denominator is the unit `(1, [])`,
`8041f53d2bb2b7e92f9e047d2ca6bad668bac36b5f2a1e0a146cec71be70af43`.
Source archive
`71934436bf932284f136d7742b398208504ef59bc07f29969bad91e6bf32abc3`.
This is a generic-open quadratic source-incidence statement for those
ten pairs through previous/pole.  It is not a statement about the
other 290 pairs, current, rank-drop fibres, a nonlinear lift, a
family, TD6, SP-2, landing, or JC2.

---

CONFIRMED
