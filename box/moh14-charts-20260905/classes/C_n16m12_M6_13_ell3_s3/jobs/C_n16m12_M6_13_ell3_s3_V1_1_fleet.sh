#!/bin/bash
# Fleet job for class C_n16m12_M6_13_ell3_s3 stem C_n16m12_M6_13_ell3_s3_V1_1
# parameter_count=333
# chart=sprime3_necessary_D1_freelead_Bsafe
# Stage 1 extracts Jacobian coefficient generators (do this anywhere).
# Stage 2 is the exact-Q standard basis (fleet; do NOT run the big std
# on a laptop).  guided_gb markers: GG__UNIT / GG__DIM.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
SINGULAR="${SINGULAR:-Singular}"
echo "FLEET_START class=C_n16m12_M6_13_ell3_s3 stem=C_n16m12_M6_13_ell3_s3_V1_1 unknowns=333"
"$SINGULAR" --cpus=1 --threads=1 --flint-threads=1 -q --no-rc \
    "builders/C_n16m12_M6_13_ell3_s3_V1_1_builder.sing"
python3 "/home/ubuntu/jc2/box/moh14-charts-20260905/sprime3_compiler.py" emit-guided --dest "$HERE" --stem "C_n16m12_M6_13_ell3_s3_V1_1"
echo "FLEET_STAGE2 guided job at jobs/C_n16m12_M6_13_ell3_s3_V1_1_Q_guided.sing"
echo "FLEET_HINT timeout 3600 $SINGULAR --cpus=1 --threads=1 --flint-threads=1 -q --no-rc jobs/C_n16m12_M6_13_ell3_s3_V1_1_Q_guided.sing"
