# Hostile bounded review: TD6 fixed-A3 q2-beta whole `U=0`

Referee: independent algebraic/source/custody pass of the frozen V33 raw
`U=0` theorem only.  Operations used: full read of the charged surfaces,
`tar` extract of the frozen archive into
`/tmp/jc2-td6-u-zero-review-grok-20260825/`, independent SHA256 via Python
`hashlib`, and short exact structural checks of center specialization,
`q_beta` / `q_beta'`, original-row GE, monic gcd/Bezout, and the parent
complete-certificate formula.  The two U=0 transport event polynomials
are identified by matching V33's printed GE stream to the already frozen
trivariate U=0 transport of the same matrix; those event polynomials are
not reprinted by V33.  No producer execution, no CAS, solver, Lean, or
other substantive computation.  Stored PASS strings are not authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-aws-20260825.md`,
`cases/td6_c1_c2_c3_q2_beta_u_zero_aws_20260825/`.

Producer actually executed, from frozen stderr:

```text
timeout 28800 /home/ubuntu/venvs/td6/bin/python jc2/cases/td6_c1_c2_c3_q2_n13_raw_20260825/replay.py --stratum=u-zero
```

Expanded tree basename `td6-aws-handoff-20260825-v33` matches the tarball
name.  Dual `main()`, V31 `main()`, and `--omit-direct-qprime` are not
called.

Import/hash pin chain executed by that producer, in order:

1. V33 `replay.py` (`9856dca2…`, independently recomputed; listed in
   `V33_SOURCE.sha256`) pins and imports
   `td6_c1_c2_c3_q2_beta_dual_20260825/replay.py`
   (`DUAL_SHA256=cf3f3f02…`).
2. Dual pins and imports
   `td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py`
   (`TRI_SHA256=1fb51264…`), then calls `tri.configure()`.  Dual defines
   `H = C - 3*U**2`.
3. Trivariate pins and imports
   `td6_c1_c3_two_center_cover_20260824/replay.py` (`56df638a…`).
4. That file imports `first_c1_c3_mpoly.py` **without** a hash pin
   (the file is nonetheless in `SOURCE.sha256` as `ce400cca…`); transport
   then loads `c1_pencil.py`, which pins
   `td6_jet_orbit_adjoint_20260824/replay.py` (`fb138b0f…`), which pins
   the q2 compiler
   `td6_boundary_q2_deformation_20260824/replay.py` (`0ba18447…`)
   and the moduli field
   `td6_moduli_uniform_third_band_20260824/replay.py` (`7a21f949…`).

V31 `td6_c1_c2_c3_q2_n13_20260825/replay.py` is in the archive and in
`V31_SOURCE.sha256`, but it is not imported by V33.

---

## Charge 1 — Exact source scope

**Result: holds in source.**  Fixed normalized A3 center `(C,V,U)`, raw
specialization `U=0` with `C,V` retained as indeterminates, polynomial
`beta`, direct `q_beta'=1+2 beta t+25 t^24`, remaining TD6 moduli frozen.

- V33 accepts exactly one `--stratum=` and optional `--omit-direct-qprime`.
  Frozen argv is `--stratum=u-zero` only.  Stdout:
  `raw_center_stratum=u-zero`, `direct_qprime_retained=true`.
- Trivariate `STRATUM` is read from the same argv at import, before
  `center_coordinates()` runs.  On `"u-zero"` it returns
  `Rat3(C), Rat3(V), Rat3(0), "U=0 over Q(C,V)"`.  It does not take the
  `generic`, `h-zero`, `v-zero`, `u-h-zero`, `origin`, `v-h-zero`,
  `v-cplus1-zero`, `v-cplus5-zero`, or `b3-param` branches.  Frozen stdout
  is `source_center=U=0 over Q(C,V)`.
- V33 copies those three coordinates into `r.fb.CENTER` and clears the
  x-power cache before `build_transport`.  `x_power_expansion` is
  polynomial in `(c1,c2,c3)`; `c3=0` drops the `U` terms and never
  divides by `U`.
- Transport g-boundary is `{1: 1, 25: 1}` (the `t + t^{25}` skeleton).
  The `beta t^2` term enters only through `source_vector_beta`, which
  attaches a derivative `ONE_VECTOR` solely at key `("g","X",0,2)`.
  Direct `q'` is installed after transport by `configure_qd(True)`:
  `qd.Q_PRIME = {0: 1, 24: 25, 1: BetaPoly([0, 2])}`, i.e.
  `1 + 2 beta t + 25 t^{24}`.  `qd` is the jet-orbit-adjoint module, so
  this mutates the `Q_PRIME` global that `first_band_polynomials` reads.
  `--omit-direct-qprime` is not on the argv.
