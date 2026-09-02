# Synthesis — full ideation round 20260902T0022Z

Coordinator: Fable 5. Packet df7df824 (frozen 00:22Z, basis
f6a4591d). Four blind equal-standing submissions, all sealed,
all delivered the full contract:

```text
2ad20b4c  ideation-20260902T0022Z-fable5.md   (22.0KB)
83319c5e  ideation-20260902T0022Z-grok46.md   (19.9KB)
dcd40a42  ideation-20260902T0022Z-opus5.md    (31.2KB)
4b0e4dde  ideation-20260902T0022Z-sol56.md    (17.1KB)
```

Round quality: NOT degraded — four/four submissions, high novelty,
low duplication. Cross-pollination is folded into this synthesis
and the SOURCE-GATE merge lane below (the three retype mechanisms
compose rather than compete). Coalescing: the mu2 review
CONFIRMED landed post-freeze and is treated as the expected echo
of the packet's PROVISIONAL flag (promotion harvested as a
micro-round in the 00:43Z LIVE STATE; no round restart).

## 1. Headline convergence — SOURCE-IS-C2 retyped, three composable razors

Opus, Sol, and Grok independently found that
OPEN[REP-96-SOURCE-IS-C2] as written ("Y ~ C^2") targets the
wrong object, and each supplied a different finite necessary
condition on the corrected object. Fable independently flagged
the same gap as jointly owned with primitive monodromy. The
corrected statement (Grok's is sharpest, consistent with all
three): SHEET-GATE Y = Spec B is NEVER C^2 (Lemma 2.2, B_Y
nonempty); the right question is whether the Riemann-existence
cover admits a Zariski-open U ~ A^2 with curve complement and
SHEET-GATE-matching four-box numbers. The three razors stack on
one input (the banked SIROCCO output + a representation):

- HOM-COVER (opus §3, instrument box/cover_h1.py DELIVERED,
  4/4 controls incl. the trefoil Z+Z/3): H_1(C^2\E) = Z^r free —
  torsion in H^ab kills; rank must equal component count.
  MEASURED 56% kill rate on the B_3->S_4 analogue census.
- FOUR-BOX EULER (grok §3/Card I): chi_c(Y)_RH vs 1 + chi_c(B_Y),
  computed from conjugacy-invariant cycle types (immune to
  OPEN[BMFACT-STRAND-VS-BLOCK]); Mode 1 (irreducible) runnable
  NOW on (9,6,2); Mode 2 waits on Path-2's D_2 type.
- BOUNDARY LATTICE (sol §4): construct the declared U = Y - B_Y,
  compactify, and test det L-tilde-infinity <= 0 (DET-LINF,
  banked unconditional); forced positive determinant kills.

DEDUP: three mechanisms, one target, zero overlap in method
(homology torsion / Euler arithmetic / lattice sign). Labels:
all NEW to the ledger; method families KNOWN externally
(Fox/Reidemeister-Schreier; branched-cover Euler; Hodge-index
trees). Retype adopted: OPEN[REP-96-SOURCE-IS-C2] is SUPERSEDED
by OPEN[SOURCE-OPEN-U] (= does U ~ A^2 exist inside the cover,
with typed boundary), which the three razors gate. Opus's typed
caution OPEN[ACS-FIX-VS-DEFICIT] (a^(i) <= #Fix, equality a
hypothesis; at N=4 the companion meridian is forced IDENTITY —
no 3-fixed-point element of S_4) is ADOPTED and must be carried
by both flagships.

## 2. Second headline — (9,6,4) is realized six-nodal (pending review)

Sol §6 (EXACT-DESK/UNREVIEWED): the HF-twin curve has exactly six
ordinary nodes (u=0 quartic gives the four banked; u!=0 forces
v=-11/8, u^2=-35/8, two further transverse nodes, distinct
images; delta_aff=6 exhausted by immersivity). If confirmed, the
N=4 residual has TWO realized substrates and job 964's outcome is
pre-empted (the locus question becomes moot; the braid question
opens). Predicted SIROCCO census for 964: eight simple
tangencies + one four-node fibre + two one-node fibres, ledger
8 + 2(4+1+1) = 20. Review lane launched (below); on CONFIRM,
bmfact_964 codegen per Sol §7 (quotient by simultaneous S_4
conjugacy, certify by full native universe, both orientations).

