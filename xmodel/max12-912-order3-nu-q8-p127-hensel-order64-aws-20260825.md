# Selected-Q8 moving-v Hensel lift through order 64

Date: 2026-08-25  
Status: **PRODUCER-EXACT FORMAL-LOCAL DATA; review required**

The coefficient-wise moving-`v` Hensel construction completed on AWS Box02
through order 64.  It works in the exact algebra

```text
F_127[s,v]/(s^64,H(25+s,v)),
```

with standard monomials `s^i v^j` for `i<64`, `j<190`.  The pinned replay
certified the base fibre degree 190, unit full-source Jacobian and `H_v` at
the base, moving quotient dimension zero and vector-space dimension 12,160,
all 63 coefficient corrections, and `final_fail=0`.  It records all 64
coefficients in `s` of each of

```text
c,d2,d4,x1,x3,x5,inv.
```

The run completed rc zero in 1:08:07 with 158,512 KiB maximum RSS.  The
order-64 stdout SHA is
`f750d965a48634d2b47b442b47577b67b900a810ab208c2dc08f03fd5cd299aa`.

This is exact formal-local data over `F_127` only.  It neither supplies a
rational coordinate formula nor proves exact substitution modulo the global
candidate `H(w,v)`, quotient-component membership, characteristic-zero
lifting, no-merger, boundary grouping, or any trajectory conclusion.  Those
acceptance gates remain charged.

