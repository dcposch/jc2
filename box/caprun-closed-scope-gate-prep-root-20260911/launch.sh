#!/bin/bash
set -euo pipefail
cd /home/ubuntu/jc2
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 08:01:00 UTC' +%s)"
sha256sum -c <<'JC2_REVIEW_PINS'
d78d45ef671c706706a12f4179abbc777684da13673263e54461c74351d453a3  box/caprun-closed-scope-implementation-astra-20260911/run_capped.py
52b3d916f4fc3941bb98c8b4f7698ab940680d09ee4e065de1f167857e3fd436  box/caprun-closed-scope-implementation-astra-20260911/dispatch.py
e4ca3c4bec335373d8fff34da8d0dac697bd89065c1c6805befa6a437e6dc91e  box/caprun-closed-scope-implementation-astra-20260911/probe.py
b8c1cfefd98a2c771fbc64ecdaac2603eafb91893b158bb00dd34ea6d4916b4d  box/caprun-closed-scope-implementation-astra-20260911/mutate.py
0e62e3fcaa0f3a299c2618206d33a38a98bdb9029f6f2e73af67f56f2efab1f8  box/caprun-closed-scope-implementation-astra-20260911/run_capped.diff
4ff4bfc5a6d110c14dc27c2e69ac80fe936d7090724c475d71bd699b03ccd1e2  box/caprun-closed-scope-implementation-astra-20260911/dispatch.diff
cfc4f8de83fa917bb56bfbac5ca883952aa7a685959ea5c13c96242b68b513aa  box/caprun-closed-scope-implementation-astra-20260911/probe.diff
1b26121339970b90e23830e61cd56a49bd2a1ffb72bfcf15d6553989998397b8  box/caprun-closed-scope-implementation-astra-20260911/mutate.diff
af7a2fab4aa6317f7386e438f2f03acc6daffdd04c3deee6a6554b675089ee81  box/caprun-closed-scope-implementation-astra-20260911/CONTRACT.md
c3a7db59b4c450ca2fc939b1c2056f54d8a5b57b46b081b787eadf6486042ba0  box/caprun-closed-scope-implementation-astra-20260911/PINS.json
eedd42920da74957d55e94f7c4ae47448d9c389da4c722a48b312aefebe1ed37  xmodel/caprun-closed-scope-implementation-astra-20260911.md
524d80c1c8cb2fc4670a25c47799404fa869b009065c1757187ae1182065b0f5  xmodel/caprun-closed-scope-implementation-astra-20260911.md.artifact.json
2a5cc42112ed2f3521772675fc3231cdd5086aaa66bc288d9633c6bc3bda59b2  box/caprun-closed-scope-implementation-astra-20260911/custody.json
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  box/caprun-closed-scope-gate-prep-root-20260911/old-run_capped.py
073e22dbcfa3a11a2afaf6fd9c845ca6ad1d0038ccd3fddc22db21e9f5beeb24  box/caprun-closed-scope-gate-prep-root-20260911/old-dispatch.py
5f1211e1a77b5ce2bb4cc496deabc533e3c41cdea88ea750149dac886cc09c69  box/caprun-closed-scope-gate-prep-root-20260911/old-probe.py
12eac7bbe5566ac0372c51b36617409e0501595024d948d6086a767f90d84eec  box/caprun-closed-scope-gate-prep-root-20260911/old-mutate.py
dee6b9472b5e2151963569342d2d9ad905524894e63f3a91c537d2589fbf69c5  xmodel/caprun-false-quiet-diagnosis-astra-20260911.md
e42ff6aaf6277c94e12e0a1a2fd5b8a97ad8fa408d137a84e81fd3d00c616acd  box/caprun-closed-scope-gate-prep-root-20260911/kernel-v7.0-cgroup-v2.rst
ed01e8cd99dfffe35672263a86e6da82c7768b6973d9bd7ae47a150a51bd15ef  box/caprun-closed-scope-gate-prep-root-20260911/kernel.source.json
eb1074585ce62af638d15680bd13ba99aab25c9b6cbed7ac88ae21b60f060f3b  box/caprun-closed-scope-gate-prep-root-20260911/cpython-v3.12.3-posixsubprocess.c
76a646589c52183032769a2b8a65773e81c91b047a406e83b51e6300154aff64  box/caprun-closed-scope-gate-prep-root-20260911/python.source.json
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
a2020e61cd106fbdca619fbb2c1f9ef2e126886f301dce025e3e33ca31ab117b  box/caprun-closed-scope-gate-prep-root-20260911/fable-invite.prompt.md
JC2_REVIEW_PINS
test ! -e xmodel/caprun-closed-scope-code-gate-fable5-20260911.md
test ! -e xmodel/caprun-closed-scope-code-gate-fable5-20260911.run.v2
test ! -e xmodel/caprun-closed-scope-code-gate-fable5-20260911.log
test ! -e box/caprun-closed-scope-code-gate-fable5-20260911
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-caprun-closedscope-term-20260911 --on-calendar='2026-09-11 08:23:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service
systemd-run --user --unit=jc2-caprun-closedscope-kill-20260911 --on-calendar='2026-09-11 08:23:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service
systemctl --user is-active jc2-caprun-closedscope-term-20260911.timer jc2-caprun-closedscope-kill-20260911.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=2400 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude caprun-closed-scope-code-gate-fable5-20260911 box/caprun-closed-scope-gate-prep-root-20260911/fable-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,comm=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-caprun-closed-scope-code-gate-fable5-20260911.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
