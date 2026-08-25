# Nonmutating preregistration erratum: row-8 carry orientation

The frozen `PREREGISTRATION.md` at SHA-256
`1a70dbaa8af1702e686c17e21443b689450a8ac15dd2618d700f8517c5ef9050`
swaps the names `rx` and `ry` in its displayed closed formula.  Preserve those
bytes as provenance; consume this correction together with them.

The projected coordinate tuple is

```text
(q1,q2,q3,q4) = (c2_1,c2_2,d2_0,d2_1).
```

Since `C_x+D_y` has `x` coefficient `2*q2+q4` and `y` coefficient
`q1+2*q3`, the source-oriented carries and scalar are

```text
rx = floor((2*q2 + q4)/3) mod 3,
ry = floor((q1 + 2*q3)/3) mod 3,
omega = ry - h*rx
      = floor((q1 + 2*q3)/3)
        + 2*h*floor((2*q2 + q4)/3) mod 3.
```

This is exactly the formula in corrected V2 source SHA-256
`8d1b070c724b7ef2b0869f7925b6bdffc38d4e8beee643192cb5fd3ac8bc1547`
and control-complete V3 source SHA-256
`c0951aaf55df349a79e99a6aaae013bb5e9eb8d1fce9ea43995ec4550ccb4296`.
Both reconstruct the literal integer source expression `E/3+M` on every
projected tuple and assert equality with the corrected formula.

The initial AWS V1 source SHA-256
`9cca43b1e15ad382c880455b1d89f7964e96141286d3dcf99b6004fbe800a5a2`
implemented the swapped formula.  Its 15 fail-closed shards and 12
coincidentally passing shards are a negative control only.  V1 is not
mathematical evidence.  Corrected V2 and V3 must be cited by their source
hashes and AWS job tags, not as executions of the uncorrected displayed
formula.

Scope is unchanged: this is a projected necessary scalar over current Q9
source fibres.  It imposes no Q8 through Q3 restoration and gives no
all-depth, counterexample, or JC2 inference.
