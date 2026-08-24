# Post-collection feasibility/readiness triage — `20260824T0453Z`

- Producer/model: OpenAI Codex, GPT-5 family; independent feasibility lens
- Basis: `dd11599b07eb05591b5c006791005eef19457d8e`
- State cutoff: `2026-08-24T04:53:35Z`
- Packet: `xmodel/ideation-20260824T0453Z-packet.md`
- Packet SHA-256: `042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5`
- Scope: post-closure theorem/certificate triage of the five frozen submissions;
  not a second novelty dedup and not a claim promotion
- Execution: no browser, task launch, research computation, external contact,
  or shared-ledger edit

The packet's `AUDIT.md` digest has the acknowledged nonsemantic transcription
error: the on-disk digest inserts `0` after `...30f`, namely
`a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32`.
The sealed packet was not edited.

## Executive verdict

The two best information-per-hour mechanisms are genuinely exact and lead to
direct counterexample certificates:

1. **Localized degree-three Keller-collision scheme.**  Its completed local
   ring has an exact dichotomy: nonzero generic fibre gives a characteristic-
   zero Keller collision, while zero generic fibre gives a finite localized
   `3^N` ideal-membership certificate.  The formulation is ready now.
2. **Non-elementary exact coframe.**  A matrix in `SL_2(C[x,y])` with two
   closed rows and a rigorous certificate of nonmembership in `E_2` integrates
   to a direct JC2 counterexample.  The logical implication is correct.  The
   only pre-launch gate is to freeze an actual non-`E_2` witness invariant;
   writing `SL_2/E_2` as though it were automatically a quotient group is not
   enough.

Three attractive proof-side objects are less ready.  The Fourier/Verdier
defect is canonical but its proposed positivity is exactly the missing
infinity lemma.  The affine-completion pair is an exact global certificate but
has no specified candidate family.  Differential saturation is definable only
after a lattice/operator choice, and the required coherence-to-boundary
implication is absent.

Two proposals should stop in their present form.  The conductor of a
nontrivial dense open immersion is zero, not an ideal cutting out its boundary;
it is a binary restatement of equality.  On a fixed algebraically stable
boundary state, every iterated log-volume equation is a formal iterate of the
one-step equation, so iteration supplies no independent constraint.

## Common exact reduction

For a Keller pair put

```text
A = C[P,Q],   B = C[x,y],   K = Frac(A),   L = Frac(B),
R = integral closure of A in L.
```

Then `A` is a polynomial ring, `L/K` is finite separable, and `R` is finite
over `A`.  Moreover `R subset B`: an element integral over `A` is also integral
over `B`, and `B` is integrally closed in `L`.  Zariski Main gives

```text
U = Spec B  --j, open-->  X = Spec R  --pi, finite-->  Spec A.
```

Since a normal surface is Cohen--Macaulay, the finite `A`-module `R` is maximal
Cohen--Macaulay over the regular ring `A`; Auslander--Buchsbaum and
Quillen--Suslin make it finite free.  Also `R^*=B^*=C^*` and `Cl(B)=0`.  The
divisor localization sequence therefore gives, for the divisorial components
`D_i` of `X-U`,

```text
Cl(X) = direct_sum_i Z[D_i].
```

This is exact.  If the complement had no divisorial component, normal Hartogs
extension would give `R=Gamma(X,O)=Gamma(U,O)=B`, so a nonempty boundary really
does have such components.  These facts validate the completion-pair target;
they do not themselves contradict a boundary.

## 1. `EXACT-COFRAME-K1`: the direct-certificate claim is correct

Let `S=C[x,y]` and use the row convention

```text
J(P,Q) = [[P_x,P_y],[Q_x,Q_y]].
```

### Why a determinant-one automorphism has Jacobian in `E_2(S)`

Jung--van der Kulk generates every plane polynomial automorphism by affine
maps and elementary triangular shears.  A shear has Jacobian
`e_12(h')` or `e_21(h')`.  An affine map has constant Jacobian in `GL_2(C)`.
The following slightly stronger induction handles decompositions whose
individual affine factors do not have determinant one:

