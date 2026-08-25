# Hostile review: TD6 V68 B3 chart-boundary factor routes

Referee: independent algebraic/source/custody pass of the frozen V68
route lemma only.  Operations used: full read of the charged surfaces
and of every named or hash-pinned direct-source package, plus the V66
B3 chart package whose exceptional factors V68 routes.  Polynomial
identities were expanded by hand.  Marker strings in frozen stdout
were compared by reading, not by hashing.  No Bash, no `tar` extract,
no `hashlib`, no `verify.py` execution, no producer execution, no CAS,
no network.  Stored PASS strings are not authority.  Anything that
would require shell execution is flagged as not independently rerun.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_b3_boundary_factor_routes_v68_aws_20260825/`.

Named / hash-pinned direct sources inspected:
`cases/td6_c1_c2_c3_q2_beta_u_zero_aws_20260825/` (V33 frozen `U0=0`);
`cases/td6_c1_c2_c3_q2_beta_rational_raw_lines_aws_20260825/` (V46
`C0=-U0^2` and V45 `C0=-5U0^2`);
`cases/td6_c1_c2_c3_q2_beta_u_zero_canonical_digest_v69_aws_20260825/`
(digest nondeterminism diagnosis; not a V68 pin).

V66 chart package:
`cases/td6_c1_c2_c3_q2_b3_source_dag_repaired_v66_aws_20260825/`.

Same line-pencil identity already lives in the unpacked B3-chart
source `audit_b3_parameterization` (trivariate snapshot v27).  V68 is
a route/dependency wrapper around that identity, not a new B3 chart.

Producer actually executed on AWS: `timeout 120 /usr/bin/python3
route_replay.py` from the staging tarball whose SHA is recorded as
`87675102…`.  Elapsed 0.03–0.05 s, RSS ~16 MiB.  That runtime is
incompatible with any rerun of the `U0=0` or rational-line source
theorems.  Live `route_replay.py` exists only inside the gzipped
archive and was not read in this no-Bash review.

---

## Charge 1 — Normalized identity and specializations

**Result: the identity holds as a polynomial identity in `Q[x,t]`.
The three specializations are correctly stated, with the chart
denominators recorded below.  The stdout banner
`t_zero_route=x_minus1_or_x_minus5` is a naming label for `x=-1` or
`x=-5`, not a test of `(x-1)(x-5)`.**

On `D(U0)` the V68/V66 normalization is

```text
x = C0/U0^2,   y = V0^2/U0^3,   w = V0/U0,
t = y/(x+5),
b(x,y) = 4x^2 - 4xy + 24x + y^2 - 20y + 20.
```

This is `B3/U0^6` for the raw polynomial
`B3 = 4C^2U^2 - 4CV^2U + 24CU^4 + V^4 - 20V^2U^3 + 20U^6`
(even in `V`).  Substituting `y = t(x+5)` and expanding:

```text
x^2:  t^2 - 4t + 4
x:    10t^2 - 40t + 24
1:    25t^2 - 100t + 20
```

The claimed right-hand side
`(x+5)((t-2)^2 x + 5t^2 - 20t + 4)` expands to the same three
coefficients.  Equality is in `Q[x,t]`; no inversion is used.

Specializations, as polynomials:

- `t=0`: `b(x,0) = 4(x+1)(x+5)`.  Zeros `x=-1` and `x=-5`.  README
  statement `4(x+1)(x+5)=0` is exact.  The printed marker name
  `x_minus1_or_x_minus5` means those two roots, not `(x-1)(x-5)`.
  If the live test had used `(x-1)(x-5)` the identity would fail and
  dual-host `rc=0` would be impossible unless the test were vacuous.
- `t=2`: `b(x,2(x+5)) = -16(x+5)`.  Only `x=-5`, hence `y=0`.
- `w=0` on `D(U0)`: `w=V0/U0` so `V0=0`.

Chart / denominator assumptions, which V68 does not erase:

- `x,y,w` and `B3 = U0^6 b` require `D(U0)`.
- The inverse `t = y/(x+5)` requires `D(U0)` and `D(x+5)`, i.e.
  `C0+5U0^2 ≠ 0`.  At `x=-5` one has `b(-5,y)=y^2`, so the only
  affine `b=0` point on that vertical is `(x,y)=(-5,0)`, already on
  `V0=0`, `C0=-5U0^2`.
- The V66 birational formulae themselves have denominator `t^2` and
  are declared open only on `D(t*w*(t-2))`.  V68 does not substitute
  the exceptional values into those formulae (they blow up).  It
  specializes the polynomial line-pencil identity and the raw
  `V0=0` factorization instead.

V66 already printed `B3_line_intersection_factorization=true` and
the same line-factor identity in `audit_b3_parameterization`.  V68
re-asserts it as a dedicated route certificate.

**Defects.**  None in the algebra.  Banner `x_minus1_or_x_minus5` is
ambiguous English; the README polynomial is the authority.

**Survival.**  The normalized identity and all three specializations
survive independent expansion.

---

## Charge 2 — Raw `V0=0` identity and omitted finite branches

**Result: the raw identity holds in `Q[U0,C0]`.  No finite
raw-center branch is omitted when translating back from
`(x,y)`.**

Set `V0=0` in `B3`:

```text
B3 = 4 C0^2 U0^2 + 24 C0 U0^4 + 20 U0^6
   = 4 U0^2 (C0^2 + 6 C0 U0^2 + 5 U0^4)
   = 4 U0^2 (C0+U0^2)(C0+5U0^2).
