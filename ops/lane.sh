#!/bin/sh
# Generic research-lane runner.
# Usage: ops/lane.sh <adapter> <unique-tag> <promptfile>
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
[ -x "$adapter_script" ] || {
  echo "unknown adapter: $adapter" >&2
  exit 2
}
[ -f "$prompt_file" ] || {
  echo "prompt file not found: $prompt_file" >&2
  exit 2
}

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

sha256_stdin() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha_line=$(sha256sum) || return 1
  elif command -v shasum >/dev/null 2>&1; then
    sha_line=$(shasum -a 256) || return 1
  else
    echo "no SHA-256 tool available" >&2
    return 1
  fi
  sha_value=${sha_line%% *}
  [ -n "$sha_value" ] || return 1
  printf '%s\n' "$sha_value"
}

for existing in "xmodel/$tag.log" "xmodel/$tag.md" "xmodel/$tag.run"; do
  if [ -e "$existing" ]; then
    echo "duplicate tag refused; choose a new attempt tag: $tag ($existing exists)" >&2
    exit 3
  fi
done

lock_dir=.lane-locks/$tag
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "tag is already live: $tag" >&2
  exit 3
fi
cleanup() { rmdir "$lock_dir" 2>/dev/null || true; }
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

log_file=xmodel/$tag.log
run_file=xmodel/$tag.run
report_file=xmodel/$tag.md
start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
prompt_sha=$(sha256_file "$prompt_file") || exit 2
adapter_sha=$(sha256_file "$adapter_script") || exit 2
basis=$(git rev-parse HEAD 2>/dev/null || echo UNKNOWN)
pre_status=$(git status --porcelain=v1 --untracked-files=all) || exit 2
pre_status_sha=$(printf '%s\n' "$pre_status" | sha256_stdin) || exit 2
pre_diff_sha=$(git diff --binary HEAD | sha256_stdin) || exit 2
pre_untracked_sha=$(
  git ls-files --others --exclude-standard |
    while IFS= read -r untracked_path; do
      printf '%s ' "$untracked_path"
      sha256_file "$untracked_path" || exit 1
    done |
    sha256_stdin
) || exit 2

{
  echo "tag=$tag"
  echo "adapter=$adapter"
  echo "pid=$$"
  echo "host=$(hostname)"
  echo "basis=$basis"
  echo "prompt=$prompt_file"
  echo "prompt_sha256=$prompt_sha"
  echo "adapter_sha256=$adapter_sha"
  echo "start_utc=$start_utc"
  echo "pre_status_sha256=$pre_status_sha"
  echo "pre_diff_sha256=$pre_diff_sha"
  echo "pre_untracked_sha256=$pre_untracked_sha"
  if [ -n "$pre_status" ]; then
    printf '%s\n' "$pre_status" | sed 's/^/pre_porcelain=/'
  else
    echo "pre_porcelain=CLEAN"
  fi
  echo "initial_status=RUNNING"
} > "$run_file"

sh "$adapter_script" "$prompt_file" > "$log_file" 2>&1 &
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

post_prompt_sha=$(sha256_file "$prompt_file") || post_prompt_sha=ERROR
post_adapter_sha=$(sha256_file "$adapter_script") || post_adapter_sha=ERROR
if [ "$post_prompt_sha" != "$prompt_sha" ] || [ "$post_adapter_sha" != "$adapter_sha" ]; then
  echo "hashed lane input changed during execution; result is quarantined" >> "$log_file"
  [ "$rc" -ne 0 ] || rc=5
fi

end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
post_status=$(git status --porcelain=v1 --untracked-files=all) || post_status=ERROR
post_status_sha=$(printf '%s\n' "$post_status" | sha256_stdin) || post_status_sha=ERROR
{
  echo "end_utc=$end_utc"
  echo "exit_code=$rc"
  echo "post_prompt_sha256=$post_prompt_sha"
  echo "post_adapter_sha256=$post_adapter_sha"
  echo "post_status_sha256=$post_status_sha"
  if [ -n "$post_status" ]; then
    printf '%s\n' "$post_status" | sed 's/^/post_porcelain=/'
  else
    echo "post_porcelain=CLEAN"
  fi
  if [ -s "$report_file" ]; then
    echo "report=$report_file"
    echo "report_sha256=$(sha256_file "$report_file" || echo ERROR)"
  else
    echo "report=MISSING"
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
