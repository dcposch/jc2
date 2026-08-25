# Hostile source/custody review: TD6 B3-chart repaired source DAG V66

Referee: independent algebraic/source-fidelity pass of the frozen V66
birational `B3=0` source-DAG claim only.  Operations used: full read of the
charged surfaces; `tar` extract of the frozen 247 KiB archive into
`/tmp/jc2-td6-v66-review-grok-20260825/`; independent SHA256 via Python
`hashlib`; structural inspection of the `(C,V)→(t,w)` chart, inverse, raw
B3 identity, N13 previous-edge selection, genuine-P12 first-only lift, every
ledger factorization cell, dual-host bytes, and normalized stdout; hand/integer
expansion of the affine `b(x(t),y(t))` identity and of `y/(x+5)=t`.  No
producer execution, no CAS, solver, Lean, or other substantive computation.
Stored PASS strings are not authority.  The lightweight `verify.py` was
inspected as a marker/custody script and then run as a short standard-library
check; it never imports `replay.py` and never divides a polynomial.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-b3-source-dag-repaired-v66-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_b3_source_dag_repaired_v66_aws_20260825/`.

Ancestry convention checked against
`xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-erratum-20260825.md`
(SHA256 `3443fcc6…`) and the reviewed V64 report/review
`xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-aws-20260825.md`,
`xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-review-grok-20260825.md`,
verdict `CONFIRMED` on `H=0, D(U*V*P3*QH)`.

Producer actually executed, from frozen stderr of both rc-zero runs:

```text
timeout 21600 ./run_v66.sh
```

on Box02 `/home/ubuntu/runs/td6_v66_b3_repaired_box02_20260825T140458Z`
and r6d `/home/ubuntu/runs/td6_v66_b3_repaired_r6d_20260825T142013Z`.
`run_v66.sh` execs
`jc2/cases/td6_c1_c2_c3_q2_b3_source_dag_repaired_v66_20260825/replay.py --stratum=b3-param`
with `PYTHONHASHSEED=0`.  Expanded tree basename
`td6-aws-handoff-20260825-v66` matches the tarball name.  Unused V64/V60/V61
wrappers remain in the tarball and are out of the executed path.

Import/hash pin chain executed by that producer, in order:

1. `run_v66.sh` execs V66 `replay.py`
   (`516821b0…`, independently recomputed).  Live asserts
   `STRATUM == "b3-param"` and `sys.argv[1:] == ["--stratum=b3-param"]`.
2. V66 pins and imports
   `td6_c1_c2_c3_q2_full_p12_n13_unit_raw_canonical_20260825/replay.py`
   (`PARENT_SHA256=77194c4b…`) and scans pinned `V44_B3_PARAM.stdout`
   (`a33dc711…`).
3. That parent pins and imports
   `td6_c1_c2_c3_q2_n13_v34_20260825/replay.py` (`1743dc29…`).
4. V34 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py` (`cf3f3f02…`).
5. Dual pins and imports
   `c1_c2_c3_trivariate.py` (`1fb51264…`), then calls `tri.configure()`.
   Dual defines `H = C - 3*U**2` on the *ring* variables; V66 never uses
   that `H` after binding it.
6. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
7. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256` as `ce400cca…`);
   pencil then pins `td6_jet_orbit_adjoint_20260824/replay.py`
   (`fb138b0f…`), which pins the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

`run_v66.sh` is the only entry that can produce this case.  Parent
`n.digest` is replaced by `canonical_digest` (E3 coordinate tuples, no
object addresses) before V66 hashes anything.

---

## Charge 1 — Exact birational `B3=0` chart, `(C,V)→(t,w)`, no weights

**Result: holds in source.**  The executed center is the birational
`B3=0` chart for the fixed source-typed A3 point `(c1,c2,c3)=(C0,V0,U0)`
over `Q(t,w)`, with the producer’s parameter-ring symbols `(C,V)` renamed
to `(t,w)` and ring `U` an unused sentinel.  No weighted source scaling
is on the path.

Live center, from `trivariate.center_coordinates()` under
`STRATUM == "b3-param"`:

```text
t, w = Rat3(C), Rat3(V)          # ring names; report names (t,w)
U0 = w^2 (t-2)^2 / (16 t)
V0 = w^3 (t-2)^2 / (16 t)
C0 = w^4 (t-2)^2 (-5 t^2+20 t-4) / (256 t^2)
```

That is exactly the README display.  Transport is
`r.fb.CENTER = (C0,V0,U0)` after `audit_b3_parameterization`, not
generic `center_coordinates()` and not a `p3_quotient` weight mode.

**Raw affine B3 and inverse, checked independently (no producer run).**
Write `x=C0/U0^2`, `y=V0^2/U0^3`, `w=V0/U0`.  Algebra of the displayed
formulas gives

```text
x = (-5 t^2 + 20 t - 4) / (t-2)^2
y = 16 t / (t-2)^2
w = w
```

The affine equation used by the audit is
`b = 4x^2 - 4 x y + 24 x + y^2 - 20 y + 20`, which is `B3/U^6` at
`C=x U^2`, `V^2=y U^3`.  Clearing `(t-2)^4` produces the zero polynomial
in `t` (integer convolution, ten sample points also return `0`).
Separately, the numerator of `x+5` is the constant `16`, so
`y/(x+5)=t` identically on `t≠2`.  The live audit also asserts
`center_v/center_u == w`, `raw_b3 == 0`, and `raw_b3+1 ≠ 0`.

On `t w (t-2) ≠ 0` one has `U0 ≠ 0`, so `B3 = U^6 b = 0` on the chart
open.  Formula denominators are units times `t` or `t^2`; the extra
open factor `w` is degeneracy of the map (the center collapses to the
origin), not a formula pole.  `B3_parameter_formula_denominator=t^2`
and `B3_parameter_open_requires=t*w*(t-2)!=0` are therefore consistent
rather than contradictory.

**Chart point loss, charged rather than silent.**

- Inverse pole `x=-5`: `b(-5,y)=y^2`, so the only affine point is
  `(-5,0)`, which lies on `V0=0` (theorem factor `w`).
- `t=2`: the line `y=2(x+5)` meets `b=0` in `-16(x+5)`; the only affine
  intersection is the same base point, the other at infinity.  The
  center formulas themselves collapse to the origin.
- Numerator `-5t^2+20t-4` is a numerator of `x` and of `C0`.  It is
  not a denominator and does not appear in any ledger prime.

**No weighted scaling.**  `p3_quotient` weighted modes `b3tq,b3half`
are not imported.  `tri.configure()` forces `B_LOCAL_PIVOTS=False`.
`B3_weighted_scaling_used=false` is a constant print after the
identity asserts; the exclusion is the `b3-param` center, not a scan
of unused weight formulas.

**Raw/internal names.**  Artifacts and `verify.py` speak `C,V`;
xmodel/README speak `t,w` with an explicit rename.  Ledger primes
`C, V, C-2, 2*C-1, C^2-4*C+2` are the theorem primes
`{t, w, t-2, 2t-1, t^2-4t+2}`.  Ring `H=C-3U^2` is a false friend
on this chart and is not used by V66 after the import binding.
Ring `U` is the sentinel `j`; it does not appear in the ledger.

**Survival.**  Exact birational `B3=0` chart for fixed A3
`(C0,V0,U0)`, rename documented, inverse and affine identity hold,
no weighted source scaling.

---

## Charge 2 — Polynomial beta, direct `q_beta'`, frozen p/F1/pole

**Result: retained in the executed path.**  V66 prints

```text
q_beta=t+beta*t^2+t^25
q_beta_prime=1+2*beta*t+25*t^24
```

and then calls `n.configure_qd(direct_qprime=True)` *before* packing
first rows.  That writes

