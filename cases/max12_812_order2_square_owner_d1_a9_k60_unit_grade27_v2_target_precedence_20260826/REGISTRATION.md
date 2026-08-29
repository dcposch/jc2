# Registration: D1 `a=9`, `D(k60)` grade-27 obstruction V2

Date: 2026-08-26

Status: **PREREGISTERED ONE-TOKEN SYNTAX REPAIR; DUAL AWS REQUIRED.**

V1 is immutable.  Its dual AWS engines returned zero after the complete
source, grade-27, moving-connection, and delayed-load identities passed, but
the validator correctly rejected diagnostics: Singular parsed
`sigma^38/4` as exponentiation by the rational number `38/4`.  Consequently
the target-retention boolean was undefined and no obstruction endpoint was
licensed.

V2 pins V1 compiler SHA-256
`abb88d2a343d0cde75cdc8c2818ccc541c9961b6eca71f3ef0cbf8e114698f74`
and V1 freeze SHA-256
`d84fef5925858f105332591df7a2027ae4f70c764517a1c1b167a60c2204d968`.
It changes exactly one generated token sequence:

```text
diff(A9V2_Q0_7,J)+sigma^38/4==0
diff(A9V2_Q0_7,J)+(sigma^38)/4==0
```

All mathematical acceptance tests, full-source ancestry, resource caps, and
the exact scope/firewall are inherited from V1.  V2 must pass exact Q on
Box03 and `F_65521` on r6d independently.

