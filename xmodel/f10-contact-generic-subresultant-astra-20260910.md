# Whole paired-contact finiteness from an integral family and a mod-7 fibre

2026-09-10. Astra producer; UNREVIEWED. First action 01:32:27 UTC;
fixed stop 01:47:00 UTC; publication reserve begins 01:45:00 UTC.
ZERO mathematical subprocesses, code, or generated coefficient artifacts.

## 1. Result and precise premises

The ENTIRE unguarded common-monic-quadratic algebra over Q is
finite-dimensional. Consequently the accepted17zi symmetric guarded ring
R, its ordered rank-two cover C, and their V!=1/3 charts are all finite-
dimensional over Q. This proves whole-locus finiteness, retaining every
original guard and every further leading-coefficient-zero locus.

It does NOT prove generic-chart emptiness, list all exponent pairs, exclude
prescribed rational/integer specializations, or close the source/JC2. The
accepted17zi closed-slice points already refute whole complex emptiness.
No older unreviewed dimension theorem is a premise.

Exactly three charged inputs were pinned before use:

- box/f10-contact-generic-subresultant-prep-20260910/ROOT-CARD.md:
  e79deea08850bccd16b8c741eadfd02b811447bc41ef4138a8d46ae657e82f87.
- xmodel/f10-contact-symmetric-remainder-astra-20260910.md:
  96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13.
- xmodel/f10-contact-symmetric-remainder-gate-fable5-20260910.md:
  f4f51690d293fff29b63a6a6e965b6168edecae70135dfeac8183bb9720e0093.

The card and new gate were read WHOLE after pins; the producer's earlier
exact WHOLE was reused after its current matching pin as expressly allowed.
ROOT17zi qualifications control: x,y are in the faithful ordered cover and
require lying-over for residue-field arguments; the closed slice has three
symmetric points and six ordered points. No other science input was read.

## 2. Literal family and the proposed cubic reduction

Use a(X)=720A_X and b(X)=5040B_X, with the accepted integer coefficients:

    a=X^4+(30V-14)X^3+(71-270V+180V^2+120W)X^2
      +(-154+780V-900V^2+120V^3-600W+720VW)X
      +120-720V+1080V^2-240V^3+720W-1440VW+360W^2;

    b=X^4+(42V-18)X^3+(119-504V+420V^2+210W)X^2
      +(-342+1974V-2940V^2+840V^3-1470W+2520VW)X
      +360-2520V+5040V^2-2520V^3
      +2520W-7560VW+2520V^2W+2520W^2.

Let q=X^2-sX+p. Write F for the four coefficients of rem_q(a), rem_q(b),
exactly the accepted17zi equations. Monic division defines F over Z and
retains nilpotents. For k=Z_(7), the rationals with denominator prime to 7,
put

    D=k[s,p,V,W]/F.                                  (1)

No guard or leading coefficient is inverted in D.

The suggested generic reduction checks, but will not be needed for the
global proof. On c=4-12V invertible, put h=(a-b)/c=X^3+uX^2+vX+w.
Comparing h=q(X-r) gives r=-u-s, p=s^2+us+v and

    f(s)=s^3+2us^2+(u^2+v)s+uv-w=0.

Writing a_i for the displayed coefficients of a, define
U=a2-v-a3*u+u^2, T=a1-w-a3*v+uv, Z=a0+(u-a3)w.
Then direct substitution gives

    rem_q(a)_X = -f(s)+U*s+T,
    rem_q(a)_0 = (u-a3)*f(s)+Z-U*(s^2+us+v).

Thus the monic cubic and these two rows are exact; modulo f(s) and U*s+T,
the second row is also T*s+u*T+Z-U*v. This verifies the card's substitution
with an actual linear remainder. No U, T, Z or other new factor is
inverted, and the proof below handles their whole zero loci by working
in the stronger unguarded algebra (1), before even c is inverted.

## 3. A proved constant leading coefficient makes D finite over k[V]

Let P(V,W)=Res_X(a,b), defined by the ordinary Sylvester determinant over
Z[V,W]. We need only its highest W coefficient, which can be proved
without constructing the other coefficients. Introduce an indeterminate
t and a polynomial variable Zeta. The exact scaling identity is

    P(V,t^2)=t^16 Res_Zeta(t^-4 a(t*Zeta;V,t^2),
                           t^-4 b(t*Zeta;V,t^2)).       (2)

