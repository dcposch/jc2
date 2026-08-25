# Hostile review: TD6 V67 finite B3 factor source DAGs

Referee: independent algebraic/source/custody pass of the frozen V67
factor-open source-DAG claim only.  Operations used: full read of the
charged surfaces and of the named V66/V68 producer reports; `tar`
extract of the frozen 137 KiB archive into
`/tmp/td6-v67-review-25151/`; independent SHA256 via Python `hashlib`;
structural inspection of curve-field typing, center/inverse identities,
N13 previous-edge selection, genuine-P12 first-only lift, every emitted
leaf/stage/chart denominator, dual-host bytes, and both q-prime-omission
streams; hand expansion of the printed center map, its inverse, and the
raw `B3` identity.  No producer execution, no CAS, solver, Lean, or
other substantive computation.  Stored PASS strings are not authority.
The lightweight `verify.py` was inspected as a marker/custody script
and then run as a short standard-library check; it never imports
`replay.py` and never divides a polynomial.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-b3-finite-factors-v67-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_b3_finite_factors_v67_aws_20260825/`.

Named provenance (read only as needed):
`xmodel/td6-c1-c2-c3-q2-b3-source-dag-repaired-v66-aws-20260825.md`
with frozen case
`cases/td6_c1_c2_c3_q2_b3_source_dag_repaired_v66_aws_20260825/`
(five-factor generic-chart radical; hostile review pending);
`xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-aws-20260825.md`
and its grok review
`xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-review-grok-20260825.md`
(verdict `CONFIRMED` that `t=0`, `w=0`, `t=2` route into
`U0=0` and the two `V0=0` lines, and that `2t-1` and
`t^2-4t+2` are not routed).

Producer actually executed, from frozen stderr of the four rc-zero
runs and the two rc-one controls:

```text
timeout 21600 ./run_v67.sh b3half
timeout 21600 ./run_v67.sh b3tq
timeout 21600 ./run_v67.sh b3half omit-direct-qprime
timeout 21600 ./run_v67.sh b3tq omit-direct-qprime
```

Expanded tree basename `td6-aws-handoff-20260825-v67` matches the
tarball name.  Launch metadata records a 12 GiB cap on every run.
V65 `main()`, V63 `main()`, `n13_curve_quotient.main()`, and
`p3_quotient.main()` are not called.

Import/hash pin chain executed by that producer, in order:

1. `run_v67.sh` execs
   `td6_c1_c2_c3_q2_b3_factor_source_dag_repaired_v67_20260825/replay.py`
   (`ada47c39…`, independently recomputed).
2. V67 pins and imports
   `c1_c2_c3_p3_quotient.py`
   (`CURVE_SHA256=f8c46d2c…`) and asserts `COMPONENT in {"b3half","b3tq"}`.
3. That file pins and imports
   `c1_c2_c3_trivariate.py` (`3459dda5…`).
4. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
5. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `V67_SOURCE.sha256` as `ce400cca…`);
   pencil then pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

V67 `replay.py` is a line-level fork of V65 `replay.py` (1160 vs 1163
lines).  The executed DAG/P12/N13 machinery is the V65 repaired
source-DAG, with `center_and_audit()` swapped from the H=P3/QH
centers to the B3 factor parameterization.  V65
`curve_source_dag_repaired_v65` `replay.py` (`de57451b…`) is listed
in `V67_SOURCE.sha256` as sibling text and is not imported.
`run_v67.sh` is the only entry that can produce this case.

---

## Charge 1 — Exact components, center map, inverse, raw `B3`, degrees

**Result: holds.**  The two source components are exactly `2t-1=0`
over `Q(w)` and `t^2-4t+2=0` over `Q(t)(w)`, in the fixed
source-typed A3 q2-beta section.  The center map and its inverse
are identities on `D(w)` of those fields.  `t` is a unit and is
not 2 on either component.  No point sampling of `w` or of the
quadratic root is used.

The parent field is `Q(U)[Z,V]/(Z^2-aZ-b, V^2-Y U^3)` with
`U_POLY=x` the univariate generator.  Mode data:

| mode | `a,b` | `Y` | `t` | claimed degree over `Q(U)` |
|---|---|---|---|---|
| `b3half` | `0,2` (dummy `Z^2=2`) | `1` | `1/2` in `Q` | 1 |
| `b3tq` | `4,-2` | `1` | `Z` with `Z^2-4Z+2=0` | 2 |

V67 never uses the dummy outer square root `V_CURVE`.  It sets
`w=U_CURVE` and

```text
x_weight = (-5t^2+20t-4)/(t-2)^2
y_weight = 16t/(t-2)^2
U0 = w^2/y_weight = w^2 (t-2)^2/(16t)
V0 = w^3/y_weight = w^3 (t-2)^2/(16t)
C0 = x_weight w^4/y_weight^2
   = w^4 (t-2)^2 (-5t^2+20t-4)/(256 t^2).