```

This is a polynomial identity, no localization.  V45/V46 source
asserts the same equality on the generic symbols `(C,U)`.

Translation from normalized coordinates:

1. On `D(U0)`, `B3=0` iff `b=0`.  `B3` is even in `V0`, so the
   squaring `y=V0^2/U0^3` loses no odd-`V0` component.
2. `t=0` on `D(U0)`: `y=t(x+5)=0` so `V0=0`, and `b(x,0)=0` so
   `x=-1` or `x=-5`, i.e. the two `V0=0` lines.
3. `w=0` on `D(U0)`: `V0=0`, then the raw identity yields
   `U0=0` (excluded from this chart) or the same two lines.
4. `t=2` on `D(U0) ∩ D(x+5)`: `b=-16(x+5)≠0`.  Empty interior.
   The closure is the base point `(x,y)=(-5,0)`, i.e.
   `V0=0`, `C0=-5U0^2`.  Independently, V66 records that the chart
   formulae at `t=2` collapse to the origin, which sits in `U0=0`
   (and on both lines).  V66 also records
   `b(-5,y)=y^2` and “other intersection at projective infinity”.
5. `U0=0` is not in the `(x,y)` chart and is listed as a target,
   not swept under the rug.

Finite-point census: every finite raw zero arising from `t=0`,
`w=0`, or `t=2` lands in

```text
U0=0
  ∪  {V0=0, C0=-U0^2}
  ∪  {V0=0, C0=-5U0^2}.
