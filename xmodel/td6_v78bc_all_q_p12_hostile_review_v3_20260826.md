# Hostile review V3: TD6 V78B/V78C all-q P12 reconciliation

Inspection only of the two charged producer cases and the two charged
producer reports.  No producer replay, no CAS, no solver, and no Lean.
Stored `PASS` / producer-verdict strings were ignored as proof.  Frozen
file bytes were hashed with Python `hashlib.sha256` and compared by
exact equality.  Both portable archives were listed and selected members
were read by `tarfile.extractfile`; they were not unpacked into the
tree.  The 23-line union tables were independently reconstructed from
the 22 frozen one-row shard tables on each host.  Printed Flint
`factor()` strings were parsed as rational monomials in `Q[C,V,U]`;
Flint was not re-invoked.  The frozen lightweight checkers
`cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/verify.py` and
`cases/td6_c1_c2_c3_all_q_p12_reconciliation_v78bc_aws_20260826/verify.py`
were run as hash/text readers only.  Every load-bearing equality below
was re-checked outside those checkers.

Charged surfaces:

- `cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/`
- `cases/td6_c1_c2_c3_all_q_p12_reconciliation_v78bc_aws_20260826/`
- `xmodel/td6-c1-c2-c3-all-q-p12-shards-v78c-aws-20260826.md`
- `xmodel/td6-c1-c2-c3-all-q-p12-reconciliation-v78bc-aws-20260826.md`

The first V78C-only delivery lane died before producing a report.  This
V3 review charges the subsequent combined V78B/V78C freeze.

Dual-host equality and simultaneous-versus-shard equality are
independent comparisons.  Both are discharged from frozen bytes, not
from report prose.

---

## Findings

**1. [Confirmed] Licensed inventory is exactly the 22 coordinates
`q2,...,q14,q16,...,q24`.  Coefficient `q15` is the lower target-shear
gauge.  No licensed coordinate is missing or duplicated.**

Write `H = C - 3U^2` and

```text
B3 = 4C^2U^2 - 4C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6
```

in the already fixed source-typed A3 section with center `(C,V,U)` and

```text
p = t^{15},
q = t + sum_{e in I} q_e t^e + t^{25},
I = {2,...,14,16,...,24}.
```

The shard producer
`source/jc2/cases/td6_c1_c2_c3_all_q_vector_ad_repaired_20260825/replay_shard.py`
(SHA `792f42de…`) and the simultaneous producer `replay.py` (SHA
`7e5ade2b…`, byte-identical in the V78C archive, both V78B payloads, and
the V78B tarball) both set

```text
ALL_Q_EXPONENTS / Q_EXPONENTS
  = tuple(range(2, 15)) + tuple(range(16, 25))
assert len(...) == 22 and 15 not in ...
```

That is 13 low exponents plus 9 high exponents, 22 total.  The V78C
launcher `run_v78c_shard.sh` (SHA `ca5108c2…`) refuses any exponent
outside the same comma-list; `fleet_launcher.sh` iterates exactly that
list; both host `launch_ledger.tsv` files are 23-line tables whose
exponent columns are `[2..14,16..24]` with no `15`.  Frozen one-row
tables, independently assembled unions, and both V78B simultaneous
tables contain those 22 row keys and no other.

Why `q15` is gauge, not a missing source modulus: the f-transport is
built from coefficient dict `{15: 1}` at degree 15, and every stdout
prints `source_p_boundary=t^15_fixed`.  The g-transport is built from
`{1: 1, 25: 1}` only.  A polynomial target shear of the pair `(p,q)` is
`q ↦ q - λ p`.  At this frozen F1 that adds a multiple of `t^{15}` to
`q`, so the coefficient of `t^{15}` in `q` is the lower target-shear
coordinate.  It is therefore excluded from the source-support inventory.
`q1` is the normalized linear leading term of `q` and `q25` is the
frozen upper boundary; neither is in `I`.  V78 preregistration states
the same exclusion.  There is no duplicate key and no hole inside `I`.

**2. [Confirmed] Each V78C run really restricts the simultaneous
square-zero compiler to one licensed basis coordinate.  The stale
module docstring that still calls a shard “simultaneous” is prose, not
a source error.**