```

This is the V66 birational chart, specialized.  Live asserts:
`2t-1=0` or `t^2-4t+2=0`; `V0/U0=w`; `C0/U0^2=x_weight`;
`V0^2/U0^3=y_weight`; `y_weight/(x_weight+5)=t`; raw

```text
B3 = 4 C0^2 U0^2 - 4 C0 V0^2 U0 + 24 C0 U0^4 + V0^4
     - 20 V0^2 U0^3 + 20 U0^6
```

equals zero, and `B3+1` does not.

Independent expansion, no CAS:

- `x_weight+5 = 16/(t-2)^2`, so
  `y_weight/(x_weight+5)=t` wherever `t≠2`.  No extra inversion.
- On the V66/V68 line-pencil identity
  `b(x,y)=(x+5)((t-2)^2 x + 5t^2-20t+4)`, the point
  `(x,y)=(x_weight,y_weight)` makes the second factor identically
  zero.  Hence `B3=U0^6 b=0` on this parameterization for every
  `t≠0,2`, and in particular on both components.
- `t=1/2`: `t≠0`, `t-2=-3/2≠0`, and
  `t^2-4t+2=1/4≠0`.
- `t^2-4t+2=0`: roots `2±√2`.  Product 2, so neither is 0.
  `(t-2)^2=2≠0`.  `2t-1=3±2√2≠0`.

Coefficient-field degrees match the parent declarations.  Dummy
adapters are inert on the live inputs: `t=1/2` and `w=U_RAT` have
`Quad.b=0` and `Curve.b=0`; addition, multiplication, and inverse
of a `Curve.b=0` element stay in that subfield.  For `b3tq` the
`Quad.b` direction is the genuine `t`.  The unused
`p3_quotient.main()` subfield-descent block is therefore not
load-bearing for this charge.  Arithmetic is exact in
`Q(w)` / `Q(t)(w)`, not evaluation at a numerical `w` or at a
floating `2±√2`.

V66 already printed the same chart, with radical
`{t,w,t-2,2t-1,t^2-4t+2}` after the documented rename
`(C,V)→(t,w)`.  V68 independently showed that `2t-1` and
`t^2-4t+2` are not the chart-boundary factors.  V67 does not
hash-pin V66; identification of these two as the remaining finite
debts is documentary.

**Failed attacks.**  Incorrect curve field: the dummy `Z^2=2` on
`b3half` and dummy `V^2=U^3` on both modes are type adapters, not
the raw center.  Invalid inverse: the four inverse identities
expand in `Q(t)(w)` on `D(t(t-2)w)`.  Missing affine point at
infinity of the `w`-line is outside `D(w)` and is not claimed.

**Defects.**  None in the algebra.  V66 is named, not pinned.

**Survival.**  Both specialized charts and the raw `B3` identity
survive independent expansion.

---

## Charge 2 — Curve parameter `w=V0/U0` versus raw center `U0`

**Result: holds.**  The implementation generator `x` / legacy
`U_POLY` is the curve parameter `w`, not raw `U0`.  Asserted
scope is `D(w)`.  `w=0` is the raw origin and is not consumed.

`RTShim.X = U_CURVE` and `w = p.U_CURVE`.  Every collected leaf
factor is compared to `str(p.U_POLY)`, printed as `x`.  Stage
denominator `x^11` and complete charts `x^27` / `x^23` are
therefore powers of `w`.  Raw `U0 = w^2 (t-2)^2/(16t)` is a
computed center coordinate, never the polynomial generator.

On either component `(t-2)^2/(16t)` is a unit, so
`U0` is a unit times `w^2`.  Geometrically `D(w)=D(U0)` along
the affine curve.  That coincidence does not secretly enlarge
the theorem to a raw-`U0` chart of the ambient three-space: the
coefficient field is `Q(w)` (resp. `Q(t)(w)`), denominators are
univariate in `w`, and the identity is a function-field
statement on the parameterized curve.

`w=0` forces `U0=V0=C0=0`.  Markers
`raw_curve_w_zero_is_origin=true` and
`raw_w_zero_origin_endpoint_still_separate=true` are honest.
V67 does not import the V33 `U0=0` package, does not hash-pin
it, and prints `component_all_beta_killed=false`.  Origin
remains a separate reviewed theorem.

Stdout banner `DAG_leaf_factors_only_U=true` is the V65 legacy
name for “only `U_POLY`”.  The charged README/xmodel text
corrects it.

**Failed attacks.**  `w`/raw-`U` confusion: if the generator were
raw `U0`, leaf degree 27 would be a statement about `U0^27`,
which is `w^{54}` times a unit, contradicting the printed
`x^27` with `x=w`.  Origin consumption: no origin producer is
on the import path.

**Defects.**  Naming nit `DAG_leaf_factors_only_U` only.

**Survival.**  Scope is `D(w)` of the two parameterized curves.

---

## Charge 3 — Source fidelity, ranks, exact component fields

**Result: holds.**  Polynomial beta, direct
`q_beta'=1+2 beta t+25 t^24`, frozen `p=t^15` / dead stretch /
F1 / pole data, and no weighted scaling are the executed
compiler state.  Staged ranks are
`3470/3602 -> 38/132 -> 38/94 -> 25/56` on both components.
The computation is exact in the component function field.

