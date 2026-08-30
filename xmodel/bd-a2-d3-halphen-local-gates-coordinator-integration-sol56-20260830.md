# Coordinator integration: D3 Halphen local gates

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `7240c67d7345b906de0314b8a63a26ad207f73fe`  
Lifecycle: **BINDING COORDINATOR INTEGRATION / LOCAL NECESSARY THEOREMS**

## 0. Disposition

Two independent hostile reviews preserve the two provisional local results.

Fable 5 returns `CONFIRM_WITH_CORRECTIONS` on the triple-line first-jet gate.
It confirms every mathematical item and asks for two replay hardenings: verify
the full Hessian-pencil identities rather than only one coefficient, and pin
the invariant convention to a classical Weierstrass cubic.  Those checks are
now supplied by the versioned replay in Section 4.

GPT-5.5 returns `CONFIRM_WITH_CORRECTIONS` on the CFS state machine.  It
independently reconstructs every forced line move, level drop, cube test,
critical flag and positive control.  Its corrections are theorem-interface
and scope repairs: generic nonsingularity and strict-Henselian insolubility are
explicit inputs; the normalization `q0=1` uses local base rescaling; the
global closure of the control is a separate object; and replay reproduction
uses a SymPy 1.14.0 environment.

This integration adopts all corrections and promotes both local necessary
theorems.  It does **not** promote global attainment of the one-point Halphen
row, a dominant affine-plane first leg, a polynomial map, or a conclusion
about JC2.

## 1. Binding triple-line first-jet gate

Let `R=C[[t]]`.  Let a spatially homogeneous ternary cubic over `R` have
smooth generic fibre, normal total hypersurface germ and central fibre a
triple line.  After a constant projective normalization, a unit rescale and
an order-by-order determinant-one formal substitution, write its first jet
as

```text
F=x^3+t(xQ(y,z)+G(y,z))+O(t^2),
Q=q0 y^2+q1 yz+q2 z^2,
G=b0 y^3+b1 y^2z+b2 yz^2+b3 z^3.
```

Normality forces `G!=0`; under the stated generic smoothness it is also the
exact codimension-one normality test along the central line.  In Fisher's
Weierstrass-anchored normalization,

```text
[t^3]c4 = 24(6b0b2q2-9b0b3q1-2b1^2q2+b1b2q1
              +6b1b3q0-2b2^2q0),
[t^4]c6 = -216 Disc_binary(G).
```

Both coefficients are independent of every higher jet.  The reason is the
vanishing of the lower Taylor tensors of `c4` and `c6` on the seven-dimensional
normal slice `xQ+G`, followed by polarization; it is not a truncation
experiment.

If the charged Hodge/CFS colength at this fibre is positive, the invariant
valuation bounds force both displayed coefficients to vanish.  Since `G` is
nonzero, its binary discriminant condition leaves only a double-root or a
triple-root orbit.  Up to `PGL2` on the central line the complete first-jet
list is

```text
G=y^2z with q2=0;              or              G=y^3.
```

Thus every squarefree transverse first jet is excluded.  For colength two,
the stronger necessary conditions are `v(c4)>=8` and `v(c6)>=12`; the
discriminant condition is redundant.  Neither direction is reversed: these
coefficient conditions do not prove an arc, level attainment or occurrence.

## 2. Binding CFS state machine on the one-point row

Assume in addition the promoted one-point index-three Halphen input: the raw
plane cubic has exact CFS level two, its strictly-Henselian-insoluble minimal
floor has level one, and the generic plane cubic is nonsingular.  Retain the
literal raw base-degree-three expression

```text
F=x^3+tF1+t^2F2+t^3F3,
F1=a x^3+ell x^2y+m x^2z+x(q0 y^2+q1 yz+q2 z^2)+H(y,z).
```

Parameter-dependent first-jet gauges may create determined higher powers of
`t`; none is discarded or treated as a free coefficient here.

The CFS singular-line moves are forced.  Moving successively along `x=0` and
`y=0` gives second reduction

```text
z^2(q2 x+C2 z),              C2=[z^3]F2.
```

If it is nonzero, the forced move along `z=0` returns `F` exactly by spatial
homogeneity.  That three-cycle contradicts the CFS four-iteration level-drop
theorem for this nonminimal level-two model.  Hence `q2=C2=0`, and the second
moved model drops by one level.

Its central reduction must be a nonzero cube because the lowered model is
minimal, strictly-Henselian insoluble and level one.  In the branch
`H=y^2z`, the simultaneous presence of `x^3` and `y^2z` and absence of
`x^2y` is incompatible with a cube.  The entire double-root branch is empty.

In the branch `H=y^3`, put `m=3s`.  The first cube comparison forces

```text
q2=C2=q1=U2=0,       R2=3s^2,       C3=s^3,
Q=q0 y^2.
```

After `X=x+s z`, define

```text
b=Q021-s q0,
c=U3+s^2 ell-s M111,
d=-s^3 a+s^2 V2-s R3,
lambda=b/3.
```

The next transverse cubic is a cube exactly when

```text
3c=b^2,                         27d=b^3.
```

After the corresponding `Y=y+lambda z` shift, its apparent `Yz^2` term
vanishes identically.  The last central form is

```text
z^2(kappa X+eta z),

kappa=3a s^2+2ell s lambda+q0 lambda^2
      -2V2 s-M111 lambda+R3,

eta=-A2 s^3-P2 s^2lambda-T2 s lambda^2-B2 lambda^3
    +V3 s^2+M3 s lambda+Q3 lambda^2.
```

The exact final critical condition is

```text
kappa=0,                         eta!=0.
```

