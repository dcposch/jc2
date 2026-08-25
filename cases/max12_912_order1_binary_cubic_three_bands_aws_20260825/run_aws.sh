#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  echo "usage: run_aws.sh STRATUM ALGORITHM OUTDIR EXPECTED_HOST REGISTERED_TAG" >&2
  exit 2
fi

stratum=$1
algorithm=$2
outdir=$3
expected_host=$4
registered_tag=$5
case_dir=$(cd -- "$(dirname -- "$0")" && pwd -P)

[[ $(uname -s) == Linux ]] || { echo "REFUSE_NON_LINUX" >&2; exit 90; }
[[ $(hostname) == "$expected_host" ]] || { echo "REFUSE_HOSTNAME" >&2; exit 91; }
[[ ${JC2_AWS_TAG:-} == "$registered_tag" ]] || { echo "REFUSE_AWS_TAG" >&2; exit 92; }
vendor=$(cat /sys/devices/virtual/dmi/id/sys_vendor 2>/dev/null || true)
[[ $vendor == *Amazon* ]] || { echo "REFUSE_NON_AWS_PLATFORM" >&2; exit 93; }
[[ $stratum =~ ^(triple|double|squarefree)$ ]] || exit 2
[[ $algorithm =~ ^(std|slimgb)$ ]] || exit 2

cd "$case_dir"
sha256sum -c SOURCE.sha256
mkdir -p "$outdir"
date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/start_utc"
hostname > "$outdir/hostname"
printf '%s\n' "$registered_tag" > "$outdir/registered_tag"
uname -a > "$outdir/uname"
python3 --version > "$outdir/python.version" 2>&1
Singular --version > "$outdir/singular.version" 2>&1

/usr/bin/time -v timeout 7200 python3 compile_three_bands.py \
  --stratum "$stratum" --algorithm "$algorithm" --outdir "$outdir" \
  > "$outdir/compiler.stdout" 2> "$outdir/compiler.stderr"
grep -q '"PASS": true' "$outdir/compiler.stdout"

/usr/bin/time -v timeout 7200 Singular "$outdir/three_bands.sing" \
  > "$outdir/singular.stdout" 2> "$outdir/singular.stderr"
grep -q '^PASS$' "$outdir/singular.stdout"

printf 'PASS %s %s\n' "$stratum" "$algorithm" > "$outdir/status.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$outdir/end_utc"
find "$outdir" -maxdepth 1 -type f ! -name OUTPUT.sha256 -print0 \
  | LC_ALL=C sort -z | xargs -0 sha256sum > "$outdir/OUTPUT.sha256"
cat "$outdir/status.txt"

