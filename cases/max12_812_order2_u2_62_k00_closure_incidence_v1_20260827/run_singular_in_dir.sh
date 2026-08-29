#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: run_singular_in_dir.sh ARTIFACT_DIR INPUT" >&2
  exit 125
fi

artifact_dir=$1
input=$2
mkdir -p "$artifact_dir"
cd "$artifact_dir"
exec Singular -q "$input"
