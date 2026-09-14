# Nonlinear-output obstruction on a one-sided Newton wedge of plane graphs

ROOT, September12,2026. MANUAL / PRODUCER-CHECKED candidate pending
different-model review. Research began01:08; transaction opened01:18:50;
publication reserve01:37/HARD01:40 was first banked01:26, not earlier.
No code/CAS/scientific execution. This is not a JC2 resolution.

## Statement and proof

Over C fix the explicit polynomials

    P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
    Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
    R=2x-3x^2 y-x^3 z.

For ANY K in C[w,v], take H(x,y)=y^2 K(xy,y) and restrict to the entire
graph z=H(x,y), writing p,q,r for the restrictions. Equivalently, every
nonzero monomial x^i y^j in H has j-i>=2: write it as
y^2 (xy)^i y^(j-i-2). There is no degree bound on K or on target outputs.
Let B=C[p,q,r] inside C[x,y], and J(f,g)=f_x g_y-f_y g_x.

CLAIM GRAPH-WEDGE-1:

    (B J(p,q)+B J(p,r)+B J(q,r)) intersect C = {0}.       (1)

Consequently, for every polynomial target map G:C^3->C^2, the two
components of G(p,q,r) do not have nonzero constant plane Jacobian.
Indeed Cauchy--Binet expresses their Jacobian as a combination in (1),
whose coefficients are evaluated polynomial target derivatives. No
converse of this necessary module condition is used. In particular B
need not be a polynomial ring or have independent generators.

Suppose instead that a constant c0!=0 has an expression

    c0=A(p,q,r)J(p,q)+B1(p,q,r)J(p,r)+C1(p,q,r)J(q,r),   (2)

with A,B1,C1 in C[U,V,W]. Fix any such representatives once and for all.
At the actual source origin, H has zero first jet, so

    (p,q,r)(0,0)=(0,0,0),
    (dp,dq,dr)(0,0)=(0,dy,2dx),
    (J(p,q),J(p,r),J(q,r))(0,0)=(0,0,-2).

Therefore C1(0,0,0)=-c0/2. The obstruction comes from other source
sequences whose target has this SAME limit, not from allowing arbitrary
source-dependent coefficients in (2).

On x!=0 put t=x^-1, w=xy, so x=t^-1 and y=tw. Set

    T(t,w)=t^-2 H(t^-1,tw)=w^2 K(w,tw),
    k(t,w)=2-3w-T(t,w),
    a(t,w)=(1+w)^3 T+w^2(1+w)(4+3w),
    b(t,w)=w+3(1+w)^2 T+3w^2(4+3w).

These are genuine polynomials in t,w. Direct substitution, retaining
all H derivatives through this coordinate change, gives

    p=t^2 a,      q=t b,       r=t^-1 k,
    b=4w+6-3(1+w)^2 k.                                (3)

For the second identity substitute T=2-3w-k. The k-free terms expand
to4w+6. Define h(w)=K(w,0) and

    k0(w)=k(0,w)=2-3w-w^2 h(w).

Then k0(0)=2 and k0'(0)=-3, so D=deg k0>=1. No genericity, nonzero h,
or fixed degree of k(t,.) is assumed.

For each root alpha of k0 there exist t_n!=0, t_n->0 and w_n->alpha
with k(t_n,w_n)=0. Here is the precise continuity fact needed. Around
alpha choose arbitrarily small circles with no k0-zero on the boundary
and no other distinct k0-root inside. On each circle, k(t,w) converges
uniformly to k0(w) as t->0, so Rouche's theorem preserves the positive
number of interior zeros counted with multiplicity. Choose a nonzero
t_n sufficiently small for the nth circle and an interior zero w_n.
Shrinking circles and |t_n|<1/n give the assertion. This works equally
for multiple roots and for a drop in polynomial degree at t=0. It needs
no Puiseux expansion or differentiation of w_n.

Along this sequence, (3) gives (p,q,r)->(0,0,0). All polynomial
expressions in a,b,k and their t,w partial derivatives stay bounded.
The exact differential identity dx wedge dy=-t^-1 dt wedge dw gives

    J_xy(f,g)=-t(f_t g_w-f_w g_t).

Writing all partial derivatives before taking limits yields

    J(p,q)=-t^3[(2a+t a_t)b_w-a_w(b+t b_t)],
    J(p,r)=-t[(2a+t a_t)k_w+a_w k-t a_w k_t],
    J(q,r)=-[(b+t b_t)k_w+b_w k-t b_w k_t].             (4)

On k(t_n,w_n)=0 the first two minors tend to zero, while the last
tends to -b(0,alpha)k0'(alpha)=-(4alpha+6)k0'(alpha).
Polynomial target coefficients in (2) tend to their values at the
target origin. Thus (2), together with C1(0)=-c0/2, forces

    (4alpha+6)k0'(alpha)=2                            (5)

at EVERY root alpha of k0. A repeated root would have k0'(alpha)=0,
immediately contradicting (5). Hence k0 is squarefree. The polynomial
L=(4w+6)k0'-2 vanishes at every root of k0 and is divisible by k0.
Its degree is D, and its leading coefficient is4D times that of k0,
so the exact polynomial identity must be

    (4w+6)k0'(w)-2=4D k0(w).

At w=0 this reads -20=8D, impossible for the positive integer D over C.
This contradicts (2) and proves (1), including all higher-weight
perturbations. The only analytic import is the standard Rouche theorem
used in the explicit local root-continuity argument; all other steps
are polynomial substitution, the chain rule and factorization over C.

