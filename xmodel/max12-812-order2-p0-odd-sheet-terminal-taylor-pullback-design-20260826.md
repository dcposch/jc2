# `(8,12)` order two: terminal and finite-Taylor receivers on the `p=0` odd sheet

Date: 2026-08-26

Status: **FAIL-CLOSED RECEIVER DESIGN.  THE INFINITY TERMINAL ROW MAY BE
COMPILED DIRECTLY.  THE TWO FINITE-BRANCH TAYLOR CLIENTS ARE SOURCE-TYPED
ONLY UNTIL GATE A BELOW IS PROVED.  NO LIFT OR ORDER-TWO VERDICT.**

## 0. Frozen predecessor and notation

The predecessor is the correction-aware odd collision chart on
`D(b*k0)`, with `b=cs0`,

```text
e0=a0=ell1=0,
12*e1^2-5*k0*b^4=0,

F=(3/8)*(a1*ee0+aa0*e1)-(3/8)*b*a1^2
  +(15/256)*k0*b*rs1^2-(5/16)*k0*ell2*b^3=0.       (0.1)
```

Use `w` for the rational sheet coordinate, reserving `u_x` for the
quadratic source root:

```text
w=e1/b^2,       k0=(12/5)*w^2,       b*w != 0.       (0.2)
```

The involution over fixed `(b,k0)` is `w -> -w`.  The order-two source deck
acts on ordinary coefficients by `z -> -z`; on the displayed odd cone it
acts diagonally on the odd coefficient coordinates, in particular

```text
b -> -b,       e1 -> -e1,       a1 -> -a1.          (0.3)
```

Thus (0.2)'s sheet involution and (0.3)'s source deck are not silently
identified.  Their diagonal and product actions, and the root-separation
deck `rho1 -> -rho1`, must all be recorded on overlaps.

## 1. Gate A: sheet-to-global algebraization

For the terminal profile `[6,2]`, normalize

```text
v=x^3*(x-1),       u_x^2=v,
T=u_x/x^2,         T^2=(x-1)/x.                     (1.1)
```

Let `A_i(x)` (`0<=i<=6`) and `R0(x)` be invariant rational functions and
put

```text
a_i=T^(i mod 2)*A_i(x).                              (1.2)
```

At coefficient infinity use `tau=T-1`.  The exact strict chart has
`Lambda=tau^3*varrho`; the odd collision chart has `Lambda=sigma^2`.
Consequently a global pullback of the odd sheet requires, at minimum, a
normal toric overlap carrying

```text
sigma^2=tau^3*varrho                                (1.3)
```

together with rational functions (1.2) whose strict-infinity principal
parts equal the complete odd source series, whose deck actions agree, and
for which the raw predecessor row `F` remains zero.  Call this collection
of two-sided maps and principal-part identities **Gate A**.

The local sheet (0.1)--(0.2) alone does not determine the global functions
`A_i,R0`, nor their germs at `x=0,1`.  Therefore no finite-branch symbol may
be replaced by `b,w,a1,aa0,rs1,ell2,...` until Gate A passes.  An injective
map in only one direction, a numerical interpolation, or equality after a
radical/projection is not Gate A.

## 2. Direct terminal-infinity pullback

Gate A is not needed to continue the same complete infinity source.  Write
the normalized odd series exactly as

```text
p=sigma^2*(2*ell2+2*sigma*ell3+...),
c=sigma^2*(b+sigma*cs1+...),
r=(p^2+sigma^2*(sigma*rs1+sigma^2*rs2+...))/4,

A=a1*z+sigma*(aa1*z+aa0)+...,
C=(sigma*b^2*w*z+sigma^2*(ee1*z+ee0)+...)/2,

K=z^4+p*z^2+c*z+r,
N=sigma^3*((z^2+p/2)*A+C),
f=K^2+sigma^2*N.                                    (2.1)
```

Every omitted coefficient in (2.1) is an independent correction, not zero.
Likewise retain complete arcs in all loads.  With the exact frozen ordinary
tails, form

```text
Phi_l = r_l(f,
              sigma^4*k10(sigma),
              sigma^12*k6(sigma),
              sigma^20*k2(sigma))
        -sigma^(2*(12+l))*delta_l(sigma),            (2.2)

(delta_1,...,delta_7)
  =(0,mu2,0,mu4,0,mu6,J/4).
```

