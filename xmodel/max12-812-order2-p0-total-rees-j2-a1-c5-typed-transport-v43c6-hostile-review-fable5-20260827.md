# Hostile review: V43C6 C5 typed-transport obstruction

Date: 2026-08-27
Reviewer: Fable5 (Anthropic), independent hostile referee, desk-scale exact replay
Charged producer:

- `cases/max12_812_order2_p0_total_rees_j2_a1_c5_typed_transport_v43c6_20260827/`
  (`PREREGISTRATION.md` `96786472…`, `audit_c5_typed_transport_v43c6.py`
  `dc0c61a1…`, `RESULT.json` `30b4ec0b…`, `FREEZE.sha256`)
- `xmodel/max12-812-order2-p0-total-rees-j2-a1-c5-typed-transport-v43c6-sol-20260827.md`
  (`cee2a228…`, listed in the producer freeze)

**Overall: `PASS-C5-TYPED-TRANSPORT-AUDIT-OBSTRUCTION` is CONFIRMED at
exactly the charged scope.  All seven review items are CONFIRMED.  No bad
symbol, row, map, localizer, or quotient was found.**

Execution disclosure: this session had a shell.  I rehashed every charged
file, replayed the producer audit in `--check` mode (byte-identical result,
0.17 s), and ran my own independent desk-scale Python replays: alphabet and
census rebuilds, raw-byte and nested-key scans of the frozen V20R2 corpus,
and — decisively — execution of the frozen `generated_alias_map` function
extracted verbatim from the pinned V46 verifier at contact `(1,3,3)` with
the pinned A1D2_R3 maxima, diffed against the producer's 67-symbol map.
No Groebner, saturation, or heavy algebra was run or needed.

---

## Item 1 — hashes, freeze, census, 67-symbol extension map: CONFIRMED

Custody.  All four `FREEZE.sha256` lines verify (`shasum -c` OK), and all
20 pinned upstream artifacts hash to their charged values, including the C5
proof `f8426bcf…`, C5 result `215a64b2…`, C5 review `0ab2a7ef…`, the five
V20R2/V19 files, the V46/V46R1/V47/V47R1 schema and result files, and the
two D23_LOW_A6 endpoint files.  The producer audit replays byte-identically:
`RESULT_SHA256=30b4ec0b30013a9061a0d6c8587096ffde9af26ced4025562eb4f4b4f71911ff`.

