#!/usr/bin/env python3
"""Fill the draft's placeholders from the run JSONs, write the xmodel report,
hash the lane artifacts, stamp the seal, verify it, and check the size window."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path("/home/ubuntu/jc2"); LANE = ROOT / "box/joint-degenerate-20260905"
OUT = ROOT / "xmodel/joint-chart-degenerate-fable5-20260905.md"
BASIS = "5f46093072e6e0d70d9e58f56f2efdb4a8cda598"
draft = (LANE / "draft.md").read_text()
w = json.load(open(LANE / "d108/delta_full_pole_witness_G.json"))
assert w["a32_equals_target"] and w["F_leading_target_via_a32_cubed"] and not w["G_pole_rows_failing"] and w["jacobian_bands_1_12_zero"]
wit = (f"the point `jet1 = jet2 = c = 1`, the 16 free coordinates `0`, pivots resolved, has "
       f"`ord_t K2(σ) = {w['ord_t_K2_sigma']}` with `a_32 = {w['a32']}`, hence "
       f"`h2(σ) = t^{{-4}}(π^2−1)^4 + O(t^{{-3}})`; all {w['G_pole_rows_checked']} G pole rows at local powers "
       f"`1..64` vanish or hit `(π^2−1)^8` at 64 by direct substitution, `a_32^3 = (π^2−1)^{{12}}` gives the F target, "
       f"the Jacobian bands `t = 1..12` are zero, `J_0 = 0`. Its `h3` has factor degrees "
       f"`{', '.join(f'{d}^{e}' for d, e in w['h3_factor_degrees'])}` (irreducible of degree 9 here), D2 faces `{w['K3_D2_face']}` and `{w['K2_D2_face']}`.")
d52 = json.load(open(LANE / "g9966/delta_depth_delta52.json"))
last = d52["ledger"][-1]
assert d52["first_unit_depth_p"] is None and last["p"] == 63 and last["residual_rows"] == 0, (d52["first_unit_depth_p"], last)
short52 = "through p = 63"
line52 = (f"rows to p = 63 (τ-units), Q* pivots {last['cumulative_pivots']}, residual EMPTY at every depth; "
          f"{len(d52['free_after'])} K2c/Hc + jet0, u, v, c free")
body = draft.replace("[[D108_WITNESS]]", wit).replace("[[DELTA52_DEPTH]]", line52).replace("[[DELTA52_SHORT]]", short52)
assert "[[" not in body
OUT.write_text(body)
# artifacts manifest
files = sorted(p for p in LANE.rglob("*") if p.is_file() and p.name not in ("artifacts.sha256", "k2_cache.pkl") and "__pycache__" not in str(p))
with open(LANE / "artifacts.sha256", "w") as f:
    for p in files:
        f.write(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}\n")
r = subprocess.run([sys.executable, str(ROOT / "ops/seal.py"), "stamp", "--basis", BASIS, str(OUT)], text=True, capture_output=True, cwd=ROOT)
print("stamp:", r.returncode, r.stdout.strip(), r.stderr.strip()[-300:])
r = subprocess.run([sys.executable, str(ROOT / "ops/seal.py"), "verify", str(OUT)], text=True, capture_output=True, cwd=ROOT)
print("verify:", r.returncode, r.stdout.strip(), r.stderr.strip()[-300:])
size = len(OUT.read_bytes()); body_bytes = body.encode().__len__()
print("file bytes", size, "body bytes", body_bytes, "window 15-30KB:", 15000 <= body_bytes <= 30000)
print(OUT.read_text()[-600:])
