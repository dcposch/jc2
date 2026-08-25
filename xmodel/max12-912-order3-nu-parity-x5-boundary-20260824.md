# `(9,12)` order-three `nu!=0` parity `x5=0` boundary

Date: `2026-08-24`  
Status: **PRODUCER-EXACT / REVIEW REQUIRED**

## Exact specialization

In approximate-cubic coordinates

```text
K=z^3+pz+q,
f=K^3+sum_(i=0)^5 x_i z^i,
```

specialize

```text
q=x0=x2=x4=k=0.                                        (1.1)
```

Then `f` is odd and its `F12` polynomial `g` is even. The exact compiler
therefore gives

```text
r1=r3=r5=r7=0                                          (1.2)
```

identically; only `r2,r4,r6,r8` remain. This is a component probe, not an
assertion that every loaded solution has parity (1.1).

## The `x5=0` solve

At `x5=0`, the first even rows begin

```text
r2=(4/9)*x3*(x1-p*x3).
```

If `x3=0`, then `r4=(2/9)*x1^2`; hence `r4=0` forces `x1=0`, and then
`r6=0`, contrary to `r6=nu!=0`. Thus `x3!=0` and `r2=0` gives

```text
x1=p*x3.
```

Substitution into all exact tail rows gives

```text
r2=r4=0,
r6=-(4/81)*x3^3=nu,
r8=0.                                                   (2.1)
```

For the normalized fibre, `x3^3=-81/4`. Algebraically this is a genuine
coefficient-fibre component over the constant field, but it cannot be an
actual trajectory: the terminal equation gives

```text
9*r8'=0 != j/u.                                         (2.2)
```

Thus the entire parity `x5=0` branch is excluded before either Taylor
boundary is used.

## Reversible next chart

The coefficient of `x1` in `r2` is `(4/9)A`, where

```text
A=x3-2*p*x5.
```

On `A=0`, exact substitution gives

```text
r2=-(4/81)*p*x5^3.                                     (3.1)
```

If `x5=0`, then `x3=0`, and the preceding `r4,r6` argument forces `nu=0`.
If `p=0`, then `x3=0` and direct substitution gives `r6=0`. Hence

```text
nu!=0  implies  A!=0.                                  (3.2)
```

After the now-excluded `x5=0` component is removed, the unresolved parity
route lies on the fail-closed chart

```text
A*x5 != 0.                                              (3.3)
```

There `r2=0` solves `x1` reversibly. The exact first resultant has the form
`Res_x1(r2,r4)=(-16/59049)*x5*P4`; retaining the `x5` factor is what exposes
the terminally impossible component (2.1). Subsequent resultants are licensed
only on (3.3).

## Scope

**Producer conclusion:** the parity `x5=0` branch is incompatible with the
terminal Keller row, and `A=0` is empty for `nu!=0`.

**Not concluded:** exhaustion by parity, emptiness of the remaining
`A*x5!=0` chart, any generic loaded component, Taylor-boundary compatibility,
all `(9,12)`, maximum-twelve automorphy, a counterexample, or JC2.