The terminal client keeps (0.1) raw and extracts every coefficient

```text
E_(l,d)=[sigma^d]Phi_l,       1<=l<=7, 13<=d<=38.   (2.3)
```

No grade in (2.3) is solved before the later grades are formed.  The exact
typing sentinels are

```text
partial E_(l,d)/partial J0=0             (d<38),
partial E_(7,38)/partial J0=-1/4,
partial E_(l,38)/partial J0=0            (l!=7),     (2.4)
```

with analogous first-target checks for `mu2_0,mu4_0,mu6_0` at grades
`28,32,36`.  All `k10,k6,k2` coefficients licensed by their exact shifts
remain in the ring.  A first unit after localization by `b*w` excludes this
odd infinity cone; a nonunit is only a deeper raw receiver.  Merely seeing
the terminal variable with (2.4) is a typing result, not an exclusion.

## 3. Universal invariant Taylor formulas

The two finite clients are the normalized branches `x=0` and `x=1`; each
client retains both coordinate families

```text
P_l=u_x^l/l! * partial_z^l f(u_x*R0),  0<=l<=8,
Q_l=u_x^l/l! * partial_z^l g(u_x*R0),  0<=l<=12.    (3.1)
```

There is a cheap exact way to emit (3.1) without choosing square roots.  If
a monomial in the coefficient of `z^s` of `f` or of the fully loaded

```text
g=F12(f)+k10*F10(f)+k6*F6(f)+k2*F2(f)
```

is

```text
c * product_i(a_i^e_i) * product_j(k_j^m_j),
O=sum_(i odd)e_i,
```

then equivariance gives `s+O` even.  After (1.1)--(1.2), its contribution
to the `l`-th Taylor coordinate is exactly

```text
c*binom(s,l)
 *x^((3*s-O)/2)*(x-1)^((s+O)/2)
 *product_i(A_i^e_i)*product_j(k_j^m_j)*R0^(s-l).   (3.2)
```

Terms with `s<l` are absent.  Formula (3.2) is invariant and lies in
`Q(x)[A_i,R0,k10,k6,k2]`; negative powers of `x` are retained rather than
cleared by an unlicensed localization.

The `x=0` client substitutes

```text
x=s0^2,     u_x=s0^3*eta0,     eta0^2=s0^2-1,       (3.3)
```

and the `x=1` client substitutes

```text
x=1+s1^2,  u_x=s1*eta1,        eta1^2=(1+s1^2)^3.  (3.4)
```

Both emit all terms of all twenty-two coordinates in (3.1), check the
parity and Faber weights term by term, and record the depression bounds

```text
ord_x(R0)>=-12 at x=0,       ord_(x-1)(R0)>=-4 at x=1. (3.5)
```

Actual regularity is imposed only after Gate A supplies Laurent germs for
every `A_i` and for `R0`.  Before then the accepted endpoint is exactly
`TYPED_WAITING_GATE_A`; `PASS_TAYLOR`, `UNIT`, `LIFT`, and `EMPTY` are
forbidden output strings.

## 4. Parallel AWS clients and stop rules

Launch three independent, capped clients as soon as the exact grades eleven
and twelve source has passed:

1. exact `Q` terminal extraction (2.2)--(2.4), retaining (0.1), every
   correction through the terminal grade, and every load;
2. exact `Q` `x=0` Taylor emitter (3.2)--(3.3); and
3. an independent good-prime `x=1` Taylor emitter (3.2)--(3.4), with exact-Q
   replay required before any characteristic-zero use.

The terminal client stops positively at a source identity, a localized raw
unit, or a frozen deeper component.  It stops negatively on timeout,
coefficient-extractor failure, missing correction/load, or any target at a
wrong grade.  Each Taylor client stops at its typed manifest until Gate A is
proved, even if every universal parity check passes.

## 5. Explicit nonclaims

This design does not prove Gate A, algebraize the odd sheet, solve the raw
terminal ideal, impose either finite Taylor family on an actual global
section, or establish a lift.  It does not cover the other `p=0` cusp, the
positive-order-load fan, fractional slopes, or omitted infinity supports.
It does not close the square component, order two, `(8,12)`, maximum twelve,
or JC2.
