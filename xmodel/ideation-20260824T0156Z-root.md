# Blind ideation — root — round 20260824T0156Z-8bf25a5

- **Author:** `/root` (Sol Ultra)
- **Snapshot consumed:** only
  `xmodel/ideation-20260824T0156Z-packet.md` and its required inputs
- **Lifecycle:** blind strategy submission; no claim promotion
- **Main update:** the D program has earned a transition-locus test, while the
  raw boundary and contact-only proof packages have earned redesigns. The most
  promising new proof mechanism is to couple field trace to the two polynomial
  target derivations before returning to boundary coefficients.

## 1. Disposition vector over all 46 avenues

```text
 1 U   2 R   3 U   4 R   5 U   6 U   7 R   8 U   9 U  10 U
11 U  12 U  13 U  14 U  15 U  16 O  17 U  18 U  19 U  20 U
21 U  22 U  23 U  24 U  25 R  26 U  27 R  28 U  29 R  30 U
31 R  32 R  33 L  34 U  35 U  36 U  37 U  38 U  39 U  40 U
41 U  42 U  43 U  44 U  45 R  46 U
```

Legend: `U=unchanged`, `R=raise`, `L=lower`, `O=reopen`.

Reasons for every change:

- **2 raise — Sigray/Eggers--Wall.** P2 identifies completed branch pairing
  over a named affine target divisor as a concrete missing decoration rather
  than a generic plea for more boundary data; this makes one precise
  packet-sufficiency test possible, while leaving `G2-PSC` entirely open.
- **4 raise — formal-germ D series.** Different-model confirmation of a typed,
  D25-source-defined, pointwise one-band transition is the first evidence that
  the windows can be organized as an actual relative system rather than only
  unrelated depth censuses. The raise is from “depth mill” to “transition-locus
  experiment,” not toward a germ or counterexample claim.
- **7 raise — asymptotic variety.** TRACE-REG's correct perimeter is regularity
  along affine target divisors, not vanishing at target infinity. This puts the
  components of `A(F)` back into the role of canonical tags for completed local
  traces and monodromy grouping.
- **16 reopen — D-module/holonomic index.** The commuting target derivations
  extend uniquely to the finite separable field extension and commute with
  field trace. They generate a concrete differential system for trace/resolvent
  coefficients, which is far more specific than the inventory's previously
  unnamed “holonomic invariant.”
- **25 raise — monodromy/passports.** Contact-only passports are now known to
  omit the coefficient convolution entering quadratic trace, but inverse-
  branch pairing and residue-field orbits are exactly monodromy data. A
  coupled two-coordinate passport can be tested against a precise observable.
- **27 raise — links/splice boundary data.** The same target-divisor-tagged
  pairing supplies a falsifiable augmentation of the current splice/contact
  packet; topology alone still does not prove realizability.
- **29 raise — Hamiltonian/commuting frames.** The two polynomial derivations
  dual to `dP,dQ` are explicit commuting Hamiltonian-type fields, and applying
  them under field trace gives a new coupled regularity attack rather than the
  old unsupported demand that a field be locally nilpotent.
- **31 raise — integrality/Zariski Main.** The exact TRACE-REG equivalence fixes
  the target: eliminate affine-divisor poles of the characteristic
  polynomials of `x,y`. Zariski Main supplies a canonical finite normalization
  on which different/conductor and trace can be formulated without a GGV
  source.
- **32 raise — collision/elimination ideal.** Minimal polynomials and
  subresultants of `x,y` over `C(P,Q)` encode the same trace data globally;
  differentiating their coefficients offers a source-level alternative to
  matching Puiseux branches by hand.
- **33 lower — raw symplectic/action residues.** The exact P1 controls make the
  untwisted primitive poles and raw Fitting/Smith splits presentation costumes.
  Exactness remains useful inside the coupled differential system, but the raw
  invariant-budget proposal loses rank.
- **45 raise — differential Galois/Ore.** Both the proposed trace system and a
  possible D-tail transition module can be tested as finite differential/Ore
  modules. This is a concrete use unlike the old tautological inverse ODE.

All implication-ladder, generic sparse-search, finite-field-census, and
higher-dimensional-descent rows remain unchanged: the new evidence does not
repair their known structural defects. In particular, no negative P1/P2 result
is evidence for HC4, odd-prime Witt lifting, or generic SAT search.

## 2. Reranked bottlenecks

