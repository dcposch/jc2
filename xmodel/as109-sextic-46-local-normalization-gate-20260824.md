# AS109 sextic `(4,6)` local-normalization gate

**Verdict: `CONDITIONAL EXACT CLOSURE OF THE FROZEN NORMAL-FORM
SYSTEM`.**

- Frozen at: `2026-08-24T11:29:17Z`
- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Parent producer: `xmodel/as109-sextic-survivor-discriminator-20260824.md`
  (`b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552`)
- Parent status consumed here: **PROVISIONAL**
- Field: characteristic zero; constants algebraically closed after harmless
  scalar extension
- Method: exact weighted Newton/Puiseux valuation, both boundary equations,
  coefficient-curve normalization, and the last-row form
- Generic support search, exponent rectangle, AWS: none
- AS109 lift, characteristic-zero counterexample, or JC2 inference: none

Under the exact normal-form equations frozen by the parent, there is no
trajectory with nonzero constant Jacobian.  Every branch over the unique
weighted-infinity point is accounted for.  The mismatch branch `L!=0` has
no formal branch at all.  In the aligned branch, the first Newton face kills
`beta!=0` and then `delta!=0`; `beta=delta=0` reduces to a finite component
split.  Its last nonlinear component is eliminated by one monic quartic
which genuinely uses both polynomial boundary equations.  Once finite
poles are excluded, the pullback of `eta` on every possible polynomial
branch has positive degree, or vanishes, and hence cannot be a nonzero
constant.

This is deliberately a conditional closure.  It does not promote the
parent derivation before review.  If that derivation is confirmed, this
artifact closes the genuine `(4,6)` pattern; the `(5,6)` branch remains
outside this gate.

## 1. Exact hypotheses

The sole mathematical dependency is the following system from the frozen
parent.  The working field is `Kbar(x)` in the square branch, or the single
prescribed quadratic extension `Kbar(x)(h)`, `h^2=H`, in the aligned
nonsquare branch; no arbitrary algebraic extension is allowed.  Let

```text
f=z^4+A z^2+B z+C,
g=z^6+L z^5+P z^4+Q_3 z^3+R z^2+S z+T,
```

where `L` is constant, the upper Jacobian rows have already been integrated,
and put `U=A^2-4C`.  The two coefficient-curve equations are

```text
J2 = 5L A^3/32+3 beta A^2/8-5L A U/16+delta A
     +5L B^2/8-3B U/4+2 gamma B-3 beta U/4 = k2,       (1.1)

J1 = -5L A^2B/32-3A B^2/4-3 beta A B/4-5L B U/16
     +delta B+3U^2/32-gamma U/2 = k1.                 (1.2)
```

Writing `z=h y+r`, `q=r^2+A/2`, `D=f(x,0)`, and
`E=g(x,0)-alpha D-epsilon`, both polynomial boundary equations are

```text
D = rB+q^2-U/4,                                        (1.3)

E = 3Lr^5/8-5Lr^3q/4-beta r^3/2+5Lr^2B/8
    +15Lrq^2/8+3rqB/2+3 beta rq/2-5LrU/16+delta r
    +q^3+5LqB/8-3qU/8+gamma q+3B^2/8+3 beta B/4.      (1.4)
```

The constant row is

```text
h eta(A',B',U') = jbar != 0,                           (1.5)
```

where

```text
eta_A = 15L A^3/64-5L B^2/16-5L A U/32+3 beta A^2/8
        +3B U/16-gamma B/2+delta A/2,
eta_B = -5L A B/16-3B^2/4-3 beta B/4,
eta_U = -15L A^2/128+5L U/64-3 beta A/16-delta/4.      (1.6)
```

No existence statement is imported with these equations.

The polynomial-origin data used below are also part of the hypothesis:
`H,D,E` lie in `Kbar[x]`; in the square/mismatch branch `h,r,A,B,U` are
rational over `Kbar(x)` before integrality; and in the nonsquare aligned
branch the quadratic involution sends

