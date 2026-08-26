# TD6 V84 bounded K2 pilot — deployment-negative custody

This immutable package records the first bounded quadratic previous/pole pilot for
the fixed source-typed A3 section. It is **not mathematical evidence about the
quadratic Kuranishi map**.

Both registered AWS executions used the identical source archive
`91b09bca835473dc081d07c53e0f6df977069812a7c1927c80757d011ba20fe3`
and the single preregistered block `(0,0)` (ten quadratic pairs among
`q2,q3,q4,q5`). Both passed source closure, the quadratic coefficient controls,
the licensed-coordinate preflight, symbolic-center assertions, and the frozen
transport reconstruction (`rank=3470`, `free=132`). Both then exited `rc=1`
before any quadratic table was produced.

The common failure is a typed-composition bug in the pilot harness:
`v81.propagate_q` calls the inherited scalar source constructor, which attempts
to coerce a symbolic center-ring polynomial to `fractions.Fraction`. The exact
terminal stack is archived in each host's `stderr`.

Consequences:

- no K2 value, rank, kernel, obstruction, or vanishing conclusion is licensed;
- the identical failure is a useful dual-host deployment negative;
- the surviving preflight facts concern only source closure and the undeformed
  transport reconstruction;
- a successor must replace this scalar boundary with a center-ring-typed source
  propagation and retain the same positive/negative controls.

AWS custody:

- r6d: `td6_v84_k2_r6d_block_0_0_20260826T0500Z`, wrapper PID 231303,
  `/home/ubuntu/runs/td6_v84_k2_pilot_r6d_20260826T0500Z`;
- Box03: `td6_v84_k2_box03_block_0_0_20260826T0500Z`, wrapper PID 163911,
  `/home/ubuntu/runs/td6_v84_k2_pilot_box03_20260826T0500Z`.

The source archive is retained under `source/`; raw host streams and registration
metadata are retained byte-for-byte under `evidence/`.