## Controls, prior interface, provenance and limits

For H=0, k0=2-3w and its unique root is2/3. Along r=0, t->0,
w=2/3, equation(4) gives J(q,r)->26, whereas its value at the source
origin is-2. The other two minors tend to zero and also vanish at that
origin. The same C1(0) cannot turn both tuples into c0!=0.

For H=y^3+y^4, a genuinely nonhomogeneous-weight example absent from the
older homogeneous family, T=t w^3+t^2 w^4 and k=2-3w-t w^3-t^2 w^4. Again k0=2-3w,
so the same -2 versus26 conflict follows from the nearby roots. The
proof does not require H itself to be homogeneous or bound its higher
terms. These controls are manual exact substitutions, not CAS runs.

On the alternative plane x=0, parametrized by(y,z), the three original
polynomials restrict to(z+4y^2,y,0). The first two have Jacobian-1.
Thus neither all embedded planes nor all graph orientations are excluded.
For an independent coefficient-ring sanity check, p=y^2,q=y,r=x gives
J(q,r)=-1. No blanket claim about three polynomial generators, graded
subalgebras or their Jacobian modules is being used.

If psi is a polynomial automorphism of the parameter plane, the chain
rule and its polynomial inverse imply J(psi) is a nonzero constant.
The transformed full module is J(psi) times psi^*M, where M is the
module in(1). Since psi^* is a ring automorphism reflecting constants,
the same obstruction survives this reparametrization. This changes
parameters on the same graph; it is not an arbitrary new source
embedding or a noninvertible parametrization.

The hypotheses in(2) are essential to THIS argument: A,B1,C1 are
polynomials in the target triple, so they approach a shared finite
value. Rational target coefficients with poles, arbitrary source
coefficients, or a change to the coordinate ring are not licensed.
Graphs with some monomial j-i<2 are not covered by this new proof;
no conclusion about them is inferred from a failed chart or a limit
that diverges. All conclusions concern the entire polynomial graph,
not a punctured source. The x!=0 chart is used only to test a supposed
global polynomial identity at finite source points and take limits.

Two exact prior interfaces have been separated:

* The promoted September6 theorem covers ALL polynomial H but only
  constant linear output projections (plus translations). Its distinct
  leading-minor degrees cannot forbid cancellation by nonlinear target
  coefficients. Its proof and Sol gate were freshly read WHOLE here.
* Astra's terminal September12 co-research covers all H=y^2 h(xy), with
  arbitrary polynomial outputs, by the exact grading wt(x)=-1,wt(y)=1.
  The identities B_0=C[qr,pr^2], B_-1=rB_0, B_-3=r^3B_0 force the same
  root equation after projection to weight zero. It does not check the
  present higher-weight extension. ROOT read its report, manifest and
  PINS WHOLE only after terminal custody-FIRST and expected verification.

The new wedge/all-output statement and old all-H/linear-output statement
are complementary, neither subsumes the other. The wedge statement does
subsume the new homogeneous-only theorem. Bounded history checks of
the old exact proof/gate, AUDIT17(tttttttttttt) and scoped report-text
searches did not locate this nonlinear-output exclusion. This is an
identified campaign scope extension, NOT an external novelty claim or
a fresh whole-corpus checksum. No theorem here supplies a general
plane source exclusion, a complete S/T pair, or a missing Keller-to-source
implication. Global ranking and critical-path hypotheses are unchanged.

Pinned scientific/provenance inputs (post-read pins reconfirmed before
seal; old proof/gate also fresh-hashed before this continuation's WHOLE):

    xmodel/alpoge-polynomial-graph-obstruction-astra-20260906.md
    1ab4e6791e6a38fd9a8313161a546554a57efcf5207bc32d42dfa4b492dd8e21
    xmodel/alpoge-polynomial-graph-gate-sol56-20260906.md
    e710aa82b58ffc97bbc3cbf7026ec8b99e91f458ed40d0b5ab51deda828882d3
    xmodel/equivariant-graph-nonlinear-obstruction-astra-20260912.md
    4c253ddf7fd1cc6c5cfad90dbefec5f609a5ea2d4dcdb5a300b2feb35a94200d

The explicit displayed P,Q,R alone are proof premises. The historical
Alpoge/Zhang attribution and dimension3 counterexample announcement are
not validated or needed here. No source page, historical checker or
scientific code was executed during this deduction. The elementary
Rouche theorem is a named standard import, not a newly audited primary
paper. No protected-tree inspection, worker or new external lane was
used in producing this report. Documentary artifact transactions and
hash/text checks are not scientific execution.

QUANTITY: whether the stated full B-Jacobian module contains a nonzero
constant, proved not under the displayed wedge hypotheses, pending
hostile review. CHEAPEST TEST: manual check of substitutions, partial
derivatives, root continuity, repeated roots and coefficient-ring limits,
planned one15-minute Fable5.1 gate of this report plus terminal Astra.
No new canonical OPEN or unlicensed descendant is raised. Stop polynomial
output searches on these graphs only after the different-model gate;
do not initiate a blanket graph or ambient descent exclusion.

Publication uses the existing marker-last begin/close/finalize/verify
transaction. Input hashes and the complete partial are checked before
the final marker; no charge is made to clipped input or peer-live bytes.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10050`.
- Body SHA-256:
  `b8da6f4b8d34142691d017754b8ee7558827c6807177562b225d6ac6536120db`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
