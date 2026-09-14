# Deflated r=3 modulo7 mixed-scalar test

MANUAL co-research only. First action 2026-09-13 03:02:54.305822988 UTC;
original reserve 03:17 / HARD 03:20 UTC. Inputs pinned before WHOLE reads;
no scientific execution, source edit or unproved quotient-integrality premise.

## Theorem

For EVERY actual r>=2 with r=3 modulo7, the SAME mixed scalar B is a unit
of the whole accepted leading algebra. At every root over Q_7's algebraic
closure, writing l=v_7(t-1)=v_7(2r+1)>=1, one has exactly

    v_7(B)=2l-15/7.                                    (1)

This is a new manual candidate theorem requiring independent review. It is
not a re-proof of the two previously promoted families. Together they would
leave r=0,4,5,6 modulo7 unresolved; no all-r or source-exclusion claim follows.

## 1. Actual source initial data

Set epsilon=t-1=(2r+1)/(3r+1). The denominator is a 7-adic unit for this
family, and epsilon is nonzero with positive valuation l. Import the accepted
septic root valuation v(X)=-2/7. The compact U,V of the charged reduction
give v(U)=-4/7 and v(V)=-1, since V's constant specializes at t=1 to2/35;
the cubic term has valuation-6/7 and all other terms are higher than-1.
Hence v(Y)=-3/7 from UY=V. No source inverse or component is removed.

Fix pi^7=7 and let x,y be residues of pi^2 X,pi^3 Y. They are nonzero.
The exact normalized d6 equation has initial part X^3-3Y^2, giving

    x^3=3y^2.

The compact UY=V equation, multiplied to its leading level, gives

    x^2y=residue(7*(2/35)/3)=2.                         (2)

These equalities hold at every source root. They are residue-field
relations at actual t, not a substitution of the forbidden rational value
t=1 into the original unnormalized equations.

## 2. Exact deflation before any reduction

