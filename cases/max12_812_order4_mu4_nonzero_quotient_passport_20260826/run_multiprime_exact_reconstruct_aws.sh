#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only multiprime client refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only multiprime client refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 4 ]]; then
  echo "usage: run_multiprime_exact_reconstruct_aws.sh AWS_ROOT AWS_RUN TAG SOURCE_INPUT" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
source_input=$4
case_dir=$aws_root/cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826
prime_dir=$aws_run/primes
compiled_dir=$aws_run/compiled
mkdir -p "$prime_dir" "$compiled_dir"
export JC2_REGISTERED_AWS_LANE=$lane_tag
ulimit -v 134217728

primes=(
  32003 32009 32027 32029 32051 32057 32059 32063
  32069 32077 32083 32089 32099 32117 32119 32141
  32143 32159 32173 32183 32189 32191 32203 32213
  32233 32237 32251 32257 32261 32297 32303 32309
)

sha256sum "$source_input" > "$aws_run/source_input.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
python3 --version > "$aws_run/PYTHON.version" 2>&1

for prime in "${primes[@]}"; do
  input=$compiled_dir/plane_prime_${prime}.sing
  python3 "$case_dir/compile_plane_prime_v2.py" "$source_input" "$input" "$prime" \
    > "$compiled_dir/prime_${prime}.compiler.stdout" \
    2> "$compiled_dir/prime_${prime}.compiler.stderr"
  printf 'prime=%s start_utc=%s\n' "$prime" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    >> "$aws_run/prime_lanes.log"
  set +e
  timeout 300 Singular -q "$input" \
    > "$prime_dir/prime_${prime}.stdout" \
    2> "$prime_dir/prime_${prime}.stderr"
  rc=$?
  set -e
  printf 'prime=%s rc=%s end_utc=%s\n' "$prime" "$rc" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    >> "$aws_run/prime_lanes.log"
  if [[ $rc -ne 0 ]]; then
    echo "prime $prime failed rc=$rc" >&2
    exit "$rc"
  fi
  grep -qx 'PRIME_COMPLETE=PASS' "$prime_dir/prime_${prime}.stdout"
done

sha256sum "$compiled_dir"/plane_prime_*.sing > "$aws_run/compiled_prime_inputs.sha256"
sha256sum "$prime_dir"/prime_*.stdout > "$aws_run/prime_stdout.sha256"
python3 "$case_dir/reconstruct_plane_v2.py" "$prime_dir" "$aws_run/candidate.json" \
  > "$aws_run/reconstruction.stdout" 2> "$aws_run/reconstruction.stderr"
grep -qx 'MULTIPRIME_RECONSTRUCTION=PASS_CANDIDATE_ONLY' "$aws_run/reconstruction.stdout"

python3 "$case_dir/compile_exact_candidate_verify_v2.py" \
  "$source_input" "$aws_run/candidate.json" "$compiled_dir/exact_candidate_verify_v2.sing" \
  > "$compiled_dir/exact_candidate.compiler.stdout" \
  2> "$compiled_dir/exact_candidate.compiler.stderr"
sha256sum "$aws_run/candidate.json" "$compiled_dir/exact_candidate_verify_v2.sing" \
  > "$aws_run/candidate_inputs.sha256"

timeout 3600 Singular -q "$compiled_dir/exact_candidate_verify_v2.sing" \
  > "$aws_run/exact_candidate.stdout" 2> "$aws_run/exact_candidate.stderr"
grep -qx 'EXACT_CANDIDATE=PASS_RELATION_AND_GEOMETRY' "$aws_run/exact_candidate.stdout"

cat "$aws_run/reconstruction.stdout"
grep -E '^(EXACT_|TAIL_TO_COEF|COEF_TO_TAIL|LEAD_RELATION|SOURCE_EQUIVALENCE)' \
  "$aws_run/exact_candidate.stdout"
echo "MULTIPRIME_EXACT_RECONSTRUCTION=PASS"
