#!/usr/bin/env python3
"""BRANCH-ORBITS: Galois orbit size of bottom-major discs, and the orbit-aware knapsack.

Moh 1983 p.201 search (8)-(11) and p.188 (conjugations of k((t^{1/A})) over k((t))),
read from the page images.  Imports the charged d1floor / moh_skeleton_N enumerator
only; every orbit formula is derived here.

Notation (Moh p.201):
  L_r     = lcm of reduced denominators of delta_s, ..., delta_r
  A_{r-1} = reduced denominator of L_r * delta_{r-1}
  deg p at D_{r-1} = V_r * d_{r-1} / d_r
  (9)  V_r (d_{r-1}/d_r) = Delta_{r-1} A_{r-1} + box_{r-1}
  Galois tbar -> omega tbar of order A_{r-1} acts on the local pi-coordinate.

Fail-closed: any check() failure aborts before a filter number is printed.
"""
from __future__ import annotations
import os, sys, time, math
from fractions import Fraction as F
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d1floor import Skel, census, qval, MOH_SURVIVORS

FAILURES = []
NCHECK = [0]

def check(name, cond, detail=""):
    NCHECK[0] += 1
    if not cond:
        FAILURES.append((name, detail))
        print("  FAIL  %-60s %s" % (name, detail))
    return cond

def lcm(a, b):
    return a // gcd(a, b) * b if a and b else 0

def lcm_list(xs):
    out = 1
    for x in xs:
        out = lcm(out, int(x))
    return out

# ---------------------------------------------------------------------------
# Moh search (8): denominator increments A_i
# ---------------------------------------------------------------------------
def moh_A(S):
    """A[r] = reduced denominator of L_{r+1} * delta_r, r = 1..s-1,
       with L_{r+1} = lcm of dens of delta_s, ..., delta_{r+1}.
       Matches Moh p.201 (8) verbatim (image)."""
    dens = {i: S.delta[i].denominator for i in range(1, S.s + 1)}
    A = {}
    L = 1
    for r in range(S.s, 1, -1):          # r = s, s-1, ..., 2
        L = lcm(L, dens[r])              # L = lcm dens of delta_s .. delta_r
        val = F(L) * S.delta[r - 1]
        A[r - 1] = val.denominator
    return A, dens

def deg_p_at(S, i):
    """deg p(pi) at D_i  = V_{i+1} * d_i / d_{i+1}   (Def 5.1(4) + Prop 4.6(4))."""
    return S.V[i + 1] * S.d[i] // S.d[i + 1]

def a1(S):
    """# g-roots in D_1 = (n/d_2) V_2 = e V_2."""
    return S.n * S.V[2] // S.d[2]

def slots_top_major(S):
    """deg p at the unique major child D_{s-1} of D_s.
       These are the child-slots of the L_1 cluster.  For s=3 this equals u."""
    return deg_p_at(S, S.s - 1)

def divmod_A(S, r_minus_1):
    """Division algorithm (9) at index r-1: deg p(D_{r-1}) = Delta A + box."""
    Amap, _ = moh_A(S)
    A = Amap[r_minus_1]
    deg = deg_p_at(S, r_minus_1)
    Delta, box = divmod(deg, A)
    return A, Delta, box, deg