`replay_shard.py` is `replay.py` with six executable edits.  The
load-bearing one is immediate:

```text
REQUESTED_Q_EXPONENT = int(os.environ["TD6_Q_EXPONENT"])
assert REQUESTED_Q_EXPONENT in ALL_Q_EXPONENTS
Q_EXPONENTS = (REQUESTED_Q_EXPONENT,)
```

Every subsequent ring, transport, `Q_PRIME`, conormal matrix, and P12
column loop reads `Q_EXPONENTS`.  `EJet.__init__` asserts
`exponent in Q_EXPONENTS`, so a second coordinate cannot even be
stored.  Transport source injection is the singleton

```text
key[:3] == ("g", "X", 0) and key[3] in Q_EXPONENTS
  => derivatives[exponent] = ONE_VECTOR
```

and the ordered transport is required to contain that key once.
Direct `q'` is installed only for the requested exponent:

```text
qd.Q_PRIME = {0: EJet(1), 24: EJet(25)}
qd.Q_PRIME[exponent - 1] = EJet.direction(exponent, exponent)
```

that is `e * eps_e * t^{e-1}` together with the frozen leading `1` and
upper `25 t^{24}`.  The q2 compiler slot is

```text
qd.B = EJet.direction(2) if 2 in Q_EXPONENTS else EJet()
```

with the complementary asserts (`B` derivative `{2: 1}` on the q2
shard; value and derivative both zero on every other shard).  That is
the V77R pure-q3 pattern, not a hidden simultaneous q2.

All 44 shard stdouts print the singleton runtime state, not the
docstring:

```text
single_coordinate_exact_shard=true
q_exponents=<e>
transport_active_q_columns=<e>
FIRST_conormal_rank=0/1
```

and each one-row table has `fields[0] == e`.  The top-of-file docstring
still says “one joint vector-AD run, not 22 point samples” and names
the full 22-fold square-zero ring.  That sentence is copy-paste from
`replay.py`.  It is not an executable premise: the ring, the launcher
gate, the stdout, and the tables all contradict it.  The producer
README already classifies the phrase as prose.  This review agrees.
Finding 4 then shows that the 22 singleton columns reconstruct the
joint 22-column table byte-for-byte, so the restriction did not drop a
cross-coordinate first-order term.

**3. [Confirmed] Dual-host V78C custody: 44 rc/PASS gates, archive and
source hashes, AWS platform/tag/cap metadata, per-shard table identity,
and two independently assembled byte-identical 23-line unions.**

V78C source archive SHA256

```text
b566a57ea50c3f4d24c091f006fe321aa9bb813368049773ee89b347d1284be4
```

matches the frozen tarball, every `launch.meta` line
`source_archive_sha256=…`, and the README.  Extracted `SOURCE.sha256`
(file SHA `07599218…`) matches all 47 listed members; tar members
`replay_shard.py`, `replay.py`, `run_v78c_shard.sh`,
`V78C_PREREGISTRATION.md`, and parent V32 `dcc7003d…` equal the
extracted bytes.  Case `MANIFEST.sha256` SHA `c93959e7…` matches all
502 listed paths.  FREEZE pins that manifest and the producer report
`cffa164e…`.

For each of the 22 exponents on each of Box02 (`ip-172-30-0-186`) and
r6d (`ip-172-30-0-45`):

- `rc` is the single byte-string `0`;
- stdout contains the standalone marker
  `TD6-A3-ALL-Q-VECTOR-AD-P12-SHARD PASS` as a whole line;
- `launch.meta` records `exponent=<e>`,
  `virtual_memory_cap_kib=12582912` (12 GiB),
  `timeout_seconds=14400`, the archive SHA above, and a unique tag
  `td6_v78c_{host}_q{e}_20260826T0030Z`;
- stdout records `aws_platform=Linux`, the host-specific
  `aws_hostname`, and the same tag.

The two hostnames are disjoint.  Each host therefore has 22 unique
tags, one cap, one timeout, one archive pin, and Linux/AWS identity.
The 22×3 products

