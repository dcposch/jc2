# Direct lift/adjoint gate for the three terminal-row survivors

For each frozen SAT state from
`as_fonly_d7_global_predecessor_sat_survivors_20260825`, reconstruct the exact
integer base pair

```text
Pbase = x - x^3 + 3 U + 9 C + 27 W,
Qbase = y       + 3 V + 9 D + 27 Z.
```

Append complete cap-seven correction digits at weights `81,243,...`.  For a
requested layer count `L`, impose the literal coefficient equations

```text
det J(P,Q) == 1 (mod 3^(4+L))
```

with all `72L` correction coefficients restricted to `{0,1,2}`.  Products
are evaluated in 64-bit bit-vectors and reduced modulo the target after each
gate; the compiler asserts the unreduced product bound.

Every SAT model must be replayed using ordinary integer polynomial
arithmetic.  The replay must also emit the next obstruction vector: all
degree-7-through-12 coefficients of `(det-1)/3^(4+L)` modulo three plus the
unique cap-seven low Cartier class `[x^2 y^2]`.  This is a pointwise bounded
transition test.  UNSAT solver output is diagnostic unless independently
proof-checked.  No all-depth, algebraization, counterexample, or JC2 claim is
licensed.
