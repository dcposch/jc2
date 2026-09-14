# Whole finite-contact eliminant interface: exact four-generator presentation

2026-09-10. Astra producer, UNREVIEWED. First action 03:36:39 UTC;
fixed cap 03:52:39 UTC; publication reserve 03:50:39 UTC; never reset.
Manual mathematics/source text only. ZERO mathematical subprocesses.

## 1. Verdict and charged scope

ROOT's proposed four-generator ideal is CORRECT. Its quotient is exactly
the unguarded common-monic-quadratic algebra localized at c*A, followed
by its monic rank-two ordered cover. Consequently it is finite-dimensional
over Q WITHOUT adding G, with nilpotents retained. Every prescribed
guarded contact maps into it, after the separately accepted c=0 slice is
excluded. The presentation is not an assertion that c*A is a unit on the
whole unguarded algebra.

This supplies one exact all-prescribed-exponent certificate target and
rational-root interface. NO univariate polynomial has been computed here;
no finite root list, prescribed exclusion, point count, source implication
or JC2 closure is claimed. The earlier single-client packet is NOT a
charged input or premise; no isolated residue work is performed.

Exactly nine inputs: this ROOT-CARD and its eight pinned accepted reports.
The card and five reports were read WHOLE anew; three earlier same-byte
WHOLE reads were expressly reused only after matching current pins.
The exact scopes/hashes are in PINS. Accepted17zi/17zj/17zn and ROOT's
qualifications control, not their old producer lifecycle prose. The 17w
incidental e_y Cramer sign is positive; u-normalization is a field-point
fact or explicit unit chart. No source/corpus/provenance expansion occurred.

## 2. Literal manageable polynomial target

Use a(Y)=Y^4+a3*Y^3+a2*Y^2+a1*Y+a0, where

    a3=30V-14,
    a2=71-270V+180V^2+120W,
    a1=-154+780V-900V^2+120V^3-600W+720VW,
    a0=120-720V+1080V^2-240V^3+720W-1440VW+360W^2.

The literal accepted difference a-b is c*Y^3+d*Y^2+e*Y+f, with

    c=4-12V,
    d=-48+234V-240V^2-90W,
    e=188-1194V+2040V^2-720V^3+(870-1800V)W,
    f=-240+1800V-3960V^2+2280V^3
        +(-1800+6120V-2520V^2)W-2160W^2,
    g=d-c*a3=8-54V+120V^2-90W.

Define ACTUAL polynomials in Q[V,W], without rational-function division,

    A=c^2*a2-c*e+d*g,
    B=c^2*a1-c*f+e*g,
    C=c^2*a0+f*g,
    t=c*A.

In the GLOBAL polynomial ring P=Q[z,V,W,X], set I=(I1,I2,I3,I4):

    I1=c*A*C-c*B^2+d*A*B-e*A^2,
    I2=d*A*C-c*B*C-f*A^2,
    I3=A*X^2+B*X+C,
    I4=z*c*A-1.                                      (1)

These defining expressions are exact polynomials, not an instruction to
execute an expansion or an emitted coefficient artifact. No resultant or
Groebner computation has been made or claimed.

## 3. Both algebra maps; powers, signs and ordered cover

Let M=Q[s,p,V,W]/F_q, where F_q is the ideal of four monic remainder coefficients of
a,b modulo q(Y)=Y^2-sY+p. Explicitly, for each a_i and then b_i, the rows are

    s^3-2sp+a3*(s^2-p)+a2*s+a1,
    p^2-s^2*p-a3*s*p-a2*p+a0.                         (2)

No guard is inverted in M. Accepted17zj proves dim_Q M finite. Put
N=M[t^-1], and D=Q[V,W,t^-1]/(I1,I2). The definitions of t in both
rings are the same polynomials in V,W. A product is a unit in a commutative
ring only if both factors are units, so c and A are units in N and D.

On the c-unit chart put u=d/c,v=e/c,w=f/c and h=(a-b)/c. The exact identity

    a=(Y+a3-u)h+U*Y^2+T*Y+Z,
    U=A/c^2, T=B/c^2, Z=C/c^2                       (3)

follows by coefficient multiplication. In N, q divides a and h. Since q
is monic of degree two, its divisibility of the last quadratic in (3)
forces that quadratic to equal U*q, over an arbitrary ring. Therefore

    T=-sU, Z=pU,       s=-B/A, p=C/A.                (4)

Monic division of h by q, followed by (4), gives precisely

    UZ-T^2+uUT-vU^2=0,
    uUZ-TZ-wU^2=0.                                  (5)

Multiplying EACH row of (5) by c^5 gives I1 and I2 respectively:
the UZ,T^2,TZ terms have denominator c^4, whereas the terms containing
u,v,w have denominator c^5. This verifies every displayed power and sign.

