#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 21:47:00 UTC' +%s)"
sha256sum -c <<'JC2_ACTUAL_GATE_PINS'
7041a28bfa457f97e428a6fab166b10ebf42dfa455b4b2a71f884b3691626517  xmodel/f10-contact-gram-execution-root-20260910.md
6ac475677fc7bf29c14be8c5988714e318704d7d22df27915ceb86c44014acbc  box/f10-contact-gram-execution-prep-root-20260910/harvest/var/lib/jc2-contact-gram-20260910T2110/custody/CUSTODY.json
e7830438b4448bebc389e27032df76c70202ced6f96e7f1145bfa4a585bd8220  box/f10-contact-gram-execution-prep-root-20260910/PREFLIGHT-METADATA.md
a8afb73605044061dea04a57aa1eea410e48b82120a961127738d503831e2877  box/f10-contact-gram-execution-prep-root-20260910/SCIENCE-METADATA.md
18b7adba04c17b74b7454733de53b7070159e6d0a607a457f8db4b8aee9ee869  box/f10-contact-gram-execution-prep-root-20260910/ROOT-REGISTRATION.json
dc72ba96108723c92a91fc9b212b4abf8ef8e9249844021cef4e139b74bbf9b0  box/f10-contact-gram-execution-prep-root-20260910/harvest/home/ubuntu/jc2-contact-gram-20260910T2110/stage/terminal-manager.jsonl
60968163acd2da84fe2d31f0189d899fa052d02561ef146ae931e7a2de4c0203  box/f10-contact-gram-execution-prep-root-20260910/outer-launch-grep.sh
709a2a598fbd8d9aed6436cbbe8c2fc58a840e15b502183b0a37c94cc0fbd0cb  box/f10-contact-gram-execution-prep-root-20260910/ROOT-SETUP-CORRECTION.md
531c249cd7a0ff6a9e982b798c462ca6a4656150e114fb882d0d9d70f9e1863b  xmodel/f10-contact-gram-code-gate-fable5-20260910.md
f2b342ad61cab88a6ad8d89ca9fcdc76f143605b23e23dbf4e78f92957926cae  xmodel/f10-contact-gram-runtime-gate-fable5-20260910.md
f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2  xmodel/f10-contact-real-window-astra-20260910.md
ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068  xmodel/f10-contact-quartic-gram-gate-fable5-20260910.md
96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13  xmodel/f10-contact-symmetric-remainder-astra-20260910.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
72b24cc2268dedaa0f58f00446dd770f02a1e506f0db3ca2cdf9c97e14d7e1be  box/f10-contact-gram-execution-relative-gate-prep-20260910/root-invite.prompt.md
JC2_ACTUAL_GATE_PINS
test ! -e xmodel/f10-contact-gram-execution-relative-gate-fable5-20260910.md
test ! -e xmodel/f10-contact-gram-execution-relative-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-contact-gram-execution-relative-gate-fable5-20260910.log
test ! -e box/f10-contact-gram-execution-relative-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-contact-gramactualrelative-term-20260910 --on-calendar='2026-09-10 22:05:39 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service
systemd-run --user --unit=jc2-contact-gramactualrelative-kill-20260910 --on-calendar='2026-09-10 22:05:44 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service
systemctl --user is-active jc2-contact-gramactualrelative-term-20260910.timer jc2-contact-gramactualrelative-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-contact-gram-execution-relative-gate-fable5-20260910 box/f10-contact-gram-execution-relative-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-contact-gram-execution-relative-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
