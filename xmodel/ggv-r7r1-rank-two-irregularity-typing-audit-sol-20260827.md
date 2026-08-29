# R7R2: typing audit of the proposed rank-two / irregularity escape

**Author:** Sol / coordinator  
**Date:** 2026-08-27  
**Status:** `DESK THEOREM / PRODUCER-ONLY / INDEPENDENT REVIEW REQUIRED`  
**Question:** Does keeping `(F,G)` coupled, or pushing the determinant equation
in the `t` direction, automatically produce a rank-two or irregular connection
with more obstruction capacity than the reviewed R7R1 rank-one tower?

## 0. Verdict

**No such connection is presently defined, and the canonical linear object
supplied by the exact determinant identity is not holonomic.**  After the
promoted R7R1 formal coordinate change it is one scalar `X`-equation with an
arbitrary formal function of the characteristic parameter in its kernel.
Consequently:

1. keeping `(F,G)` together does **not** by itself give a rank-two connection;
2. the one-operator surface `D`-module has characteristic dimension three,
   not two, so Malgrange's holonomic Euler/irregularity formula does not apply;
3. at the generic point of the face, `s=t/P` is a formally etale parameter and
   the scalar operator has no pole in `s` at zero, so its generic formal
   `s`-slope is zero;
4. an honest regular-holonomic completion of the reviewed logarithmic row
   connections stays regular under algebraic direct image.  Positive
   irregularity would require an additional irregular input or a new
   holonomic relation in the `s` direction, neither of which follows from the
   determinant identity.

This closes only the claimed **automatic** rank/irregularity escape.  It does
not prove an infinite-tower capacity bound, does not remove nonlinear
polynomial-support or descent constraints, and does not exclude a future
explicitly defined higher-rank/irregular client.

## 1. Frozen inputs

The exact inputs are:

```text
R7R1 producer     9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
R7R1 review       7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29
Opus5 proposal    a9b2eb9023ac78733dcbf100e9b584e0445a894edd4098026a073f8ec87e5cff
Fable5 review     1cc41972d5049e68b8464a634c1cfae48ec5e0e1ba995475fa90998f7aad3984
```

R7R1 works over a characteristic-zero differential field
`L=K(X)(p)`, `p^4=H`, with

```text
F=P^8,       G=P^12 W,       s=t/P,       Q=P^2,
P(0)=p in L^x.
```

For the exact normalized determinant equation it proves

```text
E=8 P^21 J(s,W)=t^22,
W_X|s=-(s^22/8)(Q+(s/2)Q_s),
w_(n+22)'=-(n+2)q_n/16.                           (1.1)
```

The reviewed solution kernel is

```text
W_particular + Phi(s),       Phi(s) in C_L[[s]],
C_L=ker(d/dX:L->L).                                  (1.2)
```

The Opus5 proposal called the coupled object rank two and proposed computing
the irregularity of a `t`-direction pushforward at `t=0`.  The Fable5 review
correctly marked that statement provisional: no theorem showed that the rows
realize a finite-rank non-rigid connection, and no pushforward module was
specified.

## 2. Exact conjugacy and the actual differential operator

Because `P(0)=p` is a unit of `L`,

```text
s=t/P=(1/p)t+O(t^2),        s_t(0)=1/p in L^x.
```

Formal inversion therefore gives an isomorphism

```text
L[[s]]  <-->  L[[t]],       t=s P(X,s).              (2.1)
```

Direct product-rule expansion, already independently reviewed in R7R1, is

```text
E=8P^19((tP_t-P)W_X-tP_XW_t).
```

In `(X,s)` coordinates,

```text
J(s,W)=-s_t W_X|s,
s_t=1/(P+sP_s),
E=-8P^21 W_X|s/(P+sP_s).                             (2.2)
```

Thus for any fixed unit `P` and target `E`, the determinant equation is the
single affine scalar equation

```text
partial_X|s W = -E(P+sP_s)/(8P^21).                 (2.3)
```

For `E=t^22=s^22P^22`, (2.3) is exactly (1.1).  Its homogeneous operator is
just `partial_X|s`; `P` is free data as far as this one equation is concerned.
There is no second differential equation for `P` and no `partial_s` equation
for `W`.

### Consequence 2.1 — the claimed rank-two connection is ill-typed

Before the substitution, `(F,G)` are two unknown series subject to one
nonlinear scalar determinant equation.  That is not a rank-two linear
connection.  After the substitution, a choice of `P` leaves one scalar affine
equation for `W`.  Algebraic support/descent conditions may later couple the
coefficients of `P` and `W`, but they do not manufacture an integrable
connection matrix.

The arbitrary `Phi(s)` in (1.2) is a direct invariant of the missing
`s`-equation: there is one independent integration constant in every formal
degree.  A finite-rank connection in the `s` direction cannot be inferred
without extra relations that reduce this infinite constant module.

## 3. Holonomicity test

Fix a particular algebraic/formal `P`.  On the smooth two-dimensional
`(X,s)` chart, ignore the inhomogeneous right side and let

```text
M = D_(X,s) / D_(X,s) partial_X.
```

The principal symbol ideal is `(xi_X)`.  Hence

