# V88Q15 authoritative V1 dual-host launch record

Date: 2026-08-26

Source archive SHA-256:
`46dee1d1333c721ef7776849603c81053466d7310e57c453fef6587b1f8871a6`.

Frozen V88 client SHA-256:
`402dc792ac565dd1da40a26df4d8257fa02e571caf2bc00740280467e6c99169`.

Frozen V87 client/result/source-inventory pins:

```text
7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463
6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda
079447d97638f18b7807cdd84b1178f9969d3f93727c7ab40588079586160a68
```

## Box02

- endpoint: `34.203.207.55`;
- run root:
  `/home/ubuntu/runs/td6_v88q15_total_shear_v1_box02_20260826T154500Z`;
- fleet supervisor PID: `285294`;
- lane supervisor PID: `285298`;
- registered start: `2026-08-26T15:43:47Z`;
- finish: `2026-08-26T15:46:02Z`.

## r6d

- endpoint: `100.26.198.153`;
- run root:
  `/home/ubuntu/runs/td6_v88q15_total_shear_v1_r6d_20260826T154500Z`;
- fleet supervisor PID: `294999`;
- lane supervisor PID: `295003`;
- registered start: `2026-08-26T15:43:47Z`;
- finish: `2026-08-26T15:46:04Z`.

Each lane used a 64 GiB virtual-memory cap, a 21,600-second timeout, exact
ascending/all-staged transport custody, and the full untruncated
`q2,...,q24` coefficient ring. Both returned `rc=0`, used zero swap, and
emitted byte-identical mathematical stdout and output files.
