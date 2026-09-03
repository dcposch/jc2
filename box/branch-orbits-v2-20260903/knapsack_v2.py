#!/usr/bin/env python3
"""BRANCH-ORBITS v2 -- orbit-aware exact knapsack on Moh (1)-(13).  REPAIRED.

Lane nested-pack-dp-grok46-20260903.  Standard library only.
Reads the charged enumerator box/moh_skeleton_full.py (never modified).

This is knapsack.py with the two binding review repairs; the charged original
box/branch-orbits-v2-20260903/knapsack.py (sha256
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276) is left
untouched.

R1: import moh_skeleton_full via --inputs DIR, $JC2_INPUTS, or paths relative
    to this file / the repo box/; no stale /tmp/jc2-lane.GqI4QH hard-code.
R2: print the 274-group s=3 Z01 subtotal (173/138) separately from the
    global all-s Z01 totals (611/493), which are not exact at s>3.

Orbit size of a bottom-major disc D_1, PROVED-HERE for the unique major
D_{s-1} (Prop 4.5 + Lemma 6.1 + p.200 Thm (6) deg q = 2 at D_s):

  |O|(D_1) = product_{j=2}^{s-1} omega_j

where omega_j = A_j if the factor of p at D_j is (pi - a), a != 0  (10)
               = 1   if the factor is pi                            (11)

If both (10) and (11) hold, both omega are admissible (do not over-kill).
A_1 is NOT an orbit-size of discs: it is the (12)/(13) increment inside D_1.

Packet of one V-assignment: weight w = |O| * V_2, value c = |O| * V_2 * q,
unbounded copies (several cyclotomic orbits of the same V-data), budget
sum w <= u.  Mixing packets from different V-assignments of the same group
is the several-orbits case.  This flat packing is EXACT at s=3 (deg p at
D_2 equals u) and a RELAXATION of nested packing at s>3 (may under-kill).

Fail-closed: any check() failure aborts before a filter number is printed.
"""
from __future__ import annotations
import os, sys, time, itertools
from fractions import Fraction as F
from math import gcd, lcm

HERE = os.path.dirname(os.path.abspath(__file__))

def _argv_opt(flag):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return None

def _enumerator_dirs():
    """Explicit --inputs, $JC2_INPUTS, then repo-relative box/ (never a stale /tmp lane)."""
    out = []
    for p in (_argv_opt("--inputs"), os.environ.get("JC2_INPUTS")):
        if p:
            out.append(p)
    out.append(os.path.join(HERE, ".."))            # box/ next to this lane dir
    out.append(HERE)
    out.append(os.path.join(HERE, "..", "..", "box"))
    seen = set(); uniq = []
    for p in out:
        ap = os.path.abspath(p)
        if ap not in seen:
            seen.add(ap); uniq.append(ap)
    return uniq

def _load_enumerator():
    tried = []
    for d in _enumerator_dirs():
        cand = os.path.join(d, "moh_skeleton_full.py")
        tried.append(cand)
        if os.path.isfile(cand):
            sys.path.insert(0, d)
            import moh_skeleton_full as MF
            from moh_skeleton_full import Skel, census, MOH_TABLE, NLO, NHI
            return MF, Skel, census, MOH_TABLE, NLO, NHI
    raise ImportError(
        "moh_skeleton_full.py not found; pass --inputs DIR (tried %s)" % tried)

MF, Skel, census, MOH_TABLE, NLO, NHI = _load_enumerator()

FAILURES = []
NCHECK = [0]

def check(name, cond, detail=""):
    NCHECK[0] += 1
    if cond:
        print("  [ok]   %s" % name)
    else:
        print("  [FAIL] %s   %s" % (name, detail))
        FAILURES.append(name)
    return cond

# ---------------------------------------------------------------------------
# orbit arithmetic
# ---------------------------------------------------------------------------
def level_omegas(S):
    """For each j=2..s-1, the admissible local orbit sizes {1, A_j}."""
    out = []
    for j in range(2, S.s):
        _ok, b10, b11 = S.cond1011(j)
        A = int(S.A(j))
        opts = []
        if b11:
            opts.append(1)
        if b10:
            opts.append(A)
        if not opts:
            opts.append(1)
        out.append(sorted(set(opts)))
    return out

