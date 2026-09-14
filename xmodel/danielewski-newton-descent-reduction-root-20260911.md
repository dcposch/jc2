# Newton homothety removes the opposite-end descent gap

ROOT manual source-interface reduction, September 11 2026.
INTERNAL/UNREVIEWED, conditional on the quoted classical Newton theorem.
No regular scalar pair, all-T exclusion or JC2 resolution. Original own
publication reserve 17:12 / HARD 17:15 UTC; no scientific execution.

For a genuine scalar pair on T, the two Laurent intervals are proportional.
Consequently an integral ratio gives a width-decreasing target shear without
a separate opposite-end bound. A target-automorphism-minimal pair must instead
have coprime ratio n/m with n>m>=2. Its endpoints have the form
[-mu,mv],[-nu,nv], with integers u>=2 and v>=1. The existing joint control
survives these restrictions, so this is a reduction of the missing hypothesis,
not a completed descent. In particular no separate opposite-end growth search
is warranted for a stipulated FULL scalar pair.

## 1. Exact object and the external theorem used

Let R=C[x,t,Z]/(t^2-1-x^2 Z), with omega=dx wedge dt/x^2 and bracket
{f,g}=x^2(f_x g_t-f_t g_x). Suppose H,G in R and {H,G}=c in C*.
In the two affine-plane charts put

    t=1+x^2 y,  Z=2y+x^2 y^2;
    t=-1+x^2 v, Z=-2v+x^2 v^2.

Both chart maps (H,G) have constant Jacobian c. Neither is an automorphism:
an inverse chart-coordinate polynomial in H,G would extend y=(t-1)/x^2
across the missing D_-={x=0,t=-1}, where it has a pole. The other chart is
symmetric. This also applies after every polynomial target automorphism.

