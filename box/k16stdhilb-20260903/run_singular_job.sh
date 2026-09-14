#!/usr/bin/env bash
set -u

if [ "$#" -ne 1 ]; then
  printf 'usage: %s JOB.sing\n' "$0" >&2
  exit 64
fi

job="$1"
case "$job" in
  *.sing) ;;
  *) printf 'job must end in .sing: %s\n' "$job" >&2; exit 64 ;;
esac

out="${job%.sing}.out"
err="${job%.sing}.err"
resource="${job%.sing}.resource"

export OMP_NUM_THREADS=4
export OPENBLAS_NUM_THREADS=4
export MKL_NUM_THREADS=4
export VECLIB_MAXIMUM_THREADS=4
export NUMEXPR_NUM_THREADS=4

/usr/bin/time -f 'wall=%e maxrss_kb=%M exit=%x' -o "$resource" \
  timeout 3000 bash -c 'ulimit -v 25165824; exec Singular --cpus=4 --threads=4 --flint-threads=4 -q "$1"' _ "$job" \
  >"$out" 2>"$err"
rc=$?
printf 'runner_exit=%s\n' "$rc" >> "$resource"
exit "$rc"
