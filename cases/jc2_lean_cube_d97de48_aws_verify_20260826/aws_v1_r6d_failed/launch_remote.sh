#!/usr/bin/env bash
set -euo pipefail

job_root=${1:?job root required}
tag=${2:?registered tag required}

expected_archive_sha=40fd09da952ae3d0aca5e8fb53497fd3aa3e259fd3d0a16cb1af3a6c53785c46
expected_verifier_sha=ef2774e789fc4bc15a23951f72a89d725a6f0ea4392a21655dec6a7d7476852a
expected_solution_sha=dabf4b5b356f637650dfcda293567ee9b1fe382d3e18e06bf45a25a869c9604d
expected_commit=d97de48d83cabdb094c708540dcfe0d00f9a0957

cd "$job_root"
[[ "$(sha256sum source.tar.gz | awk '{print $1}')" == "$expected_archive_sha" ]]
[[ "$(sha256sum verify_remote.sh | awk '{print $1}')" == "$expected_verifier_sha" ]]

mkdir source output
tar xzf source.tar.gz -C source
chmod 755 verify_remote.sh

{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "source_archive_sha256=$expected_archive_sha"
  echo "verifier_sha256=$expected_verifier_sha"
  echo "solution_sha256=$expected_solution_sha"
  echo "nested_commit=$expected_commit"
  echo "timeout_seconds=1800"
  echo "lean_jobs=4"
} > launch.meta

nohup env \
  JC2_AWS_JOB_TAG="$tag" \
  JC2_SOURCE_ARCHIVE="$job_root/source.tar.gz" \
  AWS_LEAN_JOBS=4 \
  timeout --signal=TERM --kill-after=60 1800 \
  "$job_root/verify_remote.sh" \
    "$job_root/source/jc2-lean" \
    "$job_root/output" \
    "$expected_archive_sha" \
    "$expected_solution_sha" \
    "$expected_commit" \
  > launcher.stdout 2> launcher.stderr < /dev/null &

echo $! > launcher.pid
echo "launcher_pid=$(cat launcher.pid)"
