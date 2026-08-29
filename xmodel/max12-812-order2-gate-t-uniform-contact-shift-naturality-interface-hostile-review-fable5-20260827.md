# Hostile review: uniform strict unique-`AC` source transport (naturality + linker interface)

Date: 2026-08-27
Reviewer: Fable 5 (Anthropic), adversarial algebraic-geometry / formal-series desk review.
Independence: all algebra re-derived here; the only campaign data consumed by the
executable checks is the frozen `tails.json` (byte hash verified below).  No producer
`PASS`, `CONFIRMED`, or promotion label was accepted as evidence at any point.

## 0. Candidate, comparator, and overall verdict

Candidate under review (hash re-verified byte-exact):

```text
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
```

Independent design comparator (hash re-verified; treated as comparator, not authority):

```text
8867c66a8e436107d059269e18347ef8ef01bbf8fdaa44ccec6b58fcef874944
  xmodel/max12-812-order2-gate-t-strict-uac-uniform-transport-design-grok-20260827.md
```

| # | Mandated attack | Verdict |
|---|---|---|
| 1 | Re-derive (1.1)–(1.4) coefficientwise: factors `2`,`4`, moving `P`, three loads, target subtraction | **CONFIRMED** — no bad coefficient found through grade 38 at eleven contacts |
| 2 | (1.5) simultaneously in all grades; hidden hypotheses | **CONFIRMED**, with one **REPAIRABLE** wording defect (commutation must be read through the jet-reindexing map, not bare "continuity"); hypothesis inventory in §3 |
| 3 | Layer separation; residual semantic-agreement checks | **CONFIRMED** separation; six finite layer-2 obligations remain (§4) |
| 4 | Hensel recurrence + shifted root maps (2.1)–(2.5), both signs, `D(rho)` only | **CONFIRMED** exactly |
| 5 | Finite-jet bound (3.1)–(3.2) at low band, `E`, load walls, grade-38 ceiling | **CONFIRMED** at every tested cell; one **REPAIRABLE** precision gap in the over/under-prediction discussion (§6.3) |
| 6 | Eleven endpoint families, literal-row provenance, `(a,d)=(8,3)` status | **CONFIRMED**, with one filename trap the interface must pin (§7.2) |
| 7 | Schema/linker interface and mutation controls; smallest executable verifier | **CONFIRMED** design; verifier specified and substantially prototyped in this review (§8) |
| 8 | Reversed map direction, unlicensed descent, hidden `rho`-localization, `k2c` collision, target omissions, composition inflation | **CONFIRMED clean** — none found (§9) |

**Overall: CONFIRMED as a provisional formula-level source-transport theorem**, exactly as
the candidate's own status line scopes it.  Nothing here promotes it; the two repairable
items are wording/precision, not mathematical error.  The strongest surviving theorem and
the exporter-retirement answer are in §10.

## 1. Custody verified

All hashes below were recomputed in this session and match the citing documents.

Eight charged notes (prefixes as in the design §10): `1b583d5a…` discriminator,
`d62b3f22…` Opus5 bridge review, `614ddcdb…` erratum, `db0ecebf…` a2 composition,
`1d086a79…` a2d2 composition, `85533441…` contact-ladder promotion, `cdd23058…` d23
composition audit, `94a6037d…` d23 composition review — all eight full SHA-256 match.

Compilers and tails:

```text
e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c  compile_r1_d1_ac.py
3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938  compile_t_rs0_discovery.py
77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc  compile_square_load_ladder.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  tails.json (canonical
    6eed03d4… enforced inside both compilers)
```

