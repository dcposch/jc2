# K00 ramified `(e,m)` calendar and finite-transition-type gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT SOURCE META GATE / FINITE CALENDAR FORMULAS / NO FINITE TRANSITION QUOTIENT PROVED**

## 0. Endpoint

On the normalized generic K00 ray, the literal V20R2 source admits an exact
general ramified calendar.  Its raw form depends on `(e,m)` and the five late
boundary orders.  After exact graph recentering it has a still sharper finite
bidegree table in the tangential order `m` and the first normal order `n`.
The table is source-complete: it is reconstructed from all 569 frozen tail
monomials, not extrapolated from the four solved cells.

The resulting meta verdict is

```text
PASS_EXACT_GENERAL_CALENDAR
NO_FINITE_TRANSITION_QUOTIENT_THEOREM
```

There is a finite rational/semilinear **calendar skeleton**, but none of the
available operations identifies the full jet-transition functors for
infinitely many `(e,m)` cells.  Uniformizer changes preserve `(e,m)`;
ramified base change reaches only coefficient-sparse subfunctors; gcd
reduction fails to scale the independent boundary orders; the residual
Kummer deck action scales nonzero character coefficients but cannot erase
them; graph recentering retains those coefficients and introduces the extra
normal order `n`; and the sharp sandwich `J^5 subset I subset J^2` gives a
growing order window, not a recurrence.

The four charged cells make the failure concrete.  The same fresh quadratic
cone occurs at the same grade and has different literal successors.  Thus a
recurrence which remembers only the cone/rank state, or only a primitive
ratio, is false.

The promoted scope is exactly `e=2,m=1` and `e=3,m=1`.  A concurrent
different-model review has now **confirmed** the `e=2,m=2` G10 producer,
which still awaits a binding integration.  The `e=3,m=2` G12 exclusion is an
exact producer with a passing replay and active review.  No provisional or
reviewed cell is promoted by this report, and no all-ramification closure
follows.

## 1. Literal source and cell parameters

After the licensed finite residue/Kummer extensions, put

```text
Lambda=tau^e,       C6=1,       e>=2,
ord_tau(d)=m>=1.
```

On the charged generic ray `ord_tau(k10)=ord_tau(Jdet)=0`.  For source-
partition routing one may more generally write these orders as
`h10,hJ in Z_{>=0} union {infinity}`; every K10 grade below acquires `+h10`
and the Jdet target acquires `+hJ`.  No boundary-cell conclusion follows
merely from that arithmetic.  For each of `k6,k2,mu2,mu4,mu6`, let its order
be respectively

```text
h6,h2,hmu2,hmu4,hmu6 in Z_{>=1} union {infinity};
```

order `infinity` means the zero series.  The seven rows are literally

```text
Phi_l = R_l(d)
      + tau^(2e)  k10 A10_l(d)
      + tau^(6e)  k6  A6_l(d)
      + tau^(10e) k2  A2_l(d)
      - targets_l,

targets_2=tau^(14e)mu2,
targets_4=tau^(16e)mu4,
targets_6=tau^(18e)mu6,
targets_7=tau^(19e)Jdet/4.
```

The signs do not affect the order calendar.  The exact frozen `d`-degree
minima, in row order `1,...,7`, are

```text
R:    2,2,2,2,2,3,2
A10:  2,2,2,2,2,2,2
A6:   1,1,1,2,1,2,1
A2:   1,1,1,1,1,1,1.                              (1.1)
```

These are equalities for the displayed polynomials.  The exact maxima are

```text
R:    4,4,5,5,5,6,6
A10:  3,4,4,4,5,5,5
A6:   2,2,3,3,3,4,4
A2:   1,1,1,2,2,2,3.                              (1.2)
```

