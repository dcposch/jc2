#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 17:59:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_STAGE_GATE_PINS'
6ac8e9ea645a2cb42c91ba0fe389d60d3db6c277b201c3557c2b231be8656067  box/caprun-candidate-stage-root-20260911/TASK.md
f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066  box/caprun-candidate-stage-root-20260911/stage_patch.py
fbec59b7317689fd71124bc5702ebdd0cd5ddb4ec8854592bb8a0f0447d66ff8  box/caprun-candidate-stage-root-20260911/historical_exercise.py
e8e59687fb87adf42f8656c265e8a525741c21239d4479ce0b3da8f855a8e54a  box/caprun-candidate-stage-root-20260911/test_stage_patch.py
e21c3efe2a061dfbd25328c9d0f519b6fe693938317e127ecabb351514dc9da5  box/caprun-candidate-stage-root-20260911/CONTRACT.md
88e7bc408852d226b119cc6dd26f9e91d0be16897e414b669e9c690142bab579  box/caprun-candidate-stage-root-20260911/RECIPE.js
e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5  box/caprun-candidate-stage-root-20260911/EXERCISE.json
69449fd5c02eb9f604d9b9f71532de9ecaf0e513e1e584c058da7db7bd9124d2  box/caprun-candidate-stage-root-20260911/tests.stdout
ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe  box/caprun-latebinder-code-astra-20260911/latebind.py
85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06  box/caprun-latebinder-code-astra-20260911/test_latebind.py
3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661  xmodel/caprun-latebinder-first-fable5-20260911.md
31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74  box/caprun-closed-scope-b-execution-root-20260911/ROOT-REGISTRATION.preholder.json
4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3  box/caprun-closed-scope-b-execution-root-20260911/ROOT-REGISTRATION.json
58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e  box/caprun-closed-scope-b-execution-root-20260911/AUTHORITIES.preholder.json
1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be  box/caprun-closed-scope-b-execution-root-20260911/ROOT-EXECUTION-CARD.preholder.md
a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281  box/caprun-closed-scope-b-execution-root-20260911/ROOT-EXECUTION-CARD.md
6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62  box/caprun-closed-scope-b-execution-root-20260911/final-install.preholder.sh
abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208  box/caprun-closed-scope-b-execution-root-20260911/final-install.sh
d90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943  box/caprun-closed-scope-b-execution-root-20260911/FINAL-INSTALL-INPUTS.sha256
0363a58346b318be4767cf7938d77ff199a135d86f9d916e459f8db0b8b6a95a  box/caprun-candidate-stage-root-20260911/PINS.json
498787894944fe77717687e1483979851993f93fb30a1e652e7fca3f5f9e143f  xmodel/caprun-candidate-stage-root-20260911.md
4f8a2a2990ff7dafa018132a3be01493887896c5cbebc97c87b0c9b10f220d60  xmodel/caprun-candidate-stage-root-20260911.md.artifact.json
f597c9518406d7d7c153dde916bd44a936030189838bce205621f2d888243b88  box/caprun-candidate-stage-root-20260911/custody.json
3fdacfc373ebdced7c929c1d489a6c40ccff94559e0474531b6c022ff68e2daa  box/caprun-candidate-stage-first-prep-root-20260911/fable.prompt.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
JC2_STAGE_GATE_PINS
test ! -e xmodel/caprun-candidate-stage-first-fable5-20260911.md
test ! -e xmodel/caprun-candidate-stage-first-fable5-20260911.run.v2
test ! -e xmodel/caprun-candidate-stage-first-fable5-20260911.log
test ! -e box/caprun-candidate-stage-first-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-candidate-stage-first-term-20260911 --on-calendar='2026-09-11 18:15:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-candidate-stage-first-fable5-20260911.service
systemd-run --user --unit=jc2-candidate-stage-first-kill-20260911 --on-calendar='2026-09-11 18:15:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-candidate-stage-first-fable5-20260911.service
systemctl --user is-active jc2-candidate-stage-first-term-20260911.timer jc2-candidate-stage-first-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-candidate-stage-first-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1500 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-candidate-stage-first-fable5-20260911 box/caprun-candidate-stage-first-prep-root-20260911/fable.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-candidate-stage-first-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-candidate-stage-first-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-candidate-stage-first-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
