#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 11:10:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_1100_PINS'
61272ce1abaaba4725febd6e202a82bfddaf94878a441652a703d9cd137d1dcb  box/ideation-20260911T1100Z-prep/PINS.json
224b02c9092d1625212dfd9302936200b2353ac0a76377461d26c4ef00c5e3b1  box/ideation-20260911T1100Z-prep/inputs/approaches.md
c235fca15b48d29860291e26b7c8056915110deb1a9dc15b7ff1a20926d8d4ac  box/ideation-20260911T1100Z-prep/inputs/master46-history.md
615ad4f1227a84604877d5e4ad8daef52589ed31e70dcf745af30e6573f3faa7  box/ideation-20260911T1100Z-prep/inputs/reduction-interfaces.md
9dad11eba0d7174a39c398b640a6cd42dd47c18f030cf296ceedc90c238f5792  box/ideation-20260911T1100Z-prep/inputs/previous-synthesis.md
67e8407c4e1bdece4d1b523ea35b1a5404499eadcbdf58cce8f200c26c0c68ae  box/ideation-20260911T1100Z-prep/inputs/earlier-synthesis.md
0643cf030d64989b0ab20893cb5208669f2c56b469c396485d6ea9c37c35a2f8  box/ideation-20260911T1100Z-prep/inputs/latest-websweep.md
70a8709de3f15f33e8279fe67df5711454c2b97308fa74e4ad08400af6b0383c  box/ideation-20260911T1100Z-prep/inputs/current-operations.md
d9bb20f83678cde429f04a1f4a175b013d31be2b92ccdb87d6b98ad3edc24265  box/ideation-20260911T1100Z-prep/inputs/boundary-test.md
d5e0f0560312c82de349984672dad3498db42e970555538c17948f53ccdf5c2c  box/ideation-20260911T1100Z-prep/inputs/three-weight-proof.md
e9e1b1907109f30e5fda50cf6c8ce83d08737569ef1a93a5f70277c407379a68  box/ideation-20260911T1100Z-prep/inputs/common-contract.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
30302fea1b0b4c8851ab680fdf0489e839409f7ba09c10a951c783475358bf08  box/ideation-20260911T1100Z-prep/fable-invite.prompt.md
JC2_1100_PINS
test ! -e xmodel/ideation-20260911T1100Z-fable5.md
test ! -e xmodel/ideation-20260911T1100Z-fable5.run.v2
test ! -e xmodel/ideation-20260911T1100Z-fable5.log
test ! -e box/ideation-20260911T1100Z-fable5
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-ideation1100-term-20260911 --on-calendar='2026-09-11 11:23:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-ideation-20260911T1100Z-fable5.service
systemd-run --user --unit=jc2-ideation1100-kill-20260911 --on-calendar='2026-09-11 11:23:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-ideation-20260911T1100Z-fable5.service
systemctl --user is-active jc2-ideation1100-term-20260911.timer jc2-ideation1100-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-ideation-20260911T1100Z-fable5.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude ideation-20260911T1100Z-fable5 box/ideation-20260911T1100Z-prep/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-ideation-20260911T1100Z-fable5.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-ideation-20260911T1100Z-fable5.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-ideation-20260911T1100Z-fable5.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
