#!/bin/bash
# Fleet job for class C_n36m24_Mm18_3_5_ell1_s4_V3_18_9 stem C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9
# parameter_count=100
# chart=sprime3_necessary_D1_freelead_Bsafe
# Stage 1 extracts Jacobian coefficient generators (do this anywhere).
# Stage 2 is the exact-Q standard basis (fleet; do NOT run the big std
# on a laptop).  guided_gb markers: GG__UNIT / GG__DIM.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
SINGULAR="${SINGULAR:-Singular}"
echo "FLEET_START class=C_n36m24_Mm18_3_5_ell1_s4_V3_18_9 stem=C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9 unknowns=100"
"$SINGULAR" --cpus=1 --threads=1 --flint-threads=1 -q --no-rc \
    "builders/C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9_builder.sing"
python3 "/home/ubuntu/jc2/box/moh14-charts-20260905/sprime3_compiler.py" --mode emit-guided --dest "$HERE" --stem "C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9"
echo "FLEET_STAGE2 guided job at jobs/C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9_Q_guided.sing"
echo "FLEET_HINT timeout 3600 $SINGULAR --cpus=1 --threads=1 --flint-threads=1 -q --no-rc jobs/C_n36m24_Mm18_3_5_ell1_s4_V3_18_9_V3_18_9_Q_guided.sing"
