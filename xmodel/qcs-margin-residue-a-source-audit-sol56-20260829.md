# QCS-MARGIN/v1 source-completeness audit for the filed residue-A template

Author: Sol 5.6 source-audit lane  
Date: 2026-08-29 UTC  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PROVISIONAL READ-ONLY SOURCE AUDIT / REVIEW REQUIRED / NO CANONICAL CONSUMER`

## 0. Verdict

The proposed `QCS-MARGIN/v1` discriminator cannot be run on the filed
`td=6` two-pole residue-A template.

```text
disposition       = UNDERDETERMINED
first_absent      = PairRef / actual polynomial-map provenance
Xi_min            = NOT_COMPUTED
Xi_full           = NOT_COMPUTED
n=sum_i deg(P_i)  = NOT_CHECKED
downstream_budget = NONE
```

This is the producer's specified fail-closed outcome, not a numerical verdict.
Its conservative source-packet proposal requests the actual pair and fibre
rider, the complete proper-critical-value quotient flag set, every descended
first-coordinate polynomial and its degree, every generic-high baseline, the
genus and physical end counts, an independent end-count check, and the
exit-flag-to-quotient-line map
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:434-469`).  It orders
missing or inconsistent input to return `UNDERDETERMINED`, and expressly
forbids manufacturing quotient degrees from reduced orbit counts
(`ibid.:453-468`).

For speed, however, two numerical tiers must be distinguished.  The exact
Section-7 identities give the **minimal PCB-margin evaluator**

```text
Xi_min = E_gen-(s-1) = d-s-sum_i b_i.                   (MIN)
```

It needs an actual pair/generic fibre, the complete quotient-flag/baseline
inventory, and `d,s`; it does **not** need the quotient degrees, `G`, or `n`.
The collision/Suzuki expression

```text
Xi_full = sum_i b_i(d_i-1)-(2G+2s+n-2)                 (FULL)
```

is an independent source-completeness cross-check and mechanism locator.  On
a valid full packet `Xi_min=Xi_full`.  The exit-flag map is a third,
downstream-consumption gate rather than an input to either bare integer
evaluation.  Residue A fails already before this distinction can save a run:
there is no `PairRef` and no complete quotient-baseline inventory.

One requested integer is visibly present at the formal-template tier:
`s=2`, because the two order-three pole places exhaust `td=6`.  That partial
fact cannot be combined with selected fixed-fibre charges to compute `Xi_min`,
and it cannot be combined with an abstract-cover genus or formal series counts
to compute `Xi_full`.  The filed object remains a formal/book-relative
template, not an actual polynomial Keller map.

## 1. Typed target and audit rule

For the proposed discriminator, the notation is

```text
U_i=A1_z,             phi_i=(P_i,Q_i),
d_i=deg(P_i),         b_i=kappa_i^+(u_i-1),
G=generic compactification genus,
s=# physical pole ends,       n=# physical finite-value ends,

Xi_min = d-s-sum_i b_i,
Xi_full=sum_i b_i(d_i-1)-(2G+2s+n-2).
```

