# Hostile review: `(8,12)` terminal exact differential and divisor theorem

Act as an independent hostile mathematical reviewer.  Read the immutable
target and both charged sources in full, then independently rederive or
break the theorem.  Do not use a producer verdict, prior summary, or PASS
string as evidence.

Target (immutable):

```text
1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b  xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md
```

Required sources:

```text
xmodel/max12-partial-y-kummer-preflight-20260824.md
xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md
```

Audit every bridge from scratch:

1. Verify the terminal identity `8r7'=j/u`, the character of `r7`, and the
   exact inverse-character eigenspaces in Kummer class orders four and two.
   Recompute both base ODEs with the original Jacobian constant:
   `8hA'+6h'A=j` and `8vA'+4v'A=j`.  Challenge existence, uniqueness, the
   constant-field step, and every implication in both directions.
2. Normalize every infinity place for `H=4U`.  Check unramifiedness,
   `dx/u=-q^(U-2)t^-1dq`, the sheetwise residue, exclusion of `U=1`, and
   regularity for `U>=2`.
3. At a finite root independently derive the normalization, ramification
   index, and exact orders `(4-k)/gcd(4,k)-1` and
   `(2-k)/gcd(2,k)-1`.  Check all small multiplicities, the claimed
   nonzero residues at `mult_h=4`, and the global holomorphic-exact
   contradiction that forces `mult_h>=5` in order four and `mult_h>=6` in
   order two.  Look for cancellation between branches or missed infinity
   places.
4. For `U=2,e=2`, enumerate every divisor partition and verify that
   `[3,1]` for `v` / `[6,2]` for `h` is the unique nontrivial candidate.
   Recompute on the smooth normalization all identities
   `T=u/(x-a)^2`, `T^2=(x-b)/(x-a)`,
   `dx/u=2dT/(b-a)`, and
   `r7=jT/(4(b-a))`.  Audit both branch points and both infinity points,
   including pole orders and residues.
5. Enforce the firewall: passing the terminal equation is necessary only.
   It must not imply the other six tails, Taylor polynomiality, existence,
   order-two closure, `(8,12)`, maximum twelve, or JC2.

Write exactly one report and edit nothing else:

```text
xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md
```

Include the exact target SHA, model identity, explicit verdict
`CONFIRMED`, `REPAIR`, or `REFUTED`, the smallest failing identity or
missing hypothesis, an independent proof/attack, and a strict scope
firewall.  Source reading and hand derivation only: run no CAS, solver,
substantive Python, Lean, or other heavy local computation.
