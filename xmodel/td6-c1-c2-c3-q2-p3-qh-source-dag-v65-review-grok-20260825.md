# Hostile source/custody review: TD6 P3/QH curve source DAG V65

Referee: independent algebraic/source-fidelity pass of the frozen V65
P3/QH localized source-DAG claim only.  Operations used: full read of the
charged surfaces; `tar` extract of the frozen 126 KiB archive into
`/tmp/jc2-td6-v65-review-grok-20260825/`; independent SHA256 via Python
`hashlib`; structural inspection of curve-field typing, N13 previous-edge
selection, genuine-P12 first-only lift, leaf/stage/chart denominators, dual-host
bytes, and the q-prime-omission stream; hand expansion of the printed P3/QH
Bezout polynomial.  No producer execution, no CAS, solver, Lean, or other
substantive computation.  Stored PASS strings are not authority.  The
lightweight `verify.py` was inspected as a marker/custody script and then run
as a short standard-library check; it never imports `replay.py` and never
divides a polynomial.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-p3-qh-source-dag-v65-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_p3_qh_source_dag_v65_aws_20260825/`.

The named predecessor
`xmodel/td6-c1-c2-c3-q2-n13-h-zero-v60-scope-erratum-20260825.md`
is **absent**.  The V60 correction that V64/V65 actually implement is the
ancestry erratum
`xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-erratum-20260825.md`
(SHA256 `3443fcc6…`).  Reviewed V64 H-generic theorem/report named by V65:
`xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-aws-20260825.md` and
`xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-review-grok-20260825.md`,
verdict `CONFIRMED` on `H=0, D(U*V*P3*QH)`.

Producer actually executed, from frozen stderr of the four rc-zero runs:

```text
timeout 21600 ./run_v65.sh p3
timeout 21600 ./run_v65.sh qh
```

on Box02 (`…/td6_v65_{p3,qh}_repaired_box02_20260825T1401Z`) and r6d
(`…/td6_v65_{p3,qh}_repaired_r6d_20260825T141544Z`).  The negative control is

```text
timeout 21600 ./run_v65.sh p3 omit-direct-qprime
```

from the r6d-stage tree
`/home/ubuntu/stage/td6_v65_curve_repaired_20260825T141544Z/td6-aws-handoff-20260825-v65`.
Expanded tree basename `td6-aws-handoff-20260825-v65` matches the tarball
name.  V63 `main()`, V63 `run_v63.sh`, `n13_curve_quotient` `main()`, and
`p3_quotient.main()` are not called.

Import/hash pin chain executed by that producer, in order:

1. `run_v65.sh` execs
   `td6_c1_c2_c3_q2_curve_source_dag_repaired_v65_20260825/replay.py`
   (`de57451b…`, independently recomputed).
2. V65 pins and imports
   `c1_c2_c3_p3_quotient.py`
   (`CURVE_SHA256=f8c46d2c…`) and asserts `COMPONENT in {"p3","qh"}`.
3. That file pins and imports
   `c1_c2_c3_trivariate.py` (`3459dda5…`).
4. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
5. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256` as `ce400cca…`);
   pencil then pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

V63 `curve_source_dag_v63_20260825/replay.py` (`3f0d9e74…`) is listed in
`V65_SOURCE.sha256` as the unrepaired parent text, and
`n13_curve_quotient` is in the tarball.  Neither is imported by V65.
`run_v65.sh` is the only entry that can produce this case.

---

## Charge 1 — Source typing and exact scope

**Result: holds in source.**  The only asserted loci are
`H=P3=0, D(U)` and `H=QH=0, D(U)` inside the fixed source-typed
normalized A3 section `(c1,c2,c3)=(C,V,U)` with polynomial beta and
direct `q_beta'`.  No weighted source scaling and no generic
fraction-field of `H=0` is used.

- `run_v65.sh` accepts exactly `{p3|qh}` and optional
  `omit-direct-qprime`.  Frozen argv of the theorem runs is
  `--component=p3` or `--component=qh` only.  Stdout:
  `component=p3` / `component=qh`, `direct_qprime_retained=true`,
  `weighted_scaling_used=false`,
  `scope=function_field_of_exact_printed_component`.
- After import, V65 `center_and_audit()` sets
  `center = (3 U_CURVE^2, V_CURVE, U_CURVE)` and asserts
  `C - 3 U^2 = 0` identically, plus the component equation
  `V^4 - 32 V^2 U^3 + 128 U^6 = 0` or
  `V^4 + 8 V^2 U^3 - 64 U^6 = 0`.  Transport then uses
  `r.fb.CENTER = center` over the curve field, not trivariate
  `center_coordinates()` (whose default `STRATUM` remains `"generic"`
  and is unused).