# ---------------------------------------------------------------------------
# controls against Moh's published rows and against Def 5.1 arithmetic
# ---------------------------------------------------------------------------
def control_moh_rows_A():
    print("\n-- CONTROL A: Moh (8) A_i and (9) division on the six published rows --")
    print("   %-22s %3s %3s %8s %8s %6s %6s %8s %8s %s" %
          ("row", "s", "u", "delta_2", "delta_1", "A2", "A1", "deg_p(D2)", "a1", "A|a1"))
    for (n, m, Ms, Vs, lab, pub) in MOH_SURVIVORS:
        S = Skel(n, m, list(Ms), Vs)
        check("windows %s" % lab, S.windows_ok())
        Amap, dens = moh_A(S)
        A1 = Amap[1]
        A2 = Amap.get(2)
        dp2 = deg_p_at(S, 2) if S.s >= 3 else None
        aa = a1(S)
        print("   %-22s %3d %3s %8s %8s %6s %6s %8s %8s %s" %
              (lab, S.s, str(S.u), str(S.delta[2]), str(S.delta[1]),
               A2, A1, dp2, aa, ("yes" if aa % A1 == 0 else "NO")))
        # delta_s = -1 has den 1
        check("delta_s=-1 %s" % lab, S.delta[S.s] == F(-1))
        check("den delta_s = 1 %s" % lab, dens[S.s] == 1)
        # u integer
        check("u integer %s" % lab, S.u.denominator == 1)
        # slots at D_{s-1}
        sl = slots_top_major(S)
        check("slots D_{s-1} integer %s" % lab, sl * S.d[S.s] == S.V[S.s] * S.d[S.s - 1])
        # for s=3, slots = u
        if S.s == 3:
            check("s=3 slots=u %s" % lab, sl == int(S.u), "%s vs %s" % (sl, S.u))
        # (9) at r=2: V_2 (d_1/d_2) = a1
        A, Delta, box, deg = divmod_A(S, 1)
        check("(9) deg p(D1)=a1 %s" % lab, deg == aa, "%s vs %s" % (deg, aa))
        check("(9) a1 = Delta A + box %s" % lab, aa == Delta * A + box)
        # published delta match
        if pub:
            check("pub delta %s" % lab, (S.delta[2], S.delta[1]) == pub)

def divides(a, b):
    return b % a == 0 if a else False

def control_A_identities(nmax=80):
    print("\n-- CONTROL B: A_i identities on the census n<=%d --" % nmax)
    seen = 0
    a1_div = 0
    a1_ndiv = 0
    slots_eq_u = 0
    slots_lt_u = 0
    gen_sz_gt_u = 0
    gen_sz_eq_1 = 0
    for n in range(48, nmax + 1):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok():
                continue
            seen += 1
            Amap, dens = moh_A(S)
            # L at r=s is den(delta_s)=1; A_{s-1} = den(delta_{s-1})
            if S.s >= 2:
                check("A_{s-1}=den(delta_{s-1}) n=%d" % n,
                      Amap[S.s - 1] == dens[S.s - 1],
                      "%s vs %s" % (Amap[S.s - 1], dens[S.s - 1]))
            aa = a1(S)
            A1 = Amap[1]
            if aa % A1 == 0:
                a1_div += 1
            else:
                a1_ndiv += 1
            sl = slots_top_major(S)
            u = int(S.u)
            if sl == u:
                slots_eq_u += 1
            elif sl < u:
                slots_lt_u += 1
            else:
                check("slots <= u n=%d" % n, sl <= u, "%s > %s" % (sl, u))
                return
            # generic last-split orbit size A1; product of A_1..A_{s-2}
            prod = 1
            for j in range(1, S.s - 1):
                prod *= Amap[j]
            if prod == 1:
                gen_sz_eq_1 += 1
            if prod * S.V[2] > u:
                gen_sz_gt_u += 1
            if seen > 80000:
                break
        if seen > 80000:
            break
    print("   V-skeletons %d; A|a1 %d (%.1f%%); A not| a1 %d" %
          (seen, a1_div, 100.0 * a1_div / max(1, seen), a1_ndiv))
    print("   slots(D_{s-1})=u : %d ; slots<u : %d" % (slots_eq_u, slots_lt_u))
    print("   generic prod_{j=1..s-2} A_j == 1 : %d ; prod*V2 > u : %d" %
          (gen_sz_eq_1, gen_sz_gt_u))
    check("census A identities ran", seen > 0)

def control_s3_slots():
    print("\n-- CONTROL C: for s=3, deg p(D_2) = V_3 d_2/d_3 = u  (algebra) --")
    # u = V_s K / d_s; K=d_2; for s=3, d_s=d_3, V_s=V_3, so u = V_3 d_2 / d_3
    seen = 0
    for n in range(48, 101):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok() or S.s != 3:
                continue
            seen += 1
            sl = S.V[3] * S.d[2] // S.d[3]
            if not check("s=3 slots=u n=%d" % n, sl == int(S.u),
                         "%s vs %s (K=%s d3=%s)" % (sl, S.u, S.K, S.d[3])):
                return
            if seen > 20000:
                break
        if seen > 20000:
            break
    print("   %d s=3 V-skeletons, slots=u always" % seen)

