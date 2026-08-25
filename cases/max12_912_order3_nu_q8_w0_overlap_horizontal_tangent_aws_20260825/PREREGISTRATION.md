# Preregistration: unloaded-overlap horizontal tangent screen

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Use the exact pinned six-row approximate-cubic source

```text
I=(e1,e3,e5,e7,e2,e4)
```

in variables `(w,c,d2,d4,x1,x3,x5)`.  At the raw unloaded overlap

```text
w=x1=x3=x5=0
```

set `delta w=1` and form the six exact tangent equations

```text
L_i = e_i,w + sum_y e_i,y delta y.
```

With `u=d2-d4`, verify ideal-theoretically that the `e2,e4` conditions are
equivalent over Q to

```text
F2=u^2+2*d4*(1-u)=0,
F4=2*u^2-3*u+d4*(1-u)=0,
```

and that this radical degree-two ideal is exactly

```text
(d2-2*d4, d4*(d4-2)).
```

Thus its two rational base candidates are `(d2,d4)=(0,0),(4,2)`.

For `(4,2)`, verify the `e1,e3,e5` tangent equations are equivalent to

```text
dx1=8*c+8/3,
dx3=20*c+88/9,
dx5=12*c+16/3,
```

and the remaining `e7` equation has `729*L7=-432`, so no horizontal tangent
exists.  For `(0,0)`, verify `e1,e3,e5` force

```text
dx1=dx3=dx5=0
```

and `L7=0`; this is precisely tangent to the exact boundary sheet, not to
the selected `D(x5)` open.

Acceptance requires two independent AWS Singular engine/order lanes, mutual
ideal containments (not just point substitution), fixed source hashes, no
diagnostics, and a fail-closed replay.  This is only a first-order screen
with `ord(w)=1`.  It does not exclude ramified arcs `ord(w)>1`, second-order
departure from the boundary sheet, coefficient infinity, Taylor/terminal
realization, trajectories, or any broader `(9,12)`/maximum-twelve claim.
