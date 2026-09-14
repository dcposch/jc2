#!/usr/bin/env python3
"""Replay: POLY_ODE n<=100 survivors, Phi_eff height of the 14 excess rows.

Desk-scale, stdlib + box/moh_skeleton_full.py + box/mohprog-drivers-20260903
full_tree_partition.py.  No Singular.  Confirms OPEN[MOH-PROGRAM-ARTIFACT]
= 14 rows, all u_s=1, all s_eff>=3 (13 at 3, one at 4), zero s_eff=2.
"""
import json, os, sys, time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "box"))
sys.path.insert(0, os.path.join(ROOT, "box", "mohprog-drivers-20260903"))

import full_tree_partition as FT
from moh_skeleton_full import Skel, census, MOH_TABLE


def u_s_of(S):
    return S.d[S.s] - S.V[S.s]


def descend(S):
    us = u_s_of(S)
    ds = S.d[S.s]
    Vs = S.V[S.s]
    k = Vs - us - 1
    n2, m2 = us * S.n // ds, us * S.m // ds
    s2 = S.s - 1
    M2 = {i: (S.M[i] * us) // ds for i in range(1, s2 + 1)}
    d2 = {i: (S.d[i] * us) // ds for i in range(1, s2 + 2)}
    V2 = {i: S.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return {"n": n2, "m": m2, "s": s2, "M": M2, "d": d2, "V": V2, "k": k, "us": us}


def truncate_jacobian(D):
    n, s = D["n"], D["s"]
    Mdict, ddict, Vdict = dict(D["M"]), dict(D["d"]), dict(D["V"])
    dropped = 0
    while s >= 1 and Mdict.get(s) == n - 1:
        dropped += 1
        s -= 1
        Mdict.pop(s + 1, None)
        Vdict.pop(s + 1, None)
        if (s + 1) in ddict and s >= 1:
            Vdict[s + 1] = ddict[s + 1]
    D2 = dict(D)
    D2.update({"s": s, "M": Mdict, "d": ddict, "V": Vdict, "dropped": dropped})
    return D2


def pack(S):
    D = descend(S)
    Dt = truncate_jacobian(D)
    return {
        "n": S.n,
        "m": S.m,
        "M": [S.M[i] for i in range(1, S.s + 1)],
        "V": [S.V[i] for i in range(2, S.s + 1)],
        "d": [S.d[i] for i in range(1, S.s + 2)],
        "s": S.s,
        "u_s": u_s_of(S),
        "n_prime": Dt["n"],
        "m_prime": Dt["m"],
        "k": D["k"],
        "s_eff": Dt["s"],
        "dropped": Dt["dropped"],
        "K_prime": Dt["d"].get(2),
        "M_prime": {str(i): Dt["M"][i] for i in sorted(Dt["M"])},
        "V_prime": {str(i): Dt["V"][i] for i in sorted(Dt["V"])},
    }


def is_printed(S):
    Ms_t = tuple(S.M[i] for i in range(2, S.s + 1))
    Vs_d = {i: S.V[i] for i in range(2, S.s + 1)}
    return any(
        S.n == n and S.m == m and Ms_t == tuple(Ms) and Vs_d == Vs
        for (n, m, Ms, Vs, *_rest) in MOH_TABLE
    )


def main():
    t0 = time.time()
    surv, excess, printed = [], [], []
    n_raw = 0
    for n in range(4, 101):
        for (m, Ms, V) in census(n, Kmin=2, full=True):
            n_raw += 1
            S = Skel(n, m, list(Ms), V)
            if not FT.full_tree_polynomial_ode_ok(S):
                continue
            rec = pack(S)
            surv.append(rec)
            (printed if is_printed(S) else excess).append(rec)
    classes = defaultdict(list)
    for r in excess:
        key = (r["n_prime"], r["m_prime"], r["k"], r["s_eff"], r["K_prime"])
        classes[key].append(r)
    out = {
        "raw_1_13_n_le_100": n_raw,
        "poly_ode_survivors": len(surv),
        "printed_kept": len(printed),
        "excess": len(excess),
        "excess_by_nm": {f"{a},{b}": c for (a, b), c in Counter((r["n"], r["m"]) for r in excess).items()},
        "excess_s": {str(k): v for k, v in Counter(r["s"] for r in excess).items()},
        "excess_us": {str(k): v for k, v in Counter(r["u_s"] for r in excess).items()},
        "excess_s_eff": {str(k): v for k, v in Counter(r["s_eff"] for r in excess).items()},
        "excess_s_eff_eq_2": sum(1 for r in excess if r["s_eff"] == 2),
        "printed_s_eff": {str(k): v for k, v in Counter(r["s_eff"] for r in printed).items()},
        "descended_classes": [
            {"n_prime": k[0], "m_prime": k[1], "k": k[2], "s_eff": k[3],
             "K_prime": k[4], "count": len(v)}
            for k, v in sorted(classes.items())
        ],
        "printed_rows": printed,
        "excess_rows": excess,
        "sec": round(time.time() - t0, 3),
    }
    path = os.path.join(HERE, "moh100_14_phi_eff.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print("raw", n_raw, "POLY_ODE", len(surv), "printed", len(printed),
          "excess", len(excess), "s_eff=2 among excess", out["excess_s_eff_eq_2"])
    print("excess s_eff", out["excess_s_eff"])
    print("classes", out["descended_classes"])
    print("wrote", path, "in", out["sec"], "s")
    assert len(surv) == 20, len(surv)
    assert len(printed) == 6
    assert len(excess) == 14
    assert out["excess_s_eff_eq_2"] == 0
    assert out["excess_us"] == {"1": 14}
    print("ASSERTS_OK")


if __name__ == "__main__":
    main()