These equations force `s!=0`.  A constant plane normalization then gives
`m=3,ell=0`.  The two intrinsic shards are `q0=0` and `q0!=0`.  Writing the
second as `q0=1` is licensed only after a nonzero local base-parameter
rescaling; with globally marked base data frozen, retain the principal open
`q0!=0`.

This is the complete necessary local constructible locus delivered by the
charged CFS path.  It is a locus of formal coefficients, not a list of maps
or proof of global occurrence.

## 3. Sharp positive control

The local family

```text
F=(x+t z)^3+t y^3+t^3x^2z
```

passes the gate.  Its forced level-one model is

```text
M=(x+z)^3+t y^3+t^2x^2z.
```

In `X=x+z`, the exact coefficient valuations satisfy the CFS critical
inequalities and exactness clauses, so `M` is critical of level one and `F`
has exact level two.  The generic cubic is smooth, and the total local
hypersurface is normal.

The bihomogeneous closure

```text
(Sx+Tz)^3+T S^2 y^3+T^3x^2z=0
```

is a useful global control, but it is not part of the local theorem.  Its
global rationality, resolved boundary, finite-cover ramification and any
dominant-`A2` interface require separate proofs.  In particular, existence
of this local survivor is not global attainment of the promoted surface row.

## 4. Review repairs and executable evidence

The original first-jet replay remains immutable at

```text
08c523e2b2dade813d5c12652bfc501ec02de80470f44e3763571387940e852c
  ops/d3_triple_line_first_jet_invariant_replay.py
```

The hardened wrapper is

```text
e56b323513979ccbc9841fe23e8f8c4f9716564f51be5e12192a2a14fbdfae3b
  ops/d3_triple_line_first_jet_invariant_replay_v2.py
```

It reruns the v1 derivation, verifies both full polynomial identities

```text
[u]H(F+uH(F))   = 3c4(F)F,
[u^2]H(F+uH(F)) = 6c6(F)F-3c4(F)H(F),
```

on the universal gate family, and independently anchors
`y^2z-x^3-a xz^2-bz^3` at `c4=-48a`, `c6=-864b`.  Under
`uv run --with sympy==1.14.0`, ordinary, `-O` and `-OO` output are
byte-identical, 1087 bytes, SHA-256
`a11491677c8167f22cd407e6da05b53d39c32b5c4676804ab0e9c3c04997fe0e`.
The mutation `--mutate-membership-scale` exits one at the new full-membership
check.  Both scripts have zero AST `assert` nodes.

The CFS state-machine replay remains

```text
2570d44ec3c31b4b559299099be196dd52b13b7ba1cfe4539043f96fc823ee9c
  ops/d3_halphen_cfs_state_machine_replay.py
```

With SymPy 1.14.0, ordinary, `-O` and `-OO` outputs are byte-identical,
1130 bytes, SHA-256
`52c7b6445a61ae5f518b46aa93d971603b1a0d4d7c1445767c047904c2df701a`;
the cycle-scale mutation exits one.  The replay checks coefficient algebra,
not the imported CFS, Hodge or strict-Henselian theorems.

## 5. Custody and exact dependencies

Producer custody:

```text
7e73b7a6ebd1c4f6529c8c4502e150de1a8b4e4664d03323bfc8631b03ab08c5
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md
a389b0a700a96f1ac68f3123f19fc7fa502e31b305e0973f164e50c5d6c585bd
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md.artifact.json
be42d2cf894d92928978935381028dbf5ae7ba1d3598a3474d7c1460a7b6dee9
  xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md
148ddb5e532b28a23361866f671984bd22a1b395a836484043f6f82c6001c1bf
  xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md.artifact.json
```

Review custody after receipt-first verification and sealing:

```text
6b828d61705e672ebb1a387d080f5dc7356f88545461fb4c5bcac8293ca825af
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-hostile-review-fable5-20260830.md
ed12c4aae3d63baf697da94479c2ff77b05d734d39797d8d8c1a84abb716fc32
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-hostile-review-fable5-20260830.run.v2
94e56bdd79bbcc579a845ca271f89f0d1169c21fb872a9a9fd9f481a06c716cc
  xmodel/bd-a2-d3-halphen-cfs-state-machine-hostile-review-gpt55-20260830.md
74993f90eaba2c060d4c5134a0394079c41f92a671a0c2438ccd0edc3a76788c
  xmodel/bd-a2-d3-halphen-cfs-state-machine-hostile-review-gpt55-20260830.run.v2
```

Their raw reviewed body hashes are respectively
`1af7e69e4b269ea2e8903606616628438c9b71a3a6e96c4da080a205c41be5da`
and
`4e5466c57ae109e6ab9a2acbc756d62791f0e359c138c18082ea93f2a29326d1`.

The theorem also consumes the already promoted D3 Hodge/four-row
integration
`xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md`,
including the exact level-two row, level-one Halphen floor and
strict-Henselian insolubility input.  Classical inputs are the invariant
theory of ternary and binary cubics, Serre normality, and CFS Theorem 3.5,
Theorem 4.3, Definition 5.1, Lemmas 5.2--5.4 and 5.8, and Proposition 5.6.

## 6. Successor and firewalls

The local CFS branch is exhausted.  Do not spend another large elimination
round on it.  The next decision is global and interface-level: determine
whether the surviving local singularity forces a non-rational or cyclic
boundary subconfiguration, and audit the global positive control as a sharp
negative control.  Those tasks may consume this integration provisionally
while their independent reviews run in the background.

No statement here identifies formal coefficient data with a global surface,
a global surface with a dominant affine-plane parametrization, or either
object with a Keller map.  No proof or disproof of JC2 follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10400`.
- Body SHA-256:
  `96f1687d18f5e06a910e94eca2896a9e8c9bae2c8fd5a277ba418b167227f6a9`.
- Frozen basis: `7240c67d7345b906de0314b8a63a26ad207f73fe`.