```text
output/ALL_Q_P12_COLUMNS.tsv
output/FIRST_CONORMAL.tsv
output/FIRST_KERNEL.exact.tsv
```

are byte-identical host-to-host for every exponent (0 mismatches).
Every one-row P12 table has header identity, exponent key `e`, and
`lambda_prime_rows=14`.  Assembling header plus the 22 data rows in
licensed order, with a trailing newline, reproduces each host's
`ALL_Q_P12_COLUMNS.UNION.tsv` exactly.  Both unions hash to

```text
e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef
```

and are byte-identical to each other.  First conormal files are the
header-only empty table (SHA `b1b1f698…`, rank `0/1`); first kernels
are the 1-dimensional standard basis vector of the requested exponent.
The frozen checker prints `TD6 V78C frozen custody/dual-union/anchor
verification PASS`; the equalities above do not depend on it.

**4. [Confirmed] Both V78B simultaneous runs emit that same 23-line
table.  Simultaneous-versus-shard equality is discharged independently
of dual-host equality.**

V78B source archive SHA256

```text
cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579
```

matches the frozen tarball, both `launch.meta` pins, both payload
`source/source.tar.gz` copies, and the reconciliation README.  Theorem
`replay.py` inside that tarball is `7e5ade2b…`, the same file as V78C.
Parent V32 remains `dcc7003d…`.  Both hosts ran `run_v78b.sh` under
`virtual_memory_cap_kib=33554432` (32 GiB) and `timeout_seconds=14400`,
printed `aws_platform=Linux`, and returned `rc=0` with standalone
marker `TD6-A3-ALL-Q-VECTOR-AD-P12 PASS`.  `/usr/bin/time -v` on
stderr, not report prose, gives

| Host | hostname | tag | wall | max RSS (KiB) | stdout SHA256 |
|---|---|---|---:|---:|---|
| Box02 | `ip-172-30-0-186` | `td6_v79_v78b_box02_20260825T2354Z` | 1:12:39 | 505184 | `410bacc38d39f7987c39d351dd8b55679fecc4d77cafa49e77d48249e2d95644` |
| r6d | `ip-172-30-0-45` | `td6_v79_v78b_r6d_20260825T2354Z` | 1:05:14 | 504608 | `118dcb50d003b24b445cb1968111fef4073d91f33725f6f77927e23105a6f5eb` |

Exit status 0 on both time records.  Stdout hashes differ only because
absolute `TD6_OUTPUT_DIR` paths differ; the 22 mathematical P12 lines,
the 22 first-q omission lines, ranks, and PASS marker agree.  Both
`output/ALL_Q_P12_COLUMNS.tsv` files are 23 lines and hash to
`e14ff29c…`.  They are byte-identical to each other and to both
independently assembled V78C unions.  That is four frozen productions
of one byte string.  V78B stdout itself prints
`all_q_P12_table_sha256=e14ff29c…`.  Both stdouts contain

```text
q15_lower_target_shear_gauge_excluded=true
transport_all_q_source_keys_exact_and_singleton=true
transport_active_q_columns=2,3,...,14,16,...,24
all_q_direct_qprime_batched_omission_control=true
FIRST_conormal_rank=0/22
genuine_P12_source_compiler=true
raw_base_terms=2893
P12_source_row_omission_negative_control=true
lambda_prime_aggregate_omission_negative_control=true
lambda_prime_active_directions=2,3,...,14,16,...,24
all_q_derivative_source_identities_exact=true
all_q_denominator_radicals_subset_U_H_B3=true
```

V78B first kernels are the 22-dimensional standard basis of `I`
(22 lines; SHA `ef4d3be8…`); first conormal remains the same empty
header `b1b1f698…`.  Square-zero already kills `eps_i eps_j`.  Column
agreement therefore says the joint compiler's per-coordinate P12
remainder equals the singleton-compiler remainder, including on the
shards that zero `qd.B`.  Dual-host equality (Finding 3, and the two
V78B tables against each other) does not use that comparison.
Simultaneous-versus-shard equality does not use host identity.  Both
gates are independently closed.

The frozen reconciliation checker prints `TD6 V78B/V78C
simultaneous-shard reconciliation PASS`.  Again the byte identities
were re-hashed outside it.

