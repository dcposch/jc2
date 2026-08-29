# Registration: grade-48 odd-null controls

Date: 2026-08-26

Status: preregistered fixed-slice falsifier; no full-face claim.

The coefficient-only sparse DAG gives

```text
F48=(3/32)a p^2 m^2 r0-(3/32)a p^2 y^2
    -(1/16)a p^4 d2+(3/128)a p^6 d6-(1/64)p^2 m^3.
```

The earlier rational witnesses set `F48=-1/32`.  This control changes only
their grade-44 leading transverse deviations so that `F48=0`, while retaining
all seven complete rows and every grade-48 correction variable:

```text
D(x): p=m=a=x=1, y=0, r0=1/2,
      d6=20, d2=8, dm=-23/32;
D(y): p=m=a=y=1, x=0, r0=-1,
      d6=-70, d2=-59/2, dm=179/64.
```

Both tuples satisfy the complete frozen grade-44 block.  The client asks
whether the full seven-row grade-48 ideal is a unit or has a survivor.  Exact
`Q` is evidence and `F65521` is a software control.  This is only a
fixed-rational-slice falsifier; it is not equality-face exhaustiveness,
rational regrading, source/Rees coverage, order two, maximum twelve, or JC2.

