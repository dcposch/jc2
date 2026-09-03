import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
from math import gcd
import moh_skeleton_full_frozen as B, opus5_probe as OP

def evaluate(n, m, Ms, V, label):
    S = B.Skel(n, m, list(Ms), dict(V))
    base = S.windows_ok() and S.full_ok()
    res = {"label": label, "n": n, "m": m, "Ms": list(Ms), "V": dict(V),
           "d": {k: S.d[k] for k in sorted(S.d)},
           "deltas": {k: str(S.delta[k]) for k in sorted(S.delta)},
           "A": {j: S.A(j) for j in range(1, S.s)},
           "baseline_1_13": base}
    if not base:
        return res
    for name, kw in (("partition_only", {}),
                     ("partition+ODE+pass", dict(ode=True, capacity=True, passport=True)),
                     ("GATED", dict(gate=True)),
                     ("GATED+ODE+pass", dict(gate=True, ode=True, capacity=True, passport=True)),
                     ("ungated C_FULL_TREE", {}),
                     ("ungated+ODE+pass", dict(ode=True, capacity=True, passport=True)),
                     ("ungated+recentre+ODE+pass", dict(recenter=True, ode=True, capacity=True, passport=True))):
        T = OP.Tree(n, m, Ms, **kw)
        if name.startswith("partition"):
            T._memo = {}
            if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
                r = None
            else:
                need = tuple(V[i] for i in range(T.s-1, 1, -1))
                r = T.ok(T.s-1, (V[T.s],), False, need)
        else:
            r = T.embeds(V)
        res[name] = r is not None
        if name == "ungated C_FULL_TREE" and r is None:
            res["free_exponents_on_selected_chain"] = [
                str(x) for x in OP.Tree(n, m, Ms, gate=True).free_exponents(
                    tuple(V[i] for i in range(2, T.s+1)))]
    return res

print("=== A2=6 ray:  n=9P, m=6P, M2=4P, M3=9P-2, V2=1, V3=6t+5,  P=7t+6 ===")
for t in range(4):
    P = 7*t+6
    n, m = 9*P, 6*P
    r = evaluate(n, m, (4*P, 9*P-2), {2: 1, 3: 6*t+5}, f"A2=6 ray t={t}")
    print(f"\n t={t}: D={n} m={m} M=[{4*P},{9*P-2}] V2=1 V3={6*t+5}  d={r['d']}")
    print(f"   deltas={r['deltas']}  A={r['A']}   baseline(1)-(13)={r['baseline_1_13']}")
    if r['baseline_1_13']:
        for k in ("partition_only","partition+ODE+pass","GATED","GATED+ODE+pass",
                  "ungated C_FULL_TREE","ungated+ODE+pass","ungated+recentre+ODE+pass"):
            print(f"     {k:28s} {'SURVIVES' if r[k] else 'DIES'}")
        if "free_exponents_on_selected_chain" in r:
            print(f"     free centre exponents on the selected chain: {r['free_exponents_on_selected_chain']}")

print("\n=== Sol L=8a+5 ray:  n=21L, m=14L, M2=7(3L+1)/4, M3=21L-2, V2=1, V3=5 ===")
for a in range(4):
    L = 8*a+5
    n, m = 21*L, 14*L
    M2 = 7*(3*L+1)//4
    assert 7*(3*L+1) % 4 == 0
    r = evaluate(n, m, (M2, 21*L-2), {2: 1, 3: 5}, f"L={L}")
    print(f"\n a={a}: L={L} D={n} m={m} M=[{M2},{21*L-2}] V2=1 V3=5  d={r['d']}")
    print(f"   deltas={r['deltas']}  A={r['A']}   baseline(1)-(13)={r['baseline_1_13']}")
    if r['baseline_1_13']:
        for k in ("partition_only","partition+ODE+pass","GATED","GATED+ODE+pass",
                  "ungated C_FULL_TREE","ungated+ODE+pass","ungated+recentre+ODE+pass"):
            print(f"     {k:28s} {'SURVIVES' if r[k] else 'DIES'}")
        if "free_exponents_on_selected_chain" in r:
            print(f"     free centre exponents on the selected chain: {r['free_exponents_on_selected_chain']}")
