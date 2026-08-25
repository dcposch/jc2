# Blind whole-portfolio delta — cube/max-12 owner — `20260825T1550Z`

Date: 2026-08-25  
Cutoff: coordinator's exact two-seed trigger and repository state visible at launch  
Status: **BLIND COMPLETE / ALL 46 AVENUES / NO SIBLING 1550Z SUBMISSION READ**

I reread `COORDINATION.md`, all 46 numbered rows and the current overlays in
`APPROACHES.md`, the relevant current ledgers, and the reviewed maximum-eleven,
maximum-twelve routing, and AS integral-transfer inputs.  No separate 1550Z
packet/state file was present.  I did not search inside or read any sibling
1550Z submission.  All substantive Q8 computation remained on AWS; this report
used only source reading, hand algebra, editing, and hashes locally.

The significant news is real but sharply scoped: there are now two explicit,
unit-leading, total-degree-twelve residue maps on the two primitive partial-`y`
frontiers.  They are not lifts and do not enter the presently selected Q8
chart.  They do, however, turn maximum twelve into the cheapest complete
fixed-support counterexample gate yet available.

## 1. Exact audit of the two residue seeds

Work over `F_3` and put

```text
A(s,t)=(s-s^3,t).
```

### The `(9,12)` seed

Set

```text
U=x+y^3,                 V=y+U^4,
B_9(x,y)=(U,V),          G_9=A o B_9=(U-U^3,V).
```

The triangular map is an automorphism over `Z`, not merely over `F_3`:

```text
B_9^(-1)(U,V)=(U-(V-U^4)^3, V-U^4),       det J(B_9)=1.
```

In characteristic three,

```text
det J(G_9)=1,
deg_y(G_9)=(9,12),
[y^9]G_9,1=-1,            [y^12]G_9,2=1.
```

Thus the leading UFD core is the unit `h=-1`, with `h^3=-1,h^4=1`.
The map is etale and noninjective.  For example, the three source points

```text
(0,0), (2,2), (0,2)
```

map to `(0,0)`; the first two are unit-separated in the first coordinate.

### The `(8,12)` seed

Set

```text
U=x+y^4,                 V=y+U^2,
B_8(x,y)=(U,V),          G_8=(V,U^3-U).
```

Again

```text
B_8^(-1)(U,V)=(U-(V-U^2)^4, V-U^2),       det J(B_8)=1.
```

The ordered target change

```text
T_8(s,t)=(t,-s),          G_8=T_8 o A o B_8
```

has determinant one, so

```text
det J(G_8)=1,
deg_y(G_8)=(8,12),
[y^8]G_8,1=[y^12]G_8,2=1.
```

Here the leading UFD core is `h=1`, with `h^2=h^3=1`.  The points

```text
(0,0), (0,2), (1,2)
```

all map to `(0,0)`; the first and third are unit-separated.

These calculations use no classification theorem.  They also show why the
objects are better than a random finite-field census: both have polynomial
integral source inverses, exact determinant one in the residue field, a
registered collision, and unit leading coefficients on the first unclosed
partial-`y` degree.

## 2. Where the seeds do and do not land

### They are integral right-conjugates of the AS seed

Let `T_9=id` and let `T_8` be the integral determinant-one target change
above.  If an exact map

```text
F in Z_3[x,y]^2,        det J(F)=1,        F mod 3=T o A o B
```

exists, then

```text
H=T^(-1) o F o B^(-1)
```

is an exact integral determinant-one map reducing to `A`.  Any fixed finite
support for `F` becomes another fixed finite support after this composition.
Therefore the reviewed AS residue-ball/finite-type transfer theorem applies:
an all-depth compatible lift in one fixed support would give a complex Keller
map with a genuine collision.  Equivalently, the collision can be followed
directly in the three residue balls above the displayed source points.

This is an exact transfer of the *counterexample consequence*, not of the
current D7 support or chronological state.  Composing a D7 correction with
`B` can raise total degree far beyond twelve, while pulling a D12 correction
back by `B^(-1)` produces a sparse but high-degree AS support.  No existing
D7 survivor is thereby a D12 survivor.

