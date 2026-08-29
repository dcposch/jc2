# TD6 V89H11 V1 launch erratum

Date: 2026-08-26

Both V1 AWS lanes stopped during Python module initialization, before source
construction or algebra, because the new client requested `Rat3` from the
V89H10T module rather than its imported H6 module.  The one-line R1 repair
changes only that attribute path from `t.Rat3` to `h6.Rat3`.  V1 is retained
as deployment-negative evidence and supports no mathematical claim.
