# TD6 V89 low-q shared radical/Macaulay design

Date: 2026-08-26

Status: **withdrawn as a current reduction after the V89H1 denominator gate;
retained only as a conditional design after the extra factor below is
removed or covered. No radical membership is claimed.**

## Denominator correction: V89H1 does not currently supply the reduction

Work over the registered localization

```text
R = Q[C,V,U,q2,...,q14,q16,...,q24,section]_(U H B3),
J = (literal raw P12, 38 literal packed raw FIRST maps, F),
QL = (q2,...,q14).
```

The reviewed V87 augmentation identity gives

```text
1 in J + (q2,...,q14,q16,...,q24).
```

V89H1 did verify the algebraic source replay on the low-q-zero residue block,
with arbitrary independent `q16,...,q24`, and reduced literal P12 to its
q-zero remainder. Its final denominator gate then failed. The audited common
denominator factors as an allowed scalar times

```text
K * B3 * U^2 * H^2,
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6.
```

`K` is not in the registered `U,H,B3` denominator set. Thus H1 gives, at
most, the conditional statement

```text
1 in (J + QL) localized further at K.             (A_K)
```

It does **not** currently give `1 in J+QL` on `D(U H B3)`. Every descendant
that used that unlocalized statement, including the proposed global radical
shortcut below, is withdrawn until one of these exact repairs lands:

1. identify K as an already licensed source-chart unit with exact custody;
2. prove K is a unit modulo the literal low-q-zero source ideal;
3. cover the closed K=0 stratum independently;
4. find an alternate registered pivot/certificate with no K denominator.

H1 is also not the statement that a high q jet is a source coordinate in the
full ring with arbitrary low q.

## Conditional radical reduction after a K repair

Only after a repair upgrades `(A_K)` to

```text
1 in J + QL                                          (A)
```

on the original registered open is it enough to prove

```text
QL subset radical(J).                               (B)
```

Indeed (A) and (B) imply `1 in radical(J)`. This would empty the retained
fixed source slice without opening thirteen unit-q charts. It would still
say nothing about the omitted geometric source variables listed below.

## Gate 1, conditional: freeze an explicit lift of (A)

Do not cite a quotient slogan. Lift the H1 identity back to the full V87 q
ring as follows.

1. Consume only a repaired H1 certificate whose denominator audit has removed
   K or an exact theorem proving K is a unit modulo the same literal ideal.
2. Apply those same multipliers to the literal all-q V87 P12/FIRST sources.
3. Verify that the residual specializes to zero at `q2=...=q14=0`.
4. Partition every residual q monomial by its first low-q factor, producing
   exact `g_e` with

   ```text
   1 = aP*P12 + sum_i ai*FIRST_i + F*h + sum_{e=2}^{14} q_e*g_e.
   ```

5. Replay the identity coefficientwise, with separate omission controls for
   P12, one active FIRST source, F if active, and each nonzero low-q
   partition. Audit the common denominator and reject any factor outside
   `U,H,B3`; reject every inverse of F or a q expression.

The failed H1 multipliers may be used as support-discovery hints, but not as
coefficient identities on the original open. This bridge becomes valid only
after its own exact denominator audit rejects K and every other unregistered
factor.

## Gate 2: coordinate-nilpotence certificates

For every `e=2,...,14`, seek a bounded exact identity

```text
(U H B3)^M * q_e^N
  = aP*P12 + sum_i ai*FIRST_i + F*h              (C_e)
```

in the literal all-q ring before localization. The exponents `M,N`, every
multiplier support, and every source path are part of the output. A complete
set of thirteen identities proves (B). One missing coordinate leaves the
global radical shortcut open.

Equivalent Rabinowitsch tests

```text
1 in J + (1-y*q_e)
```

may be used to discover `(C_e)`, but the accepted artifact must be translated
back to an ordinary power certificate and replayed in the literal source
ring. Neither a tangent calculation nor a reduced-P12 relation is accepted.

## One shared sparse Macaulay solve

The 39 literal source polynomials and F are compiled once. Use the union of
the following multiplier supports as the first bounded search space:

- failed H1 original-source multiplier supports, for discovery only;
- the thirteen low-q augmentation quotients from Gate 1;
- the reviewed V87 `h_e` supports for `e=2,...,14`;
- one and then two border expansions by parameter monomials appearing in the
  literal sources;
- q monomials by increasing total degree, with the high q variables retained
  independently rather than sampled away.

Assemble one sparse coefficient matrix with thirteen target columns
`q_e^N`. Reuse its symbolic sparsity ordering and fraction-free elimination
for all targets. Modular AWS scouts may select pivots and support bounds at
several good primes and legal base specializations, but they are diagnostics
only. Every producer certificate is reconstructed over the exact E3
coefficient field, replayed against literal P12/FIRST/F, and then cleared by
an audited common power of `U H B3`.

Record ranks and failure residues for every attempted `(M,N,support)`.
Failure of a bounded Macaulay solve is not nonmembership and is not evidence
for a source point.

## Fitting fallback and mixed obstruction routing

In parallel, use the reviewed q-zero 38-pivot block to form the full affine-q
matrix

```text
B(q)=A0^(-1) A(q).
```

Do not invert `det B(q)`. Fraction-free elimination may emit determinantal
strata and corresponding P12 consistency numerators. Each stratum must carry
its defining minor, an exact cover/radical proof, and a literal-source replay.
This shared Fitting atlas is the fallback if direct coordinate powers are too
large.

The tail clients are a cheap front end to the same search. After H1, add
`q14`, then lower jets, always retaining all later q variables. An acyclic
support graph and q-independent unit remainder proves the corresponding tail
empty without a unit chart. The first directed cycle is only failure of the
triangular inverse; the first positive P12 remainder is a genuine mixed
integrability obstruction and should seed the next Macaulay support. Neither
is a radical nonmembership theorem.

## Exact output and stopping rule

An accepted global radical package must contain:

- the frozen Gate-1 identity and all thirteen low-q quotients;
- thirteen ordinary coordinate-power identities `(C_e)` or one equivalent
  ideal/radical certificate implying all of them;
- exact powers and denominator factors;
- complete multiplier/source inventories and coefficientwise replays;
- P12, FIRST, F, target-coordinate, and denominator omission controls;
- specialization back to H1 at `QL=0` and to reviewed V86 on the q2 axis;
- dual exact AWS custody and an independent hostile review.

Stop fail-closed unless the emitted identities prove `QL subset radical(J)`
in the literal ring on `D(U H B3)`. Numerical ranks, finite-field membership
alone, a generic determinant, or thirteen named principal opens are not a
cover theorem.

## Scope firewall

Even a complete package concerns only the retained normalized three-center,
fixed F1/pole/dead-stretch source family, with q15 transported separately by
the reviewed target shear. It does not totalize correction, orbit/pole,
moving-center, dead-stretch, deck/torsion, other boundary moduli, or total
Rees, and proves no whole fixed-A3, TD6, SP-2, or JC2 statement.
