# Hostile review V2: TD6 V57 generic source DAG plus nonmutating repair

Inspection only of the four charged surfaces.  No producer execution, no
`verify.py` run, and no `replay.py` run.  Stored `PASS` strings were
ignored as proof.  Frozen file bytes were hashed with Python `hashlib`
and compared by exact equality.  The portable archive was listed and
read, not unpacked into the tree.  Printed ledger products were
reconstructed by rational monomial arithmetic; Flint was not re-invoked.

Charged surfaces:

- `cases/td6_c1_c2_c3_q2_generic_source_dag_v57_aws_20260825/`
- `xmodel/td6-c1-c2-c3-q2-generic-source-dag-v57-aws-20260825.md`
- `cases/td6_c1_c2_c3_q2_generic_source_dag_v57_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-generic-source-dag-v57-review-repair-20260825.md`

The original eight load-bearing points are re-audited from source and
evidence.  The V1 findings in the hash-pinned adapter log
`e7b580724de2b95bf6a96a8c2e0e51d2e54ae4edff8eded95492bde4efbc617a`
are then checked against the nonmutating supplement: ancestry, omission
flag, P12/remainder banner, q/q-prime timing, `k`-unit status,
leaf-ledger versus V43 termwise `H^3`, source-manifest custody, and the
withdrawn two-chart-glue banner.

Producer actually executed: archive path
`jc2/cases/td6_c1_c2_c3_q2_full_source_glue_dag_v57_20260825/replay.py`
via `run_v57.sh` (`PYTHONHASHSEED=0`).  Internal tarball directory is
`td6-aws-handoff-20260825-v55v56/`.  Parent `main()` is not called.

---

## Findings

**1. [Confirmed] Source typing is the generic chart `(C,V,U)` with
polynomial beta and live direct `q_beta'=1+2 beta t+25 t^{24}`.**

V57 assigns `r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))` and clears the
X-power cache before transport.  It does not take `h-zero`, `u-zero`,
`b3-param`, or any other `center_coordinates()` branch.  `sys.argv[1:]`
is asserted empty, so V34 `STRATUM` remains `generic` and
`--omit-direct-qprime` is absent.

Dual defines `H = C - 3 U^2`.  Trivariate defines the printed

```text
B3 = 4 C^2 U^2 - 4 C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6.
```

After transport, `n.configure_qd(direct_qprime=True)` installs

```text
qd.Q_PRIME = {0: BetaPoly(1), 1: BetaPoly([0, 2]), 24: BetaPoly(25)}
```

on the adjoint module.  `first_band_polynomials` reads that module-level
`Q_PRIME`; `compile_previous` / `compile_current` copy it onto the
deformation module for the duration of `compile_x_*`.  That is the
coefficient list of `1 + 2 beta t + 25 t^{24}`.

The stdout banners `q_beta=t+beta*t^2+t^25` and
`q_beta_prime=1+2*beta*t+25*t^24` are printed at the top of `main()`,
before `configure_qd`.  They are not asserts.  The live install is the
`configure_qd(direct_qprime=True)` call.  The supplement classifies those
banners as non-evidence.  V57 does not rerun V43’s omit-qprime matrix
inequality; retention is the live `Q_PRIME[1]` assignment, not a second
omit control.

**2. [Confirmed] Unique current-row N13 dependency; original current
reduces through previous/pole pivots and original first rows; no
linear-only packing of source rows.  The fourteen printed previous keys
are a lift cache, not N13 ancestry.**

Echelon first/previous/current still go through `qd.pack`, which asserts
every nonzero monomial has length 1 (the V48 failure class).  That
packer is not applied to the replayed 132-variable originals.
`source_records` keeps `g.clean(polynomial)` at every degree, including
zeros and degree 2.  Raw previous is `compile_previous` plus
`compile_pole_previous` on the 132-variable bands (54 rows, 36
quadratic).  Raw current is `compile_current` on those same 132-variable
bands.

`divide_polynomial` replays `remainder + sum quotient * pivot == original`
before returning.  `lift_previous_key` divides a raw 132-variable
previous polynomial by first pivots and asserts original-first replay.
`lift_current_key` divides the raw current polynomial by first pivots,
remaps, divides by previous/pole pivots, then rebuilds a composed first
relation with scale `-1` on the nested previous-first product.  It
asserts the composed replay against original first rows and raw
previous/pole rows equals `raw_current - embed(remainder56)`.

