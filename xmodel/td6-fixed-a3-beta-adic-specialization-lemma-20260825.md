# TD6 fixed-A3 beta-adic specialization lemma

Status: **exact formal consequence, conditional only on the frozen
fixed-A3 producer theorem at its stated source scope; union review remains
charged.**  This note performs no new CAS computation.

## Setup

Let `E` be the frozen degree-18 coefficient field.  Let `X -> A^1_beta` be
the affine finite-type scheme defined by the original transported TD6
necessary equations in the same source-typed normalized presentation as the
fixed three-center atlas:

```text
y=s^-1,
x=C s+V s^2+U s^3+t s^4,
p=t^15,
q=t+beta*t^2+t^25,
```

with the frozen F1 orbit, pole data/scale, zero dead stretch, and every
transport/free coefficient retained as an affine coordinate.  No quotient-
field pivot chart is part of the definition of `X`; those charts are only
certificates about its special fibre.

The producer-exact fixed-A3 union says that the geometric special fibre

```text
X_0 = X x_{E[beta]} E
```

has no point over any extension of `E`.  Equivalently at set-theoretic scope,
`X_0` is empty.  The fixed union is frozen at
`cases/td6_c1_c2_c3_b3_raw_divisor_aws_20260825/`, manifest SHA-256
`86102e8c906436afcf6a2397fb8b0ea736ee7acdbae3232c330ec10c536e2b70`;
hostile review of the cross-package union is still pending.

## Lemma

Let `R` be a valuation ring over `E` with residue field `k`, and let the image
of `beta` lie in the maximal ideal of `R`.  Then `X(R)` is empty.

Indeed, an `R`-point of the affine presentation reduces modulo the maximal
ideal to a `k`-point of `X_0`, contradicting the fixed-A3 theorem.  The same
argument applies to `R=K[[beta]]`, to a ramified DVR with positive valuation
of `beta`, and to any valuation-ring extension whose residue field extends
`E`.

Consequently, a `K((beta))`-valued survivor in this exact deformed source
presentation cannot have every affine source/transport coordinate integral.
At least one coordinate has negative valuation, or the family fails to
extend in this normalized affine chart.  In that precise sense, every
transverse survivor must escape to the boundary of a source-licensed
compactification.

## What this does and does not license

This specialization argument does **not** require a displayed global
Nullstellensatz combination assembled from the localized fixed-fibre
certificates.  It does require that the beta family and its reduction use one
common original-row affine source presentation.  If a normalization,
localizer, orbit quotient, or target gauge degenerates at `beta=0`, it must be
added as a separate boundary chart rather than silently treated as an
integral point.

The conclusion is not:

- a finite-beta neighborhood theorem in the complex topology;
- a classification or finite list of negative valuations;
- emptiness of the generic beta fibre;
- a four-parameter, whole-TD6, SP-2, landing, or JC2 theorem.

It only removes bounded affine formal branches in the common normalized
model.  A model such as `beta*z-1=0` has empty special fibre and a generic
solution `z=beta^-1`; this is the exact escape phenomenon still charged.

## Consequence for the live dual adjoint

The AWS dual-number replay over `D(U*H*B3)` remains valuable as a source-
typing and differentiated-certificate regression: it must retain the direct
`q'` variation, changing transport section, full `lambda'` terms, original
rows, and denominator divisors.  But a remainder
`-k/50 + epsilon*r` is automatically a unit in the dual ring because
`-k/50` is a unit.  Thus the dual calculation alone cannot decide generic
finite-beta existence or classify escape.

The next decisive exact computation is therefore:

1. audit a common original-row beta presentation and every normalization/
   localizer boundary;
2. derive the finite support-based valuation constraints with
   `ord(beta)>0` and at least one negative affine-coordinate valuation;
3. compute saturated initial ideals only on feasible cones; and
4. freeze either an exhaustive empty boundary atlas or the first exact
   source-reconstructible escape component.

All substantive valuation/initial-ideal computation belongs on AWS.  No
claim should use a tropical prevariety without exact saturation and an
exhaustive source-derived fan.