- Definitions actually executed:

  ```text
  H  = C - 3 U^2
  P3 = V^4 - 32 V^2 U^3 + 128 U^6
  QH = V^4 + 8 V^2 U^3 - 64 U^6
  T  = V^2 / U^3 = Y_CURVE = Z
  ```

  The coefficient field is `Q(U)[Z,V]/(Z^2 - a Z - b, V^2 - Z U^3)`
  with `(a,b)=(32,-128)` on P3 and `(-8,64)` on QH.  That is already
  `D(U)`: `RatU` inverts `U`.  `p3_quotient` states there is no
  scaling identification.  Unused modes `b16,bneg2,bq,b3tq,b3half`
  (the last two *do* use weights) are excluded by V65’s
  `COMPONENT in {p3,qh}` assert and by `run_v65.sh`.
  `p3_quotient.main()` is not called.
- `q_beta = t + beta t^2 + t^25` is the live g-chart X source
  `{1:1, 2:B, 25:1}` together with transport on the skeleton
  `{1:1, 25:1}` and beta propagation at key `("g","X",0,2)`.
  Direct `q_beta' = 1 + 2 beta t + 25 t^{24}` is installed by
  `configure_qd(True)` as
  `Q_PRIME = {0: 1, 1: BetaPoly([0,2]), 24: 25}`.
  `p = t^{15}` is the f-boundary `{15:1}`.  F1 patterns, pole
  scale/data, and the licensed zero dead stretch remain the imported
  `fb` constants.  Theorem argv does not contain
  `--omit-direct-qprime`.
- `BetaPoly.inverse` refuses non-constant (beta-dependent) pivots.
  `solve_stage` raises `AssertionError("beta-dependent pivot")` on a
  nonunit lead.  Both theorem runs completed with unit pivots.
- Discriminants of the T-quadratics are `512 = 256·2` and
  `320 = 64·5`, neither a square in `Q`.  `Z U^3` has odd `U`-adic
  valuation, so `V^2 - Z U^3` is not a square in `Q(Z)(U)`.  Each
  component field is degree four over `Q(U)`, not a reducible product
  of `Q(U)`-quadratics and not the generic `H=0` field `Q(V,U)`.
- On `D(U)`, `V=0` would force `Z=0`, which is not a root of either
  quadratic.  The QH run asserts `Y_CURVE` invertible and prints
  `QH_V_zero_forces_U_zero=true`.  `H` is identically zero by
  substitution and cannot appear as a denominator.

The exact statement the source can bear is a post-transport original-row
identity on each printed component intersect `D(U)`, not a whole-curve,
whole-`H`, or generic-A3 identity.

---

## Charge 2 — Original-row ancestry

**Result: genuinely implemented as live asserts, not as a renamed cache
dump.**  Current row 13 traces through exactly previous key
`('X-1', 14)` plus original first rows.  `('X-1', 0)` is an independent
quadratic positive control / lift-cache entry, never an N13 previous
edge.  Its presence in the emitted DAG is harmless cache/control
material and does **not** contaminate the claimed N13 ancestry.

V60’s false sentence was that N13 reduced through previous rows 0 and
14.  V64 repaired that on generic `H=0`.  V65 is the same repair on the
curve fields, against unrepaired V63 which still printed
`previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]` and
`N13_one_required_edge_omission_negative_control=true`.

**What the source actually does.**

- `required_current = sorted(n13_weights)` is asserted equal to `[13]`.
  Frozen stdout `N13_record_count=1`,
  `current_rows_source_lifted_indices=[13]`.
- After the N13 lifts, `n13_previous_edge_keys` is the sorted set of
  previous-row keys with nonzero `previous_relation` multipliers, then
  printed and written to the DAG.  Frozen value
  `N13_previous_edge_keys=[('X-1', 14)]` on both components.
- `quadratic_control_is_N13_edge` is the live test
  `quadratic_key in n13_previous_edge_keys`, printed `false`.
- `('X-1', 0)` is forced earlier, independently: first raw quadratic
  previous row is lifted and replayed against first rows **before**
  N13.  `quadratic_source_positive_control_exact=true` follows that
  replay, then `arbitrary_degree_original_rows_preserved=true`.
- The cache print is now named
  `previous_lift_cache_keys=[('X-1', 0), ('X-1', 14)]`.  That is a
  cache union, not N13 support.

**DAG previous-edge lines.**  The DAG still emits, from
`sorted(previous_first_relations_by_key)`:

```text
previous_edge_key=('X-1', 0)
previous_edge_key=('X-1', 14)
```

Those two blocks describe every lifted previous original row (quadratic
control plus the N13 previous edge).  They are not N13 support.
Support is the header lines

```text
N13_previous_edge_keys=[('X-1', 14)]
quadratic_control_key=('X-1', 0)
```

