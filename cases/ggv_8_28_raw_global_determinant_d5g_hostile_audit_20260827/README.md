# D5G independent hostile audit

This case independently reconstructs the D5G truncated bivariate
determinant from D3's raw support.  It does not import the producer compiler.
It also checks every serialized provenance contribution, uses a closed-form
division by `X^8-1`, uses the closed-form seven-coordinate remainder for
`M(Y)=4HY'+6H'Y`, replays the full producer reduction trace, and strengthens
the `D22 -> D22+H` mutation to its exact four differences.

After `RESULT.json` has been frozen, replay with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B audit_d5g.py --check RESULT.json
```

The audit is limited to the literal generic raw determinant and its two
linear decompositions.  It makes no local-naturality, Keller-specialization,
target, face, family, or JC2 claim.
