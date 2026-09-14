"""UNCAPPED sibling-tower closure for the T3 residue (R039,R040,R048,R063)
and re-audit of the six depth<=2 kills (R025-R028,R057,R058).

Depth is NOT capped by fiat.  It is bounded by a printed lattice fact:

  Xu Lemma 2.1(ii): for any disc, rho_f : rho_g = m : n, so every packet's
  rho_f is a positive multiple of  unit = m/gcd(n,m).   Put r = rho/unit.
  A split has >= 2 parts, each a positive multiple of unit, so
  max_j r_j <= r - 1:  r STRICTLY DROPS at every split.
  Hence any tower rooted at a packet with r units has split depth <= r - 1,
  and depth = r-1 is EXHAUSTIVE, not a cap.

  Second, independent bound: the tower parameter W = n - M strictly increases
  along a packet (Moh Def 5.1(2) window) and a major packet goes final at
  W = n+m (Xu Lemma 4.4(i)), so W ranges over the finite set
  (W_born, n+m) with rho*W/m in Z (Moh Prop 4.6(2)).  Depth <= #that set.

Constraint layers (each switchable, so the report can say what does the killing):
  BASE   Prop 4.6(2) Q=rho*W/m in Z ; #parts <= Q (4.6(3),(4)) ;
         Lemma 2.1(ii) parts in unit*Z ; kappa_j != 0 ; some kappa_j > 0 (Def 5.1(2)/A.3)
  GO     Galois orbit law: split pattern = one optional singleton + orbits of
         A = den(L*delta) equal parts ; at a FINAL disc rho_f,rho_g = 0 or 1 mod A
  LEMA   primitivity: gcd of reduced multiplicities = 1
  LEMB   cross-tower consistency: W == n (mod d_ancestor)
"""
from fractions import Fraction as Q
from math import gcd
from functools import reduce
import sys, itertools, json

sys.path.insert(0, '/home/ubuntu/jc2/box/t3-residue-20260906')
from exact_contact import tower, all_flat, Jfinal

ROSTER = '/tmp/jc2-lane.slTSed/inputs/roster.jsonl'

def lcm(a, b): return a*b//gcd(a, b)
def lcmn(v):
    a = 1
    for x in v: a = lcm(a, x)
    return a

# ---------- shape enumeration: NO orbit cap ----------
def orbit_parts(total, unit, maxpart=None):
    """partitions of `total` into positive multiples of `unit`, no cap on #parts"""
    if maxpart is None: maxpart = total
    if total == 0:
        yield ()
        return
    k = min(total, maxpart); k -= k % unit
    while k >= unit:
        for rest in orbit_parts(total-k, unit, k):
            yield (k,)+rest
        k -= unit