def orbit_sizes(S):
    opts = level_omegas(S)
    if not opts:
        return {1}
    sizes = set()
    for combo in itertools.product(*opts):
        p = 1
        for c in combo:
            p *= c
        sizes.add(p)
    return sizes

def packets(S, Nhi):
    """Unbounded Galois packets of one V-assignment: (w, c, om, tag)."""
    v2 = int(S.V[2])
    q = S.q()
    u = int(S.u)
    out = []
    for om in sorted(orbit_sizes(S)):
        w = om * v2
        c = om * v2 * q
        if w <= 0 or w > u or c <= 0 or c > Nhi:
            continue
        tag = "Z" if om == 1 else "NZ"
        out.append((w, c, om, tag))
    return out

def uni_packets(S, Nhi):
    """(UNI) size-1 packets: w = V_2, c = V_2 q  (any k discs of this type)."""
    v2 = int(S.V[2])
    q = S.q()
    u = int(S.u)
    c = v2 * q
    if v2 <= u and 0 < c <= Nhi:
        return [(v2, c, 1, "UNI")]
    return []

def Umax(skels):
    u = int(skels[0].u)
    mq = max(S.q() for S in skels)
    return u * mq

# ---------------------------------------------------------------------------
# exact unbounded knapsack: DP over (weight, fractional part)
# ---------------------------------------------------------------------------
def knapsack(items, u, Nlo, Nhi, CAP=60000):
    """items: iterable of (w, c, ...).  Unbounded.  Returns (hit, capped, nstates).

    Cheap path: copies of one packet, then two-packet search.  Then either a
    bitset (lcm of dens small) or Fraction-set DP with per-weight cap CAP.
    Capped + no hit => UNDECIDED, counted alive (kill is a floor).
    """
    uniq = {}
    for trip in items:
        w, c = int(trip[0]), trip[1]
        if w <= 0 or c <= 0 or c > Nhi or w > u:
            continue
        uniq[(w, c)] = True
    items = list(uniq)
    if not items:
        return False, False, 0
    # one packet type
    for (w, c) in items:
        kmax = u // w
        for k in range(1, kmax + 1):
            val = k * c
            if val > Nhi:
                break
            if val.denominator == 1 and Nlo <= val <= Nhi:
                return True, False, 0
    # two packet types, complete (k1, k2) -- cheap sufficient hit
    if 2 <= len(items) <= 40:
        its = sorted(items)
        L = len(its)
        for i in range(L):
            w1, c1 = its[i]
            k1max = u // w1
            for k1 in range(0, k1max + 1):
                s1 = k1 * c1
                if s1 > Nhi:
                    break
                rem = u - k1 * w1
                for j in range(i + 1, L):
                    w2, c2 = its[j]
                    if w2 > rem:
                        continue
                    k2max = rem // w2
                    for k2 in range(1, k2max + 1):
                        val = s1 + k2 * c2
                        if val > Nhi:
                            break
                        if val.denominator == 1 and Nlo <= val <= Nhi:
                            return True, False, 0
    dens = 1
    for (_, c) in items:
        dens = lcm(dens, c.denominator)
    if dens <= 4096 and int(Nhi) * dens <= 200000:
        return _bitset(items, u, Nlo, Nhi, dens)
    return _fracsets(items, u, Nlo, Nhi, CAP)

def _bitset(items, u, Nlo, Nhi, D):
    scaled = [(w, int(c * D)) for (w, c) in items]
    NhiS = int(Nhi) * D
    mask = (1 << (NhiS + 1)) - 1
    reach = [0] * (u + 1)
    reach[0] = 1
    # unbounded complete: iterate items, then 0-1-style along increasing weight
    # (standard unbounded knapsack bitset)
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

def _fracsets(items, u, Nlo, Nhi, CAP):
    reach = [set() for _ in range(u + 1)]
    reach[0].add(F(0))
    nstates = 1
    capped = False
    for (w, c) in items:
        for tw in range(w, u + 1):
            if not reach[tw - w]:
                continue
            dst = reach[tw]
            for s0 in list(reach[tw - w]):
                s1 = s0 + c
                if s1 > Nhi:
                    continue
                if s1.denominator == 1 and Nlo <= s1 <= Nhi:
                    return True, False, nstates
                if s1 in dst:
                    continue
                if len(dst) >= CAP:
                    capped = True
                    continue
                dst.add(s1)
                nstates += 1
    return False, capped, nstates

