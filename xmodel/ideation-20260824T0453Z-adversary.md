# Hostile cross-pollination report — round `20260824T0453Z-dd11599`

Status: **FROZEN ADVERSARIAL SYNTHESIS**.  Blind collection was already closed
before this comparison.  Fable missed the cutoff and was cancelled, so the
comparison population is exactly the five frozen submissions listed below.
Nothing in this report launches work, promotes a claim, edits a shared ledger,
or changes the sealed packet.

## 0. Snapshot, read perimeter, and integrity correction

- **Model:** OpenAI Codex (GPT-5), hostile/falsifier lens.
- **Clean basis:** `dd11599b07eb05591b5c006791005eef19457d8e`.
- **State cutoff:** `2026-08-24T04:53:35Z`.
- **Packet:** `xmodel/ideation-20260824T0453Z-packet.md`, SHA-256
  `042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5`.
- **Files read for cross-pollination:** only that packet and the five frozen
  submissions below.  The required packet inputs had already been read in
  full at the packet-prescribed scopes during the blind falsifier pass.  No
  other `ideation-20260824T0453Z-*.md` file was inspected.

| Frozen submission | Verified SHA-256 |
|---|---|
| `xmodel/ideation-20260824T0453Z-root.md` | `97222d63837c4b883e94c8d667014872603b67f5663a1c86e2b1063a1435b1bc` |
| `xmodel/ideation-20260824T0453Z-atlas.md` | `0e381be9a5f1b4d7e2976f473d3d038a3dd591789bdd9f5f4fc2368c0ce374b7` |
| `xmodel/ideation-20260824T0453Z-zero-base.md` | `fb804efab0c2cff524512fb7f81cceb2adaea7cce299a827211310c22052ba9a` |
| `xmodel/ideation-20260824T0453Z-falsifier.md` | `12d1fe67a1dc7be75041050be3009d8599578e10c6cb1b57d1da12ecfa800962` |
| `xmodel/ideation-20260824T0453Z-grok.md` | `6a7010e0d71d6bac03171e1b164a70668352d896b0da248fdb689c13494f7136` |

The packet's `AUDIT.md` digest is a one-character transcription defect.  It
lists the 63-character string

```text
a0033b88030fbd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

whereas the actual clean-basis SHA-256 is

```text
a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

The missing `0` is after `...030f`.  The packet remains sealed and unedited.
Grok caught this defect.  Atlas, zero-base, and falsifier each say in their
read records that every packet hash matched; those statements are false for
this one row and should be corrected in provenance, not silently read as a
different mathematical input.  This integrity defect does not itself change
the contents of `AUDIT.md` or any mathematical verdict below.

## 1. Executive hostile verdict

The five reports contain fewer independent mechanisms than their fifteen
cards suggest.  After deduplication there are three leading objects, one
useful narrow allocator, three high-level reformulations, and three proposals
that should be rejected in their submitted form.

| Rank | Fingerprint | Cross-report source | Verdict |
|---:|---|---|---|
| 1 | `EXACT-COFRAME/E2` | root C | **Keep, corrected.**  It gives a logically sound direct counterexample certificate if non-`E_2` membership is certified. |
| 2 | `LOCAL-K3/COMPACTNESS` | atlas C + zero-base C | **Merge and keep.**  Fixed-degree local generic-fibre detection is the honest bridge that another Witt level lacks. |
| 3 | `FINITE-COMPLETION-PAIR` | zero-base B + falsifier 1 | **Merge and keep as a two-sided sieve.**  The exact object is global; the proposed class/different tests are necessary, not sufficient. |
| 4 | `WEIGHTED-R/HANKEL` | atlas B + falsifier 3 | **Compose, queue.**  Quotient first, then test the declared linear state category; do not infer arbitrary finite-state impossibility. |
| 5 | `MICROLOCAL-DEFECT` | atlas A + zero-base A | **Deduplicate and defer.**  The canonical receiver is useful, but conormal vanishing is presently properness in microlocal notation. |
| 6 | `UNIT-INFINITY` | falsifier 2 | **Keep only as a negative control.**  It exactly kills the natural triangular Tate lift, not all lifts of its special fibre. |
| 7 | `ITERATED-LOG-VOLUME` | root B | **Defer at theorem gate.**  A finite algebraically stable boundary state is the missing cofinality theorem renamed. |
| 8 | `DIFF-LATTICE-UNIT` | root A | **Defer/absorb into completion-pair audit.**  The determinant divisor lands in a class group, not automatically in a principal unit relation. |
| 9 | conductor / mixed-Ritt / sidecar-line | grok A/B/C | **Reject as submitted.**  The conductor model is wrong, lift uniqueness is false, and the sidecar comparison is not typed on a common source. |

