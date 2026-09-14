# One-cycle zero-base constructive attempt

Producer: swarmHQ, gpt-6-astra. Date: 2026-09-14.
Stage basis: 46273dedf31631d1973e24566431c282da2f8b23.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Scope: one bounded constructive reset; no scientific computation or promotion.

## Result

**NO_CANDIDATE.** One explicit construction attempt reaches a rational
constant-Jacobian map of generic degree seven, but its finite normalization is
the affine plane. The frozen finite-class-group source-boundary screen therefore
already rejects it. An elementary calculation below exposes the exact failure:
every polynomial pullback has Jacobian divisible by the cube of a polynomial
whose constancy would destroy dominance.

This is a failed construction, not a new family-exclusion deliverable or a
surviving mechanism. It changes no closing test. No second candidate, nearby
exponent ladder, source read, or successor is selected.

## Construction and discriminator

Work over C. Start with L=C(x,y)=C(x,z), where z=y/x^3. The idea was to
integrate an algebraic differential along the parabolas P=x+z^2 and then
absorb the resulting volume factor into the rational source coordinate.
Take

    P=x+z^2,
    Q=x^3*z+2*x^2*z^3+(8/5)*x*z^5+(16/35)*z^7.

At fixed P, this is

    Q=P^3*z-P^2*z^3+(3/5)*P*z^5-(1/7)*z^7,
    (dQ/dz)|P=(P-z^2)^3=x^3.

In the literal original variables the rational map is

    P=x+y^2/x^6,
    Q=y+2*y^3/x^7+(8/5)*y^5/x^14+(16/35)*y^7/x^21.

Its regular domain includes x!=0; the displayed poles along x=0 are actual
poles, so these are not polynomial coordinates. The FULL determinant is
checked as follows, first differentiating in (x,z):

    P_x=1, P_z=2*z,
    Q_x=3*x^2*z+4*x*z^3+(8/5)*z^5,
    Q_z=x^3+6*x^2*z^2+8*x*z^4+(16/5)*z^6,
    det d(P,Q)/d(x,z)=Q_z-2*z*Q_x=x^3,
    det d(x,z)/d(x,y)=x^(-3),
    det d(P,Q)/d(x,y)=1.

Thus this part of the attempt succeeds exactly, on the rational function
field. The generic degree is seven: L=C(P,z), and Q is a degree-seven
polynomial in the transcendental z over C(P). This is a rational-map
degree, not the degree of any polynomial Keller example.

The first global gate immediately fails. Put A0=C[P,Q]. The equation

    z^7-(21/5)*P*z^5+7*P^2*z^3-7*P^3*z+7*Q=0

makes z integral over A0. Since x=P-z^2, the ring

    S=C[P,z]=C[x,z]

is finite over A0, has fraction field L, and is integrally closed. It is
therefore the full normalization of A0 in L. In particular Cl(S)=0: the
candidate hits the known source-boundary screen before any coefficient
search or new theorem is needed. The missing divisor x=0 is principal;
the finite map S->Spec(A0) has Jacobian x^3 there.

Here is the pole-removal condition tested without hiding it in an endpoint.
Allow ANY dominant rational source substitution

    phi*: C(x,y) -> C(u,v), with x |-> a, y |-> b,
    a,b in C(u,v), a!=0; put w=b/a^3.

Suppose BOTH pullbacks A=P(a,b), B=Q(a,b) lie in R=C[u,v], and
det d(A,B)/d(u,v)=c in C*. Their monic septic relation forces w to be
integral over R. Normality of R gives w in R, and then a=A-w^2 is in R.
The full chain rule now gives

    det d(A,B)/d(u,v)=a^3 * det d(a,w)/d(u,v).

The right side is a product in R. Equality to a nonzero constant forces
a to be a nonzero constant, which makes det d(a,w)=0, a contradiction.
Thus NO dominant rational substitution polynomializes this proposed pair
into a Keller pair. This includes substitutions with nontrivial generic
degree; no birationality assumption was used.

Negative control: phi(u,v)=(u,u^3*v) really removes every displayed pole.
The resulting polynomial pair is

    A=u+v^2,
    B=u^3*v+2*u^2*v^3+(8/5)*u*v^5+(16/35)*v^7,
    det d(A,B)/d(u,v)=u^3.

It passes polynomiality and fails the constant-Jacobian gate on u=0. This
checks precisely the temptation that motivated the construction, rather
than testing only the rational determinant on its punctured domain.

## Remaining gaps and disposition

No mathematical gap remains in rejecting this specified attempt at the
MANUAL tier. The general JC2 gap remains untouched: no new source whose
global regularity could escape the frozen boundary criterion was produced.
No assertion of novelty, exhaustive search, or literature priority is made.

The smallest test for this attempted mechanism was the displayed monic
equation and source determinant, completed by hand. Had a rational source
substitution yielded polynomial A,B with nonzero constant determinant, its
actual generic degree and global ring map would have required independent
verification before any counterexample claim. The actual outcome is the
contradiction above, so the attempt stops. There is no proposed next science
test to launch; renaming the primitive or changing its exponent would retain
the same finite-normalization obstruction. ROOT owns any history checksum,
different-model review decision, and future allocation.

## OPENs RAISED

None.

## Custody and read scope

Invitation accepted at approximately 21:44 UTC; conservative terminal cap
22:09 UTC, with target 22:05 UTC. Only this transaction is writable.

Read WHOLE, with SHA256 verified:

- box/zero-base-construction-20260914T2145Z/PROMPT.md:
  9eb9a1d01156e0c5f51c1bc9c49af3ec36a62eafb4c36a8963b6870d2579366b.
- box/ideation-swarmHQ-20260914T2110Z/STATE-DELTA.md:
  056e5ecebd2192599dde6f67af720b9c8c797b538c8b4930fc9938a9fdebfd07.
- box/ideation-swarmHQ-20260914T2110Z/FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

Governing instructions read WHOLE: AGENTS.md, README.md, COORDINATION.md,
team/swarmHQ/README.md. No mutable research ledger, current peer report, or
prior model report was opened for research. No external source was read;
no source-dependent theorem beyond the frozen screen is claimed. No CAS,
scientific code or enumeration, worker, subagent, contact, or promotion.
All identities above were derived and checked manually.

Read-scope deviation: before reading the brief, an administrative filename-only
`rg --files` search was mistakenly scoped over /home/ubuntu as well as the
assigned checkout. It displayed paths of other prompt files and another
checkout's artifact tools. None of those file contents was opened. I cannot
certify that this overbroad traversal respected the requested inspection
boundary; this deviation is disclosed rather than counted as compliant
research coverage. Subsequent reads used the exact paths stated above and
administrative tool help. The mandated collision checker is a mechanical
contract operation, not a research read or history checksum.

Administrative interpreter: Python 3.12.3. Transaction owner:
swarmHQ-zero-base-constructive. Workflow: begin with the full stage basis,
write only its private partial using apply_patch, obtain real COLLISIONS
output, append the final marker as the last author write, close, finalize,
verify. Final full/body/manifest hashes are returned in the terminal receipt.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7055`.
- Body SHA-256:
  `56dcc708deca003382fc8893cd04acf700932b0472ed559a662db6303bcc922b`.
- Frozen basis: `46273dedf31631d1973e24566431c282da2f8b23`.
