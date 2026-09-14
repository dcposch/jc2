#!/usr/bin/env python3
"""Close every major sibling of every licensed CHILD configuration (ell-shifted).

Reports, per (row, V', pattern), whether ANY completion has I'_M in Z and
I'_M >= I'_m.  base_IM excludes the sibling terms, which the closure supplies.
"""
from __future__ import annotations
import importlib.util, itertools, json, sys, time
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2"); EC = ROOT / "box" / "exact-contact-20260906"
HERE = ROOT / "box" / "xu-ell-shift-20260906"
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(EC)); sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
from box.lib.descend_own import descend_own, exact_int        # noqa: E402
import child_close as CC                                       # noqa: E402
_s = importlib.util.spec_from_file_location("child_xu", EC / "child_xu.py")
child_xu = importlib.util.module_from_spec(_s); _s.loader.exec_module(child_xu)
from exact_contact import patterns                             # noqa: E402
sys.path.insert(0, str(HERE))
from ell_shift import Src, Im_ell, child_configs               # noqa: E402

ROSTER = ROOT / "box" / "residual66-20260905" / "roster.jsonl"


def lcmn(v):
    a = 1
    for x in v:
        a = a * x // gcd(a, x)
    return a


def close_row(rid, depth, cap=4):
    row = {json.loads(l)["row_id"]: json.loads(l) for l in open(ROSTER)}[rid]
    D = descend_own(Src(row["source"]))
    ell, s = int(D["ell"]), int(D["s"])
    out = dict(row_id=rid, parent=[row["source"]["n"], row["source"]["m"]],
               child=[int(D["n"]), int(D["m"])], ell=ell, s_prime=s, depth=depth,
               V_type=D["V_type"], configs=[])
    for vec in (D["V_vectors"]["values"] if isinstance(D["V_vectors"], dict) else D["V_vectors"]):
        oc = dict(n_prime=int(D["n"]), m_prime=int(D["m"]), s_prime=s,
                  M_prime=[int(D["M"][i]) for i in range(1, s + 1)],
                  d_prime=[int(D["d"][i]) for i in range(1, s + 2)],
                  V_prime=[exact_int(x) for x in vec], ell=ell)
        T = child_xu.child_tower(oc, ell)
        n, m = T["n"], T["m"]
        for c in child_configs(T):
            dtrue = {}
            for i, (z, orb, ix) in c["pattern"].items():
                g = 0
                for r in ([z] if z > 0 else []) + list(orb):
                    g = gcd(g, r)
                dtrue[i] = T["d"][i] // g
            sib = [L for L in c["leaves"] if "MAJOR-SIB" in L]
            base_IM = c["IM"]; pools = []; dead = None
            for L in sib:
                # "L{i} MAJOR-SIB rho=R xN IMeach=J"
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
            rec = dict(V_prime=oc["V_prime"],
                       pattern=str({i: (z, list(o), ix) for i, (z, o, ix)
                                    in c["pattern"].items()}),
                       flat_IM=str(c["IM"]), flat_Im=str(c["Im"]),
                       n_sibling=len(sib), base_IM=str(base_IM))
            if dead:
                rec.update(verdict="DEAD", reason=dead, survivors=[])
                out["configs"].append(rec); continue
            surv, tot = set(), 0
            for combo in itertools.product(*pools) if pools else [()]:
                IM = base_IM + sum(a * k for (a, b), k in combo)
                Im = c["Im"] + sum(b * k for (a, b), k in combo)
                tot += 1
                if IM.denominator == 1 and IM >= Im:
                    surv.add((IM, Im))
            rec.update(n_completions=tot,
                       verdict="ALIVE" if surv else "DEAD",
                       reason="" if surv else
                       "no completion with I'_M in Z and I'_M >= I'_m",
                       survivors=[[str(a), str(b)] for a, b in sorted(surv)[:12]],
                       n_survivors=len(surv))
            out["configs"].append(rec)
    out["row_verdict"] = ("ALIVE" if any(c["verdict"] == "ALIVE"
                                         for c in out["configs"]) else "DEAD")
    return out


if __name__ == "__main__":
    depth = int(sys.argv[1]); rids = sys.argv[2:]
    for rid in rids:
        t = time.monotonic(); R = close_row(rid, depth)
        print(f"=== {rid} parent{tuple(R['parent'])} -> child{tuple(R['child'])} "
              f"ell={R['ell']} s'={R['s_prime']} depth={depth} "
              f"[{time.monotonic()-t:.1f}s]")
        for c in R["configs"]:
            print(f"  V'={c['V_prime']} {c['pattern']}")
            print(f"     flat I'_M={c['flat_IM']} I'_m={c['flat_Im']} "
                  f"siblings={c['n_sibling']} base(no-sib) I'_M={c['base_IM']}")
            print(f"     -> {c['verdict']} {c.get('reason','')} "
                  f"completions={c.get('n_completions','-')} "
                  f"survivors={c.get('n_survivors',0)} {c['survivors'][:6]}")
        print(f"  ROW VERDICT (child, depth<={depth}): {R['row_verdict']}\n")
        sys.stdout.flush()