both live f-strings (V64’s DAG `quadratic_control_key` was a string
literal; V65 repaired that).  A reader who stopped at the unlabeled
`previous_edge_key` dump could repeat V60’s two-edge mistake; the
header and stdout forbid that reading.

**Replay objects.**  `source_records` keeps `clean(polynomial)` at
every degree, including zeros.  Raw previous/current come from
`qd.compile_previous` / `qd.compile_current` on the 132-variable
bands, **not** from `qd.pack`.  Echelon stages still go through
`qd.pack`, which asserts `len(monomial) == 1`.  That packer is not
applied to the replayed original previous/current polynomials.
`divide_polynomial` replays `remainder + sum quotient * pivot == original`
before returning.  `lift_current` asserts first-only and previous-stage
replays against original rows; only nonzero previous multipliers call
`lift_previous_key`.  With the row-13 assert, the N13 previous
original-row edge is exactly key 14.

`staged_left == {(): -n13}` on the reduced 56-variable current row.
DAG `staged_left_sha256` equals `staged_target_sha256` and
`remainder56_sha256` (`8edf5e84…` on both components).  Nested
previous-first multiplier products are intentionally not expanded.
The certificate is exact edge substitution in the free equation
module, the same licensed representation as V64.

Omission of previous row 14 zeroes the unique nonzero
`previous_relation94` slot and asserts the replay fails.  Omission of
singleton current row 13 is `staged_omitted != {(): -n13}`.  Both
prints occur only after those asserts.

**Survival.**  The V60 two-edge N13 claim is repaired in the executed
V65 producer.  Row-0 in the DAG is cache/control material.

---

## Charge 3 — Genuine P12 composition

**Result: holds.**  P12 is `compile_current(...)[12]` on the
132-variable bands, reduced only through first pivots.  Live counts
are 2,885 raw terms and 28 nonzero original first rows.  Composition
with staged N13 is the exact residual `-k/50`.  Previous-stage
reduction of P12 is not used.  The object is not an affine or
synthetic surrogate.

- Lookup is `raw_current_rows[('X0', 12)]` from `source_records` of
  `qd.compile_current` on `bands132`, with no `qd.pack` and no skip of
  zeros.  First-stage only: `divide_polynomial(p12_raw, first_pivots)`,
  `lift_relations`, `source_replay` against first rows.
- `compile_x_current` is the genuine q2 current formula:
  `f1 g2' + 2 f2 g1' + 3 f3 q' - 3 p' g3 - 2 f1' g2 - f2' g1`,
  plus the degree-0 constant `-1`.  Direct `q'` enters through
  `Q_PRIME`; `p' = 15 t^{14}` is the `-45 = -3·15` g3 term.
  Lambda-prime / derivative-only columns are retained in
  `qd.pack`/`solve` (the V48 linear-packer failure class is the
  `len(monomial)==1` assert on echelon rows, not a drop of
  second-order source terms from the raw P12 polynomial).
- Live checks:
  - `len(p12_raw)==2885` and `len(raw_base)==2885`, printed as
    `genuine_P12_raw_term_count` / `genuine_P12_base_term_count`;
  - `sum(bool(relation) for relation in p12_relation)==28`;
  - `projection(p12_remainder, 0) == {(): -k/50}`;
  - `len(tail)==2`, `n13_multiplier = tail * (25/k)`,
    `n13_multiplier * n13 == tail * beta`;
  - `p12_remainder - n13_multiplier * n13 == {(): -k/50}`;
  - `p12_remainder != {(): -k/50}` (live P12-without-N13 object).
- Sign/RHS: `source_polynomial` stores `-rhs` in the constant slot;
  `pack` uses `rhs = -constant`; staged N13 is `{(): -n13}`;
  `unit = -k/50`.  DAG
  `P12_minus_multiplier_times_N13_equals_minus_k_over_50=true`.
  Glue is scalar on the first-stage remainder plus staged N13, not an
  expanded 132-variable `P12 - M N13` against a fully substituted N13
  source polynomial.  The N13 source lift is Charge 2.
- `k = 252 - 342 S + 144 S^2 - 36 S^3` in the residue field.
  `k * k.inverse() == 1` and
  `k_curve_parameter_denominator_factor_set=[]` via `flat_ratu`
  denominators.  `k` is a frozen residue-field unit, not a center
  divisor.  Residual `-k/50` is therefore a unit on both components.
- P3 vs QH: `raw_P12_base_sha256` differs
  (`3b790868…` vs `3ba9f514…`), as do `P12_relation` / `P12_source`.
  `P12_remainder`, `P12_beta_tail`, `N13_multiplier`, `unit`,
  `remainder56`, and `N13` digests **agree**.  After first-stage
  reduction the residual lives in the common A3 residue field, not on
  a hidden T-divisor.

