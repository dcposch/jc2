#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 22:06:00 UTC' +%s)"
sha256sum -c <<'JC2_LATE_UNIT_GATE_PINS'
bc39ffde5bc2e5bdd6c52dc513189dca40c599e63688383a42e034a16f4ef5a6  box/f10-all-r-late-unit-composition-gate-prep-20260910/ROOT-CARD.md
8158a7b54c441b4649f9e005a8d5e8a6f976364f8cc9154482ca167359b48123  xmodel/f10-all-r-late-unit-composition-astra-20260910.md
9b80a8cf5fc9708dabee6a5c7eeead399873c83a15e884b40699833ba50521a0  xmodel/f10-contact-gram-execution-relative-gate-fable5-20260910.md
7041a28bfa457f97e428a6fab166b10ebf42dfa455b4b2a71f884b3691626517  xmodel/f10-contact-gram-execution-root-20260910.md
7d87064e27a949b22da85afc47fdc658d57c5c24e25c70524867dd3da590b70b  xmodel/f10-all-r-late-contact-astra-20260909.md
03b2fe315c048598e57c6409b26bb7a3d6e797ff0f1c2a2f2040ab5a2dbc69de  xmodel/f10-all-r-late-contact-gate-fable5-20260909.md
4bbecd357077b422fbe636de61c9feefc5b304d88eea0a872b476456b1fbdf30  xmodel/f10-two-exponent-contact-discriminator-astra-20260909.md
4a46e7f605759016829fcfb8ad92586fa9ebe875c4b5a62835b603c8b0ab1e90  xmodel/f10-two-exponent-contact-gate-fable5-20260909.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
9bbb5d28af1d6b2412164f98a0f8b79895a68df4252ea1c5b6a11f836d01cee4  box/f10-all-r-late-unit-composition-gate-prep-20260910/root-invite.prompt.md
JC2_LATE_UNIT_GATE_PINS
test ! -e xmodel/f10-all-r-late-unit-composition-gate-fable5-20260910.md
test ! -e xmodel/f10-all-r-late-unit-composition-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-all-r-late-unit-composition-gate-fable5-20260910.log
test ! -e box/f10-all-r-late-unit-composition-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-lateunitgate-term-20260910 --on-calendar='2026-09-10 22:24:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service
systemd-run --user --unit=jc2-lateunitgate-kill-20260910 --on-calendar='2026-09-10 22:24:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service
systemctl --user is-active jc2-lateunitgate-term-20260910.timer jc2-lateunitgate-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-all-r-late-unit-composition-gate-fable5-20260910 box/f10-all-r-late-unit-composition-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-all-r-late-unit-composition-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

