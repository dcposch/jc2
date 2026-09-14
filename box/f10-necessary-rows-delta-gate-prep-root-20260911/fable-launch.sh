#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 06:21:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
8a7bd82ea589744a9de22b54877156a329d724185948538958801475f983760e  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-produce.py
5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a  box/f10-necessary-rows-producer-astra-20260911/produce.py
592df59a401a2bf292b36214496b748cf6370c17f6bf65319db67e6245a210c4  box/f10-necessary-rows-producer-astra-20260911/produce.diff
5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-authority.py
804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4  box/f10-necessary-rows-producer-astra-20260911/authority.py
6d74b9d7c879ad921a0c72f71d1a67d13fce933daa0b796653077487662f5c47  box/f10-necessary-rows-producer-astra-20260911/authority.diff
5052884779d781e55693115c3065db1207667ce224a5914bbb95721d0abe9f7b  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-check.py
1d2d5b5408bfbf13b96f09453b1f14dfe884d261e702843bc31e5a043ffa53d1  box/f10-necessary-rows-checker-astra-20260911/check.py
7ba8b176f40c37c9643856135f4d8a17fbe9d3f08b148f39c685c8158fc07044  box/f10-necessary-rows-checker-astra-20260911/check.diff
f5b6e6c43da4574c1dd9fc241d2f0596071ab505d561e67579eb28d382814480  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-dispatch.py
073e22dbcfa3a11a2afaf6fd9c845ca6ad1d0038ccd3fddc22db21e9f5beeb24  box/f10-necessary-rows-runtime-astra-20260911/dispatch.py
f3c61b9a40d16e953950e3ff6a65401475a719fae6dbe3e1386cd05c49ef515f  box/f10-necessary-rows-runtime-astra-20260911/dispatch.py.diff
09845fabff9a8b7f997e3b2d01160e5ff51d728124b9f5cd0b7176f8c19ea063  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-probe.py
5f1211e1a77b5ce2bb4cc496deabc533e3c41cdea88ea750149dac886cc09c69  box/f10-necessary-rows-runtime-astra-20260911/probe.py
6fccfd82949cc678b4c423690e098e02f902e0a62f89d9efed5c2c6dee386432  box/f10-necessary-rows-runtime-astra-20260911/probe.py.diff
cc0621aa44d17b1dac346e87d20a53f69ce950b343d68c8ed0d3791d42120af0  box/f10-necessary-rows-delta-gate-prep-root-20260911/old-mutate.py
12eac7bbe5566ac0372c51b36617409e0501595024d948d6086a767f90d84eec  box/f10-necessary-rows-runtime-astra-20260911/mutate.py
f5e3967d1603fb3e02ed0cb4a21ab306c866227f4e892a2f5c79414f2e19ed73  box/f10-necessary-rows-runtime-astra-20260911/mutate.py.diff
acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73  box/f10-direct-rows-powerfix-astra-20260911/arithmetic.py
9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e  box/f10-direct-rows-checker-astra-20260911/check_arithmetic.py
176363939a8aa6861995cd72a99c61f7d04bfeab5a9634f6d3143dcd3d3bd098  box/f10-necessary-rows-root-20260911/ROOT-ADOPTED-NECESSARY-ROWS.md
8e07e419d321b09ecd13c61a1c5fdc3dbaf9a099c1a1ebedf9b9fe6ef280073b  xmodel/f10-necessary-rows-design-gate-fable5-20260911.md
feef0643e84fbd28307c3bd3469fba974fa6b7f58ed0ef42bc2f92aa3c597aa3  box/f10-direct-rows-deployment-prep-root-20260911/ROOT-SOURCE-CONTRACT.json
0d6cb121ebdd769fb909608043b38e6ef08923d6e6a0411ca5ec057325169784  xmodel/f10-direct-rows-code-gate-fable5-20260911.md
a02f120acda2439197a9fc173ec068ec0a5a208ec8d15f6b96cc9dfe65ee6ff9  xmodel/f10-direct-rows-runtime-gate-fable5-20260911.md
7beffe39c68b19e2998edc02949f8d24b3fe55a925d53139dff1c27a6690a482  box/f10-necessary-rows-delta-gate-prep-root-20260911/ROOT-NECESSARY-ROWS-CANDIDATE.json
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
5bd4db6a32ea6f394966f952338ed9ccc3d1eae7730497ac41bfe1a06f2b1099  box/f10-necessary-rows-delta-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/f10-necessary-rows-delta-gate-fable5-20260911.md
test ! -e xmodel/f10-necessary-rows-delta-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-necessary-rows-delta-gate-fable5-20260911.log
test ! -e box/f10-necessary-rows-delta-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3necessarydelta-term-20260911 --on-calendar='2026-09-11 06:42:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3necessarydelta-kill-20260911 --on-calendar='2026-09-11 06:42:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3necessarydelta-term-20260911.timer jc2-f10-r3necessarydelta-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-necessary-rows-delta-gate-fable5-20260911 box/f10-necessary-rows-delta-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-necessary-rows-delta-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
