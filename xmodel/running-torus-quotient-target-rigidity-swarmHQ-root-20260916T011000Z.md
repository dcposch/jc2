# The running torus quotient admits no rational-target repair

Producer: swarmHQ ROOT (gpt-6-astra).
Date: September16,2026 UTC.
Basis: da1f1d30906fdf08a878c88126584173f1af7415.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Desk-only; no scientific computation or literature-priority claim.

## Statement and scope

The literal three-dimensional running map has a multiplicative-group
quotient from an affine plane to an affine plane. In coordinates u,r on
the source, put w=ur and

    s=2r+4w-3w^2,       t=w^2+wr-w^3,       Psi=(s,t).

Then:

1. J_(u,r)(s,t)=-2r^2 and Psi has generic degree3. It is NOT Keller.
2. Its set-theoretic image is exactly A2 minus the point(4/3,4/27).
3. Inside C(u,r), one has C[u,r] intersect C(s,t)=C[s,t].
4. For EVERY rational pair h,k in C(s,t) whose pullbacks through Psi
   belong to C[u,r], their source Jacobian is not a nonzero constant.

In particular no rational dominant target postcomposition, birational
or otherwise, repairs this quotient into a plane Keller map. The source
is the specified whole plane; arbitrary further rational or finite-degree
source substitutions are NOT covered. No other torus action, ambient map,
nonlinear quotient or general JC2 source is excluded.

## 1. The actual quotient, including its whole source ring

The [literal running triple](affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md)
is

    u0=1+xy,
    P=u0^3*z+y^2*u0*(1+3u0),
    Q=y+3x*u0^2*z+3x*y^2*(1+3u0),
    R=2x-3x^2*y-x^3*z.

The source action has weights(1,-1,-2) on x,y,z; the target weights on
P,Q,R are(-2,-1,1). Each displayed component is homogeneous of its
asserted weight, since u0 has weight zero.

Every invariant source monomial x^a y^b z^c has a=b+2c, so its invariant
ring is exactly C[xy,x^2z]. Set u=1+xy and r=2-3xy-x^2z. These are
affine coordinates on that quotient: xy=u-1, x^2z=5-3u-r.
Likewise, every invariant target monomial P^a Q^b R^c has c=2a+b,
so the target invariant ring is C[RQ,R^2P]. These are the literal rings,
not charts obtained by inverting x or R.

Direct substitution, as polynomial identities, gives

    R=xr,
    xQ=4u+2-3u^2r,
    x^2P=u^2+u-u^3r.

Therefore s=RQ and t=R^2P give precisely Psi above with w=ur.
The use of xQ and x^2P is only a polynomial identity check; neither
quotient plane loses its boundary by localization.

To compute its Jacobian, first use the intermediate polynomial map
(u,r)->(w=ur,r), of determinant r. The map(w,r)->(s,t) has matrix

    [ 4-6w       2 ]
    [ 2w+r-3w^2  w ],

of determinant -2r. Their composition has determinant -2r^2.
In particular s,t are algebraically independent over C.

## 2. The entire image from a cubic, not a generic-chart inference

Eliminating r gives

    c_(s,t)(w)=w^3-2w^2+s*w-2t=0,
    r=(s-4w+3w^2)/2=c'_(s,t)(w)/2.                 (1)

For a fixed target point(s,t), every SIMPLE root w of this cubic gives
r!=0 and u=w/r, hence an actual source point with the desired image.
A cubic over C has no simple root only when it is a cube(w-a)^3.
Comparing coefficients in(1) then forces

    a=2/3,       s=4/3,       t=4/27.

At this target the unique possible w is2/3 and r=0, incompatible with
w=ur for a finite source point. This target is omitted, and every other
target is hit by a simple root. This proves the exact image statement.

The exceptional source line r=0 maps to(0,0), not to the omitted point.
At(0,0), the cubic is w^2(w-2): the simple root w=2 gives the additional
source point(u,r)=(1,2), besides the entire line r=0. Thus Psi is not
quasi-finite; no such hypothesis is used in the image or ring argument.

At the function-field level C(u,r)=C(w,r)=C(s,w), since w=ur and
r=(s-4w+3w^2)/2. Equation(1) is irreducible over C(s,t): in
C(s)[w,t], it is linear in t with constant unit coefficient -2, so its
quotient ring is C(s)[w] and it is irreducible; it is primitive as a
polynomial in w over C(s)[t], so Gauss's lemma applies. Hence the generic
degree is3. Neither this degree nor the plane quotient is a counterexample,
because the displayed Jacobian vanishes on r=0.

