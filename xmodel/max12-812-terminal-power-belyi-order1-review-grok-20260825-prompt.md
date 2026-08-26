# Hostile review: `(8,12)` terminal-power/Belyi and order-one theorem

Act as an independent hostile mathematical reviewer.  Read the immutable
target and every charged source named in its Section 1.  Do not use the
target status, a producer summary, or any prior verdict token as evidence.

Target:

```text
a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633
  xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md
```

Audit from scratch:

1. Re-derive the inverse character of `r_7`, fixed-field descent of
   `T=r_7^e`, and the constant in
   `d(T')^e=(e*j/8)^e*T^(e-1)` for `e=2,4`.  Check that `d=v` rather than
   `h=v^2` in order two.
2. At every finite base point, attack all cases `T=0`, `T=infinity`, and
   `T` finite nonzero.  Verify the dictionary `k<e`, `k=e`, `k>e`, including
   uncharged zeros of order `e`, and verify that no critical point away
   the zero/pole fibres was silently omitted.
3. At base infinity, remember that the prime is `d/dx=-q^2*d/dq`.
   Independently recompute the nonzero finite, zero, and pole cases, the
   exact orders in `(0.6)`, exclusion of `U=1`, and the at-most-three branch
   values.  Challenge `lambda=0`, `U=2`, and unramified cases.
4. For order one, independently prove or refute the claim that a polynomial
   `q` with rational `R` satisfying `R'=1/q` is constant or a single-root
   pure power of degree at least two.  Check simple roots, exact pole orders,
   the global degree `deg R=U-N`, local degree `U-1` at infinity, descent of
   the unique root, all constants and converses.
5. Enforce the firewall: this is terminal necessity only, not lower-tail,
   Taylor, strict-Rees, Keller existence, `(8,12)` closure, maximum twelve,
   or JC2.

Source reading and hand derivation only.  Run no CAS, solver, substantive
Python, Lean, or other heavy local computation.  Write exactly one report
and edit nothing else:

```text
xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md
```

Include model identity, exact target SHA, verdict `CONFIRMED`, `REPAIR`, or
`REFUTED`, the smallest failing identity or missing hypothesis, an
independent proof/attack, and an exact scope firewall.
