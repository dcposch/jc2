# Preregistration: K00 first-order load-deformation cokernel V17

Date: 2026-08-27

Status: **FROZEN BEFORE ALGEBRA; ALL THREE LOAD OUTCOMES OPEN.**

## Invariant question

Work at the normalized K00 point `C6=1` in

```text
R=Q[d0,d1,d2,d3,d4,d5],  m=(d0,...,d5).
```

Let `r_i` be the seven unloaded rows, `I=(r1,...,r6)`, and let
`a_i^X` be the exact coefficient of the affine load `X` in row `i`, for

```text
X in {k10,k6,k2}.
```

These are the coefficients *before* the honest one-parameter factors
`Lambda^2,Lambda^6,Lambda^10` are restored.  Consume the exact V14R1
local relation

```text
h*r7 = sum_{i=1}^6 u_i*r_i,   h(0)!=0.
```

For each `X`, define

```text
D_X = h*a_7^X - sum_i u_i*a_i^X,
T   = Syz_R(r1,...,r6),
E_X = ( sum_i s_i*a_i^X : s in a full generating set of T ),
Q_X = R/(I+E_X).
```

The first-order obstruction is the class of `D_X/h` in `(Q_X)_m`.
Because `h` is a unit, it vanishes exactly when

```text
D_X in (I+E_X)_m.
```

The producer must decide this local-membership question independently for
all three loads and accept either answer for each.  A zero target, local
membership, and local nonmembership are all legitimate endpoints.

## Representation independence

If `q0=u/h` is changed by `s in Syz(I)_m`, then the residual changes by
`-sum_i s_i*a_i^X`, which is killed in `Q_X`.  The producer must compute
the full `Syz(I)`, replay every generator, and form `E_X` from every
generator—not from a chosen relation or only its constants.

It must also consume and replay the complete frozen 87-generator module
`S=Syz(r1,...,r7)`.  For every `v in S`, put

```text
D_X(v)=v7*a_7^X + sum_i v_i*a_i^X.
```

The exact cross-relation

```text
h*D_X(v) - v7*D_X in E_X
```

must replay for all 87 generators and all three loads.  This checks the
signs and makes invariance under changing the unit relation explicit.

## Local semantics and custody

Local membership is decided by

```text
C_X=(I+E_X):D_X,
D_X in (I+E_X)_m  iff  C_X is not contained in m.
```

The exact-Q lane must serialize the full six-row syzygy module, every image
ideal, every target, every quotient/colon ideal and standard basis, branch
markers, and any unit witness/lift that exists.  It must independently
re-emit the load coefficients from the frozen 569-tail source, verify the
unloaded rows byte-algebraically against the V14R1 prelude, and fail closed
on diagnostics, source drift, or a failed identity.  `p=65521` is only a
software control.

## Both-outcome scope

This V17 calculation is one deformation parameter at a time in the
coefficient-local ring.  It does not yet couple the three directions,
restore their `Lambda` weights, include the `mu2,mu4,mu6,Jdet` targets,
compute jets through `Lambda^19`, restrict to the honest source image, or
decide the closure-first K00 incidence.  Either outcome is therefore a
finite navigation theorem, not order two, maximum twelve, or JC2.

