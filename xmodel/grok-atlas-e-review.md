# Hostile review: 8.S8 36-fiber D23 atlas + 8.S7 corrected e

Reviewer: Grok 4.6 (hostile referee, promotion tier). Date: 2026-08-19.
Scope: two linked INTERNAL / UNREVIEWED objects.

- (A) SHEET6-DIRECTIONB.md §8.S8 + `cases/d23_atlas_p105337.json` +
  box01 `~/jc72108/atlas/` + `pilot.log` ATLAS markers.
  Claim: at p = 105337 the depth-23 obstruction eliminates NO radical
  fiber; 36/36 NONEMPTY with identical structure.
- (B) SHEET6-DIRECTIONB.md §8.S7 + `cases/valuation_e2.py` +
  `cases/d23_ecandidates.json`.
  Claim: E_CANDIDATE e = 295, 0/36 ≤ 11, stop-rule certified at all
  blocks.

Method: independent python3 reparse of both JSONs; md5 census of
every box01 fiber/det GB; monomial-support identity on the banked
a00pp GBs and on three remote fibers; exact F_p LT-staircase
dimension; replay of `valuation_e2.py --selftest`, `--point 105337 0 0`,
the fail-closed point w1/k0, and G2d at both primes; independent
30-output delayed-loss and 30×30 defect (the attack the 29-output
spec cannot answer for itself). No Singular, no msolve rerun, no
other repo file modified, no git.

The two "36"s are different objects. Atlas 36 = 3×3×2×2 radical
fibers of the D21 window at one prime. e-comp 36 = 6 a00pp witnesses
× 3 deep-kernel draws × 2 primes. Do not add them.

---

## Verdicts

### Object A — 36-fiber D23 atlas

**CONFIRMED at single-prime computational tier; GAPS for promotion
and for the second prime. Not REFUTED.**

The load-bearing sentence at `SHEET6-DIRECTIONB.md:1834-1841` survives
as a statement about p = 105337, this chart, these 36 F_p-fibers:
every fiber GB is a proper 397-element ideal, every det23 GB is a
proper 509-element ideal, and V(det23) is therefore nonempty over
the algebraic closure of F_105337. The copy-one-GB attack is dead:
35+1 content hashes are pairwise distinct, the 35 remote msolve
lanes were real, and a00pp reproduces the banked artifacts
byte-for-byte. Support identity is real (monomial-for-monomial on
every fiber I opened). The GB ≠ [1] ⇒ nonempty inference is the
affine Nullstellensatz, same as 8.S5.

What this does **not** earn, and 8.S8's scope box already withholds:
characteristic 0, a family-scheme theorem, F_p-rational points off
a00pp, D25, or a germ. The p105673 "vacuous spot-checks" are not a
second-prime atlas. Rate that gap **HIGH for promotion**, medium
as a bad-reduction residual on 35 fibers that already share the
3-prime a00pp staircase.

**Tier deserved: INTERNAL / single-prime computational atlas.
Not a promotion. Not a char-0 theorem.** 8.S8's own banner is
correct. notes.md 10:15Z "ATLAS COMPLETE: 36/36 NONEMPTY
(single-prime, internal)" is the right headline.

### Object B — corrected Euler/Ore e

**CONFIRMED as E_CANDIDATE diagnostics of the commissioned 29×29
object; the stop-rule conclusion SURVIVES the 30-output repair
(recomputed, stronger); e = 295 is not a DEPTH e and the number
itself does not survive a 30×30 redesign. GAPS on the char-0
eta29 rational (mod-p checked, exact rebuild not rerun) and on
everything E-HENSEL already withholds.**

The eta29 lemma of sol-round5 §1.2 is REFUTED, as claimed: E_29 is
supported at t^36 on the six residue-4 columns. That kills the
29-output premise and the index formula (V) as a theorem. It does
not kill the campaign stop. Independent 30-output coverage on the
replayed p105337 w0/k0 operator gives ell = 31 > 11 with all 30
inputs and ell = 31 > 11 on every 29-input block; the extra output
deepens the deficit. 0/36 ≤ 11 remains true on the object that was
run, and remains true on the repaired object at the one point I
rebuilt.

