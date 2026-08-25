# Hostile bounded review: TD6 q2-beta rational raw lines (V45/V46)

Referee: independent algebraic/source/custody pass of the frozen V45/V46
rational-line package, against the later U=0 localization erratum and the
hostile-reviewed V70 origin/`u-h-zero` repair.  Operations used: full read
of the charged surfaces; `tar` extract of both portable archives into
`/tmp/jc2-td6-rational-raw-lines-review-grok-20260825/`; independent SHA256
via Python `hashlib`; structural inspection of stratum typing, genuine-P12
reduction, abstract N13 glue, V46 first-band incompatibility, parent
complete-certificate formula, `x_power_expansion`, `q_beta` / `q_beta'`,
and the set-theoretic line/endpoint cover; short stdlib comparison of
fail-closed prefix, omit/P12-without-N13 controls, and frozen classical
trivariate transports of the same matrix.  Ranks, 13-row combination, and
P12 term arithmetic were not recomputed.  No producer execution, no CAS,
solver, Lean, or other substantive computation.  Stored PASS strings are
not authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_beta_rational_raw_lines_aws_20260825/`.

Later localization / endpoint context (not freeze-time authority):
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md`
(SHA-256 `df746976…`),
`xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-aws-20260825.md`,
`xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-review-grok-20260825.md`
(verdict `CONFIRMED`).

Already frozen N13-scope erratum, which this review does not reopen:
`cases/td6_c1_c2_c3_q2_n13_localization_scope_erratum_20260825/`
quarantines V45 all-beta *source-promotion* on `C=3U^2` and `C=-5U^2`
for lack of a full staged N13 lift, and leaves V46 independent of N13.

Producer actually executed, from frozen stderr:

```text
timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_rational_canonical_20260825/replay.py \
  --stratum=v-h-zero

timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_rational_canonical_20260825/replay.py \
  --stratum=v-cplus5-zero

timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_rational_canonical_20260825/replay.py \
  --stratum=v-cplus1-zero

timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_cplus1_first_incompatibility_canonical_20260825/replay.py \
  --stratum=v-cplus1-zero
```

The third command is the retained rc-one harness control.  The fourth is
the theorem-producing V46 adjudication.  Dual `main()`, V31 `main()`, and
V34 `main()` are not called.  `--omit-direct-qprime` is absent from argv;
the q-prime control is an in-process matrix inequality.

Import/hash pin chain executed by V45, in order:

1. V45 `replay.py` (`7e137083…`) pins and imports
   `td6_c1_c2_c3_q2_n13_v34_20260825/replay.py` (`N13_SHA256=1743dc29…`).
2. V34 pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py` (`DUAL_SHA256=cf3f3f02…`).
   Dual defines `H = C - 3*U**2`.
3. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`TRI_SHA256=1fb51264…`), then calls `tri.configure()`.
4. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
5. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256`); transport then loads
   `c1_pencil.py`, which pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

V46 is the same chain with a different leaf:
`td6_c1_c2_c3_q2_cplus1_first_incompatibility_canonical_20260825/replay.py`
(`9b1670ab…`) pins the same V34 file and asserts
`--stratum=v-cplus1-zero` only.  V33 `replay.py` is archived and listed
in `V33_SOURCE.sha256` but is not imported.

---

## Charge 1 — Source loci and `B3|_(V=0)`

**Result: holds in source.**  The three raw branches are exactly

```text
V=0, C=3U^2;    V=0, C=-U^2;    V=0, C=-5U^2
```

inside the fixed source-typed normalized A3 q2-beta section.  Centers
are substituted directly.  The B3 identity is an executable polynomial
identity, not a chart rumour.

- Trivariate `STRATUM` is read from the same argv at import, before
  `center_coordinates()` runs.  Licensed keys:

  ```text
  v-h-zero:      Rat3(3*U**2), Rat3(0), Rat3(U), "V=H=0 over Q(U)"
  v-cplus1-zero: Rat3(-U**2),  Rat3(0), Rat3(U), "V=C+U^2=0 over Q(U)"
  v-cplus5-zero: Rat3(-5*U**2), Rat3(0), Rat3(U), "V=C+5U^2=0 over Q(U)"
  ```

  Frozen stdout is exactly those three `source_center=` lines.  The
  producer does not take `generic`, `u-zero`, `h-zero`, `v-zero`,
  `u-h-zero`, `origin`, or `b3-param`.
