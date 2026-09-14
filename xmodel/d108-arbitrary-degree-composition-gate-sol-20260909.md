# Arbitrary-degree D108 composition: independent fallback gate

Tag: `d108-arbitrary-degree-composition-gate-sol-20260909`  
Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`  
Reviewer: Root Sol fallback, 2026-09-09

## Scope and disposition

I read only the literal files in `/tmp/jc2-lane.21zsKX/inputs`. I read the new
source audit and transaction whole; the accepted general-normalizer proof and
gate whole; the repaired D108 gate, Euler-envelope proof, and retained
`CROSSCHECK` whole; every frozen historical excerpt; and every supplied primary
interval whole. Manifest and custody data were used only as provenance. I did
not follow their source paths, read a current cross/F9 gate, fetch an archive,
or inspect any unsupplied theorem or certificate interior.

The three verdicts are separate:

- **A — CONFIRMED at the stated imported-theorem tier.** Every actual ordinary
  characteristic-zero pair of degrees 72 and 108 reaches one of the two
  published degree-108 chains, with the full source data needed by the accepted
  envelope and repaired `(8,28)` interface. This is source coverage, not
  containment in the old 507-variable chart.
- **B — CONFIRMED at the retained published-reduction and external-certificate
  tier.** The `(9,27)` literal system is excluded through Proposition 4.1 and
  Corollary 5.7, including its indispensable translation. Both `(8,28)` literal
  systems are excluded by the retained Helali/Suzuki record at its unchanged
  trust perimeter.
- **C — CONFIRMED CONDITIONALLY at the stated imports.** Target degree descent,
  followed by the general normalizer and the published normalized-case
  exhaustion, proves that a counterexample has maximum degree at least 125.
  This does not use the literal arbitrary-representative headline of 2022 as a
  degree classifier.

No new composition arrow is missing. The first facts not proved from the frozen
bytes are the expressly permitted imported theorem/classification interiors and
external certificates identified under each verdict.

## A — all actual 72/108 source coverage

### A1. Given-pair normalization is affine in degree 108

Start over `C`; for an alleged pair over any characteristic-zero field, the
finitely generated coefficient field embeds in `C`, preserving the two degrees,
the nonzero Jacobian constant, and all nonzero coefficients. Swap the outputs if
necessary and write the degrees as

```text
deg P = 2*36,    deg Q = 3*36.
```

They do not divide one another, so the plane-automorphism degree-division
property makes the pair nonautomorphic. The GENERAL statement of the accepted
normalizer applies to this given representative; no D25/F2 table filter is
being imported. It gives a polynomial source automorphism, attained
coordinatewise corners `2(a,b)` and `3(a,b)`, support in their two rectangles,
and positive integers `a<b`, together with inverse-coordinate degrees
`M,N >= 1`, such that

```text
36 = M*a + N*b >= a+b.
```

The equality is exact because each rectangle corner is present and uniquely
maximizes the positive degree functional `(M,N)` after inverse substitution;
the product of the two leading inverse-coordinate forms is nonzero. The
proportional second rectangle proves the original reduced output ratio rather
than assuming that an arbitrary source automorphism preserves it.

GGV Proposition 5.20 then applies to this ordinary `(2,3)`-pair. Its literal
proof uses only the identity or `y -> y+lambda`; hence it stays polynomial,
preserves the attained rectangles and their corner coefficients, and gives a
standard pair of actual total degrees

```text
2(a+b),    3(a+b).
```

If `a+b<36`, this is a nonautomorphic polynomial Keller pair of maximum degree
strictly below 108. That contradicts the already accepted robust actual
`max<108` exclusion recorded in the historical scope. This step uses neither
the proposed 125 conclusion nor the 2022 arbitrary-representative headline.
Therefore `a+b=36`, and

```text
(M-1)*a + (N-1)*b = 0.
```

Positivity of `a,b` and `M,N>=1` forces `M=N=1`. The inverse normalizer, and
therefore the normalizer itself, is affine; the Proposition 5.20 translation is
affine as well. Thus the standard pair still has actual degrees 72 and 108.
Swapping the outputs supplies the opposite `(3,2)` orientation and changes the
Jacobian only by a nonzero sign.

This is the point at which the new audit's proposed source applicability was
most vulnerable. The argument is nevertheless noncircular: only the accepted
strict-below-108 result is used to turn `a+b<=36` into equality.

### A2. The correct complete table is Section 6, not the M=35 table

Both possible starting corners have coordinate sum 36. Algorithm 8's Section 5
output with `M=35` therefore cannot classify either one; appealing to it would
miss the boundary rather than merely alter notation.

The separately supplied whole Section 6 excerpt states that it describes all 34
possible counterexample shapes with maximum degree at most 150, lists the cases
for equality (3.17), and obtains the opposite convention by swapping `m,n`.
Across its family, length-one, length-two, and length-three tables, the only rows
of maximum degree 108 are exactly

```text
A0=(8,28), A1=(11/4,7),                    (m,n)=(3,2);
A0=(9,27), A1=(9,24), A2=(11/3,8),         (m,n)=(2,3).
```

The first Section 6 table has no other 108 entry; the length-three table has
none. The other row beginning at `(8,28)` has successor `(7/4,3)`, orientation
`(3,4)`, and maximum 144, so it is not an alternative degree-108 branch. I
consume the published completeness of the Section 6 enumeration at statement
scope. I did not reproduce or execute its sieve.

### A3. The `(8,28)` row supplies the whole starting face

Orient the row as a standard `(3,2)` pair `F,G`. The fractional successor
`A1=(11/4,7)` rules out type II.a, since in that case Theorem 2.20 would make
`A1=A0'`, an ordinary integral lower corner. Hence the starting corner is type
II.b. The common weighted line through `A0` and the generated `A1` has primitive
normal `(4,-1)`.