```text
h -> -h,       r -> -r,       B -> -B,
A -> A,        U -> U,        q -> q.                  (1.7)
```

These are exactly the descent parities supplied by the common depression,
not an inference from the finite boundary system alone.

## 2. The complete local chart

Let a finite place of the base be fixed.  If any of `r,q,B,U` has a pole,
the unique weighted-infinity calculation from the parent, rechecked by the
replay, puts the branch over

```text
[r:q:B:U]=[1:0:0:0],        weights (1,2,3,4).         (2.1)
```

For completeness, the four highest weighted forms are

```text
rB+q^2-U/4,
q^3+3rqB/2-3qU/8+3B^2/8,
-3BU/4,
3r^2B^2/2-3qB^2/2+3U^2/32.
```

If `B=0`, the last and first forms force `U=q=0`.  If `U=0` and
`B!=0`, the last and first forms force `q=r^2`, `B=-r^3`; the second
then equals `-r^6/8`, so it is not zero.  This re-proves uniqueness of
(2.1), independently of the parent's prose.

Use the chart

```text
r=s^-1,       q=Q s^-2,       B=Y s^-3,       U=Z s^-4. (2.2)
```

Here `v(s)>0`, and `Q,Y,Z` have positive valuation.  The functions
`d=D(x)` and `e=E(x)` are regular at the chosen finite base place.  After
clearing weights `4,6,7,8`, respectively, the four exact equations are

```text
Fh = Y+Q^2-Z/4-d s^4,                                  (2.3)

Gh = 3Ls/8-5LQs/4-beta s^3/2+5LYs/8+15LQ^2s/8
     +3QY/2+3 beta Qs^3/2-5LZs/16+delta s^5+Q^3
     +5LQYs/8-3QZ/8+gamma Qs^4+3Y^2/8
     +3 beta Ys^3/4-e s^6,                             (2.4)

J2h = -5Ls/4+15LQs/4+3 beta s^3/2-15LQ^2s/4
      -3 beta Qs^3+5LZs/8-2 delta s^5+5LQ^3s/4
      +3 beta Q^2s^3/2-5LQZs/8+2 delta Qs^5
      +5LY^2s/8-3YZ/4+2 gamma Ys^4
      -3 beta Zs^3/4-k2 s^7,                           (2.5)

J1h = -5LYs/8+5LQYs/4+3Y^2/2+3 beta Ys^3/2
      -5LQ^2Ys/8-3QY^2/2-3 beta QYs^3/2
      -5LYZs/16+delta Ys^5+3Z^2/32
      -gamma Zs^4/2-k1 s^8.                            (2.6)
```

These are not a truncated model.  They are the full boundary cover and both
full first integrals in the local chart.

## 3. Mismatch `L!=0`: no Puiseux branch

Normalize the valuation by `v(s)=1` and write

```text
a=v(Q)>0,        b=v(Y)>0,        c=v(Z)>0.             (3.1)
```

In (2.5), the term `-5Ls/4` has order one.  Every other term has order
strictly greater than one except `-3YZ/4`; hence

```text
b+c=1,                  y0 z0=-5L/3.                   (3.2)
```

In (2.6), after (3.2), the only possible lowest terms are `3Y^2/2` and
`3Z^2/32`.  If `b<c` the first is unique; if `c<b` the second is unique.
Therefore

```text
b=c=1/2.                                                (3.3)
```

Equation (2.3) now forces `a=1/4`: `2a<1/2` would make `Q^2` unique,
while `2a>1/2` gives `z0=4y0`, which makes the leading part of (2.6)
equal to `3y0^2`, not zero.

At orders `1/2` and `3/4`, (2.3)--(2.4) give

```text
y0+q0^2-z0/4=0,
q0(q0^2+3y0/2-3z0/8)=0.                               (3.4)
```

Here `q0!=0`.  The difference of the parenthesized expression and the first
one is `(4y0-z0)/8`; hence `z0=4y0`, and the first equation then gives
`q0^2=0`, a contradiction.  Thus

```text
L!=0:       no branch above (2.1).                     (3.5)
```