def achievable_N(items, u, Nlo, Nhi, CAP=60000):
    """Return the set of integer N in [Nlo, Nhi] hit by unbounded packets, or
    None if capped before a complete enumeration.  Used only for small listings
    (D=105).  Early-out knapsack is not used here."""
    uniq = {}
    for trip in items:
        w, c = int(trip[0]), trip[1]
        if w <= 0 or c <= 0 or c > Nhi or w > u:
            continue
        uniq[(w, c)] = True
    items = list(uniq)
    if not items:
        return set(), False
    dens = 1
    for (_, c) in items:
        dens = lcm(dens, c.denominator)
    if dens > 4096 or int(Nhi) * dens > 200000:
        # Fraction DP collecting integers
        reach = [set() for _ in range(u + 1)]
        reach[0].add(F(0))
        hit = set()
        capped = False
        for (w, c) in items:
            for tw in range(w, u + 1):
                if not reach[tw - w]:
                    continue
                dst = reach[tw]
                for s0 in list(reach[tw - w]):
                    s1 = s0 + c
                    if s1 > Nhi:
                        continue
                    if s1.denominator == 1 and Nlo <= s1 <= Nhi:
                        hit.add(int(s1))
                    if s1 in dst:
                        continue
                    if len(dst) >= CAP:
                        capped = True
                        continue
                    dst.add(s1)
        return hit, capped
    scaled = [(w, int(c * D)) if False else (w, int(c * dens)) for (w, c) in items]
    D = dens
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
    bits = 0
    for tw in range(1, u + 1):
        bits |= reach[tw]
    hit = set()
    for N in range(int(Nlo), int(Nhi) + 1):
        if bits & (1 << (N * D)):
            hit.add(N)
    return hit, False

# ---------------------------------------------------------------------------
# collect
# ---------------------------------------------------------------------------
def collect(n):
    G = {}
    for (m, Ms, V) in census(n, Kmin=16, full=True):
        S = Skel(n, m, list(Ms), V)
        key = (m, Ms, S.V[S.s])
        G.setdefault(key, []).append(S)
    return G

# ---------------------------------------------------------------------------
# controls
# ---------------------------------------------------------------------------
def control_moh_rows():
    print("\n-- CONTROL M: Moh six rows, orbit size vs (10)/(11) and A_2 --")
    print("   %-24s %3s %4s %4s %4s %4s %6s %6s %8s %s" %
          ("row", "s", "A2", "V2", "u", "(10)", "(11)", "|O|", "w", "N orb [6,16]"))
    for (n, m, Ms, Vs, lab, _, _, _) in MOH_TABLE:
        S = Skel(n, m, Ms, Vs)
        check("windows+full %s" % lab, S.windows_ok() and S.full_ok())
        ok, b10, b11 = S.cond1011(2)
        A2 = S.A(2)
        oms = orbit_sizes(S)
        u = int(S.u)
        q = S.q()
        # s=3: |O| = A2 if (10) not (11) else {1} or {1,A2}
        if S.s == 3 and b10 and not b11:
            check("|O|={A2} for (10)-only %s" % lab, oms == {A2}, str(oms))
        if S.s == 3 and b11 and not b10:
            check("|O|={1} for (11)-only %s" % lab, oms == {1}, str(oms))
        pk = packets(S, 16)
        hit, cap, _ = knapsack(pk, u, 6, 16)
        Ns, _ = achievable_N(pk, u, 6, 16)
        print("   %-24s %3d %4d %4d %4d %4s %4s %6s %6s %8s  q=%s  %s" %
              (lab, S.s, A2, S.V[2], u, b10, b11, str(sorted(oms)),
               str([p[0] for p in pk]), sorted(Ns), q,
               "HIT" if hit else "miss"))
        # (12) xor (13) unless A1=1
        ok1213, b12, b13 = S.cond1213()
        A1 = S.A(1)
        if A1 > 1:
            check("(12) xor (13) at A1>1 %s" % lab, b12 != b13,
                  "b12=%s b13=%s A1=%s" % (b12, b13, A1))
        check("A1 | (n*+m*)V2-1 %s" % lab,
              ((S.e + S.dd) * S.V[2] - 1) % A1 == 0)

