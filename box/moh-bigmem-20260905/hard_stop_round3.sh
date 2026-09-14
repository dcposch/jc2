#!/usr/bin/env bash
# Bounded hard stop for exactly the eight charged round-3 workers.
# This script deliberately refuses to run before 2026-09-05T16:50:00Z.
set -uo pipefail

REPO=/home/ubuntu/jc2
ROOT="$REPO/box/moh-bigmem-20260905"
HARVEST="$ROOT/harvest"
KEY="$HOME/.ssh/jc2-fleet"
SSHO=(-i "$KEY" -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12 -o ServerAliveInterval=10 -o ServerAliveCountMax=2)
RSYNC_SSH="ssh -i $KEY -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12 -o ServerAliveInterval=10 -o ServerAliveCountMax=2"
IPS=(
  172.30.0.183 172.30.0.202 172.30.0.108 172.30.0.190
  172.30.0.121 172.30.0.55 172.30.0.45 172.30.0.125
)
IDS=(
  i-0e95f8ff97f6462ce i-0ce9ea50559403c22
  i-0193dc1295fc5234a i-0baedea1d34e4b978
  i-0780c67ecdc79cb0a i-018484399fd100293
  i-043f250f1956bd34b i-02efd7ecd26becc5a
)

cutoff=$(date -u -d '2026-09-05T16:50:00Z' +%s)
now=$(date -u +%s)
if (( now < cutoff )); then
  echo "REFUSE_EARLY_STOP utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) cutoff=2026-09-05T16:50:00Z" >&2
  exit 2
fi

run_tag=$(date -u +%Y%m%dT%H%M%SZ)-$$
run_dir="$HARVEST/hard-stop-$run_tag"
pre_dir="$HARVEST/t${run_tag}-pre"
post_dir="$HARVEST/t${run_tag}-post"
mkdir -p "$run_dir" "$pre_dir" "$post_dir"
exec > >(tee -a "$run_dir/hard-stop.log") 2>&1

errors=0
termination_done=0
term_failures=0
verify_failures=0

terminate_all() {
  (( termination_done == 0 )) || return 0
  termination_done=1
  trap - EXIT
  # A caught no-op (rather than SIG_IGN) resets to default across exec, so
  # timeout can still signal child commands while this driver finishes all IDs.
  trap ':' INT TERM
  echo "TERMINATE_BEGIN utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  local id rc
  for id in "${IDS[@]}"; do
    echo "TERM_ID=$id"
    timeout --kill-after=5s 45s sh "$REPO/ops/fleet/fleet.sh" term "$id" \
      > >(tee -a "$run_dir/terminate.txt") \
      2> >(tee -a "$run_dir/terminate.txt" >&2)
    rc=$?
    echo "TERM_RC id=$id rc=$rc" | tee -a "$run_dir/terminate.txt"
    (( rc == 0 )) || term_failures=$((term_failures+1))
  done

  local attempt remaining ips_rc state retry_rc aws_verify_rc listed
  remaining=8
  for attempt in 1 2 3 4 5 6; do
    timeout --kill-after=5s 45s aws ec2 describe-instances --region us-east-1 \
      --instance-ids "${IDS[@]}" \
      --query 'Reservations[].Instances[].{ID:InstanceId,IP:PrivateIpAddress,State:State.Name}' \
      --output json >"$run_dir/aws-post-attempt-$attempt.json" \
      2>"$run_dir/aws-post-attempt-$attempt.err"
    aws_verify_rc=$?
    if (( aws_verify_rc != 0 )); then
      echo "AWS_TERM_VERIFY_CALL_FAILED attempt=$attempt rc=$aws_verify_rc"
      remaining=8
    else
      remaining=0
      for id in "${IDS[@]}"; do
        state=$(jq -r --arg id "$id" '[.[] | select(.ID==$id)] | if length == 1 then .[0].State else "MISSING_OR_DUPLICATE" end' \
          "$run_dir/aws-post-attempt-$attempt.json")
        echo "AWS_TERM_STATE attempt=$attempt id=$id state=$state"
        if [[ $state != shutting-down && $state != terminated ]]; then
          remaining=$((remaining+1))
          echo "TERM_RETRY attempt=$attempt id=$id state=$state"
          timeout --kill-after=5s 45s sh "$REPO/ops/fleet/fleet.sh" term "$id" \
            >>"$run_dir/terminate.txt" 2>&1
          retry_rc=$?
          echo "TERM_RETRY_RC attempt=$attempt id=$id rc=$retry_rc" | tee -a "$run_dir/terminate.txt"
          (( retry_rc == 0 )) || term_failures=$((term_failures+1))
        fi
      done
    fi
    (( remaining == 0 )) && break
    sleep 5
  done
  cp "$run_dir/aws-post-attempt-$attempt.json" "$run_dir/aws-post.json" 2>/dev/null || true
  if (( remaining != 0 )); then
    verify_failures=$remaining
    echo "AWS_TERM_VERIFY_FAILED remaining=$remaining"
  else
    echo "AWS_TERM_VERIFY_OK exact_target_ids_terminal=8"
  fi

  timeout --kill-after=5s 45s sh "$REPO/ops/fleet/fleet.sh" ips \
    >"$run_dir/fleet-ips-final.txt" 2>&1
  ips_rc=$?
  cat "$run_dir/fleet-ips-final.txt"
  listed=0
  if (( ips_rc != 0 )); then
    echo "IPS_VERIFY_CALL_FAILED rc=$ips_rc"
    verify_failures=$((verify_failures+1))
  else
    for id in "${IDS[@]}"; do
      if grep -Fq "$id" "$run_dir/fleet-ips-final.txt"; then
        echo "IPS_VERIFY_TARGET_STILL_LISTED id=$id"
        listed=$((listed+1))
      fi
    done
    verify_failures=$((verify_failures+listed))
  fi
  if (( listed == 0 && ips_rc == 0 )); then
    echo "IPS_VERIFY_OK exact_target_ids_absent=8"
  else
    echo "IPS_VERIFY_FAILED listed=$listed call_rc=$ips_rc"
  fi
  echo "TERMINATE_END utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) term_failures=$term_failures verify_failures=$verify_failures"
}

