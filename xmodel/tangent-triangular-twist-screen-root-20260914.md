# Two-dimensional tangent sweep: a fixed triangular-twist screen

ROOT, September14,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
This is a bounded construction screen, not a JC2 proof, a new general
classification, or a claim of literature novelty. No computation or agent
review was used. The selected construction is stopped; no parameter farm,
twist-word search, or automatic review/extension is selected.

## Question and exact scope

Let p,q in C[t], with d=deg p>=1 and q'=t*p'/2. An arbitrary integration
constant in q is allowed. Put

    S(gamma,t)=(U,V)=(p(t)+2gamma, q(t)+gamma*t).

Its Jacobian in (gamma,t) is 2gamma. For an integer a>=1 take the fixed
birational target change

    tau_a(U,V)=(U/V^a,V),       G_a=tau_a composed with S.

Allow ANY dominant rational source substitution H:A2 -->> A2_(gamma,t),
not only a birational or symplectic one. The proposed construction is

    F=G_a composed with H.

The test is whether the two resulting rational functions can both be
polynomials with constant nonzero Jacobian. The argument below says NO.
It is uniform in d,a and H, but does NOT cover arbitrary birational target
changes, arbitrary projections of the three-dimensional construction,
or every possible plane Keller map. In particular it does not exclude the
three-dimensional monomial twist, which retains an additional coordinate.

The missing construction implication was simultaneous removal of all
source poles while retaining the nontrivial covering. The cheapest test
was the normalization of the compulsory branch curve, before any coefficient
ansatz. This test fails independently of the choice of rational source H.

## 1. Finite sweep and its actual branch valuation

We have deg q=d+1 and leading coefficient lc(q)=d*lc(p)/(2(d+1)). Eliminating
gamma gives

    q(t)-t*p(t)/2+U*t/2-V=0.

This polynomial in t has degree d+1 and nonzero constant leading coefficient
-lc(p)/(2(d+1)). Thus S is finite, with source ring C[gamma,t] integral over
C[U,V]; gamma=(U-p(t))/2. Its source is normal.

The divisor gamma=0 maps to the curve K parametrized by (p(t),q(t)). It is
generically a simple ramification divisor: the determinant has a simple
zero there, and the restricted curve map has nonzero derivative at generic
t. Equivalently, the displayed elimination polynomial has a double root
there, with second derivative -p'(t)/2 nonzero generically. Its ramification
index over the generic point of K is therefore 2.

The curve parametrization is birational. Indeed
[C(t):C(p,q)] divides both [C(t):C(p)]=d and [C(t):C(q)]=d+1, so it is 1.

On the open V!=0, tau_a is an isomorphism. Hence the SAME ramified valuation
has index 2 over the generic point of the irreducible affine curve

    Gamma_a = closure{(p(t)/q(t)^a,q(t)): q(t)!=0}.

No assertion at a deleted zero of q is needed to identify this generic
branch divisor.

## 2. The transformed branch curve has at least two punctures

Its function field is still C(p,q)=C(t), since p is recovered as the first
coordinate times the a-th power of the second. Therefore its smooth
projective normalization is P1_t, not an unexamined finite quotient of it.

At t=infinity the second coordinate q(t) has a pole. There is also at least
one FINITE zero b of q at which p/q^a has a pole. Otherwise the rational
function p/q^a would have no finite poles and would be a polynomial, so
q^a would divide p. This is impossible because a*deg q>deg p.

These are two distinct places absent from the affine normalization of
Gamma_a. There might be more; only these two are required. Consequently
Gamma_a has no nonconstant polynomial parametrization A1->Gamma_a. Such
a parametrization would lift to its normalization. A coordinate on P1
with zero and pole at two of the omitted places is an invertible regular
function there, so its pullback to A1 would be constant, forcing the lifted
map to be constant.

In particular, rationality alone is not the required polynomial
parametrizability. Cancellation at some common roots of p and q does not
remove this obstruction: the degree argument guarantees at least one
uncancelled finite pole.

## 3. A dominant rational source change cannot discard the ramification

Suppose the constructed F were a polynomial Keller map. Its fields fit into
a finite tower

    C(F_1,F_2) subset C(gamma,t) subset C(x,y),

