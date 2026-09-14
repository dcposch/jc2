set -euo pipefail
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = 'b4cea19b474a3238caf0871369baa5fc8497e1d1ac5cc6e107815372297640e2'
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/dispatch.diff' | cut -d ' ' -f 1)" = 'd80b72eaf86f9f2ad8b0716a89337d86aad4243b6ebbdbcd20b679128f6bdbbb'
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/probe.py' | cut -d ' ' -f 1)" = '1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde'
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'f62f7480201d89cf7a6bcd6419a8d239f661f3dc8fd30be3000248d7c86a5496'
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/DISABLED-REGISTRATION.json' | cut -d ' ' -f 1)" = '9116e41d1664ba28917e8e3e4110dd23c7ec037a727aba870fda7d4d7fc569b7'
test "$(sha256sum 'box/f10-r2-map-observer-code-astra-20260910/READ-SCOPE.md' | cut -d ' ' -f 1)" = '2bcceb23b3fe9c71f409578b99af8c51446bce2232e47b6167cd1bf0543010c0'
test "$(sha256sum 'xmodel/f10-r2-map-observer-code-astra-20260910.md' | cut -d ' ' -f 1)" = '255a5805733716b188744ad08f109f154653045a642b635fc1c5bc3fb1ac0519'
test "$(sha256sum 'xmodel/f10-r2-semantic-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b'
test "$(sha256sum 'xmodel/f10-r2-native-map-diagnosis-astra-20260910.md' | cut -d ' ' -f 1)" = '7577c1d50b5350044f2d2e844980655effea7b49f21b05059e883682012d9be4'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/authority.py' | cut -d ' ' -f 1)" = '2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b'
test "$(sha256sum 'ops/run_capped.py' | cut -d ' ' -f 1)" = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
test ! -e xmodel/f10-r2-map-observer-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-map-observer-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-map-observer-gate-fable5-20260910.log
test ! -e box/f10-r2-map-observer-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-mapobserve-term-20260910 --on-calendar='2026-09-10 15:06:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-mapobserve-kill-20260910 --on-calendar='2026-09-10 15:06:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-mapobserve-term-20260910.timer jc2-r2-mapobserve-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-map-observer-gate-fable5-20260910 box/f10-r2-map-observer-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-map-observer-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

