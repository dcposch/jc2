# Remaining-class mixed-scalar local test

MANUAL co-research only. First action 2026-09-13 03:20:36.391550873 UTC;
original reserve03:37/HARD03:40 unchanged. No scientific execution or source
change. The live r3 review and its claimed valuation are not premises.

## Outcome and source boundary

For every actual r>=2 with

    r=19,26,33,40,47 modulo49,

the SAME mixed scalar B is a unit on the whole leading algebra; at every
7-adic leading point v_7(B)=0. This settles five infinite subfamilies inside
r=5 modulo7, not all four requested classes. In that class the remaining
residues are r=5 or12 modulo49. The classes r=0,4,6 modulo7 remain open.
No actual B-zero is produced.

The r=0 calculation below also gives an exact deflated leading cancellation
on the v(X)=-1/3 cluster, with both factorial carries retained. It identifies
a real missing next-order step, not an obstruction to all possible methods.
All new statements here are manual co-research requiring independent review.

Use phi=1+u+Xu^2+Yu^3, t=(5r+2)/(3r+1), T_h=trunc_7(phi^h),
B=[u^14](phi'/phi)T_(2t-1)T_(4-t). The accepted whole-source map and old
coordinate valuations are imported, not the old middle Z or H7-unit results.
For r=4,5,6, every X,Y is 7-integral by the charged final-residues report.
That assertion covers every root, even when a source unit has positive
valuation; it does not license deleting its zero residue.

## 1. Exact one-factor deflation for r=5 modulo7

Here t=3 modulo7. Put delta=t-3, e=delta/7 in Z_7, and use bars for
residue-field elements. Let s=2t-1 and b=4-t. Define the actual polynomial
divided difference

    R_b=(T_b-phi)/(b-1).

It is polynomial in b,X,Y because T_1=phi. Since [u^14]phi' T_s=0,

    B=-delta J,  J=[u^14](phi'/phi)T_s R_b.             (1)

This is a universal exact identity, before any source or residue reduction.
No division by a zero residue-field element is performed. All coefficients
of R_b have at most one factor7 in their denominator. Only its pure u^7
term can have that denominator. The derivative there at b=1 is -1/42,
so 7R_b reduces exactly to u^7 when b=1 modulo7. Every other coefficient
of 7R_b reduces to zero. Thus, with integral X,Y,

    residue(7J)=[u^7](phi'/phi)(trunc_7(phi^5)+2ebar*u^7)
               =3c8(5)+2ebar,                         (2)

where c_i(h)=[u^i]phi^h, now read in characteristic7. Indeed s=5+14e,
and the sole coefficient depending on its second 7-adic digit is the pure
u^7 coefficient, with carry2ebar. Also [u^7](phi'/phi)T_5=(8/5)c8(5),
which is3c8(5) modulo7. These are exact finite binomial identities.

The source d6=d7=0 at t=3+7e gives

    X^3+6XY+3Y^2=0,
    ebar=-3Y^2-3X^2Y.                                 (3)

In the second line the pure u^7 binomial term contributes ebar; its
coefficient7*binom'(3,7)=-1/20 is1 modulo7. No carry is omitted.
The finite coefficient c8(5) is

    3X^3+5X^4+6XY+4X^2Y+2Y^2+2XY^2.

Reducing it with the first relation (3) gives2XY+2X^2Y+XY^2.
Consequently (2), with both source relations retained, becomes

    residue(7J)=Y*((3Y-1)X+Y).                         (4)

## 2. All-root exclusion except two exact carry values

Suppose (4) vanished at a source residue. If Y=0, (3) forces ebar=0.
Otherwise put d=3Y-1. The second factor cannot vanish with d=0, so d!=0
and X=-Y/d, Y=(d+1)/3. Substituting into the first equation (3) gives

    (d-3)*(2d^2+2d+5)=0.                              (5)

If d=3, then (X,Y)=(5,6) and ebar=2. On the quadratic factor,
d^2+d-1=0 and its discriminant5 is a nonsquare in F_7. Direct substitution
into the second equation (3) yields

    ebar=-(3+d)/(1-d).

An ebar in F_7 is impossible: if ebar=1 the equality gives0=-4;
otherwise it makes d=(ebar+3)/(ebar-1) rational over F_7, contradicting
the quadratic. This argument allows arbitrary residue-field extensions.
Hence every root has nonzero (4) whenever ebar is neither0 nor2.

Write r=5+7n. Then ebar=2-2n modulo7. The excluded carries0,2 correspond
exactly to r=12,5 modulo49; all other five residues are the theorem's set.
There delta has valuation1, while (4) gives v(J)=-1. Equation (1) proves
v(B)=0 at EVERY root. The whole-ring Bezout criterion therefore gives B
inverse in S_r, persisting under every base change including nilpotents.

Controls: (X,Y,ebar)=(0,0,0) and(5,6,2) actually satisfy the residual
equations and make (4) zero. They are residual controls only, not actual
Qbar leading points, lift claims or scalar zeros. In particular Yd5 is
not assumed a 7-adic unit just because it is an accepted rational algebra
unit; excluding those residues by that mistaken implication is forbidden.
The precise remaining set inside r=5 modulo7 is as stated, with arbitrary
valuations of t-3 retained there rather than silently bounded.

## 3. A genuine divided-carry cancellation for r=0 modulo7

This is an obstruction to the first deflated valuation test, not a unit or
zero theorem for this family. Put delta=t-2=-r/(3r+1), k=v_7(delta)>=1.
At all roots in the old v(X)=-1/3 class, the charged source proof gives

    v(Y)=(k-1)/2>=0,       residue(7X^3)=3.             (6)

The other allowed X-valuation, -k, is not settled below; no claim that the
entire r=0 source is covered is made.

Define beta(s,t)=[u^14](phi'/phi)T_s T_(t+3-s). Independently form the
polynomial monic quotients

    Q=beta(s,t)/(s-t-1),
    D=(Q(s,t)-Q(3,t))/(s-3).

The first root is universal because T_2=phi^2. The second division is a
polynomial divided difference. On the source beta(3,t)=0 by the accepted
extra root, and 2-t is a nonzero rational. Therefore Q(3,t)=0 there, and

    B=2delta^2*D(2t-1,t).                              (7)

This uses neither the unreviewed r3 valuation nor an assumed integral K.
Each factorial7 pole in a beta term consumes a pure-linear degree7 block.
For d such poles, a term X^iY^j therefore has 2i+3j<=15-7d and coefficient
valuation >=-d. Monic divisions preserve this bound without new denominators.
When v(X)=-1/3,v(Y)>=0, its lowest possible valuation is-7/3; any term
containing Y is strictly higher. Replacing t,s by2,3 changes coefficients
by delta times the same bounded polynomials, also strictly higher.

Consequently, for rho^3=7 and x=residue(rho X), the residue of rho^7 D
can be found from D(3,2,X,0). This is half the second s-derivative of beta
at s=3,t=2. In the auxiliary cubic q=z(z^2+z+X), both A_2 and A_3 vanish
modulo q, where A_h=z^7 T_h(1/z). The universal reciprocal trace identity
therefore reduces the required derivative to

    D(3,2,X,0)=Tr(z A'_3 A'_2).

The z=0 factor contributes zero. Modulo z^2+z+X, the highest X-degree
part of A_h is F(h)X^3*(z+h-3), with
F(h)=(h-1)(h-2)(h-3)/6. Differentiation, INCLUDING the only nonintegral
pure-linear coefficient, gives

    A'_2=X^3*(-z+1)/6 +1/105 + lower integral X-degree terms,
    A'_3=X^3*z/3       -1/140 + lower integral X-degree terms.

Here 'integral' means 7-integral; the omitted coefficients have X-degree
at most2 and cannot enter valuation-7/3. The two constants are exactly
binom'(2,7) and binom'(3,7), not rounded or discarded.
Using Tr(z)=-1, Tr(z^2)=1-2X and Tr(z^3)=-1+3X gives

    D(2t-1,t)=-5X^7/18-11X^4/1260 + terms of valuation >-7/3.

The first coefficient includes BOTH the z and constant X^3 contributions.
After multiplication by rho^7 its residue is

    4x^7+2x^4=0,                                      (8)

because x^3=3 by (6). Thus the correctly deflated leading terms cancel
on this entire valuation class, for arbitrary k>=1. Equation (8) neither
proves D zero nor forbids a next-order calculation; it identifies exactly
what this first test fails to distinguish. Dropping the factorial term
would falsely leave4x^7 nonzero, and dropping the constant X^3 term in
A'_2 would give a different, equally incorrect initial coefficient.

## 4. Exact stopping boundary and controls

There is no all-four-family theorem here. The new mixed-unit subfamilies
are exactly19,26,33,40,47 modulo49. The remaining selected set is r=0,4,6
modulo7 together with r=5,12 modulo49. No proportional reduction of a norm
degree, effective largest exception or measured computational speed follows.

For r=4 and6, coordinate integrality alone does not justify coefficient
reduction after a parameter deflation. Even before deflation the pure u^7
term depends on the second parameter digit; one cannot replace every
T_h by phi^(h modulo7). Sections1-2 explicitly account for that digit only
for the chosen r=5 test. No uncomputed common-root claim for the other
two integral families is substituted for work not completed.

The smallest unclosed local quantity at r=0 is the first nonzero term
BEYOND (8), still retaining the actual source equations and the other
valuation class. In the r=5 exceptional carries, the missing issue is
whether the displayed residual common zeros lift to zeros of B or merely
positive valuations. The known one-shot rational Bezout/exception test
remains a possible global discriminator; no new farm or successor is
authorized. None of the residual controls is a source point or counterexample.

## Reads, workflow and authority

Current-pin WHOLE reuse: the two-family report, reduction and mixed-scalar
gate from this agent's completed03:02-03:12UTC task. Fresh WHOLE reads:
the old rzero report and final-residues report. COORDINATION uses the
same-agent September12 20:05-20:14UTC WHOLE read after current pin.
The optional resonance report and own r3 report were not opened or charged;
the monic divisions above are reconstructed directly. No live Fable or
ROOT parallel body, linked input, outside text or coefficient artifact was
read. Five mathematical texts plus COORDINATION are the complete census.

Only manual math, inert text/hash/date/apply_patch and the unchanged
administrative finalizer were used. No scientific interpreter/import/AST/
syntax/test/CAS, source code, network, AWS/SSH, process control, agent,
shared edit, protected tree or mirror action. Own targets were absent;
WHOLE readback, input postpins, own collision and quantity/control checks
precede the unique final marker. Custody is last, with expected-manifest
verification and actual ALL WRITERS IDLE in the terminal handoff.
This is not independent FIRST, theorem promotion, REG, source exclusion,
all-F10 or JC2. Stop at this exact partial mathematical endpoint.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10337`.
- Body SHA-256:
  `12c52e95c6aca84efa276fe7591d2c28f6610ad4d0ccfe6073dbba2d3ec14b67`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
