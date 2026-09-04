#!/bin/bash
set -euo pipefail

frozen=/tmp/jc2-lane.Gp5PbG/inputs/t_order_system.py

set -o pipefail
timeout --signal=TERM --kill-after=10 300 \
  python3 -u "$frozen" --t 6 --gauged |
awk '
  { print }
  /tuple=\(76,52;73,3\), \(e,q\)=\(19,13\)/ { tuple_ok=1 }
  /Phi radii=\(-1,6\/19\)/ { phi_ok=1 }
  /safe target gauges: ON/ { gauges_ok=1 }
  /unknowns=63$/ { unknowns_ok=1 }
  /coefficient equations=93$/ { equations_ok=1 }
  /deterministic numeric-parameter h-adic reconstruction: True$/ { recon_ok=1 }
  END {
    if (!(tuple_ok && phi_ok && gauges_ok && unknowns_ok && equations_ok && recon_ok)) {
      print "FRESH_CHART_FAIL" > "/dev/stderr"
      exit 1
    }
    print "FRESH_CHART_PASS tuple=76,52;73,3 radii=-1,6/19 unknowns=63 equations=93 gauges=ON reconstruction=True"
  }
'
