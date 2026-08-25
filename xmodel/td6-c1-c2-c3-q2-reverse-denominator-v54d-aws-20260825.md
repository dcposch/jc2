# TD6 fixed-A3 q2-beta reverse denominator diagnostic (V54D)

Status: **PRODUCER-EXACT DUPLICATE AWS DIAGNOSTIC; NO COVER CLAIM**

V54D repairs the V54B process-address serialization defect and the V54C
reporter-namespace failure.  Two independent AWS runs from source archive
SHA256 `0386b2c7d6b199cf5a287c0826540cf48f853b3b926bcf1d9ddb8a6c80d67983`
completed with rc zero.  Their mathematical stdout is byte-identical, SHA256
`01112ab9578ce9737eba99ab7ebd0f482a007579ab3e0df76da7841635a94450`.
The canonical pivot table and pivot product are also byte-identical, with
SHA256 values
`77cafdf8facdd721e79b00a2dd4fee0d66f5374c26a26208c0125191e86cb0ce`
and
`d9b1a00112491ecfb6fb3f941f26fd00afb46b725dbc45b31c4ec710a02bd2e2`.

After the exact rank-3470/3602 transport, the independent reverse/deferred
order finds 32 unit pivots among the 132 post-transport variables, then six
nonunit pivots, giving fraction-field rank 38/132.  Every one of the six
arbitrary-degree original rows replays exactly.  Writing `H=C-3U^2`, their
ordered center-ring coefficient denominators are

```text
U^4 H, U^4 H, U^5, U^4 H^2, U^3 H^4, H^8.
```

The final canonical coefficient denominator emitted by the producer is
`U H^8` (expanded polynomial SHA256 `503718df...`).  This is an emitted
coefficient denominator, not a claim that it is the least common multiple of
the six rowwise expressions.  The beta-dependent pivot product remains a
nonunit defining this reverse chart.  It is recorded but not inverted, and
the producer explicitly reports `reverse_chart_coverage_inference=false`.

The portable lightweight verifier checks the immutable source archive,
source closure, duplicate byte identity, exact ranks and denominators,
original-row replay, address-free serializer output, and all negative scope
flags.  The AWS runs were:

- Box03 `/home/ubuntu/runs/td6_v54d_canonical_box03_20260825T1053Z`, maximum
  RSS 303,036 KiB;
- r6d `/home/ubuntu/runs/td6_v54d_canonical_r6d_20260825T1105Z`, maximum RSS
  302,368 KiB.

This result is useful denominator-support evidence for a future
rank-stratified constructible source-DAG, but it does not itself provide a
second open chart or cover any reverse-chart exceptional divisor.  It does
not replay the full V50 source identity, kill the generic open, prove an
all-beta fixed-A3 result, or imply any whole-TD6, SP-2, or JC2 statement.
