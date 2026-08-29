#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
source_dir="$job_dir/source"
output_dir="$job_dir/output"
records_dir="$job_dir/records"

registration_deadline=$((SECONDS + 30))
while [[ ! -f "$records_dir/REGISTERED" ]]; do
  if (( SECONDS >= registration_deadline )); then
    printf '%s\n' NO_VERDICT_REGISTRATION_TIMEOUT >"$output_dir/TERMINAL"
    exit 30
  fi
  sleep 0.05
done

printf '%s\n' PREFLIGHT >"$output_dir/CURRENT_STAGE"

instance_id=$(tr -d '\n' </sys/class/dmi/id/board_asset_tag)
instance_type=$(tr -d '\n' </sys/class/dmi/id/product_name)
vendor=$(tr -d '\n' </sys/class/dmi/id/sys_vendor)
mem_available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
swap_total_kib=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free_kib=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
disk_available_bytes=$(df -PB1 "$job_dir" | awk 'NR==2 {print $4}')

{
  date -u +UTC=%Y-%m-%dT%H:%M:%SZ
  printf 'vendor=%s\n' "$vendor"
  printf 'instance_id=%s\n' "$instance_id"
  printf 'instance_type=%s\n' "$instance_type"
  printf 'instance_tags=not_exposed_by_IMDS; host authorization inherited from frozen campaign audit\n'
  printf 'job_tag=%s\n' "$(basename "$job_dir")"
  printf 'mem_available_kib=%s\n' "$mem_available_kib"
  printf 'swap_total_kib=%s\n' "$swap_total_kib"
  printf 'swap_free_kib=%s\n' "$swap_free_kib"
  printf 'disk_available_bytes=%s\n' "$disk_available_bytes"
  uname -a
  ps -eo pid,ppid,pgid,sid,ni,etimes,time,%cpu,rss,stat,comm,args
} >"$records_dir/PREFLIGHT.txt"

preflight_pass=1
[[ "$(uname -s)" == Linux ]] || preflight_pass=0
[[ "$vendor" == "Amazon EC2" ]] || preflight_pass=0
[[ "$instance_id" == "i-040b7a1c2ed72d4cc" ]] || preflight_pass=0
[[ "$instance_type" == "r6i.16xlarge" ]] || preflight_pass=0
[[ "${AWS_RUN_TAG:-}" == "$(basename "$job_dir")" ]] || preflight_pass=0
(( mem_available_kib >= 450 * 1024 * 1024 )) || preflight_pass=0
(( swap_total_kib == 0 && swap_free_kib == 0 )) || preflight_pass=0
(( disk_available_bytes >= 100 * 1024 * 1024 * 1024 )) || preflight_pass=0

if [[ "$preflight_pass" -ne 1 ]]; then
  printf '%s\n' NO_VERDICT_PREFLIGHT >"$output_dir/TERMINAL"
  exit 31
fi
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$source_dir"
sha256sum -c runner/INPUT_PINS.sha256 >"$records_dir/INPUT_PINS_CHECK.stdout" \
  2>"$records_dir/INPUT_PINS_CHECK.stderr"

probe_path="$source_dir/cases/ggv_8_28_upper_endpoint_active_c2_literal_tangent_20260828/probe_tangent.py"
certificate_path="$output_dir/TANGENT_CERTIFICATE.json"
printf '%s\n' EXACT_Q_ELIMINATION >"$output_dir/CURRENT_STAGE"

set +e
/usr/bin/time -v -o "$output_dir/probe.time" \
  timeout --foreground --signal=TERM --kill-after=20s 3600s \
  prlimit --as=68719476736 --fsize=8589934592 \
  nice -n 10 taskset --cpu-list 1 \
  env PYTHONDONTWRITEBYTECODE=1 python3 -B "$probe_path" \
  --exact-output "$certificate_path" \
  >"$output_dir/probe.stdout" 2>"$output_dir/probe.stderr"
probe_rc=$?
set -e
printf '%s\n' "$probe_rc" >"$output_dir/PROBE_RC"

if [[ "$probe_rc" -eq 124 || "$probe_rc" -eq 137 ]]; then
  printf '%s\n' NO_VERDICT_TIMEOUT >"$output_dir/TERMINAL"
  exit "$probe_rc"
fi
if [[ "$probe_rc" -ne 0 || ! -s "$certificate_path" ]]; then
  printf '%s\n' NO_VERDICT_EXECUTION >"$output_dir/TERMINAL"
  exit "$probe_rc"
fi

set +e
python3 - "$certificate_path" "$output_dir/probe.stdout" "$output_dir/POSTCHECK.json" <<'PY'
import ast
import json
import sys
from pathlib import Path

certificate_path, stdout_path, postcheck_path = map(Path, sys.argv[1:])
certificate = json.loads(certificate_path.read_text())
matrix = certificate.get("matrix", {})
source_index = certificate.get("contradiction_source_row")
labels = matrix.get("ordered_row_labels", [])
source_label = labels[source_index] if isinstance(source_index, int) and source_index < len(labels) else None

modular = []
for line in stdout_path.read_text().splitlines():
    if line.startswith("{'modulus':"):
        modular.append(ast.literal_eval(line))

expected_primes = [65521, 65519, 65497]
modular_pass = (
    [row.get("modulus") for row in modular] == expected_primes
    and all(row.get("rank") == 291 for row in modular)
    and all(row.get("consistent") is False for row in modular)
    and all(row.get("contradiction_label") == [22, 0] for row in modular)
)
exact_obstruction = (
    certificate.get("consistent") is False
    and certificate.get("rank") == 291
    and certificate.get("column_count") == 308
    and matrix.get("columns") == 308
    and matrix.get("coefficient_rows") == 510
    and source_label == [22, 0]
    and certificate.get("dual_support") == len(certificate.get("dual", []))
    and certificate.get("dual_support", 0) > 0
    and certificate.get("pins", {}).get("tail_checker_sha256")
       == "f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45"
)
exact_survivor = certificate.get("consistent") is True
result = {
    "exact_obstruction": exact_obstruction,
    "exact_survivor": exact_survivor,
    "source_label": source_label,
    "modular_pass": modular_pass,
    "modular": modular,
    "internal_dual_replay": "producer assertions completed before certificate write",
    "zero_target_control": "zero tangent is a literal solution of the homogeneous system",
}
postcheck_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
if exact_obstruction and modular_pass:
    raise SystemExit(0)
if exact_survivor:
    raise SystemExit(10)
raise SystemExit(11)
PY
postcheck_rc=$?
set -e
printf '%s\n' "$postcheck_rc" >"$output_dir/POSTCHECK_RC"

case "$postcheck_rc" in
  0) printf '%s\n' TANGENT-OBSTRUCTED-AT-THIS-POINT >"$output_dir/TERMINAL" ;;
  10) printf '%s\n' TANGENT-SURVIVOR-AT-THIS-POINT >"$output_dir/TERMINAL" ;;
  *) printf '%s\n' NO-VERDICT-POSTCHECK >"$output_dir/TERMINAL" ;;
esac
