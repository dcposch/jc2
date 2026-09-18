# A whole-plane polynomial weight with a nondense derivative domain

Producer: swarmHQ (ROOT/Astra), September 18, 2026.
Evidence: MANUAL / PRODUCER-CHECKED. Lifecycle: UNPROMOTED pending
different-model hostile review. JC2 remains unresolved.
Frozen public basis: `adee75323de11912dd3ee70c1837afc80c11ef70`.

## Exact result and research use

On the WHOLE source C^2 with coordinates (x,y), set

    c(x,y) = xy^2-y,
    phi(x,y) = |x|^2 + |xy|^2 + |c(x,y)|^2,
    H = O(C^2) intersect L^2(C^2, exp(-phi) dA(x)dA(y)),
    E_x = {h in H : partial_x h in H},
    E = {h in H : partial_x h and partial_y h are in H}.

The following statements hold:

1. phi is a real polynomial, smooth and strictly plurisubharmonic on C^2.
   Its complex Hessian determinant is everywhere at least 1/2, but is NOT
   constant. The map (x,y)->(x,xy,c) is a polynomial immersion into C^3.
2. The weighted measure has finite total mass. Both 1 and c belong to H,
   whereas y and y^2 do not.
3. E_x is NOT dense in H. Consequently E is not dense either. A bounded
   linear functional on H annihilates E_x and takes value 1 on c.

This defeats a proposed generic analytic shortcut: an entire C^2 source,
a polynomial strictly psh weight, finite mass, and even a positive uniform
lower bound on the complex-Hessian DETERMINANT do not suffice for dense
holomorphic derivative domains. It supplies no polynomial Keller map.
The stronger two-output Keller form |F_1|^2+|F_2|^2, its constant
determinant, and its specific lifted derivatives are NOT realized here.
No density theorem for those maps is refuted or proved.

## 1. Exact positivity and scope of the lower bound

For G=(x,xy,xy^2-y), its complex derivative matrix has rows

    (1,0), (y,x), (y^2,2xy-1).

The complex Hessian of phi=|G|^2 is (JG)^*JG. Its two-row minors are

    x, 2xy-1, y(xy-1).

The first two cannot vanish simultaneously, so JG has rank two everywhere.
Cauchy--Binet gives, with p=xy,

    Delta = det(partial partialbar phi)
          = |x|^2 + |2p-1|^2 + |y(p-1)|^2
          >= |2p-1|^2 + 2|p(p-1)|.

Put u=2p-1. Then p(p-1)=(u^2-1)/4. If |u|^2<=1, the triangle inequality
gives

    |u|^2 + (1/2)|u^2-1| >= (1+|u|^2)/2 >= 1/2.

If |u|^2>=1, the same expression is at least 1. Thus Delta>=1/2.
Equality occurs at x=1/2,y=1. Delta(0,0)=1 and Delta(1,0)=2, so it is
not constant. This is a determinant lower bound, NOT a uniform bound of
the Hessian below by a fixed positive multiple of the identity.

The weight is not proper: for nonzero t tending to zero, (x,y)=(t,1/t)
escapes and phi=|t|^2+1. No real convexity or complete metric is asserted.

## 2. Global integrability by elementary Gaussian integration

Fix y and put r=|y|^2 and A=1+r+r^2. Completing the square in x yields

    phi = A |x-mu|^2 + E_r,
    mu = conjugate(y) r/A,
    E_r = r(1+r)/A = 1-1/A.

Hence 0<=E_r<1, and

    integral_C exp(-phi) dA(x) = (pi/A) exp(-E_r).

The total mass is

    pi^2 integral_0^infinity exp(-E_r)/A dr < infinity,

since A is positive at zero and grows quadratically. This proves 1 in H.
For c=xy^2-y, its mean in this x-Gaussian is

    mu y^2-y = -y(1+r)/A,

and its variance is r^2/A. Therefore

    integral_C |c|^2 exp(-phi) dA(x)
      = (pi/A) exp(-E_r) [ r^2/A + r(1+r)^2/A^2 ].

The bracket is at most 2: r^2<=A and
A^2-r(1+r)^2=1+r+r^2+r^3+r^4>0. Integration in y proves c in H globally,
not merely on one boundary chart. Conversely the norms of y and y^2
contain respectively

    pi^2 integral_0^infinity r exp(-E_r)/A dr,
    pi^2 integral_0^infinity r^2 exp(-E_r)/A dr.

They diverge, as their integrands are asymptotic to e^-1/r and e^-1.
In particular partial_x c=y^2 is not in H. This last strict inclusion
alone is NOT the nondensity proof; continuous separation follows below.

## 3. A boundary chart with no change of source measure

On y!=0 use the rational chart

    t=1/y,  s=xy^2-y,
    x=t+s t^2,  y=1/t.

It is a biholomorphism between t!=0 and y!=0, with s unrestricted.
The complex Jacobian of (t,s)->(x,y) is exactly 1. Thus Euclidean source
volume transforms to dA(t)dA(s), with no hidden power of |t|. The weight
becomes

    Phi(t,s)=|t+s t^2|^2 + |1+s t|^2 + |s|^2.

This is smooth across t=0, and exp(-Phi) is bounded above and below by
positive constants on every bounded closed bidisc in (t,s).