`configure_qd` sets `qd.B=BetaPoly.beta()` with only
degree-zero pivots invertible, and

```text
Q_PRIME = {0: 1, 24: 25}  plus  {1: 2β}  unless omitted.
```

That is `q'=1+2β t+25 t^{24}`.  Transport uses the frozen
rectangles `(15,60,3,{15:1})` and `(25,100,5,{1:1,25:1})` with
`r.fb.F1_*_PATTERN` and `r.fb.POLE_*_PATTERN`.  Pole compiler
data `POLE_F={1: -L^3 A, 6: L^3}` and
`POLE_G={0: (5/9)L^5 A^2, 5: -(5/3)L^5 A, 10: L^5}` match the
frozen two-chart patterns.  `weighted_scaling_used=false` is
source-true: the center is the raw triple `(C0,V0,U0)`, not a
weighted projective substitute.

Ranks, both hosts, both components, theorem runs:

```text
transport 3470/3602, two chart events
first     38/132, dependent 0
previous  38/94,  dependent 1 (zero residual; parameterize allows it)
current   25/56,  dependent 11, of which N13 is one
```

Transport chart degree differs by field (`x^16` on `2t-1`,
`x^12` on the quadratic), as expected from `absolute_norm` of
leads over different coefficient fields.  Stage denominator is
the same `x^11` digest
`14c8d2ccacc5b001e9f2d5a31a8dfb3dcc67dd2bbaa31dcab7938702f2d93b77`
on both components.  Complete charts `x^{16} x^{11}=x^{27}` and
`x^{12} x^{11}=x^{23}`.

Omission controls change previous/current, not transport/first:
first pivot digest is identical between theorem and omission on
each component.  That is the expected q-prime support.

**Failed attacks.**  Point sampling: `RatU` is exact `Q(w)`,
`b3tq` uses the quadratic tower `Z^2-4Z+2=0`.  Weighted
scaling: none on the import path.  Rank drift: four theorem
streams print the same four rank pairs.