Byte-level facts read directly from those sources, not from any note:
`source_block` of `3aa6bbbb…` is literally (1.1) with `p_total = -2*rho^2 + 2*sigma*ell1
+ …` hard-coded and scope `mod sigma^13`; `source_coefficients` of `e024a13d…` is
literally the (1.4) shape with the docstring "C and R use direct polynomial
coefficients, so the factors 2 and 4 are inserted here"; `tail_text` of `77f25216…`
enforces per-monomial weight `12+ell` under weights `(8,7,6,5,4,3,2,2,6,10)`, at most one
load, load `Lambda`-weights `(2,6,10)` with `Lambda -> sigma^2` (so delays 4/12/20), and
targets `-sigma^{2(12+ell)}*(0,mu2,0,mu4,0,mu6,J/4)`.  Census re-counted from the JSON:
`36+54+58+81+89+120+131 = 569`.  The total ring's third `k10` jet is literally named
`k2c`; the D1 rings name the `k2` load `k2load`; the D1AC ring reuses `a1,a0,c1,c0` for
*shifted leading* jets that in the total ring are *stage-zero* jets.  All three naming
hazards are real (§8, §9).

Twelve endpoint artifacts located by full-corpus hash sweep; all twelve prefixes cited
by the design resolve to existing files (`973f7953`, `829ac12f`, `3d847561`, `dfabe082`,
`8b92c22b`, `2ff74f69`, `b5c38f1b`, `9cc68702`, `02cbae00`, `551ca2f6`, `d4aceedb`,
`470ea478`).  `02cbae00…` is a hostile-*review* file, not a promotion — see §7.

Grade-20 defense chain: `cases/max12_812_order2_gate_t_actual_total_g20_custody_v44*`
exists; `v44` and `v44r1` are frozen failures; `v44r3` carries producer-labeled
`PASS-ACT-TOT-G20-CUSTODY-V44R3-{P65521,Q,CROSSLANE}`.  Used here only as evidence that
the grade-20 run exists; its PASS labels carry no weight in this review.

## 2. Attack 1 — re-derivation of (1.1)–(1.4): CONFIRMED

Hand algebra.  Under (1.3): `Ctot = sigma^2 S -> sigma^{r+2} B_z = Kc`;
`Rtot = (P^2 + sigma^2 Q)/4 -> P^2/4 + sigma^2*(4 sigma^r B_c)/4 = P^2/4 +
sigma^{r+2} B_c = Kr` — the factor `4` exists precisely to cancel the `/4` of the
generating-function chart; `N1 = sigma^3 (P*Az + Ez)/2 -> sigma^3 (P sigma^a A_z +
2 sigma^c C_z)/2 = sigma^3 (P sigma^a A_z/2 + sigma^c C_z)` — the factor `2` exists
precisely to cancel the `/2` of `D=LA+C`; `N0` likewise; `N3, N2` are pure shifts.
These are exactly the `kc, kr, n3..n0` of the frozen `source_coefficients`.  So the
factors are forced, as claimed, and any other constants break (1.4) at the first grade
where the corresponding series enters.

Executable check (independent implementation; only `tails.json` read).  With every jet a
random value and total jets *defined* through the map (D) from D1 jets, all seven `F_i`
and all seven full rows (569 tails, all three delayed loads, targets subtracted) were
compared coefficientwise, total side against D1 side:

- exact `Fraction` over `Q`: `(a,c,r;N)` = `(2,3,2;16)`, `(2,4,3;18)`, `(2,5,3;20)`,
  `(1,4,2;18)`, `(5,6,5;22)` — **zero mismatches at any grade**;
- mod `p=1000003`: `(7,8,7;26)`, `(8,9,8;28)`, `(9,10,9;30)`, `(8,11,8;38)`,
  `(10,11,10;38)`, `(20,21,20;38)` — **zero mismatches**, with `k6`, `k2`, and all four
  targets active inside the windows.

The `p0` used was a free random value, *not* `-2 rho^2`: the identity is genuinely
unsplit, confirming the candidate's separation of the Kummer step.

**Smallest bad coefficient: none.**  Negative controls (each mutation applied to one
side only) all fire, at the grades the algebra predicts:

