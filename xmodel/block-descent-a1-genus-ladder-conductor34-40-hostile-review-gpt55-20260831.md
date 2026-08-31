# Hostile review: conductor 30--40 genus-ladder S4 census

Reviewer: GPT-5.5 hostile referee  
Date: 2026-08-31

## Hash gate

Verdict: CONFIRMED.

I reproduced the six required SHA-256 hashes from the frozen lane copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.sDefQR/inputs`
before doing any review work. They match the assignment exactly.

## Frozen replay modes

Verdict: CONFIRMED.

I ran the frozen `block_descent_a1_genus_ladder_c34_c40_s4_replay.py`
directly from the lane input directory with `PYTHONDONTWRITEBYTECODE=1`.
Normal `python3`, `python3 -O`, and `python3 -OO` all emitted stdout with
SHA-256
`60c044ac2bc4d83f413e62212f031b9dd4fdeba874189efe22143cddcd869dbc`.
This confirms the advertised byte-stability of the JSON payload under
optimized modes.

## Mutation gates

Verdict: CONFIRMED.

All four advertised mutations exited nonzero at their stated gates:

- `--mutate-drop-freeness`: `RuntimeError: published conductor-14 example reproduced`.
- `--mutate-framing`: `RuntimeError: winding-two compiler specialization`.
- `--mutate-quotient`: `RuntimeError: four complement lifts exist`.
- `--mutate-promote-exclusion`: `RuntimeError: false 10+6k complete-exclusion at 34 and 40`.

The last mutation is the strategic control: after counts are computed, the
attempt to assert complete exclusion at conductors `34` and `40` fails
because positive full-`S4` rows are present.

## Recursive Census

Verdict: CONFIRMED.

I reimplemented the finite Assi--Garcia-Sanchez recursion in a short
standalone Python desk check, without importing either replay module.  The
independent list agrees exactly with the frozen `EXPECTED_CENSUSES` for all
six targets, with no missing or extra rows:

```text
C=30: 28 rows, max r1=18, max length 5
C=32: 29 rows, max r1=22, max length 4
C=34: 13 rows, max r1=14, max length 4
C=36: 26 rows, max r1=16, max length 5
C=38: 41 rows, max r1=26, max length 5
C=40: 15 rows, max r1=12, max length 4
```

The total is `152`.  Every independently enumerated row satisfies
primitive gcd, reducedness `r0 > r1 > d2 > ... > 1`, freeness
`e_k r_k in <r0,...,r_(k-1)>`, strict product ordering, and reconstructs
its target conductor.

The one-stage factorisation control also agrees: conductor `34` has only
`(35,2)`, while conductor `40` has exactly `(11,5)` and `(41,2)`.  For the
headline conductor-34 survivor `(12,8,14,15)`, the desk arithmetic gives
`gcds=(12,4,2,1)`, `e=(3,2,2)`, ordering products
`96>56>30`, freeness values `24 in <12>`, `28 in <12,8>`,
`30 in <12,8,14>`, and conductor `34`.

## Cabling Compiler

Verdict: CONFIRMED.

The frozen compiler implements the signed recursive dictionary
`K(R)=C_(w,r_h)(K(R'))`, where `w=gcd(r0,...,r_(h-1))`, and the actual braid
word is reconstructed as
`Cab_w(beta) delta_w^(q - w e(beta))`.  I spot-reconstructed every sign
variant of the high-risk rows `(24,16,12,6,3)`, `(24,16,12,6,9)`,
`(27,18,6,4)`, `(27,18,6,8)`, `(20,8,9)`, `(12,8,14,15)`,
`(12,8,14,21)`, and `(20,8,18,9)`.  In each case the rebuilt word matched
`compile_delta_sequence`, closed to one component, and had the recursive
Burau-at-`-1` Alexander determinant.

The test hits exactly the places where a framing error would hide.  For the
positive sign convention, the depth-three `1512` row `(24,16,12,6,3)` uses
successive correction exponents `-3`, `-15`, `-39`; the corresponding
`(24,16,12,6,9)` row uses outer correction `-33`.  The winding-three `936`
rows have inner correction `-7` and outer corrections `-35` for
`(27,18,6,4)` and `-31` for `(27,18,6,8)`.  The winding-four conductor-40
survivor `(20,8,9)` uses correction `-11`.  These are all of the form
`q-w e(beta)`, not raw `q`.

I also re-ran the packet's full Laurent Alexander controls: all signs of
`T(3,16)` and `T(4,11)`, and the positive winding-four survivor
`C_(4,9)(T(2,5))`, agreed up to Laurent units with the recursive satellite
formula.

## Colouring Counts

Verdict: CONFIRMED.

I spot-recomputed the `V4 -> S4 -> S3` counts at the requested attack
points.  The conductor-34 survivor `(12,8,14,15)` has `72` labelled full
`S4` colourings by the older direct `6^(n-1)` Hurwitz enumeration, agreeing
with the lift count `fox total=9`, `nonconstant lifts=96`, `full=72`.
The three conductor-40 survivors are also only eight-strand braids, so I
directly enumerated them too: `(12,8,14,21)` has `72`, `(20,8,9)` has `24`,
and `(20,8,18,9)` has `72`, matching the lift solver.

For a zero row killed at the quotient, `(8,6,23)` has only the three
constant Fox colourings: `fox total=3`, `nonconstant lifts=0`, `full=0`;
direct enumeration also gives `0`.  For a complement-only row, `(15,10,7)`
has `fox total=9`, `nonconstant lifts=24`, and `full=0`, i.e. four
non-full complement lifts for each of the six nonconstant quotient
colourings.  For a high-count row, `(24,16,12,6,3)` was group-validated
with `fox total=9`, `nonconstant lifts=1536`, and `full=1512`.

The warning about the winding-two residue theorem is necessary.  The row
`(10,4,9)=C_(2,9)(T(2,5))` is zero despite nonconstant Fox colourings, while
the further satellite `(20,8,18,9)=C_(2,9)(C_(2,9)(T(2,5)))` has `72`
full `S4` colourings.  Thus the parent theorem for `C_(2,q)(T(2,n))` cannot
be applied to an outer cable whose companion is already a satellite.

## Scope

Verdict: CONFIRMED, with GAPs exactly as stated below.

The weakest hypotheses actually used are: `B` is reduced, irreducible,
one-place at infinity, and `normalization(B)=A1`; the charged affine group
has a transitive `S4` representation sending positive generic meridians to
transpositions; the promoted parent interfaces provide
`g_3(K_infinity)=Delta_aff(B)`, the reduced plane-embedding delta-sequence
to iterated-cable dictionary, and the meridian-preserving epimorphism from
the infinity-knot group to the affine complement group.  The computation
then concerns only even conductors `30,32,34,36,38,40`.

The packet's consequence (0.1) is scoped correctly.  Zero-count rows are
row-level obstructions to carrying the charged quartic boundary
representation.  Positive counts prove compatibility of the compiled
infinity knot with a full-`S4` transposition colouring; they do not prove an
affine curve exists, do not prove a delta-sequence is attained by an
embedding, and do not assert a `FULL_ACTUAL_EXIT`.  Odd conductors are
untouched, and there is no extrapolation past conductor `40`.

Correction: the Grok prose still says the two parent packets are
`PROVISIONAL` and cites the producer lane path `jc2-lane.3TUzlG`.  In this
review I used the assignment's promoted-parent instruction and the frozen
copies in `jc2-lane.sDefQR`.  This is a provenance/status correction only:
the hashes match the charged bytes, so it has no numerical blast radius.

Residual GAPs: curve existence for any survivor row, realisability of each
abstract reduced delta sequence by a plane embedding in the charged class,
odd conductors, and all conductors greater than `40`.

## Per-Claim Verdicts

| claim | verdict | hostile attack |
|---|---|---|
| Frozen input identity | CONFIRMED | Recomputed all six SHA-256 hashes before writing the report. |
| Complete six-conductor census, 152 rows | CONFIRMED | Independent recursion found exactly the frozen lists and validated all reduced axioms. |
| One-stage rows at `34` and `40` | CONFIRMED | Direct factorisation gives only `(35,2)` and exactly `(11,5),(41,2)`. |
| `(12,8,14,15)` arithmetic | CONFIRMED | Gcds, freeness, ordering, and conductor recomputed by hand/desk arithmetic. |
| Signed nested cabling and zero framing | CONFIRMED | Rebuilt high-risk signed words using `q-w e(beta)` and checked closures plus Alexander determinants. |
| Burau/Alexander controls | CONFIRMED | Re-ran full Laurent controls for `T(3,16)`, `T(4,11)`, and `C_(4,9)(T(2,5))`. |
| `V4 -> S4 -> S3` counts | CONFIRMED | Directly enumerated the four headline eight-strand survivors; separately checked S3-death, complement-only, and `1512` high-count rows. |
| Headline: `Delta_aff=17,20` not excluded | CONFIRMED | Conductors `34` and `40` have full-`S4`-colourable rows with counts `72` and `72,24,72`. |
| Positive count implies curve existence | GAP | The packet does not claim this; no attainment theorem or witness curve is supplied. |
| Apply winding-two residue theorem to satellite companions | REFUTED | `(10,4,9)` is zero but its further satellite `(20,8,18,9)` has `72`; monotone residue-kill reasoning would be wrong. |
| Extrapolate `C=10+6k` past `40` | GAP | The packet refuses extrapolation; no later conductor was computed. |

Best next falsification test: extract explicit colouring certificates for
the four survivor rows and the complement-only rows, in a format checked by
a tiny verifier that does not import the replay modules.  The most valuable
certificate would list a Fox quotient, an affine lift, the resulting
transpositions on braid meridians, closure under the Artin action, and the
generated subgroup order.  That would make the surviving-row claims
auditable without trusting either compiler's linear-algebra implementation.

<!-- BODY-END -->