The strongest direct disproof idea is therefore root's exact-coframe card,
not the conductor or a mixed `W_2` census.  The strongest bounded
characteristic-lifting discriminator is atlas's local coefficient scheme
after merging zero-base's compactness lemma and falsifier's triangular unit
control.  The strongest global proof/counterexample object is the common
finite-normalization/open-chart pair, not a raw boundary passport.

## 2. Fingerprint deduplication and genuine compositions

### 2.1 One completion mechanism, not three votes

Zero-base B and falsifier `COMP-PAIR` have the same mathematical fingerprint:

```text
A=C[u,v]  ->  Cbar=normalization_A(L)  ->  B=C[x,y]
                 finite                    affine open
```

with `X=Spec(Cbar)`, `U=Spec(B)=X\D`, and the finite map
`pi:X->A^2`.  The finite-free multiplication-algebra language of zero-base
and the class/different/open-chart certificate of falsifier are two
descriptions of one object, not independent evidence.  Root's differential
lattice and grok's conductor are adjacent attempted invariants of the same
open immersion.  Only the former has a potentially repairable question; the
latter is algebraically broken.

The genuine composition is: construct or constrain the honest completion
pair first; then ask whether its derivation lattice produces a *principal*
boundary relation.  Starting from a meromorphic lattice and announcing that
its stabilization gives finiteness merely reverses that dependency.

### 2.2 One microlocal defect mechanism, not two votes

Atlas's cone

```text
Cone(RF_! Q[2] -> RF_* Q[2])
```

and zero-base's trace-zero middle extension are two realizations of the same
missing-sheet/vanishing-cycle receiver.  Fourier--Laplace versus inertia does
not make them orthogonal.  Both need the same absent theorem: the infinity
conormal contribution of a nonproper Keller map vanishes.  They should be
one provisional root, if retained at all, with one control ledger.

### 2.3 The legal Witt composition

Atlas C supplies the finite-type local scheme at the degree-three
Artin--Schreier point.  Zero-base C supplies the exact fixed-degree compactness
lemma explaining why an all-precision branch is decisive.  Falsifier
`UNIT-INFINITY` supplies a mandatory negative control: the displayed
triangular branch cannot reach characteristic zero polynomially, so any
generic branch must turn on genuinely mixed terms.  These mechanisms compose
because they act on the same fixed coefficient scheme at successive logical
layers.

Grok's mixed `W_2` census does not add another layer.  It only explores the
tangent/thickened special fibre already known to be nonempty and cannot tell
whether the local component is vertical.  Its proposed `W_3` child is exactly
what the sealed state stopped unless boundedness was frozen; the local
generic-fibre question dominates it.

### 2.4 The legal D-source composition

Atlas's exact change of unit coordinates

```text
C=U_g/U_f,       R=U_f^3/U_g^2,
U_f=R C^2,       U_g=R C^3
```

and falsifier's source-only minimal-state test genuinely compose: quotient by
the `(2,3)` common-carrier action first, then measure the state required by
the intrinsic stream `R`.  At first order `R-1` has coefficient
`3 alpha_1-2 beta_1`, explaining the reviewed sidecar without setting it to
zero.  This is a useful allocation gate, but it must stay in the category of
the specific linear/Ore representation being tested.

Grok C does not compose with this yet.  Its proposed question whether the
sidecar is in the span of six compatibility functions is ill-typed until all
seven functions are pulled back to one producer-certified source ring and
one tangent space.  Values from a stored graph witness and a row-42 source
form are not automatically comparable coordinates.

## 3. Mathematical stress tests and corrections

### 3.1 Exact coframes and non-elementarity: sound implication, unsafe quotient language

Let

```text
M = ((a,b),(c,d)) in SL_2(C[x,y])
```

with `a_y=b_x` and `c_y=d_x`.  Polynomial de Rham exactness on `A^2`
integrates the rows to `dP` and `dQ`; hence `M=J(P,Q)` and `[P,Q]=1`.
The counterexample implication is sound:

1. every plane polynomial automorphism is tame;
2. the Jacobian of a determinant-one affine or triangular generator is
   elementary after a constant `SL_2(C)` factor;
