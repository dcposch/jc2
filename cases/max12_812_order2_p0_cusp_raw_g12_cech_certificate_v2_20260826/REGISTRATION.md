# Registration: corrected raw cusp grade-12 Čech certificate V2

Date: 2026-08-26

V1 failed closed on both AWS lanes because it compared the ordinary/Faber
sixth row with the naive Laurent pole-six expression.  The complete source
printed the correction-aware row

```text
g12_6 = (15/32768)*k0*rs^4 -(3/64)*rs*a0*c0
         -(3/64)*cs*c0*c1 -(3/256)*rs*c1^2.
```

V2 changes only the asserted row and its explicit raw multipliers.  It tests

```text
32768*g12_6 - 35*k0*rs^4
  = -4096*rs*g10_2 - 8192*cs*g10_3.
```

Omitting `g10_3` must leave the nonzero residue
`-1536*cs*c0*c1`.  Exact Q on Box03 is the theorem lane; `F_65521` on r6d
is an independent compiler/control lane.  All V1 source extraction, load,
target, and custody checks remain unchanged.
