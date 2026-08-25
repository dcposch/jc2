# Hostile review: TD6 `(c1,c2,c3)=(C,1,U)` fixed two-center open-cover kill

| Field | Value |
|---|---|
| Reviewer | claude (different-model hostile reviewer) |
| Date | 2026-08-25 |
| Report under review | `xmodel/td6-c1-c3-two-center-cover-gate-20260824.md` |
| Case under review | `cases/td6_c1_c3_two_center_cover_20260824/` |
| Parents read for source typing | `td6_two_chart_first_band` (fb/CENTER), `td6_two_chart_next_row`, `td6_boundary_q2_deformation`, `td6_jet_orbit_adjoint` (source rows, first band, E-duals), `td6_moduli_uniform_third_band` (K, E, field certificates), `td6_c1_c3_first_ideal_eps2` and `_dual` (`c1_pencil.py`, thickening), plus the `(C,1,1)` line-kill and first-ideal-dual gate records for the `-k/50` lineage |
| Overall verdict | **CONFIRMED** (no false identity, no missing stratum, no missing hypothesis found; every hand-checkable printed identity re-derived and correct; execution-side conditions in sections 2 and 11, none charged to the artifact) |

Every file in the case directory except the four binary archives was read in
full, together with the charged report and the frozen parent chain.  No PASS
string was accepted without either hand re-derivation of the printed data or
an explicit disclosure below.  No repository byte was modified other than the
creation of this file.

## 1. Charged hashes and read-only cross-pin audit

All eight charged hashes are internally consistent across every frozen record
that states them: the charged report hash equals `FREEZE.sha256` line 2; the
charged top-manifest hash equals `FREEZE.sha256` line 1; the six charged
stdout hashes equal, simultaneously, the `MANIFEST.sha256` entries, the
`stdout_sha256` fields of the corresponding `.meta`/`launch.meta` files, and
the hash lists in the report and README.  The four archive hashes agree
between `MANIFEST.sha256`, the README, and the `archive_sha256` fields of all
four `launch.meta` files.  Every successful lane's `stderr_sha256` is
`e3b0c442…`, which is the SHA-256 of the empty byte string (a known
constant), so the empty-stderr claim is exact; the V6 stderr hash
`4b253d4f…` is pinned in `MANIFEST.sha256` and the README, and the frozen
traceback content matches the claimed intentional assertion
(`replay.py:724`, `assert common.degree() == 0 and common[0]`).
`MANIFEST.sha256` covers exactly the 32 non-manifest files present — nothing
in the directory is unpinned except the self-referential pair
`MANIFEST.sha256`/`FREEZE.sha256`, the first of which `FREEZE.sha256` pins.

## 2. Execution disclosure (reviewer-side, mandatory)

This review session has no shell: no Bash tool and no local computation.
Consequently (i) **no hash above was recomputed** — all matching is by
reading frozen text against frozen text; (ii) the four tar.gz archives could
not be extracted, so the theorem-producing programs themselves — the V4/V5/V6
`replay.py`, `h_b_raw_quotient.py`, and the archive-only
`first_c1_c3_mpoly.py`, `transport_c1_c3_mpoly.py`, and in-archive
`c1_pencil.py` — were **not read**; their hashes are pinned (V5/V6/V7
producer hashes in the frozen `launch.meta`s; V4's only inside its
hash-pinned archive).  What was read instead: all six lane stdouts, all
metadata, both `source_verify` outputs, and the complete repo parent chain
(`two_chart_first_band` → `next_row` → `q2_deformation` → `jet_orbit_adjoint`
→ `moduli_uniform_third_band`, plus the eps2/dual `c1_pencil.py` and
`c1_c3_thickening.py`), which is import-hash-pinned end to end
(`fb138b0f…`, `0ba18447…`, `7a21f949…`, `0fc299a1…`) and whose git status is
clean.  Every algebraic identity printed in the stdouts was re-derived by
hand (section 4–7).  An independent probe is staged at
`/tmp/td6_two_center_cover_probe_claude.py`; it recomputes all 40+ byte
hashes, extracts the archives, verifies each `SOURCE.sha256`, pins the
producers against the recorded hashes, byte-compares archived parents against
the repo copies, and re-derives every identity below with a from-scratch
polynomial engine.  The verdict rests on the hand algebra, the frozen
attestations, and the cross-pinned custody lattice, with section 11 naming
what only a shell-bearing session can close.

## 3. Charge 1 — source typing, `c2=1`, and the original rows