**Defects.**  Banner `source_dead_stretch=0_fixed` is inherited
from V65 and is not a named identifier in the q2 compiler; the
executed transport arguments are the frozen ones.

**Survival.**  Source typing and staged ranks survive.

---

## Charge 4 — N13 ancestry

**Result: holds.**  Current row 13 traces through exactly
previous row `('X-1',14)` plus original first rows.
`('X-1',0)` is a quadratic cache/control, never a second N13
edge.  Omission controls are live.  Provenance is original
source rows, not merely the previous-stage echelon.

Lift of current index 13:

```text
required_current == [13]
n13_previous_edge_keys == [('X-1', 14)]
quadratic_key == ('X-1', 0)
quadratic_control_is_N13_edge == false
previous_lift_cache_keys == [('X-1', 0), ('X-1', 14)]
```

The cache contains row 0 because `lift_previous_key` is invoked
for the quadratic positive control *before* the N13 lift; the
N13 previous-relation support is then computed from the
non-zero previous multipliers of current row 13 and is the
singleton `{('X-1',14)}`.  The DAG dumps *every* cached
previous edge, so a hostile reading of the DAG body sees both
keys; the schema line `N13_previous_edge_keys=[('X-1', 14)]`
is the N13 edge.

Live controls in source:

- singleton current-row omission: `staged_omitted != {(): -n13}`
  after dropping the unique weight index 13;
- previous-edge omission: zeroing slot 14 of the previous
  relation makes `source_replay` miss the previous-stage
  target;
- each selected previous edge and the current edge are
  original-row replayed against `first_rows` / `previous_rows`.

The same pair `(('X-1',14), ('X-1',0) cache)` is the V66
generic-chart ancestry.  Direct q-prime omission (Charge 7)
erases N13 entirely (`N13_record_count=0`), which is a
stronger negative control than mutating a present edge.

**Failed attacks.**  Forbidden row-0 ancestry: row 0 is not in
`n13_previous_edge_keys`.  Echelon-only provenance:
`lift_current` / `lift_previous_key` divide the *raw*
132-variable source polynomials and replay against original
packed first/previous rows.

**Defects.**  None.

**Survival.**  N13 ancestry is the repaired V65/V66 edge, on
both specialized fields.

---

## Charge 5 — Genuine P12 and P12/N13 glue

**Result: holds.**  P12 is the raw current row `('X0',12)`,
reduced only through original first pivots: 28 nonzero first
rows; 2,893 raw terms on `2t-1`; 2,885 on `t^2-4t+2`.  Glue
with `N13=(k/25)β` is exactly `-k/50`.  Direct q-prime is
necessary for N13, not for the first-only P12 reduction.
Sign convention is `remainder - multiplier·N13 = -k/50`.

P12 does not touch the previous-stage echelon:

```text
p12_raw = row_polynomial(raw current ('X0',12))
divide by first_pivots only
assert source_replay(p12_relation, first_rows)
       == p12_raw - p12_remainder
assert sum(bool(slot) for slot in p12_relation) == 28
```

`beta_tail` factors `p12_remainder = unit + β·tail` with
`unit=-k/50`.  Then `n13_multiplier = tail · (25/k)` and
`n13_multiplier · N13 = tail · β`, so

```text
p12_remainder - n13_multiplier · N13 = {(): -k/50}.
```

Live inequalities: `p12_remainder` is not already the unit
(P12-without-N13 object control); `k` is the frozen residue
unit `252-342S+144S^2-36S^3` with empty `w`-denominator
factor set.  The same `N13` digest `3ec7708f…` and unit digest
`a12fa4aa…` appear on both components, as they must: both
values live in the residue field, independent of `w` and of
the quadratic `t`.

Term counts: V66 generic chart printed 2,893 raw terms.  The
`2t-1` specialization keeps 2,893; the quadratic factor
cancels eight monomials to 2,885.  Both keep 28 first rows.
That is specialization of a genuine source polynomial, not a
synthetic compact form.