3. substitution preserves a product of elementary matrices; and
4. the chain rule therefore puts the Jacobian of every determinant-one plane
   automorphism in `E_2(C[x,y])`.

Thus a closed-row matrix in `SL_2(C[x,y])` with a valid certificate
`M notin E_2(C[x,y])` integrates to a characteristic-zero polynomial Keller
nonautomorphism.  This is the cleanest direct certificate in the round.

Four corrections are load-bearing.

- Do not call `SL_2/E_2` a quotient group or a “class” without proving the
  needed normality or specifying a pointed Mennicke orbit.  In unstable rank
  two, `E_2` is not automatically a normal subgroup.  Plain nonmembership and
  the double orbit `E_2 M E_2` suffice.
- Left/right multiplication by registered elementary matrices preserves
  nonmembership: if `E_L M E_R` were elementary, so would `M` be.  Arbitrary
  degree-two “corrections” do not preserve a Cohn/Mennicke certificate.  The
  family must be parameterized entirely inside a certified double orbit, or
  each output needs a fresh non-elementarity proof.
- `M in E_2` is not an automorphy certificate for an arbitrary exact coframe.
  Non-`E_2` is a sufficient obstruction to automorphy, not an equivalence.
- The tame-to-elementary chain-rule lemma should be written and independently
  checked before elimination.  It is short, but it is the direct bridge from
  matrix membership to JC2.

**Cheapest separator.**  Freeze the standard Cohn matrix and one bounded
family `E_L C E_R`; impose only the two curl equations, since determinant and
non-`E_2` membership are then automatic.  First check the linearized curl map
on this double orbit.  Only a nonempty exact tangent target licenses one small
elimination.  A survivor is integrated and rechecked directly; a unit ideal
closes only this bounded orbit.  No random support expansion is licensed.

### 3.2 Differential lattice/unit: the class-group gap is the theorem

The exact Keller setup does provide two commuting target derivations on
`B=C[x,y]` forming a polynomial frame.  Their extension to the finite field
extension can have poles on `D=X\U`.  What does not follow is root A's
determinant-line dichotomy.

For a normal completion pair with `B^*=C^*` and `Cl(B)=0`, the localization
sequence gives, under the stated divisorial hypotheses,

```text
Z[D_1] direct-sum ... direct-sum Z[D_r]  ~=  Cl(X).
```

This says precisely that a nonzero divisor supported on the boundary is *not*
principal.  A pole-order determinant that merely produces a boundary divisor
or a class in `Cl(X)` is therefore expected and yields no unit.  To contradict
`B^*=C^*`, the recurrence must produce a nonzero **principal relation** among
the `D_i`; factoriality of `B` does not supply one on `X`.

The other branch—“pole orders stabilize, giving a coherent integrable
`A`-lattice and hence finiteness”—is also where finiteness can be smuggled in.
A coherent meromorphic lattice on finite `X` is cheap; a lattice simultaneously
stable under the two derivations with bounded poles and strong enough to make
`B` finite over `A` is essentially the missing boundary-removal theorem.
Neither local SNC coordinates nor the one-dimensional forbidden-unit control
settles the global class relation.

**Disposition.**  Do not allocate an independent root.  In the completion-
pair root, ask the sharply weaker question: does derivation stability force a
specific integral vector in the kernel of
`Z^r -> Cl(X)`?  Since that kernel is zero for an honest counterexample pair,
one nonzero sourced vector would be decisive.  Stop if the output is only a
class, a bounded-pole lattice, or an assertion that such a lattice implies
integrality.

### 3.3 Iterated log-volume: finite-state cofinality in dynamical notation

The identity `F^*(dx wedge dy)=dx wedge dy` is exact.  On a resolution of one
iterate it can be combined with the canonical-divisor/ramification formula.
The unproved step is that all iterates act on one finite divisor cone with
functorial pullback and no accumulating indeterminacy.  If successive
resolutions add valuations, the proposed Perron--Frobenius matrix is exactly
the packet's missing absolute/cofinal type bound in new notation.

Even on a fixed rational model, the ramification recurrence can be a
tautological rewrite of the divisor of the invariant form.  A simple hostile
control is the rational map

```text
H_d(x,y) = (x^d, y/(d*x^(d-1)))       (d > 1).
```

