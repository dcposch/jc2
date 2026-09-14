set -euo pipefail
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/entry.py' | cut -d ' ' -f 1)" = 'c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = '60a290aee2ed5def7ed4242743f187dea755659f287707fa79c6c1e05f2d1f10'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = 'ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'e7fbaf54818d9fae1abff70418a566af7918d04a787fcabc21ceb8633e6e7070'
test "$(sha256sum 'xmodel/f10-r2-fullunit-modular-code-astra-20260910.md' | cut -d ' ' -f 1)" = '92036973d3a62a1264eeb874d24768859fe328306cdbe17868e32d92b225c4a5'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/authority.py' | cut -d ' ' -f 1)" = '2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/arithmetic.py' | cut -d ' ' -f 1)" = 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py' | cut -d ' ' -f 1)" = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-gate-prep-20260910/baseline-produce.py' | cut -d ' ' -f 1)" = 'eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10'
test "$(sha256sum 'xmodel/f10-r2-modular-fullsource-route-astra-20260910.md' | cut -d ' ' -f 1)" = 'f774640bc2093ba4745cae52f5892170923c79d7ad80a400d00ddd06814d2200'
test "$(sha256sum 'xmodel/f10-r2-modular-fullsource-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = 'c5cb181aa28bd5d49971b02b68721e335b0972876f9cc1e8c2444d2f73c9af63'
test "$(sha256sum 'ops/adapters/claude.sh' | cut -d ' ' -f 1)" = '34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699'
test "$(sha256sum 'ops/lane.sh' | cut -d ' ' -f 1)" = '0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396'
test "$(sha256sum 'ops/validate_charge_basis.py' | cut -d ' ' -f 1)" = 'a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e'
test "$(sha256sum 'ops/seal.py' | cut -d ' ' -f 1)" = '222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776'
test "$(sha256sum 'FALLACY-v2.md' | cut -d ' ' -f 1)" = 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5'
test ! -e xmodel/f10-r2-fullunit-modular-code-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-fullunit-modular-code-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-fullunit-modular-code-gate-fable5-20260910.log
test ! -e box/f10-r2-fullunit-modular-code-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-fullunitcode-term-20260910 --on-calendar='2026-09-10 17:02:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-fullunitcode-kill-20260910 --on-calendar='2026-09-10 17:02:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-fullunitcode-term-20260910.timer jc2-r2-fullunitcode-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-fullunit-modular-code-gate-fable5-20260910 box/f10-r2-fullunit-modular-code-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-fullunit-modular-code-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