### Proof-side

1. **Canonical actual-map source plus completed pairing.** A proof needs either
   `G2-PSC` or a genuinely GGV-free normalization source, and then a way to
   group every completed inverse branch above the same affine target divisor.
   Contact trees without coefficients are now demonstrably too coarse for the
   quadratic trace observable.
2. **A non-tautological regularity law.** Full first-`d` trace regularity is
   exactly finiteness. The missing step is a Keller-specific identity that
   rules out affine-divisor principal parts without assuming finiteness in new
   words.
3. **Complete landing/coverage and cofinal control.** Even a local boundary
   contradiction on one residue-A book cannot settle JC2 until every actual
   counterexample lands, and type-relative KJN does not bound all types.
4. **Certificate correctness is secondary but mandatory.** External exact
   terminals may repair bounded exclusions; they do not supply the global
   reduction/transport theorem.

### Counterexample/disproof-side

1. **Coherent transition locus, not another depth.** Determine whether the
   pointwise D25-to-D27 signal extends to a positive-dimensional source-defined
   base locus with exact lifts. This is the sole justified D descendant.
2. **Finite-state tail law.** If a coherent cell exists, decide whether the
   entire later obstruction sequence admits a finite transfer/Ore description.
   Without such a theorem, more modular depths are measurements, not a formal
   germ.
3. **Characteristic-zero and algebraization bridges.** Even a compatible
   inverse system over finite fields is not a common integral point; even a
   characteristic-zero formal germ is not a polynomial Keller map.
4. **Orthogonal disproof reserve.** Odd-prime Witt lifting remains the best
   conceptually independent counterexample search, but no new evidence moves
   it ahead of the reviewed D transition this round.

## 3. Idea cards

### Card A — `TRACE-HAM`: coupled trace equations under target derivations

- **Target claim.** Prove, or cheaply falsify, that the Keller equations force
  the affine-divisor principal parts of the characteristic-polynomial
  coefficients of `x` and `y` to vanish.
- **Avenues.** 7, 16, 29, 31, 32, 33, 45.
- **Novel mechanism.** Let `K=C(P,Q)`, `L=C(x,y)`, and `J(P,Q)=c`. The two
  target derivations extend to `L` as

  ```text
  delta_P = c^-1 (Q_y d/dx - Q_x d/dy),
  delta_Q = c^-1 (-P_y d/dx + P_x d/dy).
  ```

  They commute, and for a finite separable field extension field trace should
  commute with them. Hence, before module-finiteness,

  ```text
  delta_P Tr(x^m) = (m/c) Tr(x^(m-1) Q_y),
  delta_Q Tr(x^m) = -(m/c) Tr(x^(m-1) P_y),
  ```

  with analogous equations for `y` and mixed monomials. Package a finite
  resolvent/Bezout basis into a first-order differential system over `K` and
  study its singularity along an irreducible component of `A(F)`. This couples
  the two coordinates and the full Jacobian equation; P2's free one-coordinate
  completion collision did not.
- **New evidence used.** P2 gives the exact affine-divisor perimeter, proves
  that `m=1,2` alone is not an integrality criterion, and identifies the
  coefficient convolution lost by contact data. P1 says not to seek the
  missing law in untwisted primitive residues.
- **Dependencies/evidence tier.** The derivation-extension and trace-commutation
  lemmas require an independent exact proof; separability is available over
  `C`. No Sigray or D-series packet is a premise. Any boundary specialization
  must use all local factors above the same target divisor.
- **Cheapest discriminator.** In one day, derive the resolvent differential
  system abstractly for degrees `d=2,3`, replay it on a triangular
  automorphism and `(x^2,xy)`, and ask whether a paired formal local solution
  can reproduce the P2 residue collision while satisfying both coordinate
  equations and `J=c`. Use coefficient indeterminates, not fitted samples.
- **Outcomes.** A regular-singular system whose indicial constraints force all
  negative characteristic coefficients to zero is a real proof lead and can
  be lifted to symbolic `d`. A coupled formal pole solution kills the local
  mechanism and identifies the additional global input needed. Failure to
  close the mixed-trace basis means the proposal is merely TRACE-REG in a
  larger vocabulary and is stopped.
- **Cost/time.** Six-hour algebra gate; one-day exact prototype; local CAS only.
- **Stop condition.** Stop after two representations if no finite closed
  system or decreasing filtration is exhibited. Never infer regularity from
  residue-only cancellation.
