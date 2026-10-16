# A nonsingular genus-two scalar polynomial in the marked carrier ring

Claim ID: CARRIER-GENUS2-SUBMERSION-1.
Author: swarmHQ ROOT, 2026-10-16. Tier: MANUAL / UNPROMOTED pending independent review.
Basis: 8926458541ce2ed2bb8729223f2478c5c81fd24a.
No computation, external theorem import beyond elementary curve theory, or novelty assertion.

## 1. Exact claims and relevance

Work over C. Put R=C[U,V], c=UV^2, p=UV^3-V and
B=C[U,UV,c,p], the marked carrier subring of R. Define

    f = p^4 + (1/3-3c)*p^2 + 3c^2 - 2c - 1 - U.

Then:
1. f belongs to B and has no critical point anywhere on A^2_(U,V).
2. Its geometric generic fibre is an integral curve of genus two.
3. There is no rational q in C(U,V) with J_(U,V)(f,q)=kappa for any nonzero constant kappa.

Thus nonsingularity of a scalar polynomial in THIS B does not force rational
generic fibres. This is one fixed obstruction to that proposed strategy, not a
classification of submersions or of Jacobian pairs in B. It is NOT a Keller pair,
a counterexample to JC2, or an exclusion of arbitrary pairs in B. Genus two by
itself does not exclude a Jacobian mate; claim3 uses the specific differential.

## 2. A rational coordinate chart and the polynomial identity

On the open subset V!=0, set

    g=1/V,   p=UV^3-V,   r=p-g.

These give an isomorphism onto the open subset p-r!=0 of the (r,p)-plane:

    g=p-r,   V=1/g,   U=g^2+g^3*p,   c=1+g*p.

Substitution into the displayed f gives, successively,

    f=p^4-3g*p^3+3g^2*p^2-g^3*p-(8/3)*p^2+4g*p-g^2
     =G(r,p):=p^2/3+r*(r^2-2)*p-r^2.

These are polynomial identities after the stated substitution. In particular
there is no reliance on smoothness or classification of an auxiliary surface.

## 3. No affine critical point

In the (r,p) chart,

    G_p=(2/3)*p+r^3-2r,       G_r=(3r^2-2)*p-2r.

If G_p=0, then p=3r-(3/2)*r^3. Substituting into G_r gives

    G_r=-(r/2)*(3r^2-4)^2.

The simultaneous zeros therefore have r=0 or r^2=4/3. In BOTH cases p=r,
so they lie outside p-r!=0. The chart contains no critical point of f.
On the remaining line V=0 one has c=p=0 and f=-1-U, so f_U=-1 there.
This covers the whole source plane and proves claim1.

## 4. Geometric generic fibre

Let t be transcendental over C and K=C(t). Set

    H=2p+3r*(r^2-2).

On f=t, the equation G=t becomes

    H^2=h_t(r):=9r^6-36r^4+48r^2+12t.                 (1)

The inverse is p=(H-3r*(r^2-2))/2 followed by the inverse chart in section2.
The removed locus p-r=0 intersects G=t in finitely many points, since there
G=r^4-(8/3)*r^2. The line V=0 meets f=t in the single point U=-1-t; it
cannot be an additional generic fibre component. Thus (1) is birational to
the entire generic fibre, not merely to an unspecified component.

Now h_t'(r)=6r*(3r^2-4)^2. At r=0 its value is12t; at r^2=4/3 its value
is64/3+12t. These are nonzero in K, so h_t is squarefree, also over an
algebraic closure of K. In particular it is not a square in that rational
function field, and (1) is geometrically integral. Its smooth projective
model C_t is the double cover of P^1_r branched at the six simple finite roots.
There are two unramified points at infinity, since the degree is6 and the
leading coefficient is9. Riemann--Hurwitz gives 2g-2=2*(-2)+6=2, hence g=2.

## 5. A specific differential excludes even a rational Jacobian mate

Directly from U=g^2+g^3*p and V=1/g,

    dU wedge dV=g*dg wedge dp=(r-p)*dr wedge dp.

Suppose J(f,q)=kappa!=0 with q rational. Then
df wedge dq=kappa*dU wedge dV. Restricting to the generic fibre, and using
G_p=H/3, gives

    dq=kappa*eta,       eta=3*(p-r)*dr/H
       =[3/2+(-9*r^3/2+6*r)/H]*dr.                 (2)

The sign follows as well by writing dq=(q_r-q_p*G_r/G_p)dr and comparing
G_r*q_p-G_p*q_r=kappa*(r-p). This calculation takes place in the function
field, so generic denominators do not discard any possible rational mate.

At every finite point of C_t, eta is regular: at a simple zero of h_t,
dr/H is regular in the local square-root parameter; elsewhere this is immediate.
At infinity use s=1/r and label the points by

    H=+/-3*r^3*(1-2/r^2+O(r^-4)).

The coefficient of dr in (2) is -r^-2+O(r^-4) on the plus branch and
3+r^-2+O(r^-4) on the minus branch. Since dr=-ds/s^2, eta is regular at
the plus point and has EXACTLY a double pole at the minus point. There are
no other poles, and eta is nonzero.

In characteristic zero, a pole of order m>=1 of a rational function produces
a pole of order m+1 in its differential. Hence a rational primitive of
kappa*eta would have exactly one pole, of order one. Such a nonconstant
function has degree one to P^1, making the smooth projective curve rational,
contrary to g=2. This proves claim3.

## 6. Limits

All conclusions concern the displayed scalar f only. No argument here excludes
other nonsingular scalar polynomials in B, all possible Keller pairs in B,
or a hypothetical plane Keller counterexample. The construction is related to
classical nonsingular-polynomial examples; external novelty is unasserted.
The purpose is to close a specific overly strong carrier-rationality implication,
without a degree search, source family, or renewed generic dual-construction lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5190`.
- Body SHA-256:
  `ca1f1bf20e621657e3bc47259fd4dc1b2c782cc7b1f29c27109b0b87ae93a6cd`.
- Frozen basis: `8926458541ce2ed2bb8729223f2478c5c81fd24a`.
