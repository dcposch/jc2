# Independent theorem — D1 weighted-infinity exceptional support

Date: 2026-08-25  
Verdict: **PROVED (REDUCED SUPPORT ONLY)**

## Charged exact sources

```text
a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf  cases/max12_912_order3_fibre_20260824/order3_fibre.py
b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
1424037680ac7ceeb0927388c59e5028f43ca9b7d37916cfea61809ca5ed7361  xmodel/max12-912-order3-d1-classical-degree-split-20260825.md
acadfdd2be456b74c909f092f4800d674036dbf37a8972a2efdbf186a9c42778  xmodel/max12-912-order3-d1-classical-degree-split-review-20260825.md
```

## Theorem

Let `L` be a characteristic-zero field.  Put

```text
f=z^9+sum_(i=0)^7 B_i z^i,       wt(B_i)=9-i,
g=F_12(f),
```

and let `r_ell` be the frozen order-three Faber tails, with convention

```text
w=f^(1/9)=z+O(z^-1),
g(z(w))=w^12-T,                  T=sum_(ell>=1) r_ell w^-ell.
```

Let `J_infinity=(r_1,...,r_8)` in `L[B_0,...,B_7]`.  This is the exceptional
fibre obtained from the D1 descended raw tails at `s=1`, after the weighted
Rees scaling sends `k` to zero.  Then

```text
sqrt(J_infinity)=I_CC,
```

where `I_CC` is the prime graph ideal of

```text
K=z^3+p z+c,       f=K^3,       g=K^4.
```

Equivalently, the reduced weighted-projective exceptional divisor is exactly

```text
E_red = Proj L[p,c] = P(2,3).
```

To identify the descended fibre with these ordinary tails, use the etale
`t=1` sheet above `s=1`.  There `a_i=t^(i mod 3)A_i=A_i`, and each descended
raw row differs from its ordinary tail only by the nonzero character factor
used in the frozen descent.  Hence its vanishing is exactly `r_ell=0`.
The other sheets `t=zeta`, `zeta^3=1`, are obtained by the diagonal
`mu_3` action `a_i=zeta^(i mod 3)A_i`; they give the same zero-tail support
up to this weighted orbit.  Thus the `t=1` calculation classifies the whole
descended exceptional support.

## 1. Spectral-tail degree lemma

The frozen spectral identity specializes at `k=0` to

```text
W:=g^3-f^4=-3 w^24 T+3 w^12 T^2-T^3.              (1)
```

If `r_1=...=r_8=0`, then `T=O(w^-9)`.  The three terms on the right of (1)
therefore have largest possible `w`-exponents respectively

```text
24-9=15,       12-18=-6,       -27.
```

Thus `W(z(w))` has no term above `w^15`.  If a nonzero polynomial in `z` has
degree `D`, substitution of `z(w)=w+O(w^-1)` leaves its leading term equal to
its nonzero leading coefficient times `w^D`.  Consequently

```text
r_1=...=r_8=0  implies  deg_z(g^3-f^4)<=15.        (2)
```

This includes the possibility `W=0`.

## 2. Mason--Stothers forces `W=0`

Assume for contradiction that `W` is nonzero.  Let

```text
D_0=gcd(g^3,f^4),       e=deg D_0.
```

Because `D_0` divides their difference `W`, (2) gives

```text
0<=e<=deg W<=15.                                      (3)
```

In particular the possible edge `e=36` cannot occur when `W!=0`; directly,
a monic degree-36 common divisor of the two monic degree-36 powers would make
the powers equal and `W=0`.  Define

```text
A=g^3/D_0,       B=-f^4/D_0,       C=-W/D_0.
```

Then `A+B+C=0`, the three polynomials are pairwise coprime, and

```text
deg A=deg B=36-e,       deg C<=15-e.                 (4)
```

Mason--Stothers applied over `L` (or after harmless scalar extension to its
algebraic closure) now gives

```text
36-e
 <= deg rad(A B C)-1
 <= deg rad(f g)+(15-e)-1
 <= (9+12)+(15-e)-1
 = 35-e,
```

