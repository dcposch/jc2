# Exact norm loss and the whole atomic boundary measure of a normalized Keller map

Producer: swarmHQ ROOT and retained co-researcher fresh_gap_design_0640 (Astra role; actual hosted model IDs unmeasured).
Independent mathematical review: retained fresh_gap_sol56_0640 (fallback role; actual hosted model ID unmeasured).
Date: 2026-10-27 UTC.
Basis: 4fc82c8248564edb8d5446418a0fc93880956e1c.
Evidence tier: MANUAL / PASS_CONDITIONAL on the named foundations below.
Lifecycle: PROVISIONAL; independent review does not attest a different-model promotion gate.

## Statement and notation

Let F be a polynomial Keller map of the complex affine plane. Use the single target-normalized representative H of the [finite positive-thinness moment report](finite-positive-thinness-moment-swarmHQ-root-astra-20261027T191000Z.md).
Write N for its function-field degree, d>N for its algebraically stable polynomial degree, I for its finite indeterminacy set on the line at infinity, and q for its regular fixed point at infinity, with q not in I.
The extension of H maps the rest of the line at infinity to q. Every actual nonproper-image curve D_i has its only point at infinity at q.
Let theta=lim d^(-m) H^(m*)L be the normalized nef pullback eigenclass and mu its unique representing Radon probability, at the FRAME foundation tier used in that report.

On the actual finite normalization X of the target plane in the source function field, retain the WHOLE source U=A^2 as the prescribed open subset.
The omitted height-one primes are E_i; H maps E_i onto D_i with transverse index r_i and residue degree delta_i. Set b_i=-ord_Ei(ell)>0 for a generic affine linear polynomial ell, and nu_i=ord_Ei/b_i.
Use the notation

    S_pole = sum_i b_i delta_i deg(D_i),
    W      = sum_i r_i delta_i deg(D_i),
    lambda = d-S_pole.

S_pole is the quantity denoted S in the accompanying norm-loss receipts. It is NOT the nonnegative slack also called S in the earlier sheet-budget report.
For n>=0 and each i, let V_(n,i) be the finite set of primitive divisorial extensions of ord_Ei under H^n, and write

    H^n_* ord_v = e_v ord_Ei,    f_v = residue degree,    b_v = generic line pole order,
    nu_v = ord_v/b_v.

If S_pole>0, the following conclusions hold at the stated conditional tier:

1. 0<lambda<d, and for every n,i, sum_(v in V_(n,i)) f_v b_v = b_i lambda^n.
2. The labels (n,i,v) give distinct normalized valuations, first reaching an affine-centered valuation after n+1 applications of H.
3. The entire measure is

       mu = sum_(n>=0,i,v in V_(n,i))
              [b_v f_v delta_i deg(D_i)/d^(n+1)] delta_(nu_v).

   Its mass at first-exit depth n is (S_pole/d)(lambda/d)^n. No residual mass remains.
4. Every displayed atom has positive thinness A(nu_v)=e_v r_i/b_v. Thus mu(A=0)=0 and integral A dmu=W/(d-N).

If S_pole=0, there are no omitted E_i, and the prior finite-moment/THIN result gives mu(A=0)=1 instead.
Nothing here proves S_pole=0, W=0, finite support, Cartierness, valuativity, properness, N=1, or JC2.

## Dependencies and relationship to earlier work

The [all-Keller sheet-budget report](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) supplies the actual finite normalization with the whole source retained, and polynomial-A^1-normalized omitted image curves.
The [composition report](keller-deficit-composition-and-iteration-neutrality-swarmHQ-root-astra-20261026.md) supplies degree-one transport on the A^1 normalizations of polynomial curves under a Keller map. This does not set delta_i=1 for boundary divisors.
The [finite-moment report](finite-positive-thinness-moment-swarmHQ-root-astra-20261027T191000Z.md) supplies the same-H normalization, normalized pullback convergence, FRAME measure uniqueness, and the killed-divisor atom bound. Its source and custody qualifications remain in force.
We also use finite normalization of DVRs, the principal-divisor formula for a field norm, transitivity of norms, and sum e_v f_v=[K:L] for these characteristic-zero finite extensions.
These are named foundational inputs; this publication does not claim a fresh audit of their primary proofs. It imports no improper-map inverse-class expansion from the proper-only FJ A.7.

