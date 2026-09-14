set -eu
cd /home/ubuntu/jc2
sha256sum -c <<'JC2_CONTACT_GRAM_REVIEW_PINS'
c08712bb0627e7b6c875c4273fccc780f5346288db5de73ccca4a6598efc3c67  xmodel/f10-contact-gram-runtime-astra-20260910.md
61f21a2c5912cd53a46f8881783994e104a511cee1261713df53936aced9c126  box/f10-contact-gram-runtime-astra-20260910/dispatch.py
70857a11be5e21d63d8bb476663dd3587332d1968f5f26912e6851aa51d5d77c  box/f10-contact-gram-runtime-astra-20260910/mutate.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  box/f10-contact-gram-runtime-astra-20260910/probe.py
b1ce2ff5fb5ccac27e24a0e178a147f0da122fd46f6625691ca3f81c20bc59f6  box/f10-contact-gram-runtime-astra-20260910/CONTRACT.md
48fca8fe4939292d02b39f9a82e31bef940a3a1a3b77cf54ea105b1d014576cf  box/f10-contact-gram-runtime-astra-20260910/READ-SCOPE.md
531c249cd7a0ff6a9e982b798c462ca6a4656150e114fb882d0d9d70f9e1863b  xmodel/f10-contact-gram-code-gate-fable5-20260910.md
afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee  box/f10-contact-gram-code-astra-20260910/producer.py
ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06  box/f10-contact-gram-code-astra-20260910/checker.py
96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141  box/f10-contact-gram-startup-fix-astra-20260910/authority.py
29e8fa8f0c6a5d07694d3f5e3fc66a5714a4bf2ce990a44a23a8e95cdee9db7e  box/f10-contact-gram-code-astra-20260910/VALIDATION.md
08d75a6199cc414ba7c02be9cd3f3bcf1cf89a5472623d0c557777744c044c59  box/f10-contact-gram-startup-fix-astra-20260910/CONTRACT-DELTA.md
0562b82afa2b6f6da1e2c488d261fc65f22f705629c12446bbfeaf85bdccbef2  xmodel/f10-middle-real-runtime-gate-fable5-20260910.md
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  ops/run_capped.py
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
JC2_CONTACT_GRAM_REVIEW_PINS
test ! -e xmodel/f10-contact-gram-runtime-gate-fable5-20260910.md
test ! -e xmodel/f10-contact-gram-runtime-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-contact-gram-runtime-gate-fable5-20260910.log
test ! -e box/f10-contact-gram-runtime-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-contact-gramruntime-term-20260910 --on-calendar='2026-09-10 21:08:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service
systemd-run --user --unit=jc2-contact-gramruntime-kill-20260910 --on-calendar='2026-09-10 21:08:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service
systemctl --user is-active jc2-contact-gramruntime-term-20260910.timer jc2-contact-gramruntime-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1320 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-contact-gram-runtime-gate-fable5-20260910 box/f10-contact-gram-runtime-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-contact-gram-runtime-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

