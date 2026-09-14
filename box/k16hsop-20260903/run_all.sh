#!/bin/bash
# Re-run every driver in this lane, recording wall/RSS/exit in a .resource file.
# t4_ideal.py is the only job over a minute; all are under the 10-minute cap.
D=/home/ubuntu/jc2/box/k16hsop-20260903
run() { /usr/bin/time -f "wall=%e maxrss_kb=%M exit=%x" timeout 900 \
        python3 -u "$D/$1" "${@:3}" > "$D/$2.out" 2> "$D/$2.resource"; }
run ci_series_identity.py   ci_series_identity   16
run alpha_norm_audit.py     alpha_norm_audit
run tail_structure.py       tail_structure_t2    2
run tail_structure.py       tail_structure_t3    3
run tail_audit.py           tail_audit_t2        2
run tail_audit.py           tail_audit_t3        3
run crosscheck_norms.py     crosscheck_norms
run t2_boundary.py          t2_boundary
run eliminant_certificate.py eliminant_certificate
run t3_eliminant_modp.py    t3_eliminant_modp
run pure_power_sdr.py       pure_power_sdr
run tail_ideal_t3.py        tail_ideal_t3
run graded_series_t3.py     graded_series_t3
grep -H . "$D"/*.resource