**What the three coefficients are.**  Read directly from the frozen root
module (`td6_two_chart_first_band_20260824/replay.py`,
`x_power_expansion`): `(c1,c2,c3)` are the first three coefficients of the
centering jet `x = c1*s + c2*s^2 + c3*s^3 + t*s^4`, shared by every f/g term
and both x-side branches, with the quartic tail `t` remaining a tracked
system unknown (columns are indexed by `t`-degree).  The frozen base line is
`(C,1,1)` (read in `c1_pencil.py` and the eps2 thickening docstring); the
charged case sets the section `(C,1,U)` with `C,U` independent
transcendentals — the stdouts' `center_stratum=C,U independent` — and the
transport/first ranks `3470/3602`, `38/132` match the read `(C,1,1)` parents
exactly, confirming the same frozen rhs normalization (f-side `{15:1}`,
g-side `{1:1, 25:1}`, i.e. the boundary modulus at its frozen value) and pole
data.

**`c2=1` is a genuine restriction, not a proved gauge.**  Nothing in the
read parents implements or claims an `s`-rescaling equivalence.  The natural
weighted rescale `(c1,c2,c3,t) → (λc1, λ²c2, λ³c3, λ⁴t)` would need `√c2`
and an unproven equivariance of the F1/pole patterns and rhs normalizations;
the `c2=0` locus is untouched by any such argument.  The artifact never uses
or asserts the gauge: report, README, and the per-lane stdout flags
(`family_killed=false`, `SP2_killed=false`, `JC2_resolved=false`) all confine
the claim to the fixed normalized section.  The successor paragraph even
flags the gauge question as open.  Correctly scoped.

