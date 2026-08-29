# Iterated blowup makes the collision Cech cover tautological

Date: 2026-08-26

Status: **elementary arc-lifting theorem plus a source-interface reduction.
It does not prove that the present frozen collision clients are base changes
of one total source family, does not kill the exact-square zero receiver, and
does not close order two, maximum twelve, or JC2.**

## 1. DVR lifting theorem

Let `A` be a noetherian ring, let `t in A`, and let
`J=(x1,...,xn)`.  Put

```text
X = Spec(A),                 X' = Bl_J(X) = Proj(Rees_A(J)).
```

For a map `phi:A -> R` to a DVR, if `phi(J)R` is nonzero, then it is a
principal invertible ideal `(pi^m)`.  The universal property of the blowup
therefore gives a unique lift `Spec(R) -> X'`.  At least one `phi(xi)` has
valuation `m`, so the lift lands in the standard chart `D_+(xi*T)`.

Consequently, if `phi(t)` lies in the maximal ideal and the special fibre

```text
X' x_A A/(t)
```

is empty, no such map with `phi(J)R != 0` exists.  If `phi(J)R=0`, then the
map factors through the named zero receiver `V(J)`.  Rational valuations are
included after a finite ramified extension of the DVR.

This proves coverage without a normalization computation: the standard
blowup charts cover by construction, and every nonzero ideal in a DVR is
invertible.  What remains computational is emptiness of the charts and their
identification with the complete source equations.

### Proof detail and base-change warning

The special fibre required here is the base change of the **total blowup**.
It must be computed from `Rees_A(J)` and only then set `t=0`.  Blowing up the
already specialized ring `A/(t)` can lose `t`-torsion and is not a substitute.
Likewise, a naive chart presentation

```text
A[y_j]/(xi*y_j-xj)
```

can contain symmetric-algebra torsion when `xi` is a zero divisor.  Use the
actual Rees kernel (or a proved saturation/presentation of it), then take the
degree-zero localization.  This matters on the collision fibre because the
raw grade-ten ideal has nilpotent `C` thickness.

## 2. Iterated version

Let `J1` be an ideal on `X`, and on `Y=V(J1)` let `J2` be another ideal.
Every DVR arc routes in exactly one of the following ways:

1. `phi(J1)R != 0`: lift to `Bl_J1(X)` and one of its standard charts;
2. `phi(J1)R=0` but `phi(J2)R != 0`: factor through `Y` and lift to
   `Bl_J2(Y)`;
3. `phi(J1+J2)R=0`: factor through the terminal zero receiver
   `V(J1+J2)`.

Thus an ordered principal-chart argument is rigorous without pretending that
locally closed strata are an affine Cech cover.  Empty charts at stages one
and two exclude every arc except the explicitly named terminal receiver.

## 3. Collision application

In one still-to-be-built total post-`M=0`, `D(k0)` source algebra over the
Kummer base `p=-2*rho^2`, take

```text
J1=(rs,cs,c0,c1),
J2=(a0,a1) on V(J1).
```

The first blowup has the ordered routing

```text
D_+(rs),
V(rs) intersect D_+(cs),
V(rs,cs) intersect D_+(c0),
V(rs,cs,c0) intersect D_+(c1).
```

The second blowup routes the remaining `R=C=0` receiver through `D_+(a0)`
and then `V(a0) intersect D_+(a1)`.  Its complement is exactly the named
exact-square/all-load receiver `V(J1+J2)`.  Hence no independent solver is
needed to prove that these six ordered charts cover every arc with a nonzero
collision-correction ideal.  The all-zero receiver is not discarded; it is
the sole output of the theorem's third case.

The reviewed odd unit, confirmed cusp unit, and provisional two `A`-chart
units supply the expected special-fibre endpoints.  They do **not** yet apply
to this theorem: each was formed in a frozen specialized scaling.  The
remaining bridge is to prove that it is the literal base change of the
corresponding total Rees chart.

## 4. Direct cusp simplification worth testing

On the confirmed cusp quotient,

```text
u=c1/rs,
row(6,12)=-(21/1024)*rs^3*u^2=-(21/1024)*rs*c1^2,
5*k0*rs^3+96*c1^2=0.
```

Therefore in that quotient

```text
row(6,12) = (35/32768)*k0*rs^4.                   (4.1)
```

Equation (4.1) would be a unit using only the registered factors `k0*rs`.
The next producer should reconstruct the unparameterized raw grade-twelve row
and emit an explicit membership certificate for

```text
32768*row(6,12)-35*k0*rs^4
```

in the complete predecessor ideal.  The equality after cusp parametrization
does not by itself prove this lift.  If the raw certificate passes, the total
cusp chart can avoid a separate normalization-surjectivity argument.

## 5. Minimal total-family compiler contract

For the collision client, the expensive and error-prone task should now be
restricted to the following exact bridge:

1. Emit one finite raw algebra over `Q[rho]` with `rho` not inverted, all
   corrections, `k10,k6,k2`, and all target rows retained at their true
   bidegrees.
2. Form the actual Rees algebra for `J1`, and after `J1=0` the actual Rees
   algebra for `J2`; record their presentation/saturation identities.
3. On each standard chart, set `rho=0` only after chart formation and print
   bidirectional maps or raw-row ideal equalities to the frozen odd, cusp,
   trivial-`C`, and `A` clients.  Similar-looking Laurent receivers are not
   enough.
4. Emit a localized identity `s=sum h_i*f_i+rho*h` per chart, with `s` made
   only from that chart's registered units.  A finite normalization may be
   used only with a separately certified finite-surjective cover.
5. Preserve `V(J1+J2)` as the exact-square/all-load successor.  As a negative
   control, omit the two `A` charts and require the second-stage exceptional
   fibre to remain nonempty.
6. On `D(rho)`, verify the deck-equivariant transform to both generic-square
   root charts.  This overlap is separate from special-fibre coverage.

Once items 1--5 pass and the terminal zero receiver is independently empty,
the DVR theorem excludes every positive rational `rho` valuation in this one
total chart.  It does not require enumerating integer `ord(rho)` or proving a
separate normalization covers the six standard blowup charts.

## 6. Scope firewall

This theorem reduces the **coverage** part of Gate T to a universal property;
it does not manufacture the total source algebra, the Rees chart maps, or the
localized identities.  It cannot transport a unit between different
filtrations, and it says nothing about `k0=0`, other square Rees cones,
terminal/Taylor realization, global `G2-PSC` landing, the cofinal ceiling, or
JC2.
