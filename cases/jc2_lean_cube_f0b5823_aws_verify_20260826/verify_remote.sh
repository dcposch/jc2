#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "REFUSE: AWS/Linux only" >&2
  exit 64
fi

dmi="$(cat /sys/devices/virtual/dmi/id/sys_vendor 2>/dev/null || true)"
if [[ "$dmi" != *Amazon* ]]; then
  echo "REFUSE: host is not Amazon EC2 (DMI=$dmi)" >&2
  exit 64
fi

if [[ $# -ne 5 ]]; then
  echo "usage: verify_remote.sh SOURCE_ROOT OUT_DIR ARCHIVE_SHA SOLUTION_SHA COMMIT" >&2
  exit 64
fi

source_root=$1
out_dir=$2
expected_archive_sha=$3
expected_solution_sha=$4
expected_commit=$5

: "${JC2_AWS_JOB_TAG:?REFUSE: JC2_AWS_JOB_TAG is required}"
: "${JC2_SOURCE_ARCHIVE:?REFUSE: JC2_SOURCE_ARCHIVE is required}"

mkdir -p "$out_dir"
exec > >(tee "$out_dir/verify.stdout") 2> >(tee "$out_dir/verify.stderr" >&2)

echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname)"
echo "dmi=$dmi"
echo "uname=$(uname -a)"
echo "job_tag=$JC2_AWS_JOB_TAG"
echo "expected_commit=$expected_commit"

actual_archive_sha="$(sha256sum "$JC2_SOURCE_ARCHIVE" | awk '{print $1}')"
echo "archive_sha256=$actual_archive_sha"
[[ "$actual_archive_sha" == "$expected_archive_sha" ]]

project="$source_root/gcd3-69-cube"
actual_solution_sha="$(sha256sum "$project/Solution.lean" | awk '{print $1}')"
echo "solution_sha256=$actual_solution_sha"
[[ "$actual_solution_sha" == "$expected_solution_sha" ]]

cd "$project"
echo "lake=$(lake --version)"
echo "lean=$(lake env lean --version)"
sha256sum lean-toolchain lakefile.toml lake-manifest.json Solution.lean

export LEAN_NUM_THREADS=4
echo "lean_jobs=$LEAN_NUM_THREADS"

lake exe cache get
lake build
lake env lean Solution.lean > "$out_dir/axioms.stdout" 2> "$out_dir/axioms.stderr"

for theorem_name in \
  GCD369CubeConstantPoleDegreeLandingEmpty \
  GCD369CubeEarlyBoundaryDataEmpty \
  GCD369CubeRhoFourFirstLoadImpossible \
  GCD369CubeTerminalOnlyQuadraticImpossible \
  GCD369CubeDoubleRootNormalObstruction \
  GCD369CubeZeroSheetTerminalExclusion \
  GCD369CubeMixedEllipticTerminalExclusion \
  GCD369CubeUnmixedEllipticTerminalExclusion \
  GCD369CubeMixedCuspAllCoreTerminalExclusion \
  GCD369CubeDSAllCoreTerminalExclusion \
  GCD369CubeTrajectoryLandingEmpty; do
  grep -F "'$theorem_name' depends on axioms:" "$out_dir/axioms.stdout" >/dev/null
done

if grep -F "sorryAx" "$out_dir/axioms.stdout" "$out_dir/axioms.stderr" >/dev/null; then
  echo "REFUSE: audited declaration depends on sorryAx" >&2
  exit 65
fi

echo "axioms_stdout_sha256=$(sha256sum "$out_dir/axioms.stdout" | awk '{print $1}')"
echo "axioms_stderr_sha256=$(sha256sum "$out_dir/axioms.stderr" | awk '{print $1}')"
echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "VERDICT=PASS_BUILD_AND_NO_SORRYAX"
