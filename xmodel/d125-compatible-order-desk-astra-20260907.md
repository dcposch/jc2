# D125: a compatible five-row order, desk reserve only

2026-09-07, root/Astra. **PRODUCER-CHECKED; conditional on the provisional
three-row B-order statement, not promoted or execution authority.** The
current three-row implementation and its independent gate remain unchanged.
This is a possible later comparison, not a reason to delay that experiment.

## Claim and proof

Use the same unequal/Q 269 variables and 803 original equations. Keep W1,
W2 and W3 from the terminal defect-order report. Before its final dp tie-break,
append W4(A_ij)=15-i-j and W5(A_ij)=-i, both zero on B and both lambdas.
The first weight stays strictly positive on every variable, so the negative
entries of the later W5 do not prevent a global multiplicative well-order.

These refinements expose the 27 reviewed A-Hermite pivots as single-variable
leading monomials, while preserving all 192 proposed B leaders. Thus the
full ideal contains polynomials with 219 distinct variable leading monomials.
The complement has 50 variable names (44 retained A, four B kernel scalars,
two lambdas), **not a proved dimension**. No variable, equation, fixed face,
parameter, target gauge or coefficient field is changed.

For an A-negative lift row R_(s,t)=[u^t v^(5t-s)]phi(A), the reviewed
multinomial law gives k=i+j=s+3b+2d for a term
A_ij*lambda2^b*lambda3^d. If A_ij is free, that term has

    W1=15-k+3b+2d=15-s.

All its W2 and W3 entries are zero. If b+d>0, W4=15-k<15-s, so the term is
smaller than every degree-s free A variable. A fixed coefficient of degree
k<15 instead lowers W1 by 15-k. For a fixed top coefficient k=15, W1 can
tie, but W4=0<15-s. A same-layer fixed coefficient is a scalar and is also
smaller. Thus every forcing term is smaller, including nonzero prescribed
faces; zero prescribed terms simply vanish.

At 1<=s<=14 put r=ceil(s/5). The selected free columns are i=0,...,r-1.
The constant matrix of the r rows t=0,...,r-1 is

    M_(t,i)=(-1)^(s-i-t)*binom(s-i,t), det M=+1 or -1.

This is the accepted consecutive-node Hermite minor. Multiply those r
original rows by its constant inverse. Each resulting polynomial has its
own selected A variable plus same-layer unselected columns i>=r and the
strictly lower forcing above. W5=-i puts every selected variable above
every same-layer unselected one. Consequently its leading monomial is
exactly that selected A variable. No descending substitution or expanded
residual is needed for this leading-ideal conclusion. The count is
sum_(s=1)^14 ceil(s/5)=27. The three fixed top A rows remain identities.

For the B relations, the three-row proof already separates all forcing
by W1/W2 and every same-layer kernel alternative by W3. Appending W4/W5
cannot reverse a comparison decided earlier. It therefore retains its
192 B-variable leaders, conditional on that currently reviewed statement.
All 105 lift rows, every Jacobian compatibility/low row and the target stay
in the ideal. A proper ideal's Groebner basis must contain each of these
variable leaders, since the only smaller divisibility alternative is 1;
this does not prove the ideal proper or predict discovery cost.

## Dependencies and tiny discriminator

Read wholly and hash-bound:

- B-order report `xmodel/d125-defect-order-discriminator-astra-20260907.md`,
  SHA `9b6f972b2513094fe5fe33cf41721eb971e494a6762915bfda5c31e8a4e77d9b`.
- Accepted A-Hermite producer `xmodel/d125-lift-hermite-pivots-astra-20260906.md`,
  SHA `b6a81fc0c925d63f13f72d4b8ee1203adcecb8a6f4dc349f8c2a62d5805cf126`.
- Its Fable gate `xmodel/d125-lift-hermite-gate-fable5-20260906.md`,
  SHA `7e2594d53150bf4346f4e4cc6e7f6ff05a021b045b640128de763cc653a8a8ca`.

The owned check uses the frozen small baseline map and three-row witness
with in-code hashes, not full source streams. It checks all actual selected
A slots, all 14 integer minors (size at most3), the finite degree/weight
inequalities and same-layer comparisons. Setting W4 to zero reverses the
actual comparison A_g0_p1 versus lambda3*A_g0_p3; reversing W5 reverses
A_g0_p2 versus A_g1_p1. Both changed objects reject normally and under-O.
All six runs took1.55seconds with per-process30wall/25CPU/512MiB caps;
the checker and imported baseline have no Assert nodes. Higher-degree
polynomials and the full Jacobian/lift rows were never expanded.

Artifacts in `box/d125-compatible-order-desk-20260907/`:

- check.py: `f139eb51d690c350426f1a19d27de7d3cb097029c06cb775dbf7ee6531d66ca1`.
- witness.json: `86804185bbaba641f2a3305dd379aa06e2f85a5f833233c79a10b575c0be67f6`.
- replay.json: `e661c9d613c75bbafb97145e7c7889844e6a194ad041f08fb6f4d313572b1e4d`.
- Five-row descriptor: `97fc8241f29feb174bc829cebb226c03f3d1df92541fc620b74489f0fd18aa25`.

## Decision

Reserve this as a conditional desk option. Do not replace the three-row
descriptor or implementation while its gate is running. A future use needs
a narrow different-model delta review, order-aware descriptor binding and
an actual engine control. No CAS/AWS/solver, new mathematical exclusion,
properness, speedup or JC2 conclusion. No further fanout; all root writers
are finished before transactional close.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5140`.
- Body SHA-256:
  `a498a88a4be069eef7a949409dee7efc2ce01bc98b2e534c511464a911a9dbb4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
