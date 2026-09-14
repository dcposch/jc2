# Bounded independent gate: polynomial graph restriction

Date: 2026-09-06 UTC  
Reviewer: root/sol56  
Disposition scope: the three displayed polynomials, standard graphs
`z=H(x,y)`, and constant `2x3` output matrices only.

## Review target

Let `k` be a characteristic-zero field and set

```text
P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
R=2x-3x^2y-x^3z.
```

For `H in k[x,y]`, write `P_H=P(x,y,H)`, and similarly for `Q_H,R_H`.
The claim under review is that for every constant matrix `M in Mat_(2x3)(k)`,
the two components of `M(P_H,Q_H,R_H)^t` have Jacobian either zero or a
nonconstant polynomial. The claim is not an assertion about arbitrary maps
from three dimensions to two dimensions.

The complete sealed Astra report and the two other charged inputs were read.
Their local SHA-256 values are
`1ab4e6791e6a38fd9a8313161a546554a57efcf5207bc32d42dfa4b492dd8e21`
for the report and
`ff07e2d6915b21fd6ea9a112b01e63f897859d3781faed2c7490aeb128c354bc`
for the checker, matching the supplied values. No external attribution,
three-dimensional counterexample, or novelty premise is used below.

## Claim 1 — highest forms and minor degrees: CONFIRMED

Expanding only what is needed for total degree gives

```text
P_H=(1+3xy+3x^2y^2+x^3y^3)H+4y^2+7xy^3+3x^2y^4,
Q_H=y+(3x+6x^2y+3x^3y^2)H+12xy^2+9x^2y^3,
R_H=2x-3x^2y-x^3H.
```

The degree tie at `d=0` has to be handled rather than hidden in the
nonconstant argument.

* If `H` is nonconstant of degree `d>=1`, let `h` be its nonzero homogeneous
  degree-`d` part and put `T=x^3h`. The `H`-dependent terms have degrees
  `d+6,d+5,d+3`, strictly above the respective `H`-free degrees `6,5,3`.
  Thus the three highest forms are

  ```text
  p=x^3y^3h=y^3T,  q=3x^3y^2h=3y^2T,  r=-x^3h=-T.
  ```

* If `H=c` is a nonzero constant, the tied contributions combine. With
  `T_c=x^2(cx+3y)`, the highest forms are

  ```text
  p=cx^3y^3+3x^2y^4=y^3T_c,
  q=3cx^3y^2+9x^2y^3=3y^2T_c,
  r=-cx^3-3x^2y=-T_c.
  ```

* If `H=0`, considered separately because its ordinary degree is undefined,
  put `T_0=3x^2y`. Directly,

  ```text
  p=3x^2y^4=y^3T_0,
  q=9x^2y^3=3y^2T_0,
  r=-3x^2y=-T_0.
  ```

Adopt `d=0` in the last two cases and write their `T` as `T_c` or `T_0`.
In every case `T` is nonzero homogeneous of degree `d+3`. For nonconstant
`H`, write `h=sum a_(ij)x^iy^j`. Then

```text
T_x=sum (i+3)a_(ij)x^(i+2)y^j.
```

Distinct monomials stay distinct, and every integer `i+3` is nonzero in a
characteristic-zero field, so `T_x` cannot vanish. For nonzero constant `c`,
`(T_c)_x=3cx^2+6xy`; for `H=0`, `(T_0)_x=6xy`. These are also nonzero.

For `J(f,g)=f_xg_y-f_yg_x`, direct differentiation of the three highest
forms gives

```text
J(p,q)=-3y^4 T T_x,
J(p,r)= 3y^2 T T_x,
J(q,r)= 6y   T T_x.
```

All three are nonzero because `k[x,y]` is a domain. If polynomials have
highest forms of degrees `m,n`, the homogeneous degree-`m+n-2` part of their
Jacobian is the Jacobian of those highest forms; every term involving a lower
form has smaller degree. Consequently these displayed nonzero expressions
are the actual leading forms of the restricted minors, and