```text
JH = C_H E_H,  with C_H in GL_2(C) and E_H in E_2(S).
```

It holds for the generators.  If it holds for `F,G`, the chain rule gives

```text
J(F o G) = C_F E_F(G) C_G E_G
         = C_F C_G (C_G^(-1) E_F(G) C_G) E_G.
```

Substitution by `G` preserves elementary matrices.  Conjugation by a constant
matrix also preserves `E_2(S)`: over `C`, a constant matrix is a scalar times
an element of `SL_2(C)=E_2(C)`, and the scalar conjugation is trivial.  Thus the
induction closes.  If `det JH=1`, then `C_H` lies in `SL_2(C) subset E_2(S)`,
so `JH in E_2(S)`.  Without determinant normalization the unqualified claim is
false, because `E_2` is contained in `SL_2`; the Keller normalization is exactly
the case needed here.

### Why closed rows plus non-elementarity are a JC2 certificate

For `M=[[a,b],[c,d]]`, closedness means

```text
a_y=b_x,   c_y=d_x.
```

Polynomial de Rham exactness in characteristic zero gives polynomials `P,Q`
with `dP=a dx+b dy` and `dQ=c dx+d dy`; one may obtain them by termwise
integration, so this is effective.  If `det M=1`, then `J(P,Q)=1`.  If this
pair were an automorphism, the preceding argument would force `M in E_2(S)`.
Consequently

```text
closed rows + det(M)=1 + a rigorous M not-in E_2 certificate
    => a characteristic-zero polynomial Keller nonautomorphism.
```

No separately exhibited collision is logically necessary.  Nonautomorphism
already contradicts JC2 (and injectivity would imply automorphy by the standard
characteristic-zero injectivity theorem).

### Missing lemma, cheapest control, readiness

For rank two, `E_2` need not be treated as a normal subgroup, so
`SL_2/E_2` should not be used as an unexplained quotient group.  The certificate
must be actual nonmembership, for example a specified Mennicke-symbol map that
vanishes on `E_2` and is nonzero on the candidate.

The cheapest exact family starts with the standard Cohn matrix

```text
C = [[1+xy, x^2],[-y^2,1-xy]],   det(C)=1,
```

together with an independently fixed proof that `C notin E_2`, and searches
only matrices `E_L C E_R` for bounded elementary `E_L,E_R`.  Every such matrix
remains non-elementary: if `E_L C E_R` were elementary, multiplying by the
elementary inverses would make `C` elementary.  Determinant and nonmembership
are therefore automatic; only the two curl equations remain.  The original
Cohn rows fail closedness by the exact defects `x` and `-y`, so the control is
nontrivial.

**Readiness: amber-green.**  The bounded curl problem can run now after the
nonmembership witness and parameter family are frozen.  A generic
`SL_2`-membership test or additive corrections that may change the obstruction
are not ready.  This ranks second by information/hour: a survivor is decisive,
while emptiness has only the declared bounded-neighbourhood scope.

## 2. Conductor and differential-lattice audit

### The open-immersion conductor is binary, not a boundary ideal

Let `R subset S` be Noetherian domains with the same fraction field and let
`Spec S -> Spec R` be a dense open immersion.  Define

```text
(R:S) = {c in S : cS subset R}.
```

This set is well-defined as an ideal of both rings, even when `S/R` is not
finite.  But if it contains a nonzero `c`, then `c` itself lies in `R`, and
multiplication by `c` identifies `S` with the ideal `cS subset R`.  Noetherianity
makes that ideal, hence `S`, finite over `R`.  The open immersion is then also
finite.  Its image is open, closed, and dense in irreducible `Spec R`, so the
map is an isomorphism.  Therefore

```text
(R:S) = R=S  if the open immersion is an isomorphism,
(R:S) = 0    for every nontrivial dense open immersion.
```

The elementary control `C[t] subset C[t,t^(-1)]` already has conductor zero
although the complement is the divisor `t=0`.  Thus the Grok claim that this
conductor “cuts out the complement” is false in the relevant nonfinite setting.
For the Zariski-Main pair it says only `B=R` or not; `f=B` is literally the
desired equality, and a hypothetical counterexample has `f=0`.