- V45 asserts `STRATUM in {"v-h-zero","v-cplus1-zero","v-cplus5-zero"}`
  and `sys.argv[1:] == ["--stratum="+STRATUM]` before any GE.  V46
  asserts `STRATUM == "v-cplus1-zero"` and the same argv shape.
- Dual’s `H = C - 3*U**2` makes `v-h-zero` the raw residual `V=0`
  branch inside `H=0`.  V45 then asserts `not center_v and not h_center`
  on that stratum, and `not center_v and not b3_center` on the two B3
  branches.
- The displayed factorization is executed on free `(C,U)`:

  ```text
  B3 = 4C^2 U^2 - 4C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6
  B3|_(V=0) = 4C^2 U^2 + 24 C U^4 + 20 U^6
            = 4U^2 (C^2 + 6 C U^2 + 5 U^4)
            = 4U^2 (C+U^2)(C+5U^2).
  ```

  The producer asserts the last equality.  Hand expansion of
  `(C+U^2)(C+5U^2)` is the same cubic.  On `C=3U^2` this is `128 U^6`,
  a unit on `D(U)`, so `V=H=0` is not secretly a B3 branch.
- After coordinates, `r.fb.CENTER` is set and the x-power cache is
  cleared.  `x_power_expansion` is polynomial in `(c1,c2,c3)`:

  ```text
  coeff *= c1**a1 * c2**a2 * c3**a3
  ```

  `c2=0` drops the `V` terms.  There is no division by `C`, `V`, or
  `U` in that expansion.  A vanished-center inversion anywhere else in
  the exact arithmetic would have been `ZeroDivisionError`; all four
  runs completed through the asserted stage.

**Defects.**  None in the loci.  Printed `scope_open=fraction_field_of_printed_raw_stratum`
is the honest D(U) chart.  V45’s leftover `if STRATUM == "b3-param"` is
dead under its own stratum assert.

**Survival.**  Direct source typing of the three rational lines, with
the B3 pencil identity above.

---

## Charge 2 — Polynomial beta, `q_beta'`, p-boundary, dead stretch, F1, poles

**Result: holds.**  Polynomial `beta` and direct
`q_beta'=1+2 beta t+25 t^24` are retained.  No unlicensed scaling of
p-boundary, dead stretch, F1, or pole data.

- Printed `q_beta=t+beta*t^2+t^25` and
  `q_beta_prime=1+2*beta*t+25*t^24` on every stream, including the
  rc-one control.  Dual’s documented family is the same.
- After a successful transport, V45/V46 call
  `n.configure_qd(direct_qprime=True)`:

  ```text
  qd.Q_PRIME = {0: 1, 24: 25, 1: BetaPoly([0, 2])}
  ```

  i.e. `1 + 2 beta t + 25 t^{24}`.  `--omit-direct-qprime` is not on
  the theorem argv.
- Transport f-boundary is `{15: 1}` (`p=t^{15}`); g-boundary is
  `{1: 1, 25: 1}` (the `t+t^{25}` skeleton).  The `beta t^2` term
  enters through `source_vector_beta` / first-J, not by rewriting `p`.
- Stdout banners `source_p_boundary=t^15_fixed`,
  `source_dead_stretch=0_fixed`, `source_F1_orbit=frozen`,
  `source_pole_scale_and_data=frozen` name the imported `fb`
  constants used as `F1_F_PATTERN` / `POLE_F_PATTERN` and the g
  analogues.  Those objects are not reassigned in V45/V46.
- `solve_stage` still raises `AssertionError("beta-dependent pivot:
  exceptional strata required")` if any accepted lead has
  `lead.degree != 0`.  `BetaPoly.inverse` exists only for degree 0.
  Frozen first-stage lines print
  `first_full_beta_P12_all_pivots_beta_independent=true`.
- Transport is rebuilt after `CENTER`.  It never loads V33 pivots and
  never substitutes `U=0` into a fraction-field echelon.

**Defects.**  None in the typing.  `transport_matrix_beta_independent=true`
is a banner behind `assert not compatibility and len(transport_pivots)==3470`.

**Survival.**  Fixed A3 q2-beta section, polynomial beta, direct `q'`.

---

## Charge 3 — V45 on `C=3U^2` and `C=-5U^2`

**Result: the genuine-P12 / original-first-row identities, the algebraic
N13 glue, the constant `-k/50`, the term/row/slot counts, and the U-only
emitted denominators hold as dual-asserted producer algebra on `D(U)`.
All-beta *original-source* emptiness on these two lines still carries the
already frozen N13-localization caveat: V34 `main()` is not run, and
`N13_full_source_lift_in_this_file=false` is honest.  Ranks and the P12
division were not recomputed here.**