Thus V,W define a map D -> N. Conversely define s=-B/A,p=C/A in D and
q=Y^2+(B/A)Y+C/A. Since c^5 and U^2 are units, I1=I2=0 is equivalent to
both coefficients of rem_q(h) being zero. Explicitly,

    h=q*(Y+u-T/U),
    a=(Y+a3-u)h+U*q,             b=a-c*h.             (6)

Consequently q divides a,b, so (2) vanishes and the assignments define
N -> D. The two maps fix V,W and t^-1, and (4) fixes s,p:
they are mutual inverses, including nilpotents. Thus N is EXACTLY D.

Finally I4 presents localization at t with z=t^-1, and I3/A is monic.
There is an exact isomorphism

    P/I ~= N[X]/(X^2-sX+p),
    s=-B/A, p=C/A, z=t^-1,       y=s-X.              (7)

The cover in (7) is free of rank two, basis 1,X; no discriminant inversion
is needed for faithfulness. It has involution X -> s-X. It is NOT claimed
etale before Delta=s^2-4p is inverted. Nor is it identified with the naive
unguarded two-evaluation ring: at a repeated exponent two evaluations
alone do not force monic quadratic divisibility. Equations (2), not that
weaker condition, define the unguarded base used here.

## 4. Whole finite dimension and all prescribed points

A localization of a finite-dimensional Q-algebra is finite-dimensional:
in its Artinian decomposition it retains just the local factors where the
localized element is a unit. Thus N is finite-dimensional, possibly zero;
(7) is finite-dimensional as a free rank-two N-module, possibly zero.
No G or additional leading coefficient has been added to prove this.
If t is nilpotent on every factor, N=P/I=0; the argument still holds.

For the original guarded ring R=M[G^-1], retain exactly

    G=W*p*(p-s+1)*(9p-15s+25)*(p-2s+4)*(s^2-4p)
        *(s-3)*(4-s)*(36p+9s^2-114s+181)
        *(15s^2-36p-30s+35).

Accepted17zn proves U is a unit on R[c^-1]; hence A=c^2*U and t are units
there. The localization map N -> R[c^-1] exists and induces

    P/I -> R[c^-1][X]/(X^2-sX+p).                   (8)

Indeed localizing N further at G gives R[c^-1], by the U-unit result;
thus (8) is exactly further G-localization of (7). This precise ring-map
direction means that EVERY field point of the guarded ordered c-unit
chart yields a point of P/I. Spec(P/I) can be larger than the guarded
scheme because its G=0 points have not been removed. No prescribed point
is lost at A=0.

The c=0 guarded slice is separately accepted17zi: three symmetric/six
ordered reduced points, exponent coordinates in {1/3,2/3,4/3}. None has
5/3<x<y<2. This exclusion applies to the GUARDED slice, not to every
unguarded c=0 point. Therefore every prescribed normalized contact with
r>=2, m=3r+1,n=5r+2,1<=j<=r-1, x=n/m,y=(n+j)/m provides a field
evaluation of P/I via (8).
The accepted ordered-cover/source-normalization qualifications remain
necessary; no reality or rationality of V,W is inferred from real x,y.

## 5. Exact eliminant certificate contract, and a smaller-ring variant

The requested certificate is explicit F(X),H1,H2,H3,H4 such that

    0 != F in Q[X],       F=sum(i=1..4) Hi*Ii
    with every Hi in Q[z,V,W,X].                    (9)

The contract checks exact rational coefficient equality, actual absence
of z,V,W from F, and F!=0. A name, degree, header, floating approximation,
pointwise vanishing claim or uncomputed Groebner assertion is not (9).
No demand for minimality or squarefreeness is necessary: (9) is an exact
ideal membership with the full nonreduced scheme retained.

Existence is proved but not supplied as an explicit polynomial. If P/I
is nonzero finite-dimensional, the characteristic polynomial of the Q-
linear multiplication-by-X operator is monic and nonzero, and annihilates
X by Cayley-Hamilton. It therefore lies in I, giving some (9). If P/I=0,
take F=1; ideal membership again gives some H_i. No actual dimension,
operator matrix, coefficient, minimal polynomial or root list is asserted.

An equivalent smaller-ring certificate uses S0=Q[V,W,X], J=(I1,I2,I3):

    I intersect S0 = J:t^infinity.

It suffices to give N0>=0, Ki in S0 and F as above with

    t^N0*F=K1*I1+K2*I2+K3*I3.                      (10)

This is exactly clearing localization denominators, not replacing J by
its radical. Conversely (10) yields the explicit global identity (9):

    F=z^N0*sum(i=1..3) Ki*Ii
       -(zt-1)*F*sum(k=0..N0-1)(zt)^k.              (11)

For N0=0 the last sum is zero. Multiplying out the geometric sum verifies
(11) over Q[z,V,W,X]. This offers one equivalent certificate contract,
not a second representation search. No software commands are executed or
requested; ROOT's supplied Singular command premises are not a web read.

