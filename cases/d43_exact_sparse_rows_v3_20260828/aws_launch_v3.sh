#!/usr/bin/env bash
# External launcher for the D43 v3 exact a00pp conditional pipeline.
#
# This file is deliberately OUTSIDE the sealed source archive so the archive
# digest can be pinned here as a literal without self-reference; this
# launcher's own SHA-256 is pinned by the packet seal, the producer report,
# and the operator's REGISTERED.json.
#
# One launcher invocation = one fresh atomic job namespace (mkdir is the
# namespace lease) plus one nonblocking kernel flock on the host job lock
# (held on fd 9 for the whole job).  The supervisor and every descendant run
# inside one containment boundary; after the boundary exits the launcher
# reaps, censuses, and - only if no terminal object exists - publishes the
# single NO_VERDICT authority.  The launcher never overwrites TERMINAL.json.
set -uo pipefail

EXPECTED_SOURCE_ARCHIVE_SHA256="6497a9dd5c239703e49d0cc110f4e62d5e4ef4bd6d95ffd8fba94977d0b591ed"
CASE_REL="cases/d43_exact_sparse_rows_v3_20260828"
ARCHIVE_MANIFEST_REL="jc2/$CASE_REL/SOURCE_ARCHIVE_MANIFEST_V3.sha256"

usage() {
  echo "usage: aws_launch_v3.sh --job-root DIR --archive FILE \
--registration FILE" >&2
  exit 64
}

job_root=""
archive=""
registration=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --job-root) job_root=$2; shift 2 ;;
    --archive) archive=$2; shift 2 ;;
    --registration) registration=$2; shift 2 ;;
    *) usage ;;
  esac
done
[[ -n "$job_root" && -n "$archive" && -n "$registration" ]] || usage
: "${AWS_RUN_TAG:?}"
: "${AWS_EXPECTED_HOSTNAME:?}"
[[ "$(uname -s)" == Linux ]] || exit 90
[[ "$EXPECTED_SOURCE_ARCHIVE_SHA256" =~ ^[0-9a-f]{64}$ ]] || exit 65

JOB_TAG=$(basename "$job_root")
[[ "$JOB_TAG" == "$AWS_RUN_TAG" ]] || exit 66
[[ -f "$archive" && -f "$registration" ]] || exit 67
launcher_self=$(readlink -f "$0")

terminal="$job_root/TERMINAL.json"
supervisor_pid=0
supervisor_start=0
containment_mode=none
scope_unit="jc2d43v3-${JOB_TAG//[^A-Za-z0-9_.-]/-}"
scope_unit=${scope_unit:0:180}
contract=""

publish_no_verdict() {
  local reason=$1
  [[ -d "$job_root" ]] || return 0
  [[ -e "$terminal" ]] && return 0
  local temporary="$job_root/.TERMINAL.json.launcher.$$"
  printf '{\n "schema": "jc2.d43.a00pp-exact-source-rows.v3.terminal",\n "status": "NO_VERDICT_%s",\n "terminal_authority": true,\n "positive": false,\n "job_tag": "%s",\n "utc": "%s"\n}\n' \
    "$reason" "$JOB_TAG" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    >"$temporary" || return 0
  mv "$temporary" "$terminal" 2>/dev/null || true
}

kill_boundary() {
  if [[ "$containment_mode" == systemd_scope ]]; then
    systemctl --user kill --kill-whom=all --signal=KILL \
      "$scope_unit.scope" >/dev/null 2>&1 || true
  elif [[ "$containment_mode" == setsid_pgid \
          && "$supervisor_pid" -gt 1 ]]; then
    kill -KILL -- "-$supervisor_pid" 2>/dev/null || true
  fi
}

postmortem() {
  [[ -n "$contract" && -f "$contract" ]] || return 0
  mkdir -p "$job_root/records" 2>/dev/null || return 0
  python3 -B "$contract" cleanup --pgid 0 --job-tag "$JOB_TAG" \
    --exclude-pid $$ \
    --pgid-output "$job_root/records/launcher_postmortem_pgid.json" \
    --tag-output "$job_root/records/launcher_postmortem_tag.json" \
    >"$job_root/records/launcher_postmortem.stdout.txt" \
    2>"$job_root/records/launcher_postmortem.stderr.txt"
  postmortem_rc=$?
  local cgroup_state=NOT_APPLICABLE
  if [[ "$containment_mode" == systemd_scope ]]; then
    cgroup_state=$(systemctl --user show "$scope_unit.scope" \
      --property=LoadState --property=ActiveState --property=Result \
      2>&1 | tr '\n' ';')
  fi
  printf '{"schema":"jc2.d43.a00pp-exact-source-rows.v3.launcher-postmortem","cleanup_rc":%s,"containment_mode":"%s","scope_state":"%s","terminal_exists":%s,"utc":"%s","terminal_authority":false}\n' \
    "$postmortem_rc" "$containment_mode" "$cgroup_state" \
    "$([[ -e "$terminal" ]] && echo true || echo false)" \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    >"$job_root/records/LAUNCHER_POSTMORTEM.json"
}

