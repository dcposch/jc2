# Producer-side pre-review: coordinate-fibre connectedness theorem

## 0. Scope, integrity, and verdict key

This is an **UNCHARGED producer-side advisory**.  It neither promotes the
packet nor satisfies the separate different-model gate.  I inspected only the
three frozen inputs named in the request, did not inspect any other review or
`jc2-lean`, ran no CAS, and made no charged or canonical edit.

Before mathematical reading, the frozen copies reproduced the required
SHA-256 values exactly:

```text
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
8abde87c3e9320ae1b75e90d4c4c26e4a7a16dc685398bf446b5b33b230f9787  block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
```

Below, `FC`, `VS`, and `VP` abbreviate those three files respectively;
citations are frozen-input line numbers.  `CONFIRMED` means the stated claim
follows from the weakest identified hypotheses, `REFUTED` means a displayed
claim or typing has a counterargument, and `GAP` means the conclusion may be
true but the accepted premises do not establish it.

## 1. Executive verdict

The central theorem is **CONFIRMED** for both coordinates.  The intrinsic
normalization/unit/bracket argument proves

```text
C(f)^alg intersect K=C(f),       C(g)^alg intersect K=C(g),
```

so both general coordinate fibres are geometrically irreducible and
connected.  The degree-four hypothesis and every boundary-census assertion
are unnecessary for that proof.

The packet nevertheless has one material consistency defect.  Its claim that
codimension-one census exhaustivity is absent is **REFUTED on the literal
frozen statements**: the asserted exhaustive general-slice ledgers in both
coordinate directions imply it by a short cross-slice argument.  If those
ledgers are not regarded as proved, the census remains a genuine `GAP`, but
then `(3.2)`, the `d_h` table, and `(3.6)` must be conditional as well.  The
packet cannot keep both positions.

Repaired `(2.5)` and the relative-closure theorem are unconditional on that
choice.  The partition arithmetic and the new consistency clause are exact
once the frozen `E_h=0` finite-place assertion is accepted.  The special-fibre
OPEN and the surviving valuation OPENs are correctly conservative.

## 2. Main algebraic argument for `f`

**Verdict: CONFIRMED.**  The proof at FC 169--225 is sound, with normality
of the exact ring supplied by the following one-line check.

Let `q=U^2-A-A^2Z`.  It is irreducible (view it as a primitive linear
polynomial in `Z`), so `R` is a domain.  The three partials
`(-1-2AZ,2U,-A^2)` have no common zero on `V(q)`; hence `R` is smooth and
normal.  In its fraction field,

```text
K=C(A,U),                         Z=(U^2-A)/A^2,
```

as asserted at FC 171--180.

Put `E=C(f)` and let `L` be its relative algebraic closure in `K`.  It is a
finite separable extension of `E`.  Its smooth projective curve `Tbar` is
rational: the inclusion `L subset C(A,U)` gives a dominant rational map from
a rational surface to `Tbar`, and a general line restricts nonconstantly,
making `Tbar` a unirational complex curve and therefore `P1`.  This is the
only use of rationality.

Let `T` be the normalization of `A1_f` in `L`.  Every element of `O(T)` is
integral over `C[f]`, hence integral over `R`; normality puts it in `R`.
Thus `O(T) subset R` directly, without `Y`, its boundary, or the factorization
in FC 115--167.

The unit computation in FC 182--205 is exact.  Localization gives
`R_A=C[A,A^{-1},U]`, so a unit of `R` is `cA^n` in that Laurent polynomial
ring.  At the height-one prime `(A,U)`, `U` is a uniformizer and
`A=U^2/(1+AZ)`, so `ord(A)=2` (also VS 90--94).  A global unit has order zero,
forcing `n=0`; hence `R^*=C^*`.  Since `O(T)^* subset R^*`, the open curve
`T=P1-tau^{-1}(infinity)` cannot omit two or more points: two omitted points
support a nonconstant unit with divisor their difference.  The omitted set is
nonempty, so it consists of one point.  Choosing it as infinity gives

```text
O(T)=C[t],             L=C(t),             f=P(t),
[L:C(f)]=deg(P).
```