**5. [Confirmed] Transport and first-row source typing, direct-q-prime
omission, the genuine 2,893-term P12 compiler, exact original-row lift,
varying multiplier/lambda-prime terms, and both omission controls hold
in source.  Fourteen lambda-prime rows on every coordinate, including
the high-jet zeros, block reading those zeros as omitted coefficient
variation.**

Transport is the reviewed V32 construction: f-transport `(15,60,3)`
from `{15: 1}`, g-transport `(25,100,5)` from `{1: 1, 25: 1}`, ordered
so non-`X` rows precede `X` rows, `factor_transport` rank `3470/3602`
with two events, 132 free parameters.  `source_vector_jet` injects
`ONE_VECTOR = r.t.source_vector(("g","X",0,1))` only on
`('g','X',0,e)` for `e` in the active `Q_EXPONENTS`.  Every active
exponent is required to appear once.  The matrix derivative is asserted
zero; the RHS derivative is retained.  Frozen stdouts print
`transport_rank=3470/3602` and
`transport_all_q_source_keys_exact_and_singleton=true`.

First rows are `qd.pack('X-2', qd.first_band_polynomials(...))` after
`configure_qd_jet`.  The batched omission `omit_direct=Q_EXPONENTS`
rebuilds those rows with no direct `Q_PRIME[e-1]` term.  For every
licensed `e`, the column digest changes (`positive_digest !=
omitted_digest`).  V78B prints 22 such lines; each shard prints the
matching singleton line.  The q2 shard and V78B agree on
`first_q2_column=221;omit=1;sha=240fe449…`.  The q16 shard and V78B
agree on `first_q16_column=222;omit=9;sha=2c0017a1…`.  First dual GE
pivots only on nonzero base value, rank `38/132`, dependent count 0,
`first_all_q_pivot_source_replay=true`.  Selected-minor q2 and q3
derivatives are asserted to be the zero element of `E` (serializer
`c0730fa1…`) whenever those coordinates are active.

Genuine P12 is `qd.compile_current(...)[12]`, not a staged N13
surrogate.  The base projection is required to have 2,893 terms and
digest

```text
8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da
```

matching frozen V32 / V43 / V57 / V77R.  All 44 shards and both V78B
runs print those two lines.  `divide_jet` against the original first
pivots, `lift_relations`, and `exact_source_replay` rebuild
`P12 - remainder` as `sum lambda_i * source_row_i` from those original
packed first rows.  Omitting the first nonzero relation fails the
replay (`P12_source_row_omission_negative_control=true`).  The base
remainder is the unit `-k/50` with
`k = 252 - 342 S + 144 S^2 - 36 S^3` and digest `93121eef…`, so dual
emptiness on this open is automatic.

For each active exponent the Leibniz split is computed in source:

```text
lambda_zero_bprime   = sum relation_base * source_column
lambda_prime_bzero   = sum relation_column * source_base
source_identity      = lambda_zero_bprime + lambda_prime_bzero
assert source_identity == raw_column - remainder_column
```

`lambda_prime_rows` counts first-rows with nonempty `relation_column`.
It is 14 on every licensed coordinate, matching V32's
`lambda_prime_source_row_support=14`.  Whenever `lambda_prime_bzero`
is nonempty the source asserts `lambda_zero_bprime != target` and
records the exponent in `lambda_prime_active_directions`.  That set is
exactly `I` on both V78B runs, and the singleton `{e}` on every shard,
including q16--q24.  High-jet zero remainders therefore still have a
nonzero lambda-prime summand reconstructing a 29--31 term raw column.
They are original-row syzygies, not omitted coefficient variation.

In-source q2 raw/remainder digests are asserted against the V32 pins.
q3 is emitted for V77R comparison (`q3_projection_emitted_for_pure_V77R_comparison=true`)
and matched post-hoc in Finding 6; it is not a second in-source digest
assert.  That is a pin-style difference, not a source-algebra hole:
the table cell is still the four-term / three-term object reviewed in
V77R.