on_exit() {
  local rc=$?
  trap - EXIT
  if [[ ! -e "$terminal" ]]; then
    kill_boundary
    postmortem
    publish_no_verdict LAUNCHER_EMERGENCY_EXIT
  fi
  exit "$rc"
}
trap on_exit EXIT
trap 'exit 143' TERM
trap 'exit 130' INT
trap 'exit 129' HUP

# --- 1. fresh atomic job namespace (the namespace lease) --------------------
[[ ! -e "$job_root" ]] || exit 70
mkdir -m 0700 "$job_root" || exit 70
umask 077
mkdir -p "$job_root/records"

# --- 2. nonblocking kernel-backed exclusive host lease ----------------------
host_lock="${JC2_D43_V3_LOCK_PATH:-$HOME/.jc2_d43_a00pp_v3_host.lock}"
exec 9>>"$host_lock" || { publish_no_verdict LEASE_OPEN_FAILURE; exit 71; }
if ! python3 -c 'import fcntl; fcntl.flock(9, fcntl.LOCK_EX | fcntl.LOCK_NB)' \
    2>"$job_root/records/launch_flock.stderr.txt"; then
  publish_no_verdict LEASE_ALREADY_HELD
  exit 71
fi

# --- 3. verify and stage the sealed source archive --------------------------
observed_sha=$(sha256sum "$archive" | awk '{print $1}')
if [[ "$observed_sha" != "$EXPECTED_SOURCE_ARCHIVE_SHA256" ]]; then
  publish_no_verdict SOURCE_ARCHIVE_SHA_MISMATCH
  exit 72
fi
tar -tzf "$archive" >"$job_root/records/launch_archive_listing.txt" 2>&1 \
  || { publish_no_verdict SOURCE_ARCHIVE_UNREADABLE; exit 72; }
if grep -Ev '^jc2/[A-Za-z0-9._/-]+/?$' \
    "$job_root/records/launch_archive_listing.txt" \
    | grep -q . ; then
  publish_no_verdict SOURCE_ARCHIVE_UNSAFE_MEMBER
  exit 72
fi
if grep -q '\.\.' "$job_root/records/launch_archive_listing.txt"; then
  publish_no_verdict SOURCE_ARCHIVE_TRAVERSAL_MEMBER
  exit 72
fi
mkdir "$job_root/source"
tar -xzf "$archive" -C "$job_root/source" \
  2>"$job_root/records/launch_extract.stderr.txt" \
  || { publish_no_verdict SOURCE_ARCHIVE_EXTRACT_FAILURE; exit 72; }
(cd "$job_root/source" && sha256sum -c "$ARCHIVE_MANIFEST_REL") \
  >"$job_root/records/launch_source_manifest_check.txt" 2>&1 \
  || { publish_no_verdict SOURCE_MANIFEST_REPLAY_FAILURE; exit 72; }
contract="$job_root/source/jc2/$CASE_REL/job_contract_v3.py"
[[ -f "$contract" ]] || { publish_no_verdict CONTRACT_MISSING; exit 72; }
python3 -B "$contract" archive-extract-verify --archive "$archive" \
  --destination "$job_root/.archive_replay" \
  --manifest-relative "$ARCHIVE_MANIFEST_REL" --include jc2 \
  >"$job_root/records/launch_archive_replay.txt" 2>&1 \
  || { publish_no_verdict SOURCE_ARCHIVE_REPLAY_FAILURE; exit 72; }
rm -rf -- "$job_root/.archive_replay"

# --- 4. record the lease (nonce + launcher + lock identity) -----------------
RUN_NONCE=$(python3 -B "$contract" lease-record --fd 9 \
  --lock-path "$host_lock" --job-root "$job_root" --job-tag "$JOB_TAG" \
  --archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  --registration "$registration" --launcher-path "$launcher_self" \
  --output "$job_root/RUN_LEASE.json" \
  2>"$job_root/records/launch_lease_record.stderr.txt") \
  || { publish_no_verdict LEASE_RECORD_FAILURE; exit 73; }
cp "$registration" "$job_root/records/REGISTERED.json" \
  || { publish_no_verdict REGISTRATION_COPY_FAILURE; exit 73; }

manifest_json="$job_root/source/jc2/$CASE_REL/PIPELINE_MANIFEST_V3.json"
read_contract_value() {
  python3 - "$manifest_json" "$1" <<'EOF'
import json, sys
print(json.load(open(sys.argv[1]))["resource_contract"][sys.argv[2]])
EOF
}
whole_job_memory_max=$(read_contract_value whole_job_memory_max_bytes) \
  || { publish_no_verdict MANIFEST_UNREADABLE; exit 73; }