- `p = t^{15}` is the f-boundary `{15: 1}` and the first-band `-15`
  shift at degree 14.  F1 patterns, pole scale/data, and the licensed
  zero dead stretch are the imported `fb` constants.  V33 does not
  reprint the dual banners `source_p_boundary=…` / `source_F1_orbit=…`;
  the objects used are still those frozen constants.
- `solve_stage` raises `AssertionError("beta-dependent pivot: exceptional
  strata required")` if any accepted lead has `lead.degree != 0`.
  `BetaPoly.inverse` exists only for degree 0.

**Defects.**  None in the typing.  Two expository nits: V33 prints
`ring=E(C,V,U)[beta]` after `U` has been set to `0`; the working
coefficient field is `E(C,V)[beta]`.  The imported trivariate module
docstring is leftover B3-chart language (`C,V,U` as `t,w,j`).  The
`center_coordinates()` body, not that docstring, is what ran.

**Smallest repair.**  Print `ring=E(C,V)[beta]` on `u-zero`, or print
`H_after_U_zero=C` next to `source_center`.

**Survival.**  The producer is source-typed as the raw chart `U=0` over
`Q(C,V)`, with polynomial `beta` and direct `q_beta'`, inside the fixed
normalized A3 q2 section.

---

## Charge 2 — Transport rank `3470/3602`, first rank `36/132`, key `('X-2',14)`

**Result: holds as producer-asserted facts with an exact shared-transport
fingerprint.  Ranks were not recomputed here.**

`factor_transport` and `solve_stage` print rank from the GE they just
ran.  Frozen stdout:

```text
transport_rank=3470/3602
transport_event_count=2
transport_free_count=132
first_rank=36/132
first_dependent_count=1
first_incompatibility[0]_row_index=13
first_incompatibility[0]_key=('X-2', 14)
first_incompatibility[0]_source_row_count=14
```

`parameterize` returns `None` as soon as `emit_stage_incompatibilities`
sees a nonzero residual, so previous/current stages are not entered.
The PASS banner is `TD6-A3-Q2-N13-RAW-FIRST PASS`.

The transport matrix does not depend on `q_beta`.  `factor_transport`
ignores RHS.  V33's per-250-row pivot/event stream is byte-identical in
the checkpoint numbers to the frozen trivariate `U=0` transport
(`cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v11/tricenter-u-zero.stdout`
and the earlier bivariate `u_zero_v5.stdout`):

```text
rows=4750;pivots=1716;events=0
rows=5000;pivots=1966;events=1
rows=5250;pivots=2215;events=1
rows=5500;pivots=2465;events=2
… pivots=3465 at rows=6500;  rank 3470/3602
```

Those frozen U=0 transports printed the two event leads that V33
swallows:

```text
transport_event[0]=4804,('f', 'X', -1, 2),193;num=(-C);den=(1)
transport_event[1]=5380,('g', 'X', -1, 2),1289;num=(-C);den=(1)
transport_chart_denominator=(C^2)
```

Event 1 sits in `(4750,5000]` and event 2 in `(5250,5500]`, matching
V33's checkpoint flips.  First-J rank `36/132` and dependent key
`('X-2',14)` at packed `row_index=13` are the same locus as that
classical first band; V33's combination is 14 original q2 rows rather
than the classical 1-row multiplier.

`transport_matrix_beta_independent=true` and
`transport_x_and_pole_sections_exact=true` are banners, not second
tests.  The empty transport compatibility list is the real gate:
`if compatibility:` would have exited as `RAW-TRANSPORT PASS` and did
not.

**Defects.**  V33 never prints the two event polynomials.  That is a
certificate omission, charged under 4, not a rank mistype.

**Survival.**  Producer-asserted ranks and the unique first dependent
`('X-2',14)` survive.  Independently, the U=0 transport chart of this
matrix is `C^2`.

---

## Charge 3 — Beta-degree zero, 14-row original replay, monic gcd `1`, Bezout

**Result: holds as producer-asserted original-row algebra, with one
banner that is not a second composed replay.  The combination itself
was not recomputed here.**

- `first_incompatibility[0]_degree=0` and
  `first_compatibility_gcd_degree=0`.  `solve_stage` already refused
  any beta-dependent pivot.  There is no beta-root stratum.
- Dependent records store a combination over **original** row indices,
  starting at `{row_index: 1}` and reducing through stored original
  combinations of earlier pivots.  On a zero row, V33 replays
  `sum weight_i * original_row_i` and asserts the matrix part is empty
  and the RHS equals the residual.  That is an original-row identity,
  not an echelon-row assertion.
