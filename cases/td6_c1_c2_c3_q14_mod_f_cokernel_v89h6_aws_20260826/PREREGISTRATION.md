# TD6 V89H6 splitting-independent q14 class modulo F preregistration

Date: 2026-08-26

Status: producer theorem candidate; no result claimed before dual AWS replay.

## Question and literal scope

Set `q2,...,q13=0`, keep q15 absent only under the separately reviewed
target shear, and retain independent untruncated `q14,q16,...,q24`.  Rebuild
literal V87 transport, the 38 original packed raw FIRST maps, and genuine raw
P12 from pinned source bytes.

Work on the divisor

```text
F=C*U-V^2+U^3=0
```

inside the registered open `D(U*H*B3)`.  Since U is registered, use the exact
two-sided coordinate identification `C=(V^2-U^3)/U`, but do not infer any
class statement from the V89H5 chosen generic splitting.

## Exact-Q cokernel gate

1. Audit every literal raw-source denominator before specialization and fail
   if it contains F or an unregistered factor.
2. Specialize all raw P12/FIRST coefficients coefficientwise at F=0.
3. Choose 38 pivot section variables from the specialized q-zero FIRST
   matrix, compute an exact two-sided inverse of the full retained-q pivot
   block, including every cyclic SCC, and refuse all nonconstant q inverses.
4. Normalize the 38 rows as exact combinations of all 38 original FIRST
   sources.  Verify the pivot identity and original-source replay.
5. Divide specialized literal P12 by these monic rows.  Emit the complete
   remainder and its positive-q class, and verify no chosen pivot variable
   survives.
6. Require the q-zero remainder to be a scalar unit.  Decide whether the
   positive class is zero.  A nonzero canonical remainder is a
   splitting-independent nonzero class over `Frac(Q[V,U])`, hence it cannot
   vanish over the smaller registered localization.  A zero class must come
   with the full original-FIRST relation.

This is a cokernel/class gate, not by itself a unit-ideal or source-point
theorem.

## Independent good-prime gate

In a separate arithmetic implementation, reduce the 18-dimensional E-field
multiplication table modulo the good prime `p=1000003`, at

```text
(U,V,C)=(1,3,8), F=0, H=5, B3=81.
```

Independently invert the evaluated original-FIRST pivot matrix at q14=0 and
q14=1 (all q16,...,q24 zero), normalize, divide P12, and compare the two
remainders.  The difference must equal the evaluation of the exact-Q
positive class.  Emit the first nonzero modular witness.  Failure of any
finite-algebra pivot to be a unit is a closed failure, not permission to
change prime or point after seeing the answer.

Both Box02 and r6d must run both arithmetic paths from the same immutable
literal source archive, with byte-identical mathematical output/artifacts.

## Firewall

Neither outcome covers low-q unit charts, an independent q15 source modulus,
total-Rees/source lifting, omitted correction or moving-center variables, a
source point, whole fixed A3, TD6, SP-2, or JC2.
