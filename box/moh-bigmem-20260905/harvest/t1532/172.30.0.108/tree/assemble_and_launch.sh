#!/usr/bin/env bash
# Assemble payload on math-hq and detach jobs on the eight workers we launched.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
SC="$REPO/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete"
CHARTS="$REPO/box/moh14-charts-20260905"
OFFICIAL="$CHARTS/tools/msolve-0.10.1-official-intel-avx512/msolve"
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
export PATH="/usr/bin:$PATH"

echo "ASSEMBLE_START utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p "$HERE/bin" "$HERE/targets"
cp -f "$OFFICIAL" "$HERE/bin/msolve"
chmod +x "$HERE/bin/msolve" "$HERE"/*.sh "$HERE"/*.py
cp -f "$CHARTS/msolve_chart.py" "$HERE/msolve_chart.py"
cp -f "$REPO/box/lib/guided_gb.py" "$HERE/guided_gb.py"
sha256sum "$HERE/bin/msolve"

# --- targets ---
# m12: 425-gen union chart (source-complete executable body identical)
mkdir -p "$HERE/targets/m12_union"
ln -f "$CHARTS/classes/C_n24m16_Mm12_m2_5_ell1_s4/rows/C_n24m16_Mm12_m2_5_ell1_s4_union_rows.tsv" \
  "$HERE/targets/m12_union/rows.tsv"
cp -f "$SC/classes/C_n24m16_Mm12_m2_5_ell1_s4/meta/C_n24m16_Mm12_m2_5_ell1_s4_union.json" \
  "$HERE/targets/m12_union/meta.json"
cat > "$HERE/targets/m12_union/env.sh" <<'EOF'
NATIVE_META="$ROOT/targets/m12_union/meta.json"
NATIVE_ROWS="$ROOT/targets/m12_union/rows.tsv"
GRAPH_META=""
GRAPH_ROWS=""
EOF

# v38 native + circuit
mkdir -p "$HERE/targets/v38"
ln -f "$SC/classes/C_n18m12_M2_9_ell2_s3/rows/C_n18m12_M2_9_ell2_s3_V3_8_rows.tsv" \
  "$HERE/targets/v38/native_rows.tsv"
cp -f "$SC/classes/C_n18m12_M2_9_ell2_s3/meta/C_n18m12_M2_9_ell2_s3_V3_8.json" \
  "$HERE/targets/v38/native_meta.json"
ln -f "$SC/circuit/C_n18m12_M2_9_ell2_s3/rows/C_n18m12_M2_9_ell2_s3_V3_8_circuit_rows.tsv" \
  "$HERE/targets/v38/graph_rows.tsv"
cp -f "$SC/circuit/C_n18m12_M2_9_ell2_s3/meta/C_n18m12_M2_9_ell2_s3_V3_8_circuit.json" \
  "$HERE/targets/v38/graph_meta.json"
cat > "$HERE/targets/v38/env.sh" <<'EOF'
NATIVE_META="$ROOT/targets/v38/native_meta.json"
NATIVE_ROWS="$ROOT/targets/v38/native_rows.tsv"
GRAPH_META="$ROOT/targets/v38/graph_meta.json"
GRAPH_ROWS="$ROOT/targets/v38/graph_rows.tsv"
EOF

# m15 native + circuit
mkdir -p "$HERE/targets/m15"
ln -f "$SC/classes/C_n24m18_Mm15_14_ell1_s3/rows/C_n24m18_Mm15_14_ell1_s3_V1_9_rows.tsv" \
  "$HERE/targets/m15/native_rows.tsv"
cp -f "$SC/classes/C_n24m18_Mm15_14_ell1_s3/meta/C_n24m18_Mm15_14_ell1_s3_V1_9.json" \
  "$HERE/targets/m15/native_meta.json"
ln -f "$SC/circuit/C_n24m18_Mm15_14_ell1_s3/rows/C_n24m18_Mm15_14_ell1_s3_V1_9_circuit_rows.tsv" \
  "$HERE/targets/m15/graph_rows.tsv"
cp -f "$SC/circuit/C_n24m18_Mm15_14_ell1_s3/meta/C_n24m18_Mm15_14_ell1_s3_V1_9_circuit.json" \
  "$HERE/targets/m15/graph_meta.json"
cat > "$HERE/targets/m15/env.sh" <<'EOF'
NATIVE_META="$ROOT/targets/m15/native_meta.json"
NATIVE_ROWS="$ROOT/targets/m15/native_rows.tsv"
GRAPH_META="$ROOT/targets/m15/graph_meta.json"
GRAPH_ROWS="$ROOT/targets/m15/graph_rows.tsv"
EOF

# v18: circuit now; native extracted on the msolve worker
mkdir -p "$HERE/targets/v18/classdir/builders" "$HERE/targets/v18/classdir/rows"
cp -f "$SC/classes/C_n18m12_M2_9_ell2_s3/builders/C_n18m12_M2_9_ell2_s3_V1_8_builder.sing" \
  "$HERE/targets/v18/classdir/builders/"
cp -f "$SC/classes/C_n18m12_M2_9_ell2_s3/meta/C_n18m12_M2_9_ell2_s3_V1_8.json" \
  "$HERE/targets/v18/native_meta.json"
ln -f "$SC/circuit/C_n18m12_M2_9_ell2_s3/rows/C_n18m12_M2_9_ell2_s3_V1_8_circuit_rows.tsv" \
  "$HERE/targets/v18/graph_rows.tsv"
cp -f "$SC/circuit/C_n18m12_M2_9_ell2_s3/meta/C_n18m12_M2_9_ell2_s3_V1_8_circuit.json" \
  "$HERE/targets/v18/graph_meta.json"
cat > "$HERE/targets/v18/env.sh" <<'EOF'
NATIVE_META="$ROOT/targets/v18/native_meta.json"
NATIVE_ROWS=""
GRAPH_META="$ROOT/targets/v18/graph_meta.json"
GRAPH_ROWS="$ROOT/targets/v18/graph_rows.tsv"
EOF

# custody snapshot
{
  echo "# moh-bigmem payload $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  sha256sum "$HERE/bin/msolve" "$HERE/msolve_chart.py" "$HERE/guided_gb.py" \
    "$HERE/run_msolve_job.sh" "$HERE/run_guided_job.py"
  sha256sum "$HERE/targets/m12_union/rows.tsv" "$HERE/targets/m12_union/meta.json"
  sha256sum "$HERE/targets/v38/native_rows.tsv" "$HERE/targets/v38/graph_rows.tsv"
  sha256sum "$HERE/targets/m15/native_rows.tsv" "$HERE/targets/m15/graph_rows.tsv"
  sha256sum "$HERE/targets/v18/graph_rows.tsv"
} > "$HERE/payload.sha256"
cat "$HERE/payload.sha256"

push_one() {
  local ip=$1
  ssh $SSHO ubuntu@$ip "mkdir -p ~/moh-bigmem-20260905"
  rsync -az --delete -e "ssh $SSHO" \
    --exclude 'targets/*/msolve_*' --exclude 'targets/*/guided' --exclude 'targets/*/exactq_*' \
    --exclude 'targets/*/classdir/extract' --exclude 'targets/*/classdir/rows/*.tsv' \
    "$HERE/" ubuntu@$ip:~/moh-bigmem-20260905/
  ssh $SSHO ubuntu@$ip "chmod +x ~/moh-bigmem-20260905/*.sh ~/moh-bigmem-20260905/bin/msolve; ~/moh-bigmem-20260905/bin/msolve -V; command -v /usr/bin/time; command -v Singular"
}

launch_detached() {
  local ip=$1
  local log=$2
  local inner=$3
  ssh $SSHO ubuntu@$ip "cd \$HOME/moh-bigmem-20260905 && setsid bash -c 'export ROOT=\$HOME/moh-bigmem-20260905; cd \$ROOT; stdbuf -oL bash $inner > \$HOME/$log 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED $log pid=\$!"
}

echo "PUSH_START utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
for ip in 172.30.0.183 172.30.0.202 172.30.0.108 172.30.0.190 \
          172.30.0.121 172.30.0.55 172.30.0.45 172.30.0.125; do
  echo "=== push $ip ==="
  push_one "$ip" &
done
wait
echo "PUSH_DONE utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "LAUNCH_START"
# msolve r7i.24xlarge
launch_detached 172.30.0.183 m12_union.msolve.log 'run_msolve_pipeline.sh m12_union'
launch_detached 172.30.0.202 v38.msolve.log 'run_msolve_pipeline.sh v38'
launch_detached 172.30.0.108 m15.msolve.log 'run_msolve_pipeline.sh m15'
launch_detached 172.30.0.190 v18.msolve.log 'run_v18_msolve.sh'
# singular x2idn.16xlarge
launch_detached 172.30.0.121 m12_union.guided.log 'run_guided_pipeline.sh m12_union'
launch_detached 172.30.0.55 v38.guided.log 'run_guided_pipeline.sh v38'
launch_detached 172.30.0.45 m15.guided.log 'run_guided_pipeline.sh m15'
launch_detached 172.30.0.125 v18.guided.log 'run_guided_pipeline.sh v18'

echo "LAUNCH_DONE utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
for ip in 172.30.0.183 172.30.0.202 172.30.0.108 172.30.0.190 \
          172.30.0.121 172.30.0.55 172.30.0.45 172.30.0.125; do
  echo -n "$ip procs: "
  ssh $SSHO ubuntu@$ip 'pgrep -a msolve || true; pgrep -a Singular || true; ls -l $HOME/*.log 2>/dev/null | tail -5'
done
