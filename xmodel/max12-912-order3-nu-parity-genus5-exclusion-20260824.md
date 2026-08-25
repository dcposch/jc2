# `(9,12)` order-three `nu!=0` parity genus-five exclusion

Date: `2026-08-24`  
Status: **PRODUCER-EXACT / HOSTILE DIFFERENT-MODEL REVIEW REQUIRED**  
Verdict: no actual `nu!=0` order-three Keller trajectory lies on the full
odd/even specialization `q=x0=x2=x4=k=0`.

## 1. Exact parity fibre and branch partition

Use approximate-cubic coordinates

```text
K=z^3+pz+q,
f=K^3+sum_(i=0)^5 x_i z^i.
```

On

```text
q=x0=x2=x4=k=0,                                        (1.1)
```

`f` is odd and its Faber polynomial `g` is even. Thus

```text
r1=r3=r5=r7=0                                          (1.2)
```

identically, and the loaded fibre is

```text
r2=r4=0,       r6=nu in C*,       r8'=j/(9u).           (1.3)
```

This report exhausts (1.1), not the full `nu`-loaded coefficient fibre.

The frozen `x5=0` calculation gives

```text
x1=p*x3,       r6=-(4/81)*x3^3=nu,       r8=0,
```

which contradicts the terminal row. Hence retain `x5!=0` as an identity in
the function field.

Put

```text
A=x3-2*p*x5.
```

On `A=0`, the exact row `r2` is `-(4/81)*p*x5^3`. Its two branches force
`nu=0`, so `A!=0` on (1.3). It remains to split `p=0` and `p!=0`.

## 2. The `p=0` boundary

Suppose `p=0` and `x5!=0`. The exact rows successively give

```text
x1=x5^2/3,
x3^2=-x5^3/36,
nu=-(11/729)*x3*x5^3,
r8=-x5^5/486.                                          (2.1)
```

Eliminating `x3,x5` yields

```text
r8^9=(2*3^25/11^10)*nu^10.                             (2.2)
```

The right side is a nonzero element of the algebraically closed constant
field. Therefore `r8` is differential-constant, contradicting (1.3). The
entire `p=0` parity branch is empty for actual trajectories.

## 3. Rationalization on `p*x5*A!=0`

Now suppose `p*x5*A!=0` and define the weight-zero quotient

```text
v=A/(p*x5).                                             (3.1)
```

The order-three character weights are

```text
wt(p)=2,  wt(x5)=4,  wt(x3)=6 mod 3,
```

so `v` is Galois-invariant and belongs to `K=C(x)`.

Since `x3=p*x5*(v+2)`, the row `r2=0` solves reversibly as

```text
x1=x5*p^2*(v+1)+x5^2*(3v+1)/(9v).                      (3.2)
```

Substitution into `r4=0` gives

```text
(3v^2-2)*x5+36*p^2*v^2*(3v^2+3v+1)=0.                 (3.3)
```

The factors `3v^2-2` and `3v^2+3v+1` are coprime; their resultant is `27`.
If the first were the zero element of `K`, (3.3) would be impossible. If the
second were the zero element, (3.3) would force the already-excluded
`x5=0`. Thus every division below is reversible in the function field. The
factors may of course vanish at individual places; those places are retained
in the divisor/genus calculation.

Solving (3.3) gives

```text
x5=-36*p^2*v^2*(3v^2+3v+1)/(3v^2-2).                  (3.4)
```

Exact substitution into the next two tail rows yields

```text
r6=p^9*R6(v),

R6(v)= -2304*v^6*(3v^2+3v+1)^3
        *(33v^5+117v^4+131v^3+69v^2+18v+2)
        /(3v^2-2)^4,                                   (3.5)

r8=p^10*R8(v),

R8(v)= 6912*v^8*(3v^2+3v+1)^4
        *(54v^4+96v^3+75v^2+32v+6)
        /(3v^2-2)^5.                                   (3.6)
```

The portable replay reconstructs (3.2)--(3.6) from the pinned exact Faber
compiler over `Q`; no modular or numerical solve is used.

## 4. The genus-five Kummer curve

Because `p` has order-three character two,

```text
p=u^2*P,             P in K.
```

Consequently

```text
p^9=(h^2*P^3)^3
```

is a cube in `K`. Since `nu` is a nonzero constant and hence also a cube,
the equation `p^9 R6(v)=nu` makes `R6(v)` a cube in `K`.

Remove the displayed cube factors from (3.5). There is a `Y in K` satisfying

```text
Y^3=A5(v)/D(v),                                        (4.1)

A5(v)=33v^5+117v^4+131v^3+69v^2+18v+2,
D(v)=3v^2-2.
```

The exact gcd/resultant checks are

```text
gcd(A5,A5')=1,       gcd(D,D')=1,
gcd(A5,D)=1,         Res(A5,D)=97200.                   (4.2)
```

Over the algebraically closed constant field, `A5` therefore has five simple
roots and `D` has two simple disjoint roots. These seven finite points have
ramification index three in (4.1). At infinity, `A5/D` has pole order three,
so infinity is unramified. Riemann--Hurwitz gives

```text
2*g-2=3*(-2)+7*(3-1)=8,
g=5.                                                    (4.3)
```

If `v` were nonconstant, `(v,Y)` would define a nonconstant morphism from
`P1_x` to the smooth projective genus-five curve (4.1), impossible by
Riemann--Hurwitz. Thus `v` is constant.

Equation (3.5) now makes `p^9` constant, hence `p` is constant in the
function field `L`. Equation (3.6) then makes `r8` constant. This again
contradicts `9*r8'=j/u!=0`.

## 5. Exhaustion and scope

The parity branch tree is now complete:

| branch | exact outcome |
|---|---|
| `x5=0` | `r8=0`, terminal contradiction |
| `x5!=0`, `A=0` | forces `nu=0` |
| `x5*A!=0`, `p=0` | (2.2), so `r8` is constant |
| `p*x5*A!=0` | genus-five obstruction, then `r8` constant |

**Producer conclusion.** No actual `nu!=0` order-three Keller trajectory
lies on the full parity specialization (1.1).

**Not concluded:** parity exhaustion of the complete loaded fibre, exclusion
of a non-parity component, either Taylor-boundary family, the order-one core,
all `(9,12)`, maximum-twelve automorphy, a counterexample, or JC2.

## 6. Replay

Run:

```sh
python3 cases/max12_912_order3_nu_parity_genus5_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_genus5_20260824/replay.json -
```

The stdlib replay checks the exact generic rationalization, the `r6,r8`
factorizations, all gcd/resultant and genus ledgers, and the `p=0` tail
identities. It is regression for the written function-field proof, not a
substitute for the no-map argument.