Source census, recomputed independently (my own code, not the producer's):

- The 67-generator alphabet (66 positive `X19_total` symbols plus `t`)
  rebuilt from the preregistration's ring display equals
  `RESULT.json.source.generators` exactly.
- The 25 `final_multiplier_roots` names in the frozen C5 proof are exactly
  the 25 charged rows, and the 25 per-row SHA-256 values copied from the
  proof's `total_row_sha256` match `supported_rows_sha256` exactly.
  (The proof's `total_row_sha256` holds 70 slots; only the 25 final rows
  are charged, correctly.)
- Support census over all 950 `expression_nodes`: exactly 66 symbols =
  alphabet minus `ez9`, no strays.  `ez9` is the sole general-only positive
  variable, matching both the sol and the pinned C5 review's nit 4.
- C5 contract fields verified: status
  `PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2`, ambient
  `Q[t,X19_total], t maps to rho^2`, target literally
  `[{coefficient:[1,1], monomial:[["a1",628]]}]`, exponent 628,
  66/65 positive-variable counts, no source localization.

67-symbol extension map.  I extended the frozen alias rule (see Item 3) to
every family index in the alphabet and compared with
`complete_extension_variable_images`: **identical on all 67 entries**,
including `t -> rho^2`, the nine lower-ideal zeros, the factor-2 `Cz/Cc`
images, the factor-4 `Bc` images, `ell_i -> (1/2)*P_i`, and
`k,k1,k2c,k10_i -> k10_0,k10_1,k10_2,k10_i`.

## Item 2 — V20R2 lacks a serialized C5 ring / 25-row module map: CONFIRMED
(availability statement only)

Independent census of the three pinned V20R2 files:

- `SOURCE_COLUMNS.json`: 169 entries, 169 distinct variables; the
  fixed-zero boundaries are exactly five —
  `k6_0, k2_0, mu2_0, mu4_0, mu6_0` (`FIXED_ZERO_BEFORE_SOLVE`,
  columns 132/146/156/162/166) — leaving 164 `FREE`, matching
  `free_source_columns=164`.  The alphabet is `d0_1..d5_19`, load jets,
  target jets, `Jdet_0`: visibly disjoint from the C5 alphabet.
- `RESULT.json`: status
  `PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE`,
  140 literal equations, 169/164 columns; unit opens `k10_0`, `Jdet_0`
  present.
- DAG: target `Jdet`, truncation `Q[Lambda]/(Lambda^20)`, forbidden aliases
  `[J1,J2]`, normalized coordinates `C0..C6` with `C6=1`.

I went beyond the producer's top-level key check: a raw-byte grep of all
three files finds zero occurrences of the token `"a1"` and zero `Tg*_*`
tokens, and a recursive scan of every nested key at every depth finds no
`c5`/`ring_map`/`row_module`/`a1_image`-type key.  The only "C5" anywhere
is the normalized coordinate name `C5` in the coordinate map — a spelling
collision with the certificate label, which the producer explicitly
firewalls from being consumed as an alias.  The V19 historical control
verifies: `K10`, `K6`, `K2` all `NOT_TYPED_COMPOSABLE`.

The producer's wording is correctly modest: `SKIPPED_NO_LITERAL_C5_RING_OR_
ROW_MODULE_MAP` is an availability/interface statement.  Absence of a
serialized map is not a theorem that no map exists, and neither the sol nor
`RESULT.json` claims otherwise.

## Item 3 — A1D2_R3, the literal V46 contact map, `a1=Az_0`, image zero:
CONFIRMED

Endpoint selection.  The pinned V47 schema lists exactly four
`raised_subtail_manifests`: A1D2_R3 (`T_C2=16`), A2D3_R5 (20), A3D3_R5
(22), A4D3_R5 (24).  `T_C2=16` is the unique minimum — no tie-break is even
needed — so the preregistered "smallest reviewed V47 terminal grade" pick
is forced.  The A1D2_R3 manifest fields `(a,d,c,r_min;G,T_C2)=(1,2,3,3;14,16)`,
endpoint `D23_LOW_A6`, and its authority/review hashes all match the pins.

The map is frozen, not invented.  Three independent pinned sources agree:

1. `V46 SCHEMA.jet_reindexing_map` literally freezes the lower ideal
   (`az_i=ac_i=0 for i<a`, `ez_i=ec_i=0 for i<c`, `cs_i=rs_i=0 for i<r`)
   and the reindexing `az_i -> AzD1_(i-a)`, `ez_i -> 2*CzD1_(i-c)`,
   `rs_i -> 4*BcD1_(i-r)`, loads by identity on the series;
   `V46R1 SCHEMA_R1.coordinate_types.raw_to_D1` freezes the same six-family
   map with the same 1/1/2/2/1/4 factors.
2. The 2 and 4 factors also re-derive from the pinned V46 primitives alone:
   matching total `N1 = sigma^3*(P*Az+Ez)/2` against D1
   `N1 = sigma^3*(P*sigma^a*AzD1/2+sigma^c*CzD1)` forces
   `Ez = 2*sigma^c*CzD1`; matching `Rtot=(P^2+sigma^2*Q)/4` against
   `Kr=P^2/4+sigma^(r+2)*Bc` forces `Q = 4*sigma^r*Bc`.
3. `V47 GENERATED_MANIFESTS` gives the A1D2_R3 leading slice exactly as
   charged (`az_1 -> AzD1_0`, …, `ez_3 -> 2*CzD1_0`, `rs_3 -> 4*BcD1_0`),
   direction "total lower-contact quotient to shifted D1 relative leading
   jets".

`a1 = Az_0` is frozen.  The pinned V46 verifier
(`verify_uniform_naturality.py`, hash-verified) hard-codes the literal
low-index jet table
`Az: ["a1","aa1","aaa1"]`, `Ac: ["a0","aa0","aaa0"]`,
`Cz: ["c1","e1","ee1"]`, `Cc: ["c0","e0","ee0"]`,
`Bz: ["cs","cs1","cs2"]`, `Bc: ["rs","rs1","rs2"]`, then `az{i}` etc. for
`i>=3`, and `k,k1,k2c,k10_i` as the `k10_0..` jets.  So `a1` is the
stage-zero `Az` coefficient, and the names `a0, c1, c0, cs, rs` (the other
stage-zero slots) are exactly the ones absent from the C5 alphabet, as
expected from the upstream chart closures.  The verifier's own mutation
control asserts `a1 -> "0"` for any `a>=1`, and V47's
`chart.forbidden_stage_zero_names = [a0,a1,c0,c1,rs,cs]` plus V46's
collision warning ("D1 a1,a0,c1,c0 denote shifted leading jets, not total
stage-zero jets") freeze the ban on the alias `a1 -> AzD1_0`.

Decisive replay.  I extracted `generated_alias_map` verbatim from the
pinned verifier and executed it at `(a,c,r)=(1,3,3)` with the pinned
A1D2_R3 maxima `{p:2,A:2,C:2,R:0,k10:0,k6:0,k2:0}`:

- zero mismatches against the producer's 28 defined finite images (the
  `ell_i` spelling aside, see nit N2);
- the frozen in-window names intersected with the C5 alphabet, plus `t`,
  are exactly the producer's 28 DEFINED entries; the complement is exactly
  the 39 MISSING entries;
- `phi(a1) = "0"`, because `Az` index `0 < a = 1` falls in the frozen lower
  ideal.

Hence `phi(a1)=0` and `phi(a1^628)=0` exactly as charged.  The V47R1
record independently confirms `contact=[1,3,3]`, the maxima, and
`symbolic_variables_retained: 24` — the producer's 24-generator finite
manifest ring count.

## Item 4 — target nonzero, localizer `p*k0=(-2*rho^2)*k10_0` licensed,
zero not a unit: CONFIRMED

The receiver is the localized polynomial *coefficient* ring — the
24-generator finite manifest ring or the generous 63-generator complete
extension (I verified the 63-name list is exactly the finite 24 united with
every token of the complete images) — **not** the quotient by the endpoint
rows.  This matters: the D23_LOW_A6 theorem itself says the rows generate
the unit ideal in the localized `T`-jet, so that quotient is the zero ring,
where 0 *would* be a unit.  The producer's control "the target is not
silently replaced by the zero ring" guards exactly this trap, and the
argument is run in the polynomial domain, correctly.

Licensing of the localizer:

- `D(p*k0)` is the registered endpoint localization, frozen in
  `V47 SCHEMA.endpoint_authorities.D23_LOW_A6.localization` and in the
  pinned promotion ("in characteristic zero on `D(p*k0)` …"), whose
  excluded faces list `p=0`, `k0=0`.
- `p = P_0 = -2*rho^2`: the pinned V46R1 Hensel block freezes
  `lambda(sigma)^2 = -P(sigma)/2` with `lambda_0 = epsilon*rho`; at stage
  zero this is `rho^2 = -p0/2`, i.e. `p0 = -2*rho^2`, and V46 maps
  `p0 -> p`.  The V46 normative series `P = p0 + 2*sum ell_i sigma^i` also
  yields `P_i = 2*ell_i` for `i>=1`, licensing the `(1/2)*P_i` images.
- `k0 = k10_0`: the pinned endpoint review states "Inverted: `p` (via
  `lam`), `gamma=cv`, and the chart unit `k0` … `k0` is the registered D1
  chart even when `k10` is delayed out of the window" — the chart unit is
  the leading coefficient of the `k10` load, which in the frozen V46/V47R1
  D1 naming is `k10_0`.

Nonvanishing.  `(-2*rho^2)*k10_0` and `rho` (the separate V46R1 root-chart
localizer, frozen as `hensel.localization = "D(rho)"`) are nonzero elements
of the polynomial domain `Q[…]`.  The multiplicative set they generate
avoids 0, so the localization is a nonzero domain, `1 != 0`, and `0` is not
a unit.  This is elementary and airtight; no computation can perturb it.

## Item 5 — no extension to `S[a1^-1]`; the identity maps to a tautology:
CONFIRMED

By the universal property of localization, a ring map `phi: S -> T` extends
to `S[a1^-1] -> T` iff `phi(a1)` is a unit of `T`.  Here `phi(a1)=0` and
`T` is a nonzero domain, so no extension exists;
`source_D_a1_map_exists=false` is exact.  Note the C5 identity itself
needs no source localization (it is an ordinary-ring identity, per the
pinned review), so the correct and charged statement is the two-sided one
the producer makes: the forward map exists on `S` but sends the certificate
target to `0^628 = 0`; and any localized-source variant is barred outright.
Pushing the identity forward along the complete extension yields
`0 = sum_j phi(M_j) phi(Tg_j)`, which is automatically true for any ring
map and carries no Bezout/unit content in the receiver.  Under the finite
manifest map the identity cannot even be evaluated (39 images MISSING), and
the producer correctly refuses to evaluate it rather than zero-filling.

## Item 6 — row-module stage `NOT_REACHED`; 28/39 census exact: CONFIRMED

The preregistration fixes the gate order (rings; all 67 images;
localizations/extension; **unit image of `a1`**; row hashes + 25-row module
matrix; row replays) and mandates stopping at the first failed gate.  The
unit gate fails, so the row-module stage is correctly
`NOT_REACHED_AFTER_NONUNIT_A1_IMAGE`, and recording it otherwise would
require inventing images for unmapped rows — the exact `MISSING != 0`
violation the prereg forbids.  The 28-defined/39-missing census was
recomputed independently twice with agreement: (i) by family arithmetic
(defined: `t` + 9 lower-ideal zeros + 3+3+3+3 A/C jets + 1+1 R jets +
2 `ell` + `k` + `k6` = 28; missing: 5+5+4+4+4+4+6+6+1 = 39; 28+39=67), and
(ii) as the exact set difference against the frozen verifier's alias-map
window.  The three charged V47R1 literal slots `Phi1[14]`, `Phi2[14]`,
`Phi4[16]` verify against the pinned record (term counts `[2,2,2]`,
coefficient corpus `ad0c9b15…`); they are three stage-zero coefficient
formulas in `AzD1_0/AcD1_0/CzD1_0/CcD1_0/rho` and plainly not a 25-row
module map; no `row_module_map` key exists in the V47R1 schema.

## Item 7 — scope: CONFIRMED

The producer's firewall is correctly narrow and matches what was proved:
one endpoint-class obstruction (A1D2_R3 under the frozen forward V46 map)
plus a K00 interface-availability statement.  It is not nonexistence of
every possible receiver map (a different source invariant, chart
certificate, or a future constructed K00 chain map is explicitly left
open); it is not a refutation of C5 (the C5 identity remains confirmed at
its ordinary-ring scope, review `0ab2a7ef…`, which itself withheld exactly
this transport: "This does not prove a terminal-receiver chain map …
K00 transport remains separately untyped"); and it imports nothing to
`G2-PSC`, coverage, Gate T, order-two, maximum-twelve, or JC2.  One scope
remark: all four reviewed V47 manifests have `a>=1`, so the same
one-generator obstruction argument would run on each; but only A1D2_R3 was
preregistered and charged, and the producer rightly claims only it.

---

## First bad symbol / row / map / localizer / quotient

None found.  Every charged symbol image, the endpoint selection, the
localizer identity, and the census were reproduced exactly from frozen
sources.

## Nonblocking nits

- **N1 (control strength).**  Two of the seven controls are asserted
  booleans rather than computed checks: `v20_alias_is_not_map` is a literal
  `True`, and `zero_is_not_unit_in_nonzero_domain_localization` derives
  from a hard-coded `image_is_unit = False` whose guard can never fire.
  Both underlying facts were independently verified in this review (deep
  nested-key/byte scan of V20R2; the domain argument), so nothing rests on
  them, but their mutation surface inside the audit is zero.
- **N2 (p-jet spelling).**  The finite manifest ring spells the two
  retained p-jets `P_1,P_2`, while the pinned V46 alias map emits
  `ell1,ell2` (identity).  The identification `P_i = 2*ell_i` is frozen in
  the V46 normative `P` series and invertible over `Q`, so the rings are
  the same; but no pinned file prints the V47R1 generator strings
  themselves — only the maxima and the count (`symbolic_variables_retained:
  24`) are frozen, and both match the audit's 24-name ring.
- **N3 (`k0 = k10_0` is a reading, not a printed equation).**  No single
  pinned file prints `k0 = k10_0`; it is the unique consistent reading of
  the endpoint review's "chart unit `k0`" language together with the
  V46/V47R1 `k10_i` load naming.  Since any registered nonzero polynomial
  localizer yields the same nonzero-domain conclusion, this cannot flip the
  verdict.
- **N4 (`gamma` in the endpoint open).**  The endpoint review's
  scheme-theoretic paragraph works on `D(p*k0*gamma)` (also inverting
  `gamma=cv`) while the promotion headline states `D(p*k0)`.  Inverting
  additional nonzero elements of a domain keeps the localization a nonzero
  domain, so the producer's argument is insensitive to this difference.

## Narrow promotion wording

> **V43C6 (typed transport of C5): PASS-C5-TYPED-TRANSPORT-AUDIT-
> OBSTRUCTION, hostile-confirmed.**  (i) The frozen V20R2 corpus
> serializes no C5 ring map, no image of `a1`, and no 25-row module map;
> normalized K00 is therefore skipped as unavailable — an interface
> statement, not an impossibility theorem.  (ii) On the smallest reviewed
> V47 endpoint `A1D2_R3 = (a,d,c,r_min;G,T_C2) = (1,2,3,3;14,16)`
> (authority D23_LOW_A6), the frozen forward V46 contact map sends the C5
> source generator `a1 = Az_0` to `0` by the frozen lower-contact ideal
> (`0 < a = 1`).  The registered localized receiver — the polynomial
> coefficient ring on `D(p*k0)` with `p*k0 = (-2*rho^2)*k10_0`, together
> with V46R1's `D(rho)` — is a nonzero domain, so `0` is not a unit, no
> extension `S[a1^-1] -> T` exists, and the C5 identity pushes forward
> only to the tautology `0 = sum_j phi(M_j) phi(Tg_j)`.  The 25-row module
> stage is `NOT_REACHED`; the finite-manifest census is exactly 28 defined
> / 39 MISSING images.  This is one endpoint-class obstruction plus an
> unavailable K00 interface.  It does not refute C5, does not exclude a
> future receiver map or a constructed K00 chain map, and carries no
> `G2-PSC`, coverage, Gate T, order-two, maximum-twelve, or JC2 content.

FABLE5_CONFIRMED_C5_TYPED_TRANSPORT_OBSTRUCTION_V43C6
