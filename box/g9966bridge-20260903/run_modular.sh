#!/usr/bin/env bash
# Three primes, ≤20 min each, 4 cores.  Face-span std + leftover linear if present.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$HERE/work"
mkdir -p "$WORK"
export OMP_NUM_THREADS=1
PRIMES=(p32003 p104729 p1299709)

run_one() {
  local src="$1"
  local tag="$2"
  local out="$WORK/${tag}.out"
  local err="$WORK/${tag}.err"
  local t0
  t0=$(date +%s)
  if [[ ! -f "$src" ]]; then
    echo "SKIP $tag (no $src)" | tee "$out"
    echo 0 > "$WORK/${tag}.rc"
    return 0
  fi
  timeout 1200 /usr/bin/Singular -q --no-rc "$src" >"$out" 2>"$err"
  local rc=$?
  echo "$rc" > "$WORK/${tag}.rc"
  echo "elapsed $(( $(date +%s) - t0 ))s rc=$rc" >> "$out"
  echo "$tag rc=$rc"
}

# Face jobs first (tiny).  Then leftover if emitted.
for p in "${PRIMES[@]}"; do
  run_one "$WORK/face_${p}.sing" "face_${p}" &
done
wait
for p in "${PRIMES[@]}"; do
  if [[ -f "$WORK/leftover_${p}.sing" ]]; then
    run_one "$WORK/leftover_${p}.sing" "leftover_${p}" &
  fi
done
wait
echo DONE > "$WORK/modular.status"
date -u