The source pins are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json, 569 monomials
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse-Q source engine
```

Putting `Lambda=tau^e` removes the unit in `Lambda=u tau^e`; it does not
change `e`.  The weight-two Kummer normalization of the unit `C6` is a
separate unit-valued gauge and changes no order.  Once `Lambda=tau^e` is
fixed, a parameter automorphism preserving it is only
`tau -> zeta*tau`, `zeta in mu_e`; this is the residual deck action, not a
way to turn `e` into one.

## 2. Exact raw calendar

Without assuming that a branch has reached the graph, (1.1) gives the first
possible grades:

| sector | rows | first possible grade |
|---|---|---:|
| unloaded `R` | `1,2,3,4,5,7` | `2m` |
| unloaded `R` | `6` | `3m` |
| K10 | all | `2e+2m` |
| K6 | `1,2,3,5,7` | `6e+h6+m` |
| K6 | `4,6` | `6e+h6+2m` |
| K2 | all | `10e+h2+m` |
| `mu2` target | row 2 | `14e+hmu2` |
| `mu4` target | row 4 | `16e+hmu4` |
| `mu6` target | row 6 | `18e+hmu6` |
| `Jdet` target | row 7 | `19e` |

Every entry is a possible source arrival, not an assertion that its leading
coefficient survives earlier equations.  In particular, the K10 quadratic
at `2e+2m` vanishes on the leading tangent surface in all four charged cells.

The first raw representation wall is

```text
2e+2m = 3m   <=>   m=2e.                           (2.1)
```

For `m<2e`, the unloaded cubic precedes nominal K10.  At `m=2e` they must be
solved together.  For `m>2e`, K10 can enter before that cubic, so the
reviewed unloaded leading-plane passage cannot be imported without a new
mixed fan.

There are also raw homogeneous coincidences

```text
2e+2m = q*m,  q=3,4,5,6
<=> m/e = 2,1,2/3,1/2.                              (2.2)
```

They are bookkeeping walls only.  Exact graph cancellation and later series
coefficients decide the actual transition, so (2.2) is not a periodicity or
an emptiness theorem.

## 3. Exact graph/normal calendar

Use the exact graph

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T)
```

and exact normal coordinates in the four directions cut out by

```text
J=(d0-2d4-d4^2,
   8d1-(1+d4)d3,
   d2-d4-16d3^2,
   d5-2d3).
```

Write `d=D(S,T)+N`, after absorbing tangent components, with

```text
ord_tau(S,T)=m,       ord_tau(N)=n>m.
```

For a monomial of tangential/normal bidegree `(a,b)`, its pre-shift grade is
`a*m+b*n`.  Direct substitution in every frozen row gives the following
complete Pareto-minimal bidegree antichains.  Put
`G={1,2,3,5,7}`.

| sector | rows | Pareto-minimal `(a,b)` |
|---|---|---|
| `R` | `G` and row 4 | `(0,2)` |
| `R` | row 6 | `(0,3),(1,2)` |
| `A10` | `G` | `(0,2),(1,1),(3,0)` |
| `A10` | row 4 | `(0,2),(2,1)` |
| `A10` | row 6 | `(0,2),(2,1),(4,0)` |
| `A6` | `G` | `(0,1),(2,0)` |
| `A6` | row 4 | `(0,2),(1,1)` |
| `A6` | row 6 | `(0,2),(2,1),(3,0)` |
| `A2` | rows `1,3,5,7` | `(0,1),(1,0)` |
| `A2` | row 2 | `(1,0)` |
| `A2` | row 4 | `(0,1)` |
| `A2` | row 6 | `(0,1),(2,0)` |

The sector shifts `2e+h10`, `6e+h6`, and `10e+h2` are then added (with
`h10=0` in the charged cells).  This table is
strictly stronger than a surface-only calendar.  For example, on a centered
normal branch the main K10 rows can first occur at

```text
2e + min(2n,m+n,3m),                               (3.1)
```

whereas row 6 can first occur at

```text
2e + min(2n,2m+n,4m).                              (3.2)
```

Thus `(e,m)` does not determine even the possible centered arrival without
the extra state `n`.  Rank-stratum cancellations can delay these grades
further, as the four exact cells demonstrate.

On the exact graph (`n=infinity`) the table specializes to

| sector | rows `G` | row 4 | row 6 |
|---|---:|---:|---:|
| K10 | `2e+3m` | identically zero | `2e+4m` |
| K6 | `6e+h6+2m` | identically zero | `6e+h6+3m` |
| K2 | `10e+h2+m` | identically zero | `10e+h2+2m` |

The target grades are unchanged.  This recovers the reviewed surface
degrees `K10:3`, `K6:2`, `K2:1`, while also recording every exceptional
row and every normal-sector predecessor.

## 4. Ratio chambers and tie congruences

The following partition is conditional on having reached the exact graph.
Let `r=m/e`.  Compare the first main-row K10 grade

```text
nu10=2e+3m
```

with the other surface sectors.  Exact equality requires

```text
h6   = m-4e,
h2   = 2m-8e,
hmu2 = 3m-12e,
hmu4 = 3m-14e,
hmu6 = 3m-16e,
3m   = 17e                         (Jdet).          (4.1)
```

