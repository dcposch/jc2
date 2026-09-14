#!/bin/bash
# assemble the report from the sections, stamp the canonical seal, verify, and record it in the box
set -e
cd /home/ubuntu/jc2/box/k16galois-20260905
./assemble.sh
cd /home/ubuntu/jc2
python3 ops/seal.py stamp xmodel/k16-gamma-galois-fable5-20260905.md --basis 9aede1030ef87e5c47f28aa793a4c431edf62882 | tee box/k16galois-20260905/seal.log
python3 ops/seal.py verify xmodel/k16-gamma-galois-fable5-20260905.md | tee -a box/k16galois-20260905/seal.log
python3 ops/validate_charge_basis.py xmodel/k16-gamma-galois-fable5-20260905.md 2>&1 | tail -1 | tee -a box/k16galois-20260905/seal.log
sha256sum xmodel/k16-gamma-galois-fable5-20260905.md | tee -a box/k16galois-20260905/seal.log
(cd box/k16galois-20260905 && sha256sum gen.py run.sh deploy.sh analyze_patterns.py msolve_point.py crosscheck_f4.py assemble.sh finalize.sh poll.sh frobenius_tables.txt primes.txt > drivers.sha256)
echo FINALIZED
