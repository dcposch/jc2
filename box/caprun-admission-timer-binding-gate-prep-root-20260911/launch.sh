#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 10:00:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_REVIEW_PINS'
bb00d8dc15208a621dbec8293f3faf54ed3836cfeba6aed1a1622a4d533f4252  xmodel/caprun-admission-timer-binding-root-20260911.md
9982d5315f5f6920e26d4e863d3c59a6e8fcc7499a38c77a4e52766fc3edcfd2  xmodel/caprun-admission-timer-binding-root-20260911.md.artifact.json
d08e05c66d2c874f00f0485aef929a829217e89488546601c73145b11121fba1  box/caprun-admission-timer-binding-root-20260911/outer-admission.template.sh
99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c  box/caprun-admission-timer-binding-root-20260911/parent-outer-admission.template.sh
5f0cc7a9146c055b09ca0dd0db79e80cbb38ed64e79d64acfb177bbf0ffce9a4  box/caprun-closed-scope-deployment-prep-root-20260911/launch-worker.template.sh
c8912f2e54cdd207268383abe384fca3e5806743cfd3d17ad0973705c2f9c72d  xmodel/caprun-closed-scope-admission-gate-fable5-20260911.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
62049e3d3ea226b4765c23111fc9d3641b1d795b4ac75e9bbc6215e72ed9d1fc  box/caprun-admission-timer-binding-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/caprun-admission-timer-binding-gate-fable5-20260911.md
test ! -e xmodel/caprun-admission-timer-binding-gate-fable5-20260911.run.v2
test ! -e xmodel/caprun-admission-timer-binding-gate-fable5-20260911.log
test ! -e box/caprun-admission-timer-binding-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-caprun-timer-binding-term-20260911 --on-calendar='2026-09-11 10:11:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service
systemd-run --user --unit=jc2-caprun-timer-binding-kill-20260911 --on-calendar='2026-09-11 10:11:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service
systemctl --user is-active jc2-caprun-timer-binding-term-20260911.timer jc2-caprun-timer-binding-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-admission-timer-binding-gate-fable5-20260911 box/caprun-admission-timer-binding-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-admission-timer-binding-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
