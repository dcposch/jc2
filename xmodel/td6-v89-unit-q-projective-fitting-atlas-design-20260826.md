# TD6 V89 design: unit-q orbit gate and shared Fitting atlas

Date: 2026-08-26

Status: **fail-closed successor design; no unit-q result claimed.**  The
V89H1 high-tail collapse branch is withdrawn after its unregistered
`K=2 R38` denominator; the atlas/Fitting design itself remains conditional.

## Input and objective

Let

```text
E = {2,...,14,16,...,24},
p(t) = t^15,
q(t) = t + sum_{e in E} q_e t^e + q15 t^15 + t^25.
```

V87 supplies a literal total-`(F,q_e:e in E)` identity on the normalized
`q15=0` slice.  Its DVR consequence excludes the locus on which `F` and all
22 transverse q coordinates have positive valuation.  V88 supplies an exact
two-sided target-shear coordinate map, so `q15` is arbitrary and is not a
transverse generator.  The remaining problem is the complement

```text
Spec k[q_e:e in E] - V(q_e:e in E),
```

equivalently the 22 principal opens `D(q_e)`.  The objective of V89 is to
cover that complement without recompiling 22 unrelated monolithic clients.

## Gate 0: projectivization is not currently a quotient theorem

The existing exact source-dilation audit is load-bearing.  Under `t -> b t`,
after restoring `p=t^15` and `q'(0)=1`, the transverse jets have diagonal
weights `q_e -> b^(e-1) q_e` and the fixed terminal coefficient becomes
`q25 -> b^24 q25`.  Preserving `q25=1` leaves only `mu_24` (at most `mu_8`
under the determinant-one target normalization used in that audit).  Thus
there is no licensed `G_m` action that can set an arbitrary unit `q_e` to
one.  The unit value, not just the projective direction, must remain in the
coefficient ring.

The exact V88 lower shear removes only `q15`.  The two translations and
reciprocal target scaling are already part of the normalized target gauge;
none mixes two coordinates in `E`.  A nonlinear upper or lower target shear
does not preserve the `(15,60)/(25,100)` rectangles, except for the linear
lower shear already used by V88.

A regular reparametrization `t -> t+h(t)` is not a proved action on this
fixed slice.  It changes `p=t^15` and the chart coordinate as well as q.  The
reviewed orbit audit specifically found the q2-only vector transverse because
every nonzero reparametrization carries its chart component.  Replacing q by
the parameter and moving the deformation into p is therefore a different,
larger source chart unless an exact two-sided map also transports the chart,
all global section coefficients, F1/pole data, centers, and torsion/deck
variables.

**Fail-closed conclusion.**  Proven source/target actions do not identify the
22 unit-q charts.  The finite root-of-unity action preserves the earliest
nonzero exponent and cannot normalize a general unit coefficient.  Any
claimed reduction by orbit must first emit an exact two-sided integral map
on every source coordinate and preserve the registered localization and
Jacobian rows.

## A disjoint ordered cover, not an orbit reduction

For scheduling only, replace the overlapping principal-open cover by the
22 disjoint locally closed strata

```text
S_e: q_j=0 for every j in E with j<e, and q_e is a unit.
```

This uses the earliest nonzero exponent as an invariant and makes the source
dependence triangular.  It does **not** identify distinct `S_e`, set `q_e=1`,
or discard the arbitrary unit radial coordinate.  Write on `S_e`

```text
q_e = b (a registered unit),
q_j = b r_j for j>e,
```

only as a two-sided localization coordinate change.  Its inverse is
`b=q_e`, `r_j=q_j/q_e`, and therefore it is licensed only on `D(q_e)` and
must record every introduced power of `q_e^{-1}`.  Lower q coordinates are
zero by the definition of `S_e`, not by division or omission.

## Shared source-module computation

V87 measured total q-degree one.  Therefore all 39 raw source maps can be
stored once as

```text
M(q) = M_0 + sum_{e in E} q_e M_e,
```

over `Q[C,V,U]_(U H B3)`, with the 132 section labels retained.  A unit-chart
certificate should be searched in a preregistered multiplier support as a
single parametric source-module equation

```text
s = A(q) M(q) + F h(q),       s=U^12 H^3 B3,
```

not by rebuilding transport and FIRST/P12 22 times.  The compiler should:

1. emit each coefficient column `M_e` once, with exact source-key custody;
2. build the bounded Macaulay/source-DAG matrix for the chosen multiplier
   support once;
3. perform fraction-free elimination and emit the pivot minors/Fitting ideals
   that stratify q-space;
4. specialize the same matrix to each ordered chart `S_e` in parallel;
5. replay every accepted certificate against literal raw P12 and all 38 FIRST
   maps, never against only the reduced matrix;
6. fail closed on a q-dependent denominator outside the chart's registered
   unit `q_e` or on any omitted F, q, source-row, or section coordinate.

This is a computational atlas: a single universal compile with independently
replayed pivot strata.  It is not a geometric assertion that the strata are
isomorphic.

## First batching opportunity: high q jets

The reviewed V78B/V78C result separates two algebraic blocks:

- `q2,...,q14` have nonzero reduced genuine-P12 sensitivity;
- `q16,...,q24` are exact **reduced P12 source syzygies**, with their activity
  retained in FIRST/lambda-prime rows.

The second statement is not a finite unit-q coordinate action.  V89H1 sought
the following exact triangular row transformation

```text
T(q16,...,q24) M(q_low,q_high) = M(q_low,0)
```

with a polynomial two-sided inverse.  The literal replay was algebraically
triangular, but its common denominator contains the unregistered factor
`K=2 R38`.  Therefore it does not make the nine high jets source-ideal
coordinates on `D(U H B3)` and does not reduce the atlas to 13 strata.  The
V87 quotients `h_16,...,h_24` and failed H1 multipliers remain discovery
supports only.  Current exact repair gates are a proof that `K` is a unit
modulo the same literal source ideal, a cover of `K=0`, or a registered
alternate pivot/certificate.

No V78 first-order syzygy may be called a total coordinate map without this
integrability replay.

## Atlas output and stopping rule

The first V89 client should output, for every pivot stratum:

- defining equalities and registered nonzero minors;
- exact powers of `U,H,B3,F,q_e` in every denominator;
- the list of literal source rows and multiplier supports consumed;
- a coefficientwise certificate or the smallest unreduced obstruction;
- specializations to V87 at all q zero and to reviewed V86 on the q2 axis;
- a V88 pullback check showing q15 remains an independent shear coordinate;
- negative controls deleting one q transport source, one direct q-prime
  source, one FIRST row, P12, F, and the chart-unit assumption.

Run shards on AWS under unique roots.  Continue on provisionally passing
strata while hostile review runs in the background.

Stop only when the union of emitted strata is proved to be all of
`A^22-{0}` by an exact ideal/radical certificate.  A list of sampled points,
one generic rank, the 22 standard-chart names, or a projective slogan is not
a cover.

## Scope firewall

Even a complete V89 cover concerns only the retained normalized
three-center, fixed F1/pole/dead-stretch source family on `D(U H B3)`, with
q15 transported by V88.  It would not totalize omitted correction,
orbit/pole, moving-center, dead-stretch, deck/torsion, or other boundary
variables; supply a complete total-Rees chart; or prove whole fixed A3, TD6,
SP-2, or JC2.
