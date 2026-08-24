# Post-collection mechanism dedup — round `20260824T0719Z-c17bd25`

Status: **FROZEN DEDUP / NO LAUNCH / NO PROMOTION**

This report compares the four completed blind submissions.  The fifth lane
timed out and is excluded; no partial fifth-lane text was read or counted.
Card counts below are therefore mechanism counts, not model-vote counts.

## 1. Population and canonical overlay

| Input | SHA-256 |
|---|---|
| sealed packet | `ef61e5d5fe8f58081b9b36602b5bf98a83f655b9836cefe93a5a355dd90c9a2d` |
| root | `e0be8593921b5e4c298f26756be4c5e36dd8cfade43e6227f0bfdae592dd146a` |
| zero-base | `34bf61674a0cd30357a2f55bb7b960ff508ddf659aa7824c6b73c31fe3888ffb` |
| Atlas | `838fca63549888e6fc28ae4af794be92adbfa9955636b637c8c8ae00b2155284` |
| Grok | `341d1582620eb8ef221cb03f5647d6aded2b12b9fc8d31ea5e918cf81f2c5248` |

After collection, the coordinator supplied two launch-critical canonical
corrections.  They do not add an ideation vote; they correct whether a card is
new:

| Canonical record | SHA-256 | Consequence |
|---|---|---|
| `xmodel/sol-hc4probe.md` | `2ab20f16a5fc7cd6d9bac22d606a080464ad0236f5ef7667dd6b04b3a7512eb7` | The first quintic post-top `GL_4` module and the Meng--Yang `5 -> 4` linear Schur descent were already executed; verdict `NO LEVERAGE` on the y-linear/JC2 sector. |
| `ladder/SHEET6.md` | `fc0b0a2de3d2c4b6c47d2b6434087c3edf17571b5f7e597be3025fdf5118a316` | Records Domrina's four-sheet general case and the established `td <= 5` exclusion. |
| `ladder/SHEET6-CAMPAIGN.md` | `084545dc6ad74b7d216914b9b9ed5de8d931c080fdaf286da746cf1758f0cd67` | Canonical survivor book likewise records `td <= 5: 0 (CLOSED)`. |

Thus the packet sentence that ranks at least four were untouched is
inconsistent with the campaign's canonical sheet-degree ledger.  The first
open topological/function-field degree is six, not four.  Blind convergence
on degree four is convergence inherited from a stale common premise, not
independent evidence.

## 2. Mechanism clusters

All twelve cards occur exactly once in this table.

| Cluster | Submitted cards | Actual common mechanism | Dedup call |
|---|---|---|---|
| **H: Hamiltonian cokernel** | root `HAMILTONIAN-MODULAR-RESIDUE`; Grok `HAMILTONIAN-WEIGHT-SLICE` | For unimodular `dP`, decide whether `1` lies in the image of the Hamiltonian derivation `D_P`.  Root's class `[div V] mod D_P` and Grok's complementary-row curl equation are the same obstruction up to sign. | **Near-duplicate core; merge as one root.**  Keep the weight/no-leak family test and the infinity-pairing proposal as different receivers, not two votes. |
| **P: universal pencil defect** | zero-base `DUAL-PENCIL-VANISHING-DIVISOR` | Push infinity vanishing cycles of all `aP+bQ` to an effective divisor on the dual target pencil and try to prove degree zero. | **Unique.**  Adjacent to H's proposed Gauss--Manin receiver, but not duplicate unless a typed map from the Hamiltonian class to this divisor is proved. |
| **B: boundary different** | root `BOUNDARY-DIFFERENT-PIN` | Compare the standard different/canonical-divisor identity with the boundary class map and ask for a principal relation. | **Unique but only a fail-closed preflight.**  Fold into P/global-boundary source checking; it is not an independent root unless it emits a genuinely new relation. |
| **N4: quartic normalization** | zero-base `QUARTIC-RESOLVENT-OPEN-CHART`; Atlas `N4-FILLING-NIELSEN`; Grok `MAPPING-DEGREE-FOUR` | All attack generic sheet degree four.  The first uses the cubic resolvent, the second source-meridian filling, and the third is a paper-first umbrella that can route into either. | QROI and Nielsen are mathematically distinct submechanisms, while Grok's card is an umbrella/near-duplicate.  **All are stale prior-art reproofs because `td=4` is already closed.  Do not launch.** |
| **C: HC4 quintic** | root `HC4-QUINTIC-SOURCE-GATE`; Atlas `HC4-QUINTIC-MODULE` | Replay the HC4-to-JC2 bridge and inspect the first quintic `GL_4` obstruction module. | **True duplicate, and duplicate of completed work.**  Neither card names a later observable beyond the already executed first post-top module/descent.  Canonical verdict is `NO LEVERAGE`; stop absent a genuinely new later layer. |
| **A: untwisted action closeout** | Atlas `ACTION-HOMOTOPY-QUOTIENT` | Quotient the primitive of `P dQ-x dy` by universal Jacobian/homotopy/tame relations to test whether any untwisted class remains. | **Unique negative-control formulation, not a research root.**  The other three reports independently adjudicate the same nominee downward: ordinary divisorial residues of the exact form vanish and the companion primitive is dependent. |
| **W: bounded Witt algebraization** | zero-base `AS109-SUPPORT-CANCELLATION-GRAPH`; Grok `TATE-HORIZONTAL-MIXED` | For the Artin--Schreier/Frobenius seed, decide whether mixed corrections can remain in finite polynomial support rather than escape along the all-Witt ray. | **Near-duplicate objective; merge.**  The Tate/gauge obstruction and exponent-interaction hypergraph are complementary discriminators inside one bounded-support root, not independent CE votes. |

