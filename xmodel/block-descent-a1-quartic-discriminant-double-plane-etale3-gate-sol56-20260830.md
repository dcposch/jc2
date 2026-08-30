# Rank-four cyclic horn: discriminant double-plane and étale cubic gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_double_plane` lane)  
Frozen basis: `4393243bccdbe1a32d80fe8c770c2c8b909f4c01`  
Lifecycle: **FINAL+VERIFIED EXACT GATE / NO RANK-FOUR EXCLUSION**

## 0. Verdict

Let `Omega/K`, `K=C(x,y)`, be the `S4` Galois closure attached to an
actual rank-four proper block in the charged minimal connected-cycle row, and
let

```text
M=Omega^V4,                 Gal(M/K)=S3,
K2=Omega^A4=M^A3.
```

Write `W` and `D` for the normalizations of `A2` in `M` and `K2`.  If
`q_B` is a reduced equation of the target branch, then

```text
D = Spec C[x,y,s]/(s^2-q_B),
W -> D is a connected finite C3-cover.                         (0.1)
```

The exact answer to the étaleness question splits the two surviving arithmetic
rows.

```text
m=0:  W -> D is finite étale of degree 3;
m=1:  W -> D is not étale at the unique (3,1) value.            (0.2)
```

Here `m=|T31|` in the threat-map notation, every branch component is
generically `(2,1,1)`, and the minimal row has

```text
h=k=1, beta1(B)=n22=1, n4=0.
```

Consequently the `m=0` horn pays a new exact topological price:

```text
0 != alpha=[W/D] in H^1_et(D,Z/3),       iota^*alpha=-alpha,    (0.3)
```

where `iota` is the deck involution of `D/A2`.  Thus every proposed branch
whose normal double plane has zero mod-3 étale cohomology is excluded.

This does not yet exclude the abstract minimal horn.  The branch ledger fixes
`e(B)=0` and the normalization/one-identification topology, but it does not
compute the embedding-sensitive group in (0.3).  The named nodal control has
`H^1_et(D,Z/3)=0` and is excluded again by this gate.  Conversely, explicit
double planes with connected Euler-zero branch and a connected étale cubic
cover exist; the clean control below has branch normalization `Gm`, not `A1`.
Therefore neither Euler number, connectedness, nor the double-plane
construction alone gives the missing contradiction.  The remaining sharp
question is whether the **polynomial-curve/one-place** branch supplied by the
proper-block theorem can carry the nonzero locally unramified class (0.3).

## 1. Charged inputs and exact scope

```text
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
  ops/block_descent_a1_quartic_discriminant_double_plane_replay.py
```

This report assumes an actual strict rank-four block and the corrected
cyclic-`S4` theorem.  It treats only its minimal connected-cycle row with
generic `(2,1,1)` branch.  It does not assert existence of that row, does not
treat a primitive/no-proper-block Keller extension, and does not use the
cubic proper-block theorem: the normalized cubic resolvent has no inherited
Keller first leg.

## 2. The canonical `S3`, quadratic, and cyclic-cubic tower

The normal Klein four group acts trivially on the three perfect matchings of
four letters, and

```text
S4/V4 = S3,                    A4/V4 = A3=C3.           (2.1)
```

For a `D4` containing `V4`, the degree-three field `Omega^D4` is the
normalized cubic resolvent already constructed in the charged packet.  Its
Galois closure is `M=Omega^V4`.  The sign-quadratic subfield is
`K2=Omega^A4`.

The reduced branch of `M/K` is exactly `B`: a divisorial transposition maps
to a transposition in `S3`, while the cover is étale off `B`.  Since `A2` is
factorial and has no nontrivial étale quadratic cover, the square class of
`K2/K` is represented by the product of the reduced branch equations.  After
rescaling by a square in `C*`,

```text
K2=K(sqrt(q_B)).                                         (2.2)
```

The hypersurface `s^2=q_B` is `S2` and regular in codimension one because
`q_B` is reduced, hence normal.  It is therefore the normalization `D` in
(2.2).  Normalizing `A2` in the field `M` gives a connected normal finite
`S3`-cover `W`; quotienting by `A3` gives the finite cyclic map in (0.1).

## 3. Point-stabilizer criterion

Let `z` be a closed point of the target, choose a point of `W` above it, and
let `H_z <= S3` be its decomposition group.  Residue fields are `C`, so the
stabilizer for the `A3`-action on that point is exactly

```text
H_z intersect A3.                                       (3.1)
```

A finite tame group quotient is a torsor precisely when every geometric
stabilizer is trivial.  Thus `W->D` is étale at all points over `z` iff
(3.1) is trivial.  This uses decomposition groups, not the roots of a
possibly nonnormal classical resolvent polynomial.

