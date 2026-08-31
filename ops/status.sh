#!/bin/sh
# JC2 campaign live-activity dashboard. Usage: sh ops/status.sh
set -u

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
timeout_cmd=$(command -v timeout 2>/dev/null || command -v gtimeout 2>/dev/null || true)
lane_process_matcher=$script_dir/lane_process_pid.awk
if [ -L "$lane_process_matcher" ] || [ ! -f "$lane_process_matcher" ]; then
  echo "status: required regular lane-process matcher missing: $lane_process_matcher" >&2
  exit 2
fi
if ! command -v pgrep >/dev/null 2>&1; then
  echo "status: pgrep is required to avoid reading a live lane receipt" >&2
  exit 2
fi

run_bounded() {
  bound=$1
  shift
  if [ -n "$timeout_cmd" ]; then
    "$timeout_cmd" "$bound" "$@"
  else
    "$@"
  fi
}

echo "=== REPOSITORY ==="
repo_status=$(git -C "$repo_root" status --short --branch -- . ':(exclude)jc2-lean')
printf '%s\n' "$repo_status" | awk '
  NR == 1 { print "  " $0; next }
  {
    code=substr($0,1,2)
    if (code == "??") untracked++
    else {
      tracked++
      if (code ~ /M/) modified++
      if (code ~ /A/) added++
      if (code ~ /D/) deleted++
    }
  }
  END {
    printf "  tracked_changes=%d modified=%d added=%d deleted=%d untracked_entries=%d\n",
           tracked, modified, added, deleted, untracked
  }
'

echo "=== REGISTERED RUNS ==="
run_total=0
run_done=0
run_recovered=0
run_failed=0
run_stale=0
run_active=0
live_lane_processes=$(pgrep -fl '[o]ps/lane[.]sh' 2>/dev/null || true)
echo "  detached supervisors (safe sidecars + launchd only):"
if [ -x "$script_dir/lane_detach.py" ] && command -v python3 >/dev/null 2>&1; then
  if detached_status=$(python3 "$script_dir/lane_detach.py" list 2>&1); then
    printf '%s\n' "$detached_status" | sed 's/^/    /'
  else
    printf '    ERROR: %s\n' "$detached_status"
  fi
else
  echo "    unavailable"
fi
for run_file in "$repo_root"/xmodel/*.run "$repo_root"/xmodel/*.run.v2; do
  [ -e "$run_file" ] || continue
  run_total=$((run_total + 1))
  run_name=${run_file##*/}
  case "$run_name" in
    *.run.v2) run_name_tag=${run_name%.run.v2} ;;
    *.run) run_name_tag=${run_name%.run} ;;
    *) run_name_tag= ;;
  esac
  # A live lane owns this lock.  Do not open its mutable receipt, report, or
  # model log merely to render a dashboard; poll its launchd sidecar or the
  # foreground exec session instead.  Terminal lane.sh cleanup removes the
  # lock before this branch can hide a completed receipt.
  lane_pid=$(printf '%s\n' "$live_lane_processes" | \
    awk -v tag="$run_name_tag" -f "$lane_process_matcher")
  if [ -n "$lane_pid" ]; then
    run_active=$((run_active + 1))
    echo "  $run_name_tag: RUNNING pid=$lane_pid (receipt deliberately unread)"
    continue
  fi
  if [ -n "$run_name_tag" ] && [ -d "$repo_root/.lane-locks/$run_name_tag" ]; then
    echo "  $run_name_tag: stale lock (no exact lane process; terminal receipt may now be read)"
  fi
  run_tag=$(awk -F= '$1=="tag" {print substr($0,index($0,"=")+1); exit}' "$run_file")
  run_final=$(awk -F= '$1=="final_status" {print $2; exit}' "$run_file")
  if [ -n "$run_final" ]; then
    case "$run_final" in
      DONE|done*|exit0) run_done=$((run_done + 1)) ;;
      RECOVERED_REPORT) run_recovered=$((run_recovered + 1)) ;;
      *) run_failed=$((run_failed + 1)) ;;
    esac
  else
    run_stale=$((run_stale + 1))
  fi
done
if [ "$run_total" -eq 0 ]; then
  echo "  (none)"
else
  echo "  summary total=$run_total active=$run_active done=$run_done recovered_reports=$run_recovered failed_or_cancelled=$run_failed stale=$run_stale"
fi

echo "=== LOCAL HEAVY-COMPUTE GUARD ==="
local_singular=$(pgrep -cx Singular 2>/dev/null || true)
local_msolve=$(pgrep -cx msolve 2>/dev/null || true)
[ -n "$local_singular" ] || local_singular=0
[ -n "$local_msolve" ] || local_msolve=0
echo "  campaign-forbidden local executables: Singular=$local_singular msolve=$local_msolve"
if [ "$local_singular" -gt 0 ] || [ "$local_msolve" -gt 0 ]; then
  echo "  WARNING: identify campaign ownership without inspecting excluded workloads; campaign CAS belongs on AWS"
fi
if command -v sysctl >/dev/null 2>&1; then
  swap_occupancy=$(sysctl -n vm.swapusage 2>/dev/null || true)
  [ -z "$swap_occupancy" ] || echo "  swap occupancy (not a pageout-rate verdict): $swap_occupancy"