Both theorem streams are rc `0\n`.  Stdout SHA-256:

| line | SHA-256 |
|---|---|
| `V=0,C=3U^2` | `61bb5fedba625711115ed7665a6ed23f37a54b0cff44356ecac0be717668ed4e` |
| `V=0,C=-5U^2` | `0be0c4093c27d21778853908afc90a3021831cb75a926a60981cffa4e166e8e2` |

Common skeleton, then the load-bearing markers:

```text
transport_rank=3470/3602
first_full_beta_P12_rank=38/132
first_full_beta_P12_dependent_count=0
P12_compiler=genuine_2893_term_source_polynomial
later_echelon_X0_t12_used=false
remainder_term_count=3
remainder_beta_degree=1
remainder_base_is_minus_k_over_50=true
remainder_beta_tail_terms=2
remainder_beta_tail_degree=0
P12_N13_polynomial_unit_identity_exact=true
P12_without_N13_negative_control=true
beta_division_used=false
combined_unit_residual_is_minus_k_over_50=true
N13_full_source_lift_in_this_file=false
```

Line-specific counts match the README:

| | `C=3U^2` | `C=-5U^2` |
|---|---:|---:|
| `raw_P12_term_count` | 1467 | 1468 |
| `raw_P12_base_terms` | 1465 | 1466 |
| `termwise_source_slot_count` | 29097 | 28570 |
| `first_source_nonzero_rows` | 28 | 28 |
| `first_source_multiplier_terms` | 1528 | 1512 |
| `first_relations_denominator` | `U^4` | `U^3` |
| `termwise_source_denominator` | `U^3` | `U^2` |
| transport events | 4 | 2 |

`raw_P12` and `first_rows` denominators are `(U)` on both lines;
`N13_multiplier_denominator` is `(1)`.  Flint `factor()` of every
emitted LCM is a power of `U`.

Genuine P12, not later-echelon `X0,t12`: `qd.compile_current` of the
six transport-restricted x-sections, slot `[12]`.  Dual’s generic
compiler still asserts a 2893-term base; the specialized bases here
are 1465 and 1466.  Those base SHA-256 values are byte-identical to
the frozen classical trivariate genuine-P12 bases on the same loci
(`4a2ac929…` and `68ad159a…`).  That is the same compiler after
`V=0` specialization, not a synthetic row keyed `X0,t12`.

Reduction and glue, from the executed V45 body:

- `divide_polynomial` reduces P12 by the 38 normalized first-row
  pivots and replays `remainder + sum quotient*pivot = P12`.
- `lift_relations` pushes quotients through stored original
  combinations.  `exact_first_source_replay` asserts
  `sum relation_i * source_polynomial(row_i, rhs_i) = P12 - remainder`
  and that adding `BetaPoly(1)` to the target destroys the identity.
  `source_polynomial` uses constant term `-rhs`, matching `pack`.
- `k = 252 - 342 S + 144 S^2 - 36 S^3`, `expected = -k/50`.
  `projection(remainder, 0) == {(): expected}` is asserted.
- `beta_tail` certifies `remainder = expected + beta * tail` without
  inverting beta (`assert not coefficient.constant` on the
  difference, then shift).  Tail degree 0, two terms.
- Abstract N13 is `BetaPoly([0, k/25])`, not a V34 current-row.
  Multiplier `(25/k)*tail`; contribution equals `beta*tail`; combined
  first-row identity plus contribution equals `P12 - (-k/50)`.
  `first_source_identity != P12 - (-k/50)` is the live
  P12-without-N13 control.  No division by beta.

Transport events are not printed by V45.  The per-250-row
pivot/event stream is byte-identical in the checkpoint numbers to the
frozen classical transports of the same matrix
(`cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v15/`):

```text
v-h-zero:     events=4 at rows=5500; rank 3470/3602
              (-U), (-1)/U, (4 U^2), (2 U)
v-cplus5-zero: events=2; (8 U^2), (2 U)
```

Those numerators/denominators are powers of `U` only.  Parent
transport charts of the classical runs are therefore U-only, and
V45’s first-row/P12 LCMs did not grow an extra prime.  A hidden
non-U transport factor would have to vanish from every first-row
coefficient LCM and from the classical event list of the same
matrix; there is no evidence of one.

