#!/bin/sh
# Generic research-lane runner.
# Usage: ops/lane.sh <adapter> <unique-tag> <promptfile>
main() {
set -u

if [ "$#" -ne 3 ]; then
  echo "usage: $0 <adapter> <unique-tag> <promptfile>" >&2
  exit 2
fi

adapter=$1
tag=$2
prompt_arg=$3
launch_dir=$(pwd -P)
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)

case "$prompt_arg" in
  /*) prompt_file=$prompt_arg ;;
  *) prompt_file=$launch_dir/$prompt_arg ;;
esac

case "$tag" in
  ''|*[!A-Za-z0-9._-]*)
    echo "invalid tag (use A-Z, a-z, 0-9, dot, underscore, or hyphen): $tag" >&2
    exit 2
    ;;
esac

case "$adapter" in
  ''|*[!a-z0-9_-]*)
    echo "invalid adapter name: $adapter" >&2
    exit 2
    ;;
esac

adapter_script=$script_dir/adapters/$adapter.sh
fallacy_file=$repo_root/FALLACY-v2.md
charge_validator=$script_dir/validate_charge_basis.py
[ -x "$adapter_script" ] || {
  echo "unknown adapter: $adapter" >&2
  exit 2
}
[ -f "$prompt_file" ] || {
  echo "prompt file not found: $prompt_file" >&2
  exit 2
}
[ -f "$fallacy_file" ] && [ ! -L "$fallacy_file" ] || {
  echo "required regular appendix missing: $fallacy_file" >&2
  exit 2
}
[ -f "$charge_validator" ] && [ ! -L "$charge_validator" ] || {
  echo "required charge-basis validator missing: $charge_validator" >&2
  exit 2
}
seal_tool=$script_dir/seal.py
[ -f "$seal_tool" ] && [ ! -L "$seal_tool" ] || {
  echo "required seal tool missing: $seal_tool" >&2
  exit 2
}
command -v python3 >/dev/null 2>&1 || {
  echo "python3 is required for charge-basis validation" >&2
  exit 2
}
sandbox_exec=/usr/bin/sandbox-exec
[ -x "$sandbox_exec" ] || {
  echo "the macOS process sandbox is required for external-model lanes: $sandbox_exec" >&2
  exit 2
}

fallacy_bytes=$(wc -c < "$fallacy_file" | tr -d '[:space:]') || exit 2
case "$fallacy_bytes" in
  ''|*[!0-9]*)
    echo "could not measure appendix: $fallacy_file" >&2
    exit 2
    ;;
esac
if [ "$fallacy_bytes" -eq 0 ] || [ "$fallacy_bytes" -gt 2048 ]; then
  echo "appendix must be 1..2048 bytes: $fallacy_file ($fallacy_bytes bytes)" >&2
  exit 2
fi

cd "$repo_root" || exit 2
mkdir -p .lane-locks xmodel

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha_line=$(sha256sum "$1") || return 1
  elif command -v shasum >/dev/null 2>&1; then
    sha_line=$(shasum -a 256 "$1") || return 1
  else
    echo "no SHA-256 tool available" >&2
    return 1
  fi
  sha_value=${sha_line%% *}
  [ -n "$sha_value" ] || return 1
  printf '%s\n' "$sha_value"
}

for existing in "xmodel/$tag.log" "xmodel/$tag.md" "xmodel/$tag.run" \
    "xmodel/$tag.run.v2" "xmodel/$tag.raw.md" "xmodel/$tag.overflow"; do
  if [ -e "$existing" ]; then
    echo "duplicate tag refused; choose a new attempt tag: $tag ($existing exists)" >&2
    exit 3
  fi
done

lane_tmp_root=${TMPDIR:-/tmp}
case "$lane_tmp_root" in
  /*) ;;
  *)
    echo "TMPDIR must be absolute: $lane_tmp_root" >&2
    exit 2
    ;;
esac
lane_tmp_root=$(CDPATH= cd -- "$lane_tmp_root" 2>/dev/null && pwd -P) || {
  echo "temporary directory root unavailable: $lane_tmp_root" >&2
  exit 2
}

lock_dir=.lane-locks/$tag
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "tag is already live: $tag" >&2
  exit 3
fi
lane_tmp_dir=
cleanup() {
  if [ -n "$lane_tmp_dir" ]; then
    case "$lane_tmp_dir" in
      "$lane_tmp_root"/jc2-lane.*)
        rm -rf -- "$lane_tmp_dir" 2>/dev/null || true
        ;;
    esac
  fi
  rmdir "$lock_dir" 2>/dev/null || true
}
child_pid=
caught_signal=
forward_signal() {
  caught_signal=$1
  if [ -n "$child_pid" ]; then
    kill -s "$1" "$child_pid" 2>/dev/null || true
  fi
}
trap cleanup EXIT
trap 'forward_signal HUP' HUP
trap 'forward_signal INT' INT
trap 'forward_signal TERM' TERM

lane_tmp_dir=$(mktemp -d "$lane_tmp_root/jc2-lane.XXXXXX") || {
  echo "could not create secure lane temporary directory" >&2
  exit 2
}
chmod 700 "$lane_tmp_dir" || exit 2
prompt_snapshot=$lane_tmp_dir/original-prompt.txt
fallacy_snapshot=$lane_tmp_dir/FALLACY-v2.md
charge_validator_snapshot=$lane_tmp_dir/validate_charge_basis.py
seal_tool_snapshot=$lane_tmp_dir/seal.py
model_prompt_file=$lane_tmp_dir/model-prompt.txt
sandbox_profile=$lane_tmp_dir/external-model.sb
inputs_dir=$lane_tmp_dir/inputs
inputs_manifest=$lane_tmp_dir/charged-inputs.list
inputs_post_manifest=$lane_tmp_dir/charged-inputs-post.list
# Keep this lexical: boundary setup must neither resolve nor inspect the excluded
# nested worktree.  Seatbelt resolves aliases when enforcing the path filter.
excluded_tree=$repo_root/jc2-lean

log_file=xmodel/$tag.log
run_file=xmodel/$tag.run.v2
run_path=$repo_root/$run_file
report_file=xmodel/$tag.md
start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
prompt_sha=$(sha256_file "$prompt_file") || exit 2
adapter_sha=$(sha256_file "$adapter_script") || exit 2
launcher_sha=$(sha256_file "$script_dir/lane.sh") || exit 2
charge_validator_sha=$(sha256_file "$charge_validator") || exit 2
seal_tool_sha=$(sha256_file "$seal_tool") || exit 2
fallacy_sha=$(sha256_file "$fallacy_file") || exit 2
cp "$prompt_file" "$prompt_snapshot" || exit 2
cp "$fallacy_file" "$fallacy_snapshot" || exit 2
cp "$charge_validator" "$charge_validator_snapshot" || exit 2
cp "$seal_tool" "$seal_tool_snapshot" || exit 2
chmod 400 "$prompt_snapshot" "$fallacy_snapshot" "$charge_validator_snapshot" \
  "$seal_tool_snapshot" || exit 2
prompt_snapshot_sha=$(sha256_file "$prompt_snapshot") || exit 2
fallacy_snapshot_sha=$(sha256_file "$fallacy_snapshot") || exit 2
charge_validator_snapshot_sha=$(sha256_file "$charge_validator_snapshot") || exit 2
seal_tool_snapshot_sha=$(sha256_file "$seal_tool_snapshot") || exit 2
fallacy_snapshot_bytes=$(wc -c < "$fallacy_snapshot" | tr -d '[:space:]') || exit 2
prepared_prompt_sha=$(sha256_file "$prompt_file") || prepared_prompt_sha=ERROR
prepared_fallacy_sha=$(sha256_file "$fallacy_file") || prepared_fallacy_sha=ERROR
prepared_charge_validator_sha=$(sha256_file "$charge_validator") || prepared_charge_validator_sha=ERROR
prepared_seal_tool_sha=$(sha256_file "$seal_tool") || prepared_seal_tool_sha=ERROR
if [ "$prompt_snapshot_sha" != "$prompt_sha" ] || \
   [ "$prepared_prompt_sha" != "$prompt_sha" ] || \
   [ "$fallacy_snapshot_sha" != "$fallacy_sha" ] || \
   [ "$prepared_fallacy_sha" != "$fallacy_sha" ] || \
   [ "$charge_validator_snapshot_sha" != "$charge_validator_sha" ] || \
   [ "$prepared_charge_validator_sha" != "$charge_validator_sha" ] || \
   [ "$seal_tool_snapshot_sha" != "$seal_tool_sha" ] || \
   [ "$prepared_seal_tool_sha" != "$seal_tool_sha" ] || \
   [ "$fallacy_snapshot_bytes" != "$fallacy_bytes" ]; then
  echo "hashed input changed while preparing model prompt; run refused" >&2
  exit 2
fi

fallacy_marker='# FALLACY-v2.md: campaign reasoning guardrail'
if grep -F "$fallacy_marker" "$prompt_snapshot" >/dev/null 2>&1; then
  echo "prompt already contains the FALLACY-v2.md appendix marker; run refused" >&2
  exit 2
fi

# Every lane prompt must name its mandated report path so a completed model
# response cannot be lost to a misdirected or unwritten report.
if ! grep -F "xmodel/$tag.md" "$prompt_snapshot" >/dev/null 2>&1; then
  echo "prompt does not name its mandated report path xmodel/$tag.md; run refused" >&2
  exit 2
fi

# A prompt that instructs the BODY-END convention declares the marker
# contract; a finished report without the marker then fails closed as partial.
body_end_contract=NONE
if grep -F '<!-- BODY-END -->' "$prompt_snapshot" >/dev/null 2>&1; then
  body_end_contract=DECLARED
fi

# Immutable charged-input snapshots: `charged_input=<repo-relative-path>`
# lines in the prompt are frozen into the write-denied custody directory, and
# every literal `{{LANE_INPUTS}}` in the composed prompt points the model at
# those frozen bytes.  Declarations and the placeholder must appear together.
input_placeholder='{{LANE_INPUTS}}'
charged_inputs=$(sed -n 's/^charged_input=//p' "$prompt_snapshot")
prompt_has_placeholder=0
if grep -F "$input_placeholder" "$prompt_snapshot" >/dev/null 2>&1; then
  prompt_has_placeholder=1
fi
input_count=0
if [ -n "$charged_inputs" ] || [ "$prompt_has_placeholder" -eq 1 ]; then
  if [ -z "$charged_inputs" ] || [ "$prompt_has_placeholder" -eq 0 ]; then
    echo "charged_input declarations and the $input_placeholder placeholder must appear together; run refused" >&2
    exit 2
  fi
  case "$inputs_dir" in
    *[!A-Za-z0-9/._-]*)
      echo "lane inputs directory has unsupported characters: $inputs_dir" >&2
      exit 2
      ;;
  esac
  mkdir "$inputs_dir" || exit 2
  while IFS= read -r charged_rel; do
    [ -n "$charged_rel" ] || continue
    case "$charged_rel" in
      /*|*..*|*[!A-Za-z0-9/._-]*)
        echo "invalid charged input path: $charged_rel" >&2
        exit 2
        ;;
      jc2-lean|jc2-lean/*)
        echo "charged input inside the excluded tree refused: $charged_rel" >&2
        exit 2
        ;;
    esac
    charged_src=$repo_root/$charged_rel
    if [ ! -f "$charged_src" ] || [ -L "$charged_src" ]; then
      echo "charged input missing or not a regular file: $charged_rel" >&2
      exit 2
    fi
    charged_base=$(basename "$charged_rel")
    charged_dest=$inputs_dir/$charged_base
    if [ -e "$charged_dest" ]; then
      echo "duplicate charged input basename: $charged_base" >&2
      exit 2
    fi
    charged_src_sha=$(sha256_file "$charged_src") || exit 2
    cp "$charged_src" "$charged_dest" || exit 2
    chmod 400 "$charged_dest" || exit 2
    charged_snap_sha=$(sha256_file "$charged_dest") || exit 2
    if [ "$charged_snap_sha" != "$charged_src_sha" ]; then
      echo "charged input changed while being snapshotted: $charged_rel" >&2
      exit 2
    fi
    input_count=$((input_count + 1))
    printf '%s %s %s\n' "$charged_rel" "$charged_base" "$charged_src_sha" \
      >> "$inputs_manifest"
  done <<CHARGED_INPUTS_EOF
$charged_inputs
CHARGED_INPUTS_EOF
fi
# The adapter and every process it spawns inherit this Seatbelt profile.  Lane
# custody stays readable for exact prompt delivery, but even a same-user model
# shell cannot chmod or rewrite the snapshotted inputs.
if [ "$prompt_has_placeholder" -eq 1 ]; then
  if ! {
    sed "s|{{LANE_INPUTS}}|$inputs_dir|g" "$prompt_snapshot"
    printf '\n\n'
    cat "$fallacy_snapshot"
  } > "$model_prompt_file"; then
    echo "could not compose model prompt" >&2
    exit 2
  fi
elif ! {
  cat "$prompt_snapshot"
  printf '\n\n'
  cat "$fallacy_snapshot"
} > "$model_prompt_file"; then
  echo "could not compose model prompt" >&2
  exit 2
fi
chmod 600 "$model_prompt_file" || exit 2
model_prompt_sha=$(sha256_file "$model_prompt_file") || exit 2
prepared_prompt_sha=$(sha256_file "$prompt_file") || prepared_prompt_sha=ERROR
prepared_fallacy_sha=$(sha256_file "$fallacy_file") || prepared_fallacy_sha=ERROR
if [ "$prepared_prompt_sha" != "$prompt_sha" ] || \
   [ "$prepared_fallacy_sha" != "$fallacy_sha" ]; then
  echo "hashed lane input changed while preparing model prompt; run refused" >&2
  exit 2
fi
if ! {
  printf '%s\n' '(version 1)'
  printf '%s\n' '(allow default)'
  printf '%s\n' '(deny file-read* (literal (param "EXCLUDED_TREE")))'
  printf '%s\n' '(deny file-read* (subpath (param "EXCLUDED_TREE")))'
  printf '%s\n' '(deny file-write* (literal (param "EXCLUDED_TREE")))'
  printf '%s\n' '(deny file-write* (subpath (param "EXCLUDED_TREE")))'
  printf '%s\n' '(deny file-write* (subpath (param "CUSTODY_ROOT")))'
  printf '%s\n' '(deny file-write* (literal (param "RUN_FILE")))'
} > "$sandbox_profile"; then
  echo "could not create external-model sandbox profile" >&2
  exit 2
fi
chmod 400 "$model_prompt_file" "$sandbox_profile" || exit 2
sandbox_profile_sha=$(sha256_file "$sandbox_profile") || exit 2
basis=$(git rev-parse HEAD 2>/dev/null || echo UNKNOWN)

{
  echo "run_schema=2"
  echo "tag=$tag"
  echo "adapter=$adapter"
  echo "pid=$$"
  echo "host=$(hostname)"
  echo "basis=$basis"
  echo "prompt=$prompt_file"
  echo "prompt_sha256=$prompt_sha"
  echo "adapter_sha256=$adapter_sha"
  echo "launcher=ops/lane.sh"
  echo "launcher_sha256=$launcher_sha"
  echo "sandbox_enforcement=MACOS_SEATBELT"
  echo "sandbox_profile_sha256=$sandbox_profile_sha"
  echo "charge_basis_validator=ops/validate_charge_basis.py"
  echo "charge_basis_validator_sha256=$charge_validator_sha"
  echo "seal_tool=ops/seal.py"
  echo "seal_tool_sha256=$seal_tool_sha"
  echo "body_end_contract=$body_end_contract"
  echo "charged_inputs=$input_count"
  if [ "$input_count" -gt 0 ]; then
    echo "lane_inputs_dir=$inputs_dir"
    manifest_index=0
    while read -r manifest_rel manifest_base manifest_sha; do
      manifest_index=$((manifest_index + 1))
      echo "charged_input_${manifest_index}=$manifest_rel"
      echo "charged_input_${manifest_index}_basename=$manifest_base"
      echo "charged_input_${manifest_index}_sha256=$manifest_sha"
    done < "$inputs_manifest"
  fi
  echo "fallacy=FALLACY-v2.md"
  echo "fallacy_bytes=$fallacy_bytes"
  echo "fallacy_sha256=$fallacy_sha"
  echo "model_prompt=$model_prompt_file"
  echo "model_prompt_sha256=$model_prompt_sha"
  echo "start_utc=$start_utc"
  echo "provenance_scope=DECLARED_LANE_INPUTS"
  echo "initial_status=RUNNING"
} > "$run_file"

"$sandbox_exec" \
  -D "EXCLUDED_TREE=$excluded_tree" \
  -D "CUSTODY_ROOT=$lane_tmp_dir" \
  -D "RUN_FILE=$run_path" \
  -f "$sandbox_profile" \
  sh "$adapter_script" "$model_prompt_file" > "$log_file" 2>&1 &
child_pid=$!
echo "child_pid=$child_pid" >> "$run_file"
wait "$child_pid"
rc=$?

if [ -n "$caught_signal" ]; then
  while kill -0 "$child_pid" 2>/dev/null; do
    sleep 1
  done
  wait "$child_pid" 2>/dev/null || true
  case "$caught_signal" in
    HUP) rc=129 ;;
    INT) rc=130 ;;
    TERM) rc=143 ;;
  esac
  echo "cancel_signal=$caught_signal" >> "$run_file"
fi

if [ "$rc" -eq 0 ] && [ ! -s "$report_file" ]; then
  echo "adapter exited 0 but required report is absent: $report_file" >> "$log_file"
  rc=4
fi

# Truncation, not loss: a report is charged only through its sole standalone
# BODY-END line.  Non-whitespace overflow is banked uncharged beside the raw
# original; a finished report with no marker under a declared contract is
# banked as a partial draft and the lane fails closed.
seal_boundary=NOT_CHECKED
report_state=MISSING
overflow_file=xmodel/$tag.overflow
raw_report_file=xmodel/$tag.raw.md
if [ -s "$report_file" ]; then
  ready_seal_tool_sha=$(sha256_file "$seal_tool_snapshot") || ready_seal_tool_sha=ERROR
  if [ "$ready_seal_tool_sha" != "$seal_tool_sha" ]; then
    seal_boundary=TOOL_MUTATED
    report_state=UNVERIFIED
    echo "seal tool snapshot changed; result is quarantined" >> "$log_file"
    [ "$rc" -ne 0 ] || rc=5
  elif divert_out=$(python3 "$seal_tool_snapshot" divert "$report_file" \
      --overflow "$overflow_file" --raw "$raw_report_file" 2>&1); then
    printf '%s\n' "$divert_out" >> "$log_file"
    seal_boundary=$(printf '%s\n' "$divert_out" | \
      sed -n 's/.* status=\([A-Z_]*\).*/\1/p' | head -1)
    [ -n "$seal_boundary" ] || seal_boundary=UNPARSED
    case "$seal_boundary" in
      CLEAN|CLEAN_SEALED)
        report_state=BODY_SEALED
        ;;
      DIVERTED)
        report_state=BODY_SEALED_AFTER_DIVERT
        echo "post-BODY-END overflow diverted; charged body preserved" >> "$log_file"
        ;;
      NO_MARKER)
        report_state=PARTIAL_NO_MARKER
        if [ "$body_end_contract" = DECLARED ] && [ "$rc" -eq 0 ]; then
          echo "report has no BODY-END under a declared contract; banked as partial" >> "$log_file"
          rc=7
        fi
        ;;
      MULTI_MARKER)
        report_state=AMBIGUOUS_MULTI_MARKER
        echo "report has multiple BODY-END markers; not repaired" >> "$log_file"
        [ "$rc" -ne 0 ] || rc=7
        ;;
      *)
        report_state=UNVERIFIED
        [ "$rc" -ne 0 ] || rc=7
        ;;
    esac
  else
    printf '%s\n' "$divert_out" >> "$log_file"
    seal_boundary=ERROR
    report_state=UNVERIFIED
    echo "seal boundary check failed; result is quarantined" >> "$log_file"
    [ "$rc" -ne 0 ] || rc=7
  fi