### They lie on the monomial-core boundary, not selected Q8

For `(9,12)` the special-fibre common cubic is

```text
K_9=y^3+x,
G_9,1=K_9-K_9^3,        G_9,2=y+K_9^4.
```

After harmless target scaling, this is the `K^3,K^4` order-one core.  In the
approximate-cubic coordinate `K=z^3+pz+q`, it has exactly `p=0`.  The active
selected-Q8 source lives on a nontrivial order-three Kummer chart and its
generic localization contains `p`; its formulas also use the characteristic-
zero `1/3,1/9` depression/Kummer normalization.  Dividing a lift's
`p in 3 Z_3` to normalize it to one is not an integral coordinate change, and
`mu_3` is not etale over residue characteristic three.  The selected Q8
contact theorem therefore cannot consume this seed.

For `(8,12)` the special core is

```text
K_8=y^4+x,
G_8,1=y+K_8^2,          G_8,2=K_8^3-K_8,
```

the order-one quartic core.  It is in the separate `(8,12)` cell, not Q8,
and no complete lower-fibre compiler exists there yet.

The word “order-one” here applies to the residue core only.  A characteristic-
zero lift with leading core congruent to `+/-1 mod 3` can acquire nonconstant
divisors and a nontrivial Kummer class over `Q_3(x)`.  Thus the new objects
expose a missing **integral monomial-core/Kummer boundary**: the generic
character split need not extend flatly across the AS special fibre.  They do
not prove that every lift remains in the polynomial-core leaf.

The same firewall prevents importing TD6.  Its normalized source uses
relations such as `3H^3=1` and `L^8 A^3=9` in a pole field, not an integral
global polynomial-map chart carrying either displayed residue collision.

## 3. Cheapest complete degree-twelve p-adic gate

For each seed choose its canonical integer lift

```text
G_0=T o A_0 o B,          A_0(s,t)=(s-s^3,t),
det J(G_0)=1-3U^2.
```

Use the **full** total-degree-at-most-twelve coefficient envelope

```text
F=G_0+3(P,Q),             deg(P),deg(Q)<=12.
```

There are `91` monomials per coordinate, hence `182` first-digit variables.
The complete determinant has total degree at most `22`, hence exactly `276`
registered coefficient rows before removing literal zeros.  Modulo nine the
gate is one affine linear system over `F_3`; it is small enough to run twice
with exact RREF and an independently generated source matrix.

The AS conjugacy gives a useful source-honest control.  Put

```text
H=T^(-1) o F o B^(-1)=A_0+3(R_1,R_2).
```

Then the complete first divided determinant equation is

```text
R_(1,s)+R_(2,t)=s^2 mod 3.                           (3.1)
```

Here `(R_1,R_2)` is not a free low-degree rectangle: it is exactly the
182-dimensional transformed D12 support.  Direct original-coordinate rows
and (3.1) must agree.  This reuses the AS Cartier compiler without pretending
that the D7 and D12 supports coincide.

If the mod-nine system is empty, that complete D12 seed tube is closed.  If
it survives, compute the full mod-27 quadratic/Kuranishi map on its affine
kernel, including the literal integer carry and every determinant row.  A
second non-informative depth triggers a coefficient-scheme Jacobian/Fitting
and singular-Hensel split rather than point sampling.  Only an arbitrarily
deep compatible tower of this same fixed scheme invokes compactness and the
collision transfer.

This is complete only for total degree at most twelve.  An empty gate does
not exclude the whole partial-`y` `(8,12)` or `(9,12)` cell, whose `x`-degree
is unbounded.  A finite-depth survivor is not a counterexample.

## 4. Full 46-avenue disposition

Baseline is the 1440Z synthesis.  `U` means no allocation change; changes
below are scheduling or experiment changes, never silent theorem promotion.

