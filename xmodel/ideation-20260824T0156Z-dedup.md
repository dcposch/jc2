# Post-collection deduplication — round `20260824T0156Z-8bf25a5`

- **Producer/session:** OpenAI Codex, Bacon dedup lane (`/root/compute_audit`)
- **Round cutoff:** `2026-08-24T01:56:44Z`
- **Basis:** `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`
- **Packet:** `xmodel/ideation-20260824T0156Z-packet.md`
- **Packet SHA-256 (recomputed):**
  `4c1e582041db9e5f7267c13dbd681cacc56b0e7176d81dc185ee2662818c967a`
- **Mode:** post-collection comparison of the five frozen submissions.  This is
  a deduplication and hostile perimeter audit, not a vote, promotion, launch,
  or shared-ledger update.

I read the sealed packet and all five named submissions only after blind
collection closed.  The previous-round synthesis/portfolio, already common
required inputs of the sealed packet, are used solely to distinguish new
mechanisms from renamed round-00:35Z candidates.  No D2 result or post-cutoff
review verdict is consumed.

## 1. Integrity, hashes, and blindness metadata

The following hashes are hashes of the frozen report bytes as collected, not
self-hashes claimed by their authors.

| Submission | Lines / words | Recomputed SHA-256 | Blindness metadata audit |
|---|---:|---|---|
| `root` | 322 / 2,657 | `c5ab3481a71a884c2558ea9b1fcf9bb829ac35e7477b6bd356888917caabd888` | **PASS by declaration, metadata thin.** The header says only the packet and its required inputs were consumed and labels the report blind/no-promotion (`root:1-6`). It does not restate the basis, cutoff, freeze time, or an input-hash table. No internal sign of a post-cutoff premise was found. |
| `bacon` | 442 / 3,552 | `f7763776836180f0e792d47deb6104bc2555070236389e50c1b880af2523622b` | **PASS, strong metadata.** Producer, cutoff, basis, lens, freeze time, all-input hash verification, all-46 scan, sibling exclusion, no post-cutoff use, and no launch/promotion are explicit (`bacon:1-14`). |
| `nash` | 406 / 3,499 | `5c98eed6e0e05246c0f3340851047168266c93e964440446f4f8ebf4380b5b48` | **PASS by declaration, metadata incomplete.** Producer, round, cutoff, lens, blind/frozen lifecycle and no post-cutoff use are explicit (`nash:1-9`); the report does not state a basis, packet/input hashes, read list, or an explicit same-round-sibling exclusion. Its complete 46-row vector and evidence perimeter are consistent with the packet. |
| `grok` | 388 / 6,658 | `9a2da45bd446e566d1ef88f3ef191280655c2608e8c2a512f714410784f7595e` | **PASS, strong metadata.** Producer/tool, basis, cutoff, packet hash, every required-input hash, all-46 scan, sibling exclusion, and excluded post-cutoff artifacts are explicit (`grok:1-43`). It also declares reading the prior-round `0035Z-grok2` report for formatting; that is outside the forbidden *same-round* sibling set and is disclosed (`grok:35-37`). |
| `fable` | 428 / 4,573 | `f40970c06a331c27b2a6cb33f6e5f7e7794caee7ab817ff97d2bd4d663b5e9a9` | **PASS, strong metadata.** Producer/tool, cutoff, basis, packet hash, sibling exclusion, no post-cutoff use, complete read list and all 13 hash matches are explicit (`fable:1-32`). |

Blindness is necessarily a provenance assertion, not something derivable from
the report bytes.  The hash and metadata checks establish stable inputs and no
visible contamination; they cannot prove what a process did not read.  The
weaker `root`/`nash` metadata should not be converted into lower mathematical
weight, but future packets should require the same basis/cutoff/read-list/hash
footer from every producer.

Commands used for this audit:

```text
shasum -a 256 xmodel/ideation-20260824T0156Z-{root,bacon,nash,grok,fable}.md
wc -c -l -w xmodel/ideation-20260824T0156Z-{root,bacon,nash,grok,fable}.md
shasum -a 256 xmodel/ideation-20260824T0156Z-packet.md
```

## 2. Frozen evidence perimeter used in the comparison

The common evidence floor is small and must not be raised by vote counting.

