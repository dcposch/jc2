#!/usr/bin/env bash
set -uo pipefail

readonly BASE=/home/ubuntu/jc2/box/k8-b11-q1-20260905/certificate-audit/full-lift
readonly CUSTODY="$BASE/custody"
readonly INPUT=/home/ubuntu/jc2/box/k8-b11-q1-20260905/input/K8_B11_Q1_p0.ms
readonly CONVERTER=/home/ubuntu/jc2/box/k7-strata-gate-20260905/cert-audit/make_singular.py
readonly SCRIPT="$BASE/K8_B11_Q1_p0_lift.sing"
readonly SINGULAR=/usr/bin/Singular
readonly EXPECTED_INPUT_SHA=66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb
readonly EXPECTED_CONVERTER_SHA=e3581ed645d3f32cd63e1162675500388028611fd000b82c517291e758f58470
readonly EXPECTED_SCRIPT_SHA=922ae8e915ca195c3eb5987f0ebb90e558fb542695f9601cb627f84cf10e565a
readonly FILE_BLOCK_LIMIT=2097152
readonly VM_KIB_LIMIT=104857600
readonly WALL_SECONDS=2700
readonly SHM_LIMIT_BYTES=2147483648

mkdir -p "$CUSTODY"

input_sha=$(sha256sum "$INPUT" | awk '{print $1}')
converter_sha=$(sha256sum "$CONVERTER" | awk '{print $1}')
script_sha=$(sha256sum "$SCRIPT" | awk '{print $1}')
if [[ "$input_sha" != "$EXPECTED_INPUT_SHA" ||
      "$converter_sha" != "$EXPECTED_CONVERTER_SHA" ||
      "$script_sha" != "$EXPECTED_SCRIPT_SHA" ]]; then
  printf 'preflight hash mismatch\n' >&2
  exit 86
fi

shm_dir=$(mktemp -d /dev/shm/k8-b11-q1-full-lift.XXXXXX)
printf '%s\n' "$shm_dir" >"$CUSTODY/shm-dir.txt"

singular_sha=$(sha256sum "$SINGULAR" | awk '{print $1}')
start_ns=$(date +%s%N)
start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'START_NS=%s\n' "$start_ns"
  printf 'START_UTC=%s\n' "$start_utc"
  printf 'HOST=%s\n' "$(hostname -f 2>/dev/null || hostname)"
  printf 'INPUT=%s\n' "$INPUT"
  printf 'INPUT_SHA256=%s\n' "$input_sha"
  printf 'INPUT_BYTES=%s\n' "$(stat -c %s "$INPUT")"
  printf 'CONVERTER=%s\n' "$CONVERTER"
  printf 'CONVERTER_SHA256=%s\n' "$converter_sha"
  printf 'SCRIPT=%s\n' "$SCRIPT"
  printf 'SCRIPT_SHA256=%s\n' "$script_sha"
  printf 'SINGULAR=%s\n' "$SINGULAR"
  printf 'SINGULAR_SHA256=%s\n' "$singular_sha"
  printf 'SINGULAR_VERSION_BEGIN\n'
  "$SINGULAR" --version
  printf 'SINGULAR_VERSION_END\n'
  printf 'ULIMIT_V_KIB=%s\n' "$VM_KIB_LIMIT"
  printf 'ULIMIT_F_1K_BLOCKS=%s\n' "$FILE_BLOCK_LIMIT"
  printf 'TIMEOUT_SECONDS=%s\n' "$WALL_SECONDS"
  printf 'TIMEOUT_KILL_AFTER_SECONDS=30\n'
  printf 'SHM_DIR=%s\n' "$shm_dir"
} >"$CUSTODY/run-preflight.txt"

printf '%s\n' \
  "ulimit -v $VM_KIB_LIMIT; ulimit -f $FILE_BLOCK_LIMIT; /usr/bin/time -v -o $shm_dir/time.txt timeout --signal=TERM --kill-after=30s ${WALL_SECONDS}s $SINGULAR --no-rc -q $SCRIPT >$shm_dir/stdout.txt 2>$shm_dir/stderr.txt" \
  >"$CUSTODY/command.txt"

ulimit -v "$VM_KIB_LIMIT"
ulimit -f "$FILE_BLOCK_LIMIT"
/usr/bin/time -v -o "$shm_dir/time.txt" \
  timeout --signal=TERM --kill-after=30s "${WALL_SECONDS}s" \
  "$SINGULAR" --no-rc -q "$SCRIPT" \
  >"$shm_dir/stdout.txt" 2>"$shm_dir/stderr.txt"
run_rc=$?

end_ns=$(date +%s%N)
end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'END_NS=%s\n' "$end_ns"
  printf 'END_UTC=%s\n' "$end_utc"
  printf 'ELAPSED_NS=%s\n' "$((end_ns-start_ns))"
  printf 'RC=%s\n' "$run_rc"
} >"$CUSTODY/run-result.txt.tmp"
mv "$CUSTODY/run-result.txt.tmp" "$CUSTODY/run-result.txt"

for name in stdout.txt stderr.txt time.txt; do
  source_path="$shm_dir/$name"
  if [[ -f "$source_path" ]]; then
    size=$(stat -c %s "$source_path")
    sha=$(sha256sum "$source_path" | awk '{print $1}')
    printf '%s_BYTES=%s\n%s_SHA256=%s\n' "$name" "$size" "$name" "$sha" \
      >>"$CUSTODY/output-custody.txt"
    if (( size < SHM_LIMIT_BYTES )); then
      cp -- "$source_path" "$BASE/$name"
    else
      printf '%s_NOT_COPIED=size_not_below_%s\n' "$name" "$SHM_LIMIT_BYTES" \
        >>"$CUSTODY/output-custody.txt"
    fi
  else
    printf '%s_MISSING=1\n' "$name" >>"$CUSTODY/output-custody.txt"
  fi
done

printf '%s\n' "$run_rc" >"$CUSTODY/rc.tmp"
mv "$CUSTODY/rc.tmp" "$CUSTODY/rc"
exit "$run_rc"
