# TD6 fixed-A3 q2 `B3=0` repaired source-DAG certificate (V66)

Status: **producer-exact only on the birational `B3=0` chart open**

```text
D(t*w*(t-2)*(2*t-1)*(t^2-4*t+2)).
```

The fixed source-typed center is `(c1,c2,c3)=(C0,V0,U0)` and
`q_beta(t)=t+beta*t^2+t^25`.  To avoid symbol collision, this report calls
the producer's parameter-ring symbols `C,V` by `t,w`.  Its chart is

```text
U0 = w^2 (t-2)^2/(16t)
V0 = w^3 (t-2)^2/(16t)
C0 = w^4 (t-2)^2 (-5t^2+20t-4)/(256t^2).
```

V66 exactly replays current row 13 through previous row `('X-1',14)` and
original first rows.  Row `('X-1',0)` is an independent quadratic positive
control, not an N13 edge.  It also replays genuine P12 directly through
original first rows (counts `2893/28/1649`) and composes it with
`N13=k*beta/25` to the residual `-k/50`.  Omission controls detect loss of
previous row 14, current row 13, and the live N13 correction.

The exact leaf-plus-P12 denominator radical is

```text
{t, w, t-2, 2t-1, t^2-4t+2}.
```

All five factor loci remain separate raw-source obligations.  In particular,
this is not a whole-`B3=0` theorem.  It is not a whole fixed-A3, full-TD6,
SP-2, landing, or JC2 claim, and it does not audit every unused row.

## AWS custody

The same source archive ran under 12 GiB caps on Box02 and r6d:

- Box02 `/home/ubuntu/runs/td6_v66_b3_repaired_box02_20260825T140458Z`,
  `2026-08-25T14:05:34Z`--`14:51:07Z`, rc 0, max RSS 2,111,172 KiB;
- r6d `/home/ubuntu/runs/td6_v66_b3_repaired_r6d_20260825T142013Z`,
  `2026-08-25T14:20:54Z`--`14:54:28Z`, rc 0, max RSS 2,113,008 KiB.

Source archive SHA256 is
`dbb97927b097cf2eb5876f782c2b94cfc8b2830b07fe4db288db8aa13fdfbfe6`.
The two hosts produced byte-identical proof DAG and denominator ledger at
SHAs `3751f623...` and `fc655dea...`; stdout differs only in absolute
artifact paths.  Run `python3 verify.py` for the lightweight custody/scope
gate.  No heavy computation is performed by that verifier.