- `pack('X-2', …)` keys are `(family, degree)`.  Packed degree 14 is
  first-J `t^{14}`.  `source_row_count=14` is `len(combination)`.
- There is exactly one bad residual, so `polynomial_ideal_gcd` is
  monic scaling of that single generator: `gcd = residual *
  residual.leading.inverse()`.  Degree 0 plus monic forces `gcd = 1`
  in `E(C,V)[beta]`.  The xgcd/ideal helpers both `assert`
  `sum weight*value == gcd`.
- Signs: no extra `normalizer = -1` is applied.  The identity is
  `residual^{-1} * residual = 1`.  `pack` uses RHS `-constant`; the
  replay is against that same convention.
- `first_compatibility_original_row_replay=true` is printed
  unconditionally after the gcd, not a second replay of
  `(bezout * combination)` against the original rows.  For one bad
  row the composition is algebraic from the two asserts.

**Defects.**  None load-bearing.  The composed unit certificate
`(residual^{-1} * combination) · original_rows = 1` is not itself
reprinted or re-asserted.

**Survival.**  On this chart the first-J incompatibility is
beta-degree 0 with a 14-row original combination and monic gcd `1`.

---

## Charge 4 — Complete certificate denominator `1`; no discarded C/V/beta stratum

**Result: REFUTED as a completeness and specialization claim.**  The
printed LCM is not the parent complete certificate, and it silently
drops the transport-chart factor `C`.  The entire `U=0` divisor does
not follow.

V33's `emit_stage_incompatibilities` LCMs only

```text
residuals + bezout weights + combination multipliers + gcd.inverse()
```

and prints

```text
first_compatibility_certificate_denominator=(1)
first_compatibility_certificate_denominator_factor=(1, [])
first_generic_raw_stratum_empty=true
```

The parent trivariate emitter, still sitting in the same imported
`c1_c2_c3_trivariate.py`, defines the complete chart as

```text
transport_chart * first_source_denominator
  * combination_denominator * residual_denominator
```

and sets `whole_stratum_empty` only if that product has degree 0.
On the frozen U=0 transport of this same matrix the factors were

```text
transport_chart_denominator=(C^2)
first_source_denominator=(C)
combination_denominator=(1)
residual_denominator=(1)
certificate_chart_denominator=(C^3)
whole_stratum_empty=false
```

V33 includes the last two 1's and omits the first two C-powers.
`denominator_lcm` itself only sees Rat3 *polynomial* denominators;
constant-field Q-denominators of E are absorbed into numerators and
would not appear even if present.  Over E those are units, so they
are not a C/V stratum.  The missing `C^2` is not a unit.

Specialization: the two U=0 transport pivots have lead `-C`.  At
`C=0` those leads vanish, so the 3470-pivot / 132-free
parameterization of this run does not specialize.  `C=0` on `U=0`
is exactly `H=0` after `U=0` (`H=C-3U^2` becomes `C`).  That is the
already-named raw stratum `u-h-zero`, which this package did not
run.  Declaring “no residual C- or V-factor” discards that locus.

Beta is not discarded: gcd degree 0, all first pivots beta-independent.

**Defects.**  Theorem defect, not a nit.

1. “Complete certificate denominator = 1” is false as a complete
   chart: it is an LCM of residual/Bezout/combination only.
2. The entire `U=0` divisor is not proved.  The supported open is
   `U=0` and `C ≠ 0` (equivalently the function field `E(C,V)` of
   this chart).  `C=U=0` remains charged.
3. xmodel/README promote the incomplete LCM to “no residual C- or
   V-factor” and “entire raw U=0 center divisor empty … over every
   extension of E”.  That overreaches the producer runbook, which
   still says a degree-zero gcd proves emptiness only on the printed
   raw fraction field, and which prints
   `raw_fraction_field_not_complete_stratum=true` (unconditional
   banner, but the right methodological warning).

**Smallest repair.**  Erratum the theorem to emptiness of the fixed
A3 q2-beta section on the raw chart `U=0` over `D(C)`, i.e. in
`E(C,V)[beta]`, with remaining raw obligation `C=0` (stratum
`u-h-zero`, and then origin).  Reprint the two transport events, or
multiply the printed LCM by `transport_chart_polynomial(events)`.
Do not say the complete denominator is `1`.

**Survival.**  First-J q2-beta incompatibility on `U=0 ∩ D(C)` for
every beta, in this fixed section.  Not the whole plane `U=0`.

---

## Charge 5 — Custody