The corrected local table gives

```text
quartic fibre       image H_z in S3       H_z intersect A3
(2,1,1)             C2                    1
(2,2)               C2                    1
(3,1), finite       S3                    A3
(4)                 A3 or S3              nontrivial.   (3.2)
```

For the finite `(3,1)` row here, generic branch inertia is a transposition;
the three-point orbit plus such an element forces the full local `S3`, not
`C3`.

## 4. The no-cusp row forces a nonzero mod-3 class

In the `m=0,n4=0` row, every affine fibre is of type `(2,1,1)` except the
unique `(2,2)` value.  Equations (3.1)--(3.2) show that the `A3` action on
`W` is free at every closed point.  Hence

```text
W -> D is a finite étale C3-torsor.                      (4.1)
```

It is connected because `M` is a field.  A trivial `C3`-torsor is the
disjoint union of three copies, so (4.1) defines a nonzero class `alpha` in
`H^1_et(D,Z/3)`.  A transposition in `S3` conjugates a three-cycle to its
inverse.  Therefore the residual involution `iota` of `D/A2` acts by

```text
iota^*alpha=-alpha.                                     (4.2)
```

Since `C` contains the cube roots of unity, Kummer theory gives the useful
candidate-by-candidate exact sequence

```text
0 -> O(D)^*/O(D)^{*3} -> H^1_et(D,Z/3) -> Pic(D)[3] -> 0. (4.3)
```

Thus if a proposed `D` has only constant units, (4.1) forces a nonzero
anti-invariant three-torsion line bundle.  This report does not assume that
all double planes in the horn have constant units; (4.3) deliberately keeps
the unit alternative visible.

There is also a necessary codimension-two extension gate.  Put
`Dreg=D-Sing(D)`.  Restriction of finite étale covers from a normal scheme to
`Dreg` is fully faithful.  A `C3`-torsor on `Dreg` extends over `D` only when
its restriction to every punctured strict-henselian singular neighborhood is
trivial.  An Alexander/sign-cover computation on the curve complement sees
the punctured class first; local link residues must still be killed.  This is
why a cusp cannot be treated as an étale point merely because the cyclic
cover is unramified in codimension one.

## 5. The unique-cusp row is only quasi-étale

For `m=1,n4=0`, (3.2) gives a point with `H_z=S3`.  Its stabilizer in the
cyclic subgroup is `A3`, so the canonical `W->D` is not étale there.  After
deleting that point it is a connected étale `C3`-cover, but its class has a
nonzero local residue and does not supply (0.3).

The ordinary-cusp control makes the distinction literal.  The double plane
is the `A2` singularity

```text
Dloc: U*V=X^3
     = Spec C[a*b,a^3,b^3],
```

and the cyclic map is

```text
A2_(a,b) -> A2_(a,b)/mu3,
(a,b) |-> (zeta*a,zeta^(-1)*b).                         (5.1)
```

It is étale away from the origin and fixed at the origin.  The punctured
surface has the expected nontrivial `C3` cover, while the whole positive-
weight affine cone is contractible and has
`H^1_et(Dloc,Z/3)=0`.  The model is a control, not a claim that every
`(3,1)` germ is analytically ordinary.

## 6. Named nodal control: exact vanishing

For

```text
B0: y^2=x^2(x+1),
D0: w^2=y^2-x^2(x+1),
```

put `u=y+w`, `v=y-w`.  Then

```text
D0 = Spec R0,       R0=C[x,u,v]/(u*v-x^2(x+1)).         (6.1)
```

This normal Danielewski surface has no nonconstant units.  Indeed, after
inverting `u`,

```text
R0[1/u]=C[x,u,u^(-1)]
```

has units `c*u^n`; a unit of `R0` has zero Weil divisor, forcing `n=0`.

Nagata's class-group computation uses the two height-one primes

```text
P0=(u,x),       P1=(u,x+1),       div(u)=2P0+P1.
```

It gives

```text
Cl(R0)=Z^2/<(2,1)> = Z.                                (6.2)
```

In particular `Pic(D0)`, a subgroup of the torsion-free class group, has no
three-torsion.  Equations (4.3), (6.1), and (6.2) yield

```text
H^1_et(D0,Z/3)=0.                                      (6.3)
```

Thus the named node cannot be the `m=0` discriminant of an `S3` resolvent.
This independently recovers the earlier van-Kampen exclusion, now at the
quadratic-subcover interface.

## 7. Positive odd-étale controls

Two controls prevent a false universal vanishing claim.

First,

```text
Dpar: w^2=x^2-1
```

has coordinates `t=x+w`, `t^(-1)=x-w`, hence

```text
Dpar = Gm_t x A1_y.
```