This is where rationality plus units stop: they force a polynomial
decomposition, not its linearity.  The charged bracket is decisive.  Since
`t,g in R`, the chain rule gives

```text
kappa={f,g}=P'(t){t,g}.
```

Both factors are in `R`, and their product is a unit.  Therefore `P'(t)` is a
unit, hence a nonzero scalar; characteristic zero and transcendence of `t`
force `deg(P)=1`.  Consequently `L=C(f)`.

An exact hostile candidate shows what this last step kills.  Take
`f_0=A^4`, `g_0=U`.  Then
`[K:C(f_0,g_0)]=[C(A,U):C(A^4,U)]=4`, while the relative closure of
`C(A^4)` in `K` is the proper field `C(A)`.  It passes the rationality/unit
reduction with `t=A`, `P=t^4`.  But the actual bracket gives
`{A^4,U}=8A^5`, not a unit.  Thus degree four is insufficient and the
constant-unit bracket excludes precisely this type of intermediate field.
The divisibility observation at FC 93--95 is correct but redundant; neither
degree four nor any census fact is used in the intrinsic proof.

## 3. Symmetry and the argument for `g`

**Verdict: CONFIRMED.**  Nothing in the preceding argument privileges `f`.
For the relative closure `L_g` of `C(g)`, the same rationality argument makes
its projective curve `P1`; normality embeds the affine normalization in `R`;
and `R^*=C^*` leaves one point at infinity.  Hence `L_g=C[t]` and `g=Q(t)`.
Now

```text
kappa={f,g}=Q'(t){f,t},
```

so `Q'(t)` is a unit of `R` and `deg(Q)=1` (FC 249--279).  The sign is
correct: the formula uses `{f,Q(t)}`, whereas the restricted Hamiltonian
field later satisfies `X_g(f)={g,f}=-kappa`.  The symmetry needs no horizontal
boundary assertion and no interchange of an unproved census.

## 4. Boundary route and census-exhaustivity interface

**Verdict on the route up to its last step: CONFIRMED.  Verdict that the last
interface is genuinely absent from the frozen inputs: REFUTED.**

If `delta=[L:C(f)]>1`, the connected cover `Tbar->P1_f` must ramify over a
finite value.  If all ramification were over infinity, then, with `r` points
there, its ramification would be `delta-r<=delta-1`, and Riemann--Hurwitz would
give `2g(Tbar)-2<=-delta-1<-2`, impossible (FC 89--113).  The normalization
factorization through `T x A1_g` is also valid: `O(T)[g]` lies in the
normalization `O(Y)`, and finite generators over `C[f,g]` remain generators
over the intermediate ring.  A divisor over a ramified point `q` then has

```text
ord_D(f-a)=e(D/({q}xA1_g)) e(q/a)>1,
```

so etaleness removes it from `S` and finiteness makes its image the entire
vertical line (FC 115--157).  The coordinate-swapped construction gives a
horizontal line.  These steps are sound.

FC 40--55 is narrowly right that neither a cofinite image nor an exhaustive
statement about a *general vertical slice alone* excludes a vertical boundary
divisor.  It overlooks the frozen assertion in the other direction.  VS
398--413 says that on a general `f`-slice there are **no other finite deleted
points** beyond the listed `B`-points, and VS 446--453 invokes the
coordinate-swapped conclusion.  VP 103--113 expressly confirms the former and
applies the same discussion after interchange.  FC itself consumes both
versions at 291--329.

Here is the exact cross-slice lemma.  Let `D` be a prime divisor of `Y-S` and
`C=pi(D)`.  Since `Y->A2` is finite, `C` is a curve.  If `f|C` is nonconstant,
a general vertical line meets `C`; unless `C=B`, this supplies an extra finite
deleted point outside `B`, contradicting the frozen `f`-slice assertion.  If
`f|C` is constant, `C` is vertical and `g|C` is nonconstant, so a general
horizontal slice gives the same contradiction using the `g` assertion.
Thus every boundary-divisor image is `B` (a stronger conclusion than the
ramified `(BC)` needed by the proof).  In particular the Stein-produced
vertical or horizontal divisor is impossible because the cuspidal `B` is
neither coordinate line.