| Object | Tier at cutoff | What it licenses here | What it does not license |
|---|---|---|---|
| `D25 -> D27` / `FREE-TAIL-SIGNAL` | Different-model `CONFIRMED`, pointwise one-band MOD-p | The typed ten-row transition, the four named point ranks, six affine directions at two witnesses, two cokernel cuts, and nonzero later residuals for the displayed lifts | Generic rank, a nonempty D27 scheme, persistence, a formal germ, characteristic zero, or a counterexample |
| `D2-CELL26` | Sole running D child | Ranking conditional continuations and outcome branches | Any D2 outcome; none is in this snapshot |
| `D43-NF-FID` | `CONFIRMED WITH GAPS`, MOD-p source/NF fidelity | A scoped source-honesty audit | Integral/p-adic transfer, flatness, Hensel, a germ, or even source reduction of the adjoined P4P1 correction |
| P1 raw-boundary probe | Producer-checked plus coordinator replay, review running | Motivation to stop the tested raw Smith/Fitting/action-pole representations | A promoted theorem that every canonical, signed, twisted, minimized, or complete-data invariant is impossible |
| P2 TRACE-REG probe | Producer-checked plus coordinator replay, review running | A precisely stated trace/localization target and an exact contact-schema collision under its recorded hypotheses | An actual Keller countermodel, a refutation of every augmented packet, or a smaller theorem than properness at full scope |
| SuperMind/Guo intake | Producer-checked, unpromoted, review running | Conditional exact support for the two residual systems and software/provenance lessons | An independent vote, the GGV reduction/transcription bridge, an unconditional `(72,108)` exclusion, or JC2 |
| Tame/Henon/class-kill and promoted book/D25 objects | Promoted at their recorded scopes | Controls and source-side objects | A positive nonautomorphic Keller control or complete landing/coverage |
| Jelonek/Chau statements invoked by Fable | `[LIT]`, not independently verified in this round | Motivation only | A campaign proof premise before source verification and hypothesis matching |

## 3. Exact raw fingerprint map

The fingerprint key is the ordered quadruple

```text
(target obstruction, mechanism, mathematical object, cheapest decisive test).
```

