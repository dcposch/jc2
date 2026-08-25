# TD6 q2-beta rational raw-line closures — AWS exact replay

## Verdict

**PRODUCER-EXACT PASS on all three whole lines; hostile review pending.**

In the fixed source-typed A3 section, exact AWS rebuilds exclude for every
beta the lines

```text
V=0,C=3U^2;   V=0,C=-U^2;   V=0,C=-5U^2.
```

The first and third have full genuine-P12 plus staged-N13 polynomial unit
identities with only powers of `U` in all source denominators.  The middle
line is already inconsistent in the first band: rank `37/132`, one
`('X-2',12)` dependency, compatibility gcd one, exact 13-row source Bezout
replay, and complete denominator `U^6`.  The V45 rank-38 assertion failure is
retained as a fail-closed harness control; V46 is the theorem-producing
adjudication.

Each `D(U)` line is therefore empty, and its parameter-zero endpoint is
covered by the separately frozen all-beta `U=0` theorem.  These results close
the residual `V=0` rational branches needed by the live all-beta `H/B3`
atlas.

The immutable package is
`cases/td6_c1_c2_c3_q2_beta_rational_raw_lines_aws_20260825/`.
No generic-divisor, fourth-modulus, whole-TD6, SP-2, landing, or JC2 claim is
made here.