`current_dependent` is filtered to `('X0', 13)` with nonzero rhs;
`len(n13_records) == 1`.  Frozen DAG: `current_row_index=13`,
`current_row_key=('X0', 13)`, `N13_left_null_support=1`,
`previous_nonzero_rows=1`, `composed_first_nonzero_rows=28`.
`remainder56`, staged left-null, and `{(): -n13}` share digest
`fd4415b2…`, so the reduced current row is already the scalar `-n13`
with left-null weight 1.

The printed list

```text
previous_rows_source_lifted_keys =
  ('X-1', 0) … ('X-1', 12), ('X-1', 14)
```

is `sorted(previous_first_relations_by_key)`.  That cache is filled by
lifting **both** P12 and N13, plus the forced quadratic positive control
`('X-1', 0)`.  It is not N13 support.  The DAG records one N13 previous
original-row summand and does not name its key.  No `P1` key appears in
the cache, so that unique previous original-row edge is an `X-1` row,
not a pole original row.  Pole rows sit in the previous/pole echelon
(`previous_pole_v50_rank=38/94`) as packed pivots; they are not N13
original-row summands.

`proof_rule=exact_edge_substitution_in_free_equation_module` is a
proof-representation choice: V57 does not expand the giant 132-variable
N13 source polynomial.  Nested products of previous-first multipliers
are intentionally not expanded beyond the `-1` correction.  That is not
linear-only packing.

The supplement states this classification and does not invent a
singleton key the frozen producer never printed.

**3. [Confirmed] Genuine 2,893-term P12 original-row replay; live glue
is the first-remainder identity `R - M N13 = -k/50`; `k` is a unit of
`E`.**

P12 is `compile_current(...)[12]` on the 132-variable bands, looked up
as `raw_current_rows[('X0', 12)]` via `source_records`, not the packed
later-echelon `X0,t12` row.  Live checks:

- `len(projection(p12_raw, 0)) == 2893` and digest `8d5c3550…`, matching
  pinned V43 `raw_P12_base_sha256`;
- `lift_current` of that raw polynomial, so P12 does get an original-row
  replay through first and previous, with the composed remainder56
  identity;
- the glue uses `p12_remainder94` (after first pivots, before previous):
  `projection(remainder94, 0) == {(): -k/50}`;
- `tail = beta_tail(remainder94, -k/50)`, remapped to 132 variables;
  digest `0639f8cd…` matches V43 `remainder_beta_tail_sha256`;
- `n13 == (k/25) beta` and `k * k.inverse() == E3(1)`;
- `M := (25/k) * tail`; `M * n13 == tail * beta`.

Let `R` be that first-pivot remainder.  Then `R = -k/50 + beta * tail`,
so `R - M * n13 = -k/50`.  The sign of the residual is the written
`-k/50`.  The last multiplier identity is automatic from
`n13 = (k/25) beta` and the definition of `M`.  Nontrivial live algebra
is the 2,893-term compiler, the first-remainder projection, and the
invertibility of `k`.

Typing of `k`:

```text
S = E3(qd.uniform.S_FIELD)
k = E3(252) - 342*S + 144*S**2 - 36*S**3
```

`k` is an `E`-constant in the `(C,V,U)` chart, not a polynomial in
`C,V,U`.  `E3.inverse` itself asserts `self * result == E3(1)`.  V57
repeats `k * k.inverse() == E3(1)`.  Invertibility is the nonvanishing
and unit statement in the residue field `E`, hence in `E(C,V,U)`.  `50`
is inverted in `Q`.  Ledger keys `N13_scalar` and `P12_unit` land on
`1`, so `k` contributes no extra `(C,V,U)` leaf factor.

V43 `main()` is not called.  Parent `main()` proves
`first_source + M N13 = P12 - (-k/50)` against original first rows
(28 nonzero rows, 1,648 multiplier terms, 39,583 termwise slots).  V57
scans six V43 stdout markers, including
`full_beta_first_original_row_replay=true` and
`P12_N13_polynomial_unit_identity_exact=true`.  DAG line
`P12_source_edge=V43_CANONICAL.stdout` is accurate.  DAG line
`P12_minus_multiplier_times_N13_equals_minus_k_over_50=true` names the
full polynomial identity; the live V57 assert is the remainder identity.
The supplement reads that flag as
`P12_first_remainder_minus_M_n13_equals_minus_k_over_50`.

**4. [Confirmed] Both negative controls are exact against weaker
statements: singleton current-row omission, and `tail ≠ 0`.**

