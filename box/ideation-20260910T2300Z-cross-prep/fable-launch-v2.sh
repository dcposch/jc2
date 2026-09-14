#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 23:22:00 UTC' +%s)"
sha256sum -c <<'JC2_2300_CROSS_PINS'
6a915d4046f8d7a9c30d45ada099a40bfee79a146aa9460ed54c5993215fda40  box/ideation-20260910T2300Z-cross-prep/ROOT-CROSS.md
c9da5199be69e33e79693d0c19d5ca5ea2bd86d84c89e138c2ed471adcb40314  xmodel/ideation-20260910T2300Z-coordinator.md
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  xmodel/ideation-20260910T2300Z-astra-source.md
e6435445c141b7fe17ae353addb84ca15ddb94b3e7fa12ca61b04a9296b1a95c  xmodel/ideation-20260910T2300Z-astra-geometry.md
3add44c6c10c6629d7034e982b0f5a55cd7f9fd2c7db6627c29a94f7859a2609  xmodel/ideation-20260910T2300Z-astra-construction.md
c14d89e94ad74807c5a21efc0e8de7169d760e8c5c3c903a00410cd8077d8cfd  xmodel/ideation-20260910T2300Z-fable5.md
53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312  box/ideation-20260910T2300Z-prep/inputs/allr-kernel-producer.md
097736365b7afcd0701c83063ee87a691532491124106d0346f9c2dfbb8b4617  box/ideation-20260910T2300Z-prep/inputs/allr-kernel-first.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
bde5669d992f63d71d848a126abb922c7e88807286c1fe97f4f4ffd3be703f54  box/ideation-20260910T2300Z-cross-prep/fable-invite.prompt.md
JC2_2300_CROSS_PINS
test ! -e xmodel/ideation-20260910T2300Z-cross-fable5.md
test ! -e xmodel/ideation-20260910T2300Z-cross-fable5.run.v2
test ! -e xmodel/ideation-20260910T2300Z-cross-fable5.log
test ! -e box/ideation-20260910T2300Z-cross-fable5
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-ideation2300cross-term-20260910 --on-calendar='2026-09-10 23:33:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-ideation-20260910T2300Z-cross-fable5.service
systemd-run --user --unit=jc2-ideation2300cross-kill-20260910 --on-calendar='2026-09-10 23:33:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-ideation-20260910T2300Z-cross-fable5.service
systemctl --user is-active jc2-ideation2300cross-term-20260910.timer jc2-ideation2300cross-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-ideation-20260910T2300Z-cross-fable5.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude ideation-20260910T2300Z-cross-fable5 box/ideation-20260910T2300Z-cross-prep/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-ideation-20260910T2300Z-cross-fable5.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-ideation-20260910T2300Z-cross-fable5.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-ideation-20260910T2300Z-cross-fable5.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1