```text
qd.Q_PRIME = {0: 1, 24: 25, 1: BetaPoly([0, 2])}
```

i.e. `q_beta' = 1 + 2 beta t + 25 t^{24}`.  `--omit-direct-qprime` is
absent from argv; V34’s `OMIT_DIRECT_QPRIME` is therefore false and
V34 `main()` is not called.

Transport uses the frozen q2/F1/pole data, identical to pinned V44:

```text
build_transport(15, 60, 3, {15: 1}, F1_F_PATTERN, POLE_F_PATTERN)
build_transport(25, 100, 5, {1: 1, 25: 1}, F1_G_PATTERN, POLE_G_PATTERN)
pole_coefficient(15, 60, -2, ·), pole_coefficient(25, 100, -4, ·)
```

That is p-boundary `t^{15}`, g-skeleton `{1:1, 25:1}` with beta at
key 2, dead-stretch `0` (no extra stretch keys), frozen F1/pole
patterns.  V66 does **not** reprint V44’s
`source_p_boundary=t^15_fixed` / `source_dead_stretch=0_fixed` /
`source_F1_orbit=frozen` / `source_pole_scale_and_data=frozen`
banners; those strings live on the pinned V44 scan.  The live
constants are the same.

First-stage pivot digest
`102c26f1b84efcc0af65d66a532e53abdb4fb6e90373f52ff0df3d12f9fafbf1`
equals V44 `first_full_beta_P12_pivot_digest` computed with direct
q-prime.  V66 does not repeat V44’s live
`first_rows_omit != first_rows` omission control.  The digest match
is the cross-check that q-prime was not dropped.

**Survival.**  Polynomial beta and direct `q_beta'` are the live
objects.  p-boundary / dead-stretch / F1 / pole data are the frozen
patterns, not a V66 mutation.

---

## Charge 3 — N13 row 13 through exactly `('X-1',14)`; row 0 is not an edge

**Result: the V60 erratum convention is implemented as live asserts,
as in reviewed V64.**  Current `('X0',13)` traces through previous
`('X-1',14)` and original first rows.  `('X-1',0)` is an independent
quadratic cache/control, never a second N13 edge.

- `n13_records` is filtered to `('X0',13)` with nonzero left-null row.
  Frozen stdout: `N13_left_null_support=1`,
  `current_rows_source_lifted_indices=[13]`.
- For `key == ('X0',13)`, `lift_current_key` **asserts**
  `selected_previous == [('X-1', 14)]`.
- After the N13 lifts,
  `n13_previous_edge_keys` is the sorted union of those selected
  previous keys over N13 support only, then
  `assert n13_previous_edge_keys == [('X-1', 14)]`.
- `('X-1',0)` is forced earlier, independently: first raw quadratic
  previous row is lifted and replayed against first rows **before**
  N13.  Frozen stdout
  `quadratic_source_positive_control_key=('X-1', 0)` is that live
  key, not a DAG string.
- Cache print
  `previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]`
  is the cache union, immediately followed by
  `N13_previous_edge_keys=[('X-1', 14)]` and
  `quadratic_control_is_not_N13_edge=true`.  That is the V60-requested
  split.

**DAG previous-edge lines.**  The DAG still emits, from
`sorted(previous_first_relations_by_key)`:

```text
previous_edge_key=('X-1', 0)
previous_edge_nonzero_first_rows=14
previous_edge_key=('X-1', 14)
previous_edge_nonzero_first_rows=38
```

Those blocks are every lifted previous original row (quadratic
control plus N13 previous edge), not N13 support.  Support is the
later lines `N13_previous_edge_keys=[('X-1', 14)]` /
`quadratic_control_key=('X-1', 0)` /
`quadratic_control_is_not_N13_edge=true`.  Current-13 first-only
support is 38, matching previous-14 and not previous-0’s 14.
xmodel and README state the one-edge N13 trace.  They do not repeat
V60’s two-edge N13 prose.