| # | disposition | cutoff-honest reason |
|---:|---|---|
| 1 | U | Two finite-field seeds supply no GGV transport or cofinal degree ceiling. |
| 2 | **raise/redesign** | Both primitive max-12 cells now have exact unit-leading residue controls, but selected Q8 covers neither monomial-core landing. |
| 3 | U | Strip ODEs remain post-landing tools, not integral Kummer-boundary theorems. |
| 4 | **raise** | The D12 coefficient schemes and the Q8 `p=0` boundary are exact formal/Kuranishi clients. |
| 5 | **raise narrowly** | The triangular `B_8,B_9` show partial-`y` frontier is source-coordinate-sensitive; right-equivalence must be tracked integrally. |
| 6 | U-low | One-place recognition still needs a constructed asymptotic component. |
| 7 | U-high | No general asymptotic-set construction or properness theorem follows. |
| 8 | U-low | No uniform formal-inverse truncation bound appears. |
| 9 | U | Conjecture-E remains an unbounded implication ladder. |
| 10 | U-low | The executed HC4 probe remains `NO LEVERAGE`. |
| 11 | U-stopped | Refuted stronger Mathieu/Zhao statements remain unusable. |
| 12 | U-low | The seeds do not provide an independent face-isolation limit. |
| 13 | U-low | DC(2) remains harder than the direct D12 coefficient gate. |
| 14 | U-low | No Weyl endomorphism candidate is supplied. |
| 15 | U-low | No two-variable spectral-surface dictionary is supplied. |
| 16 | U-narrow | Explicit finite obstruction modules remain clients, not a general D-module route. |
| 17 | U-stopped | Stabilization still leaves the plane and enters known higher-dimensional counterexample territory. |
| 18 | U-stopped | Graded plane Keller maps are already automorphisms. |
| 19 | **raise strongly** | The two exact D12 AS-conjugate seeds are the first unit-leading counterexample gates exactly at the max-eleven escape frontier. |
| 20 | U-low | Reduction mod `p` is the input, but no p-curvature theorem is invoked. |
| 21 | **raise strongly** | A fixed finite-type D12 scheme plus integral right-conjugacy is an exact Greenberg/compactness client. |
| 22 | U-low | Heights still control the wrong varying family. |
| 23 | U-stopped | Holomorphic and dimension-free metric analogues remain false. |
| 24 | U-low | No Pinchuk-to-constant-J deformation appears. |
| 25 | U-high | Q8 passport/primitivity stays useful after landing; it does not classify the new order-one special fibre. |
| 26 | U-high | Galois grouping remains local to selected Q8 and gives no global sheet bound. |
| 27 | U | Splice data remain post-construction checks. |
| 28 | U-high | Q8 coefficient compactification remains live; D12 adds an integral special boundary, not a log-surface theorem. |
| 29 | **raise as mechanism** | First Cartier cokernels, quadratic Kuranishi maps, and Fitting strata are now shared by AS-D12, Q8, and TD6. |
| 30 | U-low | ML invariants still miss the embedded map. |
| 31 | **raise** | Integral source conjugacy succeeds exactly, while Q8 normalization fails integrally at `p=0`; this is a named integrality interface. |
| 32 | **raise** | Each seed has an explicit unit-separated residue collision, and every complete lift inherits moving collisions. |
| 33 | U-stopped | Untwisted action residues remain exact-form costume. |
| 34 | U | Rational pole removal does not repair the nonintegral Q8 normalization. |
| 35 | U-low | No descent from a higher-dimensional counterexample occurs. |
| 36 | **raise strongly** | The complete 182-variable D12 gates are structured counterexample searches, not random sparse scans. |
| 37 | **raise narrowly** | The two seeds are exact positive controls; a broad finite-field census is still low value. |
| 38 | **raise** | The `p=0` monomial-core normal cone is the exact tropical/Rees boundary between integral AS and generic Kummer charts. |
| 39 | U | No new global cohomological class is named. |
| 40 | U-low | Commutative determinant one still does not imply a free lift. |
| 41 | U-stopped | Naive scaling remains falsified. |
| 42 | U-low | Constant Jacobian still does not imply Hurwitz spectrum. |
| 43 | U-low | The explicit compositions are controls, not a Ritt-prime reduction theorem. |
| 44 | U-stopped | The prime-td proof remains refuted as proof input. |
| 45 | U-low | Differential inverse equations add nothing before a lift exists. |
| 46 | **raise as infrastructure** | Integral transform provenance and complete divided-determinant compilers become shared acceptance gates. |