The earlier CURVE1758 norm calculation retained finite generic-position orders but did not establish one all-iterate position or eigenmeasure weights.
Here the SAME H has all relevant image infinities at q and all relevant source centers in I, disjoint from q. This fixes the orders simultaneously and permits iteration of one rational factor group.
The earlier sufficient proposal to force d^n inverse-pole growth is rejected, not proved: its omitted-divisor denominator changes that growth to (d-S_pole)^n.
The prior finite-moment theorem identified the positive-thinness part. The probability saturation below identifies the WHOLE measure in the hypothetical nonproper case.

## Proof

### 1. One position for all curve equations and inverse divisors

Every E_i has source-plane center in I. At a point of the line at infinity outside I, H is regular and maps to q at infinity, so a valuation centered there cannot map to a generic affine point of D_i.
The same holds for every v in V_(n,i). An affine-centered valuation stays affine-centered under a polynomial map. A valuation centered at infinity outside I maps to a valuation centered at q, which then stays centered at q, since q is regular and fixed.
Neither can eventually become nu_i, whose center is in I. Thus all these v have source-plane centers in I and b_v>0.

Every forward image H^j(D_i) is polynomial-A^1-normalized and has only infinity q. Its degree is d^j deg(D_i).
More generally, if C is polynomial-A^1-normalized and has only infinity q, its polynomial parametrization is generically one-to-one; H restricted to its normalization has degree one by the adopted Keller curve-transport result.
At the only point at infinity of that parametrization, the regular leading behavior at q multiplies its pole degree by d. Therefore deg H(C)=d deg C and H(C) again has only infinity q.
For an irreducible equation f_C of such a curve, its leading homogeneous part is nonzero at each point of I. Consequently, for every relevant v centered in I,

    ord_v(f_C) = -b_v deg(C).

This is one simultaneous condition, not a new generic choice for each iterate.

### 2. The exact norm on an invariant group of rational functions

Identify the target rational-function field with C(x,y), and write N_H for the field norm associated to H^*: C(x,y) -> C(x,y).
On X the divisor of a source polynomial f_C consists of its retained affine prime C, with coefficient one, and the omitted primes with coefficients ord_Ei(f_C).
Pushing this divisor through the finite map gives

    div N_H(f_C) = [H(C)] + sum_i delta_i ord_Ei(f_C) [D_i].

The retained coefficient is one because C -> H(C) has normalization degree one. In the omitted term the coefficient is delta_i ord_Ei(f_C); there is NO extra r_i.
All negative coefficients and coincident image factors are retained. Since the target affine plane is factorial, equality of these divisors identifies the rational functions up to a nonzero constant.
Writing c_i for an irreducible equation of D_i, Step 1 therefore gives

    N_H(f_C) = constant * f_H(C) / product_i c_i^(b_i delta_i deg(C)).

Let Gamma be the multiplicative group generated by constants and equations of polynomial-A^1-normalized curves whose only infinity is q.
The displayed formula proves N_H(Gamma) is contained in Gamma. On this group, ordinary degree at generic infinity, deg_infty(a/b)=deg(a)-deg(b), satisfies

    deg_infty N_H(g) = lambda deg_infty(g).

Ratios, repetitions and cancellations are handled by additivity of degree and divisors. No numerator-only degree estimate is being substituted for this equality.

Choose ONE line ell=0 whose point at infinity avoids I. Every relevant v then satisfies ord_v(ell)=-b_v.
The polynomial image H(ell=0) has degree d, A^1 normalization, and only infinity q. The same finite-divisor formula shows N_H(ell) belongs to Gamma and has degree at generic infinity lambda.
Transitivity of field norms, with the source/target identifications just specified, now gives

    deg_infty N_(H^n)(ell) = lambda^n        (n>=1).

For g in Gamma, ord_Ei(g)=-b_i deg_infty(g), including rational g. The finite-DVR norm formula consequently yields

    -b_i lambda^n = ord_Ei N_(H^n)(ell)
                   = sum_(v in V_(n,i)) f_v ord_v(ell)
                   = -sum_(v in V_(n,i)) f_v b_v.

For n=0 this is the identity b_i=b_i. For n=1, existence of an extension and positivity of b_v and f_v imply lambda>0. If S_pole>0, also lambda<d.
This proves the inverse-pole identity with the full boundary correction.

### 3. Actual omitted primes of iterates and their atom bounds

A v in V_(n,i) maps generically under H^n to E_i and under H^(n+1) to D_i. Its center on the finite normalization for H^(n+1) is a height-one prime over the generic point of D_i.
Its source-plane center lies at infinity, so it is an actual omitted prime of that normalization, not a retained affine curve. Its residue degree over D_i is f_v delta_i.
No earlier iterate can be affine-centered, because polynomial maps cannot return an affine-centered valuation to infinity. Hence its first exit occurs after exactly n live steps, followed by the application of H that sends E_i to D_i.
The deterministic orbit and its terminal E_i make all labels (n,i,v) disjoint.

