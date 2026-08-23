# Toric-circuit closure of the pinned D21 monomial relaxation

## Executive summary — five lines

1. **VERDICT: NO-KILL-AT-TIER-1.** The complete degree-one toric/Macaulay closure is exactly consistent on at least one characteristic-zero factor: coefficient rank = augmented rank = **3,852**.
2. The pinned input was independently reconstructed as **76 equations x 4,351 nonconstant monomial coordinates, rank 56, consistent**, with 68 active underlying variables and (z_0=1).
3. The cheapest occurrence-closed exact tier adds 944 sound row-variable products on the same 4,351 columns; its unit-pivot (E)-rank grows **56 -> 471** but it remains consistent with zero undecided rows.
4. The full occurring-pair census has **7,819,143** fiberwise-independent quadratic binomials; explicit storage is unattractive, while Macaulay degree two already projects to 135,240 reduced rows, 6,939,164 columns, and 87,058,335 nonzeros.
5. Thus in-memory iterated linear closure is not presently a viable kill lane under 8 GB; it is **not** promoted to the avenue's formal DEAD-END verdict because the pre-registered three-prime/zero-codimension/cubic-census abandon gate was not met.

## 1. Exact object and notation

Hard-substitute the six proved no-log pins

\[
tf1_{42}=tf2_{42}=tg1_{42}=tg2_{42}=tg01_{42}=tg02_{42}=0
\]

in the banked D21 state. A term is deleted exactly when its variable tuple contains a pinned variable. `Row_10[eta^28]` then vanishes, leaving 76 nonzero affine equations. At the pilot fiber

\[
(s_1,s_2,w_1,w_2)=(+1,+1,1,1),
\]

write them as

\[
F_i(x)=\sum_{e\ne0} a_{i,e}x^e+c_i=0,
\qquad i=1,\ldots,76,
\]

over the same etale algebra (E) used by `directionb_window.py`. The (+42) inhomogeneity is included once in (c_i) for `Row_20[eta^0]`. There are 4,351 distinct nonconstant exponent vectors, using 68 underlying variables. Their degree distribution is

| degree | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| monomials | 62 | 508 | 1,151 | 1,211 | 816 | 399 | 156 | 48 |

Six active variables (`uf18`, `uf24`, `vf1_34`, `vf1_36`, `vf2_34`, `vf2_36`) have no singleton coordinate among the occurring monomials. The affine relaxation has 36,519 nonconstant coefficient entries and nine scalar entries. Its accepted exact unit-pivot rank is 56 and it is consistent.

Introduce (z_e) for every occurring (x^e), and (z_0=1). The starting relaxation is the affine linear system (L_i(z)=0), with the (z_e) independent.

## 2. What “circuit closure” means here

Every genuine tail assignment satisfies

\[
z_a z_b-z_c z_d=0\quad\text{whenever}\quad a+b=c+d.
\]

These are valid quadratic toric binomials. Not every such binomial is a circuit in the technical support-minimal sense, so below “pair circuit” means an equal-pair-sum binomial, not necessarily a primitive circuit.

The pinned occurrence set has 4,352 coordinates after adjoining (z_0). Its homogenized exponent configuration ((1,e)) has rank 69, hence its toric relation lattice has rank

\[
4352-69=4283.
\]

### Circuit tiers considered

| tier | exact census | assessment |
|---|---:|---|
| Factor-to-target, (z_a z_b=z_0z_c), (a+b=c) | 6,783 binomials on 2,207 target coordinates; exponent-relation rank 2,590 | Cheapest direct quadratic subset, but still a nonlinear feasibility problem and far from the full lattice. |
| Singleton-peel restriction | 3,972 distinct binomials; a one-parent subset has 2,207 | Smaller and sound, but even weaker. |
| Within each row support | 18,519,733 per-row star binomials before cross-row deduplication; 2,946,552 unique; 2,447,725 independent quadratic-polynomial rows | Huge and algebraically arbitrary. Its exponent relations have rank 4,104 modulo 2, versus 4,283 for the full lattice, so it does not generate the full integer lattice. |
| All occurring-coordinate pairs | 7,819,143 star binomials, or 50,778,314 all-pairwise binomials | Natural full quadratic tier, but too large to materialize naively. |
| Exact downward-closure graph | 4,511 monomial coordinates and 4,442 selected triangular definitions | Scheme-exact, but it is just the original 68-variable nonlinear problem in auxiliary coordinates. |

For the full occurring-pair tier, 9,472,128 unordered coordinate pairs hash into 1,652,985 exponent-sum fibers. Of those, 1,363,363 are collision fibers; the maximum fiber has 63 decompositions. Choosing one anchor decomposition in every fiber gives exactly 7,819,143 independent binomial rows in the vector space of quadratic (z)-monomials.