**Readiness: stop.**  There is no conductor computation to launch as a new
invariant.  A finite-extension different/codifferent remains meaningful, but
`NORM-MOMENT-SEP` already shows that such local finite-algebra data do not
recover the open chart or coordinate multiplication.

### Differential saturation is definable, but the proposed implication is
missing

The target derivations extend uniquely to `L` and, in Keller coordinates, are

```text
delta_u = Q_y d/dx - Q_x d/dy,
delta_v = -P_y d/dx + P_x d/dy.
```

They commute, preserve `B`, and form a determinant-one frame on `Spec B`.
They need not preserve `R`.  In the one-dimensional ramified control
`t=s^e`, one has `d(s)/dt=1/(e s^(e-1))`, which immediately leaves the
normalization.

Given an initial finite lattice `Lambda subset L`, the smallest submodule of
`B` closed under multiplication by `R` and under `delta_u,delta_v` is a
well-defined operator saturation.  It depends on `Lambda` (unless, for
example, `Lambda=R` is declared), and it need not be coherent.  Until
coherence is proved there is no finite determinant line.  Even after
coherence, a rational determinant section may represent a nontrivial boundary
class rather than a principal divisor; the exact identity
`Cl(X)=direct_sum Z[D_i]` explains why constant units on `U` do not turn that
class into a unit.

The load-bearing missing statement is therefore precise:

> factoriality and constant units of `B`, together with the stable frame,
> force the canonical differential saturation to be coherent and force its
> boundary pole class to be principal (or otherwise force `D` empty).

Neither implication follows from the submitted construction.  A finite
stable *algebra* containing `R` would be integral over `A` and collapse back
to `R`; requiring it also to contain all of `B` is just finiteness.  A finite
stable module alone need not contain the coordinate multiplication that the
receiver-separation result identified as essential.

**Cheapest exact control:** first prove the unbounded denominator growth for
`t=s^e`; then do one SNC chart with both a ramified and an unramified deleted
divisor and record whether the saturation detects the latter.  The route may
run as a local theorem audit, but not as a global JC2 lane.  **Readiness:
amber-red; rank seventh.**

The codifferent `Hom_A(R,A)` and the codimension-one different divisor are
well-defined for the finite separable normalization.  They need not be an
invertible ideal on a non-Gorenstein normal surface.  Canonical-divisor
equalities should therefore be stated as Weil-divisor or dualizing-module
identities, not as an unproved Cartier equality.  None of these distinctions
recovers `B` from `R`.

## 3. `ITERATED-LOG-VOLUME`: iteration adds no independent equation

Assume the strongest version of the proposed prerequisite: a single
algebraically stable model carrying a finite boundary basis, a pullback matrix
`M`, the coefficient vector `w=div(dx wedge dy)`, and ramification vector `r`.
The rational-form identity `F^*(dx wedge dy)=dx wedge dy` gives the one-step
divisor equation

```text
w = M w + r.
```

The iterate ramification formula then gives

```text
w = M^n w + (I+M+...+M^(n-1)) r.
```

The second line follows algebraically by iterating the first.  It imposes no
new condition on the fixed finite state.  Perron--Frobenius may amplify a sign
already present in the one-step equation, but cannot create the needed sign,
identify topological degree with a boundary spectral radius, or prove that the
same finite state controls every iterate.

Two exact controls expose the gaps.  A determinant-one Hénon automorphism has
topological degree one but boundary/dynamical degree greater than one, so
spectral growth is not generic fibre degree.  The rational map

```text
(x,y) -> (x^d, y/(d x^(d-1)))
```

has Jacobian one and generic degree `d>1`; invariant meromorphic volume alone
therefore cannot provide the contradiction.  Polynomial regularity and a
cofinal bounded boundary model would have to do all the work.

**Cheapest exact control:** write the one-step/iterate identity on the Hénon
and rational examples before building any checker.  **Readiness: stop in the
present form; rank tenth.**  It can reopen only with a new theorem supplying a
canonical finite invariant boundary cone and a plane-polynomial sign not
already equivalent to the one-step formula.

## 4. Localized fixed-degree collision scheme: highest readiness

