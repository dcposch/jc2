# Erratum V2 — mandatory localization at the nonzero Jacobian constant

Date: 2026-08-25  
Status: **NONMUTATING REPAIR OF CLIENT `(3.7)` AND COMPILER CONTRACT ITEM 5**

Immutable original:

```text
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
```

The theorem assumes `j in L^*`.  Because the compiler retains `j` as a ring
variable to seek a uniform result, the correct interior saturation is

```text
I=(Psi_1,...,Psi_7),
KT=I:(tau)^infinity,
KR=KT:(varrho)^infinity,
K=KR:(j)^infinity,
H=(K+(tau,varrho)):(B_0,...,B_6)^infinity.           (E.1)
```

Equation `(E.1)` replaces original `(3.7)`.  Equivalently one may specialize
`j` to a fixed nonzero scalar before saturation.  Omitting both operations
retains a literal `j=0`, all-load-zero common-quartic component, as proved in

```text
xmodel/max12-812-order2-u2-62-strict-rees-v1-j-saturation-failure-20260825.md.
```

Compiler-contract item 5 is repaired to require agreement of sequential
saturation by `tau,varrho,j` with saturation by their product, in addition
to the original slope-three negative control.  Every other equation,
weight, twist, target, branch chart, raw-support statement, and firewall in
the original client is unchanged.

This erratum does not add the optional Shioda/Hall all-zero-lower-load
saturation.  That is a separate theorem-dependent optimization.  It also
does not compile either Taylor family, assert a unit endpoint, close the
order-two client, or touch JC2.
