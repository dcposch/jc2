import sys, time, json; sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B, opus5_probe as OP

SCREENS = {
    "baseline":        None,
    "partition_only":  dict(),
    "partition_pass":  dict(ode=True, capacity=True, passport=True),
    "gated":           dict(gate=True),
    "gated_pass":      dict(gate=True, ode=True, capacity=True, passport=True),
    "ungated":         dict(),
    "ungated_pass":    dict(ode=True, capacity=True, passport=True),
}

def alive(n, m, Ms, V, name, kw):
    if name == "baseline":
        return True
    T = OP.Tree(n, m, Ms, **kw)
    if name.startswith("partition"):
        T._memo = {}
        if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
            return False
        need = tuple(V[i] for i in range(T.s-1, 1, -1))
        return T.ok(T.s-1, (V[T.s],), False, need) is not None
    return T.embeds(V) is not None

dlo, dhi = 48, 120
res = {k: {"rows":0, "groups":set(), "uni":0, "degs":set(), "gitems":{}} for k in SCREENS}
t0 = time.time()
for n in range(dlo, dhi+1):
    print(f"  n={n} ({time.time()-t0:.0f}s)", flush=True)
    for m, Ms, V in B.census(n, Kmin=16, full=True):
        S = B.Skel(n, m, list(Ms), V)
        g = (n, m, tuple(Ms), S.V[S.s])
        for name, kw in SCREENS.items():
            if alive(n, m, Ms, V, name, dict(kw) if kw is not None else None):
                r = res[name]
                r["rows"] += 1; r["groups"].add(g); r["degs"].add(n)
                r["gitems"].setdefault(g, []).append((S.V[2], S.q(), S.u))
print(f"enumeration wall {time.time()-t0:.1f}s")
base_degs = res["baseline"]["degs"]
out = {}
for name in SCREENS:
    r = res[name]
    uni = sum(1 for g, items in r["gitems"].items() if B.uni_hits(items, 6, None))
    out[name] = {"rows": r["rows"], "groups": len(r["groups"]), "uni_N_ge_6": uni,
                 "empty_degrees_among_baseline": sorted(base_degs - r["degs"])}
    print(f"{name:16s} rows={r['rows']:6d} groups={len(r['groups']):6d} UNI(N>=6)={uni:5d} "
          f"newly-empty degrees={len(sorted(base_degs - r['degs']))}")
json.dump(out, open("drange-48-120.json","w"), indent=1, sort_keys=True)
for name in SCREENS:
    print(f"\n{name}: empty degrees among baseline-nonempty:\n  {out[name]['empty_degrees_among_baseline']}")