Set G=H^(n+1). Then deg G=d^(n+1)>N^(n+1), the point q is still regular and fixed, and every nonproper-image curve of G is among the forward images H^j(D_i), all with only infinity q.
The normalized pullbacks for G form a subsequence of those for H. They therefore converge to the same theta, and FRAME uniqueness gives the same measure mu.
The killed-divisor atom bound from the finite-moment report, applied with these checked hypotheses to G, gives

    mu({nu_v}) >= b_v f_v delta_i deg(D_i)/d^(n+1).

Equivalently, resolve G once retaining v. Its complete divisor maps onto the complete D_i with degree f_v delta_i. Later iterates are regular along that curve, including q, and multiply its line degree by successive powers of d.
Finite-model Cartier/refinement compatibility gives the same lower bound. This argument requires no single resolution common to all n or all divisors.
The atomic carrier at each depth is finite. We do not assert that the entire Borel set of valuations with that first-exit time is a finite set.

### 4. Saturation and the moment

Sum the preceding lower bounds over each finite V_(n,i), using Step 2. Their total over all depths is

    sum_(n>=0) sum_i delta_i deg(D_i) b_i lambda^n / d^(n+1)
      = (S_pole/d) sum_(n>=0) (lambda/d)^n
      = S_pole/(d-lambda) = 1.

Because mu is a probability and the atoms are distinct, equality forces every lower bound to be exact and leaves zero mass off their countable union.
This proves the full measure formula and the geometric first-exit law, without assuming finite thinness moment or continuity of an unbounded signed functional.

Constant global Jacobian gives raw discrepancy a_v=e_v r_i and hence A(nu_v)=e_v r_i/b_v>0. For each i, the finite extension identity gives sum_v e_v f_v=N^n.
Using the now exact atoms and nonnegative summation,

    integral A dmu
      = sum_(n>=0) sum_i r_i delta_i deg(D_i) N^n / d^(n+1)
      = (W/d) sum_(n>=0) (N/d)^n = W/(d-N).

This agrees with the earlier finite-moment theorem. In the S_pole=0 case, positivity of each omitted-divisor summand makes the omitted list empty, so W=0; the already proved conditional finite-moment/THIN result yields mu(A=0)=1.

## Replay, review and negative checks

This is a desk-only derivation. There are no random seeds, primes, numerical precision claims or new computations.
The [evidence bundle](../box/norm-loss-whole-measure-swarmHQ-20261027T203000Z/README.md) preserves byte-identical proof and review receipts with a repository-relative checksum manifest.
NORMREVIEW2010 independently accepted the exact formulas and iterate hypotheses without mathematical repair. Its late reading of two earlier custody receipts is explicitly recorded in the preserved supplement; it is not retrospectively represented as receipt-first coverage.
All prior source and custody qualifications remain. A separate publication review checks this frozen exposition and bundle; its receipt is supplied alongside them.
The retained divisor coefficients furnish an important negative check: dropping the denominator would incorrectly replace lambda by d and revive the rejected divergence test. Replacing delta_i by one or inserting r_i into the norm coefficient is also unsupported.
Polynomial automorphisms have no omitted divisors, so S_pole=W=0; the positive-atomic conclusion is explicitly restricted to S_pole>0 and does not exclude them.

## Limitations and next discriminator

This is a structural necessary condition in a hypothetical nonproper Keller case, not a contradiction. Countably many divisorial atoms do not supply a finite support or a common finite Cartier model.
The missing step is a further actual global Keller constraint excluding this precise measure and norm configuration, or another independently sufficient global implication.
No new bounded closing test is established here, and no source expansion, control-family successor or degree-range audit follows automatically.

## OPENS RAISED

None. The remaining global exclusion is described as an unproved research gap, not as a newly admitted bounded test.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `4fc82c8248564edb8d5446418a0fc93880956e1c` (Git blobs only).

This lexical EMPTY result is not a novelty or historical-absence certificate. The preceding comparison identifies the prior mechanisms and the changed all-iterate argument.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13925`.
- Body SHA-256:
  `466868ccbb516f4a81606ab5609bf5f9df84291c64f3e451e04a01207ed00891`.
- Frozen basis: `4fc82c8248564edb8d5446418a0fc93880956e1c`.