Fifteen submitted cards contain sixteen operational ideas because Grok Card C
bundles two mathematically unrelated stages.  One additional uncarded launch
proposal (Fable's odd-prime Witt lane) is recorded so that the portfolio
outlier is not lost.  Only two pairs are operational duplicates; all other
similarities are thematic rather than identity of the quadruple.

| Raw ID / source | Target obstruction | Mechanism | Mathematical object | Cheapest decisive test | Dedup / ancestry |
|---|---|---|---|---|---|
| **R-A** `root:115-173` | Affine-target poles in the characteristic coefficients/traces of `x,y` | Extend `partial_P,partial_Q` to `L`, commute them with field trace, and seek a finite closed mixed-trace differential system | A resolvent/Bezout trace module over `K=C(P,Q)` localized at a target DVR | Derive degrees 2 and 3; run triangular-automorphism and `(x^2,xy)` controls; ask whether a paired P2-style formal pole solves both coordinate equations and `J=c` | **Distinct.** New differential mechanism inside the prior TRACE-REG/canonical-normalization theme |
| **B-A** `bacon:118-205` | Poles of `x,y` at height-one primes of the finite normalization | Compare the inverse-Jacobian derivation lattice with the inverse different and pole lattice | `I_delta` in `Cbar`, its divisor, the different, and the `B=C[x,y]` pole divisor | Identity/tame, `(x^2,xy)`, small ramified extensions, and one denominator-42 formal local control; stop on tautology or local failure | **Distinct.** New lattice/conductor mechanism; not R-A because neither its object nor its discriminator is a trace differential system |
| **N-A** `nash:122-195` | Ramification/trace defect of the finite normalization over the affine target | Seek a compactification-independent signed global different/discriminant degree; attack all local-only variants with Darboux freedom | Completed finite normalization algebra, inverse different, trace moments, and a proposed global divisor `Delta_nu` | Exact Laurent checker plus `x=z_b(u)`, `y=q e u^(e-1)/(c x_u)`; one signed global formula gets at most a six-hour covariance/control gate | **Distinct.** New proposed global formula, but a refinement of prior canonical normalization rather than a new established avenue |
| **F-1** `fable:177-230` | Failure to determine trace principal parts on components of the nonproper-value locus | Direct-image completed branch coefficients from tagged dicritical divisors into a trace receiver | A candidate `A(F)` component, all boundary divisors above it, local factors, discrepancy/two-form orders, and `PP_C Tr(z^m)` | Re-derive localization; replay four controls; parse one certified residue-A book and decide whether book+`J=1` determines `m<=2` convolutions | **Distinct.** New books-to-`A(F)`-to-trace connection, built from prior boundary/TRACE/PSC candidates; it is not yet a new ledger row |
| **R-C** `root:222-268` | The old GGV/Sigray packet may not determine even the quadratic trace observable | Type the packet, embed the P2 pair, find a collision, then identify the first separating tag | Serialized target-divisor grouping, completed branch pairing, residue-field trace, and coefficient convolution | Four-hour type gate followed by the P2 collision and minimal-augmentation search | **Exact duplicate cluster `PAIR-IR` (vote 1/2).** This is the prior-round `PSC-FINGERPRINT` candidate made concrete |
| **N-C** `nash:248-298` | Same packet-fidelity/transport obstruction as R-C | Same typed-certificate/collision mechanism, with explicit provenance and coordinate hashes | Same moment-carrying target-local record, extended by an actual registered GGV population attempt | Automorphism canonicalization, P2 moment separation, then one GGV packet; stop on missing field/collision | **Exact duplicate cluster `PAIR-IR` (vote 2/2).** Nash adds controls and IR hygiene but not a different mechanism |
| **G-B** `grok:206-245` | A coefficient convolution may remain presentation-dependent even after P1 | Minimize an automorphism presentation first, then test a trace convolution at target infinity for covariance | Completed inverse branches of small automorphisms in two compactification charts | Identity, `T2`, `T4`, `T4^-1 o T4`, explicit blow-up, optional Henon only after a candidate | **Adjacent, not duplicate.** A refinement of prior P1/PSC work; it tests covariance at infinity, not injectivity of the affine-target packet |
| **F-3** `fable:273-306` | Trace/`A(F)` experiments are one-off and hard to replay | Build an exact elimination/local-expansion instrument | Resultants or multiplication polynomials, saturated denominator divisors, and `PP_C Tr(z^m)` for `m<=3` | Byte-replay P2 plus automorphisms and `(x^2,xy)` | **Distinct engineering idea.** New tool for the prior TRACE-REG candidate; no theorem content by itself |
| **F-2** `fable:232-271` | No exact local model is known that obeys all proved Keller boundary constraints while retaining a trace pole | Form a bounded constructible local-model space and solve it exactly for a witness or emptiness | One-place local parameter, completed branch package, semigroup/two-form/exactness constraints, and an `m<=2` principal part | At a fixed denominator/support/characteristic-pair cap, produce a rational witness or an elimination/Nullstellensatz emptiness certificate | **Distinct.** New counterexample-side use of the P2 receiver; Nash's Darboux family is a prefilter, not an operational duplicate |
| **R-B** `root:175-220` | Fixed-depth D survival does not decide an inverse tail | Prove eventual finite state, then form a transfer/Ore module and compute torsion/free rank | The source first-occurrence registry and a shift-module presentation of the band recurrence | Finite-state/type theorem first; source-derived operator; validation on banked bands; Smith/annihilator computation | **Exact duplicate cluster `D-ORE` (vote 1/2).** New finite-tail refinement of the prior D-transition/compiler candidate |
| **N-B** `nash:197-246` | Same D inverse-tail obstruction as R-B | Same six-periodic finite shift/Ore presentation and torsion/free test | Same band-state module over a shift ring, with source hashes | Two source derivations of the operator, banked-band prediction, then Fitting/Smith data | **Exact duplicate cluster `D-ORE` (vote 2/2).** Nash supplies a pilot; Root supplies the essential theorem-first gate |
| **B-B** `bacon:207-283` | The D source has no proved arrow to target-affine trace data | Apply Reynolds/Newton sums to a cyclic source orbit, but require an exact source-orbit-to-completed-factor dictionary before cell reduction | Content-addressed D-source AST, orbit sums, one named target DVR factor, and P2 convolution | Two-hour dictionary gate on one denominator-42 orbit; only after reviewed D2 reduce `m<=2` modulo compatibility functions | **Distinct.** New D-to-trace bridge; neither `D-ORE` nor `PAIR-IR` manufactures this missing source functor |
| **B-C** `bacon:285-349` | A coherent one-band D locus may still have a finite higher compatibility obstruction | Compute the graded symbol and first Spencer/Janet compatibility module over the saturated D2 base | `A_26`, left syzygies, next inhomogeneity class, Hilbert signature, certified remainder | After a reviewed nonempty D2 base, reduce the first source-defined next class modulo syzygies; stop after one obstruction | **Distinct.** New involutivity mechanism, adjacent to but not duplicated by `D-ORE` |
| **G-A** `grok:162-202` | The six-dimensional D1 fiber may be chart/automorphism gauge rather than CE-shaped freedom | Quotient the kernel by a *proved continuous* gauge action; treat finite symmetries discretely | The two reviewed right kernels, continuous chart-coordinate gauge Jacobian, and discrete torsor/orbit equivalences | After repairing the tangent definition, compare both-prime kernels with the continuous gauge image and canonical representatives modulo finite symmetries | **Distinct.** New interpretation test; the submitted finite-group tangent formulation needs correction in section 7 |
| **G-C1** `grok:249-281` | The band-42 P4P1 correction lies outside D43 checkpoint traces and may be load-bearing | Compare the source/checkpoint row with the finally assembled row | Symbolic P4P1 correction polynomial and its evaluations/remainders on the registered modular fiber | Symbolic difference/reduction at one prime, then origin and one banked nonzero sample as controls | **Distinct scoped hygiene audit.** New follow-up to `D43-NF-FID`, not a D-depth or integrality attack |
| **G-C2** `grok:249-268,283-311` | Small topological degree might be incompatible with a proved bound on branch places and primitivity | Enumerate primitive branch-cycle types subject to Riemann--Hurwitz and an independently proved support bound | Primitive permutation groups of degrees 6--9 and admissible inertia tuples | Local GAP enumeration with an exactly specified support bound and Orevkov `(48,64)` negative control | **Distinct but not new.** Revival of existing avenue 26; the support bound is still absent |
| **F-X** `fable:109-111,402-420` | The D lane may collapse while no orthogonal CE search runs | Bounded odd-prime/other-support low-support collision search retaining W2 survivors | Registered characteristic-`p` collision/Witt obstruction equations over `F3,F5` | Pre-capped local enumeration; freeze any W2 survivor for review | **Uncarded portfolio outlier, not new.** Existing avenue 19; no new evidence in this packet |

Therefore the 17 raw entries reduce to **15 operational fingerprints**:
`R-C/N-C` merge once and `R-B/N-B` merge once.  Nothing else satisfies all
four equality fields.  In particular, sharing the words “trace,” “different,”
or “D-module” is not enough to merge mechanisms.

## 4. Cluster overlaps, votes, disagreements, and outliers

### 4.1 Preserved vote map

| Cluster | Direct operational votes | Adjacent support | What the count does and does not mean |
|---|---:|---|---|
| Typed `PAIR-IR` / quadratic-receiver schema | **2**: Root, Nash | Grok's minimized-convolution covariance; Fable's `A(F)` receiver and `trace_atlas`; Bacon's demand for a D-to-target dictionary | Strong agreement that the missing field is now typable. It is not evidence that an actual GGV packet has a target functor or that an augmented fingerprint is injective globally. |
| Finite D shift/Ore tail | **2**: Root, Nash | Bacon's Spencer completion and trace-orbit compiler; Grok's fiber interpretation | Agreement on replacing depth sampling by structure. It rests on the same reviewed D1 artifact and a future D2 premise, so it is not two independent mathematical observations. |
| Canonical target-divisor proof objects | **4 distinct mechanisms**: Root R-A, Bacon B-A, Nash N-A, Fable F-1 | Grok G-B | This is a theme, not a merged candidate: differential closure, a derivation conductor, a signed global different, and a dicritical trace receiver can fail independently. All were triggered by the same P1/P2 packet, so “four votes” is weak evidence for truth. |
| D kernel as gauge versus extra fiber | **1**: Grok | Bacon explicitly treats formal integrability; Root/Nash mention automorphism controls only as perimeter | A genuine outlier and useful hostile question, but its submitted tangent construction is partly ill-posed. |
| D43 P4P1 source-honesty close | **1**: Grok | The other reports preserve the D43 gap but do not propose this check | A cheap audit outlier; high reliability value, low direct JC2 leverage. |
| Primitive-group `td` probe | **1**: Grok | None | Existing avenue 26, conditional on a support bound not supplied by the packet. |
| Odd-prime Witt launch | **1 launch vote**: Fable | Root, Bacon, Nash and Grok retain it as an orthogonal reserve/held fallback | Allocation outlier, explicitly not evidence-driven in Fable's own disposition. |

### 4.2 Material disagreements

1. **`A(F)` readiness, not relevance.** Root, Bacon, Nash and Fable raise or
   reopen the target-divisor/integrality direction; Grok lowers avenue 7 because
   P1 removed the cheap compactification handle.  The apparent disagreement is
   resolved by separating *canonical receiver* from *available source*: all five
   accept the former as the correct target; only Fable asserts a cheap route
   from present books/resultants to the latter, and that assertion still owes
   the corrections in section 7.
2. **Packet/passport priority.** Root, Nash and Fable raise avenues 2/25;
   Grok lowers them; Bacon leaves them unchanged.  Root/Nash/Fable mean a
   coefficient-complete tagged receiver, not more contact passports.  Grok's
   lower applies to the old contact-only representation.  There is little real
   disagreement once the objects are typed, but there is no consensus that a
   source can populate the enriched record.
3. **D follow-up.** Root/Nash favor a finite shift module; Bacon favors first
   Spencer compatibility and a separate D-to-trace dictionary; Grok favors
   identifying gauge directions; Fable launches no post-D2 child.  These are
   distinct questions and should not run as siblings.  D2's reviewed outcome
   must select at most one.
4. **Immediate capacity.** Bacon and Nash keep the packet's four active roots
   (`C`, `D2`, external review, P1/P2 review) occupied until reviews harvest.
   Root, Grok and Fable describe new proof/falsification roots by treating some
   reviews as coordination/background.  The sealed packet itself lists those
   activities as active.  Safest reading: **no new root launches before a slot
   is explicitly closed or reclassified by the coordinator.** This dedup does
   not launch anything.
5. **Orthogonal CE allocation.** Fable alone would spend a root on the odd-prime
   Witt refinement now; the other four see no new trigger.  Preserve it as the
   first fallback if D2 closes the D chart, not as a five-report consensus.

### 4.3 Apparent agreements sharing one assumption

- Every trace/normalization proposal consumes P2's producer-checked
  localization/formula as either premise or motivation. Re-deriving it in a
  child can remove review exposure; five restatements cannot.
- Every D follow-up consumes one source implementation and one reviewed
  pointwise transition. A mistranscribed orbit product or chart-specific source
  convention would correlate `D-ORE`, Spencer, Reynolds, and gauge tests.
- Every GGV/Sigray fingerprint assumes an actual source-side object can be
  functorially tagged by affine target divisor and completed factor. The P2
  collision proves only that the old schema lacks information.
- Every normalization/different proposal lacks a positive nonautomorphic Keller
  control. Automorphisms plus non-Keller maps can falsify a candidate, but they
  cannot validate the missing sign or global bridge.
- SuperMind, Guo, Helali, Suzuki, and the campaign residual systems share
  mathematical cores and an unresolved derivational-lineage graph. None of
  these submissions mistakenly promotes them, and repository count remains no
  vote count.

## 5. Genuinely new mechanisms versus prior-round renames

The previous round retained six candidates: external intake, D transition
before depth, canonical boundary source/covariance, TRACE-REG audit,
`PSC-FINGERPRINT`, and sublinear type only downstream.  Against that list:

### New mechanisms or materially new cross-connections

- **`TRACE-HAM`**: commuting target derivations plus a finite mixed-trace
  differential closure gate.
- **Derivation conductor**: compare the polynomial inverse-Jacobian frame with
  the normalization/different lattice.
- **`CAN-DIFF`**: a specific signed global different/discriminant target with an
  explicit arbitrary-`b` Darboux falsifier. It is new machinery inside the old
  canonical-normalization architecture, not a new theorem.
- **Finite `D-ORE`**, **D-Spencer completion**, and **D-to-trace Reynolds
  compilation**: three distinct post-D1 structure tests. The old round asked
  for a typed D compiler; it did not supply these operator/module mechanisms.
- **D gauge quotient**: asks what the new one-band fiber *is*, rather than
  whether another depth is nonempty.
- **`A(F)`-anchored trace receiver**: a new composition of books, nonproper
  divisor images and P2 moments, conditional on landing and literature checks.
  It does not yet justify adding avenue 47.
- **Pole-surviving local-model scheme**: a new two-sided CE/proof discriminator
  seeded by P2, provided emptiness is certified algebraically.
- **`trace_atlas`** and **P4P1 symbolic comparison**: new reusable/scoped
  software checks, not mathematical avenues.

### Renamed, refined, or revived prior work

- Root `PAIR-FINGERPRINT` and Nash `PAIR-IR` are the queued prior
  `PSC-FINGERPRINT`, now correctly specialized to the coefficient convolution.
- Grok's minimized convolution is the next covariance layer after the prior P1
  boundary kill test and P2 audit; it is a refinement, not an independent new
  route.
- The finite D shift cards refine the previous D-transition/compiler direction;
  their *Ore theorem* is new, but “structure before depth” is not.
- Primitive-group `td` enumeration is existing avenue 26.
- Odd-prime W2 survivor search is existing avenue 19.
- No submission revives sublinear type as a standalone lane, and no new external
  certificate campaign is proposed.

## 6. Novel cross-report connections worth preserving

1. **Nash's Darboux family is the common hostile prefilter.** The exact family
   `x=z_b(u)`, `y=q e u^(e-1)/(c x_u)` should be tested before theorem work in
   Root's trace system, Bacon's conductor, and Fable's local-model scheme. If a
   proposal uses only the local two-form and retained branch decoration, the
   arbitrary `b` freedom is designed to kill it cheaply. Surviving requires a
   genuinely global or paired-coordinate condition.
2. **The trace receiver separates three missing arrows.** `PAIR-IR` tests
   *information content*; Bacon B-B tests *D-source provenance*; Fable F-1 tests
   *book/dicritical provenance*. A collision in the first does not answer the
   latter two, and a source dictionary does not prove injectivity.
3. **`D-ORE` and Spencer are complementary only after one base is real.** Ore
   asks eventual finite state; Spencer asks the first compatibility class over
   a saturated base. A cheap Spencer unit obstruction can preempt the larger
   finite-state theorem, while a nonstationary registry can preempt Ore without
   refuting formal integrability by some other method.
4. **P4P1 is a compiler acceptance test.** If the correction is load-bearing
   but absent from the checkpoint provenance, any future common-integral D
   compiler must either source-reduce that correction or narrow its object. It
   cannot inherit `D43-NF-FID` by hash association.
5. **The gauge question must precede CE rhetoric, not source algebra.** A
   corrected continuous-gauge/discrete-symmetry quotient can interpret D1's
   fiber. It cannot replace D2's compatible-base calculation or prove a tail.
6. **A trustworthy `trace_atlas` would unify controls but not bridges.** It can
   replay P2, CAN-DIFF, and Fable's local search from one exact instrument. It
   cannot manufacture landing, branch pairing, or a GGV/D source functor.

## 7. Mathematical corrections and mandatory perimeter tightening

The following are corrections to formulations, not post-cutoff verdicts.

| Source claim | Correction |
|---|---|
| Bacon says the later band-30/36/40 residuals prove the band-26 kernel “is not a gauge” (`bacon:304-308`). | They prove only that the displayed band-26 lift directions are not automatically compatible with those later equations. They do **not** identify the whole kernel modulo automorphism/chart gauge, and they do not prove that no subspace is gauge. Grok's Card A exists precisely because this remains open. |
| Grok proposes infinitesimal tangent vectors from the promoted finite torsor and cyclic eta permutations (`grok:183-187`). | Over the registered primes, these finite groups are etale and have zero Lie algebra. Discrete permutations/torsor elements may be quotiented by orbit/stabilizer or compared through finite differences, but they do not supply tangent directions. Only an explicitly defined continuous scaling/shear/chart action can have a tangent image. `GAUGE-TAIL` is unavailable until that dictionary is repaired. |
| Grok's P4P1 test asks origin plus one nonzero sample to say whether a correction is “identically zero” (`grok:270-281`). | Two evaluations cannot prove a multivariate polynomial identity. Decide identity by symbolic subtraction and exact reduction in the registered source/base ideal, or by a proved degree-bounded interpolation set. Samples may only report pointwise load-bearing behavior. |
| Grok treats agreement after minimization on a small automorphism suite as a map-intrinsic fingerprint (`grok:225-241`). | Sample covariance is only evidence. “Map-intrinsic” additionally requires a canonical, choice-independent minimizer and a covariance theorem. Moreover an infinity convolution is not automatically the affine-target principal-part receiver needed by TRACE-REG. |
| Fable identifies the polar support with `A(F)`, says books enumerate the carriers, and uses the Keller two-form order (`fable:49-63,182-208`). | A defensible target is: after proving the DVR Newton/trace criterion, the **union over both coordinates and all `1<=m<=d`** of height-one polar supports detects the codimension-one nonfinite locus. Individual traces may cancel. Identifying that locus with all relevant `A(F)` components, obtaining every divisor from the campaign books, and the one-place statement require the stated Zariski-Main/resolution and external-literature proofs plus complete landing/coverage. `ord_E(dP wedge dQ)>=0` applies only where `F` extends regularly at the generic point of `E`, with relative-canonical conventions fixed; contracted and target-infinity divisors need separate treatment. Fable labels much of this `[ECD]/[LIT]`, so the correction is to prevent the executive prose from outrunning those labels. |
| `trace_atlas` promises an “exact `A(F)` equation as denominator support” from bivariate resultants (`fable:277-293`). | Raw resultant or denominator support can contain leading-coefficient/extraneous divisors and can depend on presentation. Exactness requires elimination saturation, generic-degree control, reduced characteristic data (or verified multiplication algebra), normalization/local-factor handling, and the proved union-of-trace-poles criterion. Until the controls and these invariance checks pass, call the output a **candidate polar-support upper bound**, not `A(F)`. |
| Fable's bounded local-model card calls for an “exhaustive exact scan” (`fable:236-266`). | Bounding support and denominators still leaves coefficient parameters over an infinite field. A negative result is exact only if it is a Groebner/elimination/constructible-stratum or Nullstellensatz certificate (with saturations/inequations), not failure to find a sample. A survivor remains a local formal package, never a polynomial Keller map. |
| Nash proposes an effective different supported over the asymptotic divisor and a degree-zero global formula (`nash:127-155`). | These are correctly labeled **PROPOSED**. The finite normalization and inverse different are standard; support identification, compactification-independent signed degree, codimension-two flatness/purity, and the bridge from that cover back to the open source are separate unproved gates. No report may cite `CAN-DIFF` as an established divisor formula. |
| Nash's two-instance Ore pilot can appear to decide a finite presentation (`nash:220-240`). | It can falsify a proposed state machine or provide a conjectural operator. Positive finite-state/torsion/free conclusions require Root's theorem-first gate: derive eventual finite generation from the source registry, then prove the operator for all bands. |
| Grok's primitive-group card chooses an `N` that “still includes” the Orevkov control (`grok:253-285`). | `N` must come from an independently proved relation between the Keller boundary data and the number/type of branch places. Choosing it post hoc to retain a control is not a theorem. Without that bound, GAP output is only a conditional census of branch-cycle tuples. |

Two proposed claims survive this audit without correction but retain their
stated hypotheses:

- In characteristic zero a base derivation extends uniquely through a finite
  separable field extension and commutes with field trace. Root's `TRACE-HAM`
  formulas are therefore a legitimate exact starting identity; finite closure
  and regularity are the conjectural steps.
- Finiteness of the normalization of `C[P,Q]` in `C(x,y)` does not assume that
  `C[x,y]` is finite over `C[P,Q]`. Bacon and Nash correctly distinguish these
  rings. The hard step is relating the polynomial source lattice/open immersion
  to that finite normalization.

No submitted mathematical conclusion flips JC2, the D-series perimeter, or the
external `(72,108)` perimeter. The corrections above change proposed-test
semantics and evidence labels, not a promoted/global result.

## 8. Dependency/evidence tiers for consolidated candidates

| Candidate family | Exact inputs | Unreviewed or missing dependencies | Maximum legitimate output tier |
|---|---|---|---|
| `PAIR-IR` / receiver schema | Exact P2 formulas re-derived in-lane; promoted native source fields; exact substitutions/hashes | P1/P2 reviews at cutoff; actual GGV-to-target or pure-book source functor; landing/coverage | Typed schema insufficiency or bounded computational injectivity. An actual-map transport refutation needs realizable source pairs |
| `TRACE-HAM` / conductor / `CAN-DIFF` | Characteristic-zero finite separable algebra, target derivations, finite normalization, exact controls | Finite differential closure; non-tautological `B`--`Cbar` lattice identity; global signed divisor/covariance formula | Exact local countermodel or candidate lemma for review; never properness from controls alone |
| `A(F)` receiver / local models / atlas | Independently re-derived DVR trace criterion and exact elimination controls | Jelonek/Chau source verification; complete resolution/book landing; target-divisor grouping; saturated exact atlas | Candidate receiver, exact bounded local witness, or certified bounded emptiness only |
| `D-ORE` / Spencer / D-to-trace | Reviewed pointwise MOD-p D1 plus source compiler | A reviewed nonempty D2 base; source stationarity; common integral model; target-affine dictionary | Cell-scoped MOD-p obstruction or formal-tail signal. No characteristic-zero/germ/polynomial inference |
| D gauge quotient | Reviewed pointwise MOD-p D1 kernels | A real continuous gauge action on the registered coordinates; discrete quotient semantics | Chart-and-prime-scoped kernel decomposition only |
| P4P1 audit | Reviewed `D43-NF-FID` gap and exact modular source/assembly code | Source derivation/reduction of the correction | MOD-p compiler-scope verdict; no D43 integral permission |
| Primitive-group census | Classical finite group/Riemann--Hurwitz computations and a negative control | A proved branch-support/type bound and provenance from actual Keller boundary data | Conditional small-degree exclusion only |
| Odd-prime Witt search | Promoted characteristic-`p` equations at recorded scope | New support choice, W2 obstruction computation, all-level/integral lift and char-zero algebraization | A finite-field survivor or scoped negative census only |

## 9. Ranked consolidated candidates — queue only, no launch

Ranking is by expected decision value per bounded exact effort, with readiness
and dependency exposure included. It is not a truth probability or permission
to consume an active root.

1. **Typed affine-target trace receiver (`PAIR-IR` plus a corrected minimal
   atlas).** Two true duplicate votes and three adjacent designs converge on a
   precise test whose prerequisite was supplied by P2. Start, when a root is
   free, with independent re-derivation and controls; stop at the first missing
   source field or collision. Keep schema insufficiency separate from
   actual-map transport.
2. **Hostile normalization/derivation gate.** Run the explicit Nash Darboux
   freedom as a shared prefilter, then choose exactly one of `TRACE-HAM`, the
   derivation conductor, or a signed global `CAN-DIFF` formula. These are
   separate mechanisms, not parallel votes. Two failed formulations stop the
   representation.
3. **Post-D2 structural tail discriminator.** If and only if D2 returns a
   reviewed coherent positive-dimensional base, use the first cheaper of a
   Spencer obstruction and the finite-state theorem; proceed to `D-ORE` only
   after source stationarity is proved. No band 28 and no integral D43 follows.
4. **Corrected D-kernel quotient.** Define the continuous chart/gauge action,
   treat finite symmetries discretely, and decide whether any stable both-prime
   kernel complement remains. This can retire CE-shaped rhetoric cheaply, but
   it neither duplicates nor replaces D2.
5. **`A(F)` receiver / local realize-or-refute, after theorem and atlas gates.**
   Verify the literature/hypotheses and saturated elimination first. Then one
   book-determination test or one certified bounded local-model scheme can
   distinguish persistent coefficient freedom from a candidate identity.
6. **Symbolic P4P1 source-honesty close.** Smallest and most reliable audit,
   but scoped impact. A load-bearing correction narrows compiler provenance; a
   symbolic zero closes only that gap and does not release integral D43.

Not ranked into the six: primitive-group enumeration lacks its support bound;
the odd-prime Witt lane has one allocation vote and no new trigger; minimized
infinity convolution is downstream of a canonical minimizer not yet proved.

## 10. Recommended four-root portfolio

The packet lists four active roots at cutoff.  Preserve them until their
registered gates close; “background review” is still campaign work unless the
coordinator explicitly reclassifies it.

| Root | Work now | Close / handoff rule | Evidence exposure |
|---|---|---|---|
| **C — coordinate** | Freeze this round, verify hashes, harvest D2 and the two review streams, maintain holds and the claim DAG | No mathematical child. Rebalance only when a named root closes | None |
| **D — sole D child** | Continue `D2-CELL26` exactly under its registered base-locus/saturation stop; no sibling and no band 28 | Empty/special base: close and rerank. Positive coherent base: freeze for different-model review; only after that choose **one** of Spencer-first or finite-state/`D-ORE` | Reviewed D1 only; no D2 result is presumed |
| **E — external review** | Finish the already-running different-model review of the frozen SuperMind/Guo intake | Archive the exact conditional perimeter unless the reviewer names one load-bearing bounded gap. After closure, the first recommended handoff is the typed `PAIR-IR` receiver gate | External drafts are objects under review, never proof premises |
| **P — P1/P2 review** | Finish the already-running hostile P1/P2 review and reconcile any narrowed scope | If the trace formulas/collision survive or are independently re-derived, hand the same root to **one** hostile normalization gate: Nash Darboux prefilter, then exactly one of `TRACE-HAM`, derivation conductor, or `CAN-DIFF` | Zero unreviewed descendants before the review/re-derivation gate |

Queue order after those closures: `PAIR-IR` first; one normalization/derivation
discriminator second; a corrected D-gauge quotient or post-D2 structure test as
selected by D2; symbolic P4P1 audit when D is free.  The `A(F)` atlas/local-model
programme waits for its saturation and literature gates. Primitive groups and
odd-prime Witt remain fallback capacity, not current roots.

## 11. Coordinator synthesis and hard perimeter

The five reports do not change the conjecture's truth status. Their real joint
result is architectural:

1. **One receiver is now precise.** Target-affine-divisor-tagged completed
   factors with residue extensions, branch pairing, and coefficient
   convolutions are the minimum payload for the quadratic trace test.
2. **No source is yet proved to populate it.** GGV, pure books, and the D source
   owe three different functorial/provenance bridges.
3. **The D lane remains exactly one running child.** Every shift, Spencer,
   gauge, trace, integral, or deeper proposal is conditional or orthogonal.
4. **Canonical normalization is a source of exact objects, not yet a proof.**
   Trace dynamics, conductors, differents and asymptotic divisors are promising
   because they are falsifiable; each can still collapse to finiteness in new
   notation.
5. **External exact evidence preserves only the registered conditional
   perimeter.** Exact residual-system correctness and coordinate equivalence do
   not prove the GGV reduction/transcription bridge or derivational independence.

Until an active root closes, the legal action is harvest and review, not a new
launch.  No fixed-depth extension, band 28, integral D43, B=168, D75, new book
cell, generic sparse search, heavy Sage/container job, author contact, public
wording change, or msolve upstream action is licensed by this dedup.

---

**Frozen:** `2026-08-24T02:32:29Z`.  This report edits no shared ledger and
launches no descendant.