Material changes are rows `2,4,5,19,21,29,31,32,36,37,38,46`.

## 5. Reranked bottlenecks and portfolio impact

### Counterexample side

1. **Paired D12 mod-nine Cartier gates.**  This is now the cheapest complete
   high-information experiment in the portfolio: exact linear algebra on two
   182-variable schemes, with a direct conjugacy control.
2. **First nonlinear transition.**  On any surviving affine kernel, compute
   the full mod-27 Kuranishi/Fitting map, not selected points.  Compare its
   obstruction support with the live D7 AS operator.
3. **Compatible tower or finite closure.**  Only source-complete schemes and
   exact truncation maps count.  The reviewed integral inverse/residue-ball
   theorems make either outcome decisive at fixed support.

### Proof side

1. **Finish the live selected-Q8 finite/moving/infinity saturation.**  The new
   seeds do not reverse that priority or consume its theorem.
2. **Build an integral monomial-core boundary chart.**  Clear denominators in
   the original max-12 coefficient equations before splitting Kummer order;
   identify which horizontal components meet `p=0 mod 3`.  This is the only
   honest interface between the new `(9,12)` seed and selected Q8.
3. **Open the `(8,12)` polynomial-core first rows only after the D12 gate.**
   Its exact seed is useful, but a large characteristic-zero expansion is
   lower information than the complete first p-adic lift.

### Global wall and allocation

The new maps do not prove or disprove JC2.  They do not change `G2-PSC`, any
invoked `G2-BD`, full landing/coverage, or an absolute/cofinal complexity
ceiling.  Conversely, an empty total-D12 gate would not close either
partial-`y` frontier because `x`-degree/support can grow.

For one bounded sprint, change `Q8 40 / AS 30 / TD6 25 / global 5` to

```text
Q8 selected proof 35 / paired D12-AS disproof 35 / TD6 25 / global 5.
```

Revert the extra five points after both mod-nine matrices and, for any
survivor, one complete mod-27 obstruction are frozen.  Existing AWS Q8 jobs
continue; the new gate should use otherwise idle shards and must not preempt
the moving-`d4`/coefficient-infinity endpoints.

## 6. New mechanism, connections, and history/dedup

### New mechanism — integral right-conjugate Cartier compiler

Input an integral polynomial automorphism `B`, a residue seed `A o B`, and a
finite support `S`.  The compiler must:

1. verify `B,B^(-1)` and determinant one over `Z`;
2. preserve the original support and all determinant rows;
3. pull the correction module through `B^(-1)` and prove equality with the
   direct original-coordinate Cartier matrix;
4. retain every divided integer carry at higher precision;
5. track an explicit unit-separated collision pair and refuse nonunit source
   or target normalizations.

This is a genuinely new reusable proof object.  It connects row 5's source
automorphisms, row 19's Witt lifting, row 21's finite-type compactness, row
29's obstruction modules, row 31's integrality, row 32's collision scheme,
and row 46's proof-carrying software.

### New connection — wild Kummer degeneration as the proof/disproof seam

The same `(9,12)` coefficient space contains a characteristic-three
monomial cubic core and characteristic-zero order-three Kummer charts, but
the character decomposition is not integral across `p=3`.  The correct
common object is the denominator-cleared original coefficient scheme with a
Rees/normal-cone split along `3=p=0`, not a reduction of the selected Q8
coordinates.  This links the AS and Q8 lanes without importing either lane's
conclusions.

### History/dedup checksum

- `ARTIN-SCHREIER-SEED`: **KNOWN**.
- `TRIANGULAR-HIGH-DEGREE-EMBEDDING`: **NEW EXACT OBJECT/CONNECTION** at both
  primitive max-12 degree pairs, with unit leading coefficients.
- `RESIDUE-BALL-COLLISION/COMPACTNESS`: **KNOWN REVIEWED THEOREM**, newly
  consumed through an exact integral right-conjugacy.