**Survival.**  Genuine direct-first P12, 2,885 terms, 28 first rows,
residual `-k/50`, no previous-stage reduction of P12.

---

## Charge 4 — Denominator ledger

**Result: every displayed leaf and the certificate chart have radical
exactly `{U}` with chart exponent `U^13`.**  This is a coefficient-leaf
union plus transport/stage chart, independently inspected, not a
printed summary trusted on its own.  No hidden P3, QH, V, H, or pivot
prime appears in `Q[U]`.  It is not a fully expanded N13
termwise-product LCM.

Both components emit 7 ledger lines (header plus 7 data rows; stdout
`DAG_leaf_denominator_count=7`).  Independent reconstruction of every
claimed product (no CAS):

| denominator | P3 multiplicity | QH multiplicity | first_label | factors |
|---|---|---|---|---|
| `1` | 3655432 | 3655128 | `current_13_weight` | `[]` |
| `x` | 1155 | 1025 | `current_13_first_multipliers` | `x` |
| `x^2` | 518 | 448 | `current_13_first_multipliers` | `x^2` |
| `x^3` | 154 | 106 | `current_13_first_multipliers` | `x^3` |
| `x^4` | 44 | 26 | `current_13_first_multipliers` | `x^4` |
| `x^5` | 8 | 2 | `current_13_first_multipliers` | `x^5` |
| `x^6` | 1 | 1 | `transport_chart_clear` | `x^6` |

`x` is `U_POLY = fmpq_poly([0,1])`, the polynomial variable for `U`.
Union of factor strings is exactly `{x}`.  Stdout
`DAG_leaf_denominator_factor_set=['x']`,
`DAG_leaf_factors_only_U=true`.  Multiplicities differ between P3 and
QH, so the ledgers are not copies of one file.  Artifact SHAs
`0befb53e…` (P3) and `887f8ce6…` (QH) recompute and agree across hosts.

`x^6` is first seen as `transport_chart_clear`, not as a coefficient
leaf: selected-edge coefficient denominators stop at `U^5`.  The
transport chart is degree 6, one nonzero coefficient, SHA
`b9489dcc…`, two events, identical on P3, QH, and the omission run
(omission does not change transport).  Stage denominator, from all
first/previous/current pivot leads plus compatibility residuals, is
degree 7, factored `(1, [(x, 7)])`, SHA `22bc4fe5…`.  Certificate
chart `monic(transport * stage)` is degree 13, factored
`(1, [(x, 13)])`, SHA `c5f32376…`.  If both factors are monic powers
of `U`, the product is `U^13`.  Printed
`only_parameter_zero_exception=true`.

**Where factors sit, and what is absent.**

- Ledger ingestion includes N13 weights, current-13 first/previous
  multipliers and selected rows, raw/reduced current 13, **both**
  cached previous keys 0 and 14, N13 scalar, P12 unit/raw/remainder/
  first multipliers/rows/tail/multiplier, and the transport chart.
  A new radical from previous-14, the quadratic control, or P12 would
  have appeared as a new key.  None did.  No
  `previous_('X-1', 0)_…` first_label: the quadratic control
  introduces no new radical.
- P3 and QH are the **relations** of the coefficient field, hence
  zero, not `Q[U]` denominator primes.  Inverting them would be
  `ZeroDivisionError`.  `V` is a field-basis element; a `V`-inverse
  contributes `U`-powers through `norm_quad = a^2 - b^2 Y U^3`, not a
  `V` factor in `Q[U]`.  `H` is identically zero.  Flint emitted each
  denominator as a power of `x` only.
- `k` and `-k/50` contribute no `U` factor.
- Unused (zero-multiplier) first/previous/current rows are outside
  the selected-edge leaf design; their pivot leads **are** in the
  stage denominator, still only `U^7`.
- Nested multiplier products are unexpanded.  Products cannot
  introduce a prime absent from the leaves.  Cancellation in a sum
  can only shrink support.  Conservatively charging `U^13` is
  correct.

**Survival.**  Complete as a coefficient-leaf union plus transport/stage
chart on each component intersect `D(U)`.  The raw `U=0` endpoint
remains a separate theorem, as printed
`raw_U_endpoint_still_separate=true`.

---

## Charge 5 — Dual-host replay and custody