It has rational Jacobian determinant one and generic degree `d`, hence
preserves `dx wedge dy` while having nontrivial dynamics and boundary poles.
Any cone argument using only invariant log-volume and nonnegative
ramification must accept this control.  The contradiction, if one exists,
must visibly use polynomiality and absence of finite poles, not volume alone.

**Cheapest separator.**  Before a matrix checker, prove either (i) a finite
algebraically stable compactification theorem specialized to polynomial
Keller maps, or (ii) a valuation-space identity that does not truncate the
Riemann--Zariski boundary.  Then replay `H_d`.  If the proof assumes bounded
blowup type, algebraic stability, or properness, record `COFINALITY-RENAME`
and stop.  Linear feasibility on promoted finite books is not evidence that
the required cone is complete.

### 3.4 The conductor card: fatal orientation/use error

For `Cbar subset B`, the standard conductor is

```text
(Cbar:B) = { c in Cbar : c*B subset Cbar }.
```

Writing the set inside `B` does not enlarge it, since the condition with
`1 in B` already forces `c in Cbar`.  It is an ideal of both rings when the
usual hypotheses hold.  But conductors detect finite birational extensions;
the Zariski--Main open immersion `Spec(B)->Spec(Cbar)` is normally not finite.
For the elementary localization `A subset A_f` in a Noetherian domain with
nonunit `f`, the conductor is generally zero: an element divisible by every
power of `f` must vanish.  Its vanishing set is then all of `Spec(A)`, not the
deleted divisor.  Therefore the submitted claim that this ideal cuts out
exactly the complement is false.

The advertised control `(x^2,xy)` is also misdiagnosed.  The map is not
quasi-finite along `x=0`, so it is not a Keller/Zariski--Main open-immersion
control.  Its nonproperness set contains, and in fact is, the target line
`u=0`: take `x->0` and `y->v/x` to approach any `(0,v)` from infinity.  It is
not supported only at the origin.

`(Cbar:B)=B` would tautologically force `B=Cbar`, but the conductor supplies
no usable boundary ideal in the nonfinite case.  Polynomial primitives of
ad hoc generators do not repair this and re-enter the recorded `COSTUME`
failure unless a global source functor is supplied.  Reject grok A rather
than merging it into the completion-pair root.

### 3.5 Mixed Witt and Ritt: uniqueness is explicitly false

The claimed uniqueness of determinant-one lifts in the slice
`P in R_n[x]`, `Q in y R_n[x]` holds only after `P` itself is frozen.  If
`R_n=Z/p^n` and the special polynomial is `P_0=x-x^p`, then for every
polynomial `A(x)` one may set

```text
P = x-x^p + p*A(x),
q = (P')^(-1) mod p^n
  = sum_{j=0}^{n-1} (-(P'-1))^j,
Q = y*q(x).
```

Because `P'=1+p*h(x)`, the displayed inverse is polynomial modulo `p^n`, and
`J(P,Q)=P'q=1`.  These are generally distinct lifts with the same reduction.
Taking, for example, `A=x(x-1)` also preserves the marked collision at
`(0,0)` and `(1,0)`, so the collision condition does not rescue uniqueness.
If `P=x-x^p` is frozen exactly, then `q=(1-px^(p-1))^{-1} mod p^n` is indeed
unique; that much is just inversion of a unit.

The characteristic-zero restricted slice needs no Ritt theory.  If
`P=P(x)` and `[P,Q]=1` over a characteristic-zero field, then
`P'(x) Q_y(x,y)=1`; both factors are polynomial, so `P'` and `Q_y` are
constants and the map is triangular/affine in the relevant coordinate.
What fails is the bridge from `P_y=0 mod p` to `P_y=0` in characteristic
zero: arbitrary `p`-multiple mixed terms disappear on reduction.  A Ritt
decomposition of the special fibre cannot forbid them.

Consequently a mixed degree-three `W_2` census mostly measures tangent
thickness, which is already known to be nonzero.  It cannot decide whether
the component is vertical, and the family above predicts many survivors.
Do not spend the one speculative generation on another finite level.

The corrected exact object is atlas's localized ring `R=(K_3^coll)_s`.
Faithful flatness of completion gives

```text
R_hat[1/3] != 0   <=>   R[1/3] != 0,
```

and a prime avoiding `3` contracts to a finite-type characteristic-zero
solution, hence transfers to `C`.  If the generic fibre is zero, the exact
certificate is local: `3^N=0` in `R`, equivalently
`h*3^N` lies in the global defining ideal for some `h` outside the chosen
special prime.  It is not necessarily the unlocalized assertion
`3^N in I`.  Fitting or tangent data alone are not a positive generic-branch
certificate.