Let `Z_D` be the finite-type coefficient scheme over `Z` for degree-at-most
`D` pairs satisfying `J(P,Q)=1` and
`F(0,0)=F(1,0)`.  Let `s` be the degree-three Artin--Schreier point over
`F_3`, let `O=(O_{Z_3,s})`, and let `Ohat` be its completion.

There is an exact dichotomy.

- If `Ohat[1/3] != 0`, faithful flatness of completion gives
  `O[1/3] != 0`.  Hence there is a prime of the finite-type coefficient ring,
  contained in the special-point prime but not containing `3`.  Its residue
  field has characteristic zero; the finitely generated coefficient field
  embeds in `C`.  The corresponding `P,Q` have Jacobian one and the marked
  collision, so they are a genuine JC2 counterexample.
- If `Ohat[1/3] = 0`, then `3^N=0` in `Ohat` for some `N`.  Faithful flatness
  (equivalently injectivity of Noetherian local completion here) gives the same
  equality in `O`.  Thus there is a denominator `g notin m_s` with
  `g 3^N` in the global defining ideal.  That finite ideal-membership identity
  is a checkable certificate that the entire local degree-three component is
  vertical.  The known `Z/9` point merely implies that the least possible
  thickness is at least two.

This also sharpens the fixed-degree compactness card.  If `Z_D(Z/3^n)` is
nonempty for every `n`, the finite reduction tree has an infinite branch by
König's lemma, yielding a `Z_3` Keller collision of degree at most `D` and
hence, after field transfer, a characteristic-zero counterexample.  The local
generic-fibre test decides the same issue without guessing compatible nodes
level by level.

**Missing lemma:** none in the implication; only the exact local algebra is
unknown.  A positive verdict must use the prime/component argument above (or
an explicit point), not mere failure to find `3^N`.  A negative verdict must
print `g,N` and the ideal representation, not a truncated empty search.

**Cheapest exact control:** `D=3` has twenty coefficient variables before
normalizations, coefficient equations for the degree-at-most-four Jacobian,
and the marked collision equations.  First replay the special point and its
mod-9 lift, compute the exact tangent/obstruction map, and then attempt one
localized saturation/standard-basis certificate.  This is a single bounded
local calculation, not `W_3`, a support sweep, or a fleet job.

**Readiness: green; rank first.**  It can run now as specified.  The full
local scheme strictly dominates a degree-three mixed-support mod-9 census:
that census is useful tangent data but cannot decide whether the component
reaches characteristic zero.

## 5. Fourier--Verdier / trace-zero microlocal defect

For a quasi-finite Keller map the object

```text
K_F = Cone(RF_! Q[2] -> RF_* Q[2])
```

is canonical and well-defined without assuming `B` finite over `A`.  In the
Zariski-Main factorization,

```text
K_F = R pi_* Cone(j_! Q_U[2] -> Rj_* Q_U[2]).
```

At a boundary point the `H^0` stalk of `Rj_*Q_U` is nonzero, whereas the
`j_!` stalk is zero.  Since finite pushforward is a finite direct sum on
stalks, a nonempty boundary gives `K_F != 0`; away from `pi(D)` the cone is
zero.  Thus in this setting

```text
K_F=0  iff  D is empty  iff  F is proper.
```

This immediate implication is exact, but it also shows that bare vanishing of
`K_F` is the desired theorem repackaged.  The trace-zero middle extension is a
useful refinement: zero conormal multiplicities would make it smooth across
the nonproperness curve; trivial permutation monodromy plus connectedness
would force degree one.  The missing lemma is exactly a Keller-specific index
identity forcing those nonnegative conormal multiplicities to vanish.

The fact that every `aP+bQ` has no affine critical point only moves possible
vanishing cycles to infinity; it does not kill them.  The cheapest exact audit
is therefore the open embedding `G_m x A^1 -> A^2`, a one-dimensional deleted
cover, triangular and Hénon automorphisms, `(x^2,xy)`, and the known
dimension-three Keller counterexample.  A proposed sign must distinguish the
plane polynomial case without assuming properness or suppressing an irregular
infinity term.