Direct-q-prime control: `configure_qd(False)` builds `first_rows_omit`,
asserts inequality with the direct-q-prime pack, then restores
`True`.  That shows the first-J matrix depends on the `2 beta t`
slot.  It does **not** show that the P12/N13 unit identity survives
deletion of `q'`.  There is no separate omit AWS run.  That is the
correct scope of this control, not a second theorem.

**Defects, none of which kill the identities.**

- N13 is `BetaPoly([0, k/25])`.  V34 `main()` is not called.  The
  banner `N13_dependency=matching_V34_raw_staged_original_row_replay`
  is a label.  The already frozen N13-localization erratum is
  therefore still in force: these identities are exact
  cross-certificates with abstract `N13=(k/25)beta` on `D(U)`, not a
  composed original-source lift of staged N13 through previous/pole
  and transport on these lines.  `raw_fraction_field_full_beta_family_empty=true`
  is true in the quotient by that abstract relation, which is what
  V45 actually proves.
- V45 does not print transport events or compose a parent-style
  complete chart `transport_chart * first_source * inner`.  Emitted
  LCMs and the classical event list are still U-only, so the
  exceptional set of the *identity* remains `V(U)`.
- `n.digest = canonical_digest` patches the attribute used for
  tail/N13 hashes.  V34 `solve_stage` / `emit_stage_incompatibilities`
  still call the module-global `digest = sha256(repr(...))`, which is
  the address-bearing serializer V69 repaired for V33.  Pivot
  digests on these streams were not dual-host checked.

**Survival.**  Exact genuine-P12 first-row identities on both lines
over `Q(U)`, remainder `-k/50 + beta*tail`, algebraic N13 glue to
the unit `-k/50`, only powers of `U` in every denominator this file
emits.  Not a staged-N13 original-source cover of those lines, and
not a U=0 result.

---

## Charge 4 — `C=-U^2`: V45 rc-one harness and V46 unit certificate

**Result: holds as producer-asserted original-row first-band algebra
on `V=0, C=-U^2, D(U)`.  V45 rc-one is a rank-expectation harness,
not a theorem.  V46 is the adjudication.  Rank and the 13-row
combination were not recomputed here.**

V45 `--stratum=v-cplus1-zero` dies at

```text
assert len(first_pivots) == 38
AssertionError
```

rc `1\n` (SHA-256 `4355a46b…`, body exactly `1\n`).  Stdout SHA
`f45da292…` is an exact 43-line prefix of V46 stdout
`01fa0f2e…`, through

```text
first_full_beta_P12_rank=37/132
first_full_beta_P12_dependent_count=1
first_full_beta_P12_pivot_digest=4bb14a41eeaee074ba209217d51d8f4c858eb3ef0e6c42879bf0f0e514b7f2a3
first_full_beta_P12_original_row_replay=true
```

The harness expected the V45 P12 rank 38; the specialization is
strictly stronger and lower-rank.  That failure is fail-closed
evidence, not a missing identity.

V46 then asserts `len(first_pivots)==37`, exactly one nonzero
residual, `polynomial_ideal_gcd` with `gcd == BetaPoly(1)`, Bezout
replay `sum weight*residual = gcd`, and
`emit_stage_incompatibilities`.  Frozen theorem markers:

```text
first_full_beta_P12_incompatibility[0]_row_index=12
first_full_beta_P12_incompatibility[0]_key=('X-2', 12)
first_full_beta_P12_incompatibility[0]_degree=0
first_full_beta_P12_incompatibility[0]_source_row_count=13
first_full_beta_P12_compatibility_gcd_degree=0
first_full_beta_P12_compatibility_certificate_denominator=(U^6)
first_full_beta_P12_compatibility_certificate_denominator_factor=(1, [(U, 6)])
first_full_beta_P12_unit_certificate_denominator=(U^6)
first_full_beta_P12_only_U_exception=true
rational_raw_stratum_first_band_empty=true
```

`pack` keys are `(family, degree)`.  Packed degree 12 is first-J
`t^{12}`.  `source_row_count=13` is `len(combination)`.  Dependent
records start at `{row_index: 1}` and reduce through stored original
combinations of earlier pivots.  `solve_stage` replays each dependent
against original packed rows: empty matrix part and `replay_rhs == rhs`.
That positive identity is live.  There is no V70-style plus-one
wrong-row perturbation on this combination.

Beta degree 0 plus monic gcd one forces `gcd = 1` in `E(U)[beta]`.
No beta-root leftover.  N13 and P12 are not used: V46 `return`s
before the copied P12/N13 block.  Stdout has no `raw_P12_term_count`.
The leftover P12-without-N13 source after `return` is dead code.
The N13-localization erratum already recorded that this line is
independent of N13; that is correct.