## 3. Companion front (Path-2) — three injections banked for harvest

Path-2 flagship is running and must NOT be touched mid-flight.
On landing, its r2/continuation charge receives:
(a) deg D_2 >= 3 (sol §4: conic impossible via Gate SELF/EMB —
    smooth conic embeds A^1; at deg 3: exactly one node + smooth
    infinity point; explicit control y^2 = x^2(x+1) ATTAINS the
    collapsed (M') identity -> Euler data alone provably cannot
    kill the companion; redesign toward common-infinity /
    intersection / source-boundary constraints);
(b) the identity-meridian consequence (opus §4): F^{-1}(D_2) ->
    D_2 is an unbranched a^(2)-sheeted cover; its component count
    is exactly what HOM-COVER's RANK test consumes — the
    source-side handle the target-side charge lacks;
(c) BURNSIDE-CHI (fable §3, NEW): the full subgroup-lattice
    chi_c system (11 rows of S_4 vs the natural-action pair);
    cheapest discriminator = the 11-row table at the pinned N=4
    profile with (chi_2, sigma_2, j) unknowns. Either the first
    new all-N identity family since (M'), or a permanent closure
    of the more-Euler-identities direction. Launched as its own
    desk lane (below) so Path-2 can consume the outcome.

## 4. Highest single-shot item — Card C: solve for F directly

Opus §6/Card C: encode J(F)=1 + the two prescribed dicritical
germ conditions ((9,6,2) as the W_1=2 image; W_2=1 companion) as
a QQ[coeffs] ideal; EMPTY kills (9,6,2) at the strongest level,
NONEMPTY is a counterexample candidate. BLOCKED on desk step-0:
pin deg f, deg g from td=4, W=(1,2), the (9,6) place. Risk typed:
if step-0 fails to pin, this degrades to the banked-tried GGV
degree farm and must be re-costed, not run. Step-0 launched as an
Opus desk lane (below). SCOPE-CONFLICT label carried.

## 5. N=5 — sound-frontier redesign (no suite clone)

Convergent (4/4 raise). Merged design from grok Card III + fable
§4(d) + sol cautions: (0) soundness first — DET-LINF vs Zoladek
Lemma 4.10 (is det<=0 the unsupported inclusion?), Sigray 9.1
replay at geometric degree 5, BEFORE census compute; (1) free
screen: the only primitive subgroup of S_5 containing a
transposition is S_5, and prime N forces primitivity — the
S_5-representation space collapses; (2) census-level fixed-tuple
/ Hurwitz screens BEFORE any curve realization (the (9,6,2)
lesson: the census-derived pins were realization-free); (3) never
transfer S_4 rep kills; curve-level facts only; (4) faithfulness
preflight mandatory (see §7). One Grok lane launched on (0)+(1).

## 6. Cheap decisive extras launched

- HOM-COVER discriminator on the constrained N=4 cabled place
  (opus Card B's gate): does EVERY campaign-constrained rep at
  the (9,6,2) place carry torsion? YES -> fund the all-degree
  transfer lemma (candidate JC2-at-every-degree obstruction);
  NO -> permanent scope limit, razor stays a filter. (Grok,
  delivered script.)
- DOMRINA-INSTANTIATE (fable Card C): desk-walk the repaired
  Domrina II chain on the campaign's own residual (D_1 =
  (9,6,2) + forced companion). Kill / package-localization /
  genuine-tension trichotomy; third branch escalates to DC
  immediately. (Sol.)
- N-A sharpness at equality (grok Card II): YES kills (9,6,4) +
  downstairs rows without Box03. (Grok.)

## 7. Systems (one tracked upgrade + one free adoption)

- ADOPTED FREE (opus §8, instrument delivered): OPEN-token triage
  at every round close. MEASURED now: 74 raised / 20 charged /
  54 orphaned. This synthesis charges or retires five orphans:
  OPEN[SOURCE-IS-C2] superseded by OPEN[SOURCE-OPEN-U] (charged
  to SOURCE-GATE lane); OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]
  charged (Card II lane); OPEN[SHAPE-2-INNER-g>=3] RETIRED
  (closed by CABLE-3); OPEN[BMFACT-STRAND-VS-BLOCK] charged
  (SAGE-NATIVE running + SOURCE-GATE consumes cycle types only);
  OPEN[A2-CELL-32] already owned (horn lane).
- ONE TRACKED UPGRADE (grok §7, chosen over fable's
  FAIL-CLOSED-LINT and sol's SNAPSHOT-READSET as
  highest-value/lowest-risk): encoding-faithfulness PREFLIGHT as
  a required gate on every nodal-type Groebner job — emit the
  reduced approximate root beside the .ms, diff against the raw
  binomial, refuse on nonempty diff; positive control = (9,6,2)
  corrected, negative control = the Delta=(8,6,19) false
  positive. Queued to the qqideal oracle harvest (P1 disagreement
  machinery already exists). FAIL-CLOSED-LINT and
  SNAPSHOT-READSET are RECORDED as next-window candidates, not
  lost; sol's canary test design is banked in its submission.

## 8. Launch table (this synthesis)

| lane | seat | charge |
|---|---|---|
| source-gate-962 (merge: retype + 3 razors, Mode 1 on (9,6,2)) | opus (#3/5) | opus+grok+sol submissions, rep-96, sheet-gate |
| card-c-step0 (pin degrees for the direct F solve) | opus (#4/5) | opus submission, rep-96, cage r2 |
| 964-nodality-review (gate sol §6) | grok | sol submission, HF-twin |
| homcover-discriminator (constrained reps at the cabled place) | grok | opus submission (script), rep-96 |
| n5-soundness (DET-LINF vs 4.10; Sigray 9.1; primitive screen) | grok | grok submission, GGV, sigray, zoladek custody |
| na-sharpness (Card II) | grok | grok submission, N-A packet, rep-96 |
| domrina-instantiate (fable Card C) | sol | fable submission, gap-repair, rep-96 |
| burnside-chi discriminator (11-row table at the N=4 profile) | sol (after domrina-instantiate) or gpt55 | fable submission, rep-96, cage r2 |

Running lanes: MPRIME-ALLN-H2 and COMPANION-CURVE-ALLN
CONTINUE untouched (injections at harvest, per §3 and
OPEN[ACS-FIX-VS-DEFICIT]); SAGE-NATIVE, 869, oracle window,
box01 provisioning CONTINUE. Deferred, does not block: N=5
census compute (behind n5-soundness), bmfact_964 (behind the
nodality review), Mode-2 Euler (behind Path-2's D_2 type).

## 9. Dedup and history-checksum record

Fingerprints (target obstruction x mechanism x object x test):
no operational duplicates across the four submissions. The three
SOURCE-IS-C2 retypes share the target but differ in mechanism
and were merged, preserving three independent votes that the old
typing was wrong. BURNSIDE-CHI vs (M')-family: fable's own
novelty check (zero corpus hits for Burnside/table-of-marks)
spot-confirmed. Opus's HOM-COVER vs KEF-ONE-VERTEX: correctly
distinguished in-submission. Grok's Chern-species connection
((8,6,9) c_2(T) and (9,6,2) chi_c(Y) are one calculator) is
ADOPTED into the source-gate lane's §6 spec. Sol's Y-label
caution and grok's SHEET-GATE citation agree; no scope conflict.
Card C carries its SCOPE-CONFLICT label (GGV farm) explicitly.
No submission contradicts a banked exact result; no stale-packet
correlated error identified (the one post-freeze event, the mu2
review, only confirmed the packet's stated PROVISIONAL flag).