whole_job_pids_max=$(read_contract_value whole_job_pids_max) \
  || { publish_no_verdict MANIFEST_UNREADABLE; exit 73; }
whole_job_timeout=$(read_contract_value whole_job_timeout_seconds) \
  || { publish_no_verdict MANIFEST_UNREADABLE; exit 73; }

# --- 5. choose the containment boundary -------------------------------------
probe_unit="${scope_unit}-probe-$$"
if command -v systemd-run >/dev/null 2>&1 \
    && command -v systemctl >/dev/null 2>&1 \
    && [[ -r /sys/fs/cgroup/cgroup.controllers ]] \
    && systemctl --user show-environment >/dev/null 2>&1 \
    && timeout 10 systemd-run --user --scope --wait --collect --quiet \
      --unit "$probe_unit" \
      --property=MemoryMax="$whole_job_memory_max" \
      --property=MemorySwapMax=0 \
      --property=TasksMax="$whole_job_pids_max" \
      true >/dev/null 2>&1; then
  containment_mode=systemd_scope
else
  containment_mode=setsid_pgid
  command -v setsid >/dev/null 2>&1 \
    || { publish_no_verdict NO_CONTAINMENT_TOOLING; exit 76; }
fi

launcher_identity="{\"pid\":$$,\"hostname\":\"$(hostname)\",\"launcher_sha256_self\":\"$(sha256sum "$launcher_self" | awk '{print $1}')\"}"
printf '{"schema":"jc2.d43.a00pp-exact-source-rows.v3.launch","containment_mode":"%s","scope_unit":"%s","archive_sha256":"%s","launcher":%s,"utc":"%s","terminal_authority":false}\n' \
  "$containment_mode" "$scope_unit" "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  "$launcher_identity" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >"$job_root/records/LAUNCH.json"

# --- 6. start the supervisor inside the boundary ----------------------------
export JOB_ROOT="$job_root"
export JOB_TAG
export RUN_NONCE
export CONTAINMENT_MODE="$containment_mode"
supervisor="$job_root/source/jc2/$CASE_REL/run_conditional_pipeline_aws_v3.sh"
[[ -f "$supervisor" ]] || { publish_no_verdict SUPERVISOR_MISSING; exit 76; }
if [[ "$containment_mode" == systemd_scope ]]; then
  systemd-run --user --scope --wait --collect --quiet --unit "$scope_unit" \
    --property=MemoryMax="$whole_job_memory_max" \
    --property=MemorySwapMax=0 \
    --property=TasksMax="$whole_job_pids_max" \
    bash "$supervisor" \
    >"$job_root/records/launch_supervisor.stdout.txt" \
    2>"$job_root/records/launch_supervisor.stderr.txt" &
else
  setsid --wait bash "$supervisor" \
    >"$job_root/records/launch_supervisor.stdout.txt" \
    2>"$job_root/records/launch_supervisor.stderr.txt" &
fi
supervisor_pid=$!
supervisor_start=$(python3 -B "$contract" pid-start --pid "$supervisor_pid" \
  2>"$job_root/records/launch_supervisor_identity.stderr.txt" || echo 0)
printf '%s %s\n' "$supervisor_pid" "$supervisor_start" \
  >"$job_root/records/launch_supervisor.pid"

# --- 7. bounded wait with an outer launcher deadline ------------------------
launcher_deadline=$(($(date +%s) + whole_job_timeout + 7200))
launcher_timeout_hit=0
while :; do
  if ! kill -0 "$supervisor_pid" 2>/dev/null; then
    wait "$supervisor_pid"
    supervisor_rc=$?
    break
  fi
  if [[ "$(date +%s)" -ge "$launcher_deadline" ]]; then
    launcher_timeout_hit=1
    kill_boundary
    sleep 5
    kill -KILL "$supervisor_pid" 2>/dev/null || true
    wait "$supervisor_pid" 2>/dev/null
    supervisor_rc=124
    break
  fi
  sleep 10
done
printf '%s\n' "$supervisor_rc" >"$job_root/records/launch_supervisor.rc"

# --- 8. post-mortem: reap, census, and fail-closed terminal coverage --------
kill_boundary
postmortem
if [[ ! -e "$terminal" ]]; then
  if [[ "$launcher_timeout_hit" == 1 ]]; then
    publish_no_verdict LAUNCHER_DEADLINE_KILL
  else
    publish_no_verdict SUPERVISOR_DIED_WITHOUT_TERMINAL
  fi
fi
status=$(python3 - "$terminal" <<'EOF' 2>/dev/null
import json, sys
print(json.load(open(sys.argv[1])).get("status", "UNREADABLE"))
EOF
) || status=UNREADABLE
echo "TERMINAL_STATUS=$status"
[[ -e "$terminal" ]] || exit 77
exit 0
