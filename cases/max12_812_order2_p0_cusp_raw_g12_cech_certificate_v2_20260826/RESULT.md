# Producer result: direct raw cusp grade-12 Čech certificate

Date: 2026-08-26

Status: **PROVISIONAL EXACT-SOURCE CERTIFICATE; DUAL AWS PASS.  HOSTILE
REVIEW IS REQUIRED BEFORE THIS BRIDGE IS CONSUMED BY TOTAL-REES GLUE.**

The complete unparameterized post-`M=0`, fixed-`p=0` source gives the raw
ordinary/Faber row

```text
g12_6 = (15/32768)*k0*rs^4 -(3/64)*rs*a0*c0
         -(3/64)*cs*c0*c1 -(3/256)*rs*c1^2.        (1)
```

Together with the literal grade-ten rows

```text
g10_2=(5/1024)*k0*rs^3+(3/8)*a0*c0+(3/32)*c1^2,
g10_3=(3/16)*c0*c1,
```

the complete source verifies the polynomial identity

```text
32768*g12_6 - 35*k0*rs^4
 = -4096*rs*g10_2 - 8192*cs*g10_3.                (2)
```

Thus, in the raw predecessor quotient and before cusp parametrization,
normalization, radical, saturation, or a grade-eleven pivot,

```text
g12_6=(35/32768)*k0*rs^4.
```

This is a unit on the already registered open `D(k0*rs)`.  Equation (2)
removes the normalization/finite-cover debt from the cusp endpoint itself;
it does not prove that this endpoint is the base change of a total
unspecialized-`p` Rees chart.

The nilpotent row is load-bearing: omitting `g10_3` leaves the exact nonzero
residue `-1536*cs*c0*c1`.  V1 is preserved as a fail-closed negative control:
it incorrectly compared (1) with the naive Laurent pole-six expression and
both lanes rejected that assertion.  V2 changes only the asserted
ordinary/Faber row and its multipliers.

Exact Q on Box03 and the independent `F_65521` r6d control both pass.  The
complete compiler retains all seven frozen tails, every second correction,
`k10,k6,k2`, and all targets; the compiled source census records 174 `k6`,
282 `k2`, and 23 occurrences each of `mu2,mu4,mu6,J`.  All later loads and
targets are source-certified absent from grade twelve.

This certificate is restricted to the post-`M=0`, fixed-`p=0`, unit-load
cusp open `D(rs*k0)`.  It does not cover the odd, `C`, or `A` charts, prove
the iterated blowup maps, exclude positive-valuation moving `p`, eliminate
the all-zero higher-contact receiver or `k0=0`, close order two, maximum
twelve, or JC2.
