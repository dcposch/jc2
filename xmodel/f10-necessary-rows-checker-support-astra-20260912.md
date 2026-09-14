# Necessary-row checker: retained-support and wire feasibility

First action 2026-09-12 03:09:52 UTC. Original reserve 03:26 / HARD 03:29.
STATIC manual source analysis only; no execution or place choice.

## Scope and provisional result

This report traces the frozen necessary-row checker and its unchanged
independent arithmetic. Term support, not CPU/RSS or completion time, is
the quantity. Removed alternative inverse/pole computation is not a new
contribution and is not restored. Exact source read scopes and hashes
will accompany the sealed report.

Conclusion: on any execution reaching these operations without an earlier
place, scalar-unit or structural refusal, EVERY retained scientific
polynomial and every sparse arithmetic accumulator has fewer than 21000
possible terms. The unchanged 100000-term guard cannot cause a stop on
that circuit. A genuine graph polynomial has at most412 possible terms;
the30-polynomial graph payload is below1450000 bytes. The separately
authorized authority source closes the metadata bound: a genuine complete
canonical wire is below4MiB, below the unchanged128MiB cap. None of
these statements predicts CPU/RSS, mathematical acceptance or completion.

## 1. Counting lemma and source grading

For positive integer weights w1,...,wk, unit cubes based at integer
points of sum(wi*ei)≤W are disjoint and lie inside the weighted simplex
of radius W+sum(wi). Thus their number is at most
(W+sum(wi))^k/(k! product(wi)). For an EXACT homogeneous degree, eliminate
one weight-one exponent: the remaining exponents satisfy this inequality.
This bounds all potential supports, not just coefficients that survive.

The seven sparse coordinates are X1,X2,X3,X4,z,S,theta. Raw weights are
(1,2,3,4,7,1,3). In formal band objects S is absent and the auxiliary
theta has weight0. Coefficients lie in the selected field of degree f≤7;
its f dense coordinates are ONE sparse coefficient, not f support terms.

Three useful deliberately loose integer bounds follow by hand:

* Raw exact weight≤23: after eliminating X1 the other weights are
  (2,3,4,7,1,3), with sum20 and product504. The bound is
  43^6/(720*504)<20000. One explicit upper check is
  44^6=7256313856<20000*362880=7257600000.
* S-free, theta-free band exact weight≤27: remaining weights(2,3,4,7)
  give 43^4/(24*168)<849.
* Graph exact weight≤30: remaining weights(2,3,4) give
  39^3/(6*24)=59319/144<412.

These bounds hold in every admitted characteristic, including
specializations that make coefficients vanish. They require neither
generic nonvanishing nor a chosen prime. Addition and multiplication
accumulators stay inside the union or Minkowski-sum support envelope
BEFORE cancellation. Therefore post-operation homogeneity alone is not
being used to overlook a transient dictionary.

## 2. Retained operation ledger before SCALE

Checker line references are to the pinned514-line source.

| Source region | Retained and temporary objects | Support envelope |
|---|---|---|
| 54–147, leading/scalar work | c,C,D, finite series, contact scalars, ODE products | Weight0; auxiliary theta degree≤8 here |
| 149–243, formal upper solve and completed maps | oper products/partial sums, defects, basis, forcing, rhs, xyz, rho and diagnostics | At fixed gap h≤10, weight h; basis/variation objects weight0 |
| 244–298, late bands | y,N, targets including U² theta³, full residuals, Psi and values | Weight h≤10; same for every nonzero summand |
| 266–270, special integration | R*invC2, primitive, C²*primitive | Weight0; theta degrees≤7,8,14 respectively |
| 300–326, installation and auxiliaries | A, coefficient slices, pi, delta, dp,vp,kp | Raw degrees10,≤10,10,23; Laurent auxiliaries discussed below |
| 328–361, Euler reconstruction | other,rhs,qji,Bc, partial B, band readbacks | Coefficient weight17−3j; full B weight17 |
| 363–388, full bracket | EACH product before theta shift, J,residual, all108 slices,45 low rows,150 diagnostics | Raw weight≤23; theta-free slices have band weight≤23 |
| 464–471, graph input | Hq,Psi,z*P1[0],U*P0[0],mixed | Theta-free band weights≤27 |

