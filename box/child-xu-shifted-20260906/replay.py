#!/usr/bin/env python3
"""46-row replay: licensed-child configs under printed closure, I'_M and I'_m^l.

Does not rewrite the ell-shifted calculus.  Imports:
  box/xu-ell-shift-20260906/{ell_shift,child_close,child_row_close}
  box/lib/descend_own.py
  box/exact-contact-20260906/child_xu.py  (via those scripts)

Shifted: ell = v_s - u_s - 1 from descend_own (parent).
Printed closure: child_close.search with actual-centre L updates
(L2 = lcm(L, den delta) on a split), same loop as child_row_close.close_row,
but this driver records EVERY completion (I'_M, I'_m), not only survivors.

Unshifted comparison (same licensed (n',m',M',V')):
  (U1) child_tower(oc, ell=0) + child_configs  — parent formulae on the child
  (U2) I_m = 1 + sum (delta-1) on the same shifted packets
       (t = delta-(1+ell) from evaluate, so I_m = 1 + sum c*(t+ell)).
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
import time
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = Path(__file__).resolve().parent
XELL = ROOT / "box" / "xu-ell-shift-20260906"
EC = ROOT / "box" / "exact-contact-20260906"
LANE = Path("/tmp/jc2-lane.u8U4Ga/inputs")
ROSTER = LANE / "roster.jsonl"

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(EC))
sys.path.insert(0, str(XELL))
sys.dont_write_bytecode = True

from box.lib.descend_own import descend_own, exact_int  # noqa: E402
from ell_shift import Src, child_configs  # noqa: E402
from child_row_close import lcmn  # noqa: E402
import child_close as CC  # noqa: E402
import child_xu  # noqa: E402


def qstr(x) -> str:
    x = Q(x)
    return str(x.numerator) if x.denominator == 1 else str(x)


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def vecs_of(D):
    v = D["V_vectors"]
    if isinstance(v, dict):
        v = v["values"]
    return v


def oc_from(D, vec):
    s = int(D["s"])
    return dict(
        n_prime=int(D["n"]),
        m_prime=int(D["m"]),
        s_prime=s,
        M_prime=[int(D["M"][i]) for i in range(1, s + 1)],
        d_prime=[int(D["d"][i]) for i in range(1, s + 2)],
        V_prime=[exact_int(x) for x in vec],
        ell=int(D["ell"]),
    )


def Im_unshifted(minor_terms, ell):
    """Xu Cor 5.3 unshifted: 1 + sum_Pm (delta-1), on the same packets."""
    return Q(1) + sum(Q(c) * (Q(t) + ell) for c, t in minor_terms)


def close_pattern(T, c, ell, depth, cap):
    """Same sibling continuation as child_row_close.close_row; keep ALL I'_M."""
    n, m, s = T["n"], T["m"], T["s"]
    dtrue = {}
    for i, (z, orb, ix) in c["pattern"].items():
        g = 0
        for r in ([z] if z > 0 else []) + list(orb):
            g = gcd(g, r)
        dtrue[i] = T["d"][i] // g
    sib = [L for L in c["leaves"] if "MAJOR-SIB" in L]
    base_IM = c["IM"]
    pools = []
    dead = None
    for L in sib:
        i = int(L.split()[0][1:])
        rho = int(L.split("rho=")[1].split()[0])
        cop = int(L.split(" x")[1].split()[0])
        each = Q(L.split("IMeach=")[1].split()[0])
        base_IM -= each * cop
        kap = rho * ((1 + ell) - T["delta"][i]) + T["lam"][i]
        W0 = n - T["M"][i]
        Lden = lcmn([T["delta"][j].denominator for j in range(i, s + 1)])
        R = CC.search(n, m, rho, kap, W0, Lden, dtrue[i], depth, ell, cap)
        if not R:
            dead = f"sibling rho={rho} kappa={kap} W0={W0} has NO completion"
            break
        pools.append([((a, b), cop) for (a, b) in R])
    rec = dict(
        pattern=str({i: (z, list(o), ix) for i, (z, o, ix) in c["pattern"].items()}),
        V=list(map(int, c.get("V", []))),
        flat_IM=qstr(c["IM"]),
        flat_Im=qstr(c["Im"]),
        flat_int=c["IM"].denominator == 1,
        flat_ge=c["IM"] >= c["Im"],
        n_sib=len(sib),
        Im_unshifted=qstr(Im_unshifted(c["minor"], ell)),
        Im_shift_diff=qstr(c["Im"] - Im_unshifted(c["minor"], ell)),
    )
    if dead:
        rec.update(dead=dead, n_closed=0, closed=[])
        return rec
    closed = []
    seen = set()
    for combo in itertools.product(*pools) if pools else [()]:
        IM = base_IM + sum(a * k for (a, b), k in combo)
        Im = c["Im"] + sum(b * k for (a, b), k in combo)
        key = (IM, Im)
        if key in seen:
            continue
        seen.add(key)
        closed.append(dict(
            IM=qstr(IM), Im=qstr(Im),
            integral=IM.denominator == 1,
            ge=IM >= Im,
        ))
    rec.update(dead=None, n_closed=len(closed), closed=closed)
    return rec


