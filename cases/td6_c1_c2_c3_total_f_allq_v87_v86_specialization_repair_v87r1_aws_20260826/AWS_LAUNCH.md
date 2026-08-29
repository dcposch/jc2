# TD6 V87R1 authoritative dual-host launch record

Date: 2026-08-26

Source archive SHA-256:
`c7933417e0d0ad2e69a99a2a982a3a2cf2d670eecf0b018f72ac8ea402675a78`.

Frozen V87R1 client SHA-256:
`5227b6763aca6833c8aab117337f74c45b0be89b6112b0c35f0b6580c1143237`.

Frozen source manifest SHA-256:
`a0c4421bf52784cd949a649bb09a9045de8bb13f84c22f087245becba7967614`.

## Box02

- endpoint: `34.203.207.55`;
- run root:
  `/home/ubuntu/runs/td6_v87r1_v86_specialization_v1_box02_20260826T155316Z`;
- registered start: `2026-08-26T15:53:49Z`;
- finish: `2026-08-26T16:03:06Z`;
- elapsed: 9:16.96;
- maximum RSS: 1,173,092 KiB;
- swap: zero.

## r6d

- endpoint: `100.26.198.153`;
- run root:
  `/home/ubuntu/runs/td6_v87r1_v86_specialization_v1_r6d_20260826T155316Z`;
- registered start: `2026-08-26T15:53:49Z`;
- finish: `2026-08-26T16:02:55Z`;
- elapsed: 9:06.28;
- maximum RSS: 1,172,144 KiB;
- swap: zero.

Each lane used a 64 GiB virtual-memory cap, a 43,200-second timeout, exact
ascending/all-staged transport custody, and the full untruncated V87 q ring.
Both returned `rc=0`.  Mathematical stdout and all four output files are
byte-identical; host metadata and timing records remain distinct.
