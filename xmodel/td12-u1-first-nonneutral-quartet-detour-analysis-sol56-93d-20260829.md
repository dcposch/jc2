# TD12 U1 first-nonneutral quartet and detour analysis

Date: 2026-08-29 UTC  
Author: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `READ_ONLY_RESEARCH / CONDITIONAL_QUARTET_PROVED / OCCURRENCE_OPEN`

## 0. Executive disposition

The missing arrow is not an abstract completion constructor.  An exact
counterexample together with an actual boundary vertex already determines its
Newton--Puiseux completion, actual child shears, decorated tree, and finite
coefficient maps.  The missing arrows are occurrence and coverage:

```text
globally GGV-minimal exact counterexample
  -X-> td=12
  -X-> actual m=3 off-axis U1 equality record
  -X-> named actual B25 or S17 occurrence.
```

The strongest result available after assuming an actual td12 U1 record is a
four-way first-nonneutral alternative.  After any provenance-preserving
clean-neutral `M=2` prefix, the first budget-surviving nonneutral trunk child
is one of

```text
A7, C5, B25, S17.
```

The desired B/S landing therefore reduces to excluding the A7 and C5
detours.  This report gives an explicit obstruction to doing that with the
current reduced laws: both detours admit short P0/P1 budget-fitting tails,
and every dirty cell on those tails has a nondegenerate vertex-local
Proposition 8.1(iv) solution.  These are formal necessary-data paths, not
actual polynomial-pair realizations.  They identify cross-vertex source
transport, full-index synchronization, and Puiseux-prefix gluing as the
smallest remaining consumers.

Binding disposition:

```text
PROMOTE NO GLOBAL OCCURRENCE CLAIM
RETAIN CONDITIONAL FIRST-NONNEUTRAL QUARTET
RETAIN A7/C5 TAILS AS ADVERSARIAL FORMAL FIXTURES
DO NOT CALL LOCAL T1 SOLVABILITY GLUING OR REALIZABILITY
NEXT: TD12-U1-DETOUR-EXCLUSION AT ACTUAL SOURCE-TYPED SCOPE
```

## 1. Exact theorem ledger and the two independent selector gaps

The following arrows are already supported.

1. If JC2 is false, GGV permits selection of some globally minimal standard
   counterexample.  The minimized invariant is

   ```text
   B_GGV = gcd(deg P,deg Q),
   ```

   over all counterexamples.  It is not topological degree.
2. The selected exact pair may be Sigray-normalized without changing its
   field-extension degree `td`.  This normalizes the same pair; it does not
   select a route in its Laurent tree.
3. For an exact pair, fibre, and actual vertex, the intrinsic two-chart tree,
   DVR completions, finite Laurent pieces, and parent-to-child shears exist.
   Statement 3.18 creates an actual child from a residual root only after the
   actual parent and its source prefix are present.
4. The repaired pole-mass theorem gives a finite pole-entry menu for every
   fixed `td`.  It gives neither an upper bound on `td` nor a single selected
   value of `td`.
5. Inside the explicitly assumed `td=12`, `m=3`, off-axis `[2,2,2]` sector,
   the unique L6-surviving entry is

   ```text
   type (2,3), Lambda=(4,4,4),
   poles (a,b,nu)=(1,2,3)^3,
   incoming (mu,w)=(2,3/2)^3.
   ```

   Its star U1 equality merge has the constant reduced trunk state
   `(w,M)=(9/2,2)`.
6. Conditional on a named actual B occurrence with

   ```text
   (nu,kbar,X,M,w)=(25,17,25,3,2/3),
   ```

   the promoted B source bridge constructs the native completion/operator
   and its inhomogeneous landing row.  It does not create the occurrence.
7. Conditional on a named actual S occurrence with

   ```text
   (nu,kbar,X,M,w)=(17,13,17,4,3/4),
   ```

   the promoted S source bridge supplies the repaired map, floor, gauge, and
   degree-floor statements.  It likewise does not create the occurrence or
   positive-order source values.

