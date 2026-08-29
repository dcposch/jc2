Act as an independent mathematical researcher on the live generic-square
branch of the plane Jacobian campaign in `/Users/dc/code/math/jc2`.  This is
an ideation/derivation lane, not a reviewer endorsement.  Read completely:

```text
xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md
cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md
xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md
xmodel/max12-812-order2-square-a-prolongation-design-20260826.md
cases/max12_812_order2_square_a_prolongation_20260826/RESULTS.md
cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/RESULT.md
xmodel/cross-pollination-order2-square-normalized-rees-20260826T0640Z.md
xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
```

Do not run Bash, Python, Singular, Sage, Lean, msolve, or any CAS.  Work by
hand and do not edit existing files.  The adapter permits only reading and
writing the one requested report.

After the reviewed half-weight ray, use

```text
Lambda=sigma^2,
K=L^2+sigma^2 R,        L=z^2+p/2,
D=L A+C,
f=K^2+sigma^5 D,
R,C in sigma*K[[sigma]][z],
deg_z A,deg_z R,deg_z C <= 1,
k10=sigma^4*k(sigma),   k(0)!=0.
```

The fixed-`L` negative expansion through absolute grade fifteen appears to
be, modulo `O(sigma^16)`,

```text
(3/8)sigma^10 * (
   2AC/L + C^2/L^2
  -sigma^2*R*A^2/L^2
  -2sigma^2*R*A*C/L^3
  -sigma^2*R*C^2/L^4)
+(5/16)sigma^10*k*R^3/L
+(5/8)sigma^11*k*C*R/L
-(5/32)sigma^13*k*A*R^2/L^2
+(5/32)sigma^14*k*A^2/L
+(5/16)sigma^14*k*A*C/L^2
-(1/16)sigma^15*A^3/L^3.
```

First verify or correct this formula from the binomial expansions of
`f^(3/2)+sigma^4*k*f^(5/4)`; explicitly charge every omitted load and every
polynomial term.  The term `-sigma^2 R C^2/L^4` is the known reason a naive
universal modulo-`L` grade-fifteen argument fails when both corrections start
at order one.

Then solve the strategic problem as far as possible:

1. Establish whether the correction orders `r=ord_sigma R` and
   `c=ord_sigma C` may be taken as positive integers in this normalized ray,
   or whether ramified arcs require rational cones with a different
   normalization.
2. Classify the complete lowest-weight fan, including every tie.  The first
   candidate weights are `10+c`, `10+3r`, `12+r`, and `14`; explain why the
   other displayed monomials cannot be initially minimal.
3. Use squarefreeness of `L` and the degree-one bounds to route strict cones
   and root allocations.  Do not set future corrections to zero.  At each
   next grade retain all fresh coefficients that can cancel the obstruction.
4. Focus especially on the hard low-contact cases `(r,c)=(1,1),(1,2),
   (1,3)`, the `L|A*C` root-allocation faces, and moving `p`.  Determine
   whether the earlier coefficient equations force the `R*C^2/L^4` and
   `R*A*C/L^3` residues to vanish, or whether a real survivor cone remains.
5. Seek a coordinate-free shortcut over `K[[sigma]][z]` using the moving
   divisor `L(sigma)` rather than termwise expansion around fixed `L`, but
   reject it if lower-denominator terms invalidate it.
6. Give the smallest exact-source compiler that could certify all remaining
   cases at once.  Prefer coefficient extraction plus quotient/normal-cone
   identities over one monolithic radical.  Specify needed jet depth,
   variables, localizations, row-transform checks, and fail-closed endpoints.
7. State the strongest theorem currently proved, the sharpest remaining
   mathematical gap, and the highest-value next calculation.  Do not infer a
   square-branch, order-two, `(8,12)`, maximum-twelve, or JC2 result.

Output exactly one new file and no other file:

`xmodel/max12-812-order2-square-fan-independent-analysis-claude-20260826.md`

Make it a self-contained technical memo with corrected formulas, a complete
fan/tie table, proof sketches or explicit counterexamples for each claimed
route, and a ranked next-action list.  End with exactly
`ORDER2_SQUARE_FAN_IDEATION_COMPLETE`.