**Readiness: amber; rank fourth.**  The stalk equivalence can be proved now.
No D-module instrument should be built until a paper formula survives all
controls.  Failure would efficiently retire a broad cohomological slogan;
success would be a genuine proof critical path.

## 6. Affine completion pair / finite-flat open-chart synthesis

The certificate `(X,D,pi,j,r0,r1)` is exact: `X` normal affine,
`pi:X->A^2` finite, `j:A^2->X` an explicitly verified open immersion with
image `X-D`, `pi o j` of nonzero constant Jacobian, and two distinct marked
points with the same image.  Pulling back target coordinates gives an explicit
characteristic-zero Keller collision.  Conversely every hypothetical JC2
counterexample produces the finite normalization/open-chart part by Zariski
Main, and nonautomorphy supplies a collision.

The finite-free and class-group deductions in the common setup are sound.
The codifferent/relative dualizing module and effective codimension-one
different are also exact finite-map data, subject to the Weil/Cartier caveat
above.  What is missing is not another deduction from them but an actual
family in which all of the following are simultaneously checkable:

```text
finite normal A-algebra; A^2 open chart; boundary basis for Cl(X);
etaleness on the chart; constant Jacobian; marked collision.
```

Class group and canonical data alone cannot certify the open chart or
coordinate multiplication.  The proposed rank-two/rank-three monogenic
search has no preregistered equations or classified family, so its stated
runtime is not yet meaningful.

**Cheapest exact control:** finish the class-group localization proof and the
dualizing-module convention on one explicitly named affine modification, then
require mutually inverse ring maps for `X-D ~= A^2` before imposing volume or
collision.  **Readiness: amber-red; rank fifth.**  The certificate is excellent,
but no search should run until the surface family is frozen.

## 7. Weighted-unit quotient and `X-HANKEL`

The weighted coordinate change is exact:

```text
C=U_g/U_f,  R=U_f^3/U_g^2,  U_f=R C^2,  U_g=R C^3.
```

Under `(U_f,U_g)->(V^2U_f,V^3U_g)`, `R` is invariant and `C` transforms by
`C->VC`.  At a first new weight,

```text
[t^N](R-1)=3 alpha_N-2 beta_N,
```

so the row-42 sidecar is indeed the tangent of the invariant quotient.  This
is a useful exact reparametrization, not evidence that the common-carrier
action is a symmetry of the normalized polynomial source, that `C` is
triangular, or that `R` has a six-shift recurrence.

The cheapest valid gate is two source-defined x-side occurrences in the
unreduced product, with every chain-rule term retained.  If no complete source
registry supplies those occurrences, the proposed test cannot yet be formed.
**Readiness: amber; rank sixth.**  It is worth a paper check, but not a D-depth
or solver launch.

The Hankel idea has an exact conditional core: a finite linear realization of
dimension `r` forces every block-Hankel rank to be at most `r`, so a certified
`(r+1)`-minor kills that realization.  Its missing hypotheses are currently
load-bearing.  The D system must first be proved to lie in the relevant linear
rational-series category, and the allowed `alpha_N,beta_N` must be typed by
the genuine polynomial source.  Treating them as universally independent
makes rank growth automatic but says nothing about polynomial maps; imposing
a recurrence assumes the desired result.  **Readiness: red; rank ninth.**

## 8. `UNIT-INFINITY`, triangular rigidity, and mixed escape

For the fixed characteristic-zero triangular coordinate
`P=x-x^p`, the Jacobian equation is

```text
(1-p x^(p-1)) Q_y = 1.
```

No polynomial `Q` can satisfy it.  The Tate solution is the exact analytic
unit `(1-px^(p-1))^(-1)`, and polynomial-automorphism conjugacy cannot make the
map polynomial: otherwise conjugating back by polynomial inverses would make
the original map polynomial.  This closes the fixed triangular tower exactly.

The stronger uniqueness wording in the Grok card needs correction.  If
`P` itself is allowed to vary among lifts in `R_n[x]`, then `P'` varies and its
inverse, hence `Q=y(P')^(-1)`, varies.  Uniqueness holds for **fixed** `P`
(and the normalization `Q in y R_n[x]`), not for all one-variable lifts of the
special fibre.

