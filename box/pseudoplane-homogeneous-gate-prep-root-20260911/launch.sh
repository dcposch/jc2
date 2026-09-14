#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 07:54:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  xmodel/pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  xmodel/pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
ddc81d815420aadd800c78683922866423d7d7a298d09d843d623af247de3f61  box/pseudoplane-homogeneous-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/pseudoplane-homogeneous-gate-fable5-20260911.md
test ! -e xmodel/pseudoplane-homogeneous-gate-fable5-20260911.run.v2
test ! -e xmodel/pseudoplane-homogeneous-gate-fable5-20260911.log
test ! -e box/pseudoplane-homogeneous-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-pseudoplane-homogeneous-term-20260911 --on-calendar='2026-09-11 08:08:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service
systemd-run --user --unit=jc2-pseudoplane-homogeneous-kill-20260911 --on-calendar='2026-09-11 08:08:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service
systemctl --user is-active jc2-pseudoplane-homogeneous-term-20260911.timer jc2-pseudoplane-homogeneous-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude pseudoplane-homogeneous-gate-fable5-20260911 box/pseudoplane-homogeneous-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-pseudoplane-homogeneous-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
