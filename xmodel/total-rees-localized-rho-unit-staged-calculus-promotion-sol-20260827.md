# Promotion: localized rho-unit certificates for staged Rees-chart emptiness

Date: 2026-08-27

Status: **PROMOTED ELEMENTARY INTERFACE THEOREM.**  This promotes the repaired
certificate calculus, not any unreviewed chart and not a global landing
claim.

## Evidence

```text
43adf31727136c68c3f2ce1f8465517382262d0d5e04493a00bf49d101bac4b9
  xmodel/ideation-20260826T2350Z-opus5.md

db160c13351bab3a238582601e9a4f444ff98319524722176afb4ef047c54b00
  xmodel/ideation-20260826T2350Z-rho-unit-hostile-review-fable5.md
```

Fable 5's different-model review gives verdict `REPAIRABLE`: Opus 5's core
lemma and its three obligation removals are exact, while the certificate type
and the claimed literal `T-rs` instantiation require the repairs incorporated
below.

## Theorem

Let `A=R/Q` be a commutative source ring, let `rho in R`, and let
`I=(f_0,...,f_n) in A`.  The `i`th standard chart of
`Proj(Rees_A(I))` has the exact presentation

```text
A[y_j:j!=i] / ((f_i*y_j-f_j:j!=i):f_i^infinity).       (1)
```

This remains true when `f_i` is a zero divisor.  Suppose that, after adding
honest ordered-stratum generators `z_e`, there is a polynomial identity

```text
f_i^N * s * (1+rho*W)
  = sum_j H_j*(f_i*y_j-f_j) + sum_m G_m*q_m + sum_e L_e*z_e,  (2)
```

where the `q_m` lift the literal total source relations, `s` is a registered
genuine localizer, and no factor of `rho` is inverted.  Then the `rho=0`
fibre of that stratum of the `i`th chart is contained in `V(s)`.  If `s` is
already a unit on the registered source open, that chart stratum has empty
`rho=0` fibre.

The three roles in (2) are distinct and must be stored separately:

```text
f_i^N    exceptional-chart power, absorbed freely by saturation;
s        genuine localizer, producing the residual closed stratum V(s);
z_e      ordered-stratum equations, with source provenance required.
```

Indeed (2), (1), and localization at `s` give `1 in (rho)` in the chart
ring.  Conversely, chart-fibre emptiness has a homogeneous power-containment
form after clearing a finite saturation exponent.  Standard Rees charts
cover `Proj`, and their least-index ordered strata cover set-theoretically;
therefore chartwise emptiness needs neither pairwise overlap isomorphisms nor
scheme-theoretic gluing data.

For a DVR arc with `I R' != 0`, the pulled ideal is invertible, so the
universal property gives a unique lift to the blowup.  Its closed point would
lie in the empty `rho` fibre when `ord(rho)>0`, a contradiction.

## Exact obligation change

For the **emptiness / DVR-arc-exclusion endpoint only**, a direct identity
(2) removes the need for:

1. equality between the total chart's special fibre and a chart recomputed
   after specialization;
2. pairwise overlap/gluing calculations among the standard charts;
3. separate nilpotent or embedded-component analysis of that special fibre.

It does not remove:

- literal total-source and stratum-generator provenance;
- the chart certificates themselves;
- every residual `V(s)` localizer stratum;
- the generic deck/square comparison;
- the terminal zero receiver;
- any effective bound on the decisive source grade.

A specialized unit remains only a screen.  In general the specialized Rees
chart is a closed subscheme of the total special fibre; the converse
emptiness implication fails because of Rees base-change torsion.

## Staged `J1` / `J2` form

For the campaign's ordered collision geometry, apply the theorem separately
to

```text
J1=(rs,cs,c0,c1) over A,
J2=(a0,a1) over A/J1.
```

The six certificates form a staged tree: four `J1` charts, two `J2` charts
on `V(J1)`, and the separate terminal receiver `V(J1+J2)`.  The single ideal
`(rs,cs,c0,c1,a0,a1)` proposed in the root blind report instead defines the
uncharged blowup of `J1+J2`; existing `J1` certificates do not automatically
re-embed there.  That proposal is withdrawn and replaced by the staged tree.

Per-stage homogeneous power containments may be accumulated with the usual
pigeonhole exponent.  They must retain the `s` localizer decoration; a
single unqualified irrelevant-ideal containment is not the certificate type.

## Repaired `T-rs` instantiation

The promoted `T-rs` identity is not literally Opus's original bilinear-only
lemma.  It is an instance of (2) in the presented source chart: its relation
list contains four divided raw source rows, its exceptional power is `rs^4`
after returning to the presentation, and its genuine localizer is `35*k`.
The review independently checks the specialization sign, constant, and
`rho^2` sentinel.  Thus the existing `T-rs` promotion is unchanged on `D(k)`;
the only retained debt is its already recorded upstream total-emitter row
provenance.

## Scope firewall

This is an elementary interface theorem and a correction of the landing
obligation graph.  It does not promote `T-cs`, `T-c0`, `T-c1`, either
second-stage `A` chart, the terminal receiver, `k=0`, the deck/square bridge,
order two, maximum twelve, a global complexity ceiling, or JC2.