In Q[s,t,X,Y] define

    beta(s,t)=[u^14](phi'/phi) T_s T_(t+3-s),
    Q(s,t)=beta(s,t)/(s-1),
    C(s,t)=(Q(s,t)-Q(t,t))/(s-t).                       (3)

All these are POLYNOMIALS: beta(1,t)=0 universally by degree, and the
second numerator is a polynomial divided difference. Both divisions in (3)
are monic in s, so neither introduces parameter denominators or factors7.
This construction is not division by a vanishing residue-field epsilon.

On the actual source beta(t,t)=0. This follows from the accepted six-root
identity, and can also be checked directly without the other four roots:
for arbitrary phi and t!=0, retaining d6,d7 before quotienting,

    beta(t,t)=3(t-2)Y^3*d6/t +(8t-21)XY^2*d7/t.         (4)

Indeed T3=phi^3-u^8(3XY^2+Y^3u), while through degree6,
(phi'/phi)T_t=T_t'/t. The first term contributes3Y^3*d6+8XY^2*d7;
the removed tail contributes6Y^3*d6/t+21XY^2*d7/t. This proves (4).
Since epsilon is a nonzero rational, Q(t,t)=0 in the actual source.
Putting s=2t-1 in (3) therefore gives the exact source identity

    B=2epsilon^2*C(2t-1,t).                            (5)

The source equality (5) is established before any carry or integrality
argument. It is valid on the entire source algebra, not just its points.

## 3. The denominator/weight bound survives deflation

Restore the linear coefficient L temporarily, with weights1,2,3 for L,X,Y.
Every beta term has total weight15. In each degree<=7 truncated power the
multinomial coefficient is a falling factorial divided by e0!e1!e2!.
A factor7 in this denominator is possible ONLY for the pure L^7 term.
If d=0,1,2 counts these possible factors in a product, and w is its X,Y
weight, then

    coefficient valuation >=-d,       w<=15-7d.         (6)

The logarithmic-derivative coefficients are integral by formal inversion.
Monic division by s-1 and the polynomial divided difference at s=t preserve
this termwise bound: they only add integer polynomial multiples in s,t,
without changing X,Y monomials or introducing numerical denominators.
Thus (6) applies to C, with the same labelled summands even if coefficients
subsequently combine.

At t=1+epsilon and s=1+2epsilon, each coefficient difference from t=s=1
is epsilon times a polynomial with the same bound. Since
v(X^iY^j)=-(2i+3j)/7, equation (6) proves

    v(pi^15*C(2t-1,t))>=0,
    residue(pi^15*C(2t-1,t))=residue(pi^15*C(1,1)).     (7)

The discarded difference has valuation at least l>0. This proves the
required divided-coefficient control for every l>=1; it is not an inference
from the rational factor epsilon^2 or from the old degree-eight K alone.

## 4. Complete derivative trace, including the factorial carries

Put q=z^3+z^2+Xz+Y and A_h=z^7 T_h(1/z). The universal identity
beta(s,t)=-Tr(z A_s A_(t+3-s)) follows from
det(I-u M_z)=phi(u) and its formal logarithmic derivative. This is an
identity of multiplication matrices over a free rank-three algebra, not
an assumption about distinct roots. At h=1, A_1=z^4 q. From (3),

    C(1,1)=Tr(z A'_1 A'_3)-(1/2)Tr(z A''_1 A_3),       (8)

where primes differentiate the exponent h. The term containing A_1 itself
vanishes modulo q. Thus (8) is exactly half the second s-derivative of
beta(s,1) at s=1, not a guessed second-order source expansion.

Use Z=pi*z. The scaled cubic reduces to Z^3+xZ+y. The reductions of
pi^7 A_h and its exponent derivatives have two possible contributions:
their linear-coefficient-zero weight7 part and the pure-linear u^7
coefficient with its factorial7 denominator. Every other term is higher
valued, by the same multinomial count as (6).

For the first part, direct monic reduction in the depressed cubic gives

    A_h=(h-1)(h-2)*[xy Z^2+(y^2/2+(h-3)x^3/6)Z
                              +(h-1)x^2y/2].           (9)

For the second part the exact rational derivatives are

    binom'(1,7)=-1/42,
    binom'(3,7)=-1/140,
    binom''(1,7)=11/180.

For example the last is twice -1/42 times
1-1-1/2-1/3-1/4-1/5=-77/60. After multiplication by7, the residues of
these three constants are respectively1,1,0. In particular neither of the
two first derivatives can be treated as an integral-coefficient derivative
with its constant term discarded.

Differentiate (9), apply x^3=3y^2 and x^2y=2 from (2), and include these
constants. With a=xy,b=y^2, the four reduced polynomials are

    R1 = residue(pi^7 A'_1)  =6a Z^2+4b Z+1,
    R3 = residue(pi^7 A'_3)  =3a Z^2+6b Z+2,
    R11= residue(pi^7 A''_1) =2a Z^2+5b Z+5,
    R0 = residue(pi^7 A_3)   =2a Z^2+ b Z+4.            (10)

In characteristic7, multiplying the explicit quadratics gives

    R1 R3-(1/2)R11 R0
       =2a^2 Z^4+(6a+4b^2)Z^2+5b Z+6.                (11)

The Z^3 coefficient is zero. Newton sums for the depressed cubic are
Tr(Z)=0, Tr(Z^2)=-2x, Tr(Z^3)=-3y and Tr(Z^5)=5xy.
Taking the trace of Z times (11) gives

    6xy^2+2y^5=5xy^2 !=0,                             (12)

because y^3/x=(x^2y)/3=3 in the residue field. Equations (7)-(12) prove

    residue(pi^15*C(2t-1,t))=5xy^2 !=0.

Therefore v(C)=-15/7; (5), with2 a 7-adic unit, proves (1). All roots
have the same nonzero-form conclusion; neither a real embedding nor a
single septic factor was selected.

## 5. Controls, consequences and exact scope

An arithmetic control is visible in (10): dropping BOTH first-derivative
factorial carries changes the final trace from5xy^2 to3xy^2. The difference
is2xy^2, obtained by tracing Z times the sum of the two nonconstant
derivative polynomials. Even though this mistake happens not to change
nonzeroness here, it gives the wrong initial coefficient and is not used.
The accepted undeﬂated initial cancellation is consistent with (1), but it
could not justify (7) without the exact monic quotient and bound (6).

The traditional six-root formula retains a (7!)^-2 coefficient and a
factor (t-1)^2. Nothing in this proof declares its degree-eight quotient
integral. As a posterior consistency check only, (1) and that formula
would give valuation -1/7 for K_r(2t-1), since the remaining rational
factors are units here and v((7!)^-2)=-2. Thus pretending that quotient
is integral would contradict, not prove, the computed answer.

At every actual r=3 modulo7, no root of P is a zero of B. Since U is a
unit, gcd(P,U^7 B(t,X,V/U))=1 over Q. A rational Bezout identity therefore
gives B inverse in the whole leading algebra, and the inverse survives
arbitrary base change, including nonreduced ones. This is an existence
proof, not a computed coefficient certificate. Irreducibility was available
but was not substituted for the required nonzero scalar calculation.

The requested family is fully covered, including every l=v_7(2r+1)>=1.
The complementary classes0,4,5,6 are not addressed. Neither the earlier
asymptotic theorem nor the present result supplies an effective all-r cutoff
or a source exclusion. No new computation, code change, residue farm,
worker, further task, canonical OPEN or execution authority is selected.

## Reads and publication

The five specified mathematical texts were freshly pinned and read WHOLE:
the previous two-family report, its ROOT FIRST intake, the reduction note,
the mixed-scalar gate and the old septic irreducibility report. COORDINATION
uses exact-byte prior personal WHOLE reuse from September12 20:05-20:14UTC,
with a fresh current pin. The optional reciprocal report was not opened;
the finite trace identity is reconstructed in section4. No linked text,
live peer, ROOT parallel file, outside reference or coefficient body was read.

Only text/hash/date/apply_patch and the unchanged finalizer were used. No
scientific interpreter/code/import/AST/syntax/test/CAS/dummy, network,
AWS/SSH, new agent, process control, protected tree, mirror or shared edit.
Own targets were absent. Own WHOLE/quantity/control/collision readback and
all input postpins precede the unique final marker; custody is the last
authored object. Final expected-manifest verification and actual IDLE UTC
are returned to ROOT. This is manual co-research, not its own FIRST or
promotion, and makes no REG/full-source/all-F10/JC2 claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9863`.
- Body SHA-256:
  `d33228a82320e8d74790271684d6c950096c1db16b92ccba1ae18eab9acd9cbb`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