There are consequently two logically independent global gaps:

```text
G1: GGV-minimal exact pair -> td=12 and the m=3 off-axis sector;
G2: actual td12 U1 record -> named actual B25 or S17 occurrence.
```

Solving G2 does not solve G1.

## 2. Conditional first-nonneutral quartet theorem

### Theorem `TD12-U1-FIRST-NONNEUTRAL-QUARTET`

Let `(f,g)` be an exact normalized Keller counterexample of `td=12`.  Assume
a named actual occurrence of the source-pinned `m=3` U1 equality merge above,
and retain its fibre, physical component, place, edge, merge parameter, full
index, finite Puiseux prefix, and rootward trunk.  Let `F` be the first trunk
child after the merge that is not a clean-neutral `M=2` step.  Do not erase
the neutral prefix; merely record that each such step preserves the reduced
state `(9/2,2)` and has zero recorded lower price.

Then either the continuation already violates MP2, P1, or the shared budget,
or the reduced data of `F` are exactly one of the following four rows:

| name | `(nu,dp,dq,E,kbar,X)` | child `(w,M)` | lower price | status |
|---|---|---|---:|---|
| A7 | `(7,21,15,9,15,21)` | `(2,3)` | 6 | nonterminal detour |
| C5 | `(5,20,16,12,12,15)` | `(9/4,4)` | 6 | nonterminal detour |
| B25 | `(25,75,51,27,17,25)` | `(2/3,3)` | 8 | P1-fitting terminal |
| S17 | `(17,68,52,36,13,17)` | `(3/4,4)` | 8 | P1-fitting terminal |

If `F` is B25 or S17, its retained actual provenance names the actual
occurrence required by the corresponding conditional source bridge.

### Proof

The independently reviewed one-step menu from `(9/2,2)` is exhaustive at the
maximal first-step `td=12` budget `10`, not merely at the advertised B budget
`9`.  It contains 13 edges:

```text
0 clean-resonant,
2 clean-neutral,
1 pure-epsilon,
10 dirty.
```

An actual polynomial tree is finite, and `w=9/2>1` is not terminal.  Thus an
actual rootward continuation has a first nonneutral edge after a finite
neutral prefix.  The menu depends on the reduced state and remaining lower
budget, so it applies at that edge while the actual prefix stays serialized.

The clean-neutral `M=1` row, pure-epsilon row, and all epsilon-present dirty
rows have `M=1` and are MP2-dead as interior trunk rows.  The six
epsilon-zero dirty survivors are

```text
(k,nu)=(1,7),(1,25),(2,5),(2,17),(4,13),(8,11).
```

The last two are P1-shaped but fail their own terminal budgets:

```text
nu=13: (w,M)=(5/6,6), lambda=8, psi=5, budget=6;
nu=11: (w,M)=(9/10,10), lambda=8, psi=9, budget=2.
```

The remaining four rows are A7, C5, B25, and S17.  This proves the
alternative.  Notice that the proof never identifies two object-level states
merely because their reduced `(w,M)` values agree.

## 3. Exact A7 and C5 adversarial tails

Substitution into the promoted epsilon-zero P0 formulas gives the following
five exact rows.  For an extra multiplicity `m`, put
`delta=X/m-kbar`.

| row | parent `(w,M)` | `(l,k,mults,nu)` | `(dp,dq,E,kbar,X)` | child `(w,M)` | deltas | price |
|---|---|---|---|---|---|---:|
| A7 | `(9/2,2)` | `(2,1,(1),7)` | `(21,15,9,15,21)` | `(2,3)` | `(6)` | 6 |
| C5 | `(9/2,2)` | `(2,2,(1,1),5)` | `(20,16,12,12,15)` | `(9/4,4)` | `(3,3)` | 6 |
| A-middle | `(2,3)` | `(3,2,(2,2),9)` | `(63,28,21,8,18)` | `(6/7,7)` | `(1,1)` | 2 |
| C-middle | `(9/4,4)` | `(4,1,(3),17)` | `(119,35,21,15,51)` | `(6/7,7)` | `(2)` | 2 |
| H | `(6/7,7)` | `(7,1,(6),19)` | `(247,39,26,9,57)` | `(6/13,13)` | `(1/2)` | 1 |

