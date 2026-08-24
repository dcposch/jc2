# Coordinator synthesis — round `20260824T0453Z-dd11599`

Status: **FROZEN / DEGRADED / LAUNCH DECISION**  
Packet cutoff: `2026-08-24T04:53:35Z`  
Round close: `2026-08-24T06:29:30Z`  
Clean basis: `dd11599b07eb05591b5c006791005eef19457d8e`  
Packet SHA-256:
`042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5`

This closes the event-triggered full-spectrum round.  It ranks and allocates
work; it does not promote a mathematical claim.  Fable missed the collection
cutoff and was cancelled after one hour without a report, so the round is
formally `DEGRADED`.  The five on-time blind all-46 submissions nevertheless
give adequate breadth: four independent GPT-5-family scans and one Grok scan.
The missing Fable lane reduces model diversity and is not counted as a vote.

## 1. Frozen population and integrity record

| Artifact | SHA-256 |
|---|---|
| `xmodel/ideation-20260824T0453Z-root.md` | `97222d63837c4b883e94c8d667014872603b67f5663a1c86e2b1063a1435b1bc` |
| `xmodel/ideation-20260824T0453Z-atlas.md` | `0e381be9a5f1b4d7e2976f473d3d038a3dd591789bdd9f5f4fc2368c0ce374b7` |
| `xmodel/ideation-20260824T0453Z-zero-base.md` | `fb804efab0c2cff524512fb7f81cceb2adaea7cce299a827211310c22052ba9a` |
| `xmodel/ideation-20260824T0453Z-falsifier.md` | `12d1fe67a1dc7be75041050be3009d8599578e10c6cb1b57d1da12ecfa800962` |
| `xmodel/ideation-20260824T0453Z-grok.md` | `6a7010e0d71d6bac03171e1b164a70668352d896b0da248fdb689c13494f7136` |
| `xmodel/ideation-20260824T0453Z-dedup.md` | `d100616a66115ab0fa1dedc49bfbee910b8d70a0b915268c8e974a197a11747b` |
| `xmodel/ideation-20260824T0453Z-adversary.md` | `cb878f2f942cb205bc5fe292447279200ce7911967cde96da31e1794586a6cd6` |
| `xmodel/ideation-20260824T0453Z-feasibility.md` | `87464f7a4367ec2b61c67321fa70365bd0759fbd07ef569d9e8b8aefe4e9c5cd` |

The packet transcribed the `AUDIT.md` digest with one missing `0`.  Its
63-character string

```text
a0033b88030fbd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

must read

```text
a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

The clean-basis file and mathematical input are unambiguous.  The packet stays
sealed; `xmodel/ideation-20260824T0453Z-packet-erratum.md` records the
correction.  Grok caught the mismatch.  Atlas, zero-base, and falsifier each
incorrectly said all packet hashes matched; that is a provenance error in
their read records, not evidence that they read different mathematics.

## 2. Deduplicated idea graph

Fifteen cards reduce to twelve operational fingerprints.  There are two firm
duplicates and one looser composition:

1. `COMP-PAIR`: zero-base B and falsifier 1 are the same finite-normalization /
   affine-open-chart object.
2. `MICRO-DEFECT`: atlas A and zero-base A are the same nonproperness defect,
   expressed through Fourier--Verdier and trace-zero/inertia receivers.
3. `FIXED-STRATUM`: atlas C and zero-base C are the same fixed-degree local
   coefficient scheme plus compactness bridge; falsifier's triangular
   unit-at-infinity result is its negative control, not a third vote.

The remaining distinct fingerprints are `DIFF-LATTICE-UNIT`,
`ITERATED-LOG-VOLUME`, `EXACT-COFRAME-K1`, the weighted `D` quotient,
`UNIT-INFINITY`, `X-HANKEL`, `ZMT-CONDUCTOR`, repaired
`AS-MIXED-RIGIDITY`, and the typed version of `SIDECAR-ADJOINT`.

