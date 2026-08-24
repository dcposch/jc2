# AS109 wild-symplectic first gate — preregistration

Date: 2026-08-24  
Scope: one completed-bidisc theorem and one first-Witt-digit compiler at
`p=3,5`; no `p=109` computation, no AWS, no global polynomial descent, and no
JC2 inference.

## Mathematical gate

Conditionally assume a polynomial pair over `Z_p`

```text
F=(P,Q) == (x-x^p,y) mod p,       det J(F)=1.
```

For `B=Z_p<U,V>` and `A=Z_p<x,y>` (restricted Tate algebras), test the
following claim and stop at the first failed implication:

1. `A/pA` is free of rank `p` over `B/pB` on `1,x,...,x^(p-1)`.
2. Successive `p`-adic division lifts that basis, making `A` finite free of
   rank `p` over `B`.
3. `det J(F)=1` makes the finite map etale.
4. The finite-etale lifting equivalence for the Henselian pair `(B,pB)`
   uniquely lifts every special Artin--Schreier translation, giving a free
   `C_p` action on the unit bidisc with determinant one.
5. This statement is only completed/restricted-analytic.  It gives neither a
   polynomial/rational deck transformation nor removal of the previously
   registered `A_infinity` factor.

Also test whether unrestricted completed symplectic gauge is already
transitive: for any two determinant-one restricted-analytic lifts `F,G` with
the same special fibre, multivariate Hensel should give a unique
`phi == id mod p` with `F o phi=G`; the chain rule should give
`det J(phi)=1`.  If true, no finite-depth support statistic is gauge-invariant
unless the gauge itself is uniformly support/degree bounded.

## Exact compiler window

Run only `p in {3,5}`.  At the first Witt digit write

```text
P=x-x^p+p P1, Q=y+p Q1,
tau=(x+1,y)+p(a,b) mod p^2.
```

The registered coordinate window is

```text
0 <= x-degree <= p,       0 <= y-degree <= 1
```

for each of `P1,Q1`.  It is the smallest rectangle containing the rational
cotangent control `P1=0, Q1=x^(p-1)y` and the unavailable formal
`x`-primitive `x^p/p`.  The compiler must:

1. derive and check `N(a)=-1`, `N(b)=0`, `a_x+b_y=0`;
2. check `a=c-Delta(P1)`, `b=-Delta(Q1)`, and
   `P1_x+Q1_y=x^(p-1)` for the cotangent control;
3. row-reduce the entire registered coefficient window, verify that its
   affine solution set is a torsor under the divergence-free gauge kernel,
   and test whether the coefficient of `x^(p-1)y` in `Q1` is forced;
4. verify the exact finite cotangent tower through depths `2,3,4` only as a
   control (determinant, inverse unit, support law).  It must not treat that
   tower's growth as gauge-invariant.

All arithmetic is deterministic sparse integer/modular polynomial arithmetic
using only the Python standard library.

## Stop outcomes

- `COMPLETION-GAP`: any rank, flatness, etaleness, lifting, action, or
  determinant implication fails.  Freeze the first false sentence; do not
  run the support interpretation.
- `FINITE-MIXED-CLASS`: the full first-digit quotient has a nonzero class not
  represented by the cotangent control.  Freeze it as a motif only.
- `GAUGE-TRIVIAL/CONTROL-ONLY`: the completed action theorem holds, the
  first-digit affine space is one gauge orbit, and the rational control
  passes.  Stop raw finite-depth cohomology.  A successor is licensed only
  after preregistering a *uniformly bounded* polynomial-gauge category or a
  genuine algebraic boundary conductor.

No outcome proves or disproves the plane Jacobian conjecture.
