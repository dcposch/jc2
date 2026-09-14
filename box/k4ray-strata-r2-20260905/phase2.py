#!/usr/bin/env python3
"""Phase 2: rerun msolve directly on an already-emitted .ms file with a longer budget.
No re-formation: the generator file is the round-2 chart, hashed here for custody."""
import argparse, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
B = Path("/home/ubuntu/jc2/box/k4ray-strata-r2-20260905")
ap = argparse.ArgumentParser()
ap.add_argument("stem"); ap.add_argument("char", type=int)
ap.add_argument("--threads", type=int, default=32)
ap.add_argument("--timeout", type=int, default=4200)
ap.add_argument("--la", type=int, default=0, help="msolve -l variant; 42 = probabilistic (SCREEN ONLY)")
a = ap.parse_args()
ms = B / "msolve" / f"{a.stem}_p{a.char}.ms"
sfx = f".ph2l{a.la}" if a.la else ".ph2"
outp = B / "msolve" / f"{a.stem}_p{a.char}{sfx}.msout"
sha = hashlib.sha256(ms.read_bytes()).hexdigest()
nrows = ms.read_text().count("\n") - 2
t0 = time.time()
cmd = ["/usr/bin/time", "-v", "msolve", "-g", "2", "-v", "2", "-t", str(a.threads),
       "-f", str(ms), "-o", str(outp)]
if a.la: cmd[2:2] = []; cmd += ["-l", str(a.la)]
try:
    pr = subprocess.run(cmd, capture_output=True, text=True, timeout=a.timeout, check=False)
    rc, so, se, to = pr.returncode, pr.stdout, pr.stderr, False
except subprocess.TimeoutExpired as exc:
    so = (exc.stdout or b""); se = (exc.stderr or b"")
    so = so.decode("utf-8","replace") if isinstance(so,bytes) else so
    se = se.decode("utf-8","replace") if isinstance(se,bytes) else se
    rc, to = None, True
wall = round(time.time()-t0, 3)
m = re.search(r"Maximum resident set size \(kbytes\): (\d+)", se)
degs = [int(d) for d in re.findall(r"[Dd]egree\D{0,12}(\d+)", so)]
txt = outp.read_text() if outp.exists() else ""
length = None
body = []
for ln in txt.splitlines():
    if ln.startswith("#"):
        mm = re.search(r"length of basis:\s*(\d+)", ln)
        if mm: length = int(mm.group(1))
        continue
    body.append(ln)
flat = re.sub(r"\s+","","".join(body)).rstrip(":")
inner = flat[1:-1] if flat.startswith("[") and flat.endswith("]") else flat
parts = [q for q in inner.split(",") if q]
cls = "EMPTY" if not flat else ("UNIT" if parts==["1"] else ("ZERO" if parts in ([ "0" ],[]) else "NONUNIT"))
pre = "EXACTQ" if a.char==0 else "MODULAR"
verdict = pre+"_TIMEOUT" if to else (f"MSOLVE_RC_{rc}" if rc!=0 else f"{pre}_{cls}")
P = dict(stem=a.stem, phase=2, char=a.char, la=a.la, ms_sha256=sha, ms_rows=nrows, wall=wall,
         rc=rc, timed_out=to, verdict=verdict, basis_length=length,
         peak_rss_kb=int(m.group(1)) if m else None,
         f4_max_degree=max(degs) if degs else None,
         msout_bytes=len(txt), msout_head=txt[:300], host=os.uname().nodename)
if cls == "NONUNIT": P["msout_full"] = txt[:200000]
(B/"msolve"/f"{a.stem}_p{a.char}{sfx}.ph2.json").write_text(json.dumps(P, indent=2, sort_keys=True)+"\n")
print("PH2__RESULT "+json.dumps(P, sort_keys=True), flush=True)