**Omission controls are live asserts.**

1. Previous-14: unique nonzero `previous_relation94` slot is zeroed;
   `source_replay(omitted, previous_rows) != previous_target`.  Print
   `N13_previous_edge_14_omission_negative_control=true` is after
   that assert.
2. Current-13: `staged_n13_left == {(): -n13}` and
   `staged_without_one != {(): -n13}` with
   `omitted_index = min(n13_weights)` (support size 1 ⇒ 13).
   Renamed `N13_singleton_current_row_omission_negative_control`.
3. `arbitrary_degree_original_rows_preserved=true` is printed after
   the quadratic replay, replacing the early `pending_live_control`
   banner.  `verify.py` matches the later string.

**Packaging nits, not ancestry reversal.**  DAG
`quadratic_control_key=('X-1', 0)` is a string literal, not
`f"quadratic_control_key={quadratic_key}"`.  Frozen stdout’s live
print is `('X-1', 0)`, so this run is consistent.
`quadratic_control_is_not_N13_edge=true` is a constant print after
the N13-keys assert, not `quadratic_key not in n13_previous_edge_keys`.
The N13 assert already excludes key 0.

**Survival.**  Forbidden row-0 N13 ancestry does not hold.  The V60
repair is the live source.

---

## Charge 4 — Genuine P12, 2893/28/1649, residual `-k/50`, no affine surrogate

**Result: holds.**  P12 is `compile_current(...)[12]` on the
132-variable bands, reduced only through first pivots.  Live B3-chart
counts match pinned V44.  Composition with staged N13 is the exact
residual `-k/50`.  Previous-stage reduction of P12 is not used.  The
later-echelon packed current row 12 is not substituted.

- Lookup is `raw_current_rows[('X0', 12)]` from `source_records` of
  `qd.compile_current` on `bands132`, with no `qd.pack` and no skip
  of zeros.  That is the same slot V44 calls
  `P12_compiler=genuine_2893_term_source_polynomial` /
  `later_echelon_X0_t12_used=false`.
- First-stage only: `divide_polynomial(p12_raw, first_pivots)`,
  `lift_relations`, `source_replay` against first rows.
  `P12_previous_stage_reduction_required=false`.
- Affine parameterization (`parameterize_with_pivots`) is used only
  to restrict later *bands* through first/previous pivots for the
  N13 echelon.  It asserts every first/previous original row is
  recovered from those affine forms.  P12 is not taken from
  `current_rows` (56-variable packed echelon).
- Live checks, then digest pins against V44 `a33dc711…`:
  - `len(raw_base)==2893` and
    `polynomial_digest(raw_base)==3176eab0…` (V44
    `raw_P12_base_sha256`);
  - 28 nonzero first relations and 1649 multiplier terms
    (V44 `first_source_nonzero_rows=28`,
    `first_source_multiplier_terms=1649`);
  - tail digest `0639f8cd…` and N13-multiplier digest `aef2b851…`
    (both V44);
  - `len(p12_remainder132)==3`, `len(tail132)==2`;
  - `projection(remainder, 0) == {(): -k/50}`.
- These are the B3 counts, not the H-zero `2885/28/1640`.  A
  synthetic reuse of the H-zero P12 would fail the 2893 hash pin.
- Glue: `R - M * n13_staged == {(): -k/50}` with
  `M = (25/k)*tail`, `n13 == (k/25)*beta`, and
  `k = 252 - 342 S + 144 S^2 - 36 S^3` a residue-field unit
  (`k * k.inverse() == 1`,
  `k_coordinate_denominator_factor_set=[]`).
  Signs: `unit = -k/50`; composed remainder equals that unit;
  `p12_first_source != P12 - unit` is the live P12-without-N13
  object.  This is the first-stage remainder plus staged N13, not
  an expanded 132-variable `P12 - M*N13` against a fully
  substituted N13 source polynomial.  The N13 source lift is
  Charge 3.
