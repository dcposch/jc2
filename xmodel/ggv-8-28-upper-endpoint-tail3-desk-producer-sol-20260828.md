# Producer report: cutoff-three upper endpoint desk reduction

Status: provisional exact producer packet; AWS successor frozen, not run.

Packet:
`cases/ggv_8_28_upper_endpoint_tail3_desk_20260828/`.

The authoritative raw branch-P system was independently specialized by
zeroing only weight-two coordinates.  The exact compile has 296 retained
variables, prefix rank 40/nullity 256, and literal endpoint

```text
-1-p32*p189+p86*p91=0.
```

No endpoint carrier is normalized.  The squarefree cascade through `D15`,
all literal source-row cofactors, the corrected `E13,E14,E15`, and every later
compatibility through `D22` are in `TAIL3_DESK_ANALYSIS.json`.

The first failure of the naive shifted-cutoff-five core is the exact `D14`
residual

```text
-(3/64)*V0*Q0*L0 -(3/8)*R0*Q0^2.
```

After quotienting the 17-dimensional `D21` root core by the degree-one ideal
module of actual `E13,E14,E15`, the quotient is one-dimensional.  Its exact
representative is

```text
K=Q0*(b_bar*Q0+L0^2),  b_bar=p189-V0*R0/16.
```

`K` is not in the cumulative span through `D16` and first has an exact
13-term ideal/source witness at `D17`.  A sign mutation of `L0^2` is rejected.
The three scalar field branches of `K` and their exact reductions are frozen
in the target JSON.

Routing is exact: `T=(X^4-1)V`, hence `T=0` iff `V=0`.  The zero branch is the
cutoff-four packet and remains review-dependent here.  The new `V!=0` branch
has a six-localization AWS cover.  The default necessary target has 56
variables, 36 generators, and 120,823 terms; the full exact fallback has 125
generators and 403,266 terms.  A three-branch root-core diagnostic precedes
the endpoint jobs.  Exact custody is split into pinned ordered pairs
r6a:{0,1}, r6c:{2,3}, and r6d:{4,5}; no exact-all invocation is licensed, and
only the fail-closed combined manifest is coverage-complete.

Requested hostile-review checks:

1. replay every field-radical implication from the literal rows, especially
   the corrected `D12` and `D14-D15` square remainders;
2. re-expand the 13-term `D17` cofactor witness for `K` and confirm quotient
   dimension one;
3. audit `p161` as a genuine globally absent additive gauge;
4. audit the `T=0` iff `V=0` handoff and do not import cutoff-four closure
   without its separate review;
5. inspect the AWS core/full semantics, six-chart coverage, restored literal
   `c` relation/endpoint, and fail-closed resource guards before launch.

The rejected external five-mode/full-fixture reduction is not used; the
literal staged source retains the forced `c14,c16,c18,c20` coefficients.

Replay:

```bash
cd cases/ggv_8_28_upper_endpoint_tail3_desk_20260828
python3 analyze_tail3.py --check --output .
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
```

No local CAS and no AWS job were used by the producer.