This exhausts fractional valuations; it does not assume integral powers of
`s`.

## 4. Aligned `L=0`: the Newton strata

Eliminate `Z=4(Y+Q^2-ds^4)` using (2.3).  Multiplying the remaining three
equations by harmless nonzero scalars gives

```text
G0 = 4Q^3-3Y^2+4 beta s^3-12 beta Qs^3-6 beta Ys^3
     -(8 gamma+12d)Qs^4-8 delta s^5+8e s^6,            (4.1)

H2 = -6Q^2Y-6Y^2+3 beta s^3-6 beta Qs^3
     -3 beta Q^2s^3-6 beta Ys^3+(4 gamma+6d)Ys^4
     -4 delta s^5+4 delta Qs^5+(6 beta d-2k2)s^7,      (4.2)

H1 = 3Q^4+6Q^2Y-3QY^2+6Y^2+3 beta Ys^3
     -3 beta QYs^3-(4 gamma+6d)Q^2s^4
     -(4 gamma+6d)Ys^4+2 delta Ys^5
     +(4 gamma d+3d^2-2k1)s^8.                         (4.3)
```

Let `a=v(Q), b=v(Y)>0`, allowing either value to be infinity when that
series is identically zero.

### 4.1 `beta!=0`

The lowest candidates in `(G0,H2,H1)` are

```text
(3a,2b,3),       (2a+b,2b,3),
(4a,2a+b,a+2b,2b).                                     (4.4)
```

The first triple can tie only in the following exhaustive ways:

| leading relation in `G0` | consequence |
|---|---|
| `b=3a/2`, `a<1` | `2b` is unique in `H2` |
| `a=1`, `b>3/2` | the order-three term is unique in `H2` |
| `b=3/2`, `a>1` | `2b` is unique in `H1` |
| `a=1`, `b=3/2` | `2b` is unique in `H1` |

The cases `Q=0` or `Y=0` give the same unique-term obstruction directly.
There is no branch.

### 4.2 `beta=0`, `delta!=0`

The lowest candidates in `G0` are `3a,2b,4+a,5`; those in `H2` are
`2a+b,2b,4+b,5`.  A tie can only occur at

```text
b=3a/2 with a<=5/3,       a=5/3,       or b=5/2.       (4.5)
```

Before an endpoint, `2b` is unique in `H2`; at every endpoint it is unique
in `H1`.  A putative tie with the `s^4Q` term would require simultaneously
`a>=2` and `a<=1`.  Again `Q=0` or `Y=0` is immediate.  There is no branch.

Consequently every aligned branch must satisfy

```text
beta=delta=0.                                           (4.6)
```

## 5. The last aligned stratum

Put

```text
V=U-8 gamma/3.                                          (5.1)
```

The coefficient curve becomes exactly

```text
B V = -4k2/3,
V^2 = 8A B^2 + (32/3)(k1+2 gamma^2/3).                 (5.2)
```

### 5.1 `k2!=0`: both boundaries reject the branch

Suppose `v(r)=-n<0`, and put `b=v(B)`.  The first equation in (5.2) gives
`v(V)=-b`; the second, together with `A/r^2 -> -2`, forces

```text
b=n/2.                                                  (5.3)
```

Write the leading coefficients of `rB,V,q` as `w0,v0,q0`.  From the first
boundary, `v(q)>=-n/4`.  If the inequality is strict, it gives `v0=4w0`,
whereas (5.2) gives `v0^2=-16w0^2`, impossible.  At equality, the first and
second boundaries give

```text
w0+q0^2-v0/4=0,
q0(q0^2+3w0/2-3v0/8)=0.                               (5.4)
```

Since `q0!=0`, subtracting the two parenthesized relations gives
`v0=4w0`, then `q0^2=0`.  Thus this stratum also has no branch.

### 5.2 `k2=0`: exact component split

In the function field of an irreducible branch, `BV=0`, so either `B=0`
or `V=0` identically.

If `B=0`, (1.6) restricts to `eta=0`, contradicting (1.5).

If `V=0`, write

