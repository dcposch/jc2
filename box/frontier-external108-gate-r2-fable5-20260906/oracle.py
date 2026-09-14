#!/usr/bin/env python3
"""Independent fixed oracle for the external-108 overlay (Fable r2 scratch).

Usage: oracle.py GATE_PATH [--tsv]
Runs the 10 charged control-matrix rows plus extra boundary rows against the
given gate copy and compares with hand-derived expectations.  Exit 0 iff all
rows match.  Expectations were derived from Theorem 2.1 (max>=108 consequence)
and the gcd>=16 legacy rule, not copied from the producer's TSV.
"""
import json, subprocess, sys
gate = sys.argv[1]
tsv = "--tsv" in sys.argv
NC, RC, MC = "NOT_CLOSED_BY_THIS_GATE", "REFUSE_CLASSICALLY_CLOSED", "METHOD_CONTROL_ONLY"
EX, IN, OUT = "EXCLUDED_BY_EXTERNAL_LT108", "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND", "OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED"
G, H = "GGV-Heitmann-gcd16", "GGHV-actual-max-total-degree-108"
# name, argv, rc, legacy verdict, external conclusion, overall, excluded_by
ROWS = [
 ("actual_99_66", ["--total-degrees","99","66"], 3, NC, EX, RC, H),
 ("actual_108_72", ["--total-degrees","108","72"], 0, NC, IN, NC, "-"),
 ("actual_108_108", ["--total-degrees","108","108"], 0, NC, IN, NC, "-"),
 ("cap_107", ["--total-cap","107"], 3, NC, EX, RC, H),
 ("cap_108", ["--total-cap","108"], 0, NC, IN, NC, "-"),
 ("partial_y_99_66_total_unbounded", ["--partial-y-degrees","99","66","--total-unbounded"], 0, NC, OUT, NC, "-"),
 ("actual_99_66_method_control", ["--total-degrees","99","66","--purpose","method-control"], 0, NC, EX, MC, H),
 ("gcd_only_actual_108_107", ["--total-degrees","108","107"], 3, RC, IN, RC, G),
 ("old_gcd_actual_9_12", ["--total-degrees","9","12"], 3, RC, EX, RC, G+","+H),
 ("old_gcd_cap_12", ["--total-cap","12"], 3, RC, EX, RC, G+","+H),
 # --- extra rows (Fable r2), not in the producer matrix ---
 ("x_actual_107_107", ["--total-degrees","107","107"], 3, NC, EX, RC, H),
 ("x_actual_72_108_reversed", ["--total-degrees","72","108"], 0, NC, IN, NC, "-"),
 ("x_actual_64_96", ["--total-degrees","64","96"], 3, NC, EX, RC, H),
 ("x_actual_100_125", ["--total-degrees","100","125"], 0, NC, IN, NC, "-"),
 ("x_cap_16_old_pass_new_fail", ["--total-cap","16"], 3, NC, EX, RC, H),
 ("x_cap_15_both", ["--total-cap","15"], 3, RC, EX, RC, G+","+H),
 ("x_actual_16_16_method_control", ["--total-degrees","16","16","--purpose","method-control"], 0, NC, EX, MC, H),
 ("x_actual_1_1000_gcd_only", ["--total-degrees","1","1000"], 3, RC, IN, RC, G),
 ("x_partial_y_1_1_unbounded", ["--partial-y-degrees","1","1","--total-unbounded"], 0, NC, OUT, NC, "-"),
 ("x_cap_108_method_control", ["--total-cap","108","--purpose","method-control"], 0, NC, IN, NC, "-"),
]
bad = []
for name, argv, erc, ev, ec, eo, eex in ROWS:
    p = subprocess.run([sys.executable, gate, *argv, "--tag", "fable-r2-"+name], capture_output=True, text=True)
    try:
        j = json.loads(p.stdout)
    except Exception:
        j = {}
    got = (p.returncode, j.get("verdict"), j.get("conclusion"), j.get("overall_verdict"),
           ",".join(j.get("excluded_by", [])) or ("-" if "excluded_by" in j else None))
    exp = (erc, ev, ec, eo, eex)
    ok = got == exp
    if tsv:
        print("\t".join(str(x) for x in (name, *got)))
    if not ok:
        bad.append((name, exp, got))
if not tsv:
    print(f"gate={gate} rows={len(ROWS)} mismatches={len(bad)}")
    for b in bad:
        print("  MISMATCH", b[0], "expected", b[1], "got", b[2])
sys.exit(1 if bad else 0)