Direct q-prime contribution: omitting `Q_PRIME[1]=2β` leaves
first-stage P12 machinery intact (identical first pivot
digest) and destroys N13 (`N13_record_count=0`,
`current_dependent_count` 11→10, `previous_pole_dependent_count`
1→0).  Without N13 the glue cannot fire; the reporter then
raises `IndexError` at `n13_records[0]`.  Varying-echelon
contribution is exactly N13’s previous row 14; P12 does not
use it.

**Failed attacks.**  Synthetic P12: the polynomial is the raw
current row, term-counted by `len(p12_raw)`.  Sign flip to
`+k/50`: the code sets `unit=-k/50` and asserts equality to
`BetaPoly(unit)`, matching every prior A3 q2 unit certificate
in this family.

**Defects.**  None.

**Survival.**  Genuine P12 and the unit glue survive.

---

## Charge 6 — Denominators

**Result: holds.**  Every emitted DAG leaf, every staged pivot
lead, and both complete charts have radical support only `w`.
Stage `w^11`; complete charts `w^{27}` and `w^{23}`.  No hidden
`t` / factor / norm / pivot prime survives in the univariate
denominator radical.

Leaf ledgers (byte-identical Box02/Box03):

- `2t-1`: nine keys `{1, x, x^2, …, x^7, x^{16}}`, all
  factorization `[('x', k)]`.  Count 9 matches stdout.
- quadratic: ten keys `{1, x, …, x^8, x^{12}}`.  Count 10
  matches stdout.

`leaf_denominator_ledger` walks `flat_ratu` of every N13
weight, first/previous multiplier, raw/reduced row, P12
object, and the transport-chart clearer — i.e. all four
`Curve` components of every recorded scalar.  A dummy-`V`
inverse of a generic element has relative norm `a^2-b^2 U^3`,
which is not a power of `U` unless `b=0`.  A genuine `t`
element that vanished would be a zero divisor and would crash
the rc-zero runs.  Constants in `Q(t)` are units on these
components and are not `w`-factors.

Stage LCM of first/previous/current leads plus current
residuals is `(1, [(x,11)])` on both fields.  Complete chart
`monic(transport_chart * stage_denominator)` is
`(1, [(x,27)])` and `(1, [(x,23)])`.  Additive degrees
16+11 and 12+11 show there is no cancelled extra prime
between transport and stage.

`k_curve_parameter_denominator_factor_set=[]`: the residue
unit `k` introduces no `w` divisor.  Marker
`every_denominator_norm_factor_still_charged=true` is
scope-correct: `w=0` remains charged.

**Failed attacks.**  Hidden norm denominator: any non-`w`
univariate prime in a Quad/Curve inverse would appear in
`flat_ratu` denominators or in `absolute_norm` of a transport
lead.  None appears.  Hidden `t` or `2t-1` as a `w`-factor:
those are constants or zero on the component, not `U_POLY`.

**Defects.**  None in the radical.  The parent’s unused
`curve_base_subfield` audit is not re-run on V67’s DAG
objects; Charge 1’s type-closure argument already shows the
dummy `V` direction is inert.

**Survival.**  Denominator radical is `{w}` on both opens.

---

## Charge 7 — Custody

**Result: holds, with documentary nits that do not contaminate
the theorem streams.**  Source closure, four rc-zero theorem
runs, dual Box02/Box03 DAG/ledger equality, path-only
whole-stream equality, MANIFEST/FREEZE, and both rc-one
q-prime omission controls all independently recompute.
Reporter `IndexError`s are negative controls only.

Independent SHA256 (this review):

| object | SHA256 prefix |
|---|---|
| frozen archive | `13bdaa2a…` |
| README | `bf97d2b8…` |
| `verify.py` | `00174bd8…` |
| MANIFEST | `c4c6fa50…` |
| xmodel checkpoint | `32cf1bf2…` |
| V67 `replay.py` | `ada47c39…` |
| `p3_quotient.py` | `f8c46d2c…` |
| `V67_SOURCE.sha256` | `66e27642…` |
| `2t-1` DAG / ledger | `5fe6def1…` / `1d18859a…` |
| quadratic DAG / ledger | `d71cf73a…` / `795ca7bc…` |
| `2t-1` normalized stdout | `bf5b63f1…` |
| quadratic normalized stdout | `538b70f5…` |