Displayed `U^6` is the inner residual/Bezout/combination LCM, the
quantity V46 actually LCMs and factors, with
`assert all(factor == U ...)`.  It is **not** the parent complete
chart

```text
transport_chart * first_source * inner.
```

The matching classical transport of the same matrix
(`evidence/v15/v-cplus1-zero.stdout`) has events `(4 U^2)`, `(2 U)`,
transport chart `U^3`, first-source `U`, combination `U^6`, complete
chart `U^{10}`, and the same dependent key `('X-2', 12)` at packed
index 12.  Classical `source_row_count` is 7 rather than 13; that is
the same q2-beta vs classical ancestry split already seen on V33/V70.
All of those extra factors are still `U`.  The exceptional set of
the certificate is `V(U)` either way.  Treating printed `U^6` as
the parent complete chart would be the V33-style wording error; here
it does **not** hide a second prime, so it does not change D(U).

Direct-q-prime control is the same in-process matrix inequality as
V45.  It is not a second 13-row certificate without `q'`.

**Defects.**  None load-bearing for D(U) emptiness.  Printed
`P12_compiler=genuine_2893_term_source_polynomial` on V46 is a
copied banner; P12 is not compiled.  `*_compatibility_original_row_replay=true`
from V34 emit is a banner; the load-bearing replay is the
`solve_stage` assert that actually ran.

**Survival.**  First-J original-row unit incompatibility on
`V=0, C=-U^2 ∩ D(U)` for every beta, inner denominator `U^6`,
exceptional set `V(U)`.  V45 rc-one is the rank-38 harness control.
Not the origin, and not an N13 identity.

---

## Charge 5 — Custody, rc, controls

