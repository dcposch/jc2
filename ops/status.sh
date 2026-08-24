#!/bin/sh
# JC2 campaign live-activity dashboard. Usage: sh ops/status.sh
set -u

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
timeout_cmd=$(command -v timeout 2>/dev/null || command -v gtimeout 2>/dev/null || true)

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
git -C "$repo_root" status --short --branch | sed 's/^/  /'

echo "=== LOCAL LANES ==="
local_lanes=$(pgrep -fl '[c]odex exec|[g]rok (-p|--prompt-file)|[d]irectionb_compress|[f]leet_fc1' 2>/dev/null || true)
if [ -n "$local_lanes" ]; then
  printf '%s\n' "$local_lanes" | sed 's/^/  /'
else
  echo "  (none)"
fi

echo "=== REGISTERED RUNS ==="
run_found=0
for run_file in "$repo_root"/xmodel/*.run; do
  [ -e "$run_file" ] || continue
  run_found=1
  run_tag=$(awk -F= '$1=="tag" {print substr($0,index($0,"=")+1); exit}' "$run_file")
  run_pid=$(awk -F= '$1=="pid" {print $2; exit}' "$run_file")
  run_host=$(awk -F= '$1=="host" {print substr($0,index($0,"=")+1); exit}' "$run_file")
  run_final=$(awk -F= '$1=="final_status" {print $2; exit}' "$run_file")
  if [ -n "$run_final" ]; then
    echo "  $run_tag: $run_final"
  elif [ -d "$repo_root/.lane-locks/$run_tag" ] && \
       [ "$run_host" = "$(hostname)" ] && kill -0 "$run_pid" 2>/dev/null; then
    echo "  $run_tag: RUNNING pid=$run_pid"
  else
    echo "  $run_tag: STALE-RUNNING pid=$run_pid host=$run_host"
  fi
done
[ "$run_found" -eq 1 ] || echo "  (none)"

echo "=== LANE MARKERS (last 5) ==="
if [ -s "$repo_root/pilot-local.log" ]; then
  tail -5 "$repo_root/pilot-local.log" | sed 's/^/  /'
else
  echo "  (none)"
fi

echo "=== FLEET ==="
if command -v ssh >/dev/null 2>&1; then
  remote_status=$(run_bounded 15 ssh -i "$HOME/.ssh/claude-cli.pem" -o BatchMode=yes \
    -o ConnectTimeout=6 ubuntu@54.175.21.169 \
    'm=$(pgrep -cx msolve 2>/dev/null || true); p=$(pgrep -fc "[p]ython[^ ]* .*fleet_fc1" 2>/dev/null || true); [ -n "$m" ] || m=0; [ -n "$p" ] || p=0; printf "msolve=%s fc1=%s" "$m" "$p"' \
    2>/dev/null || true)
  if [ -n "$remote_status" ]; then
    echo "  box01: $remote_status"
  else
    echo "  box01: unreachable"
  fi
else
  echo "  box01: ssh unavailable"
fi

if command -v aws >/dev/null 2>&1; then
  for fleet_spec in "Box02 i-010201a5da47795c4" "Box03 i-0ece0b9a3b4a7512f"; do
    set -- $fleet_spec
    fleet_state=$(run_bounded 20 aws ec2 describe-instances --instance-ids "$2" --profile personal \
      --query 'Reservations[0].Instances[0].State.Name' --output text 2>/dev/null || true)
    [ -n "$fleet_state" ] || fleet_state=unknown
    echo "  $1: $fleet_state"
    if [ "$fleet_state" = running ]; then
      fleet_ip=$(run_bounded 20 aws ec2 describe-instances --instance-ids "$2" --profile personal \
        --query 'Reservations[0].Instances[0].PublicIpAddress' --output text 2>/dev/null || true)
      if [ -n "$fleet_ip" ] && [ "$fleet_ip" != None ]; then
        fleet_jobs=$(run_bounded 15 ssh -i "$HOME/.ssh/claude-cli.pem" -o BatchMode=yes \
          -o ConnectTimeout=6 "ubuntu@$fleet_ip" \
          'pgrep -fl "[m]solve|[p]ython[^ ]* .*jc72108|[p]ython[^ ]* .*cases" || true' \
          2>/dev/null || true)
        if [ -n "$fleet_jobs" ]; then
          printf '%s\n' "$fleet_jobs" | sed 's/^/    job: /'
        else
          echo "    jobs: none detected (verify exact lane directories before stop)"
        fi
      else
        echo "    jobs: public IP unavailable"
      fi
    fi
  done
else
  echo "  Box02/Box03: aws CLI unavailable"
fi

echo "=== NEWEST LIVE STATE ==="
live_state=$(awk '
  /^## .* LIVE STATE$/ { block=""; capture=1; found=1; next }
  capture && /^## / { capture=0 }
  capture { block = block $0 ORS }
  END { if (found) printf "%s", block }
' "$repo_root/notes.md")
if [ -n "$live_state" ]; then
  printf '%s\n' "$live_state" | sed 's/^/  /'
else
  echo "  (none; coordinator must append one)"
fi