### Exact equivalence inside cluster H

Choose a polynomial vector field `V` with `V(P)=1` and put
`D_P=P_y partial_x-P_x partial_y`.  Any other lift is `V+hD_P`, and

```text
div(V+hD_P) = div(V)+D_P(h).
```

Hence root's `kappa(P)=[div V]` is exactly the obstruction solved by Grok's
curl-correction equation.  Vanishing produces a divergence-free lift, hence
a polynomial Hamiltonian `Q` with `[P,Q]=1`.  The submissions differ only in
what they try next: a family-specific weight certificate versus a global
atypical-end functional.  They must share one source/identity gate and must
not be scheduled as two independent roots.

### Distinctions that must not be collapsed

- P is topological/microlocal data of the whole target pencil; H is an
  algebraic cokernel attached to one first component.  A hoped-for
  Gauss--Manin pairing does not yet identify them.
- The quartic resolvent and Nielsen filling objects are genuinely different,
  even though both are now campaign-stale.  A later degree-six redesign
  would require a fresh mechanism and cannot be inferred by replacing `4`
  with `6` in either card.
- In W, Grok's `p=3` calculation is only a cheap method/gauge control below
  known plane degree bounds.  Zero-base's `p=109` instance is the legal-degree
  falsification target.  A survivor at `p=3` is not a characteristic-zero or
  legal-degree CE signal.

## 3. Conflicts and their resolution

1. **Degree-four frontier.**  All four reports raised or targeted rank four
   because the packet said ranks at least four were untouched.  Domrina's
   general four-sheet theorem and the canonical `td <= 5` ledger override
   that premise.  No quartic card survives the dedup.
2. **HC4 priority.**  Root and Atlas budgeted a quintic module; zero-base kept
   it as reserve; Grok lowered it.  The completed `sol-hc4probe` is decisive
   for the cards as written: the named first layer has already returned no
   JC2-sector leverage.  A future HC4 proposal must name a later covariant or
   observable and explain why it avoids the factorization
   `C_11|_{y-linear}=2a_6a_5`; “one quintic module” is not enough.
3. **Action residue.**  There is no substantive disagreement.  Atlas permits
   a short quotient closeout, while every lane rejects it as a principal
   proof root.  Keep at most a coordination-owned retirement check.
4. **Hamiltonian versus pencil.**  These compete for some of the same
   infinity/Gauss--Manin expertise but make different mathematical bets.
   Share literature and controls; do not assume either result as a dependency
   of the other.
5. **Witt prime and representation.**  The prime choices are scopes, not
   rival claims.  Use small-prime Tate/gauge work only to validate or kill the
   invariant, and require a legal-degree frozen support before any CE-facing
   coefficient child.