**Result: listed custody hashes recompute.  Declared `SOURCE.sha256`
closes against the archive inventory.  All four theorem `rc` values
are `0`.  Box02 and r6d exact-expression artifacts are byte-identical.
Normalized stdout agrees.  Path-only differences are the absolute
artifact directory and are safely normalized.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v65.tar.gz` | `eb481ca9e686a5fec349c5ce42915cd032d0096aee53f7a33b156ec5598edb6f` | MANIFEST, xmodel, `verify.py` EXPECTED, Box02 `ARCHIVE.sha256`, r6d `archive.sha256` |
| Box02 P3 `v65.stdout` | `63905105269deb7952094ec749bcaa835322024edb80372fc55b16d3fa100be0` | MANIFEST, EXPECTED |
| r6d P3 `v65.stdout` | `56296ed9529a733c2d1ad3534dea42c1a90611d9803a3c261556861331230d02` | MANIFEST, EXPECTED |
| Box02 QH `v65.stdout` | `d5b4ff8826e5a595e0503118d1491b88e3685c2575b1d40fcd73991a437e9edb` | MANIFEST, EXPECTED |
| r6d QH `v65.stdout` | `c9d9fca38d0581962526814ed7059fdd08312315db65739a5f6c6cb25f599c25` | MANIFEST, EXPECTED |
| P3 DAG | `52eada0af5c08a5775fff7efba77eed5bfb8a73df18d3cd0696961c7c5292f78` | MANIFEST, EXPECTED, both hosts, stdout |
| P3 ledger | `0befb53ee429d0f72c1f9d3cd04857a3c4038cfdd092007c68dbf17e8283c276` | same set |
| QH DAG | `4efbee5fcf38c84eb4966b2721b91287e82fc347b095bbfe93b4b656d63711c3` | same set |
| QH ledger | `887f8ce6b8c0ebf49f91ff9f7e6876a42fdab2b09b5370daea05c70d8337b87c` | same set |
| omit stdout | `d3125bbd34d4799e92794e1956c8e0d3aa1429bb8990f596ab6dccaf3e5c5087` | MANIFEST, EXPECTED |
| omit stderr | `51226a5b75e62aa58592da26d17ef49514bc12e355f217c4bd4b31ec995395cb` | MANIFEST, EXPECTED |
| Box02 `source-check.txt` | `6475f36334fb0c638bcc00ce752cc94b4f28c265ae6ebf06f5c2e147f6d106ec` | MANIFEST, EXPECTED; P3 and QH identical |
| theorem `rc` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body `0\n` |
| omit `rc` | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` | MANIFEST; body `1\n` |
| `README.md` | `7c952ba821cfeb09e8903af974b149749a611835e10e0cbb3abf788e71addda1` | MANIFEST |
| `verify.py` | `3d15b07162d76a896eea0d5d0d0d2d07a2db01f34c09364186f21bca308ad300` | MANIFEST |
| `MANIFEST.sha256` | `8cb2736e2bbd310bf5b2dbadce756c2e4513f38beb4bfb2fb43d1e378dd00b45` | FREEZE |
| xmodel V65 report | `936f5470ae104a352591929ce35bc74ece68974ca85f5dd1b230a22a885a0bcd` | FREEZE |
| extracted `SOURCE.sha256` | `753041d31aec3c3edef2865815845b3a999ed263c589a9805e2bfe0c55b68b5c` | all 40 members recompute |
| extracted V65 `replay.py` | `de57451b878f9c409828bc86ad6cc9bd1fd5b6d560d6689af919aa35066a303b` | `SOURCE.sha256`, `V65_SOURCE.sha256` |
| extracted curve source | `f8c46d2cec5f83f4e02b13272cdc4a761c6dcbc939a343e03f32f3517bab0505` | live `CURVE_SHA256`; DAG `curve_source_sha256` |
| V60 ancestry erratum | `3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069` | V64 xmodel |
| V64 xmodel report | `096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39` | V64 FREEZE |

All 61 MANIFEST paths recompute.  FREEZE’s two paths recompute.
Extracted `SOURCE.sha256` has 40 members, all OK.  The tarball has 41
files; the only unlisted member is `SOURCE.sha256` itself.  Frozen
`source-check.txt` is exactly those 40 names, each `: OK`.  Declared
source-check closure holds, and unlike V64 it is an inventory of the
archive.

Normalized stdout (replace
`/home/ubuntu/runs/td6_v65_[^/\n]+/artifacts` by `ARTIFACTS`) is
byte-identical host-to-host, SHA

```text
P3  2ab37f8da764f5b44df6c931897aa83bee077f1fd449f89d2617075e03d89b4a
QH  bc5e95c35459ea96b628e4816e90bade0d2c81bbaa8eb78db3dd3f1a21e6c55c
```

Raw stdout differs in exactly two lines per component, the absolute
artifact paths

```text
…/td6_v65_{p3,qh}_repaired_box02_20260825T1401Z/artifacts/…
…/td6_v65_{p3,qh}_repaired_r6d_20260825T141544Z/artifacts/…
```

`canonical()` is address-free (ECurve via `scalar_exact`, BetaPoly,
dicts sorted by `repr(key)`).  `PYTHONHASHSEED=0` is set by
`run_v65.sh`.  DAG and ledger bytes are host-independent, so the
path-only stdout difference is a logging artifact, not a
serialization split.