def control_s3_Q_eq_u():
    print("\n-- CONTROL Q: s=3 => deg p at D_2 = u  (algebra + census) --")
    seen = 0
    for n in range(48, 121):
        for (m, Ms, V) in census(n, full=True):
            S = Skel(n, m, list(Ms), V)
            if S.s != 3:
                continue
            seen += 1
            Q = S.V[3] * S.d[2] // S.d[3]
            if not check("Q=u n=%d" % n, Q == int(S.u), "%s vs %s" % (Q, S.u)):
                return
    check("s=3 Q=u on all (1)-(13) s=3 assignments", seen > 0)
    print("   %d s=3 V-assignments, Q=u always" % seen)

def control_mult_on_Cstar():
    """Galois tbar |-> omega tbar acts by multiplication on the pi-coordinate:
       a |-> omega^k a.  Free on C*, so NZ orbit size is exactly A, not a
       proper divisor.  This is the algebraic content of (10), checked on
       the six rows: A2 * V2 <= u whenever (10) and not (11)."""
    print("\n-- CONTROL FREE: (10)-only => A_{j} V_j <= Q_j  (six rows + census sample) --")
    bad = 0
    tot = 0
    for n in range(48, 101):
        for (m, Ms, V) in census(n, full=True):
            S = Skel(n, m, list(Ms), V)
            for j in range(2, S.s):
                tot += 1
                ok, b10, b11 = S.cond1011(j)
                tri, sq, A, Q = S.div9(j)
                if b10 and not b11:
                    if A * S.V[j] > Q:
                        bad += 1
    check("(10)-only implies A V <= Q on 48<=D<=100 full census", bad == 0,
          "%d / %d" % (bad, tot))
    print("   %d levels, %d (10)-only violations (want 0)" % (tot, bad))

def control_rebase_reproduction():
    """Reproduce census-rebase §6 uni>=6 / uni6-16 / mix6-16 totals."""
    print("\n-- CONTROL R: census-rebase §6 reproduction (uni / mix, size-1 packets) --")
    T = dict(g=0, u1=0, u2=0, mx=0, cap=0)
    empty_mix = []
    per = {}
    t0 = time.time()
    for n in range(48, 121):
        G = collect(n)
        if not G:
            continue
        a1 = a2 = am = cp = 0
        for key, skels in G.items():
            items = [(S.V[2], S.q(), S.u) for S in skels]
            h1 = bool(MF.uni_hits(items, NLO, None))
            h2 = bool(MF.uni_hits(items, NLO, NHI))
            hm, c = MF.mixed_hit(items)
            a1 += h1; a2 += h2; am += (hm or c); cp += c
        T['g'] += len(G); T['u1'] += a1; T['u2'] += a2; T['mx'] += am; T['cap'] += cp
        per[n] = (len(G), a1, a2, am, cp)
        if am == 0:
            empty_mix.append(n)
        print("   rebase D=%-3d groups=%-4d uni>=6=%-4d uni[6,16]=%-4d mix[6,16]=%-4d cap=%d"
              % (n, len(G), a1, a2, am, cp)); sys.stdout.flush()
    print("   TOTAL groups %d uni>=6 %d uni[6,16] %d mix[6,16] %d cap %d  [%.1fs]"
          % (T['g'], T['u1'], T['u2'], T['mx'], T['cap'], time.time()-t0))
    check("groups = 1189", T['g'] == 1189, str(T['g']))
    check("uni>=6 = 670", T['u1'] == 670, str(T['u1']))
    check("uni[6,16] = 589", T['u2'] == 589, str(T['u2']))
    check("mix[6,16] = 648", T['mx'] == 648, str(T['mx']))
    check("rebase empty mix degrees = {48} (66,78 have no skeleton)",
          empty_mix == [48], str(empty_mix))
    # D=105 three groups
    check("D=105 groups = 14 (alive mix = 3)", per.get(105, (0,))[0] == 14
          and per[105][3] == 3, str(per.get(105)))
    return T, per

# ---------------------------------------------------------------------------
# main census
# ---------------------------------------------------------------------------
LISTING = (105, 108, 112, 117, 120)