```

Points at projective infinity are outside the stated finite-debt
claim.  The origin is in every member of the union.

**Defects.**  None.

**Survival.**  The raw identity and the finite-branch translation
survive independent expansion.

---

## Charge 3 — These three are exactly V66 factor debts; `2t-1`
and `t^2-4t+2` are not covered

**Result: holds, as a citation of frozen V66 artifacts plus
independent specializations of the V68 identity.  V68 does not
hash-pin V66.**

V66 leaf-plus-P12 radical, after the documented rename
`(C,V)→(t,w)`, is exactly

```text
{t, w, t-2, 2t-1, t^2-4t+2}.
```

Witnesses, byte-identical on Box02 and r6d:

- `DAG_leaf_denominator_factor_set=['2*C - 1', 'C', 'C - 2', 'C^2 - 4*C + 2', 'V']`;
- `B3_parameter_open_requires=t*w*(t-2)!=0`;
- `raw_denominator_factor_strata_still_charged=true`;
- `whole_raw_stratum_killed=false`.

So `t=0`, `w=0`, `t=2` are three of the five V66 debts, and they
are exactly the three poles of the chart formulae / chart open.
The remaining two are finite DAG factors, not chart-parameter
poles.

V68 does not silently cover them.  Independent specializations of
the same line-pencil identity:

- `t=1/2`: `b = (1/4)(x+5)(9x-19)`.  The extra branch `x=19/9`
  has `y=(1/2)(x+5)=32/9 ≠ 0`, hence `V0≠0` on `D(U0)`, not in
  the target union.
- `t^2-4t+2=0`: `b = 2(x+5)(x-3)`.  The extra branch `x=3` has
  `y=8t` with `t=2±√2 ≠ 0`, again `V0≠0`.

V68 stdout prints `whole_B3_killed=false` and
`route_target_union=U0_zero_union_(V0_zero_C0_plus_U0sq_zero)_union_(V0_zero_C0_plus5U0sq_zero)`.
README and xmodel both name `2t-1` and `t^2-4t+2` as V67
obligations.  No V67 package exists in-tree.

**Defects.**  V68 hash-pins the three *target* stdout files, not
the V66 ledger/DAG whose factor list it routes.  Identification of
`{t,w,t-2}` as V66 debts is documentary (this review read V66),
not a V68 freeze entry.  That is a custody gap, not an algebraic
error.

**Survival.**  The three named factors are V66 debts; the other
two are not routed.

---

## Charge 4 — Frozen dependency hashes and marker checks vs
source algebra; `U0=0` digest nondeterminism

**Result: V68 is a hash/marker dependency audit, not an
independent rerun of the three source theorems.  It pins the
immutable V33 `U0=0` stdout and does not promote V69 or the
cross-host noncanonical mirrors.**

`verify.py` is a custody/marker gate: archive SHA, dual-host
`rc=0`, byte-identical stdout SHA `c84447f9…`, per-host stderr
SHAs, identical `source-check.txt` SHA, five archive-member SHAs
(`SOURCE.sha256`, `route_replay.py`, three evidence stdouts), then
`assert marker in out` for thirteen banners.  It never imports a
source producer and never divides a polynomial.  Dual-host runtime
0.03–0.05 s / ~16 MiB RSS independently shows the same: V68 cannot
have rerun V33/V45/V46.

Hash-pin *strings* in `verify.py` match the original packages’
MANIFEST/README claims:

| pinned member | SHA256 prefix | original package |
|---|---|---|
| `evidence/u_zero/n13-u-zero.stdout` | `94e2267d…` | V33 `U0=0` MANIFEST / README |
| `evidence/rational_lines/v46.stdout` | `01fa0f2e…` | rational-lines MANIFEST / README (`V=0,C=-U^2`) |
| `evidence/rational_lines/v45-v-cplus5-zero.stdout` | `0be0c409…` | rational-lines MANIFEST / README (`V=0,C=-5U^2`) |

Those SHA256 values were **not** independently recomputed here.
String-level consistency across packages is all this no-Bash
review licenses.

Markers actually present in those frozen stdout files, matching
V68’s claimed source-audit (this is a read of the original
packages, not of the copies inside the unreadable archive):

- `U0=0` (V33): `first_original_row_replay=true`,
  `first_compatibility_gcd_degree=0`,
  `first_compatibility_certificate_denominator=(1)`,
  `first_incompatibility[0]_key=('X-2', 14)`,
  PASS `TD6-A3-Q2-N13-RAW-FIRST`.  No
  `direct_qprime_omission_negative_control` line (only
  `direct_qprime_retained=true`).
- `C0=-U0^2` (V46): `source_center=V=C+U^2=0 over Q(U)`,
  `first_full_beta_P12_original_row_replay=true`,
  `first_full_beta_P12_compatibility_gcd_degree=0`,
  `first_full_beta_P12_compatibility_original_row_replay=true`,
  `first_full_beta_P12_unit_certificate_denominator=(U^6)`,
  `direct_qprime_omission_negative_control=true`,
  PASS `TD6-A3-Q2-CPLUS1-FIRST-UNIT-INCOMPATIBILITY-CANONICAL`.
  Unpacked V46 `replay.py` *returns before* the
  `P12_without_N13` block (dead code after `return`).  That
  control is **not** live on this line.
- `C0=-5U0^2` (V45): `source_center=V=C+5U^2=0 over Q(U)`,
  `full_beta_first_original_row_replay=true`,
  `remainder_base_is_minus_k_over_50=true`,
  `combined_unit_residual_is_minus_k_over_50=true`,
  `P12_without_N13_negative_control=true`,
  `direct_qprime_omission_negative_control=true`,
  `P12_compiler=genuine_2893_term_source_polynomial`,
  PASS `TD6-A3-Q2-FULL-P12-N13-UNIT-RATIONAL-RAW-CANONICAL`.

xmodel’s phrase “available direct-q-prime/P12 omission controls”
is accurate.  README’s sentence “The two rational-line certificates
include direct q-prime and P12-without-N13 negative controls”
overstates: both have q-prime omission; only `Cplus5` has live
P12-without-N13.

**`U0=0` internal-digest nondeterminism.**  V69 diagnoses that V33
hashed `repr(E3)` with process addresses.  Fresh noncanonical
Box02/Box03 predecessors in the V69 package agree with V33 on every
mathematical marker (ranks `3470/3602` and `36/132`, key
`('X-2',14)`, degree 0, denominator `1`, original-row replay, PASS)
and disagree on the six printed digests:

```text
first_pivot_digest
  V33 frozen   ae2f4f6e…
  Box02 fresh  06dac00d…
  Box03 fresh  5a2556f1…
