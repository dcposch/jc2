# First concrete `(8,12)` order-two strict-Rees client: `U=2`, profile `[6,2]`

Date: 2026-08-25  
Status: **EXACT SOURCE-TYPED CLIENT / AWS PREREGISTRATION DESIGN**

## Verdict and exact scope

Assume the provisional terminal divisor theorem

```text
xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md
```

at its exact stated scope.  The first order-two source profile not removed
by the terminal differential is, after an affine source normalization,

```text
h=x^6(x-1)^2,       v=x^3(x-1),       u^2=v,
T=u/x^2,            T^2=(x-1)/x.                       (0.1)
```

The normalized Kummer curve is rational:

```text
x=1/(1-T^2),       u=T/(1-T^2)^2.                     (0.2)
```

Its deck involution is `T->-T`.  Its two finite branch points are `x=0`
(`T=infinity`) and `x=1` (`T=0`); the two unramified coefficient-infinity
points are `T=1` and `T=-1`.  The terminal target is exactly

```text
r_7=(j/4)T.                                           (0.3)
```

After the reviewed target quotient, the full high-row polynomial is

```text
g=F_12(f)+k_10F_10(f)+k_6F_6(f)+k_2F_2(f),           (0.4)
```

and the exact seven-tail targets are

```text
(r_1,...,r_7)=(0,mu_2,0,mu_4,0,mu_6,(j/4)T).         (0.5)
```

All three lower Faber loads and all three constant tail loads are charged.
No mod-four filter is legal on this quadratic leaf.

At the selected infinity point `T=1`, put `tau=T-1`.  The exact strict-
Rees equations are displayed in Section 3.  Their **raw associated-graded
special fibre** is the ordinary unloaded seven-tail system, with reduced
support the common-quartic cone `f=K^2`, `g=K^3`.  The boundary of the
interior-saturated strict family may be a proper closed subset of that cone;
only the full saturation can decide accessibility.

This artifact source-types the first client.  It does not compute the
saturation, solve either finite Taylor boundary, or assert existence or
emptiness.

## 1. Global character descent on the rational Kummer curve

Write

```text
f=z^8+sum_(i=0)^6 a_i z^i,       z=u(y+R_0).          (1.1)
```

The deck involution sends `u,z,T` to their negatives.  Invariance of the
original first coordinate gives

```text
a_i=T^(i mod 2) A_i(x),       A_i in L(x).            (1.2)
```

For an ordinary Faber tail, equivariance gives

```text
r_ell=T^(ell mod 2) D_ell(x,A,k),                     (1.3)
```

where `D_ell` is invariant.  Equations (0.5) therefore descend exactly to

```text
(D_1,...,D_7)=(0,mu_2,0,mu_4,0,mu_6,j/4).            (1.4)
```

This is an isotrivial ordinary-tail fibre: all descended targets are
scalars, while the ordinary terminal target acquires precisely the unit
factor `T`.

The coefficient of `y^7` in the first Taylor coordinate is

```text
[y^7]P=8h^2R_0.                                      (1.5)
```

Thus `R_0` is invariant and rational.  Before the polynomial source shear,
its base pole orders are at most twelve at `x=0` and four at `x=1`; after
subtracting its polynomial part, it is regular at infinity.  No finite part
of `R_0` is set to zero in this client.

## 2. Both finite Taylor boundaries remain charged

For `0<=ell<=8` and `0<=ell<=12`, respectively, define

```text
P_ell(x)=u^ell/ell! * partial_z^ell f(uR_0),
Q_ell(x)=u^ell/ell! * partial_z^ell g(uR_0).          (2.1)
```

The exact original polynomiality conditions are

```text
P_ell in L[x]       (0<=ell<=8),
Q_ell in L[x]       (0<=ell<=12).                    (2.2)
```

Every expression in (2.1) is deck-invariant.  On the smooth normalization,
the two branch charts are:

```text
x=0: x=sigma_0^2,       ord_(sigma_0)(u)=3,
x=1: x-1=sigma_1^2,     ord_(sigma_1)(u)=1.          (2.3)
```

Therefore (2.2) retains, in particular, all conditions

```text
ord_(sigma_0)(P_ell),ord_(sigma_0)(Q_ell)>=0,
ord_(sigma_1)(P_ell),ord_(sigma_1)(Q_ell)>=0.         (2.4)
```

Conversely, because the functions are invariant and the only finite branch
or pole candidates of the fixed source are `0,1`, finite regularity plus
the infinity pole bound is exactly membership in `L[x]`.  A tail-only Rees
calculation is therefore an over-approximation until both complete families
(2.2) are imposed; neither branch point may be represented by a single
generic numerical value.