### 3.6 Microlocal defect: canonical receiver, circular vanishing theorem

The two microlocal cards improve on local contact passports because their
objects are canonical and retain global monodromy.  That is a legitimate
receiver design.  No submitted argument, however, makes the decisive
conormal coefficient vanish.

`d(aP+bQ)` having no affine zero only says every vanishing cycle is at
infinity.  It does not say there are none.  The Broughton polynomial
`x+x^2 y` is a standard elementary control: its gradient has no common zero,
yet its fibres have atypical behaviour at infinity.  The Keller frame gives
a two-parameter strengthening, but the report still owes the theorem that
this strengthening cancels the infinity term without assuming properness.

There is also a flatly false proposed control in atlas A: there is no known
characteristic-zero three-dimensional polynomial Keller counterexample.
The Jacobian conjecture is open in dimension three as well.  Such an object
cannot be a mandatory “dimension-free refuter.”  Replace it with explicit
nonproper open immersions, non-Keller quasi-finite maps, Broughton's
critical-point-free polynomial, and rational volume-preserving maps; none is
a Keller counterexample, so each tests only the claimed intermediate index
lemma.

Before positivity, one must prove all of the following at the stated level:

1. the support/equivalence relating `Cone(RF_!->RF_*)` to nonproperness in
   this quasi-finite setting;
2. the relevant perverse cohomological concentration, so alternating
   constituents cannot cancel;
3. control of irregular Fourier terms at infinity; and
4. a local formula turning trace-zero conormal multiplicity into inertia or
   conductor without an unmeasured boundary correction.

Singular support contained in the zero section says that a constituent is a
smooth local system; by itself it does not make its rank one.  A constant
local system of rank `d` is still zero-section-supported, so atlas's generic-
rank-one conclusion also needs the trace splitting, connectedness, and the
missing concentration/extension argument.

“No conormal component” then implies degree one only after these bridges and
extension of the finite étale cover are proved.  As submitted, the desired
zero coefficient is the missing properness theorem, not a consequence of
characteristic-cycle nonnegativity.  Deduplicate the cards and defer them
until one exact open-immersion calculation leaves a Keller-specific term of
known sign.

### 3.7 Finite completion pair: exact deductions, insufficient search invariants

The merged zero-base/falsifier object survives hostility better than the
boundary slogans.  For a hypothetical Keller counterexample:

- the normalization `Cbar` is finite over `A=C[u,v]`;
- a normal two-dimensional ring is Cohen--Macaulay, and the finite module is
  maximal Cohen--Macaulay over regular `A`; local Auslander--Buchsbaum plus
  Quillen--Suslin makes it finite free;
- `Cbar^*=B^*=C^*`; and
- the divisor localization sequence makes the divisorial boundary components
  a free basis of `Cl(X)` because `Cl(B)=0` and there is no unit relation.

These are exact conditional deductions, subject to checking the open
complement and codimension-one components.  A purely codimension-two missing
set cannot persist between these normal affine models without a Hartogs/ring
equality issue, so it is not an escape from the divisor audit.

The candidate contract must explicitly require `pi|_U` to be étale (or direct
constant-Jacobian verification); finite `pi` plus `U~=A^2` does not imply it.
On singular `X`, canonical/different claims must use the dualizing module and
the correctly oriented codifferent.  The class-group basis and effective
ramification vector are necessary conditions, not evidence that an affine
`A^2` chart exists.  Conversely, finding an abstract finite-free algebra with
the right trace matrix is not a counterexample until mutually inverse chart
maps and the recovered `P,Q` are verified.

This architecture is still at risk of restating JC2: “no finite cover admits
an étale `A^2` open with nonempty boundary” is exactly the desired theorem.
Its value comes only from a strictly weaker, independently computable
class/canonical obstruction.

**Cheapest separator.**  First write a theorem-grade proof of finite
freeness, the unit exact sequence, and the dualizing/different convention.
Then test the one-boundary monogenic rank-two and rank-three schemas on paper.
The outcome must be either an explicit kernel relation in the free boundary
class group, an exact no-go restricted to those ranks, or an honest open-chart
candidate.  Stop before higher ranks if the equations simply say “the open
restriction is finite/étale.”  Do not count zero-base B and falsifier 1 as two
independent portfolio roots.