def run_orbit(dlo=48, dhi=120):
    print("\n== ORBIT-AWARE KNAPSACK on (1)-(13), %d <= D <= %d ==" % (dlo, dhi))
    print("   %5s %7s %7s %7s %7s %7s %7s %7s %7s %7s %8s" %
          ("D", "grp", "s3", "uni>=6", "uni616", "mix616",
           "orb>=6", "orb616", "cap", "empty?", "wall"))
    T = dict(g=0, s3=0, u1=0, u2=0, mx=0, o1=0, o2=0, cap=0)
    empty_orb6 = []; empty_orb16 = []; empty_mix = []
    surv = {n: [] for n in LISTING}
    delta_kill16 = []   # mix-alive, orbit-dead in [6,16]
    delta_kill6 = []
    t_all = time.time()
    for n in range(dlo, dhi + 1):
        t0 = time.time()
        G = collect(n)
        if not G:
            continue
        a_u1 = a_u2 = a_mx = a_o1 = a_o2 = cp = ns3 = 0
        alive16 = []
        for key, skels in G.items():
            u = int(skels[0].u)
            items_uni = [(S.V[2], S.q(), S.u) for S in skels]
            h_u1 = bool(MF.uni_hits(items_uni, 6, None))
            h_u2 = bool(MF.uni_hits(items_uni, 6, 16))
            h_mx, c_mx = MF.mixed_hit(items_uni, 6, 16)
            Um = Umax(skels)
            Nhi6 = max(int(Um), 6)
            # orbit packets at the two windows
            pk16 = []
            pk6 = []
            for S in skels:
                pk16.extend(packets(S, 16))
                pk6.extend(packets(S, Nhi6))
            h_o2, c2, _ = knapsack(pk16, u, 6, 16)
            h_o1, c1, _ = knapsack(pk6, u, 6, Nhi6)
            if skels[0].s == 3:
                ns3 += 1
            a_u1 += h_u1; a_u2 += h_u2
            a_mx += (h_mx or c_mx)
            a_o1 += (h_o1 or c1); a_o2 += (h_o2 or c2)
            cp += int(c1 or c2)
            if (h_mx or c_mx) and not (h_o2 or c2):
                delta_kill16.append((n, key, skels))
            if h_u1 and not (h_o1 or c1):
                delta_kill6.append((n, key, skels))
            if n in LISTING and (h_o2 or c2):
                alive16.append((key, skels, h_o2, c2, h_u2, h_mx))
        T['g'] += len(G); T['s3'] += ns3
        T['u1'] += a_u1; T['u2'] += a_u2; T['mx'] += a_mx
        T['o1'] += a_o1; T['o2'] += a_o2; T['cap'] += cp
        if a_o1 == 0: empty_orb6.append(n)
        if a_o2 == 0: empty_orb16.append(n)
        if a_mx == 0: empty_mix.append(n)
        if n in LISTING:
            surv[n] = alive16
        flag = ""
        if a_o2 == 0:
            flag = " EMPTY[6,16]"
        print("   %5d %7d %7d %7d %7d %7d %7d %7d %7d %7s %7.1fs%s"
              % (n, len(G), ns3, a_u1, a_u2, a_mx, a_o1, a_o2, cp,
                 "Y" if a_o2 == 0 else "", time.time()-t0, flag))
        sys.stdout.flush()
    print("   ---- totals ----")
    print("   groups %d  (s=3 groups %d)" % (T['g'], T['s3']))
    print("   (UNI)   N>=6 %d   [6,16] %d" % (T['u1'], T['u2']))
    print("   mixed   [6,16] %d" % T['mx'])
    print("   ORBIT   N>=6 %d   [6,16] %d   capped %d" % (T['o1'], T['o2'], T['cap']))
    print("   empty mix[6,16]     : %s" % (empty_mix or "NONE"))
    print("   empty orbit N>=6    : %s" % (empty_orb6 or "NONE"))
    print("   empty orbit [6,16]  : %s" % (empty_orb16 or "NONE"))
    print("   mix-alive / orbit-dead [6,16] : %d groups" % len(delta_kill16))
    print("   uni-alive / orbit-dead N>=6   : %d groups" % len(delta_kill6))
    print("   wall %.1fs" % (time.time()-t_all))
    return T, surv, delta_kill16, delta_kill6, empty_orb6, empty_orb16

