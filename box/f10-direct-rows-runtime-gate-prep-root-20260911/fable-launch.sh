#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 03:51:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
f5b6e6c43da4574c1dd9fc241d2f0596071ab505d561e67579eb28d382814480  box/f10-direct-rows-runtime-astra-20260911/dispatch.py
09845fabff9a8b7f997e3b2d01160e5ff51d728124b9f5cd0b7176f8c19ea063  box/f10-direct-rows-runtime-astra-20260911/probe.py
cc0621aa44d17b1dac346e87d20a53f69ce950b343d68c8ed0d3791d42120af0  box/f10-direct-rows-runtime-astra-20260911/mutate.py
e2ce5a5f91a61a253e0d355fbb3c982b0968bd2e4bd05a7fcb9eeab95fe402a1  box/f10-direct-rows-runtime-astra-20260911/CONTRACT.md
eab97643f515b17716e86f72689a46a1dc73eb9091c1c90b789f690bfa7aeeae  box/f10-direct-rows-runtime-astra-20260911/DISABLED-REGISTRATION.json
f5f283bc68bfd35cbdc1019c0f7c13f8cd656e47ab11dce9a491552a4c9b3d0f  box/f10-direct-rows-runtime-astra-20260911/DISPATCH.diff
ee0f1b5b9ec44db883a803df48375e66b79f82e8d35d09e55b4dd62bf6e9b614  xmodel/f10-direct-rows-runtime-astra-20260911.md
05775a6f4484e677aff987ef0f203861440721801471fb6f4b20a782cdcbeb11  xmodel/f10-source-cone-r3-runtime-gate-fable5-20260911.md
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  ops/run_capped.py
90c940b021ba9f99f2298aaf394cb082793812ad4428e249b970ecf06baa6c47  xmodel/f10-direct-rows-wire-root-20260911.md
2b2770fe494098812a52c6829a4bd97803f44bb0474863b8008a69f3725956fd  box/f10-direct-rows-wire-root-20260911/ROOT-ADOPTED-WIRE-PINS.md
a0a40804071a6dac83eaf6acf38073229a6d15c8866af32e283015d65c1c74e7  box/f10-direct-rows-parallel-prep-root-20260911/ROOT-AUTHOR-INTERFACE.md
5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29  box/f10-direct-rows-producer-astra-20260911/authority.py
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
5efe13bda6a5d8b6bbcc6dee5273797eb7c17b7b5a36c5bace47518eebd2f1f1  box/f10-direct-rows-runtime-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/f10-direct-rows-runtime-gate-fable5-20260911.md
test ! -e xmodel/f10-direct-rows-runtime-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-direct-rows-runtime-gate-fable5-20260911.log
test ! -e box/f10-direct-rows-runtime-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3directrt-term-20260911 --on-calendar='2026-09-11 04:16:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3directrt-kill-20260911 --on-calendar='2026-09-11 04:16:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3directrt-term-20260911.timer jc2-f10-r3directrt-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-direct-rows-runtime-gate-fable5-20260911 box/f10-direct-rows-runtime-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-direct-rows-runtime-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

