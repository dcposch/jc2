# Why divisor closure does not define the proposed nonproper pushforward

Producer: swarmHQ coordinator (gpt-6-astra).
Date: 2026-10-06 UTC.
Public basis: 7fa5ab7ac5fce1c41946f72f561cb2ab3cb31ee2.
Evidence tier: MANUAL; desk proof with the named standard imports below.
Lifecycle: PRODUCER-CHECKED; UNPROMOTED. Novelty: UNKNOWN.

This is an exposition of an already adjudicated correction, not a new JC2
criterion, a counterexample, or a new research admission. The original argument
received a same-model Astra hostile check. That is not different-model FIRST,
and this new exposition has no independent review of its own.

## Statement and scope

Let X be the complex affine plane and let j:X -> Y be an open immersion into
a normal integral affine surface. Identify their function fields using j.
Let E_1,...,E_r be the prime divisors in Y minus j(X), and assume r>0.
Suppose f:Y -> X is finite and dominant of degree N. Set

    F = f composed with j : X -> X,
    G = j composed with f : Y -> Y.

This is the formal setup used for the finite normalization of a hypothetical
noninvertible plane Keller map. The argument below does not construct such a map,
and does not assume that arbitrary affine enlargements admit compatible Keller
coordinates. In fact, its divisor calculation does not require the Keller
Jacobian condition.

There is a natural operation on Weil DIVISORS: first apply the finite
pushforward f_*, then take closures of the resulting prime divisors along j.
Write this cycle operation as G_# = j_# f_*.

Under the stated assumptions, G_# does NOT preserve principal-divisor relations.
It therefore does not induce the proposed endomorphism G_* of Cl(Y).
In particular, one cannot combine such a G_* with pullback on Cl(Y) in a
push-pull argument to derive a contradiction.

## Dependencies and prior work

The two standard imports are the localization sequence for Weil divisor classes
on a normal variety and the principal-divisor/norm identity for a finite dominant
map. They are named imports here, not newly source-proof-audited theorems.

The correction appeared in section 3 of the October 6 whole-portfolio synthesis.
Its sealed source has SHA256
e901a727e276218ef1321858ff7aa3e6fa4d33ebfed4e93d3a570ff53ae6ccae,
17855 bytes; associated manifest SHA256
419de65d6fdec4abe6bc234e65b60d5a5c66d9f75541f0998cf4e83e7b6fff8a.
That internal artifact is provenance, not an extra premise: the full relevant
argument is reproduced below. No historical report is rewritten or promoted.

## Proof

Every unit of O(Y) restricts to a unit of O(X)=C[x,y], hence to a nonzero
constant. Conversely constants are units on Y. Thus

    O(Y)^* = O(X)^* = C^*,       Cl(X)=0.

The localization sequence consequently identifies

    Cl(Y) = direct sum over i of Z [E_i].

In particular the omitted divisor classes are independent and nontorsion.
Here and below the field identification used to extend a function from X to Y
is the one induced by the OPEN IMMERSION j, not the distinct embedding f^*.

Choose a nonzero rational function a on X whose extension to Y has
v_(E_i)(a) != 0 for at least one i. Such an element exists because the
divisorial valuation v_(E_i) is nontrivial on K(Y)=K(X).
Write the principal divisor of that extension on Y as

    div_Y(a) = j_# div_X(a) + sum_i v_(E_i)(a) E_i.

Passing to Cl(Y) gives

    [j_# div_X(a)] = - sum_i v_(E_i)(a) [E_i] != 0.

Thus divisor closure itself does not respect principal relations.
To see the failure for the stated self-map G rather than merely for j,
take h=f^*a. The finite-map norm identity, which is valid for f, gives

    f_* div_Y(h) = div_X Norm_(K(Y)/f^*K(X))(h)
                = N div_X(a).

The last equality uses Norm(f^*a)=a^N, with the target field identified in
the usual way. Consequently

    [G_# div_Y(h)] = -N sum_i v_(E_i)(a) [E_i] != 0,

although div_Y(h) is principal. This proves the asserted failure to descend
to Cl(Y). The multiplication by N cannot kill the nonzero class because the
displayed boundary lattice is free.

## What remains valid

Restriction j^*:Cl(Y)->Cl(X) is valid. Pulling back the Cartier classes on
the smooth X along f gives the relevant factorized pullback
G^*=f^* j^*=0. This supplies no missing pushforward.

The finite-map identity for f_* is also valid. The error is extending it
through divisor closure along a nonproper open immersion while silently
discarding the omitted-boundary terms.

## Replay and negative controls

Desk-only. No computation, source acquisition, or new control family is needed.
The proof explicitly keeps the valid finite pushforward as a control and locates
the failure in the following closure operation. If the omitted boundary is empty
and j is an isomorphism, the displayed obstruction disappears; the statement
does not assert that every nonproper map fails every possible class-group action.

## Limitations and next test

This corrects an invalid operation under its own hypothetical setup. It does
not exclude that setup, establish properness, or produce a polynomial Keller
counterexample. JC2 remains unresolved. No new mathematical test is proposed.
A different global argument would have to establish its operations and boundary
hypotheses separately; the valid zero pullback is not a substitute.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `7fa5ab7ac5fce1c41946f72f561cb2ab3cb31ee2` (Git blobs only).

This is the checker's lexical result for a report raising no new OPENs, not
evidence of mathematical novelty or an exhaustive search for prior statements.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5645`.
- Body SHA-256:
  `789899f6670b407f361f5c66cb643e1e35730fb99ad05edce42ca6613847b172`.
- Frozen basis: `7fa5ab7ac5fce1c41946f72f561cb2ab3cb31ee2`.
