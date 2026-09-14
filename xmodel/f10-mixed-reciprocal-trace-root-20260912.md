# The mixed scalar as a reciprocal-cubic trace

ROOT, September 12, 2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
This is an exact alternative representation of the selected scalar, not a
unit certificate, measured speedup, source exclusion or JC2 result. No
scientific program was executed and no existing source was changed.

## 1. Universal finite trace identity

Work over any commutative Q-algebra K. Put

    phi(u)=1+u+X*u^2+Y*u^3,
    q(z)=z^3+z^2+X*z+Y,
    C=K[z]/(q).

For arbitrary polynomials T_1,T_2 of degree at most seven define
A_i(z)=z^7*T_i(1/z). Then the following is an identity in K:

    [u^14] (phi'/phi)*T_1*T_2 = -Tr_(C/K)(z*A_1*A_2).       (1)

Proof without a reducedness or root hypothesis: if M is multiplication by
z in the free basis (1,z,z^2), det(I-uM)=phi(u). The formal determinant
identity gives

    phi'/phi = -sum_(k>=0) Tr(M^(k+1))*u^k.

Multiplying by T_1*T_2 and extracting u^14 proves (1), because every exponent
15-i-j is positive for 0<=i,j<=7. All operations are polynomial identities
over Q[X,Y] and hence survive arbitrary base change and nilpotents. There
is no hidden inversion of Y or a discriminant in this universal statement.

Reduce z*A_1*A_2 modulo the MONIC cubic q to w_0+w_1*z+w_2*z^2. Newton sums
give Tr(1)=3, Tr(z)=-1, Tr(z^2)=1-2X. Thus the same scalar is

    -3*w_0+w_1-(1-2X)*w_2.                                (2)

This replaces the expanded logarithmic-derivative convolution by two cubic
remainders, a product/remainder and a three-entry trace functional. It does
not by itself reduce the remaining septic unit question.

## 2. The two actual powers are ordinary division quotients

Now impose the exact leading relations d_6=d_7=0, where
d_j=[u^j]phi^t and d=sum_(j=0)^5 d_j*u^j. Then phi^t=d modulo u^8.
Both series have constant term one, so multiplication and inversion give

    T_(2t-1)=trunc_7(d^2/phi),
    T_(4-t)=trunc_7(phi^4/d).                               (3)

Set D(z)=z^5*d(1/z), which is monic of degree five. The reverse polynomials
of these two truncations are exactly

    A=quo(D^2,q),     B=quo(q^4,D),                         (4)

where quo means ordinary polynomial-division quotient at infinity. Indeed
d^2/phi=u^7*D(1/u)^2/q(1/u), and the proper remainder contributes only
u^8 and higher; the second identity is identical with q^4/D. Both quotients
have degree seven. All divisors are monic, so (4) introduces no parameter
denominator or localization. Equations (1)--(4) compute the SAME actual
mixed scalar as

    B_r = -Tr_(C/S_r)(z*quo(D^2,q)*quo(q^4,D)).             (5)

Here S_r is the WHOLE leading algebra from the accepted septic interface,
not a chosen point or field factor; the cubic C is auxiliary over S_r.
It is not the separate degree-seven leading algebra itself. The identity
(3) is source-relative: the two quotient expressions must not replace the
unrestricted polynomial B(t,X,Y) without charging d_6=d_7=0.

## 3. What the source identity supplies, and what it does not

For actual r>=2 set m=3r+1, n=5r+2, c=Y*d_5, a known unit in S_r.
Reverse the accepted identity m*phi*d'-n*phi'*d=-c*u^7. Since 5m-3n=-1,
one obtains the exact polynomial identity

    z*(n*q'*D-m*q*D')-q*D=-c.                             (6)

Modulo q, n*z*q'*D=-c. Consequently z, q' and D are all units in C.
In particular the auxiliary cubic is finite etale and its trace pairing
is perfect, without selecting a geometric root.

For clarity, writing a,b for the coefficient vectors of A mod q and B mod q,
equation (5) is -a^T*G*b, where G_(i,j)=p_(i+j+1), 0<=i,j<=2, and

    p_1=-1,
    p_2=1-2X,
    p_3=-1+3X-3Y,
    p_4=1-4X+2X^2+4Y,
    p_5=-1+5X-5X^2-5Y+5XY.

Its determinant is -Y*disc(q): the ordinary trace Gram determinant is
disc(q), and multiplication by z has norm -Y. Thus G is invertible in the
actual leading algebra. This does NOT prove the distinguished pairing
a^T*G*b nonzero, much less a unit. A perfect bilinear form can pair two
nonzero vectors to zero. That is exactly the unclosed step, not an omitted
genericity assumption. No assertion that A or B is automatically a unit is
needed or made.

## 4. Direct checks and stopping boundary

Universal sign/shift check: take X=Y=0 and T_1=T_2=1. The left side of
(1) is [u^14](1+u)^-1=1. On the right q=z^2(z+1), A_1=A_2=z^7 and
Tr(z^15)=-1, giving 1. Dropping the factor z incorrectly gives -1. This
checks the universal formula only, not an actual leading source.

Matched old boundary: at t=5/3, phi=(1+u/3)^3 and d=(1+u/3)^5. Then
q=(z+1/3)^3, D=(z+1/3)^5 and both quotients in (4) equal (z+1/3)^7.
Their product is zero in C, so (5) returns the known B=0. This parameter
is no finite actual r, and q' is not a unit; the actual-source perfectness
argument has not been extended to it.

The concrete representation avoids building the fifteen logarithmic
coefficients used by the current producer and replaces rational-power
expansions by two monic divisions after taking the leading quotient.
Expanded support and the final all-r elimination may still dominate cost.
No performance measurement or smaller physical cap requirement follows.
The existing producer/checker, their accepted source scope and the stopped
worker attempts remain unchanged. Do not launch a new implementation or
review merely to turn this identity into another unused instrument.

The selected closing question remains whether this ONE distinguished scalar
is a unit on all seven leading components for every integer r>=2. No actual
zero or unit has been established. Even an affirmative answer would still
need the separate complete-source comparison and would not resolve JC2.

## Provenance and priority

Whole mathematical inputs: f10-mixed-univariate-reduction-root-20260912.md,
SHA256 7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8;
f10-mixed-scalar-unit-gate-fable5-20260911.md,
aa8b0148f8bfb63ef072b23106f92bafa703a6b83033984e17a62f49eb70230f.
The existing produce.py was read as static text, SHA256
8aee305b5fc32f0a20f2bb8ccfe01ac1c389c98594ea7724070e1badfae2abe0.
Current pins were reproduced; no execution/import was used as validation.
The old middle-septic producer was additionally read for its source etaleness
argument; (6) above independently supplies the needed cubic-unit deduction.

A targeted history check of f10 reports, APPROACHES, AUDIT, PROGRESS and
REDUCTION found no prior instance of this mixed-scalar reciprocal trace;
the live Astra report was explicitly excluded. This is not exhaustive
novelty evidence: Newton sums, trace functionals and polynomial division are
standard. Only their exact attachment to this scalar is claimed here.
ROOT sent the elementary residue observation and (3) to Astra as unreviewed
co-research inputs. No live peer report was read. A suggested proportionality
to the leading Jacobian times disc(phi) is only a conjectural discriminator,
NOT an identity, premise or result of this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6930`.
- Body SHA-256:
  `a8849f66f8208b350dac8f70d20097d73e4844297efce038940556ce89b0d6ff`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
