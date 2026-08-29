# Custody: reducer-safe quotient-NF endpoint charts R1

Frozen packet:

```text
PREREGISTRATION.md       a0e48107919d0cf3e67db552234d7465cb21acd0508e695e94abef23845278a0
SOURCE_MANIFEST.sha256   8bcf1b34890d98bc498e4db9d46033618d7d1ff32cbac7d7097cd55f30612ccd
SOURCE.tar.gz            4d51223a6c5d9ddb777a1b36b24630a6a66b1ef31b8f3fa8206bf4a5ffeb7a04
build_endpoint_chart.py  8bcb1abaf34b551f72512b96a6acc80850684a8d56f371e1f65e3cc6596517d4
adapter_selfcheck.sing   4b908895e8d283a056dfdbf67735a6dabb2de7fa65b1d8fea26ead691c39b00c
```

Clean execution:

```text
host/IP       ip-172-30-0-106 / 54.224.45.13
instance      i-0f089e64c378f5da3, r6i.4xlarge, 16 vCPU, 128 GiB
job           ggv_quotient_nf_endpoint_charts_r1_20260828T170400Z_i0f089_r2
CPU           1
PID/PGID/SID  5771/5771/5771
UTC           2026-08-28T17:03:37Z..17:04:29Z
resource      2-hour hard cap; 96-GiB address cap; max run RSS 21,392 KiB
swap/orphans  total/free swap remained 0; supervisor exited; no worker survived
```

The frozen remote Singular prelaunch selfcheck passed exact zero/nonzero NF,
Cramer identity, endpoint cross-term, and complement parser fixtures before the
worker launched.  The terminal worker return code and swap-violation marker are
both zero.

Archive custody:

```text
clean terminal archive   1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787
terminal manifest        337037b06d2699f5985d940fc53bab4e875611cc99f5ca8067e8990231ffe441
terminal VERDICT.txt      c7086914e704f6c5aa92f647c7f9390a91fb7d39e48a35486ec3b39384a790c7
prelaunch failure archive a3364c899a489bbe3687567c6e568b55f076998779e29cfee825e903877d178d
```

All 259 ordinary extracted manifest entries replayed.  Twenty-two AppleDouble
`._` source metadata entries are restored by local bsdtar as extended
attributes instead of standalone files; the exact terminal archive SHA is the
authoritative custody for those metadata records.  No mathematical output is
among them.
