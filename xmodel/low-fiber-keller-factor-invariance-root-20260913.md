# Low-fiber postcomposition preserves polynomial Keller right factors

ROOT, September13 2026. MANUAL / PRODUCER-CHECKED, pending different-model
FIRST. JC2 remains unresolved. This is a theorem-interface composition of
the accepted small-second-leg argument, not a reproof of those exclusions.

## Exact claim and changed test

Let j:A2_C->A^{n0}_C be polynomial with two-dimensional image closure.
Let phi_r:A^{n(r-1)}->A^{nr}, r=1,...,m, be polynomial maps. Put j_0=j,
j_r=phi_r j_(r-1), and Z_r=closure(j_r(A2)) with its reduced structure.
Assume each Z_r has dimension2 and each induced dominant map
Z_(r-1)->Z_r has function-field degree at most3. These are degrees on the
ACTUAL image closures, not generic degrees in the ambient spaces.

For any plane polynomial Keller map h=(f,g), the following are equivalent:

    j_m = i h for some polynomial i:A2->A^{nm};
    j   = i_0 h for some polynomial i_0:A2->A^{n0}.

In the first case i_0 is unique and i=phi_m ... phi_1 i_0. Thus
postcomposition by this whole chain creates NO NEW polynomial Keller right
factor. There is NO bound on the generic degree of j and NO iterate-count,
ordinary-degree or coefficient bound.

This does NOT prove that h is invertible for arbitrary j. It says that a
prospective Keller factor must already be a polynomial right factor of j.
In particular h IS invertible if j is finite, or if the coordinate algebra
C[j_1,...,j_n0] contains a polynomial source coordinate. These corollaries
include high-degree noninjective parametrizations outside the earlier
degree-at-most-three source statement.

The changed construction test is on the INITIAL parametrization, before
applying or iterating an ambient counterexample: discard finite j and
coordinate-containing j; for another j, seek its Keller right factor
directly. This is an exact factor-set equality, not a claim that every
factor-finding algorithm is equally fast or that arbitrary projections are
covered. No new parametrization farm is proposed.

## Accepted dependencies, consumed without reproof

Use the same complex-plane premises as the accepted
[LOW-FIBER-TOWER-TRANSFER-1 FIRST](low-fiber-tower-transfer-gate-sol-20260913.md):

1. Keller mapping degree2 or3 is excluded (the campaign has a stronger
   accepted bound, but does not need it here).
2. For an actual Keller field K=C(f,g) inside L=C(x,y), no strict proper
   intermediate K<M<L has [M:K]=2 or3. This is the SECOND leg, not [L:M].
3. Birational Keller maps are automorphisms.

The strict cubic-block addendum and the named external tiers of those
premises remain binding. This report does not extend their degree range or
review their proofs. Basic finite/proper Keller automorphy is used in one
corollary. The elementary intersection argument below is supplied in full
to make the field-to-polynomial descent explicit.

## 1. Stop the compositum tower at the initial image field

Embed all image fields into L by pullback and write E_r=C(Z_r). They form

    L >= E_0 >= E_1 >= ... >= E_m,
    [E_(r-1):E_r]<=3 for r=1,...,m.

The full factorization j_m=i h gives E_m subset K. It does not require i
to be birational onto its image. Put M_r=K E_r inside L, so M_m=K.
Scalar extension of the finite E_r-vector space E_(r-1), followed by its
multiplication image in L, gives

    [M_(r-1):M_r] <= [E_(r-1):E_r] <=3.

The image is a finite-dimensional domain over M_r, hence a field, and is
precisely M_(r-1). This is an inequality, NOT degree divisibility.

If M_0>K, take the last strict drop. Its lower field is K and its upper
field M has degree2 or3 over K. If M=L, premise1 applies. If K<M<L,
premise2 applies. Either case is impossible. Hence M_0=K and E_0 subset K.

Unlike the earlier theorem, this argument never puts the possibly large
extension L/E_0 into the small-degree tower. It concludes containment of
E_0 in K, not L=K. That distinction is the point of the extension.

## 2. Field containment becomes polynomial factorization

For a dominant quasi-finite polynomial F=(f,g):A2->A2, set R=C[x,y] and
A=C[f,g]. Then

    R intersect Frac(A) = A.

Indeed, write a rational target function as a(U,V)/b(U,V) with a,b coprime.
If b is nonconstant, choose an irreducible p dividing b. Dominance implies
p(f,g) is a nonconstant polynomial. Let q be an irreducible factor of it
in R, and let C=V(q). Quasi-finiteness prevents the curve C from mapping
to one point, so its image is dense in the irreducible target curve V(p).
Since p does not divide a, a(f,g) does not vanish identically on C. Thus q
divides b(f,g) but not a(f,g), making the quotient nonpolynomial in the UFD
R. Contradiction. Therefore b is constant. The reverse containment is clear.

A Keller map is dominant and quasi-finite, so this applies to h. Each
coordinate of j belongs both to R and to E_0 subset K. Consequently it is
a polynomial in f,g. These polynomials define i_0 and give j=i_0 h.
Dominance of h proves uniqueness and also i=phi_m ... phi_1 i_0.
The reverse factorization implication follows simply by composition.

