# Hostile no-shell source review — TD6 raw `H=P3=0` quotient-field closure

Reviewer: hostile different-model review (Claude), 2026-08-25.
Charge: `xmodel/td6-c1-c2-c3-p3-raw-curve-review-claude-20260825-prompt.md`,
extended by the readable source-custody supplement
`cases/td6_c1_c2_c3_p3_raw_curve_source_snapshot_20260825/`.

## Execution-gap disclosure

This session has no Bash, no shell, no web, and no local computation.
Consequences, disclosed up front:

- **No SHA-256 was recomputed.**  Every hash statement below is a
  string-equality check between frozen attestations (charged prompt values,
  `MANIFEST.sha256`, `FREEZE.sha256`, `DEPENDENCIES.sha256`,
  `payload/SOURCE.sha256`, lane `.meta` files, READMEs), not a re-hash of
  bytes.  If the supplement's payload bytes and its manifest were *jointly*
  doctored to tell one consistent false story, textual cross-checking cannot
  detect it; the freeze system and any shell-capable re-audit cover that.
- **No archive was extracted.**  The V17 archive
  (`b207bbba…`) and the V14 checkpoint archive (`d37407c8…`) are unreadable
  here.  Byte-identity of the readable supplement payload to the executed V17
  payload rests on: the on-host `sha256sum -c SOURCE.sha256` passes frozen in
  both lanes (`source-check.stdout`, identical hash in both, empty stderr),
  the lane metas' `source_manifest_sha256=7b00ab87…` matching the supplement's
  pinned `payload/SOURCE.sha256`, and the supplement `MANIFEST.sha256`
  agreeing entry-for-entry with `SOURCE.sha256` (verified line by line; 24
  payload files, no extras, no hidden files by glob).
- **Nothing was rerun.**  Verdicts rest on hand algebra plus the frozen
  program and outputs, per the campaign's AWS-only replay policy.

## Custody verification (string-level)

All charged hashes are mutually consistent across the two packages:

- AWS package: `FREEZE.sha256` lists the charged manifest `95869889…` and
  report `a15c85c5…`; `MANIFEST.sha256` lists the charged dependency pin
  `6d366b00…`, archive `b207bbba…`, ascending stdout `c38471a0…`, reverse
  stdout `900c3829…`; the `e3b0c442…` entries are the empty-input SHA-256,
  matching the claimed empty supervisor/source-check stderr.
- Supplement: `FREEZE` lists the charged manifest `8e581d57…`; `MANIFEST`
  lists the charged README `9e81509b…`, dependencies `6cacc319…`,
  `payload/SOURCE.sha256` `7b00ab87…`, and the charged P3 producer
  `1b492ad2…` at the executed path.  Its `DEPENDENCIES` pins the theorem
  package's freeze `ddbf7dff…` (the charged freeze), manifest, archive, and
  report — bidirectional pinning is closed.
- Lane metas record the charged archive, source-manifest, and producer hashes
  on-host before execution, rc=0, and stdout hashes equal to the manifest
  entries; both lanes ran the same UTC start on distinct hosts
  (`ip-172-30-0-45`, `ip-172-30-0-186`), Python 3.12.3, python-flint 0.9.0,
  and the reverse meta alone carries `--reverse-first`.
