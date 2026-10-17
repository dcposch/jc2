# Cubic-cusp donor: all constant-J birational target changes

Status: AUTHOR-COMPLETE / UNPROMOTED pending different-model FIRST.
Producer: swarmHQ ROOT, with native Astra co-check completed02:09:04 UTC.
Public basis: 3ad6508c437bd1f82faf8ebaf8e68732478d8d9a.
Operational admission: swarmHQ 77962737bd848d5b0e56071ffbcc162da5fe1545.
Manual proof with explicitly named accepted classical imports; no CAS.

## 1. Claims and boundary

Let C be the standard cusp q^2=p^3 in A2_C. Suppose tau=(u,v) is a birational
rational map of the plane with J_(p,q)(u,v)=c in C*, and tau is NOT polynomial.
Then C is neither contracted nor sent entirely to the line at infinity.
For its reduced affine image closure C', either its normalization is not A1,
or C' itself is smooth and isomorphic to A1.

Consequently, consider the rational donor over C

    t=X/Y,  p=Y-3t^2,  q=-tY+2t^3,  K=C(X,Y),  K0=C(p,q).

No constant-J birational rational change of the target coordinates, followed
by any finite rational source-field embedding K -> C(x,y), makes the two
resulting target coordinates polynomials with nonzero constant Jacobian on
the entire source plane. This includes polynomial target changes as well.

This is a theorem about this donor and all target changes in the stated class,
not about all rational donors, all affine-radial donors after target change,
nonconstant-J target changes, or a normal form for hypothetical Keller maps.
No general finite-normalization emptiness or JC2 conclusion follows.

## 2. Explicit prior premises

We use the independently reviewed [CUSP-AVOIDANCE-1](cusp-avoidance-review-swarmHQ-sol56-root-20261017T015830Z.md):
every closed irreducible rational curve in A2_C meets q^2=p^3, with arbitrary
normalization punctures allowed. It is not re-proved here.

We also use the accepted surface and attachment interface of
[SYMPLECTIC-TARGET-SMOOTH-BRANCH-1](symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md),
with its [different-model review](symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md):

- A birational rational plane map with nonzero constant Jacobian, and its
  inverse, have no finite projective basepoints. They are morphisms A2 -> P2,
  although they need not map A2 into A2.
- Resolve such a map by blowups over the source line at infinity only. The
  resolution contains the entire affine source unchanged. A proper birational
  morphism between smooth projective surfaces factors into point blowups;
  its irreducible exceptional curves are smooth rational curves.
- A ramified divisorial valuation over a finite target curve remains ramified
  under a further finite source-field extension. For a hypothetical polynomial
  Keller map that curve must be a component of its actual nonproper-value set.
- Such nonproperness components have normalization A1 by polynomial coverage;
  no such component can itself be a smooth A1. These are the named accepted
  Jelonek/Nguyen Van Chau inputs, not new imports or proofs of their source chain.

The old surface proof was selected at frozen public3ad6508c, 14180 bytes,
SHA256 f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a.
ROOT read its lines1–176 for this interface. Its original whole-donor theorem
required EVERY projective branch component smooth; that hypothesis does not
hold for the cubic donor, so its whole-donor conclusion is NOT imported.

## 3. Pole curves and noncontraction

Write omega_old=dp wedge dq and omega_new=du wedge dv on the two projective
planes. Their divisors are -3 times their respective lines at infinity.
Resolve tau by pi:Z -> P2_old and psi:Z -> P2_new, with pi unchanged on A2_old.
Then psi^*omega_new=c*pi^*omega_old.

Because tau is not polynomial, one of u,v has a pole along an irreducible
closed affine curve E. A rational function regular throughout A2 is polynomial;
normality excludes isolated poles. The extended projective morphism tau maps
E into L_infinity_new. If E dominated that line, psi would identify their
generic DVRs (a proper birational morphism to a smooth surface is an isomorphism
there). The orders of the two sides of the displayed form identity along E
would then be -3 and 0, impossible. Hence the closure of E in Z is an
irreducible psi-exceptional curve. It is smooth rational. In particular E is
a closed irreducible rational affine curve, with no restriction on its punctures.

The affine cusp C cannot be contracted by tau: its closure in Z would be
psi-exceptional and hence smooth, but pi is unchanged at the cusp singularity.
Nor can C dominate L_infinity_new, by the same -3 versus 0 order argument.
Thus C has a genuine affine image curve C'. Its projective strict image is
birational to C, because a nonexceptional curve under a birational surface
morphism has the same generic DVR. We identify both smooth projective
normalizations with the parameter line P1_t of p=t^2,q=t^3.

## 4. One puncture forces the old cusp point to infinity

Assume C' has affine normalization A1. In the common P1_t there is exactly
one point t0 outside that affine normalization. Equivalently it is the sole
point where the induced projective parametrization of C' lies at infinity.
This equivalence does not assume that C' is already smooth: if u and v are
regular in a parameter DVR, their integral closure is regular there too.

Choose the pole curve E from Section3. CUSP-AVOIDANCE-1 says E meets C in
the old affine plane. Since tau is projectively defined at every affine point,
all those intersections map to new infinity. Thus t0 is a finite parameter.
For an irreducible polynomial H defining E, put h(t)=H(t^2,t^3).
It is not identically zero, since E cannot equal the singular curve C.
It has at least one root, and every root is t0. Hence

    h(t)=a*(t-t0)^k,  a!=0, k>=1.

