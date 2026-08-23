#!/bin/bash
# Bootstrap an Ubuntu box for the jc72108 campaign.
#   Local:  scp setup_remote.sh <host>: && ssh <host> bash setup_remote.sh
#   Deploy: rsync -av systems/ <host>:jc72108/systems/
#   Run:    ssh <host> 'cd jc72108 && nohup ./run_probes_remote.sh > probes.log 2>&1 &'
set -euo pipefail
sudo apt-get update -qq
sudo apt-get install -y -qq build-essential autoconf automake libtool git \
    libgmp-dev libmpfr-dev libflint-dev python3 rsync htop time
if ! command -v msolve >/dev/null; then
  git clone --depth 1 https://github.com/algebraic-solving/msolve.git
  cd msolve && ./autogen.sh && ./configure && make -j"$(nproc)" && sudo make install
  cd ..
fi
mkdir -p jc72108/{systems,runs}
cat > jc72108/run_probes_remote.sh <<'RUNNER'
#!/bin/bash
# Run every .ms system in systems/ that has no output yet, smallest first.
# Per-process memory ceiling via ulimit (default 1200 GB), full thread count.
set -u
MEMGB=${MEMGB:-1200}
T=${T:-$(nproc)}
MSOLVE_SEED=${MSOLVE_SEED:-0}
cd "$(dirname "$0")"
MSOLVE_BIN=$(command -v msolve)
MSOLVE_VERSION=$(msolve --version 2>&1 | head -n 1)
ulimit -v $((MEMGB * 1024 * 1024))
for f in $(ls -S -r systems/*.ms); do
  base=$(basename "$f" .ms)
  o="runs/${base}.out"
  timefile="runs/${base}.time"
  meta="runs/${base}.meta"
  [ -s "$o" ] && continue
  echo "=== $base start $(date -u +%H:%M:%S) size=$(wc -c < "$f")"
  char=$(sed -n '2p' "$f" | tr -d '[:space:]')
  {
    echo "utc_start=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "host=$(hostname)"
    echo "msolve_bin=$MSOLVE_BIN"
    echo "msolve_version=$MSOLVE_VERSION"
    echo "input=$f"
    echo "input_characteristic=$char"
    echo "input_sha256=$(sha256sum "$f" | awk '{print $1}')"
    echo "random_seed=$MSOLVE_SEED"
    echo "command=msolve -v 2 -g 2 --random-seed $MSOLVE_SEED -t $T -f $f -o $o"
  } > "$meta"
  /usr/bin/time -v msolve -v 2 -g 2 --random-seed "$MSOLVE_SEED" -t "$T" -f "$f" -o "$o" 2> "$timefile"
  status=$?
  grep -i 'initial prime' "$timefile" >> "$meta" || true
  echo "utc_end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$meta"
  echo "exit_status=$status" >> "$meta"
  [ -s "$o" ] && echo "output_sha256=$(sha256sum "$o" | awk '{print $1}')" >> "$meta"
  if [ "$status" -ne 0 ]; then
    echo "=== $base FAILED (see $timefile)"
  elif grep -qx '\[1\]:' "$o"; then
    if [ "$char" = 0 ]; then
      echo "=== $base FIRST-PRIME-EMPTY (NOT Q-EMPTY)"
    else
      echo "=== $base EMPTY over F_$char (GB=[1])"
    fi
  elif [ "$char" = 0 ]; then
    if grep -q '^#length of basis:' "$o" && grep -q '^\[' "$o" && grep -q '\]:$' "$o"; then
      echo "=== $base NONEMPTY over Qbar (reconstructed Q basis; engine-trusted)"
    else
      echo "=== $base NO-VERDICT (no complete basis body emitted)"
    fi
  else
    echo "=== $base NONEMPTY-OR-OTHER over F_$char"
  fi
done
echo "ALL DONE"
RUNNER
chmod +x jc72108/run_probes_remote.sh
echo "REMOTE READY: msolve $(msolve -h 2>&1 | head -1 || true)"