def list_D105(surv):
    print("\n== D=105 SURVIVORS, full packet structure ==")
    rows = surv.get(105, [])
    print("   orbit-alive groups in [6,16]: %d" % len(rows))
    G = collect(105)
    print("   all (1)-(13) groups at D=105: %d" % len(G))
    for key, skels in sorted(G.items()):
        m, Ms, Vs = key
        S0 = skels[0]
        u = int(S0.u)
        print("\n   -- m=%d M=%s V_s=%d  s=%d K=%d (d,e)=(%d,%d) u=%d --"
              % (m, list(Ms), Vs, S0.s, S0.K, S0.dd, S0.e, u))
        pk16 = []
        for S in skels:
            oms = orbit_sizes(S)
            ok, b10, b11 = S.cond1011(2)
            ok12, b12, b13 = S.cond1213()
            A1, A2 = S.A(1), S.A(2)
            q = S.q()
            v2 = S.V[2]
            pks = packets(S, 16)
            pk16.extend(pks)
            print("      V=%s  q=%s  d1=%s  A2=%s A1=%s  (10)=%s (11)=%s  (12)=%s (13)=%s  |O|=%s  packets=%s"
                  % (dict(S.V), q, S.delta[1], A2, A1, b10, b11, b12, b13,
                     sorted(oms), [(w, str(c), om, tag) for (w,c,om,tag) in pks]))
        Ns_orb, cap = achievable_N(pk16, u, 6, 16)
        items_uni = [(S.V[2], S.q(), S.u) for S in skels]
        Ns_uni = sorted(MF.uni_hits(items_uni, 6, 16))
        h_mx, c_mx = MF.mixed_hit(items_uni, 6, 16)
        print("      achievable N (UNI)[6,16]  = %s" % Ns_uni)
        print("      achievable N (ORBIT)[6,16]= %s%s" % (sorted(Ns_orb),
              " [CAPPED]" if cap else ""))
        print("      mixed[6,16] hit=%s" % (h_mx or c_mx))

def list_delta(delta, label):
    print("\n== DELTA: %s (%d groups) ==" % (label, len(delta)))
    for (n, key, skels) in delta[:80]:
        m, Ms, Vs = key
        S0 = skels[0]
        u = int(S0.u)
        bits = []
        for S in skels:
            bits.append("V2=%s q=%s |O|=%s A[2:s]=%s 10/11=%s" %
                        (S.V[2], S.q(), sorted(orbit_sizes(S)),
                         [S.A(j) for j in range(2, S.s)],
                         [S.cond1011(j)[1:] for j in range(2, S.s)]))
        items = [(S.V[2], S.q(), S.u) for S in skels]
        Ns_uni = sorted(MF.uni_hits(items, 6, 16))
        print("   D=%d m=%d M=%s V_s=%d s=%d u=%d UNI-N=%s" %
              (n, m, list(Ms), Vs, S0.s, u, Ns_uni))
        for b in bits:
            print("      %s" % b)
    if len(delta) > 80:
        print("   ... %d more" % (len(delta)-80))

def knapsack_z01(skels, Nlo, Nhi, CAP=60000):
    """NZ packets unbounded; Z packets 0-1 and at most one Z in total
    (one pi-factor per parent; at s=3 there is one parent, so this is exact)."""
    u = int(skels[0].u)
    nz, z = [], []
    for S in skels:
        for p in packets(S, Nhi):
            (nz if p[3] != "Z" else z).append(p)
    h, c, _ = knapsack(nz, u, Nlo, Nhi, CAP)
    if h or c:
        return True, c
    seen = set()
    for zp in z:
        w, cv = int(zp[0]), zp[1]
        key = (w, cv)
        if key in seen:
            continue
        seen.add(key)
        if w > u:
            continue
        if cv.denominator == 1 and Nlo <= cv <= Nhi:
            return True, False
        # NZ in the leftover budget, values shifted by cv
        if not nz:
            continue
        # brute: copies of NZ plus this one Z, via DP on leftover
        # reach after unbounded NZ, then add Z
        uniq = {}
        for trip in nz:
            ww, cc = int(trip[0]), trip[1]
            if 0 < ww <= u and 0 < cc <= Nhi:
                uniq[(ww, cc)] = True
        items = list(uniq)
        if not items:
            continue
        dens = 1
        for (_, cc) in items:
            dens = lcm(dens, cc.denominator)
        dens = lcm(dens, cv.denominator)
        if dens <= 4096 and int(Nhi) * dens <= 200000:
            scaled = [(ww, int(cc * dens)) for (ww, cc) in items]
            nZ = int(cv * dens)
            NhiS = int(Nhi) * dens
            mask = (1 << (NhiS + 1)) - 1
            reach = [0] * (u + 1)
            reach[0] = 1
            for (ww, n) in scaled:
                if n > NhiS:
                    continue
                for tw in range(ww, u + 1):
                    src = reach[tw - ww]
                    if src:
                        reach[tw] |= (src << n) & mask
            target = 0
            for N in range(int(Nlo), int(Nhi) + 1):
                target |= 1 << (N * dens)
            # add one Z
            for tw in range(0, u - w + 1):
                src = reach[tw]
                if not src:
                    continue
                shifted = (src << nZ) & mask
                if shifted & target:
                    return True, False
        else:
            # Fraction leftover
            h2, c2, _ = knapsack(items, u - w, Nlo, Nhi, CAP)
            # not shifted -- wrong. Do a small Fraction DP
            reach = [set() for _ in range(u - w + 1)]
            reach[0].add(F(0))
            capped = False
            for (ww, cc) in items:
                for tw in range(ww, u - w + 1):
                    if not reach[tw - ww]:
                        continue
                    dst = reach[tw]
                    for s0 in list(reach[tw - ww]):
                        s1 = s0 + cc
                        if s1 > Nhi:
                            continue
                        val = s1 + cv
                        if val.denominator == 1 and Nlo <= val <= Nhi:
                            return True, False
                        if s1 in dst:
                            continue
                        if len(dst) >= CAP:
                            capped = True
                            continue
                        dst.add(s1)
            if capped:
                return True, True  # conservative
    return False, False