**Tier deserved: E_CANDIDATE (EXPERIMENTAL) only. No DEPTH e. No
germ. No promotion.** 8.S7's own banner and BLOCKNOTE are correct.
The notes.md 10:00Z reading "no near-term germ" is an earned
campaign diagnostic, not a theorem.

### Combined reading (notes.md 10:15Z)

"Family-wide D23 survival + e = 295 ultra-degeneracy = survival
everywhere, certifiability nowhere" is the right INTERNAL
summary, with two corrections of language: "everywhere" means the
36 F_p-fibers at p = 105337, and "e = 295" is an unpromoted
29-output index, not a DEPTH. D25 is still the discriminating
computation. Neither object upgrades the other's tier.

---

## Object A — attack surface

### A1. Did each fiber get its own GB, or a copy?

**Own GBs. The copy attack is closed.**

| object | unique hashes | source |
|---|---|---|
| `fiber_ms_md5` (folded CORE2 input) | 36/36 | atlas JSON |
| `det_ms_md5` (det23 input) | 35/35 (a00pp omitted; uses banked file) | atlas JSON |
| `det_out_md5` (det23 GB) | 36/36; 35/35 match box01 byte-for-byte; a00pp = banked `directionb_det23_gb_p105337.out.txt` | JSON + ssh md5 |
| fiber GB `.out` on box01 | 35/35 distinct md5, sizes 10 532 763–10 533 322 | box01 `atlas/fib_*.out` |
| det23 GB `.out` on box01 | 35/35 distinct md5, sizes 15 177 063–15 178 519 | box01 `atlas/det_*.out` |
| operator / zc hashes in the e-JSON | n/a (different 36) | — |

box01 `pilot.log`: `LAUNCH ATLAS FIBGB x35` 08:51Z, 35 `ATLAS FIBGB
a…: rc=0` lines, 3 lane-DONE lines; `LAUNCH ATLAS DET23 x35` 09:10Z,
35 `ATLAS DET23 a…: rc=0` lines, 3 lane-DONE lines. Lane scripts
are sequential `timeout 1800 msolve -g 2 -t 4 -f fib_<lab>_p105337.ms
-o fib_<lab>_p105337.out` (and the det analogue) on distinct files.
First polynomial of the 35 fiber GBs takes 3 coefficient classes,
not 1: a copied a00pp prefix would have given one class.

a00pp was correctly **not** re-solved on box01 (35 = 36 − 1). Its
`fiber_ms_md5 = 7f6fa9ebdf43bdc516a8e16641cb5b65` equals banked
`cases/directionb_core2_fiber_p105337.ms`. Its `det_out_md5 =
0e4b9e58f6f1765faa85a52be3f71439` equals banked
`cases/directionb_det23_gb_p105337.out.txt`.

### A2. Support-identity claim vs distinct systems

**Both true, and not in tension.** Distinct coefficient
specializations, one monomial skeleton.

Reparsed (coeff-stripped, printed order) the banked a00pp fiber GB
and det23 GB, and the remote `fib/det_{a00mm,a11pm,a22pp}` files:

| class | n els | n `coeff*monomial` terms | sha256/16 of monomial tuples |
|---|---|---|---|
| D21 fiber, a00pp banked + 3 remote | 397 | 282 302 | `ff740f68e20a33af` |
| det23, a00pp banked + 3 remote + p105673 + p200257 | 509 | 405 522 | `36c5c7f24041366a` |

Supports are equal element-for-element across those fibers and
across the three a00pp primes. The claimed atlas fingerprints
`a9498f3c39e50803` / `e2c2e64ef0014d15` were **not reproduced**
by any hash convention I tried (repr of monomial tuples, sorted
multisets, LT lists, concatenated bodies). The JSON's own
`lt_multiset_hash` values `612b24a377a04ebb` / `3194e4b59ce00605`
are a third convention. Identity stands; that particular
sha256/16 is a scratchpad fingerprint not recoverable from the
banked files. Rate as a provenance nit, not a math hole.

Term-count off-by-2 vs 8.S8 (282 304 / 405 524): the two saturation
binomials `W_i uW_i + (p−1)` contribute a constant term my
`digit*monomial` lexer drops. Same nit as grok-det23-review §4.
Including those constants recovers the sheet.

### A3. radical_point regression

