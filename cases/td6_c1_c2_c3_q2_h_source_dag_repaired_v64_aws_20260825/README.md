# TD6 fixed-A3 q2 H-divisor repaired source-DAG certificate (V64)

Status: **producer-exact localized source identity on
`H=0, D(U V P3 QH)`; the four complementary factor strata remain separate.**

Here

```text
H  = C - 3 U^2,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 + 8 V^2 U^3 - 64 U^6.
```

The fixed source-typed center is `(c1,c2,c3)=(C,V,U)` and the transverse
boundary source is

```text
q_beta(t) = t + beta t^2 + t^25.
```

V64 is the nonmutating repair successor to V60 required by the hostile
review in
`../../xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-review-grok-20260825.md`
and the custody erratum in
`../../xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-erratum-20260825.md`.
It preserves arbitrary-degree original source rows and replays the unique
N13 current row 13 through exactly the previous row `('X-1',14)` and the
original first rows.  The cached quadratic row `('X-1',0)` is replayed as a
separate positive control and is explicitly not an N13 ancestor.

The genuine V44 P12 relation has 2,885 terms, 28 nonzero first rows, and
1,640 multiplier terms.  Its direct original-row replay composes with N13
to give the exact unit residual `-k/50`.  Omitting previous row 14, omitting
the singleton current row, and omitting the live N13 correction from P12
all provide exact negative controls.

The complete leaf-coefficient plus V44 termwise-clear denominator ledger
has radical support

```text
{U, V, P3, QH}.
```

Consequently this package certifies only the localized H-divisor open
`H=0, U*V*P3*QH != 0`.  It does not cover `U=0`, `V=0`, `P3=0`, or `QH=0`,
and it does not prove a whole-H, whole-fixed-A3, TD6, SP-2, landing, or JC2
statement.

## Exact AWS custody

The source archive was run on r6d `100.26.198.153` under a 12 GiB cap:

- remote path:
  `/home/ubuntu/runs/td6_v64_h_repaired_r6d_20260825T1333Z`;
- UTC interval: `2026-08-25T13:33:12Z`--`2026-08-25T14:00:56Z`;
- exit code: `0`;
- maximum RSS: `674204` KiB;
- source archive SHA256:
  `1a2e4f6766ffe5b15b963dd6ac86c02d538eb3e6d45b27d4a5a99e3c87a7aac6`;
- source manifest SHA256:
  `777551c9ecff94cc98e16e8d076bffee7171e37e9690914b66d440615f9b53c7`;
- stdout SHA256:
  `14775e9ad4adfb0a20512823be01bdd48da711e30b8ac7796e094841f41edd06`;
- proof-DAG SHA256:
  `ef721416a7aac4f97167003801bfe94033e0b6627942d4ba9269c5565d9a962e`;
- denominator-ledger SHA256:
  `259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385`.

Run the lightweight custody and marker check with:

```bash
python3 verify.py
```