Write the ordinary last lower corner as `A0'=(u,v)`. The face equation and the
II.b sign condition are

```text
4u-v=4,    u>=1,    v>=0,    u-v>0.
```

They force `A0'=(1,0)`. Theorem 2.20(8) then gives
`l1=lcm(4,1)=4`, so the ramification is 4. In the swapped coordinates used by
Proposition 4.3, the accepted Corollary 7.4 interface has Euler endpoint
`(21,6)=(3/4)(28,8)`, hence its denominator `q` is also 4.

The two full `(4,-1)` faces have vanishing leading bracket. Applying the
statement of GGV Proposition 2.1 gives one common homogeneous polynomial `R`
and nonzero scalars `c_F,c_G` with

```text
ell_(4,-1) F = c_F R^3,    ell_(4,-1) G = c_G R^2.
```

The attained endpoints `(1,0)` and `(8,28)` of `R` make

```text
R = x*r(x*y^4),    deg r=7,
```

with both the constant and leading coefficients of `r` nonzero. Theorem
2.20(8) chooses a nonzero root `lambda` of the `F` face with multiplicity 21,
because the successor's normalized second coordinate is 7. Since the `F` face
is a cube, `r(z^4)` has multiplicity 7 at `z=lambda`. Characteristic zero and
`lambda!=0` make `z -> z^4` unramified there, so `r(w)` has the nonzero root
`alpha=lambda^4` with multiplicity 7. Its degree is 7; consequently

```text
R = kappa*x*(x*y^4-alpha)^7,    kappa,alpha != 0.
```

The linear source scaling `x -> alpha*x` converts this, up to a nonzero scalar,
to `H=x*(x*y^4-1)^7`. Independent nonzero target rescalings then make the two
entire faces exactly `H^3,H^2`. Because the rectangle corners are attained and
coordinatewise maximal, their total leaders are simultaneously the unique
monomials `x^24*y^84` and `x^16*y^56`, with coefficient one after those same
rescalings. No root at zero, vanished leader, or generic coefficient stratum is
being discarded.

The manual changed-successor control isolates why the table successor is
essential: replacing `R` by
`x*(x*y^4-1)^3*(x*y^4-2)^4` keeps endpoints `(1,0),(8,28)`, but a root of
multiplicity 3 generates `(7/4,3)`, not `(11/4,7)`. Thus top-degree matching
alone would not prove the attachment. Its pure powers have zero bracket and are
not offered as Keller examples.

### A4. Envelope and repaired Proposition 4.3 interface

The accepted Euler-envelope proof assumes precisely a polynomial Keller pair,
the two unique total leaders, and the two complete normalized faces just
derived. It does not assume the old `h,D,C` formulas, fourteen residuals, or a
point in their coefficient chart. Its polynomial Euler theorem first rules out
larger exponents in the opposite coordinate and gives

```text
ell_(0,1) F=(x+s)^24*y^84,
ell_(0,1) G=(x+s)^16*y^56
```

