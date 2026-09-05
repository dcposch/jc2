#!/usr/bin/env python3
"""Replay the charged whole-tree screens on the eight (1)-(13)-admissible
(99,66) skeletons.

Imports unmodified from box/centre-gate-20260903/ (byte-identical to the
frozen lane inputs): moh_skeleton_full_frozen, opus5_probe.Tree.  The
ok()/window call is the same as rerun_screens.run_one.

Foreground, exact rationals, no subprocess fan-out.
"""
from __future__ import annotations

import json
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
CENTRE = os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903"))
sys.path.insert(0, CENTRE)

import moh_skeleton_full_frozen as B  # noqa: E402
from opus5_probe import Tree  # noqa: E402

# Charged S1..S8 labels from 17(cccccc) / g9966-n1-skeletons-gpt55 (key = (M2,V3,V2)).
S_IDS = {
    (-22, 9, 1): "S1",
    (22, 7, 1): "S2",
    (22, 7, 5): "S3",
    (22, 8, 1): "S4",
    (22, 10, 1): "S5",
    (55, 10, 2): "S6",
    (77, 7, 8): "S7",
    (77, 8, 8): "S8",
}

# Same five screens as the fable desk replay, plus GATED / POLY for the
# hostile "does 17(hh) still carry a gate?" test.  Flags match rerun_screens.py.
SCREENS = [
    ("PARTITION", dict(danger=False, gate=False)),
    ("PARTITION_ODE", dict(danger=False, gate=False, ode=True)),
    ("PARTITION_PASS", dict(danger=False, gate=False, ode=True, passport=True)),
    ("GATED", dict(danger=True, gate=True)),
    ("GATED_ODE", dict(danger=True, gate=True, ode=True)),
    ("UNGATED", dict(danger=True, gate=False)),
    ("UNGATED_ODE", dict(danger=True, gate=False, ode=True)),
    ("UNGATED_PASS", dict(danger=True, gate=False, ode=True, passport=True)),
    ("POLY", dict(danger=True, gate=False, recenter=True)),
    ("POLY_ODE", dict(danger=True, gate=False, ode=True, recenter=True)),
]


def surv(n, m, Ms, V, *, danger, gate, ode=False, passport=False, recenter=False):
    """Exact rerun_screens.run_one call, plus optional recenter for POLY."""
    kw = dict(gate=gate, ode=ode, capacity=passport, passport=passport)
    T = Tree(n, m, Ms, **kw)
    if recenter:
        T.recenter = True
    T._memo = {}
    T.why = []
    window_ok = T.d[T.s] > V[T.s] > (T.d[T.s] / 2)
    if not window_ok:
        return False, "FAIL-window", T, None
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    r = T.ok(T.s - 1, (V[T.s],), danger, need)
    return r is not None, ("SURVIVES" if r is not None else "DEAD"), T, r


def chain_modes(T, V):
    """At the unique s=3 node j=2, list how V2 can be realised as zero / nonzero."""
    j = T.s - 1
    high = (V[T.s],)
    dl, L, A, P, Q, lo = T.node(j, high)
    V2 = V[j]
    zmaj_ok = False
    zero_matches = []
    coins = []
    for b in range(P % A, P + 1, A):
        zmaj = F(b) > lo
        if V2 == b and zmaj:
            zero_matches.append(b)
            zmaj_ok = True
        total = (P - b) // A
        for v in range(1, total + 1):
            maj = F(v) > lo
            if v == V2:
                coins.append({"b": b, "v": v, "major": maj, "total": total})
    nh_sel = (V2,) + high
    bottom_ok, A1, c12, c13 = T.bottom(nh_sel)
    free = [str(x) for x in T.free_exponents(nh_sel)]
    return {
        "j": j,
        "delta_j": str(dl),
        "L": L,
        "A": A,
        "P": P,
        "Q": Q,
        "lo": str(lo),
        "V2": V2,
        "V2_major": F(V2) > lo,
        "zero_factor_realisations_b": zero_matches,
        "nonzero_orbit_realisations": coins,
        "selected_bottom_ok": bottom_ok,
        "A1": A1,
        "c12": c12,
        "c13": c13,
        "free_exponents_selected_chain": free,
        "P_mod_A": P % A,
        "A_divides_Q_minus_1": ((Q - 1) % A == 0),
    }


def enumerate_rows():
    rows = []
    for m, Ms, V in B.census(99, Kmin=2, full=True):
        if m != 66:
            continue
        S = B.Skel(99, m, list(Ms), V)
        key = (Ms[0], V[3], V[2])
        sid = S_IDS.get(key)
        ok1011, b10, b11 = S.cond1011(2)
        ok1213, b12, b13 = S.cond1213()
        tri, sq, A2, Q = S.div9(2)
        T = Tree(99, m, Ms)
        modes = chain_modes(T, V)
        rec = {
            "id": sid,
            "n": 99,
            "m": m,
            "s": S.s,
            "M": {str(i): S.M[i] for i in range(1, S.s + 1)},
            "d": {str(i): S.d[i] for i in range(1, S.s + 2)},
            "V": {str(i): S.V[i] for i in range(2, S.s + 1)},
            "u_s": S.d[S.s] - S.V[S.s],
            "v_s": S.V[S.s],
            "delta": {str(i): str(S.delta[i]) for i in range(1, S.s + 1)},
            "A1": S.A(1),
            "A2": S.A(2),
            "windows_ok": S.windows_ok(),
            "full_ok": S.full_ok(),
            "any10": S.any10(),
            "cond1011_j2": {"ok": ok1011, "by10": b10, "by11": b11},
            "cond1213": {"ok": ok1213, "by12": b12, "by13": b13},
            "div9_j2": {"TRI": tri, "SQ": sq, "A": A2, "Q": Q},
            "modes": modes,
            "Ms": list(Ms),
            "V_dict": {int(k): int(v) for k, v in V.items()},
        }
        rows.append(rec)
    rows.sort(key=lambda r: (r["M"]["2"], r["V"]["3"], r["V"]["2"]))
    return rows


