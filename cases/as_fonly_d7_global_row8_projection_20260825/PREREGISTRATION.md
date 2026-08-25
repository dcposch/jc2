# Global Q9-fibre projection of the Q2/Q1 row-8 scalar

Consume the corrected Q10-to-Q9 source compiler
`cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py` at
SHA-256 `54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`.
Do **not** substitute the older one-predecessor 13-trit canonical Q9 chart.

For every source-accepted Q10 predecessor state and its complete 32-variable
Q9 affine fibre, project to the four coordinates `q9_1,...,q9_4`.  The global
row-8 emitter simplifies the eliminated scalar to

```text
rx = floor((q9_1 + 2*q9_3)/3) mod 3
ry = floor((2*q9_2 + q9_4)/3) mod 3
omega = ry - h*rx mod 3.
```

For source honesty, reconstruct `E/3+M` over the integers on every projected
four-coordinate point and require exact agreement with this formula.  Compute
the affine image in `F3^4` from an exact RREF/kernel basis; enumerate at most
`3^4=81` image points and multiply by the exact constant fibre factor.  Record
the `omega=0,1,2` histogram, full/partial/empty zero-locus classification,
per-base totals, first zero witness, and a deterministic state stream hash.

The result is a projection/census of a necessary scalar over the complete
current Q9 source fibres.  It does not impose Q8/Q7/Q6/Q5/Q4/Q3 restoration,
does not prove the complete global formula SAT/UNSAT, and makes no all-depth,
counterexample, or JC2 inference.  All execution is AWS-only.