fi

echo "=== LANE MARKERS (last 5) ==="
if [ -s "$repo_root/pilot-local.log" ]; then
  tail -5 "$repo_root/pilot-local.log" | sed 's/^/  /'
else
  echo "  (none)"
fi

echo "=== FLEET (KNOWN CAMPAIGN INSTANCES ONLY) ==="
if command -v aws >/dev/null 2>&1; then
  fleet_rows=$(run_bounded 20 aws ec2 describe-instances --profile personal \
    --instance-ids \
      i-029d0899cdb7c1ed1 i-010201a5da47795c4 i-0ece0b9a3b4a7512f \
      i-02cb2b4a379ffcc64 i-0f089e64c378f5da3 i-040b7a1c2ed72d4cc \
      i-07eeaf8ba6f0bc419 \
    --query 'Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress]' \
    --output text 2>/dev/null || true)
  running_campaign_vcpu=0
  stopped_campaign_vcpu=0
  unknown_campaign_instances=0
  while read -r fleet_name fleet_id fleet_vcpu; do
    [ -n "$fleet_name" ] || continue
    fleet_row=$(printf '%s\n' "$fleet_rows" | awk -v wanted="$fleet_id" '$1==wanted {print; exit}')
    fleet_state=$(printf '%s\n' "$fleet_row" | awk '{print $2}')
    fleet_ip=$(printf '%s\n' "$fleet_row" | awk '{print $3}')
    [ -n "$fleet_state" ] || fleet_state=unknown
    echo "  $fleet_name ($fleet_id, ${fleet_vcpu}vCPU): $fleet_state"
    if [ "$fleet_state" = running ]; then
      running_campaign_vcpu=$((running_campaign_vcpu + fleet_vcpu))
      if command -v ssh >/dev/null 2>&1 && [ -n "$fleet_ip" ] && [ "$fleet_ip" != None ]; then
        fleet_usage=$(run_bounded 12 ssh -n -i "$HOME/.ssh/claude-cli.pem" -o BatchMode=yes \
          -o ConnectTimeout=5 "ubuntu@$fleet_ip" \
          'ps -u ubuntu -o pid=,%cpu=,rss=,comm=,args= | awk '\''
            $4=="msolve" || $4=="Singular" || $4=="python3" {
              jobs++; cpu+=$2; rss+=$3;
              label=($4=="python3" ? $6 : $5); sub(/^.*\//,"",label);
              if (length(label)>0 && shown<6) { names=names (shown ? "," : "") label; shown++ }
            }
            END { printf "jobs=%d cpu_pct=%.1f rss_gib=%.2f names=%s", jobs, cpu, rss/1048576, (names ? names : "none") }
          '\''' 2>/dev/null || true)
        if [ -n "$fleet_usage" ]; then
          echo "    $fleet_usage"
        else
          echo "    utilization unreachable (run SG auto-update once on SSH timeout)"
        fi
      else
        echo "    utilization unavailable"
      fi
    elif [ "$fleet_state" = stopped ]; then
      stopped_campaign_vcpu=$((stopped_campaign_vcpu + fleet_vcpu))
    else
      unknown_campaign_instances=$((unknown_campaign_instances + 1))
    fi
  done <<'FLEET_INVENTORY'
box01 i-029d0899cdb7c1ed1 64
Box02 i-010201a5da47795c4 128
Box03 i-0ece0b9a3b4a7512f 64
r6a i-02cb2b4a379ffcc64 16
r6b i-0f089e64c378f5da3 16
r6c i-040b7a1c2ed72d4cc 16
r6d i-07eeaf8ba6f0bc419 32
FLEET_INVENTORY
  echo "  campaign inventory: running=${running_campaign_vcpu} stopped-restart=${stopped_campaign_vcpu} all-in=336 vCPU"
  if [ "$unknown_campaign_instances" -eq 0 ]; then
    documented_excluded_vcpu=16
    account_running_vcpu=$((running_campaign_vcpu + documented_excluded_vcpu))
    immediate_headroom=$((512 - account_running_vcpu))
    all_in_headroom=$((512 - 336 - documented_excluded_vcpu))
    echo "  quota: documented running use=${account_running_vcpu}/512 vCPU, immediate headroom=${immediate_headroom}; all campaign boxes running leaves ${all_in_headroom}"
    echo "  the documented 16-vCPU separately owned formalization instance is arithmetic only and remains outside inspection/control"
  else
    echo "  quota headroom not computed: unknown campaign instance states=$unknown_campaign_instances"
  fi
else
  echo "  aws CLI unavailable"
fi

echo "=== NEWEST LIVE STATE ==="
live_state=$(awk '
  /^## .* LIVE STATE([[:space:]]|$)/ { block=""; capture=1; found=1; next }
  capture && /^## / { capture=0 }
  capture { block = block $0 ORS }
  END { if (found) printf "%s", block }
' "$repo_root/notes.md")
if [ -n "$live_state" ]; then
  printf '%s\n' "$live_state" | sed 's/^/  /'
else
  echo "  (none; coordinator must append one)"
fi