The robust all-lane consensus is narrower than the apparent card count:
current weighted-D, fixed-row coframe, K3, unrestricted Witt continuation,
and untwisted action residues remain stopped; no new book cells or generic
sparse search is licensed.

## 4. Recommended unique candidate set

These are scheduling candidates only.  Nothing is launched here.

### 1. `HAMILTONIAN-COKERNEL/WEIGHT` — fastest exact discriminator

- **Merged from:** root H + Grok H.
- **Prerequisite:** freeze the sign conventions and source priority for
  `kappa(P)`, and replay the equivalence between `kappa(P)=0` and a polynomial
  Jacobian mate.
- **Cheapest decisive test:** after coordinate and Broughton controls, prove
  or refute a no-leak weight filtration for one provenanced unimodular family
  beyond the fixed Broughton row.  Do not widen to generic sparse `P`.
- **Outcomes:** a terminal recurrence gives a scoped family kill; a certified
  polynomial slice at legal degree gives a CE candidate for immediate hostile
  review; `NO-WEIGHT` or a merely classical restatement stops the family
  mechanism.  A universal infinity pairing is a later theorem, not assumed.
- **Why retained:** it has an exact algebraic object and the cheapest hostile
  controls of the surviving ideas.  Its two submissions collapse to one
  mechanism, but that mechanism remains campaign-new beyond the fixed row.

### 2. `DUAL-PENCIL-VANISHING-DIVISOR` — strongest universal proof bet

- **Source:** zero-base P, with root B used only as a boundary-different
  duplicate/control gate.
- **Prerequisite:** define a resolution-independent effective divisor for the
  universal pencil and source-check the zero-defect-to-coordinate endpoint.
- **Cheapest decisive test:** derive one degree/localization formula on a
  common resolution and replay identity, triangular/tame, Hénon, and
  Broughton controls.  First reduce every term against the standard different,
  pure-boundary, and no-log identities.
- **Outcomes:** presentation dependence, an automorphism control failure, a
  costume identity, or an uncontrolled positive boundary term stops the
  object.  A choice-independent zero formula is a provisional global lemma,
  not yet JC2.
- **Why retained:** it is the only surviving card built functorially from an
  arbitrary Keller pair and all target directions.  Its high sign/priority
  risk is exposed at the first paper gate.

### 3. `AS-p-BOUNDED-SUPPORT/POLE-ESCAPE` — orthogonal CE falsifier

- **Merged from:** zero-base S + Grok W.
- **Prerequisite:** freeze the nilpotent/triangular gauge and prove the
  exponent interaction enumeration is complete under the registered cap.
- **Cheapest decisive test:** use `p=3` only to falsify the Tate/gauge
  invariant cheaply, then apply the support-height/cycle discriminator to the
  fixed legal-degree `p=109` seed with at most eight correction monomials.
- **Outcomes:** an integral height closes the registered bounded-support motif;
  a gauge cycle is rejected; a genuine minimal cycle licenses at most one
  later fixed integral coefficient scheme.  No finite-Witt survivor implies a
  characteristic-zero point.
- **Why retained:** it is disjoint from the two infinity proof objects and is
  the only surviving card aimed at the explicit polynomial-algebraization
  bottleneck rather than another unrestricted Witt level.

If three producer slots are available, these three form a nonduplicative
portfolio: exact family obstruction, universal global proof receiver, and
bounded counterexample falsifier.  H and P may share source-control work but
must produce separate artifacts; W is orthogonal.

## 5. Coordination-owned closeouts, not roots

- **Boundary-different pin:** spend only enough paper effort to decide whether
  it is already the canonical-divisor line.  Fold any exact duplicate into P;
  promote nothing unless a new principal boundary relation is written.
- **Action homotopy quotient:** optional terminal audit only.  Stop on the
  first homotopy/tame/blowup dependence; do not launch Laurent-jet descendants.
- **Quartic cards:** archive as prior-art rediscoveries.  Do not retarget to
  degree six without a fresh all-46 or micro-round that names a degree-six
  mechanism and respects the existing sheet-six campaign.
- **HC4 cards:** archive as duplicates of the completed kill-probe.  Reopen
  only on a named later observable with a reason it can see the y-linear
  sector after the `a_6a_5` failure.

No shared ledger was edited, no computation or fleet job was launched, and no
proof or characteristic-zero counterexample is claimed.