**Original rows.**  The first band is the packed list of nonzero rows of the
40-degree compile `Σ_i Q'[d−i]·f1[i] − 15·g1[d−14]` over the 132-dimensional
transport kernel (read in `jet_orbit_adjoint.first_band_polynomials` and
`pack`); "original" means these compiled rows, prior to any echelon.  The
count 28 is the certificate support — "nonzero original first rows in the
source lift", exactly as the first-ideal-dual gate tabulates for the same
machinery (28 rows / 1489 slots on the `(C,1,1+ε)` line, identical to this
case's generic lane).  The V5 incompatibility is the strongest possible
original-row form: support `{row 13}` with coefficient exactly `1` — the
original row `('X-2',14)` itself has empty parameter side and nonzero
constant side — and `first_incompatibility_original_row_replay=true`;
V6/V7 print `source_relation_original_row_replay=true`; the V4 lanes print
the corresponding `first/source replay PASS`.  The row-index/key offset
(index 13, degree 14) is consistent with exactly one empty lower-degree row
under `pack`.  No compiled row enters any certificate except through this
28-row original support.

## 4. Charge 2 — the generic/B-local cover of `UH != 0`

All printed denominators were expanded by hand and match monomial-for-
monomial:

- generic relation `(1/4)·B·U²·H²` — all 11 printed monomials exact;
- generic termwise `(1/4)·B·U³·H³` — all 15 printed monomials exact;
- B-local relation `(1/4)·U²·T` and termwise `(1/4)·U³·H·T` — exact;
- `B` and `T` are genuinely distinct: `T − B = 4U³(CU + U³ − 1)`.

Resultant, derived by hand: `Res_C(B,T) = lc·Res_C(B, T−B) =
4U²·(4U³)²·U²·B((1−U³)/U)` with `B((1−U³)/U) = 1` (the `U⁶` and `U³`
buckets cancel exactly), giving `64U^10` — as printed.  At any point with
`u ≠ 0` both leading `C`-coefficients are `4u² ≠ 0`, so specialization
commutes with the resultant and `B, T` have no common zero off `U=0`;
`B(C,0)=1` (hand-checked, decorative here since `U=0` is excluded anyway).
Hence every point with `UH ≠ 0` lies in the generic chart (`B ≠ 0`) or the
B-local chart (`T ≠ 0`).  The printed cross-checks
`Res_C(B,(1/4)U²T)=4U^14` and `Res_C(B,(1/4)U³HT)=4U^16·P` also reproduce by
hand (`Res_C(B,H)=B(3U²,U)=P`), confirming that the only points of `{B=0}`
outside the B-local chart are exactly the `H=P=0` fibre handled by V7.

**No lost component.**  Soundness does not depend on how the echelon found
the relation: the frozen flags
`cleared_relation_coefficients_polynomial=true` /
`termwise_polynomial_clear_checks=true` assert a denominator-cleared,
coefficientwise polynomial identity `D·P12 = D·(−k/50) + Σ M_i·L_i` against
the original rows — the read parents (`primitive_cleared_relation`,
`replay_polynomial_relation` in `c1_pencil.py`) implement exactly this
pattern.  Such an identity specializes to every point of every extension
field; the only excluded loci are the zero sets of the printed conservative
termwise denominators, `UHB` and `UHT`, and both transport/first charts
(`U·H`, printed) divide them.  Saturation is never used; fraction-field
inversion can lose only the printed loci; no chart factor is treated as a
unit anywhere it can vanish.

## 5. Charge 3 — the complete `U=0` divisor

Over `Q(C)` at `U=0` the rebuilt transport has two exceptional pivots, both
with numerator `−C` (chart `C²`, matching `detdeg=2` at `events=2`), the
first-band compile adds source denominator `C`, and the conservative
certificate chart is `C³` — precisely the README's claim.  The
incompatibility is `0 = r` with `r` the residual whose 18 printed
coordinates are rational constants (leading block `−9 + 3S`, an `A²` block
with five nonzero coordinates): a nonzero element of the degree-18 field `E`
(read: `E = K[A]/(A³−ALPHA)` over `K = Q[S]/(F)`), hence a unit — and
constant in `C`, so the kill holds at every `C ≠ 0`.  At `(C,U)=(0,0)` the
intersection lane rebuilds raw: zero transport events, every printed
denominator `(1)`, chart `1`, `whole_stratum_empty=true`, and the residual
coordinates are byte-identical to the `Q(C)` lane — consistent, since the
residual is constant.  Union: `{U=0, C≠0} ∪ {(0,0)}` is the whole divisor,
dead before P12 (`P12_compile_skipped_first_band_empty=true`).  No excluded
point, no source mismatch (same row 13, same key, same certificate shape,
same residual hash `97c09c59…` in both lanes).

## 6. Charge 4 — the complete `H=0` divisor

The h-zero lane substitutes `C = 3U²` over `Q(U)` and prints transport/first
chart `U`, relation denominator `(1/128)·U²·P`, termwise `(1/128)·U³·P` —
both hand-verified, with `P = B(3U²,U) = 128U⁶ − 32U³ + 1` hand-verified.
So the raw certificate kills `H=0` off `U·P = 0`.  The `U=0` root of the
divisor is the single point `(0,0)` (since `H=U=0 ⇒ C=0`), already rebuilt
raw by the intersection lane — the overlap is exact, with no gap and no
double standard between the two arguments.

The residual fibre `H=P=0`: **`P` is irreducible over `Q`** — the V7 print
(`H_B_modulus_irreducible_squarefree=true` with the flint factorization) is
independently confirmed by hand: `y = x³` gives `128y² − 32y + 1` with
discriminant `512` non-square, roots `(2±√2)/16`, and
`N_{Q(√2)/Q}((2+√2)/16) = 1/128 = 2^{−7}` with `−7 ∤ 3`, so the root is not
a cube in `Q(√2)` and `[Q(α):Q] = 6`.  Squarefree follows.  Hence
`Q[U]/(P)` is a field and the one Galois orbit of six fibre points dies all
at once.  `H_B_u_inverse = −128x⁵ + 32x²` is exact:
`x·(−128x⁵+32x²) = 1 − P ≡ 1`.

**`-k/50` is a unit in the actual base extension.**  From the frozen
line-kill lineage, `k = 252 − 342S + 144S² − 36S³`, a nonzero coordinate
vector in `K = Q[S]/(F)` with `F = (24S⁶−252S⁵+1170S⁴−3045S³+4680S²
−4032S+1411)/24`.  I audited the parent's Rabin certificate
(`certify_irreducible_mod_31`) line by line — it is a correct degree-6
irreducibility test (gcd of `x^{31²}−x` and `x^{31³}−x` with `F` trivial,
`x^{31⁶} ≡ x`) — so `K` is a field and `−k/50 ∈ K^×`.  I also re-derived the
parent's `E`-field certificate by hand: `3H³=1` gives `Norm_K(H)=3^{−2}`,
so `Norm_K(ALPHA) = 9⁶/(25⁶·3^{−2})⁸ = 3^{28}/5^{96}` — exactly the frozen
assertion — and `28 ∤ 3` makes `ALPHA` a non-cube, `A³−ALPHA` irreducible,
`E` a field.  In `E ⊗_Q Q[U]/(P)` (étale in characteristic 0), any unit of
`E` embeds diagonally with its inverse, so `−k/50` remains a unit there and
after every further scalar extension.  V7 additionally *exhibits* the
inverse (`remainder_inverse_sha256`, `remainder_is_constant_unit=true`) and
asserts `remainder_is_expected_constant=true` with `remainder_terms=1`,
`remainder_degree=0`.

**The 7,590 inverse checks.**  The stdout pins only the count
(`KP_inverse_count=7590`) — plausible for 3470 transport plus 38 first
pivots with propagation-side inversions — and the claim that each check
certifies the inversion *used* rests on the archived
`h_b_raw_quotient.py`.  Three mitigations, none a substitute for reading it:
every readable ancestor in this codebase implements inversion as
extended-gcd-with-unit-assert *at the point of use* (`K.inverse`,
`E.inverse`, `Frac.inverse`); the run is `rc_inferred=0` with empty stderr,
so no assert fired; and the identical machinery at `(C,1,1)` was
independently re-executed and CONFIRMED by a different-model reviewer with
local recomputation.  This is the single heaviest residual condition
(section 11).

## 7. Charge 5 — V6 genuinely fails, V7 genuinely repairs

V6's own printed data invalidate it: relation denominator `(1/128)·U³·P` and
termwise `(1/128)·U⁴·P` (both hand-verified expansions) contain the modulus
`P`, the producer computes `H_B_relation_denominator_gcd = (1/128)P` and
aborts on its intentional unit assertion — the frozen traceback matches.  A
certificate with `P` in its denominator says nothing on `P=0`; retaining V6
as a negative control and *not* as a proof step is the correct logic, and it
is what makes V7 necessary rather than cosmetic.

V7 does not cancel `P` under a new name: it works in `Q[U]/(P)`, where `P`
is literally zero and cannot be divided by; it rebuilds transport
(`3470/3602`), first band (`38/132`, zero incompatibilities — so on this
fibre the first band is consistent and the P12 obstruction is genuinely
needed), and the raw P12 from source (`H_B_raw_quotient_source=true`),
with certified inversions, a genuine-P12 check, the 2,885-term count exactly
matching the `H=0` specialization, the 28-row/1,540-slot original-row lift,
and a `plus_one` perturbation negative control on the relation replay.  The
reduction lands on the same constant `−k/50` as every other lane (identical
remainder hash `93121eef…` across generic/B-local/h-zero/V6/V7), which is a
unit by section 6.  The fibre is empty.

## 8. Charge 6 — custody, exhaustiveness, and logical scope

**Custody.**  The v4/v5 lane pipeline was read (`ops/aws_td6_v4_lane.sh`,
launch scripts): it verifies `SOURCE.sha256` before running and writes the
exact meta schema frozen here, including captured `rc`.  Weaknesses, all
disclosed rather than hidden: V6/V7 record `rc_inferred` instead of a
captured exit code; no on-host `source_verify` output is frozen for V6/V7
(their producers are hash-pinned in `launch.meta` instead); V4's producer
hash exists only inside its pinned archive; V6's `argv` line is cosmetically
mangled (`python h_b replay …`); no `ops/` launch script is frozen for
V6/V7; V4's own `u_zero`/`intersection` lanes were superseded by V5's
original-row certificate versions and are not charged (consistent with the
notes log).  None of these breaks the chain: every charged byte is pinned by
`MANIFEST.sha256` → `FREEZE.sha256`, and every executed producer is pinned
either directly or through its archive hash.

**Exhaustiveness.**  `A² = {UH≠0} ∪ {U=0} ∪ {H=0}` is a tautological cover;
`{UH≠0}` splits into the two charts by the resultant (section 4); `{U=0}`
splits as `C≠0` plus the origin (section 5); `{H=0}` splits as `UP≠0`, the
origin, and the `P=0` fibre (section 6).  All certificates are polynomial
identities over `E` (or the quotient), so the kill holds at points over
every field extension of `Q`; nothing restricts to rational points.  The
displayed loci exhaust the plane with no residual stratum.

**Scope.**  Report, README, and all seven stdouts carry the quarantine:
`family_killed=false / SP2_killed=false / JC2_resolved=false` per lane — the
family kill exists only as the case-level conjunction of the five strata,
which is the honest formulation.  The strongest conclusion supported, and
the only one claimed, is emptiness of the frozen source-typed fixed family
`(C,1,U)` at the first-band/P12 gate.  No full-centering, neighbourhood,
`c2≠1`, SP-2, maximum-degree, or JC2 statement appears anywhere in the
charged bytes.

## 9. Smallest false identity, missing stratum, or missing hypothesis

**None found.**  Every identity that the frozen evidence makes checkable was
re-derived by hand and is exact: four denominator factorizations (11-, 15-,
6-, 9-monomial expansions), the two h-zero/V6 denominators, `T−B`,
`Res_C(B,T)=64U^10`, `B(C,0)=1`, `P=B(3U²,U)`, both B-local resultants,
`P` irreducible and squarefree, the `U`-inverse mod `P`, `F` irreducible
mod 31, `Norm(ALPHA)=3^28/5^96` with the non-cube conclusion, `k ≠ 0`, the
unit-ness of `−k/50` under every scalar extension in scope, the `U=0`
residual's nonzero constancy, the chart bookkeeping (`C²·C=C³`,
`detdeg`/event consistency in all six lanes), and the exhaustiveness of the
stratification.  Nearest misses, all non-blocking and none a defect of the
mathematics: (i) the report's phrase "left-null witness" for the `U=0` kill
denotes the degenerate single-row functional (support `{13}`, coefficient
`1`) — accurate but worth a word in any successor; (ii) `B(C,0)=1` is
decorative in the cover argument; (iii) the V6/V7 `rc_inferred` and absent
on-host source-verify records are custody softness, disclosed in the frozen
metas themselves; (iv) the semantics of the V4 `reduction PASS` /
`first/source replay PASS` lines and of `KP_inverse_count` live in archived,
in-session-unreadable producers — the one heavy residual condition, pinned
by hash and corroborated by the readable parents and the re-executed
`(C,1,1)` predecessor, but not read here.