Because every `h` must be a positive integer, the coarse bands are:

| ratio band | sectors that may reach no later than K10 by choosing a finite positive order |
|---|---|
| `0<r<=4` | none; K10 is strictly first among the displayed surface loads |
| `4<r<=14/3` | K6, K2, `mu2` |
| `14/3<r<=16/3` | previous three, plus `mu4` |
| `16/3<r<17/3` | previous four, plus `mu6` |
| `r=17/3` | previous five, with Jdet tied to K10 |
| `r>17/3` | Jdet is earlier; all five variable sectors can also be earlier/tied/later according to their orders |

At the endpoints `r=4,14/3,16/3`, the corresponding right side in (4.1)
is zero, so the positive-order sector is still strictly later.

The exact arithmetic constraints at a tie are:

```text
h2 is even;
hmu2 is divisible by 3;
hmu4 == e   (mod 3);
hmu6 == 2e  (mod 3);
Jdet/K10 tie <=> (e,m)=q*(3,17), q>=1.             (4.2)
```

The first three surface sectors tie K10 simultaneously precisely when, for
`d=m-4e>0`,

```text
(h6,h2,hmu2)=(d,2d,3d).                            (4.3)
```

The smallest already registered example is `(e,m,d)=(2,9,1)`, where K10,
K6, K2, and `mu2` all reach G31 if the orders are `(1,2,3)`.

For a fixed complete load-order vector, ordering the finitely many affine
grade functions gives a finite semilinear chamber complex.  This is the
finite part of the answer.  It does not identify the transition equations
inside a chamber, and ratio alone is insufficient.  For example, with
`h6=1`, the same reduced ratio `m/e=9/2` gives

```text
(e,m)=(2,9):   nu10=31, nu6=31  (tie),
(e,m)=(4,18):  nu10=62, nu6=61  (K6 first).         (4.4)
```

Dividing by the gcd forgets the additive boundary order.  Scaling `h6` as
well would still reach only the coefficient-sparse base-change subfunctor,
not the full second cell.

## 5. Why the proposed reductions do not close the family

### 5.1 Uniformizer change and ramified base change

An automorphism of a DVR preserves every valuation, hence preserves `e` and
`m`.  A ramified base change `tau=sigma^q` multiplies all orders by `q`, but
its image has coefficients only in degrees divisible by `q`.  It is not
surjective onto the `(qe,qm)` cell.  Conversely, descending by `tau^q`
requires every coordinate series to lie in `K[[tau^q]]`; gcd divisibility of
the two leading orders does not imply that coefficientwise invariance.

The independently reviewed `e=2,m=2` fixture has

```text
S=8i*tau^2+3*tau^3,       T=tau^2+5*tau^3
```

and a nonzero odd normal lift.  It satisfies every row through G8 and first
fails at G9.  The hostile review strengthens this: the full odd G8 survivor
component forces both `N3!=0` and `N5!=0`, so it is disjoint from the
`tau^2`-pullback locus, not merely represented by one odd fixture.  Deleting
odd coefficients changes the transition.  This is an exact finite-jet
obstruction to using composition with `tau^2` as an equivalence of source
functors.  It does not assert a formal arc in that empty cell.

### 5.2 Kummer deck action

The residual action `tau -> zeta*tau` multiplies the grade-`j` coefficient by
`zeta^j`.  It permutes nonzero character coefficients; it cannot send one to
zero.  For `e=2`, it flips the essential odd coefficients above.  Quotienting
by the deck group retains only invariant series and therefore again selects
the sparse `K[[tau^e]]` subfunctor.  The separate weight action used to set
`C6=1` is unit-valued, fixes `Lambda`, and supplies no descent in `e`.

### 5.3 Graph recentering

The graph change is an exact polynomial coordinate change.  At a rank-zero
transition it absorbs only the tangent-plane part of the newest normal
coefficient into the corresponding next coefficients of `S,T`.  All later
surface and normal coefficients remain arbitrary and are shifted, not
deleted.  The state after recentering therefore includes at least

```text
(e,m,n, retained S/T jet, retained normal jet, load-order vector),
```

not just the fresh cone `Q` and its rank.  Sections 3 and 6 show that this
extra state changes the next map.

### 5.4 The sharp unloaded sandwich

The promoted theorem

```text
J^5 subset I subset J^2
```

