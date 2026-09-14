#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 03:42:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
3be532afc6e784842694cf02d4399573228362abb47ae36130ef97c4274faa59  box/f10-source-cone-direct-circuit-astra-20260911/OPERATIONS.md
61b9ce5e1f9b40a765dcb2a2ea5aa3a928197b61bc41cb5cf945632b99ad4de2  box/f10-source-cone-direct-circuit-astra-20260911/ASSERTIONS.md
b9060f0bbc14e92464079b0daca12faa1ba2d367f9ecc7307ba301689de5b77d  box/f10-source-cone-direct-circuit-astra-20260911/WIRE-AND-VALIDATION.md
39ed9b3910efee02dd2f17ced7951a8b83557e612d100d4ae34f76e0895b4002  box/f10-source-cone-direct-circuit-astra-20260911/ROOT-ADOPTED-CORRECTIONS.md
90c940b021ba9f99f2298aaf394cb082793812ad4428e249b970ecf06baa6c47  xmodel/f10-direct-rows-wire-root-20260911.md
68488229c5ff839f8c155662f903ba174d59d4e96bb5e046a53967313d497f1b  xmodel/f10-direct-rows-wire-gate-fable5-20260911.md
2b2770fe494098812a52c6829a4bd97803f44bb0474863b8008a69f3725956fd  box/f10-direct-rows-wire-root-20260911/ROOT-ADOPTED-WIRE-PINS.md
a0a40804071a6dac83eaf6acf38073229a6d15c8866af32e283015d65c1c74e7  box/f10-direct-rows-parallel-prep-root-20260911/ROOT-AUTHOR-INTERFACE.md
5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29  box/f10-direct-rows-producer-astra-20260911/authority.py
d196346966f09f1e9ef2a4f6e20df74f8d218c32e06d2f341ccf25fb4b39d90b  box/f10-direct-rows-producer-astra-20260911/arithmetic.py
8a7bd82ea589744a9de22b54877156a329d724185948538958801475f983760e  box/f10-direct-rows-producer-astra-20260911/produce.py
9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e  box/f10-direct-rows-checker-astra-20260911/check_arithmetic.py
5052884779d781e55693115c3065db1207667ce224a5914bbb95721d0abe9f7b  box/f10-direct-rows-checker-astra-20260911/check.py
f264cb7577a4a08ba07a403856d72af243c1bd91e5443f8f08f6da16c3528f0b  box/f10-direct-rows-producer-astra-20260911/CONTRACT.md
692c89cbe333e33c87c85f0ba92e6e39b505c57ae9f36d17814036a22c5e2833  xmodel/f10-direct-rows-producer-astra-20260911.md
bfac10237e7cbb10db0d2893c1cd14480a0fe9bfb438824f94cf8c2bf999f4a7  xmodel/f10-direct-rows-checker-astra-20260911.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
974a668f6910bc6141821042ab9fecb2344f48370ee5bcc7bd355b4870be2f71  box/f10-direct-rows-code-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/f10-direct-rows-code-gate-fable5-20260911.md
test ! -e xmodel/f10-direct-rows-code-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-direct-rows-code-gate-fable5-20260911.log
test ! -e box/f10-direct-rows-code-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3rowscode-term-20260911 --on-calendar='2026-09-11 04:05:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3rowscode-kill-20260911 --on-calendar='2026-09-11 04:05:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3rowscode-term-20260911.timer jc2-f10-r3rowscode-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-direct-rows-code-gate-fable5-20260911 box/f10-direct-rows-code-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-direct-rows-code-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
