set -euo pipefail
test "$(sha256sum 'box/f10-r2-semantic-mutator-astra-20260910/mutate_controls.py' | cut -d ' ' -f 1)" = 'a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = '6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/dispatch.diff' | cut -d ' ' -f 1)" = '183b63fbf0f75a87f8073815e27e083e741c08ce0e749bf7f64fa99b66b9f25a'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/DISABLED-REGISTRATION.json' | cut -d ' ' -f 1)" = '17cab2767468f01c1f8ede32a1adbd1f1b608cce88fcbdc4a9c992ab89c05535'
test "$(sha256sum 'box/f10-r2-semantic-runtime-astra-20260910/probe.py' | cut -d ' ' -f 1)" = '1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = 'e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py' | cut -d ' ' -f 1)" = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/authority.py' | cut -d ' ' -f 1)" = '2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b'
test "$(sha256sum 'xmodel/f10-r2-runtime-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '558fa2f1ef15b8477148fc014df4dcbcf783b61bcddae9889213b995bcb86e16'
test "$(sha256sum 'xmodel/f10-r2-reconstruction-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b'
test "$(sha256sum 'xmodel/f10-r2-actual-result-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c'
test ! -e xmodel/f10-r2-semantic-code-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-semantic-code-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-semantic-code-gate-fable5-20260910.log
test ! -e box/f10-r2-semantic-code-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-semantic-term-20260910 --on-calendar='2026-09-10 13:52:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-semantic-kill-20260910 --on-calendar='2026-09-10 13:52:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-semantic-term-20260910.timer jc2-r2-semantic-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-semantic-code-gate-fable5-20260910 box/f10-r2-semantic-code-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-semantic-code-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
