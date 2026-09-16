# Different-model review: all additive actions on the fixed running core

Reviewer: swarmHQ gpt-5.6-sol, native task torus_quotient_sol_review.
Recorder: ROOT, faithfully recording the terminal mathematical review and
final verdict; this is not a verbatim execution log or a Sol-authored file.
Evidence: MANUAL hostile proof review. Verdict: CONFIRMED, items A-E.
Mathematical completion: 2026-09-16T02:32:48Z.
Reviewed contribution: 05ec9c9151b6c55e4904ed741252a2b68d6aa275.

## Custody and literal scope

The [charged proof](running-core-additive-rigidity-swarmHQ-root-20260916T023000Z.md)
and its manifest were frozen before review. Sol verified the expected
basis, body/full/manifest hashes and 0444 modes, and unchanged comparison
pins and HEAD. ROOT collected the whole mathematical message and final
verdict and observed authoritative COMPLETED before recording this review.

Exact pins:

- Producer body:
  d0d854cf0c064c15446b3d2839af2b1f14c0437110120f57d5604f00fd4d3425.
- Producer full:
  018b92535b7bd51313b2c005d85ab6dd9043b873c8b8276a35b9ccc386925f47.
- Producer manifest:
  7403c0c4437bf851d45071fa4e4bc3b8099f945cb945838e871a8d76cfbea9a5.
- Embedded basis: f70043e502f4c754671309f1786640113734dcab.
- [Earlier single-action comparison](additive-quotient-descent-swarmHQ-root-20260915T232000Z.md):
  a6919a3e38f1e0c9d78b88262435164e7905284d465e4fb94bc37a690642e96e.
- [Whole-fiber comparison](embedded-plane-transfer-root-20260913.md):
  dacca2ffa54c839fc4c9c0e20b55033379c3b5bd8defeffd9c58ce3a57af3709.
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

The literal map over C is

    P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
    Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
    R=2x-3x^2 y-x^3 z,
    F=(R,Q,P), target coordinates (r,s,t).

The review concerns ALL algebraic source and target Ga actions satisfying
F rho_a=tau_a F. It does not assume linearity, primitivity, freeness,
equal actions, or full polynomial quotient kernels.

No reviewer files, network, scientific computation, cloud jobs or descendants
were used. Hash checks support custody, not mathematical validity.

## A. Exact nonproperness and cubic fibers — CONFIRMED

On x!=0, put v=y+1/x, w=1/x. The reconstructed formulas are

    s=2w+4v-3rv^2,       t=v^2+vw-rv^3,
    p(V)=rV^3-2V^2+sV-2t,       w=p'(v)/2.

The two chart Jacobians are -x and -2w, giving det DF=2 everywhere.
Simple roots correspond bijectively to source points in this chart;
repeated roots do not. When r!=0 the cubic discriminant is 4b, where

    b=s^2-rs^3-16t-27r^2t^2+18rst.

When r=0 the quadratic discriminant is b(0,s,t), and the unique extra
x=0 point is (0,s,t-4s^2). Thus every fiber has three points off B=V(b),
and fewer on B; there is no extra r=0 component.

The inverse-function theorem and the global three-point bound justify
properness near a full fiber. Approaching a deficient fiber through full
fibers forces some preimages to escape: otherwise compactness and local
injectivity would fit three branches into fewer central points. Therefore
the actual nonproper-value locus is exactly B, not just a polynomial
discriminant or a ramification locus in a chosen completion.

## B. Normalization and singular hyperbola — CONFIRMED

The polynomial b is primitive in C[r,s][t], with quadratic discriminant
4(4-3rs)^3 nonsquare in C(r,s), hence irreducible. The normalization is

    nu(r,v)=(r,4v-3rv^2,v^2-rv^3).

Finiteness and birationality follow respectively from

    v^2-sv+3t=0,       (3rs-4)v=9rt-s.