## 10. Promotable sentence and strict scope

> Under the frozen TD6 source typing of the charged archives — fixed
> transport patterns, rhs normalization (f-side `{15:1}`, g-side
> `{1:1,25:1}`), pole data, and centering jet `x = c1·s + c2·s² + c3·s³ +
> t·s⁴` with tail `t` a system unknown — the normalized two-center section
> `(c1,c2,c3) = (C,1,U)` admits, over every field extension of `Q`, no
> parameter point whose transported first band is consistent and whose
> genuine P12 row vanishes: off `U·H` the generic and B-local 28-row
> original-row certificates (charts `(1/4)BU³H³` and `(1/4)U³HT`, disjoint
> vanishing off `U·H` by `Res_C(B,T)=64U^10`) force `P12 = −k/50` with
> `k = 252−342S+144S²−36S³` a unit of `K=Q[S]/(F)`; the `U=0` divisor is
> first-band-inconsistent (unit constant residual at original row
> `('X-2',14)`, chart `C³`, rebuilt raw at the origin); and on
> `H = C−3U² = 0` the raw certificate applies off `U·P(U)` while the
> residual fibre `P = 128U⁶−32U³+1 = 0` is emptied by the raw rebuild over
> the field `Q[U]/(P)` with certified inversions and the same unit
> remainder `−k/50`.