Induction is literal: C,D and scalar matrices have parameter weight0.
Forcing multiplies gap i and h−i, so has weight h. The formal operator
uses only scalar theta coefficients. Upper solving removes theta
coefficients and divides by field scalars; completed maps preserve h.
At h7, y=z−U*d0 has weight7; at h8 the fixed term is U² of weight8;
at h10 val has weight10. No inversion of a parameter polynomial occurs.
Formal theta degrees are≤6 in residual operations, except the explicit
scalar integration product of degree14. A single coarse band bound
15*849=12735 covers all these objects, their slices and accumulators.

Installed A has weight10 and theta degree≤3. Euler coefficient Bc[j]
has weight17−3j. Before the bracket shift, a product has weight
26−3(ak+bl)≤23 because ak+bl≥1; after multiplication by
theta^(ak+bl−1) it has weight23. The identical calculation gives the
Euler rhs degree. Coefficient extraction can only lower these weights.
This proves the raw <20000 bound for partial products, not just final J.

Do not assume auxiliary negative coefficients vanish before their late
diagnostic. Exactly

    dp=S^(-1)(Ac[2]+U),
    vp=S^(-1)(Ac[1]−z+U*dp).

Thus S*dp is ordinary homogeneous weight4 and S²*vp is ordinary
homogeneous weight8. Their numerators, products and partial sums satisfy
these translated support envelopes even if a canonical anomaly would
later refuse them. They are far below the same20000 bound.

The arithmetic file's dense rational/field operations are separate:
literal septic formation is degree≤7, field products are reduced modulo
degree f≤7, and Euclidean algorithms act on these univariate scalar
arrays. Reduced products have at most2f−1≤13 entries before reduction;
extended-Euclid coefficient degrees are bounded by f (a conservative
product bound2f gives at most15 entries). Literal rational septic
assembly has at most8 entries. These never create Poly support keys.
No scientific step uses their array length as a substitute for the sparse
support count. Lines442–463 only inventory/alias already bounded diagnostics
and test their emptiness; they create no larger polynomial.

## 3. Every retained SCALE intermediate

Write Phi for the injective Laurent monomial map z→s², theta→s*t,
with Xi,S fixed, and Psi_d(p)=s^(−d)Phi(p). This is precisely to_scale
when theta is rescaled; theta-free inputs use the same map. Injectivity
follows because the theta exponent is retained, so the old z exponent
is recovered from (new s exponent−theta exponent+d)/2. Translations by
fixed S or s powers preserve support count. No specialization s=1 occurs.

The source expressions, not the late zero comparisons, imply:

    origA=Psi_3(A), origB=Psi_5(B);
    origd=Psi_1(dp), origv=Psi_2(vp), origk=Psi_3(kp);
    origu=Psi_1(U), origell=Psi_3(E);
    origPi=Psi_3(pi), origUpper=Psi_7(delta), origJ=Psi_7(J).

For recovered-A, every completed theta term and their partial sums
are Psi_3 of Laurent homogeneous weight10 expressions with S exponent≥−1:
the raw pieces are S*theta³, (S*dp−U)*theta²,
(z−U*dp+S*vp)*theta and kp. Translating by S makes this ordinary
weight11. Earlier coefficient-only partials are Psi_1 of weight4
expressions, or Psi_2 of weight7 expressions with S exponent≥−1;
their ordinary translated weights are at most8. The intermediate
bracket products before their t shifts
are Psi_(8−ak−bl) of raw homogeneous degree26−3(ak+bl)≤23.
After shifting they share Psi_7 and raw degree23. Every partial
sum, product and comparison in these groups therefore has <20000 terms.

origResidual adds precisely two further support classes:

    Psi_7(J−delta) − 1 − Psi_2(U*theta).

