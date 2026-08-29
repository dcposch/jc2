# Registration: raw cusp grade-12 Čech certificate

Date: 2026-08-26

Reconstruct the complete seven frozen source rows on the unparameterized
post-`M=0`, `p=0` cusp chart through absolute sigma-grade twelve.  Retain all
moving-center/correction jets, `k10,k6,k2`, and all targets at their frozen
weights.  Before cusp parametrization, radical, saturation, or any
grade-eleven pivot, test the exact raw identity

```text
32768*g12_6 - 35*k0*rs^4
  = -8192*rs*g10_2 - 32768*cs*g10_3.
```

The expected literal sixth row is

```text
g12_6 = -(3/128)*rs*c1^2 -(3/32)*rs*a0*c0
         -(3/16)*cs*c0*c1 -(5/32768)*k0*rs^4.
```

Run exact Q on Box03 and an independent `F_65521` compiler/control lane on
r6d.  Exact Q carries the characteristic-zero statement.  The certificate
would make the cusp unit a direct registered-unit identity on `D(k0*rs)` and
remove normalization-surjectivity from that one Čech chart.  It says nothing
about the other charts, total-Rees base change, the all-zero receiver, or
order-two closure.