- Direct q-prime contributes through `configure_qd(True)` before
  first rows and through `compile_current` on the same Dual/Q_PRIME.
  Varying-echelon substitution (beta=0 first, then lift) is not
  used; pivots are asserted beta-independent and rows keep polynomial
  beta.

DAG line `P12_source_edge=V44_RAW_CANONICAL.stdout` is a leftover
filename; the pinned file is `V44_B3_PARAM.stdout` at `a33dc711…`.
The live P12 is recomputed, then hashed against that scan.  Not a
substitution of the scan for the object.

**Survival.**  Genuine direct-first P12 with 2,893 raw terms, 28
original first rows, 1,649 multiplier terms, residual `-k/50`, no
previous-stage reduction of P12, no affine/H-zero surrogate.

---

## Charge 5 — Denominator radical exactly `{t,w,t-2,2t-1,t^2-4t+2}`

**Result: the TSV agrees with the summary print.**  All 111 data
rows of both hosts’ ledgers were parsed.  Unique `factor()` primes:

```text
['2*C - 1', 'C', 'C - 2', 'C^2 - 4*C + 2', 'V']
```

Under the documented rename that is exactly
`{t, w, t-2, 2t-1, t^2-4t+2}`.  No `U`, no ring-`H`, no raw `B3`,
no `-5t^2+20t-4`, no extra cyclotomic, no integer prime `2` as a
polynomial factor.

One empty-factorization row is denominator `1` (unit coordinates),
first labelled `current_13_weight`, multiplicity `862694`.  That is
the shared unit key, not a hidden prime.  `C - 1/2` appears as a
raw key and factors as `[('2*C - 1', 1)]`; the radical uses `2t-1`.

V44 termwise clear is present as
`V44_P12_termwise_clear` with factorization
`[(2*C-1,1), (C,19), (C-2,4), (C^2-4*C+2,3), (V,5)]`, matching
pinned V44
`termwise_source_denominator_factor=(1/2, […])`.  The DAG prints
the associate `2 C^{30} V^5 - 41 C^{29} V^5 + ⋯`; the ledger stores
the monic-with-halves form.  Same radical.  The live B3 branch
constructs

```text
C^19 V^5 (C-2)^4 (2C-1) (C^2-4C+2)^3
```

The leftover `if STRATUM == "h-zero"` P12-clear (using `U V^2 P3`)
is dead: `STRATUM` is asserted `b3-param`.

Every displayed prime occurs on a live N13 or P12 leaf, not only on
the quadratic control:

| prime | N13/P12 leaves (not only row 0) |
|---|---|
| `C` | current-13 first/raw/previous-reduced, previous-14, P12, V44 clear |
| `V` | current-13, previous-14, P12, V44 clear |
| `C-2` | current-13, previous-14, P12, V44 clear |
| `2C-1` | current-13 first-only, P12, V44 clear |
| `C^2-4C+2` | current-13 first-only/raw, P12, V44 clear |

Row-0 leaves also use `C`, `V`, `2C-1`, `C^2-4C+2`.  Including them
is conservative.  They introduce no extra prime.

The ledger is a coefficient-leaf support ledger plus the pinned P12
termwise clear, not a fully expanded N13 termwise-product LCM, and
it does not prove that any one prime is essential after cancellation.
That is the same support-kind as reviewed V64, now on the B3 chart.
`factored_clear_scalar_expansion_required=false` records that choice.
The theorem still charges every displayed factor as a separate
raw-source obligation.

**Survival.**  Complete leaf-plus-P12 radical is exactly the five
stated primes.  The summary print matches the artifacts.

---

## Charge 6 — Box02/r6d custody, rc 0, source closure, negatives