U uses only Xi and has weight4, so its support is bounded by412 already.
Thus even before cancellation this union has <20000+1+412<21000 terms.
For low1/low0 comparisons, coefficient extraction leaves a single
common Psi_6/Psi_7 image of the raw coefficient class, with at most
origu or1 added at i=0. Subtracting wanted does not double the
support-envelope size: both operands lie in those SAME coordinate
classes. The guard product and its intermediate scalar monomials each
have at most one term. This covers all13 SCALE fields and six comparison
groups, including their arithmetic before anomaly checks.

The typed exponent guard is likewise not approached: raw exponents
are bounded by their degree≤23, graph Xi exponents by30, formal theta
by14, and the only auxiliary S shifts are down to−2. The displayed
SCALE reindex uses offsets≤7, doubles z exponents and retains theta;
even the loose absolute bound64 is below256. This is not a bound on
the number of simultaneous retained objects or their Python memory.

## 4. Graph Horner transients and all wire caps

At graph substitution the input is theta/S-free and homogeneous with
z weight7. At descending Horner index k, the partial polynomial after
addition has Xi weight w−7k. Multiplication by zeta of weight7 gives
the next exact weight; both summands lie in that same envelope.
All such weights are≤27. The guard product g and its independent
identity use weight30. Parser-admitted graph terms have those same
fixed weights even for a subsequently rejected candidate.

Consequently each of the30 polynomials has ≤412 possible terms,
strictly below20000; their aggregate is≤12360, strictly below400000.
Each exponent string has at most two digits because its weight≤30.
Each of at most seven field-coordinate strings has at most ten digits
because p<2^31. In canonical compact JSON a term occupies at most116
bytes, or117 allowing its separator. A64-byte allowance per polynomial,
plus the fixed graph container and two scalar vectors, gives
30*(412*117+64)+400=1448440<1450000 bytes.

ROOT's later administrative hint was independently checked against the
newly authorized authority.py, not accepted as another author's agreement.
Its load_pinned reads at most65537 bytes and rejects authority documents
above65536. The returned contract/source-vector/place data are copied
subobjects of that authority. Reencoding those disjoint subobjects with
ensure_ascii=True uses at most six times their raw authority byte budget,
plus a fixed small container allowance. Even the deliberately generous
bound 1450000+6*65536+4096 is below4MiB. Thus the complete genuine
canonical artifact cannot hit the128MiB encoded-object cap.

This is not permission to remove parser caps: arbitrary incoming bytes
can still be oversized or malformed and must refuse. Native loading,
whole-unit output aggregation, unrelated metadata/streams and every
runtime resource budget remain outside this polynomial-wire theorem.

## 5. Source boundary and remaining quantity

The result covers scalar-leading Poly objects, complete formal bands,
all forced upper/low diagnostics, Laurent-S auxiliaries, fixed installation,
Euler reconstruction, full bracket, all retained SCALE computations,
graph substitution and parser-admitted graph supports. Intermediate
cancellations or finite-place deletions were never assumed to reduce a
count. The removed alternative Laurent-q branch remains NOT_COMPUTED;
this proof would not automatically bound that different computation.

No source polynomial, fixture, matrix or coefficient payload was read or
generated. No code import, AST/syntax/compile/test, scientific subprocess,
external lookup or live ROOT report was used. Source bodies were read
as inert text; hash/diff-style metadata and the artifact transaction are
documentary only. The binding PINS file was read without following its
historical provenance links. A targeted root-box PINS.json lookup was
absent; no replacement corpus search was made.

Support/wire OPEN quantity: none identified for the stated retained
checker. Cheapest independent next check: one manual audit of this ledger,
especially the SCALE union classes and Horner transients; planning5–10min
is UNMEASURED, not an observed or authorized run. Whether a registered
good-place checker completes within CPU/RSS/wall limits remains entirely
UNMEASURED. This report grants no place admissibility, source-zero,
rank, Keller/JC2 or execution conclusion and changes no guard/source.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12358`.
- Body SHA-256:
  `7b40c1806d0cb0c71988869719a33eeb7e0f3babfb25394fa17e70f73729ce9d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
