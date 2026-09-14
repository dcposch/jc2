#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 00:38:00 UTC' +%s)"
sha256sum -c <<'JC2_R3_SOURCE_PINS'
8b8c6296f3e94b0b176631d848bfe0cca11ba6eac64877196d0a129df212f30a  xmodel/f10-source-cone-r3-code-astra-20260911.md
407c5784ba07abbf289e2ba4fd82f24fc661987eb55f378bf39cc954da1ee07b  box/f10-source-cone-r3-code-astra-20260911/authority.py
40b18453b6127d1b8217a6d6e1d3eb3aff1e911c15243ed9c640277f24175431  box/f10-source-cone-r3-code-astra-20260911/arithmetic.py
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  box/f10-source-cone-r3-code-astra-20260911/produce.py
10e57542f9aa06eb69fd9562b2aa0bb27567c6d14186ffa90d77d6e08e80ae2c  box/f10-source-cone-r3-code-astra-20260911/check_arithmetic.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  box/f10-source-cone-r3-code-astra-20260911/check.py
b742af9afa22e026607baa32934fdc63fee175bd228777a35b495b140ac641d8  box/f10-source-cone-r3-code-astra-20260911/CONTROLS.md
8a2d041b64320a1409ff0ebe870f8caf63237cd09fce91c43d6d7fd4dbcf9a4b  box/f10-source-cone-r3-code-astra-20260911/READ-SCOPE.md
1966972e0e9e2fac2d7eaf9c00c4c207a460d0ea8117320486218337684e052a  box/f10-source-cone-r3-code-astra-20260911/custody.json
a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5  xmodel/f10-whole-mate-euler-elimination-astra-20260909.md
85e7b800829b0af63b7217d7d9a3ac5e1190dc1128fb664b1500a4aa8b11369b  xmodel/f10-all-r-early-band-tower-astra-20260909.md
5282cf73f7be20ecdf0bef9613764a78fd4ec030b01dc78257a4b1c1d86dee8c  xmodel/f10-all-r-middle-band-astra-20260909.md
b5de468d2283b732cde7cfde02eb4457a70713743682870ed1e7940129cef3a2  xmodel/f10-all-r-critical-band-astra-20260909.md
55f370386f0835d3c69e5eddc40ef8fc306721bc5c97ced8b15c98d5940b6ced  xmodel/f10-all-r-ell-column-unit-root-20260910.md
b6c5e8946104e797e2ee61ae6693aaf1ef24f98444eb8c5b7a21383153a668e1  xmodel/f10-all-r-scale-cover-astra-20260910.md
8158a7b54c441b4649f9e005a8d5e8a6f976364f8cc9154482ca167359b48123  xmodel/f10-all-r-late-unit-composition-astra-20260910.md
53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312  xmodel/f10-all-r-kernel-highest-interface-astra-20260910.md
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  xmodel/ideation-20260910T2300Z-astra-source.md
7dae0ba7c0c03418676d55a93b7deebcd01805b212ab13e284ce59b3bebf691a  xmodel/ideation-20260910T2300Z-cross-fable5.md
890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5  xmodel/f10-middle-univariate-unit-astra-20260910.md
82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6  xmodel/f10-middle-full-boundary-astra-20260910.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
3a8321daa60218e122e596990152fddfd55e584c1edfa041848f6ecec8459556  box/f10-source-cone-r3-code-gate-prep-20260911/fable-invite.prompt.md
JC2_R3_SOURCE_PINS
test ! -e xmodel/f10-source-cone-r3-code-gate-fable5-20260911.md
test ! -e xmodel/f10-source-cone-r3-code-gate-fable5-20260911.run.v2
test ! -e xmodel/f10-source-cone-r3-code-gate-fable5-20260911.log
test ! -e box/f10-source-cone-r3-code-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-f10-r3source-term-20260911 --on-calendar='2026-09-11 01:03:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service
systemd-run --user --unit=jc2-f10-r3source-kill-20260911 --on-calendar='2026-09-11 01:03:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service
systemctl --user is-active jc2-f10-r3source-term-20260911.timer jc2-f10-r3source-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1800 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-source-cone-r3-code-gate-fable5-20260911 box/f10-source-cone-r3-code-gate-prep-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-source-cone-r3-code-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