## 3. Cofinite image prevents rational target poles from disappearing

We prove the needed elementary fact directly. Let a dominant polynomial
map Phi:A2->A2 have image containing the complement of a finite set.
Let h=a/b in C(s,t), with coprime a,b in C[s,t]. Suppose h(Phi) is a
polynomial H on the entire source. Clearing denominators in the source
domain gives the polynomial identity

    a(Phi)=b(Phi)*H.

If b is nonconstant, choose an irreducible factor beta of b. The target
curve V(beta) contains a point q outside both V(a) and the finite omitted
set: coprimality makes V(beta) not contained in V(a), and a nonempty open
part of a complex curve cannot be finite. Choose p with Phi(p)=q.
The cleared identity gives a(q)=0, contradicting its choice. Therefore
b is constant and h is polynomial.

This proof does not assume finiteness, flatness or quasi-finiteness of Phi.
In particular it applies despite the contracted line of Psi. Applying it
to Psi proves C[u,r] intersect C(s,t)=C[s,t] in the specified embedding.
The lemma is an elementary regular-function observation, not claimed new.

Now let h,k in C(s,t) have polynomial pullbacks. They are polynomials by
the lemma, so the polynomial chain rule gives

    J_(u,r)(h(Psi),k(Psi))=-2r^2 * J_(s,t)(h,k)(Psi).

The right side vanishes along r=0, and cannot be a nonzero constant.
There is no rational cancellation left after the global regularity test.

## 4. Comparison, controls and the remaining boundary

The accepted [volume-neutral torus theorem](volume-neutral-torus-quotient-swarmHQ-root-20260915.md)
requires trivial determinant character. The present source weights sum to
-2 and are explicitly outside that theorem. We have not changed its
hypotheses or reverified its closing import. Instead the actual quotient
has nonconstant Jacobian, and its cofinite image independently excludes
all rational-target repairs on the fixed source.

The accepted polynomial/rational-coefficient donor filter excludes fixed
polynomial target presentations after finite source extensions. Here (1)
indeed exhibits a cubic polynomial donor, but that existing fixed-target
statement is not substituted for the new rational-target quantifier.
The proof above covers rational target changes with the original whole
source, not simultaneous arbitrary changes of both source and target.

The earlier [affine target-plane section classification](affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md)
and first-pair graph results concern embedded source surfaces, not this
quotient map. Their stronger-looking words do not supply its image or
intersection-ring calculation. All relevant formulas were derived here.
The old cubic-thickening control concerns a finite cubic cover and a
different source; its fibre-length conclusion is not a premise.

The exceptional source line and omitted target point above test the
global-image distinction. For the pole lemma, dropping cofinite image
really changes the conclusion: Phi(a,b)=(a,ab) has h(s,t)=t/s,
which is not a target polynomial but pulls back to b. Its image omits
the punctured target line s=0. This control is explicitly NON-KELLER
and is only a check on the pole lemma's hypothesis.

No new source construction survives this test. No family of weights,
quotients, target degrees, finite covers or graph sections is selected.
JC2 remains unresolved; this is one exact construction exclusion.

## Evidence and read scope

ROOT derived the formulas, image and elementary pole lemma manually.
Native Astra independently checked the exact quotient, Jacobian, whole
image, intersection-ring statement and rational-target conclusion, giving
CONFIRMED; terminal mathematical completion01:10:19 UTC. ROOT collected
the whole terminal derivation before sealing. Its alternate divisor proof
also explicitly handles the contracted source line; the shorter evaluation
proof above suffices. Same-model checking is not different-model FIRST.
Different-model hostile review is required for promotion.
No mathematical subprocess, degree enumeration or computational certificate.
Replay is the displayed algebra and the exact exceptional-fibre check.
No source theorem is newly imported and no broad literature claim is made.

Frozen comparison pins:

- volume-neutral-torus-quotient-swarmHQ-root-20260915.md:
  181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80.
- affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md:
  4f47a46ee118fefe613dfefb01d223d80b957e931703235aad8b6d773eb3361c.
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

## OPENS RAISED

None. The exact candidate test is decided; out-of-scope sources are not solved.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Canonical checker exit0, handle collected. Identifier emptiness is not a
novelty certificate. Targeted history comparisons are those named above;
broad literal-fraction searches were noisy and narrowed to exact formulas.
All three comparison/guardrail hashes matched again before closure.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9178`.
- Body SHA-256:
  `22837333166c2916e082461405d2d1b9fdead05dc6d527d01eaa195952a049a5`.
- Frozen basis: `da1f1d30906fdf08a878c88126584173f1af7415`.
