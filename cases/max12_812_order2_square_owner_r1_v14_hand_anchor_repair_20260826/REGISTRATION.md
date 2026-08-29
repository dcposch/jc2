# Registration: order-two square `r=1` V14 hand-anchor repair

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS SOFTWARE REPAIR.  NO D1, SQUARE-BRANCH,
OR ORDER-TWO VERDICT.**

V13 correctly standardized the radical and hardened the validator, but its
new hand-remainder sentinel was placed before `R1_e1,R1_e0` were declared.
Both AWS fields failed closed with the identical undefined-symbol diagnostic.

V14 pins V13 and changes only placement of that exact sentinel: it removes
the six-line block from before the denominator marker and reinserts it
immediately after

```text
poly R1_e1=diff(R1_rem,z); poly R1_e0=subst(R1_rem,z,0);
```

The standard-basis repair, source rows, analytic identity, coefficients,
localization, radical computation, memory/time caps, and fail-closed
validator are unchanged.  Run exact Q on Box03 and `F_65521` on r6d with
24-GiB virtual-memory, 600-second compile, and 1800-second engine caps.