For h in H define q(t,s)=h(t+s t^2,1/t) on t!=0. It is locally L2 with
ordinary Euclidean volume in every punctured bidisc reaching t=0.
Consequently it extends holomorphically across t=0. For completeness,
expand q=sum_{k in Z} a_k(s)t^k. Laurent coefficients are holomorphic in s.
Parseval and Fubini imply that a nonzero negative coefficient would force
the divergent radial integral integral_0^epsilon r^(2k+1)dr for k<=-1
on an open set of s. Therefore every negative coefficient vanishes.
The resulting local extensions agree by uniqueness.

This is an extension in an AUXILIARY chart, not an identification of t=0
with points of the original C^2 or a claimed proper source map.

## 4. A bounded functional that separates the full domain

For h in E_x, the chain rule gives

    q_s = t^2 (partial_x h)(t+s t^2,1/t).

Both q and the pullback of partial_x h extend holomorphically across t=0
by Section 3. Hence q_s is divisible by t^2. In particular q(0,s) is
constant on any connected s-disc. This assertion applies to EVERY h in
E_x, not just to its polynomial members.

Take a disc containing s=0 and s=1 and define

    ell(h)=q(0,1)-q(0,0).

For a fixed sufficiently small rho>0, each term is the Cauchy integral

    q(0,s_j) = (1/(2 pi i)) integral_|t|=rho q(t,s_j) dt/t,
    s_j in {0,1}.

The two circles map into a compact subset of the ORIGINAL source C^2.
Its weighted density exp(-phi) is smooth and strictly positive on a
compact neighborhood. The elementary holomorphic submean estimate gives
supremum on these circles <= C times ||h||_H. Thus ell is a bounded
linear functional on H. This also follows directly from local L2 bounds
on a compact annulus, but no boundary evaluation continuity is assumed.

We proved ell(E_x)=0, so closure_H(E_x) is contained in ker(ell).
For the globally integrable polynomial c from Section 2, q_c(t,s)=s.
Therefore ell(c)=1. The kernel is proper, proving E_x nondense and,
since E is contained in E_x, proving E nondense as well.

The space H is a Hilbert space: weighted L2 limits of holomorphic
functions converge locally uniformly after the usual submean bounds,
so its holomorphic subspace is closed. No closability/adjoint-domain
assumption is needed for this continuous-separation argument.

## 5. Controls, dependencies, and exclusions

Positive comparison: for phi_0=|x|^2+|y|^2, all holomorphic monomials
have norm squared pi^2 a!b!. Taylor expansion and angular orthogonality
give density of polynomials in its entire Gaussian space, and polynomials
lie in both derivative domains. Thus the failure is not a formal feature
of every weighted entire space or an artifact of the definition of E.

All computations above are manual: Gaussian completion/integration,
Cauchy--Binet, the chain rule, Laurent/Parseval removal and a fixed-interior
Cauchy functional. No CAS, numerical integration, parameter search or
external analytic estimate is an evidentiary dependency.

The affine geometry is classical. With a=x,b=xy,c=xy^2-y, one has
ac=b(b-1); the displayed chart is the usual missing-line chart of this
Danielewski surface. No novelty claim is made for the surface, its chart,
or the general theory of nondensely defined operators. No use of a
surface-classification theorem is required by this proof.

Nearest campaign comparisons, checked before commissioning:

- [Source-volume integration](source-volume-residue-integration-root-20260911.md)
  records a different marked affine enlargement and its classical Wright
  duplicate. It does not supply this weighted-domain calculation.
- [Rational spectral control](gaussian-spectral-gap-control-swarmHQ-root-20260918T184800Z.md)
  uses a punctured rational source and addresses a different gap. Here the
  original source is literally C^2, but the weight is not a Keller weight.
- [Keller holomorphic density criterion](holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md)
  with its [binding independent review](holomorphic-density-first-swarmHQ-fable-20260918T194700Z.md)
  identifies density for the ACTUAL lifted derivatives and ACTUAL Keller
  Gaussian with invertibility. This example does not instantiate that
  setup and does not invalidate any of its conclusions.

Frozen history comparison: public adee7532 and HQ f13aae22. Scoped
searches are not an exhaustive priority audit. Two targeted primary-source
discovery queries returned unrelated indices, with no theorem imported.

The resulting restriction on a future proof is precise: use more than
whole-source topology, polynomial strict plurisubharmonicity, finite mass,
and a determinant lower bound. This is NOT a positive density estimate,
a new completeness theorem, or evidence against JC2. No new family,
generalization, numerical test, or automatic successor is requested.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Administrative command: `python3 ops/open_collision.py <this partial report>
--root .`, terminal exit 0. This mechanical result is not a novelty audit.
No new exit-price assertion. Live client: the proposed generic
whole-plane weighted-holomorphic-domain shortcut. Bounded quantity:
density of E_x for this one explicit weight. Cheapest test: the manual
Gaussian and continuous-functional calculations above, with one hostile
different-model review before promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9654`.
- Body SHA-256:
  `27ebd647bf3e7cb3d07c53ab64a691db3db21c95e34c41d3888be4e1050fac02`.
- Frozen basis: `adee75323de11912dd3ee70c1837afc80c11ef70`.