# ---------------------------------------------------------------------------
# orbit-size of a bottom disc, two readings
# ---------------------------------------------------------------------------
def last_split_orbit_size(S):
    """Relative Galois orbit size of a nonzero-center child of D_2: A_1.
       0-center child: 1.  Returned as (A1, a1_divides, Delta, box)."""
    Amap, _ = moh_A(S)
    A1 = Amap[1]
    aa = a1(S)
    Delta, box = divmod(aa, A1)
    return A1, (aa % A1 == 0), Delta, box

def generic_orbit_size_from_Dsm1(S):
    """Product of relative A_j for j=1..s-2: generic (all nonzero centers)
       orbit size of D_1 inside the Galois-fixed unique major D_{s-1}.
       A_{s-1} is excluded because D_{s-1} is the unique major child of D_s
       (Prop 4.5, two linear factors, different multiplicities) and is
       0-centered by the coordinate change of Lemma 6.1 (8)."""
    Amap, _ = moh_A(S)
    prod = 1
    for j in range(1, S.s - 1):
        prod *= Amap[j]
    return prod

# ---------------------------------------------------------------------------
# knapsack: packets
# ---------------------------------------------------------------------------
def packet_items(S, Nhi, mode="s3strict"):
    """Items contributed by ONE V-assignment, as (weight, value, tag).

    weight = # of V_2-slots consumed = |O| * V_2
    value  = contribution to N     = |O| * V_2 * q

    mode:
      gen       size-1 packets only (old general knapsack)
      both      Z (size 1) and NZ (size A1), every s
      nz        NZ only, |O|=A1 (A1=1 => size 1)
      s3strict  PROVED-HERE for s=3: Prop 5.6 kills Z (sigma_1 = pi t^{delta_1}),
                so NZ only.  For s>3, both Z and NZ (a 0-center at the last
                split is allowed if some earlier center is nonzero, so sigma_1
                is not monomial).

    Mixing packets from different V-assignments of the same group is the
    several-orbits case: each orbit carries its own lower-V data.
    """
    q = qval(S)
    v2 = S.V[2]
    A1, a1div, Delta, box = last_split_orbit_size(S)
    u = int(S.u)
    out = []
    allow_Z = False
    allow_NZ = False
    if mode == "gen":
        allow_Z = True
    elif mode == "both":
        allow_Z = True
        allow_NZ = A1 > 1
    elif mode == "nz":
        allow_NZ = True
    elif mode == "s3strict":
        if S.s == 3:
            allow_NZ = True          # 0-center at last split => Prop 5.6
        else:
            allow_Z = True
            allow_NZ = A1 > 1
    else:
        raise ValueError(mode)
    if allow_Z:
        w1 = v2
        c1 = v2 * q
        if w1 <= u and 0 < c1 <= Nhi:
            out.append((w1, c1, "Z"))
    if allow_NZ:
        wA = A1 * v2
        cA = A1 * v2 * q
        if wA <= u and 0 < cA <= Nhi:
            out.append((wA, cA, "NZ"))
    return out

def lcm_denoms(vals):
    D = 1
    for v in vals:
        D = lcm(D, v.denominator)
    return D

