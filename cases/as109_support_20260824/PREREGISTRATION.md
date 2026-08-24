# AS109 support-cancellation gate — frozen preregistration

- Round: `20260824T0719Z-c17bd25`
- Root: `S — AS109 bounded support`
- Status at freeze: **SPECIFICATION GATE; NO ENUMERATION RUN**
- Scope: one prime, one seed, one marked collision, at most eight distinct
  correction slots, and the first nonlinear successor only.
- Forbidden: an exponent rectangle or degree cutoff, cap widening, a second
  seed, generic sparse search, AWS, and every modular-to-characteristic-zero
  inference.

This file and `manifest.json` are frozen before a transition enumerator is
written or run. Their hashes are recorded separately in `FREEZE.sha256`.

## 1. Ring, seed, and lift equations

Fix `p=109`. The special-fibre seed is

```text
F_bar=(P_bar,Q_bar)=(x-x^109,y) over F_109.
```

The marked source sections are

```text
r_0=(0,0),  r_1=(1,0),
```

and both map to `(0,0)`. For the first two correction layers use the fixed
integral representative

```text
P=x-x^p+p A_0+p^2 A_1,
Q=y      +p B_0+p^2 B_1                    (mod p^3).
```

Put `L(A,B)=A_x+B_y`. Exact expansion gives

```text
J(P,Q)=1
 +p (A_0x+B_0y-x^(p-1))
 +p^2(A_1x+B_1y
      +(A_0x-x^(p-1))B_0y-A_0y B_0x)       (mod p^3).
```

Thus the frozen coefficient tests over `F_109` are

```text
E1: L(A_0,B_0)=x^108,
E2: L(A_1,B_1)=-N(A_0,B_0),
N(A,B)=(A_x-x^108)B_y-A_yB_x.
```

Collision preservation at both layers is

```text
A_i(1,0)-A_i(0,0)=0,
B_i(1,0)-B_i(0,0)=0,             i=0,1.
```

The two source sections remain distinct. Therefore an exact lift satisfying
these identities remains noninjective at this finite-ring tier. This is not a
characteristic-zero polynomial map.

## 2. Vertex and interaction grammar to be typed

There are exactly three vertex sorts:

1. `P_CORRECTION(component=P, exponent=(a,b), valuation_layer=i)` for a
   nonzero coefficient of `x^a y^b` in `A_i`;
2. `Q_CORRECTION(component=Q, exponent=(c,d), valuation_layer=i)` for a
   nonzero coefficient of `x^c y^d` in `B_i`;
3. `RESIDUAL(exponent=(u,v), layer=i)` for a nonzero coefficient of
   `x^u y^v` in `E1` or `E2`.

The derivative edges are

```text
P(a,b) -> residual(a-1,b), coefficient a, when a>0;
Q(c,d) -> residual(c,d-1), coefficient d, when d>0.
```

The nonlinear bracket edge is fixed by

```text
[x^a y^b, x^c y^d]
 =(a*d-b*c) x^(a+c-1)y^(b+d-1),
```

with the integer coefficient reduced modulo 109. Edges with zero coefficient
modulo 109 do not cancel a residual. Negative exponents are forbidden.

The base residual is `RESIDUAL((108,0),layer=0)`. Base-seed monomials are not
counted against the cap. A correction slot is a labeled pair
`(P-or-Q,(a,b))`; the same slot used at both valuation layers counts once.
There may be at most eight distinct correction slots total.

Literal exponents range over all of `N^2`. No rectangle, total-degree bound,
or maximum exponent is part of this preregistration.

## 3. Frozen gauge equivalence

At first order, quotient by source reparametrizations

```text
G_(U,V)=(x+pU,y+pV) mod p^2
```

such that

```text
U_x+V_y=0,
U(r_0)=U(r_1)=V(r_0)=V(r_1)=0.
```

They are determinant-one polynomial automorphisms modulo `p^2`, with inverse
`(x-pU,y-pV)`, fix the marked sections, and act by precomposition as

```text
(A_0,B_0) -> (A_0+U,B_0+V).
```

For a support graph to be enumerated, this quotient must admit a proved
finite normal-form grammar that satisfies both conditions:

1. it is exhaustive for every literal correction support with at most eight
   slots and no exponent bound; and
2. successor feasibility in `E2`, including the same-slot condition below,
   is independent of the chosen first-order representative or is transported
   by an explicitly frozen determinant-one lift of the gauge through
   `mod p^3`.

If either condition lacks a proof, the registered verdict is
`NO-FROZEN-GRAMMAR`. Replacing the full quotient by an ad hoc list of tame or
Hamiltonian moves is not allowed after freeze.

## 4. Finite-grammar acceptance gate

Before enumeration, produce a proof that the cap plus the grammar and gauge
above yield finitely many normal forms or finitely many symbolic motifs with
a terminating, exhaustive integer-constraint procedure. A symbolic rule
with free exponent parameters is acceptable only if its procedure decides
all nonnegative solutions and all coefficient-zero congruence branches; a
finite sample of those parameters is not.

The gate must reject any purported finiteness argument that silently uses:

- a box `0<=a,b,c,d<=D`;
- a degree bound inferred merely from the eight-slot cap;
- deletion of divergence-free corrections without proving successor/gauge
  invariance;
- an ordering assumption that every correction individually cancels an
  earlier residual, unless a minimal-support theorem proves that ordering
  exhaustive.

Failure returns `NO-FROZEN-GRAMMAR` and stops the root before any transition
enumerator exists.

## 5. Registered graph and coefficient outcomes

Only after the finite-grammar gate passes may two independently implemented
transition enumerators run.

- `CONTROL-FAIL`: an exact seed, collision, bracket, escaping-ray, gauge, or
  toy control fails. Stop.
- `HEIGHT-CERT`: an independently verified integral height strictly
  increases on every transition in the frozen grammar. Exact only for this
  grammar and cap.
- `NO-CYCLE-AT-8`: exhaustive frozen grammar has no support SCC at the cap.
  Exact only for this grammar and cap; do not try nine.
- `SUPPORT-ONLY`: an SCC exists, but the coefficient equations or gauge test
  fail, or `E2` needs a new slot. Stop; it licenses no child.
- `FEASIBLE-CYCLE`: an SCC contains the base residual, `E1` has an exact
  collision-preserving coefficient solution with every declared layer-zero
  slot active, and `E2` has an exact collision-preserving solution using no
  correction slot outside that same set, all after the frozen gauge replay.
  This alone may be submitted for review; it is still only a finite-ring
  necessary condition.

The canonical all-Witt ray

```text
B_0=x^108 y,
B_1=x^216 y,
...
```

is the escaping control: its first nonlinear successor introduces a new
slot. A declared cycle must not count a layer-zero coefficient of zero as an
already active slot.

## 6. Characteristic-zero firewall

No registered outcome proves a lift over `Z_109`, `Q_109`, `Q`, or `C`.
`FEASIBLE-CYCLE` would license at most a later, separately preregistered
integral coefficient scheme. Characteristic-zero counterexample language
requires an independently verified nonempty saturated generic fibre after
inverting 109, followed by exact determinant, collision, degree, and
nonautomorphy replay. Neither an `F_109` point, a `Z/109^n` point, nor a
compatible collection of finite-level points supplies that bridge.