- **Expected information gain.** High: it tests whether the Jacobian actually
  supplies content beyond the trace/finiteness equivalence, with a formal
  countermodel available as an honest negative result.
- **Resurrection trigger.** A canonical finite trace basis from the ZMT
  normalization, a simple-pole theorem, or a new boundary identity coupling
  `x` and `y`.
- **Hostile attack.** The mixed traces may proliferate until the system is just
  the full multiplication algebra, making its regularity exactly finiteness.
  The finite-closure gate is therefore mandatory and precedes theorem work.

### Card B — `D-TRANSFER`: source transition module after `D2-CELL26`

- **Target claim.** Decide whether the D source equations have a coherent
  compatible tail on the one promoted cell, without paying for isolated fixed
  depths.
- **Avenues.** 3, 4, 16, 38, 45, 46.
- **Novel connection.** Treat the bandwise Schur/cokernel maps as coefficients
  of a transfer or Ore module. The exponent semigroup and first-occurrence
  registry may make the infinite lower-triangular recurrence finitely
  generated after a transient. A Smith/annihilator computation in the shift
  variable would then decide an entire tail class: torsion can obstruct it;
  a free summand can parameterize compatible formal tails.
- **New evidence used.** D1 proves that a typed projection exists and that its
  fiber/cokernel behavior varies on the D25 base. The nonzero later residuals
  at bands 30/36/40 explicitly prohibit calling the six band-26 directions
  persistent.
- **Dependencies/evidence tier.** `D2-CELL26` is already running and is the
  only child. This card launches no work unless D2 returns a reviewed
  positive-dimensional coherent locus. It uses the unreduced source compiler,
  not D43 NF data.
- **Cheapest discriminator.** First prove a finite-state/type theorem for the
  source support and transition registry. If that gate passes, generate the
  symbolic transition operator, verify it against the existing bands, and
  compute a module rank/annihilator. No interpolated recurrence is acceptable.
- **Outcomes.** Torsion/empty inverse limit is a proof-side kill scoped to the
  cell. A nonzero free module gives a formal counterexample lead only. Prime
  split, growing state, or a fitted recurrence is `NO-FINITE-TRANSFER` and
  stops the lane. Neither outcome supplies characteristic zero or
  algebraization automatically.
- **Cost/time.** Type theorem: six hours. Prototype: one day local exact
  algebra; AWS only after a bounded matrix and memory forecast exist.
- **Stop condition.** Do not sample another fixed depth merely to guess a
  pattern. Do not start integral D43, band 28, or Hensel work until D2 and any
  transfer claim have different-model review.
- **Expected information gain.** Very high conditional on D2 coherence: this
  is the first plausible conversion of “survives at depths” into an actual
  inverse-system question.
- **Resurrection trigger.** A proved periodic source registry, rational
  generating function, or common integral coherent D2 locus.
- **Software acceleration.** One source compiler should emit transition rows,
  pivot strata, cokernel functions, provenance hashes, and later the transfer
  operator; one verifier replays every emitted layer. This prevents another
  family of incompatible one-off D engines.
- **Hostile attack.** New coefficient types may appear without bound, so the
  supposed finite transfer state may be false. That is why finite generation
  is the first theorem, not an inference from two or three depths.

### Card C — `PAIR-FINGERPRINT`: information lower bound for `G2-PSC`

- **Target claim.** Determine whether the recorded GGV/Sigray packet can
  identify the target-divisor grouping and completed branch pairing needed by
  even the quadratic trace observable.
- **Avenues.** 1, 2, 7, 25, 27, 31, 38.
- **New connection.** Replace the vague “same packet, different tree” test by
  a precise observable: for every source place above an affine target divisor,
  record enough paired coefficients to compute

  ```text
  sum_w e_w Tr_{kappa_w/kappa_v}
      (sum_{r+s=-e_w} a_(w,r) a_(w,s)).
  ```

  Ask whether the existing packet determines this value. If not, record the
  smallest augmentation that does, and separately ask whether that augmented
  object has an actual-map source functor.
- **New evidence used.** P2 supplies an exact completion collision for the
  current contact-only data and identifies the varying slot beyond the retained
  level. The collision is not itself an actual Keller/source collision, so it
  is only the schema-level starting point.