- `DEPENDENCIES.sha256` pins the checkpoint MANIFEST/FREEZE, the V14 archive,
  `origin.stdout` `c31a0f60…` (equal to the charged prior-origin stdout and
  to the checkpoint MANIFEST's entry), `origin.meta` `ec33aa59…`, and the
  erratum.

## Import closure (read in full)

`c1_c2_c3_p3_quotient.py` (charged producer) pins `c1_c2_c3_trivariate.py`
(`3459dda5…`), which pins the two-center `replay.py` (`56df638a…`).  From
there: `replay.py` → `first_c1_c3_mpoly.py` → `transport_c1_c3_mpoly.py` →
{`c1_rational_transport.py` → pins `td6_two_chart_first_band/replay.py`
`c55e2136…`} and {`c1_pencil.py` → pins `td6_jet_orbit_adjoint/replay.py`
`fb138b0f…` → pins `td6_boundary_q2_deformation/replay.py` `0ba18447…` (→
pins `td6_two_chart_next_row/replay.py` `0fc299a1…`, which pins the first-band
replay again) and `td6_moduli_uniform_third_band/replay.py` `7a21f949…` (→
pins `td6_moduli_uniformity/replay.py` `55340fa6…`)}, plus `fast_evec.py`,
`fast_efield.py`.  The hops `replay→first_c1_c3_mpoly→transport→
{c1_rational_transport, c1_pencil}→{fast_evec, fast_efield}` are loaded
**without** per-import hash pins; custody for those five edges rests entirely
on the on-host `SOURCE.sha256` check, which the frozen source-check output
shows passing for all 24 files.  The three remaining payload files
(`h_b_raw_quotient.py`, eps2 `replay.py`, `c1_c3_thickening.py`) are
standalone producers for other runbook lanes and are not imported by the P3
chain.  `c1_rational_transport` is instantiated more than once under
different module names; I traced that every center-dependent call in the P3
path (`build_transport`, `x_chart_coefficient`, `_X_POWER_CACHE`) goes
through the single instance `r.fb` whose `CENTER` is set and whose cache is
cleared, and that `configure()` rebinds `Rat2`, `factor`, `FIELD`, `EField`,
`E2`, `REVERSE_PIVOTS`, `Dual`, `Q_PRIME` on exactly the module objects the
executed code paths read.

## Attack 1 — source typing and specialization

The producer sets `CENTER=(3U², V, U)` as genuine curve elements — the true
`H=C−3U²=0` section with `V` kept as an honest coordinate (contrast the
two-center lane's normalized `(C, 1, U)`); `weighted_scaling_used=false` is
accurate.  `x_power_expansion` builds `(c1 s+c2 s²+c3 s³+t s⁴)^i` by exact
multinomials — every x-side entry is a **polynomial** in `(3U², V, U)`; F1/F0
rows have integer/binomial entries with the fixed rational patterns
(`TAYLOR_L=3` and both pole scales are center-independent constants).  The
affine transport rhs comes from `qd.source_rhs(key).value` — the licensed
E-valued source at `B=0` (`R3/R5`, pole patterns, X-boundaries `{15:1}`,
`{1:1,25:1}`), matching the parents.  Rectangles `(15,60)/(25,100)`,
`pack('X-2')`, `Q_PRIME={0:1,24:25}`, `p'=15t¹⁴` (the `−45·g3` term), and
`P12 = compile_x_current(...)[12]` are parameter-identical to the frozen
trivariate/two-center parents.  The first rows and P12 are transport-restricted
objects; the certificate replays the P12 identity against those **original
transported first rows** (exactly the report's wording), and the transport
restriction itself is licensed on `D(U)` by Attack 4.

## Attack 2 — function-field fidelity

Hand-verified: `Z²−32Z+128` has discriminant `512`, not a rational square, and
constants' squares in `Q(U)` are constant squares, so the quadratic is
irreducible over `Q(U)` and `Quad ≅ Q(√2)(U)` (`Z=16±8√2`).  `v_U(ZU³)=3` is
odd and `v_U` is a valuation on `Q(√2)(U)`, so `ZU³` is a nonsquare and
`Curve = Quad[V]/(V²−ZU³)` is a field of degree 4 over `Q(U)`.  `V` satisfies
`P3` in the tower (asserted in-run, with the `+1` negative control), `[Q(U)(V):Q(U)]=4`
forces the monic quartic `P3` to be its minimal polynomial, hence `P3` is
irreducible over `Q(U)` and (Gauss, content 1) in `Q[U,V]`; the tower **is**
`Frac(Q[U,V]/(P3))` — a field, no lost component, no nilpotents, no scaling.
Implementation audited: `Quad` multiplication/norm/inverse implement
`Z²=32Z−128`, `N=a²+32ab+128b²`, inverse `(a+32b−bZ)/N`; `Curve` implements
`V²=ZU³`, `N=a²−b²ZU³`; both `inverse()` methods carry in-path
`assert self*result == 1`, as do `ECurve` and the `fast_efield`
`KField`/`EField` inversions (extended-gcd plus product assert).  The frozen
counters read `RatU=Quad=Curve=7589` in **both** lanes: every inversion in the
run was a `Curve` inversion (product-asserted) consuming exactly one `Quad`
norm inversion (product-asserted) consuming exactly one `RatU` swap — no
inversion executed outside the checked chain, which answers the 7,589-inversion
question affirmatively.  The coefficient system `E=K[A]/(A³−α)`,
`K=Q[S]/(F)`, is an honest degree-18 number field: `F` is certified
irreducible by Rabin mod 31 in the pinned parent, and `α` is a non-cube by the
frozen norm computation `N(α)=3²⁸/5⁹⁶` with `28 ∤ 3`.

## Attack 3 — compatibility certificate

Both frozen stdouts assert-and-print `transport_rank=3470/3602` with zero
affine compatibility and `first_rank=38/132` with zero incompatibility;
`raw_terms=2885` with **identical** P12 digest `3b790868…` across the two
hosts (independent replication of the compile), identical remainder and
expected digests, `remainder_is_expected_constant=true`, and an in-run
inverse check of `−k/50`.  `k=252−342S+144S²−36S³` has degree 3 < 6 in the
generator of the degree-6 field `K`, so `k≠0` unconditionally — the remainder
is a nonzero constant of `E`, and a nonzero element of `E⊗_Q κ` stays nonzero
for every field `κ ⊇ Q`, which is what the pointwise contradiction needs (the
run's unit check is stronger than required).  The ascending lift uses 28
rows/1,540 terms, the reverse 38 rows/2,152 terms — genuinely different
certificates of the same identity, each verified by `source_replay` against
the original first rows with the `+1` negative control (which also defeats a
degenerate-equality failure mode in `clean`).  Honest limitation: the
`--reverse-first` flag flips only the first-band pivot chooser (`max` vs
`min`) and the division order; the **transport elimination is byte-identical
in both lanes**, so lane independence covers the lift stage only.  This is
acceptable because the transport stage is not certified by cross-lane
agreement but by the chart audit plus polynomial source entries (Attack 4),
and the final identity is certificate-replayed, not trusted from elimination.
The stdouts contain counts and digests, not the full multiplier coefficients;
independent re-verification of the lift coefficients requires AWS replay of
the pinned producer, consistent with campaign policy.

## Attack 4 — localization and clearing

The decisive structural fact, verified at source: **all original rows are
polynomial** (multinomial coefficients times monomials in `3U², V, U`;
integer F1/F0 entries; rational pattern rhs; E-constant affine rhs), so
denominators can enter only through pivot inversions.  Exactly two
nonconstant pivot norms occur (both lanes, rows 4804/5282, pivots 194/1185):
`128U⁶` and `16U⁴`, denominators 1 — and these are precisely the absolute
norms of the h-zero certificate's leads `−V` and `2U` at the same rows/pivots
(`N(−V)=N_q(−ZU³)=128U⁶`, `N(2U)=N_q(4U²)=16U⁴`), a hand-checked
cross-package consistency.  Conjugation (`Z↦32−Z`, `V↦−V`) is integral on the
component basis and every norm is `c·U^m`, so by induction every echelon
quantity has pure `U`-power denominators in the `{1,Z,V,ZV}` basis; since
`Z=V²/U³` is regular on `D(U)`, the entire elimination lives in
`(Q[U,V]/(P3))[1/U] ⊗ E`, every pivot lead is a unit there (its norm `c·U^m`
is), and the transport substitution is therefore valid at **every** point of
`D(U)`, not only generically.  The audited LCMs — raw `U²`, first `U²`,
relation `U⁵`/`U⁷`, termwise `U⁷`/`U⁹` — cover every coefficient of every
object in the final identity (all 72 `RatU` components per scalar), the
termwise product check clears all 31,976/60,121 slots, and the certificate
charts factor as claimed and are arithmetically consistent:
`U¹⁷=U⁶·U²·U²·U⁷` and `U¹⁹=U⁶·U²·U²·U⁹`.  Multiplying the identity by the
termwise denominator gives an identity over `(Q[U,V]/(P3))[1/U] ⊗ E`;
specializing at any solution point of `D(U)` yields `0 = −k/50 ≠ 0`.  The
`D(U)` claim is fully licensed.  Robustness note (not a gap in this
evidence): `only_U_exception` and `P3_intersection_U_zero_is_origin` are
*printed*, not *asserted* — the PASS marker alone would not have failed on a
non-`U` chart factor; the frozen stdouts show `true`, and the report
correctly consumes the printed chart rather than the marker.

## Attack 5 — raw complement at `U=0`

Set-theoretically, on `H=P3=0`: `U=0 ⇒ P3=V⁴ ⇒ V=0`, and `H ⇒ C=3U²=0` — the
raw center origin, exactly as claimed (the claim is explicitly
set-theoretic; the scheme structure `V⁴=0` is irrelevant to it).  The
separately frozen origin certificate (`origin.stdout`, `c31a0f60…`, pinned in
both the checkpoint MANIFEST and this package's DEPENDENCIES) is a
transport-level incompatibility with **unit chart**: a 21-row `±1` integer
combination of original rows with constant nonzero residual and a `+1`
negative control.  I hand-verified its combinatorial core from the frozen
`fb` source: at center `(0,0,0)`, `x=t·s⁴`, so each `('g','X',−k,k+1)` row is
the single unit entry at variable `(k+1,5k+4)`, while `('g','F0',−5,0)` has
unit entries exactly at `{(i,5i−1): i=1..20}` — the printed combination
(20 X-rows minus the F0 row) cancels the matrix identically, and the residual
is `1−(5/9)L⁵A²`, visibly nonzero (rational coordinate 1; `A²`-block in
coordinates 12–16, matching the printed vector).  The V14 **B3-local**
erratum does not touch this: it demotes only the b-local lane's remainder
claim (a 1,681-term degree-2 remainder wrongly described as `−k/50`) and
explicitly leaves the raw `U=0`, `V=0`, `H=0` opens and the origin lift
unaffected; the origin lane is a different stdout, different producer
invocation (`--stratum=origin`), and its content is of a different, stronger
kind (constant integer certificate, unit chart).  Residual gap, disclosed:
the V14 origin producer's bytes (`ca6afb3d…` in `origin.meta`) live inside
the pinned V14 archive and cannot be read here; the hand verification above,
plus the printed exact certificate and the current trivariate producer's
matching fail-closed emission path, is the compensating evidence.

## Attack 6 — composition and scope

Hand-verified: `B3(3U²,V,U) = 36U⁶−12U³V²+72U⁶+V⁴−20V²U³+20U⁶ = P3` — the P3
curve is exactly the still-open `B3` divisor restricted to `H=0`, which is
why it was the last raw curve there; the whole-`H=0` claim is compatible with
generic `B3=0` remaining open off `H=0`.  The union over the fixed
source-typed section:

- `H=0` generic: V11 h-zero certificate, chart factored in the frozen stdout
  as exactly `U⁶·V⁵·P3¹` (and its relation denominator is `V·U²·P3`, which is
  precisely why that identity dies on the curve and a raw rebuild was
  required);
- `U=H=0`: V12, first-band inconsistent, constant residual, unit gcd, chart
  `V³`; its `V=0` endpoint is the origin;
- `V=H=0`: V15, P12 `→ −k/50` (same remainder digest as h-zero), chart `U¹²`;
  its `U=0` endpoint is the origin;
- `P3=H=0`: this package on `D(U)` (charts `U¹⁷`/`U¹⁹`), plus the origin at
  `U=0`;
- origin: V14 unit-chart transport incompatibility.

Every chart factor is consumed by another listed certificate; the
set-theoretic cover of the fixed-section `H=0` divisor closes, so the
"final producer-exact `H=0` debt" claim is correct at its stated scope.  The
producer prints `P3_whole_curve_killed=false` (the whole-curve statement is
correctly made only cross-package in the README/report), and all
neighborhood/full-centering/boundary/dead-stretch/SP-2/maximum-degree/JC2
denials are present and accurate.

## Smallest error or missing hypothesis

No false identity, missing stratum, or missing mathematical hypothesis was
found.  The smallest genuine defects are evidentiary, not mathematical, in
descending order of importance: (1) this reviewer could not recompute any
hash or open either pinned archive, so byte-custody rests on the frozen
cross-attestations rather than independent hashing (inherent to the no-shell
charge); (2) the two lanes share one transport elimination, so pivot-order
independence covers only the first-band/lift stage — the transport instead
rests on the chart audit, which is sound; (3) `only_U_exception` is printed
rather than asserted, so the PASS marker alone under-specifies the theorem
and consumers must (and here do) read the printed chart.

## Promotable sentence

At the fixed source-typed three-center TD6 section, the set-theoretic raw
curve `H=C−3U²=0, P3=V⁴−32V²U³+128U⁶=0` is producer-exactly empty — on
`D(U)` because two frozen AWS pivot orders over the degree-four function
field `Q(U)[Z,V]/(Z²−32Z+128, V²−ZU³)` of the irreducible `P3` reduce the
genuine 2,885-term P12 through the original transported first rows to the
nonzero constant `−k/50` with every certificate divisor a power of `U`, and
at its single `U=0` point, the raw center origin, by the separately frozen
unit-chart 21-row V14 origin transport incompatibility that the B3-local
erratum does not touch — so, combined with the frozen h-zero
(chart `U⁶V⁵P3`), `U=H=0` (chart `V³`), and `V=H=0` (chart `U¹²`)
certificates, the fixed-section `H=0` divisor carries no remaining
producer-exact raw debt; this licenses no neighborhood, full-centering,
boundary/dead-stretch, generic-`B3`, whole-TD6, SP-2, maximum-degree, or JC2
statement.

## Verdict

CONFIRMED
