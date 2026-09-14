#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 02:26:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
5144a325c822952012f5c2b5446c37736445b3228da9728a6fbd26e9e2880f98  xmodel/f10-source-cone-direct-circuit-astra-20260911.md
3be532afc6e784842694cf02d4399573228362abb47ae36130ef97c4274faa59  box/f10-source-cone-direct-circuit-astra-20260911/OPERATIONS.md
61b9ce5e1f9b40a765dcb2a2ea5aa3a928197b61bc41cb5cf945632b99ad4de2  box/f10-source-cone-direct-circuit-astra-20260911/ASSERTIONS.md
b9060f0bbc14e92464079b0daca12faa1ba2d367f9ecc7307ba301689de5b77d  box/f10-source-cone-direct-circuit-astra-20260911/WIRE-AND-VALIDATION.md
82fa6c2885740a06215b322b19c1bf51d4cab51d9086873321aef555c98b6173  box/f10-source-cone-direct-circuit-astra-20260911/custody.json
e6df0a6458c682128c841a054e4cfb0be00cb2efde0325743f197cdcb0564725  xmodel/f10-source-cone-direct-place-astra-20260911.md
8b8c6296f3e94b0b176631d848bfe0cca11ba6eac64877196d0a129df212f30a  xmodel/f10-source-cone-r3-code-astra-20260911.md
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  box/f10-source-cone-r3-code-astra-20260911/produce.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  box/f10-source-cone-r3-code-astra-20260911/check.py
712ac6023b6799c079e5b950822d07c20295d46788f38d64a433af7f45cd3103  xmodel/f10-source-cone-r3-code-gate-fable5-20260911.md
11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b  xmodel/f10-source-cone-fullrank-place-astra-20260911.md
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  xmodel/ideation-20260910T2300Z-astra-source.md
40b18453b6127d1b8217a6d6e1d3eb3aff1e911c15243ed9c640277f24175431  box/f10-source-cone-r3-code-astra-20260911/arithmetic.py
1aca7ad822cf88a95b30b2cb43c4a07227a78ca389fa28679e8fc1947e530ab0  xmodel/f10-source-cone-direct-place-gate-fable5-20260911.md
10e57542f9aa06eb69fd9562b2aa0bb27567c6d14186ffa90d77d6e08e80ae2c  box/f10-source-cone-r3-code-astra-20260911/check_arithmetic.py
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
d76f3ab9cb5869eeaf3464da417ee1de9dc25fcfdd00804b24dd6e1215a5e7e9  box/f10-source-cone-direct-circuit-gate-prep-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/f10-source-cone-direct-circuit-gate-fable5-20260911.md
test ! -e xmodel/f10-source-cone-direct-circuit-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-source-cone-direct-circuit-gate-fable5-20260911.log
test ! -e box/f10-source-cone-direct-circuit-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3directcircuit-term-20260911 --on-calendar='2026-09-11 02:49:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3directcircuit-kill-20260911 --on-calendar='2026-09-11 02:49:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3directcircuit-term-20260911.timer jc2-f10-r3directcircuit-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-source-cone-direct-circuit-gate-fable5-20260911 box/f10-source-cone-direct-circuit-gate-prep-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-source-cone-direct-circuit-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
