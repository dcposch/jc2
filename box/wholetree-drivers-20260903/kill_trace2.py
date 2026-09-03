"""D=105 and D=117: which sibling kills each baseline row (Kmin=16 census)."""
import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B, opus5_probe as OP

def node_report(T, j, high, V, danger, gate):
    dl, L, A, P, Q, lo = T.node(j, high)
    out = [f"    D_{j}: delta={dl} A={A} P={P} Q={Q} thr={lo} selected V_{j}={V[j]}"]
    bs = list(range(P % A, P + 1, A))
    out.append(f"        zero-root multiplicity b == P mod A == {P%A} (mod {A}) -> b in {bs[:8]}")
    usable = []
    for b in bs:
        if not (F(b) > lo):
            out.append(f"        b={b}: minor, stops (p.200(5))")
            usable.append(b); continue
        nh = (b,) + high
        if j == 2:
            good, A1, c12, c13 = T.bottom(nh)
            if danger and (not gate or not T.free_exponents(nh)):
                out.append(f"        b={b}: FORCED MAJOR zero sibling; all-zero chain reaches "
                           f"D_1 -> Prop.5.6")
                continue
            if not good:
                out.append(f"        b={b}: FORCED MAJOR zero sibling fails (12)/(13) at A_1={A1}")
                continue
        else:
            T._memo = {}
            if T.ok(j-1, nh, danger, None) is None:
                out.append(f"        b={b}: FORCED MAJOR zero sibling has no lower major tower")
                continue
        usable.append(b)
        out.append(f"        b={b}: usable")
    return out, usable

for D in (105, 117):
    for label, kw in (("bare source tree (charged C_FULL_TREE)", dict()),
                      ("gap-free gated tree", dict(gate=True))):
        print(f"\n######## D={D} -- {label} ########")
        nlive = 0; ntot = 0
        for m, Ms, V in B.census(D, Kmin=16, full=True):
            ntot += 1
            T = OP.Tree(D, m, Ms, **kw)
            ok = T.embeds(V) is not None
            nlive += ok
            print(f"\n  (n,m)=({D},{m}) M={list(Ms)} V={dict(sorted(V.items()))} -> "
                  f"{'ALIVE' if ok else 'DEAD'}")
            high = (V[T.s],); danger = True
            for j in range(T.s-1, 1, -1):
                lines, usable = node_report(T, j, high, V, danger, kw.get('gate', False))
                for L in lines: print(L)
                if not usable:
                    print(f"        => no admissible partition at D_{j}: killed here")
                    break
                dl = T.delta(j, high)
                danger = danger and (V[j] == (T.node(j, high)[3] % T.node(j, high)[2])
                                     or (kw.get('gate') and dl.denominator == 1))
                high = (V[j],) + high
        print(f"\n  D={D}: {ntot} baseline rows, {nlive} survive under {label}")
