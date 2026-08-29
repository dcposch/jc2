# V24 exact grade-seven two-cokernel contraction

Date: 2026-08-27

Status: **PRODUCER PASS; HOSTILE REVIEW PENDING.**

## Exact result

On the constructible chart

```text
C6(normalization)=1,
v(d)=1,
k10_0 != 0,
W != 0,
Phi[row,grade]=0 for rows 1..7 and grades 2..6,
F10=0,
```

the honest grade-seven newest-coefficient matrix has rank five.  Here

```text
W = det A[rows 0,1,2,3,4; columns 0,1,2,3,6]
```

is V23's frozen nonzero 226-term minor.  Exact Cramer minors give a complete
two-dimensional polynomial left kernel on `D(W)`.  Contracting the literal
grade-seven inhomogeneous term with this basis gives two exact compatibility
polynomials, called `C6` and `C7` in the evidence file.  On this chart,
grade-seven solvability is equivalent to their simultaneous vanishing.

The two polynomials have 110,117 and 83,298 terms.  The compiler checked all
seven left-kernel identities coefficientwise, detected a sign mutation, and
reconstructed all 42 literal coefficients (seven rows, grades 2 through 7)
against the frozen V20R2 DAG on two exact-Q and two F65521 fixtures.

## Modular diagnostic and unresolved custody point

Over `F_65521`, both compatibility polynomials reduce to zero modulo the
prior grade-2-through-6 equations plus `F10`, localized at `k10_0*W`.
The V24 script did not record whether that localized prior ideal is proper.
Consequently this zero reduction is retained only as a diagnostic: it may be
genuine membership or a vacuous reduction modulo the unit ideal.  A frozen
narrow properness repair is required before consuming the modular membership.
No exact-Q membership follows in either case.

## Custody

- preregistration SHA256:
  `3e48bb009c82a1a988aca5f17a65f290f916e83a3fc1773252ef9b5b59227e0c`
- compiler SHA256:
  `1652cf3f2cefff9490062aade6e4c5be1c20b82cbefa01a7ef8a039530c39022`
- runner SHA256:
  `5fbcb8ebe22fb11701000b367e84c22777feb2536bf7c16a6a7573bc538a7829`
- source-freeze manifest SHA256:
  `48e38dfb3ace6301af078b1e2ccd7c3d59a898fbe091c13567f371d0884eb3f9`
- AWS tag:
  `max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827T132850Z_r6b`
- exact compatibility artifact SHA256:
  `4f4c2bac49270fdd220e2333fbf82ba8bd4cc507cff90ea3eb8c2bf8c614ddd2`
- left-kernel basis SHA256:
  `6c857c91220965ee25d4483b122277c174a0dc0b9f740311fce02390b92893e1`
- inhomogeneous vector SHA256:
  `dc7696e1c1552533418eba1f91e14227ef8663aeded38b111d3295d1afb3f289`
- RESULT JSON SHA256:
  `22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b`
- endpoint evidence manifest SHA256:
  `8fedd7c3ea3c693679b1fa96a9ebce849c0455c44021cb86ad699bc8592b7c60`
- independent local replay of endpoint manifest: 14/14 entries.
- runtime: 5:01 wall, 300.34 CPU seconds, 1,840,916 KiB maximum RSS,
  zero swap, exit status zero.

## Firewall

This is an exact grade-seven linear-algebra theorem only on the one chart
`D(k10_0*W)`, conditional on the complete listed prefix.  It says nothing
about `W=0`, grades 8 through 19, existence of a compatible prefix, a full
jet or arc, K00 closure incidence, order two, maximum twelve, or JC2.  The
modular zero normal forms are not an exact-Q theorem.
