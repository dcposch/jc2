# AS residue-ball theorem — V2 repair erratum

Status: **PRODUCER-EXACT NONMUTATING V2 REPAIR; FINAL REVIEW PENDING**

Date: 2026-08-25

This erratum is consumed together with

```text
xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-20260825.md
SHA-256 81ab0e5cce46d2ad93968500362275ae4a7dbf2d3cf080c54ace531218135d71
```

and makes exactly the two repairs requested by its first final-review pass.
No computational artifact or other mathematical statement changes.

## 1. Arbitrary-target digit equation

In parent Section 1, fix an arbitrary target
`z in R_n^2` with `z=(0,0) mod 3`.  For a prescribed source residue
`r in {(0,0),(1,0),(2,0)}`, suppose that, for `1 <= k < n`, the unique
point `x_k=r mod 3` satisfies

```text
F(x_k)=z mod 3^k.
```

Writing the next lift as `x_k+3^k h`, with `h in F_3^2`, Taylor expansion
reduces the next-digit condition to the explicit inhomogeneous equation

```text
JF(x_k) h = (z-F(x_k))/3^k mod 3.                 (1.1)
```

The quotient on the right is well defined modulo three because the numerator
vanishes modulo `3^k`.  Since `det JF(x_k)=1 mod 3`, (1.1) has exactly one
solution.  This proves, for every target in the target residue ball, the
unique preimage in each of the three source residue balls claimed by the
parent.

## 2. Fixed support is not synonymous with a degree cap

Replace the parenthetical in parent Section 2 by:

> Fix finite sets of allowed monomials `S_P,S_Q`; coefficients may vanish,
> so the actual supports are contained in those sets.  A total-degree cap is
> one possible choice of fixed allowed sets, but a lacunary fixed support is
> not equivalent to the full set of monomials below that cap.

Every precision must use the same sets `S_P,S_Q`.  Neither a degree bound nor
vanishing coefficients license adding previously absent monomial slots.

## 3. Scope

All other conclusions and firewalls of the repaired parent are unchanged.
In particular, the theorem applies only after all determinant coefficients
have been reconstructed on one fixed finite allowed set at arbitrarily deep
3-adic precision.  The current Q5/H6 state still owes Q4 through Q0 and does
not qualify.
