# Two-bad-fiber pullback with independent numerator and denominator

Status: MANUAL / PRODUCER-CHECKED / UNPROMOTED; independent FIRST pending.
Author: swarmHQ ROOT, 2026-10-20. JC2 remains unresolved.
Frozen basis: 965ab03b37e0a1843581188d8f29c616e205b17e.
External novelty UNKNOWN. No machine proof or new source audit is claimed.

## Statement

Let F=(P,Q):A2_C -> A2_C be a polynomial Keller map. Identify
K=C(u,v) with its image in L=C(x,y) under F*. Let a,b in C[u,v]
be coprime and algebraically independent, and put f=a/b.
Assume C(f) is relatively algebraically closed in K.

For lambda in C take the affine fiber divisor div(a-lambda*b);
for lambda=infinity take div(b). Empty divisors count as reduced.
Assume at most TWO of these divisors are nonreduced. Then
C(f) is relatively algebraically closed in L: Keller pullback preserves
primitivity of this rational pencil. Affine basepoints are allowed.
No rational-generic-fiber or basepoint-free hypothesis is imposed.

The independent-numerator/denominator hypothesis is essential to THIS proof.
The statement does not cover arbitrary primitive polynomial functions.
It asserts neither genus zero nor finite-normalization equality B=R.

## 1. Pullback preserves coprimality and divisor multiplicities

F is dominant, etale and quasi-finite. The target base locus V(a,b) is
finite. A common source prime factor of a(P,Q),b(P,Q) would define a curve
mapped into that finite set, contradicting quasi-finiteness. Thus the
two pulled-back polynomials remain coprime. They remain algebraically
independent because F is dominant.

Etaleness preserves the multiplicity of a target prime at every source
prime dominating it. Every target prime divisor D is dominated by at
least one source prime: its irreducible defining polynomial d has
nonconstant pullback d(P,Q), hence a curve of zeros; quasi-finiteness
prevents contracting any such curve to a point of D. In particular,
reduced affine fiber divisors stay reduced.

## 2. Independence excludes every divisor-empty intermediate fiber

Suppose a finite intermediate field E/C(f) lies inside L. It is the
function field of a curve rationally dominated by A2. Restricting to
a suitable line gives a nonconstant rational map P1 to its smooth
projective model; Riemann-Hurwitz makes that model rational. Hence
E=C(H) and f(P,Q)=R(H), where R is a rational function of degree
d=[E:C(f)]. These are the same classical curve imports used in ONEBAD.

Write H=c/e with coprime source polynomials c,e. If an affine fiber
of H at some P1 value were divisor-empty, a Mobius transformation
would make its generator polynomial: for an empty infinite fiber e
is constant; for an empty finite alpha fiber, c-alpha*e is a nonzero
constant and 1/(H-alpha) is polynomial.

Call that polynomial generator T and rewrite the same equality as

    a(P,Q)/b(P,Q) = U(T)/V(T),

where U,V in C[t] are coprime. Bezout in C[t] implies U(T),V(T)
are coprime in C[x,y]. Both sides are reduced fractions in this UFD,
so a(P,Q)=gamma*U(T) and b(P,Q)=gamma*V(T) for a nonzero constant gamma.
This contradicts their algebraic independence.

Therefore EVERY P1 fiber of H has an affine prime divisor component.
This argument concerns a divisor-empty fiber, not merely a missing point
at a basepoint. It does not assume that H is a globally defined morphism.

## 3. The intermediate rational map has at most two branch values

Let alpha be a ramification point of R, and put lambda=R(alpha).
Take a prime component C of the affine H=alpha divisor, which exists
by Section2. At its generic point H is defined, including when alpha
is infinity. The local multiplicity of the composite fiber is

    ord_C(f(P,Q)-lambda)
      = e_alpha(R) * ord_C(H-alpha)

in appropriate local parameters; use reciprocals for infinite values.
Both factors on the right are positive and e_alpha(R)>1.
Thus the corresponding pulled-back fiber is nonreduced. By Section1
this is impossible if the target affine fiber at lambda is reduced.

All ramification VALUES of R therefore belong to the set of at most
two bad target values. There is no extra omitted-fiber exception:
Section2 has removed it using independence, not a pure-power assumption.

## 4. Cyclicity and descent of a power

If d>1, enlarge that branch-value set to two distinct P1 values
lambda0,lambda1 if necessary. Let k_i be the number of distinct
points over lambda_i. Riemann-Hurwitz gives

    2d-2 = (d-k_0)+(d-k_1),   hence k_0+k_1=2.

Thus each k_i=1. Both fibers are totally ramified, and
R=M composed with (z^d) composed with N for Mobius maps M,N.
Constants can be absorbed over C. Consequently M^(-1)(f(P,Q))
is a dth power in L.

Every target prime is hit with ramification index one by Section1.
All its valuations on M^(-1)(f) are therefore divisible by d.
Unique factorization in C[u,v], including negative exponents for a
rational function, and dth roots of nonzero complex constants give
M^(-1)(f)=h^d for some h in K.
Since f is nonconstant, C(h)/C(f) has degree d. This contradicts
target primitivity. Hence d=1 and the claimed relative algebraic
closedness follows.

## Relation, construction consequence and limits

[ONEBAD](one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md)
allows at most one bad fiber without numerator/denominator independence.
The present statement allows two but adds independence; it does not
replace ONEBAD's polynomial or dependent-numerator cases.
[BIN1128](binomial-pencil-primitivity-review-swarmHQ-sol56-root-20261020T115104Z.md)
is the special case f=u^m/v^n, gcd(m,n)=1. Its two reduced-fraction
polynomials are independent, its only potentially nonreduced affine
fiber divisors are at0 and infinity, and its monomial character is primitive.
No claim of a previously unrecorded or externally novel proof is needed.

For any target f satisfying this statement, a dominant rational donor D
with f composed D=R(H), deg R>1, cannot undergo a dominant rational SOURCE
substitution retaining these target functions and become polynomial Keller.
The embedded proper algebraic subextension survives, contradicting the theorem.
This includes a finite source-field enlargement if the resulting source
is a rational plane. Arbitrary birational TARGET changes are not covered.

No such f or compositeness relation is supplied for an arbitrary hypothetical
Keller counterexample. The normalization/boundary-to-pencil existence gap
remains open. No surjectivity, degree bound, counterexample or JC2 proof follows.
The bounded public/HQ history gate found related homogeneous/moving-pencil
work, not an exhaustive novelty certificate. Those older results are not
imported into this proof. No control family or automatic successor is proposed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6726`.
- Body SHA-256:
  `9aef4f6a0dda76ea7e55f2fcf21d92bfa5171ca1891f815f7ae1bdefa88dca28`.
- Frozen basis: `965ab03b37e0a1843581188d8f29c616e205b17e`.
