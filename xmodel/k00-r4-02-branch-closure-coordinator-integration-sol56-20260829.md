# K00 V20R2 valuation four: coordinator integration closing R4-02

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `327db542d77588d91b1d4cb4541eb3bececc0d16`  
Lifecycle: `PROMOTED EXACT R4-02 EXCLUSION / R4-00 SOLE INTEGER RESIDUAL`

## Binding verdict

Promote the exact grade-15 exclusion of the entire old-plane,
next-rank-two valuation-four cell. On the normalized V20R2 source, assume

```text
d=Lambda^4*x+Lambda^5*y+...,
x=ell(s,t), (s,t)!=(0,0),
A(y)=B(y)=0,
Delta_y=u_y^2+64*v_y^2 != 0,
k10[0]!=0, Jdet[0]!=0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0.
```

Then no field-valued characteristic-zero jet satisfies the literal rows
through grade 15. In particular both reviewed `R4-02` branches are empty.
Composed with the reviewed parent rank fan, the only literal
exact-valuation-four residual through grade 19 is `R4-00`, where both
`x` and `y` lie on the old rank-zero plane. `R4-00` is not asserted
nonempty or attained.

## Evidence

The Opus 5 producer is
`xmodel/k00-r4-02-branch-closure-opus5-20260829.md`, full SHA-256
`a4fe05d33066d956016b3ef152fc138b5bd3a1dd0a4eec77f8ba05ada2c5f812`,
body SHA-256
`32f79463afee2083dd5ca010d8783942484961a290766d06c707a2ed99c0a6b0`.

Fable 5 independently rebuilds the 569-tail source with two separate exact
evaluation paths in
`xmodel/k00-r4-02-branch-closure-hostile-review-fable5-20260829.md`, full
SHA-256
`3d9500d3ce2ad2db105d23968b9b9a5e5e0e129b6597ac46b088b03978cba7b2`,
body SHA-256
`83ccbb0f7d03992addc429e9e630f4ec4d7b63df3b99b6f14cb64421e717a863`.
All seven attack areas are `CONFIRMED`; its verdict is
`PASS_WITH_MINOR_REPAIRS`.

The reviewed parent narrowing is binding integration
`xmodel/k00-r4-jetfan-coordinator-integration-sol56-20260829.md`, full
SHA-256
`bb6ebb1273865f92fec12313216bc36e66a36d7238b7eb988d813e84f7906839`,
body SHA-256
`75dce8299048dff7b36238a5c2dda9485e59b2e4e14826dfe29f963af8c0755d`.
It supplies the exhaustive leading and next-coefficient rank split; the
present result supplies the previously missing next-rank-two kill.

## Exact obstruction

For

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4,
```

the image of `DQ(y)` on the reduced cone lies in one fixed two-plane
`W`; it equals `W` on `D(Delta_y)`. Five fixed functionals annihilate
`W`. The raw grade-11 system has no inhomogeneity and forces
`A(d[6])=B(d[6])=0`.

Three exact grade-15 cokernel combinations, with every later jet, load and
target coordinate still symbolic, reduce modulo the grade-11 equations to

```text
D1 = (3/4096)*Phi,
D2 = -(1/512)*Phi,
D3 = (1/65536)*Psi,

Phi = v_y*(64*v_y^2-3*u_y^2),
Psi = u_y*(192*v_y^2-u_y^2).
```

The equations `Phi=Psi=0` contradict `Delta_y!=0` over every
characteristic-zero field. On the two original `R4-02` branches the
certificates specialize to the explicit units

```text
u_y=0:                 D1=(3/64)*v_y^3,
u_y^2=192*v_y^2:       D1=-(3/8)*v_y^3.
```

The branch open makes `v_y` a unit. The displayed five-row membership
certificate therefore puts one in each localized branch ideal. No
`k2[1]`, `k6[1]`, free cone coordinate, later jet, or target column can
rescue the branches; the raw support of `D1,D2,D3` excludes them. A witness
through grade 14 confirms grade 15 is the first kill rather than an omitted
earlier obstruction.

## Repairs folded into promotion

1. The producer's grade-12/13 cokernel rows vanish after imposing the
   grade-11 equations, not as raw identities. The sequential argument is the
   promoted one.
2. The uniform rank-two exclusion uses the pair `Phi=Psi=0` and both
   `v_y=0` / `v_y!=0` charts. The `v_y`-localized units above certify
   the two registered `R4-02` branches; no single such unit is claimed on
   the whole uniform cell.
3. The producer's auxiliary 57-record `CERTIFICATE_DIGEST` lacks a pinned
   serialization rule and is dropped. The displayed polynomial identities
   and independently reconstructed membership certificates carry custody.

## Sole integer residual and scope

The remaining `R4-00` entry has both first visible coefficients on the old
plane. Its first nontrivial successor is the six-row grade-12 system

```text
Q_i(z)+kappa*polar_M2_i(x,z)=0
```

with row six identically zero; all later literal rows remain imposed.
Nothing here proves that system has a point, arc, or lift.

This is reduced, field-valued finite-jet emptiness on one normalized support.
It is not scheme-theoretic, a ramified-DVR closure theorem, an actual map, a
counterexample, or a JC2 result. Formal data are not maps and a residual
packet is not attainment.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4550`.
- Body SHA-256:
  `0e4dc8077e53fec6d69eb572db6e17ef3f2944fcd0736f2c7ffb9fbd37df888a`.
- Frozen basis: `327db542d77588d91b1d4cb4541eb3bececc0d16`.