where the middle embedding is the pullback by H. Dominance of H makes it
an embedding, and dimension two makes the extension finite. Extend the
index-2 branch valuation from the middle field to C(x,y). Ramification
indices multiply, so its index over the target Gamma_a is at least 2.

Let Z be the finite normalization of the target A2 in C(x,y). The extended
valuation has a divisorial center on Z over the generic point of Gamma_a.
The actual Keller map is quasi-finite and factors as an open immersion
A2_source -> Z followed by the finite map. Since F is etale, that ramified
divisor cannot be in its source open subset.

Thus F is nonproper along the generic point of Gamma_a, and Gamma_a is a
component of its nonproperness locus. One can also see the last implication
by contradiction: properness on a neighborhood would make the quasi-finite
F finite there and identify its normal source with the full normalization,
which would leave no room for the ramified missing divisor.

But every irreducible curve component of the nonproperness set of a
generically finite polynomial plane map is polynomially parametrized.
This contradicts Section2. Therefore no such F exists.

This argument needs the actual FULL-plane polynomial source only at this
last nonproperness theorem. It does not claim the same theorem for every
smooth affine surface or every open subset of A2.

## 4. Untwisted check and stopping decision

For a=0 the simpler integrality argument already stops the construction:
polynomial outputs U,V make the rational t integral over C[x,y], hence
polynomial, and then gamma is polynomial too. The identity

    J(U,V)=2gamma*J(gamma,t)

cannot be a nonzero constant: it would make gamma a constant unit, making
the right side zero. This is the familiar normality/pole-removal obstruction,
not a new theorem about all rational regularizations.

An exact out-of-scope positive control checks the nonconstant-p hypothesis.
If p=q=0 and a=1, then G_1(gamma,t)=(2/t,gamma*t). The dominant rational
substitution H(x,y)=(xy/2,2/x) gives the polynomial identity map (x,y).
Here the untwisted sweep is NOT finite and gamma=0 is contracted to a point;
the index-2 branch-curve argument is unavailable. Thus the proof cannot be
extended merely from the formula J(S)=2gamma to every such rational map.

The a>=1 screen uses the branch curve in addition to that old principle.
It stops this direct plane transplant before source-parameter searches.
It supplies neither a construction outside this family nor a necessity
theorem placing hypothetical JC2 counterexamples in the family. No change
to the global avenue ranking follows. Different-model FIRST has NOT been
performed; no result is promoted or used as a premise for descendants.

## Sources and history scope

- Gao, arXiv2608.00222v1, Sections3.1--3.3, supplies the displayed sweep,
  derivative identities and the distinct three-dimensional twist:
  https://arxiv.org/html/2608.00222v1 . ROOT read these selected sections,
  the introduction, and selected Section4.4 material, not the whole paper
  or its computational appendix. No reported higher-dimensional example
  was reverified or newly adopted.
- Jelonek--Lason, arXiv1411.5011v2, Theorem1.2, Definitions2.1/2.3,
  Proposition3.1 and Theorem3.2 with its complete proof on printed pages4--5:
  https://arxiv.org/pdf/1411.5011v2 . These are selected primary passages,
  not a whole-paper audit. Only polynomial coverage is used, not its
  quantitative degree bound. This is already a campaign import (see
  tangent-coordinate-descent-astra-20260913), not a new external theorem.
  Attempts to open the 1993 publisher PDF and a Citeseer mirror failed;
  they supplied no primary body for this screen.
- History checked before this construction: current APP geometry/construction
  sections; September13 notes16:50 fixed cotangent target regularization,
  20:23 secant escape, 14:27 Gaussian test and 06:06 eigenvaluation stop;
  selected tangent-coordinate-descent report; targeted canonical/report
  searches. The Gaussian, dynamical and moving-line proposals were recovered
  as old gaps and received no agent or successor. No exhaustive novelty
  search is claimed. Some broad read/search output clipped; only recovered
  named passages were used.

The standard valuation-extension, multiplicativity and quasi-finite
normalization facts above are used at manual mathematical tier. This screen
is not an independently reviewed replacement for their hypotheses.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8831`.
- Body SHA-256:
  `ade6e356f0b81639e324765806f62626ee3035021793553dc9ecffe6fd11a6bf`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
