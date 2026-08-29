# TD6 V89H5 q14-plus-high unimodular inverse preregistration

Date: 2026-08-26

Status: producer theorem candidate; no result claimed before dual AWS replay.

## Scope and lead

Set `q2,...,q13=0`, keep q15 absent under the reviewed target shear, and
retain independent untruncated `q14,q16,...,q24`.  Rebuild literal V87
transport, all 38 packed raw FIRST maps, and genuine raw P12 from frozen
source bytes.

V89H3 found that the reviewed q-zero FIRST pivot block has one cyclic SCC,

```text
S = {0,1,2,3,4,5,6,13},
```

and that its q14-axis determinant has degree zero and constant coefficient
one.  This observation is preregistered only as a lead: V89H5 must test the
full retained-q block and construct the inverse explicitly.

## Exact inverse gate

1. Recompute the support graph and require S to be its only cyclic SCC.
2. Extract the full 8 by 8 S block, audit all retained q support, and compute
   its determinant by division-free subset DP.  Fail unless the determinant
   is exactly the constant polynomial one.
3. Construct the exact adjugate S-block inverse, emit every nonzero
   coefficient, and verify both matrix products.
4. Split the 38 by 38 FIRST block into this diagonal S block plus singleton
   diagonal blocks.  Topologically order the SCC condensation graph,
   construct the remaining finite polynomial inverse, emit every nonzero
   coordinate of the full inverse, and verify both products with the literal
   FIRST pivot block.
5. Replay the normalized rows against the original 38 FIRST sources.  No
   determinant, q expression, F, K, or other polynomial may be inverted.

## P12 and total-F gate

Only after the inverse gate passes, reduce literal P12 and replay every
multiplier in original-source coordinates.  If the remainder is not exactly
the frozen q-zero unit, emit the first obstruction and make no collapse
claim.

If it is the unit, audit the complete rational common denominator.  Write it
exactly as `K^n*A`, require `n>=1`, and require every factor of A to be
registered on `D(U H B3)`.  Clear the relation coefficientwise.  Compose it
without division by K using

```text
B3 = K + 2*F*G,       G = 2*C*U - V^2 + 2*U^3,
B3^n - K^n = 2*F*G*sum_{i=0}^{n-1} B3^(n-1-i)*K^i.
```

Emit the resulting P12/FIRST/F identity with target `A*B3^n`, all exact
multipliers, its denominator ledger, and omission controls for P12, one
active FIRST source, and F.

## Fail-closed scope

Require byte-identical mathematical output and artifacts on Box02 and r6d.
The strongest possible result is a literal total-F identity on this exact
ten-q residue block.  It is not a P12/FIRST-only collapse, a cover of any
q2-through-q13 unit chart, a total-Rees theorem, a source point, whole fixed
A3, TD6, SP-2, or JC2 result.
