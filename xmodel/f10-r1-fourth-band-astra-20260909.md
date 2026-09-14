# F10 r1 fourth band: global ell-column elimination

2026-09-09. NEW producer-only manual discriminator, pending independent
review. First action17:44:10 UTC; controlling cap17:56:10 UTC. ZERO mathematical
subprocesses. Only the three explicitly charged accepted reports were read
WHOLE, after exact current hashes matched; their paths/read scopes are in
input-pins.json. No earlier-band theorem or specialization is a premise.

## 1. Exact scope and conclusion

Use accepted16r's complete r1 Euler presentation, and accepted17b's retained
leading algebra

    B=Q[v]/(p(v)), Lambda=B[s,s^-1],
    F=v/(w*s), H=1/(w*s^2), a=1/(w*s^3),
    w=R(v)/(112L(v)).

Here p,L,R,w and f5 are exactly those of the accepted univariate report/gate;
L,w,f5 are units. Keep u,d0,v0,v1,k1,k2,k3 independent. In particular this
report imports NO first-, second- or third-band elimination. The two literal
rows [S^4]E1 and [S^5]E0 are

    Acol*ell+P=0, Bcol*ell+Q=0,                 (1)
    Acol=8a-44FH/15+8F^3/15,
    Bcol=8aF/5-5H^2/3+4F^2H/15.

P,Q are the full ell=0 rows, with every other parameter retained. They are
specified without ambiguity by the finite rational recurrence below, not by
discarding cross-band forcing. The column (Acol,Bcol) is unimodular over ALL
Lambda. Section4 gives a literal finite determinant/adjugate leftinverse,
without selecting an irreducible factor or dividing an arbitrary product-ring
coefficient. Consequently ell can be eliminated losslessly, replacing these
two rows by one compatibility while substituting into EVERY other row. This
is not a source point, inconsistency proof, emitted row set or runtime claim.

## 2. Full affine response, not a homogeneous truncation of the source

Use different symbols for the compact coefficient polynomials:

    d=d0+FS, h=1-u*d+S*(v0+v1*S+H*S^2),
    f=S*d-u, k=k1*S+k2*S^2+k3*S^3+a*S^4,
    A=S*t^3+f*t^2+h*t+k.

A is independent of ell. Accepted16r reconstructs B5=S^2 and B4,...,B0 using
E_j=j-3S*d/dS, fixed rational inversions, beta=gamma=0. Its target coefficients
are exactly

    (delta0,...,delta7)=
    (1,u,-ell,ell*u-1,2u-ell*S,-u^2-2S,2uS,-S^2).

The reconstruction is linear in this target for fixed A. Therefore the ENTIRE
mate, not just a leading piece, is affine in ell. Let W_j=partial B_j/partial ell.
Differentiating the complete recurrence gives directly

    W5=W4=W3=0, W2=S,
    W1=-u+(2F/5)*S^2,
    W0=(v0/3-7uF/15)*S
          +(v1/2-F*d0/5)*S^2
          +(25H-4F^2)*S^3/45.                 (2)

Details fixing the constants/signs: E2 W2=-S, whose eigenvalue on S is-1.
E1 W1=u-2f'S+2f=-u-2F*S^2, with eigenvalues1,-5. Finally

    E0 W0=-1-f'W1+2fW1'-2h'S+h
          =(7uF/5-v0)S+(6F*d0/5-3v1)S^2
                              +(4F^2/5-5H)S^3.

Divide the last three coefficients by-3,-6,-9, respectively. Its constant
coefficient is zero; gamma=0 fixes W0(0)=0. No division by u, d0, v0, v1 or
any previous-band coefficient occurred. All original target terms remain in
the ell=0 reconstruction, including -u^2*t^5 and the constant target1.

The exact low residuals are those of16r:

    E1=2k'B2+h'B1-hB1'-2fB0'-u,
    E0=k'B1-hB0'-1.

Hence their ell derivatives are obtained by replacing each B_j with W_j.
The degree envelopes in (2) show that the highest S coefficients in these
derivatives are precisely Acol at S^4 and Bcol at S^5. For example

    [S^4]partial_ell E1
      =8a+(6FH/5-4FH/5)-2F(25H-4F^2)/15,
    [S^5]partial_ell E0
      =8aF/5-H(25H-4F^2)/15.