The quotient `Z_p<x,y>^*/Z_p[x,y]^*` is well-defined, but a “horizontal
divisor” for a general analytic unit is not automatically a covariant
algebraic invariant.  For the displayed rational unit it explains the pole;
for arbitrary mixed lifts a presentation-independent divisor and its behavior
under sourced formal isomorphisms are missing.

**Cheapest exact control:** prove the fixed-`P` lemma above and place every
degree-three mixed correction inside the full local collision scheme of
Section 4.  A separate mod-9 mixed census has lower information value and
should be only tangent reconnaissance.  **Readiness: green for the lemma,
red for a universal unit invariant; combined rank third.**  The unit-twist
factorizer is useful exact software for controls but is not itself a JC2
mechanism.

## Final information/hour ranking and launch gates

| Rank | Mechanism | Exact payoff | Can run now? | Fatal prerequisite / gate |
|---:|---|---|---|---|
| 1 | Localized `K_3^coll` at the `F_3` seed | char-0 collision or localized `3^N` certificate | **Yes** | print a prime/point or `g 3^N` ideal identity |
| 2 | Non-elementary exact coframe | direct JC2 counterexample | **After one paper freeze** | explicit non-`E_2` invariant and obstruction-preserving family |
| 3 | Fixed-`P` rigidity plus mixed tangent control | exact closure of triangular escape; input to rank 1 | **Paper yes** | do not overstate uniqueness when `P` varies |
| 4 | Fourier/Verdier trace-zero defect | proof if a plane-specific positive index vanishes | **Paper controls only** | infinity/irregular sign independent of properness |
| 5 | Completion pair / affine open chart | direct global counterexample or scoped family no-go | **No** | freeze an explicit normal finite-cover family and chart maps |
| 6 | Weighted quotient `R,C` | decides one/two/unbounded D drivers at first sources | **Conditional** | actual source covariance and two typed occurrences |
| 7 | Differential lattice | possible ramification/boundary obstruction | **Local audit only** | canonical coherent saturation and principal boundary implication |
| 8 | Unit-at-infinity beyond the fixed tower | category obstruction for another lift | **No** | presentation-independent covariance |
| 9 | `X-HANKEL` | finite state or exact rank-growth certificate | **No** | source registry and linear-realization theorem |
| 10 | Iterated log-volume | none beyond one-step on a fixed state | **Stop** | genuinely new bounded-state/sign theorem |
| 11 | Open-immersion conductor | binary equality test only | **Stop** | impossible as proposed: nontrivial conductor is zero |

The launch recommendation is therefore singular: if a computation is later
authorized, the localized degree-three scheme is the only fully specified
exact calculation.  The coframe route deserves the next paper freeze.  All
other mechanisms first owe the stated theorem-level prerequisite; extra D
depth, another Witt level, or a boundary-state checker would not discharge it.

## Files read and freeze record

For this post-closure triage I read exactly the packet and the five frozen
submissions requested:

| File | SHA-256 |
|---|---|
| `xmodel/ideation-20260824T0453Z-packet.md` | `042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5` |
| `xmodel/ideation-20260824T0453Z-root.md` | `97222d63837c4b883e94c8d667014872603b67f5663a1c86e2b1063a1435b1bc` |
| `xmodel/ideation-20260824T0453Z-atlas.md` | `0e381be9a5f1b4d7e2976f473d3d038a3dd591789bdd9f5f4fc2368c0ce374b7` |
| `xmodel/ideation-20260824T0453Z-zero-base.md` | `fb804efab0c2cff524512fb7f81cceb2adaea7cce299a827211310c22052ba9a` |
| `xmodel/ideation-20260824T0453Z-falsifier.md` | `12d1fe67a1dc7be75041050be3009d8599578e10c6cb1b57d1da12ecfa800962` |
| `xmodel/ideation-20260824T0453Z-grok.md` | `6a7010e0d71d6bac03171e1b164a70668352d896b0da248fdb689c13494f7136` |

Fable missed the collection cutoff and was not read.  No other current-round
prompt or submission was inspected.  This audit is frozen without promotion
or descendant launch.