```text
rs factor 4->1 : first F-mismatch (F0, grade r+2): grade 4 at r=2, grade 5 at r=3;
                 first ROW mismatch grade 16 at (2,3,2) — grade 15 really is R-free;
ez factor 2->1 : first F-mismatch (F0, grade c+5): grade 8 at c=3, grade 10 at c=5;
                 first ROW mismatch at G=15 resp. 17;
drop 2*sigma*ell1 (total side only): first F-mismatch grade 1; first ROW mismatch
                 grade 16 — the moving term is invisible in rows at grade 15, exactly
                 as the Opus5 record states;
k2c -> k2load  : NO mismatch of any kind through N=16; first ROW mismatch grade 18 at
                 (2,3,2) (k10 jet-2 via the grade-16 k10 families), grade 20 at
                 (2,5,3) (k10A^2 at 18 + 2).  A grade-15/16 replay cannot catch this
                 wiring bug; only a syntactic check of the map can (§8).
```

## 3. Attack 2 — does (1.5) really hold in all grades at once: CONFIRMED, one repair

The candidate's proof sentence — "coefficient extraction commutes with a continuous
`sigma`-adic homomorphism" — is **false as a general statement**: a continuous
substitution that moves a generator's `sigma`-grade (e.g. `x -> sigma*y`) does not
commute with `[sigma^g]`.  What makes (1.5) correct is that the series substitution
(1.3) is the coefficientwise extension of a **jet-reindexing map** on the polynomial
ring of jets (`az_i -> A_{z,i-a}` etc., with the scalar factors), i.e. the map (D) of
the design.  A map that fixes `sigma` and sends jet variables to scalar multiples of
jet variables commutes with `[sigma^g]` trivially, and its coefficientwise extension
sends the input series exactly to their (1.3) images.  That reading makes (1.5) an
unconditional formal identity, grade by grade, for **all** nonnegative `(a,c,r)` — the
unique-`AC` inequalities are not needed for the identity itself, only for which chamber
theorem covers the cell.  **Repair: state the jet-map form (D) in the theorem, or cite
it; do not rest the proof on "continuity" alone.**

Hypothesis inventory (searched for, as mandated):

- **Inversion:** none.  (1.3)/(1.4) divide only by `2` and `4`; no leading form of
  `A`, `C`, `R`, no `theta`/`eta` normalization, no `rho` is inverted.  Verified: the
  numeric identity holds with all leading D1 jets random (closed orders), and with
  `p0` free.
- **Coefficient ring:** the complete set of denominators of all 569 tail coefficients
  was extracted: `{2^2, 2^3, …, 2^20, 2^23}` — all powers of `2`.  So (1.5) is an
  identity over any `Z[1/2]`-algebra; "characteristic zero" is safe but stronger than
  needed, and the odd-prime finite-field replays are licensed.
- **Parity:** none used; confirmed by the free-`p0` run (no `rho`-evenness anywhere in
  the identity).
- **Truncation:** none at formula level.  The quotient (1.2) kills only *lower* jets;
  every higher jet is retained on both sides.  Truncation enters only through the
  finite-manifest depths, which is §6's business, not (1.5)'s.
- **Source-completion:** real, and correctly handled by the candidate: (1.1) with
  infinitely many jets is a *definition made by this note*.  The only frozen total
  emitter (`3aa6bbbb…`) is `mod sigma^13` with Kummer hard-coded, so for grades `>= 13`
  there is no byte-level total emitter at all — the schema's pinning of (1.1) as
  normative text is what gives "actual total" a meaning at higher grades.  One repair
  suggestion for §4 of the candidate: the schema field "the total-emitter
  implementation hash" should be optional/plural evidence, with the seven formulas
  themselves normative; otherwise the schema silently inherits the `sigma^13`
  limitation of the only existing implementation.

Conclusion: (1.5) is one formal-power-series identity, not an induction; truncating
both sides `mod sigma^{T+1}` yields every finite endpoint comparison at once.  The
candidate's sentence to that effect survives attack.

## 4. Attack 3 — layer separation and what is still needed: CONFIRMED

