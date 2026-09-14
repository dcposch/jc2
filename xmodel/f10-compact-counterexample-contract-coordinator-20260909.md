# F10 compact sufficient counterexample contract and exact finite system

2026-09-09, coordinator. UNREVIEWED mathematical proof, pure hand algebra;
ZERO mathematical subprocesses. Basis0d39df3c9fd69c939a8420c54d03228b9077777d
is provenance only. This is not a constructed point, a solved ideal, or JC2.

## 1. Exact statement, orientation and dependency boundary

Let K be a characteristic-zero field, r>=1 an integer, m=3r+1 and n=5r+2.
Let u,ell,c belong to K, with c!=0. In K[R,t] put

    Pi=t-u*t^2+R*t^3,
    Delta=1+u*t-ell*t*Pi-t*Pi^2.

Suppose Ahat,Bhat are polynomials satisfying ALL the following conditions:

1. Ahat=sum_(k=0)^3 A_k(R)t^k, deg A_k<=m-rk;
   Bhat=sum_(k=0)^5 B_k(R)t^k, deg B_k<=n-rk.
2. The coefficients of R^m in A_0 and R^n in B_0 are exactly one.
3. The full identity [Ahat,Bhat]_(R,t)=c*Delta holds.
4. BOTH substitutions

       Ahat(p*z^3-z^2+u*z,z^-1),
       Bhat(p*z^3-z^2+u*z,z^-1)                  (I)

   have zero negative-z parts, identically in K[p,z,z^-1].

Then there are ordinary source polynomials P,Q in K[U,V] with

    [P,Q]_(U,V)=c,
    deg P=28m, deg Q=28n,
    top P=U^(7m)*V^(21m), top Q=U^(7n)*V^(21n). (II)

Consequently P,Q are not a polynomial automorphism, by the classical
Jung--van der Kulk plane-automorphism degree-divisibility theorem. Thus
ANY field solution of conditions1--4 gives a characteristic-zero plane
Jacobian counterexample, and by embedding the finitely generated
coefficient field into C, a complex counterexample. This statement imports
that named classical automorphism theorem; it does not re-prove it.

Importantly, this sufficient endpoint does NOT require proving that the
reconstructed source has a particular printed F10 chain. That chain is
needed for the separate NECESSARY direction from the campaign's source
family, not to recognize the explicit noninvertible Keller pair (II).

The accepted full compression supplies conditions1--4 for every actual
source in its scope. It used S=R-v0 instead of R; translating the base
coordinate by v0 preserves the coefficient bounds, monic highest powers,
Jacobian and inverse condition, and removes v0. The old-reference letter R
and the translated R here must not be identified without this translation.
The NECESSARY direction retains the compression's original source imports
and coalescence assumptions (separately forced in the accepted campaign
chain). The SUFFICIENT direction below is self-contained algebra apart
from the named automorphism degree theorem; it does not assume an F10
source already exists or use the pending rank-three module report.

Frozen scientific dependencies checked current before these reads:

- xmodel/f10-source-polynomial-cubic-quintic-compression-astra-20260909.md,
  SHA9b77ece0a8076d0a8ef498f0a9c152e1de52e85c7ce3cd6b575d5475d0d3337c,
  root custody/current/transaction verification10:38:40, then WHOLE.
- xmodel/f10-source-polynomial-compression-gate-fable5-20260909.md,
  SHA651dafb531955d76a579d9aace450856132a9733d2a667a2d79222cd7c025bf9,
  terminal/alloriginalsabsent, receipt-first/currentpins10:51:40 then WHOLE.

No other report, source theorem or pending peer is a mathematical premise.
The compression gate correctly did not prove the degree endpoint; this
report supplies that missing implication rather than broadening its verdict.

## 2. Explicit polynomial reference on the source plane

Define in K(U,V)

    g=V^-1, p=V^3*U-V,
    d=p^2+ell*p-u,
    W=1-V*d,
    z=d-V^-1=-W/V,
    t=-V/W,
    R=p*z^3-z^2+u*z.                            (1)

The first two expressions invert U=g^2(1+gp),V=g^-1. All p,d,W are
ordinary polynomials in U,V and W modulo V is one. In particular W is
nonzero for every parameter value; its leading term is -U^2 V^7.

R itself is an ORDINARY polynomial, not merely regular generically. To see
this without a high-power source expansion, use

    p*z-1=-(V^2*U-1)W-1=-V^2*U*W-V*d.

Then

    R=z^2(p*z-1)+u*z
     =-U*W^3-W*(d*W+u)/V.

