# Actual-total all-row grade-13/14 source export V20

Date: 2026-08-27

Status: **PREREGISTERED AWS PRODUCER; NO MATHEMATICAL VERDICT YET.**

## Question

The frozen actual-total prefix through grade 12, together with `Tg14_5`, has
exact `Q[rho]` zero-sections

```text
CS0: cs=1; every other source variable except rho is zero,
A00: a0=1; every other source variable except rho is zero,
A10: a1=1; every other source variable except rho is zero.
```

On `J1=(rs,cs,c0,c1)=0`, twelve of the 22 rows survive but both `A00` and
`A10` still kill every row.  Before starting a second-stage Groebner search,
export **all seven** literal actual-total source rows at grades 13 and 14 and
ask whether any new row is nonzero on `A00` or `A10`.  Also test `CS0` and
the terminal-origin section `Z00`, where every source variable except `rho`
is zero.

## Frozen producer contract

1. Reconstruct the literal total moving-`p` emitter from the independently
   reviewed sparse arithmetic module and all 569 frozen canonical tails.
   Row `j` must satisfy the exact tail-weight contract `12+j`.
2. Before exporting anything new, reproduce all 21 V9 coefficients
   `Tg10_1..Tg12_7` exactly in an ordinary Singular ring, over `Q` and
   `F_65521` independently.
3. Reproduce the already reviewed `Tg14_5` V17 polynomial byte-for-byte in
   each characteristic.
4. Export `Tg13_1..Tg13_7` and `Tg14_1..Tg14_7`, including an explicit zero
   polynomial if a coefficient vanishes.  Record hashes, term counts, and
   variable supports.
5. Assert rho-deck evenness of every exported coefficient.
6. Evaluate the exact sparse polynomials, before characteristic reduction,
   on `CS0`, `A00`, `A10`, and `Z00`, retaining `rho` as an indeterminate.
   Record every nonzero residual exactly; do not turn a point test into an
   ideal-membership claim.
7. Perturb by `+1` the coefficient of one frozen tail monomial whose induced
   grade-10--12 delta is nonzero over both `Q` and `F_65521`; the corresponding
   V9 bridge must then fail.  This is the source-sensitivity control.
8. Run only as registered, capped AWS EC2 jobs.  No qring, randomization,
   local CAS, or access to `jc2-lean` is permitted.

## Interpretation fixed before output

- A nonzero `A00` or `A10` residual kills only that explicit zero-section and
  names the first bounded row through which the corresponding `J2` chart can
  receive source information.  It does not prove that `a0` or `a1` belongs to
  a radical and does not empty a Rees chart.
- If both sections persist, grades 13--14 cannot remove the reviewed prefix
  obstruction; the next source action must move above grade 14 or change the
  route.
- A nonzero `CS0` residual is information about the off-unit-load sibling,
  not about the registered unit-`k10` family on `D(k)`.
- A nonzero `Z00` residual only kills the displayed terminal-origin section;
  it does not close the terminal receiver.
- No output proves Gate T, order two, maximum twelve, or JC2.

