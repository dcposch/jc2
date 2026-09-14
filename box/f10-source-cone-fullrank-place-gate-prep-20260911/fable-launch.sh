#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 00:44:00 UTC' +%s)"
sha256sum -c <<'JC2_R3_RANK_PINS'
11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b  xmodel/f10-source-cone-fullrank-place-astra-20260911.md
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  xmodel/ideation-20260910T2300Z-astra-source.md
7dae0ba7c0c03418676d55a93b7deebcd01805b212ab13e284ce59b3bebf691a  xmodel/ideation-20260910T2300Z-cross-fable5.md
890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5  xmodel/f10-middle-univariate-unit-astra-20260910.md
460129a51fce4ee17d5d71815be014cbb4075dee71a39bb269721761ba29e97d  xmodel/f10-middle-septic-irreducibility-astra-20260910.md
df3b91a0a16360cde2436943bd8783def5c848d25c9c3770a175a7a49d1786db  xmodel/f10-middle-septic-irred-gate-fable5-20260910.md
4576a030642db9808094f31db59faa7d48014cc313fce292b16418c9e2bd1180  xmodel/f10-source-cone-unit-pivot-contract-root-20260911.md
d1e87f980894090ec6104db2c3ac4dc5726d269fb42240dc187734fe211c484f  xmodel/f10-source-cone-unit-pivot-gate-fable5-20260911.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
fe0a5d58d94fd4a4f12f7733511768298d9dfb2987c9b377696899da6fb810f4  box/f10-source-cone-fullrank-place-gate-prep-20260911/fable-invite.prompt.md
JC2_R3_RANK_PINS
test ! -e xmodel/f10-source-cone-fullrank-place-gate-fable5-20260911.md
test ! -e xmodel/f10-source-cone-fullrank-place-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-source-cone-fullrank-place-gate-fable5-20260911.log
test ! -e box/f10-source-cone-fullrank-place-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-rankplace-term-20260911 --on-calendar='2026-09-11 00:56:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-rankplace-kill-20260911 --on-calendar='2026-09-11 00:56:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-rankplace-term-20260911.timer jc2-f10-rankplace-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-source-cone-fullrank-place-gate-fable5-20260911 box/f10-source-cone-fullrank-place-gate-prep-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-source-cone-fullrank-place-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