But h belongs to C[t^2,t^3], so h'(0)=0. In characteristic zero the derivative
of the displayed pure power at0 is nonzero if t0!=0. Therefore t0=0.
In particular, tau sends the old cusp point o=(0,0) to new infinity.
The old parameter infinity is now finite in the normalization of C'; this
exchange is allowed, not silently ruled out.

## 5. The new affine curve is smooth

Resolve the inverse map by rho:Z' -> P2_new and sigma:Z' -> P2_old. The entire
new affine plane is unchanged by rho. Let C_tilde be the strict transform of
the old projective cusp under sigma. Its intersection with this unchanged
affine plane is precisely C'.

The old projective cusp q^2*z=p^3 has its only singularity at old o; its old
infinite point [0:1:0] is smooth. Factor sigma into point blowups. Strict
transforms of a smooth curve under point blowups remain smooth. Thus C_tilde
can be singular only above old o.

No point b of the unchanged A2_new can satisfy sigma(b)=o. Indeed, tau is
projectively regular near o. On the open neighborhood sigma^-1(A2_old),
the morphisms tau composed with sigma and rho agree on a dense open set,
hence agree everywhere by separatedness. If sigma(b)=o, this would give

    b=rho(b)=tau(o) in L_infinity_new,

contradicting b in A2_new. Therefore C' contains no point above the only
possible singularity. It is smooth. Since its normalization was assumed A1,
it is itself isomorphic to A1. This proves the first claim.

## 6. Application to the cubic donor

The identities

    t^3+p*t+q=0,  Y=p+3t^2,  X=t*(p+3t^2)

give K=C(p,t) and [K:K0]=3. Indeed q=-t^3-p*t is a degree-three polynomial
map in t over C(p). Directly dp wedge dq=Y*dt wedge dY=dX wedge dY, so the
donor has Jacobian one as a rational map in (X,Y).

Its generic ramification curve p=-3t^2 has index2 and image
B={4p^3+27q^2=0}. The derivative 3t^2+p has a simple zero at its generic
point, equivalently this is the ordinary cubic discriminant branch. A constant
invertible linear scaling identifies B with the standard cusp; it preserves
the class of nonzero-constant-J birational target changes.

If the target change is nonpolynomial, Sections3–5 show B is not contracted
and its affine image B' either has normalization not A1 or is a smooth A1.
Its generic ramification persists under target-field identification and any
finite source-field embedding. The accepted attachment interface would make
B' a nonproperness component of the hypothetical polynomial Keller landing.
Polynomial coverage excludes the first alternative; the no-smooth-A1-component
theorem excludes the second. Additional branch components do not repair this
contradiction, and no claim about their smoothness is needed.

If the target change is polynomial, a birational polynomial Keller map is an
automorphism. This uses only the birational case, not JC2: Zariski's Main
Theorem makes it an open immersion. A complementary divisor would give a
nonconstant polynomial with nowhere-vanishing pullback on A2, impossible.
With complement of codimension at least2, regular inverse coordinate functions
extend across it by normality, giving a polynomial inverse. Undo this target
automorphism and apply the already reviewed fixed-target affine-radial
obstruction. This also excludes the polynomial-target case.

## 7. Controls and limits

- Identity is a polynomial target automorphism and leaves the cusp singular
  with normalization A1. The first claim therefore explicitly requires a
  NONPOLYNOMIAL target change; the donor exclusion treats automorphisms separately.
- The constant-J map (p,q)->(1/p,-p^2*q) sends the cusp parametrization to
  (t^-2,-t^7). Its affine image has equation u^7*v^2=1 and normalization C*,
  not A1, as the first alternative predicts.
- The same map sends the line q=0 birationally to the line v=0, exchanging
  its zero and infinity. Thus infinity exchange is possible; the proof does
  not assume otherwise. The singular cusp and h'(0)=0 are load-bearing.
- The nonconstant-J map (p,q)->(q/p,p-q^2/p^2) has Jacobian -1/p and sends
  the cusp to a line. It has a finite projective basepoint at the origin,
  so it is not covered. This is not a Keller repair or an exclusion theorem
  for nonconstant-J target changes.
- No bound on pole-curve punctures, target degree, source-extension degree,
  or number of additional branch components has been imposed.
- No assertion that arbitrary donors have this branch curve, or are reducible
  to this donor by allowed target/source changes, is made.

## 8. Custody

ROOT reasoning is explicit above. The native Astra co-check independently
confirmed the bridge relative to the named accepted premises, including both
noncontraction and nondomination of new infinity, the k=1 edge case in the
derivative argument, the inverse-resolution smoothness step, donor ramification,
and the fact that additional branch components cannot undo the contradiction.
Same-model co-checking is not independent FIRST and does not promote the claim.

Co-research startup02:05:19, read gate02:07:47, terminal/postpins02:09:04 UTC.
Nine unchanged whole governing reads were reused after matching pins;
APPROACHES894 and frozen STATE430 at7796273 were read wholly. The authorized
legacy proof blob's metadata matched before selected lines55–176 were read.
All eleven governing/STATE postpins and the selected legacy-blob postpin matched.
Executable paths were verified. No deviations, writes, extra queries/bodies,
external sources, CAS/scientific subprocesses, children or paid lanes were used.
Original partial02:11:31 and hard02:26:31 were met early, without a cap reset.

This report requires canonical sealing and independent different-model FIRST
before promotion. No exit-price or new Keller-compatible example is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11550`.
- Body SHA-256:
  `0d9c2f3042ce6b79d58e356728a02aa7975b3240a8de64566d6580d40d3f6d0c`.
- Frozen basis: `3ad6508c437bd1f82faf8ebaf8e68732478d8d9a`.