### 3.8 Weighted unit quotient and Hankel rank: good allocator with a narrow scope

The formulas for `C,R` and the tangent `3 alpha_1-2 beta_1` are exact.  What is
not exact is that the formal common-carrier action is the actual normalized
polynomial-source action at every weight, that `C` is triangularly absorbed,
or that `R` has only one source stream.  Those are exactly what the first two
source occurrences must test.

Hankel rank characterizes finite **linear/recognizable** representations over
a fixed coefficient category.  Growing minors can refute the declared
linear/Ore state or a claimed rational generating series.  They do not by
themselves rule out every nonlinear finite-state parametrization, nor may
they treat all future `alpha_N,beta_N` as independent without reading the
actual source registry.  The general coefficient claimed in falsifier 3 is a
conjectural extrapolation beyond the reviewed row 42 until derived from the
unreduced product.

**Cheapest separator.**  Pull the actual producer expressions into `(C,R)`,
compute the first two source-defined x-side occurrences, and make one of four
exact returns: `NO-QUOTIENT`, `TWO-DRIVER`, a new certified linear Hankel
pivot, or a complete sourced recurrence in the stated category.  Stop there;
no band-28, D43, or syzygy continuation.  This is a high-value queued
allocator, but it loses a portfolio slot to the three more global objects.

### 3.9 Unit at infinity: exact slice kill, not a seed invariant

For the natural all-Witt triangular tower,

```text
P=x-x^p,
Q_y=(1-p*x^(p-1))^(-1),
```

so no characteristic-zero polynomial `Q` exists.  Its limit is an analytic
unit on the closed `p`-adic disc and a nonpolynomial rational function with a
horizontal pole outside that disc.  Polynomial conjugacy cannot make this
map polynomial, because polynomiality is preserved in both directions by a
polynomial automorphism.  This is exact and useful.

It is not an invariant of the Artin--Schreier special fibre or of every
formal lift.  Mixed `p`-multiple terms can alter the denominator, and a
general analytic unit need not even possess the same rational horizontal
divisor description.  Use the triangular locus as a saturated negative
control inside `K_3^coll`; do not allocate a separate theorem root or claim
that the unit quotient closes all polynomial escapes.

## 4. Cheapest separating experiments, in order

No experiment is launched by this report.  The order below minimizes the
chance of spending computation on a circular theorem.

| Order | Object | First exact question | Positive interpretation | Negative/stop interpretation |
|---:|---|---|---|---|
| 1 | Exact coframe | Does one certified bounded `E_2 C E_2` orbit meet the two-curl locus? | Integrate and independently certify a direct JC2 counterexample candidate. | Unit ideal closes that orbit only; no support expansion this generation. |
| 2 | Local `K_3^coll` | Is the completed local ring at the `F_3` seed nonzero after inverting `3`? | A characteristic-zero collision point exists after finite-type contraction/base transfer. | A localized `h*3^N` certificate kills every degree-three branch through that seed. |
| 3 | Completion pair | Do rank-two/three monogenic schemas violate an explicit boundary-class or dualizing relation before chart recovery? | A non-tautological global invariant or an honest chart candidate. | Scoped low-rank no-go, or stop if the equations merely restate finiteness/étaleness. |
| 4 | Weighted `R` source | At two source occurrences, is `(C,R)` covariant and finite in the declared linear state category? | One sourced recurrence licenses exactly one reviewed first syzygy. | `NO-QUOTIENT`, two drivers, or one new pivot stops the current D-state route. |
| 5 | Microlocal defect | In an open immersion and Broughton control, is there a separately named Keller-only nonnegative remainder? | Freeze the exact local index for review. | Infinity correction or perverse cancellation retires the vanishing slogan. |
| 6 | Log-volume/lattice | Can a finite stable cone or a principal boundary relation be proved without bounded type/finiteness? | Only then build a small exact checker. | `H_d`, nonprincipal class, or stabilization assumption returns `RESTATEMENT`. |

Before order 2, source-check any existing low-degree Keller theorem that may
already exclude degree three; do not rediscover a known degree bound by local
algebra.  Before order 1, source-check the precise Cohn non-elementarity
certificate and the tame-to-`E_2` lemma.  These are background reviews, not
speculative descendants.

## 5. Circularity ledger

The following phrases are not progress unless their missing implication is
isolated as a theorem strictly weaker than JC2.