`omitted_index = min(n13_weights)`.  Support size 1 implies row 13.
The control is `staged_without_one != {(): -n13}`.  With singleton
support that is `{} != {(): -n13}`, i.e. `n13 ≠ 0`.  It does not drop
the unique previous original-row multiplier or a first-row edge and
re-test.  `omitted_row_index=13` in the DAG records that fact.  The
supplement reads the flag only as
`N13_singleton_current_row_omission_negative_control`.

P12 without N13: `M * 0 != tail * beta`, i.e. `tail ≠ 0`.  Together with
`R = -k/50 + beta*tail` this says first rows alone do not produce P12
with residual `-k/50`.  V43’s parent has the stronger in-memory test
`first_source_identity != P12 - (-k/50)`.  V57 does not re-assert that
object inequality; it pins the V43 marker.  Neither control tests
omission of the unique `X-1` previous edge.

Both controls hit real identities (`n13 ≠ 0`, `tail ≠ 0`).

**5. [Confirmed] Eleven leaf-coefficient denominator entries; reconstructed
products have radical support only in `{U, H, B3}`.**

Header plus 11 data rows; stdout `DAG_leaf_denominator_count=11`.  Gate
is `b.factors_only_allowed`, which returns true iff Flint `factor()`
emits only `U`, `H = C-3U^2`, and `B3`.  Independent reconstruction of
every claimed product (rational monomial arithmetic, no Flint):

| denominator | claimed factors | reconstructs? |
|---|---|---|
| `1` | `[]` | yes (unit) |
| `C-3U^2` | `H` | yes |
| `CU-3U^3` | `U H` | yes |
| `C^2-6CU^2+9U^4` | `H^2` | yes |
| line 5 (9 terms) | `(1/4) H B3` | yes |
| line 6 | `(1/4) U H B3` | yes (= line 5 × `U`) |
| line 7 | `(1/4) H B3 U^2` | yes (= line 5 × `U^2`) |
| line 8 (11 terms) | `(1/4) B3 H^2` | yes |
| line 9 | `(1/4) U B3 H^2` | yes (= line 8 × `U`) |
| line 10 | `(1/4) U^2 B3 H^2` | yes (= line 8 × `U^2`) |
| `U` | `U` | yes |

No extra prime appears.  Units `1/4` are in `Q`.  Multiplicity is
leaf-occurrence count, not algebraic multiplicity of a prime.  First
labels are N13 weights / first multipliers / previous rows, plus later
`N13_scalar`, `P12_unit`, `P12_beta_tail`, `N13_multiplier` sharing
those keys.

Not in the 11 lines: P12’s own first-row multipliers.  V43
`first_relations_denominator` is line 10’s polynomial, but V43’s
termwise `(1/4) U B3 H^3` is only a DAG string
`v43_termwise_denominator=(1/4)*U*B3*H^3`, copied from V43 stdout, not
fed through V57’s ledger.  Transport’s two events are not ledgered.
Leafwise radical still cannot grow under products/sums; extra **powers**
of `H` can (V43 termwise `H^3` versus V57 leaf max `H^2`).  The
supplement states this exactly.

Flint’s treatment of `B3` as a single factor was not re-run.  `B3` is
not an obvious `(2CU-V^2+p U^3)(2CU-V^2+q U^3)` over `Q` (`p+q` cannot
be both 12 and 20).  Independent irreducibility of `B3` over `Q` is not
a V57 theorem; the claim is leaf support inside `{U,H,B3}`.

**6. [Confirmed] Dual-host DAG/ledger equality; source archive and
manifest custody hold; uncharged helpers are source-manifest pinned, not
import-assert pinned.**

Independent SHA-256 of every original `MANIFEST.sha256` entry: zero
mismatches.  Original `FREEZE.sha256` walks: zero mismatches.  Repair
`MANIFEST.sha256` / `FREEZE.sha256` walks: zero mismatches.

Positive identity bytes, identical across r6d and Box03:

| object | SHA-256 |
|---|---|
| proof DAG | `a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32` |
| leaf ledger | `69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf` |
| `rc` (`0\n`) | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |

Stdout mathematical lines agree after dropping the two absolute artifact
paths (`td6_v57_dag_r6d_20260825T1048Z` versus
`…_box03_20260825T1108Z`): 94 lines, including all rank, digest, and
scope flags.  Independent runs, not a copy: distinct systemd units,
wall 1:52:37 versus 1:46:10, RSS `1050484` / `1051132` KiB matching
README and stderr `Exit status: 0`.