with one common `s`; equality of the two shifts follows from cancellation of
the weight-139 leading bracket, not from choosing roots independently. The
single translation `x -> x-s` lowers both total degree and `(4,-1)` weight for
every newly created term. It therefore preserves Keller-ness, actual degrees,
the unique total leaders, every coefficient and endpoint of both starting
faces, standardness, the type-II.b starting triple, `q=4`, and the selected
multiplicity.

The repaired gate then applies at exactly this interface. Its whole-positive-
interval and opposite-predecessor steps remain the stated external imports
through the cited Corollary 7.4 and predecessor results; they are not inferred
from the fixed edge alone. I retain the accepted correction verbatim in
substance: `st(P)` has ordinate `12d`, while `st(R)` has ordinate `d`. The
gate's bound `d<=1` is the scaled-lattice conclusion, not a condition that
`st(R)` itself have ordinate `12d`.

Accordingly A is confirmed for every actual 72/108 pair and both output
orientations. It establishes a forward attachment to the published cases. It
does **not** establish reverse containment in the 507-variable physical chart,
and no such containment is used below.

## B — both literal exclusions at retained trust

### B1. The `(9,27)` literal system

Proposition 4.1, read with its whole supplied proof, gives `P*,Q* in L^(1)`,
`[P*,Q*]=x`, and exactly

```text
N(P*)=conv{(0,0),(1,1),(6,16),(6,18),(0,18)},
N(Q*)=conv{(0,0),(1,0),(9,24),(9,27),(0,27)}.
```

Every vertex is attained, and both hulls lie in the nonnegative quadrant; a
Laurent polynomial with either Newton hull therefore has no negative-exponent
term and is an ordinary polynomial. The final Laurent morphism in the proof
changes the bracket by `-x`; multiplication of one output by a nonzero scalar
absorbs the sign without changing a hull or an attainment guard.

Corollary 5.7, not Theorem 5.1 by itself, is the literal exclusion. Its proof
first obtains
`ell_(0,1)P*=lambda_p*y^18*(x-lambda)^6`, with both scalars nonzero, and applies
the ordinary translation `x -> x+lambda`. The bracket becomes `x+lambda`, a
permitted `x+g(y)`, and the translated faces acquire the exact endpoint guards
of Theorem 5.1. Skipping that translation would leave the original upper face
and would not discharge Theorem 5.1's endpoint hypotheses. The interior of
Theorem 5.1 is an explicit published import; Corollary 5.7's supplied proof is
the checked bridge to it.

### B2. Both `(8,28)` literal systems

Proposition 4.3, read with its whole supplied proof, yields `[P*,Q*]=x^2` and
one of these two exact outcomes:

```text
larger:
 N(P*)=conv{(0,0),(1,0),(8,14),(8,16),(0,8)},
 N(Q*)=conv{(0,0),(2,1),(12,21),(12,24),(0,12)};

smaller:
 N(P*)=conv{(0,0),(1,0),(8,14),(8,16)},
 N(Q*)=conv{(0,0),(2,1),(12,21),(12,24)}.
```

All displayed vertices are attained and both hulls are nonnegative, so these
too are ordinary rather than genuinely Laurent systems. The proof's final
morphism has determinant `-x^2`; a nonzero output scaling gives the printed
positive convention and preserves all vertices and guards.

The retained `CROSSCHECK` matches these exact two hulls, the convention
`P_x Q_y-P_y Q_x=x^2`, the complete lattice supports, corner-attainment
conditions, and the larger/smaller numbering. It records exact Helali and
Suzuki exclusions for **both** branches. The frozen historical errata withdraw
the campaign's internal cCa2/cCa6 characteristic-zero-header inference but
expressly preserve this independent external route. I therefore consume the
external exclusions only with their recorded artifact, normalization,
transcription, reduction, and lifting-lemma trust debts. I did not replay a
certificate, promote a first-prime msolve trace, or treat an unavailable
archive as new evidence.

Thus B is confirmed at unchanged retained trust. Omitting the larger polygon
would leave a literal Proposition 4.3 alternative open; it is not omitted
here.

## C — maximum degree at least 125 by composition

### C1. Finite target degree descent

Assume over `C` that a nonautomorphic ordinary Keller pair has component
degrees `d,e` and maximum strictly below 125. A component cannot be constant.
If both degrees are one, its nonsingular linear part makes the pair affine
invertible.

