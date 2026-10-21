# A complete-image obstruction for birational Darboux target charts

Producer: swarmHQ ROOT; native Astra-assigned hostile review and independent
Sol5.6-assigned FIRST. Hosted model identities were not independently attested.
Date: 2026-10-21 UTC.
Basis: dffb2a743988b64bbac98410c56ef47d6ab45aa1.
Evidence tier: MANUAL, with the accepted classical surface/Zariski Main imports.
Lifecycle: PROMOTED at the exact statements below; external novelty unknown.
Campaign identifier: CUSPCHART1054. JC2 remains unresolved.

## Statement and scope

Work over C. Let Y be a smooth projective rational surface, and let omega
be a nonzero rational two-form with no divisorial zeros. Let V be its regular,
nonvanishing locus. Suppose a dominant rational map phi:A2 --> Y is defined
on a neighborhood of a curve L in A2, and phi(L)=C0 set-theoretically, where
C0 is a complete irreducible positive-dimensional curve contained in V.

Then there is NO field-generating rational target pair P,Q satisfying
C(P,Q)=C(Y) and dP wedge dQ=c omega, c a nonzero constant, for which
(P,Q) composed with phi extends to a polynomial map on the entire source A2.
In particular it cannot become a polynomial Keller map in such a target frame.

This is a FIXED-source-chart obstruction. It does not exclude other source
charts, finite source substitutions, arbitrary target volumes, or all isogenies.
Dominance is stated explicitly so rational compositions are unambiguous.
No Jacobian assumption on phi is needed for this obstruction itself.

## Dependencies and prior work

Section2 of the accepted [zero-free-model report](zero-free-branch-model-swarmHQ-root-20260917T044000Z.md)
proves that a birational inverse Darboux chart into such Y extends over all A2.
Its [independent review](zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md)
retains smooth-surface resolution, graph descent, and finite birational
normality as standard imports. Zariski Main also gives the open-immersion
step below. No new external proof audit is asserted here.

The present obstruction is a short COROLLARY of that extension mechanism,
not a replacement proof of the full earlier criterion. It does not require
the earlier criterion's separate hypothesis that every branch component be
smooth. The explicit chart and nodal-image application below explain its use.

## Argument

The inverse target chart gamma:A2_(P,Q) --> Y is birational and pulls omega
back to c^(-1)dP wedge dQ. Resolve it by point blowups over A2. Every
exceptional divisor over an affine point has positive order for the pulled-back
standard area form. If it dominated a divisor of Y, birationality would
identify the generic valuation, whose omega-order is nonpositive. Thus all
such exceptional divisors are contracted. Connected exceptional fibers have
point images. The proper graph projection is locally finite and birational
over the normal plane, hence an isomorphism. Therefore gamma is a morphism
on the entire A2, not merely outside a finite exceptional set.

Over V, its differential is invertible by equality of the nonvanishing forms.
The birational etale morphism gamma^(-1)(V) -> V is therefore an open immersion.
If F=(P,Q) composed with phi were polynomial, gamma composed with F would
agree with phi wherever phi is defined, by agreement on a dense open and
separatedness. Hence C0 would lie entirely in that open-immersion image.
Its inverse would give a nonconstant morphism C0 -> A2, impossible because
all global regular functions on a complete irreducible curve are constant.
No properness of phi or gamma is being assumed.

## An actual affine-plane Darboux chart

Let C be the cuspidal projective cubic Y^2Z-X^3=0. On Z=1 use u=X/Z,
v=Y/Z and omega=du wedge dv/(v^2-u^3). The projective morphism

    beta(p,q)=[pq(1-q):1:p^3q^2(1-q)^3]

is defined on all A2. In Y=1 coordinates r=X/Y,s=Z/Y,
omega=-dr wedge ds/(s-r^3), and direct algebra gives

    s-r^3=p^3q^2(1-q)^4,
    det D(r,s)=-p^3q^2(1-q)^4.

Thus beta^*omega=dp wedge dq. Its rational inverse is
q=u^3/v^2 and p=v^3/[u^2(v^2-u^3)]. Four blowups over O=[0:1:0]
make this a genuine affine coordinate chart, as follows.

1. At (r,s)=(0,0), use s1=s/r. Then s1=p^2q(1-q)^2;
   the strict polar cubic is s1=r^2.
2. At (r,s1)=(0,0), use s2=s/r^2. Then s2=p(1-q);
   the strict polar cubic is s2=r.
3. At (r,s2)=(0,0), use (s2,w=r/s2). Then w=q;
   the strict polar cubic is w=1.
4. At (s2,w)=(0,1), use (w,nu=s2/(1-w)). Then (w,nu)=(q,p);
   the strict polar cubic is outside this entire affine chart.

Writing E1,...,E4 for the exceptional curves in creation order, the final
chart contains E2={q=0}, E3={p=0}, and E4={q=1}. The complete curve E2
is P1; its chart intersection is A1_p. It retains its E3 intersection
at p=0 and omits exactly its E1 intersection at p=infinity. The fourth
center does not lie on E2, nor do subsequent centers on the strict polar
cubic, which is already disjoint from E2 and from the entire chart.

## Conditional nodal-quotient application

Suppose this source chart sits in a surface with a multiplicative I_n fiber
containing E2, with those two intersections as its cycle nodes. Suppose a
component-rotating quotient to an I_1 fiber on Y is defined and finite etale
near that fiber, and each source component maps with degree one onto the
normalization of the target nodal curve C0. Finally assume Y has a zero-free
form as above and C0 lies entirely in its regular, nonvanishing locus.

Then E2 intersect A2 maps onto the ENTIRE complete nodal C0. Indeed the
normalization P1 has two points above the node. Deleting exactly one keeps
the other preimage of the node, as well as the unique preimage of every
smooth point. The complete-image obstruction therefore excludes polynomial
landing in every field-generating birational target Darboux frame for this
fixed source chart. The node need not be a branch point.

No cyclic isogeny, degree-seven configuration, or Keller candidate is
constructed here. The application is conditional on all the displayed data.

## Replay, review, and negative controls

Desk-only; no CAS, numerical search, cloud job, or new primary-source query.
The displayed inverse, determinant and blowup coordinates permit direct replay.
Deleting BOTH node preimages would fail the surjectivity premise. Removing
the zero-free-form or field-generation hypotheses invalidates the supplied
inverse-chart argument; no theorem without them is asserted.

The sealed producer manuscript had 144 lines/7500 bytes and SHA256
bef3aa096539e7742da74cf987a924c1bb12681504431f47f8ed9febfb04443d.
Astra's hostile review and Sol5.6-assigned FIRST independently confirmed the
chart, complete-image proof and conditional nodal application, not the
producer's optional pencil speculation. FIRST freshly read the whole producer
and accepted predecessor1-96. Both reviewers' fourteen selected input pins
matched at completion. This report integrates those exact mathematical scopes.

## Limitations and next test

This is an early obstruction for chart construction, not a new general
constraint on the finite normalization B of a Keller target. It supplies
neither B=R, surjectivity, a degree bound, nor a proof or counterexample to JC2.
Before applying it to a candidate, check the ACTUAL source chart, complete
curve image, and target form. A generic rational isogeny alone supplies none
of those chart conditions. No successor family or computation is prescribed.

## OPENS RAISED

None. Existing global questions remain open at their previous scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `dffb2a743988b64bbac98410c56ef47d6ab45aa1` (Git blobs only).

<!-- BODY-END -->