The strongest real convergence is object-level, not mechanism-level.  All
five scans seek a canonical global receiver or completion; four use bounded
characteristic-`p` algebra; three redesign the full `D` source.  Only one scan
found the exact-coframe route, but it is genuinely new and its payoff is a
direct characteristic-zero counterexample, so vote count does not dominate
its information value.

## 3. Mathematical adjudications

### 3.1 Exact coframes: a valid direct counterexample bridge

Let `S=C[x,y]` and let

```text
M = [[a,b],[c,d]] in SL_2(S),
a_y=b_x,  c_y=d_x.
```

Polynomial de Rham exactness integrates the rows to `dP,dQ`, giving
`M=J(P,Q)` and `[P,Q]=1`.  The load-bearing automorphism lemma is also
correct: Jung--van der Kulk expresses a plane automorphism using affine maps
and triangular shears; shear Jacobians are elementary, substitution preserves
elementary matrices, constant `GL_2(C)` matrices normalize `E_2(S)`, and the
chain rule puts the Jacobian of every determinant-one plane automorphism in
`E_2(S)`.  Hence

```text
closed rows + det(M)=1 + M notin E_2(C[x,y])
    => a characteristic-zero plane Keller nonautomorphism.
```

This uses plain nonmembership, not an unsafe group quotient `SL_2/E_2`.
Left and right multiplication by registered elementary matrices preserves
nonmembership even though no normality assertion is made.  The standard Cohn
matrix

```text
C = [[1+xy,x^2],[-y^2,1-xy]]
```

has determinant one and a known non-elementarity lineage, but its two rows are
not closed.  The first gate is therefore a frozen bounded double orbit
`E_L C E_R`, first at the linearized curl level and then, only if licensed, by
one exact small elimination.  A survivor would be decisive after independent
nonmembership, integration, determinant, collision/nonautomorphy, and source
replay.  A unit ideal closes only the preregistered orbit.

Post-cutoff source intake, excluded from the blind vote, found the 2024/2026
preprint *Decomposition of matrices from SL2(K[x,y])* (arXiv:2412.03688),
which restates Cohn non-elementarity and classifies low-entry-degree matrices
up to elementary/Cohn-type factors.  It justifies an immediate literature and
certificate freeze; it is not yet an independent review of this bridge.

### 3.2 Fixed-degree lifting: exact dichotomy, but degree three is a known
negative control

For a fixed coefficient scheme `Z_D` with the marked collision and its local
ring `O` at the Artin--Schreier point, completion gives the exact dichotomy

```text
Ohat[1/3] != 0  <=>  a characteristic-zero point through the local component,
Ohat[1/3] = 0   <=>  some localized g*3^N ideal-membership certificate.
```

The prime-contraction/base-transfer and faithful-flatness implications are
sound.  This is the correct replacement for “one more Witt level.”  Grok's
claimed lift uniqueness is false unless `P` is frozen: over `Z/9`, for
example, varying `P=x-x^3+3A(x)` varies the polynomial inverse of `P'` and
therefore produces different triangular lifts.  The submitted mixed/Ritt
route is rejected; the fixed-`P` triangular obstruction remains an exact
negative control.

However, the proposed `D=3` characteristic-zero positive branch is already
excluded by established plane low-degree results (far stronger degree bounds
are part of the campaign baseline).  The post-cutoff source check includes
GGV-Horruitiner et al., arXiv:2204.14178, which explicitly confirms Moh's
degree-100 lower bound while pushing it further.  Thus a `D=3` local
calculation can only recover a vertical-thickness/no-lift certificate and
improve the lifting instrument; it cannot discover a characteristic-zero
plane counterexample unless it simultaneously overturns a load-bearing known
theorem.  This correction moves `FIXED-STRATUM` from a live top-three root to
the first exact software/negative-control reserve.

### 3.3 Canonical finite normalization/open chart: exact global object

For a hypothetical plane Keller counterexample, with

