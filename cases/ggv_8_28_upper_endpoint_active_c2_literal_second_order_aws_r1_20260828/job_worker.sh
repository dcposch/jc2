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
if ! python3 "$source_dir/runner/preflight.py" \
  --run-dir "$job_dir" --job-tag "$(basename "$job_dir")" \
  --output "$records_dir/PREFLIGHT.json" \
  >"$records_dir/preflight.stdout" 2>"$records_dir/preflight.stderr"; then
  printf '%s\n' NO_VERDICT_PREFLIGHT_OR_ACTIVE_CONFLICT >"$output_dir/TERMINAL"
  exit 31
fi
printf '%s\n' AWS_PREFLIGHT_PASS >"$records_dir/PREFLIGHT_PASS"

cd "$source_dir"
if ! sha256sum -c runner/INPUT_PINS.sha256 \
  >"$records_dir/INPUT_PINS_CHECK.stdout" \
  2>"$records_dir/INPUT_PINS_CHECK.stderr"; then
  printf '%s\n' NO_VERDICT_SOURCE_DRIFT >"$output_dir/TERMINAL"
  exit 32
fi

probe_path="$source_dir/cases/ggv_8_28_upper_endpoint_active_c2_literal_second_order_20260828/probe_second_order_relaxed.py"
certificate_path="$output_dir/SECOND_ORDER_CERTIFICATE.json"
printf '%s\n' SECOND_ORDER_RELAXED_EXACT_Q >"$output_dir/CURRENT_STAGE"

set +e
/usr/bin/time -v -o "$output_dir/probe.time" \
  timeout --foreground --signal=TERM --kill-after=30s 7200s \
  prlimit --as=137438953472 --fsize=8589934592 \
  taskset --cpu-list 1 \
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
python3 - "$certificate_path" "$output_dir/POSTCHECK.json" <<'PY'
import json
import sys
from pathlib import Path

certificate_path, postcheck_path = map(Path, sys.argv[1:])
data = json.loads(certificate_path.read_text())
base = data.get("base_tangent", {})
second = data.get("second_order", {})
exact = data.get("exact_relaxed", {})
modular = data.get("modular", [])
pins = data.get("pins", {})
shape_pass = (
    base == {"rows": 510, "columns": 308, "rank": 291, "kernel_dimension": 17}
    and second.get("correction_columns") == 308
    and second.get("symmetric_monomial_columns") == 153
    and second.get("augmented_columns") == 461
    and second.get("prefix_curvature_included") is True
    and second.get("veronese_rank_one_constraints_imposed") is False
)
pin_pass = (
    pins.get("tangent_source_sha256")
      == "ddcd7b5d9cc5dd37e56412f606eb4b0fb37bc976280b224ac9dcf91a04be20a1"
    and pins.get("tangent_certificate_sha256")
      == "d21fc8538e908f9a1bc6705fd9e5cf99a2c3d0be3f3b8a82318906ef817c0a8b"
)
expected_primes = [65521, 65519, 65497]
modular_reject = (
    [row.get("modulus") for row in modular] == expected_primes
    and all(row.get("consistent") is False for row in modular)
)
modular_accept = (
    [row.get("modulus") for row in modular] == expected_primes
    and all(row.get("consistent") is True for row in modular)
)
dual = exact.get("dual", [])
exact_reject = (
    exact.get("consistent") is False
    and exact.get("column_count") == 461
    and exact.get("dual_support") == len(dual)
    and len(dual) > 0
)
exact_accept = exact.get("consistent") is True and exact.get("column_count") == 461
if shape_pass and pin_pass and modular_reject and exact_reject:
    classification = "SECOND_ORDER_RELAXED_INCONSISTENT_AT_THIS_POINT"
    code = 0
elif shape_pass and pin_pass and modular_accept and exact_accept:
    classification = "SECOND_ORDER_RELAXED_CONSISTENT_NO_VERDICT"
    code = 10
else:
    classification = "NO_VERDICT_MIXED_OR_POSTCHECK"
    code = 11
result = {
    "classification": classification,
    "shape_pass": shape_pass,
    "pin_pass": pin_pass,
    "modular_reject": modular_reject,
    "modular_accept": modular_accept,
    "exact_reject": exact_reject,
    "exact_accept": exact_accept,
    "dual_support": len(dual),
    "internal_dual_replay": "producer exact_dual_certificate assertions completed before output write",
    "zero_target_control": "v=w=0 solves the zero-target system",
}
postcheck_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
raise SystemExit(code)
PY
postcheck_rc=$?
set -e
printf '%s\n' "$postcheck_rc" >"$output_dir/POSTCHECK_RC"

case "$postcheck_rc" in
  0) printf '%s\n' SECOND_ORDER_RELAXED_INCONSISTENT_AT_THIS_POINT >"$output_dir/TERMINAL" ;;
  10) printf '%s\n' SECOND_ORDER_RELAXED_CONSISTENT_NO_VERDICT >"$output_dir/TERMINAL" ;;
  *) printf '%s\n' NO_VERDICT_MIXED_OR_POSTCHECK >"$output_dir/TERMINAL" ;;
esac

