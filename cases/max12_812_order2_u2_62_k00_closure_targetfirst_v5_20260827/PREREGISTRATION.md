# K00 closure V5: affine targets first

Date: 2026-08-27

Status: **PREREGISTERED ORDERING SCREEN; NO ENDPOINT.**

V5 computes the exact V2 g-open ideal with all variables retained, reordered
into global blocks

```text
(mu2,mu4,mu6,Jdet) | (k10,k6,k2) | (Lambda,C0,...,C6)
(       lp(4)     ) | (  dp(3)  ) | wp(1,8,7,6,5,4,3,2).
```

The first four variables occur as the affine targets in exactly one row
each.  The three lower loads are affine-linear in every frozen tail.  This
order lets the Gröbner engine expose that triangularity; it does not solve,
delete, project, specialize, or move any load to a coefficient field.
`M_K00` is still imposed only after the source saturation, and every V1/V2
control remains.

Unsupported coded `quit` calls are replaced by supported `exit(code)`.
First screen: characteristic 65519 on AWS Box01, 20-minute / 64-GiB cap.
It is not a Q endpoint.  This is the final order variant in the current
race; timeout/failure is no verdict and does not license further unbounded
variants.
