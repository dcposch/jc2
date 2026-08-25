# B9 complete fixed-D12 quadratic gate at modulus `3^11`

This package consumes the exact `3^165` family modulo `3^10` over the
displayed B9 mod-243 parent and tests its complete transition to
`3^11=177147`.  Both coordinates use the full total-degree-12 monomial
simplex.

For `F=F5+243*T+3^10*W`, all 276 determinant rows are

```text
(D5 + 243*A*T)/3^10 + det J(T) + A*W = 0  (mod 3).
```

The compiler first quotients by the rank-108 fresh-digit image, then changes
the 165 predecessor coordinates into 18 directions visible modulo three and
147 directions divisible by three.  The latter have rank 56 in the
168-dimensional fresh cokernel.  The complete constant/linear/quadratic
coefficient space has rank 16, and adjoining it does not increase rank 56.
Thus every coefficient lies in the spectator image and the final quadratic
Kuranishi system has zero equations.

Consequently exactly `3^109` predecessor points lift, and every such point
has `3^74` fresh lifts: the complete displayed lift family has cardinality
`3^183`.  A literal witness replays all 276 integer determinant coefficients
modulo `177147`.  Its honest partial-y and total-degree pairs modulo the target
are both `(12,12)`; this package does not establish a `(9,12)` lift.

Box02 and Box03 V4 results are byte-identical at SHA-256
`7a1b5da26974ee5e5f4fb42ade1575abc0b18d9de54349c8fdcc08ab4a267379`.
The V2 missing-helper failure and V3 false `(9,12)` assertion are preserved as
deployment/source-scope negative controls.  The earlier V1 result is not the
frozen producer because it lacked the degree and containment audit fields.

This is a finite-depth theorem over one fixed B9 mod-243 parent.  It is not a
mod-`3^12` result, an all-depth branch, a characteristic-zero point, a
maximum-twelve theorem, a counterexample, or a JC2 result.

Heavy replay is AWS-only under the campaign resource policy.  From a staged
source closure, run `run_aws.sh` with `JC2_ROOT`, `OUTPUT_JSON`,
`PARENT_REPLAY_JSON`, `ANF_OUTPUT`, and `SMT2_OUTPUT` set to explicit paths.