## 3. Exact ordinary strict-Rees chart at `T=1`

At coefficient infinity,

```text
q=1/x=1-T^2=-tau(2+tau),       T=1+tau.              (3.1)
```

The bounded-pole threshold is three because `U+1=3`.  For a strict branch,
write first `Lambda=q^3 rho`.  Since `-(2+tau)` is a unit, absorb its cube
into an invertible Rees coordinate and write exactly

```text
Lambda=tau^3 varrho.                                  (3.2)
```

Define the ordinary scaled coefficients

```text
C_i=(1+tau)^(i mod 2) B_i.                            (3.3)
```

Faber homogeneity assigns weights

```text
wt(B_i)=8-i,
wt(k_10)=2,       wt(k_6)=6,       wt(k_2)=10,
wt(r_ell)=12+ell.                                     (3.4)
```

Hence the exact seven equations are

```text
Psi_ell=
r_ell(C,
      tau^6 varrho^2 k_10,
      tau^18 varrho^6 k_6,
      tau^30 varrho^10 k_2)
-tau^(3(12+ell)) varrho^(12+ell) gamma_ell(tau)=0,   (3.5)
```

where

```text
gamma_1=gamma_3=gamma_5=0,
gamma_2=mu_2,       gamma_4=mu_4,       gamma_6=mu_6,
gamma_7=(j/4)(1+tau).                                (3.6)
```

Every exponent in (3.5) follows from the original weight, including the
terminal exponent `57` and its nonconstant unit `(1+tau)`.  The other
infinity point `T=-1` is obtained by the deck involution and gives a
unit-equivalent chart; it is not a new independent source component.

Let

```text
I=(Psi_1,...,Psi_7),
K=I:(tau varrho)^infinity,
H=(K+(tau,varrho)):(B_0,...,B_6)^infinity.           (3.7)
```

The unit-ideal result `H=(1)` would exclude every strict formal/Puiseux arc
for this fixed tail fibre, hence every rational strict tail trajectory.
It would still not discharge (2.2).  A nonunit `H` gives only an accessible
algebraic boundary support, not a rational trajectory.

## 4. Raw associated-graded support and required charts

At `tau=varrho=0`, all lower Faber loads and target loads in (3.5) vanish,
and `C_i=B_i`.  The raw special-fibre equations are exactly

```text
r_1(B,F_12(B))=...=r_7(B,F_12(B))=0.                 (4.1)
```

By the confirmed Faber--Mason theorem, their reduced support is

```text
K=z^4+pz^2+cz+r,       f=K^2,       g=K^3,           (4.2)
```

with

```text
B_6=2p,       B_5=2c,       B_4=p^2+2r,
B_3=2pc,      B_2=c^2+2pr,  B_1=2cr,       B_0=r^2. (4.3)
```

The reduced projective support is `P(2,3,4)`.  A fail-closed saturation
must form (3.7) before restricting to the three standard charts `p!=0`,
`c!=0`, `r!=0`; saturating by `pcr` loses all coordinate boundaries.  The
four normal coordinates transverse to (4.3) must remain in the deformation
ideal.

The raw support (4.2) need not equal the support of `H`: saturation can add
initial equations and remove inaccessible points.  No scheme-reducedness or
lifting assertion is made.

## 5. AWS-only compiler and controls

The first compiler must:

1. reconstruct `F_12,F_10,F_6,F_2` and the ordinary tails `r_1,...,r_7`
   independently of every `(9,12)` source;
2. verify tail weights `13,...,19` and the twists (1.2)--(1.3);
3. emit (3.5) with all seven scalar load symbols retained in the polynomial
   ring (`k_10,k_6,k_2,mu_2,mu_4,mu_6,j`);
4. recover (4.3) as the raw boundary radical before interpreting any
   saturation;
5. verify saturation by `tau` followed by `varrho` agrees with saturation by
   their product, and that a `varrho`-unit slope-three control is absent from
   the strict boundary;
6. cover the `p`, `c`, and `r` charts only after interior saturation;
7. keep the two complete Taylor families (2.2) in the manifest as charged
   successor gates.

All generator, Singular, Sage, msolve, and substantive exact-Python runs are
AWS-only.  Every launch must record host, remote job directory, PID, input
hash, UTC start, timeout, memory cap, and engine version before the payload
starts.

## Firewall

This client consumes a provisional terminal theorem while its hostile
review runs in the background.  It is source-typed but uncomputed.  It does
not prove the seven-tail ideal reduced, a strict saturation empty or
nonempty, either Taylor boundary, existence of a Keller pair, emptiness of
the order-two leaf, the `(8,12)` cell, maximum twelve, or JC2.
