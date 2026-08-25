#!/usr/bin/env bash
set -euo pipefail

# Run campaign Lean verification only on a Linux/AWS worker.  Usage:
#   aws_lean_verify.sh REPO_ROOT OUT_DIR PROJECT [PROJECT ...]

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "REFUSE: campaign Lean verification is AWS/Linux-only" >&2
  exit 64
fi

if [[ $# -lt 3 ]]; then
  echo "usage: $0 REPO_ROOT OUT_DIR PROJECT [PROJECT ...]" >&2
  exit 64
fi

repo_root=$1
out_dir=$2
shift 2

command -v lake >/dev/null 2>&1 || {
  echo "REFUSE: lake is not installed on this AWS worker" >&2
  exit 69
}

lean_jobs=${AWS_LEAN_JOBS:-8}
if ! [[ "$lean_jobs" =~ ^[1-9][0-9]*$ ]]; then
  echo "REFUSE: AWS_LEAN_JOBS must be a positive integer" >&2
  exit 64
fi
export LEAN_NUM_THREADS=$lean_jobs

mkdir -p "$out_dir"
exec > >(tee "$out_dir/verify.stdout") 2> >(tee "$out_dir/verify.stderr" >&2)

echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname)"
echo "uname=$(uname -a)"
echo "lake=$(command -v lake)"
echo "lake_jobs=$lean_jobs"

for project in "$@"; do
  project_dir="$repo_root/$project"
  test -f "$project_dir/lakefile.toml"
  test -f "$project_dir/lean-toolchain"
  echo "project=$project"
  (
    cd "$project_dir"
    lake --version
    sha256sum lean-toolchain lakefile.toml lake-manifest.json Challenge.lean Solution.lean
    lake exe cache get
    lake build
    bash scripts/check_axioms.sh
  )
done

echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "VERDICT=PASS"