Adjoining a cube root of `t` is a connected étale `C3`-cover.  Its branch in
`A2` is the disconnected union of two parallel lines, so it is outside the
minimal horn but proves that the phrase "affine double plane" carries no
odd-cohomology vanishing theorem.

Second, there is a connected full-`S3` control.  Over `A2_(x,y)` take

```text
p(T)=T^3+x*T+x*y+1,
Delta=-4*x^3-27*(x*y+1)^2.                             (7.1)
```

The branch `B1=(Delta=0)` is smooth and has the mutually inverse
parametrizations

```text
x=-3*r^2,       y=(1-2*r^3)/(3*r^2),       r in Gm,
r=-3*(x*y+1)/(2*x).                                    (7.2)
```

It is therefore connected with `e(B1)=0`, but its normalization is `Gm`.
There is no triple root because `x=0` and `x*y+1=0` have no common solution.
The cubic is irreducible: over `C(x)`, equation `p(T)=0` writes `y` as a
degree-three polynomial rational function of `T`.  Its nonsquare
discriminant then gives Galois group `S3`.

The Galois closure is explicit:

```text
W1: a^3+b^3-3*a*b*y+1=0,
mu3: (a,b) |-> (zeta*a,zeta^(-1)*b).                    (7.3)
```

The action has no fixed point: a fixed point would have `a=b=0`, contrary to
the constant term `1`.  Its invariant ring is generated by

```text
x=-3*a*b,       y,       a^3-b^3,
```

and is precisely the double plane `s^2=Delta` after scaling the last
generator.  Hence `W1->D1` is a connected finite étale cubic cover and

```text
H^1_et(D1,Z/3) != 0.                                   (7.4)
```

This is not a proper block or a quartic spectator.  It is the sharp negative
control: connectedness and `e(B)=0` coexist with the required odd class; what
it violates is exactly the charged `A1` normalization/one-place input.

## 8. Maximum-safe conclusion and successor

Promote only the following scoped facts.

1. The minimal `m=0` cyclic-`S4` horn forces a connected finite étale
   degree-three cover of its normal discriminant double plane, hence a
   nonzero anti-invariant class (0.3).
2. In the `m=1` horn the canonical cyclic cover has a nontrivial `C3`
   stabilizer at the unique `(3,1)` value and is not an étale cover of the
   whole double plane.
3. The named nodal double plane has zero mod-3 étale cohomology and is
   excluded.
4. Odd étale classes occur on affine double planes, including the connected
   Euler-zero `S3` control (7.1)--(7.4); no universal vanishing theorem follows
   from the coarse branch ledger.

The cheapest exact successor for `m=0` is therefore:

```text
R4-DP3:
  For a reduced plane curve B whose components normalize to A1 and which is
  obtained from one connected source forest by exactly one two-point
  identification, compute the locally extendable anti-invariant part
  H^1_et({s^2=q_B},Z/3)^-.  Prove it is zero using the one-place infinity
  relation, or exhibit a branch with a nonzero class satisfying all local
  C2 splitting conditions.
```

For a frozen equation, compute `O(D)^*` and `Pic(D)[3]` via (4.3), or compute
the sign-character cover of the curve complement and then impose triviality
on every singular link.  A punctured/Alexander class without the local
extension check is not enough.

Do not promote an exclusion of all `m=0` branches, a vanishing theorem for
all rational or all Danielewski double planes, an étale cover in the `m=1`
row, a cubic proper-block structure, a rank-four block exclusion, or JC2.

## 9. Desk replay and firewalls

The deterministic replay is

```text
2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
  ops/block_descent_a1_quartic_discriminant_double_plane_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256:
66ecf7bae2685fb6c379fef27cbcad006cc513d2b1b32af700a3821411119745

status=PASS-QUARTIC-DISCRIMINANT-DOUBLE-PLANE
payload_sha256=e5bd7a7fc837d40a7aa604c1b213964c2b7e91e9f09d95cf1a996f674960fafb
```

The verifier has zero Python `Assert` nodes.  The mutation
`--mutate-cusp-as-etale` exits nonzero.  It checks `S4/V4=S3`, the node and
cusp stabilizer orders, the nodal Danielewski identity, the ordinary-cusp
quotient relation, and every displayed identity in the connected odd-étale
control.

The replay does not prove normality, the finite-group torsor criterion,
Kummer theory, the Nagata class-group computation, cubic irreducibility, or
existence of an actual block.  Those are written mathematical arguments and
must not be inferred from the finite check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13844`.
- Body SHA-256:
  `4b1a7bf4b829fb2bf653a5421375d8caac159491c3a0986df0428e0b5f77c285`.
- Frozen basis: `4393243bccdbe1a32d80fe8c770c2c8b909f4c01`.