- `MAX11 -> MAX12 FRONTIER`: **KNOWN REVIEWED ROUTING**.
- `Q8 p=0 / ORDER-ONE BOUNDARY`: **KNOWN OPEN LOCUS**, newly supplied with an
  exact noninjective residue control; no theorem promotion.
- `D12 FULL-SUPPORT CARTIER GATE`: **NEW EXPERIMENT**.
- `GLOBAL LANDING/CEILING`: **UNCHANGED WALL**.

## 7. Three detailed cards

### Card A — paired complete D12 Cartier/Kuranishi gates

**Dependencies.**  The two exact integer seed lifts, all 91 monomials per
coordinate through total degree twelve, all 276 determinant rows, and no
gauge quotient before direct replay.

**Cheapest falsifier.**  Generate the mod-nine affine matrices independently
in original and AS-conjugate coordinates.  Any rank/augmented-rank mismatch,
missing determinant row, or failure of (3.1) rejects the compiler.  An
inconsistent system kills that seed's full total-D12 tube immediately.

**Outcomes.**  Empty/empty is a strong bounded proof-side no-go.  A survivor
feeds one full mod-27 Kuranishi/Fitting computation.  A source-complete
compatible tower would, by reviewed compactness and collision transfer, give
a complex counterexample.

**Stop rule.**  Stop point sampling after the first affine kernel.  Stop the
fixed cap on a unit Fitting ideal.  After two surviving depths, require exact
truncation maps and singular-stratum classification before increasing depth.

**Information gain/cost.**  Extremely high / low-to-moderate: two exact
linear systems first, then only survivor kernels.

### Card B — integral max-12 monomial-core/Kummer boundary

**Dependencies.**  Original `(9,12)` and `(8,12)` coefficient equations,
denominator-cleared Taylor rows, explicit leading-core variables, and the
reviewed Kummer routing only on its licensed generic opens.

**Cheapest falsifier.**  Specialize the integral source to each residue seed
and verify every original row before any division by `3`, `p`, or a Kummer
root.  Compute the horizontal normal cone along `3=p=0`; test whether any
component dominates the 3-adic base and reaches the selected order-three
open on the generic fibre.

**Outcomes.**  No horizontal component proves the present Q8 chart cannot
receive this seed.  A component supplies the first honest AS-to-Q8 landing
and inherits terminal/Taylor obligations.  A purely order-one component
routes to a new polynomial-core lower system, not selected Q8.

**Stop rule.**  Stop on a nonunit normalization or failed original-row
specialization.  Do not run large lower-row Gröbner bases until the horizontal
component and its Kummer order are certified.

**Information gain/cost.**  Very high / moderate; it decides whether the two
best current proof/disproof lanes actually meet.

### Card C — proof-carrying integral-transform/collision oracle

**Dependencies.**  Exact `B_8,B_9` formulas, source and target transformation
matrices, fixed support manifests, and the reviewed residue-ball theorem.

**Cheapest falsifier.**  Round-trip every monomial basis through `B` and
`B^(-1)`, compare determinants coefficientwise, and replay the displayed
collision pairs over `F_3`, `Z/9`, and each accepted higher precision.  The
oracle must reject any source scaling with nonunit determinant or any support
slot introduced after launch.

**Outcomes.**  A PASS makes AS/Q8/TD6 normalization provenance machine-
checkable and lets one coefficient scheme be viewed in the cheapest chart.
Failure names the first denominator/support obstruction instead of allowing
an invalid p-adic inference.

**Stop rule.**  Implement only the two seeds and one negative nonintegral Q8
normalization first.  Generalize only if both D12 matrix controls agree.

**Information gain/cost.**  High / low; it removes a recurring source-
honesty failure across all three live lanes.

## Final recommendation

Launch Card A first on idle AWS capacity, both seeds in parallel.  Keep the
current Q8 moving-`d4` and coefficient-infinity jobs untouched.  Preflight
Card B from source equations while the linear gates run; Card C is the shared
acceptance harness.  Treat consensus or finite-depth survival as scheduling
evidence only.  The first theorem-level event would be either a complete
fixed-cap unit obstruction or a compatible all-depth integral tower; neither
exists at this cutoff.
