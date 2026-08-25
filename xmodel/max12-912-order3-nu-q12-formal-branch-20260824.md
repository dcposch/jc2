# Max12 `(9,12)` order-three loaded fibre: `Q12` forces a non-parity formal branch

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Exact scope

Work in the reviewed order-three high-coefficient fibre with fixed

```text
k=mu=0,    nu != 0,
r1=r2=r3=r4=r5=r7=0,    r6=nu.                         (1.1)
```

There are eight dynamic coefficients `a0,...,a7` and seven equations in
(1.1).  The eighth reconstructed row `r8` is not imposed here: it belongs to
the terminal differential equation.  This note proves a statement about the
completed seven-row coefficient fibre, not about a Keller trajectory.

The exact predecessor isolated the residual parity-normal rank divisor
`Q12(v)=0`.  No predecessor bytes are changed here.

## 2. Involution blocks and exact ranks

The involution `f(z) -> -f(-z)` negates

```text
n=(a0,a2,a4,a6)
```

and fixes the four parity coordinates

```text
b=(p,x1,x3,x5),
a7=3p,  a5=3p^2+x5,  a3=p^3+x3,  a1=x1.              (2.1)
```

The replay reconstructs every original row `r1,...,r8` and checks monomial by
monomial that `r_l` has involution character `(-1)^l`.  Thus the Jacobian of
(1.1) at parity is block diagonal:

```text
J_N = d(r1,r3,r5,r7)/d(a0,a2,a4,a6),
J_I = d(r2,r4,r6)/d(p,x1,x3,x5).                       (2.2)
```

On the reviewed generic chart

```text
v=(x3-2*p*x5)/(p*x5),    p*x5*(x3-2*p*x5) != 0,
```

the predecessor proved

```text
det(J_N)=p^20*(-8388608/243)
         *v^14*(3v^2+3v+1)^7*Q12(v)/(3v^2-2)^10.      (2.3)
```

At every root of `Q12`, exact univariate gcd certificates give:

```text
rank J_N = 3:
  det d(r3,r5,r7)/d(a2,a4,a6) is a unit;

rank J_I = 3:
  det d(r2,r4,r6)/d(x1,x3,x5) is a unit.              (2.4)
```

Consequently the parity fixed fibre is a smooth curve, the full Jacobian has
rank six, and the full Zariski tangent space has dimension two.

The replay also checks

```text
gcd(Q12,Q12')=1,
gcd(Q12,num(R6'))=1,                                   (2.5)
```

as well as coprimality with every unit factor in (2.3).  The second identity
is a redundant but useful control that the loaded fixed curve is not tangent
to the `Q12` divisor in the `p` coordinate.

## 3. Equivariant formal implicit-function theorem

Fix a loaded parity point above a root `v0` of `Q12` over the algebraic
closure of the constant field.  Such points exist: `R6(v0)` is nonzero, so
`p^9 R6(v0)=nu` has a nonzero solution.

Use the unit minors (2.4) to eliminate simultaneously three invariant and
three anti-invariant variables.  Retain one invariant coordinate `s` along
the fixed curve and one anti-invariant coordinate `t`.  Uniqueness in the
formal implicit-function theorem respects the involution, so the sole
remaining odd equation has the exact form

```text
t*Phi(s,t^2)=0.                                        (3.1)
```

The branch `t=0` is the parity fixed curve.  On `t=0`, the Schur-complement
identity gives

```text
Phi(s,0) = unit * det(J_N).                             (3.2)
```

On the reversible parity chart the loaded equation is

```text
p^9 R6(v)=nu.
```

Its derivative with respect to `p` is a unit, so `v-v0` is a valid local
coordinate on the fixed curve.  Equation (2.3), squarefreeness of `Q12`, and
the unit-factor gcd checks imply

```text
d Phi/ds (0,0) != 0.                                   (3.3)
```

Applying the formal implicit-function theorem once more to `Phi=0` produces
a unique solution

```text
s=psi(t^2).
```

Hence (3.1) has two reduced smooth formal curve components with distinct
tangent directions:

```text
parity:      t=0,
non-parity:  Phi(s,t^2)=0.                              (3.4)
```

This conclusion does not require the cubic coefficient of `Phi`; the simple
motion of the normal eigenvalue along the fixed curve is already decisive.

## 4. What this does and does not establish

The `Q12` divisor is not a nilpotent-only rank accident.  Every loaded `Q12`
contact point lies on a second smooth non-parity formal component of the
seven-row constant-invariant fibre.  Thus a global loaded-fibre analysis must
retain this component; generic parity trapping cannot close the leaf.

This is **not** an algebraic or rational Keller trajectory.  The following
remain mandatory:

- expand or normalize the new component and pull back `r8`;
- impose `9*r8'=j/u` together with Kummer descent;
- reconstruct Taylor, simplicity, and coprimality boundaries in the original
  polynomial pair;
- classify components disjoint from parity.

There is no all-`(9,12)`, maximum-degree-twelve, counterexample, or
Jacobian-conjecture conclusion.

## 5. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q12_formal_branch_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.json -
```

The stdlib replay pins all dependencies, reconstructs and fingerprints all
eight original rows, checks their involution characters, recomputes (2.3),
and certifies both unit minors and every gcd used above.
