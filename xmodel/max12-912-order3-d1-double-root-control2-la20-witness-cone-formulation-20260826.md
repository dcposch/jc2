# D1 control-2 witness cone and exceptional faces

Status: **symbolic formulation; finite support pending the registered AWS V2
certificate**.

## Fixed-source witness lemma

Let

```text
x = (la,tau,rho,q1,q0,r2,r1,r0)
```

and let `J` be the dehomogenized (`s=1`) ideal of the pinned nine-generator
control-2 Rees system over `Q`. Suppose an exact checked preimage produces

```text
W(x) = A*la^20 + sum_{e in S} B_e*x^e in J,
```

where `A` is nonzero and `S` is finite. For any weight vector `w` satisfying

```text
e dot w > 20*w_la                 for every e in S with B_e != 0,
```

the least-weight initial form of `W` is `A*la^20`. Consequently
`la^20` belongs to `in_w(J)`. On the torus where all eight coordinates are
nonzero, `la` is a unit, so the torus saturation of `in_w(J)` is the unit
ideal. There is no torus-valued leading coefficient for that fixed source and
weight.

This is a direct one-polynomial argument: it does not require the full
initial ideal to stay constant. Thus the half-space intersection should be
called the **witness obstruction region**, not a full Gröbner cone.

For the registered control, the charged point is

```text
w0 = (4,1,1,22,22,30,30,30),       20*w0_la = 80.
```

The global-`dp` V2 job must enumerate every nonzero term of `W`, check that
`la^20` is the unique term of weight 80, and check that every other term has
weight greater than 80. Its output then supplies the finite defining
inequalities of the obstruction region containing `w0`.

## Coefficient and parameter version

For a moving source parameter `theta`, the safe form of a parametric
certificate is

```text
D(theta)*W(theta,x)
  = A(theta)*la^20 + sum_e B_e(theta)*x^e in J_theta,
```

with every denominator charged into `D`. The witness obstruction persists on
the parameter open set

```text
D(theta)*A(theta) != 0
```

and on the same strict weight inequalities for every exponent whose
coefficient is nonzero at that parameter. Vanishing of a non-target `B_e`
only removes an inequality and is harmless. Vanishing of `A`, a pole of the
certificate, or a change in the charged source ideal is exceptional and must
be recomputed; it cannot be crossed by continuity rhetoric.

The current V2 jobs are only over the pinned rational point

```text
a=1, h=q2=k=nu=0, mu=2/3.
```

They do not provide such a parametric certificate.

## Exceptional weight faces

For an exponent `e` in the witness support, a boundary wall is

```text
H_e: e dot w = 20*w_la.
```

On a face `F`, the witness initial form is

```text
A*la^20 + sum_{e in F} B_e*x^e.
```

A non-monomial initial form generally has torus zeros, so the interior
monomial argument does not settle the face. Each inclusion-minimal face must
instead be tested using the full face initial ideal and torus saturation. A
face is excluded only if that saturation is exactly `(1)` (or by another
explicit monomial/preimage certificate). Face results do not automatically
propagate to adjacent cancellation walls.

## Smallest proof-producing successor on AWS

Once V2 closes, use its frozen term list, not a reconstructed witness, to:

1. normalize each inequality to a primitive integer normal;
2. remove duplicates and test redundancy by exact rational linear
   programming;
3. enumerate inclusion-minimal boundary faces meeting the positive valuation
   orthant (optionally in the slice `w_la=4`);
4. for each surviving face, compile the full face initial ideal directly from
   the nine frozen generators and test eight-coordinate torus saturation;
5. retain the exact witness identity, support SHA, facet list, and per-face
   unit/nonunit certificate.

All polyhedral and ideal computations in this successor are AWS-only. A
finite list is complete only relative to the explicit witness support. It is
not a completeness theorem for the whole double-root Newton fan, because a
different source/support or a cancellation wall not represented in this
fixed system can introduce other initial equations.

## Firewall

Even a successful V2 witness and all-face audit excludes only an open region
and its audited faces for the exact fixed axis, fixed loads, support, and
charged equations above. It does not cover moving axis, nonzero `q2`, moving
`k,mu,nu`, all double-root directions, D1 globally, or JC2.
