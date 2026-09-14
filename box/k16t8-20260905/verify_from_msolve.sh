#!/bin/bash
# After msolve -P 1 finishes: extract F_p-points and emit a verifypoint job.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
PARAM=${1:?param file}
OUTDIR=${2:-$HERE}
python3 "$HERE/msolve_point.py" "$PARAM" > "$OUTDIR/msolve_points.txt" 2>"$OUTDIR/msolve_points.err"
echo "extracted points:" 
cat "$OUTDIR/msolve_points.txt"
# first ROOT line
line=$(grep -m1 '^ROOT' "$OUTDIR/msolve_points.txt" || true)
if [ -z "$line" ]; then
  echo "NO_FP_ROOT"
  exit 2
fi
# ROOT a COORDS q2 q3 q4 q5 q6 q7 b3   (CI system vars)
# verifypoint wants b4,q2,q3,q4,q5,q6,q7  (no b3)
python3 - <<PY
import re, pathlib, subprocess, sys
line=open("$OUTDIR/msolve_points.txt").read().splitlines()
root=None
for ln in line:
    if ln.startswith("ROOT"):
        root=ln; break
assert root, "no ROOT"
parts=root.split()
# ROOT <a> COORDS <c1> <c2> ...
i=parts.index("COORDS")
coords=list(map(int, parts[i+1:]))
print("ncoords", len(coords), coords)
# CI: q2,q3,q4,q5,q6,q7,b3
assert len(coords) in (6,7)
qs=coords[:6]
point="1," + ",".join(str(c) for c in qs)
print("POINT", point)
pathlib.Path("$OUTDIR/affine_point.txt").write_text(point+"\n")
PY
POINT=$(cat "$OUTDIR/affine_point.txt")
python3 "$HERE/gen.py" 8 --mode mod --prime 32003 --branch 0 --job verifypoint --point "$POINT" --outdir "$OUTDIR"
# gen.py prints the path
echo "emitted verifypoint for $POINT"
# run it
cd "$OUTDIR"
./run.sh verifypoint_t8_mod_p32003_b0.sing 180
cat verifypoint_t8_mod_p32003_b0.out
cat verifypoint_t8_mod_p32003_b0.time
