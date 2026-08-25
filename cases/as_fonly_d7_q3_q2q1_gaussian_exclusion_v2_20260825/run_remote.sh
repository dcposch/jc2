#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${MEMORY_KIB:=33554432}"
case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/certify_all_v2.py" \
  "$case_dir/verify_certificates_v2.py" "$0" "$MODEL_OUTPUT" \
  > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
  PARENT_OUTPUT_JSON="$JOB_DIR/q3_parent.json" \
  OUTPUT_JSON="$JOB_DIR/certificates.json" \
  python3 "$case_dir/certify_all_v2.py" \
  > "$JOB_DIR/producer.stdout" 2> "$JOB_DIR/producer.stderr"
grep -q '^PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-V2$' "$JOB_DIR/producer.stdout"
env CERTIFICATE_JSON="$JOB_DIR/certificates.json" \
  python3 "$case_dir/verify_certificates_v2.py" \
  > "$JOB_DIR/verifier.stdout" 2> "$JOB_DIR/verifier.stderr"
grep -q '^PASS-AS-Q3-Q2Q1-INDEPENDENT-CERTIFICATE-VERIFY-V2$' \
  "$JOB_DIR/verifier.stdout"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
echo PASS-AS-Q3-Q2Q1-GAUSSIAN-PRODUCER-AND-VERIFY-V2