The candidate's four evidence layers are the right partition, and my byte reads confirm
the layer-2/3 landscape it presupposes: the D1 and total compilers do implement
(1.4)/(1.1); the Opus5 bridge review separately records that V20/V22 exporters use their
own `build_row` (the producer's "same frozen `tail_text` function" claim was false) with
positional agreement verified, and that the entire grade-15 raw row ideal deflates to
two binomials — so a grade-15/16 replay is a very weak semantic control (my mutation
table quantifies this: factor `4`, moving term, and `k2c` wiring are all invisible at
15, and `k2c` is invisible through 16).

Before serial actual-total grade exporters can be retired, exactly these
semantic-agreement obligations remain; all are finite and desk-scale:

1. Freeze the **schema object** with (1.1), delays `4/12/20`, targets `28/32/36/38`,
   the tails byte hash `d72f774c…` and canonical hash `6eed03d4…`, the 1..7 census, and
   the alias table — as normative text, per the repair above.
2. Record as a lemma: `source_block` (`3aa6bbbb…`) = (1.1) after `p0 -> -2 rho^2`,
   `mod sigma^13` (checked here by byte read); `source_coefficients` (`e024a13d…`) =
   (1.4) shape (checked here); V20/V22 `build_row` agreement (already in the Opus5
   record; cite it, do not restate it as "same function").
3. Per endpoint manifest, the linker's duty-3 comparison of that chamber compiler's
   coded primitives against (1.4) — I verified the shared `r1_d1_ac` module only; each
   chamber producer's own compiled source must be compared by the linker, not assumed.
4. The **renaming-map derivation** must be syntactic and generated, never hand-written:
   three concrete hazards found in frozen bytes — total `k2c` (a `k10` jet) vs D1
   `k2load` (the `k2` load); D1AC's reuse of `a1,a0,c1,c0` for shifted leading jets;
   `theta`/`eta` normalizations absorbed into leading forms.
5. The executable linker/verifier itself (§8), frozen and hostile-reviewed once.
6. The `(a,d)=(8,3)` narrow promotion, or an explicit conditional label on the union
   (§7).

No additional `ACT-TOT-G22`, `-G24`, … appears on this list, and nothing mathematical
can appear on it: `[sigma^g] Phi_ell^tot` at `g=22` is a defined polynomial the moment
the schema exists, and an exporter adds only layer-3 bytes of it.

## 5. Attack 4 — moving Hensel and shifted root maps: CONFIRMED

Re-derived by hand and re-executed exactly (independent code, `Fraction` arithmetic):

- `[sigma^n]` of `lambda^2 = -P/2` gives `2 lambda_0 lambda_n = -ell_n -
  sum_{1<=i<n} lambda_i lambda_{n-i}` — (2.2) exact; both branches `lambda_0 = ±rho`
  satisfy `lambda^2 + P/2 ≡ 0 mod sigma^{13}` in the executed check; every `lambda_n`
  carries `(2 lambda_0)^{-1}`, so existence/uniqueness holds on `D(rho)` and **only**
  there.
- Deck: the recurrence is determined by `lambda_0`, so `lambda^{(+)}|_{rho -> -rho} =
  lambda^{(-)}` termwise (verified; the jets flip sign with the branch).
- (2.3) regularity: after (1.2), `Ac ± lambda Az`, `(Ec ± lambda Ez)/2`, `Q/4 ± lambda
  S` have `sigma`-valuation `>= a, c, r` respectively (verified: all lower coefficients
  vanished identically), so the shifts are regular — no localization beyond `D(rho)`
  is hidden in (2.3).
- (2.5) jet formulas exact for both pair signs and both deck branches; (2.4) leadings
  identify with the D1 direct coefficients as `A(±rho)`, `C(±rho)`, `R(±rho)`; the
  level-`n` diagonal blocks have determinants `-2 lambda_0`, `-lambda_0/2`,
  `-lambda_0/2` (the stage-zero determinants of the discriminator, now acting on
  shifted jets), and the triangular inversion was executed at level 3 — it requires
  `1/lambda_0` and nothing else.  Nothing in (2.1)–(2.5) survives at `rho=0`; the
  candidate says so and the ramified fibre stays a separate Gate-T obligation.
- Stage-zero annihilation: under (D) with `a>=1, c>=1, r>=1`, all six stage-zero
  values `rs, cs, c0, c1, a0, a1` map to `0`; the stage-zero pairs evaluate to `0`
  identically (executed).  They cannot be "substituted back in": the shifted-pair
  inverse reconstructs shifted jets only, and any composition of the stage-zero
  matrices with (D) is the zero map — the erratum (`614ddcdb…`, "delta_D1 annihilates
  `J1+J2`") is honored, and the candidate's §2 closing paragraph states the correct
  replacement.

## 6. Attack 5 — the finite-jet bound: CONFIRMED at every tested cell, one refinement

### 6.1 Empirical window checks (t-tagging)

Each family's jets were tagged with a formal `t` and the rows expanded mod `p`; "first
grade with `t`-dependence" is then the family's true first arrival in the *rows* (not
in raw `F`'s).  Every prediction of the polar table survives:

```text
(2,3,2):  A first at 15 (=10+a+c); R first at 16 (grade 15 R-free);
          k6 first at 20 (=17+c);  k2 first at 24 (=22+r);  mu2 first at 28;
(1,4,2):  A first at 15; max A-degree 2 at grade 17, 3 at grade 18 (=15+3a):
          the pole-three A^3 family enters exactly at the E-cell's T=18;
(10,11,10): k6 first at 28 (=17+c, the first polar), A first at 31 (=10+a+c),
          k2 first at 32 (=22+r), J first at 38;
(20,21,20): k6 first at 38 (=17+c).
```

Row-level first-nonzero grades, observed on the D1 side, corroborate the chamber
pictures: at `(2,3,2)` all rows start at 15 except row 4 (16) and row 6 (none through
16); at `(1,4,2)` row 6 turns on at 18 with the `A^3` cubic; at `(8,11,8)` and
`(10,11,10)` rows start at 28 with row 4 at 32 (`C^2`+`mu4`) and row 6 at 36 (`mu6`);
at `(20,21,20)` the odd rows and `J` start at 38 while rows 2/4/6 below 38 are *bare
targets* at 28/32/36.  The last line is a direct empirical confirmation of the
design's counterexample: at `a=20` there is no `C^2` content in the used window at
all — a `T_C2`-based transport would be comparing against nothing.

### 6.2 Jet maxima (3.2)/(3.3)

Single-jet tagging (tag exactly one relative jet, ask whether any row through `T`
depends on it) reproduces the claimed ceilings **exactly, in both directions**:

```text
(2,5,3), T=20:  A[3] in / A[4] out;  C[3] in / C[4] out;  R[1] in / R[2] out;
                k10[2] in / k10[3] out;  ell[3] in / ell[4] out;  k6, k2 absent.
                => (3.3) "p/A/C=3, R=1, k10=2, k6=0, k2=0; targets absent" is exact.
(10,11,10), T=38:  A[7]/A[8], C[10]/C[11], R[6]/R[7], k10[6]/k10[7], k6[10]/k6[11],
                k2[6]/k2[7], ell[10]/ell[11] — in/out at exactly the reviewed
                `A_7, C_10, R_6, k10_6, k6_10, k2_6, p_10` ceilings.
```

### 6.3 Over/under-prediction: the precise statement the note should carry

The candidate says raw valuations of the unreduced `F_i` "can overpredict because the
frozen tail polynomial cancels them."  Correct, but the safety analysis should be made
explicit, because it is asymmetric and one family is special:

- Cancellation can only *raise* `sigma`-valuation.  Hence a raw-valuation census can
  never omit a jet that actually enters grades `<= T`: it over-retains (predicts
  families/jets that cancel), which is sound and merely wasteful, and it underpredicts
  first *row* grades (a false-obstruction risk, not a missing-jet risk).
- For the moving `P`-jets the raw bound is **vacuous**, not merely loose: `F6 = 2P`
  has valuation `0`, so raw census retains every `ell_j` through `T`.  The useful
  bound `m_P = T - g_0` needs the reviewed first polar grade `g_0`, i.e. the reviewed
  statement that the tails cancel *all* pure-`K` content below `g_0`.  So the
  candidate's insistence that (3.2) "must consume the chamber's reviewed polar
  primitive inventory" is not a stylistic preference; for `P`-jets it is the only
  non-trivial bound, and my `ell`-tagging verified it exactly at two chambers
  (`ell_3`/`ell_4` at `(2,5,3)`, `ell_10`/`ell_11` at `(10,11,10)`).

The polar inventory itself is corroborated at the byte level: the frozen
`universal_hshift` in `e024a13d…` carries exactly the eight `k10`-band families with
delays `10,10,12,15,10,11,13,14` and pole orders `inv1/inv2/inv3`, including
`-(1/16) sigma^15 t^4 A^3 inv3`; the `k6C` (`17+c`) and `k2R` (`22+r`) arrivals were
verified empirically above.  A complete reviewed polar inventory is genuinely
sufficient for (3.2); its completeness is a chamber-review obligation already inside
the eleven reviews, which is where the candidate places it.

`T` is the chamber's terminal grade, not `10+2c`: confirmed at the `E` cell (obstruction
is the `A^3` unit, arriving at the same numerical grade 18 that `T_C2` happens to give —
same `T`, different theorem), at the walls `a=7,8,9` (k6-tie at 25/25; load-first 26
before `AC` 27; split at 27), and at the ceiling (`T=38` fixed while `AC` recedes to 51
at `a=20`).  My census run reproduces the strict cell list: eight `d=1` tails
(`a=2..9`), eighteen `d=2,3` tails with the stated `s_min` pattern, and exactly the two
`AC=R3` equality exclusions `(2,2,2)`, `(3,3,3)`.

## 7. Attack 6 — endpoint families and provenance: CONFIRMED, one trap to pin

### 7.1 The eleven families

The d23 composition audit (`cdd23058…`) lists the `d=2,3` assignments with full
promotion+review hashes; all resolve to existing files matching the design's §10 table,
and the `d=1` chain (`973f7953`, `829ac12f`, `3d847561`, `dfabe082`) exists.  Counting
cells: 8 (`d=1`) + 12 (`lowa6` eleven-block + `E`) + 2 (`a=7`) + 2 (`a=8`) + 2 (`a=9`)
= 26 = my independent census of `a<=9` strict cells, plus the `a>=10` cone
(`d4aceedb…` exact-contact parent + `470ea478…` closed ceiling).  No strict cell is
unassigned.  The union's theorem types are mixed (arcwise on `D(p*k0)`-type loci vs.
unit-ideal at `a=9`/ceiling), and the candidate correctly refuses to reconcile them.

