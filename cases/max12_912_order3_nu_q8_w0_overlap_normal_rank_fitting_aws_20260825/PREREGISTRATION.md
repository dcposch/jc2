# Preregistration: raw-overlap normal-rank/Fitting split

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

The first formal-IFT probe falsified the blanket assertion that the raw
special-fibre overlap `A3` is smooth everywhere: the six-by-three normal
Jacobian block `M` drops rank on a nonempty exact-Q locus.  This successor
stratifies that locus without discarding it.

On

```text
A3: w=x1=x3=x5=0,
```

let `M` be the six source-row derivatives in `(x1,x3,x5)` and let
`N=[M|F_w]`.  Form all Fitting minors and the four tangent-incidence ideals:

```text
K3 = I_4(N) : I_3(M)^infinity,
K2 = (I_3(M)+I_3(N)) : I_2(M)^infinity,
K1 = (I_2(M)+I_2(N)) : I_1(M)^infinity,
K0 = I_1(M) + (F_w entries).
```

These are respectively the closures of first-order horizontal tangent
incidence on the exact-rank `3,2,1,0` strata.  Print exact reduced bases,
unit status, and inverse-variable tests on `D(d2)` and `D(d4)`.  Also print
the rank-drop ideal `I_3(M)` itself for factor/elimination routing.  No
candidate is discarded merely because it is rank-deficient.

Acceptance requires two independent exact-Q AWS engines/orders, all source
rows vanishing on A3, tangent-coordinate columns zero, original minors
reducing into the printed bases, fixed source hashes, and no diagnostics.
This is a first-order/Fitting classification only.  Rank-drop weighted or
ramified arcs, special-fibre embedded/intersecting branches, global
saturation, projective infinity, Taylor/terminal reconstruction, and all
broader claims remain charged.