**Result: listed hashes recompute; declared source-check closure
holds; rc classifications are correct; omission/wrong-row controls
are exactly the ones that ran; lack of a dual-host mirror is a
custody gap, not a mathematical defect.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v45.tar.gz` | `e9dd234d861e9aa64a3087f2307186f20468e8a14296407ed01908ad34787164` | MANIFEST, README |
| `archives/td6-aws-handoff-20260825-v46.tar.gz` | `c3fab24308e36ffad4addf13c9b56e026e1eb96ac43ccad79aa01132adaa7487` | MANIFEST, README |
| `source/v45/replay.py` / extracted V45 leaf | `7e1370834460e2bc3123631825f04cb04a0b457a14449985635f3d0af86f8dd1` | MANIFEST, V45_SOURCE, README |
| `source/v46/replay.py` / extracted V46 leaf | `9b1670abf55a20f26f02abcc593083ce07dd2b1e4afa0571ac8b9a0f890203c7` | MANIFEST, V46_SOURCE, README |
| `source/v45/V45_SOURCE.sha256` | `1a286d49e53710100ea7f79549c28c230103b3f710f5a9b14cfabbab7feb4580` | MANIFEST, V46_SOURCE |
| `source/v46/V46_SOURCE.sha256` | `2fb26fcb1bf32fbb6d3b1e0212fef066b2ada2ed483dfca11a3e6812a005b10f` | MANIFEST |
| extracted V34 `replay.py` | `1743dc294ca3e3f7f8c1cc1a471d340fc2a1ac7e39d29eddf7e025327578a5c6` | V45/V46 pin |
| extracted dual `replay.py` | `cf3f3f028b99771a156a422d73a99eefdc9f04fbdc0698d8e8baf962efa4cf7f` | V34 pin, SOURCE |
| extracted trivariate | `1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea` | dual pin, SOURCE |
| `v45-v-h-zero.stdout` | `61bb5fed…` | MANIFEST, README, output.sha256 |
| `v45-v-cplus5-zero.stdout` | `0be0c409…` | MANIFEST, README, output.sha256 |
| V45 fail-closed stdout | `f45da292…` | MANIFEST, README, output.sha256 |
| V46 stdout | `01fa0f2e…` | MANIFEST, README, output.sha256 |
| theorem `rc` files | `9a271f2a…` | MANIFEST; body `0\n` |
| fail-closed `rc` | `4355a46b…` | MANIFEST; body `1\n` |
| README | `89d9e78f…` | MANIFEST |
| `MANIFEST.sha256` | `be876b0a…` | FREEZE |
| `FREEZE.sha256` file | `f93d1f46…` | N13-erratum AFFECTED_FREEZES |
| xmodel AWS report | `0101a2f2…` | FREEZE, AFFECTED_FREEZES |
| V33 u-zero MANIFEST/FREEZE | `0ae3c460…` / `1c860097…` | DEPENDENCIES (stale whole-U pin) |

All 54 MANIFEST paths recompute.  Both FREEZE paths recompute.  All 4
DEPENDENCIES targets recompute.  Extracted V45 and V46 `SOURCE.sha256`
are 31/31 against the trees.  Nested `V45_SOURCE`, `V46_SOURCE`,
`V34_SOURCE`, `V33_SOURCE` recompute.  Bundled producers are
byte-identical to the archive leaves that stderr executed.

Source-check stdout is the nested-manifest prefix (V45: 6 OK lines
through `V39_SOURCE.sha256`; V46: 6 OK lines through V44), not a
full 31-file walk.  That is weaker observability than V70, not a
hash mismatch: the portable bundles contain the ancestry that ran.

All four runs are r6d, Python 3.12.3, python-flint 0.9.0.  Three V45
invocations share `start_utc=2026-08-25T06:53:26Z`.  V46 is a later
adjudication (`07:04:58Z`--`07:05:18Z`).  Wall times ~5:52 / ~5:46 /
0:20 / 0:20; RSS ~580 MiB / ~187 MiB.  `PYTHONHASHSEED=0` is required
by the runbooks and is not visible in `time -v`.  There is no
`verify.py` in this package.  Host IPs are README-only.

**Controls, exactly as available.**

- Direct q-prime: in-process `first_rows_omit != first_rows` on all
  four invocations, including the rc-one prefix.  Not a second
  certificate without `2 beta t`.
- P12-without-N13: live exact negative identity on both V45 theorem
  streams.  Dead on V46 (`return` first).
- V45 rc-one: rank-38 harness, exact prefix of V46, not discarded.
- V46 original-row replay: positive `solve_stage` identity.  No
  plus-one wrong-row.
- No dual-host mirror.  Canonical identity of the *algebra* does not
  depend on proving a second host; pivot/residual SHA lines from
  V34’s `repr` digest would be the first thing a second host would
  disagree on, as in V33.

**Defects.**  None that touch the D(U) identities.  Custody nits are
collected below.  Dual-host absence is not a flip of the algebra.

**Survival.**  Freeze/manifest/archive/source hashes and rc
classifications survive independent recomputation.  Controls are
correctly scoped.

---

## Charge 6 — Scope: D(U) independent of U=0; freeze-time wording; V70 restoration

**Result: the three D(U) results stand independently of any U=0
theorem.  The frozen whole-line wording consumed the overbroad
V33/V69 whole-`U=0` claim and was never valid at freeze time.  The
later hostile-reviewed V70 origin leaf restores each line’s `U=0`
endpoint by a fresh composition.  That restoration does not
legitimate the old dependency, and it does not lift staged N13.**

Geometry of the endpoints.  Each charged line is

```text
V=0,  C = a U^2,   a in {3, -1, -5}.
```

Intersecting with `U=0` forces `C=0` and `V=0`, hence only the
origin `C=V=U=0`.  The three lines do **not** contain the rest of
the plane `U=0`.  The missing point of each `Q(U)` chart is the
origin, not `U=0 ∩ D(C)` and not `C=U=0 ∩ D(V)`.

Why the freeze-time composition was invalid, even before V70:

- V33/V69 as frozen claimed “the entire raw `U=0` divisor is empty”
  with displayed complete denominator 1.  Hostile review
  `706f6ad4…` returned `CONFIRMED_WITH_REPAIRS`: the surviving
  theorem is `U=0 ∩ D(C)`, transport chart `C^2`, parent complete
  chart `C^3`.  The origin has `C=0` and is not on that open.
- The U=0 erratum (`df746976…`) withdrew the whole-divisor sentences
  and quarantined “the parameter-zero endpoints in the all-beta
  rational-line … packages.”  This package is named there.
- DEPENDENCIES still pins the V33 u-zero MANIFEST/FREEZE.  README and
  xmodel still say the parameter-zero endpoint “lies in the
  separately frozen whole raw `U=0` divisor, already empty for every
  beta with a unit compatibility ideal.”  That sentence was false at
  freeze time: the endpoint is the origin, and V33 does not cover it.

V70, already hostile-reviewed `CONFIRMED`, rebuilds two leaves:

- `C=U=0 ∩ D(V)`: first-J, complete chart `V^3`;
- origin `C=V=U=0`: transport row 6460 / `('g','X',-19,20)`, complete
  chart 1.

Together with corrected V33 they partition `V(U)`.  For *these three
lines* the only required piece is the origin leaf.  Set-theoretic
fresh composition, not a specialization of anyone’s echelon:

```text
line = [line ∩ D(U)] ∪ {origin}.
```

- `line ∩ D(U)` is this package (V46 original-row unit; V45 P12/N13
  identities with the N13 caveat of Charge 3).
- `{origin}` is V70 origin, complete denominator one, same fixed
  section, polynomial beta.

The old V33 pin is not used.  V70 `u-h-zero` (`V≠0`) is not on these
`V=0` lines.  Corrected V33 (`C≠0`) is not on these endpoints.

N13 is a separate debt.  V70 does not run previous/current/N13 on
`C=3U^2` or `C=-5U^2`.  The N13-localization erratum remains in
force on those two D(U) all-beta *source-promotions*.  Endpoint
restoration does not cancel it.

**Defects.**  Freeze-time whole-line prose and the V33 DEPENDENCIES
pin are stale.  That is a nonmutating dependency/custody repair, not
a defect of the D(U) algebra that ran.

**Survival.**  D(U) results independent.  Endpoints restorable by
V70 origin.  Freeze-time whole-U dependency not retrospectively
valid.

---

## Charge 7 — Exact final scope

If the nonmutating dependency erratum described below is applied,
the restored theorem is only:

```text
in the fixed source-typed normalized A3 q2-beta section,
with q_beta = t + beta t^2 + t^25 and direct q_beta',
for every beta:

  V=0, C=-U^2     empty as a whole line
                  (V46 first-J original-row unit on D(U)
                   ∪ V70 origin);

  V=0, C=3U^2
  V=0, C=-5U^2    D(U) genuine-P12 / first-row / abstract-N13
                  unit identities with only U inverted,
                  plus V70 origin at U=0.
                  All-beta original-source promotion on those
                  two D(U) opens remains N13-erratum scoped.