### 7.2 `(a,d)=(8,3)`: confirmed-but-unpromoted, and a filename trap

The chamber review `02cbae00…` is a hostile review returning holds on all counts, with
the obstruction being the **four literal odd `SourcePhi` rows** expanded independently
over exact `Q` (`[sigma^28] Phi1 = (3/4) k60 c1` verified there with term census 907,
and `FullPhi7 = SourcePhi7 - sigma^38*(J/4)` read from compiled bytes).  No narrow
emptiness promotion exists; the d23 audit says so explicitly.  **Trap:** the file
`max12-812-order2-square-d1-a8d3-moving-connection-rankjump-route-promotion-20260826.md`
*is* named a promotion, but its status line is "PROMOTED ROUTE FALSIFICATION ONLY" — it
promotes the negative statement that no single universal odd functional exists in that
chamber and falsifies the fixed-`z` analytic bridge (`k6A^2` column `(-3/16, +3p/64)` vs
`k6RC` `(-3/16, -3p/64)`, determinant `9p/512`).  A linker that greps for
"a8d3…promotion" would wrongly conclude the endpoint is promoted.  The manifest's
`endpoint status` field must therefore bind to the *hash* of the specific promotion
artifact, never to a filename pattern.  With that pinned, the candidate's treatment is
exactly right: the link must select the literal odd-row certificate; the earlier
analytic bridge is a frozen no-verdict route failure and its family-16 coefficients are
affirmatively falsified — an analytic-only `(8,3,8)` certificate must be rejected, and
the promoted route-falsification is independent grounds for doing so.