def run_strict_s3(dlo=48, dhi=120):
    """Z 0-1 packing on every group; s=3 subtotal is exact, all-s total is not.

    R2: the all-s Z01 numbers (611/493) are printed as GLOBAL-Z01; the 274-group
    s=3 subtotal (173/138) is printed separately as STRICT s=3 only.
    """
    print("\n== Z01 packing (NZ unbounded, at most one Z per group) ==")
    print("   GLOBAL-Z01 = all s (NOT exact at s>3).  STRICT s=3 = exact.")
    T = dict(g=0, mix=0, unb=0, st16=0, st6=0)
    T3 = dict(g=0, mix=0, unb=0, st16=0, st6=0, uni6=0, uni16=0)
    empty16 = []; empty6 = []
    d105 = []; d117 = []; d88 = None
    for n in range(dlo, dhi + 1):
        G = collect(n)
        if not G:
            continue
        # whole degree, all s (strict Z on every group)
        a_st16 = a_st6 = a_unb16 = a_mix = 0
        ns3_alive16 = 0
        for key, skels in G.items():
            u = int(skels[0].u)
            items = [(S.V[2], S.q(), S.u) for S in skels]
            hm, _ = MF.mixed_hit(items, 6, 16)
            Um = Umax(skels)
            Nhi6 = max(int(Um), 6)
            pk16 = []
            for S in skels:
                pk16.extend(packets(S, 16))
            h_unb, c_unb, _ = knapsack(pk16, u, 6, 16)
            h16, c16 = knapsack_z01(skels, 6, 16)
            h6, c6 = knapsack_z01(skels, 6, Nhi6)
            h_u1 = bool(MF.uni_hits(items, 6, None))
            h_u2 = bool(MF.uni_hits(items, 6, 16))
            a_mix += int(hm)
            a_unb16 += int(h_unb or c_unb)
            a_st16 += int(h16 or c16)
            a_st6 += int(h6 or c6)
            if skels[0].s == 3:
                T3['g'] += 1
                T3['mix'] += int(hm)
                T3['unb'] += int(h_unb or c_unb)
                T3['st16'] += int(h16 or c16)
                T3['st6'] += int(h6 or c6)
                T3['uni6'] += int(h_u1)
                T3['uni16'] += int(h_u2)
                if h16 or c16:
                    ns3_alive16 += 1
            if n == 105 and (h16 or c16):
                d105.append((key, skels, h16))
            if n == 117 and (h16 or c16):
                d117.append((key, skels, h16))
            if n == 88:
                d88 = (h16 or c16, h6 or c6, key, skels)
        T['g'] += len(G); T['mix'] += a_mix; T['unb'] += a_unb16
        T['st16'] += a_st16; T['st6'] += a_st6
        if a_st16 == 0:
            empty16.append(n)
        if a_st6 == 0:
            empty6.append(n)
        if a_st16 != a_unb16 or n in (88, 105, 112, 117, 120, 80):
            print("   D=%-3d grp=%-4d mix16=%-4d unb16=%-4d z01_16=%-4d z01_>=6=%-4d s3alive16=%d"
                  % (n, len(G), a_mix, a_unb16, a_st16, a_st6, ns3_alive16))
            sys.stdout.flush()
    print("   GLOBAL-Z01 (all s, NOT exact at s>3): mix16 %d  unb16 %d  z01_16 %d  z01_>=6 %d"
          % (T['mix'], T['unb'], T['st16'], T['st6']))
    print("   STRICT s=3 only (exact, %d groups): UNI N>=6 %d  UNI[6,16] %d  mix16 %d  UNB[6,16] %d  z01_>=6 %d  z01_16 %d"
          % (T3['g'], T3['uni6'], T3['uni16'], T3['mix'], T3['unb'], T3['st6'], T3['st16']))
    print("   STRICT s=3 subtotal: %d groups, Z01 N>=6 = %d, Z01 [6,16] = %d"
          % (T3['g'], T3['st6'], T3['st16']))
    print("   empty z01 [6,16]: %s" % (empty16 or "NONE"))
    print("   empty z01 N>=6 : %s" % (empty6 or "NONE"))
    print("   D=88 z01 [6,16]=%s N>=6=%s" % (d88[0] if d88 else None,
                                              d88[1] if d88 else None))
    print("   D=105 z01-alive [6,16]: %d" % len(d105))
    for (key, skels, _) in d105:
        print("      m=%s M=%s Vs=%s" % (key[0], list(key[1]), key[2]))
    print("   D=117 z01-alive [6,16]: %d" % len(d117))
    for (key, skels, _) in d117:
        S = skels[0]
        print("      m=%s M=%s Vs=%s |O|=%s 10/11=%s V2=%s q=%s"
              % (key[0], list(key[1]), key[2], sorted(orbit_sizes(S)),
                 S.cond1011(2)[1:], S.V[2], S.q()))
    return T, empty16, empty6, T3

