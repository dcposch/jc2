# A section excludes nontrivial plane descent of the marked quartic invariants

Producer: swarmHQ ROOT (gpt-6-astra), September17,2026.
Basis: `582bf727e707799bb570dfe35a2fd5ec3b71b257`.
Claim: MARKED-QUARTIC-SECTION-1.
Evidence: MANUAL elementary ring algebra, with the accepted classical birational
Keller theorem for the final automorphism conclusion.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model hostile review.
Native Astra supplied a same-model manual co-check, not independent FIRST.
No literature novelty claim; JC2 remains unresolved.

## 1. Exact whole-source map and statement

Use the literal n=4 formula of the
[marked-root report](marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md),
on the WHOLE source with coordinate ring R=C[x,y,z3,z4]. In binary variables T,S put

    p=1+xy,  L=pT-xS,  V=S-yT,
    W=4y(yT+S/2)S+z3(pT+xS/2)S+z4 T^2,
    Phi=L V^3+L^2 W
       =A T^4+B T^3 S+C T^2 S^2+D T S^3+E S^4.

All five coefficients belong to the original polynomial ring R. In fact D=1:
the first summand contributes p+3xy=1+4xy and the second contributes
-4pxy+4x^2 y^2=-4xy. Define the explicit polynomial functions

    I=12AE-3BD+C^2,
    J=72ACE+9BCD-27AD^2-27B^2E-2C^3,
    u=-I/3,  v=-J/27,  q=(u,v): A4 -> A2.

Then C(u,v) is relatively algebraically closed in C(x,y,z3,z4).
Equivalently in this characteristic-zero finite-type setting, q has a
geometrically integral generic fiber. No assertion about every special fiber,
a global affine-space bundle, or a global inverse is made.

Consequently, if rho:A4 --> A2 is ANY dominant rational map and H:A2->A2
is polynomial with nonzero constant Jacobian, and the rational-map identity

    H composed rho = q

holds, then H is a polynomial automorphism. NO geometric-integrality assumption
on the generic fibers of rho is required. The same conclusion holds with (I,J)
in place of q, since their target coordinates differ by an invertible linear map.

This excludes nontrivial plane Keller descent through this FIXED invariant map
of the original four-variable source. It does not exclude arbitrary maps
A2->A4, other projections, other target subfields, other donors or degrees.

## 2. The section and normality proof

At x=y=0, p=1 and direct substitution gives

    Phi=T S^3+z3 T^3 S+z4 T^4,
    I=-3z3,  J=-27z4.

Therefore sigma(a,b)=(0,0,a,b) is a polynomial section of q. In particular
u,v are algebraically independent. With A0=C[u,v], the inclusion A0->R
has an A0-algebra retraction epsilon:R->A0 supplied by that section.
This remains true at a=b=0 and uses no discriminant localization.

Here is the general elementary lemma used. Suppose A0 is an integral ring,
R is a normal integral ring containing A0, and R->A0 is an A0-algebra
retraction. Let K=Frac(A0), M=Frac(R), and R_K=(A0\{0})^(-1)R.
Then K is relatively algebraically closed in M.

Indeed R_K is normal, has fraction field M, and the retraction extends to
a K-algebra map epsilon_K:R_K->K. If alpha in M is algebraic over K,
its monic polynomial over K also has coefficients in R_K. Normality implies
alpha belongs to R_K. The same argument puts alpha^(-1) in R_K when
alpha is nonzero. Thus the relative algebraic closure is a field contained
in R_K, and epsilon_K restricts to a K-field homomorphism from it to K.
For any alpha in that field, alpha-epsilon_K(alpha) cannot be nonzero:
it would be invertible in R_K but have image zero. Hence alpha belongs to K.

Our R is a polynomial ring, hence normal. This proves the stated relative
closure on the whole original source. Characteristic zero supplies separability,
so the generic fiber is geometrically integral. This last standard equivalence
is not needed for the construction exclusion below.

## 3. Descent exclusion and the undefined-section trap

Write rho=(r,s), with r,s in M and algebraically independent by dominance.
The identity H composed rho=q gives inclusions of fields

    K=C(u,v) subset N=C(r,s) subset M.

Since H has nonzero Jacobian, it is dominant and generically finite; equivalently
N/K is finite algebraic. The relative-closure result forces N=K. The isomorphism
C(X,Y)->N sending X,Y to r,s identifies C(H1,H2) with K, so H is birational.
The classical birational Keller theorem, already an accepted campaign import,
then makes H a polynomial automorphism. No general JC2 assertion is used.

One must NOT prove this by composing rho with sigma: rho may be undefined
along the entire section. The localization/normality argument instead shows
that all algebraic intermediate-field elements, and their nonzero inverses,
extend to R_K and can be evaluated there. This is the load-bearing step.

## 4. Controls, comparison and exact limits

- Normality matters to the lemma. The domain
  C[t,a,b]/(a^2-t b^2) has the section a=b=0 over C[t], but its fraction
  field contains a/b, a square root of t not in C(t). This ring is not normal:
  a/b is integral and not in the ring. For instance its degree-zero part under
  deg(a)=deg(b)=1 is C[t], whereas a/b is not in C[t]. The polynomial
  a^2-t b^2 is irreducible, and t is not a square in C(t).
- A normal source alone is insufficient: C[x^2] inside C[x,y] has the
  nontrivial algebraic element x in the larger fraction field. There is no
  polynomial section of the map (x,y)->x^2 over the whole affine line.
- The explicit section works at the repeated-root quartic T S^3. No removed
  discriminant or x!=0 chart is hidden in this argument.
- The [linear/cubic SL2 quotient report](linear-cubic-sl2-quotient-swarmHQ-root-20260916T174200Z.md)
  and [Sol review](linear-cubic-sl2-review-swarmHQ-sol-20260916T174500Z.md)
  normalize a DIFFERENT source, the resultant-one factorization variety.
  They motivate this target choice but do not automatically transfer a
  generic-fiber statement to the original A4. The section supplies that
  missing whole-source attachment. Their invariant-ring classification,
  the upstream map's Jacobian/degree and its external fiber assertions are
  not dependencies of this proof. The displayed polynomials suffice.
- The old fixed-high-coefficient slice classification is a different test.
  This result fixes a target field and permits arbitrary compatible rational
  source quotients; it does not assume a plane component of an old slice.
  It does not give a construction or rule out unrelated plane Keller maps.

Decision: no parameter, degree, projection or generic-rationality family is
commissioned. The elementary section test closes this one proposed quotient
route, subject to different-model review; stronger parametrization is unnecessary.

Input SHA-256 values were checked before and after the manual co-check:

- Marked-root producer: `a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5`.
- Linear/cubic producer: `f5781c10bbc848ef39b140312b8f0d8e3871a6df0cd1f4208f661566fc4fa593`.
- Its Sol review: `63d08b15fc3fee4a9a5e5f23a7c2f7739c41e0bb6cd2d8d20083903b3b70bb0c`.
- FALLACY-v2: `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`.

No CAS, scientific Python, numerical experiment, primes, seeds, worker, or
degree cutoff was used. There is no new exit-price assertion. Integrity tools
check custody, not the algebra. No literature-priority finding is asserted.

## COLLISIONS

status: EMPTY

- NONE -- no explicitly raised OPEN entry or automatic successor.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7373`.
- Body SHA-256:
  `254fffaa6d83774bdff6f5e0f5dd4437c918de26f886f53d03ef1234f74a4206`.
- Frozen basis: `582bf727e707799bb570dfe35a2fd5ec3b71b257`.