Immediate parent `3cc0fc3b…` and V43 stdout `a53cc30d…` match
`V57_SOURCE.sha256` and the V57 import asserts.  First-pivot digest
`f6eeaf7a…` and P12 tail/multiplier digests match V43.  Every
`V57_SOURCE.sha256` entry is present in the tarball with matching
hash (33 files, 0 mismatches).

Import chain actually executed, in order:

1. V57 pins and imports the canonical P12/N13 parent (`3cc0fc3b…`) and
   scans pinned `V43_CANONICAL.stdout` (`a53cc30d…`).  Parent `main()`
   is not called.
2. That parent pins V34 (`1743dc29…`).  V34 `main()` is not called.
3. V34 pins dual (`cf3f3f02…`).  Dual defines `H`.
4. Dual pins trivariate (`1fb51264…`) and calls `tri.configure()`.
5. Trivariate pins two-center `replay.py` (`56df638a…`).
6. Two-center `exec_module`s `first_c1_c3_mpoly.py` with no hash pin.
   That file loads `transport_c1_c3_mpoly.py` with no hash pin.  Pencil
   pins adjoint (`fb138b0f…`) and loads `c1_rational_transport.py`,
   `fast_evec.py`, `fast_efield.py` with `expected=None`.

Those unpinned-at-import files **are** listed in `V57_SOURCE.sha256`.
Dual `tri.configure()` at import sets field/pivot flags; it does not
change V57’s later `CENTER = (C,V,U)` assignment.  No uncharged
mathematical parent is called for a different theorem.  The supplement
records this as archive-custody pinning, which is V1’s allowed
alternative to import-time SHA.

Packaging nits, recorded by the supplement and not algebraic:

- tarball member prefix `td6-aws-handoff-20260825-v55v56/` versus frozen
  file `td6-aws-handoff-20260825-v57.tar.gz`;
- extra V55/V56 shard files, `run_v55.sh` / `run_v56.sh`, V53 producer,
  and runbooks sit in the tar and are absent from `V57_SOURCE.sha256`;
  V57 does not import them;
- `__pycache__/replay.cpython-314.pyc` is in the tar, unlisted; AWS venv
  is the campaign 3.12 interpreter;
- r6d `start_utc` is `2026-08-25T10:54:37Z`; README says `10:54:38Z`
  (one second); end time matches;
- host IPs `100.26.198.153` / `98.80.65.144` do not appear in
  stdout/stderr.

Original `verify.py` is custody: hashes, `rc`, and `assert marker in
out`.  It never imports `replay.py` and never reconstructs a ledger
product.  Stored `PASS` strings remain non-authoritative under this
charge.

**7. [Confirmed] Strict refusal of divisor, whole-A3, transverse-modulus,
TD6, SP-2, landing, or JC2 inference from V57 alone.**

xmodel, README, producer terminal lines, `verify.py`, and the repair
overlay all keep:

- `raw_U_H_B3_strata_still_separate=true` / `raw_divisor_cover_complete=false`
- `full_A3_beta_family_killed=false`
- `whole_TD6_killed=false`
- `SP2_killed=false`
- `JC2_resolved=false`

Unused previous/current rows are explicitly not audited
(`full_unused_previous_current_row_audit_complete=false`; V55/V56 named
as an independent cross-check).  No transverse-modulus, landing, or
second-chart glue is proved.  The printed
`two_chart_glue_required_form=a*d1+b*d2=(U*H*B3)^N` is a banner with no
computation.  The supplement withdraws it as an unproved design banner.

`generic_open_localization_repaired=true` and
`composed_localized_source_identity_exact=true` are post-ledger banners.
The supported statement is the dependency-closed DAG plus V43 pin on
`D(U H B3)`, not a divisor cover.

**8. [Confirmed] The nonmutating supplement exactly repairs the V1
ancestry/flag/banner/ledger/custody findings without changing positive
identity bytes or broadening `D(U*H*B3)`.**

The repair directory contains none of the DAG, ledger, stdout, stderr,
archive, or producer files.  Original positive identity bytes still
match the freeze:

- archive `cc34d029fc30f469239ebb0d4c07eb33992c7de75fbd71242eed24bbbc2df310`
- DAG `a906b803…` / ledger `69c1086b…`
- r6d stdout `2bb3374c…` / Box03 stdout `24b9f9ba…`
- original `MANIFEST.sha256` `7d337a218b5436caad67ac2dc5b96349d2821262a7243c5750c82dc07903017b`
- original `FREEZE.sha256` `c42633c4eeed8bfbfd388ba9c97a3c6c9aa9fee656b71f3f3256efac8a96f911`
- producer report `b3d3438710d720442ee289060837d8bc531bd800cb31c4c937ee340b8cb481af`