Indeed `d-1=sum_i I_i` and `E_gen=sum_i(I_i-b_i)`, so
`E_gen-(s-1)=d-s-sum_i b_i`; the collision/Suzuki derivation proves that this
equals the full expression
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:14-45,231-259`).
On a generic fibre, `i` indexes proper critical-value flags/quotient lines,
whereas physical pole places, physical finite-value places, and direction
clusters are different typed sets (`ibid.:149-152`).  The campaign-wide type
audit likewise distinguishes a place/ray, its several possible conjugate
Puiseux series, and an orbit-level critical-value flag
(`xmodel/flag-place-series-consumer-audit-sol56-20260829.md:74-98`).

Accordingly this audit uses three evidence labels:

- `FILED`: the exact required object is serialized for one source-bearing
  generic fibre;
- `FORMAL/PARTIAL`: a book-relative number or necessary-data statement exists,
  but not the required source object;
- `MISSING`: the required object is neither serialized nor recoverable without
  a new mathematical construction.

`FORMAL/PARTIAL` is not silently upgraded to `FILED`.

## 2. Field-by-field completeness table

| required field | role | status | what is actually filed | why the stated role cannot consume it |
|---|---|---|---|---|
| `PairRef` / actual-map provenance | `MIN`, `FULL`, downstream | **MISSING — first blocker** | A rigid formal Puiseux/Newton genome, fixed-depth coefficient systems, and modular source controls | No characteristic-zero polynomial pair with serialized coefficients/support and `J(f,g)=1` certificate is filed. |
| generic fibre value/rider | `MIN`, `FULL`, downstream | **FORMAL/PARTIAL** | The notation `C={f=a}` for a hypothetical generic residue-A fibre, with conditional smoothness and irreducibility | No actual `f`, named `a_gen`, or source rider is serialized.  The stronger full rider cannot exclude critical/exceptional images of the absent `P_i`. |
| complete proper-cv quotient flag set | `MIN`, `FULL`, downstream | **MISSING** | One x-side flag is pinned formally; selected y-side exit-carrier information and lower floors exist | There is no complete indexed reference quotient-flag inventory for one actual fibre.  The B-side finite-end/cv data remain unconstructed or ungrouped. |
| every descended `P_i` | `FULL` cross-check | **MISSING** | Tree-pattern polynomials and pole vertices named `P_i` occur in the ladder files | Those are not the Section-7 maps `P_i:U_i->A1`; no residue-A quotient map is serialized.  This does not block `MIN` once its smaller source packet exists. |
| every `d_i=deg P_i` | `FULL` cross-check | **MISSING** | Degree-42 series/place controls, tree-pattern degrees, and degree-six monodromy passports | None is a quotient degree.  No `d_i` list exists.  These degrees are unnecessary for `MIN`. |
| every `b_i=kappa_i^+(u_i-1)` | `MIN`, `FULL` | **MISSING AS A PACKET** | Partial fixed-fibre charges: the x-side control has one flag with `kappa=1`, and the R3 ledger has selected y-side total `lambda=2` | No complete per-quotient generic-high baseline list or quotient-line association is filed.  A total selected floor is not a list of `b_i`. |
| `d` | `MIN`, consistency | **FORMAL-TEMPLATE FILED: `6`** | The residue-A book and pole profile have `td=6` | It is not tied to an actual `PairRef`; by itself it cannot license `MIN`. |
| `G` | `FULL` cross-check | **UNDERDETERMINED** | A symbolic genus formula and a `G=18` abstract B-unramified Hurwitz control | The B-side tail/place/ramification data are unpinned, and the `G=18` cover is expressly not a plane polynomial fibre.  `G` is unnecessary for `MIN`. |
| `s` | `MIN`, `FULL` | **FORMAL-TEMPLATE FILED: `2`** | Two pole places, each of `g`-order three, exhaust `td=6` | This is conditional on realizing the formal residue-A genome; it supplies no missing PairRef or quotient baselines. |
| `n` | `FULL` cross-check | **UNDERDETERMINED** | The squarefree generic x-side control gives 42 physical x-places; the B-side has 42 series with unpinned place partition | The total number of physical finite-value places is not a filed integer.  `n` is unnecessary for `MIN`. |
| independent `n=sum_i deg P_i` | `FULL` cross-check | **UNAVAILABLE** | The identity is proved abstractly in the QCS producer | Both the numerical `n` and all quotient degrees are absent, so the source-level check cannot run. |
| selected exit flag `->` quotient-line `i` | downstream budget consumer | **MISSING** | Actual first-exit theorems map fixed-fibre exits to distinct same-ray cv carriers and unique attachment vertices | Their codomain is not a serialized Section-7 quotient-line index, and the formal residue-A object supplies no cross-fibre quotient map.  This map is not needed merely to print `MIN` or `FULL`. |

Both numerical tiers therefore fail at their first field.  The later rows are
recorded to prevent a future caller from bypassing the first failure by mixing
controls, and the role column prevents the full cross-check from needlessly
blocking a future minimal evaluator.

## 3. Exact source evidence

### 3.1 No `PairRef` or actual polynomial map

The template calls itself `FORMAL-CANDIDATE` and says that the coefficient
lift passes the audited edge constraints
(`ladder/SHEET6-TEMPLATE.md:11-31,269-283`).  Its own residual list states that
everything between the genome and an actual pair remains to be supplied,
including global Jacobian closure (`ibid.:285-317`).  The campaign checksum is
equally explicit: the reviewed two-pole terminal object is a formal-candidate
template and a local terminal-class book, not a global survivor or landing
theorem (`ladder/SHEET6-CAMPAIGN.md:16-34,209-214`).

The current canonical ledger preserves that boundary.  It describes the filed
residue-A object as book-relative and not a characteristic-zero polynomial
counterexample (`AUDIT.md:54-62`).  The deepest exact D43 carrier is nonempty
at modular/fixed-depth tiers, but the source index explicitly withholds a
common characteristic-zero point, germ, or Keller pair
(`AUDIT.md:2265-2293`).

The monodromy file supplies no substitute.  Riemann existence yields an
abstract compact curve cover, but not a plane curve with the pinned Newton
corner or a polynomial `g` satisfying the Keller identity
(`ladder/GROK-MONODROMY.md:357-365`).  Its residual algebraization problem is
stated again at `ladder/GROK-MONODROMY.md:393-399`.

Thus no exact source object can occupy the producer's first required field.

### 3.2 The generic fibre is a conditional description, not a packet

`ladder/GROK-MONODROMY.md:28-46` writes
`C={f=a}` for a generic fibre and derives smoothness, irreducibility, and the
degree-six meromorphic `g`-map under the hypothesis that the residue-A data
come from a Keller pair.  Since no such pair is serialized, this is a
conditional fibre description.

The full collision derivation additionally chooses `a_gen` outside the
critical values of every descended `P_i`, every `P_i(0)`, and every
exceptional-weight image
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:175-182`).  With no
descended `P_i` and no exceptional-weight packet, the residue-A files cannot
state that full rider.  `MIN` need not enumerate those `P_i`-images once an
actual generic fibre and its complete baseline inventory are independently
certified, but neither object is present here.  A bare symbolic word “generic”
is not the required source-bearing fibre record for either tier.

