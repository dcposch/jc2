#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: run_aws.sh OUTDIR EXPECTED_HOST REGISTERED_TAG INPUT" >&2
  exit 2
fi
outdir=$1
expected_host=$2
registered_tag=$3
input=$4
case_dir=$(cd -- "$(dirname -- "$0")" && pwd -P)

[[ $(uname -s) == Linux ]] || { echo REFUSE_NON_LINUX >&2; exit 90; }
[[ $(hostname) == "$expected_host" ]] || { echo REFUSE_HOSTNAME >&2; exit 91; }
[[ ${JC2_AWS_TAG:-} == "$registered_tag" ]] || { echo REFUSE_AWS_TAG >&2; exit 92; }
vendor=$(cat /sys/devices/virtual/dmi/id/sys_vendor 2>/dev/null || true)
[[ $vendor == *Amazon* ]] || { echo REFUSE_NON_AWS_PLATFORM >&2; exit 93; }

cd "$case_dir"
sha256sum -c SOURCE.sha256
mkdir -p "$outdir"
date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/start_utc"
hostname > "$outdir/hostname"
printf '%s\n' "$registered_tag" > "$outdir/registered_tag"
python3 --version > "$outdir/python.version" 2>&1
Singular --version > "$outdir/singular.version" 2>&1

/usr/bin/time -v timeout 300 python3 emit_split.py --input "$input" \
  --output "$outdir/split.sing" > "$outdir/emitter.stdout" \
  2> "$outdir/emitter.stderr"
grep -q '^PASS_EMIT 7 8 ' "$outdir/emitter.stdout"

/usr/bin/time -v timeout 7200 Singular "$outdir/split.sing" \
  > "$outdir/singular.stdout" 2> "$outdir/singular.stderr"
grep -q '^ORIGINAL_REMAINDERS_ZERO$' "$outdir/singular.stdout"
grep -q '^PASS$' "$outdir/singular.stdout"
printf 'PASS squarefree split-slimgb\n' > "$outdir/status.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/end_utc"
find "$outdir" -maxdepth 1 -type f ! -name OUTPUT.sha256 -print0 \
  | LC_ALL=C sort -z | xargs -0 sha256sum > "$outdir/OUTPUT.sha256"
cat "$outdir/status.txt"