Thus the two formal paths are

```text
(9/2,2) -> A7 (2,3) -> A-middle (6/7,7) -> H (6/13,13),
(9/2,2) -> C5 (9/4,4) -> C-middle (6/7,7) -> H (6/13,13).
```

They contain neither B25 nor S17.

### 3.1 Exact legality checks

For epsilon zero, `T=l+Sm`.  The P0 divisor checks are

```text
A7:       9 | 2*9*3   = 54,
C5:      12 | 2*9*4   = 72,
A-middle:21 | 3*2*7   = 42,
C-middle:21 | 4*9*7   = 252,
H:       26 | 7*6*13  = 546.
```

The exact P0 resolvent identity

```text
E * (l*a*(1+k+lex) - kbar*d*C_P0) = l*a*T,
C_P0=l*k-Sm,  w=a/d,
```

gives respectively `54,72,42,252,546` on the two sides.  Integrality and N1
hold:

```text
gcd(kbar,nu)=gcd(15,7)=gcd(12,5)=gcd(8,9)
             =gcd(15,17)=gcd(9,19)=1.
```

R1.0 also gives `gcd(M_child,nu)=1` on all five rows.  Strict northeast
inequalities are

```text
15<21, 16<20, 2*28<63, 3*35<119, 6*39<247.
```

Hence these are legal records for the current P0/N1/R1.0/MP2 necessary-data
system.

### 3.2 Terminal and price check

At H,

```text
j=M(1-w)=13*(1-6/13)=7,
psi=ceil(13/7)-1=1,
td-1-psi=10.
```

Each downstream path has lower-floor sum

```text
6+2+1=9 <= 10,
```

with slack one.  The last row has nonintegral `delta=1/2`.  Even after
supplying the strongest natural full-actual carrier tag, its numerical floor
would remain

```text
L_safe(1/2)=ceil(2*(1/2))=1.
```

The current finite-pole integration explicitly says that the td12 U1 family
is not yet a typed `s>=3` consumer.  Therefore this is a numerical robustness
check, not an invocation of an unavailable carrier.  The three U1 pole-entry
prices are likewise not source-pinned.  The inequality above is a post-U1
lower-floor calculation, not an attainment claim for the whole actual
configuration.  A new positive entry price could kill U1; it would not force
B/S occurrence.

## 4. Vertex-local Proposition 8.1(iv) solutions

The detours also survive the reduced terminal-pattern equation at every
dirty row.  For epsilon zero, write

```text
p=P(t),  q=eta*Q(t),  t=eta^nu,  theta=dp/dq.
```

The reduced Proposition 8.1(iv) expression is

```text
L/P = theta*Q + nu*t*(theta*Q' - (P'/P)*Q).
```

The cell is locally admissible when this expression is a nonzero constant
and the root-law guards hold.

### 4.1 Two-root calculation

For

```text
P=(t-A)^l*(t-B)^m,  Q=(t-A)*(t-B),
theta=nu*(l+m)/(2*nu+1),
```

the top coefficient cancels by the degree identity.  Constancy is equivalent
to

```text
nu*(l*B+m*A)=theta*(nu+1)*(A+B),
```

and the resulting constant is `theta*A*B`.  It gives:

| cell | `(l,m,nu,theta)` | forced ratio | constant |
|---|---|---|---|
| A7 `(21,15)` | `(2,1,7,7/5)` | `B/A=3/2` | `21 A^2/10` |
| C-middle `(119,35)` | `(4,3,17,17/5)` | `B/A=3/2` | `51 A^2/10` |
| H `(247,39)` | `(7,6,19,19/3)` | `B/A=2` | `38 A^2/3` |