An integer propagation audit found a triangular, unit-pivot set of all 4,283 exponent-lattice directions in three passes (611, 2,382, and 1,290 new pivots). Thus the quadrics span the entire integer relation lattice. This does **not** imply that the unsaturated quadratic ideal equals the full toric ideal scheme-theoretically: it can have extra zero-coordinate components. Saturating by every (z_e) recovers the dense-torus lattice ideal, but is not sound for this affine kill problem because individual tail monomials are allowed to vanish.

The exact affine alternative is to adjoin the downward closure of the occurring exponents. It contains 4,511 monomials including the unit—only 159 more than the current occurrence set plus unit—and all 68 singleton variables. There are 13,349 possible Hasse factor edges. Choosing one parent for each degree-at-least-two monomial gives 4,442 definitions

\[
z_e=x_jz_{e-e_j}.
\]

This removes toric-boundary artifacts completely, but reconstructs the original nonlinear (F_i(x)=0) system rather than simplifying it.

## 3. Sound closure used for the pilot

Directly appending millions of quadratic equations would require a nonlinear solver. The cheapest exact linear certificate search is instead a toric moment/Macaulay closure.

For a multiplier monomial (q=x^u), form (qF_i) and canonicalize every product by its summed exponent. This is precisely the linear consequence obtained after identifying all moment products related by the relevant toric binomials. If a linear combination of these rows equals 1, then

\[
1=\sum_{i,u}\lambda_{i,u}x^uF_i,
\]

which is an exact Nullstellensatz certificate of emptiness. Conversely, equal coefficient and augmented ranks only say that no certificate exists in the chosen multiplier space; they do not produce a tail point.

I used two nested tiers.

### Tier 0: occurrence-closed products

For each base equation and each of the 68 active variables, retain (x_jF_i) only if every resulting nonconstant exponent is already among the 4,351 columns; if (F_i) has a scalar, its singleton (x_j) must also occur. This gives 944 distinct new rows without introducing any new moment column:

| source band | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| products | 342 | 220 | 135 | 99 | 90 | 40 | 18 | 0 |

Every row is an actual polynomial multiple of a window equation, so this tier is sound even for the six variables lacking singleton coordinates. Notice the weakness relevant to the advertised obstruction: no Row-20 product is occurrence-closed, so this cheapest tier does not directly propagate the six Row-20 obstruction components.

### Tier 1: complete degree-one products

Use every multiplier in

\[
\{1,x_1,\ldots,x_{68}\}.
\]

Products outside the original occurrence set become new moment columns, always identified by their underlying exponent vector. The raw matrix has (76\cdot69=5,244) rows, 241,110 nonconstant columns, and 2,520,432 full polynomial nonzeros. Reducing the accepted base system to 56 generators gives an equivalent 3,864-row matrix with 2,487,381 full nonzeros (2,487,372 after removing the affine scalar column).

## 4. Pilot results and exact certificates

### Tier 0 result

The exact `directionb_window.esolve` unit-pivot calculation on the 76+944 rows gave

\[
\operatorname{rank}(A)=\operatorname{rank}([A\mid b])=471,
\]

with 3,880 free columns, no inconsistency, and zero undecided rows. Thus the same-column outer approximation gains 415 linear directions, from rank 56 to rank 471, but does not kill. The shipped replay took 206.6 seconds and about 188 MiB maximum RSS (about 199 MiB peak footprint).

### Tier 1 result

The complete degree-one matrix has 12 additional independent syzygies beyond the 1,380 relations inherited from the 20 base-row dependencies and their 69 multiples. Hence the raw left-nullity is

\[
1380+12=1392,
\]

and the candidate row rank is (5244-1392=3852).

The rank certificate has two exact halves.

1. Twelve sparse syzygies, with support sizes

   \[
   5,9,5,11,11,11,11,24,24,27,27,12,
   \]

   were lifted with exact (E)-arithmetic and checked coefficient-by-coefficient against the complete polynomial rows. Every residual dictionary is empty. Distinct normalized terminal rows certify their independence. None loses an affine scalar term, so the same 12 relations bound both the coefficient and augmented ranks by 3,852 on every (E)-factor.

2. The certified good-prime map

   \[
   E\longrightarrow\mathbf F_{105337},\qquad
   (r_3,a_1,a_2,\mu)=(795,50630,10114,50267)
   \]

   satisfies all four defining square/cube relations. At 3,864 deterministic evaluation points (seed 7210821), both coefficient and augmented evaluation matrices have rank 3,852. Evaluation can only lower coefficient-matrix rank, so this supplies a nonzero 3,852-minor. Its nonzero reduction proves that the corresponding characteristic-zero (E)-element is nonzero.

Together these give, on at least one characteristic-zero field factor of (E),

\[
\boxed{\operatorname{rank}(A_1)=
       \operatorname{rank}([A_1\mid b_1])=3852.}
\]