fi

charge_basis_status=NOT_CHECKED
if [ -s "$report_file" ]; then
  ready_charge_validator_sha=$(sha256_file "$charge_validator_snapshot") || ready_charge_validator_sha=ERROR
  if [ "$ready_charge_validator_sha" != "$charge_validator_sha" ]; then
    charge_basis_status=VALIDATOR_MUTATED
    echo "charge-basis validator snapshot changed; result is quarantined" >> "$log_file"
    [ "$rc" -ne 0 ] || rc=5
  elif charge_basis_result=$(python3 "$charge_validator_snapshot" "$report_file" 2>&1); then
    charge_basis_status=${charge_basis_result#charge_basis=}
  else
    charge_basis_status=INVALID
    echo "charge-basis validation failed; result is quarantined" >> "$log_file"
    echo "$charge_basis_result" >> "$log_file"
    [ "$rc" -ne 0 ] || rc=6
  fi
fi

post_prompt_sha=$(sha256_file "$prompt_file") || post_prompt_sha=ERROR
post_adapter_sha=$(sha256_file "$adapter_script") || post_adapter_sha=ERROR
post_launcher_sha=$(sha256_file "$script_dir/lane.sh") || post_launcher_sha=ERROR
post_sandbox_profile_sha=$(sha256_file "$sandbox_profile") || post_sandbox_profile_sha=ERROR
post_charge_validator_sha=$(sha256_file "$charge_validator") || post_charge_validator_sha=ERROR
post_charge_validator_snapshot_sha=$(sha256_file "$charge_validator_snapshot") || post_charge_validator_snapshot_sha=ERROR
post_seal_tool_sha=$(sha256_file "$seal_tool") || post_seal_tool_sha=ERROR
post_seal_tool_snapshot_sha=$(sha256_file "$seal_tool_snapshot") || post_seal_tool_snapshot_sha=ERROR
post_fallacy_sha=$(sha256_file "$fallacy_file") || post_fallacy_sha=ERROR
post_model_prompt_sha=$(sha256_file "$model_prompt_file") || post_model_prompt_sha=ERROR
if [ "$post_prompt_sha" != "$prompt_sha" ] || \
   [ "$post_adapter_sha" != "$adapter_sha" ] || \
   [ "$post_launcher_sha" != "$launcher_sha" ] || \
   [ "$post_sandbox_profile_sha" != "$sandbox_profile_sha" ] || \
   [ "$post_charge_validator_sha" != "$charge_validator_sha" ] || \
   [ "$post_charge_validator_snapshot_sha" != "$charge_validator_sha" ] || \
   [ "$post_seal_tool_sha" != "$seal_tool_sha" ] || \
   [ "$post_seal_tool_snapshot_sha" != "$seal_tool_sha" ] || \
   [ "$post_fallacy_sha" != "$fallacy_sha" ] || \
   [ "$post_model_prompt_sha" != "$model_prompt_sha" ]; then
  echo "hashed lane input changed during execution; result is quarantined" >> "$log_file"
  [ "$rc" -ne 0 ] || rc=5
fi

# Charged-input custody: a mutated snapshot quarantines the run; drift of the
# repo original is recorded but does not, because the model read frozen bytes.
if [ "$input_count" -gt 0 ]; then
  manifest_index=0
  while read -r manifest_rel manifest_base manifest_sha; do
    manifest_index=$((manifest_index + 1))
    post_snap_sha=$(sha256_file "$inputs_dir/$manifest_base") || post_snap_sha=ERROR
    post_src_sha=$(sha256_file "$repo_root/$manifest_rel") || post_src_sha=ERROR
    if [ "$post_snap_sha" != "$manifest_sha" ]; then
      input_state=SNAPSHOT_MUTATED
      echo "charged input snapshot changed during execution; result is quarantined: $manifest_rel" >> "$log_file"
      [ "$rc" -ne 0 ] || rc=5
    elif [ "$post_src_sha" != "$manifest_sha" ]; then
      input_state=REPO_DRIFT
    else
      input_state=UNCHANGED
    fi
    printf '%s %s\n' "$manifest_index" "$input_state" >> "$inputs_post_manifest"
  done < "$inputs_manifest"
fi

end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
{
  echo "end_utc=$end_utc"
  echo "exit_code=$rc"
  echo "post_prompt_sha256=$post_prompt_sha"
  echo "post_adapter_sha256=$post_adapter_sha"
  echo "post_launcher_sha256=$post_launcher_sha"
  echo "post_sandbox_profile_sha256=$post_sandbox_profile_sha"
  echo "post_charge_basis_validator_sha256=$post_charge_validator_sha"
  echo "post_charge_basis_validator_snapshot_sha256=$post_charge_validator_snapshot_sha"
  echo "post_seal_tool_sha256=$post_seal_tool_sha"
  echo "post_seal_tool_snapshot_sha256=$post_seal_tool_snapshot_sha"
  echo "post_fallacy_sha256=$post_fallacy_sha"
  echo "post_model_prompt_sha256=$post_model_prompt_sha"
  echo "charge_basis_status=$charge_basis_status"
  echo "seal_boundary=$seal_boundary"
  echo "report_state=$report_state"
  if [ "$input_count" -gt 0 ] && [ -f "$inputs_post_manifest" ]; then
    while read -r manifest_index input_state; do
      echo "charged_input_${manifest_index}_post=$input_state"
    done < "$inputs_post_manifest"
  fi
  if [ -s "$report_file" ]; then
    echo "report=$report_file"
    echo "report_sha256=$(sha256_file "$report_file" || echo ERROR)"
  else
    echo "report=MISSING"
  fi
  if [ -s "$raw_report_file" ]; then
    echo "raw_report=$raw_report_file"
    echo "raw_report_sha256=$(sha256_file "$raw_report_file" || echo ERROR)"
  fi
  if [ -s "$overflow_file" ]; then
    echo "overflow=$overflow_file"
    echo "overflow_sha256=$(sha256_file "$overflow_file" || echo ERROR)"
  fi
  echo "log=$log_file"
  echo "log_sha256=$(sha256_file "$log_file" || echo ERROR)"
  if [ -n "$caught_signal" ]; then
    echo "final_status=CANCELLED"
  elif [ "$rc" -eq 0 ]; then
    echo "final_status=DONE"
  else
    echo "final_status=FAILED"
  fi
} >> "$run_file"

echo "$tag done rc=$rc start=$start_utc end=$end_utc" >> pilot-local.log
exit "$rc"
}

# Parsing the complete function before execution makes an already-running
# lane immune to later atomic rewrites of this launcher.
main "$@"