```text
theta=A B^2
      =-(4/3)(k1+2 gamma^2/3).                         (5.5)
```

When `theta=0`, the components are `B=0` and `A=0`.  The first is already
dead.  On `A=0`, both boundaries eliminate `B` to

```text
r^8-6 P r^4+8E r^2-3P^2=0,
P=D+2 gamma/3.                                         (5.6)
```

This is monic, and the second boundary is monic quadratic in `B` after a
nonzero scalar normalization.  Hence `r` and `B` are integral.

When `theta!=0`, set

```text
K=B^2,          w=rB,          P=D+2 gamma/3.           (5.7)
```

The two boundaries are exactly

```text
w=P-q^2,
E=-q^3/2+3Pq/2+3K/8,          w^2=qK-theta/2.          (5.8)
```

Eliminating `K,w` gives the monic quartic

```text
q^4-6Pq^2+8Eq-3P^2-3 theta/2=0.                       (5.9)
```

Thus `q` and `K` are integral.  On all `V=0` components,

```text
eta=-(3/4)B^2 dB.                                      (5.10)
```

If `h` lies in the base field, `h` and `B` are polynomials after
integrality; (1.5) is a product of polynomials, so `B` would be a unit and
then `B'=0`, a contradiction.

If `h` is genuinely quadratic, conjugation sends `h,r,B` to their negatives
and fixes `A,U,q`.  Then

```text
K=B^2 in Kbar[x],          M=hB in Kbar[x],
M^2=H K,                   h eta=-(3/8)M K'.            (5.11)
```

The nonzero constant equation makes `M` and `K'` units.  Since `M^2=HK`,
both `H` and `K` are units, so `K'=0`, again a contradiction.  The same
argument includes the `A=0` line after (5.6).

This finishes every finite Puiseux branch over (2.1).

## 6. Why finite-pole integrality is enough here

It remains necessary to rule out polynomial trajectories; integrality alone
does not do so.

For `L!=0`, the parent's leading UFD relation makes `h` a polynomial in the
base field.  Since (2.1) is the only weighted-infinity point and Section 3
finds no branch over it, `r,q,B,U,A` are polynomials.  Therefore `eta` is a
polynomial and (1.5) would make both `h` and the pullback of `eta` nonzero
constants.

For `L=0`, if `h` is genuinely quadratic, parity under `z -> -z` forces

```text
beta=0             from Q_3=3B/2+beta,
delta=0            from the z coefficient S,
k2=0               from BV=-4k2/3.                    (6.1)
```

Those are precisely the components closed in Section 5.  In every other
aligned stratum, `h` lies in the base field, so absence of finite poles again
makes all coefficient functions polynomials.

### 6.1 Polynomial branches for `L!=0`

Let lower-case letters denote positive degrees of nonconstant `A,B,U`.
The top-degree supports of `(J2,J1)` are

```text
max(3a,a+u,2b,b+u),
max(2a+b,a+2b,b+u,2u).                                 (6.2)
```

The finite cone split is:

| nonconstant entries | only possible degrees | pullback of `eta` |
|---|---:|---:|
| `A,B,U` | `(4n,5n,7n)` | degree `16n-1` |
| `B,U`, with `A` constant | `(n,n)` | degree `3n-1` |
| any other proper subset | impossible by a unique top monomial | -- |

For the zero/constant cases explicitly: if `A` is nonconstant and `B` is
constant, cancellation of `A^3` in `J2` requires a nonconstant `U`, after
which `U^2` is unique in `J1`; if `U` is constant, `J2` forces
`3a=2b` and `AB^2` is then unique in `J1`.  With `A` constant, a lone
nonconstant `B` leaves `B^2` unique and a lone nonconstant `U` leaves
`U^2` unique.  If both vary, `J2` forces equal degrees, giving the second
row.  Thus the table includes identically zero leading coefficients as well
as nonzero constants.

For the first row, the leading invariant equations are

```text
5L a0^3=24 b0 u0,             u0^2=8a0 b0^2.          (6.3)
```