```text
Char(M) = {xi_X=0} subset T^* A^2,
dim Char(M)=3.
```

A nonzero holonomic module on a smooth surface has characteristic dimension
two.  Therefore `M` is coherent but **not holonomic**.  Equivalently, its
solution sheaf permits an arbitrary function of `s`, exactly as (1.2) says.

The Malgrange index formula quoted in the proposal,

```text
chi_dR = rank * chi_top - sum irregularity,
```

is a statement about a finite-rank meromorphic connection / holonomic
`D`-module on a curve.  It cannot be applied to `M`, and the direct image of
this underdetermined one-operator module is not thereby a finite-rank
`t`-connection.  Calling its missing equation “positive irregularity” changes
an absence of holonomicity into a numerical invariant that is not defined.

### Mutation controls

- Adding a second relation such as `partial_s W=A(X,s)W` can make a
  holonomic connection, but its compatibility and slopes depend on the new
  matrix `A`; the determinant equation supplies no such `A`.
- Choosing `partial_s W=s^(-2)W` manufactures positive irregularity, while
  choosing `partial_s W=0` gives a regular connection.  Both share (2.3).
  Thus irregularity is not determined by the R7R1 data.
- Removing the unit hypothesis `P(0)=p in L^x` can break the coordinate
  change, but that leaves the licensed generic-field R7R1 object and moves to
  an extension across `H=0`; it is a different theorem obligation.

## 4. What is regular and what is not supplied

Each reviewed row connection

```text
nabla_m=d+(m/4)dH/H       on U=A^1-Z(H)
```

is rank one and logarithmic, hence regular singular.  The row label `m` is a
discrete grading/character; the collection of all `m` is not automatically a
finite-rank connection in the formal parameter `s`.

At the generic point used by R7R1, (2.1) is unramified and the coefficients in
(2.3) lie in `L[[s]]`; for the normalized target the right side is divisible
by `s^22`.  There is no pole at `s=0`, no exponential factor and no positive
formal slope.  Thus the only canonical generic formal object has
`s`-irregularity zero.

One could instead construct a regular-holonomic extension of the logarithmic
Kummer local system over an algebraic `(X,s)` family and take an algebraic
direct image.  Standard regular-holonomic stability under the six operations
(for example Hotta--Takeuchi--Tanisaki, Chapter 6) preserves regularity, so
that route also does not create positive irregularity for free.  Confluence
at roots of `H` may require a nontrivial extension analysis, but any claimed
irregular module must then be specified and shown not to be the regular
holonomic extension; it is not encoded in (1.1).

This distinction is load-bearing:

```text
current exact object       = nonholonomic one-operator family / rowwise regular connections;
positive irregular escape = additional finite-rank irregular holonomic object, not yet defined.
```

## 5. Campaign consequences

### Promotable after independent review

1. The determinant identity does not canonically define a rank-two
   connection by retaining `(F,G)`.
2. Its fixed-`P` linear `D`-module on `(X,s)` is nonholonomic, with
   characteristic dimension three and kernel `C_L[[s]]`.
3. The formal coordinate change is etale at `t=s=0` over `L`, and the generic
   scalar equation has zero `s`-slope.
4. Malgrange's holonomic irregularity term cannot be used as additional gate
   capacity without first supplying a new holonomic `s`-relation.

### Allocation change

- **Close avenue 16's automatic irregularity escape** as presently stated.
  Reopen only upon an explicit finite-rank holonomic `D`-module, a complete
  connection matrix, and a proof that it is forced by polynomial Keller data.
- **Narrow avenue 25's rank-two escape** the same way.  Coupled nonlinear
  support equations remain important, but “two series” is not “rank two.”
- Continue the upper-face programme through exact raw support, descent and
  nonlinear mixed rows.  Those are precisely the constraints discarded by
  the field-level integration (2.3).
- Do not infer that the infinite `q_n` tower is capacity-bounded.  This audit
  removes one proposed way to increase its index; it does not count the
  nonlinear or all-order algebraic constraints.

### Cheapest honest revival test

Require a proposed higher-rank client to provide all four objects:

```text
(i) a finite-rank O(*D)-module,
(ii) both X- and s-connection matrices,
(iii) flatness/integrability,
(iv) a theorem mapping every polynomial Keller pair into its horizontal sections.
```

Then compute its formal slopes at `s=0`.  Without (i)--(iv), an
“irregularity computation” is not a discriminator.

## 6. Scope and review request

This is a typing/no-free-lunch theorem about a proposed research instrument.
It proves no endpoint nonexistence, no survivor-family exclusion, no
`G2-PSC`, landing theorem, degree ceiling, counterexample or JC2 result.  It
does not weaken the promoted R7R1/de Rham law; it uses that theorem's exact
conjugacy and full integration-constant kernel.

Independent review must check the characteristic-variety calculation, the
distinction between a nonlinear two-unknown equation and a rank-two
connection, the formal-etale/zero-slope claim, and the scope of
regular-holonomic direct-image preservation.  If the last paragraph is too
broad for a nonproper family, delete it: Sections 2--3 already establish the
load-bearing no-go without any direct-image theorem.

No heavy algebra, AWS mutation or `jc2-lean` access was used.  This report is
the only file written for this atom.
