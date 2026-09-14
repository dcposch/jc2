# Low-fiber towers cannot transfer a counterexample to the plane

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
A composition of accepted inputs with a field-base-change argument, not a
new quadratic/cubic block theorem or a resolution of JC2.

## Exact field statement

Let h=(f,g):A2_C->A2_C be polynomial with nonzero constant Jacobian.
Regard K=C(f,g) as a subfield of L=C(x,y). Suppose there is a finite tower

    L=E_0 >= E_1 >= ... >= E_m,
    E_m contained in K,        [E_(r-1):E_r] <= 3 for every r.

Equal adjacent fields are allowed. Then h is an automorphism.
No bound on m, [L:E_m], or the ordinary polynomial degrees is imposed.
The bottom field need not equal K. This last point permits a nonbirational
target parametrization in the geometric application below.

Accepted campaign premises, consumed without reproof:

1. A complex plane Keller map of geometric mapping degree <=3 is an
   automorphism (the accepted quadratic/cubic and birational cases).
2. For a nonautomorphic plane Keller map there is no strict intermediate
   K < M < L with [M:K]=2 (BD-D2).
3. The same exclusion holds for [M:K]=3 (strict cubic second-leg closure,
   with its binding Fable addendum).

Premises2 and3 concern the SECOND leg [M:K], not [L:M]. They apply to
arbitrary strict intermediate fields of the actual Keller extension.
All their recorded external and internal proof dependencies remain trusted
at the existing accepted tiers. No smoothness or properness of a newly
constructed intermediate image surface is assumed here.

## Proof: first align the tower with the actual target field

Form composita INSIDE L:

    M_r=K E_r.

Then M_0=L and M_m=K. Every adjacent degree is at most three. Indeed,
the multiplication map from

    E_(r-1) tensor_(E_r) M_r

onto its image in L has an image that is a finite-dimensional domain over
M_r, hence a field. That image is exactly K E_(r-1)=M_(r-1).
Its dimension is at most [E_(r-1):E_r]. Thus

    [M_(r-1):M_r] <= [E_(r-1):E_r] <=3.

Only an inequality is asserted; the new degree need not divide the old one.
No linear-disjointness, Galoisness or primitive-element choice is required.

If L!=K, let r be the LAST strict drop in the M tower. All later fields
equal K, so M_r=K and [M_(r-1):K] is2 or3. If M_(r-1)=L, premise1
already contradicts nonautomorphy. Otherwise M_(r-1) is a strict
intermediate field excluded by premise2 or3. Consequently L=K, and the
accepted birational Keller case gives the claimed polynomial automorphism.

## Geometric transfer, including arbitrary finite compositions

Let V_0,...,V_m be complex affine varieties and let phi_r:V_(r-1)->V_r
be morphisms with at most three points in EVERY point fiber. Let

    j:A2->V_0,       i:A2->V_m,
    phi_m ... phi_1 j = i h.                         (1)

Assume j has two-dimensional image and is generically finite of degree at
most three onto its image closure. In particular any polynomial embedding,
point-injective polynomial map, or birational parametrization is allowed.
No point-injectivity, birationality or degree bound is imposed on i.

Put j_r=phi_r ... phi_1 j and Z_r=closure(j_r(A2)), with reduced structure.
Each Z_r is integral. The fiber bound makes each restricted map
Z_(r-1)->Z_r quasi-finite, so dimensions stay two and each is dominant
generically finite of degree <=3. In characteristic zero its generic
geometric fiber consists of that many distinct points, which are a subset
of a fiber of phi_r. Take their function fields as subfields of L through
the pullbacks of j_r. They give a tower

    L >= C(Z_0) >= C(Z_1) >= ... >= C(Z_m)

whose first step has degree <=3 by the assumption on j and whose remaining
steps have degree <=3 by the EVERY-fiber bound. Equation(1) gives
C(Z_m) contained in K. It does not generally give equality, but the
compositum proof above was designed for precisely this distinction.
The field statement now proves h an automorphism.

