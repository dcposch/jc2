#!/bin/bash
# Tiny replay of the producer checker from an own scratch copy; caps per child.
S="$1"; OUT="$2"; PY=/usr/bin/python3
: > "$OUT/replay-individual.tsv"
printf 'optimized\tmutation\trc\tstdout_sha256\tstderr_sha256\tmarker\twall_s\n' >> "$OUT/replay-individual.tsv"
for opt in "" "-O"; do
  for mut in "" --change-hyperbola --change-CRT-sign --change-nilpotent-algebra --omit-gamma-shear --change-unit-root; do
    tag="${opt:-normal}${mut:+_}${mut}"; tag="${tag//--/}"
    t0=$(date +%s.%N)
    ( ulimit -t 25; ulimit -v 524288; timeout 30 $PY -I -B $opt "$S/check.py" $mut > "$OUT/out_${tag}.txt" 2> "$OUT/err_${tag}.txt" ); rc=$?
    t1=$(date +%s.%N)
    so=$(sha256sum "$OUT/out_${tag}.txt" | cut -c1-64); se=$(sha256sum "$OUT/err_${tag}.txt" | cut -c1-64)
    mk=$(grep -o 'ValueError: .*' "$OUT/err_${tag}.txt" | head -1)
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%.3f\n' "${opt:-normal}" "${mut:-positive}" "$rc" "$so" "$se" "$mk" "$(echo "$t1 - $t0" | bc)" >> "$OUT/replay-individual.tsv"
  done
done
cat "$OUT/replay-individual.tsv"
