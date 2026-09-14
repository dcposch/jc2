#!/usr/bin/env python3
"""ell-shifted Xu calculus: I'_M AND I'_m on licensed Prop 6.3 children.

New here (derived in the report, sec. 2):
  (4.3)^l  I(f_xi, f_y g)  = (1+l)*deg_y f + sum_{Pm} |D^f_s|(delta_s - 1 - l)
  (4.4)^l  I(f_y, f_xi g_y) <= (1+l)*(deg_y f - 1) + sum_{Pm}(|D^f_s|-1)(delta_s-1-l)
  Thm 4.7(ii)^l  I(f_xi,g) >= (1+l) + sum_{Pm}(delta_s - 1 - l) + I(f_y,g_y)
  ==> I_m^l := (1+l) + sum_{Pm}(delta_sigma - 1 - l)     and Cor 5.3^l: I_M^l >= I_m^l.
child_xu.evaluate already returns the per-final-minor-sigma terms (count, -kappa/rho)
with -kappa/rho = delta_sigma - (1+l); summing them is the only new line of code.
"""
from __future__ import annotations
import importlib.util, itertools, json, sys
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
EC = ROOT / "box" / "exact-contact-20260906"
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(EC))
sys.dont_write_bytecode = True

from box.lib.descend_own import descend_own, exact_int          # noqa: E402
from exact_contact import tower, all_flat, patterns             # noqa: E402
_s = importlib.util.spec_from_file_location("child_xu", EC / "child_xu.py")
child_xu = importlib.util.module_from_spec(_s); _s.loader.exec_module(child_xu)

ROSTER = ROOT / "box" / "residual66-20260905" / "roster.jsonl"


class Src:
    def __init__(self, src):
        self.n, self.m, self.s = src["n"], src["m"], src["s"]
        self.M = {i + 1: src["M"][i] for i in range(self.s)}
        self.V = {i + 2: src["V"][i] for i in range(len(src["V"]))}


def Im_ell(minor_terms, ell):
    """I_m^l = (1+l) + sum over final minor sigma of (delta_sigma - 1 - l)."""
    return Q(1 + ell) + sum(Q(c) * Q(t) for c, t in minor_terms)


def child_configs(T):
    levels = list(range(T["s"], 1, -1))
    opts = []
    for i in levels:
        cand = []
        for p in patterns(T["P"][i], T["Qd"][i], T["A"][i], T["V"][i], T["lo"][i]):
            cl = ([p["z"]] if p["z"] > 0 else []) + list(p["orbits"])
            for ix, c in enumerate(cl):
                if c == T["V"][i]:
                    cand.append((p, ix))
        opts.append(cand)
    seen, out = set(), []
    for combo in itertools.product(*opts) if opts else [()]:
        ch = {i: c[0] for i, c in zip(levels, combo)}
        sl = {i: c[1] for i, c in zip(levels, combo)}
        r = child_xu.evaluate(T, ch, sl)
        if r is None:
            continue
        key = (r["IM"], tuple(r["leaves"]))
        if key in seen:
            continue
        seen.add(key)
        pat = {i: (c[0]["z"], c[0]["orbits"], c[1]) for i, c in zip(levels, combo)}
        out.append(dict(pattern=pat, IM=r["IM"], Im=Im_ell(r["minor"], T["ell"]),
                        minor=r["minor"], leaves=r["leaves"]))
    return out


def run(rids):
    rows = {json.loads(l)["row_id"]: json.loads(l) for l in open(ROSTER)}
    report = []
    for rid in rids:
        row = rows[rid]
        src = row["source"]
        T = tower(src)
        par = []
        for r in all_flat(T):
            par.append(dict(pattern=str({i: (z, list(o), ix) for i, (z, o, ix)
                                         in r["pattern"].items()}),
                            IM=str(r["IM"]), Im=str(r["Im"]),
                            margin=str(r["IM"] - r["Im"]),
                            IM_integral=r["IM"].denominator == 1,
                            IM_ge_Im=r["IM"] >= r["Im"]))
        D = descend_own(Src(src))
        vecs = D["V_vectors"]["values"] if isinstance(D.get("V_vectors"), dict) else None
        if vecs is None:
            vecs = D.get("V_vectors")
        ch = []
        for vec in vecs:
            oc = dict(n_prime=int(D["n"]), m_prime=int(D["m"]), s_prime=int(D["s"]),
                      M_prime=[int(D["M"][i]) for i in range(1, D["s"] + 1)],
                      d_prime=[int(D["d"][i]) for i in range(1, D["s"] + 2)],
                      V_prime=[exact_int(x) for x in vec], ell=int(D["ell"]))
            CT = child_xu.child_tower(oc, oc["ell"])
            for c in child_configs(CT):
                ch.append(dict(V_prime=oc["V_prime"],
                               pattern=str({i: (z, list(o), ix) for i, (z, o, ix)
                                            in c["pattern"].items()}),
                               IM=str(c["IM"]), Im=str(c["Im"]),
                               margin=str(c["IM"] - c["Im"]),
                               IM_integral=c["IM"].denominator == 1,
                               IM_ge_Im=c["IM"] >= c["Im"],
                               minor=[[str(a), str(b)] for a, b in c["minor"]],
                               leaves=c["leaves"]))
        report.append(dict(row_id=rid, n=src["n"], m=src["m"], ell=int(D["ell"]),
                           child_nm=[int(D["n"]), int(D["m"])], s_prime=int(D["s"]),
                           M_prime=[int(D["M"][i]) for i in range(1, D["s"] + 1)],
                           d_prime=[int(D["d"][i]) for i in range(1, D["s"] + 2)],
                           V_vectors=[[str(x) for x in v] for v in vecs],
                           V_type=D["V_type"], route=D["provenance"] if "provenance" in D else None,
                           descent_license=D["descent_license"],
                           top_license=D["top_license"],
                           parent=par, child=ch))
    return report


if __name__ == "__main__":
    rids = sys.argv[1:] or ["R063", "R009", "R050"]
    rep = run(rids)
    for R in rep:
        print(f"\n########## {R['row_id']}  parent ({R['n']},{R['m']}) -> child "
              f"{tuple(R['child_nm'])}  ell={R['ell']}  s'={R['s_prime']} "
              f"M'={R['M_prime']} d'={R['d_prime']}")
        print(f"   licensed V' ({R['V_type']}): {R['V_vectors']}  "
              f"license={R['descent_license']}/{R['top_license']}")
        print("   PARENT (ell=0):")
        for c in R["parent"]:
            print(f"     I_M={c['IM']:>8}  I_m={c['Im']:>8}  margin={c['margin']:>8}"
                  f"  int={'Y' if c['IM_integral'] else 'N'}  ge={'Y' if c['IM_ge_Im'] else 'N'}"
                  f"  {c['pattern']}")
        print(f"   CHILD (ell={R['ell']}):")
        for c in R["child"]:
            print(f"     I'_M={c['IM']:>8}  I'_m={c['Im']:>8}  margin={c['margin']:>8}"
                  f"  int={'Y' if c['IM_integral'] else 'N'}  ge={'Y' if c['IM_ge_Im'] else 'N'}"
                  f"  V'={c['V_prime']} {c['pattern']}")
            for L in c["leaves"]:
                print("          ", L)
            print("           minor sigma (count, delta-(1+l)):", c["minor"])