**Result: listed hashes recompute; source-check closure holds for the
declared manifests; `rc=0`; the archive contains the executed V33
producer and its pin chain.  Six printed algebraic sha256s are not
content hashes.**

Independent SHA256 (Python `hashlib.sha256` of file bytes):

| object | SHA256 | matches |
|---|---|---|
| `archives/td6-aws-handoff-20260825-v33.tar.gz` | `718457551eab373d043e9b711aa8df06fc18fccecb31bb97c2250284f55c48e2` | MANIFEST, README, xmodel |
| `evidence/n13-u-zero.stdout` | `94e2267d62b162f44abaf32d36405440dd213e1efb4f446cc281ace08b47d0da` | MANIFEST, README, xmodel |
| `evidence/n13-u-zero.stderr` | `63de97c9cac23252a736da9d02b14f874ee0e9e30ec0e4c3373f5c5d25fb6791` | MANIFEST, README |
| `evidence/rc` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | MANIFEST; body `0\n` |
| `evidence/source-base.stdout` | `d6aa62c59b110fcf3da35af6b3f26c12b4ff0cb55434ed52ee94bd2e767e2664` | MANIFEST |
| `evidence/source-v31.stdout` | `2f71913e5f24c18811f8dc448ca3ae4fd7acdb61c8acfc3727a3003f366080e5` | MANIFEST |
| `evidence/source-v33.stdout` | `5bf058979930a50ba9045893e070814cb7f246b1bf1a20afa2f48b6bc9d618eb` | MANIFEST |
| README | `eeed5ecc6f735edb3e331b998f7fcab027f69491da9afe575cd5ab7d80639e2b` | MANIFEST, FREEZE |
| `MANIFEST.sha256` | `0ae3c4602e09279c9213f48ce0d0bb4c98e243129b46b47e96e428aaad8291b0` | FREEZE |
| `DEPENDENCIES.sha256` | `ced03c05cbbc57638922f67a53059ba3697152b8a710b7a2b57485c06e598dd3` | MANIFEST, FREEZE |
| xmodel report | `4e19a56bbaeb56e46c25ff3342c3b3a927be46a0d31a2641899a889cedbae635` | FREEZE |
| extracted `V33_SOURCE.sha256` | `dbca25673571f125cd949617f9879721db45541368a25b4b9b94042357782350` | README |
| extracted V33 `replay.py` | `9856dca271754843acc761d2e4ca57a3a27d1a4cab6fed1c3ebe861494ac9026` | `V33_SOURCE.sha256` |
| extracted `SOURCE.sha256` | `a71f9aef89bde54bbdb1ffcdf7090ea557e137348e28736b4dd4b1572e5bbc90` | `V31_SOURCE.sha256` |

All 9 MANIFEST paths recompute.  All 4 FREEZE paths recompute.  All 4
DEPENDENCIES targets recompute.  All 31 `SOURCE.sha256` members, all 3
`V31_SOURCE.sha256` members, and both `V33_SOURCE.sha256` members
recompute against the extracted tree.

Source-check stdout: 31/31 `: OK` (base), 3/3 (V31, including
`SOURCE.sha256`), 2/2 (V33).  The extracted tree has 38 files: the 36
listed members plus the two unlisted manifest files `V31_SOURCE.sha256`
and `V33_SOURCE.sha256`.  Check stderr is not frozen; README claims it
was empty.

Stderr is only `/usr/bin/time -v`, wall `0:22.78`, RSS `201132` KB,
`Exit status: 0`.  README also claims “archive xattr warnings”; the
frozen stderr file contains none.

`digest()` is `sha256(repr(value))` and `BetaPoly.__repr__` calls
`repr` of `E3` coefficients.  `E3` has no `__repr__`, so the six
printed algebraic fingerprints

```text
first_pivot_digest
first_incompatibility[0]_residual_sha256
first_incompatibility[0]_source_certificate_sha256
first_incompatibility[0]_bezout_sha256
first_compatibility_gcd_sha256
first_compatibility_bezout_sha256
```

embed process addresses.  They are not replay-stable content hashes.
Ranks, keys, degrees, and the printed denominator string do not use
those fingerprints.

**Hosts.**  README states r6d `100.26.198.153` and tag
`td6_v33_n13_u-zero_r6d_20260825T0528Z`.  Those strings do not appear
in stdout or stderr.  The artifacts prove one timed invocation of the
V33 producer with `--stratum=u-zero`.  They do not prove the IP.

**Survival.**  Freeze/manifest/archive/source hashes, `rc=0`, 36/36
declared source-check, and “the archive contains the code that ran”
all survive independent recomputation.  The six `repr(E3)` digests do
not.