On that factor the chosen 56 base rows span the accepted rank-56 base system, so this is also the verdict for all 76 raw rows and their degree-one multiples. This is an exact characteristic-zero **consistency** certificate for the tier, not merely a modular guess. It is deliberately not claimed uniform over every (E)-factor. The shipped run took 35.1 seconds, with about 694 MiB maximum RSS (about 943 MiB peak footprint).

Neither consistency result is a point of the original variety. The 241,110 moment coordinates remain independent beyond the degree-one identifications, and no (x)-assignment was reconstructed.

## 5. Exact kill semantics

Every genuine pinned D21 tail assignment maps to every circuit and Macaulay relaxation above. Therefore exact inconsistency of **any** selected valid subset is a sound proof that the corresponding pinned window fiber is empty.

For a full D21 residue-A window kill, the statement to prove is:

> There is no assignment over an algebraic closure to the inherited D21 chart variables satisfying the raw Rows 6–20 (including the (+42) Row-20 inhomogeneity), the six no-log pins, the banked B/off-grid freezes, the radical relations, and the chart nonvanishing conditions.

Such a proof is a kill of the forced-tail locus in this promoted template/window. It is not by itself a theorem about every Jacobian pair or every untruncated chart. Deeper rows are unnecessary for the implication—every genuine realization must already satisfy D21—but the inherited template and freeze perimeter remains part of the conclusion.

The present pilot fixes ((s_1,s_2,w_1,w_2)=(+,+,1,1)). A contradiction there would kill only that fiber unless a separate torus-rescaling argument made it uniform. A global nonlinear kill must retain the nonzero (w_1,w_2) parameters or certify all four sign branches and all relevant radical/scale components. No tail coordinate may be saturated merely for convenience; tails can legitimately be zero.

## 6. Iteration, convergence, and viability

Degree-(d) Macaulay closure uses every multiplier of degree at most (d). The multiplier counts in 68 variables are

| (d) | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| multipliers (\binom{68+d}{d}) | 69 | 2,415 | 57,155 | 1,028,790 |

This hierarchy is theoretically complete for **emptiness**: by the Hilbert Nullstellensatz, if the characteristic-zero affine variety is empty, some finite degree contains a certificate (1\in(F_1,\ldots,F_{76})). It is not a constructive convergence theorem for nonempty varieties; a consistent tier supplies neither a point nor a bounded degree at which one will appear.

The exact support-only degree-two census already gives:

\[
\begin{array}{rcl}
\text{multipliers}&=&2,415,\\
\text{reduced-basis rows}&=&135,240\quad(183,540\text{ raw}),\\
\text{columns including }1&=&6,939,164,\\
\text{formal reduced-basis nonzeros}&=&87,058,335.
\end{array}
\]

The support census itself took 6.9 seconds and about 1.12 GiB maximum RSS, but materializing and eliminating 87 million Python sparse (E)-coefficients is projected above the 8 GB cap. Degree three has 57,155 multipliers before any matrix construction. Thus straightforward exact iteration is not viable; an out-of-core/block-F4 implementation or a strong character/band decomposition would be required.

The alternative “complete toric closure” does not rescue the route. Occurrence-wide quadrics are millions of equations and retain boundary artifacts unless treated carefully; the 4,442-relation exact graph simply returns to the original 68-variable nonlinear Groebner problem.

Against the pre-registered avenue criterion, the honest call is:

- The selected closure does **not** add zero linear leverage: the same-column rank grows by 415.
- Only one good-prime minor was needed because exact (E)-syzygies close the tier-1 rank proof; the requested three-prime zero-codimension screen for declaring the avenue dead was not run.
- The occurrence-closed tier has no Row-20 products, but no exhaustive character-coupling audit of all short quadrics was performed.
- A first cubic-circuit census was not run, although degree-two Macaulay growth is already prohibitive.

Therefore the registered DEAD-END gate is not satisfied. The defensible verdict is **NO-KILL-AT-TIER-1**, with the narrower engineering conclusion that naive in-memory linear closure cannot presently be pushed to tier two under the resource cap.

## 7. Reproduction

From the repository root:

```bash
cd /Users/dc/code/math/jc72108
export DIRECTIONB_STATE="$PWD/directionb_tails_D21.pkl"

# Full occurring-pair and factor-to-target census (~6 s)
python3 cases/directionb_toric.py census

# Within-row census (~24 s); illustrates why this tier was rejected
python3 cases/directionb_toric.py rowcensus

# Cheapest exact occurrence-closed closure (~3.5 min)
python3 cases/directionb_toric.py internal

# Complete degree-one exact certificate (~35 s; requires python-flint)
python3 cases/directionb_toric.py pilot

# Exact degree-two support/cost census only (~7 s)
python3 cases/directionb_toric.py projection
```

`pilot` asserts the pinned dimensions and nonzero counts, the four good-prime defining relations, all 12 exact (E)-syzygies, and both rank-3,852 minors. `census`, `rowcensus`, `internal`, and `projection` also contain exact numerical regression guards. The script only reads the banked state and does not intentionally mutate it or write result files.
