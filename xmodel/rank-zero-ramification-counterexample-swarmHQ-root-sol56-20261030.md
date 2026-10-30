# A rank-zero obstruction to the smooth-critical-curve extension

Producer: swarmHQ (ROOT; main configured gpt-6-astra, hosted identity unverified).
Independent hostile reviewer: swarmHQ (configured gpt-5.6-sol, hosted identity unverified).
Date: 2026-10-30T18:08:00.032300+00:00
Basis: e84ee01e12a7713a59b72679308ecc1d44264c1a
Evidence tier: MANUAL, relative to the named standard foundations below.
Lifecycle: PROVISIONAL. Independent verdict PASS at the exact reduced-support scope.

## Exact reviewed argument

The following argument, foundations and limitations are byte-identical to lines12–91 of the [sealed independent review](rank-zero-counterexample-review-sol56-20261030T1800Z.md). The [sealed author candidate](../box/rank-zero-ramification-counterexample-swarmHQ-20261030/author-candidate.md) is preserved with its historical pre-review label. No mathematical statement changes in this integration.

The pair

    P = u^4 + u*v,
    Q = 3*v^2 + 12*u^3*v + 8*u^6

is a finite polynomial map from the smooth affine plane to the smooth affine plane. Its critical scheme is the doubled line V(v^2), and its reduced critical locus is the single smooth line E=V(v). At the origin the differential has rank zero. The induced map from E to the normalization of its reduced image has local parameter t=u^2, of order two at the origin.

Therefore it is a valid counterexample to deleting the rank-one hypothesis from the local lemma when the retained critical-curve hypothesis concerns the smooth reduced critical support. It is not a counterexample to the rank-one lemma, to JC2, or to a stronger variant that separately requires the Jacobian divisor itself to be reduced.

## Independent checks

### Jacobian, support, and ranks

The derivatives are

    P_u = 4*u^3+v,       P_v = u,
    Q_u = 36*u^2*v+48*u^5,  Q_v = 6*v+12*u^3.

Thus

    P_u Q_v - P_v Q_u
      = (36*u^3*v+48*u^6+6*v^2)
        -(36*u^3*v+48*u^6)
      = 6*v^2.

Hence the critical scheme is V(v^2), while its reduction E=V(v) is one smooth affine line. All four derivatives vanish at (0,0), so the rank there is zero. At (u,0) with u nonzero, P_u=4u^3 is nonzero; the determinant is zero, so the rank is exactly one.

### Algebraic independence and finiteness

In C(u,v),

    dP wedge dQ = 6*v^2 du wedge dv != 0.

The characteristic-zero differential criterion therefore makes P,Q algebraically independent, so A=C[P,Q] is a polynomial ring in two variables and is the stated target coordinate ring.

Direct substitution gives the first monic identity:

    u^8-6*P*u^4+Q*u^2-3*P^2
      = u^8-6*(u^8+u^5*v)
        +(3*u^2*v^2+12*u^5*v+8*u^8)
        -3*(u^8+2*u^5*v+u^2*v^2)
      = 0.

The second monic identity is

    v^2+4*u^3*v+(8/3)*u^6-Q/3 = 0.

Thus u is integral over A and v is integral over A[u]. Since C[u,v]=A[u,v] is finitely generated, transitivity of integrality makes it a finite A-module. The polynomial map is finite.

### Fibre over the origin and the analytic germ

If P=0, then u=0 or v=-u^3. In the first case Q=3v^2, so Q=0 forces v=0. In the second case Q=-u^6, so Q=0 forces u=0 and then v=0. The set-theoretic fibre over (0,0) is therefore the single origin. Analytification/localization of the finite morphism gives the claimed finite holomorphic germ at that point.

### Image cusp, normalization, and local order

On E,

    u maps to (P,Q)=(u^4,8*u^6).

Its reduced image is the irreducible cusp D given by Q^2=64*P^3. With t=u^2, its image ring is

    C[u^4,8*u^6] = C[t^2,t^3].

In the cusp function field t=Q/(8P), and t is integral because t^2=P. The finite birational normal extension C[t^2,t^3] contained in C[t], with C[t] integrally closed, is the normalization. Compatibility forces the induced map E -> D_normal to be t=u^2. Equivalently, the completed local-ring map is C[[t]] -> C[[u]], t maps to u^2, so its local order/ramification index at zero is two. Its function-field degree is two.

For u_0 nonzero on E, dt/du=2*u_0 is nonzero, so the normalized-image parameter has local order one. This exactly matches the rank-one conclusion away from the origin and creates no contradiction with that lemma.

### Whole-source obstruction

The complement is

    S minus E = Spec C[u,v,v^(-1)] = A1 times G_m.

Its coordinate ring has the nonconstant unit v, whereas every unit of C[x,y] is constant. Hence this complement is not A2. In addition, the Jacobian 6v^2 is not a nonzero constant. The example therefore does not realize the whole-source Keller normalization package and supplies no global boundary application.

## Foundations and limitations

The proof uses only standard foundations: the characteristic-zero Kahler-differential criterion for algebraic independence; finite generation plus transitivity of integrality; analytification/localization of finite morphisms; normalization of the cusp by a finite birational normal ring C[t]; DVR/completed-local-ring order; and invariance of the unit group under affine-ring isomorphism. These are identified foundations, not a fresh literature audit.

No generic surface degree, group classification, actual Keller realization, singular-source conclusion, global exclusion, or JC2 conclusion was checked or inferred. No web, repository/history, source, or collision search was authorized; no CAS/scientific computation or secondary model was used. The stopped historical review body was not supplied or read. Historical attribution is not a proof premise. Novelty and collision priority remain unassessed.

## Dependencies, history and replay

Desk-only. The derivative and monic identities, cusp normalization and unit obstruction are explicitly checked above. No CAS or parameter sweep is part of the proof. The author's comparison with the old CJD1311 rational quotient is provenance, not an imported theorem or novelty claim; the old donor-repair stops remain. The stopped historical DC2-REVIEW body was not used.

The [evidence README](../box/rank-zero-ramification-counterexample-swarmHQ-20261030/README.md) and SHA256SUMS retain exact custody, including the ROOT display qualification. The independent review passed; the earlier rank-one lemma is unchanged. A separately reduced Jacobian divisor is a stronger hypothesis than the smooth reduced support used here.

## Limitations and next question

This closes the unrestricted rank-zero extension as a proposed local route. Excluding this behavior for the actual marked Keller source still requires a whole-source argument. Singular normalization surfaces remain outside the local positive lemma. No new local-control family or source-construction route is proposed here.

## OPENS RAISED

None. Existing whole-source and singular-source gaps retain their scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `e84ee01e12a7713a59b72679308ecc1d44264c1a` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6901`.
- Body SHA-256:
  `dec376b508fd8c4fab69cfee1eb597468940721a2249654f8b6a0550290bd212`.
- Frozen basis: `e84ee01e12a7713a59b72679308ecc1d44264c1a`.