### 7.3 Analytic devices generally

The frozen D1AC compiler contains both the literal `Phi` rows and the
`universal_hshift` analytic device, tied by `ROW_IDENTITIES` (`row_checks` compares `h`
values against literal row coefficients through `transform_series`).  That is the
licensed pattern: analytic charts as derivation devices with a reviewed bridge to the
rows.  The candidate's linkability criterion (literal-row identity, possibly localized,
or a reviewed bridge through `T`; otherwise reject) matches what the frozen artifacts
actually do.  Presently no promoted unique-`AC` emptiness rests on an unbridged `H`.

## 8. Attack 7 — interface and the smallest executable verifier: CONFIRMED

The candidate's six fail-closed linker duties and four-layer output discipline are the
right shape, and its mutation-control list is well-chosen: my executed controls confirm
each listed mutation is (a) detectable at the stated place and (b) *not* detectable by
shallow row replays — in particular `k2c -> k2load` is invisible in all seven rows
through grade 16 and first visible at 18/20 depending on the chamber, so only a
syntactic check of the derived renaming map can enforce it at shallow `T`.  Two
additions from this review: (vii) bind endpoint status to promotion-artifact hashes,
never filename patterns (§7.2); (viii) derive the alias table for rings that reuse
stage-zero names for shifted jets (D1AC `a1` ≠ total `a1`), which is a special case of
the candidate's duty 1 worth naming.