```

and likewise for residual / source-certificate / Bezout / gcd
digests.  V69’s repaired canonical stdout is `9726fb09…`.  V68 pins
`94e2267d…` (V33 frozen bytes) and does not mention `9726fb09…`.
That is the correct freeze discipline: immutable predecessor, not a
fresh mirror and not the V69 reporter repair.

This review did not see `route_replay.py`, so it cannot list the
exact marker predicates.  Given the runtime, those predicates are
string searches on the frozen files, not a live `U0=0` rebuild.
They must not compare the six noncanonical digest lines against a
fresh rerun; nothing in the readable V68 surfaces does so.

**Defects.**  Hash values themselves were not recomputed.  V66 is
named but not pinned (Charge 3).  README P12-without-N13
overclaim (documentary).

**Survival.**  V68 is a pin/marker wrapper of frozen source
certificates.  It does not promote nondeterministic `U0=0` mirrors.

---

## Charge 5 — Wrong-coefficient, missing-branch, marker-omission
controls

**Result: the three banners printed `true` on both hosts.  Live
control bodies were not read (producer is only in the gzipped
archive).  Intended failures can be stated from the identities;
this review cannot certify that the executed tests are those
tests rather than tautologies.**

Stdout, both hosts:

```text
route_wrong_coefficient_negative_control=true
route_missing_branch_negative_controls=true
source_marker_omission_controls=true
```

`verify.py` only checks that those strings occur.  That is not a
test that the controls fire on the intended mutants.

What a correct implementation *must* detect, given Charges 1–2:

- Wrong coefficient: e.g. replace `4` by `5` in
  `B3|_{V0=0}=4U0^2(C0+U0^2)(C0+5U0^2)`, or replace `(t-2)^2` by
  `(t-1)^2` in the line-pencil identity.  Either perturbation
  breaks equality in `Q[…]`.
- Missing branch: `t=0` is not `4(x+1)` alone and not `4(x+5)`
  alone; `V0=0` is not `4U0^2(C0+U0^2)` alone and not
  `4U0^2(C0+5U0^2)` alone; `t=2` is not the empty set on the
  affine plane (the base point remains).
- Marker omission: deleting
  `first_original_row_replay=true`,
  `first_compatibility_certificate_denominator=(1)`,
  `combined_unit_residual_is_minus_k_over_50=true`, or a PASS
  line from a copy of a pinned stdout must fail the dependency
  gate.  A control that only checks “stdout is nonempty” does
  not detect the intended failure.

Unpacked V45/V46 `replay.py` *source-theorem* controls (not V68’s)
are inspectable and do real work: q-prime omission is
`assert first_rows_omit != first_rows`; Cplus5 P12-without-N13 is
`assert clean(first_source_identity) != clean(target)` after the
combined identity.  Those are the target theorems’ controls, not
V68’s route controls.

**Defects.**  V68 did not unpack `route_replay.py` next to
`verify.py`, unlike the rational-lines package.  Under the
no-Bash charge this makes Charge 5 unclosed as a live-code
audit.

**Survival of the route lemma.**  Independent of whether V68’s
regression tests are live: Charges 1–3 do not depend on those
banners.

---

## Charge 6 — Exact scope

**Result: the charged surfaces do not license a whole-B3,
whole-A3, TD6, SP-2, landing, or JC2 claim.  Source-theorem
review status and the two finite factors remain separate.**

Readable scope quarantine:

- V68 xmodel: “producer-exact route/dependency theorem, not an
  independent replay of every source certificate and not a
  whole-B3 theorem”; “two finite B3 factors remain V67
  obligations”; status
  `PRODUCER-EXACT ROUTE / HOSTILE REVIEW PENDING / NO WHOLE-B3 CLAIM`.
- V68 README: does not cover `2t-1` or `t^2-4t+2`; does not
  replace producer/review status of the three targets.
- V68 stdout / `verify.py`: `whole_B3_killed=false`,
  `exact_scope=route_of_t0_w0_t2_into_U0_and_two_V0_lines`,
  `whole_B3_cover_complete=false`.
- Each target package already prints
  `full_A3_beta_family_killed=false`, `whole_TD6_killed=false`,
  `SP2_killed=false`, `JC2_resolved=false`.
- V66 prints `raw_denominator_factor_strata_still_charged=true`
  and `whole_raw_stratum_killed=false`.

Independent AWS mirrors of the three target strata, mentioned in
the xmodel, are not V68 evidence and were not inspected as V68
outputs.

Hostile-review status of the targets, as of this reading:

- V33 `U0=0`: producer-exact, hostile review pending (no grok
  review file in-tree).  V69 is a reporter/custody repair of the
  same theorem, also pending review of the underlying result.
- V45/V46 rational lines: producer-exact, hostile review pending.
- V66 B3 chart DAG: producer-exact, hostile review pending.

V68 does not close any of those reviews.

**Defects.**  None of scope overreach on the charged surfaces.

**Survival.**  Only the narrow route lemma is licensed by V68
alone.

---

## Charge 7 — MANIFEST / FREEZE design and AWS custody

**Result: two-layer freeze design is coherent on a read of the
text files.  Dual-host `rc=0` and byte-identical stdout are
directly visible.  Archive SHA, member SHAs, and `verify.py`
were not independently rerun.  The 1 GiB cap is README-only.**

MANIFEST lists the case payload: README, the v68 tarball, seven
Box02 files, seven r6d files, `verify.py`.  It does not list
`FREEZE.sha256` or the xmodel file.  FREEZE lists MANIFEST,
README, `verify.py`, and the xmodel checkpoint.  README SHA
`8db8dd12…` and `verify.py` SHA `23fb294f…` are the same strings
in both files.  This is the same two-layer pattern as V66.
FREEZE does not directly pin the archive; MANIFEST does.  That is
the intended split.

AWS readable evidence:

- Both `archive.sha256` files contain `87675102…` and a *staging*
  path `/home/ubuntu/stage/td6_v68_b3_routes_20260825T1532Z.tar.gz`,
  not the frozen basename `td6-aws-handoff-20260825-v68.tar.gz`.
  Same hash, different filename.  Permissible if the bytes match;
  bytes were not hashed here.
- Both `rc` files are the two bytes `0\n`.
- Box02 and r6d `v68.stdout` are the same 15 lines of text
  (read-equal, not hashed).  Claimed SHA `c84447f9…` was not
  recomputed.
- `source-check.txt` is read-equal on both hosts: eleven members
  `: OK`, including `route_replay.py` and the three evidence
  stdouts plus FREEZE/MANIFEST/report.md wrappers.  It does not
  list `SOURCE.sha256` as a checked path (normal for
  `sha256sum -c SOURCE.sha256`).  `verify.py` additionally pins
  `SOURCE.sha256` content `c4152092…`.
- stderr is `/usr/bin/time -v` of
  `timeout 120 /usr/bin/python3 route_replay.py`, Exit status 0.
  Box02 0.03 s / 16572 KiB; r6d 0.05 s / 16348 KiB.  The 120 s
  timeout is in-artifact.  The README “1 GiB” cap is not.
- Box02 `start_utc=end_utc=2026-08-25T15:25:36Z`; r6d both
  `15:25:53Z`.  Same-second stamps are consistent with a 0.03 s
  job.

Not independently rerun in this review (would need Bash or
equivalent): archive extract, SHA256 of any file, `python3
verify.py`, `route_replay.py`, AWS `sha256sum -c`.

**Defects / nits.**  1 GiB cap is README-only.  Staging tarball
name differs from the frozen basename.  `verify.py` does not
assert the `route_target_union=…` line (other markers already
carry the claim).  Producer source is not unpacked in the case
directory.

**Survival.**  Dual-host rc 0 and read-identical stdout survive as
readable custody.  Hash closure does not survive this no-Bash
pass as an independent recomputation.

---

## Leftover nits (not load-bearing for the route lemma)

1. Marker `t_zero_route=x_minus1_or_x_minus5` / `t_two_route=x_minus5_only`
   names roots `x=-1,-5`, while the README writes `(x+1)(x+5)`.
2. README overclaims live P12-without-N13 on both rational lines.
3. V68 does not hash-pin the V66 ledger SHA `fc655dea…` or DAG SHA
   `3751f623…`.
4. `verify.py` is a marker gate, not an algebraic replay.
5. Independent AWS mirrors of the three target strata are status,
   not V68 evidence.
6. V45/V46 `legacy_object_address_digest_used=false`; V33 `U0=0`
   is the digest-unstable predecessor.  V68 pins the latter’s
   frozen bytes, which is correct, but a reader could confuse
   V33 internal digest lines with portable hashes.

---

CONFIRMED

Strongest statement licensed: in the frozen V66 B3 birational
chart of the fixed source-typed A3 q2-beta section, after the
documented rename `(C,V)→(t,w)`, the chart-boundary factors
`t=0`, `w=0`, and `t=2` have their complete finite raw-center
debt inside the union

```text
U0=0
  ∪  {V0=0, C0=-U0^2}
  ∪  {V0=0, C0=-5U0^2}.
