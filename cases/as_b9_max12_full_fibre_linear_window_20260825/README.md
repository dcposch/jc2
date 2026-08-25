# B9 complete fixed-D12 affine families through modulus `3^10`

Starting from the displayed mod-243 point, the exact coefficient identity

```text
det J(F5+243*T)-1 = D5 + 243*A*T + 3^10*det J(T)
```

makes all complete fixed-D12 gates through modulus `3^10=59049` linear.
Exact Bocksteins on all 276 rows and 182 coefficients give:

| modulus | rank | new kernel | liftable prior dimension |
|---:|---:|---:|---:|
| 729 | 108 | 74 | 0 |
| 2187 | 147 | 109 | 35 |
| 6561 | 162 | 129 | 55 |
| 19683 | 164 | 147 | 73 |
| 59049 | 164 | 165 | 91 |

All five stages are consistent and literally replay over the integers.  The
quadratic term is still zero modulo `3^10`; it first contributes to the
divided carry for the transition from `3^10` to `3^11=177147`.

Box02 and Box03 results are byte-identical at SHA-256
`6a2145187e5697890e9838bfb6370505329c01e905abd060310f8b73cd606168`.
This is finite-depth evidence over one fixed mod-243 point, not an inverse
limit or counterexample.
