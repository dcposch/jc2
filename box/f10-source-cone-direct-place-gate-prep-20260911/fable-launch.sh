#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 01:41:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
e6df0a6458c682128c841a054e4cfb0be00cb2efde0325743f197cdcb0564725  xmodel/f10-source-cone-direct-place-astra-20260911.md
747154de042e27a6593e5b3f3fe7579b8bf4720328cdd77085b422ab03e4c715  box/f10-source-cone-direct-place-astra-20260911/READ-SCOPE.md
77a7cb4f3ea31940419f96692c6db29866671e003c6c88e35ff0111f0e980e3a  box/f10-source-cone-direct-place-astra-20260911/custody.json
8b8c6296f3e94b0b176631d848bfe0cca11ba6eac64877196d0a129df212f30a  xmodel/f10-source-cone-r3-code-astra-20260911.md
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  box/f10-source-cone-r3-code-astra-20260911/produce.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  box/f10-source-cone-r3-code-astra-20260911/check.py
10e57542f9aa06eb69fd9562b2aa0bb27567c6d14186ffa90d77d6e08e80ae2c  box/f10-source-cone-r3-code-astra-20260911/check_arithmetic.py
712ac6023b6799c079e5b950822d07c20295d46788f38d64a433af7f45cd3103  xmodel/f10-source-cone-r3-code-gate-fable5-20260911.md
11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b  xmodel/f10-source-cone-fullrank-place-astra-20260911.md
6e73b5b992fb75d456c71928cacf980f30d0065117e8875403438c12e49112bc  xmodel/f10-source-cone-fullrank-place-gate-fable5-20260911.md
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  xmodel/ideation-20260910T2300Z-astra-source.md
40b18453b6127d1b8217a6d6e1d3eb3aff1e911c15243ed9c640277f24175431  box/f10-source-cone-r3-code-astra-20260911/arithmetic.py
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
d44153d5f4b8dfff3c926c7b1f55d407e7043fc733bfd0150e01c543f20a95ea  box/f10-source-cone-direct-place-gate-prep-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/f10-source-cone-direct-place-gate-fable5-20260911.md
test ! -e xmodel/f10-source-cone-direct-place-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-source-cone-direct-place-gate-fable5-20260911.log
test ! -e box/f10-source-cone-direct-place-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3directplace-term-20260911 --on-calendar='2026-09-11 02:00:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3directplace-kill-20260911 --on-calendar='2026-09-11 02:00:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3directplace-term-20260911.timer jc2-f10-r3directplace-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-source-cone-direct-place-gate-fable5-20260911 box/f10-source-cone-direct-place-gate-prep-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-source-cone-direct-place-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
