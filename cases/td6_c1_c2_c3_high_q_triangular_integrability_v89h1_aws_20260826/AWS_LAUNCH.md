# TD6 V89H1 dual-AWS launch record

Date: 2026-08-26

## V1

Archive SHA256:
`395afc049393323966c9a4323642363179e1bcf92fa3b7e2e89a6febc6bb3169`.

Tags:

- `td6_v89h1_high_q_box02_20260826T162000Z`;
- `td6_v89h1_high_q_r6d_20260826T162000Z`.

Both runs returned rc=1 in about 0.1 seconds before algebra because the
wrapper omitted `TD6_Q_EXPONENT=2`. See `DEPLOYMENT_ERRATUM.md`.

## V2

Archive SHA256:
`6869022c70203f1ec7559a599d935f14f425e7ca7663749b000b3e0c55ccdff1`.

Box02:

- tag: `td6_v89h1_high_q_box02_20260826T162500Z`;
- root: `/home/ubuntu/runs/td6_v89h1_high_q_v2_box02_20260826T162500Z`;
- elapsed: 19:15.10;
- maximum RSS: 298,076 KiB;
- swap: zero;
- rc: 1 at the denominator gate.

r6d:

- tag: `td6_v89h1_high_q_r6d_20260826T162500Z`;
- root: `/home/ubuntu/runs/td6_v89h1_high_q_v2_r6d_20260826T162500Z`;
- elapsed: 18:56.97;
- maximum RSS: 297,376 KiB;
- swap: zero;
- rc: 1 at the same denominator gate.

All three partial mathematical output artifacts and stdout are byte-identical
between the V2 hosts. Both stderr streams record the identical extra factor
K and exact common-denominator factorization.
