# FULL2110 Fable5.1 adversarial cross-review — swarmHQ ideation

report: xmodel/ideation-swarmHQ-fable5-cross-20260914T2110Z.md
author: swarmHQ Fable5.1 independent cross-reviewer (claude-fable-5-1), independent of the Astra producer
stage: cross-review after completed blind collection; stage basis 748d8973 (packet basis 441fe861)
evidence: MANUAL; lifecycle UNPROMOTED; no theorem promotion; no charge_basis line; no exit-price claim
status: COMPLETE; skeleton first, bounded sections by apply_patch, BODY-END appended as the last author write; external ops/lane.sh receipt custody unchanged, no artifact_finalize
clock_start: 2026-09-14T21:28:16Z
inputs_dir: /tmp/jc2-lane.2X9nct/inputs (seven files by explicit basename only)

## 0. Input custody (pre-read, sha256sum at 21:28:16Z)

| file | sha256 | bytes |
|---|---|---|
| CROSS-COMMON.md | 3f1b17d8f569e8cc5871c240ea3d3470b435e207a608a26ffbe3893da3d7c05a | 4325 |
| ideation-swarmHQ-root-20260914T2110Z.md | 1000bafc2db13befb25b68463976c4f2fe10b9e8e044e837ba0ed9ac86194fbd | 7764 |
| ideation-swarmHQ-astra-20260914T2110Z.md | 61ac17778be3a1d1f4aeeb14f4d1048f1d30141343fc6cf8b50299815b9b017f | 11883 |
| ideation-swarmHQ-fable5-20260914T2110Z.md | f157854a610d403450c6178370bd55834bf0ac9252338bfd0d979702b949b77e | 13020 |
| APPROACHES.snapshot.md | 06cd4458487a1c53c51f64bd06dcd6b97d604e6a444a82896a20bd0537b4a645 | 106038 |
| STATE-DELTA.md | 056e5ecebd2192599dde6f67af720b9c8c797b538c8b4930fc9938a9fdebfd07 | 6620 |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 | 1985 |

The six SHAs printed in CROSS-COMMON match; CROSS-COMMON prints no self-hash, so its value is recorded here.

## 1. Read coverage