### 3.3 The quotient flags and polynomials are absent

The Section-7 quotient object has a precise type.  For each reference
critical-value flag it is an abstract quotient line `U_i=A1_z` with a
polynomial map

```text
phi_i(z)=(P_i(z),Q_i(z)),
```

and its quotient points parametrize finite-value direction clusters
(`xmodel/sigray-section7-resolution-free-coordinator-repair-sol-ultra-20260828.md:237-283`).

No such residue-A list appears in the canonical source files.  In particular,
the symbols `P_i` in the template are the two **pole vertices** of its tree
(`ladder/SHEET6-TEMPLATE.md:33-46,106-111`), not descended first-coordinate
polynomials.  The displayed tree patterns, the leading degree-42 x-side
coefficient equation, and the polynomial `L(a_3)` used in the monodromy
control have different domains and codomains.

Only partial flag information is filed.  The repaired LR2 statement gives one
x-side cv flag with `kappa_G=1` and common truncation through it
(`ladder/SHEET6-LROOT.md:156-192`).  By contrast, the template's residual R3
states that the B-orbit cv vertices and x-side cv-side patterns are
unconstructed (`ladder/SHEET6-TEMPLATE.md:303-309`).  Current global scope
independently records that the residue-A vertical data are not grouped by
target component and that no horizontal finite-end list exists
(`AUDIT.md:1994-2002`; `APPROACHES.md:778-795`).

Therefore neither a complete proper-cv quotient flag set nor even one
source-typed descended `P_i` is filed.  The first absence blocks `MIN`; the
second blocks the `FULL` cross-check.  It follows immediately that the
quotient degree list is absent.

### 3.4 Partial charges are not a baseline table

The QCS baseline is not an arbitrary selected floor.  It is the generic-high
quantity