There are therefore only two coherent readings:

1. Accept the frozen two-sided “no other finite deleted points” claims, as FC
   does in its table.  Then `(BC)` follows, and
   `OPEN[CENSUS-EXHAUSTIVITY]` at FC 447--450 must be removed; the boundary
   proof closes redundantly.
2. Treat the unsupported inference “there are no other” at VS 405--407 as the
   intended open interface.  Then both general-slice assertions must be
   demoted, and §5.2's equality with `d_h` and its table provenance become
   `GAP` as well.

The packet cannot consume those assertions in both coordinate directions and
simultaneously type their codimension-one consequence `OPEN`.  Its
`(x,y)->(x^4+x,y)` countercontrol (FC 56--65) illustrates only one-directional
failure: every general horizontal slice detects its deleted vertical
divisors, so it does not satisfy the frozen symmetric slice assertion.

**Independence check: CONFIRMED.**  The intrinsic proof in §§2--3 above uses
only normality, `K=C(A,U)`, `R^*=C^*`, and the unit bracket.  Its backward
reference to §3.2 is needed only for `O(T) subset R`, which follows directly
from integrality and normality.  It imports no boundary conclusion.

## 5. Re-derived identities and partition table

### 5.1 `(2.5)`

**Verdict: CONFIRMED from the newly proved connectedness.**  Let `h` be one
coordinate, `k` the mate, and `D=X_h|C_h`; then
`D(k)=epsilon_h kappa`, with `epsilon_f=1`, `epsilon_g=-1`.  At a finite
deleted place and at a place over infinity, respectively,

```text
k-k(p)=z^e:       D=(epsilon_h kappa/e) z^(1-e) partial_z,
k=z^(-e):         D=-(epsilon_h kappa/e) z^(e+1) partial_z.
```

Thus the pole and zero orders are `e-1` and `e+1`.  On the connected
degree-four completion,

```text
sum_infinity e=4,             R_infinity=4-r_h.
```

Riemann--Hurwitz gives

```text
2gamma_h-2=-8+R_fin+(4-r_h),
R_fin=2gamma_h+2+r_h.
```

Consequently

```text
deg Zero(D)=4+r_h,
deg Pole(D)=2gamma_h+2+r_h,
deg div(D)=2-2gamma_h,
```

exactly FC 298--315.  The local attainment comes from the displayed
uniformizers, not a valuation floor.

This agrees exactly with VP's multi-component correction.  If there are
`delta` components, total genus `G`, and total `r` infinity places, summing
componentwise gives

```text
deg Zero(D)=4+r,
deg Pole(D)=2G+4-2delta+r,
deg div(D)=2delta-2G                         (VP 87--95).
```

At `delta=1`, `G=gamma_h`, and these are precisely the repaired identities.

### 5.2 `(3.2)` and the table

**Verdict: CONFIRMED under the frozen general-slice assertion, but not from
connectedness alone.**  If the finite ramified places are exactly the `d_h`
transverse `B`-places and each has `e=2` (VS 398--413), then `R_fin=d_h`, so

```text
d_h=2gamma_h+2+r_h.                              (3.2)
```

The pole orders at infinity are a positive partition of four of length
`r_h`; the list in FC 335--340 is exhaustive:

| `r_h` | `lambda_h` | necessary `d_h` |
|---:|---|---:|
| 1 | `(4)` | `2gamma_h+3` |
| 2 | `(3,1)` or `(2,2)` | `2gamma_h+4` |
| 3 | `(2,1,1)` | `2gamma_h+5` |
| 4 | `(1,1,1,1)` | `2gamma_h+6` |

All rows are necessary only; none asserts existence or attainment.

If the slice exhaustivity is instead left open, define

```text
E_h=sum(e_p-1)
```

over finite ramified deleted places not among the `d_h` transverse
`B`-places.  The safe formula is then

```text
d_h+E_h=2gamma_h+2+r_h,
```