def list_specials(surv):
    print("\n== SPECIAL DEGREES: orbit-alive counts vs rebase ==")
    for n in LISTING:
        rows = surv.get(n, [])
        print("   D=%d orbit-alive [6,16] groups: %d" % (n, len(rows)))
        if n in (105, 117) or (n == 112 and len(rows) <= 40):
            for (key, skels, h_o2, c2, h_u2, h_mx) in sorted(rows, key=lambda r: r[0]):
                m, Ms, Vs = key
                u = int(skels[0].u)
                V2s = sorted(set(S.V[2] for S in skels))
                oms = sorted(set().union(*[orbit_sizes(S) for S in skels]))
                print("      m=%d M=%s V_s=%d u=%s V2=%s |O|=%s uni=%s mix=%s orb=%s%s"
                      % (m, list(Ms), Vs, u, V2s, oms, h_u2, h_mx, h_o2,
                         " CAPPED" if c2 else ""))

def main():
    print("branch-orbits-v2 knapsack_v2 -- Moh (1)-(13) orbit-aware (R1/R2)")
    print("charged knapsack.py sha256 aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276")
    print("enumerator %s" % os.path.abspath(MF.__file__))
    print("=" * 78)
    control_moh_rows()
    control_s3_Q_eq_u()
    control_mult_on_Cstar()
    if FAILURES:
        print("CONTROLS FAILED before census: %s" % FAILURES)
        sys.exit(1)
    control_rebase_reproduction()
    if FAILURES:
        print("REBASE REPRODUCTION FAILED: %s" % FAILURES)
        sys.exit(1)
    T, surv, d16, d6, e6, e16 = run_orbit()
    list_D105(surv)
    list_specials(surv)
    list_delta(d16, "mix-alive / orbit-dead in [6,16]")
    list_delta(d6, "uni-alive N>=6 / orbit-dead N>=6")
    run_strict_s3()
    print("\n" + "=" * 78)
    if FAILURES:
        print("CONTROLS FAILED (%d): %s" % (len(FAILURES), FAILURES))
        sys.exit(1)
    print("ALL CONTROLS PASSED.  NCHECK=%d" % NCHECK[0])

if __name__ == "__main__":
    main()