Smallest executable verifier (measured feasibility — this review's throwaway harness
already performs the core of V1/V3/V5-lite in ≈15 s total, pure Python, no CAS):

- **V0 pins** (<1 s): byte+canonical hash of `tails.json`, census 569 = 36+…+131,
  weights/loads/targets table; compiler hashes; manifest hashes; refuse on any drift.
- **V1 naturality** (≈5 s): independent truncated-series build of both sides of (1.5)
  at one representative contact per family — the eleven of §7.1, including `E`, the
  three walls, and the ceiling at `N=38` — over `Q` at shallow windows and mod an odd
  prime at deep ones; zero-mismatch required.
- **V2 mutation controls** (≈5 s): the candidate's six plus stage-zero-in-place-of-
  shifted (must produce the zero map) plus the two additions above; each must fire at
  its predicted grade, and the `k2c` control must be syntactic.
- **V3 support tables** (<1 s): recompute the polar table and `T_* - w` maxima from
  each manifest's `(a,c,r_floor,T_*)`; reject `T_C2` at the exceptional, wall, and
  ceiling chambers; optionally re-verify maxima by single-jet tagging as done here.
- **V4 provenance** (<1 s): per family, require the promotion/review hash to resolve
  and its status line to be an emptiness promotion (not a route falsification); require
  a literal `Phi`/`SourcePhi` obstruction or a reviewed bridge; special-case `(8,3,8)`
  to the literal odd-row certificate.

One Python file, no AWS, no 569-tail symbolic expansion beyond the truncated windows
above.  A frozen, hostile-reviewed implementation of V0–V4 is the last artifact needed
before the interface is usable as campaign infrastructure.

## 9. Attack 8 — adversarial search: clean

- **Reversed scheme-map direction:** not present.  (1.5) is a coefficient identity;
  emptiness transport is stated only through arc factorization (total DVR arc of the
  exact contact factors through (D) at grades `<= T`), the direction the erratum
  licenses.  The candidate's §5 explicitly refuses the reverse direction without
  finite-jet factorization.
- **Unlicensed Kummer descent:** none.  `p0` stays free through (1.5); Kummer enters
  afterwards, finite flat, used only on `D(rho)`; the candidate refuses `rho=0`
  extension of (2.3), and the a2-composition countermodel (`A=Q[rho,u]`, `I=(u-1)`,
  `q: A -> A/(u)`) is not contradicted anywhere — no cover claim is made.
- **Hidden `rho`-localization:** (1.5) verified with `p0` a free unit-free random
  value; denominators are powers of 2 only.  §2 requires `D(rho)` and says so.
- **`k2c`/`k2load` collision:** real (byte-verified in both rings), controlled, and
  quantified here (invisible through grade 16).
- **Target-window omissions:** none found; schedule `28/32/36/38` verified in both
  frozen compilers and empirically (`mu2` tag fires at exactly 28, `J` at exactly 38);
  the deep-window runs had all targets active and still matched.
