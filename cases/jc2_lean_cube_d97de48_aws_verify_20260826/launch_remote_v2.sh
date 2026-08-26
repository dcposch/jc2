#!/usr/bin/env bash
set -euo pipefail

job_root=${1:?job root required}
tag=${2:?registered tag required}

expected_archive_sha=40fd09da952ae3d0aca5e8fb53497fd3aa3e259fd3d0a16cb1af3a6c53785c46
expected_solution_sha=dabf4b5b356f637650dfcda293567ee9b1fe382d3e18e06bf45a25a869c9604d
expected_commit=d97de48d83cabdb094c708540dcfe0d00f9a0957

cd "$job_root"
actual_archive_sha="$(sha256sum source.tar.gz | awk '{print $1}')"
actual_verifier_sha="$(sha256sum verify_remote_v2.sh | awk '{print $1}')"
actual_wrapper_sha="$(sha256sum run_with_rc_v2.sh | awk '{print $1}')"
[[ "$actual_archive_sha" == "$expected_archive_sha" ]]

mkdir source output
tar xzf source.tar.gz -C source
chmod 755 verify_remote_v2.sh run_with_rc_v2.sh

{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "source_archive_sha256=$actual_archive_sha"
  echo "verifier_sha256=$actual_verifier_sha"
  echo "wrapper_sha256=$actual_wrapper_sha"
  echo "solution_sha256=$expected_solution_sha"
  echo "nested_commit=$expected_commit"
  echo "timeout_seconds=1800"
  echo "lean_jobs=4"
} > launch.meta

nohup "$job_root/run_with_rc_v2.sh" \
  "$job_root" "$tag" "$job_root/source/jc2-lean" "$job_root/output" \
  "$expected_archive_sha" "$expected_solution_sha" "$expected_commit" \
  > launcher.stdout 2> launcher.stderr < /dev/null &

echo $! > launcher.pid
echo "launcher_pid=$(cat launcher.pid)"
