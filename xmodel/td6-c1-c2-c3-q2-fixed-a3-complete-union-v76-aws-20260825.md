# Producer report: fixed-A3 q2-beta complete union (V76C)

Status: **dual-AWS producer-exact; promotion held for V57/V75 hostile
reviews.**

V76C checks the exact constructible cover

```text
Spec Q[C,V,U]
 = D(U*H*B3) union V(U) union V(H) union V(B3),
H=C-3U^2,
B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

Its four leaves and review states are:

| Leaf | Source theorem | Status consumed by V76 |
|---|---|---|
| `D(U*H*B3)` | V57 full original-source N13/P12 DAG | dual-AWS producer-exact; hostile review missing |
| `U=0` | V70 raw three-piece source cover | `CONFIRMED`, review SHA `2a3520866a537a80d17d2f66c2433ba7fcf895606027d755993a1c95402853f6` |
| `H=0` | V71 reviewed five-piece source cover | `CONFIRMED`, review SHA `4ec0f26f5c2b8c497b8cc86548ce9b2acde1481e7eec20c853e931b2ddee40d0` |
| `B3=0` | V75 repaired source atlas | dual-AWS producer-exact; hostile review pending |

V57's complete denominator ledger has radical support only on `U,H,B3`;
its proof-DAG and ledger hashes are respectively
`a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32`
and
`69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf`.
V75 consumes only reviewed V70/V46/V66/V67/V68 plus source-repaired V73/V74.

The checker proves the Boolean cover and four deletion controls.  Its dual
AWS endpoints are:

- Box02 stdout:
  `dd726a31ab48368315d8c449a1967f3dc0b73245d80ed5ba923f4b1848df1847`;
- Box03 stdout:
  `8a7d9aa21cf5eb621aa9983a34fc44cd4526a684fa8437913b99099bcf7ab1a3`;
- shared source manifest:
  `c2ea462aa4418ade7e64fd1dc10e60bada0cb661ad0afb242aad4f60e69417a9`;
- executed replay:
  `dd9bb146e43bf778d83e3b6420442bc4e4b42effd388be75cb3c3d00f609157a`.

The mathematical consequence is provisional but exact at producer tier:
the entire fixed source-typed A3 q2-beta compatibility family is empty for
all beta.  V76 explicitly refuses promotion until V57 and V75 are hostile-
reviewed.

Scope firewall: no additional source modulus varies.  No whole TD6, SP-2,
landing, ceiling, counterexample, or JC2 conclusion follows.