For nonzero `A`, all constants are nonzero and the two roots are distinct.
The `(119,35)` row agrees with the independently reviewed six-cell solution.

### 4.2 Three-root calculations

For C5,

```text
P=(t-A)^2*(t-B)*(t-D), Q=(t-A)*(t-B)*(t-D),
nu=5, theta=5/4.
```

Vanishing of the `t^2` and `t` coefficients is exactly

```text
B+D=3A,  B*D=3A^2,
```

and the constant is `-15 A^3/4`.

For A-middle,

```text
P=(t-A)^3*(t-B)^2*(t-D)^2, Q=(t-A)*(t-B)*(t-D),
nu=9, theta=9/4.
```

The same two relations result, and the constant is `-27 A^3/4`.
The quadratic for `B,D` is

```text
z^2-3A*z+3A^2,
```

whose discriminant is `-3A^2`.  Thus for nonzero `A`, `B,D` are distinct,
nonzero, and different from `A`.  Every displayed local root-law guard
passes.

### 4.3 Exact scope

The symbols `A,B,D` at different vertices are independent local scales.
These computations do not transport one scale to the next, match a source
coefficient, instantiate Statement 3.9, or produce an actual child.  They do
prove that any proposed detour exclusion using only reduced Proposition
8.1(iv) is false.

## 5. Global `td` selector no-go

There is no current route from GGV minimality to `td=12`.

The logical form of the current reduction is

```text
counterexample -> select some GGV-minimal pair P,
td(P)>=6,
for every fixed d, the necessary entry set E_d is finite.
```

The statement `forall d, |E_d|<infinity` neither bounds `d` nor selects one
value.  Normalization preserves the unknown `td`; it cannot change this
quantifier structure.

The promoted td-uniform sheet supplies a concrete obstruction to any proof
using only the present local kill set.  At `td=9` it has the hand-verified
formal entry

```text
type (3,4), a=1, b=3, nu=4, Lambda=9,
Q=(3,9,4,3,7), w=1/3, M=3,
```

followed by a zero-price IIa0 step to a case-IV terminal with

```text
psi=2,  sum lambda=0 <= 9-1-2=6.
```

This is not an actual polynomial pair.  It is sufficient to show that the
promoted local necessary-data axioms alone cannot imply `td=12`; any such
selector must use a new source-level premise that excludes all other
degrees.

Nor does the unique `td=12,m=3` U1 row repair the gap.  It is unique only
after assuming `td=12`, `m=3`, the off-axis sector, and `[2,2,2]`.  No theorem
forces those hypotheses for the globally selected pair.

## 6. False hopes and precise missing premises

The following shortcuts are invalid.

1. **Minimal means minimal `td`.**  False invariant: GGV minimizes a gcd of
   polynomial degrees.
2. **Finite entry menu at each `td` gives a `td` ceiling.**  False quantifier
   exchange.
3. **The U1 row is unique, hence selected.**  It is unique only inside its
   already-assumed sector.
4. **Statement 9.6 supplies B25/S17.**  Its raw ratio rows
   `(k,n,nu)=(1,12,25),(2,8,17)` violate `n=1 mod 3`.  The audited legal rows
   are `(1,10,7),(2,7,5)`, producing `(21,15)` and `(20,16)`.  The printed
   `(1,13,25)` fails the ratio itself.  The fractional child frames are not
   B25/S17 occurrences.
5. **Neutral reduced states may be object-level quotiented.**  The full
   index, coefficient prefix, edge, and place can change and must remain in
   the packet.
6. **Full-actual pricing kills the detours.**  Numerically false on the
   displayed rows, and the U1 consumer tag is currently absent.
7. **Reduced T1 kills A7/C5.**  Explicitly false by Section 4.
8. **Local T1 solutions glue.**  False without Statement 3.9/source-prefix
   transport.

## 7. Minimal prove-or-refute lemma

### `TD12-U1-DETOUR-EXCLUSION`