```

It is not whole `H=0`, not whole `B3=0`, not whole A3, not another
TD6 modulus, not TD6, not SP-2, not landing, and not JC2.  Every
theorem stream already prints

```text
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

Those denials are correct.  Later independent original-row work on
`V=H=0, D(U)` exists outside this package and is not consumed here.

---

## Attempted flips that did not kill the supported D(U) algebra

- **Wrong center / B3 branch mix-up.**  `v-h-zero` asserts `H=0`,
  not `B3=0`.  On `C=3U^2, V=0`, `B3 = 128 U^6 ≠ 0` on `D(U)`.
  The two B3 branches are `C=-U^2` and `C=-5U^2` from the executable
  factorization.
- **Synthetic P12 / later-echelon `X0,t12`.**  Compiler is
  `compile_current(...)[12]`; banner `later_echelon_X0_t12_used=false`.
  Specialized base SHA-256 values match frozen classical genuine P12
  on the same loci.
- **Rank/harness confusion on `C=-U^2`.**  V45 rc-one is the rank-38
  assert.  V46 is rank 37, key `('X-2',12)`, 13-row unit.  Prefix
  identity of the two stdout files is exact.
- **Hidden non-U denominator.**  Every flint-factored LCM V45/V46
  print is a power of `U`.  Classical transport events of the same
  matrix are U-only.  Parent complete charts `U^{12}`, `U^9`, `U^{10}`
  on the three classical lines do not introduce a second prime.
- **Q-prime omission as a broader theorem.**  The live control is
  `first_rows_omit != first_rows`.  It is not used to drop `q'`.
- **Wrong residual sign.**  `source_polynomial` uses `-rhs`.  V45
  asserts remainder base `-k/50` and combined unit `-k/50`.  V46
  asserts `replay_rhs == rhs` and Bezout sum equal to `gcd=1`.  A
  sign error would have aborted.
- **Beta specialization / beta-root leftover.**  First pivots are
  forced degree 0.  V45 tail is degree 0; V46 residual and gcd are
  degree 0.
- **Stale V33 echelon specialized through `U=0`.**  Transport is
  rebuilt on `CENTER = (a U^2, 0, U)`.  Classical event numerators
  are `U`-powers, not the V33 `-C` events.
- **Endpoint mismatch.**  The U=0 point of each line is the origin,
  which V33’s actual open `D(C)` misses and which V70 origin hits.