**CONFIRMED, byte-level on the objects that exist in-repo.**

- a00pp fiber coordinates = `valuation_e.radical_env(105337)`:
  A1 = 50630, A2 = 10114, HW_i/W_i = h32 = 50267. Cube-root orbits
  of A1, A2 recover the other 8 A-values; −h32 = 55070 recovers
  the sign pair. 36/36 coordinate 4-tuples distinct.
  `2 h32² ≡ 3`, `A1³ ≡ 3+r3`, `A2³ ≡ 3−r3` (r3 = 795).
- a00pp `g_rows` are coefficient-exact against
  `cases/directionb_det23_p105337.rows.txt`.
- a00pp `w_vectors` are coefficient-exact against the same file.
- Square piece is `(x57−x65)²` with integral `(1, −2, 1)`:
  `105335 = p−2` at every fiber.
- JSON omits `det_ms_md5` on a00pp only. They used the banked
  emission rather than re-emitting. The three added rows are the
  banked g's; the 397-prefix identity was already the 8.S5
  perimeter. Not a silent swap.

### A4. Vacuous p105673 spot-checks — severity

**GAPS. HIGH for promotion. MEDIUM as a residual on an honestly
scoped INTERNAL claim. The word "vacuous" is process-correct and
mathematically empty.**

What 8.S8 actually did at p105673: built stage-1 / stage-3 banks
and passed the a00pp fiber-emission / compat / row22red
regressions. What it did **not** do: fold, NF, or msolve any of
the other 35 fibers at a second prime. The pre-registered trigger
("spot-check if an EMPTY or anomalous fiber arises") never fired
because only one prime was run. That is a skipped check, not a
passed check.

Why this is not immediately fatal for NONEMPTY, and why it is
still not promotion:

- For an ideal I defined over a number field, I_p ≠ (1) at one
  prime of good reduction implies I ≠ (1). So a single good-prime
  NONEMPTY is evidence of a Qbar-nonempty fiber, not a "lucky
  nonempty".
- The real escape is **bad reduction**: a unit becoming 0 mod p
  can make a char-0 empty (or thinner) fiber look proper. The
  3-prime identical-support echo on a00pp is the standard defence.
  The other 35 share that support at p = 105337 and are Galois
  conjugates of a00pp over F_p, which is the expected picture if
  reduction is good, and is not a second prime.
- The 36 fibers are F_p-points of the radical base at a split
  prime, not 36 a-priori Q-ideals sitting in the repo. Folding
  CORE2 already reduced at p, then specializing, is the reduction
  of the geometric fiber only under a commutation that 8.S8 does
  not write down.

8.S8's scope box already says "nothing about primes other than
105337 (except the banked three-prime a00pp chain)". Keep that
sentence welded to any external use. A promotion of "the D23
obstruction eliminates no radical fiber" to a Qbar / scheme
statement without a second-prime atlas or a written reduction
lemma is an over-read.

### A5. Verdict inference GB ≠ [1]

**CONFIRMED. No unit-ideal / saturation subtlety.**

All 35 remote fiber GBs header `length of basis: 397`; all 35
remote det23 GBs header `length of basis: 509`; characteristic
105337; grevlex; 22 vars in the banked order. No file is a
1-element basis; no parsed polynomial is a bare constant. Banked
a00pp det23 GB: 509 els, 3 linear LTs `{x52, x47, x70}`, no
constant, maxdeg 16. In a polynomial ring over a field the only
units are nonzero constants, so a reduced GB other than `{1}`
means `1 ∉ I`. Affine Nullstellensatz: V(I) nonempty over
F_p-bar. Chart inverses are polynomial generators
`uW_i W_i − 1 ∈ I` (LTs `W_i uW_i` sit in the basis); a hidden
saturation unit would already force `1 ∈ I`.

I did not rerun msolve. The trust that the 509-el files are the
reduced GBs of the emitted 400-row inputs is the same perimeter
as grok-det23-review: emission g-rows match, 35 distinct
contentful outputs, support identity with the 3-prime a00pp
object, 70/70 rc=0. A catastrophic msolve bug producing 36
proper-looking bases of a unit ideal, with identical supports and
distinct coefficients, is outside what python3 closes.

### A6. Dimension, g-class structure, inherited rank-2 pin

