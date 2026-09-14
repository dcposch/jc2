set -euo pipefail
cd '/home/ubuntu/jc2-f10-integer-wire-actual-20260910'
test "$(cat /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(cat /proc/sys/kernel/random/boot_id)" = '745dc9ea-182a-446a-8821-042f8145f284'
test "$(sha256sum dispatch.registration.json | cut -d ' ' -f 1)" = '327b136f9761b15b363f1f34266d20e17ade9b60a97ab99dc360a18e96c9d639'
test "$(sha256sum fixed.sha256 | cut -d ' ' -f 1)" = 'd938ea600e21ab6eb2af62f3eb81dbf76e730f64f30aa80724180a5d735ccc95'
sha256sum -c fixed.sha256 --quiet
for jc2_file in solver.py checker.py evidence.py algebra.py execution_gate.py run_capped.py probe.py admissibility.md frontier.json dispatch_batch.py semantic_controls.py univariate.json univariate.full.receipt.json ROOT-UNIVARIATE-ACCEPTANCE.json dispatch.registration.json; do
 test -f "$jc2_file"
 test ! -L "$jc2_file"
 chmod 444 "$jc2_file"
done
test "$(systemctl show 'jc2-f10-integer-wire-actual-20260910.service' -p LoadState --value)" = not-found
test ! -e batch.PASS.json
test ! -e batch.STOP.json
test ! -e candidate.json
test ! -e dispatch.stdout
test ! -e dispatch.stderr
jc2_remaining=$(( $(date -u -d '2026-09-10 07:38:00 UTC' +%s) - $(date -u +%s) ))
test "$jc2_remaining" -ge 1215
date -u '+PRELAUNCH_177_FIXED_MATCH %Y-%m-%dT%H:%M:%S.%NZ'
sudo systemd-run --no-block --unit='jc2-f10-integer-wire-actual-20260910.service' --property=User=ubuntu --property=WorkingDirectory='/home/ubuntu/jc2-f10-integer-wire-actual-20260910' --property=RuntimeMaxSec=1250 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=3221225472 --property=MemorySwapMax=0 --property=TasksMax=64 --property=LimitFSIZE=16777216 --property=CPUAccounting=yes --property=MemoryAccounting=yes --property=StandardOutput=append:'/home/ubuntu/jc2-f10-integer-wire-actual-20260910/dispatch.stdout' --property=StandardError=append:'/home/ubuntu/jc2-f10-integer-wire-actual-20260910/dispatch.stderr' --setenv=LD_PRELOAD= --setenv=LD_LIBRARY_PATH= --setenv=OMP_NUM_THREADS=1 --setenv=OPENBLAS_NUM_THREADS=1 /usr/bin/python3 -I -B '/home/ubuntu/jc2-f10-integer-wire-actual-20260910/dispatch_batch.py' &
jc2_launch_pid=$!
declare -A jc2_seen
jc2_end=$((SECONDS+40))
while test "$SECONDS" -lt "$jc2_end"; do
 if test -r '/sys/fs/cgroup/system.slice/jc2-f10-integer-wire-actual-20260910.service/cgroup.procs'; then
  jc2_pids=()
  mapfile -t jc2_pids < '/sys/fs/cgroup/system.slice/jc2-f10-integer-wire-actual-20260910.service/cgroup.procs' || true
  for jc2_pid in "${jc2_pids[@]}"; do
   test -r "/proc/$jc2_pid/cmdline" || continue
   jc2_argv=$(tr '\000' ' ' < "/proc/$jc2_pid/cmdline" 2>/dev/null) || continue
   case "$jc2_argv" in *'/home/ubuntu/jc2-f10-integer-wire-actual-20260910'*)
    if test "${jc2_seen[$jc2_pid]-}" != "$jc2_argv"; then
     jc2_seen[$jc2_pid]="$jc2_argv"
     date -u '+PROCESS %Y-%m-%dT%H:%M:%S.%NZ'
     echo "PID $jc2_pid ARGV $jc2_argv"
     ps -p "$jc2_pid" -o pid=,ppid=,pgid=,sid=,stat=,rss= || true
     cat "/proc/$jc2_pid/stat" 2>/dev/null || true
     readlink "/proc/$jc2_pid/ns/pid" || true
    fi;;
   esac
  done
 fi
 sleep 0.005
done
wait "$jc2_launch_pid"
sudo systemctl show 'jc2-f10-integer-wire-actual-20260910.service' --property=MainPID --property=InvocationID --property=ControlGroup --property=ActiveState --property=SubState --property=ExecMainStatus --property=CPUUsageNSec --property=MemoryPeak
date -u '+STATUS_CHECK %Y-%m-%dT%H:%M:%S.%NZ'