# Even an interrupted harvest must still attempt all eight exact-ID terminations.
trap terminate_all EXIT INT TERM

echo "HARD_STOP_BEGIN utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) run_tag=$run_tag"

validate_pairs() {
  local phase=$1 json_path="$run_dir/aws-$1.json" err_path="$run_dir/aws-$1.err"
  local out_name=$2 aws_rc i id expected_ip actual_ip state
  local -n out_ref="$out_name"
  out_ref=()
  timeout --kill-after=5s 30s aws ec2 describe-instances --region us-east-1 \
    --instance-ids "${IDS[@]}" \
    --query 'Reservations[].Instances[].{ID:InstanceId,IP:PrivateIpAddress,State:State.Name}' \
    --output json >"$json_path" 2>"$err_path"
  aws_rc=$?
  echo "AWS_${phase^^}_RC=$aws_rc"
  if (( aws_rc != 0 )); then
    echo "PAIR_VALIDATION_UNAVAILABLE phase=$phase no_worker_will_be_contacted"
    errors=$((errors+1))
    return 1
  fi
  for i in "${!IDS[@]}"; do
    id=${IDS[$i]}
    expected_ip=${IPS[$i]}
    actual_ip=$(jq -r --arg id "$id" '.[] | select(.ID==$id) | .IP // ""' "$json_path")
    state=$(jq -r --arg id "$id" '.[] | select(.ID==$id) | .State // ""' "$json_path")
    echo "PAIR phase=$phase id=$id expected_ip=$expected_ip actual_ip=$actual_ip state=$state"
    if [[ $actual_ip == "$expected_ip" && $state == running ]]; then
      out_ref+=("$expected_ip")
    else
      echo "PAIR_NOT_CONTACTED phase=$phase id=$id expected_ip=$expected_ip actual_ip=$actual_ip state=$state"
      errors=$((errors+1))
    fi
  done
}

# An IP is contacted only when its charged ID is currently running at that
# exact private address. This check is repeated immediately before stopping.
ACTIVE_IPS=()
validate_pairs pre ACTIVE_IPS || true