**Result: listed custody hashes recompute.  Declared `SOURCE.sha256`
closes against the archive inventory.  Both `rc` files are `0`.
Paired DAG/ledger are byte-identical.  Normalized stdout agrees.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v66.tar.gz` | `dbb97927b097cf2eb5876f782c2b94cfc8b2830b07fe4db288db8aa13fdfbfe6` | MANIFEST, README, xmodel, both `archive.sha256`, `verify.py` EXPECTED |
| `aws_box02/v66.stdout` | `c7c3342a5e0efcc790b35719b3d3fbc6ca775de727285b9e60b586adc697edf4` | MANIFEST, EXPECTED |
| `aws_r6d/v66.stdout` | `263418670de0a9ad02f495e1a45e125f29495ada12776751f50830c3348e68e7` | MANIFEST, EXPECTED |
| `aws_box02/v66.stderr` | `0ab846e6ca67ecf0ccc572584d770b5440c5c3eb313af2094e5e72212b7079e7` | MANIFEST, EXPECTED |
| `aws_r6d/v66.stderr` | `2a70b90df2becf8ed9c272c7e8b2145c0bd4de743b826228090a2d5bcce01927` | MANIFEST, EXPECTED |
| proof DAG (both hosts) | `3751f623e2f60e899f0214e2151e6a2f5923ee2d6a07a9b9424dd87a2877def8` | MANIFEST, stdout, DAG self-hash, EXPECTED |
| denominator ledger (both hosts) | `fc655dea4b85f836d7372f1b7c6e34835b8403d0b755a154c82911dfff605b7e` | MANIFEST, stdout, EXPECTED |
| `aws_box02/rc` and `aws_r6d/rc` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body `0\n` |
| `README.md` | `93335234975e547fc2cfac858da405df7079dfd9c4970ec6fd02c5f553b64828` | MANIFEST, FREEZE |
| `verify.py` | `de285e2afd11464b09ba2ae876a38f1af00721e16c79ac46c10dccfa1777d2bc` | MANIFEST, FREEZE |
| `MANIFEST.sha256` | `7a7ea735327ad625814702be7a0092a4bbc50b29def870e1f8d4315d30b4fcc5` | FREEZE |
| xmodel V66 report | `50361e0838995ba8d863a6f485a06e2060df6e76cfcaa777383e301d01bfc32b` | FREEZE |
| extracted `SOURCE.sha256` | `d264f1341b0a2c480026a5d14429833a666643251cb3fa14337cbe6925ff6402` | 103 members, all recompute |
| extracted V66 `replay.py` | `516821b0926180b4e03081a3e0370a3b2d259b1bd23f5baa179234cd600cc8a5` | `SOURCE.sha256`, `V66_SOURCE.sha256` |
| extracted parent raw-canonical | `77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef` | live `PARENT_SHA256`; **also** in top-level `SOURCE.sha256` |
| V60 erratum | `3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069` | V64 xmodel |

All 19 MANIFEST paths recompute.  FREEZE’s four paths recompute.
Case files not in MANIFEST are only `MANIFEST.sha256` and
`FREEZE.sha256` (outer seal).  No failed-run mix: both stderrs
`Exit status: 0`; Box02 elapsed `45:33.28`, RSS `2111172` KiB;
r6d elapsed `33:34.07`, RSS `2113008` KiB.  README UTC intervals,
remote paths, RSS, and rc match the artifacts.

**Source closure.**  Extracted archive has 104 files: 103 listed in
`SOURCE.sha256` plus `SOURCE.sha256` itself.  Unlisted count is 0.
No `__pycache__`.  The executed parent, V34, dual, trivariate,
pencil, `first_c1_c3_mpoly.py`, jet-orbit, q2 compiler, moduli,
`run_v66.sh`, and V66 producer are all on the declared list.  This
closes the V64 declared-list hole (parent was live-pinned there but
absent from `SOURCE.sha256`).  `first_c1_c3_mpoly.py` is still
imported without a *live* hash pin; it is on the list.

**Normalized streams.**  Raw stdout differs only in the absolute
artifact directory
(`…/td6_v66_b3_repaired_{box02_20260825T140458Z,r6d_20260825T142013Z}/…`).
After that substitution the streams are byte-identical.  DAG and
ledger are byte-identical without substitution.  Digests are
canonical E3 coordinates with `PYTHONHASHSEED=0`; dual-host equality
is the portability check.

**`verify.py` is not algebra.**  It hashes five paths, checks both
`rc` and archive SHAs, then `assert marker in out` / DAG / ledger
equality.  This session ran it: it printed
`TD6-V66-B3-REPAIRED-SOURCE-DAG-CUSTODY PASS`.  That string is not
the theorem.

**Negative controls actually executed.**  Previous-14 omission,
current-13 omission, P12-without-N13 live inequality,
`B3_parameter_plus_one_negative_control` (`b+1 ≠ 0` and
`raw_b3+1 ≠ 0`), and `k * k.inverse() == 1` are asserts.  Direct
q-prime omission is *not* re-run in V66 (Charge 2).

**Survival.**  Dual-host custody, rc 0, source inventory, paired
DAG/ledger, and normalized stdout survive independent recomputation.
Host IPs are not in the artifacts.  The 12 GiB cap is a README
statement, not an in-artifact cgroup proof.

---

## Charge 7 — Exact theorem scope

**Result: the licensed statement is only
`B3=0, D(t*w*(t-2)*(2t-1)*(t^2-4t+2))` inside the fixed source-typed
A3 q2-beta section.**  Every displayed factor remains a separate
raw-source obligation.  No whole-B3, whole fixed-A3, TD6, SP-2,
landing, or JC2 inference is made.

Stdout/DAG/README/xmodel/`verify.py` all keep
`whole_raw_stratum_killed=false`, `full_A3_beta_family_killed=false`,
`whole_TD6_killed=false`, `SP2_killed=false`, `JC2_resolved=false`,
`raw_denominator_factor_strata_still_charged=true`.
`full_unused_previous_current_row_audit_complete=false` is honest:
unused rows are not audited.  Chart open `t w (t-2) ≠ 0` is strictly
smaller than the theorem `D(…)`; the extra primes `2t-1` and
`t^2-4t+2` come from source leaves, not from the parameterization
formulas, and are not silently absorbed.

---

## Attacks that did not flip

1. **Bad inverse.**  `y/(x+5)=t` is an identity (`x+5` numerator `16`).
   `w=V0/U0` is an identity on the open.  Affine `b` is the zero
   polynomial in `t`.
2. **Silent chart point loss.**  The missed affine base point and the
   `t=2` collapse lie on charged loci `w` / origin / `t-2`.
3. **Raw/internal variable confusion.**  Rename `(C,V)→(t,w)` is
   documented; ring `H` is unused; sentinel `U` is absent from the
   ledger.
4. **Hidden denominator / norm factor.**  All 111 factorization cells
   yield only the five primes.  `C-1/2` is `2t-1`.  Integer `2` is a
   unit in `Q`.  `t^2-4t+2` is irreducible over `Q` (discriminant 8).
5. **Forbidden row-0 N13 ancestry.**  Live assert is `('X-1',14)` only.
6. **Synthetic / H-zero P12.**  Live 2893-term digest is the B3 V44
   pin, not the H-zero 2885-term object.
7. **Affine surrogate for P12.**  P12 is raw `compile_current[12]` at
   132 variables, first-stage only.
8. **Failed-run contamination.**  Both hosts rc 0, identical DAG/ledger,
   no mixed PASS/FAIL.
9. **Nonportable digest.**  Canonical E3 coordinates plus
   `PYTHONHASHSEED=0`; dual-host artifacts are byte-identical.
10. **Scope drift.**  Whole-B3 / A3 / TD6 / SP-2 / JC2 banners stay
    false.  Landing is named as out-of-scope in xmodel/README and is
    not given a stdout token.

---

## Nits that do not flip the theorem

1. DAG still lists `previous_edge_key=('X-1', 0)` as a lifted cache
   row.  N13 support is the later exclusive marker.  Same convention
   as reviewed V64.
2. DAG `quadratic_control_key=('X-1', 0)` is a string literal.
3. DAG `P12_source_edge=V44_RAW_CANONICAL.stdout` names the wrong
   filename; the pin is `V44_B3_PARAM.stdout`.
4. Leftover `if STRATUM == "h-zero"` P12-clear branch and docstring
   sentence “exactly one of … `H=0` or … `B3=0`”.  Execution is
   `b3-param` only.
5. `B3_weighted_scaling_used=false` is a constant print.  Weighted
   modes are excluded by not importing them.
6. V66 stdout omits V44’s p-boundary/dead-stretch/F1/pole banners.
   The live `build_transport` arguments are those frozen values.
7. V66 does not rerun V44’s live direct-q-prime omission control.
   First-pivot digest still matches V44-with-qprime.
8. `first_c1_c3_mpoly.py` is imported without a live hash pin.  It is
   on `SOURCE.sha256`.
9. Nested previous-first products are unexpanded.  Unused
   previous/current rows are not audited.
10. P12/N13 glue is scalar on the first-stage remainder plus staged
    N13, not an expanded 132-variable normal form.
11. AWS trees have no `source-check.txt`.  Archive-wide `SOURCE.sha256`
    closure was checked here instead.
12. Host IPs and the 12 GiB cgroup cap are README statements, not
    in-artifact proofs.
13. `verify.py` is a marker gate.  Its PASS string is not algebra.
14. No stdout `landing_killed=false` token; xmodel/README still
    exclude landing.

---

## Commands and hashes used

Extract (read-only; producer not executed):

```bash
mkdir -p /tmp/jc2-td6-v66-review-grok-20260825
tar -xzf cases/td6_c1_c2_c3_q2_b3_source_dag_repaired_v66_aws_20260825/archives/td6-aws-handoff-20260825-v66.tar.gz \
  -C /tmp/jc2-td6-v66-review-grok-20260825