```text
b_i=kappa_i^+(u_i-1)
```

on a named quotient line
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:110-129`;
`xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md:115-128`).

There are useful partial local numbers.  LR2 gives the formal x-side flag and
`kappa_G=1`; the monodromy control pins its first split to height three
(`ladder/GROK-MONODROMY.md:133-147`), so that control has local charge two.
The R3 residue-A ledger also records selected y-side mass `lambda=2`
(`ladder/SHEET6-LROOT.md:238-250`).  But it does not enumerate each Section-7
quotient line or identify its generic-high lattice value.  In particular, a
total selected y-side floor cannot be split into per-line `b_i` values without
the absent flag and quotient packet.

The QCS producer itself makes this dependency binding: a generic excess may
lower a downstream ceiling only after selected flags are mapped into the full
quotient flag set, and it forbids subtraction on a formal pole/merge floor
before generic-fibre provenance is constructed
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:422-432`).

### 3.5 The full `G,s,n` cross-check triple is incomplete

The pole count is the one clean formal integer.  Each of the two pole places
has `g`-pole order three, there are no other poles, and the profile is `(3,3)`
(`ladder/GROK-MONODROMY.md:102-120`).  The classical source records the same
degree exhaustion (`ladder/SHEET6-CLASSICAL.md:47-52`).  Thus an actual map
realizing precisely this genome would have `s=2`.

The genus is not comparably pinned.  The classical calculation gives

```text
G=2763-(SigS/42+SigU+r_B+r_X)/2,
```

with B/x contact sums and place counts in the formula
(`ladder/SHEET6-CLASSICAL.md:112-131`).  The B-side ramification and place
partition remain optional/unpinned in the monodromy control
(`ladder/GROK-MONODROMY.md:206-218`).  Taking the generic squarefree x-side
and the allowed B-unramified completion gives the displayed `G=18`
(`ibid.:220-241`), but the file expressly limits this to an abstract cover,
not the required plane polynomial fibre (`ibid.:357-365`).  Therefore `18`
is a control value, not the QCS field `G` for an actual residue-A `PairRef`.

The finite-end count is also incomplete.  On the generic squarefree x-side,
the degree-42 leading coefficient equation yields 42 distinct physical
x-places (`ladder/GROK-MONODROMY.md:149-174`).  The B-side consists of 42
series whose physical place partition is unpinned, with degrees only known to
lie in `7 Z` (`ibid.:48-55,206-218`; see also
`ladder/SHEET6-CLASSICAL.md:33-50`).  Hence no total numerical `n` is filed.

Even the valid x-place count is not a quotient degree.  A quotient degree may
be checked against physical ends only after the complete flag and descended
map construction; it may not be inferred from the number of conjugate series,
formal orbits, places in one partial sector, or a monodromy passport.

### 3.6 The existing exit theorem has the wrong downstream codomain

The current two-pole rider is a real fixed-fibre theorem: every actual up
non-chain microchild has a complete set of distinct same-ray cv carriers with
unique attachment to the two-pole path union, and different direction/vertex
sets are disjoint.  Its alias `FULL_ACTUAL_FIRST_SEPARATION=FULL_ACTUAL_EXIT`
means complete carrier plus a lower floor, never attainment
(`ladder/SHEET6-2POLE.md:3-14`; canonical summary `AUDIT.md:814-843`).

That theorem maps an actual exit to a cv carrier and attachment vertex.  It
does not serialize the further map

```text
selected book exit flag -> reference quotient-line index i
```

required by the proposed downstream portion of `QCS-MARGIN/v1`
(`xmodel/pcb-generic-collision-surplus-sol56-20260829.md:436-445`).  Since the
complete quotient index set is absent, no such mapping can be checked for
injectivity or completeness.  This blocks consumption of a future positive
margin by the selected book, not the bare integer evaluation of `Xi_min` or
`Xi_full`.

## 4. Fail-closed evaluation

The accelerated minimal evaluator has the gates

