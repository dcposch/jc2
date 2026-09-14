set -euo pipefail
test "$(sha256sum 'box/f10-r2-highest-bezout-code-astra-20260910/entry.py' | cut -d ' ' -f 1)" = '055bff5a98f9068c71124d9b301ce01d2419bd88d938febd2f86b5a2f1043c14'
test "$(sha256sum 'box/f10-r2-highest-bezout-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = '470d52330bc5c547374607610f52bcac9b8c02a721f9841498b13b9bb8ba876a'
test "$(sha256sum 'box/f10-r2-highest-bezout-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = 'bb86eb0c8fc475ce78672c734b3a0403ad0f80b48057bc5b4657084ffc9a8a98'
test "$(sha256sum 'box/f10-r2-highest-bezout-code-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'f5e570e35b0f3aa022f65ff961b12cdf9d1cec9e08fedd251b9bfb19e7452527'
test "$(sha256sum 'xmodel/f10-r2-highest-bezout-code-astra-20260910.md' | cut -d ' ' -f 1)" = '294d7d72d2dd766aa2293457042133f3bd5f417122aa2da97f17f0a6f7f95956'
test "$(sha256sum 'box/f10-r2-highest-bezout-code-astra-20260910/READ-SCOPE.md' | cut -d ' ' -f 1)" = '9db0610a91e04beed6fccfec9770488a3d8ab7f7c9ab7522f60458ad16af0777'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/arithmetic.py' | cut -d ' ' -f 1)" = 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py' | cut -d ' ' -f 1)" = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
test "$(sha256sum 'xmodel/f10-r2-reconstruction-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b'
test "$(sha256sum 'xmodel/f10-r2-cyclic-core-astra-20260910.md' | cut -d ' ' -f 1)" = '5afce82cc0478da08bfc8df5a6321c6edfefd1a4081be9bc50a032052dd54edd'
test "$(sha256sum 'xmodel/f10-r2-cyclic-core-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '41a586169d3a944ba5025d115041170bf7bacf5d9054dab71d57f293b0ccfc7b'
test "$(sha256sum 'xmodel/f10-r2-infinity-forcing-final-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '99155a6e6afa0577e95e0dc0ed8a69784fd4197fcfb956d22c6779f405c55ecf'
test ! -e xmodel/f10-r2-highest-bezout-code-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-highest-bezout-code-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-highest-bezout-code-gate-fable5-20260910.log
test ! -e box/f10-r2-highest-bezout-code-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-bezout-term-20260910 --on-calendar='2026-09-10 14:20:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-bezout-kill-20260910 --on-calendar='2026-09-10 14:20:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-bezout-term-20260910.timer jc2-r2-bezout-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-highest-bezout-code-gate-fable5-20260910 box/f10-r2-highest-bezout-code-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-highest-bezout-code-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

