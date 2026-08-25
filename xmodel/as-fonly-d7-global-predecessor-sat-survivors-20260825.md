# AS F-only `D=7`: three exact global-predecessor terminal-gate survivors

**Status: PRODUCER EXACT / DIRECT INTEGER REPLAY PASS; PROVISIONAL PENDING
FOCUSED DIFFERENT-MODEL SOURCE-TO-FORMULA AND REPLAY REVIEW.**

The exact 79-structural-base falsification race has produced three SAT
states.  Each is on a structural base with one accepted corrected-Q10
predecessor and 43,046,721 accepted Q9 completions:

| base | structural digits | formula SHA-256 | model SHA-256 | replay JSON SHA-256 |
|---:|:---:|:---|:---|:---|
| 303 | `0102020` | `1ed0efc49b2b1cf1f1cd3f171f4fb6a361d85e34918eb34b827dc710b642c6b7` | `16bbac68d8db1551d0e9e2b131b9337a2b6c35cf2d11a3bddbe94771fe10d4f6` | `da9ab0f27ff7cb7926b38677ed66827fcdc9c6ab6f260364eb41fcb0e9852760` |
| 513 | `0201000` | `5aae4f2817bab998466630293118866b3b6967e87c16d85514d08db367bbd2eb` | `e857efac30af976846f79036e99d9fb28721482450f4cf13c7629cd849d8b925` | `3c78da43ce8c1812320bb3a45747e20d0148ba0e7cc45e7cdd41d653d71f9d16` |
| 519 | `0201020` | `1c92d5bff3fb8acb88671ee4a2ed0117829f0b7fb6778176f2b52ea5319401bd` | `b4bf0cc46f3bd204f2418abf6aa4181f9c84a05d6bd6aca38d928f674133ae2e` | `f4e79878d906a4c442b6ec25ca40d4d098b00e6cc87703911411e6e13994a388` |

For every state, an independent literal-integer reconstruction verifies:

```text
20 predecessor rows = 0
corrected top-row shapes 5,12,11 = 0
23 Q9 source rows = 0
22 Q8 source rows = 0
19 Q7 source rows = 0
recursive carry = literal (det J(P,Q)-1)/243
46 terminal rows in degrees 12,11,10,9 = 0.
```

The designated successor is base 519.  Its exact decoded state is recorded
in the case README and `direct_replay.json`.  Boolector found it in 5:35.79
using 1,426,176 KiB maximum RSS on Box02; the independent replay used 21.17 s
and 21,716 KiB.

This is positive bounded evidence, so no SAT proof trace is needed: the
literal integer replay is the certificate.  It falsifies global emptiness at
this displayed gate and invalidates any attempt to aggregate the per-base
UNSAT lanes into an exclusion.  It does **not** yet solve Q6, degrees 8 and 7,
or the following Cartier/divided-carry equation.  It is not an all-depth
formal lift, an algebraization, a fixed-support characteristic-zero map, a
counterexample, or a JC2 conclusion.