def knapsack_fracpart(items, u, Nlo, Nhi, CAP_STATES=4000):
    """Exact unbounded knapsack.  DP over (weight, reachable sums).

    Each item is (weight w, value c as Fraction, [, tag]).  Unbounded.
    N = sum copies * c must be an integer in [Nlo, Nhi], total weight <= u.

    Cheap path: one packet type already hits.  Then complete unbounded
    DP over weights, storing Fractions pruned to <= Nhi; per-weight set
    cap CAP_STATES.  Capped + no hit => UNDECIDED (surviving; kill is a floor).
    """
    if not items:
        return False, False, 0
    uniq = {}
    for trip in items:
        w, c = trip[0], trip[1]
        if w <= 0 or c <= 0 or c > Nhi:
            continue
        uniq[(int(w), c)] = True
    items = list(uniq)
    if not items:
        return False, False, 0
    # cheap: copies of a single packet
    for (w, c) in items:
        kmax = u // w
        for k in range(1, kmax + 1):
            val = k * c
            if val > Nhi:
                break
            if val.denominator == 1 and Nlo <= val <= Nhi:
                return True, False, 0
    # cheap: two packet types.  Hard cap on types and copies -- this is
    # a sufficient hit, not a completeness claim; the DP below is complete
    # up to CAP.
    if 2 <= len(items) <= 10:
        its = sorted(items)
        L = len(its)
        for i in range(L):
            w1, c1 = its[i]
            k1max = min(u // w1, 8)
            for k1 in range(0, k1max + 1):
                s1 = k1 * c1
                if s1 > Nhi:
                    break
                rem = u - k1 * w1
                for j in range(i + 1, L):
                    w2, c2 = its[j]
                    if w2 > rem:
                        continue
                    k2max = min(rem // w2, 8)
                    for k2 in range(1, k2max + 1):
                        val = s1 + k2 * c2
                        if val > Nhi:
                            break
                        if val.denominator == 1 and Nlo <= val <= Nhi:
                            return True, False, 0
    D = lcm_denoms([c for (_, c) in items])
    if D <= 1500:
        return _bitset_dp(items, u, Nlo, Nhi, D)
    return knapsack_fraction_sets(items, u, Nlo, Nhi, CAP_STATES)

def _bitset_dp(items, u, Nlo, Nhi, D):
    scaled = [(w, int(c * D)) for (w, c) in items]
    NhiS = int(Nhi) * D
    mask = (1 << (NhiS + 1)) - 1
    reach = [0] * (u + 1)
    reach[0] = 1
    for (w, n) in scaled:
        if n > NhiS:
            continue
        for tw in range(w, u + 1):
            src = reach[tw - w]
            if src:
                reach[tw] |= (src << n) & mask
    target = 0
    for N in range(int(Nlo), int(Nhi) + 1):
        target |= 1 << (N * D)
    for tw in range(1, u + 1):
        if reach[tw] & target:
            return True, False, 1
    return False, False, 1

def knapsack_fraction_sets(items, u, Nlo, Nhi, CAP_STATES):
    """Complete unbounded DP: for each item, push sums along increasing weight."""
    reach = [set() for _ in range(u + 1)]
    reach[0].add(F(0))
    nstates = 1
    capped = False
    for (w, c) in items:
        for tw in range(w, u + 1):
            if not reach[tw - w]:
                continue
            dst = reach[tw]
            for s0 in reach[tw - w]:
                s1 = s0 + c
                if s1 > Nhi:
                    continue
                if s1.denominator == 1 and Nlo <= s1 <= Nhi:
                    return True, False, nstates
                if s1 in dst:
                    continue
                if len(dst) >= CAP_STATES:
                    capped = True
                    continue
                dst.add(s1)
                nstates += 1
    return False, capped, nstates

def knapsack_uni(items_one_type, u, Nlo, Nhi):
    """(UNI): one type, N = k * V2 * q with k V2 <= u.  items_one_type is
       a list of (V2, q) for the assignments; a group survives if ANY
       assignment has some k with k V2 q integral in [Nlo, Nhi]."""
    for (v2, q) in items_one_type:
        if v2 <= 0:
            continue
        kmax = int(u) // int(v2)
        for k in range(1, kmax + 1):
            val = k * v2 * q
            if val.denominator == 1 and Nlo <= val <= Nhi:
                return True
    return False

# ---------------------------------------------------------------------------
# census drivers
# ---------------------------------------------------------------------------
def collect_groups(n):
    """group key (m, Ms, V_s) -> list of Skel with windows_ok."""
    groups = {}
    for (m, Ms, V) in census(n):
        S = Skel(n, m, list(Ms), V)
        if not S.windows_ok():
            continue
        key = (m, Ms, S.V[S.s])
        groups.setdefault(key, []).append(S)
    return groups

def run_orbit_stats(degs, label=""):
    print("\n== ORBIT-SIZE STATISTICS  %s ==" % label)
    print("   %5s %8s %8s %8s %8s %8s %8s %8s" %
          ("D", "groups", "A1=1", "A1>1", "A|a1", "prod=1", "prodV>u/2", "s3"))
    T = dict(g=0, a1eq1=0, a1gt1=0, adiv=0, prod1=0, big=0, s3=0)
    for n in degs:
        groups = collect_groups(n)
        ng = na1 = ngt = ndiv = nprod1 = nbig = ns3 = 0
        for key, skels in groups.items():
            ng += 1
            # representative: max-A1 assignment, and whether ANY assignment
            # has prod=1 / A1=1.  Report per-group: "has an assignment with A1=1"
            has_A1_1 = False
            has_A1_gt = False
            has_adiv = False
            has_prod1 = False
            has_big = False
            is_s3 = False
            for S in skels:
                Amap, _ = moh_A(S)
                A1 = Amap[1]
                if A1 == 1:
                    has_A1_1 = True
                else:
                    has_A1_gt = True
                if a1(S) % A1 == 0:
                    has_adiv = True
                prod = generic_orbit_size_from_Dsm1(S)
                if prod == 1:
                    has_prod1 = True
                if prod * S.V[2] * 2 > int(S.u):
                    has_big = True
                if S.s == 3:
                    is_s3 = True
            if has_A1_1: na1 += 1
            if has_A1_gt: ngt += 1
            if has_adiv: ndiv += 1
            if has_prod1: nprod1 += 1
            if has_big: nbig += 1
            if is_s3: ns3 += 1
        T['g'] += ng; T['a1eq1'] += na1; T['a1gt1'] += ngt
        T['adiv'] += ndiv; T['prod1'] += nprod1; T['big'] += nbig; T['s3'] += ns3
        if ng:
            print("   %5d %8d %8d %8d %8d %8d %8d %8d" %
                  (n, ng, na1, ngt, ndiv, nprod1, nbig, ns3))
            sys.stdout.flush()
    print("   TOTAL groups %d; some A1=1: %d; some A1>1: %d; some A|a1: %d"
          % (T['g'], T['a1eq1'], T['a1gt1'], T['adiv']))
    print("   some generic-prod=1: %d; some prod*V2 > u/2: %d; some s=3: %d"
          % (T['prod1'], T['big'], T['s3']))
    return T

def run_filters(degs, Nlo, Nhi, label="", CAP=2500):
    """Three filters on the same groups:
         UNI     one V-assignment, N = k V2 q, k V2 <= u
         ORBIT   mix of packets (Z size 1 and NZ size A1) from the group's
                 V-assignments, unbounded knapsack, weight = |O| V2 <= u
         GEN     mix of size-1 packets only (the old general knapsack)
    Capped groups counted as SURVIVING.
    """
    print("\n== FILTERS  N in [%d,%d]  %s  CAP=%d ==" % (Nlo, Nhi, label, CAP))
    print("   %5s %8s %8s %8s %8s %8s %8s %8s %8s" %
          ("D", "groups", "uniK", "orbK", "genK", "orbC", "genC", "wall", "maxst"))
    T = dict(g=0, uk=0, ok=0, gk=0, oc=0, gc=0)
    per = {}
    for n in degs:
        t0 = time.time()
        groups = collect_groups(n)
        ng = uk = ok = gk = oc = gc = 0
        maxst = 0
        for key, skels in groups.items():
            ng += 1
            u = int(skels[0].u)
            uni_items = [(S.V[2], qval(S)) for S in skels]
            uni_hit = knapsack_uni(uni_items, u, Nlo, Nhi)
            if not uni_hit:
                uk += 1
            # cheap ORBIT: UNI witness whose disc-count k is a multiple of A1
            # (s=3 NZ forces |O|=A1; A1=1 always works; s>3 size-1 packets exist)
            orb_cheap = False
            if uni_hit:
                for S in skels:
                    v2 = S.V[2]; q = qval(S)
                    if v2 <= 0:
                        continue
                    A1, _, _, _ = last_split_orbit_size(S)
                    kmax = u // v2
                    for k in range(1, kmax + 1):
                        val = k * v2 * q
                        if val.denominator == 1 and Nlo <= val <= Nhi:
                            if S.s > 3 or A1 == 1 or k % A1 == 0:
                                orb_cheap = True
                                break
                    if orb_cheap:
                        break
            if orb_cheap:
                hit_o, cap_o, st_o = True, False, 0
            else:
                orb_items = []
                for S in skels:
                    orb_items.extend(packet_items(S, Nhi, mode="s3strict"))
                hit_o, cap_o, st_o = knapsack_fracpart(orb_items, u, Nlo, Nhi, CAP)
            maxst = max(maxst, st_o)
            if not hit_o:
                if cap_o:
                    oc += 1
                else:
                    ok += 1
            # GEN: UNI-hit => GEN-hit (size-1 packets realise every UNI k)
            if uni_hit:
                hit_g, cap_g, st_g = True, False, 0
            else:
                gen_items = []
                for S in skels:
                    gen_items.extend(packet_items(S, Nhi, mode="gen"))
                hit_g, cap_g, st_g = knapsack_fracpart(gen_items, u, Nlo, Nhi, CAP)
            maxst = max(maxst, st_g)
            if not hit_g:
                if cap_g:
                    gc += 1
                else:
                    gk += 1
        T['g'] += ng; T['uk'] += uk; T['ok'] += ok; T['gk'] += gk
        T['oc'] += oc; T['gc'] += gc
        per[n] = (ng, uk, ok, gk, oc, gc)
        wall = time.time() - t0
        print("   %5d %8d %8d %8d %8d %8d %8d %7.1fs %8d" %
              (n, ng, uk, ok, gk, oc, gc, wall, maxst))
        sys.stdout.flush()
    def pct(k):
        return 100.0 * k / max(1, T['g'])
    print("   TOTAL %s: groups %d" % (label, T['g']))
    print("     UNI   killed %d (%.2f%%)" % (T['uk'], pct(T['uk'])))
    print("     ORBIT killed %d (%.2f%%)  capped/UNDECIDED %d" % (T['ok'], pct(T['ok']), T['oc']))
    print("     GEN   killed %d (%.2f%%)  capped/UNDECIDED %d" % (T['gk'], pct(T['gk']), T['gc']))
    empty_u = [n for n in per if per[n][0] and per[n][1] == per[n][0]]
    empty_o = [n for n in per if per[n][0] and per[n][2] == per[n][0]]
    empty_g = [n for n in per if per[n][0] and per[n][3] == per[n][0]]
    print("     degrees emptied UNI  : %s" % (empty_u if empty_u else "NONE"))
    print("     degrees emptied ORBIT: %s" % (empty_o if empty_o else "NONE"))
    print("     degrees emptied GEN  : %s" % (empty_g if empty_g else "NONE"))
    return per, T

def run_nz_only(degs, Nlo, Nhi, label="", CAP=2500):
    """Hostile-to-UNI variant: NZ packets ONLY (size A1), no size-1.
       If A1=1 this coincides with GEN for that assignment."""
    print("\n== NZ-ONLY (nonzero-center, |O|=A1; A1=1 reduces to size 1)  %s ==" % label)
    print("   %5s %8s %8s %8s %8s" % ("D", "groups", "nzK", "nzC", "wall"))
    T = dict(g=0, k=0, c=0)
    per = {}
    for n in degs:
        t0 = time.time()
        groups = collect_groups(n)
        ng = nk = nc = 0
        for key, skels in groups.items():
            ng += 1
            u = int(skels[0].u)
            items = []
            for S in skels:
                q = qval(S); v2 = S.V[2]
                A1, _, _, _ = last_split_orbit_size(S)
                w = A1 * v2; c = A1 * v2 * q
                if w <= u and c <= Nhi:
                    items.append((w, c, "NZ"))
            hit, cap, _ = knapsack_fracpart(items, u, Nlo, Nhi, CAP)
            if not hit:
                if cap: nc += 1
                else: nk += 1
        T['g'] += ng; T['k'] += nk; T['c'] += nc
        per[n] = (ng, nk, nc)
        print("   %5d %8d %8d %8d %7.1fs" % (n, ng, nk, nc, time.time() - t0))
        sys.stdout.flush()
    print("   TOTAL %s: groups %d, NZ-killed %d (%.2f%%), capped %d" %
          (label, T['g'], T['k'], 100.0 * T['k'] / max(1, T['g']), T['c']))
    empty = [n for n in per if per[n][0] and per[n][1] == per[n][0]]
    print("   degrees emptied NZ-ONLY: %s" % (empty if empty else "NONE"))
    return per, T

def probe_examples():
    print("\n== WORKED EXAMPLES (Moh six rows + a few census) ==")
    print("   %-22s %3s %4s %6s %6s %6s %8s %8s %6s %6s %s" %
          ("row", "s", "u", "V2", "A1", "prod", "slots", "a1", "A|a1", "q", "N_UNI"))
    rows = list(MOH_SURVIVORS)
    # add a couple of small census skeletons
    extra = []
    for n in (48, 54, 64):
        seen = 0
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.windows_ok():
                extra.append((n, m, list(Ms), V, "n=%d m=%d" % (n, m), None))
                seen += 1
            if seen >= 3:
                break
    for (n, m, Ms, Vs, lab, _) in rows + extra:
        S = Skel(n, m, list(Ms), Vs)
        if not S.windows_ok():
            continue
        Amap, _ = moh_A(S)
        A1 = Amap[1]
        prod = generic_orbit_size_from_Dsm1(S)
        q = qval(S)
        uni = []
        v2 = S.V[2]; u = int(S.u)
        for k in range(1, u // v2 + 1):
            val = k * v2 * q
            if val.denominator == 1:
                uni.append(int(val))
        print("   %-22s %3d %4s %6d %6d %6d %8d %8d %6s %6s %s" %
              (lab[:22], S.s, str(S.u), v2, A1, prod, slots_top_major(S), a1(S),
               "yes" if a1(S) % A1 == 0 else "no", str(q), uni[:8]))

def run_fast(degs, Nlo, Nhi, label="", CAP=400, do_gen=True):
    """UNI + s3strict ORBIT + NZ-only, optional GEN.  Progress every degree."""
    print("\n== FAST FILTERS  N in [%d,%d]  %s  CAP=%d gen=%s ==" %
          (Nlo, Nhi, label, CAP, do_gen))
    print("   %5s %8s %8s %8s %8s %8s %8s %8s %8s" %
          ("D", "groups", "uniK", "orbK", "nzK", "genK", "orbC", "nzC", "wall"))
    T = dict(g=0, uk=0, ok=0, nk=0, gk=0, oc=0, nc=0, gc=0)
    per = {}
    for n in degs:
        t0 = time.time()
        groups = collect_groups(n)
        ng = uk = ok = nkilled = gk = oc = nc = gc = 0
        for key, skels in groups.items():
            ng += 1
            u = int(skels[0].u)
            uni_items = [(S.V[2], qval(S)) for S in skels]
            uni_hit = knapsack_uni(uni_items, u, Nlo, Nhi)
            if not uni_hit:
                uk += 1
            # NZ-only
            nz_items = []
            for S in skels:
                nz_items.extend(packet_items(S, Nhi, mode="nz"))
            hit_n, cap_n, _ = knapsack_fracpart(nz_items, u, Nlo, Nhi, CAP)
            if not hit_n:
                if cap_n: nc += 1
                else: nkilled += 1
            # ORBIT s3strict: cheap UNI-with-A1|k, else DP
            orb_cheap = False
            if uni_hit:
                for S in skels:
                    v2 = S.V[2]; q = qval(S)
                    if v2 <= 0:
                        continue
                    A1 = last_split_orbit_size(S)[0]
                    kmax = u // v2
                    for k in range(1, kmax + 1):
                        val = k * v2 * q
                        if val.denominator == 1 and Nlo <= val <= Nhi:
                            if S.s > 3 or A1 == 1 or k % A1 == 0:
                                orb_cheap = True
                                break
                    if orb_cheap:
                        break
            if orb_cheap:
                hit_o, cap_o = True, False
            else:
                orb_items = []
                for S in skels:
                    orb_items.extend(packet_items(S, Nhi, mode="s3strict"))
                hit_o, cap_o, _ = knapsack_fracpart(orb_items, u, Nlo, Nhi, CAP)
            if not hit_o:
                if cap_o: oc += 1
                else: ok += 1
            if do_gen:
                if uni_hit:
                    hit_g, cap_g = True, False
                else:
                    gen_items = []
                    for S in skels:
                        gen_items.extend(packet_items(S, Nhi, mode="gen"))
                    hit_g, cap_g, _ = knapsack_fracpart(gen_items, u, Nlo, Nhi, CAP)
                if not hit_g:
                    if cap_g: gc += 1
                    else: gk += 1
        T['g'] += ng; T['uk'] += uk; T['ok'] += ok; T['nk'] += nkilled
        T['gk'] += gk; T['oc'] += oc; T['nc'] += nc; T['gc'] += gc
        per[n] = (ng, uk, ok, nkilled, gk, oc, nc, gc)
        print("   %5d %8d %8d %8d %8d %8d %8d %8d %7.1fs" %
              (n, ng, uk, ok, nkilled, gk, oc, nc, time.time() - t0))
        sys.stdout.flush()
    def pct(k):
        return 100.0 * k / max(1, T['g'])
    print("   TOTAL %s: groups %d" % (label, T['g']))
    print("     UNI   killed %d (%.2f%%)" % (T['uk'], pct(T['uk'])))
    print("     ORBIT killed %d (%.2f%%)  capped %d" % (T['ok'], pct(T['ok']), T['oc']))
    print("     NZ    killed %d (%.2f%%)  capped %d" % (T['nk'], pct(T['nk']), T['nc']))
    if do_gen:
        print("     GEN   killed %d (%.2f%%)  capped %d" % (T['gk'], pct(T['gk']), T['gc']))
    empty = {
        "UNI": [n for n in per if per[n][0] and per[n][1] == per[n][0]],
        "ORBIT": [n for n in per if per[n][0] and per[n][2] == per[n][0]],
        "NZ": [n for n in per if per[n][0] and per[n][3] == per[n][0]],
    }
    for lab2, lst in empty.items():
        print("     degrees emptied %s: %s" % (lab2, lst if lst else "NONE"))
    return per, T

if __name__ == "__main__":
    t0 = time.time()
    print("orbits.py  BRANCH-ORBITS  python %s" % sys.version.split()[0])
    print("=" * 78)
    control_moh_rows_A()
    control_s3_slots()
    control_A_identities(80)
    print("\n== %d controls, %d failures ==" % (NCHECK[0], len(FAILURES)))
    if FAILURES:
        for nm, dt in FAILURES[:12]:
            print("   FAILED: %s %s" % (nm, dt))
        sys.exit(1)
    print("ALL CONTROLS PASSED.")
    probe_examples()
    run_orbit_stats(list(range(48, 101)), "D<=100")
    run_orbit_stats([105, 108, 112, 117, 120], "MOH-SHARP-2")

    # campaign frontier N>=6; H2 window [4,16] also, for comparison with charged UNI numbers
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"

    if mode in ("all", "h2", "fast"):
        run_fast([105, 108, 112, 117, 120], 4, 16, "MOH-SHARP-2 H2 [4,16]",
                 CAP=400, do_gen=False)
        run_fast([105, 108, 112, 117, 120], 6, 16, "MOH-SHARP-2 N>=6 [6,16]",
                 CAP=400, do_gen=False)
    if mode in ("all", "n6", "fast"):
        run_fast(list(range(48, 101)), 6, 16, "D<=100 N>=6 frontier [6,16]",
                 CAP=400, do_gen=True)
    if mode in ("all", "h2low"):
        run_fast(list(range(48, 80)), 4, 16, "D in [48,79] H2 (compare 24.7%)",
                 CAP=400, do_gen=True)

    print("\nwall %.1f s" % (time.time() - t0))