Fix an exact normalized `td=12` Keller pair and a named actual U1 equality
record with its entire typed source prefix.  Let an actual rootward
continuation begin, after a finite serialized clean-neutral `M=2` prefix,
with A7 or C5.  Then every such continuation either

```text
(a) contains a named actual B25 or S17 occurrence, or
(b) meets a reviewed source, adjacency, MP2, T1, or shared-budget
    contradiction before a P1 terminal.
```

Together with the quartet theorem, this lemma proves the conditional
`TD12-U1-ACTUAL-LANDING` statement.  A source-compatible actual realization
of either explicit Section 3 tail would refute the lemma, but not JC2.  A
formal tail alone does not refute it.

The lemma is the smallest honest downstream target.  A global theorem still
also needs the independent `GGV-minimal -> td12` and `td12 -> actual U1`
selectors.

## 8. Exact next packet

Launch `TD12-U1-DETOUR-EXCLUSION/v1` with these mandatory fields and stops.

### Inputs

- one exact normalized pair and fibre;
- named actual U1 merge, physical component, place, and outgoing trunk edge;
- merge arithmetic-progression parameter and full indices of `f` and `g`;
- every clean-neutral prefix row, without quotient deletion;
- finite Puiseux/source coefficient prefix through the first nonneutral row;
- the A7 and C5 branch tags;
- the two Section 3 tails as adversarial fixtures;
- the Section 4 local T1 witnesses.

### Required proof steps

1. Reproduce the first-nonneutral quartet at the full typed state and show
   that no actual edge was lost when passing to the reduced menu.
2. Instantiate corrected Statements 3.7/3.9 and 3.18 on A7/C5, the middle
   rows `(63,28)` and `(119,35)`, and the common row `(247,39)`.
3. Transport the full sheet count/index from the U1 merge parameter through
   every shear.  This is an actual source consumer, not a reduced-pattern
   identity.
4. Substitute the explicit local T1 solutions and test cross-row coefficient
   compatibility, deck action, root choice, and Puiseux-prefix gluing.
5. Serialize actual first-separation directions.  Apply the finite-pole
   carrier only after proving the `s=3`, one-fibre, one-component tag; retain
   its lower-floor-only semantics.
6. Account for all three U1 pole-entry prices from the actual source rather
   than silently setting unknown contributions to zero.
7. Exhaust every in-budget actual A7/C5 continuation, retaining neutral
   prefixes and full-index exceptional classes.

### Verdicts

```text
PROVED_DETOUR_EXCLUSION:
  both A7 and C5 actual continuations contradict before a B/S-free terminal;

REFUTED_BY_ACTUAL_TAIL:
  an exact source-compatible A7 or C5 continuation reaches a B/S-free P1
  terminal;

SOURCE_TRANSPORT_OPEN:
  only reduced/local compatibility is obtained; occurrence remains open.
```

Do not emit a B/S occurrence, `PairRef` value packet, route kill, degree
ceiling, or JC2 conclusion under the third verdict.

## 9. Research custody and firewall

This report is a desk-scale, read-only synthesis of the current overlays,
the td12 source-interface audit, the reviewed U1 menu and hostile review,
the B/S bridge integrations, the finite-pole carrier integration, the
td-uniform survivor sheet, and the cited Sigray source/audits.  It introduces
no canonical theorem status.  No source, case engine, canonical Markdown,
Lean object, or external resource was modified or invoked in deriving the
mathematics.

No actual counterexample, occurrence, gluing, cap, terminal attainment,
degree bound, or JC2 conclusion follows.

<!-- END-SEALED-BODY::td12-u1-first-nonneutral-quartet-detour-analysis-sol56-93d-20260829 -->

## Seal

- Body definition: every byte from the first byte through the unique body-end
  marker line, including its terminating newline.
- Body byte count: `17030`.
- Body SHA-256:
  `7204148ee85590dfc3d02d57340f6372e16997d11481c55652bfc630e3d652d4`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
