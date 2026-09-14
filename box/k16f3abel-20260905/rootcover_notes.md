# Exact ordered-root contacts for the all-b Abel equation

Subtask status: PARTIAL. These are universal characteristic-zero identities
and necessary conditions, not an all-t nonexistence proof. Source formulas
are (F1)--(F3) in the frozen
`/tmp/jc2-lane.zx9GKm/inputs/k16-8point1-astra-20260905.md`.
No live lane report or ledger was used.

## 1. Polynomial factorization retaining b and all root multiplicities

Work over an algebraically closed characteristic-zero field containing the
chosen factor of the normalizer. Let n=t-1 and N=t+1. Thus C is monic of
degree n and K=x^2 C-yb is monic of degree N. Put

    P=xW-b^2/4,
    H=2xP'-3P-Bx+3K(K+yb)/(2y^2),
    Q=K(K+2yb)-4By^2x,
    J=bK/(2y)+Bx,
    R=3K^2 Q/(16y^4)-eta x^2 J.

Equation (F3), with eta=W'(0), is exactly

    P H=R.                                                     (RC1)

In fact x^2 times the left side minus the right side of (F3) is PH-R.
No square root, root derivative, discriminant, or polynomial factor has
been inverted. The degree of P and H is 2t+2; their leading coefficients
are omega and (4t+1)omega+3/(2y^2), respectively. The leading relation
in (RC1) is precisely the banked normalizer equation, and is not an
additional obstruction.

The identity can also be written

    2xPP'=3P^2+[Bx-3K(K+yb)/(2y^2)]P
             +3K^3(K+2yb)/(16y^4)-3BxK^2/(4y^2)
             -eta x^2[bK/(2y)+Bx].

This transformation uses the linked A,D coefficients. A generic Abel
equation of the same degrees does not have its quartic K factorization.

## 2. Coprimality and a norm identity on the nonzero chart

Assume bB eta is nonzero. Since P(0)=-b^2/4 and K(0)=-yb, both P and K
are coprime to x. Reduction of (RC1) modulo K gives

    P H = -B eta x^3  in k[x]/(K).                            (RC2)

The right side is a unit in this finite algebra, even when K has multiple
roots. Consequently P and H are both units there:

    gcd(P,K)=gcd(H,K)=1.                                      (RC3)

Equivalently, a common root of P and K would be nonzero, and substituting
it into (RC1) would give 0=-B eta x^3. The Artin-algebra version shows
explicitly that this is not a reduced-root assumption.

Multiplicativity of resultants gives the stronger exact identity

    Res_x(K,P) Res_x(K,H) = -(B eta)^N (yb)^3.                 (RC4)

Indeed, Res(K,x)=(-1)^(N+1)yb, while K is monic; hence
Res(K,-B eta x^3)=(-B eta)^N Res(K,x)^3 has the displayed sign.
This identity is compatible with both roots of 3d^2=t+1. It does not force
either factor on the right to vanish.

There is a linked contact condition to the next order. Define

    E0=2xPP'-3P^2-BxP+B eta x^3.

Then (RC1) implies

    E0 = -bK(3P+eta x^2)/(2y)  modulo K^2.                   (RC5)

Thus, if alpha is a root of K of multiplicity m, E0 has multiplicity at
least m there. Its coefficient at order m is prescribed by the right
side of (RC5). If 3P(alpha)+eta alpha^2 is nonzero, its multiplicity is
exactly m. If that value vanishes, the contact increases; it cannot be
discarded. For a simple K root the derivative form is

    E0'(alpha)=-bK'(alpha)[3P(alpha)+eta alpha^2]/(2y).

Writing this only after assuming K' nonzero would discard repeated K
roots, whereas (RC5) is valid uniformly.

## 3. An intersection of length at most three with the ordered C roots

At C=0 one has K=-yb. Introduce the cubic

    Qc=16B eta x^3-8b^2 eta x^2+12Bb^2x+3b^4.

The full expansion of R in powers of C is

    R=3x^8 C^4/(16y^4)-3b x^6 C^3/(8y^3)
        -3B x^5 C^2/(4y^2)
        +b x^2(3b^2+12Bx-4eta x^2)C/(8y)-Qc/16.

Consequently every solution satisfies

    PH = -Qc/16  modulo C,                                  (RC6)
    PH+Qc/16 = b x^2(3b^2+12Bx-4eta x^2)C/(8y)
                    modulo C^2.                             (RC7)

Unlike the K-unit assertion, (RC6)--(RC7) do not require b nonzero. If
B eta is nonzero, Qc has degree exactly three. Therefore

    gcd(C,PH)=gcd(C,Qc),                                     (RC8)
    deg gcd(C,PH) <= 3.                                     (RC9)

In particular gcd(C,P) and gcd(C,H) each divide Qc and have degree at
most three. The bound includes intersection multiplicity. It is valid
at every t, rather than only when the C roots are distinct. It becomes
a restrictive intersection-length statement once t>=5, because then
deg C=t-1 is greater than three.

The corresponding exact norm identity is

    Res_x(C,P) Res_x(C,H)
      =(-1/16)^(t-1) Res_x(C,Qc).                            (RC10)