Staged ranks on every theorem stream:

```text
transport       3470 / 3602
first             38 / 132
previous/pole     38 / 94
current           25 / 56
```

with `transport_event_count=2`, `current_compatibility_count=11`,
`N13_record_count=1`.  First/previous/current pivot digests differ
between P3 and QH, as they must; N13 residual digests agree.

RSS from `/usr/bin/time`: Box02 P3 `3050444` KiB ≈ 2.91 GiB, Box02 QH
`3049060` KiB, r6d P3 `3053724` KiB, r6d QH `3046252` KiB.  Exit
status 0.  xmodel’s “about 3.06 GiB” is a mild overstatement of the
same measurement.  Box02 wall ~2h12; r6d wall ~2h52 (P3) / ~2h49 (QH).

r6d trees omit `source-check.txt` and preflight; Box02 has both
preflights (`curve_source_sha256=f8c46d2c…`).  Dual-host identity is
carried by archive hash, normalized stdout, and the two artifacts.
Host IPs are not in stdout/stderr.

**`verify.py` is not algebra.**  It hashes a declared subset, checks
`rc`, then `assert marker in out` / DAG / ledger, and checks the omit
stream’s `IndexError` plus `direct_qprime_omission_changes_N13=true`.
This review does not treat its PASS string as a theorem.  The script
did print `TD6-P3-QH-SOURCE-DAG-V65 CUSTODY PASS` when executed as a
custody check.

---

## Charge 6 — Controls

**Result: the direct-q-prime omission run is a post-math negative
control, not theorem evidence.  Its rc-one failure detects the
omission, then hits the absent-record reporter `IndexError` named by
the producer.  It is not a generic harness crash before the
mathematics.**

Frozen omit stdout, through the last printed line:

- `direct_qprime_retained=false`;
- transport ranks and chart identical to the P3 theorem
  (`3470/3602`, two events, chart SHA `b9489dcc…`, first pivot digest
  `70edd473…` unchanged);
- `previous_pole_dependent_count=0` (theorem: 1);
- `current_dependent_count=10` (theorem: 11);
- `current_compatibility_count=10`, `N13_record_count=0`;
- compatibility keys `('X0', 0)` and `('X0', 4)`–`('X0', 12)` only,
  all degree 0; current row 13 is absent;
- `direct_qprime_omission_changes_N13=true`;
- `N13_equals_k_beta_over_25=true` is **not** present;
- quadratic control still replays, then the stream ends.

That is the live assert

```text
assert len(n13_records) != 1 or n13 != expected
print("direct_qprime_omission_changes_N13=true")
```

The next theorem-only step is `_, _, _, n13_weights = n13_records[0]`,
which raises `IndexError: list index out of range` at V65
`replay.py:918`.  stderr records that traceback and `Exit status: 1`.
`rc` is `1\n`.  Elapsed 2:02:36, RSS ~1.75 GiB.  No DAG or ledger is
emitted.  xmodel, README, and `verify.py` refuse this stream as
theorem evidence.

Dropping `Q_PRIME[1] = 2 beta` therefore deletes the singleton N13
row rather than merely renaming a residual.  The subsequent
`IndexError` is an absent-record reporter, not an earlier crash.
The producer never reaches the unused banner
`TD6-A3-Q2-CURVE-SOURCE-DAG-REPAIRED-V65-OMISSION-CONTROL PASS`; that
is a reporter nit, not contamination.

Internal theorem-run controls (previous-14 omission, singleton
current-13 omission, live P12-without-N13 inequality, quadratic
positive control) are asserts in the rc-zero path and are not this
omit stream.

---

## Charge 7 — P3/QH relation

**Result: the printed identities hold as polynomials in `T` and are
checked on the QH field.  They prove divisor disjointness on `D(U)`.
They do not themselves exclude either divisor.**

On `D(U)`, `T = V^2/U^3`.  Field relations are
`Z^2 - 32 Z + 128 = 0` on P3 and `Z^2 + 8 Z - 64 = 0` on QH, with
`V^2 = Z U^3`, so

```text
P3 / U^6 = T^2 - 32 T + 128
QH / U^6 = T^2 +  8 T -  64
```

Hand expansion, no CAS:

```text
(5T-136)(T^2+8T-64) = 5T^3 - 96 T^2 - 1408 T + 8704
(5T+64)(T^2-32T+128) = 5T^3 - 96 T^2 - 1408 T + 8192
difference = 512
((5T-136) QHnorm - (5T+64) P3norm) / 512 = 1
```