snapshot_one() {
  local ip=$1 dest="$pre_dir/$1" rc=0 harvest_rc=0 ssh_rc=0 hp sp
  mkdir -p "$dest"
  timeout --kill-after=5s 20s bash "$ROOT/harvest_one.sh" "$ip" "${run_tag}-pre" \
    >"$dest/harvest-one.log" 2>&1 &
  hp=$!
  timeout --kill-after=5s 20s ssh "${SSHO[@]}" ubuntu@"$ip" 'bash -s' \
    >"$dest/prestop-custody.txt" 2>&1 <<'REMOTE' &
echo UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo HOST=$(hostname)
echo PROCESS_GROUPS_BEGIN
ps -eo pid,ppid,pgid,sid,lstart,etime,rss,vsz,pcpu,state,comm,args
echo PROCESS_GROUPS_END
echo INPUT_OUTPUT_SHA256_BEGIN
find "$HOME/moh-bigmem-20260905/targets" -type f \
  \( -name "*.ms" -o -name "*.sing" -o -name "*.tsv" \
     -o -name "*.manifest.json" -o -name "*.status.json" -o -name "*.emit.json" -o -name "*meta.json" \
     -o -name "guided_gb_result.json" -o -name "*.g2.out" \
     -o -name "*.g2.stderr" -o -name "*.g2.stdout" \
     -o -name "*.out" -o -name "*.err" -o -name "*.stdout" -o -name "*.stderr" -o -name "*.rc" \
     -o -name "*.meta" -o -name "*.rss.log" \) -print0 \
  | sort -z | xargs -0 -r sha256sum
echo INPUT_OUTPUT_SHA256_END
REMOTE
  sp=$!
  wait "$hp" || harvest_rc=$?
  wait "$sp" || ssh_rc=$?
  echo "$harvest_rc" >"$dest/harvest-one.rc"
  (( harvest_rc == 0 && ssh_rc == 0 )) || rc=1
  echo "$rc" >"$dest/snapshot.rc"
  return "$rc"
}

pids=()
for ip in "${ACTIVE_IPS[@]}"; do snapshot_one "$ip" & pids+=("$!"); done
for pid in "${pids[@]}"; do wait "$pid" || true; done
for ip in "${ACTIVE_IPS[@]}"; do
  rc=$(<"$pre_dir/$ip/snapshot.rc")
  echo "PRE_SNAPSHOT_RC ip=$ip rc=$rc"
  (( rc == 0 )) || errors=$((errors+1))
done

