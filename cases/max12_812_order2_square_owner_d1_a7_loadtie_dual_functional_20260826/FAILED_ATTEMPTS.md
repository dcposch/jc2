# Failed attempts: D1 `a=7` load-tie producer

Date: 2026-08-26

The first Box03 preflight stopped at the moving-root exactness sentinel.
Inspection showed a compiler string-parenthesization error: the complete
Hensel root series was interpolated into a square without outer
parentheses, so Singular squared only the final syntactic summand under
operator precedence.  The preflight therefore made **no mathematical
verdict**.

The compiler was repaired by emitting

```text
((lambda+sigma*rho1+...)^2+P/2)
```

as a single protected expression.  The repaired compiler was frozen before
the final triple-AWS run.  All final exact-Q and prime-screen sentinels,
including the full moving-root quotient, pass.  This file records the
preflight lifecycle only; no failed bytes are used as theorem evidence.