V65 checks the specialization
`((5 Y - 136)/512) qh - ((5 Y + 64)/512) p3 == 1` on the QH
component, with `qh == 0` and `p3 != 0`.  That is the Bezout
identity at `T = Y`, hence `P3` is a unit on `QH ∩ D(U)`.  Printed
`QH_P3_disjoint_on_DU=true`.  The P3 run does not reprint the
identity; one check in `Q[T]` is enough.

Disjointness is a cover fact.  Exclusion of each component is the
independent source-DAG unit identity of Charges 2–4.

---

## Charge 8 — Scope firewall

**Result: the written scope is the largest conclusion the source can
bear.**

Producer terminal flags on both theorem streams:

```text
curve_fraction_field_source_identity_exact=true
only_parameter_zero_exception=true
raw_U_endpoint_still_separate=true
component_all_beta_killed=false
fixed_A3_all_beta_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

`verify.py` prints
`exact_scope=(H=P3=0 or H=QH=0) intersect D(U), fixed A3 q2-beta`
and `whole_curve_or_H_cover_complete=false`.  xmodel/README refuse
whole P3 or QH curve in this package, whole `H`, whole A3, other
boundary/center/pole/F1/dead-stretch moduli, TD6, SP-2, landing, a
cofinal complexity bound, and JC2.

xmodel’s “all-beta emptiness certificates on `D(U)`” is the residual
`-k/50` for every beta on those two opens.  It is not
`component_all_beta_killed`, which correctly remains false because
`U=0` is uncharged.

V64 remains the reviewed generic-`H` identity on
`H=0, D(U*V*P3*QH)`.  V65 rebuilds the two inverted curve factors
on `D(U)` only.  It does not rebuild `U=0`, `V=0`, or generic `H`,
and it does not compose them.  Composition with the separately
reviewed raw `U=0` theorem and the other H-cover leaves is explicitly
a later obligation, and even that composition would be a theorem
about `H=0` in this fixed A3 q2-beta section, not TD6 generally.

---

## Flip attempts

| attack | outcome |
|---|---|
| Hidden P3/QH/V/H denominator | Field relations or units; Flint/`Q[U]` support is only `U`. |
| Source-row / echelon confusion | Raw P12/N13 from `compile_*` on 132-var bands; `pack` is echelon-only. |
| Two-previous-row N13 reading | Live `N13_previous_edge_keys=[('X-1',14)]`; cache renamed. |
| Cached row 0 contaminates N13 | Independent quadratic control; live `quadratic_control_is_N13_edge=false`. |
| q-prime omission as theorem | Separate rc-one tree; `verify.py` and xmodel exclude it. |
| Wrong sign / RHS | `unit=-k/50`; `P12 - M N13 = unit`; `staged_left={():-n13}`. |
| Reducible / ill-typed function field | T-discriminants 512 and 320 not squares; odd `U`-valuation on `V^2`. |
| Affine/synthetic P12 | Direct-first 2,885-term `compile_current[12]`, 28 original first rows. |
| Nonportable serialization | Address-free `canonical()`; DAG/ledger byte-identical across hosts. |
| Failed-control contamination | Omit stream never supplies N13/P12/DAG; theorem `rc=0` independently. |
| Scope overreach | `component_all_beta_killed=false`; `D(U)` only; V64/U=0 uncomposed. |
| Generic `H=0` fraction field | Center is the curve field with `C=3U^2`, not trivariate `h-zero`. |
| Weighted scaling | Unused `b3tq`/`b3half` modes; executed center is `(3U^2,V,U)`. |
| Lambda-prime dropped | `Q_PRIME` and derivative-only reduction retained in `qd`. |

None of these flips.

---

## Separate verdicts

**Mathematical identity.**  Holds in source, as a post-transport
function-field identity on each printed component: genuine P12 through
28 original first rows with residual `-k/50` against staged
`N13=(k/25) beta`, and current row 13 through previous original row
`('X-1', 14)` and original first rows, with `k` a frozen A3
residue-field unit.

**Ancestry/source.**  The V60 two-edge N13 claim is repaired on both
curve fields.  Row 13 has exactly one previous original-row edge,
`('X-1', 14)`.  `('X-1', 0)` is a separate quadratic positive control.
The DAG’s two `previous_edge_key` blocks are the lift-cache dump and
are restricted by the header `N13_previous_edge_keys` line.

**Factor-ledger.**  7-line coefficient-leaf union plus transport
`U^6` and stage `U^7`; certificate `U^13`; radical exactly `{U}`.
No missing displayed selected-edge or `k` denominator.  Not an N13
termwise-product LCM.

**P3/QH relation.**  Bezout in `Q[T]` holds by hand.  Disjoint on
`D(U)`.  Exclusion is the two unit identities, not the Bezout.

**Custody.**  Freeze, manifest, artifact, `rc`, dual-host normalized
stdout, and declared `SOURCE.sha256`/`source-check.txt` hashes
recompute.  Archive-wide inventory closes.  `verify.py` is a marker
gate.  Path-only stdout differences are safely normalized.

**Exact licensed scope.**
`H=P3=0, D(U)` and `H=QH=0, D(U)` inside the fixed source-typed A3
q2-beta section, with the printed `P3`, `QH`, polynomial beta, and
direct `q_beta'`.  Not whole P3/QH curves, not whole `H`, not
`U=0`/`V=0`/generic-H, not whole A3, not TD6 / SP-2 / landing / JC2.

