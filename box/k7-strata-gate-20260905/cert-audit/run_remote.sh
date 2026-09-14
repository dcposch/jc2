#!/usr/bin/env bash
set -u

kind=$1
stem=$2
base=/home/ubuntu/jc2/box/k7-strata-gate-20260905
results=$base/cert-audit/results
input=$base/chart-audit/emitted/${stem}_p0.ms
mkdir -p "$results"

case "$kind" in
  msolve101)
    command=(/home/ubuntu/msolve-0.10.1-gate -g 2 -t 8 -f "$input" -o "$results/${stem}_msolve101.out")
    ;;
  msolve065)
    command=(/usr/bin/msolve -g 2 -t 8 -f "$input" -o "$results/${stem}_msolve065.out")
    ;;
  singular)
    command=(Singular --no-rc -q "$results/${stem}_std.sing")
    ;;
  lift)
    command=(Singular --no-rc -q "$base/cert-audit/lifts/${stem}_lift.sing")
    ;;
  loclift)
    command=(Singular --no-rc -q "$base/cert-audit/lifts/${stem}_loclift.sing")
    ;;
  directlift)
    command=(Singular --no-rc -q "$base/cert-audit/lifts/${stem}_directlift.sing")
    ;;
  subsetlift)
    command=(Singular --no-rc -q "$base/cert-audit/lifts/${stem}_subset_lift.sing")
    ;;
  *)
    echo "unknown kind: $kind" >&2
    exit 2
    ;;
esac

timeout --signal=TERM --kill-after=20s 2400s \
  /usr/bin/time -v -o "$results/${stem}_${kind}.time" \
  "${command[@]}" \
  >"$results/${stem}_${kind}.stdout" \
  2>"$results/${stem}_${kind}.err"
rc=$?
printf '%s\n' "$rc" >"$results/${stem}_${kind}.rc"
