set -eu
cd /home/ubuntu/jc2
sha256sum -c <<'JC2_CONTACT_GRAM_REVIEW_PINS'
449e27527e12e7af44669b2f57c7b4ae925861b1cc3f805222d2f3e262491484  xmodel/f10-contact-gram-code-astra-20260910.md
afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee  box/f10-contact-gram-code-astra-20260910/producer.py
ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06  box/f10-contact-gram-code-astra-20260910/checker.py
96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141  box/f10-contact-gram-startup-fix-astra-20260910/authority.py
5ddae470316b37c90506a05c1d70e581e22aec532e9509950c4a61e4f9b3c594  box/f10-contact-gram-code-astra-20260910/CONTRACT.md
29e8fa8f0c6a5d07694d3f5e3fc66a5714a4bf2ce990a44a23a8e95cdee9db7e  box/f10-contact-gram-code-astra-20260910/VALIDATION.md
1ea0cf0197bc8a0bf0fa29c3a33d079fc1f2f013f65fb3ce41e8878e2e997575  box/f10-contact-gram-code-astra-20260910/DISABLED-REGISTRATION.json
c3cf516950680e9af110c7e95b35ba257f5e742c9529354f9f7ec6c9105cefd6  box/f10-contact-gram-code-astra-20260910/READ-SCOPE.md
f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2  xmodel/f10-contact-real-window-astra-20260910.md
ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068  xmodel/f10-contact-quartic-gram-gate-fable5-20260910.md
96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13  xmodel/f10-contact-symmetric-remainder-astra-20260910.md
d3b8c09234d50b51b9dbcfaa7a9f341f34263540bd35e798c9f794137640c932  xmodel/f10-middle-real-code-gate-fable5-20260910.md
cab1bc10ca61306037e8ed9c1c4d5d01227413c6b50d0b535f6eb194032d2cf3  xmodel/f10-contact-gram-startup-fix-astra-20260910.md
08d75a6199cc414ba7c02be9cd3f3bcf1cf89a5472623d0c557777744c044c59  box/f10-contact-gram-startup-fix-astra-20260910/CONTRACT-DELTA.md
34070f15592c99d2c2fef012c5675f802469846899f26fe79018fb80cbe1b699  ops/adapters/claude.sh
0726b8428208ba3e8b0ca2ae7afd4bcf329b28c24a2b04caf977823f5d59f396  ops/lane.sh
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
222e6de4076e1a3169ff27bd0f6b9deff8c2389aa2ff9dd44b8b4ec90c2ea776  ops/seal.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
JC2_CONTACT_GRAM_REVIEW_PINS
test ! -e xmodel/f10-contact-gram-code-gate-fable5-20260910.md
test ! -e xmodel/f10-contact-gram-code-gate-fable5-20260910.run.v2
test ! -e xmodel/f10-contact-gram-code-gate-fable5-20260910.log
test ! -e box/f10-contact-gram-code-gate-fable5-20260910
test -x /home/ubuntu/.nvm/versions/node/v22.23.2/bin/claude
test -x /home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch
systemd-run --user --unit=jc2-contact-gramcode-term-20260910 --on-calendar='2026-09-10 20:36:00 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=TERM jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service
systemd-run --user --unit=jc2-contact-gramcode-kill-20260910 --on-calendar='2026-09-10 20:36:05 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl --user kill --kill-whom=all --signal=KILL jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service
systemctl --user is-active jc2-contact-gramcode-term-20260910.timer jc2-contact-gramcode-kill-20260910.timer
date -u '+ORIGINAL_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --user --unit=jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service --property=WorkingDirectory=/home/ubuntu/jc2 --property=RuntimeMaxSec=1200 --property=TimeoutStopSec=5 --property=KillMode=control-group --setenv=PATH=/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7:/home/ubuntu/.nvm/versions/node/v22.23.2/bin:/usr/local/bin:/usr/bin:/bin /bin/sh ops/lane.sh claude f10-contact-gram-code-gate-fable5-20260910 box/f10-contact-gram-code-gate-prep-20260910/root-invite.prompt.md
for jc2_attempt in $(seq 1 100); do
 jc2_main=$(systemctl --user show jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service --property=MainPID --value)
 if test "$jc2_main" != 0; then
  jc2_bwrap=$(pgrep -P "$jc2_main" -x bwrap || true)
  if test -n "$jc2_bwrap"; then
   jc2_model=$(pgrep -P "$jc2_bwrap" -x claude || true)
   if test -n "$jc2_model"; then
    systemctl --user show jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service --property=MainPID --property=InvocationID --property=ActiveState --property=ControlGroup --property=ExecMainStartTimestamp
    ps -p "$jc2_main,$jc2_bwrap,$jc2_model" -o pid=,ppid=,pgid=,lstart=,args=
    date -u '+SAME_CALL_MODEL_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
    exit 0
   fi
  fi
 fi
 sleep 0.1
done
systemctl --user show jc2-lane-f10-contact-gram-code-gate-fable5-20260910.service --property=MainPID --property=ActiveState --property=ExecMainStatus
exit 1

