#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 01:14:00 UTC' +%s)"
sha256sum -c <<'JC2_R3_RUNTIME_PINS'
968e4163eadde723a6dc2f9bc806994a0771912be42bd6fc836b905b1a4b1617  xmodel/f10-source-cone-r3-runtime-astra-20260911.md
f3e5128677c872eb139e7c75c6b0f7ab89081ce738c5760bed9b4195fc6ebb4b  box/f10-source-cone-r3-runtime-astra-20260911/dispatch.py
85ba351b176d6498df3df13e4dcf91ab2e2765ebabff927d35d1821bbca9df04  box/f10-source-cone-r3-runtime-astra-20260911/probe.py
fcb62c4df2f8f78cc7c349b3f19331a76284ba97bbf4e5ffd122dda12ab811cb  box/f10-source-cone-r3-runtime-astra-20260911/mutate.py
52102dc47050c7b3c725618bda8006010cd72dc4a30fba12d4e268719a2e6d9b  box/f10-source-cone-r3-runtime-astra-20260911/CONTRACT.md
a66aa1ba9aa2c18837460a1e6bf5b446c44984985cf1fb7ce58c586c504dab52  box/f10-source-cone-r3-runtime-astra-20260911/DISABLED-REGISTRATION.json
e9b64185e2dc46802befbafe7687f69ee9b0143f5a9e485ef843fd1578c499ea  box/f10-source-cone-r3-runtime-astra-20260911/READ-SCOPE.md
1ea6f2055074f5d24a538e4e074d21e0f62ad940533bffcb86781a270e3b3c5c  box/f10-source-cone-r3-runtime-astra-20260911/custody.json
407c5784ba07abbf289e2ba4fd82f24fc661987eb55f378bf39cc954da1ee07b  box/f10-source-cone-r3-code-astra-20260911/authority.py
40b18453b6127d1b8217a6d6e1d3eb3aff1e911c15243ed9c640277f24175431  box/f10-source-cone-r3-code-astra-20260911/arithmetic.py
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  box/f10-source-cone-r3-code-astra-20260911/produce.py
10e57542f9aa06eb69fd9562b2aa0bb27567c6d14186ffa90d77d6e08e80ae2c  box/f10-source-cone-r3-code-astra-20260911/check_arithmetic.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  box/f10-source-cone-r3-code-astra-20260911/check.py
558fa2f1ef15b8477148fc014df4dcbcf783b61bcddae9889213b995bcb86e16  xmodel/f10-r2-runtime-gate-fable5-20260910.md
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  ops/run_capped.py
712ac6023b6799c079e5b950822d07c20295d46788f38d64a433af7f45cd3103  xmodel/f10-source-cone-r3-code-gate-fable5-20260911.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
9928d1f26844e0ab2cad8c552fc7ed8cacf780c8a5ca5767a76cb9b0b6563b52  box/f10-source-cone-r3-runtime-gate-prep-20260911/fable-invite.prompt.md
JC2_R3_RUNTIME_PINS
test ! -e xmodel/f10-source-cone-r3-runtime-gate-fable5-20260911.md
test ! -e xmodel/f10-source-cone-r3-runtime-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-source-cone-r3-runtime-gate-fable5-20260911.log
test ! -e box/f10-source-cone-r3-runtime-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3runtime-term-20260911 --on-calendar='2026-09-11 01:44:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3runtime-kill-20260911 --on-calendar='2026-09-11 01:44:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3runtime-term-20260911.timer jc2-f10-r3runtime-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-source-cone-r3-runtime-gate-fable5-20260911 box/f10-source-cone-r3-runtime-gate-prep-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-source-cone-r3-runtime-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