```

Independent SHA256: Python `hashlib.sha256(path.read_bytes()).hexdigest()`
over every MANIFEST path, FREEZE path, charged xmodel files, extracted
`SOURCE.sha256` members, extracted V66 producer/parent/trivariate/V44
scan, and dual-host stdout/artifacts.  Lightweight `verify.py` inspected
and run as a custody script only.

Principal hashes:

```text
dbb97927b097cf2eb5876f782c2b94cfc8b2830b07fe4db288db8aa13fdfbfe6  source archive
516821b0926180b4e03081a3e0370a3b2d259b1bd23f5baa179234cd600cc8a5  V66 replay.py
77194c4b9a30b9190da026e94c0f476449cbeeba8a679b1abfa6768c37caf2ef  parent raw-canonical
1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea  trivariate.py
a33dc711c1b8b7d215912aa8c86c43eac8b9be43cc30e1c219583bf952c937ee  V44_B3_PARAM.stdout
3751f623e2f60e899f0214e2151e6a2f5923ee2d6a07a9b9424dd87a2877def8  N13_PROOF_DAG.txt
fc655dea4b85f836d7372f1b7c6e34835b8403d0b755a154c82911dfff605b7e  DAG_LEAF_DENOMINATORS.tsv
c7c3342a5e0efcc790b35719b3d3fbc6ca775de727285b9e60b586adc697edf4  Box02 stdout
263418670de0a9ad02f495e1a45e125f29495ada12776751f50830c3348e68e7  r6d stdout
7a7ea735327ad625814702be7a0092a4bbc50b29def870e1f8d4315d30b4fcc5  MANIFEST.sha256
50361e0838995ba8d863a6f485a06e2060df6e76cfcaa777383e301d01bfc32b  xmodel V66 report
3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069  V60 ancestry erratum
096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39  xmodel V64 report
```

CONFIRMED