WHOLE reads of all seven inputs by explicit basename, no globbing, no other file:
CROSS-COMMON 1-72, ROOT 1-146, Astra 1-223, Fable 1-224, STATE-DELTA 1-99, FALLACY 1-36
(one cat each); APPROACHES.snapshot.md 1-807 in line windows 1-140, 141-270, 271-540,
541-680, 681-807. The harness clipped about 2.2 KB inside the last window; repaired by an
explicit re-read of lines 743-759 (Li sparse-profile stop through the section-9 "future
computation" paragraph). No peer cross-report, ledger, log, receipt, jc2-lean, jc2-web,
scientific code, worker command or network read. Nothing computed.

## 2. Candidate adjudication

### 2.1 Fable FJ-boundary / numerical-LC card: REFUTED at scope; DUPLICATE of the log-route gap; withdraw

I reject my own model's blind card. Exact objects: F is a normalized Keller map viewed as
a self-map of A2 through the standard source/target identification (the dynamical
premise). An FJ admissible compactification X is a smooth projective surface containing
the SOURCE plane with an SNC rational boundary tree; algebraic stability is a property of
the RATIONAL self-map F: X -> X (no iterate sends a boundary curve into the indeterminacy
set, so (F^n)^* = (F^*)^n on NS(X)). It is not regularity or properness: a Henon map is
algebraically stable on P2 and still has an indeterminacy point. NORMAL-NUMERICAL-LOG-1
needs a different object: the finite full normalization Ybar of the TARGET P2 in C(x,y)
(Mondal's surface, where q lives), a GENUINE SNC resolution Z -> Ybar, i.e. a birational
MORPHISM from a smooth surface whose total boundary is SNC, and the discrepancies of every
prime over q.

Missing implication: X dominates Ybar only if the extension X -> P2_target of F is a
morphism; then, X being normal, it factors through Ybar by the universal property of
normalization. Algebraic stability of the self-map supplies no such regularity, and the
card, the FJ import and the packet supply none. Hence the FJ boundary primes have no
computed centre on Ybar, let alone a discrepancy over q: the card's bounded quantity is
undefined. Even given regularity, one resolution decides LC only if it is a log resolution
of the PAIR (Ybar, boundary), which is exactly the "genuine SNC" clause the card assumed.
Both controls are vacuous: Henon is an automorphism (Ybar = P2, no q) and the non-Keller M
carries no Keller LC constraint, so neither can fail and the stop condition never fires
(FALLACY floor/attainment). The APP paragraph after the Mondal attachment says q is ONE
necessary LC failure; outcome (i) of the card silently needs it to be the only route, and
that withdrawn stronger claim is not restored. Distinct from the old zero-thinness
criterion in wording, identical in the missing arrow (source compactification -> target
normalization). One fragment survives as KNOWN-COMPOSED: lambda1 >= d_t >= 6 gives
lambda1^2 > d_t, so the small-topological-degree regime holds for every normalized
counterexample; it yields existence of a stable source compactification only, no boundary
object for the log route. The FJ theorem is not audited by citation. OPEN[FJ-BOUNDARY-LC]
should be closed as withdrawn by cross-review, not carried. 2, 27, 28 stay UNCHANGED.

### 2.2 Astra minimizer/genus transport: CONFIRMED (three identities); KNOWN-COMPOSED; no new source constraint

Checked separately. (a) b_N K_N b_N^{-1} = theta a_N^{-1} a_N F b_N b_N^{-1} = theta F is a
group identity. (b) lambda1(theta F) = mu: theta F = b0 (a0 F b0) b0^{-1} is conjugate to
the minimizer, and lambda1 is conjugation-invariant because deg(b K^n b^{-1}) is bounded
above and below by deg(K^n) times fixed factors from b and b^{-1}; a_N, b_N, theta have
determinant one, so K_N stays in the normalized class. (c) K_N^{-1}(ell) =
b_N^{-1}((a_N F)^{-1}(ell)) is the restriction of an automorphism, so genera equal those
of a_N F. Hidden premise made explicit: generic inverse-line genus is a right
(source-automorphism) invariant, while lambda1 is a conjugacy invariant; so for EVERY
target frame a the frame (a, theta a^{-1}) is a lambda1-minimizer with the genus of aF.
The transport is correct and essentially tautological. Its content is negative: the
selection "lambda1-minimal frame" provably cannot be the specially selected frame that the
UNPROMOTED target-shear statement says is missing. It produces no new actual-source
constraint and preserves the old missing secondary minimizer/genus bound exactly. The
"tends to infinity" clause inherits the UNPROMOTED conditional genus formula; the
identities do not. No FIRST, promotion or successor; 5, 18, 31 UNCHANGED. Label:
CONFIRMED / KNOWN-COMPOSED, DUPLICATE in effect of STATE-DELTA's "no minimal-frame bound"
line, sharpened by one sentence.

### 2.3 Fable positive-construction time: GAP as a task; KNOWN as allocation; NO history-distinct test

Fair opportunity cost: since FULL1300 every banked tranche was an exclusion or a
proof-gap diagnosis and construction received no time, while the guard protects
construction half-slots equally. But the blind names no new ansatz: "arbitrary H on T/S
plus the full Laurent-block extension identity" is APP section 7's existing endpoint
verbatim, after DS-INV-1 merged the three search spaces and PP-HOM/LIN-U/SEP-WT/3WT
excluded the sparse families. No weight window is specified and none is authorized. I
looked for a specifiable history-distinct test: the Newton reduction's nonintegral-ratio
branch is unreviewed nonexistence work, not construction; the mixed-moment control's
failing nonzero-weight row and the two-chart jet matching are finite-jet objects that
section 7 already excludes as the endpoint. So no concrete construction test exists in
the packet. The two-tranche stops (rational mate, elliptic multiplication, Liouville
fibres) and the scalar/preflight/r3 park have exact scopes that do not touch S/T; the
request is not a SCOPE-CONFLICT, only an unfunded allocation argument. Keep a protected
construction half-slot available for the first changed S/T object (a named block ansatz
with an explicit stop); fund nothing now.

## 3. Deduplication, strongest attack, test selection, dispositions

Deduplication: all three blinds keep 1-46 UNCHANGED and return NO_NEW_MECHANISM; Fable's
only card falls above, so the round is NO_TEST on the evidence, not by vote. Objects: ROOT
and Astra name the same chain A subset B=A[H] subset R with the same missing step (graph
normality, equivalent to invertibility); Fable names Ybar and q (log route, KNOWN missing
resolution arrow); Astra's K_N is a tautological reframing. Mechanisms: none new.
Decisive tests: Astra's ten-minute hand check is completed above; Fable's one-lane-hour
derivation has an undefined quantity. Compatible combination: the small-topological-
degree remark (2.1) and the transport (2.2) can be banked together as one KNOWN-COMPOSED
note under the two dynamical promotions: minimality of lambda1 neither bounds genus nor
attaches a boundary object.

Strongest surviving proposal: ROOT/Astra graph normality of B=A[H] for the compatible
single pair. Attack on its hidden premises: (i) every proposed intermediate (conductor
descent, codifferent, trace-square, formal-flow containment, Euler stability) is already
recorded as reducing to integrality of R over A, and the hypersurface pinching control
refutes every relaxed form; (ii) the two-polar criterion is an equivalent endpoint;
(iii) a new argument must use full-plane polynomiality of BOTH f and g, and nobody names
a statement strictly between "R finite over B" and "B normal" that is known to hold for
an actual Keller source. It survives as the right target with no changed test.

Selected test: NO_TEST. No candidate has a defined bounded quantity whose two outcomes
change the global bridge. Changed all-46 dispositions: none; the near-change in Fable's
blind (2/27/28 via the FJ card) is withdrawn. No new OPEN is raised.

## 4. Systems and recommendation

Systems: NO_CHANGE. Measured-benefit criterion for any UPGRADE: a measured reduction of
whole-read time or of semantic-duplicate cards on a frozen packet against a control
round; none exists. Local observation: one 127-line APP window was clipped by the harness
and repaired in under a minute by an explicit bounded re-read; keep windows near 120
lines, no framework. apply_patch resolved on the supplied PATH.

Recommendation: CONTINUE protected all-degree reasoning (Astra primary, Fable
independent, Sol fallback). STOP the FJ-boundary card and close its OPEN as withdrawn.
RECORD the minimizer transport as a KNOWN-COMPOSED negative, UNPROMOTED. Keep the
construction half-slot reserved and unfunded until a changed S/T object is named. No
lane, compute, FIRST, deadline reset or successor.

## COLLISIONS

Verbatim output of `python3 ops/open_collision.py xmodel/ideation-swarmHQ-fable5-cross-20260914T2110Z.md --root .`
at 2026-09-14T21:33:40Z (exit 0), the sole mechanical repository check run:

```
## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.
```

Semantic collisions stated from the packet: 2.1 collides with the log-route resolution
gap and near-collides with zero thinness; 2.2 collides with STATE-DELTA's minimal-frame
line; 2.3 collides with APP section 7's endpoint. No OPEN raised, none carried.

## 5. Closing custody

Post-read sha256sum at 21:33:40Z, all seven identical to section 0:

| file | post sha256 | match |
|---|---|---|
| CROSS-COMMON.md | 3f1b17d8f569e8cc5871c240ea3d3470b435e207a608a26ffbe3893da3d7c05a | yes |
| ideation-swarmHQ-root-20260914T2110Z.md | 1000bafc2db13befb25b68463976c4f2fe10b9e8e044e837ba0ed9ac86194fbd | yes |
| ideation-swarmHQ-astra-20260914T2110Z.md | 61ac17778be3a1d1f4aeeb14f4d1048f1d30141343fc6cf8b50299815b9b017f | yes |
| ideation-swarmHQ-fable5-20260914T2110Z.md | f157854a610d403450c6178370bd55834bf0ac9252338bfd0d979702b949b77e | yes |
| APPROACHES.snapshot.md | 06cd4458487a1c53c51f64bd06dcd6b97d604e6a444a82896a20bd0537b4a645 | yes |
| STATE-DELTA.md | 056e5ecebd2192599dde6f67af720b9c8c797b538c8b4930fc9938a9fdebfd07 | yes |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 | yes |

Shell actions used: date, sha256sum/wc on the seven inputs, sed/cat/grep line-range reads
of the seven inputs only, apply_patch (three writes including this one), the single
collision command, wc on this report. No charge_basis line; no exit price asserted;
evidence MANUAL, UNPROMOTED. Word count before this write 1480 including hash tokens and
header, prose within the 1400 target. Clock at last write: before the 21:58 target.

<!-- BODY-END -->