Since

    d*W+u=p^2+ell*p-V*d^2
           =V*((V^2*U-1)(p+ell)-d^2),

we obtain the explicit factored polynomial

    R_source=W*(d^2-(V^2*U-1)(p+ell)-U*W^2).   (2)

No division by u,ell,p,R or a boundary value occurred. In ordinary total
degree in U,V, p has degree4 and leading UV^3, d has degree8 and leading
U^2V^6, and W has degree9 and leading -U^2V^7. The three displayed terms
of (2) have degrees25, at most16, and28 respectively. Thus

    deg R_source=28,
    top R_source=U^7 V^21.                      (3)

This degree is independent of u and ell, including their zero values.
The rational function t_source=-V/W has ordinary rational degree -8 and
leading homogeneous rational function U^-2 V^-6.

## 3. Full reverse polynomiality and the exact Jacobian

By condition4 the expressions (I) define ordinary A'(p,z),B'(p,z). The
polynomial automorphism z=p^2-g+ell*p-u makes them ordinary A(g,p),B(g,p).
The substitution g=V^-1,p=V^3U-V places them in K[U,V,V^-1]. On the other
hand their equal expressions Ahat(R_source,-V/W),Bhat(R_source,-V/W)
belong to K[U,V,W^-1]. Because V is prime and W mod V=1,

    K[U,V,V^-1] intersect K[U,V,W^-1]=K[U,V].

For example, if a/V^j with j>0 minimal equals b/W^k, then aW^k=bV^j
forces V|a, a contradiction. Hence P,Q are ordinary, with no omitted
source divisor. This is exactly why condition4 cannot be dropped.

The rational maps are birational and the chain rule is an identity in their
common rational function field. Directly,

    det d(U,V)/d(g,p)=g,
    det d(p,z)/d(g,p)=1,
    det d(R,t)/d(p,z)=-z,
    p=Pi(R,t), g=-Delta(R,t)/t.

Condition3 therefore gives [A',B']_(p,z)=(-z)cDelta=cg, then
[A,B]_(g,p)=cg. The first determinant gives [P,Q]_(U,V)=c. All these
are polynomial identities once polynomiality has been established;
localization did not discard a separate component or parameter value.

## 4. Actual source degrees and the counterexample implication

For a nonzero rational function f in K(U,V), define its degree at ordinary
infinity by deg numerator minus deg denominator in any polynomial fraction.
This is well-defined and additive on products; the associated leading
homogeneous rational function multiplies. For a sum the largest degree is
an upper bound, and a unique largest-degree summand cannot cancel.

A monomial R^i t^k in either compressed output, after (1), has rational
degree

    28i-8k.

Its coefficient bound i+rk<=e implies

    28i-8k<=28e-(28r+8)k.

If k>=1 this is STRICTLY below28e. If k=0 and i<e it is again strictly
below28e. The single monomial R^e occurs with coefficient one by
condition2, and by (3) has degree28e and leading U^(7e)V^(21e).
It cannot cancel against any other term, even though individual other
terms are rational before the intersection argument. For the now-proved
ordinary P,Q, rational degree equals ordinary polynomial degree. This
proves every part of (II), not just an upper bound or an allowed corner.

Finally 5m-3n=-1, so gcd(m,n)=1, m>=4 and n>=7. Neither 28m nor28n
divides the other. An automorphism of the plane over a characteristic-zero
field has one coordinate degree dividing the other; applying that classical
theorem after scalar extension shows (P,Q) is not invertible. If K is not
already a subfield of C, restrict to the subfield generated over Q by the
finitely many coefficients and choose an embedding into C. c remains
nonzero, the identities remain true, and the monic leading terms persist.

For r=1 the exact degrees are112 and196. No solution at r=1, or at any
other r, has been found here. The implication is sufficient, not a
counterexample announcement or a proof of properness.

## 5. A literal finite coefficient ideal, not a subset or truncation

For a fixed r, introduce an independent coefficient for every slot

    R^i t^k, 0<=k<=3, 0<=i<=m-rk, for Ahat;
    R^i t^k, 0<=k<=5, 0<=i<=n-rk, for Bhat.

Set the two R^m/R^n coefficients equal to one by substitution. Add scalar
variables u,ell,c and eta. Define the ideal I_r over Q to be generated by:

- EVERY coefficient of [Ahat,Bhat]-cDelta in Q[parameters][R,t];
- EVERY coefficient in p of EVERY negative-z row of BOTH (I) expressions;
- eta*c-1.