The same argument needs only degree <=3 for the restrictions to the actual
image closures. The ambient EVERY-fiber bound is a sufficient, independently
available way to establish it; an ambient GENERIC degree bound is not enough.
The intermediate morphisms are not assumed finite or etale, and their images
are not assumed normal, smooth, closed copies of A2, or surjective onto V_r.

## Application to the explicit 3D core and its stabilizations

EMBEDDED-PLANE-TRANSFER-1 already proves that EVERY fiber of the explicit
3D core G has <=3 points, and this survives identity stabilization and
polynomial source/target automorphisms. Therefore any finite composition
of such ambient maps satisfies the tower hypotheses one step at a time.
Every iterate G^m is covered without estimating its fibers by 3^m or
asserting its geometric degree is 3^m. The same holds in any fixed larger
dimension after stabilization, including arbitrary intervening polynomial
automorphisms.

Under full factorization(1), no embedded source plane can therefore produce
a plane Keller counterexample from ANY such finite composition. The source
can even have generic degree2 or3, as specified above. Long's four-variable
application remains conditional on the exact polynomial source-coordinate
factorization in the accepted prior report; no additional symplectic theorem
or ambient source program is imported or rechecked here.

This closes the previously named ITERATION escape from the single-step
three-point counting test, by a different accepted field-block mechanism.
It does not require the unreviewed first-canonical-pair units argument.

## Controls and boundaries

- Degree DROP control: alpha^3=2, zeta a primitive cube root of unity,
  L0=Q(alpha,zeta), E=Q(alpha), K0=Q(zeta*alpha). The tower
  L0/E/Q has degrees2,3, while K0 E=L0 and [L0:K0]=2. Thus the cubic
  step can become quadratic under compositum; replacing the inequality by
  divisibility would be incorrect. This tests the elementary field lemma,
  not the complex Keller premises.
- Generic-versus-EVERY-fiber control: on A4, let
  phi(a,b,c,d)=(a,ab,c,d), j(s,t)=(0,s,s^4,t), and i(u,v)=(0,0,u,v).
  The ambient phi is birational, but phi j=i(s^4,t), and its restriction
  to the embedded source has geometric degree4. Its exceptional ambient
  fibers are positive-dimensional. The plane map here is NOT Keller;
  the example refutes only the false restriction-degree inference.
- An arbitrary output projection h=pi phi_m ... phi_1 j does NOT imply(1):
  it yields K contained in C(Z_m), the opposite inclusion to the one used.
  No arbitrary-projection exclusion is asserted.
- No result for unrestricted high-degree source parametrizations, steps
  of degree>=4, or every integer degree of the form2^a3^b is asserted.
  A numerical factorization of a degree supplies no intermediate field
  tower. Solvability of a Galois closure is not substituted for this tower.
- Identity/automorphism chains satisfy all hypotheses and the conclusion.
  Repetitions/equalities in the field tower and a nonbirational i are
  explicitly handled; the empty tower with E_0 contained in K has L=K.

## Provenance, read scope and stop

ROOT read the WHOLE three binding block records and the prior embedded-plane
producer; current strategy and selected canonical history searches preceded
this composition. Scoped searches are not an exhaustive novelty audit.
The elementary field lemma is standard; the claimed campaign delta is its
actual Keller/block attachment to arbitrary finite ambient compositions.

- BD-D2 integration f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8.
- Cubic binding integration c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85.
- Cubic binding addendum b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419.
- Prior embedded-plane FIRST12799476c027a8b8d96c6e153c62471e5579d6303da6c1b90f09fda431838b29.
- APPfc0946a8447e9396863dc0739256b21f4a38c375b6ec03e2dc0a93b58c8966df;
  COORD517fca6f67f3d705f9b4045e10f9039aaf11bf3280dfd27bb90bf003ee4a3ead.

Only manual mathematics; no CAS/interpreter/scientific test, worker or source
execution. One different-model FIRST is required before promotion. No
coefficient search, iterate-by-iterate farm, extension to arbitrary projections,
or automatic successor is selected. The full JC2 objective remains open.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8314`.
- Body SHA-256:
  `94b257a818e2abef0df39df82860a959486aa61ffe377bacaeb6b87cbc14c324`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