**Dimension CONFIRMED on the banked a00pp GBs. g-class structure
CONFIRMED from the atlas JSON. Per-fiber NF → g derivation for
the other 35: ATTESTED in JSON, not independently recomputed
(payloads not in-repo).**

Exact min-hitting-set of LTs, 22-variable grevlex, banked files:

- fiber GB: height 9, dim 13. Atlas `max_indep_set` of 13 is a
  genuine independent set (no LT supported on it). So is the
  different 13-set this review found. Max independent sets are
  not unique; both certify dim 13.
- det23 GB: height 11, dim 11. Atlas 11-set
  `{x55,x58,x59,x60,x62,x63,x65,x66,x68,x71,x73}` is independent.

g-rows in the JSON organize exactly as 8.S8 claims:

- 18 / 6 / 3 distinct g1 / g2 / g3, 36 distinct triples.
- g3 = `x70 + e x72` with e ∈ `{52700, 54113, 103861}`, constant
  on (j−i) mod 3 (12 fibers each). Sum of the three e's = 2p.
  e = 52700 is the banked a00pp value.
- g2 determined by (j, s2): 6 classes of 6.
- g1 determined by (i, j, s1): 18 classes of 2.
- w3 determined by j only (3 values, 12 fibers each); w1, w2 are
  the banked a00pp vectors on every fiber (constant leftker of a
  constant C, as advertised).

Inherited, and the honest gap: the 8.S5 both-directions
equivalence "V(det23) empty iff V(row22red) empty" uses rank A = 2
on the chart, which follows from rank C = 2 plus `uW_i` units in
the GB. grok-det23-review confirmed that on a00pp at three primes.
8.S8 claims the same pin, replayed, on all 36. JSON has
`rankC = 2`, `schur_rankC10 = 4`, `cond_dim = 3`, `kernel_dim = 1`,
`nf_rank = 5` uniformly, and the g-rows have the same square /
carrier shape. I do not have the 35 non-a00pp NF payloads in the
repo, so I did not rebuild C for e.g. a11pm. The spot G-C on
`{a11pm, a20mp, a02mm, a10pp}` is claimed, not banked. Terminal
NONEMPTY (proper det23 GB) does not need that pin. The slogan
"Row_22 eliminates no fiber" in the 8.S5 sense (both directions)
does.

### A7. Findings, object A (worst first)

1. **Severity: promotion-blocker, not a math error — single prime
   on 35 fibers.** File: `SHEET6-DIRECTIONB.md:1853-1858`. The
   family sentence at :1834-1841 is easy to quote without the
   scope box. Keep "p = 105337, mod p, chart-local" in the same
   breath. A second-prime atlas, or a written good-reduction
   lemma commuting fold-at-fiber with reduction of the geometric
   fiber, is what promotion would require.
2. **Severity: consumer-hazard — per-fiber rank-2 pin not
   independently closed off a00pp.** JSON attests it; NF payloads
   are scratchpad-only. Anyone promoting the 8.S5 *equivalence*
   (not just det23-NONEMPTY) to 36 fibers owes those payloads or
   a Galois-constancy argument for C.
3. **Severity: nit — claimed support sha256/16 unreproduced.**
   Identity holds under an independent monomial parse; the
   printed `a9498f3c…` / `e2c2e64e…` are not a function of the
   banked GB files.
4. **Severity: nit — a00pp has no `det_ms_md5`.** Regression is
   still byte-closed on `fiber_ms` and `det_out` and
   coefficient-closed on g/w.

---

## Object B — attack surface

### B1. 29-vs-30 and the stop-rule

**The lemma is refuted. The stop-rule conclusion survives, and
the 30-output object is worse for the germ, not better.**

Replayed p105337 w0/k0 (`--point`, 6.7 s, operator hash
`d2bd6de58c90ebdc…` byte-identical to the JSON; zc hash
`43c2c36808643328…` identical):

- G2b WARN: E_29 support `{t^36}`, six residue-4 columns
  `{tf1,tf2,tg1,tg2,tg01,tg02}_48`. Value 0 at the witness.