This proves (1) with no conditions on earlier parameters. An independent
homogeneous check uses theta=t/S, Cbar=theta^3+Ftheta^2+Htheta+a and
V=theta^2+(2F/5)theta+(25H-4F^2)/45. Then

    4Cbar*V'-3Cbar'*V=-theta^4+Acol*theta+Bcol.

The theta^5 coefficient first forces V3=0. This is the ell derivative only:
the FULL weight-five target is -u^2*theta^5-ell*theta^4, and lower-band pair
products still enter the full P,Q. They have not been asserted zero.

Literal finite definition of P,Q: run16r's displayed recurrence with the
displayed f,h,k and all delta_j at ell=0, taking beta=gamma=0, to obtain B_j^0;
then take [S^4](2k'B2^0+h'B1^0-h(B1^0)'-2f(B0^0)'-u) and
[S^5](k'B1^0-h(B0^0)'-1). All operations are bounded polynomial coefficient
projections and fixed rational inversions. This is an exact formula retaining
all cross terms; no expanded row artifact or coefficient computation is claimed.

## 3. The column has no leading-field zero

We independently verify the root-suggested rank test using only the accepted
leading recurrence. Suppose both column entries vanish in a characteristic-zero
field point of the guarded leading algebra. If F=0 then Acol=8a!=0, impossible.
Thus F!=0 at such a hypothetical point. Put z=H/F^2, kappa=a/F^3. The equations
give

    kappa=(11z-2)/30,
    q(z):=125z^2-64z+8=0.                     (3)

This temporary leading-coefficient rescaling is solely a contradiction test;
it is not a normalization imposed on the full source. Let d_i=D_i/F^i for
the accepted leading D recurrence. Then

    d1=6/5, d2=(12+65z)/45,
    d3=(686z-84)/585,
    d4=(21125z^2+3912z-1224)/49725
       =(14728z-2576)/49725 mod q.

The first expression for d4 follows from
17d4=-6d3+5z*d2+16kappa*d1; the second uses125z^2=64z-8.
Also21d5=-10d4+z*d3+12kappa*d2. Therefore the necessary leading equation
q7/F^7=7z*d5-4kappa*d4=0 implies

    (4-72z)d4+5z^2*d3+60z*kappa*d2=0.

Multiplying by49725 and reducing only the displayed d4 gives the necessary
polynomial congruence N(z)=0 modulo q, where

    N=(4-72z)(14728z-2576)
         +425z^2(686z-84)+2210z(11z-2)(12+65z)
      =1871700z^3-1091696z^2+191344z-10304.

The scalar relation is15*(q7/F^7)=N/49725 modulo q; thus no zero scalar has
been cancelled. Hand reduction by125z^2=64z-8 and
15625z^3=3096z-512 gives

    N = (1200/15625)*(42471z-23012) mod q.     (4)

For an independently checkable arithmetic checkpoint, the reduced constant
numerator is
-1871700*512+1091696*1000-10304*15625=-27614400;
the linear numerator is50965200. Both are exactly1200 times the integers in
(4). The discriminant of q is96, not a rational square. Thus q is irreducible
over Q and cannot share a root with the nonzero rational linear polynomial
42471z-23012. Equations (3)-(4) contradict q7=0 over every characteristic-zero
extension field. This is a hand remainder argument, not a computed resultant,
factorization, numerical root comparison or branch sample.

The accepted leading algebra B is finite over Q. Its every residue field is
characteristic zero and gives the exact guarded leading solution. Consequently
the two column entries cannot vanish together on any factor. This argument
does not require choosing a factor or assuming it is real, and it would also
establish the ideal claim without a reducedness assumption.

## 4. Literal global finite leftinverse

For an explicit finite expression, define in B

    alpha=30w^2-11v*w+2v^3,
    beta=(24v-25)w+4v^2.

Then

    Acol=4alpha/(15w^3*s^3),
    Bcol=beta/(15w^3*s^4).                    (5)