```text
deg J(P_H,Q_H)=2d+9,
deg J(P_H,R_H)=2d+7,
deg J(Q_H,R_H)=2d+6.
```

This includes the exact degree triple `(9,7,6)` for both `H=0` and every
nonzero constant `H`.

## Claim 2 — every constant `2x3` matrix: CONFIRMED

Let the rows of `M` be `a=(a_1,a_2,a_3)` and `b=(b_1,b_2,b_3)`, and let
`F=(P_H,Q_H,R_H)`. Bilinearity and alternation of the Jacobian, equivalently
the `2x3` Cauchy--Binet identity, give

```text
J(a.F,b.F)=Delta_12 J(P_H,Q_H)
          +Delta_13 J(P_H,R_H)
          +Delta_23 J(Q_H,R_H),
Delta_ij=a_i b_j-a_j b_i.
```

If `rank(M)<2`, all three `Delta_ij` vanish and the Jacobian is zero. If
`rank(M)=2`, at least one is nonzero. Cancellation was checked in descending
degree, not inferred from a generic matrix:

* if `Delta_12` is nonzero, the sum has degree `2d+9`;
* otherwise, if `Delta_13` is nonzero, it has degree `2d+7`;
* otherwise `Delta_23` is nonzero and it has degree `2d+6`.

At each step the selected leading form has a nonzero scalar coefficient and
the remaining minors have strictly smaller degree, so they cannot cancel it.
All three possible degrees are positive. Hence every rank-two matrix gives a
nonconstant Jacobian, while every lower-rank matrix gives zero. This proves
the reviewed universal claim for all matrices, rather than for sampled
projections. Constant output translations, if added, do not change the
derivatives.

## Claim 3 — polynomial-automorphism precomposition: CONFIRMED, narrowly

Let `alpha=(alpha_1,alpha_2)` be a polynomial automorphism of the parameter
plane and let `G=M F`. The chain rule says

```text
J(G_1 after alpha,G_2 after alpha)
  =(J(G_1,G_2) after alpha) J(alpha_1,alpha_2).
```

If `beta` is the polynomial inverse of `alpha`, applying the chain rule to
`beta after alpha=id` shows that `J(alpha_1,alpha_2)` is a unit of `k[x,y]`,
hence a nonzero element of `k`. This uses the given inverse; it invokes no
converse Jacobian assertion. Substitution by `alpha` is a ring automorphism,
so it sends zero to zero and reflects constants: if a polynomial becomes
constant after substitution, applying substitution by `beta` shows it was
already constant. The zero/nonconstant alternative therefore survives this
precomposition.

This is only a change of parameters of the full graph map
`(x,y) -> (x,y,H(x,y))`. It does not cover a noninvertible parameter map, a
general embedded plane, a different graph orientation, an ambient nonlinear
three-dimensional map, or a nonlinear map of the three outputs.

## Claim 4 — boundary counter-controls: CONFIRMED

For the other orientation `x=0`, parametrized by `(y,z)`, the restrictions are

```text
(P,Q,R)=(z+4y^2,y,0).
```

Selecting `(P,Q)` and using the same convention `J(P,Q)=P_yQ_z-P_zQ_y`
gives `-1`. Thus an alternate plane orientation really can have nonzero
constant Jacobian. It is a direct counter-control to any attempted extension
from standard polynomial `z`-graphs to all embedded or differently oriented
planes; it does not contradict the reviewed claim.

The rational substitution `H=-3y/x` is also outside the proof. It belongs to
the localization `k[x,y,x^(-1)]`, not to `k[x,y]`, and it already erases the
combination controlling the cubic part of `R`:

```text
x^3H+3x^2y=0.
```

Accordingly there is no polynomial highest homogeneous part `h` to which the
degree argument above applies, and restriction need not even leave all three
components in `k[x,y]`. This observation establishes only the necessity of
the polynomial-domain hypothesis for this proof; it supplies neither a
rational-graph theorem nor a counterexample.