def main():
    rows = enumerate_rows()
    print("=== ENUMERATION (99,66) census(Kmin=2, full=True) ===")
    print("count", len(rows))
    ids = [r["id"] for r in rows]
    print("ids", ids)
    if len(rows) != 8 or set(ids) != set(S_IDS.values()) or None in ids:
        print("ENUMERATION MISMATCH", ids)
        sys.exit(1)

    out_rows = []
    for rec in rows:
        n, m, Ms, V = 99, rec["m"], rec["Ms"], rec["V_dict"]
        print()
        print("=" * 72)
        print(
            f"{rec['id']}  M={tuple(rec['M'][str(i)] for i in range(1, rec['s']+1))}"
            f"  d={tuple(rec['d'][str(i)] for i in range(1, rec['s']+2))}"
            f"  V2={rec['V']['2']} V3={rec['V']['3']}"
            f"  u_s={rec['u_s']} v_s={rec['v_s']}"
        )
        print(
            f"  delta={rec['delta']}  A1={rec['A1']} A2={rec['A2']}"
            f"  windows_ok={rec['windows_ok']} full_ok={rec['full_ok']}"
            f"  any10={rec['any10']}  (10)={rec['cond1011_j2']['by10']} (11)={rec['cond1011_j2']['by11']}"
            f"  (12)={rec['cond1213']['by12']} (13)={rec['cond1213']['by13']}"
        )
        md = rec["modes"]
        print(
            f"  D2 node: A={md['A']} P={md['P']} Q={md['Q']} lo={md['lo']}"
            f"  V2_major={md['V2_major']}  zero_b={md['zero_factor_realisations_b']}"
            f"  nonzero={md['nonzero_orbit_realisations']}"
            f"  bottom_ok={md['selected_bottom_ok']} A1={md['A1']}"
            f"  free={md['free_exponents_selected_chain']}"
        )
        screens = {}
        for name, kw in SCREENS:
            ok, label, T, witness = surv(n, m, Ms, V, **kw)
            why = list(T.why)[-6:] if T.why else []
            wshort = None
            if witness is not None:
                wshort = {
                    "j": witness.get("j"),
                    "A": witness.get("A"),
                    "P": witness.get("P"),
                    "Q": witness.get("Q"),
                    "b": witness.get("b"),
                    "mode": witness.get("mode"),
                    "orbits": witness.get("orbits"),
                    "zero_major": witness.get("zero_major"),
                    "danger": witness.get("danger"),
                    "delta": witness.get("delta"),
                    "lo": witness.get("lo"),
                }
            screens[name] = {
                "result": label,
                "ok": ok,
                "why_tail": [tuple(str(x) for x in t) if isinstance(t, tuple) else str(t) for t in why],
                "witness": wshort,
            }
            print(f"  {name:16s} {label}" + (f"  mode={wshort['mode']} b={wshort['b']} orbits={wshort['orbits']} danger={wshort['danger']}" if wshort else "")
                  + (f"  why={screens[name]['why_tail'][:2]}" if not ok else ""))
        rec["screens"] = screens
        out_rows.append(rec)

    print()
    print("=== TABLE ===")
    hdr = ["id", "M2", "V2", "V3", "u_s", "any10", "free"] + [n for n, _ in SCREENS]
    print(" | ".join(hdr))
    for rec in out_rows:
        cells = [
            rec["id"],
            str(rec["M"]["2"]),
            str(rec["V"]["2"]),
            str(rec["V"]["3"]),
            str(rec["u_s"]),
            str(rec["any10"]),
            ",".join(rec["modes"]["free_exponents_selected_chain"]) or "∅",
        ]
        for name, _ in SCREENS:
            cells.append("SURV" if rec["screens"][name]["ok"] else "DEAD")
        print(" | ".join(cells))

    claim = {
        "PARTITION_dead": ["S1", "S4", "S5", "S6"],
        "UNGATED_dead_not_PARTITION": ["S2", "S3", "S7"],
        "survives_all": ["S8"],
    }
    print()
    print("=== CLAIM CHECK ===")
    ok_claim = True
    for sid in claim["PARTITION_dead"]:
        rec = next(r for r in out_rows if r["id"] == sid)
        p = rec["screens"]["PARTITION"]["ok"]
        print(f"  {sid} PARTITION dead? {not p}")
        if p:
            ok_claim = False
    for sid in claim["UNGATED_dead_not_PARTITION"]:
        rec = next(r for r in out_rows if r["id"] == sid)
        p = rec["screens"]["PARTITION"]["ok"]
        u = rec["screens"]["UNGATED"]["ok"]
        print(f"  {sid} PARTITION survives={p} UNGATED dead={not u}")
        if not p or u:
            ok_claim = False
    rec8 = next(r for r in out_rows if r["id"] == "S8")
    s8_all = all(rec8["screens"][n]["ok"] for n, _ in SCREENS)
    print(f"  S8 survives every listed screen? {s8_all}")
    if not s8_all:
        ok_claim = False
    print("CLAIM_MATCH", ok_claim)

    dest = os.path.join(HERE, "screen_eight.json")
    with open(dest, "w") as f:
        json.dump({"count": len(out_rows), "claim_match": ok_claim, "rows": out_rows}, f, indent=2, sort_keys=True)
        f.write("\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
