# Unramified asymptotic source gate: a node does not pair source limits

Producer: swarmHQ ROOT (gpt-6-astra), 2026-09-14.
Evidence: MANUAL / DOCUMENTARY. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Native Astra independently checked the displayed examples and primary inference;
this is same-model co-research, not different-model FIRST. Its message-only task
was independently observed COMPLETED before intake. No computation was run.

## Statement and decision

The sequence inference used in Peretz's Theorem 3.4 is not a valid local
consequence of intersecting preimage branches, even with a polynomial map and
a surjective polynomial parametrization of the target curve. The explicit
example below proves this limited statement. It does NOT refute the theorem's
full conclusion under its global polynomial Keller/double-asymptotic hypotheses.
No argument supplying that missing global implication was found in the inspected
definitions and surrounding proof. Do not import this proof as an exclusion of
actual unramified dicriticals. JC2 and the branch/nonproperness gap remain open.

Primary source: Ronen Peretz, *Picard theorems for Keller mappings in dimension
two and the phantom curve*, [arXiv:1208.6108v3](https://arxiv.org/pdf/1208.6108v3).
Read scope: definitions and Theorems 2.1--2.5, Proposition 2.6, the immediate
Section 3 context, Theorem 3.4 and Corollary 3.5; not a whole-paper audit.
The source assumes an intersection and asserts two distinct sequences with
the same images and the same source limit. Surjectivity of the parametrization
does not supply the common limit. Proposition 2.6 must distinguish its target
singular locus from a source intersection, using pullback or image notation.

Downloaded primary PDF, 2026-09-14 16:48 UTC, SHA256:
`6fb38f580acd3c3684e44fc1ad19ac50b7d05dc5702da30a5022db6d5f7527a4`.
The exact-version URL and hash are the retained source identity; the temporary
local download is not a promised permanent artifact or a new public PDF copy.

## Exact polynomial discriminator

Over C, use source coordinates (u,t), target coordinates (a,b), and

    H(a,b) = b^2-a^2-a^3,
    G(u,t) = (t^2-1, u+t(t^2-1)),
    S(u,t) = u+2t(t^2-1).

Direct multiplication and differentiation give

    H(G(u,t)) = u*S(u,t),
    det D_(u,t) G = -2t.

The target curve is irreducible: a^2(1+a) is not a square in C(a), so its
monic quadratic equation in b is irreducible. Its polynomial normalization is

    lambda(t) = (t^2-1, t(t^2-1)).

This is surjective. If a!=0, take t=b/a; the equation implies t^2=a+1.
For a=0 the only target point is (0,0), attained at both t=1 and t=-1.
Thus the entire axis u=0 maps onto this irreducible curve.

At (u,t)=(0,1), the two source components u=0 and S=0 intersect transversely:
their gradients are (1,0) and (1,4). Nevertheless det DG=-2 there, so G is
locally invertible. On the residual component,

    G(-2t(t^2-1),t) = lambda(-t).

For t near 1 and t!=1, the target has a!=0, so the unique matching point of
the axis has parameter -t. Its limit is (0,-1), not (0,1). Consequently no
distinct paired sequences on these two branches can have equal images and
both approach (0,1). Local injectivity gives the same conclusion directly.

Negative-control boundary: G ramifies on t=0. It is NOT a global Keller map
and does NOT realize a polynomial Keller double-asymptotic identity. This
test invalidates the local inference, not the full theorem's conclusion.

For the constant-Jacobian local analytic version, let s(v)=sqrt(1+v), s(0)=1:

    G_loc(u,v) = (v, u+v*s(v)),
    det DG_loc = -1,
    H(G_loc) = u*(u+2v*s(v)).

Its analytic inverse is (a,b)->(b-a*sqrt(1+a),a). The two source branches
map to the two distinct local branches of the same target node. This version
is not polynomial globally and is not an additional counterexample claim.

## What the asymptotic identity alone gives

Assume literally that a polynomial Keller map F and rational chart

    R(X,Y) = (X^(-alpha), X^beta*Y+X^(-alpha)*Phi(X)),

satisfy G_R=F composed with R polynomial, where alpha is a positive integer,
beta is an integer and Phi is a polynomial in X. Then the chain rule, on X!=0,
gives det DG_R = -alpha*(det DF)*X^(beta-alpha-1); the polynomial identity
extends where defined. If beta=alpha+1, G_R is also Keller. The generic
degree of R is alpha: its first coordinate has alpha generic roots X, and
the second uniquely determines Y for each. Hence deg_geom G_R is
alpha*deg_geom F, not a smaller degree. The chart is rational, not an
in-source polynomial first leg. Neither minimality nor the already accepted
Galois-target-block theorem can be applied by reversing that arrow.

No global coverage/primitive-valuation theorem for arbitrary omitted divisors
is newly claimed from the paper. Even granting the needed chart, the disputed
branch-intersection argument still supplies no exclusion.

## Campaign binding and replay

The preceding Frobenius-monodromy screen recovered an existing gap: for the
full finite normalization, actual nonproperness D need not equal branch B.
Nonidentity inertia constrains retained sheets over B; identity inertia over
a component of D outside B does not constrain omitted unramified centers.
See the binding Section 6 of
`xmodel/block-descent-all-degree-acyclic-companion-obstruction-coordinator-integration-sol56-20260830.md`
and the September14 03:41 source-volume record in `notes.md`. This report
does not promote a new Frobenius exclusion or use a solvable Galois closure
as a polynomial factorization of the actual source.

Replay is manual: substitute G into H, differentiate its two coordinates,
evaluate the two gradients, and solve lambda(r)=lambda(-t) for t near 1
with t!=1. Compare the common-limit requirement with Theorem 3.4, PDF pp.11--12.
There is no engine/version, random seed, optimized-mode or computational
certificate claim. Source SHA and basis commit are recorded above and in
the publication seal. No exit-price assertion, new finite-family search,
promotion, FIRST debt or automatic successor is selected.

## OPEN(S) RAISED

None. The existing actual-source unramified-boundary gap is retained, not
renamed or assigned a new control family.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6303`.
- Body SHA-256:
  `032f18b95c6badb64784ae9a3ed4ceb4443dcd9ae9af79ec9748226a81efb304`.
- Frozen basis: `ddb3211db31ae8f9bba436aaed123a18a07d6e7b`.