# Close the validation-to-mutation window before sending any signal.
STOP_IPS=()
validate_pairs prestop STOP_IPS || true
if (( ${#STOP_IPS[@]} != 8 )); then
  echo "PRESTOP_VALIDATION_RETRY prior_count=${#STOP_IPS[@]}"
  sleep 1
  validate_pairs prestop-retry STOP_IPS || true
fi
if (( ${#STOP_IPS[@]} != 8 )); then
  echo "PRESTOP_VALIDATION_UNRESOLVED count=${#STOP_IPS[@]} terminating_exact_ids_without_unsafe_ssh"
  errors=$((errors+1))
  terminate_all
  echo "HARD_STOP_ABORT utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=prestop-validation errors=$errors"
  exit 1
fi

stop_one() {
  local ip=$1 label=${2:-stop} dest="$pre_dir/$1" rc
  mkdir -p "$dest"
  timeout --kill-after=5s 75s ssh "${SSHO[@]}" ubuntu@"$ip" 'bash -s' \
    >"$dest/$label.txt" 2>&1 <<'REMOTE'
set -u
echo "STOP_BEGIN utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
control_sid=$(ps -o sid= -p $$ | tr -d ' ')
declare -A job_sids=()
discover_sids() {
  local sid
  while read -r sid; do
    [[ -n $sid && $sid != 0 && $sid != 1 && $sid != "$control_sid" ]] || continue
    job_sids[$sid]=1
  done < <(
    ps -eo sid=,comm=,args= | awk -v self="$control_sid" '
      $1 != self &&
      ($2 == "msolve" || $2 == "Singular" ||
       $0 ~ /[m]oh-bigmem-20260905/ ||
       $0 ~ /[r]un_msolve_pipeline[.]sh/ ||
       $0 ~ /[r]un_guided_pipeline[.]sh/ ||
       $0 ~ /[r]un_v18_msolve[.]sh/ ||
       $0 ~ /[r]un_msolve_job[.]sh/ ||
       $0 ~ /[r]un_guided_job[.]py/ ||
       $0 ~ /[e]xtract_native[.]sh/) {print $1}' | sort -nu
  )
}
discover_sids
printf 'CAPTURED_SIDS'
for sid in "${!job_sids[@]}"; do printf ' %s' "$sid"; done
printf '\n'
for sid in "${!job_sids[@]}"; do pkill -TERM -s "$sid" 2>/dev/null || true; done
sleep 5
discover_sids
for sid in "${!job_sids[@]}"; do pkill -KILL -s "$sid" 2>/dev/null || true; done
sleep 2
left=0
for sid in "${!job_sids[@]}"; do
  if ps -eo pid=,sid=,stat=,comm=,args= | awk -v sid="$sid" '$2 == sid && $3 !~ /^Z/ {print; found=1} END {exit(found ? 0 : 1)}'; then
    echo "SESSION_LEFT sid=$sid"
    left=1
  fi
done
if ps -eo pid=,sid=,stat=,comm=,args= | awk -v self="$control_sid" '
  $2 != self && $3 !~ /^Z/ && ($4 == "msolve" || $4 == "Singular" ||
  $0 ~ /[m]oh-bigmem-20260905/ || $0 ~ /[r]un_msolve_pipeline[.]sh/ ||
  $0 ~ /[r]un_guided_pipeline[.]sh/ || $0 ~ /[r]un_v18_msolve[.]sh/ ||
  $0 ~ /[r]un_msolve_job[.]sh/ || $0 ~ /[r]un_guided_job[.]py/ ||
  $0 ~ /[e]xtract_native[.]sh/) {print; found=1}
  END {exit(found ? 0 : 1)}'; then
  echo CAMPAIGN_PROCESS_LEFT
  left=1
fi
echo "STOP_VERIFY_LEFT=$left utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$left"
REMOTE
  rc=$?
  echo "$rc" >"$dest/$label.rc"
  return "$rc"
}

pids=()
for ip in "${STOP_IPS[@]}"; do stop_one "$ip" & pids+=("$!"); done
for pid in "${pids[@]}"; do wait "$pid" || true; done
STOPPED_IPS=()
RETRY_IPS=()
for ip in "${STOP_IPS[@]}"; do
  rc=$(<"$pre_dir/$ip/stop.rc")
  echo "STOP_RC ip=$ip rc=$rc"
  if (( rc == 0 )); then STOPPED_IPS+=("$ip"); else RETRY_IPS+=("$ip"); fi
done
if (( ${#RETRY_IPS[@]} != 0 )); then
  sleep 1
  RETRY_VALIDATED_IPS=()
  validate_pairs stop-retry-validate RETRY_VALIDATED_IPS || true
  if (( ${#RETRY_VALIDATED_IPS[@]} != 8 )); then
    echo "STOP_RETRY_VALIDATION_UNRESOLVED count=${#RETRY_VALIDATED_IPS[@]} terminating_exact_ids_immediately"
    errors=$((errors+1))
    terminate_all
    echo "HARD_STOP_ABORT utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=stop-retry-validation errors=$errors"
    exit 1
  fi
  pids=()
  for ip in "${RETRY_IPS[@]}"; do stop_one "$ip" stop-retry & pids+=("$!"); done
  for pid in "${pids[@]}"; do wait "$pid" || true; done
  for ip in "${RETRY_IPS[@]}"; do
    rc=$(<"$pre_dir/$ip/stop-retry.rc")
    echo "STOP_RETRY_RC ip=$ip rc=$rc"
    if (( rc == 0 )); then STOPPED_IPS+=("$ip"); else errors=$((errors+1)); fi
  done
fi
if (( ${#STOPPED_IPS[@]} != 8 )); then
  echo "STOP_UNRESOLVED stopped_count=${#STOPPED_IPS[@]} terminating_exact_ids_immediately"
  terminate_all
  echo "HARD_STOP_ABORT utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=stop-verification errors=$errors"
  exit 1
fi

# Revalidate again before the final read-only SSH/rsync custody pass.
POST_IPS=()
validate_pairs postvalidate POST_IPS || true
if (( ${#POST_IPS[@]} != 8 )); then
  echo "POST_VALIDATION_RETRY prior_count=${#POST_IPS[@]}"
  sleep 1
  validate_pairs postvalidate-retry POST_IPS || true
fi

poststop_one() {
  local ip=$1 dest="$post_dir/$1" rc=0 pull_rc=0 hash_rc=0
  mkdir -p "$dest/tree"
  timeout --kill-after=5s 60s ssh "${SSHO[@]}" ubuntu@"$ip" 'bash -s' \
    >"$dest/poststop-custody.txt" 2>&1 <<'REMOTE' || hash_rc=$?
echo UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
find "$HOME/moh-bigmem-20260905" -type f \
  \( -name "*.ms" -o -name "*.sing" -o -name "*.tsv" \
     -o -name "*.manifest.json" -o -name "*.status.json" -o -name "*.emit.json" -o -name "*meta.json" \
     -o -name "guided_gb_result.json" -o -name "*.g2.out" \
     -o -name "*.g2.stderr" -o -name "*.g2.stdout" \
     -o -name "*.out" -o -name "*.err" -o -name "*.stdout" -o -name "*.stderr" -o -name "*.rc" \
     -o -name "*.meta" -o -name "*.rss.log" -o -name "*.log" \) \
  -print0 | sort -z | xargs -0 -r sha256sum
REMOTE
  timeout --kill-after=5s 120s rsync -az -e "$RSYNC_SSH" \
    --include='*/' \
    --include='*.stderr' --include='*.stdout' --include='*.log' --include='*.out' \
    --include='*.meta' --include='*.manifest.json' --include='*.status.json' --include='*meta.json' \
    --include='*.emit.json' --include='*.rc' --include='*.rss.log' \
    --include='guided_gb_result.json' --include='*.err' --include='*.g2.out' \
    --exclude='*.ms' --exclude='*.sing' --exclude='*.tsv' --exclude='*.pyc' \
    --exclude='bin/' --exclude='circuit-src/' \
    --exclude='*' \
    ubuntu@"$ip":~/moh-bigmem-20260905/ "$dest/tree/" \
    >"$dest/strict-rsync.log" 2>&1 || pull_rc=$?
  find "$dest/tree" -type f -print0 | sort -z | xargs -0 -r sha256sum \
    >"$dest/local-sha256.txt"
  awk '{h=$1; $1=""; p=$0; sub(/^[[:space:]]+/,"",p); sub(/^.*\/moh-bigmem-20260905\//,"",p); print h"  "p}' \
    "$dest/poststop-custody.txt" >"$dest/remote-relative-sha256.txt"
  awk -v prefix="$dest/tree/" '{h=$1; $1=""; p=$0; sub(/^[[:space:]]+/,"",p); sub("^" prefix,"",p); print h"  "p}' \
    "$dest/local-sha256.txt" >"$dest/local-relative-sha256.txt"
  : >"$dest/hash-compare.txt"
  while read -r local_hash rel; do
    remote_hash=$(awk -v p="$rel" '$2 == p {print $1; exit}' "$dest/remote-relative-sha256.txt")
    if [[ -z $remote_hash ]]; then
      echo "MISSING_REMOTE_HASH $rel" >>"$dest/hash-compare.txt"
      rc=1
    elif [[ $remote_hash != "$local_hash" ]]; then
      echo "HASH_MISMATCH $rel local=$local_hash remote=$remote_hash" >>"$dest/hash-compare.txt"
      rc=1
    fi
  done <"$dest/local-relative-sha256.txt"
  [[ -s $dest/hash-compare.txt ]] || echo HASH_COMPARE_OK >"$dest/hash-compare.txt"
  (( hash_rc == 0 && pull_rc == 0 )) || rc=1
  echo "hash_rc=$hash_rc pull_rc=$pull_rc compare_rc=$rc" >"$dest/poststop.rc"
  return "$rc"
}

pids=()
for ip in "${POST_IPS[@]}"; do poststop_one "$ip" & pids+=("$!"); done
for pid in "${pids[@]}"; do wait "$pid" || true; done
for ip in "${POST_IPS[@]}"; do
  read -r status <"$post_dir/$ip/poststop.rc"
  echo "POSTSTOP ip=$ip $status"
  [[ $status == *"compare_rc=0" ]] || errors=$((errors+1))
done

terminate_all
errors=$((errors+term_failures+verify_failures))
echo "HARD_STOP_END utc=$(date -u +%Y-%m-%dT%H:%M:%SZ) errors=$errors term_failures=$term_failures verify_failures=$verify_failures run_dir=$run_dir"
(( errors == 0 ))
