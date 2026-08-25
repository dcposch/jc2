# Fixed-D12 `(9,12)` order-one binary-cubic first bands

This frozen producer package classifies the first two denominator-free
homogeneous Jacobian bands after the characteristic-zero normalization

```text
P9=K^3,  Q12=K^4
```

for the three geometric root-multiplicity types of a nonzero binary cubic
`K`: triple, double, and squarefree.  It also gives a sharply scoped interface
from one frozen B9 finite-SAT witness to the squarefree type.

## Exact results

| type | degree-18 rank / kernel | degree-17 fresh rank / kernel / cokernel | nonzero projected quadrics / span rank | obstruction-scheme dimension |
|---|---:|---:|---:|---:|
| `L^3` | 11 / 10 | 10 / 9 / 8 | 6 / 6 | 7 |
| `L^2M` | 12 / 9 | 11 / 8 / 7 | 6 / 6 | 6 |
| `LMN` | 12 / 9 | 11 / 8 / 7 | 7 / 6 | 6 |

The exact Singular bases retain nilpotents and all components.  In particular,
none of these first-two-band ideals is the unit ideal, as required by the
zero-lower-face positive control.

For the literal common-cubic witness at SHA-256
`a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`,
the coefficient valuations are `(0,4,5,>=11)`.  The cubic discriminant has a
unique lowest-valuation term `-4b^3`, of valuation 15.  Thus **if that finite
witness has an exact characteristic-zero continuation**, its total-homogeneous
cubic is squarefree.  Fixed total degree 12 independently forces the
partial-`y` Kummer history to order one.  This is a route to the order-one
polynomial-core lane and a scope conflict with the selected order-three Q8
leaf; it is not an all-depth lift.

See `PREREGISTRATION.md` for the registered computation and refusal list, and
`CUSTODY_SUPPLEMENT.md` for the quarantined stale remote self-hash entry.