or `d_h+E_h=2G_h+4-2delta_h+r_h` before connectedness.  Full absence of other
deleted points is stronger than the exact extra hypothesis needed here;
`E_h=0` suffices.  Thus the arithmetic is correct, but retaining the packet's
census OPEN would give `(3.2)` and the `d_h` column a `GAP`.

### 5.3 `(3.6)`

**Verdict: CONFIRMED conditional on `(3.2)`.**  The new clause

```text
gamma_h=(d_h-r_h-2)/2
```

is essential.  Parity and nonnegativity of `d_h-r_h-2` do not constrain an
independently recorded genus: `(d,r,gamma,lambda)=(5,1,17,(4))` passes the old
literal tests and violates `(3.2)` (VP 115--121; FC 348--367).  Together with
`d_h>=3` and the positive-partition condition, the repaired exclusions are
arithmetically complete for these necessary invariants.  If `E_h` has not
been killed, however, the consistency equation becomes
`gamma_h=(d_h+E_h-r_h-2)/2`, and every `d_h`-only exclusion in `(3.6)` remains
open.

## 6. Special fibres, bad values, and geometric irreducibility

**General-fibre verdict: CONFIRMED.**  In characteristic zero, relative
algebraic closedness of `C(h)` in `K` makes `K/C(h)` regular, so the generic
`h`-fibre is geometrically integral.  Geometric integrality spreads after
shrinking `A1`; its complement is finite (FC 78--83, 223--225, 276--279).

Every fibre is smooth and reduced.  Indeed, the nonzero constant bracket makes
`df,dg` independent everywhere on the smooth surface, hence `pi=(f,g)` is
etale; composing with either projection `A2->A1` is smooth.  On a smooth curve,
distinct irreducible components are disjoint, so connectedness and
irreducibility agree.  Every fibre is also nonempty without invoking the
packet's cofinite-image sentence: if `h-a` had no zero on affine `S`, it would
be a unit of `R`; `R^*=C^*` would then make nonconstant `h` constant.

**`OPEN[SPECIAL-FIBRES]`: CONFIRMED.**  Nothing supplied determines the
component counts or normalized boundary-place ledger at the finitely many
excluded values (FC 227--247, 451--453).  Smoothness does not close this for a
nonproper family.  As a desk control,

```text
Spec C[t,x,y]/(x(x-1)-ty) -> A1_t
```

is smooth, has connected generic fibre `A1`, and has the disconnected smooth
fibre `{x=0} disjoint_union {x=1}` at `t=0`.  This is not proposed as a charged
model; it verifies the logical need for the OPEN.

For use of the boundary table, the safe general set is the intersection of
the geometric-integrality open with the open on which the charged
degree-four/general-slice assertion holds, followed by removal of the finitely
many listed singular, critical, tangency, and target-complement values.  FC
236--247 should say this intersection explicitly.  Under the literal
two-sided slice exhaustivity there are no extra coordinate-line boundary
components.  Under the alternative OPEN reading, coordinate-constant
components contribute finitely many additional bad values, but a missing
boundary curve nonconstant in `h` cannot be removed by finitely many
`h`-values; that is exactly why `(3.1)` and the table must then remain open.

## 7. Audit of OPEN typings and valuation corrections

The valuation repairs restated in FC 369--430 survive as follows.

- **CONFIRMED:** At the interior cusp companion,
  `Ohat_(S,u_c)=C[[p,q]]`, `X_f=kappa partial_q`, and
  `X_g=-kappa partial_p` (FC 396--407; VS 198--215).  The signs agree with
  `{f,g}=kappa`.

- **CONFIRMED:** The detectability statement is now properly narrow.  The
  unmarked formal vector-field germ is the translation pair and no fixed
  finite jet of that unmarked germ detects global non-local-finiteness.  A
  full *marked* expansion of a finite algebra generating set can detect it by
  failure of a constant-coefficient polynomial recurrence (FC 409--423; VP
  58--66).  This does not confuse a finite jet with the whole marked series.