Section3 implies (alpha,beta)=B, by the maximal-ideal criterion for a proper
ideal. This statement is global over the full finite product algebra; it
is not localization at one coefficient. Here is a literal finite leftinverse
recipe involving only fixed rational matrices, even if no coefficients are
expanded. In the basis1,v,...,v^6 of B let M_alpha,M_beta be multiplication
matrices, with columns the remainders of alpha*v^i and beta*v^i modulo the
fixed p for0<=i<=6. These are entirely specified rational7-by7 matrices:
w=R/(112L), with the inverse of L in B supplied by the accepted exact unit
identity. Define

    K=M_alpha*M_alpha^tr+M_beta*M_beta^tr,
    e=(1,0,0,0,0,0,0)^tr,
    rvec=M_alpha^tr*adj(K)*e/det(K),
    tvec=M_beta^tr*adj(K)*e/det(K).

The horizontal matrix (M_alpha M_beta) is surjective over Q because its image
is exactly the ideal(alpha,beta)=B. Thus it has full row rank. Over the real
numbers its rational Gram matrix K is positive definite: for nonzero x,
x^tr K x is the sum of squared norms of M_alpha^tr*x and M_beta^tr*x, and
cannot vanish. Hence det(K) is a NONZERO RATIONAL constant. This positivity
argument is on coefficient matrices, not an assertion that B's fields are
real. No arbitrary element of the product algebra is divided.

Let r0,t0 be the elements represented by rvec,tvec. The matrix identity yields
alpha*r0+beta*t0=1. Consequently the exact finite expressions

    lambda_A=(15/4)*w^3*s^3*r0,
    lambda_B=15*w^3*s^4*t0                     (6)

satisfy lambda_A*Acol+lambda_B*Bcol=1 in ALL Lambda. Equations (5)-(6), with
the fixed7-by7 determinant/adjugate specification, are a literal unexpanded
leftinverse, not a computed array of coefficients. They require no root choice,
generic pivot, factorization, or actual arithmetic subprocess. Evaluating that
formula is not authorized here and its size/performance has not been measured.

## 5. Lossless full-source substitution and controls

Let T=Lambda[u,d0,v0,v1,k1,k2,k3]. Put

    ell_star=-lambda_A*P-lambda_B*Q,
    compatibility=Bcol*P-Acol*Q.              (7)

In T[ell], the pair of rows(1) is equivalent to
ell=ell_star and compatibility=0. Indeed substituting ell_star into the first
row gives lambda_B*compatibility, and into the second gives
-lambda_A*compatibility. Conversely the leftinverse applied to(1) forces
ell_star. This is an exact quotient-ring isomorphism, not just field-point
coverage: replace the two rows by compatibility and substitute ell_star into
EVERY other retained residual. All earlier parameters and all other residual
rows are retained; the top/guard restoration stays exactly as17b. No earlier
row is assumed solved. Starting from the formal17 retained slots, this single
operation leaves16 formal equations; no nonzero-row count was measured.

Changed-object control: omit the leading ODE and take the field Q[z]/(q),
F=1,H=z,a=(11z-2)/30. Here a,H are nonzero: q(0)=8 and q(2/11)=60/121.
Both column entries are zero by (3), but q7 is nonzero by (4). Thus treating
unimodularity as a free coefficient identity without the accepted leading
equations would be false. This control is NOT a compact source point and no
claim is made about its missing full leading/boundary guard conditions.

A second scope control is(2): lower coefficients u,d0,v0,v1 really occur in
the ell response. Keeping only V while asserting all full affine forcing
vanishes would drop these terms and the ell=0 target contributions. Equations
(1),(2),(7) instead retain them exactly. Neither ell_star nor a leading point
solves the remaining residuals automatically.

## Completion and own checks

PROVED producer delta: exact affine column, its global unimodularity, finite
unexpanded leftinverse and lossless one-variable elimination at the stated
full-source interface. No higher band, numerical solve, source exclusion,
speedup or runtime authorization follows. The P,Q definition is complete but
unexpanded; no source coefficient artifact was read or emitted.

Pending quantity: one independent review of the hand remainder, affine
response and matrix leftinverse. Cheapest test: manual replay of (2)-(7) at
the same literal accepted scope. Zero matrix entries or retained rows were
computed as artifacts. No new OPEN identifier is introduced. Own WHOLE report
read and own raised-OPEN/scope check precede the marker. The only inputs are
the three pinned reports; no provenance followers, live reviews, earlier-band
reports, network, process inspection, code or mathematical subprocesses were
used. Terminal custody and expected transaction follow with all writers IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11614`.
- Body SHA-256:
  `8c1a4b6985e91ac4ff32eeb22ec2cc7a426d3f3a52e0cc3b88b04fb5775206f6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