Suppose `d|e` and `d+e>2`; the equal-degree case is included. The homogeneous
component of degree `d+e-2` in the bracket is
`[P_d,Q_e]`, and it is zero because the full bracket is constant. Apply only
the **statement** of GGV Proposition 2.1 at total weight. Writing `k=e/d`, it
gives a nonzero scalar `lambda` with

```text
Q_e = lambda*P_d^k.
```

The target triangular automorphism

```text
(P,Q) -> (P, Q-lambda*P^k)
```

preserves the nonzero bracket and nonautomorphy, cancels the whole degree-`e`
part, strictly lowers the degree sum, and cannot raise the maximum. For `d=e`,
this is the same argument with `k=1`. If `e|d`, interchange the roles and
subtract the corresponding power from `P`. Proposition 2.1's proof is not in
the charged bytes and remains an imported theorem proof, exactly as required.

The changed component cannot become constant, since its bracket with the other
component is still nonzero. If either component becomes linear, an affine
source change makes it `x`; then the bracket equation makes the other component
`c*y+f(x)` with `c!=0`, so the pair is triangularly invertible. A counterexample
therefore cannot terminate in either exceptional case.

The positive integer `d+e` decreases at each subtraction, so the process ends.
At its counterexample endpoint neither degree divides the other. Writing

```text
d=mD,    e=nD,    gcd(m,n)=1,
```

then has `m,n>1`: `m=1` would say `d|e`, and `n=1` would say `e|d`.

### C2. Normalization does not undo the degree bound

Apply the accepted GENERAL normalizer to this terminal pair. Its exact identity

```text
D=M*a+N*b >= a+b
```

gives standard degrees `m(a+b)<=mD=d` and `n(a+b)<=nD=e`. Thus the maximum is
nonincreasing both through target descent and through source normalization.
Literal Proposition 5.20 preserves these two total degrees and polynomiality;
it does not restore a larger representative. Source and target automorphisms
also preserve nonautomorphy.

Now consume the 2022 Section 2 list as the published **normalized-case**
exhaustion below 125. I do not infer it from Theorem 2.1's literal
arbitrary-representative headline. The other normalized cases in its table
(maxima 64, 75, 84, 96, 99, 112, and 120) remain excluded by the published
results cited there and in the accepted historical scope; their proof
interiors are explicit imports. The normalized exhaustion leaves only the two
degree-108 chains. Verdict A attaches each actual chain to its literal
published interface, and verdict B excludes both.

This contradiction proves, conditional on precisely those imported
classification and exclusion results, that every characteristic-zero
counterexample has maximum degree at least 125. For a general
characteristic-zero coefficient field, embed its finitely generated
coefficient subfield in `C`. If a polynomial inverse exists only after this
base change, membership of `x` and `y` in the generated polynomial algebra is
a finite linear system over the coefficient field and descends; thus a genuine
counterexample is not lost by the embedding.

The equal-degree representative is a load-bearing manual control. Conditional
on a 72/108 pair `(P,Q)`, target addition can produce an apparent 108/108
representative such as `(P+Q,Q)`. The 2022 headline alone would misclassify
that label. The equal-degree subtraction above removes its proportional top
part and returns the descent to a nondividing representative. This is why C
does not inherit the audit12j fallacy.

## Trust boundaries and non-claims

The first nonlocal boundaries for A are the accepted general-normalizer
theorem, the accepted robust `max<108` theorem, published completeness of the
2017 Section 6 table, and the theorem interiors retained by the Euler and
repaired Proposition 4.3 gates. For B they are Theorem 5.1's interior and the
retained external exact certificates plus their reduction/transcription
bridge. For C they are the proof of GGV Proposition 2.1, the normalized-case
exhaustion, and the other published small-case exclusions. These are declared
imports, not silently filled gaps.

The conclusions do not establish physical-chart coverage, a 507-variable
containment map, a new unit/cofactor certificate, a source point, degree-140
exclusion, all-degree JC2, solver permission, or any automatic promotion. The
manual changed-successor, zero-J face, omitted-large-polygon, skipped-
Corollary-5.7-translation, and divisible/equal-degree controls above are
factored reasoning only; none was executed.

Zero mathematical subprocesses, agents, CAS operations, generators, source
expansions, certificate replays, or external actions were used in this review.

## OPEN(S) RAISED

None.

<!-- BODY-END -->
