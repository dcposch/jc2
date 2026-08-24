# `(9,12)` order-three spectral Wronskian ladder at `k=0`

Date: `2026-08-24`  
Status: **PRODUCER-EXACT ALGEBRAIC IDENTITY / REVIEW REQUIRED FOR PROMOTION**

## 1. Scope

Work on the reviewed order-three Faber landing for `(9,12)`, and specialize
the differential-constant target parameter `k` to zero. Thus

```text
f=w^9,
g=w^12-T,
T=sum_(l>=1) r_l*w^-l,
F_j=[w^j]_+.
```

The general spectral identity would require retaining the `W_k J(f,k)` term
if `k` varied with `x`; in the reviewed Faber landing `k` is differential-
constant, and here it is identically zero. No general-`k` chain-rule claim is
made.

Define the `z`-Wronskian

```text
B=3*f*g_z-4*g*f_z.                                    (1.1)
```

This report derives its exact expression in the lower Faber tails. It does
not classify an algebraic component or a rational trajectory and does not
consume either original Taylor boundary.

## 2. Exact identity

Put `X=T*w^-12`. Then

```text
beta=g^3/f^4=(1-X)^3,
beta_z=-3*(1-X)^2*X_z,
g^2/f^5=w^-21*(1-X)^2.
```

Since also `beta_z=g^2*B/f^5`, the common factor cancels identically:

```text
B=-3*w^21*X_z
 =3*sum_(l>=1) (l+12)*r_l*w^(8-l)*w_z.                (2.1)
```

For `l>=9`, the corresponding Laurent series has no polynomial part. For
`1<=l<=8`,

```text
[w^(8-l)*w_z]_+ = F_(9-l)'/(9-l).
```

Because `B` is a polynomial, (2.1) gives the finite exact ladder

```text
B=sum_(l=1)^8 3*(l+12)/(9-l) * r_l * F_(9-l)'.         (2.2)
```

The coefficient list for `l=1,...,8` is

```text
39/8, 6, 15/2, 48/5, 51/4, 18, 57/2, 60.
```

The portable replay reconstructs `f,g,r1,...,r8` from the frozen compiler and
checks (2.2) coefficient-for-coefficient over
`Q[a0,...,a7][z]`; no quotient ideal or numerical point is used.

## 3. Order-three specialization

The order-three character filter gives

```text
r1=r2=r4=r5=r7=0,       r3=mu,       r6=nu.
```

Therefore

```text
B=(15/2)*mu*F6' + 18*nu*F3' + 60*r8.                  (3.1)
```

For a monic depressed degree-nine core,

```text
F3=z^3+(a7/3)z+a6/3 = z^3+pz+q.
```

This gives three exact successive spectral defects:

| invariant stratum | exact `B` degree | first `W=g^3-f^4` degree |
|---|---:|---:|
| `mu!=0` | 5 | 21 |
| `mu=0,nu!=0` | 2 | 18 |
| `mu=nu=0,r8!=0` | 0 | 16 |

In particular, the smallest nonzero-load successor is not a generic
seven-row fibre. It has the centered quadratic Wronskian

```text
B=54*nu*z^2+18*nu*p+60*r8.                            (3.2)
```

There is no `z` term. Its two critical points, counted with multiplicity,
satisfy

```text
z^2=-(18*nu*p+60*r8)/(54*nu).                         (3.3)
```

Since `p` and `r8` both have Kummer character two, write
`p=u^2*P`, `r8=u^2*R`; then (3.3) descends after `z=uZ` to a quadratic over
`K=C(x)`. This is the natural quotient coordinate for a component/genus
classification of the `nu!=0` fibre.

## 4. Ramification interpretation and next test

For `mu=0,nu!=0`, `beta-1` has order `18` at infinity. The roots of `f` and
`g` contribute `27+24=51` to Riemann--Hurwitz and infinity contributes `17`.
Exactly two ramification units remain, matching the quadratic (3.2). They may
occur as two simple critical points, one double critical point, or collide
with the `beta=1` fibre; those boundary strata must all be retained.

The cheapest next discriminator is therefore:

1. normalize the nonzero differential constant `nu` to one;
2. compute the reduced component/function-field decomposition of the exact
   eight-variable, seven-equation fibre;
3. use the quadratic constant term in (3.2) as the projection coordinate;
4. determine each component's genus and reconstruct `r8` and the two original
   Taylor boundaries before any trajectory claim.

The bounded standard-basis width probe is registered in
`cases/max12_912_order3_nu1_probe_20260824/generate.py`. A standard-basis
dimension or degree is only a routing statistic, not a component or
trajectory theorem.

## 5. Replay and firewall

Run:

```sh
python3 cases/max12_912_order3_nu1_probe_20260824/wronskian_ladder.py \
  | diff -u cases/max12_912_order3_nu1_probe_20260824/wronskian_ladder.json -
```

**Producer conclusion.** Equation (2.2), its order-three specialization
(3.1), and the centered quadratic (3.2) are exact polynomial identities.

**Not concluded:** irreducibility, dimension, genus, a rational trajectory,
Taylor-boundary compatibility, emptiness of a loaded fibre, emptiness of
`(9,12)`, maximum-twelve automorphy, a counterexample, or JC2.