The precise imported statement is [Gwozdziewicz, Theorem 2.1](https://arxiv.org/pdf/alg-geom/9305008):
for a plane Keller pair of degrees greater than one, its Newton polygons
with the origin included satisfy N(G)=(deg G/deg H)N(H). The same paper's
Theorem 1.1 makes a Keller map injective on a line an automorphism, and its
Lemma 2.2 handles a coordinate of degree at most one. We apply the printed
statements, not a fresh proof of their underlying references.

Every coordinate here is nonconstant on each of the lines D_+,D_- in the
appropriate chart. Indeed, a constant restriction of H would make the
restricted Jacobian a nonzero constant product of H's normal derivative and
G's tangential derivative. Both polynomial factors must be nonzero constants;
G is affine of nonzero slope on the line. The chart map would be injective
there and hence an automorphism, a contradiction. The identical argument
applies to the chart lines y=0 and v=0 and to G.

Write H=sum x^i p_i(t), G=sum x^j q_j(t), with respective intervals [a,A]
and [b,B]. Each interval has both signs. If H had only i>=0, its restriction
to D_+ would be constant; if only i<=0, its restriction to y=0 would be
constant since every negative p_i vanishes at t=1. The argument for G is
identical. Thus a,b<0<A,B, with no support or degree bound assumed.

## 2. Proportional intervals and a genuine finite shear step

Every monomial in x^i p_i(1+x^2 y) has (x,y)-weight i for the linear weight
L(r,s)=r-2s. A nonzero polynomial p_i remains nonzero under this substitution.
Different i cannot cancel in this grading. Including the origin does not
change the negative minimum or positive maximum. Hence

    min L on N(H)=a, max L on N(H)=A,
    min L on N(G)=b, max L on N(G)=B.

Newton homothety therefore gives, with lambda>0,

    b=lambda*a, B=lambda*A.                         (1)

The same argument works in the minus chart and gives the same lambda=B/A,
even if the ordinary degrees differ between charts. This is a consequence
for the FULL scalar pair, not for arbitrary commuting leading terms.

Suppose lambda=k is a positive integer. The bracket at weight A+B+1>0
has only the extremal pair and must vanish. Its coefficient is

    A p_A q_B' - B p_A' q_B=0.

Consequently q_B=d p_A^k for some d in C*, since the rational derivative
of q_B/p_A^k is zero. The global target shear G'=G-d H^k cancels weight B.
Every weight of H^k lies between ka=b and kA=B, so

    lo(G')>=b, hi(G')<B.

The mate is still regular and {H,G'}=c. It cannot be constant, zero or
one-sided by section 1. Thus the positive integer

    W(H,G)=(A-a)+(B-b)

strictly decreases. No equality of the two extremal cancellation constants
is needed. The lower endpoint need only avoid getting worse. An integral
reciprocal is treated by exchanging the coordinates, including lambda=1.

The previous Astra sufficient criterion correctly kept the opposite-end
bound as a hypothesis under weakened data. Equation (1) supplies it for
genuine scalar pairs. It is therefore no longer a separate global gap.
It does not supply integrality of lambda.

## 3. The honest minimal configuration and boundary lower bound

Choose, from the polynomial-target-automorphism orbit of a stipulated pair,
one minimizing W. This uses only well-ordering of positive integers, not
a classification or a promise that the next shear always works. Write
lambda=n/m in lowest terms and interchange H,G if needed. Section 2 forces

    n>m>=2, gcd(m,n)=1.

Equation (1) and integer endpoints then imply

    a=-m u, A=m v, b=-n u, B=n v,
    u,v positive integers.                         (2)

Restriction to x=0 in each chart reads off the corresponding vertical-axis
intercept of the Newton polygon. Since these restrictions are nonconstant,
homothety and coprimality give positive integers r_+,r_- such that

    deg(H|D_+)=m r_+, deg(G|D_+)=n r_+,
    deg(H|D_-)=m r_-, deg(G|D_-)=n r_-.

The global regularity criterion is P^ceil(-i/2)|p_i for negative i, where
P=t^2-1. A negative even block x^(-2k) P^k h(t) restricts on D_+ or D_-
to Z^k h(1) or Z^k h(-1). A negative odd block has an extra factor x and
vanishes there. Positive blocks vanish; weight zero contributes a constant.
Therefore deg(H|D_+),deg(H|D_-)<=floor(mu/2). It follows that

    1<=r_+,r_-<=floor(u/2), hence u>=2.              (3)

In particular W=(m+n)(u+v)>=15. This is an interval-width necessary bound,
not an actual-total-degree bound, a frontier certificate, or a proof of
existence at width 15. Arbitrarily high t-degrees remain unbounded.

## 4. Endpoint roots are regular, but not automatically squarefree

For the endpoints in (2), the two extremal commutation equations and UFD in
C[t] give nonzero scalars alpha_+,beta_+,alpha_-,beta_- and polynomials s,r
such that

    H_(mv)=alpha_+ (x^v s(t))^m,
    G_(nv)=beta_+  (x^v s(t))^n,
    H_(-mu)=alpha_- (x^(-u) r(t))^m,
    G_(-nu)=beta_-  (x^(-u) r(t))^n.               (4)

For example, commutation of the lower terms says p^n/q^m is a nonzero
constant. Every irreducible factor has multiplicities divisible by m in p
and n in q, since gcd(m,n)=1. Constants can be absorbed over C. The upper
calculation is the same. Both common roots in (4) are globally regular:
the upper one plainly is; if e is the multiplicity of t-1 or t+1 in r,
regularity of H's lower block gives me>=ceil(mu/2), hence the integer
e>=ceil(u/2). The exact global extension criterion therefore applies to
x^(-u)r(t). This is not merely a rational common-root assertion.

Regularity does NOT force that root to have a reduced zero divisor, or to
have geometrically integral generic fibre. Neither root is required to be
primitive with respect to further powers. If u=2, equations (3) force
r_+=r_-=1, and the lower root has the form Z h(t) with h(1)h(-1)!=0.
This conclusion follows because the degree-m boundary term can only come
from the lowest weight -2m and must survive on both boundaries. It does not
make h squarefree, provide a normal reference for the full pair, or cover
all u. No special u=2 follow-on is selected.

## 5. Surviving control, history and next-action consequence

The already banked pair, with A=x^2, U=xt, w=t^2,

    H=(A+Z)^2+U+w,
    G=(A+Z)^3+Z(5/2-2w)-UZ,

has intervals [-4,4],[-6,6] and both chart Newton polygons proportional by
3/2. It fits m=2,n=3,u=2,v=2 and r_+=r_-=1. Its lower common root is Z;
the upper common root x^2 is a proper power. On either D boundary the
restrictions are Z^2+1 and Z^3+Z/2, of degrees 2 and 3. All mixed moments
and the entire weight-zero bracket equation pass, but the weight-eight
bracket is -6x^8. Thus these new necessary restrictions still do not turn
the earlier control into a scalar pair or force an integer ratio.
The control's previously proved affine/single-shear minimality is NOT being
upgraded to minimality over its entire polynomial-automorphism orbit.

The classical homothety theorem already underlies this reduction. This is
an attachment and correction of the current missing-premise list, not a
new external theorem. It removes the independent opposite-end hypothesis
from the previous Astra criterion for FULL scalar pairs only. It leaves
the genuine nonintegral-ratio case and the full nonzero-weight equations.
Do not fund a separate opposite-end-bound proof or an integer-ratio scan.
No full reduction of arbitrary JC2 to T exists in these reports.

The parallel first-contact attachment task is separate. ROOT received its
interim warning about repeated divisors and an invisible normal remainder,
but did not read its live report. That warning is not a premise of sections
1--4, nor a completed or different-model review of this report. Its final
source-gap control must be collected and checked separately. No blind-round
or promotion status is implied by simultaneous Astra work.

QUANTITY decided: whether the opposite-end width bound needs an additional
proof once the FULL scalar identity is assumed. CHEAPEST TEST performed:
apply the printed Newton homothety to the exact linear weight i-2j and
retain all weights of the shear power; manual, no scientific subprocess.
Outcome: no separate gap there. The universal integer-ratio/descent step
remains unproved. No new canonical OPEN or automatic gate/worker/successor.

## 6. Read scope and pins

Own derivations began after the 16:51:54 UTC state check; publication opened
17:01:29. The two-page primary paper was freshly read WHOLE through web in
this turn. Its retained text had been read WHOLE in the preceding turn and
is reused at the identical pin; the local PDF is HASHONLY, not a new visual
inspection. The three earlier T reports were read WHOLE during their prior
ROOT intake, reused after current hash checks. Current pins:

    two-chart-interface-root: 9107e171cb1db948eabae96cad8961fbc3c1ceb6b8d8ddbe442c2381caed0033
    moment-extrema-root: f5958c163f48807e9811083e15e2788a99acca54862ebd4c06ffa1f6860c3071
    extremal-descent-astra: 28e548eb25230166390a567cf95b533bec207d2b09523412b86543717ddf05f8

Under box/d125-marked-fiber-global-discriminator-20260907/:

    gwozdziewicz-alg-geom-9305008v1.pdf: 4cce6a7334640ea47036b1fb8c676e28da7946dbd15d0a48868b30d94c68585a
    gwozdziewicz-alg-geom-9305008v1.txt: 906eeac29957c4c8a78481f7c212513e0a6551d9bf20239e9a0f22f6500d128f

The history check covered the named T reports and targeted canonical
Newton/first-contact/cokernel references, not the entire repository. ROOT
also read the uniform cone report WHOLE as exploratory comparison for the
separate source-interface task; no cone conclusion is imported here.
Targeted searches recovered the already-known BGV and conditional primary-
submodule sources. BGV's current arXiv record was read, while its large HTML
body failed retrieval; no new theorem was obtained or invoked. This is not
a broad sweep or a corpus-wide novelty claim.

All mathematical work is manual. No CAS, coefficient export, scientific
subprocess of any size, AWS allocation, external message, protected-project
access or shared instrument change. The report uses apply_patch and the
existing begin/close/finalize/expected-verify transaction. Final own WHOLE
readback, current postpins and documentary collision check precede sealing.

## COLLISIONS

KNOWN classical Newton homothety; new attachment to the current interval
gap only. No new OPEN identifier and no reopening of a closed family.

Documentary open_collision.py returned EMPTY (no explicitly raised OPENs).
This is not a mathematical verification or a novelty certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12006`.
- Body SHA-256:
  `29897702389cecc2d0c02f4467d9fea0b4f347b7fdef114f7ac3929fcf02832a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
