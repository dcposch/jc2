# Max12 `(9,12)` order-three loaded parity: exact normal rank and `Q12`

Date: 2026-08-24  
Status: **producer checkpoint; frozen pending hostile review**

## 1. Scope and dependencies

Work on the reviewed order-three fibre with

```text
k=mu=0,    r1=r2=r3=r4=r5=r7=0,    r6=nu != 0.
```

This note uses the reviewed parity coordinates and generic chart from the
frozen genus-five exclusion, but asks a different question: can a component
leave the parity fixed locus infinitesimally?  The answer is generically no,
with one explicit residual rank boundary.  Nothing below excludes that
boundary or classifies a disjoint non-parity component.

The replay pins the exact order-three compiler and reviewed parity replay by
SHA-256.  It has no non-stdlib dependency.

## 2. Involution and square normal block

The involution

```text
f(z) |-> -f(-z)
```

fixes the parity locus

```text
a0=a2=a4=a6=0.
```

With `k=0`, its anti-invariant tail equations are

```text
r1=r3=r5=r7=0,
```

while `r2,r4,r6,r8` are invariant.  Thus the normal linearization is the
square matrix

```text
J_N = d(r1,r3,r5,r7) / d(a0,a2,a4,a6).                (2.1)
```

The replay checks directly from the coefficient compiler that the odd rows
vanish on parity and that every even row has zero normal differential there.

Write the parity polynomial as

```text
f=(z^3+p*z)^3+x5*z^5+x3*z^3+x1*z.
```

## 3. Exact determinant on the reviewed generic chart

Retain the reversible chart

```text
A=x3-2*p*x5,    p*x5*A != 0,    v=A/(p*x5).
```

The reviewed equations `r2=r4=0` give

```text
x3=p*x5*(v+2),
x1=x5*p^2*(v+1)+x5^2*(3v+1)/(9v),
x5=-36*p^2*v^2*(3v^2+3v+1)/(3v^2-2).
```

Exact substitution into (2.1) yields

```text
det(J_N) = p^20 * (-8388608/243)
           * v^14 * (3v^2+3v+1)^7 * Q12(v)
           / (3v^2-2)^10,                              (3.1)
```

where

```text
Q12(v)=2893401*v^12+4809213*v^11-2488077*v^10
       -12217797*v^9-12251574*v^8-5322618*v^7
       -503280*v^6+391932*v^5+111060*v^4+4608*v^3
       +8664*v^2+4688*v+480.                           (3.2)
```

The replay proves (3.1) by exact rational-function equality rather than
numeric sampling or a Gröbner reduction.

On this chart `p` and `v` are nonzero.  The reviewed parity relation separates
`3v^2-2=0` and forces `x5=0` when `3v^2+3v+1=0`; those boundary cases were
already handled in the parity theorem.  Therefore the only new normal-rank
boundary on the retained chart is

```text
Q12(v)=0.                                               (3.3)
```

Exact Euclidean checks show that `Q12` is squarefree and coprime to

```text
v,  3v^2+3v+1,  3v^2-2,
A5(v)=33v^5+117v^4+131v^3+69v^2+18v+2.
```

In particular, (3.3) is not made empty by `r6=nu != 0`: over the algebraic
closure, the equation `p^9 R6(v)=nu` still supplies loaded points above roots
of `Q12`.

## 4. Exact conclusion and retained gap

Away from (3.3) and the already separated `p`, `x5`, and `A` boundaries, the
loaded fibre is scheme-theoretically normal-unramified along the parity fixed
locus at first order.  Hence a formal component meeting parity there cannot
acquire a new normal tangent.

At `Q12=0`, the normal matrix drops rank and this note makes **no trapping
claim**.  A higher-order Kuranishi calculation or a component computation is
required.  This checkpoint does not exclude a non-parity component, either
meeting parity at (3.3) or disjoint from it.  It has no all-`(9,12)`,
maximum-degree-twelve, counterexample, or Jacobian-conjecture conclusion.

## 5. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_normal_q12_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.json -
```

The replay regenerates the normal determinant from the exact coefficient
compiler, verifies the involution typing, proves (3.1), and checks all stated
squarefreeness and gcd assertions.