- **CONFIRMED:** The local divisor formula `(2.1)` and uniformizer iteration
  `(2.4)` are componentwise exact.  Once a finite ramified place exists,
  Riemann--Roch and the same local calculation give
  `ord_p(D^jH)=-M-je_p` with a nonzero coefficient product, so `(2.6)` is
  exact.  Its repaired provenance at FC 369--392 is now sufficient:
  connectedness plus degree four gives
  `R_fin=2gamma_h+2+r_h>0`, independently of the `B` census.  A transverse
  `B`-place is a second, conditional provenance route.

- **CONFIRMED with a proof-detail dependency:** The generic-boundary
  non-local-finiteness witness mentioned at FC 425--428 is valid, but its exact
  induction uses `D(W) subset s^{-1}W`, the inverse-different estimate inserted
  at VP 70--81.  FC does not itself restate that estimate.

- **CONFIRMED OPEN:** No charged length-three cusp-boundary completion, cusp
  Puiseux/Newton expansion, special-boundary leading term, or transport from
  monogenic order index to a dicritical jump is supplied (VS 236--241,
  297--298, 621--642; VP 139--145; FC 425--430).  The alternatives
  `u_c in Phi`, `L0/L1`, transverse/tangent, the integer `kappa_B`, and the
  actual numerical `(d_h,r_h)` also remain unresolved; no table row is proved
  to occur.

For FC §7 itself, `OPEN[SPECIAL-FIBRES]` is correctly typed, while
`OPEN[CENSUS-EXHAUSTIVITY]` is **REFUTED on the literal frozen assertions** by
§4 above.  If “two limitations remain” at FC 445 is meant only as a list of
connectedness-specific limitations, it is harmless after that correction; it
must not be read as closing the other valuation OPENs just listed.

## 8. Weakest hypotheses, corrections, blast radius, and falsification test

### Weakest intrinsic lemma

For one coordinate `h`, the proof needs only:

1. a normal finitely generated complex domain `R` with `R^*=C^*`;
2. rationality of the smooth projective curve belonging to the relative
   algebraic closure of `C(h)` in `Frac(R)` (rationality of `Frac(R)` is a
   sufficient stronger hypothesis); and
3. a complex derivation `D:R->R` with `D(h)` a unit.

Then the normalization argument gives `h=P(t)` with `t in R`, and
`D(h)=P'(t)D(t)` forces `P` linear.  For the charged pair take
`D(x)={x,g}` for `h=f`, and `D(x)={f,x}` for `h=g`.  Jacobi, degree four,
`Y`, `B`, the cusp, and all boundary data are unnecessary.  Alternatively,
independent smoothness of `h` can replace the final derivation condition:
if `P` were nonlinear, a root `alpha` of `P'` would make the nonunit
`t-alpha` vanish somewhere and force `dh=0` there.  In the charged setup that
smoothness is itself supplied by the unit bracket, so the bracket is not
decorative.

The no-nonconstant-units hypothesis is essential.  On
`C[t,t^{-1},s]` with `{t,s}=1`, the pair

```text
f=t^4,                    g=s/(4t^3)
```

has `{f,g}=1` and degree four, yet `C(t)` is a proper relative closure of
`C(t^4)`.  The countercontrol fails the exact-ring hypothesis precisely
because `t` is a unit.

### Corrections and blast radius

The producer must make one of two explicit census repairs.

- On the literal-input reading, insert the cross-slice lemma of §4 and delete
  `OPEN[CENSUS-EXHAUSTIVITY]`.  This also deletes references to possible
  vertical/horizontal boundary components.  The boundary proof becomes a
  redundant second proof, and §5.2 remains valid.
- On a proof-from-first-principles reading, type the “no other finite deleted
  points” inference in VS 405--407 as `OPEN`, carry `E_h` in §5.2, and make
  `(3.2)`, the `d_h` table, the genus formula, and `(3.6)` conditional on
  `E_h=0`.

This correction has no blast radius on the intrinsic relative-closure proof,
generic geometric integrality, repaired `(2.5)`, or the local formulas
`(2.1)`, `(2.4)`, and `(2.6)`.  The bad-value paragraph should additionally
say that it intersects all independently supplied genericity opens.  That is
a narrow bookkeeping repair.