def run_row(row, depth, cap):
    src = row["source"]
    D = descend_own(Src(src))
    ell_src = int(src["v_s"]) - int(src["u_s"]) - 1
    ell = int(D["ell"])
    vecs = vecs_of(D)
    flats = []
    closed_recs = []
    unshifted = []
    for vec in vecs:
        oc = oc_from(D, vec)
        T = child_xu.child_tower(oc, ell)
        T0 = child_xu.child_tower(oc, 0)
        for c in child_configs(T):
            c = dict(c)
            c["V"] = [exact_int(x) for x in vec]
            flats.append(c)
            closed_recs.append(close_pattern(T, c, ell, depth, cap))
        for c0 in child_configs(T0):
            unshifted.append(dict(
                IM=qstr(c0["IM"]), Im=qstr(c0["Im"]),
                integral=c0["IM"].denominator == 1,
                ge=c0["IM"] >= c0["Im"],
                V=[exact_int(x) for x in vec],
            ))
    flat_IM = [qstr(c["IM"]) for c in flats]
    flat_Im = [qstr(c["Im"]) for c in flats]
    closed_vals = [x for r in closed_recs for x in r["closed"]]
    closed_IM = [x["IM"] for x in closed_vals]
    all_nonint_flat = bool(flats) and all(not (Q(x).denominator == 1) for x in flat_IM)
    all_nonint_closed = bool(closed_vals) and all(not x["integral"] for x in closed_vals)
    no_closed = (not closed_vals) and bool(flats)
    flat_set = sorted(set(flat_IM), key=lambda s: Q(s))
    closed_set = sorted(set(closed_IM), key=lambda s: Q(s))
    u_set = sorted({x["IM"] for x in unshifted}, key=lambda s: Q(s))
    Im_u_set = sorted({r["Im_unshifted"] for r in closed_recs}, key=lambda s: Q(s))
    Im_s_set = sorted(set(flat_Im), key=lambda s: Q(s))
    return dict(
        row_id=row["row_id"],
        n=src["n"], m=src["m"],
        us=src["u_s"], vs=src["v_s"],
        ell=ell, ell_vs_us=ell_src, ell_match=(ell == ell_src),
        child=[int(D["n"]), int(D["m"])],
        s_prime=int(D["s"]),
        M_prime=[int(D["M"][i]) for i in range(1, int(D["s"]) + 1)],
        V_type=D["V_type"],
        V=[[str(x) for x in v] for v in vecs],
        license=D["descent_license"],
        top_license=D["top_license"],
        route=D["route_state"],
        n_flat=len(flats),
        n_closed=len(closed_vals),
        n_unshifted=len(unshifted),
        flat=[{
            "IM": qstr(c["IM"]), "Im": qstr(c["Im"]),
            "int": c["IM"].denominator == 1,
            "ge": c["IM"] >= c["Im"],
            "nsib": sum(1 for L in c["leaves"] if "MAJOR-SIB" in L),
            "pat": str({i: (z, list(o), ix) for i, (z, o, ix) in c["pattern"].items()}),
        } for c in flats],
        closed=closed_recs,
        unshifted=unshifted,
        flat_IM=flat_set,
        closed_IM=closed_set,
        unshifted_IM=u_set,
        Im_shifted=Im_s_set,
        Im_unshifted=Im_u_set,
        all_nonint_flat=all_nonint_flat,
        all_nonint_closed=all_nonint_closed,
        no_printed_completion=no_closed,
        IM_closed_ne_flat=(closed_set != flat_set),
        IM_shift_ne_ell0=(flat_set != u_set),
        Im_ne_unshifted=(Im_s_set != Im_u_set),
        n_flat_int=sum(1 for c in flats if c["IM"].denominator == 1),
        n_flat_ge=sum(1 for c in flats if c["IM"] >= c["Im"]),
        n_closed_int=sum(1 for x in closed_vals if x["integral"]),
        n_closed_ge=sum(1 for x in closed_vals if x["ge"]),
        n_closed_surv=sum(1 for x in closed_vals if x["integral"] and x["ge"]),
    )


