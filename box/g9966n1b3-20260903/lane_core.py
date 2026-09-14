#!/usr/bin/env python3
"""Batch-3 closure lane core: frozen enumeration + descended chart plumbing.

Everything written stays under box/g9966n1b3-20260903.  The Prop 6.3(3)
descended Jacobian exponent is ell = v_s - u_s - 1 (Moh 1983, p.197).
"""
from __future__ import annotations

import hashlib, importlib.util, json, math, os, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
INPUTS = Path("/tmp/jc2-lane.g0hNAR/inputs")
ORDER_BASIS = ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py"

THREAD_ENV = {
    "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1",
}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha256(path):
    d = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            d.update(blk)
    return d.hexdigest()


def atomic_write(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def run_call(command, stdout_path, stderr_path, timeout):
    env = os.environ.copy(); env.update(THREAD_ENV)
    wrapped = ["timeout", str(timeout), "stdbuf", "-oL", "-eL", *command]
    t0 = time.monotonic()
    with open(stdout_path, "w") as o, open(stderr_path, "w") as e:
        r = subprocess.run(wrapped, cwd=ROOT, env=env, stdout=o, stderr=e, text=True, check=False)
    return {"command": wrapped, "returncode": r.returncode, "timed_out": r.returncode == 124,
            "elapsed_seconds": round(time.monotonic() - t0, 3),
            "stdout": str(stdout_path), "stderr": str(stderr_path),
            "stdout_sha256": sha256(stdout_path)}


def frozen_enumeration():
    moh = load_module("b3_moh", INPUTS / "moh_skeleton_full.py")
    found = []
    for m, Ms, V in moh.census(99, Kmin=2, full=True):
        if m != 66:
            continue
        found.append(moh.Skel(99, m, list(Ms), V))
    found.sort(key=lambda r: (r.M[2], r.V[3], r.V[2]))
    assert len(found) == 8, len(found)
    rows = []
    for idx, sk in enumerate(found, 1):
        ds = sk.d[sk.s]; vs = sk.V[sk.s]; us = ds - vs
        np_ = us * sk.n // ds; mp = us * sk.m // ds
        K = math.gcd(np_, mp)
        desc = {"n": np_, "m": mp, "M2": us * sk.M[2] // ds, "V2": sk.V[2],
                "K": K, "ell": vs - us - 1}
        desc["u_prime"] = K - desc["V2"]
        rows.append({"id": f"S{idx}", "s": sk.s,
                     "M": [sk.M[i] for i in range(1, sk.s + 1)],
                     "d": [sk.d[i] for i in range(1, sk.s + 2)],
                     "V": {str(i): sk.V[i] for i in range(2, sk.s + 1)},
                     "u_s": us, "v_s": vs, "delta_ceiling": f"{vs}/{us}",
                     "descended": desc, "prop64_automatic": us == 1})
    return {"method": "frozen moh_skeleton_full.census(99,Kmin=2,full=True), m=66, charged sort",
            "count": 8, "rows": rows, "source_sha256": sha256(INPUTS / "moh_skeleton_full.py")}


if __name__ == "__main__":
    payload = frozen_enumeration()
    atomic_write(HERE / "enumeration.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for r in payload["rows"]:
        d = r["descended"]
        print(f"{r['id']}  M={r['M']} V={r['V']} u_s={r['u_s']} v_s={r['v_s']} "
              f"ceil={r['delta_ceiling']} | desc n'={d['n']} m'={d['m']} M2'={d['M2']} "
              f"V2'={d['V2']} K'={d['K']} u'={d['u_prime']} ell={d['ell']}")
