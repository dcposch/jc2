# D1 a=8,d=3 isolated `k6 R C` bridge diagnostic — adjudicated

Date: 2026-08-26

## Narrow verdict

The triple-AWS exact diagnostic is computationally **PASS** and the
preregistered fixed-`z` Laurent prediction is **falsified**.  This is not a
defect in the frozen canonical tails and not a defect in the direct source
coefficient substitution.  The missing term is the motion of the inverse
root `z=z(w)` under the `R` perturbation.

Consequently, the earlier a=8,d=3 grade-38 producer remains a no-verdict, but
its rows 4--7 bridge failure has been localized and repaired mathematically.
No cell closure is claimed here.

## Exact derivation

Suppressing the already-accounted sigma powers, put

```
f_0=L^4,                 L=z^2+p/2,
delta_R f=2L^2 R,        delta_C f=C,
alpha=3/4.
```

For the negative Laurent part `q=f^alpha-F_6`, at fixed `z`,

```
q_C=(3/4) C/L,
q_RC=-(3/8) R C/L^3.
```

At fixed Faber coordinate `w`, the inverse root moves by

```
z_R=-(delta_R f)/(partial_z f_0)=-R/(4zL).
```

Therefore the actual mixed tail is

```
q_RC + (partial_z q_C) z_R
  = -(3/16) R C'/(z L^2).
```

The two `RC/L^3` contributions cancel.  In this cell `C'=c1` and
`R=b1 z+b0`.  Since `L=w^2` and
`z=w(1-(p/2)w^-2)^(1/2)`, this becomes

```
-(3/16)c1 b1 w^-4
-(3/16)c1 b0 w^-5 (1-(p/2)w^-2)^(-1/2).
```

Thus, through row 7, the only nonzero mixed coefficients are exactly

```
e4[k60*c1*b1] = -3/16,
e5[k60*c1*b0] = -3/16,
e7[k60*c1*b0] = -3p/64.
```

Every charged `c0` coefficient and `e6[k60*c1*b1]` is zero.  These are the
canonical literal outputs over Q; both finite-field runs are their exact
reductions.

## AWS custody

All three V2 jobs used archive SHA-256
`520e2dde5dd1d7d5b67be4296fce536d3297705bd6059a3eb4d444cdea04f06e`,
returned engine rc 0 and validator
`PASS_A8D3_K6RC_ISOLATED_DIAGNOSTIC`, and recorded zero swap.

| coefficient field | host | immutable tag | stdout SHA-256 |
|---|---|---|---|
| Q | Box02 | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_q_box02_20260826T205500Z` | `9b496cb7ab68530fdb2355832278e224f629c3ad359ae25ced037c685df536a1` |
| F65519 | Box03 | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_p65519_box03_20260826T205500Z` | `1247bc3a4e74f327d5c0aeb0afcb105e0146c93203a4e77b894475ea3677ae3c` |
| F65521 | r6d | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_p65521_r6d_20260826T205500Z` | `8aecf0af84f76da049c3572beeb97191f8a098c2f307edaf22da3d8958d3c15f` |

The V1 archive failed before any mathematical test because Singular parsed a
polynomial power expression as `poly^number`; it is retained only as failed
syntax evidence and is not a verdict.

## Firewall

This artifact adjudicates only the isolated grade-38 `k6 R C` bridge term.
It does not close a=8,d=3, does not alter the already frozen literal-tail
compiler, and does not extrapolate to a=7 or a=9 timing chambers.
