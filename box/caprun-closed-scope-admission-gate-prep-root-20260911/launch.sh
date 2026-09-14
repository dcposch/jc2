#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 09:40:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_REVIEW_PINS'
cbbddf401192c7548c12e3bc8c59c291ecc2b3b101a20e6f18bcf1f67318fa20  box/caprun-closed-scope-admission-astra-20260911/holder.template.py
99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c  box/caprun-closed-scope-admission-astra-20260911/outer-admission.template.sh
5cb4b2ab34f34f35de3bc7da36b41bbc983ccdf3d3b9ae40976487056258e82c  box/caprun-closed-scope-admission-astra-20260911/README.md
e4345bab4096f2b856524619d3c5408ae4044b27f95ab45a7b8fa35d688bb59c  xmodel/caprun-closed-scope-admission-astra-20260911.md
8db41bfae391268e5819b218b887dbc08468310b512c4f9704e7db841be04c93  xmodel/caprun-closed-scope-admission-astra-20260911.md.artifact.json
d91e854348bac0836eea57feb67665b9ea06941eeb574c8ce286e5698d4cb20e  xmodel/caprun-closed-scope-launch-order-astra-20260911.md
db925cbf9dad59b39444ea4250b839584be68c3bc5353aee5af924d96034e8f4  box/caprun-closed-scope-registration-prep-root-20260911/ROOT-REGISTRATION.template.json
af7a2fab4aa6317f7386e438f2f03acc6daffdd04c3deee6a6554b675089ee81  box/caprun-closed-scope-implementation-astra-20260911/CONTRACT.md
2a4a7ff45c19f8bfa386da8caddd44e8cd80c44d54e04e043f7e3fb731cb478e  box/f10-necessary-rows-deployment-prep-root-20260911/outer-launch.template.sh
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
8bd8715bb73c91775f40dbefd3a0bc6002bda83b30075a304462652576a28326  box/caprun-closed-scope-admission-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/caprun-closed-scope-admission-gate-fable5-20260911.md
test ! -e xmodel/caprun-closed-scope-admission-gate-fable5-20260911.run.v2
test ! -e xmodel/caprun-closed-scope-admission-gate-fable5-20260911.log
test ! -e box/caprun-closed-scope-admission-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-caprun-admission-term-20260911 --on-calendar='2026-09-11 09:57:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service
systemd-run --user --unit=jc2-caprun-admission-kill-20260911 --on-calendar='2026-09-11 09:57:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service
systemctl --user is-active jc2-caprun-admission-term-20260911.timer jc2-caprun-admission-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-closed-scope-admission-gate-fable5-20260911 box/caprun-closed-scope-admission-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-closed-scope-admission-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
