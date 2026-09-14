set -euo pipefail
test "$(sha256sum 'xmodel/f10-r2-semantic-ready-actual-root-20260910.md' | cut -d ' ' -f 1)" = '5756fe88a027e084435a85d9a8c27c410a46bc3286de05d18ae9d4e3f88ac749'
test "$(sha256sum 'xmodel/f10-r2-actual-result-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c'
test "$(sha256sum 'xmodel/f10-r2-semantic-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/CUSTODY.json' | cut -d ' ' -f 1)" = 'da4d484397e3896c74a073a8ab4f2317513ea11fca5ac374a89a2324ba004fee'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/ROOT-REGISTRATION.json' | cut -d ' ' -f 1)" = '0d0b00638cb42de7b7a59e1661ff0ae21668ff9ce0175e50a8b575d1d4ee3605'
test "$(sha256sum 'box/f10-r2-actual-execution-prep-20260910/harvest/run/jc2-r2-20260910T1230/frozen/artifact.json' | cut -d ' ' -f 1)" = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/frozen/mutate.receipt.json' | cut -d ' ' -f 1)" = '4f851182ae7249354550ed50768f3a1538fcbdbc99a9c7d235a3441940b37990'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/semantic-binding.json' | cut -d ' ' -f 1)" = 'f634a181a30025378d2aa5ae19e0ee82bd7eead896809c0d5753e327109a678b'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/frozen/mutated6.json' | cut -d ' ' -f 1)" = 'b70af8a2620ad3e50579d65d0632387a2046d19a57170396882a4af05736eca5'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/frozen/mutated10.json' | cut -d ' ' -f 1)" = 'f89081b780278c3f6716374077a26dfc4935cfb46c13edf23802f1701986a0ab'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check6.stderr' | cut -d ' ' -f 1)" = 'ce039446437d873d08384bd82bc35348f1a799ae798ba3d0bb7c052685956598'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check10.stderr' | cut -d ' ' -f 1)" = '93a1933455ed50c0397bcaf75c2f2cb3816eec6edba1398f5857d55147d6f2b0'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/mutate.telemetry.json' | cut -d ' ' -f 1)" = 'f80a9612f2bfb04f01ad95be8fbfc14f9c706455f9c39a7c8527a70f468e7911'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/mutate.pre.json' | cut -d ' ' -f 1)" = '564fc829335258e6318a26e26e76b275480423b606d01f2278d592a67e0b17ff'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/mutate.post.json' | cut -d ' ' -f 1)" = '7f54710b5aab525d31da0558456778d5161b43d398acd48a991171650bd1c0ed'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/mutate.python-live.json' | cut -d ' ' -f 1)" = '8b5b0de48e8af3c5e6e1e84a76fb795ccc02eb5f8b2b956daf16ab09e1e11fa3'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check6.telemetry.json' | cut -d ' ' -f 1)" = '5ac9ce903aff71159e9c7209e0438c9f67be76b9d2e7eb5ac885b922c05ebabb'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check6.pre.json' | cut -d ' ' -f 1)" = 'ffba5a81bc7d7098637db11650ab7ea8104a04ee7d8cdc4d5f5d2494c6630e0b'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check6.post.json' | cut -d ' ' -f 1)" = '2759c9e09cccefb86a5f7dfbd8b24c25dd07207bca365b26f46fa154a7ff5e64'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check6.python-live.json' | cut -d ' ' -f 1)" = '4db790f4c0584901edb306cba5bcd526efc85404971e5d2744af9758bcb48cf9'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check10.telemetry.json' | cut -d ' ' -f 1)" = '09f85d71a9d34dbab17a6f4ac3f807941ab188566bcedf09620adfb7f4326104'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check10.pre.json' | cut -d ' ' -f 1)" = '507759e178998d3beeb7be5630c2703acc536494e43bfe61c0f26130b5e7aaa0'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check10.post.json' | cut -d ' ' -f 1)" = '041fa2c14af81a6892bb900a175dab1b388c7c42e7fa7ef25ac540de34bdfe86'
test "$(sha256sum 'box/f10-r2-semantic-ready-execution-20260910/harvest/run/jc2-r2-controls-ready-20260910T1620/check10.python-live.json' | cut -d ' ' -f 1)" = '92674b6cfea7a0dd2153f1cbea01b3770b55958594ca6605577affda986e949d'
test "$(sha256sum 'ops/adapters/claude.sh' | cut -d ' ' -f 1)" = '34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699'
test "$(sha256sum 'ops/lane.sh' | cut -d ' ' -f 1)" = '0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396'
test "$(sha256sum 'ops/validate_charge_basis.py' | cut -d ' ' -f 1)" = 'a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e'
test "$(sha256sum 'ops/seal.py' | cut -d ' ' -f 1)" = '222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776'
test "$(sha256sum 'FALLACY-v2.md' | cut -d ' ' -f 1)" = 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5'
test ! -e xmodel/f10-r2-semantic-ready-result-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-semantic-ready-result-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-semantic-ready-result-gate-fable5-20260910.log
test ! -e box/f10-r2-semantic-ready-result-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-semreadyresult-term-20260910 --on-calendar='2026-09-10 17:10:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-semreadyresult-kill-20260910 --on-calendar='2026-09-10 17:10:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-semreadyresult-term-20260910.timer jc2-r2-semreadyresult-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-semantic-ready-result-gate-fable5-20260910 box/f10-r2-semantic-ready-result-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-semantic-ready-result-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
