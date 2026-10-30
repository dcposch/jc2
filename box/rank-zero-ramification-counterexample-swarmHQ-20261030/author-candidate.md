# Rank-zero obstruction to unramified critical-curve restriction

Status: INTERNAL / ROOT-MANUAL / UNREVIEWED. One explicit scope control; no JC2 conclusion.
Task: RANKZERO1755. Basis: e84ee01e12a7713a59b72679308ecc1d44264c1a.
Producer: swarmHQ ROOT. No CAS, parameter sweep, external theorem adoption or paid lane.

## Exact construction

On the smooth source S=A2_C with coordinates u,v define the polynomial map to T=A2_C by

    P=u^4+u*v,
    Q=3*v^2+12*u^3*v+8*u^6.

This is a finite map. Its reduced critical divisor is the single smooth line E={v=0}.
The differential has rank zero at (0,0). The map E to the normalization of its image
has local parameter order two at that point, and global curve degree two.
Thus the rank-one assumption of the reviewed local lemma cannot simply be removed,
even while retaining smooth source, smooth target, finiteness and one smooth critical curve.

## Jacobian and rank

    P_u=4*u^3+v,              P_v=u,
    Q_u=36*u^2*v+48*u^5,      Q_v=6*v+12*u^3.

Therefore

    P_u*Q_v-P_v*Q_u
      =36*u^3*v+48*u^6+6*v^2-(36*u^3*v+48*u^6)
      =6*v^2.

Every displayed first derivative vanishes at the origin. Away from the origin on E,
P_u=4*u^3 is nonzero, so the old rank-one lemma applies there without contradiction.

## Finiteness

The following identity is monic in u over A=C[P,Q]:

    u^8-6*P*u^4+Q*u^2-3*P^2=0.

After substitution, its u^8, u^5*v and u^2*v^2 coefficients are respectively
1-6+8-3, -6+12-6 and 3-3, all zero. Thus u is integral over A.
The second coordinate satisfies the monic equation over A[u]

    v^2+4*u^3*v+(8/3)*u^6-Q/3=0.

Hence v is integral over A[u], and C[u,v] is finite over A by transitivity and
finite generation. The Jacobian is not identically zero, so P,Q are algebraically
independent in characteristic zero; the target is the stated affine plane.
The only point over (P,Q)=(0,0) is the origin: P=0 gives either u=0 or v=-u^3;
the first case forces v=0 and the second gives Q=-u^6, hence u=0.
The same construction therefore gives a finite holomorphic germ at the origin.

## Image normalization and local ramification

On E the map is u -> (u^4,8*u^6). Its reduced image is the cusp D: Q^2=64*P^3.
Put t=u^2. The image coordinate ring is C[t^2,t^3], and its normalization is C[t].
Indeed t=Q/(8*P) belongs to the image function field, t^2=P proves integrality,
and C[t] is integrally closed with that same function field.
The induced map E -> normalization(D) is exactly t=u^2.
It has degree two and ramification index two at u=0; away from zero its local order is one.
This is an actual counterexample to the rank-zero extension, not to the rank-one lemma.

## Scope, history and remaining gap

The map is not Keller: its Jacobian vanishes on E. The complement S\E has coordinate
ring C[u,v,v^(-1)] and a nonconstant unit v, so it is not an affine plane.
Consequently this does not realize the marked whole-source Keller normalization package.
It blocks a local smoothness-only inference; it proves neither existence nor exclusion of
rank-zero obstructions for the actual Keller source, and leaves singular-source cases open.

The October20 CJD1311 journal already records A(z)=1+4z+(8/3)z^2, B(z)=1+z and
R(z)=z*B(z)^3/A(z)^2. For this construction z=u^3/v gives 9*P^3/Q^2=R(z).
Thus the one-variable rational quotient is recovered, not novel. No identification of
the two surface maps, monodromy claim, donor repair or construction successor is inferred.
The old fixed-target descent stops remain. The stopped DC2-REVIEW body was not read.
Fresh frozen searches are lexical routing only; priority for this exact use is unassessed.
External search snippets supplied no theorem used in the construction.

Independent review must recompute the two identities, finiteness, cusp normalization,
local parameter order and the whole-source scope limitation before public integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3887`.
- Body SHA-256:
  `9363cfb529bd6d9452d30b3d768c620d3b6c3bba7b1581b4917d315c1fb4bb94`.
- Frozen basis: `e84ee01e12a7713a59b72679308ecc1d44264c1a`.
