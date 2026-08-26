# Unique-output V2 delta hostile review

Review only the V1-to-V2 repair delta and its freeze closure.  Read:

```text
xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-20260825.md
SHA-256 0877fc072583c3a484ad7740e0abc6a0a981be6ad4b17e4002765f21e97cd57b

xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md
SHA-256 c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621

cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve_v2.py
SHA-256 b000ed1557bd307dc37b92fd1ff3fbe1e075cec169721d346a28599374890e1b

cases/max12_812_order4_mu4_nonzero_curve_20260825/FREEZE_V2.sha256
SHA-256 d4a5c584a792d38d74c09b607da4777ba83715d0d092c590b99f15083b35e31b
```

Recompute every V2 manifest hash directly.  In particular verify that the
three repaired parent strings are the actual SHA-256 values of the named
source audit, terminal theorem, and terminal review; verify that the V2
compiler pins the V2 client and retains the already-reviewed mathematics,
tail reconstruction, no-load order-four scope, AWS guard, two presentation
checks, lead identity, and mandatory `r7` saturation unchanged.  Diff V1 and
V2 and identify every semantic change.  Do not use any live AWS endpoint as
evidence and do not inherit the V1 verdict token.

This is source reading and hand review only: no CAS, solver, substantive
exact Python, Sage, Singular, msolve, or Lean locally.

Write exactly one file and no other file:

```text
xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-v2-20260825.md
```

Classify any issue as fatal, repairable, or cosmetic, state the strongest
surviving result and scope firewall, and end with exactly one overall verdict
token: `CONFIRMED`, `REPAIR`, or `REJECTED`.