- **Whole H / B3 / A3 / TD6 / SP-2 / JC2.**  Denied by producer
  flags, by the three-line charge, and by the N13 and U=0 errata.

## Attempted flips that would have killed a stronger claim, and did not apply to the surviving algebra

- **Abstract N13 treated as a full staged original-source lift on
  `C=3U^2` and `C=-5U^2`.**  Real if anyone promoted those two D(U)
  identities to a composed N13 certificate.  V45 prints
  `N13_full_source_lift_in_this_file=false`.  The N13 erratum already
  quarantined that promotion.  This review does not reverse it.
- **Printed V46 `U^6` treated as the parent complete chart.**  Real
  as a wording error; not real as a hidden prime.  Exceptional set
  remains `V(U)`.
- **Freeze-time “whole U=0 covers the endpoint” treated as valid.**
  Real, and withdrawn.  V70 origin is a new composition.

---

## Leftover nits (not load-bearing)

- Single r6d host; no Box02/Box03 mirror.
- No packaged `verify.py`.
- Source-check walks the nested-manifest prefix, not 31/31
  `SOURCE.sha256`.
- `PYTHONHASHSEED=0` is not visible in `time -v`.
- V45 canonical `n.digest` patch does not replace V34’s global
  `repr` digest used by GE reporters.
- V46 leftover P12/N13 source after `return`; copied P12 compiler
  banner.
- V45 leftover `b3-param` branch.
- Transport events not printed by V45/V46 (classical v15 of the
  same matrix still has them).
- `first_c1_c3_mpoly.py` is imported without a live hash pin.
- V31/V33 are archived and listed, not executed.
- Printed ring language after specialization still names the
  ambient `E(C,V,U)` in imported modules.
- DEPENDENCIES still names the V33 u-zero freeze and the older
  common-centering line-kill gate; neither is a live import.

---

## Required nonmutating repair (not a producer rerun)

No frozen producer byte needs to change.  The D(U) algebra that ran
survives.  What does not survive is the freeze-time whole-line
sentence that consumed V33/V69 as a whole-`U=0` theorem.

A nonmutating dependency/custody erratum on this package should:

1. Withdraw README/xmodel sentences that the parameter-zero endpoint
   is already covered by the frozen whole raw `U=0` divisor with
   complete denominator 1.  Record that this composition was invalid
   at freeze time (V33 chart `D(C)` misses the origin).
2. Replace that dependency with the hostile-reviewed V70 origin leaf
   (or the reviewed three-piece whole-`U=0` cover, of which the
   origin is the only piece these lines meet).  Pin V70
   FREEZE/review, not V33 MANIFEST/FREEZE, as the endpoint authority.
3. Restate whole-line scope exactly as Charge 7.  Keep the N13
   localization erratum in force on V45 all-beta source-promotion.
4. Optionally record that V46’s printed `U^6` is the inner
   certificate LCM, parent-complete still U-only.

That is custody/scope repair.  It is not a mathematical defect of
the V45 identities or the V46 unit.

---

## Survival statement

The frozen V45/V46 producer, if it ran as written, is a source-typed
triple of D(U) certificates in the fixed normalized A3 q2-beta
section:

- `V=0, C=3U^2` and `V=0, C=-5U^2`: transport rank `3470/3602`,
  first rank `38/132`, genuine 2893-term P12 compiler, original
  first-row replay, remainder `-k/50 + beta*tail` (3 terms, tail
  degree 0), algebraic glue to abstract `N13=(k/25)beta` yielding
  unit `-k/50`, slot counts 29097 and 28570, every emitted
  denominator a power of `U`.  Exact identities on `D(U)`.  Not a
  staged-N13 original-source lift.
- `V=0, C=-U^2`: V45 rc-one rank-38 harness retained; V46 first rank
  `37/132`, unique original dependent `('X-2',12)`, 13-row original
  combination, beta-degree 0, monic gcd 1, inner denominator `U^6`.
  Exact first-J obstruction on `D(U)`.

Each line meets `U=0` only at the origin.  The freeze-time appeal to
whole V33/V69 `U=0` was invalid.  Reviewed V70 origin restores that
endpoint by a fresh composition.  Restored scope is only these three
rational lines in this section, all beta, with the N13 erratum still
limiting original-source promotion on the two P12 lines.  It does
**not** survive as: whole `H=0`; whole `B3=0`; whole A3; other TD6
moduli; TD6; SP-2; landing; JC2; a specialization of V33 through
`C=0`; or a staged-N13 repair.

CONFIRMED_WITH_REPAIRS