Strict scope: emptiness of this one fixed, source-typed, normalized
two-parameter section at the first-band/P12 gate, conditional on the frozen
parent chain and on the archived producers meaning what their printed
certificates say (section 11).  Not promotable: any `c2 ≠ 1` or `c2 = 0`
point, any gauge claim for the `s`-rescaling, a third centering or
dead-stretch/boundary modulus, any neighbourhood statement in the full TD6
source space, any SP-2, maximum-degree, or JC2 conclusion.

## 11. Residual conditions

A shell-bearing session should run, from the repository root,
`python3 /tmp/td6_two_center_cover_probe_claude.py`, which closes: all
charged and manifest byte hashes (this session recomputed none), archive
extraction with `SOURCE.sha256` verification, the pinned producer hashes
(`8b4d6a36…`, `56df638a…`, `9b3de6b5…`), byte-equality of the archived
parent modules with the read repo copies, and independent recomputation of
every identity in sections 4–6.  It should additionally read, inside the
extracted archives, the four theorem-producing programs to confirm: the
`reduction PASS` asserts `remainder == −k/50` via the coefficientwise
cleared original-row identity; `KP_inverse_count` counts unit-certified
inversions at their point of use; and the `genuine`/`plus_one` controls are
implemented as advertised.  Every relation checkable by reading in this
session is consistent; a failure of any listed check would reopen this
review.

CONFIRMED