- G2c PASS (confinement).
- G2d PASS at both primes: numeric
  `d(eta^29 t^36)/d(tf1_48)` at the all-zero configuration equals
  `ETA29_NUM/ETA29_DEN` reduced mod p
  (105337: 48635; 105673: 50809). This is a mod-p check of a
  claimed char-0 rational, not a rerun of
  `r1_experiment.gm_jet2 + directionb_strike.jrows` at depth 37.
  The *existence* of a nonzero E_29 at t^36 does not depend on
  that rational.

Independent coverage on the same operator, bands ≤ 40, causal
(no `n < r` entries):

| object | ell | vs 11 |
|---|---|---|
| 29 outputs, 29 inputs (spec, 30 blocks) | 24..31 | all > 11 |
| 29 outputs, all 30 inputs | 24 | > 11 |
| 30 outputs, all 30 inputs (repaired square) | **31** | > 11 |
| 30 outputs, 29 inputs (any one stream free) | **31** on all 30 | all > 11 |

Adding the extra input stream does **not** drop the 29-output
delay below 24. Adding H_29 (start 36) *raises* the delay to 31.
The extra output is a genuine extra condition in-window; it does
not get absorbed.

30×30 defects (rows with n < 42): `[25, 41, 53, 57, 57]`,
stabilized d = 57. The repaired index analogue
`6d + 276 − 288 = 6d − 12` is 330, not 295. So:

- e = 295 is a number of the *wrong* (29-output) object. It
  does not survive a 30×30 redesign.
- "no e ≤ 11" *does* survive. A delay-31 lower bound, certified
  inside the window by causality (inputs with r > 40 cannot
  reach bands ≤ 40), is already past the DEPTH-STAB threshold
  of 11. Promotion of any e ≤ 11 at these witnesses, at this
  truncation, is incompatible with the repaired operator as
  well as with the commissioned one.

8.S7's claim that "the extra output only deepens the deficit"
is confirmed by the 30-output ell, not just by
`delta_plus_eta29 = delta + 1`.

I did not rebuild the operator at the other 35 e-points for the
30-output ell. Structure gates, residual bands, eta29 support,
and 86/86 banked-row match are identical across all 36 JSON
points; the six residue-4 columns of E_29 are point-independent
within a prime (G2d / G2c). A point at which 30-output ell
dropped below 12 would have to break that uniformity. Residual,
not a hole in the w0/k0 certificate.

### B2. argmin convention

**Implemented as specified for an *unpromoted* diagnostic; not
the spec's promoted min.**

sol-round5 §1.2/1.3: among blocks that *promote*, take smallest
e_c, STREAMS order as tie-break; if none promote, report no
DEPTH e. The tool sets `depth_e_strict = None` and
`promoted: false` on every block and every point. Correct.

What it then reports as `e_candidate` is
`min { e_index_V : block consistent }`, first in STREAMS order.
Consistent = `d_c` stabilized on N = 4,5 AND `e_idx ≥ 0` AND
`ell_window ≤ e_idx`. On 27/36 points that min is 295 at
`tf1/r1` (`r_c = 7`, `d_c = 56`, `6·56 + 7 − 48 = 295`).
Recomputed on the JSON: 0 argmin mismatches. On the replayed
w0/k0 the 30 printed blocks match the JSON line-for-line.

This is a deterministic diagnostic of the 29×29 object, not the
spec's e(s). 8.S7 tags it E_CANDIDATE and says so. A consumer
who writes "e = 295" without the tag is over-reading; a consumer
who writes "no DEPTH e, and every consistent 29×29 index is
≥ 295" is reading the file.

Residue-0 streams (`r_c = 6`) are inconsistent even on the 27
"good" points (profile `(24,40,52,56,57)`). If those later
stabilized at 57, e_idx = 300 > 295; argmin would not move.

### B3. Fail-closed handling

**Correct, and conservative for the ≤ 11 claim.**

