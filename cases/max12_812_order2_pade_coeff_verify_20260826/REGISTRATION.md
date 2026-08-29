# Registration: exact Padé coefficient identity verifier

Date: 2026-08-26

Status: **PREREGISTERED AWS-ONLY EXACT IDENTITY CONTROL.**

```text
tag=max12_812_order2_pade_coeff_verify_20260826T053600Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_pade_coeff_verify_20260826T053600Z_box03
payload=custom exact rational multivariate recurrence in Python
timeout=300 s
virtual-memory cap=1048576 KiB
CPU cap=one process / one core
```

The verifier independently reconstructs coefficients `t^15,t^16,t^17` of
`(1+p*t^2+c*t^3+r*t^4)^(7/2)` from the differential recurrence, checks the
three proposed factorizations in terms of `d=p^2-4r`, and checks the two
polynomial identities used in the contradiction.  It does not consume or
assert the Laurent-series-to-Padé implication, a scheme decomposition,
order-two exclusion, `(8,12)`, maximum twelve, or JC2.
