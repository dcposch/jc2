#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 22:30:00 UTC' +%s)"
sha256sum -c <<'JC2_MASTER_GATE_PINS'
05d0e3f23b4c769910f6295022e8cb467996a5cf7551fcd9041f762fa4cf19aa  box/f10-all-r-kernel-highest-gate-prep-20260910/ROOT-DELTA.md
53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312  xmodel/f10-all-r-kernel-highest-interface-astra-20260910.md
7512ae1ced5afd80708f26eb17616afe769288223a01082ceb4677f84a5e9134  box/f10-all-r-kernel-highest-interface-prep-20260910/ROOT-CARD.md
a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5  xmodel/f10-whole-mate-euler-elimination-astra-20260909.md
85e7b800829b0af63b7217d7d9a3ac5e1190dc1128fb664b1500a4aa8b11369b  xmodel/f10-all-r-early-band-tower-astra-20260909.md
5282cf73f7be20ecdf0bef9613764a78fd4ec030b01dc78257a4b1c1d86dee8c  xmodel/f10-all-r-middle-band-astra-20260909.md
b5de468d2283b732cde7cfde02eb4457a70713743682870ed1e7940129cef3a2  xmodel/f10-all-r-critical-band-astra-20260909.md
55f370386f0835d3c69e5eddc40ef8fc306721bc5c97ced8b15c98d5940b6ced  xmodel/f10-all-r-ell-column-unit-root-20260910.md
b6c5e8946104e797e2ee61ae6693aaf1ef24f98444eb8c5b7a21383153a668e1  xmodel/f10-all-r-scale-cover-astra-20260910.md
8158a7b54c441b4649f9e005a8d5e8a6f976364f8cc9154482ca167359b48123  xmodel/f10-all-r-late-unit-composition-astra-20260910.md
21700e6419dc0f8878f103ccd84655e2f8dc0c9f7b01e5068adcd030df35e819  xmodel/f10-all-r-late-unit-composition-gate-fable5-20260910.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
1dfd04ba70a5026cf4cb0871f80d982c86cf8a2843d1f1a826587e38912831eb  box/f10-all-r-kernel-highest-gate-prep-20260910/root-invite.prompt.md
JC2_MASTER_GATE_PINS
test ! -e xmodel/f10-all-r-kernel-highest-interface-gate-fable5-20260910.md
test ! -e xmodel/f10-all-r-kernel-highest-interface-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-all-r-kernel-highest-interface-gate-fable5-20260910.log
test ! -e box/f10-all-r-kernel-highest-interface-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-masterhighestgate-term-20260910 --on-calendar='2026-09-10 22:50:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service
systemd-run --user --unit=jc2-masterhighestgate-kill-20260910 --on-calendar='2026-09-10 22:50:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service
systemctl --user is-active jc2-masterhighestgate-term-20260910.timer jc2-masterhighestgate-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1440 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-all-r-kernel-highest-interface-gate-fable5-20260910 box/f10-all-r-kernel-highest-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-all-r-kernel-highest-interface-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