Each normalized monic quartic has coefficients in Z[V,t^-1]. Its constant
term with respect to t^-1 is respectively

    A0=Zeta^4+120Zeta^2+360,
    B0=Zeta^4+210Zeta^2+2520.

Therefore P has W-degree at most eight and its W^8 coefficient is the
constant integer L=Res_Zeta(A0,B0). This coefficient is explicitly nonzero:
writing Y=Zeta^2, the two quadratic polynomials differ by 90(Y+24), and

    (Y^2+120Y+360)|_(Y=-24)=-1944,
    L=[90^2*(-1944)]^2=90^4*1944^2 != 0.              (3)

The square in (3) follows because each root in Y contributes twice to
the resultant after Y=Zeta^2; equivalently it is the universal composition
identity for these monic even quartics. Moreover L mod 7 is 4. This also
checks directly: B0 mod 7 is Zeta^4 and A0(0) mod 7 is 3, so the resultant
is 3^4=4. Thus L is a UNIT in k, and P/L is monic of degree eight in W
over k[V]. This is a proved leading-coefficient identity, not an asserted
nonzero uncomputed resultant or an extrapolation from one parameter fibre.

Here is why P vanishes in D, and why all remaining coordinates are integral.
Adjoin x via E=D[x]/q(x), and put y=s-x. This extension is free of rank two
and hence D->E is injective, WITHOUT assuming Delta invertible. Both a and
b are divisible by q in D[X], so a(x)=b(x)=0. The Sylvester adjugate Bezout
identity puts P in (a,b) in k[V,W,X]; evaluating at x and using injectivity
gives P=0 already in D. Thus W is integral over k[V].

Also a(x)=a(y)=0, with a monic quartic over k[V,W]. Hence x,y are integral
over the image of k[V,W] in E. Their sum s and product p are integral
there as well. The same monic identities hold in D by injectivity. Since
D is generated by W,s,p over k[V], transitivity of integrality and finite
generation prove

    D is a FINITE k[V]-module.                         (4)

All statements use exact ring identities; reducedness and field-point
assumptions have not been introduced. In particular (4) controls fibres
escaping to infinite W, which a mere empty special guarded fibre would not.

## 4. The whole V=1 fibre modulo 7 is zero

Specialize V=1 and reduce modulo 7. The literal formulas give

    b=(X-3)(X-4)(X-5)(X-6) in F7[X],

independent of W, with four distinct roots. The four values of a are

    f3(W)=a(3)=3W^2+6W+1,
    f4(W)=a(4)=3W^2+5,
    f5(W)=a(5)=3W^2+3W+3,
    f6(W)=a(6)=3W^2+W+3.                           (5)

For example a at V=1 modulo 7 is
X^4+2X^3+(2+W)X^2+WX+2+W+3W^2, which independently checks all four rows.
Any monic quadratic divisor of b over an algebraic closure of F7 uses two
distinct members of {3,4,5,6}. None can divide a: subtracting the associated
rows of (5) forces the W value in this complete six-pair table, where the
remaining row is nonzero. Every entry is in F7.

| Pair | Forced W from difference | Remaining nonzero value |
|---|---:|---:|
| 3,4 | 3 | f4(3)=4 |
| 3,5 | 3 | f5(3)=4 |
| 3,6 | 6 | f6(6)=5 |
| 4,5 | 3 | f4(3)=4 |
| 4,6 | 2 | f4(2)=3 |
| 5,6 | 0 | f5(0)=3 |

The linear differences have nonzero coefficients, so the table holds over
the whole algebraic closure, not just for W in F7. Repeated-root quadratics
cannot divide the squarefree b. This exhausts every possible q, including
all otherwise excluded guards. Therefore

    D/(V-1,7)=0.                                      (6)

For the nonreduced issue: by (4) this is a finite-dimensional F7 algebra.
If nonzero it has a maximal ideal and a point over the algebraic closure,
contrary to the exhaustive table. Thus (6) is zero as a ring, not merely
a count of reduced points.

## 5. From this fibre to total finite dimension