is valuable but has the wrong type for a finite recurrence.  In graph
coordinates let `n=v(J(d))`.  For the unloaded ideal,

```text
2n <= v(I(d)) <= 5n.                               (5.1)
```

If all loads are absent below a grade `L` and the mixed equations force
`v(I(d))>=L`, then (5.1) gives only

```text
n >= ceil(L/5).                                    (5.2)
```

If the seven quadratic initials do not vanish at the leading normal
coefficient, then `v(I)=2n`, hence `n>=ceil(L/2)`.  A potentially degenerate
normal direction can therefore lie in the window

```text
ceil(L/5) <= n < L/2,                              (5.3)
```

plus the exact-graph case `n=infinity`.  The width of (5.3) grows with the
load grade, so it is pruning, not a uniform finite list.  Moreover the seven
quadrics do not generate the full `J`-initial ideal, and the loaded source
does not set `I=0`.  Neither graph membership nor coefficientwise recurrence
follows from the sandwich.

## 6. Exact same-state/different-successor controls

These are literal source comparisons, not analogy.

| common reduced state | first cell successor | second cell successor | consequence |
|---|---|---|---|
| fresh `n=3` cone `Q` at G6 | `e=2,m=1`: K10 participates at G7 and every rank dies | `e=3,m=1`: only rank two dies at G7; rank one reaches G8 and rank zero recenters | the cone/rank state does not determine G7 |
| fresh `n=4` cone `Q` at G8 | `e=3,m=1`: loaded G9 fan kills all ranks | `e=2,m=2`: G9 is an honest tangent image and closure waits until loaded G10 | identical cone grade, different immediate successor |
| fresh `n=4` cone `Q` at G8, with the same `m=2` in both cells | `e=2,m=2`: actual K10 collision at G10 kills the final fan | `e=3,m=2`: K10 G10/G11 cancels; rank zero recenters to `n=5`, and a rank-one branch can survive G11 before G12 | changing only `e` changes the G10 map |

The four terminal grades happen to equal the first main-row surface K10
grade:

```text
(2,1)->G7,  (3,1)->G9,  (2,2)->G10,  (3,2)->G12,
G_terminal=2e+3m.                                  (6.1)
```

Equation (6.1) is verified only on these four cells.  Their transition trees
are different, so it is not evidence for a coefficient-blind proof of the
same formula at all `(e,m)`.

## 7. Exact coverage and lifecycle

All four cells are over an algebraic closure of a characteristic-zero
residue field after the licensed finite extensions, on `C6,k10,Jdet` unit
opens.  In every row below, each of the five late boundary series may have
arbitrary positive order or be identically zero; it lies beyond the terminal
prefix and is not used.

| cell | strongest current artifact | exact point-set conclusion | lifecycle consumed here |
|---|---|---|---|
| `e=2,m=1` | all-face coordinator integration `7c73616d...` | empty through G7; hence no formal source arc in this cell | **PROMOTED** |
| `e=3,m=1` | complete-fan coordinator integration `6c719521...` | empty through G9; hence no formal source arc in this cell | **PROMOTED** |
| `e=2,m=2` | producer/replay `fa5a4ef6...` / `efd2f4fe...`; Fable review `4710349b...` | empty through G10; odd G8 component is strictly non-pullback | **DIFFERENT-MODEL CONFIRMED / BINDING INTEGRATION NOT YET FILED** |
| `e=3,m=2` | producer `3a4565b8...`, replay `7cbc45a1...` | producer-empty through G12 | **PROVISIONAL / DIFFERENT-MODEL REVIEW ACTIVE AT SEAL** |

All four exact cell replays were separately executed successfully in ordinary
Python.  The meta replay pins them and independently reconstructs (1.1),
(1.2), and the complete bidegree table from the 569 tails.  No provisional
cell is promoted by agreement with this same-model synthesis.

Not covered:

1. any other `(e,m)`, including `e=4,m=1` and `e=2,m=3`;
2. `C6=0`, `k10=0`, `Jdet=0` or positive-order K10/Jdet boundary cells;
3. another K00 support, load ray, square normal, receiver, or Gate T;
4. positive characteristic, nonreduced scheme-valued points, multiplicities,
   or a localized Bezout identity unless separately supplied;
5. closure-source completeness, reachability, converse lifting,
   algebraization, attainment, a polynomial Keller map, a counterexample, or
   JC2.

Point-set emptiness of a finite prefix excludes a formal arc only inside the
same exact cell.  It supplies no map-to-cell or source-exhaustion theorem.