The quasi-finiteness requirement is real: F=(x,xy) contracts x=0, and
y=(xy)/x lies in R intersect C(x,xy) but not in C[x,xy]. Its Jacobian is
x, not a nonzero constant. This is a negative control, not a Keller map.

## 3. Two unbounded source exclusions

If j is finite and j=i_0 h, then h is proper: its graph is closed in
A2_source times_(A^{n0}) A2_target because i_0 is separated, and projection
to A2_target is the base change of the proper map j. Thus h is proper and
quasi-finite, hence finite. The accepted finite Keller automorphy result
applies. A proper affine morphism j would give the same corollary.

If D=C[j_1,...,j_n0] contains a polynomial source coordinate a, choose a
complementary coordinate b, so R=C[a,b]. Since D subset A by section2,
we have R=A[b]. The usual monogenic-unramified argument gives R=A: write
R=A[T]/(P) with P irreducible primitive of positive T-degree. The vanishing
of Omega_(R/A) makes P_T(f,g,b) a unit in R, hence a constant lambda!=0.
Then P divides P_T-lambda, impossible by T-degree unless P_T=lambda.
So P=lambda*T+P_0 and b belongs to A. This is the same elementary lemma
already used by the accepted two-polar criterion, not a new foundation.

For a concrete beyond-old-scope control, j(s,t)=(s,s*t^6,0) has generic
degree6 and a positive-dimensional fiber at s=0. It is not finite, but its
coordinate algebra contains s. The second corollary therefore excludes
nonautomorphic Keller right factors after every chain in the theorem.
This example is not a Keller map and asserts no new degree bound for JC2.

## 4. Application and hard scope boundaries

The accepted EMBEDDED-PLANE-TRANSFER-1 FIRST proves that every point fiber
of the named three-dimensional core G has at most three points, including
exceptional targets. Identity stabilizations and polynomial conjugations
preserve that property. Restricting such a map to an actual image closure
is quasi-finite; over C its generic geometric fiber has as many distinct
points as its function-field degree. Thus every restricted step has degree
at most three, and the present theorem applies to any finite composition
of those maps. No bound on the full iterate's fiber count is required.

The Long four-dimensional application remains conditional on the previously
accepted explicit polynomial source-coordinate factorization in the cited
FIRST. This is not a fresh primary-source or symplectic audit.

An ambient GENERIC degree bound alone is insufficient. The old control
phi(a,b,c,d)=(a,ab,c,d) is generically birational, but its restriction to
j(s,t)=(0,s,s^4,t) is (0,0,s^4,t), of degree four. The exceptional ambient
fibers are infinite. This step is deliberately outside the theorem.
Likewise h=pi j_m, an arbitrary projection, gives K subset E_m, reversing
the needed inclusion. Actual restricted steps of degree at least four,
maps without the full polynomial factorization, and general initial
parametrizations without an independent Keller-factor exclusion remain
outside the conclusion.

## 5. Priority, provenance and review contract

The scoped canonical/report history search found no exact prior
Keller-right-factor-invariance statement. Its mechanism is nevertheless a
direct composition of the accepted tower argument with the elementary
intersection lemma. No literature novelty or global JC2 closure is claimed.

This is a targeted theorem-interface micro-round: it changes the test for
one construction family, not the global ranking or current all-degree
closing gaps. One different-model Fable FIRST is selected before promotion;
no speculative descendants, scientific computation, AWS worker, source
degree farm or instrument change is selected. Review should attack the
unbounded initial degree, the last strict drop, polynomial descent, both
source corollaries, and the distinction between factorization and projection.

Frozen basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.
Consumed reports were read WHOLE; exact SHA-256 pins:

- low-fiber-tower-transfer-gate-sol-20260913.md:
  63e69b73ced5f3b5026632f4c6e70c70a83daaa90ae39d6e1da3f4688b6418d5.
- embedded-plane-transfer-gate-sol-20260913.md:
  12799476c027a8b8d96c6e153c62471e5579d6303da6c1b90f09fda431838b29.
- Historical two-polar CLAIM.md (producer header superseded by accepted
  FIRST in the canonical record):
  3576962bed4195916367c80cb57b60d6041fc7766395f55a9ca59d8031627386.

Current policy SHA77ec0b282f4813ee9a2b71ebced492cc6f0b9262acf90a28f444ed9a507190bd;
APP061485540b27f8523ee3abf8e68f395c4559be12768f663f92cc7c4603316e01;
AUDITbc5d9c81b81de8276f886661034acf2beb6a7a1f034ce01562a10cb18032d821.
Manual mathematics and inert text/hash operations only. No new OPEN ID,
scientific execution, publication or external contact. The complete body
is read back and input pins checked before the completion marker is added.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9855`.
- Body SHA-256:
  `2537b3a5fd6e8cee32af1a9abfafeb5bd3bae85dea298110474a76759d9cfa2b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