def main():
    t0 = time.monotonic()
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    cap = 4
    rows = [json.loads(l) for l in open(ROSTER)]
    complete = [r for r in rows if r["source"]["u_s"] == 1]
    assert len(complete) == 46
    out_rows = []
    for row in complete:
        rec = run_row(row, depth, cap)
        out_rows.append(rec)
        print(
            f"{rec['row_id']} ell={rec['ell']} nF={rec['n_flat']} nC={rec['n_closed']} "
            f"n0={rec['n_unshifted']} flatIM={rec['flat_IM']} clIM={rec['closed_IM']} "
            f"Im^l={rec['Im_shifted']} Im_u={rec['Im_unshifted']} "
            f"allN_F={rec['all_nonint_flat']} allN_C={rec['all_nonint_closed']} "
            f"cl≠flat={rec['IM_closed_ne_flat']} IM≠ell0={rec['IM_shift_ne_ell0']} "
            f"Im≠u={rec['Im_ne_unshifted']} surv={rec['n_closed_surv']}",
            flush=True,
        )

    cand_flat = [r["row_id"] for r in out_rows if r["all_nonint_flat"]]
    cand_closed = [r["row_id"] for r in out_rows if r["all_nonint_closed"]]
    cl_ne = [r["row_id"] for r in out_rows if r["IM_closed_ne_flat"]]
    ell0_ne = [r["row_id"] for r in out_rows if r["IM_shift_ne_ell0"]]
    im_ne = [r["row_id"] for r in out_rows if r["Im_ne_unshifted"]]
    empty_u = [r["row_id"] for r in out_rows if r["n_unshifted"] == 0]
    no_cl = [r["row_id"] for r in out_rows if r["no_printed_completion"]]

    summary = dict(
        n_complete=46,
        n_flat_total=sum(r["n_flat"] for r in out_rows),
        n_closed_total=sum(r["n_closed"] for r in out_rows),
        n_unshifted_total=sum(r["n_unshifted"] for r in out_rows),
        n_flat_int=sum(r["n_flat_int"] for r in out_rows),
        n_closed_int=sum(r["n_closed_int"] for r in out_rows),
        n_closed_surv=sum(r["n_closed_surv"] for r in out_rows),
        all_nonint_flat=cand_flat,
        all_nonint_closed=cand_closed,
        IM_closed_ne_flat=cl_ne,
        IM_shift_ne_ell0=ell0_ne,
        Im_ne_unshifted=im_ne,
        ell0_empty=empty_u,
        no_printed_completion=no_cl,
        ell_match_46=all(r["ell_match"] for r in out_rows),
        controls=dict(
            R009=[r for r in out_rows if r["row_id"] == "R009"][0],
            R050=[r for r in out_rows if r["row_id"] == "R050"][0],
            R063=[r for r in out_rows if r["row_id"] == "R063"][0],
        ),
    )
    # drop bulky nested copies from summary.controls (keep compact flags)
    for k in list(summary["controls"]):
        R = summary["controls"][k]
        summary["controls"][k] = dict(
            ell=R["ell"], child=R["child"], n_flat=R["n_flat"], n_closed=R["n_closed"],
            flat_IM=R["flat_IM"], closed_IM=R["closed_IM"],
            Im_shifted=R["Im_shifted"], Im_unshifted=R["Im_unshifted"],
            n_flat_int=R["n_flat_int"], n_closed_int=R["n_closed_int"],
            n_closed_surv=R["n_closed_surv"],
            all_nonint_flat=R["all_nonint_flat"],
            all_nonint_closed=R["all_nonint_closed"],
        )

    payload = dict(
        schema="jc2.child-xu-shifted-46/v1",
        depth=depth, cap=cap,
        roster_sha256=sha256_file(ROSTER),
        descend_own_sha256=sha256_file(ROOT / "box" / "lib" / "descend_own.py"),
        elapsed_s=round(time.monotonic() - t0, 3),
        summary=summary,
        rows=[{k: r[k] for k in (
            "row_id", "n", "m", "ell", "ell_match", "child", "s_prime",
            "V_type", "V", "license", "top_license", "route",
            "n_flat", "n_closed", "n_unshifted",
            "flat", "closed", "unshifted",
            "flat_IM", "closed_IM", "unshifted_IM",
            "Im_shifted", "Im_unshifted",
            "all_nonint_flat", "all_nonint_closed",
            "no_printed_completion", "IM_closed_ne_flat",
            "IM_shift_ne_ell0", "Im_ne_unshifted",
            "n_flat_int", "n_flat_ge", "n_closed_int",
            "n_closed_ge", "n_closed_surv",
        )} for r in out_rows],
    )
    outp = HERE / "replay.json"
    text = json.dumps(payload, separators=(",", ":")) + "\n"
    outp.write_text(text)
    print("==== SUMMARY ====", flush=True)
    print("n_flat", summary["n_flat_total"], "n_closed", summary["n_closed_total"],
          "n_unshifted", summary["n_unshifted_total"], flush=True)
    print("n_flat_int", summary["n_flat_int"], "n_closed_int", summary["n_closed_int"],
          "n_closed_surv", summary["n_closed_surv"], flush=True)
    print("all_nonint_flat", cand_flat, flush=True)
    print("all_nonint_closed", cand_closed, flush=True)
    print("IM_closed_ne_flat", cl_ne, flush=True)
    print("IM_shift_ne_ell0", ell0_ne, flush=True)
    print("Im_ne_unshifted", im_ne, flush=True)
    print("ell0_empty", empty_u, flush=True)
    print("no_printed_completion", no_cl, flush=True)
    print(f"wrote {outp} bytes={len(text.encode())} elapsed={payload['elapsed_s']}s",
          flush=True)


if __name__ == "__main__":
    main()
