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
cd "$(dirname "$0")"
ulimit -v $((MEMGB * 1024 * 1024))
for f in $(ls -S -r systems/*.ms); do
  base=$(basename "$f" .ms)
  o="runs/${base}.out"
  [ -s "$o" ] && continue
  echo "=== $base start $(date -u +%H:%M:%S) size=$(wc -c < "$f")"
  /usr/bin/time -v msolve -g 2 -t "$T" -f "$f" -o "$o" 2> "runs/${base}.time" \
    && { grep -qx '\[1\]:' "$o" && echo "=== $base EMPTY (GB=[1])" \
         || echo "=== $base NONEMPTY-OR-OTHER"; } \
    || echo "=== $base FAILED (see runs/${base}.time)"
done
echo "ALL DONE"
RUNNER
chmod +x jc72108/run_probes_remote.sh
echo "REMOTE READY: msolve $(msolve -h 2>&1 | head -1 || true)"
