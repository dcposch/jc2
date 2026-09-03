#!/usr/bin/env python3
"""Independent enumeration of full trees for a Moh row and distance-based IM / Im floor.
Does NOT import xu_screen.py.  Uses only Skel (n,m,M,d,V), Def 5.1(3) radii and
level_data (A,P,Q,lo) from the frozen full_tree_partition evaluator, plus its
bottom() (12)/(13) check and the Prop 5.6 danger rule when strict=True.

IM  = sum over major roots alpha of (1 - S(alpha)),  S(alpha) = -ord f_y(alpha) (Lemma 4.1)
Im_floor = 1 + principal_floor + sum over minor children of A_orbit*(S_out/N - 1)^+
principal_floor: V_s/u_s - 1 if u_s == 1 (driver policy) ; 0 if u_s > 1 (driver policy);
                 also reported: sharpened V_s/u_s - 1 for u_s > 1 (gate-derived).
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/tmp/jc2-lane.AQwgL6/inputs")
import moh_skeleton_full as M
import full_tree_partition as FT

def partitions(total, max_coins, start=1):
    """multisets of positive ints (nondecreasing) summing to total with <= max_coins parts"""
    if total == 0:
        yield ()
        return
    if max_coins == 0:
        return
    for v in range(start, total + 1):
        for rest in partitions(total - v, max_coins - 1, v):
            yield (v,) + rest

class Trees:
    def __init__(self, S, strict=True):
        self.S = S; self.strict = strict
        self.E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
        self.req = {i: S.V[i] for i in range(2, S.s)}
        self.us = S.d[S.s] - S.V[S.s]

    def node(self, j, path, Sout, dangerous, embed):
        """Enumerate completions below a level-j node whose disc has N_j roots and whose
        roots see outside sum Sout (= -sum of ord to roots outside the disc).
        Yields (IM, Imfloor) pairs for the subtree. embed: selected child must appear."""
        S = self.S; n, m = S.n, S.m
        delta, L, A, P, Q, lo = self.E.level_data(j, path)
        Nj = F(path[j + 1] * m, S.d[j + 1])
        unit = F(m, S.d[j])
        residue = P % A
        for b in range(residue, P + 1, A):
            if self.strict and b > 0 and P - Q * b == 0:
                continue
            total = (P - b) // A
            for coins in partitions(total, Q // A):
                if self.strict and any(P - Q * v == 0 for v in coins):
                    continue
                children = ([(b, 1, True)] if b > 0 else []) + [(v, A, False) for v in coins]
                if not any(v > lo for v, _, _ in children):
                    continue
                if embed:
                    vreq = self.req[j]
                    if not any(v == vreq and v > lo for v, _, _ in children):
                        continue
                # per-child (IM, Im) option lists
                opts = []
                sel_done = False
                for v, orb, is_zero in children:
                    Nc = v * unit
                    Sout_c = Sout - (Nj - Nc) * delta
                    if v <= lo:
                        contrib = Sout_c / Nc - 1
                        opts.append([(F(0), orb * (contrib if contrib > 0 else F(0)))])
                        continue
                    newpath = self.E.extend(path, j, v)
                    removable = delta.denominator == 1 and delta <= 0
                    newdanger = dangerous and (is_zero or removable)
                    this_embed = embed and (not sel_done) and v == self.req[j]
                    if this_embed: sel_done = True
                    if j == 2:
                        if self.strict and newdanger:
                            opts.append([]); continue
                        ok, _ = self.E.bottom(newpath)
                        if self.strict and not ok:
                            opts.append([]); continue
                        d1 = self.E.radius(1, newpath)
                        Sa = Sout_c - (Nc - 1) * d1
                        opts.append([(orb * Nc * (1 - Sa), F(0))])
                    else:
                        sub = list(self.node(j - 1, newpath, Sout_c, newdanger, this_embed))
                        if not sub:
                            opts.append([]); continue
                        # keep only extreme pairs to bound blowup: max IM, min Im, and both
                        imax = max(sub, key=lambda p: p[0]); imin = min(sub, key=lambda p: p[1])
                        opts.append(sorted({(orb * imax[0], orb * imax[1]), (orb * imin[0], orb * imin[1])}))
                if any(len(o) == 0 for o in opts):
                    continue
                # combine: independent extremes
                IMmax = sum(max(o, key=lambda p: p[0])[0] for o in opts)
                Immin = sum(min(o, key=lambda p: p[1])[1] for o in opts)
                yield (IMmax, Immin)

    def run(self):
        S = self.S
        E = self.E
        path = E.initial_path()
        Np = F(self.us * S.m, S.d[S.s])            # principal minor root count
        Nmaj = F(S.V[S.s] * S.m, S.d[S.s])
        Sout_top = Np                              # major side sees Np roots at distance -1
        res = list(self.node(S.s - 1, path, Sout_top, True, True))
        if not res:
            return None
        IMmax = max(p[0] for p in res); Immin_tree = min(p[1] for p in res)
        princ_driver = (F(S.V[S.s], self.us) - 1) if self.us == 1 else F(0)
        princ_sharp = F(S.V[S.s], self.us) - 1
        return dict(IM_max=IMmax, tree_minor_min=Immin_tree,
                    Im_min_driver=1 + princ_driver + Immin_tree,
                    Im_min_sharp=1 + princ_sharp + Immin_tree, n_trees=len(res))

def show(label, S, strict=True):
    r = Trees(S, strict).run()
    if r is None:
        print(label, "NO TREE"); return
    print(f"{label:45s} strict={strict} IM_max={r['IM_max']} tree_minor_min={r['tree_minor_min']} "
          f"Im_min(driver)={r['Im_min_driver']} Im_min(sharp)={r['Im_min_sharp']} "
          f"kill(driver)={r['IM_max'] < r['Im_min_driver']} trees={r['n_trees']}")

if __name__ == "__main__":
    rows = [
        ("(84,56) M=(64,82) V=(2,3) u_s=1 [killed]", M.Skel(84, 56, [64, 82], {2: 2, 3: 3})),
        ("(144,108) M=(126,135,142) V=(3,7,6) u_s=3 [killed]", M.Skel(144, 108, [126, 135, 142], {2: 3, 3: 7, 4: 6})),
        ("(64,48) M=(52,62) V=(3,3) [survivor]", M.Skel(64, 48, [52, 62], {2: 3, 3: 3})),
        ("(99,66) M=(77,97) V=(8,8) u_s=3 [survivor]", M.Skel(99, 66, [77, 97], {2: 8, 3: 8})),
        ("(84,56) M=(72,82) V=(5,3) [Xu: 10>=4]", M.Skel(84, 56, [72, 82], {2: 5, 3: 3})),
        ("(75,50) M=(55,73) V=(2,4) [Xu split ii 4<6; (i) 8>=4]", M.Skel(75, 50, [55, 73], {2: 2, 3: 4})),
    ]
    for lab, S in rows:
        show(lab, S, True)
        show(lab, S, False)
