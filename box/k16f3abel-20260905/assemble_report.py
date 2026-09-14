#!/usr/bin/env python3
"""Bounded report assembly. Only --seal adds the completion marker and seal."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
REPORT = WORKSPACE/'xmodel/k16-f3abel-astra-20260905.md'
RECEIPT = WORKSPACE/'xmodel/k16-f3abel-astra-20260905.run.v2'

BODY = r'''# K=16 coefficient-sensitive polynomial Abel equation

Lane: `k16-f3abel-astra-20260905`. Date: 2026-09-05.

**PARTIAL. The all-t coefficient-sensitive polynomial solution theorem is
not proved. OPEN[K16-8.1-RADICAL] remains OPEN, and theorem (T) is not
promoted on the whole K=16 ray.** The report gives new uniform support and
collision-stratum exclusions, exact root-contact constraints with
multiplicities, and exact certificates on the maximally coincident-root
locus at the split indices t=11,26,47, on both factors. It does not turn a
formal Laurent nonresonance or a finite-index computation into the missing
global rigidity theorem.

There is a necessary correction to the requested negative control. For the
stated (F1)–(F3), **t=2,y=1/5 does force B W'(0)=0**. It is V0 that fails on
this fibre. The direct exact computation below proves this product belongs
to the residual ideal itself, and displays the free b-axis with B=eta=0.
Thus the instruction that the product “must NOT be forced zero” conflicts
with the equations and with the charged statement that (8.1) holds there.
The report preserves the exceptional fibre instead of altering (F3) to fit
that inconsistent expectation.

The principal uniform results are:

- The high coefficients of (F3) uniquely reconstruct W and B as polynomial
  functions of the translated coefficients of C and b. All scalar pivots
  are proved units for every t>=2 and both d. B and eta are affine in b.
- If the nonzero input weights do not generate both 2t and 2t+1 as an
  additive semigroup, then B eta=0. This excludes every nontrivial scaling
  stabilizer and explicit sparse C families, including repeated roots.
- On C=x^(t-1), the only normalized solution for t>=3 is
  b=B=eta=0, W=omega*x^(2t+1). An explicit cubic coefficient gives the
  obstruction and correctly vanishes at t=2.
- A polynomial factorization PH=R retains the linked A,D coefficients.
  On bB eta!=0, P and H are units modulo K; on B eta!=0, including b=0,
  the scheme-theoretic intersection of C and PH has length at most three.
  Exact contacts modulo C^2 and K^2 retain all root collisions.
- The only possible integral infinity resonance occurs at the split
  indices t=3m^2-1. For d=-m it is the residual coefficient of x^(6m-2);
  this locates a compatibility equation, without proving its obstruction.

## 1. Frozen custody and scope

Before mathematical work, all ten frozen files in
`/tmp/jc2-lane.zx9GKm/inputs` were verified. The manifest was generated
mechanically from `xmodel/k16-f3abel-astra-20260905.run.v2` with awk pairing
`charged_input_<i>_basename` and `charged_input_<i>_sha256`, and
`sha256sum -c` returned ten OK results. No hash digit was retyped. The
durable manifest is `box/k16f3abel-20260905/inputs.sha256`.

The mathematical sources are the four frozen charged reports and the
frozen Python drivers, with `FALLACY-v2.md` as the reasoning guardrail.
The charged Abel report, especially Sections 1–5, 8, and 10, supplies
the normalization and reconstruction equivalence. The rank, BRCR, and
hsop reports supply their explicitly conditional structural statements
and the banked finite ranges. No other lane's report, ledger, jc2-lean,
or ideation file was read or edited. No external classification theorem
is imported. New drivers, certificates, notes, and logs are confined to
`box/k16f3abel-20260905/`; the report is the only new xmodel body.

A skeleton was written after hash verification and before calculations.
Exact CAS was run in foreground processes under `timeout` and
`stdbuf -oL`. Each CAS job used one core; the lane remained below the
five-core ceiling. No daemon or unattended background search was used.
The marker and seal are completion-only, not present in the skeleton.

## 2. Exact statement, coefficient fields, and dependency to (T)

Set

    q=2t+1, e=3t+1, 3d^2=t+1,
    y=(d+t+1)/(2q),
    g=e*t*(3d+2t+2)/(6q^3), alpha=3/(4y^2),
    omega=3(2d-1)/(4y^2(4t+1))=1/(4y^2(2d+1)).

Fix t>=2. Work over an algebraic closure k of a field factor of
`A_t=Q[d]/(3d^2-t-1)`. If this algebra splits, all assertions are made
on both factors separately; a nonzero element of a product algebra is
never treated as a unit without the factorwise check. For integer t,
the split indices are exactly t=3m^2-1, d=+m,-m, m>=1. The quantities
y,g,alpha,omega,d used as divisors are units on every permitted factor.
For y and g this follows, for example, from the charged nonzero norms

    N(y)=(t+1)(3t+2)/(12q^2),
    N(g)=t^2(t+1)(3t+1)^2(4t+1)/(36q^6).

Use translated x=L=h-b4. Write

    C=x^(t-1)+c1*x^(t-2)+...+c_(t-1),
    W=omega*x^q+w_(q-1)*x^(q-1)+...+w1*x-B,
    eta=W'(0)=w1, r=b^2/4,
    K=x^2 C-yb, A=alpha*x^3 C^2, D=3b*x*C/(2y).

Here c_j are the translated C coordinates, not split-tail coefficients;
b=b3 and B=b2. A prime in this report means d/dx when attached to a
polynomial, not a label. The exact equation is

    2(xW-r)W' = W^2+(B-2A+D)W+A(A-D)/3-B(A-D)
                 -b*eta*K/(2y)-B*eta*x
                 +(2rA-4r(B+W))/x.                         (F3)

The quotient is polynomial since x divides A and B+W. No division by a
root, b, C, W, or xW-r is part of this statement. Let F denote its left
side minus its right side. The sought assertion is

    for every t>=3 and both d, F=0 implies B*eta=0.         (PS)

The charged translated-coordinate theorem identifies

    R_t=k[c1,...,c_(t-1),b]
       =k[b4,u2,...,u_(t-1),b3]

by a global triangular polynomial map using scalar units only. Its
weights are `wt(c_j)=j`, `wt(b)=t+1`. In particular c1 is a unit scalar
multiple of b4 and c_(t-1)=C_h(b4). These are actual coefficient
coordinates, rather than a generic-root chart.

For clarity, the charged reconstruction behind the equivalence is
recalled explicitly. Define T by

    2y*T'=g(5C+3xC'),

and set

    U'=y(2xW'-W-B)/(3x)
          +x^2 C(5C+2xC')/(4y)-bC-(b/2)xC',
    S=g(W+B)/x-3g*x^2 C^2/(4y^2)+gbC/(2y)+xCT/y,
    F_aux=xT-gb, Y=xS-bT-gB, b1=-b*eta/3,
    V'=(ygb1-KY'+K'Y+2U'F_aux)/(2yx).                    (REC)

Every displayed division by x has zero constant numerator. In the last
one this follows from U'(0)=y*eta/3-bC(0) and
Y'(0)=g*eta-2gbC(0)/y. The leading coefficients are exactly q, g2, g1,
and e in the charged normalized spine. Integrate U', translate to the
unique U gauge with its h^(q-1) coefficient zero, and fix the additive
constant. The T integration gauge fixes the prescribed V' coefficient
with the nonzero scalar pivot q/y. Thus all normalized ansatz shapes
are recovered. The banked high-spine uniqueness identifies this
reconstruction with the terminal residual point.

The charged identities, now with explicit constant shift, are

    R_boundary=U_h'(b4)+b3*C_h(b4)=y*eta/3,
    tau=T_(t,0)-yg,
    tau+g*b2*R_boundary=-sum_(k>=1) b4^k*T_(t,k),
    tau=-(gy/3)*B*eta on V(I_(t,+)),
    I_(t,+)=(T_(t,1),...,T_(t,2t-1)).                    (DEP1)

The independent coefficient recurrence below gives the same F3 solution
functor. In the original residual coordinates the charged row-image
identity is

    gy*F(x)+3x*(D0(x+b4)-D0(b4))=0.

Translation is triangular on the nonconstant coefficient rows and
multiplication by x shifts their indices. This identifies the positive
row ideal after high elimination; it is not an inference from equal
dimensions or from matching variable names.

Consequently the complete dependency chain, at each fixed t, is

    (PS)
      <=> B*eta vanishes at every geometric point of the normalized
          F3 solution scheme
      <=> tau in radical(I_(t,+))
      <=> 1 in (I_(t,+),1-z*b2*R_boundary) in S_t[z]
      <=> (I_(t,+),T_(t,0))=S_t                         [(8.1)]
       => terminal normalized receiver chart has no solution
       => original K=16 ray system has no solution, by the banked
          constant spine, normalizer lemma, and second affine spine
       => theorem (T) at t.                              (DEP2)

The equivalence with (8.1) uses the weighted cone lemma, not V0: if tau
is nilpotent modulo I+, then yg+tau has a finite geometric-series
inverse. Conversely a cone point with tau nonzero can be rescaled by
a weight-4t+1 scalar to make tau=-yg, contradicting that unit ideal.
Literal T_(t,0), whose constant is yg!=0, is never substituted for tau
in a radical assertion. No zero-dimensionality, CM, or DVR hypothesis
is needed for this weaker route.

A proof of (PS) for every t>=3 would complete this chain and promote
(T) on the whole K=16 ray: that would be a **MAJOR, NOTIFY-WORTHY
milestone**. It is not achieved here. The banked characteristic-zero
range is t=2 on both factors and t=3,...,7; the current exact full-cone
controls independently cover t=2,3,4. The structural slice results below
do not promote (T) at a new whole index.

## 3. Uniform polynomial reconstruction directly from the high F3 coefficients

**Theorem H.** For every t>=2 and both factors, arbitrary monic C and
arbitrary b determine a unique pair W,B of the prescribed constant and
leading form for which `[x^j]F=0` for q<=j<=2q. Its coefficients are
polynomials in c1,...,c_(t-1),b, with scalar-unit denominators only.
The remaining full equation is exactly the 2t-1 rows

    E_k=[x^k]F, k=2,...,2t.                              (H1)

**Proof.** The x^(2q) equation is the leading identity

    (2q-1)*omega^2+2alpha*omega-alpha^2/3=0.

For k=q-1,q-2,...,1 solve the coefficient of x^(q+k) for w_k. Its
diagonal is

    lambda_k=2((q+k-1)*omega+alpha)
            =2omega*(k+2t+3+6d).                        (H2)

Every other w coefficient entering that row has larger index. The
lower-degree linked terms cannot introduce an unsolved smaller index:
deg D=t<q, and the b^2 derivative and quotient terms lower degree.
Terms involving B or eta have degree at most q at this stage.
The scalar in (H2) is nonzero on both real embeddings. Indeed

    (k+2t+3)^2-(6d)^2=(k+2t+3)^2-12(t+1)>0

for t>=2 and k>=0, with k+2t+3 positive. Thus the recurrence uses units
on each factor, including every split index. After w1 is solved, impose
w0=-B. The x^q coefficient has B diagonal

    -((2q-1)*omega+alpha)=-2alpha*d,                     (H3)

another unit. It solves B. The coefficients x^0 and x^1 of F are
identically zero from W(0)=-B and eta=w1. Hence (H1) is exactly the
remaining F=0 condition. This is a polynomial construction, so it also
works over arbitrary k-algebras and preserves nonreduced fibres. QED.

Let B_C,b and eta_C,b denote these actual reconstructed polynomials,
and let J_t=(E_2,...,E_(2t)) in R_t. The exact residual form of (PS) is

    B_C,b*eta_C,b in radical(J_t).                       (H4)

Theorem H neither asserts that the E_k form a regular sequence nor
that their common zero set is finite. It isolates the coefficient
linkage needed for every statement below.

The weighted action

    c_j -> lambda^j c_j, b -> lambda^(t+1)b,
    C(x) -> lambda^(t-1)C(x/lambda),
    W(x) -> lambda^q W(x/lambda)

commutes with the recurrence. Thus w_k has weight q-k, B has weight q,
eta has weight q-1, and E_k has weight 2q-k. In particular all w_k for
k>=1, B, and eta are affine in b, since their weights are less than
2(t+1). Write

    W=P0+bP1, B=M+bN, eta=rho+b*sigma.

Here the P0,P1 labels are auxiliary polynomials for this paragraph,
unrelated to the later factor P. One has deg P1<=t and P1(0)=-N,
P1'(0)=sigma. Direct substitution gives the entire cubic b layer

    [b^3]F=-P1'/2+(N+P1)/x-sigma/2
           =-(1/2)*sum_(j=3)^t (j-2)[x^j]P1*x^(j-1).   (H5)

Its top coefficient is a scalar unit for t>=3, computed in Section 5.
This is a linked layer identity. It does not permit setting each b
coefficient to zero separately at a solution with a fixed scalar b.

## 4. Uniform support exclusions on the coefficient and ordered-root spaces

For a point (C,b), define its actual nonzero weight support

    Sigma={j:c_j!=0} union ({t+1} if b!=0),

and let `<Sigma>` be the additive semigroup it generates, including 0.

**Theorem S.** If 2t+1 is not in `<Sigma>`, then B=0. If 2t is not in
`<Sigma>`, then eta=0. Consequently a normalized solution with B eta!=0
must have both 2t and 2t+1 in `<Sigma>`.

**Proof.** By Theorem H, B and eta are polynomial functions of the actual
input coefficients and are homogeneous of weights 2t+1 and 2t. After
setting absent coordinates to zero, every possible surviving monomial
has weight in `<Sigma>`. If the required weight is absent there can be
no surviving monomial. This proves the claim even before imposing the
lower rows. No root is assumed distinct. QED.

In particular, a point on B eta!=0 has trivial multiplicative scaling
stabilizer. If a nonidentity scalar lambda fixed (C,b), uniqueness of
the high reconstruction would imply B=lambda^q B and
eta=lambda^(q-1) eta. Their nonzero values force both powers of lambda
to be one; since q and q-1 are consecutive, lambda=1, a contradiction.
This includes the all-zero input with its full multiplicative
stabilizer. For nonempty finite support, gcd(Sigma)>1 is excluded.
The semigroup test is stronger than this gcd test: coprime generators
can still fail to represent either of the two required weights.

An explicit broad family is

    C=x^(t-1)+c*x^(t-1-j), 2<=j<=t-1,

with arbitrary b and c. Its support is contained in {j,t+1}. In the
*enlarged* semigroup `<j,t+1>` one has

    2t+1 is representable iff j|(2t+1) or j|t,
    2t   is representable iff j|(2t)   or j|(t-1).

These equivalences concern the enlarged support, which may be larger
than the actual support when b or c is zero. Both representations
are possible only if

    j|t, or j=3 and t=1 mod 3.                           (S1)

Indeed pairing divisibility of 2t+1 with 2t is impossible for j>=2;
pairing that of t with t-1 is likewise impossible; the remaining
nontrivial pair forces j|3. Therefore every other binomial-C stratum
has B eta=0 uniformly in b,c, for every t and both factors. The listed
exceptions are possible supports, not assertions that solutions exist.
If b=0 the smaller actual support excludes every j>=2 directly.

At t=11, every j=2,...,10 is excluded, on both d=+2 and d=-2. More
generally this holds for every prime t=2 mod 3. There is no inference
here that an arbitrary C is a binomial.

Repeated-root families are included without taking a squarefree part.
For example

    C=x^r(x^ell-a)^m, r+ell*m=t-1, ell>=2,

is excluded on B eta!=0 whenever b=0 or ell divides t+1. For a!=0 every
nonzero root has multiplicity m and zero has multiplicity r. At a=0
all roots coalesce with multiplicity t-1. Both cases are included.
This follows from the nontrivial stabilizer, not an
argument on the dense distinct-root locus.

The same assertions pull back to the finite free ordered-root cover
`C=product_i(x-rho_i)`. Its rank is (t-1)!, obtained by successive monic
root adjunction and synthetic division of degrees t-1,t-2,...,1.
It is faithfully flat even on collisions. For an ideal I and element f,
faithful flatness gives `IB intersect R=I`; applying this to powers of
f proves radical membership descends and ascends. Thus a proof there
would be enough, but Theorem S only removes the stated support strata.

## 5. Complete monomial-C classification and the exceptional control

On C=x^(t-1), Theorem H and homogeneity force

    B=eta=0, W=omega*x^q+nu*b*x^t,
    nu=-1/(2y(3d+2)).                                   (M1)

For the positive coefficients only the weight t+1 can be a positive
multiple of wt(b), giving the x^t term. Weight q=2t+1 is not a multiple
of t+1, so B=0; eta=0 follows similarly. The high x^(q+t) row gives
the displayed nu. The factor 3d+2 is nonzero since |d|>=1.

Substitution leaves just two terms:

    F=E*b^2*x^(2t)+(t-2)*b^3*x^(t-1)/(4y(3d+2)),         (M2)
    E=-3(d+1)(9d^3+8d^2-1)
          /[4y^2(2d+1)(3d+2)^2].                        (M3)

For t>=3 the cubic coefficient in (M2) is a scalar unit, so b=0.
The unique solution on the entire monomial stratum is therefore

    C=x^(t-1), b=B=eta=0, W=omega*x^q.                   (M4)

This also proves the unit cubic leader of the direct residual row
E_(t-1). Formula (M3) is the scalar b^2 coefficient of the top row
E_(2t) for arbitrary C by homogeneity: no C coefficient of positive
weight can accompany b^2 there. It is nonzero for every t>=3. For
d>=1 the cubic 9d^3+8d^2-1 is positive. For d=-s, s>=1, it equals
-9s^3+8s^2-1<0, since s^2(9s-8)+1>0. The only admissible zero of
(M3) is d=-1, t=2. Thus E_(2t)/E is monic quadratic in b for t>=3,
and defines a finite free rank-two cover over k[c1,...,c_(t-1)].
Repeated roots of this quadratic remain in the cover. Its other
residual rows are still required; finite freeness is not nonexistence.

At t=2,d=-1,y=1/5, both coefficients in (M2) vanish. The exact family is

    C=x, W=-25*x^5/4+(5b/2)*x^2, B=eta=0, b arbitrary.  (M5)

At t=2,d=+1,y=2/5, the same candidate is

    C=x, W=25*x^5/48-(b/4)*x^2, B=eta=0,
    F=-2b^2*x^4,                                       (M6)

so only b=0 survives. These equations explain the exact V0 contrast
without reversing the product-vanishing criterion. The universal
identities and both specializations were checked symbolically in
`infinity_structure.py`; the full t=2 ideals are treated in Section 8.

There is also a converse classification on a different entire stratum:
**b=B=0 forces C=x^(t-1), W=omega*x^q for every t>=2.** Here the equation
is `2xWW'=W^2-2AW+A^2/3`. If W had a nonzero root rho, then A(rho)=0.
Write s=ord_rho(W)>0 and ord_rho(A)=2m, the latter even because
A=alpha*x^3*C^2 and rho!=0. The left side has order 2s-1. If s<=2m,
the right side has order at least 2s, a contradiction. If s>2m, the
right side has order 4m, also impossible since 2s-1 is odd. Thus W has
no nonzero root and is omega*x^q. At zero, comparing the least orders
of the same identity forces ord_0(A)=q; since deg A=q, A=alpha*x^q
and C=x^(t-1). This proof explicitly retains every repeated root.
It classifies a zero-target stratum; it is not a proof on B*eta!=0.
'''

def read_optional_json(path):
    return json.loads(path.read_text()) if path.exists() else None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seal', action='store_true')
    args = parser.parse_args()
    extra = (ROOT/'report_remainder.md').read_text()
    body = BODY.rstrip()+'\n\n'+extra.rstrip()+'\n'
    assert '<!-- BODY-END -->' not in body
    if args.seal:
        outcomes = json.loads((ROOT/'run_outcomes.json').read_text())
        assert outcomes['all_lane_jobs_finished'] is True
        assert outcomes['final_audit_pass'] is True
        body += '\n<!-- BODY-END -->\n'
        receipt = dict(line.split('=',1) for line in RECEIPT.read_text().splitlines() if '=' in line)
        data = body.encode()
        seal = ('\n## Seal\n\n'
                '- Body definition: every byte through the unique standalone '
                '`<!-- BODY-END -->` line, including its terminating newline.\n'
                f'- Body bytes: `{len(data)}`.\n'
                f'- Body SHA-256: `{hashlib.sha256(data).hexdigest()}`.\n'
                f'- Frozen basis: `{receipt["basis"]}`.\n')
        output = body+seal
    else:
        output = body
    assert 20000 <= len(output.encode()) <= 45000, len(output.encode())
    REPORT.write_text(output)
    print(json.dumps({'path':str(REPORT),'bytes':len(output.encode()),'sealed':args.seal}),flush=True)

if __name__ == '__main__':
    main()