```text
M0  exact PairRef + polynomial/Jacobian provenance          MISSING
M1  actual generic fibre + complete quotient flags/b_i      NOT REACHED
M2  source-certified d,s                                    NOT REACHED
M3  Xi_min=d-s-sum_i b_i                                    NOT REACHED
```

The independent full cross-check then has the additional gates

```text
C0  every descended P_i and degree d_i                      MISSING
C1  actual G,n and independent n=sum_i d_i                  MISSING
C2  Xi_full=sum_i b_i(d_i-1)-(2G+2s+n-2)                   NOT REACHED
C3  Xi_min=Xi_full                                          NOT REACHED
```

Finally, using a positive margin in a selected book has the separate gate

```text
D0  selected-exit-to-quotient-line mapping                  MISSING
```

Therefore the unique licensed output is

```text
MIN-PCB-MARGIN / FULL-QCS-CROSSCHECK(residue-A filed template)
  = UNDERDETERMINED(first_absent=PairRef).
```

No provisional value at either tier is printed.  For `MIN`, formal `d=6` and
`s=2` cannot be combined with selected lower floors in place of the complete
`b_i` inventory.  For `FULL`, the combinations
`(G,s)=(18,2)`, “42 x-series,” “42 x-places,” a guessed B-place count, and
selected charge totals do not belong to one source-complete QCS packet.

## 5. Smallest completion task

To make the **minimal** discriminator executable on residue A, a future
producer must serialize one common packet containing:

1. an actual characteristic-zero polynomial `PairRef=(f,g)`, including
   coefficient/support custody and a verified nonzero constant Jacobian;
2. one actual generic fibre value/rider;
3. the complete proper-cv reference quotient-flag set on that fibre, with
   every generic-high baseline `b_i`; and
4. source-certified `d` and the complete physical pole list giving `s`.

Those four objects suffice to compute `Xi_min=d-s-sum_i b_i`.  A **full
collision/Suzuki cross-check** should additionally serialize, for every flag,
the quotient line and descended `(P_i,Q_i)`, exact `d_i=deg P_i`, the actual
compactification genus and physical finite-end list giving `G,n`, and the
independent equality `n=sum_i d_i`.  A **downstream selected-book consumer**
must further map every selected exit flag to its quotient-line index.

The absence of these tiered packets is a mathematical source/construction
debt, not a need for CAS or for interpreting existing formal counts more
aggressively.  Future scheduling should run `MIN` as soon as its four-object
packet exists, while building `FULL` and the downstream mapping in parallel.

## 6. Nonclaims

This audit does not:

- refute or prove `QCS`, `PCB-EXCESS`, or any Section-7 identity;
- assert that the missing quotient lines or polynomials do not exist for a
  hypothetical actual residue-A map;
- refute the formal residue-A genome, its fixed-depth source systems, the
  formal value `s=2`, the generic x-side 42-place control, or the abstract
  `G=18` Hurwitz cover;
- turn absence of a `PairRef` into an exclusion of `td=6`;
- produce a Keller map, counterexample, landing theorem, degree ceiling,
  budget reduction, or result on JC2;
- identify pole vertices, places, flags, quotient points, or conjugate series;
- infer any quotient degree from 42 series, 42 places, tree-pattern degrees,
  reduced orbit counts, or monodromy cycles; or
- claim that `P_i,d_i,G,n` or the exit mapping are prerequisites for the
  cheapest integer evaluation once a valid `MIN` source packet exists; or
- authorize a canonical-ledger edit, a downstream consumer, CAS, AWS work, or
  a web search.

The maximum conclusion is the typed source verdict
`UNDERDETERMINED(first_absent=PairRef)`.

## 7. Audit perimeter

This was a read-only inspection of the sealed QCS producer and the relevant
canonical residue-A, Section-7, scope, and type-audit sources on frozen basis
`31777ce90994a106aade85064c0d868e32863f94`.  No mathematical computation,
web access, AWS action, external-model call, or canonical file edit was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20257`.
- Body SHA-256:
  `3e1a3824e0d4db85281f12b0c7de6c3b9d785ff5fca8148cecc7dd7c35c97be3`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