## Bounded executable controls

The charged checker was read in full before execution. Each invocation was
wrapped in a 30-second timeout; the checker itself fixes a 512 MiB address-space
limit and a 25-second CPU limit.

```text
timeout 30s python3 box/alpoge-polynomial-graph-20260906/check.py
timeout 30s python3 -O box/alpoge-polynomial-graph-20260906/check.py
timeout 30s python3 box/alpoge-polynomial-graph-20260906/check.py --mutate
timeout 30s python3 -O box/alpoge-polynomial-graph-20260906/check.py --mutate
```

The normal and optimized positive runs both exited `0` with
`GRAPH_LEADING_CONTROLS_PASS`. The normal and optimized mutation runs both
exited `1` at `CHECK_FAILED: graph-chain minor leading forms`. Every run took
less than 2.4 seconds. The checker also rejects Python `assert` statements by
AST inspection, so optimization did not remove its required checks.

The mutation is substantive. The correct graph derivatives are

```text
(P_H)_x=(P_x)|_(z=H)+(P_z)|_(z=H) H_x,
(P_H)_y=(P_y)|_(z=H)+(P_z)|_(z=H) H_y,
```

and likewise for `Q`. The mutation instead forms the ambient `(x,y)` minor
`J(P,Q)` while holding `z` independent and only then substitutes `z=H`.
Thus it suppresses both graph-chain derivative directions, rather than merely
changing formatting or an expected literal.

As an independent tiny check, a separate standard-library sparse-polynomial
implementation over exact rational coefficients was run without importing
the charged checker or SymPy. It independently expanded `H=0`, `H=2`,
`H=-2x+3y+1`, and `H=x^2+y`; checked the three output leaders, all three
minor leaders and degree triples; verified the Cauchy--Binet identity and
noncancellation for four rank-two matrices covering each possible highest
surviving minor; checked a rank-one zero case; and recomputed the `x=0`
Jacobian as `-1`. It returned `INDEPENDENT_SPARSE_ARITHMETIC_PASS` in under
0.1 seconds under the same 30-second/512 MiB envelope. Its first invocation
stopped before evaluating a claim because a scratch multiplication helper had
the wrong arity; correcting that harness-only typo produced the stated pass.

## Verdicts

| Claim | Status | Decisive point |
|---|---|---|
| Three restricted highest forms, including nonzero-constant and zero cases | CONFIRMED | The tied degree-six/five/three terms combine into the stated nonzero `T`. |
| Nonvanishing of `T_x` in characteristic zero and minor degrees `(2d+9,2d+7,2d+6)` | CONFIRMED | Monomial coefficients `i+3` cannot vanish, and the three computed leading minors are nonzero. |
| Every constant rank-two `2x3` output matrix gives a nonconstant Jacobian | CONFIRMED | Cauchy--Binet plus strictly distinct positive degrees prevents cancellation for every nonzero Pluecker coordinate pattern. |
| Every lower-rank constant `2x3` output matrix gives zero Jacobian | CONFIRMED | All `2x2` minors of the matrix vanish. |
| Invariance under polynomial-automorphism reparametrization of the same graph | CONFIRMED | Pullback is a ring automorphism and its Jacobian factor is a nonzero constant. |
| `x=0` orientation counter-control and exclusion of rational `H` from this proof | CONFIRMED | The former has Jacobian `-1`; the latter leaves the polynomial ring and can erase the leader. |
| Overall bounded elementary graph-restriction claim | CONFIRMED | No cancellation, characteristic, chain-rule, or scope gap remains within the stated hypotheses. |

There is no `REFUTED` or `GAP` item. This verdict makes no claim about
nonlinear three-output maps, general embedded planes, alternate orientations,
rational graphs, arbitrary maps from three dimensions to two, or novelty.

<!-- BODY-END -->