```text
A=C[P,Q], B=C[x,y], L=Frac(B),
R=normalization of A in L,
```

`R` is finite over `A`, `X=Spec R` is a normal affine surface, and Zariski
Main gives the open immersion `U=Spec B -> X`.  The following deductions are
exact after the codimension-one perimeter is stated carefully:

- `R` is a maximal Cohen--Macaulay module over regular `A`, hence finite
  projective and then finite free;
- `R^*=B^*=C^*`;
- a nonempty complement has a divisorial component by normal Hartogs; and
- the divisor localization sequence gives
  `Cl(X) ~= direct_sum_i Z[D_i]` for the boundary components.

These facts do not themselves remove the boundary.  They instead show exactly
why the proposed differential determinant must produce a nonzero *principal
relation* among the `D_i`; merely producing a boundary divisor or coherent
meromorphic lattice gives the expected nonzero class and no forbidden unit.
Different/codifferent statements must use dualizing modules or Weil divisors
unless Gorenstein/Cartier hypotheses are proved.  The live task is to seek a
strictly weaker, independently computable obstruction in ranks two and three,
not to restate “no such affine chart exists.”

### 3.4 Weighted `D` quotient: a typed allocator, not yet a theorem

The coordinate change

```text
C=U_g/U_f,  R=U_f^3/U_g^2,
U_f=R C^2,  U_g=R C^3
```

is exact, and the first tangent of `R` is `3 alpha_1-2 beta_1`, explaining the
reviewed P4P1 sidecar without setting it to zero.  It does not prove that the
common-carrier action is a symmetry of the full normalized polynomial source,
that `C` disappears, or that `R` has finite linear state.  The only licensed
gate is to derive the first two actual x-side source occurrences from the
unreduced producer expressions and return one of `NO-QUOTIENT`, `TWO-DRIVER`,
a certified linear-state pivot, or a fully sourced recurrence.  Hankel rank
may refute only the declared linear/recognizable category.

### 3.5 Rejections and deferrals

- **Reject `ZMT-CONDUCTOR`.**  For a nontrivial dense open immersion of
  noetherian integral affine schemes, a nonzero conductor would make the open
  immersion finite and hence an isomorphism.  The conductor is therefore zero,
  as in `C[t] subset C[t,t^-1]`; it does not cut out the deleted boundary.
  `(x^2,xy)` is not quasi-finite along `x=0` and was also misused.
- **Reject the submitted `SIDECAR-ADJOINT`.**  The band-42 form and six
  band-26 compatibility functions have no declared common source tangent and
  codomain.  No span comparison exists until a producer supplies that typing.
- **Defer `MICRO-DEFECT`.**  Its cone is a canonical detector, but its bare
  vanishing is equivalent to properness.  A Keller-specific nonnegative index
  term must survive open-immersion, Broughton, Hénon, rational
  volume-preserving, and the known 2026 three-dimensional Keller
  counterexample controls.  The adversarial report's assertion that no such
  three-dimensional counterexample exists is stale/false relative to the
  campaign basis; the Alpoge--Fable map is part of the existing 2026 context.
- **Stop `ITERATED-LOG-VOLUME` as submitted.**  On a fixed finite state,
  `w=Mw+r` already implies every iterate identity.  The missing stable/cofinal
  boundary state and polynomial-specific sign do all the work.
- **Absorb `DIFF-LATTICE-UNIT` into the completion audit.**  It earns a root
  only if it emits an explicit nonzero vector in the kernel of the boundary
  divisor-to-class-group map, not merely a class or bounded-pole lattice.

## 4. Coordinator ranking

Ranking is by expected decisive information per wall-clock hour after the
corrections above, not by raw votes.

