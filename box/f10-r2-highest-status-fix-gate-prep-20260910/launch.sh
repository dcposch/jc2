set -euo pipefail
test "$(sha256sum 'box/f10-r2-highest-status-fix-gate-prep-20260910/old-dispatch.py' | cut -d ' ' -f 1)" = '00b12b15cf97f860b963e3fe91d947771722392b96fc8efdb3de168e75e89328'
test "$(sha256sum 'box/f10-r2-highest-runtime-status-fix-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = '396dc3b42f082ffbc08516a3dd41528516e2e69e3994fc005b22b79b3a605927'
test "$(sha256sum 'box/f10-r2-highest-status-fix-gate-prep-20260910/old-CONTRACT.md' | cut -d ' ' -f 1)" = 'e79249f9620eb6b4bf519b826a4f12e5f82440cfbc76a0dffb5769d1c4ce4e90'
test "$(sha256sum 'box/f10-r2-highest-runtime-status-fix-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'f0bfb025d5445f5cb16b48c29ff0d9aef909616216482c52973bd5c8f37f4318'
test "$(sha256sum 'box/f10-r2-highest-runtime-status-fix-astra-20260910/STATUS-DELTA.diff' | cut -d ' ' -f 1)" = 'cd498fec4577f7234c2ce413dbf0b4b035821f1fa6759f9acc2f080ee1081eb5'
test "$(sha256sum 'box/f10-r2-highest-modular-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = '6f094c4b468afe7e9f09d8b0d4ee4f33faa3017afb9809eaa312ff2f70904913'
test "$(sha256sum 'xmodel/f10-r2-highest-modular-runtime-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '8358693287a2874f05b431ab0081c98db9461bdc6eaf06be33f40a2f83c72ca8'
test "$(sha256sum 'xmodel/f10-r2-highest-runtime-status-fix-astra-20260910.md' | cut -d ' ' -f 1)" = '3d282cbed69ee9ca919f4f9e9151ad65a0cc624886ddf707f1c04240b0254a62'
test "$(sha256sum 'ops/adapters/claude.sh' | cut -d ' ' -f 1)" = '34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699'
test "$(sha256sum 'ops/lane.sh' | cut -d ' ' -f 1)" = '0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396'
test "$(sha256sum 'ops/validate_charge_basis.py' | cut -d ' ' -f 1)" = 'a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e'
test "$(sha256sum 'ops/seal.py' | cut -d ' ' -f 1)" = '222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776'
test "$(sha256sum 'FALLACY-v2.md' | cut -d ' ' -f 1)" = 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5'
test ! -e xmodel/f10-r2-highest-status-fix-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-highest-status-fix-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-highest-status-fix-gate-fable5-20260910.log
test ! -e box/f10-r2-highest-status-fix-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-highstatusfix-term-20260910 --on-calendar='2026-09-10 16:55:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-highstatusfix-kill-20260910 --on-calendar='2026-09-10 16:55:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-highstatusfix-term-20260910.timer jc2-r2-highstatusfix-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-highest-status-fix-gate-fable5-20260910 box/f10-r2-highest-status-fix-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-highest-status-fix-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