All 79 MANIFEST entries recompute.  FREEZE pins MANIFEST and
the xmodel file; both recompute.  `V67_SOURCE.sha256` (44
members) recomputes against the extracted tree.  `python3
verify.py` prints
`TD6-A3-Q2-B3-FINITE-FACTORS-V67 CUSTODY PASS`.

Dual-host theorem stdout: 147 lines each, **exactly two**
differing lines, both absolute artifact paths.  After the
frozen replacement of those directories by `<ARTIFACTS>/`,
the streams are byte-identical at the hashes above.  No
other byte differs.  Path-only normalization does not hide a
real difference.

Four theorem `rc` files are the two bytes `0\n`.  Both
omission `rc` files are `1\n`.  Omission stdout prints
`direct_qprime_omission_changes_N13=true` with
`N13_record_count=0` *before* the traceback
`IndexError: list index out of range` at
`n13_records[0]` (`replay.py:921`).  Both control stderrs
record `Exit status: 1`.  Control `artifacts/` directories
are empty; those streams are not theorem evidence.

Archive pin `13bdaa2a…` is on Box03 `archive.sha256`, both
Box02 `launch.meta` files, and both control `archive.sha256`
files.  Staging filename
`td6_v67_b3_factors_20260825T1518Z.tar.gz` differs from the
frozen basename; same hash.  Box02 `launch.meta` additionally
pins `source_manifest_sha256=66e27642…`, which is
`V67_SOURCE.sha256`.

12 GiB cap is in every `launch.meta` (`memory_cap=12G` /
`cap=12G`).  Timeout 21600 s is in stderr and launch
metadata.  RSS: Box03/Box02 `2t-1` 3,002,732 / 3,000,420
KiB; quadratic 3,438,400 / 3,437,592 KiB.  Elapsed ~2 h,
consistent with a real source-DAG and incompatible with a
marker-only wrapper.

**Custody nits, not theorem-blocking.**

1. Box02 recorded `source-check.txt` is `sha256sum -c
   SOURCE.sha256` (parent list, 40 members).  It does **not**
   list `V67 replay.py`, `V67_RUNBOOK.md`, or `run_v67.sh`.
   Box03 `source-check.txt` is the full `V67_SOURCE.sha256`
   (44 members, including those three).  Box02 still executed
   `./run_v67.sh` from the archive whose SHA it pinned, and
   produced byte-identical DAGs.  The checked-in Box02
   source-check is an incomplete listing, not a second
   producer.
2. Box02 theorem directories have no `archive.sha256` file;
   the pin lives in `launch.meta`.
3. `verify.py` does not re-hash MANIFEST/FREEZE/source-check
   and does not assert the scope firewall lines
   `whole_TD6_killed=false` / `SP2_killed=false` /
   `JC2_resolved=false` (those lines are present in stdout).
4. `first_c1_c3_mpoly.py` is imported without an in-source
   SHA pin (same V64/V65 nit); it is in `V67_SOURCE.sha256`.
5. V67 does not hash-pin the V66 ledger `fc655dea…` or DAG
   `3751f623…`.  Factor provenance from V66 is documentary.

**Failed attacks.**  Failed-control contamination: theorem
`rc=0` streams never contain the omission marker or the
`IndexError`; control `rc=1` streams never write a DAG.
Path-only normalization hiding a real difference: refuted by
a full 147-line dual-host compare.

**Survival.**  Dual-host source-DAG custody survives
independent recomputation.

---

## Charge 8 — Scope

**Result: holds.**  Exact scope is the two factor opens `D(w)`,
for all polynomial beta, in the fixed source-typed A3 q2
section.  No whole factor, whole `B3`, whole A3, TD6, SP-2,
landing, or JC2 claim is licensed.