| Rank | Mechanism | Present gate | Disposition |
|---:|---|---|---|
| 1 | `EXACT-COFRAME-K1` | Freeze the non-`E_2` certificate and one bounded `E_2 C E_2` curl family | **Launch** |
| 2 | `COMP-PAIR` / finite normalization | Prove the exact perimeter, then rank-two/three principal-class or chart separator | **Launch, paper first** |
| 3 | weighted `D` quotient | Two full-source occurrences in `(C,R)` | **Launch as cheap allocator** |
| 4 | fixed-degree local lifting | Exact `D=3` verticality certificate / reusable local compiler | **Reserve; known-negative only** |
| 5 | `MICRO-DEFECT` | Isolate a Keller-specific index remainder on explicit controls | **Reserve paper gate** |
| 6 | fixed-`P` `UNIT-INFINITY` | Exact triangular closure | **Bank as control** |
| 7 | differential lattice | Principal boundary relation | **Inside rank 2 only** |
| 8 | `X-HANKEL` | Source registry plus linear-realization theorem | **Not ready** |
| 9 | iterated log volume | New cofinal state/sign theorem | **Stop current form** |
| 10 | conductor / mixed Ritt / untyped sidecar | Fatal algebra/type defects | **Reject current form** |

The exact-coframe route outranks the localized `D=3` scheme despite the
feasibility report's reverse order: both have exact logic, but only the former
still has a possible direct positive payoff.  The degree-three scheme remains
valuable as a reusable algebraization instrument and verticality control.

## 5. Launch portfolio and stop conditions

The live portfolio uses three independent mathematical roots beside
coordination.  No result below is yet `PROVISIONAL`, so there are no
speculative descendants or review debt at launch.

| Root | Share | Deliverable | Immediate stop |
|---|---:|---|---|
| **E — exact coframe** | 35% | Primary-source/nonmembership freeze; theorem-grade tame-to-`E_2` bridge; linearized curl map on one preregistered bounded Cohn double orbit; at most one exact elimination if licensed | survivor, empty tangent, unit ideal, invalid nonmembership lineage, or any support expansion |
| **X — finite completion pair** | 30% | Theorem-grade finite-free/unit/class/duality perimeter and one named rank-two/three schema; return a principal boundary relation, explicit chart candidate, scoped no-go, or `RESTATEMENT` | first exact separator or proof that the schema merely restates finiteness/etaleness |
| **D — weighted source quotient** | 20% | Pull two actual x-side source occurrences into `(C,R)` with all chain-rule terms and a declared state category | `NO-QUOTIENT`, `TWO-DRIVER`, first certified pivot/recurrence, or missing source registry |
| **C/R — coordination/review** | 15% | Preserve holds and claim DAG; source-check; route the first provisional result to different-model hostile review; prepare fixed-degree local compiler as replacement only | first decisive gate triggers a micro-round/rebalance |

The localized degree-three scheme replaces the first stopped root only if its
pre-registration makes the verticality certificate materially cheaper than a
full local Groebner campaign.  `MICRO-DEFECT` is the next paper-only
replacement.  No root may silently widen to generic sparse search, another
Witt level, band 28/deeper `D`, or a new boundary book.

Any exact-coframe survivor freezes immediately.  Cheap reversible checking
may continue under a visible provisional label only after the five-part
provisional gate is satisfied and different-model hostile review has been
enqueued.  Promotion, publication, fleet expansion, and further fanout wait
for that review; unrelated roots continue.

## 6. Holds and next event

The prior holds remain unchanged: B=168, D75, band 28 or deeper `D`, new book
cells, another DIR/A-SCALE census, cCa6 F4, HC4 expansion, generic sparse
search, integral D43, public/external communication, and msolve disclosure.
The checkpointed legacy box01 process is not touched.  Box02 and Box03 remain
stopped unless a preregistered exact calculation earns a separately recorded
launch.

The round closes with no proof, no characteristic-zero counterexample, and no
new promoted claim.  The first root verdict triggers a micro-round; a
rank-changing survivor or refutation triggers a full round under the
coalescing rule.  The quiet full-round backstop is
`2026-08-24T18:29:30Z`, and broad web sweep #9 remains due by
`2026-08-24T21:25Z`.
