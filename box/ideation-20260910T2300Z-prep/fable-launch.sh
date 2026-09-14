#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 23:10:00 UTC' +%s)"
sha256sum -c <<'JC2_2300_PINS'
e44683c3590e5a2546ae64f4c24d6d8d45e97a5e1840489b1d657de998500ec4  box/ideation-20260910T2300Z-prep/PINS.json
c1a5a5eda441e9756ca90e998d1da9daf7bc235462da23f354044cdfcef52983  box/ideation-20260910T2300Z-prep/inputs/approaches.md
c235fca15b48d29860291e26b7c8056915110deb1a9dc15b7ff1a20926d8d4ac  box/ideation-20260910T2300Z-prep/inputs/master46-history.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  box/ideation-20260910T2300Z-prep/inputs/binding-bd-gal.md
8f8403bed0950dec54ab78d1ba5fdd0ac1dcb9e586bd3a181ada0b67c7c07ea1  box/ideation-20260910T2300Z-prep/inputs/reduction-interfaces.md
67e8407c4e1bdece4d1b523ea35b1a5404499eadcbdf58cce8f200c26c0c68ae  box/ideation-20260910T2300Z-prep/inputs/previous-synthesis.md
0643cf030d64989b0ab20893cb5208669f2c56b469c396485d6ea9c37c35a2f8  box/ideation-20260910T2300Z-prep/inputs/latest-websweep.md
53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312  box/ideation-20260910T2300Z-prep/inputs/allr-kernel-producer.md
097736365b7afcd0701c83063ee87a691532491124106d0346f9c2dfbb8b4617  box/ideation-20260910T2300Z-prep/inputs/allr-kernel-first.md
a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5  box/ideation-20260910T2300Z-prep/inputs/whole-euler-source.md
890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5  box/ideation-20260910T2300Z-prep/inputs/leading-rank7.md
360c625219de44a7e286a6284cd9fc1ccc7b1b8a76bcfd585976f7371b1a8093  box/ideation-20260910T2300Z-prep/inputs/packet-guide.md
9a31befd0c555474918e9888770f06ee3d25f2a795c65dfe1a287db4e7d4cdc7  box/ideation-20260910T2300Z-prep/inputs/common-contract.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
f0d471001ebe7dbd92157fb4c3785c4e57593ca9122250920ff22bc44974f423  box/ideation-20260910T2300Z-prep/fable-invite.prompt.md
JC2_2300_PINS
test ! -e xmodel/ideation-20260910T2300Z-fable5.md
test ! -e xmodel/ideation-20260910T2300Z-fable5.run.v2
test ! -e xmodel/ideation-20260910T2300Z-fable5.log
test ! -e box/ideation-20260910T2300Z-fable5
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-ideation2300-term-20260910 --on-calendar='2026-09-10 23:18:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-ideation-20260910T2300Z-fable5.service
systemd-run --user --unit=jc2-ideation2300-kill-20260910 --on-calendar='2026-09-10 23:18:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-ideation-20260910T2300Z-fable5.service
systemctl --user is-active jc2-ideation2300-term-20260910.timer jc2-ideation2300-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-ideation-20260910T2300Z-fable5.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude ideation-20260910T2300Z-fable5 box/ideation-20260910T2300Z-prep/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-ideation-20260910T2300Z-fable5.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-ideation-20260910T2300Z-fable5.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-ideation-20260910T2300Z-fable5.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