**Best next falsification test.**  Produce the codimension-one support ledger
of `Y-S` (equivalently, normalize one genuine general vertical slice and one
general horizontal slice) and compute

```text
E_h=sum_outside_the_listed_B_places(e_p-1),       h=f,g.
```

One component with image different from `B`, or one place with `E_h>0`,
simultaneously falsifies the frozen exhaustivity claim and the stated
`d_h`-table provenance, while leaving the connectedness theorem and `(2.5)`
untouched.

## 9. Per-claim verdict table

| Claim attacked | Verdict | Hostile result |
|---|---|---|
| Exact `R` is normal, `K=C(A,U)`, and `R^*=C^*` | **CONFIRMED** | Gradient, localization, and the `(A,U)` valuation prove all three. |
| Relative closure of `C(f)` is trivial | **CONFIRMED** | Normalization gives `f=P(t)`; the unit bracket forces `P` linear. |
| `{f,g}=kappa` is merely decorative | **REFUTED** | `f=A^4,g=U` preserves rationality and degree four but has proper closure; its bracket is the nonunit `8A^5`. |
| Degree four is needed for primitivity | **REFUTED** | It gives only the unused divisibility `delta_h|4`; it is needed later for the quartic table. |
| Symmetric closure statement for `g` | **CONFIRMED** | The same normalization and unit argument applies, with no sign error. |
| General fibres are geometrically irreducible/connected | **CONFIRMED** | Relative algebraic closedness gives regular generic extensions and spreads over a nonempty open. |
| Every fibre is smooth, reduced, and nonempty | **CONFIRMED** | Unit bracket gives etaleness/smoothness; `R^*=C^*` rules out an empty fibre. |
| Special-fibre component counts are determined | **GAP** | Only general integrality is proved; `OPEN[SPECIAL-FIBRES]` is correct. |
| Boundary-route construction before `(BC)` | **CONFIRMED** | Riemann--Hurwitz, finite factorization, and the divisor valuation are exact. |
| Census exhaustivity is truly absent from all frozen statements | **REFUTED** | The two asserted exhaustive slice ledgers imply it crosswise. |
| Census exhaustivity is proved from the earlier VS argument | **GAP** | VS 405--407 does not itself classify the support of `Y-S`; choose one coherent repair. |
| Intrinsic proof silently consumes the census | **REFUTED** | Its only reused inclusion follows from normality alone. |
| Repaired `(2.5)` | **CONFIRMED** | Direct local orders plus connected Riemann--Hurwitz give all three degrees. |
| VP multi-component formulas specialize correctly at `delta=1` | **CONFIRMED** | `2G+4-2delta+r` becomes `2gamma+2+r`. |
| `(3.2)` and four-row arithmetic when `E_h=0` | **CONFIRMED** | `d_h=R_fin`; the positive partitions of four are exhaustive. |
| Unconditional `d_h` table while census remains OPEN | **GAP** | The safe identity is `d_h+E_h=2gamma_h+2+r_h`. |
| New genus-consistency clause in `(3.6)` | **CONFIRMED** | It excludes tuples passing parity but contradicting `(3.2)`. |
| Corrected existence/provenance for `(2.6)` | **CONFIRMED** | Connected quartic Riemann--Hurwitz already makes `R_fin>0`. |
| Cusp-companion and marked/unmarked correction | **CONFIRMED** | Exact translations and the infinite-jet distinction are stated safely. |
| Remaining cusp/valuation data are OPEN | **CONFIRMED** | No length-three completion, Puiseux data, row attainment, or index-to-jump transport is supplied. |

## 10. Final assessment

**Central claim: CONFIRMED.  Packet-level disposition: correction required,
not promotion.**  The independent rationality/unit/bracket proof is complete
for both coordinates and repairs the connected Riemann--Hurwitz ledger.  The
sole material defect is not in that theorem but in the packet's incompatible
treatment of two-sided slice exhaustivity: accept it and close the boundary
OPEN, or keep it open and carry `E_h` through the table.  No exit price is
asserted.

<!-- BODY-END -->
