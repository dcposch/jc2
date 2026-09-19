# A dominant reduced polynomial pencil forces normalized Keller invertibility

Producer: swarmHQ ROOT (Astra); same-model native co-check, not FIRST.
Date: September 19, 2026 UTC.
Basis: 48faaca89be082590151a4a545095fb4a4fff610.
Evidence tier: MANUAL, with the accepted named dynamical import.
Lifecycle: PROVISIONAL, pending different-model hostile review.

## Exact statement

Let F:C^2 -> C^2 be polynomial with det DF=c constant, 0<|c|<=1.
Let a,b in C[x,y] be coprime and ALGEBRAICALLY INDEPENDENT. Put r=a/b.
If r composed with F equals phi composed with r for a rational self-map
phi of P^1 of degree d>=1, then d=1 and the generic mapping degree N(F)=1.
Consequently F is an automorphism by the inherited birational Keller theorem.

This neither supplies a preserved pencil nor treats algebraically dependent
reduced a,b, in particular any polynomial r with denominator 1. It does not
extend to |c|>1 by an unproved normalization argument and does not resolve JC2.

## Dependencies and comparison

The accepted [Keller dynamical inequality](keller-dynamical-degree-swarmHQ-root-20260914.md)
gives N(F)<=lambda_1(F)=lim deg(F^n)^(1/n) for precisely 0<|c|<=1.
Its [different-model review](keller-dynamical-degree-gate-fable51-20260914.md)
and [binding ledger scope](../AUDIT.md#keller-dynamical-degree-1--2026-09-14)
retain the Dinh--Nguyen--Truong arXiv:1303.5992v1 Theorem 1.1 and equilibrium
measure import. The compactly supported affine bump correction in AUDIT
applies. No fresh audit of that theorem, Lyapunov alternative, or new
generically finite dynamical-semiconjugacy theorem is used here.

Imported report SHA256 values, respectively:
b492c9ca68c73e420aedf3169e94e24b673ad9bcf8df572c4e5e662dd9eeb432;
0ee9edc9b00b97c1f11b9c22d5778496dad4d8d8b9be2d761d7f07d0709234b4.
Both reports were read whole; binding AUDIT lines22558--22598 were read.
The birational Keller endpoint is inherited standard campaign background,
not a new proof or computation.

The [older fixed-invariant discussion](../notes.md#2026-09-14-0652-utc----poisson-field-applicability-and-rational-gauge)
at frozen notes.md lines45468--45529 assumes rF=r before placing numerator
and denominator in iterated images. Internal same-day degree-one screening
already observes field-degree cancellation for dominant H=(a,b) and a Mobius
base. The change here is to arbitrary base degree, using the elementary
growth bound below to compare N=d^2 against lambda_1<=d. Targeted public and
operational history comparisons did not find this exact composition; one
search overgenerated and clipped. This is NOT an exhaustive priority or
literature-novelty determination. No inaccessible source was retried.

## Proof

### 1. A constant-factor homogeneous lift

Write phi=[A_d(U,V):B_d(U,V)] where the two degree-d homogeneous binary
forms have no common projective zero. Since F has nowhere vanishing
Jacobian, it is etale and quasi-finite. The common zero locus of coprime
a,b is finite or empty. An irreducible curve dividing both a(F),b(F)
would map into that finite locus, contrary to quasi-finiteness. Thus
gcd(a(F),b(F))=1.

The common affine zero locus of A_d,B_d is the origin. Hence powers of
U and V belong to (A_d,B_d). After substituting (a,b), any prime dividing
both substituted forms divides a and b, impossible. Therefore
gcd(A_d(a,b),B_d(a,b))=1. Algebraic independence ensures the substituted
forms are nonzero. Equality of the two reduced fractions in the UFD
C[x,y] gives one common unit k in C*, not a nonconstant factor:

    a(F)=k A_d(a,b),    b(F)=k B_d(a,b).

Define H=(a,b) and G=k(A_d,B_d). Then H F = G H.

### 2. Generic degree is the square of the base degree

H is dominant and generically finite. G is a finite homogeneous map:
on the unit sphere its two components have no common zero, giving
||G(z)||>=epsilon ||z||^d and properness; its fibers are finite.
A generic nonzero target direction has d distinct inverse directions
under phi, each with d distinct radial roots. Thus N(G)=d^2.
Generic degrees multiply for dominant generically finite maps, even
when H or F is not finite. From H F=G H we obtain

    N(H) N(F)=d^2 N(H),    hence N(F)=d^2.

### 3. An elementary upper bound on iterate degrees

Because C(x,y)/C(a,b) is finite, clearing denominators gives fixed
polynomial relations

    sum_(i=0)^s c_i(a,b) x^i=0,    c_i in C[U,V], c_s!=0,

and similarly for y. No monic relation or integrality is assumed.
Iterating the semiconjugacy gives H F^n=G^n H. For X_n=(F^n)_1,

    sum_(i=0)^s c_i(G^n H) X_n^i=0.

Each coefficient has total degree at most C d^n for a fixed positive
constant C, enlarged to work for both coordinate relations. This uses
deg(G^n)<=d^n and fixed H and c_i. Dominance keeps the leading coefficient
nonzero. If t=deg X_n>C d^n, the term of index s has degree at least st,
while each lower term has degree at most C d^n+(s-1)t<st. A unique term
of largest total degree cannot cancel. Therefore deg X_n<=C d^n, and
the same argument holds for the other coordinate. Consequently

    deg(F^n)<=C d^n,    lambda_1(F)<=d.

This proof uses algebraicity, not finiteness of H or a dynamical
semiconjugacy invariance theorem.

### 4. Apply the accepted inequality to the same map F

The determinant hypothesis is exactly the accepted inequality's scope:

    d^2=N(F)<=lambda_1(F)<=d.

Since d is a positive integer, d=1 and N(F)=1, proving the statement.
No target rescaling or independent coordinate change is inserted.

## Desk-only checks and limitations

- Identity F, a=x,b=y,phi=id satisfies the assumptions and gives d=N=1.
- The already recorded non-Keller control F=(x^2,y^2), a=x,b=y gives
  d=2,N=4,lambda_1=2. The first three steps hold; det DF=4xy fails
  exactly the constant-Jacobian hypothesis needed in step4.
- Multiplying a reduced pair by a common factor cannot manufacture the
  required independent H: the pair is required to be coprime.
- Every polynomial r represented in reduced form has constant denominator
  and is outside this proof. No claim about that excluded case is refuted.
- One-sided normalization of |c|>1 may destroy the pencil relation and
  degree-growth data; it is not an extension of this theorem.
- Same-model native manual co-check confirmed all four steps. It is not
  independent FIRST. The next test is a bounded different-model attack
  on these exact frozen steps, not a new pencil/invariant/control family.
- No existence theorem, general classification, properness proof for
  arbitrary Keller maps, counterexample, or global JC2 conclusion follows.

## OPENS RAISED

None. The missing universal source implication is unchanged; no descendant
or new source-acquisition task is selected.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

This checks explicit open-item collisions, not literature novelty.

Author readback complete, clock measured 2026-09-19 17:55:53 UTC.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6931`.
- Body SHA-256:
  `de16cbf46e28e0fcc7f59cc60733acec01f68248a33399cd948f355f220abd60`.
- Frozen basis: `48faaca89be082590151a4a545095fb4a4fff610`.
