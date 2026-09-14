set -euo pipefail
test "$(sha256sum 'box/f10-r2-native-cache-correction-prep-20260910/ROOT-NATIVE-CORRECTION.md' | cut -d ' ' -f 1)" = 'bd77d02ea15d813a07ddde9ccb3c060dc3f5095473cb2ccceaf0984e18ee51e9'
test "$(sha256sum 'box/f10-r2-map-observer-execution-prep-20260910/RESULT.md' | cut -d ' ' -f 1)" = '91d0052e07106a847dbffed3565e9c4c21a6125ba16bb222a47ff5a5891ca97c'
test "$(sha256sum 'box/f10-r2-map-observer-execution-prep-20260910/harvest/var/lib/jc2-r2-map-observer-20260910T1500/CUSTODY.json' | cut -d ' ' -f 1)" = '8b1112984ae6d95939669db1f32fb2aa8feacbdd19b56c1eb26dc382bd762678'
test "$(sha256sum 'box/f10-r2-map-observer-execution-prep-20260910/harvest/var/lib/jc2-r2-map-observer-20260910T1500/map-rejection.UNVALIDATED.json' | cut -d ' ' -f 1)" = '191f90071bb5c6f75d0cb4b38e420e942496d4e4e1066aff3719736099bdfea7'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = '6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b'
test "$(sha256sum 'xmodel/f10-r2-semantic-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b'
test "$(sha256sum 'xmodel/f10-r2-map-observer-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '1944f1d87853b35e0efcca72c8097cc35f70947a81a78d7b87b7025832f2c9ae'
test "$(sha256sum 'box/f10-r2-map-observer-execution-prep-20260910/native-metadata.sh' | cut -d ' ' -f 1)" = '1c9e90633abdcb921e23bb505163a04b400ddc4bf859d1500b26913b503a1bd1'
test ! -e xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.log
test ! -e box/f10-r2-native-cache-correction-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-cachecorrection-term-20260910 --on-calendar='2026-09-10 15:54:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-cachecorrection-kill-20260910 --on-calendar='2026-09-10 15:54:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-cachecorrection-term-20260910.timer jc2-r2-cachecorrection-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-native-cache-correction-gate-fable5-20260910 box/f10-r2-native-cache-correction-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-native-cache-correction-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
