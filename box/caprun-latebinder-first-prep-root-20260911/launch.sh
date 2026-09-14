#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 15:25:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_LATEBINDER_GATE_PINS'
4ea388079a13753351533209e947d0080f6d0371c233c627968c3b8625aefe15  box/caprun-latebinder-code-astra-20260911/custody.json
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
26cdfb6a2016d3618a4fdd60c3687fbec17b8fcb74576b23baae6471e4292deb  box/caprun-latebinder-first-prep-root-20260911/fable.prompt.md
JC2_LATEBINDER_GATE_PINS
jq -r '(.input_pins + .owned_pins_excluding_custody_itself) | to_entries[] | "\(.value)  \(.key)"' box/caprun-latebinder-code-astra-20260911/custody.json | sha256sum --check --strict
test ! -e xmodel/caprun-latebinder-first-fable5-20260911.md
test ! -e xmodel/caprun-latebinder-first-fable5-20260911.run.v2
test ! -e xmodel/caprun-latebinder-first-fable5-20260911.log
test ! -e box/caprun-latebinder-first-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-latebinder-first-term-20260911 --on-calendar='2026-09-11 15:40:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-latebinder-first-fable5-20260911.service
systemd-run --user --unit=jc2-latebinder-first-kill-20260911 --on-calendar='2026-09-11 15:40:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-latebinder-first-fable5-20260911.service
systemctl --user is-active jc2-latebinder-first-term-20260911.timer jc2-latebinder-first-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-latebinder-first-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1500 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-latebinder-first-fable5-20260911 box/caprun-latebinder-first-prep-root-20260911/fable.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-latebinder-first-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-latebinder-first-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-latebinder-first-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
