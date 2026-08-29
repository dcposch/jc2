# TD6 V89H12 V1 launch erratum

Date: 2026-08-26

Both V1 AWS lanes stopped during Python module initialization, before any
compiler or algebra computation, because the new wrapper omitted the
inherited required environment value

```text
TD6_Q_EXPONENT=2.
```

The traceback ends at the top-level environment assertion in frozen
`replay_v85tf1_total_f.py`.  V1 is deployment-negative only and makes no
mathematical claim.  R1 adds the missing value to the wrapper and run gate;
the preregistered mathematical scope and H12 client are unchanged.