## 8. Cheapest next cells and theorem target

The cheapest source-partition residue is the newly reviewed producer's own
boundary child

```text
e=2, m=2, h10=1,       first surface K10 grade G11. (8.1)
```

The review proves that the G10 terminals are proportional to `k10[0]`, so
they disappear on this child, while the earlier K10-independent steps remain
available.  Its proposed G11 extraction has the same surface cubics
multiplied by `k10[1]` together with a fresh quadratic block; that G11 fan is
not yet solved and must be re-extracted literally.  This is a one-grade
marginal extension of reviewed work.  It lies outside the charged
`k10`-unit incidence, so it advances source partitioning rather than the
generic-ray `(e,m)` atlas.  The `h10=infinity` face is separate and is not
decided by the `h10=1` calculation.

The cheapest untouched **unit-ray** cell by terminal calendar is

```text
e=4, m=1,       first surface K10 grade G11.        (8.2)
```

Through G11, K6, K2, and all targets are absent: their raw lower grades are
G26, G42, G57, G65, G73, and G76.  This makes `(4,1)` cheaper than the next
new transverse order `(2,3)`, whose surface K10 grade is G13.  It is also the
sharpest next control: if the anticipated fresh `n=5` G10 cone is actually
reached, `(4,1)` places K10 at G11 whereas the provisional `(3,2)` packet
places the first actual K10 at G12.  The producer must re-extract that state;
it may not import it by recurrence.

Mandatory `(4,1)` controls are:

1. retain every surface and normal coefficient capable of reaching G11,
   including all nonzero deck characters;
2. use the G10 cone only after literal equality with the frozen source;
3. compare the G11 map against the `(3,2)` G10/G11 cancellation as a
   same-state/different-shift mutation; and
4. stop at the first complete reduced rank fan.  Any uncertain elimination
   is AWS-only.

If `(4,1)` confirms a corrected pattern, the next general theorem target is
not bare `m=1` induction.  It is a state-complete parametric transition lemma
whose input explicitly includes `(e,m,n)`, the required surface-jet window,
deck characters, and the load-order vector, and whose output is the next
literal coefficient map.  Only such a theorem could turn the finite calendar
skeleton into finitely many transition types.

After the boundary G11 child and `(4,1)`, the ranked discriminators are
`(2,3)` at G13, the mixed raw
wall `(2,4)` where `m=2e`, and the first coupled surface-load cell
`(2,9)` with `(h6,h2,hmu2)=(1,2,3)` at G31.

## 9. Exact replay

Run

```text
python3 -B xmodel/k00-ramified-em-calendar-meta-replay-sol56-20260830.py
python3 -B -O xmodel/k00-ramified-em-calendar-meta-replay-sol56-20260830.py
```

Both modes print identically:

```text
K00_RAMIFIED_EM_CALENDAR_META_REPLAY=PASS
TAIL_TERMS=569
RAW_MINIMA=R:2222232;K10:2222222;K6:1112121;K2:1111111
GRAPH_BIDEGREES=EXACT_PARETO_ANTICHAINS
SURFACE_MINIMA=K10:333_INF_343;K6:222_INF_232;K2:111_INF_121
CHARGED_TERMINALS=E2M1:G7;E3M1:G9;E2M2:G10;E3M2:G12
SAME_STATE_DIFFERENT_SUCCESSOR=N4_G8_E3M1_vs_E2M2;N4_G8_E2M2_vs_E3M2
RATIO_CONTROL=(2,9,h6=1):TIE31;(4,18,h6=1):K6_61_BEFORE_K10_62
FINITE_TYPE_VERDICT=CALENDAR_ONLY;NO_TRANSITION_QUOTIENT_THEOREM
CERTIFICATE_BYTES=3812
CERTIFICATE_SHA256=afb3979a091647fb1c2567c06295400358bf84d65387cc6447faabb92231f501
MUTATIONS=CUSTODY,SURFACE_16_TO_15,RATIO_SCALE,CHARGED_SUCCESSOR_TEXT
```

The replay is pure Python stdlib exact rational arithmetic, writes no files,
and completes in well under one second.  It adds an exact certificate for the
general raw and graph-normal calendars; it deliberately does not duplicate a
cell solve.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20154`.
- Body SHA-256:
  `5b57d03dbb11de8b2e837339e2e89091b994d02ddd9a665800a6e5c922b9e731`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
