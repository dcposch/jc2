# Selected-Q8 deterministic broad fixed-fibre dispatcher

Date: 2026-08-25

This orchestration-only package dispatches disjoint `(prime,w)` ranges through
the pinned Box02 `msolve` 0.10.1 DRL/FGLM runner.  It limits concurrent lanes,
preserves one complete evidence directory per fibre, and emits an exact JSON
histogram of `empty`, `nonempty`, `failed`, and `missing` outcomes plus every
reported quotient degree.

An `empty` result is only an empty localized fixed modular fibre.  It can be a
bad specialization or a value omitted by the chosen affine/localization chart;
it does not establish generic or characteristic-zero emptiness.  A `nonempty`
result also remains modular evidence.  No component or trajectory conclusion
is made here.

Example:

```sh
run_dispatch.sh REPO OUT q8_p127_drl_all_v1 127 1 126 drl 32 1 0 1800
```

The dispatcher itself performs no algebra.  All algebra is delegated to the
source-pinned hardened runner; use only on an authorized AWS worker.