V1 required repairs, discharged by overlay rather than mutation:

| V1 repair | overlay |
|---|---|
| stop treating the 14-key list as N13 ancestry; emit the singleton previous key | cache reclassified; singleton stated as unnamed original `X-1`; key not invented |
| rename singleton omission | read only as current-row omission |
| rename DAG `P12_minus_multiplier_times_N13_…` | live glue named as first-remainder identity; full original-row identity remains the V43 pin |
| move q/q-prime prints; print `k` unit | banners classified as non-evidence; live `configure_qd`; source assert `k*k.inverse()==1` |
| import-time SHA or document `V57_SOURCE.sha256` | source-manifest pinning stated |
| archive rename / drop unused members / pyc / timestamp | recorded as custody nits |
| label ledger as leaf-coefficient; V43 `H^3` as parent pin | stated |
| delete or compute `two_chart_glue_required_form` | withdrawn |

Scope is not broadened.  Repair strongest claim is incompatibility of
the original-source system on the principal open `D(U*H*B3)` in the
fixed source-typed A3 q2-beta section, with the same three raw strata
left separate.  The adapter log is byte-identical to
`xmodel/td6_v57_generic_hostile_review_20260825.log` and contains the
strings the repair `verify.py` requires, including
`CONFIRMED_WITH_REPAIRS`.  That `PASS` print of the repair checker is
not used as algebra.

Because the original package is immutable, leftover producer banners are
not remaining required repairs.  They are read through the overlay.

---

## Strongest exact claim that survives

On the **fixed source-typed A3 q2-beta section** with center `(C,V,U)`,
`q_beta = t + beta t^2 + t^{25}`, and live compiler derivative
`q_beta' = 1 + 2 beta t + 25 t^{24}`, after transport to 132 free
variables:

1. Current row `('X0', 13)` is the unique N13 left-null support.  Its
   staged value is `N13 = (k/25) beta`, with
   `k = 252 - 342 S + 144 S^2 - 36 S^3` a unit of the campaign residue
   field `E` (`k * k^{-1} = 1`).
2. The raw 132-variable current polynomial of that row reduces, by exact
   sparse division and original-row replay, through original first rows
   and **exactly one** original previous `X-1` row, to the scalar
   `-N13`.  Pole original rows are not N13 summands.  Quadratic source
   rows are retained; the linear packer is used only on reduced echelon
   and affine first-band rows.
3. Genuine `compile_current[12]` is the 2,893-term polynomial with V43
   base digest `8d5c3550…`.  Its first-pivot remainder has beta-degree-0
   part `-k/50`.  The scalar `M = (25/k) tail` satisfies
   `R - M * N13 = -k/50`.  The full original-row identity
   `first_source + M N13 = P12 + k/50` is the pinned V43 certificate,
   not a live V57 expansion.
4. Every V57 leaf-coefficient denominator factors through `U`,
   `H = C-3U^2`, and the printed `B3`.  V43’s termwise clear
   `(1/4) U B3 H^3` is a parent pin with the same radical.

This is an exact localized source identity on **`D(U H B3)` inside that
fixed section**.  It does not kill `U=0`, `H=0`, or `B3=0`; it is not a
whole-A3, transverse-modulus, TD6, SP-2, landing, or JC2 theorem.

---

## Remaining required repairs

None.

The V1 ancestry, flag, banner, ledger, and custody findings are
discharged by the nonmutating supplement.  No algebraic change to the
positive original-row identity, the residual `-k/50`, or the
`{U,H,B3}` radical is required.  No positive identity byte changed.
The strict `D(U*H*B3)` fixed-section scope is preserved.

Recommended, not required:

1. A future mutating producer may print `N13_previous_edge_keys` from
   the unique nonzero `previous_relation132` slot, move the q/q-prime
   banners after `configure_qd`, rename the DAG remainder flag, and
   drop the two-chart-glue line.  The overlay already supplies the
   correct reading.
2. Import-time SHA on `first_c1_c3_mpoly.py`, `transport_c1_c3_mpoly.py`,
   and the three pencil helpers would match the existing
   `V57_SOURCE.sha256` pin.
3. The frozen original `verify.py` still treats stdout `PASS` markers as
   a custody gate.  That script is not the theorem.

---

CONFIRMED
