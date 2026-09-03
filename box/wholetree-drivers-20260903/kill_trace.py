"""Explain, node by node, WHY a row dies under the bare source tree."""
import sys, json
sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B
import opus5_probe as OP


def explain(n, m, Ms, V, **kw):
    T = OP.Tree(n, m, Ms, **kw)
    s = T.s
    lines = []
    if not (T.d[s] > V[s] > F(T.d[s], 2)):
        return ["top window fails"]
    need = tuple(V[i] for i in range(s-1, 1, -1))
    high = (V[s],)
    j = s-1
    danger = True
    idx = 0
    while True:
        dl, L, A, P, Q, lo = T.node(j, high)
        vsel = need[idx]
        rec = T.recenter and dl.denominator == 1 and dl <= 0
        head = (f"  D_{j}: delta={dl} A={A} P={P} Q={Q} S={(Q-1)//A} "
                f"thr={lo} selected V_{j}={vsel} danger={danger}")
        lines.append(head)
        bs = list(range(P % A, P+1, A))
        lines.append(f"      admissible b (mult of the fixed zero root): {bs}")
        okb = []
        for b in bs:
            zmaj = F(b) > lo
            tag = f"b={b}" + (" [zero factor MAJOR]" if zmaj else " [zero minor]")
            if zmaj:
                sub = T.ok(j-1, (b,)+high, danger, None) if j > 2 else None
                if j == 2:
                    good, A1, c12, c13 = T.bottom((b,)+high)
                    nd = danger
                    if nd:
                        lines.append(f"      {tag}: forced zero sibling reaches the "
                                     f"bottom on an all-zero chain -> Prop.5.6 kills it")
                        continue
                    if not good:
                        lines.append(f"      {tag}: zero sibling fails (12)/(13) (A_1={A1})")
                        continue
                else:
                    T._memo = {}
                    if sub is None:
                        lines.append(f"      {tag}: forced zero sibling V_{j}={b} has NO "
                                     f"complete lower major subtree")
                        continue
            okb.append(b)
            lines.append(f"      {tag}: usable")
        if not okb:
            lines.append(f"      => node D_{j} has no admissible partition: ROW DIES here")
            return lines
        # follow the selected path (choose the first usable b that admits it)
        T._memo = {}
        r = T.ok(j, high, danger, need[idx:])
        if r is None:
            lines.append(f"      => selected V_{j}={vsel} does not embed: ROW DIES here")
            return lines
        mode = r["mode"]
        lines.append(f"      selected embeds as the {mode} factor with b={r['b']}, "
                     f"orbits={r['orbits']}")
        danger = danger and (mode == "zero" or rec)
        high = (vsel,) + high
        idx += 1
        j -= 1
        if j == 1:
            lines.append("      reached D_1: (12)/(13) satisfied; row SURVIVES")
            return lines


def report(D, **kw):
    print(f"===== D = {D} =====")
    tot = alive = 0
    for m, Ms, V in B.census(D, Kmin=2, full=True):
        tot += 1
        T = OP.Tree(D, m, Ms, **kw)
        ok = T.embeds(V) is not None
        alive += ok
        print(f"\n row (n,m)=({D},{m}) M={list(Ms)} V={dict(sorted(V.items()))} "
              f"-> {'ALIVE' if ok else 'DEAD'}")
        for L in explain(D, m, Ms, V, **kw):
            print(L)
    print(f"\n D={D}: {tot} baseline rows, {alive} survive\n")


if __name__ == "__main__":
    for D in (105, 117):
        report(D)
