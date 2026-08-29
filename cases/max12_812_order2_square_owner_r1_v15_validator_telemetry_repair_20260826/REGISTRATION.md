# Registration: order-two square `r=1` V15 validator telemetry repair

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS VALIDATOR-ONLY REPLAY.  NO D1,
SQUARE-BRANCH, OR ORDER-TWO VERDICT.**

V14's fresh exact-Q and `F_65521` source inputs each produced every required
mathematical marker exactly once, with no Singular diagnostic, and returned
engine `rc=0`.  Its validator nevertheless failed because it rejected every
nonempty stderr file, while `ops/aws_exact_lane.sh` intentionally records
benign `/usr/bin/time -v` telemetry there.

V15 pins and invokes the frozen V14 compiler without changing its Singular
input.  It changes only validation: time telemetry is allowed, while `=FAIL`,
`// **`, a leading Singular `?`, or `error occurred` is rejected in either
stream.  Missing or duplicate markers, timeout, and nonzero engine return
remain fatal.  Run exact Q on Box03 and `F_65521` on r6d with 24-GiB
virtual-memory, 600-second compile, and 1800-second engine caps.

