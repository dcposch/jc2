#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 18:33:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_CALLER_GATE_PINS'
34bfd0953a0f08cd2e2ea16284da01fe23d26e424ce7d44afde3d39304a6e937  box/caprun-candidate-caller-astra-20260911/TASK.md
ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe  box/caprun-latebinder-code-astra-20260911/latebind.py
3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661  xmodel/caprun-latebinder-first-fable5-20260911.md
f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066  box/caprun-candidate-stage-root-20260911/stage_patch.py
e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5  box/caprun-candidate-stage-root-20260911/EXERCISE.json
d96d979c950bf51faea0ad430af4f2eed1366d8f7b3e952e27d048ca2dff2273  xmodel/caprun-candidate-stage-first-fable5-20260911.md
31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74  box/caprun-closed-scope-b-execution-root-20260911/ROOT-REGISTRATION.preholder.json
4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3  box/caprun-closed-scope-b-execution-root-20260911/ROOT-REGISTRATION.json
58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e  box/caprun-closed-scope-b-execution-root-20260911/AUTHORITIES.preholder.json
1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be  box/caprun-closed-scope-b-execution-root-20260911/ROOT-EXECUTION-CARD.preholder.md
a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281  box/caprun-closed-scope-b-execution-root-20260911/ROOT-EXECUTION-CARD.md
6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62  box/caprun-closed-scope-b-execution-root-20260911/final-install.preholder.sh
abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208  box/caprun-closed-scope-b-execution-root-20260911/final-install.sh
d90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943  box/caprun-closed-scope-b-execution-root-20260911/FINAL-INSTALL-INPUTS.sha256
73596b115c73db9aac6751c08d26b2a90cbddccfaa1d6a8615ada65a8076df90  box/caprun-candidate-caller-astra-20260911/caller.py
e5c6a438016c5b0129f13b2f0cf2ae5a1cdf450750429c8c5a5450c590b4cc35  box/caprun-candidate-caller-astra-20260911/test_caller.py
f57c247414746a6f4576b45a84f8f17c52052be4414f69e951e3be093b82e9cd  box/caprun-candidate-caller-astra-20260911/CONTRACT.md
e465ca6c062a8de1822eedd3f29ed5cb7bc2490b8d09fccaa89e79890048970d  box/caprun-candidate-caller-astra-20260911/PINS.json
d4d68584e3b60bb166155a20fcedc5bb67a1526235726ca0b2c53fda8d96853a  box/caprun-candidate-caller-astra-20260911/fixture-pins.json
6b4ab0834f67b69fa4f6af8d7246ec4d1de5f26a3b2731a2f4cf637280430126  box/caprun-candidate-caller-astra-20260911/fixture-observation.json
7f9ff04852b1d2c6a59815aff6ca28968204abb42ece7e5c5d444d489186e53e  box/caprun-candidate-caller-astra-20260911/fixture-decision.json
2a673cbd51a163c476f5b0a14faa4683a51851477a9780a0f76c5fbd05ca26da  xmodel/caprun-candidate-caller-astra-20260911.md
511b7c06ab00dc1609039589415b231d0934f912332c3116badf443d6337bfc2  xmodel/caprun-candidate-caller-astra-20260911.md.artifact.json
633742acc2ce021047cc1162a724a62e1ef8ef7f69c1f818f5e75ba65778de28  box/caprun-candidate-caller-first-prep-root-20260911/fable.prompt.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
af1f0001f826cf8852c4a51d464d1b46ea330869e0b88dfdb4b39e3dc0e3983c  box/caprun-candidate-caller-astra-20260911/custody.json
JC2_CALLER_GATE_PINS
test ! -e xmodel/caprun-candidate-caller-first-fable5-20260911.md
test ! -e xmodel/caprun-candidate-caller-first-fable5-20260911.run.v2
test ! -e xmodel/caprun-candidate-caller-first-fable5-20260911.log
test ! -e box/caprun-candidate-caller-first-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-candidate-caller-first-term-20260911 --on-calendar='2026-09-11 18:51:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-candidate-caller-first-fable5-20260911.service
systemd-run --user --unit=jc2-candidate-caller-first-kill-20260911 --on-calendar='2026-09-11 18:51:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-candidate-caller-first-fable5-20260911.service
systemctl --user is-active jc2-candidate-caller-first-term-20260911.timer jc2-candidate-caller-first-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-candidate-caller-first-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1500 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-candidate-caller-first-fable5-20260911 box/caprun-candidate-caller-first-prep-root-20260911/fable.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-candidate-caller-first-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-candidate-caller-first-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-candidate-caller-first-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

