#!/usr/bin/env python3
"""Build the three exact-Q long-solve job scripts for K7_B9_Q0 from the frozen chart.

Chart bytes are the msolve list K7_B9_Q0_p0.ms (72 vars / 241 gens),
SHA-256 15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275.
Ring map is positional and declared: the .ms header names ARE the Singular
variable names (v0..v71); v69=q0, v70=q1, v71=q0_inv, localizer row 241.
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path("/home/ubuntu/k7-b9q0-longsolve")
MS = ROOT / "chart" / "K7_B9_Q0_p0.ms"
CHART_SHA = "15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275"
# frozen positive wp vector (box/k7-cofactors-20260906/r3-custody.json sources[0].weights)
WP = [7,6,5,4,3,2,1,6,5,4,3,2,1,5,4,3,2,1,4,3,2,1,3,2,1,2,1,
      14,13,12,11,10,9,8,7,6,13,12,11,10,9,8,7,6,12,11,10,9,8,7,6,
      11,10,9,8,7,6,10,9,8,7,6,9,8,7,6,8,7,6,5,5,1]
# r3b section 5: rows 1,2,3,4,8,9,10,11 solve successively for these pivots
PIVOTS = [(1,"v6"),(2,"v12"),(3,"v35"),(4,"v43"),(8,"v5"),(9,"v11"),(10,"v16"),(11,"v20")]

raw = MS.read_bytes()
assert hashlib.sha256(raw).hexdigest() == CHART_SHA, "CHART SHA MISMATCH"
lines = raw.decode().splitlines()
names = lines[0].split(",")
assert lines[1].strip() == "0", "chart is not characteristic 0"
rows = [l.rstrip(",") for l in lines[2:] if l.strip()]
assert len(names) == 72 and len(rows) == 241, (len(names), len(rows))
assert names == [f"v{i}" for i in range(72)], "positional name map broken"
assert rows[240] == "v69*v71-1", rows[240]
assert len(WP) == 72

IDEAL = "ideal I=\n" + ",\n".join(rows) + ";\n"

TAIL = r'''
print("CERT__CHAR "+string(char(basering)));
print("CERT__NVARS "+string(nvars(basering)));
print("CERT__NGEN "+string(size(I)));
print("CERT__PARSED 1");
int t0=timer; int rt0=rtimer;
ideal G=%(ALGO)s(I);
print("CERT__SOLVE_TIMER "+string(timer-t0)+" RT "+string(rtimer-rt0));
attrib(G,"isSB",1);
print("CERT__GB_SIZE "+string(size(G)));
int i; int u=0;
if (size(G)==1) { if (G[1]==1) { u=1; } }
print("CERT__GB_BEGIN");
if (size(G)<=25) { for (i=1;i<=size(G);i++) { print(string(G[i])); } }
else { print("CERT__GB_LEADS_ONLY 1"); for (i=1;i<=size(G);i++) { print(string(lead(G[i]))); } }
print("CERT__GB_END");
print("CERT__UNIT "+string(u));
print("CERT__DONE 1");
quit;
'''

def write(job, body):
    d = ROOT / "runs" / job
    d.mkdir(parents=True, exist_ok=True)
    p = d / "job.sing"
    p.write_text(body)
    return p, hashlib.sha256(body.encode()).hexdigest(), len(body)

HEAD = 'option(redSB);\nshort=0;\noption(noredefine);\n'

# (a) exact-Q slimgb, dp, redSB -- full 241-row chart
a = (HEAD + 'print("CERT__ROUTE a_slimgb_dp");\n'
     + "ring R=0,(" + ",".join(names) + "),dp;\n"
     + 'print("CERT__ORDER dp"); print("CERT__ALGO slimgb");\n'
     + IDEAL + TAIL % {"ALGO": "slimgb"})

# (b) exact-Q std under the frozen chart bigrading wp vector
b = (HEAD + 'print("CERT__ROUTE b_std_wp");\n'
     + "ring R=0,(" + ",".join(names) + "),wp(" + ",".join(str(w) for w in WP) + ");\n"
     + 'print("CERT__ORDER wp_frozen"); print("CERT__ALGO std");\n'
     + IDEAL + TAIL % {"ALGO": "std"})

# (c) exact-Q(v69) triangular pre-reduction, then slimgb on the reduced system
cvars = [n for n in names if n != "v69"]
csteps = []
for k, (r, piv) in enumerate(PIVOTS, start=1):
    csteps.append(f'''
// pivot {k}: source row {r} solves for {piv}
pr = I[{r}];
pa = diff(pr,{piv});
print("TRI__PIV {k} ROW {r} VAR {piv} LINEAR "+string(int(diff(pa,{piv})==0))
      +" COEF_IS_FIELD "+string(int(deg(pa)<=0))+" NONZERO "+string(int(pa!=0)));
prest = pr - pa*{piv};
pq = -prest/pa;
print("TRI__PIV {k} EXACT_DIV "+string(int(pa*pq+prest==0))
      +" ROW_VANISHES "+string(int(subst(pr,{piv},pq)==0))
      +" NO_PIVOT_LEFT "+string(int(diff(pq,{piv})==0)));
I = subst(I,{piv},pq);
print("TRI__PIV {k} DONE nnz "+string(size(simplify(I,2))));
''')
c = (HEAD + 'print("CERT__ROUTE c_tri_qv69_slimgb");\n'
     + 'print("CERT__LOCALIZED_FIELD Q(v69)");\n'
     + "ring R=(0,v69),(" + ",".join(cvars) + "),dp;\n"
     + 'print("CERT__ORDER dp"); print("CERT__ALGO tri+slimgb");\n'
     + IDEAL
     + 'print("CERT__CHAR "+string(char(basering)));\n'
       'print("CERT__NVARS "+string(nvars(basering)));\n'
       'print("CERT__NGEN "+string(size(I)));\n'
       'print("CERT__NPARS "+string(npars(basering)));\n'
       'print("CERT__PARSED 1");\n'
       'poly pr; poly pa; poly prest; poly pq;\n'
       'int tt0=timer;\n'
     + "".join(csteps)
     + 'print("TRI__ALLDONE 1 TIMER "+string(timer-tt0));\n'
       'I = simplify(I,2);\n'
       'print("CERT__REDUCED_NGEN "+string(size(I)));\n'
     + TAIL % {"ALGO": "slimgb"})

man = {"chart_sha256": CHART_SHA, "chart_bytes": len(raw), "nvars": len(names),
       "ngens": len(rows), "localizer_row": 241, "localizer": rows[240],
       "wp": WP, "pivots": [{"row": r, "var": v} for r, v in PIVOTS], "jobs": {}}
for job, body in (("a_slimgb_dp", a), ("b_std_wp", b), ("c_tri_qv69_slimgb", c)):
    p, sha, n = write(job, body)
    man["jobs"][job] = {"path": str(p), "sha256": sha, "bytes": n}
(ROOT / "jobs-manifest.json").write_text(json.dumps(man, indent=1) + "\n")
print(json.dumps({k: {kk: vv for kk, vv in v.items()} for k, v in man["jobs"].items()}, indent=1))