def shapes(rho, unit, A, use_GO, use_LEMA):
    """multisets of parts summing to rho.  With GO: [z] optional + A equal copies
    of each orbit size.  Without GO: any partition into multiples of unit."""
    out = []
    if not use_GO:
        for pt in orbit_parts(rho, unit):
            if len(pt) < 2: continue
            if use_LEMA and reduce(gcd, [p//unit for p in pt]) != 1: continue
            out.append((0, (), tuple(pt)))
        return out
    for z in range(0, rho+1, unit):
        rest = rho - z
        if rest % A: continue
        per = rest//A
        if per == 0: continue
        for orb in orbit_parts(per, unit):
            parts = ([z] if z > 0 else []) + [r for r in orb for _ in range(A)]
            if len(parts) < 2: continue
            if use_LEMA and reduce(gcd, [p//unit for p in parts]) != 1: continue
            out.append((z, tuple(orb), tuple(parts)))
    return out

# ---------- the packet closure ----------
class Closure:
    def __init__(self, n, m, unit, d, GO=True, LEMA=True, LEMB=True,
                 minor_split=False, maxdepth=None, GOFIN=True):
        self.n, self.m, self.unit, self.d = n, m, unit, d
        self.GO, self.LEMA, self.LEMB = GO, LEMA, LEMB
        self.minor_split = minor_split
        self.GOFIN = GOFIN            # GO split-shape and GO final-congruence, separately
        self.maxdepth = maxdepth            # None = exhaustive (r-1)
        self.memo = {}
        self.nodes = 0
        self.depth_reached = 0
        self.enum = 0                       # candidate towers enumerated

    def run(self, rho, kappa, Wborn, L, depth=0):
        """dict {dIM : (min dIm, witness)} of every admissible completion."""
        key = (rho, kappa, Wborn, L)
        if key in self.memo: return self.memo[key]
        self.memo[key] = {}                 # cycle guard (W strictly increases anyway)
        n, m, unit = self.n, self.m, self.unit
        self.nodes += 1
        self.depth_reached = max(self.depth_reached, depth)
        res = {}
        def put(k, v, w):
            if k not in res or v < res[k][0]: res[k] = (v, w)
        # --- terminate ---
        if kappa < 0:
            put(Q(0), -kappa/rho, f"minor(rho={rho},delta={1-kappa/rho})")
            self.enum += 1
        elif kappa > 0:
            dfin = 1 - Q((n+m)*kappa, (n+m)*rho - m)
            ok = True
            if self.GO and self.GOFIN:
                Afin = (L*dfin).denominator
                rgo = Q(n*rho, m)
                ok = (rho % Afin in (0, 1) and rgo.denominator == 1
                      and int(rgo) % Afin in (0, 1))
            if ok:
                put(Jfinal(n, m, rho, kappa), Q(0),
                    f"FINAL(rho={rho},delta={dfin})")
                self.enum += 1
        # --- split ---
        may_split = (kappa > 0) or self.minor_split
        if may_split and rho >= 2*unit and (self.maxdepth is None or depth < self.maxdepth):
            for W in range(Wborn+1, n+m):
                if self.LEMB and (n-W) % self.d: continue
                q = Q(rho*W, m)
                if q.denominator != 1: continue
                Qd = int(q)
                if Qd < 2: continue
                delta = 1 - Q(W*kappa, W*rho - m)
                A = (L*delta).denominator
                L2 = lcm(L, delta.denominator)
                for z, orb, parts in shapes(rho, unit, A, self.GO, self.LEMA):
                    if len(parts) > Qd: continue
                    kj = [Q(kappa*(p*W - m), rho*W - m) for p in parts]
                    if any(k == 0 for k in kj): continue
                    if not any(k > 0 for k in kj): continue
                    sub = [self.run(p, k, W, L2, depth+1) for p, k in zip(parts, kj)]
                    if any(not s for s in sub): continue
                    acc = {Q(0): (Q(0), "")}
                    for s in sub:                       # min-plus convolution
                        nxt = {}
                        for a, (b, wa) in acc.items():
                            for c, (e, wc) in s.items():
                                k2, v2 = a+c, b+e
                                if k2 not in nxt or v2 < nxt[k2][0]:
                                    nxt[k2] = (v2, wa+"|"+wc)
                        acc = nxt
                    tag = f"SPLIT@W={W}(M={n-W},delta={delta},A={A},z={z},orb={orb})"
                    for a, (b, w) in acc.items():
                        put(a, b, tag+"["+w+"]")
                        self.enum += 1
        self.memo[key] = res
        return res

# ---------- row driver ----------
def row_verdict(rid, rows, GO=True, LEMA=True, LEMB=True, minor_split=False,
                dmode='dtrue', maxdepth=None, verbose=True, GOFIN=True):
    src = rows[rid]['source']; T = tower(src)
    n, m, s = T['n'], T['m'], T['s']
    g = gcd(n, m)
    unit_floor = m//g                            # Xu Lemma 2.1(ii), the weakest floor
    out = dict(row=rid, n=n, m=m, s=s, unit_floor=unit_floor, gcd=g, configs=[],
               alive=False, layers=dict(GO=GO, LEMA=LEMA, LEMB=LEMB,
                                        minor_split=minor_split, dmode=dmode,
                                        GOFIN=GOFIN))
    tot_nodes = tot_enum = 0; maxd = 0; rmax = 0
    for c in all_flat(T):
        dtrue = {}
        for i, (z, orb, ix) in c['pattern'].items():
            gg = 0
            for r in ([z] if z > 0 else [])+list(orb): gg = gcd(gg, r)
            dtrue[i] = T['d'][i]//gg
        dtrue[s] = T['d'][s]//gcd(T['d'][s]-T['V'][s], T['V'][s])
        sib = [l for l in c['leaves'] if l['kind'] == 'major-sibling']
        base_IM = c['IM'] - sum(l['IM_each']*l['copies'] for l in sib)
        base_Im = c['Im']
        if minor_split:
            # CONTROL: minor packets are NOT forced to terminate at once; give each
            # the same closure.  (Terminating them at once is a hypothesis, and the
            # claim that it minimises I_m must be tested, not assumed.)
            mins = [l for l in c['leaves'] if l['kind'] == 'minor']
            base_Im = base_Im - sum(l['copies']*(l['delta']-1) for l in mins)
            sib = sib + mins
        pools = []; ok = True; sibdesc = []
        for l in sib:
            i = l['level']; rho = int(l['rho'])
            kap = l['kappa'] if 'kappa' in l else rho*(1-l['delta'])
            W0 = n - T['M'][i]
            L = lcmn([T['delta'][j].denominator for j in range(i, s+1)])
            dd = dtrue[i] if dmode == 'dtrue' else (g if dmode == 'gcd' else 1)
            # Moh Prop 4.6(1): f_sigma_i = c*p^{m/d_i}, so every sub-packet of D_i
            # has rho_f in (m/d_i)Z.  d_i | M_1 = -m for i>=2, so this is integral.
            # Without Lemma B the deeper divisor is gcd(d_i,M) <= d_i, i.e. unit only
            # GROWS with depth; m/d_i is therefore the MOST PERMISSIVE unit throughout.
            unit = m//dtrue[i] if dmode == 'dtrue' else unit_floor
            C = Closure(n, m, unit, dd, GO, LEMA, LEMB, minor_split, maxdepth, GOFIN)
            R = C.run(rho, kap, W0, L)
            tot_nodes += C.nodes; tot_enum += C.enum
            maxd = max(maxd, C.depth_reached); rmax = max(rmax, rho//unit)
            sibdesc.append(dict(level=i, mult=l['mult'], rho=rho, kappa=str(kap),
                                copies=l['copies'], W0=W0, L=L, d=dd, unit=unit,
                                r_units=rho//unit, depth_bound=rho//unit-1,
                                outcomes=len(R)))
            if not R: ok = False; break
            pools.append([(a, b, l['copies']) for a, (b, w) in R.items()])
        rec = dict(pattern={str(k): [v[0], list(v[1]), v[2]] for k, v in c['pattern'].items()},
                   flat_IM=str(c['IM']), flat_Im=str(c['Im']),
                   n_siblings=len(sib), siblings=sibdesc)
        if not ok:
            rec['verdict'] = 'DEAD: a major sibling has NO admissible completion'
            out['configs'].append(rec); continue
        best = {}
        for combo in itertools.product(*pools) if pools else [()]:
            IM = base_IM + sum(a*k for a, b, k in combo)
            Im = base_Im + sum(b*k for a, b, k in combo)
            if IM.denominator == 1 and IM >= Im:
                if IM not in best or Im < best[IM]: best[IM] = Im
        if best:
            out['alive'] = True
            rec['verdict'] = 'SURVIVES'
            rec['survivors'] = [[str(k), str(v)] for k, v in sorted(best.items())][:6]
        else:
            rec['verdict'] = 'DEAD: no completion with I_M in Z and I_M >= I_m'
        out['configs'].append(rec)
    out['nodes'] = tot_nodes; out['towers_enumerated'] = tot_enum
    out['max_depth_reached'] = maxd; out['depth_bound_r_minus_1'] = max(0, rmax-1)
    if verbose:
        print(f"=== {rid} ({n},{m}) s={s} unit_floor={unit_floor} layers GO={GO} A={LEMA} B={LEMB} "
              f"minor_split={minor_split} d={dmode} maxdepth={maxdepth}")
        for rec in out['configs']:
            print(f"    pat {rec['pattern']} sibs={rec['n_siblings']} -> {rec['verdict']}"
                  + (f"  e.g. {rec.get('survivors')[:3]}" if 'survivors' in rec else ""))
        print(f"    nodes={tot_nodes} towers={tot_enum} depth_reached={maxd} "
              f"depth_bound={out['depth_bound_r_minus_1']}  ROW: "
              f"{'ALIVE' if out['alive'] else 'DEAD'}")
        sys.stdout.flush()
    return out

if __name__ == '__main__':
    rows = {json.loads(l)['row_id']: json.loads(l) for l in open(ROSTER)}
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('rows', nargs='+')
    ap.add_argument('--no-go', action='store_true')
    ap.add_argument('--no-gofinal', action='store_true')
    ap.add_argument('--no-a', action='store_true')
    ap.add_argument('--no-b', action='store_true')
    ap.add_argument('--minor-split', action='store_true')
    ap.add_argument('--dmode', default='dtrue')
    ap.add_argument('--maxdepth', type=int, default=None)
    ap.add_argument('--json', default=None)
    a = ap.parse_args()
    res = [row_verdict(r, rows, GO=not a.no_go, LEMA=not a.no_a, LEMB=not a.no_b,
                       minor_split=a.minor_split, dmode=a.dmode,
                       maxdepth=a.maxdepth, GOFIN=not a.no_gofinal) for r in a.rows]
    if a.json: json.dump(res, open(a.json, 'w'), indent=1)
