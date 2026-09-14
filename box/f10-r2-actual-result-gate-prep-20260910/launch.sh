set -euo pipefail
test ! -e xmodel/f10-r2-actual-result-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-actual-result-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-actual-result-gate-fable5-20260910.log
test ! -e box/f10-r2-actual-result-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-result-term-20260910 --on-calendar='2026-09-10 13:13:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-result-kill-20260910 --on-calendar='2026-09-10 13:13:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-result-term-20260910.timer jc2-r2-result-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=900 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-actual-result-gate-fable5-20260910 box/f10-r2-actual-result-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-actual-result-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
