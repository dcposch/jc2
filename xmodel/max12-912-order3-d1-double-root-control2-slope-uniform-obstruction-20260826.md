# Slope-uniform obstruction for the strict D1 control-2 interval

Status: **exact consequence of the frozen witness and literal AWS replay;
focused hostile mapping/firewall review pending**.

## Theorem

Fix

```text
K=(z-1)^2(z+2),
a=1, h=q2=k=nu=0, mu=2/3,
Q=q1*z+q0,
R=r2*z^2+r1*z+r0,
Lambda=tau^3*rho,
```

and let `J` be the exact eight-row finite coefficient ideal together with
`Lambda-tau^3*rho`, as charged in the control-2 Rees package. Let `L>0`,
`T>0`, `H>0`, and `beta` be rational, with

```text
L=3*T+H,
w(Lambda,tau,rho)=(L,T,H),
w(q1)=w(q0)=beta*L,
w(r2)=w(r1)=w(r0)=(15/2)*L.
```

If `beta>5`, then the least-weight initial ideal `in_w(J)` contains
`Lambda^20`. Hence it has no point with `Lambda` nonzero, in particular no
point in the eight-coordinate leading-coefficient torus.

Consequently the entire strict correction-control interval

```text
alpha=15/2,       5<beta<6
```

is excluded at once for this fixed cubic, fixed loads, and displayed
five-coefficient support. This includes, but is not limited to, the sampled
ramification

```text
(L,T,H; beta*L; alpha*L)=(4,1,1;22;30).
```

The conclusion is uniform in the nonzero leading residue and in the positive
split `(T,H)` subject to `L=3T+H`.

## Proof

The frozen LPDP certificate and its literal r6d replay prove that `J`
contains

```text
W = Lambda^20*tau + Lambda^20
  + (1/243)*q1*q0^3
  + (1/54)*q1*r2*r1
  + (7/108)*q1*r1^2
  + (1/54)*q1*r2*r0
  - (1/54)*q0*r1*r0
  + (1/108)*q1*r0^2.
```

At the displayed general control-2 weights, the term weights are

```text
20*L+T                         (Lambda^20*tau),
20*L                           (Lambda^20),
4*beta*L                       (q1*q0^3),
(beta+15)*L                    (each of the five q*r*r terms).
```

Since `L,T>0`, both non-target classes are strictly above `20L` exactly when

```text
beta>5.
```

Thus `in_w(W)=Lambda^20` up to its nonzero scalar, so
`Lambda^20 in in_w(J)`. If `Lambda` is invertible, this monomial is a unit and
the localized initial ideal is `(1)`. The proof never substitutes a particular
residue, hence it kills the whole leading-coefficient torus at each such
weight.

## Why the family substitution is licensed

The Rees computation was performed at one integral weight only to discover a
preimage. After setting `s=1`, the checked polynomial `W` belongs to the exact
unhomogenized finite ideal `J`; its membership no longer depends on the
discovery weight. Therefore it may be reweighted by any `w` on the same fixed
polynomial ideal. No continuity of a Gröbner basis is invoked: the argument
uses only the explicit finite support of `W`.

The relation `Lambda=tau^3*rho` imposes `L=3T+H` on a torus-valued leading
term. Positivity gives `T>0`, which is the first witness inequality. The six
remaining witness inequalities collapse to either `4 beta L>20L` or
`(beta+15)L>20L`, both equivalent to `beta>5`.

## Boundary and scope firewall

At `beta=5`, seven terms reach weight `20L`: `Lambda^20` together with
`q1*q0^3` and the five `q*r*r` terms. The witness is nonmonomial there, so the
boundary requires the full face initial ideal and torus saturation. This file
makes no boundary claim.

The theorem fixes the double-root cubic, axis, loads, and the finite support
`q1,q0,r2,r1,r0` with the charged exact eight rows. It does not cover moving
axis, nonzero `q2`, moving `k,mu,nu`, a different support, the tied
`alpha=2 beta` chart, another strict branch, the full double-root fan, D1, or
JC2. Although the inequality remains true for `beta>6`, this theorem only
promotes the interval whose control-2 interpretation and omitted-layer
firewall were previously charged: `5<beta<6`.

## Frozen evidence

- LPDP witness freeze:
  `cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826/WITNESS_FREEZE.sha256`,
  SHA-256
  `04cd09886ed78e1af48a6387ee2c67996856d2b6f59791963450e7e4380e32a3`.
- Literal replay freeze:
  `cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/FREEZE.sha256`,
  SHA-256
  `616628e959c6b458948bcf72102c46118e5e6c4c95165f0133e5324579a120ee`.