---

## Charge 6 — Scope

**Result: the strongest statement the artifact can support is emptiness
of the fixed source-typed A3 q2-beta family on the raw chart `U=0`
over `D(C)`.  It does not cover `C=0` on `U=0`, `U!=0`, whole A3,
other moduli, TD6, SP-2, landing, or JC2.**

Stdout and xmodel both print:

```text
full_A3_beta_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

Those denials are correct.  The overreach is the positive claim
“entire `U=0` center divisor empty for every beta over every
extension of `E`”.  Charge 4 is why that is too strong: the transport
chart is `C`, and `C=0` on `U=0` is a different raw stratum.  “Every
extension of `E`” does not license specializing through a vanished
transport lead.

No claim is made, or earned, about `U!=0`, H or B3 as center
equations, p-boundary, dead stretch, F1, pole scale, whole TD6,
SP-2, landing, or JC2.  V33 never varies those moduli.  Dual’s
generic open `D(U*(C-3U^2)*B3)` is a different producer.

**Defects.**  The entire-divisor sentence in xmodel/README.  The
scope *ceiling* in the charge is exactly that sentence; the artifact
does not reach the ceiling.

**Survival.**  Fixed-section first-J emptiness on `U=0 ∩ D(C)`, and
nothing stronger.

---

## Attempted flips that did not kill the supported theorem

- **Illicit extra specialization.**  `center_coordinates()` keeps
  generic `C,V`.  `U` is the only center coordinate set to `0`.
- **Q-prime omission.**  `--omit-direct-qprime` is absent;
  `configure_qd(True)` writes the `beta t` slot; stdout
  `direct_qprime_retained=true`.  This package did not freeze an omit
  control.
- **Rank/dependency mistype.**  Printed ranks match the GE
  `len(pivots)/nvariables` formula; the unique bad key is
  `('X-2',14)` at packed index 13, the same first-J slot as the
  classical U=0 band.
- **Beta specialization.**  Pivot leads are forced degree 0; the
  residual is degree 0; gcd degree 0.  No beta-root leaf.
- **Gcd/Bezout sign.**  One generator, monic scaling, asserted
  identity `weight*residual = 1`.  No hidden minus.
- **Echelon-only certificate.**  Combination and replay are over
  original packed first-J rows.
- **Archive mismatch.**  Executed path, dual pin, trivariate pin, and
  q2/moduli pins are in `SOURCE.sha256` / `V33_SOURCE.sha256` and
  live-hash to the listed values.
- **Whole-A3 / TD6 / SP-2 / JC2.**  Denied by the producer flags.

## Attempted flip that did kill the claimed theorem

- **Hidden C denominator / entire-divisor overreach.**  Real.  The
  U=0 transport inverts `-C` twice.  V33’s “complete” LCM does not
  include that chart.  `C=U=0` is not covered.

---

## Leftover nits (not load-bearing)

- `E3` has no `__repr__`; six stdout sha256s are address-dependent.
- README mentions xattr warnings that are not in the frozen stderr.
- Host IP/tag are README-only.
- Source-check stderr is not frozen.
- `first_c1_c3_mpoly.py` is imported without a live hash pin.
- `first_compatibility_original_row_replay=true` is a banner.
- `transport_matrix_beta_independent=true` is a banner.
- Printed ring still names `U` after `U=0`.
- Trivariate module docstring is B3-chart leftover.
- V31 is archived and checked but not executed.
- `raw_fraction_field_not_complete_stratum=true` is unconditional, so
  it does not by itself record a remaining C obligation.

---

## Survival statement

The frozen V33 producer, if it ran as written, is a source-typed raw
`U=0` first-J incompatibility in the fixed normalized A3 q2-beta
section: transport rank `3470/3602`, first rank `36/132`, unique
original dependent `('X-2',14)`, 14-row original combination,
beta-degree 0, monic compatibility gcd `1`, combination/Bezout/residual
Rat3 denominators `1`.  That is an exact obstruction on
`U=0 ∩ D(C)`, i.e. over `E(C,V)[beta]` in this section.

It does **not** survive as: emptiness of the whole plane `U=0`;
absence of a C-factor; a `u-h-zero` or origin theorem; a complete
certificate in the parent sense; a `U!=0` result; whole A3; other
TD6 moduli; TD6; SP-2; landing; or JC2.  The six `repr(E3)`
fingerprints are not content hashes.

Required repair is a scope erratum (Finding, Charge 4), not a
different center and not a different first-J row.

CONFIRMED_WITH_REPAIRS
