set -eu
cd /home/ubuntu/jc2
sha256sum -c <<'JC2_DEGREE_REVIEW_PINS'
32ff9aef453f1d82d479c5bad9e97e723f92dbe93ac078a870b035d6748b9a90  xmodel/f10-r2-degree-scope-astra-20260910.md
81ab7f3685e330ffac746fdcef5e911ea27d795c15265ceacc047be05b20be95  xmodel/f10-r1-degree-scope-astra-20260910.md
bd2dfc3807db534e5deb02ef1a55af75466b9b6e96b9b91e7fe63fb600886160  xmodel/f10-r1-degree-scope-gate-fable5-20260910.md
b6c5e8946104e797e2ee61ae6693aaf1ef24f98444eb8c5b7a21383153a668e1  xmodel/f10-all-r-scale-cover-astra-20260910.md
c9fcecfcae96fc5f4bc0b98478fcd18ba46df6e23aa6228487bf904fae61edac  xmodel/f10-all-r-scale-cover-gate-fable5-20260910.md
579199ec08218491bbfb0fc9e909237c47ade1fd2f6fb63b35b1c731baac169a  xmodel/d28-uniform-actual-degree-selection-astra-20260909.md
c5824c135ebb3014fa8f6639854e96b0ece13c143b52f526d4a1bbc4fa40e83c  xmodel/d28-uniform-actual-degree-gate-fable5-20260909.md
9b77ece0a8076d0a8ef498f0a9c152e1de52e85c7ce3cd6b575d5475d0d3337c  xmodel/f10-source-polynomial-cubic-quintic-compression-astra-20260909.md
651dafb531955d76a579d9aace450856132a9733d2a667a2d79222cd7c025bf9  xmodel/f10-source-polynomial-compression-gate-fable5-20260909.md
a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5  xmodel/f10-whole-mate-euler-elimination-astra-20260909.md
77d59f7b54e545d6a05f61ab270739c1498f93eed5d155e40222cecdc96c0a8c  xmodel/f10-euler-complete-presentation-gate-fable5-20260909.md
9f1c44dfd44b48cc3b36d46d79ec407a88addab19e60af2a307f4a17bf82ec3b  xmodel/f10-r2-full-source-transfer-astra-20260910.md
e89e6fb1d107eda73a2a1f334e2bdc4161fb9a78511ff8061cf7fba05ae0b514  xmodel/f10-r2-full-source-gate-fable5-20260910.md
5ef15abfab036b6ad624e17431bbfe5d11214092d8f02c73333049cc5313fbdb  xmodel/f10-r2-fullunit-ready-result-gate-fable5-20260910.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
JC2_DEGREE_REVIEW_PINS
test ! -e xmodel/f10-r2-degree-scope-gate-fable5-20260910.md
test ! -e xmodel/f10-r2-degree-scope-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-r2-degree-scope-gate-fable5-20260910.log
test ! -e box/f10-r2-degree-scope-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-r2-degreescope-term-20260910 --on-calendar='2026-09-10 19:20:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service
systemd-run --user --unit=jc2-r2-degreescope-kill-20260910 --on-calendar='2026-09-10 19:20:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service
systemctl --user is-active jc2-r2-degreescope-term-20260910.timer jc2-r2-degreescope-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1080 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-r2-degree-scope-gate-fable5-20260910 box/f10-r2-degree-scope-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-r2-degree-scope-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1