Quarantine on the charged surfaces:

- xmodel: “exact all-beta incompatibility certificates only
  on `D(w)`”; “No whole factor or whole `B3=0` is claimed
  here, and nothing implies whole A3, TD6, SP-2, landing, or
  JC2.”
- README: the same firewall, plus “does not consume the
  origin theorem.”
- stdout, both components, both hosts:
  `component_all_beta_killed=false`,
  `fixed_A3_all_beta_killed=false`,
  `whole_TD6_killed=false`, `SP2_killed=false`,
  `JC2_resolved=false`,
  `only_parameter_zero_exception=true`,
  `raw_w_zero_origin_endpoint_still_separate=true`.
- `verify.py` prints
  `exact_scope=two finite B3 factor function fields on D(w)`
  and `whole_factor_or_B3_or_A3=false`.
- V66 still charges `{t,w,t-2}` as generic-chart debts; V68
  routes those three and leaves these two to V67.  V67 does
  not absorb V66/V68 into a whole-`B3` union.

“For all beta” is the polynomial-`BetaPoly` identity with
constant pivots, not a numeric `β` sample.  It is not a claim
that the *whole factor including `w=0`* is killed for all
beta.

**Failed attacks.**  Scope drift into whole factor / whole B3 /
whole A3 / TD6 / SP-2 / landing / JC2: contradicted by the
printed firewall on every charged surface.

**Defects.**  None of scope overreach.

**Survival.**  Only the two `D(w)` factor-open certificates
are licensed.

---

## Leftover nits (not load-bearing)

1. Banner `DAG_leaf_factors_only_U=true` uses the V65 letter
   `U` for `U_POLY=w`.
2. Box02 `source-check.txt` audits the parent `SOURCE.sha256`
   list, not the executed V67 producer file.  Launch archive
   pin and dual DAG equality close the gap.
3. V66 ledger/DAG hashes are not V67 freeze entries.
4. Parent `p3_quotient.main()` subfield-descent is unused;
   dummy adapters are inert by type closure instead.
5. `verify.py` is a marker/custody gate, not an algebraic
   replay.  That is as declared.
6. `first_c1_c3_mpoly.py` lacks an in-source SHA pin.
7. Staging tarball name differs from the frozen basename.
8. Hostile review of V66 (generic five-factor chart) remains
   pending.  V67 rebuilds the two finite factors from source
   and does not consume V66 as a lemma.

---

Strongest statement licensed: in the fixed source-typed A3
q2-beta section, on each of the exact function fields

```text
2t-1 = 0  over Q(w),
t^2-4t+2 = 0  over Q(t)(w),
w = V0/U0,
```

with the V66/V67 center

```text
U0 = w^2 (t-2)^2/(16t),
V0 = w^3 (t-2)^2/(16t),
C0 = w^4 (t-2)^2 (-5t^2+20t-4)/(256 t^2),
```

the original-row source DAG of current row 13 through previous
row `('X-1',14)` plus original first rows, together with the
genuine first-only P12 (2,893 terms / 28 rows on `2t-1`;
2,885 / 28 on the quadratic), is an all-beta incompatibility
certificate on `D(w)` with unit residual `-k/50`.  The complete
emitted denominator radical is `{w}`.  `w=0` is the raw origin
and is not consumed.  This is not a whole-factor, whole-`B3`,
whole-A3, TD6, SP-2, landing, or JC2 theorem.

Residual obligations (no theorem-blocking producer repair is
required for the two `D(w)` certificates):

1. Hostile review of V66’s generic-chart five-factor DAG
   remains pending.
2. The origin `w=0` / `U0=V0=C0=0` remains a separate
   source-rebuild/review obligation, as do the V68-routed
   strata `U0=0` and the two `V0=0` lines.
3. Optional custody: record Box02 `sha256sum -c
   V67_SOURCE.sha256` next to the theorem stdout, and pin V66
   ledger/DAG hashes beside the V67 archive pin.
4. Optional naming: print `DAG_leaf_factors_only_w` rather
   than `only_U`.

CONFIRMED