Let N=D/(V-1). It is a finite module over the LOCAL ring k=Z_(7), by (4).
Equation (6) says N/7N=0, so Nakayama gives N=0. After tensoring with Q,

    M=D tensor_k Q is finite over Q[V],
    M/(V-1)M=0.

Nakayama at the maximal ideal (V-1) of Q[V] now gives M_(V-1)=0. Choose
finitely many Q[V]-module generators of M. Each is killed by some polynomial
not vanishing at V=1; their product f(V) kills all of M and satisfies f(1)!=0.
Consequently M is a finite module over the finite-dimensional Q-algebra
Q[V]/(f), and hence

    dim_Q M < infinity.                               (7)

This proves total zero-dimensionality, not just generic emptiness: the
module is finite over a ONE-dimensional parameter ring before using its
empty fibre. No coefficient of f, or uncomputed norm, is being supplied
as a certificate; its existence and nonzeroness follow from the explicit
module argument. Multiplication by W on the resulting finite Q algebra
likewise has a nonzero univariate annihilator. Thus the accepted17zi
finiteness predicate is proved by a direct dimension argument.

Finally, the exact original symmetric guard is

    G=W*p*(p-s+1)*(9p-15s+25)*(p-2s+4)*(s^2-4p)
      *(s-3)*(4-s)*(36p+9s^2-114s+181)
      *(15s^2-36p-30s+35).

The guarded ring is exactly R=M[G^-1], and its generic chart is
R[(3V-1)^-1]. Localization of a finite-dimensional Q algebra remains
finite-dimensional, including nilpotents. Accepted17zi gives the literal
faithful rank-two cover C=R[x]/(x^2-sx+p), y=s-x, with G=(y-x)H and unit
discriminant. Thus C and its generic chart are finite-dimensional as well.
Every G factor is retained, and no further divisor was discarded: the
proof established (7) even before G or 3V-1 were inverted.

## 6. Controls, limits, and disposition

- FINITENESS IS LOAD-BEARING TWICE. The k-module k[1/7] has zero mod-7
  fibre but is nonzero; it is not finite over k. The Q[V,W]-module
  Q[V,W]/(V), regarded over Q[V], has empty V=1 fibre and dimension one;
  it is not finite over Q[V]. These changed objects explain why both
  Nakayama uses require (4), rather than a bare one-fibre assertion.
- ALL QUADRATIC FACTORS WERE CHECKED. In (5) b is squarefree. A repeated
  q is therefore impossible; for distinct q the table has all six pairs.
  No W=0 or exponent/guard divisor was removed from the fibre proof.
- REDUCTION IS NOT A CHARACTERISTIC-ZERO POINT ARGUMENT. The mod-7 table
  is transported through the finite k-family and Nakayama. It does not
  assert that rational points must have arbitrary chosen good reduction.
- No list of the remaining characteristic-zero points is obtained. Even
  though whole complex finiteness is proved, prescribed rational/integer
  exclusions, earlier forcing and companion equations, and source/JC2
  closure remain outside the conclusion. Generic-chart emptiness is not
  established. No positive-dimensional component can survive this result,
  subject to the required independent gate of this unreviewed producer.

## OPEN(S) RAISED

- NONE new. The assigned generic finiteness question is answered by (7).
  Enumeration/emptiness and prescribed specialization exclusion remain
  outside this bounded task; no follow-on execution or promotion is given.

## COLLISIONS

status: EMPTY

- Own targets were ABSENT at first action; own-only extraction. No corpus,
  ledger, historical, live-body, provenance or shared-file scan occurred.

Own WHOLE report/PINS and own-only OPEN/collision extraction were checked
at 01:42:49 UTC. The completion edit clarifies the two simultaneous modulus
relations in the optional cubic reduction. Exactly three science inputs;
all mathematical derivations, including the six mod-7 checks, were manual.
No mathematical subprocess ANY size, code or generated coefficient file,
network/AWS/SSH/process/agent, live/corpus/shared/protected/Git work, or
frozen-file alteration occurred. Only own apply_patch documentary writes
and the existing publication workflow were used. Root retains custody and
the FIRST different-model gate; this producer gives no promotion or follow-on
authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11480`.
- Body SHA-256:
  `2c36f7913f5583752e566f02445e8a632ca86e95c2289b44d17c0867c13f0cc4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