- **Composition inflation:** the candidate states, twice, that the eleven endpoint
  families remain eleven independent inputs and that the interface creates no new
  emptiness theorem.  Its status line claims replacement only of serial per-grade
  actual-total *builders*, which §10 below endorses.

## 10. Strongest surviving theorem, remaining obligations, exporter answer

**Theorem (uniform contact-shift naturality; survives this review unconditionally).**
Fix the schema data: the seven formulas (1.1), the 569 frozen tails (byte
`d72f774c…`), load delays `(4,12,20)`, target schedule `(28,32,36,38)`.  Over any
commutative ring in which `2` is invertible, for every triple of nonnegative shifts
`(a,c,r)` the jet-reindexing map (D) (equivalently the substitution (1.3), with factors
`4` on `Q` and `2` on `Ez,Ec` forced) satisfies, for all seven rows and every grade
`g >= 0`,

```text
delta_{(a,c,r)}([sigma^g] Phi_ell^total) = [sigma^g] Phi_ell^{D1(a,c,r)}.
```

No inversion, parity, truncation, or `rho`-condition enters.  On `D(rho)` (after the
separate Kummer step) the shifted pairs (2.3)–(2.5) are triangular with diagonal
determinants `-2 lambda_0, -lambda_0/2, -lambda_0/2`, deck-exchanged, and the
stage-zero pairs are annihilated — the erratum's correction is built in.

**Composition (conditional, unchanged from the design's schema).**  For each strict
unique-`AC` cell whose reviewed chamber theorem asserts literal-row arcwise emptiness
through its own `T_*`, the finite-depth restriction of the identity (sound by the
chamber's reviewed polar inventory; empirically exact at the cells tested here) kills
every total DVR arc of that exact contact on the stated open locus.  This is eleven
implications with mixed theorem types, **not** one universal emptiness theorem, and it
is conditional on the `(a,d)=(8,3)` narrow promotion (or an explicit conditional label)
for full-fan coverage.

**Remaining finite obligations** (nothing else): the six layer-2 items of §4 —
schema freeze with (1.1) normative, recorded compiler-agreement lemmas, per-manifest
primitive comparison, generated renaming maps, the frozen V0–V4 verifier with one
hostile review, and the `(8,3)` promotion/label.  Plus the standing chamber-level
authorities themselves, which this interface consumes and does not re-prove.

**Serial exporters.**  The candidate's central economic claim is CONFIRMED: serial
general-`rho` actual-total exporters at grades 22, 24, … are layer-3 byte
reconstructions of polynomials that (1.1)+(1.5) already define and equate; they are
not mathematical proof obligations, and `ACT-TOT-G20`'s framing as a "missing
transport lemma" is superseded in its mathematical reading (its custody discipline —
never relabel `rho=0` face bytes as general-`rho` rows — survives and is carried into
the mutation controls).  They may be removed from the critical path **once the schema
and V0–V4 verifier are frozen and independently reviewed**; until then the transport
remains, as the candidate itself labels it, a provisional source-transport theorem.
The completed grade-20 defense run (`v44r3`) stays banked as defense in depth; nothing
here re-validates its producer PASS labels.

**Not promoted here, and not concluded here:** any generic-square cover, the ramified
fibre `rho=0`, equality faces, positive-order loads, `V(k)`, the six Rees charts, the
terminal/Taylor receiver, either `G2` obligation, Gate T, order two, maximum twelve,
JC2, or any counterexample.

## 11. Execution record

Desk-scale only: pure-Python exact `Fraction` and mod-`p` truncated-series checks
(throwaway harness under `/tmp`, ≈15 s total; two harness bugs of mine — a pair-sign
/deck-branch mixup and an `ell`-index off-by-one — were found and fixed during the
session; both were defects of my harness, not of the candidate).  No AWS, no heavy CAS,
no web sweep, no canonical-ledger edit, no entry into `jc2-lean`, and no campaign
artifact touched other than writing this file.  Only `tails.json` bytes were consumed
by the executable checks; compiler semantics were taken from byte reads quoted in §1.

**CONFIRMED (provisional source-transport theorem; two repairable wording items;
promotion withheld pending schema + verifier freeze and their independent review).**