| Phrase | Hidden conclusion being reintroduced |
|---|---|
| “the differential lattice stabilizes and hence is finite” | bounded poles / integrality of `B` over `A` |
| “one algebraically stable boundary cone contains every iterate” | absolute/cofinal bounded type |
| “the nonproperness defect has zero conormal multiplicity” | absence of the boundary/nonproperness being detected |
| “the conductor cuts out the missing boundary” | finiteness of the ring extension; false for localization |
| “the trace/codifferent and class cone determine the chart” | existence of the global affine `A^2` open and polynomial origin |
| “all finite Witt lifts exist, therefore a characteristic-zero polynomial exists” | uniform degree/support and algebraization |
| “reduction has `P_y=0`, therefore the lift is univariate/Ritt” | preservation of support across characteristic |
| “finite Hankel rank is the only possible finite state” | linearity/recognizability of the chosen state category |

The reports correctly agree that local different/contact data do not recover
coordinate multiplication, raw passports are presentation costumes, and one
more unrestricted Witt or D depth is not a bridge.  No merged mechanism may
silently consume any of those stopped assumptions.

## 6. Recommended legal four-root portfolio

This portfolio is a proposal only.  It uses one coordination/review root and
the three leading independent mathematical fingerprints.  Each mathematical
root is itself the single speculative generation; none may spawn a theorem
or computation child from an unreviewed provisional claim.

| Root | Share | Work | Background review / one-generation discipline | Hard stop |
|---|---:|---|---|---|
| **C/R — coordination and hostile review** | 15% | Preserve the sealed DAG, holds, clocks, hashes, and exact-certificate perimeter; route any survivor to different-model review. | No mathematical child.  Source-check Cohn/tame-`E_2`, completion duality, and any known degree-three theorem in the background. | Any post-cutoff premise change reseals a later round; do not mutate this packet. |
| **E — exact coframe** | 30% | Paper bridge plus one bounded certified `E_2 C E_2` curl family. | The bounded family is the only speculative object.  Any survivor freezes immediately for independent integration, determinant, and non-`E_2` replay; no descendant first. | First survivor, exact unit ideal, certificate failure, or support/degree expansion. |
| **W — localized bounded collision** | 30% | Merge atlas C, zero-base compactness, and the triangular unit negative control at `p=3,D=3`, one local component. | Freeze equations and localized certificate format before algebra.  A nonzero generic fibre receives immediate independent transfer review; no `W_3` child. | First exact generic/vertical verdict, failed control, or fixed time cap; no `D=4`, new seed, or prime sweep. |
| **X — finite completion pair** | 25% | Merge zero-base B and falsifier 1: theorem audit, then one-boundary monogenic ranks two/three only. | Differential-lattice input is admitted only if it emits an explicit principal boundary relation.  No higher-rank/family child before review. | Honest triple, scoped rank no-go, or first proof that the schema merely restates étaleness/finiteness. |

The queued `WEIGHTED-R/HANKEL` discriminator is the first replacement if one
of E/W/X stops at its paper gate; it is not a fifth live root.  Microlocal,
log-volume, and differential-lattice slogans remain deferred until their
named circularity gate is passed.  Conductor, mixed-Ritt census, and the
untyped sidecar adjoint receive no allocation.

This portfolio touches none of the sealed holds: no B=168, D75, band-28 or
deeper D enumeration, new book cell, DIR/A-SCALE census, cCa6 F4, HC4
expansion, generic sparse search, integral D43, public/external contact,
msolve disclosure, remote launch, or interference with the checkpointed
box01 process.  The exact-coframe family is a fixed certified unstable-`K_1`
orbit, and the Witt root is one localized finite-type component; neither is a
generic support sweep.

## 7. Bottom line

The round's most important positive cross-pollination is not a grand unified
proof.  It is a disciplined separation of three honest global/direct objects:
an exact polynomial coframe with an independent nonautomorphy certificate, a
fixed finite coefficient scheme whose generic fibre is decisive, and the
canonical finite normalization with its actual affine source chart.  The
weighted D quotient is a cheap fourth allocator once a slot opens.

The strongest negative result of this comparison is equally useful:
conductor support, finite-Witt uniqueness/Ritt escape, dimension-three Keller
controls, automatic principal units, and automatic finite dynamical cones
cannot be used as stated.  Every one either has an explicit counterexample,
a type error, or contains finiteness/properness/bounded type as its hidden
premise.  No claim is promoted from this report.
