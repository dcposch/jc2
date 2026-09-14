set -eu
cd /home/ubuntu/jc2
sha256sum -c <<'JC2_REVIEW_INPUTS'
e115b8e3d3e749560b386db70b62bef113d082bd80b90ddb2c6af77e1b3fc5af  xmodel/f10-r2-fullunit-ready-actual-root-20260910.md
42344f9b020dc962b0a3d073c87ee5a36c7f98b33ce53e2c3c1b9138ef9f55fd  xmodel/f10-r2-semantic-ready-result-gate-fable5-20260910.md
22fea3eeeea5a9877eb2749384294f070b174889b42a210804665a0fa617a918  xmodel/f10-r2-fullunit-modular-code-gate-fable5-20260910.md
eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317  xmodel/f10-r2-fullunit-runtime-gate-fable5-20260910.md
e78db151ddfda1bc974887ccc6350e2eae01c4d062bffb9929edd5a51925462b  xmodel/f10-r2-highest-ready-result-gate-fable5-20260910.md
f774640bc2093ba4745cae52f5892170923c79d7ad80a400d00ddd06814d2200  xmodel/f10-r2-modular-fullsource-route-astra-20260910.md
c5cb181aa28bd5d49971b02b68721e335b0972876f9cc1e8c2444d2f73c9af63  xmodel/f10-r2-modular-fullsource-gate-fable5-20260910.md
8113a3b52560e1b341b0087758ee8ff421601ed40cd0ebaf7d4ec5dce7ae5681  box/f10-r2-fullunit-ready-typefix-execution-20260910/CUSTODY.json
ed4173cff602b016951e178818bdfd3bef1fe7be5f8bfcdafce7ef1e6aa277ea  box/f10-r2-fullunit-ready-typefix-execution-20260910/ROOT-REGISTRATION.json
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  box/f10-r2-actual-execution-prep-20260910/harvest/run/jc2-r2-20260910T1230/frozen/artifact.json
a8890f17f04e9d4b54dfb68e7ff13e3ab192baa1235abc0004ba7a75b5f72cfe  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/candidate.json
785a0363aeb23cddbf56a34eb9e876cf115ab85dcbc17029a84b6c3f11549de6  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/changed.json
d1dac8345b925f5511967396da41e7232eeec40c85cc140bfaf4753f23c5840b  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-produce.receipt.json
f382b4a46ad0fd0e4d7d97ac2ccc37719ea8af002c8215f1df938d577257e911  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-positive.receipt.json
00815dc07ef192b6045f786461097536fdd087476d9115e203974778f720dac2  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/mutate.receipt.json
ed4c2a48430ff7692d3b59168ba403dce0eae1a1faf7aed13cad6c49b0a6ec9d  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-binding.json
399a74d08daf911cd59e38a0eddfdab40288ec19db9d5e403053be58a220c550  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.stderr
262cd2fc2ee2a5d3a788cdfabd4db045664cc74872880af8aeaa9ecea18f7ff9  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.telemetry.json
d573b833257eb9607c932438a1ae621177c225aacff51877a4103c37f4ac29e7  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.pre.json
22f48da46c07c6cef3820ac69d0a51797757438e1553042fc2d09f9f3c553811  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.post.json
f16499874a834599cf6ad07cd02510f8defe9e78b395a7a2cd53c79112089a6d  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.python-live.json
1b1c47d23c5944168395e05c736bd0f10359b4ee5c4aade764b35fe07b776c7b  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.telemetry.json
94d11c0c549e9532cbd68c7a8438b8e39bcfa12d7ab32adfac555bb81ef3914a  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.pre.json
aa111416464967e32e38f49c08811c0bcb0881e9a8109aecfff636c2db1c02e5  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.post.json
344637a9bb3897779e157d4b689d4161cdbde3ea82f5600486908aa2ca19a5ec  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.python-live.json
dbb1ece76588f20494dc2f3bb1d97c61ed081bf10e02fef50fe7197aa1626f60  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.telemetry.json
0a4dbb6ac66ba525705eeb9dac6cfe5f5993cff54ad40a430f6b6e15fe83330f  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.pre.json
beb6b01751ddc1da8fd81732ecabba80430cf97ed65464ad55239bc623869d19  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.post.json
e9d72b7d9f789d9b7e913b3ce9270cb2c4e43f8639f3ca1b09c37147753c76f2  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.python-live.json
4274618cf4c52e41ac57ca889bb756d006a2890c879b47368fdd91f2220dcbd1  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.telemetry.json
615e38dfe779abf5a098e0ea6c373b7afc0c2f31b9f1c2e317f243f4e8d8e9d5  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.pre.json
31c1b32542bf8c46d66b44c7890080117ea417f6d4f7ccdef716c75c212c23eb  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.post.json
ad27d1feeb65e1df7bb792b9b445f5f094f0ce34961d0164aefd536c535a0c8a  box/f10-r2-fullunit-ready-typefix-execution-20260910/harvest/run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.python-live.json
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
JC2_REVIEW_INPUTS
test ! -e xmodel/f10-r2-fullunit-ready-result-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-fullunit-ready-result-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-fullunit-ready-result-gate-fable5-20260910.log
test ! -e box/f10-r2-fullunit-ready-result-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-fullunitreadyresult-term-20260910 --on-calendar='2026-09-10 19:00:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-fullunitreadyresult-kill-20260910 --on-calendar='2026-09-10 19:00:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-fullunitreadyresult-term-20260910.timer jc2-r2-fullunitreadyresult-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-fullunit-ready-result-gate-fable5-20260910 box/f10-r2-fullunit-ready-result-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-fullunit-ready-result-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
