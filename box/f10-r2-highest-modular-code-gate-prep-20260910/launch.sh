set -euo pipefail
test "$(sha256sum 'box/f10-r2-highest-modular-code-astra-20260910/entry.py' | cut -d ' ' -f 1)" = '8afc9b158483183e1afefef65c5aad54a8a46615b0f3b3d4682812c8dd8d74b2'
test "$(sha256sum 'box/f10-r2-highest-modular-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = '6f094c4b468afe7e9f09d8b0d4ee4f33faa3017afb9809eaa312ff2f70904913'
test "$(sha256sum 'box/f10-r2-highest-modular-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = '1e685c413484f90d68db77bba844cb220f0d1b86c33c1d82ac9f587ad76c15f5'
test "$(sha256sum 'box/f10-r2-highest-modular-code-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'a7201e30705a301e432ffcad531c60c950cb0274fb98ee09434353f6d8a5f401'
test "$(sha256sum 'xmodel/f10-r2-highest-modular-code-astra-20260910.md' | cut -d ' ' -f 1)" = 'fde400591dcf57ef1f3059ec32577d206af75978800c78cb6041708ba6a9f39a'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/arithmetic.py' | cut -d ' ' -f 1)" = 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py' | cut -d ' ' -f 1)" = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
test "$(sha256sum 'xmodel/f10-r2-modular-properness-route-astra-20260910.md' | cut -d ' ' -f 1)" = 'f7ef8185dc5ef941c0ee8e7c8652541d6e5cac959bd4115585703d39e972131c'
test "$(sha256sum 'xmodel/f10-r2-modular-properness-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '215afdc5bfc637260ca9fb08d884521422b786dd036c383181f08a1a528b0625'
test "$(sha256sum 'xmodel/f10-r2-highest-bezout-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = 'ec7b0ed1767f5a015e3344dba220219bfef98f7afb4a8bb166ca386cea2e0230'
test ! -e xmodel/f10-r2-highest-modular-code-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-highest-modular-code-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-highest-modular-code-gate-fable5-20260910.log
test ! -e box/f10-r2-highest-modular-code-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-highmodcode-term-20260910 --on-calendar='2026-09-10 15:51:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-highmodcode-kill-20260910 --on-calendar='2026-09-10 15:51:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-highmodcode-term-20260910.timer jc2-r2-highmodcode-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-highest-modular-code-gate-fable5-20260910 box/f10-r2-highest-modular-code-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-highest-modular-code-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