The normal ring C[r,v] is finite over C[B] with the same fraction field,
so it is the entire normalization. Differentiating b gives no singular
point at r=0. At r!=0 the singular locus is exactly

    rs=4/3,       r^2t=4/27.

Its reduced inverse image is H=V(rv-2/3), using
rs-4/3=-3(rv-2/3)^2 and the second singular equation. In particular H
is a hyperbola, not a line.

## C. Algebraic lifting and Ga-rigidity of B — CONFIRMED

An algebraic action on B lifts algebraically to its normalization:
the dominant composite Ga x A2 -> B has normal source and factors
uniquely through nu; uniqueness gives the group laws. Automorphisms
preserve the singular locus, so the lift preserves H.

For its LND D, preservation of the principal ideal of h=rv-2/3 gives
D(h) in (h). Additivity of LND-degree in a characteristic-zero domain
then forces D(h)=0. Factorial closure of the kernel applied to rv
forces D(r)=D(v)=0. Thus both the lifted action and the original action
on B are trivial. This uses an algebraic action, not just separate
rational lifts or a formal flow.

## D. No hidden ambient action — CONFIRMED

An ambient LND E preserving B has E(b) in (b), hence E(b)=0 by the
same degree argument. Divide its three polynomial coefficients by their
maximal common power b^m to obtain E=b^m E0. Then E0(b)=0, and

    E^n(a)=b^(mn) E0^n(a).

Consequently E0 is locally nilpotent. Some coefficient of E0 is nonzero
modulo b, so it induces a nonzero LND on C[B], contradicting C.
This rules out even ambient actions that initially fix B pointwise.

## E. Every equivariance is trivial — CONFIRMED

Equivariance transports properness under source/target automorphisms,
so every tau_a preserves the exact nonproper-value set B. Item D
makes tau trivial. Every rho-orbit then lies in a finite fiber, and
connectedness of Ga makes it a point. Thus rho is also trivial.

Separate polynomial source and target conjugacies preserve this
conclusion. Stabilization does not: F x id admits translations in the
added coordinate. Other maps, other groups, arbitrary projections,
nonalgebraic flows and general JC2 remain outside scope.

## Negative controls and provenance — CONFIRMED

- The cusp cylinder s^2-r^3=0 admits t-translation. Its normalization
  has singular preimage a line, showing that nonnormality alone is not
  the rigidity argument.
- The nonzero LND r partial_s fixes V(r) pointwise. The maximal-factor
  argument needs rigidity of the actual quotient ring.
- The Gm action (r,s,t)->(lambda r,s/lambda,t/lambda^2) preserves B,
  lifting to (r,v)->(lambda r,v/lambda); the theorem does not exclude
  multiplicative symmetry or all automorphisms.
- Stabilized added-coordinate translation is an exact scope control.

The charged proof credits the [shadybrook audit, Sections4--5](https://github.com/shadybrook/jacobian-counterexample-audit/blob/main/paper/main.md)
for prior overlap in the nonproperness surface, normalization and
triple-root hyperbola. That geometry is not a novelty claim. The review
does not certify an exhaustive literature search or the entire external
paper. No low-degree plane Keller theorem is needed for this proof.

## ROOT intake

ROOT's independent reconstruction agrees with A-E. Sol found no correction
or missing implication at this literal scope. The result closes the
fixed-core additive-quotient construction without an action-coefficient
search; the earlier general conditional quotient bridge is not refuted.
Producer lifecycle wording remains frozen; promotion belongs in AUDIT.
No descendant, expanded family or JC2 conclusion is proposed.

## OPENS RAISED

None; review complete at its charged scope.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised OPEN identifier. This lexical check does
  not certify mathematical novelty or correctness.

Checker exit0/EMPTY was collected. ROOT matched all five charged file
hashes and producer 0444 modes after intake; unchanged. Recording complete.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7478`.
- Body SHA-256:
  `62e279f7265061badc0db7cf0daf371325d3f58ce609a8df7daa853fa4932779`.
- Frozen basis: `05ec9c9151b6c55e4904ed741252a2b68d6aa275`.
