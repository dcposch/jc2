#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 11:25:00 UTC' +%s)"
sha256sum --strict -c <<'JC2_1100_CROSS_PINS'
7b13a6f78128e86d4998dd700066ced66611a37ab67c87199f7a293b473f6ec7  box/ideation-20260911T1100Z-cross-prep/ROOT-CROSS.md
3c45826741e8bdc7222a78b5d20c118515b0d5d61d8188f02bebf65beed38e58  xmodel/ideation-20260911T1100Z-coordinator.md
43eae05446b8aeaaa15844880ea37466759342833bebca9ef00146794a1b6e32  xmodel/ideation-20260911T1100Z-astra-geometry.md
72e901ea33e07a5f6ad2f918da4c7674dc6f84e6f366f6b03d3a974d8bd4df8e  xmodel/ideation-20260911T1100Z-astra-source.md
a1f2c500c2274da314ff5f7db06252bd76bac18abbca90cb74bd88a653e5cf1d  xmodel/ideation-20260911T1100Z-fable5.md
53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312  box/ideation-20260910T2300Z-prep/inputs/allr-kernel-producer.md
9dad11eba0d7174a39c398b640a6cd42dd47c18f030cf296ceedc90c238f5792  box/ideation-20260911T1100Z-prep/inputs/previous-synthesis.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
96cf0f725cf0f174bf0d275891278e1a829e14625f88e701538f95f74142b27c  box/ideation-20260911T1100Z-cross-prep/fable-invite.prompt.md
JC2_1100_CROSS_PINS
test ! -e xmodel/ideation-20260911T1100Z-cross-fable5.md
test ! -e xmodel/ideation-20260911T1100Z-cross-fable5.run.v2
test ! -e xmodel/ideation-20260911T1100Z-cross-fable5.log
test ! -e box/ideation-20260911T1100Z-cross-fable5
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-ideation1100cross-term-20260911 --on-calendar='2026-09-11 11:35:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-ideation-20260911T1100Z-cross-fable5.service
systemd-run --user --unit=jc2-ideation1100cross-kill-20260911 --on-calendar='2026-09-11 11:35:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-ideation-20260911T1100Z-cross-fable5.service
systemctl --user is-active jc2-ideation1100cross-term-20260911.timer jc2-ideation1100cross-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-ideation-20260911T1100Z-cross-fable5.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude ideation-20260911T1100Z-cross-fable5 box/ideation-20260911T1100Z-cross-prep/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-ideation-20260911T1100Z-cross-fable5.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-ideation-20260911T1100Z-cross-fable5.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-ideation-20260911T1100Z-cross-fable5.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
