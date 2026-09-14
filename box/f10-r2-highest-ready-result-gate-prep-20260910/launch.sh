set -euo pipefail
test "$(sha256sum 'xmodel/f10-r2-highest-ready-actual-root-20260910.md' | cut -d ' ' -f 1)" = '272f2b4b460a51a9478f2e393b4c295a0531286cfce16ec68d44a00349959bd4'
test "$(sha256sum 'xmodel/f10-r2-highest-modular-code-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '94bbf7f57e3535000560f2a1494ab15c21cde9455bb05ea7ce2ece003dd23ba5'
test "$(sha256sum 'xmodel/f10-r2-highest-modular-runtime-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '8358693287a2874f05b431ab0081c98db9461bdc6eaf06be33f40a2f83c72ca8'
test "$(sha256sum 'xmodel/f10-r2-highest-status-fix-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '85ce5e9ab2067ae07033fca52e0c4d0c8853032133f9799d388d8d0745c24698'
test "$(sha256sum 'xmodel/f10-r2-semantic-ready-result-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = '42344f9b020dc962b0a3d073c87ee5a36c7f98b33ce53e2c3c1b9138ef9f55fd'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/CUSTODY.json' | cut -d ' ' -f 1)" = 'f8fc2182a7eb3ce888f639e6ce4030f18b8bed0532d46e0604042dada4f10f10'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/ROOT-REGISTRATION.json' | cut -d ' ' -f 1)" = '476ebfff4ec5ddb46e656d87e4509d5e61f731704a0a5a5ae2d63acd5b1ba887'
test "$(sha256sum 'box/f10-r2-actual-execution-prep-20260910/harvest/run/jc2-r2-20260910T1230/frozen/artifact.json' | cut -d ' ' -f 1)" = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/frozen/candidate.json' | cut -d ' ' -f 1)" = '0f61b24dd6978ed646cba9fb872988bbcfef480f0290ea20ad7803b1ae369875'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/frozen/changed.json' | cut -d ' ' -f 1)" = 'a1276deef8b2cb53c7d59b40a425cb0cc009ae8d0baf56fdcf793082fff6c013'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/frozen/highest-produce.receipt.json' | cut -d ' ' -f 1)" = '6112970870d344a056dcbc61d1a3676b8399fbdbef322fd67f071f81968814c3'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/frozen/highest-positive.receipt.json' | cut -d ' ' -f 1)" = '6b76278e468fd5233b6ec1b9456ed1bffb2eb8dfb47577cf3af47fd240aeed09'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/frozen/mutate.receipt.json' | cut -d ' ' -f 1)" = '38fb84ef232ec19a402582833ee13c3f6c1cea3f324607c25df8ed57dc2e0d80'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-binding.json' | cut -d ' ' -f 1)" = '144bfa010ecec73a8b2d8b4109268f2d0e6d678f7c6a82d978b19c7c0faeb5c5'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-negative.stderr' | cut -d ' ' -f 1)" = '5422b1a0ac465f9d9e6631a47d1a1219cdaf59bd0ae3bd81372bc1404f24bfe9'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-produce.telemetry.json' | cut -d ' ' -f 1)" = '79d33883ee049bde3d8bf5129e08b23343f2520dc1ae5a34f7d121e1f197fc5a'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-produce.pre.json' | cut -d ' ' -f 1)" = '3a0d60b77ddb6dd4cab40cda5ed0588a8cb8d70a47c8c2653b8b78d170915a75'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-produce.post.json' | cut -d ' ' -f 1)" = '4f14732c158bd13063187d9238dab18e82ca17093836cf831bed748a9046cdcb'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-produce.python-live.json' | cut -d ' ' -f 1)" = 'b3ac997fcb40f393b5cdde9f6a42e07d574c7a310425cb48fbed2da26d280a09'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-positive.telemetry.json' | cut -d ' ' -f 1)" = 'd499c36eb7d7c43efc361cbe25e52254a7cb99ba4e27404b81958d75f99da6ae'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-positive.pre.json' | cut -d ' ' -f 1)" = 'ce93dab5a481a933618b29d85c3f9bd71f8da4604dbffd1c8f42b9f2b4d3f430'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-positive.post.json' | cut -d ' ' -f 1)" = '29665dd7241e421d9621f9b2c30757e37cef846f65cefb031e145cf45cc995e4'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-positive.python-live.json' | cut -d ' ' -f 1)" = 'a5c228b6ab39cdf537b31e3ac6ae7f71a0b26485d5cd46849e4b8db4dd642b7e'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/mutate.telemetry.json' | cut -d ' ' -f 1)" = '86aa803638cd248bce1064ad7116d1a886f63d33bd010b60f2e4f969635b8c41'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/mutate.pre.json' | cut -d ' ' -f 1)" = '4377a71aae46d0976e974de595cbbb610612a4d5b8067f6b6178a146d764ef14'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/mutate.post.json' | cut -d ' ' -f 1)" = '13344f457959bd44b5fd8f68191b74aa6bc622a92589501a303222095eba8e96'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/mutate.python-live.json' | cut -d ' ' -f 1)" = '2ab4594d31fa6091d93389e39ec6792f897ee70e88bc8009b2c5b97a33df4e53'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-negative.telemetry.json' | cut -d ' ' -f 1)" = 'f9dc008f498f7397837905ff95568e046444a0cbc1773626243669c800913656'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-negative.pre.json' | cut -d ' ' -f 1)" = '0542814a31dd54aa31810b33f1f91e84fe1de182a8c9d7c2f6d703f7a537333b'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-negative.post.json' | cut -d ' ' -f 1)" = '76c272fe9450369ca3c71fae0c4bb71ad219797f215f8264ead142abf4223ec8'
test "$(sha256sum 'box/f10-r2-highest-ready-execution-20260910/harvest/run/jc2-r2-highest-ready-20260910T1720/highest-negative.python-live.json' | cut -d ' ' -f 1)" = '95ffeedac5d0e94e1fc12e497b550539d381e8fa16b2531e63ce916760669a73'
test "$(sha256sum 'ops/adapters/claude.sh' | cut -d ' ' -f 1)" = '34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699'
test "$(sha256sum 'ops/lane.sh' | cut -d ' ' -f 1)" = '0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396'
test "$(sha256sum 'ops/validate_charge_basis.py' | cut -d ' ' -f 1)" = 'a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e'
test "$(sha256sum 'ops/seal.py' | cut -d ' ' -f 1)" = '222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776'
test "$(sha256sum 'FALLACY-v2.md' | cut -d ' ' -f 1)" = 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5'
test ! -e xmodel/f10-r2-highest-ready-result-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-highest-ready-result-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-highest-ready-result-gate-fable5-20260910.log
test ! -e box/f10-r2-highest-ready-result-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-highreadyresult-term-20260910 --on-calendar='2026-09-10 18:07:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-highreadyresult-kill-20260910 --on-calendar='2026-09-10 18:07:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-highreadyresult-term-20260910.timer jc2-r2-highreadyresult-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-highest-ready-result-gate-fable5-20260910 box/f10-r2-highest-ready-result-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-highest-ready-result-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