---

## Remaining nits (none reverses the licensed identity)

1. DAG still dumps unlabeled `previous_edge_key=('X-1', 0)` after the
   N13-restriction header.  Harmless cache material; a careless reader
   could repeat V60.  Stdout and the header forbid that reading.
2. `first_c1_c3_mpoly.py` is still imported without a hash pin (file
   is in `SOURCE.sha256`).
3. `verify.py` remains a custody/marker gate, not an algebraic replay.
4. Host IPs are not in stdout/stderr.  r6d trees omit preflight and
   `source-check.txt`; the shared archive hash covers the source.
5. Direct-q-prime omission ends in reporter `IndexError` rather than
   the unused `OMISSION-CONTROL PASS` banner.  The math detection
   already printed.
6. `factor_transport` always prints the prefix `p3_transport`, even
   on QH.  `Curve`’s docstring still says “the P3 function field”
   in QH mode.  Expository only.
7. `weighted_scaling_used=false` is a constant print; the unused
   weighted modes are excluded by the component assert, not by a
   live scan of the weight formulas.
8. Nested previous-first products are unexpanded.  Unused
   previous/current rows are not audited.
9. P12/N13 glue is scalar on the first-stage remainder plus staged
   N13, not an expanded 132-variable normal form.
10. xmodel RSS “about 3.06 GiB” overstates the `/usr/bin/time`
    figures (~2.91 GiB).
11. The named V60 path
    `td6-c1-c2-c3-q2-n13-h-zero-v60-scope-erratum-20260825.md`
    is absent; the ancestry erratum `3443fcc6…` is the relevant
    predecessor.
12. V63 and `n13_curve_quotient` remain in the tarball unused.  They
    are listed in `SOURCE.sha256` and are out of the executed path.

---

## Commands and hashes used

Extract (read-only; producer not executed):

```bash
mkdir -p /tmp/jc2-td6-v65-review-grok-20260825
tar -xzf cases/td6_c1_c2_c3_q2_p3_qh_source_dag_v65_aws_20260825/archives/td6-aws-handoff-20260825-v65.tar.gz \
  -C /tmp/jc2-td6-v65-review-grok-20260825
```

Independent SHA256: Python `hashlib.sha256(path.read_bytes()).hexdigest()`
over every MANIFEST path, FREEZE path, charged xmodel files, extracted
`SOURCE.sha256` members, extracted V65 producer, extracted curve source,
and dual-host stdout/artifacts.  Lightweight `verify.py` inspected and
run as a custody script only.

Principal hashes:

```text
eb481ca9e686a5fec349c5ce42915cd032d0096aee53f7a33b156ec5598edb6f  source archive
de57451b878f9c409828bc86ad6cc9bd1fd5b6d560d6689af919aa35066a303b  V65 replay.py
f8c46d2cec5f83f4e02b13272cdc4a761c6dcbc939a343e03f32f3517bab0505  curve p3_quotient.py
52eada0af5c08a5775fff7efba77eed5bfb8a73df18d3cd0696961c7c5292f78  P3 N13_P12_PROOF_DAG.txt
0befb53ee429d0f72c1f9d3cd04857a3c4038cfdd092007c68dbf17e8283c276  P3 DAG_LEAF_DENOMINATORS.tsv
4efbee5fcf38c84eb4966b2721b91287e82fc347b095bbfe93b4b656d63711c3  QH N13_P12_PROOF_DAG.txt
887f8ce6b8c0ebf49f91ff9f7e6876a42fdab2b09b5370daea05c70d8337b87c  QH DAG_LEAF_DENOMINATORS.tsv
2ab37f8da764f5b44df6c931897aa83bee077f1fd449f89d2617075e03d89b4a  P3 normalized stdout
bc5e95c35459ea96b628e4816e90bade0d2c81bbaa8eb78db3dd3f1a21e6c55c  QH normalized stdout
8cb2736e2bbd310bf5b2dbadce756c2e4513f38beb4bfb2fb43d1e378dd00b45  MANIFEST.sha256
936f5470ae104a352591929ce35bc74ece68974ca85f5dd1b230a22a885a0bcd  xmodel V65 report
3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069  V60 ancestry erratum
096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39  xmodel V64 report
```

CONFIRMED
