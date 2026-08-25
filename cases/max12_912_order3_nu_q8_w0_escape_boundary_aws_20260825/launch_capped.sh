#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "usage: launch_capped.sh VM_KIB REPO OUT TAG GENERATOR_ARGS..." >&2
  exit 64
fi

vm_kib=$1
repo=$2
outroot=$3
tag=$4
shift 4
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_escape_boundary_aws_20260825"

ulimit -v "$vm_kib"
set +e
"$case_dir/run_remote.sh" "$repo" "$outroot" "$tag" "$@"
rc=$?
set -e

if [[ -d "$outroot/$tag" ]]; then
  {
    echo "launcher_virtual_memory_limit_kib=$vm_kib"
    sha256sum "$case_dir/launch_capped.sh"
  } >> "$outroot/$tag/run.meta"
fi
exit "$rc"
