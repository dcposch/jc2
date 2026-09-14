#!/usr/bin/env bash
set -euo pipefail

here=$(cd -- "$(dirname -- "$0")" && pwd)
audit_dir=$(mktemp -d "$here/.summary-audit.XXXXXX")
trap 'rm -rf -- "$audit_dir"' EXIT

fresh_out="$audit_dir/summarize_exact_tail.out"
fresh_err="$audit_dir/summarize_exact_tail.err"
generated=(
  explicit_tail_t2_split_b0.txt
  explicit_tail_t2_split_b1.txt
  explicit_tail_t3_exact.txt
  explicit_tail_t4_exact.txt
  explicit_tail_t5_exact.txt
  explicit_tail_t6_exact.txt
  support_leaders.json
  support_leaders.tsv
  support_leaders_compact.tsv
  t3_q2_axis_control.json
  alpha_formula_checks.json
)
before_manifest="$audit_dir/generated.before.sha256"
after_manifest="$audit_dir/generated.after.sha256"
for name in "${generated[@]}"; do
  sha256sum "$here/$name"
done > "$before_manifest"

start_ns=$(date +%s%N)
set +e
timeout 1200 python3 -u "$here/summarize_exact_tail.py" > "$fresh_out" 2> "$fresh_err"
exit_code=$?
set -e
end_ns=$(date +%s%N)
wall_ms=$(( (end_ns - start_ns) / 1000000 ))

stdout_match=false
stderr_match=false
stderr_empty=false
cmp -s "$fresh_out" "$here/summarize_exact_tail.out" && stdout_match=true
cmp -s "$fresh_err" "$here/summarize_exact_tail.err" && stderr_match=true
test ! -s "$fresh_err" && stderr_empty=true
script_hash=$(sha256sum "$here/summarize_exact_tail.py" | cut -d' ' -f1)
stdout_hash=$(sha256sum "$fresh_out" | cut -d' ' -f1)
leaders_hash=$(sha256sum "$here/support_leaders.tsv" | cut -d' ' -f1)
for name in "${generated[@]}"; do
  sha256sum "$here/$name"
done > "$after_manifest"
generated_artifacts_match=false
cmp -s "$before_manifest" "$after_manifest" && generated_artifacts_match=true
generated_manifest_hash=$(sha256sum "$after_manifest" | cut -d' ' -f1)

{
  printf 'exit\twall_ms\tstdout_match\tstderr_match\tstderr_empty\tgenerated_artifacts_match\tscript_sha256\tstdout_sha256\tleaders_tsv_sha256\tgenerated_manifest_sha256\n'
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$exit_code" "$wall_ms" "$stdout_match" "$stderr_match" "$stderr_empty" \
    "$generated_artifacts_match" "$script_hash" "$stdout_hash" "$leaders_hash" \
    "$generated_manifest_hash"
} > "$audit_dir/summary_audit.tsv"
mv -- "$audit_dir/summary_audit.tsv" "$here/summary_audit.tsv"
cat "$here/summary_audit.tsv"

if test "$exit_code" -ne 0 \
  || test "$stdout_match" != true \
  || test "$stderr_match" != true \
  || test "$stderr_empty" != true \
  || test "$generated_artifacts_match" != true
then
  exit 1
fi