The unique degree-`16n-1` contribution is `eta_A A'`, whose coefficient is

```text
15L a0^3/64+3b0u0/16 = 35L a0^3/128 !=0.              (6.4)
```

For the second row, `-3B^2B'/4` is the unique degree-`3n-1` term.  Thus the
pullback cannot be constant.  Constant `A,B,U` give `eta=0`.

### 6.2 Polynomial branches for `L=0`

Use `X=B+beta`, `V=U-8 gamma/3`.  If `beta!=0` and `A` is nonconstant,
the two shifted curve equations force

```text
(deg A,deg X,deg V)=(4n,3n,5n).                        (6.5)
```

The unique top term of `eta` has degree `12n-1`, with coefficient

```text
3X0V0/16+3 beta A0^2/8 = 15 beta A0^2/32 !=0.          (6.6)
```

If `beta=0`, `delta!=0`, the degrees are

```text
(deg A,deg X,deg V)=(4n,n,3n),                         (6.7)
```

and the unique degree-`8n-1` coefficient is

```text
3X0V0/16+delta A0/2 = 3 delta A0/4 !=0.                (6.8)
```

If `A` is constant, the shifted equations make `X,V` constant except for
the specialization `A=V=delta=0`; there
`eta=-3X(X-beta)dX/4`, of degree `3 deg(X)-1`, never zero-degree nonzero.

Finally, `beta=delta=0` gives `XV=constant`.  A nonzero constant makes
`X,V`, then `A`, constant.  The zero-product components are exactly those
of Section 5; their pullback is zero or has degree `3 deg(B)-1`.

Hence no polynomial coefficient trajectory satisfies (1.5).

## 7. Exact conclusion and scope

Combining Sections 3--6 gives the exact conditional statement:

> Every solution of the frozen `(4,6)` normal-form equations (1.1)--(1.6)
> over a characteristic-zero polynomial base has zero last row or violates
> at least one of the two polynomial boundary equations.  In particular,
> none has nonzero constant Jacobian.

The resurrection condition is correspondingly narrow: an error must be
found in the provisional parent reduction to (1.1)--(1.6), in the stated
quadratic parity descent, or in the uniqueness of the weighted-infinity
point.  There is no surviving local branch of the exact system to search.

This does **not** prove the full `y`-degree-at-most-six theorem: the genuine
`(5,6)` system is untouched.  It does not raise an AS109 degree floor unless
the complete low-degree chain and its reviews are separately promoted.  It
does not construct or exclude an AS109 lift outside the displayed normal
form and makes no JC2 inference.

## 8. Deterministic replay

Run

```text
Singular -q cases/as109_sextic_46_local_normalization_20260824/verify_46_local_normalization.sing
```

Expected output:

```text
PASS-SEXTIC-46-LOCAL-NORMALIZATION
mismatch_finite_pole_branches=0
aligned_finite_pole_survivors=0
polynomial_eta_trajectories=0
as109_inference=false
jc2_inference=false
```

The replay verifies the full weighted chart from (1.1)--(1.4), the exact
aligned elimination (4.1)--(4.3), both leading-face contradictions, the
shifted curve, the monic quartic (5.9), the restricted `eta`, and all three
nonzero leading coefficients used in Section 6.

Replay environment: `Singular 4.4.1`, arm64 Darwin.  Frozen replay hash:

```text
a705526c12675d7fba0330f9f45d17db34d87a085f877b30bc6d73de81a7e404
```

Frozen inputs, used only under the dependency labels stated above:

| artifact | SHA-256 | status |
|---|---|---|
| `xmodel/as109-sextic-survivor-discriminator-20260824.md` | `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552` | provisional parent |
| `cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing` | `d2c29ef530f7bd3aa511d245db2f9fb6eb72cfb001f5dc14d92b74c16345723f` | parent replay |
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | grandparent scope |

Artifact hashes are frozen in
`cases/as109_sextic_46_local_normalization_20260824/FREEZE.sha256`.
No parent, review, canonical file, ledger, or AWS resource was edited.