It allows common roots with C on the cubic exceptional locus. In
particular, gcd(P,C)=1 cannot be asserted on the entire bB eta nonzero
chart. Even removing gcd(C,PH) from C need not produce a polynomial
coprime to PH: a C root may have larger multiplicity than Qc at that root.

The cubic discriminant is

    Disc_x(Qc)=768 eta b^6
        [8eta^2 b^4-177B^2 eta b^2-144B^4].                  (RC11)

On the chart where it is nonzero, suppose alpha is a C root of
multiplicity m>=2 and PH(alpha)=0. Equation (RC8) then forces the total
multiplicity of alpha in PH to be exactly one. Hence exactly one of P,H
has a simple root there and the other is nonzero. If the discriminant
vanishes, Qc may have repeated roots and this conclusion must be replaced
by the exact valuation identity

    min(m, ord_alpha(P)+ord_alpha(H))
      =min(m, ord_alpha(Qc)).                                (RC12)

No discriminant-zero stratum is excluded by these statements.

## 4. A controlled exceptional denominator

One possible next step is to divide (RC1) by x^2J and view eta as a
constant value of the rational map

    3K^2[K(K+2yb)-4By^2x]/(16y^4 x^2 J).

On bB eta nonzero, x and K are already units in k[x]/(P). J need not be.
If alpha is a common root of P and J, then (RC1) implies Q(alpha)=0.
Substituting B alpha=-bK(alpha)/(2y) into Q gives

    Q(alpha)=K(alpha)[K(alpha)+4yb].

By (RC3), K(alpha) is nonzero. Therefore every failure of J to be a unit
on the P algebra is supported at the single explicit point

    alpha=2b^2/B,  K(alpha)=-4yb,
    C(alpha)=-3yb/alpha^2,  W(alpha)=B/8.                    (RC13)

This is a necessary condition, not a proof that this exceptional point
is impossible. Its multiplicity and derivative conditions remain part
of the problem. An argument dividing by J must retain this chart.

## 5. Correct use on a finite free ordered-root cover

The coordinate extension obtained by writing

    C(x)=product_(i=1)^(t-1) (x-rho_i)

is the finite free cover of rank (t-1)! from the frozen source. It is
faithfully flat, so the residual radical-membership question can be
tested there. Roots rho_i=rho_j are included.

There is a useful warning about translating the identities to root
equations. The value equations

    P(rho_i)H(rho_i)=-Qc(rho_i)/16

alone do not enforce C|(PH+Qc/16) on repeated-root fibres. Use synthetic
division, which supplies polynomial equations without a Vandermonde
denominator. Starting with f0=PH+Qc/16, define recursively

    a_i=f_(i-1)(rho_i),
    f_i=(f_(i-1)-a_i)/(x-rho_i).

Each quotient is polynomial in x and all coefficients/rho variables.
Then C divides f0 exactly when all a_i vanish. If the ordered roots
repeat at a point, this implements the required Hermite jets there;
it remains valid when every root coincides. The same construction can
apply to the C^2 contact, using the ordered list of roots twice.

The contact, coprimality, and norm statements constrain the root cover
but do not replace the full differential equation PH=R. In particular,
the existence of a factor P of R is insufficient: its complementary
factor has to equal the prescribed differential expression H. Any
successful root-cover argument must retain this differential linkage
and global polynomial truncation.

## 6. Independent audit of the Laurent-resonance arithmetic

For fixed C,B,b,eta, the leading linearization under W -> W+h x^k is

    lambda_k=2omega(k+2t+3+6d)

at degree q+k. Here alpha=3/(4y^2) and alpha/omega=6d+3. The only
possible resonance is

    k*=-2t-3-6d=-6d(d+1)-1.

For integer t, k* is integral if and only if d is integral. Indeed,
integrality makes d rational, and writing d=a/c in lowest terms in
3a^2=(t+1)c^2 forces c^2 to divide 3, hence c=1. Thus the resonant
indices are exactly t=3m^2-1, d=+/-m. At d=-m,

    k*=-6m(m-1)-1,  q+k*=6m-2.

For m>=2 this coefficient lies in the positive residual range 2..2t;
for t=2,d=-1 it lies at degree 4. At d=+m it lies at degree -6m-2.
These arithmetic statements are consistent with the requested t=2
control and do not infer any polynomial contradiction from
nonresonance. An invertible Laurent recurrence can simply generate
an infinite negative-power tail.

## 7. Exact verification and residual

`rootcover_identities.py` was run in the foreground as

    timeout 60s stdbuf -oL python3 .../rootcover_identities.py

It completed in under one second with all eight PASS markers in
`rootcover_identities.log`. The universal calculation proves (RC1),
(RC5), (RC6)--(RC7), (RC11), and the elimination used in (RC13) over Q.
Separate exact resultant checks use repeated K and repeated C controls;
those inputs test algebraic identities and are not claimed to satisfy
the normalized F3 equation. There is no modular-to-characteristic-zero
promotion and no remaining process.

No mechanism established here proves B eta=0 at any new t. The exact
remaining task is to couple the prescribed differential factor H with
the norm/contact data on the complete ordered-root cover and prove
global truncation impossible on B eta nonzero. The cubic intersection
bound is a uniform partial reduction, including multiple roots and
the b=0 limit. Laurent resonance alone does not close either generic
indices or the split indices.