- **Dependencies/evidence tier.** A schema-level collision kills only a claim
  that the schema alone determines the observable. Killing `G2-PSC` for actual
  maps additionally requires both sides to lie in the proved source domain.
  Pure Sigray work cannot import GGV restrictions.
- **Cheapest discriminator.** Formalize the exact current packet as a typed
  serialization, construct the P2 pair inside that type, and run an injectivity
  collision search. Then identify which coefficient/pairing tag first separates
  it. Stop before book enumeration or positivity.
- **Outcomes.** A collision proves a precise information lower bound and blocks
  any transport theorem using only the old packet. A unique match on one case
  proves nothing global but yields a candidate augmentation. If the packet
  cannot be typed without importing the desired tree, declare `NO-SOURCE-
  SCHEMA`; that is itself the current `G2-PSC` gap exposed cleanly.
- **Cost/time.** Four-hour schema gate, then at most one day of exact bounded
  enumeration. No AWS.
- **Stop condition.** One collision ends the old-packet test. No new Sigray
  book cells and no claim that the trace observable alone determines the full
  tree.
- **Expected information gain.** Medium-high: it can retire an underspecified
  bridge cheaply or turn “need more data” into a minimal, testable contract.
- **Resurrection trigger.** A proved GGV-to-normalization functor or an actual
  source pair with identical augmented fingerprints.
- **Hostile attack.** The P2 collision may exploit completions that no Keller
  source can realize. The report must keep “schema insufficiency” separate from
  “actual-map transport refuted.”

## 4. Major-lane calls

- **D series — continue under redesign.** Finish only `D2-CELL26`. If coherent
  and reviewed, try the finite-state theorem before any further depth or
  integral D43 engineering. Otherwise stop the cell or repair its typing.
- **GGV/Sigray — redesign, do not expand.** Preserve the hybrid/pure fork. Run
  at most the typed `PAIR-FINGERPRINT` information test; no book-cell census.
- **Boundary/trace — stop raw passports; reopen coupled trace only.** P1's raw
  invariant budget and an `m=1,2` TRACE engine stop. `TRACE-HAM` is permitted
  because it adds the missing coupled field dynamics and has a hard closure
  test.
- **Local DIR/KJN and A-SCALE/G2-BD — stop as critical paths.** Keep them as
  adversarial controls until actual-map provenance supplies the missing global
  source/type theorem.
- **External artifacts — finish review, then archive exact scope.** Repair
  public wording only with human authorization. Do not count repositories or
  model labels as independent proofs.

## 5. Proposed four-root portfolio

| Root | Allocation | Immediate state | Gate |
|---|---:|---|---|
| **C** coordination/review | 15% | integrate reviews, hashes, claim DAG; keep AWS idle | zero unreviewed descendants beyond D2 |
| **D** transition locus | 35% | `D2-CELL26` already running; nothing else | reviewed coherent cell or scoped stop |
| **T** coupled trace | 30% | design `TRACE-HAM` finite-closure test; launch only after P review harvest | finite closed system or formal coupled pole countermodel |
| **S** source/pairing | 20% | type `PAIR-FINGERPRINT`; no book expansion | collision, minimal augmentation, or `NO-SOURCE-SCHEMA` |

Different-model review runs in the background and preempts T/S launch if it
reverses a premise. External evidence is a review object under C, not a fifth
mathematical root. Box02/03 remain stopped; box01 should not receive a solver
job from this portfolio.

## 6. Hidden assumptions and invalidators

Shared hidden assumptions:

1. A finite closed trace/transition representation exists; both leading cards
   explicitly test rather than assume it.
2. Formal source or boundary packets reflect actual polynomial-origin maps;
   schema countermodels do not establish actual-map independence.
3. Modular agreement at two primes predicts characteristic-zero geometry;
   it does not, absent an integral model and flatness.
4. The chosen compactification/normalization and target divisor tags are
   choice-independent enough to support a global statement.
5. Complete landing/coverage and a cofinal type ceiling will eventually be
   available; no local success supplies either.

Events invalidating this ranking include: hostile reversal of D1; a D2 typing
failure; a Claude finding that the P2 collision changes retained data; an
external replay failure or genuinely independent unconditional proof; a new
actual-map source/transport theorem; or a coupled formal Keller completion
showing `TRACE-HAM` has arbitrary poles. In each case, unrelated roots continue
and the affected descendants are quarantined by the claim DAG.