`d_c` is set only when `delta[N] == delta[N−1]`; else None, no
e_idx, block excluded from the argmin, point-level e_cand = None
if every block is excluded. 9/36 points are fully fail-closed
(w1 both primes, w3 at p105673; all 3 draws): all 30 blocks have
delta 57 → 58 (or the JSON's `(25,41,53,57,58)`), n_consistent =
0, e = None, ell still 25..31 > 11. Replayed w1/k0: operator
hash `0db222440c1b39d6…` matches the JSON, e = None, ell 25..31.

All recorded profiles are monotone nondecreasing. A fail-closed
growing defect, if it ever stabilizes, gives a *larger* e_idx,
not a smaller one. The residual is the N = 5 window: a later
drop is possible in principle and not certified impossible. It
is not suggested by any profile in the file.

Fail-closed is *not* a hidden e ≤ 11. Those 9 points still hit
the stop-rule via ell > 11.

### B4. Gate adequacy

**Adequate for an unpromoted 29-object diagnostic. Not adequate
for a DEPTH e, and they do not claim one.**

Recomputed:

| gate | result |
|---|---|
| selftest (toeplitz, dual jmul, rankp, coverage, dual derivative) | PASS |
| G2a eta^30..33 vanish | PASS (replay) |
| G2b eta29 == 0 | WARN / REFUTED, hard=False — correct |
| G2c / G2d | PASS, both primes |
| G3a odd bands, G3b congruence, G4 starts | PASS; starts = S_A |
| G5 witness rows vanish through band 22 | PASS |
| G6 86/86 banked-row match | PASS, 86 exact, 0 rescaled |
| G7 Ore affinity 2605/2605 | PASS |
| G8 zeta→zeta^5, G9 path-A | PASS on the full `--point` (not `--light`) |
| G10 band-22 deep block rank 4 | PASS |
| G11 cross-prime structure | attested in JSON (`ore_support_hash` unique, starts unique); G11c is hard=False |
| float64 exactness bound | 34·42·p² ≈ 1.6×10¹³ < 2⁵³ at both primes |

Gaps that do not flip the stop-rule:

- G1 still *asserts* 29 outputs / sum s_a = 240 after the
  refutation. Intentional spec-literal; documented. A repaired
  tool would assert 30 / 276 and run 30×30 as the primary object.
- No in-tool 30-output ell gate. This review supplied it at
  w0/k0.
- DEEP_RELABEL is measured, not derived from first principles.
  G5/G6 are the check that the banked witnesses and the 86
  window rows hold under it. That is the right gate; it is not
  a uniqueness proof of the involution.
- N = 5 stabilization window (above).
- CONJECTURE E-HENSEL unproved; no Ore-Popov / causal recurrence
  closure. Already the BLOCKNOTE. Nothing here promotes.
  DEPTH-STAB e ≤ 11 is the eventual criterion only.

### B5. Findings, object B (worst first)

1. **Severity: none on the stop-rule — 30-output repair does not
   create an e ≤ 11.** Recomputed at w0/k0. The number 295 is
   what dies; the inequality > 11 is what the campaign uses.
2. **Severity: consumer-hazard — "e = 295" is the wrong object
   after the lemma repair.** File: `SHEET6-DIRECTIONB.md:1687-1693`
   and notes.md 10:00Z. Write "unpromoted 29×29 index 295; repaired
   30×30 index analogue 330 at w0/k0; both ≫ 11".
3. **Severity: residual — char-0 eta29 rational not rerun.**
   Mod-p G2d closed. The fraction
   `−147880611647231905314470776689 / 1024` is a claimed exact
   output of the original machinery, not recomputed here. The
   *refutation* (E_29 ≠ 0) does not need it.
4. **Severity: residual — 30-output ell only rebuilt at one
   point.** Uniform eta29 / residual-band / G6 pattern in the
   JSON makes a ≤ 11 escape on another witness unlikely, not
   certified.
5. **Severity: nit — JSON billed as 3.1 MB, file is 2 291 979
   bytes.** Hash prefix `d0a52d432eee538b` matches.

---

## What this does and does not decide

Decided, at p = 105337, residue-A B-frozen no-log W1W2 ≠ 0 chart
with PIN42:

- All 36 radical fibers have a proper depth-23 det23 ideal,
  hence a nonempty V(det23) over F_p-bar, with the same staircase
  (dim 13 → 11, support identity). The obstruction does not wipe
  a fiber at this prime.
- On the a00pp witness family, at two primes, the commissioned
  29×29 Euler/Ore diagnostic and the repaired 30-output operator
  both have certified in-window delayed-loss > 11. No promoted
  e ≤ 11 exists at these witnesses at this truncation.

Still open, and both sections say so:

- Characteristic 0 of the 35 non-a00pp fibers.
- A second-prime atlas.
- F_p-rational points off a00pp.
- DEPTH e (Ore-Popov + E-HENSEL).
- D25.
- A formal germ. NONEMPTY is not a germ. e ≫ 11 is evidence
  *against* a near-term germ, not a proof that the locus is a
  mirage.

---

## Recomputation ledger (this review)

- Parsed `cases/d23_atlas_p105337.json` (sha256
  `9c029b8cff87beb7…`, 87 468 bytes) and
  `cases/d23_ecandidates.json` (sha256 `d0a52d432eee538b…`,
  matches the sheet prefix).
- ssh box01: `pilot.log` ATLAS markers; md5 of 35 fib + 35 det
  GBs; header census 397/509; monomial-support parse of
  `{a00mm, a11pm, a22pp}` at both tiers; lane script read.
- md5 of banked `directionb_core2_fiber_p105337.ms`,
  `directionb_det23_gb_p105337.out.txt`,
  `directionb_det23_p105337.ms` against a00pp JSON.
- Independent msolve-GB parse of banked fiber + det23 GBs at
  three primes: n els, LTs, term counts, support hashes,
  min-hitting dimension, max-indep verification of the atlas
  sets.
- `radical_env(105337)` vs a00pp coordinates; cube-root / ±h32
  orbit; (1,−2,1) square; g-class tables.
- `valuation_e2.py --selftest`; `--point 105337 0 0`; fail-closed
  `--point` equivalent at w1/k0; `zero_config_crosscheck` at
  both primes.
- Independent 29- and 30-output `Colspace` coverage and 30×30 /
  29×30 defects on the replayed w0/k0 operator.
- JSON-internal checks: argmin, stop-rule boolean, e_idx formula
  `6 d_c + r_c − 48`, consistent-flag definition, distribution
  `{295: 27, None: 9}`, 1080/1080 `stopped_gt11`, ell ≥ 24,
  36 distinct operator hashes, 36 distinct zc hashes, witness-file
  sha256s.

Not done: msolve rerun; Singular NF of the 35 non-a00pp fibers;
char-0 gm_jet2/jrows at depth 37; 30-output ell at the other 35
e-points; any D25 work.

---

## Tier table

| claim | verdict | tier it deserves |
|---|---|---|
| A. 36/36 det23 NONEMPTY at p=105337 | CONFIRMED | INTERNAL, single-prime computational |
| A. identical structure / support identity | CONFIRMED (fingerprint nit) | same |
| A. own GB per fiber, not a copy | CONFIRMED | same |
| A. a00pp regression vs banked 8.S5 | CONFIRMED | same |
| A. GB ≠ [1] ⇒ V nonempty over F_p-bar | CONFIRMED | same (Nullstellensatz) |
| A. Row_22 eliminates no fiber, 8.S5 both-directions, all 36 | CONFIRMED on a00pp; ATTESTED on 35 | INTERNAL; promotion needs NF payloads or a pin lemma |
| A. same statement over Qbar / as a scheme | GAPS | not earned |
| A. p105673 vacuous spot-checks as a second prime | GAPS | not earned; HIGH for promotion |
| B. eta29 ≡ 0 lemma | REFUTED (as claimed) | the refutation is earned mod p; char-0 rational residual |
| B. E_CANDIDATE e=295 on 27/36, fail-closed 9 | CONFIRMED as 29×29 diagnostic | E_CANDIDATE only |
| B. 0/36 ≤ 11 on the 29×29 object | CONFIRMED | E_CANDIDATE only |
| B. stop-rule at all 1080 blocks (29×29) | CONFIRMED | E_CANDIDATE only |
| B. stop-rule survives 30-output repair | CONFIRMED at w0/k0; residual on the other 35 e-points | E_CANDIDATE only |
| B. e=295 as a DEPTH / as the 30×30 index | REFUTED as a number; they do not promote it | no DEPTH e exists here |
| B. E-HENSEL / germ / DEPTH-STAB theorem | GAPS (already disclaimed) | not earned |
| Combined "survival everywhere, certifiability nowhere" | CONFIRMED as INTERNAL campaign reading | INTERNAL; D25 still decides |