a contradiction.  The nonzero-constant edge is included: then `e=0` and
`deg C=0`, which only strengthens the contradiction.  Hence `W=0`.

## 3. UFD, depression, and the explicit prime

The identity `g^3=f^4` in the UFD `L[z]` and `gcd(3,4)=1` imply, factor by
factor, that there is a monic cubic `K` with

```text
f=K^3,       g=K^4.
```

Write `K=z^3+d z^2+p z+c`.  The absent `z^8` coefficient of the depressed
`f` is `3d`, so characteristic zero gives `d=0`.  Expansion of
`(z^3+pz+c)^3` yields

```text
B_7=3p,             B_6=3c,
B_5=3p^2,           B_4=6pc,
B_3=p^3+3c^2,       B_2=3p^2c,
B_1=3pc^2,          B_0=c^3.                         (5)
```

Conversely, the frozen compiler checks exactly that (5) makes all eight
tails zero.  Since `p=B_7/3` and `c=B_6/3`, the image in (5) is closed and
its graph ideal is prime.  One explicit generating set is

```text
3 B_5- B_7^2,
3 B_4-2 B_7 B_6,
27 B_3-B_7^3-9 B_6^2,
9 B_2-B_7^2 B_6,
9 B_1-B_7 B_6^2,
27 B_0-B_6^3.                                         (6)
```

The point `B_0=...=B_7=0` is the legitimate affine common-cubic point
`K=z^3`; it is not an extra component.  The Nullstellensatz applied after
base extension, followed by contraction to `L`, proves
`sqrt(J_infinity)=I_CC`.  Both ideals are weighted homogeneous.  Since the
prime (6) does not contain the irrelevant ideal
`m=(B_0,...,B_7)`, it is already `m`-saturated.  Therefore

```text
sqrt(J_infinity : m^infinity)=I_CC
```

Here saturation removes only components supported entirely at the irrelevant
ideal; it does not delete the origin from the affine common-cubic variety.
Rather, `Proj` omits that irrelevant affine point and gives exactly
`Proj L[p,c]=P(2,3)`.

## 4. Exact rational ramification charts

Let `q=s-1`, let a rational strict-pole branch have pole orders `d_i`, and
put

```text
alpha=max_i d_i/(9-i)=m/n>3,       gcd(m,n)=1.
```

On the minimal ramified pullback `q=epsilon^n`, normalize

```text
B_i(epsilon)=epsilon^(m(9-i)) A_i(1+epsilon^n).
```

Every `B_i` is regular, at least one `B_i(0)` is nonzero, and rationality in
`q` gives the exact monodromy law

```text
B_i(zeta epsilon)=zeta^(m(9-i)) B_i(epsilon),
zeta^n=1.                                               (7)
```

Thus `B_i(0)!=0` forces `n | (9-i)`.  Applying this to the complete reduced
support (5) leaves exactly three cases:

1. `p c!=0`: the active weights include `2` and `3`, so `n=1`.
2. `p!=0,c=0`: the active weights are `2,4,6`, so `n=1` or `2`.
3. `p=0,c!=0`: the active weights are `3,6,9`, so `n=1` or `3`.

The case `p=c=0` is the irrelevant affine origin and supplies no projective
arc.  Hence a rational strict coefficient-infinity branch can have only an
integral weighted slope, a half-integral slope on the `c=0` axis, or a
third-integral slope on the `p=0` axis.  These possibilities are sharp for
the exceptional source equations: the corresponding scaled common cubics
give exact zero-tail controls.  They are not thereby lifts of the nonzero D1
loads.

## Firewall

This theorem classifies only the reduced support of the weighted exceptional
fibre.  It does not prove that `J_infinity` is reduced, exclude embedded or
nilpotent structure, construct or exclude a Rees deformation, solve any
`20m` load-complete jet, produce a rational Stage-A section, establish
Taylor polynomiality, or close D1, another passport, `(8,12)`, the full
maximum-twelve frontier, or JC2.