**6. [Confirmed] q2 matches frozen V32 raw/remainder hashes.  q3
matches corrected, hostile-reviewed V77R.  Quarantined V77 is not used
as an authority.**

Union row 2:

```text
raw 816da33cd8e77b035740b7811e56d9ac8742160974a690506dec35d9b002d6a0
rem 1acfd5c0169b466d16c6d87de34b3ec0f5b78f6bb073a6191e9bed2ac36775b3
```

Both strings occur in frozen `evidence/anchors/V32_q2.stdout`
(`raw_beta_sha256=…`, `remainder_beta_sha256=…`; file SHA `13ced1e7…`).
V32 parent source is the pinned `dcc7003d…` file imported by both
producers.  V32 also carries the same 2,893-term base digest
`8d5c3550…` and `lambda_prime_source_row_support=14`.

Union row 3:

```text
raw 70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c
rem 3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458
```

Both strings occur in frozen `evidence/anchors/V77R_q3_box02.stdout`
(file SHA `9f3be97b…`).  The accompanying review
`evidence/anchors/V77R_review.md` is byte-identical to
`xmodel/td6_v77r_pure_q3_repaired_hostile_review_20260826.md` (SHA
`13e6df09…`) and ends on the standalone line `CONFIRMED`.  V77R source
typing is the singleton `('g','X',0,3)` plus direct `3 gamma t^2`, with
`qd.B` exact zero; the P12-gamma object is four raw terms and three
remainder terms, which is exactly union row 3.  Theorem V78/V78C
imports V32, not V77.  The unrepaired V77 sibling
`td6_c1_c2_c3_q3_gamma_dual_20260825/replay.py` (`5e088d8c…`) sits in
the archives unused.  The q3 comparison authority is V77R, not the
quarantined V77 case.

**7. [Confirmed] Every printed denominator radical lies in `{U, H, B3}`.
The open is not enlarged.**

Source `factors_only_allowed` accepts only Flint factors in
`(U, H, B3)` (units of `Q` permitted).  The assertion is executed on
the first-conormal denominator and on every P12 column LCM.  First
conormal prints `(1, [])`.  Every P12 row prints a factorisation of
the form

```text
(1/4, [ (U, a), (B3_poly, 1), (C - 3*U^2, 2) ])
```

or the same three atoms with `U` to power 2.  The printed sextic is
letter-for-letter the `B3` polynomial above; `C - 3*U^2` is `H`.
Parsing all 22 rows yields extra-atom set empty.  The unit `1/4` is in
`Q`.  Extra *powers* of `U` and `H` occur; extra *primes* do not.  The
supported open remains `D(U*H*B3)`.  Flint irreducibility of `B3` over
`Q` is not a V78 theorem and is not used.

**8. [Confirmed] Reduced genuine-P12 derivatives are nonzero on
`q2..q14` and exactly zero on `q16..q24`.  This is a P12 tensor
statement, not a claim about every current row or the nonlinear
family.**

From the common 23-line table, `remainder_terms` (column 4) is

```text
q2..q14 : 2,3,5,7,12,17,17,17,17,17,17,17,17   (all > 0)
q16..q24: 0,0,0,0,0,0,0,0,0
```

The nine high-jet remainder digests are the common empty-polynomial
value `2e38e77b…`.  Raw columns on those nine rows still have 29--31
terms with distinct nonzero digests, so the *unreduced* P12 derivative
is not zero; the *reduced* remainder after original-row division is.
Both V78B stdouts print the same 22 `q{e}_raw_terms=…;remainder_terms=…`
lines; each shard prints its singleton, matching the union row.  First
conormal is zero in every basis direction (`0/1` per shard, `0/22`
jointly).  The producer sentence “sharp degree-14 cutoff for this P12
adjoint/source-support tensor” is therefore exact, and is not a
statement that q16--q24 vanish in other current rows, in staged
previous/pole compatibility, or in a nonlinear q-neighborhood.

**9. [Confirmed] Scope is first-order/source-support evidence on the
already-empty fixed A3 open `D(U*H*B3)`.  No nonlinear q-neighborhood,
q-family, all-beta-away-from-fixed-A3, full TD6, SP-2, or JC2
implication is licensed.**