```

This is a producer-exact route/dependency lemma: the line-pencil
and raw-`V0=0` identities hold independently, and V68 hash-pins
(as declared strings) the frozen V33/V46/V45 stdout files for
those three targets together with dual-host duplication of the
route script.  It is not a replay of the source algebra, not a
whole-`B3=0` theorem, and it does not cover `2t-1` or
`t^2-4t+2`.

Residual obligations (no theorem-blocking producer repair is
required for the route lemma itself):

1. Hostile review of the V33 `U0=0` source theorem remains
   pending.  V69 repairs only digest custody of that same
   theorem and is not a V68 pin.
2. Hostile review of the V46 `V0=0,C0=-U0^2` and V45
   `V0=0,C0=-5U0^2` source theorems remains pending.
3. Hostile review of V66 (generic-chart DAG, five-factor radical)
   remains pending.
4. The finite V66 factors `2t-1` and `t^2-4t+2` remain V67 (or
   successor) source-rebuild obligations.
5. Live V68 negative-control bodies were not read in this
   no-Bash pass.  Optional custody improvement: unpack
   `route_replay.py` beside `verify.py` so a no-shell review can
   inspect them.
6. SHA256 values declared by MANIFEST/FREEZE/`verify.py` were not
   independently recomputed here.  Optional: pin V66 ledger/DAG
   hashes next to the three target stdout pins.
7. Documentary: tighten the README sentence on P12-without-N13
   so it matches the xmodel (“available” controls) and the live
   V46 control set.
8. No whole-B3, whole-A3, TD6, SP-2, landing, or JC2 claim is
   licensed by V68, nor by composing V68 with unreviewed source
   certificates.
