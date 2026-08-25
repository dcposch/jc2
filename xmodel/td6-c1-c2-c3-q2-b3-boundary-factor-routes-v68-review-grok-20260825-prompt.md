# Hostile review charge: TD6 V68 B3 boundary-factor routes

You are the independent hostile reviewer. Work read-only except for the single
review report named below. Do not modify producer files, manifests, freezes,
canonical ledgers, or any other report. Do not use Bash, external web search,
or network access. Read the relevant files in full with the allowed read/search
tools.

Review these producer artifacts:

- `cases/td6_c1_c2_c3_q2_b3_boundary_factor_routes_v68_aws_20260825/`
- `xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-aws-20260825.md`

Also inspect every direct-source dependency named or hash-pinned by the V68
package, and the V66 B3 chart package whose exceptional factors V68 routes.

The claimed narrow result is only this: the V66 exceptional factors `t=0`,
`w=0`, and `t=2` route exactly into the raw-center union

```text
U0=0,
V0=0, C0=-U0^2,
V0=0, C0=-5U0^2.
```

Audit adversarially:

1. Recheck the normalized identity
   `b(x,t(x+5))=(x+5)((t-2)^2*x+5*t^2-20*t+4)` and all three
   specializations, including denominator/chart assumptions.
2. Recheck the raw identity
   `B3|_(V0=0)=4*U0^2*(C0+U0^2)*(C0+5*U0^2)` and prove that no finite
   branch is omitted when translating back from normalized coordinates.
3. Verify that `t=0`, `w=0`, and `t=2` are exactly V66 factor debts in the
   stated chart, and that V68 does not silently cover `2t-1` or
   `t^2-4t+2`.
4. Audit all frozen dependency hashes and marker checks. Distinguish a
   hash/marker dependency audit from an independent rerun of the underlying
   source algebra. Note the known cross-host nondeterminism in fresh `U0=0`
   internal digests; V68 must rely only on the immutable frozen dependency,
   not promote those nondeterministic mirrors.
5. Inspect the wrong-coefficient, missing-branch, and marker-omission negative
   controls. State whether they really detect the intended failures.
6. Audit exact scope. No whole-B3, whole-A3, TD6, SP-2, landing, or JC2 claim
   is licensed by this route package alone. The finite factors and review
   status of every target source theorem remain separate obligations.
7. Check MANIFEST/FREEZE design and AWS custody claims from readable evidence,
   while clearly flagging anything that would require shell execution as not
   independently rerun in this no-Bash review.

Write a concise but technically explicit report to exactly:

`xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-review-grok-20260825.md`

End with one verdict from `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, `PROVISIONAL`,
or `REJECTED`, followed by the exact strongest statement licensed after the
review and a numbered list of every required repair or residual obligation.