There is no additional optional chart, truncation, nonsingularity guess or
monic-stratum exclusion: these are exactly conditions1--4 and c invertible.
The bound in t is3/5 because that is an actual necessary output of the
accepted source compression, not an experimental degree cap.

The number of A coefficient slots is
(3r+2)+(2r+2)+(r+2)+2=6r+8; B has15r+18. After fixing two coefficients
and adding the four scalar variables, the ambient polynomial ring has

    21r+28 variables, hence49 at r=1.            (4)

This is a literal coefficient count, not a solver-cost estimate. It includes
all slots, even ones that later equations may force to vanish.

There is also a small finite row envelope, requiring no high source-power
construction. The coefficient of t^h in the Jacobian has R-degree at most
7r+2-rh for h=0,...,7: a term with t-indices k,l has k+l=h+1 and the
R-derivative lowers the sum of R-degree bounds by one. The explicit target
Delta satisfies the same bounds. Thus at most

    sum_(h=0)^7 (7r+3-rh)=28r+24

coefficient rows encode the ENTIRE Jacobian. For the negative-z conditions,
R in (I) has z-order at least one. A monomial R^i z^-k can contribute a
pole only when i<k<=5; high i cannot do so. A factor p can arise only with
at least three z powers. Therefore the A pole rows z^-1,z^-2,z^-3 have
p-degree zero; the B rows z^-1,z^-2 have p-degree at most one and the
rows z^-3,z^-4,z^-5 have p-degree zero. At most3+7=10 scalar rows suffice
for the entire inverse condition. Including eta*c-1 gives at most

    28r+35 rows, hence63 at r=1.                 (5)

Some listed rows may be zero or redundant. These are proved upper counts,
not an assertion that a generated file with exactly this many nonzero
rows exists; no coefficient builder or solver was run. In particular the
finite inverse-row extraction needs powers of R only up to four, whatever r.

Over an algebraically closed characteristic-zero field, I_r proper is
sufficient for a counterexample by Hilbert's Nullstellensatz and sections
2--4. Conversely every actual F10 source in the accepted necessary scope
gives such a point after the explicit constant translation of R. This does
not prove that EVERY Keller counterexample belongs to one of these ideals.
If I_r is a unit, it excludes that exact necessary source stratum, not JC2.

An exact point in a NONZERO finite Q-algebra, satisfying every row and with
eta*c=1, is also a sufficient certificate: pass first to any residue field,
which is a finite extension of Q. Monicity and c invertible survive; apply
the FIELD proof there and embed into C. No theorem over arbitrary nilpotent
parameter rings or a smooth-mod-p lifting assumption is needed. No such
point or properness certificate is supplied.

## 6. Manual controls, composition and stop

- Dropping condition4 admits t as a coordinate function: its inverse is
  z^-1 and the two-ring argument fails. Polynomiality in K[R,t] alone is
  never enough, even though the Jacobian target is retained.
- Dropping monicity or permitting the top coefficient to vanish loses the
  unique degree28e term; a support upper bound is not an actual degree.
- Replacing Delta by one changes the exact source Jacobian; dropping
  eta*c-1 admits c=0 and cannot certify a Keller map.
- The two-row negative-pole estimate uses z-order AT LEAST one and hence
  remains valid when u=0 raises that order. The row envelope does not throw
  away u=0 or select a generic boundary point.
- A bare numerical49-variable/63-row description is not the system:
  I_r is defined by the FULL identities above. A future builder must be
  independently checked against that contract, including inverse rows and
  the nonzero c equation, before any solver output is evidence.

The accepted compression's caution about missing support/chain/canonical
requirements is respected for the claim of reconstructing that exact
printed source profile. For the distinct counterexample endpoint, the
ordinary full pair, constant bracket and exact nondividing degrees proved
here discharge the necessary obligations directly. No backward actual-chain
theorem is assumed, and no particular face equality is used as a surrogate
for the actual degree computation.

This is a concrete source-attached complete system of linearly growing
size, not the previously stopped generic cubic-norm shortcut and not a
claim of a measured computational speedup. The next acceptance gate must
independently check source ordinaryness, the unique highest-degree term,
the entire coefficient ideal and both count bounds. No mathematical
subprocess, AWS allocation, large solve, descendant or public claim is
authorized by this report. Root authored only this leased private partial;
existing shared and protected work was not touched.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13021`.
- Body SHA-256:
  `9d0d06033eacd5069b6d8e7f6bb8c5e9c866ef4f22ee9f4e78837c8ee396faa1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