Every theorem stdout prints

```text
scope_open=D(U*(C-3U^2)*B3)
dual_base_ideal_already_unit=true
result_use=tangent_conormal_and_source_support_discriminator_only
base_q2_beta=0
source_center=(C,V,U)
```

The unit base remainder `-k/50` makes square-zero emptiness automatic
on this open; that is not a family theorem.  Both producer reports and
both case READMEs state the same firewall.  Staged-mode flags
`all_q_tangent_family_killed=false` / `whole_TD6_killed=false` /
`SP2_killed=false` / `JC2_resolved=false` are not even on the p12
path that was run.  V76 already emptied the base ideal on
`D(U*H*B3)`; this package is a source-support discriminator at that
empty base, nothing more.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. `replay_shard.py` still carries the simultaneous module docstring.
   Executable `Q_EXPONENTS`, the launcher, stdout, and tables already
   identify a singleton.  Patch the docstring on the next source freeze
   so a later reader cannot mistake prose for the ring.

2. `run_v78c_shard.sh` is a weaker AWS preflight than `run_v78b.sh`: it
   checks Linux and the registered tag, but not `hostname ip-*` or EC2
   DMI, and it does not run `sha256sum -c SOURCE.sha256`.  Actual hosts
   were the same two AWS instances as V78B, launch metadata pins the
   archive SHA, and dual-host products agree.  Adding the V78B
   preflight to the shard wrapper would make the two packages
   custody-identical.

3. The frozen V78C checker does not read `aws_platform` / tag / hostname
   (it does read cap, timeout, archive SHA, rc, PASS, union, anchors).
   Those fields were checked independently here.

4. The V78B tarball's unused sibling
   `td6_c1_c2_c3_q3_gamma_dual_repaired_20260825/replay.py` hashes to
   `17388682…`, not the hostile-reviewed V77R file `7a961c02…` carried
   in the V78C archive.  V78B does not import that sibling.  The q3
   authority used here is the V77R stdout and `CONFIRMED` review frozen
   under V78C `evidence/anchors/`.  Aligning the unused sibling on a
   later freeze would remove a custody mismatch that is not on the
   theorem path.

5. q2 matching V32 is an in-source digest assert.  q3 matching V77R is
   a table-versus-anchor comparison plus the print
   `q3_projection_emitted_for_pure_V77R_comparison=true`.  Both matches
   hold.  An in-source q3 digest assert, parallel to q2, would make the
   two anchors the same kind of pin.

---

## Independent discharge

- **Dual-host equality** is discharged by the 44 pairwise-identical
  shard products and by the two independently assembled 23-line unions,
  both SHA `e14ff29c…`, on Box02 versus r6d.  The two V78B simultaneous
  tables are a second, separate dual-host identity on the same two
  hosts.
- **Simultaneous-versus-shard equality** is discharged by comparing
  those V78B tables to both V78C unions.  All four frozen byte strings
  are identical.  That comparison does not use host identity, and the
  dual-host comparison does not use the V78B simultaneous compiler.

---

## Strongest exact theorem that survives

On the fixed source-typed A3 chart, over the square-zero extension in
the 22 licensed coordinates `q2,...,q14,q16,...,q24` (q15 excluded as
the lower target-shear gauge of `p=t^{15}`), localized on
`D(U*(C-3U^2)*B3)`, the first-stage conormal map is the zero map and
the genuine-P12 reduced remainder, lifted against original first rows,
has support exactly through q14.  Directions q16--q24 are exact P12
source syzygies: their reduced remainder is empty while 14 lambda-prime
rows remain active.  Denominator radicals are contained in `{U,H,B3}`.
The 22 singleton V78C columns, assembled independently on two AWS
hosts, equal the 22-column V78B simultaneous table on those same two
hosts; the common table SHA256 is
`e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef`.
q2 matches frozen V32; q3 matches corrected hostile-reviewed V77R.
Dual emptiness on this open is automatic from the unit base remainder.
Nothing is claimed about a nonlinear q-neighborhood, a q-family, other
current rows, all-beta away from this fixed A3 source, full TD6, SP-2,
or JC2.

---

CONFIRMED
