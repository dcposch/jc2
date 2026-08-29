# Hostile review: K00 V20R2 valuation-three remaining-fan grade-12 certificate

Reviewer/engine: Fable 5 (independent hostile lane)  
Date: 2026-08-29  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94` (verified = HEAD)  
Primary: `xmodel/k00-r3-erfan-grade12-certificate-sol56-20260829.md`  
Verdict: **PASS_WITH_REPAIRS — every mathematical claim of the primary
certificate CONFIRMED by full independent reconstruction; one custody FAIL on
the upstream preflight artifact; the upstream fan packet, which had no
completed hostile review, is independently re-derived and confirmed here.**

No exit price is reported and no charge_basis claim is made.

## 1. Custody

| artifact | pinned | on disk | status |
|---|---|---|---|
| certificate (full, 12256 B) | `e84f2951…8638bb4` | same | PASS |
| certificate body (11923 B through the body-end marker) | `0dca07ec…a06c1e` | same | PASS |
| producer replay | `02fb368a…f4e2053` | same | PASS |
| source/threat packet (full) | `6940e1ea…948dc4` | same | PASS |
| packet body (19763 B) | `c2fffead…c0efbdcd` | same | PASS |
| frozen `tails.json` | `d72f774c…813848` | same | PASS |
| V20R2 compiler | `2ac7653c…8ad6d2b` | same | PASS |
| arithmetic/tail-parser library (r2 replay) | `2c918d5b…255e7c4` | same | PASS |
| canonical semantic tail digest | `6eed03d4…ce387e8` | reproduced independently | PASS |
| **source preflight** | `bac4b688…d38486aa` (task pin **and** packet §8) | **`a6eec646…353b94`** | **FAIL** |

**Custody finding (D1).** The on-disk
`xmodel/k00-r3-source-preflight-sol56-20260829.py` does not match the byte pin
recorded both in my tasking and inside the sealed packet's own §8.  The file
is untracked in git, so the sealed bytes are unrecoverable; the packet's §8
"observed output" is therefore unverifiable evidence.  I did not run the
drifted file and nothing in this review consumes it.  Compounding this, the
Opus 5 hostile-review lane for the packet emitted no report (96-byte
metadata-only log), so the branch-completeness packet the certificate charges
was, until now, both unreviewed and without valid replay custody.  Section 4
below repairs the mathematical content by independent re-derivation; the
provenance defect itself still needs the coordinator repair listed in §6.

Body-marker note: in both the certificate and the packet the marker string
also occurs once inside the seal prose, but each file has exactly one
standalone marker line, so the body definition is unambiguous and the body
hashes above are well defined.

## 2. What was independently reconstructed

All checks below were performed with a fresh implementation written for this
review (own JSON parser, own exact Gaussian-rational sparse polynomial and
series arithmetic, own localization test).  The pinned engine library was
**not** imported; the producer replay was executed only as a black-box
cross-check (§9).  Localization identities were decided by an independent
method (multiply out the bounded inverse-variable degree by powers of the
base and test literal zero in the free ring — valid because the quotient is a
localization of a domain), not by the replay's rewriting reducer.

From the frozen 569 tails I rebuilt the seven literal rows
`R + Λ²K10·A10 + Λ⁶K6·A6 + Λ¹⁰K2·A2` under the pinned coordinate map, and
confirmed against the pinned compiler (not the engine) the tail semantics:
load flags at monomial slots 7/8/9, Λ-shifts 2/6/10, targets at
`Λ^{12+l}` with sign −1 and `Jdet/4`.  The parse reproduces the packet §3.1
rowwise support table exactly (R: 234|234|2345|2345|2345|3456|23456, and the
A10/A6/A2 tables).  79 independent checks passed; every load-bearing identity
also carries at least one deliberate-mutation probe confirming sensitivity
(5/6→5/7 shift, 192→193, 6144→6143, 64→63, wrong resultant scalar 2^75, wrong
ER1 source ray).

## 3. Claim-by-claim verdicts on the primary certificate

| # | claim | verdict |
|---|---|---|
| 1 | custody pins of tails/compiler/library/replay/basis | CONFIRMED |
| 2 | 38-column source completeness through grade 12; no omitted K2 or target column can arrive | CONFIRMED (machine census, §5.1 below) |
| 3 | grade-11 common input: shift `U=u+(5/6)κs, V=v−(5/6)κt`; matrix `[[U,−V],[64V,U]]` with row scalars 3/1024, 3/16384; det Δ | CONFIRMED |
| 4 | grades 6–10 replay to zero on every residual input with all kernel/tangent/load data free | CONFIRMED |
| 5 | ER1(±): `h1 = −(5/16)t³κ − (3/4)t²V`; single normal solve on `D(V)`; all seven grade-11 rows ≡ 0 mod `qV·V−1` | CONFIRMED (both signs, separately) |
| 6 | ER1(±) grade-12 cokernel: displayed C1, C3; `C2=0`, `C4=−C3/8`, `C5=−C3/128` | CONFIRMED |
| 7 | ER1-UNIT: `12288·C1 − 6144·j·C3 = 800·t⁶κ²qV²` | CONFIRMED (both signs; T-, T²-, and all kernel/load-dependence cancels exactly) |
| 8 | ER1 Bezout: `1 = M·P − (A−1)(1+…+A⁵)B² − (B−1)(B+1)` | CONFIRMED as an exact identity in the free polynomial ring; a genuine unit-ideal certificate on `D(κtV)` |
| 9 | ER2: `h1,h2` as displayed; exact inverse `(1/Δ)[[U,V],[−64V,U]]`; all seven grade-11 rows ≡ 0 mod `qD·Δ−1` | CONFIRMED |
| 10 | ER2 grade-12: `C2=0`, dependents −1/8, −1/128; `C1,C3` of qD-degree ≤ 2; `N1,N3` exact binary quadratic **forms** in (U,V) (11 and 10 monomials, no dropped non-form terms) with the literal A–F coefficient table | CONFIRMED |
| 11 | ER2-RES: displayed closed form is the 4×4 homogeneous Sylvester resultant (generic identity checked), and `Res = −(5⁸/(2⁷⁶3⁴))κ⁸(s²+64t²)¹²` exactly | CONFIRMED |
| 12 | ray specializations `N1|ρ = −(25/3)t⁶κ²(U+ρ8iV)²`, `N3|ρ = ρ(50i/3)t⁶κ²(U+ρ8iV)²`; `Δ=(U+8iV)(U−8iV)`; contradiction with `D(Δ)` | CONFIRMED |
| 13 | three cells exhaust all residuals (charged to the packet) | CONFIRMED — independently re-derived end to end, see §4 |
| 14 | grades 13–19 typed "unreachable after certified empty prefix", not inferred empty; target grades 15/17/19 consistent with the anchor calendar | CONFIRMED (correct sequential-early-termination typing) |
| 15 | replay behavior: PASS in plain and `-O` (~5.0 s each here), identical output, four emitted hashes match the certificate, combined hash arithmetic correct, custody/mutation gates present, no `assert`-statement reliance | CONFIRMED |

No claim is REFUTED; no mathematical GAP was found.

## 4. Independent re-derivation of the charged fan (packet §5.1–§5.4)

Because the packet's preflight custody is broken and its review lane emitted
no report, I re-derived the entire case tree from my own row reconstruction.
Every stage was expanded with the widest legal generality (fully general
next coefficient before each forcing; all kernel, tangent, and load columns
`k10[1..4]`, `k6[1..3]` free symbols throughout).

* **Entry.** Grade 6 with fully general x equals `Q_i(x)`; the reduced-cone
  identities `Q1+8Q3=(3/2048)A·B` and `Q4=(3/524288)(B²−64A²)` hold over a
  fully general 6-vector, so the field-valued zero set is exactly
  `{A=B=0}` and the leading trichotomy by `(u,v)` (rank 2 / rank 1 / rank 0 =
  old plane, since `cone(a,b,0,0)=ell(b,8a)`) is exhaustive over an
  algebraically closed characteristic-zero field.
* **§5.1 L2.** Grade 7 is exactly the alpha/beta block on `(A(y),B(y))` with
  zero inhomogeneity (y forced to the cone); grade 8 is solved exactly by
  `A(z)=(10/3)κv, B(z)=−(10/3)κu` (consistent with the independently computed
  `M4|cone = (−5uv/256, (5/8192)(u²−64v²), coker-compatible)`); the grade-9
  cokernel is literally `G9_6=u(192v²−u²)/65536` and the displayed `G9_4`,
  with no y/z/w kernel or later-load dependence.  The `u=0` branch forces
  `b=0` then `S3=(1/4)v²(v+3a)`, `S5=−(3/64)v²(v+2a)` (kill).  On
  `u²=192v²`, solving row 4 for `b` gives `S5=(1/8)v³` and `S7=−(1/64)v³`
  exactly.  **Wording repair W1:** the packet's "exact two quotient
  constants 1/8 and −1/64" are the coefficients of `v³`, not literal
  constants; the kill is honest because `v≠0` on the branch, but a promoted
  statement should say `v³`-multiples.
* **§5.1 L1(±).** Grades 6–7 vanish; `G8_4=−(3/4096)v²λ²` with fully general
  z forces `λ=0`; after the full grade-8 solve including the tangent
  parameter, `G9_6=εiv³/32` exactly.  Both conjugates expanded separately.
* **§5.2 N2.** Grade 9 equals the y-block on `(A(z),B(z))` exactly (z forced
  to the cone); the displayed w-solve kills grades 6–10; the grade-11
  cokernel is generated by `−(3/2048)D` and `−(3/32768)F` (row 6 is zero and
  the remaining two rows are −1/8 and −1/128 multiples of the D-row), with
  both syzygies and both isotropic ray forms
  `D|ρ = t(u−8ρiv)²`, `F|ρ = 8ρit(u−8ρiv)²` verified; the kill against
  `Δ_y≠0` is complete in the nonisotropic and both isotropic source cases.
* **§5.3 N1(±).** `G10_4=−(3/4096)v_y²λ²` forces `λ=0`; grade-11 row 4 is
  exactly `(3/256)·v_y²·(s−8εit)` — **linear** in s with the unique root
  `s=8εit`, so exactly one source ray survives per branch (no conjugate
  leak).  After the p-image solve on `D(v_y)`, rows 1,3,4,5,6,7 vanish and
  the sole remaining grade-11 obstruction is literally the displayed
  τ-relation; `τ=0` is impossible on it (`t≠0, κ≠0`), and after solving it
  for `v_z` on `D(τv_y)`, `G12_6 = εi·v_y³/32` exactly, killing both
  branches.  **Robustness note:** on N1 the omitted deep column `d[8]` does
  polarize into grade-12 rows 1,2,3,5,7 through the y-block, but row 6 is
  universally jet-blind (`alpha_6=beta_6=0` at every cone point), so the row-6
  kill is unconditionally `d[8]`-robust; the packet should state this.
* **§5.4 fan.** With x=ell, y=ell and fully general z,w: grades 6–9 vanish
  identically and grade 10 is **exactly**
  `Q_i(z) + (5/6)κ[alpha_i(s,−t)A(z)+beta_i(s,−t)B(z)]`, so the two displayed
  identities force `A(z)=B(z)=0` over a field and all rows then vanish:
  z-forcing is complete.  The 5/6 shift is derived, not assumed: the M4
  polarization identity
  `2M4_i(ell(s,t),q) = (5/6)[alpha_i(s,−t)A(q)+beta_i(s,−t)B(q)]` holds for
  all seven rows.  At grade 11 (free cone parameters u,v) the rows are
  exactly the alpha/beta block at `(U,V)` on `(A(w),B(w))` plus a
  coker-compatible inhomogeneity matching the certified `h1,h2`; there is no
  other w- or p-dependence, so the grade-11 system is equivalent to the 2×2
  system and the E0/E1(±)/E2 trichotomy in `(U,V)` is an exhaustive
  field-valued cover.  E0 is empty (the two displayed cubics have binary
  resultant `2²⁴ ≠ 0`, so no common `(s,t)≠(0,0)` over any field, given
  `κ≠0`).  On E1(ε) the sixth cokernel row equals
  `(5κ/65536)(s+8εit)³` for both signs, forcing `s=−8εit`, `t≠0`; the image
  is solvable on `D(V)`.  The `(u,v)→(U,V)` reparameterization used by the
  producer is a triangular affine change of cone coordinates, bijective over
  any field, so no locus is lost.

Conclusion of §4: the residual cover after grade 11 is exactly
`R3-00-ER1(+), R3-00-ER1(−), R3-00-ER2` — the charged claim is CONFIRMED
independently of the packet's broken preflight.

## 5. Findings on the six tasked attack surfaces

1. **Source/open typing and completeness through grade 12.**  Machine census
   over all (piece, Λ-shift, coefficient multiset) combinations reaching
   grade ≤ 12 at exact valuation three: active columns are exactly
   `d_j[3..7]` (30), `k10[0..4]` (5), `k6[1..3]` (3) = 38.  The only routes
   involving `d[8]/d[9]` are the R-quadric polarizations (3,8)@11, (3,9)@12,
   (4,8)@12, all annihilated identically by `DQ(ell)≡0` (verified for all 7
   rows × 6 columns); on N1 the (4,8) route additionally cannot touch the
   killing row (row-6 jet-blindness).  `k6` columns are carried symbolically
   and are in fact inert on the residual branches (`A6^[1]` vanishes on the
   cone, hence lies in span{A,B}); `k10[4]` is likewise inert but harmlessly
   included.  First K2 arrival is 10+1+3=14; first target arrivals are
   μ2:15, μ4:17, μ6:19, Jdet:19 — none reaches 12.  The five boundary zeros
   are fixed before expansion.  No silent specialization found.
2. **The 5/6 shift and grade-11 split completeness.**  Confirmed from the
   tails (§4, §5.4 item): the shift is forced by the K10 polarization
   identity, the split is by the shifted `(U,V)` — splitting by the unshifted
   `DQ(z)` would be wrong, and my probe confirms the block identity fails
   with any other shift constant.  The trichotomy is exhaustive; zero
   coefficients live in rank-zero cells (no projectivization loss).
3. **ER1 both signs.**  Confirmed end to end with my own code for each sign
   separately (no conjugation shortcut), including the grade-11 solution,
   C1/C3, the unit combination (with exact cancellation of the free
   grade-6 datum T and all kernel/load data), and the Bezout identity, which
   I verified as a literal free-ring identity; it certifies
   `1 ∈ (P, ηκtV−1, qV·V−1)`, i.e. the localized unit ideal.  The wrong-ray
   probe (`s=+8εit`) leaves a nonzero grade-11 row, so the branch data are
   not interchangeable.
4. **ER2.**  Confirmed: inverse matrix (checked by composition), denominator
   clearing faithful (qD-degree ≤ 2, Δ invertible on the cell), N1/N3 are
   exact binary quadratic forms with the literal coefficient table, the
   closed resultant formula equals the 4×4 homogeneous Sylvester determinant
   generically, the scalar `−5⁸/(2⁷⁶3⁴)` is exact (probe at 2⁷⁵ fails), both
   ray specializations hold, and the endgame is sound: a survivor gives the
   two forms a common nontrivial root ⇒ Res=0 ⇒ `s²+64t²=0` (κ unit) ⇒ a
   ray ⇒ `N1=0` forces a linear factor of Δ to vanish ⇒ contradicts `D(Δ)`.
   `t≠0` on the rays follows from `(s,t)≠(0,0)`.
5. **Exhaustiveness and grades 13–19.**  The full case tree
   L2/L1(±)/L0→N2/N1(±)/N0→E0/E1(±)/E2 is exhaustive and now independently
   verified at every node (§4).  Grades 13–19 are correctly typed
   "unreachable after a certified empty prefix": every branch is obstructed
   at a grade ≤ 12, so no residual input exists to truncate further; this is
   sequential early termination, not an inferred-empty or missing-output
   claim.  No false-empty pattern found.
6. **Semantics, localization, controls, overclaims.**  Field-valued
   characteristic-zero scope is declared and is exactly what the square/cube
   root steps (`λ²=0`, `(s+8εit)³=0`, `(U+ρ8iV)²=0`, `B²=64A², AB=0`) need;
   emptiness over the algebraic closure implies emptiness over any
   characteristic-zero field, which is the right direction for a
   constructible-emptiness endpoint; no scheme or nilpotent claim is made
   (the packet's §4 firewall is respected).  Localizations are honest: ER1
   carries inverse relations plus an explicit Bezout unit certificate; ER2
   clears only powers of the defining unit and reuses the defining open at
   the contradiction; every division site has its localizer in the cell
   definition (κ source, V cell, t forced, Δ cell, v_y cell, τ forced).
   The producer's four mutation gates are real (I reproduced the 6144→6143
   and 64→63 kills in my own frame) and my six additional probes all
   detect.  Formal-data-not-map discipline holds: all later data stay free
   symbols; no arc, map, or attainment is constructed.  The only overclaim
   candidates found are the two wording items W1 (v³-multiples) and the
   cosmetic table reference in the certificate's "Frozen literal source"
   section ("the last file is imported" — the imported library is the third
   table row, the fourth row is the replay itself); neither affects any
   mathematical claim.

## 6. Defects and repairs required for safe promotion

* **D1 (custody, material).**  Preflight pin mismatch (`bac4b688…` sealed vs
  `a6eec646…` on disk), sealed bytes unrecoverable.  Repair: coordinator
  either (a) re-issues/re-pins the preflight under a fresh seal, or
  (b) formally supersedes its evidentiary role by this review's independent
  reconstruction (all of its §5 content is re-proved here) and records the
  drift in the ledger.  Do not promote the packet's §8 "observed output" as
  evidence in either case.
* **D2 (process, discharged here).**  The packet had no completed hostile
  review; §4 of this report now supplies an independent re-derivation of all
  charged content.  A promotion note should cite this review, not the absent
  Opus report.
* **W1/W2 (wording, minor).**  State the L2 `u²=192v²` kill values as
  `(1/8)v³` and `−(1/64)v³`; add the N1 row-6 `d[8]`-robustness sentence;
  fix the "last file" table reference.

No mathematical repair is required.  No AWS or Gröbner escalation is needed:
every check in this review is desk-scale (my full independent suite runs in
about ten seconds; the producer replay in about five).

## 7. Maximum exact theorem safe to retain

> **Theorem (normalized V20R2, exact valuation three, finite-jet and
> formal-arc emptiness).**  Fix the reviewed V20R2 compiler specialization
> `C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1` with
> boundary zeros `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`, `κ=k10[0]≠0`,
> `Jdet[0]≠0`.  Over every field of characteristic zero there is no exact
> valuation-three solution datum `d=Λ³x+Λ⁴y+Λ⁵z+…` with `x≠0` of the seven
> literal rows: every such finite jet violates some row at a grade ≤ 12
> (grade 9 on L1/L2, 11 on N2 and E0, 12 on N1 and on ER1(±)/ER2).
> Consequently the normalized V20R2 valuation-three stratum is empty at
> finite-jet scope, and by truncation no same-source valuation-three formal
> arc exists.

Scope boundary: field-valued only (no scheme/nilpotent statement), this one
normalized support only, no claim about other valuations, no periodicity
import or export, no Keller map or JC2 consequence, and the normalized
valuation atlas ↔ JC2 bridge remains a separate campaign obligation.

## 8. Closure statement

All three residual cells are confirmed empty at grade 12.  With the upstream
fan independently re-derived in §4, **this closes exact valuation three on
the normalized V20R2 support at finite-jet and formal-arc scope, and at no
broader scope**, subject only to the D1 provenance repair (which concerns
custody bookkeeping, not mathematical content).

## 9. Cheapest successor

Fold the (now custody-broken) preflight content and the grade-12 endpoint
into one re-pinned desk-scale closure replay for the valuation-three lane —
a single file, single seal, running the §5 fan and the three residual-cell
certificates under one custody gate — then promote the stratum closure and
retire the lane.  This is a one-session coordinator task with no new
mathematics; after it, the next open obligation in this campaign is the
remaining strata of the normalized valuation atlas and the atlas-to-JC2
bridge, not anything at valuation three.

## 10. Execution record

Verified pins with `shasum`; ran the producer replay in ordinary and
optimized mode (both PASS, 4.98 s / 5.02 s, byte-identical output except the
runtime line; all four emitted hashes equal the certificate's, and the
combined hash is the SHA-256 of the three concatenated hex digests).  All
independent mathematics ran from a fresh implementation in a scratch
directory outside the repository; 79 checks passed with 8 sensitivity probes.
Basis commit confirmed unchanged.  No web, no CAS, no AWS, no jc2-lean
access, no ledger or artifact modification; the only repository write is this
report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19677`.
- Body SHA-256:
  `611ff99b2404d5f640b1fb1acf87755991a38bef7abf194ea70bf2d4c6d8c98f`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