Every mapped contact obeys F(x)=0. Swapping the ordered root in (7) also
gives F(y)=0. Thus ONE certified F constrains BOTH exponents for every r,j.
A surviving pair of roots is only a necessary condition: it need not share
V,W, satisfy G, or satisfy any further source/affine equation.

## 6. Primitive-integer and uniform prescribed-parameter discrimination

Multiply a certified F by a nonzero rational constant to obtain primitive
P0(X)=a_D*X^D+...+a_0 in Z[X], with a_D!=0. This scaling preserves (9).
If D=0 the nonzero constant immediately excludes every contact. For D>0,
put n=5r+2,m=3r+1. The exact identity 3n-5m=1 proves gcd(n,m)=1.
From m^D*P0(n/m)=0, reduction modulo m gives m | a_D*n^D; coprimality
therefore proves

    3r+1 divides |a_D|.                              (12)

All possible r are among (m-1)/3 where m is a positive divisor of |a_D|,
m>=7 and m=1 mod 3. Substitution P0((5m+1)/(3m))=0 then checks this finite
list exactly. This is only a conditional interface until P0 is supplied.
For example no such divisor, in particular |a_D|<7, would exclude all r.

Two cleaner uniform tests are available after actual coefficient custody:

- Since x=5/3+1/[3(3r+1)], it lies in the sharp bounding interval
  (5/3,12/7], with upper endpoint at r=2 and lower limit as r grows. A certified
  absence of real roots of P0 in this interval excludes all first exponents.
  Alternatively, at most one DISTINCT real root in (5/3,2) excludes all
  off-diagonal prescribed pairs because BOTH x and y must be roots.

- Remove exact factors (X-2) from P0 until the remaining integer polynomial
  P1 has P1(2)!=0; this preserves vanishing at every prescribed x<2, but
  is NOT claimed to preserve ideal membership. For d1=deg(P1), define

      K(R)=(3R+1)^d1*P1((5R+2)/(3R+1)) in Z[R].

  This polynomial is nonzero: the fractional-linear substitution has
  inverse R=(2-X)/(3X-5), so is injective on rational functions. Also
  K(0)=P1(2)!=0. Each admissible integer r>=2 is a root of K, hence
  r divides |P1(2)|. This supplies a second finite divisor filter and,
  for example, |P1(2)|=1 would exclude all r>=2. If P1 is constant it
  already excludes them. The filters may be intersected, never assumed
  sufficient for a contact. This is a symbolic all-r interface, not a
  residue campaign or a computed polynomial/root assertion.

## 7. Load-bearing saturation control and remaining GAP

Omit ONLY I4 and consider J=(I1,I2,I3) without t-saturation. At V=W=0,
c=4,d=-48,e=188,f=-240,g=8 and

    A=16*71-4*188-48*8=0,
    B=16*(-154)-4*(-240)+188*8=0,
    C=16*120-240*8=0.

Thus all three rows vanish for EVERY X: the changed ideal has an affine
X-line (and arbitrary z if z was retained). It cannot support a nonzero
univariate member in X. By contrast the true unguarded common factors
at V=W=0 divide gcd(a,b)=(Y-3)(Y-4)(Y-5), giving only the three monic
quadratic choices over a field. Clearing denominators without saturation
has created spurious positive dimension. I4 correctly excludes this t=0
locus; it is allowed to do so because the target is N, not the whole M,
and accepted17zn guarantees t!=0 on the prescribed guarded c-unit chart.

The complete representation, finiteness and certificate contract are
proved. The smallest remaining computational GAP is an ACTUAL nonzero
univariate F together with (9) or (10), followed by exact root/divisor
discrimination; no such output is present. Even successful normalized
contact exclusion requires an independently accepted source map to infer
anything about earlier affine forcing, companion conditions or JC2.
No actual contact computation, runtime registration, review, promotion or
follow-on execution is authorized by this report.

## OPEN(S) RAISED

- ASSIGNED GAP ONLY; no new canonical ID: obtain and independently check
  the explicit certificate (9)/(10), then classify/exclude its prescribed
  roots with all source caveats. No new residue client or execution task.

## COLLISIONS

status: EMPTY FOR THIS INTERFACE TASK

- Exact own report and box were ABSENT at first action. Own-only checks;
  no corpus/history scan or all-corpus novelty assertion.
- The earlier single-client packet and older unreviewed dimension claim
  were not read, charged or used. No residue mechanism is re-presented.

Own WHOLE report/PINS and own-only OPEN/collision extraction completed at
2026-09-10 03:43:03 UTC. Completion clarified only ring-map notation and
the discrete prescribed set's bounding interval. Every mathematical step
was manual. No forbidden subprocess, source expansion, shared/protected
work or downstream action occurred. ROOT retains custody-FIRST intake and
any FIRST different-model review; this producer grants no promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13377`.
- Body SHA-256:
  `2ab37c87fed5bcd75ab6740fe9050fbf57569290cedb493f7fbf58033fd2389c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
