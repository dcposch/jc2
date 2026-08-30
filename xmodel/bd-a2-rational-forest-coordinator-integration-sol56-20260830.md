# Coordinator integration: rational-forest first-leg obstruction

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`  
Lifecycle: **BINDING INTEGRATION / PRESENTATION-SCOPED QUADRATIC CONSEQUENCE**

## 0. Disposition

Opus 5 returned `CONFIRM_WITH_CORRECTIONS` on the sealed producer

```text
367d8ffa1a374b25ee27ca2a2079721c6b17bd71980a13687b11aa87e86f2986
  xmodel/bd-a2-firstleg-rational-forest-multisection-producer-sol56-20260830.md
```

through a sandbox-attested raw review body

```text
40841431c554c63cedb13bda8f662e2633d97695ee8f5d91659479169e2d13e5
  xmodel/bd-a2-rational-forest-multisection-hostile-review-opus5-20260830.md
```

whose sealed full-file SHA-256 is
`24b61d503e5849576093139261d5bc748e2dc7d83ddcc657ac9e4d1d9a004b5f`.
The receipt pins unchanged prompt, adapter, launcher, Seatbelt profile,
validator, fallacy appendix, and model-prompt hashes, with exit code zero.

The review preserves the producer's main theorem and improves the
multisection formula.  This integration adopts the review's repairs: strict
SNC/geometric-genus language, a direct differential-form proof of
`p_g=q=0`, dominant rational rather than only morphic input, open-subset
monotonicity, the exact unibranch equality condition, the projective-coordinate
convention in the sharp control, exact `[X:Y]`-degree three, and the separation
of reduced ramification support from different and discriminant
multiplicities.  The conditional value `barP_1=18` is not promoted.

## 1. Binding rational-forest theorem

Let `U` be a smooth quasi-projective complex surface and `(X,D)` a smooth
projective completion with `D` reduced strict SNC.  Write `Gamma_D` for the
dual multigraph, retaining parallel edges, and put

```text
tau(D)=sum_i g(D_i)+b_1(Gamma_D).
```

Residue, normalization, and Serre duality give

```text
barP_1(U)=p_g(X)+tau(D)-rank(partial),
rank(partial)<=min(tau(D),q(X)).                       (1.1)
```

This includes disconnected boundaries: if `V,E,c` are the numbers of
vertices, edges, and connected components, then
`b_1=E-V+c`.

If there is a dominant rational map `A^2 --> U`, resolve it to a generically
finite morphism.  Pullback injects global one-forms and pluricanonical forms,
so `p_g(X)=q(X)=0`; logarithmic pullback also forces
`bar kappa(U)=-infinity` and hence `barP_1(U)=0`.  Equation (1.1) then gives

```text
g(D_i)=0 for every i,          b_1(Gamma_D)=0.         (1.2)
```

Thus every resolved boundary component is rational and the dual multigraph
is a forest.  The obstruction is monotone under shrinking the target: adding
boundary cannot decrease logarithmic plurigenera.  Consequently any one
boundary subconfiguration with positive geometric genus or a graph cycle
already forbids a dominant rational first leg from `A^2`.

## 2. Exact multisection formula

For a reduced curve `H` on a smooth projective surface, let its irreducible
components have normalization genera `g_i`, let `m_q` be the number of
analytic branches at a singular point, let `s` be the component count, and
let `c` be the connected-component count.  Direct edge/vertex cancellation
in an embedded resolution gives

```text
tau(H_res)
 = sum_i g_i + sum_(q in Sing H)(m_q-1)-s+c.           (2.1)
```

For a `P^1`-bundle over `P^1`, a section `D_infinity`, and an irreducible
multisection `C` of normalization genus `g`, let `r` be the total number of
analytic branches of `C` at its contacts with `D_infinity`.  Then

```text
barP_1(P minus (C union D_infinity))
 = g + max(r-1,0)
   + sum_(q in Sing(C), q notin D_infinity)(m_q-1).    (2.2)
```

Several branches at one point and resolution paths sharing exceptional
vertices do not reduce the right side.  In particular the gate fires if
`g>0`, `r>=2`, or an off-infinity singularity is multibranch.  Equality with
the lower bound `g+max(r-1,0)` requires only that every off-infinity
singularity be unibranch, not smoothness there.

This is sharp.  With the convention `z=Z_1/Z_0`, the complement

```text
(P^1_z x P^1_w) minus ({w=infinity} union closure{z=w^k})
```

is `A^2`, via `(w,t) |-> (w,[t:1+t*w^k])`.  Hence multisection degree alone
cannot obstruct a first leg.

## 3. Miranda-incidence consequence

Consider a fixed global trace-zero Miranda presentation whose homogenized
incidence closure is a smooth irreducible hypersurface

```text
X_d subset P^2 x P^1,          [X_d]=d*A+3*B,          (3.1)
```

with literal degree three in `[X:Y]`.  Adjunction and restriction cohomology
give

```text
K_X=(d-3)A+B,
p_g(X_d)=(d-1)(d-2).                                  (3.2)
```

Therefore every such presentation with `d>=3` is incompatible with a
dominant rational `A^2` first leg.

For `d=2`, `X_2` is rational on the stated smooth irreducible conic-bundle
stratum.  Its infinity curve is generically a smooth irreducible curve of
bidegree `(2,3)` on `P^1 x P^1`, hence has genus two.  Already

```text
barP_1(X_2 minus H_infinity)=2>0,                     (3.3)
```

so every dense open of this generic stratum is excluded.  No ramification
divisor is needed for (3.3).

The stronger generic intersection calculation

```text
R_pi=2A+B,   g(H_infinity)=2,   p_a(R_pi)=9,
H_infinity.R_pi=8,   nominal barP_1=18
```

remains only a conditional diagnostic: it additionally requires that the
reduced ramification support is deleted, smooth and irreducible, has class
`2A+B`, and meets infinity in eight distinct transverse points.  It is not a
binding theorem.

## 4. Exact survivor boundary

The theorem is presentation-scoped.  It does not exclude nonreduced
incidence closure, singular ambient closure, projective basepoints,
extraneous/reducible projective components, degree drop in `(u,v)`, or degree
drop in `[X:Y]`; bidegree `(d,1)` has `p_g=0` even for large `d`.  It also
does not identify arithmetic with geometric genus on a singular component,
or reduced ramification support with the different or target discriminant.

On the remaining reduced quadratic infinity stratum, if `H` has bidegree
`(2,3)`, then `p_a(H)=2`, and its ample support is connected.  Combining the
arithmetic-genus formula with (2.1) gives the finite successor gate

```text
2 = G + B + K,
G=sum component normalization genera,
B=b_1(resolved dual graph),
K=sum_q(delta_q-m_q+1).                                (4.1)
```

Thus a rational-forest resolution is possible exactly when `K=2` (and then
necessarily `G=B=0`).  Classifying the reduced factor-degree partitions and
their distributions of this two-unit non-nodal defect is the cheapest next
step.  Nonreduced and projective-degree-drop strata remain separate.

No general cubic-block theorem, intrinsic bound on presentation degree,
primitivity statement, polynomial-map construction, counterexample, or JC2
claim follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6810`.
- Body SHA-256:
  `9c6501222049980161f209d57e1a575ebe80c4de1b8018aedf303f692e1dae46`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
