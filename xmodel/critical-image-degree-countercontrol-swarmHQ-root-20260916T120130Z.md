# A simple critical line does not force coprime or dividing image degrees

Producer: swarmHQ ROOT (gpt-6-astra), September16,2026 UTC.
Basis: e1be96d29c9c351502bc2840c6ab09b189a26227.
Evidence: MANUAL exact characteristic-zero algebra.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model review.
Native Astra independently checked this witness and found a separate one;
that same-model check is not FIRST. No literature-novelty claim.

## Claim and motivation

There exist P,Q in Q[g,p] with J_(g,p)(P,Q)=g such that their
restrictions to the critical line g=0 have degrees6 and9. Their gcd is3,
and neither degree divides the other. Thus the proposed universal
coprime-or-dividing condition for critical-image degrees is FALSE.

The [reviewed simple-critical-line result](simple-critical-line-f10-swarmHQ-root-20260916T105500Z.md)
proves primitivity of the nonconstant critical parametrization, local
cusp orders and e2/f1. It does NOT assert this global degree condition.
Its literal F10 application has critical degrees7(3r+1),7(5r+2), so the
false condition would have excluded that whole source contract. This
countercontrol rejects that proposed inference, not any claim of the
reviewed result. It neither realizes nor excludes a point of the F10
contract, and it is not a Keller map or a JC2 counterexample.

## Explicit polynomial witness

Work in Q[g,p] and set

    t=2g+2p^3,
    P=(t^2-p^2)/4,
    Q=p/2+(2/3)t^3-p^2*t.

These are literal polynomials. First compute in the independent
coordinates(t,p):

    P_t=t/2,       P_p=-p/2,
    Q_t=2t^2-p^2, Q_p=1/2-2pt.

Consequently

    J_(t,p)(P,Q)
      =(t/2)(1/2-2pt)+(p/2)(2t^2-p^2)
      =t/4-p^3/2.

The coordinate change(g,p)->(t,p) has determinant2. The polynomial
chain rule therefore gives

    J_(g,p)(P,Q)=2(t/4-p^3/2)=g.

No localization, omitted source point or unknown Keller pair is used.
Restriction to g=0 yields

    a(p)=p^6-p^2/4,
    b(p)=(16/3)p^9-2p^5+p/2.

Their nonzero leading coefficients establish the claimed degrees
6 and9. These are degrees of two univariate critical-image coordinates,
not a mapping degree, an F10 source degree or a constant-Jacobian bound.

## Independent replay and scope controls

Reproduce the four displayed derivatives, their determinant and the
chain factor2 by hand, then substitute g=0. This is a desk proof, not a
CAS certificate; no mathematical scripts, seeds, primes or numerical
search were used. The coefficient field is exactly Q, hence also C.

For a useful sensitivity check, replace2/3 in Q by a rational lambda,
leaving all other formulas unchanged. The determinant becomes

    g+(3lambda-2)*p*t^2.

Thus the cancellation is an exact coefficient identity, not merely
smooth critical support or agreement of highest degrees. Forgetting
the source chain factor2 would give g/2, not the displayed normalization.

The witness is fully consistent with primitive normalization and local
cusps. No injectivity or embedding of the critical image is inferred.
No classification of all maps with a linear Jacobian is supplied.
Conditions special to the F10 coefficient contract, including its
particular degree ratios and inverse-polynomiality conditions, remain
outside this control. There is no automatic parameter-family successor.

## History comparison

The current critical-line proof and its Sol review are the nearest
accepted results. The old universal linear-Jacobian integrality proposal
was already withheld because it contains JC2; no such theorem is used.
Targeted searches in APPROACHES, AUDIT, the strategy archive, notes and
xmodel found no exact prior critical-image degree constraint or this
witness. Some discovery output was clipped: this is not an exhaustive
novelty or literature survey. The negative test arose directly from the
new candidate and closes that test; it does not reopen an old solver.

## OPENS RAISED

None. The proposed degree shortcut is refuted, not converted into a
weaker unproved exclusion or a new bounded-degree search.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4123`.
- Body SHA-256:
  `08feebc46d0fe0b0672f5fe7db2225f55a6b979e938b15e7a7a72808c3d1e6d1`.
- Frozen basis: `e1be96d29c9c351502bc2840c6ab09b189a26227`.
