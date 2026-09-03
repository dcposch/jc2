#!/usr/bin/env python3
"""
box/moh_skeleton_full.py -- Moh 1983 search conditions (1)-(13), IMPLEMENTED VERBATIM.

Lane CENSUS-REBASE (opus5, 2026-09-02).  Standard library only.  FAIL-CLOSED:
every control must pass before any census/filter number is printed.

This file is a DERIVED COPY of box/moh_skeleton_N.py: the (1)-(7) + Def 5.1 core
(Skel, census) is RE-DERIVED here from the printed source and then CHECKED, row by
row, against the imported original (CONTROL 0).  box/moh_skeleton_N.py itself is
never modified.  New here: conditions (8)-(13), both branches.

SOURCE (read from 300-dpi renderings of refs/moh1983_jram340_configurations_of_roots.pdf,
sha256 6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51; the
pdftotext OCR in box/depth-drivers-20260902/moh.txt drops all display math there):

  p.201 l.1-8   (4) {n,M_1,...,M_s} is the part of characteristic data of (f,g) which
                    are less than n-2,     (5) d_r = g.c.d.{n, M_1, ..., M_{r-1}}.
  p.201 l.13    (6) 3 <= s <= 5,  d_s >= 4.
  p.201 l.18    (7) V_{r+1}(d_r/d_{r+1}) >= V_r > d_r/(n - M_r).
  p.201 l.20-26 (8) "the radii delta_s,...,delta_1 of D_s,...,D_1 can be computed from
                    Definition 5.1.  We shall consider the increment of the denominator
                    A_{r-1} of delta_{r-1} with respect to delta_s,...,delta_r.  Namely
                    let the l.c.m. of the reduced denominators of delta_s,...,delta_r be
                    L.  Then A_{r-1} is defined to be the reduced denominator of
                    L*delta_{r-1}."
  p.201 l.28    (9) V_r (d_{r-1}/d_r) = TRI_{r-1} A_{r-1} + SQ_{r-1}     [division algorithm]
  p.201 l.30-34 "Let (tbar)^{L A_{r-1}} = t.  Due to the existence of the following
                    automorphism of k<<tbar>> over k<<tbar^{A_{r-1}}>>,  tbar -> omega tbar,
                    where omega is a A_{r-1}-th root of unity, the value of V_{r-1} is
                    further restricted by"
  p.201 l.36   (10) V_{r-1} <= TRI_{r-1}
  p.201 l.38   "if the corresponding factor of p(pi) is of the form pi - a with a != 0
                    or for some j the following"
  p.201 l.41   (11) V_{r-1} = j A_{r-1} + SQ_{r-1}
  p.201 l.43   "if the corresponding factor of p(pi) is of the form pi.  Finally, when
                    r = 2 we must have the following (cf. the proof of Proposition 5.5):"
  p.201 l.46   (12) A_1 | (n/d_2) V_2,   A_1 | (m/d_2) V_2 - 1
  p.201 l.48   "or"
  p.201 l.50   (13) A_1 | (m/d_2) V_2,   A_1 | (n/d_2) V_2 - 1.
  p.201 l.52   "Furthermore we shall note that the situation indicated by the equation
                    (11) can not always happen as established by Proposition 5.6."

  p.179  Definition 5.1(2),(3) -- the windows and the logarithmic radii delta_i.
  p.188  the derivation of (12)/(13): "A | n* V_2 and A -| m* V_2 or A -| n* V_2 and
         A | m* V_2.  Moreover we always have from the very definition of A the
         following  A | (n* + m*) V_2 - 1."
  p.202  the published table of ALL surviving skeletons at n <= 100 (4 (n,m) classes,
         6 rows counting Moh's bracketed alternates) -- the fail-closed control.

INDEXING.  Moh's A_j is the object the TIME-FUNCTION CALIBRATION lane called Delta_j.
Conditions (10)/(11) constrain V_{r-1} for r = s,...,3, i.e. they constrain
V_j for j = s-1,...,2.  (12)/(13) is the separate bottom (r = 2) condition.
"""
import sys, os, time, argparse
from fractions import Fraction as F
from math import gcd, lcm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FAILURES = []
def check(name, cond, detail=""):
    if cond: print("  [ok]   %s" % name)
    else:    print("  [FAIL] %s   %s" % (name, detail)); FAILURES.append(name)

# ===========================================================================
# PART 0.  the (1)-(7) core, re-derived (checked against moh_skeleton_N in CONTROL 0)
# ===========================================================================
class Skel:
    """Moh skeleton (n, m, [M_2..M_s], {i: V_i}).  M_1 = -m, M_s = n-2, V_{s+1} = d_{s+1}."""
    def __init__(self, n, m, Ms, Vs):
        self.n, self.m = n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i+1: full[i] for i in range(s)}
        d = [n]
        for M in full: d.append(gcd(d[-1], M))
        self.d = {i+1: d[i] for i in range(len(d))}
        self.V = dict(Vs); self.V[s+1] = self.d[s+1]
        self.K = self.d[2]; self.e = n//self.K; self.dd = m//self.K
        self.delta = {i: self._delta(i) for i in range(1, s+1)}
        self.u = F(self.V[s]*self.K, self.d[s])

    def _delta(self, i):                              # Def 5.1(3), p.179
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        num = F(n-M[i]); den = F(n-M[s]-1)
        for j in range(i+1, s+1):
            num *= (V[j]*(n-M[j]) - d[j]); den *= (V[j]*(n-M[j-1]) - d[j])
        return 1 - num/den

    def windows_ok(self):                             # search (7) = Def 5.1(2)
        for i in range(2, self.s+1):
            lo = F(self.d[i], self.n-self.M[i]); hi = F(self.V[i+1]*self.d[i], self.d[i+1])
            if not (self.V[i] > lo and self.V[i] <= hi): return False
        return True

    # ---- (8): the increment denominators A_j -----------------------------
    def A(self, j):
        """A_j = reduced denominator of L_j*delta_j,  L_j = lcm{den delta_s,...,den delta_{j+1}}."""
        L = 1
        for i in range(j+1, self.s+1): L = lcm(L, self.delta[i].denominator)
        return (L*self.delta[j]).denominator

    def L(self, j):
        L = 1
        for i in range(j+1, self.s+1): L = lcm(L, self.delta[i].denominator)
        return L

    # ---- (9),(10),(11) at level j = r-1 (j = s-1,...,2) -------------------
    def div9(self, j):
        """(9) with r = j+1:  V_{j+1}(d_j/d_{j+1}) = TRI_j A_j + SQ_j."""
        Q = self.V[j+1]*self.d[j]//self.d[j+1]        # exact: d_{j+1} | d_j
        assert self.V[j+1]*self.d[j] % self.d[j+1] == 0
        A = self.A(j)
        return divmod(Q, A) + (A, Q)                  # (TRI_j, SQ_j, A_j, Q)

    def cond1011(self, j):
        """returns (ok, by10, by11) for level j."""
        tri, sq, A, Q = self.div9(j)
        b10 = (self.V[j] <= tri)                       # (10) alpha != 0
        b11 = ((self.V[j] - sq) % A == 0)              # (11) alpha  = 0
        return (b10 or b11), b10, b11

    def cond1213(self):
        """(12)/(13) at r = 2, with n* = n/d_2, m* = m/d_2."""
        A1 = self.A(1); ns, ms, V2 = self.e, self.dd, self.V[2]
        b12 = (ns*V2 % A1 == 0) and ((ms*V2 - 1) % A1 == 0)
        b13 = (ms*V2 % A1 == 0) and ((ns*V2 - 1) % A1 == 0)
        return (b12 or b13), b12, b13

    def full_ok(self):
        """(8)-(13) verbatim."""
        for j in range(self.s-1, 1, -1):
            if not self.cond1011(j)[0]: return False
        return self.cond1213()[0]

    def any10(self):
        """at least one level j in {2..s-1} admits the alpha != 0 branch (10).
           = the numerical shadow of Moh's Prop 5.6 remark ('(11) can not always happen')."""
        return any(self.cond1011(j)[1] for j in range(self.s-1, 1, -1))

    # ---- integration-#17 quantities --------------------------------------
    def q(self):
        """D1-PIN:  q = (1-delta_1) d e/(d+e), the contribution of one unit of V_2 to N."""
        return (1 - self.delta[1]) * F(self.dd*self.e, self.dd+self.e)

def divisor_chains(K, floor=4):
    out = []
    def rec(cur, ch):
        for dd in range(floor, cur):
            if cur % dd == 0: out.append(ch+[dd]); rec(dd, ch+[dd])
    rec(K, []); return out

def census(n, Kmin=16, with_V=True, full=False):
    """(1)-(7) [+ (8)-(13) if full] enumeration at degree n = deg g.
       Yields (m, (M_2..M_s), {i: V_i}).  full=True prunes with (10)/(11) inside the
       recursion and applies (12)/(13) at the bottom."""
    for K in range(Kmin, n//3+1):
        if n % K: continue
        e = n//K
        if e < 3: continue
        for ch in divisor_chains(K, 4):
            dfull = [n, K]+ch; dfull.append(gcd(dfull[-1], n-2))
            s = 2+len(ch)
            d = {i+1: dfull[i] for i in range(len(dfull))}
            dlist = ([K]+ch)[:-1]; tg = ch
            for dd in range(2, e):
                if gcd(dd, e) != 1: continue
                m = K*dd
                M = {1: -m, s: n-2}
                def Mrec(i, prev):
                    if i == s:
                        if prev < n-2: yield True
                        return
                    for Mi in range(prev+1, n-2):
                        if gcd(dlist[i-2], Mi) == tg[i-2]:
                            M[i] = Mi; yield from Mrec(i+1, Mi)
                for _ in Mrec(2, -m):
                    Ms = [M[i] for i in range(2, s+1)]
                    if not with_V:
                        yield (m, tuple(Ms), None); continue
                    V = {s+1: d[s+1]}
                    # R_i = prod_{j>i} P_j/Q_j  ;  delta_i = 1 - (n-M_i) R_i/(n-M_s-1)
                    def delta_of(i, R): return 1 - F(n-M[i])*R/F(n-M[s]-1)
                    def Vrec(i, R, Lcm):
                        # R = R_i (needs V_{i+1..s}); Lcm = lcm{den delta_s..den delta_{i+1}}
                        if i == 1:
                            yield None; return
                        lo = F(d[i], n-M[i]); hiQ = V[i+1]*d[i]//d[i+1]
                        w0 = lo.numerator//lo.denominator + 1
                        cand = range(max(w0, 1), hiQ+1)
                        if full and i <= s-1:
                            di = delta_of(i, R)
                            A = (Lcm*di).denominator
                            tri, sq = divmod(hiQ, A)
                            cand = [w for w in cand if w <= tri or (w - sq) % A == 0]
                        for w in cand:
                            if i == s and w >= d[s]: continue
                            V[i] = w
                            R2 = R*F(V[i]*(n-M[i])-d[i], V[i]*(n-M[i-1])-d[i])
                            if full and i == 2:
                                d1 = delta_of(1, R2)
                                Lc = lcm(Lcm, delta_of(2, R).denominator)
                                A1 = (Lc*d1).denominator
                                ns, ms_ = n//d[2], m//d[2]
                                b12 = (ns*w % A1 == 0) and ((ms_*w - 1) % A1 == 0)
                                b13 = (ms_*w % A1 == 0) and ((ns*w - 1) % A1 == 0)
                                if not (b12 or b13): continue
                                yield None; continue
                            Lc = lcm(Lcm, delta_of(i, R).denominator) if full else 1
                            yield from Vrec(i-1, R2, Lc)
                        V.pop(i, None)
                    for _ in Vrec(s, F(1), 1):   # L_s = lcm over empty range = 1

                        yield (m, tuple(Ms), {i: V[i] for i in range(2, s+1)})

# p.202 table, transcribed verbatim (Moh's bracketed alternates split into rows).
# last field = ERRATUM flag: the printed delta_1 disagrees with Def 5.1(3).
MOH_TABLE = [
    (64,48,[52,62],{3:3,2:3}, "(64,48)",             F(1,4), F(9,16), False),
    (84,56,[64,82],{3:3,2:2}, "(84,56) M2=64,V2=2",  F(2,7), F(16,21), False),
    (84,56,[72,82],{3:3,2:5}, "(84,56) M2=72,V2=5",  F(1,4), F(7,12), False),
    (75,50,[55,73],{3:4,2:3}, "(75,50) V2=3",        F(1,5), F(1,2), False),
    (75,50,[55,73],{3:4,2:2}, "(75,50) V2=2",        F(1,5), F(1,3), True),
    (99,66,[77,97],{3:8,2:8}, "(99,66)",             F(1,3), F(4,9), False),
]
# ERRATUM (PROVED-HERE, control_1): the bracketed alternate of the n=75 row prints
# delta_1 = 1/3.  Def 5.1(3) at (n,m,M_2,M_3,V_3,V_2) = (75,50,55,73,4,2) gives 2/3,
# and delta_1 = 1/3 is attained by NO (1)-(7)-admissible skeleton at (75,50) at all
# (exhaustive check below), so 1/3 is a misprint for 2/3.  Everything else on p.202
# reproduces exactly, including the other two bracketed alternates.

# ===========================================================================
# PART 1.  CONTROLS  (all must pass before any number is printed)
# ===========================================================================
def control_0_core_identical():
    """the re-derived (1)-(7) core reproduces box/moh_skeleton_N.py exactly."""
    print("\n-- CONTROL 0: re-derived (1)-(7) core == box/moh_skeleton_N.py --")
    import moh_skeleton_N as O
    bad = 0; tot = 0
    for n in range(48, 91):
        a = list(census(n)); b = list(O.census(n))
        tot += len(a)
        if a != b: bad += 1; print("     mismatch at n=%d: %d vs %d" % (n, len(a), len(b)))
    check("census identical to moh_skeleton_N for 48<=n<=90 (%d V-assignments)" % tot, bad == 0)
    bad = 0
    for n in (48, 60, 64, 75, 84, 90, 99):
        for (m, Ms, V) in census(n):
            S, T = Skel(n, m, list(Ms), V), O.Skel(n, m, list(Ms), V)
            if S.delta != T.delta or S.u != T.u or S.windows_ok() != T.windows_ok(): bad += 1
    check("Skel delta/u/windows identical on 7 degrees", bad == 0, str(bad))

def control_1_delta_table():
    """Moh p.202 prints delta_2 and delta_1 for every survivor row."""
    print("\n-- CONTROL 1: Def 5.1(3) reproduces Moh's printed delta columns (p.202) --")
    print("   %-24s %8s %8s   %8s %8s" % ("row", "delta_2", "delta_1", "printed", "printed"))
    for (n,m,Ms,Vs,lab,p2,p1,err) in MOH_TABLE:
        S = Skel(n,m,Ms,Vs)
        print("   %-24s %8s %8s   %8s %8s %s" % (lab, S.delta[2], S.delta[1], p2, p1,
              "<- ERRATUM: printed delta_1 unattainable" if err else ""))
        if not err:
            check("delta_2,delta_1 = p.202 for %s" % lab, (S.delta[2],S.delta[1])==(p2,p1),
                  "%s,%s" % (S.delta[2], S.delta[1]))
        else:
            check("delta_2 = p.202 for %s" % lab, S.delta[2]==p2, str(S.delta[2]))
            check("ERRATUM: printed delta_1=%s attained by NO (1)-(7) skeleton at (%d,%d)"
                  % (p1, n, m),
                  not any(Skel(n,mm,list(MM),VV).delta[1] == p1
                          for (mm,MM,VV) in census(n, Kmin=2) if mm == m))
            check("ERRATUM: Def 5.1(3) gives delta_1 = 2/3 for %s" % lab,
                  S.delta[1] == F(2,3), str(S.delta[1]))
        check("delta_s = -1 for %s" % lab, S.delta[S.s] == -1)

def control_2_moh_rows_pass():
    """FAIL-CLOSED: every printed row must satisfy (1)-(13)."""
    print("\n-- CONTROL 2: Moh's six published rows satisfy (1)-(13) --")
    print("   %-24s %3s %4s %4s %4s %4s %4s %5s %5s %5s %6s %6s" %
          ("row","s","L_2","A_2","TRI2","SQ2","V_2","(10)","(11)","L_1","A_1","(12)/(13)"))
    for (n,m,Ms,Vs,lab,_,_,_) in MOH_TABLE:
        S = Skel(n,m,Ms,Vs)
        ok1011, b10, b11 = S.cond1011(2)
        tri, sq, A2, Q = S.div9(2)
        ok1213, b12, b13 = S.cond1213()
        print("   %-24s %3d %4d %4d %4d %4d %4d %5s %5s %5d %6d %6s" %
              (lab, S.s, S.L(2), A2, tri, sq, S.V[2], b10, b11, S.L(1), S.A(1),
               ("(12)" if b12 else "")+("(13)" if b13 else "")))
        check("(7) windows %s" % lab, S.windows_ok())
        for j in range(S.s-1, 1, -1):
            check("(10)or(11) at j=%d %s" % (j, lab), S.cond1011(j)[0])
        check("(12)or(13) %s" % lab, ok1213)
        check("full_ok %s" % lab, S.full_ok())
        # the p.188 identity  A | (n*+m*)V_2 - 1  ("from the very definition of A")
        check("p.188 identity A_1 | (n*+m*)V_2-1 %s" % lab,
              ((S.e+S.dd)*S.V[2]-1) % S.A(1) == 0)

def control_3_prune_equals_filter():
    """the in-recursion pruning (fast path) == post-filtering by full_ok (slow path)."""
    print("\n-- CONTROL 3: in-recursion (8)-(13) pruning == post-filter by full_ok --")
    bad = tot = 0
    for n in range(48, 76):
        fast = list(census(n, full=True))
        slow = [(m,Ms,V) for (m,Ms,V) in census(n) if Skel(n,m,list(Ms),V).full_ok()]
        tot += len(fast)
        if fast != slow:
            bad += 1; print("     n=%d fast=%d slow=%d" % (n, len(fast), len(slow)))
    check("fast == slow for 48<=n<=75 (%d survivors)" % tot, bad == 0)

def control_4_moh_table_is_complete():
    """FAIL-CLOSED, the decisive control: at n <= 100 Moh's program 'produces only the
       following exceptions' (p.202).  Run (1)-(13) over Moh's own space (no GGV K>=16,
       no D>=48) and compare the output set with the printed table."""
    print("\n-- CONTROL 4: (1)-(13) over Moh's own n <= 100 space vs the p.202 table --")
    out = []
    t0 = time.time()
    for n in range(4, 101):
        for (m, Ms, V) in census(n, Kmin=2, full=True):
            out.append((n, m, Ms, tuple(sorted(V.items()))))
    print("   (1)-(13) survivors at n <= 100 (Kmin=2, Moh's own space): %d   [%.1fs]"
          % (len(out), time.time()-t0))
    for r in sorted(out):
        n, m, Ms, V = r
        print("      n=%-4d m=%-4d M_2..M_s=%-16s V=%s" % (n, m, list(Ms), dict(V)))
    printed = set((n, m, tuple(Ms), tuple(sorted(Vs.items())))
                  for (n,m,Ms,Vs,_,_,_,_) in MOH_TABLE)
    got = set(out)
    # FAIL-CLOSED half: every printed row must survive.  This is the half that can
    # falsify the transcription, and it passes.
    check("every p.202 row survives (1)-(13)", printed <= got,
          "missing %s" % sorted(printed - got))
    # MEASURED half: (1)-(13) as PRINTED does NOT cut n<=100 down to the table.
    # Reported, not asserted -- see OPEN[MOH-PROGRAM] in the report.
    print("   MEASURED: (1)-(13) leaves %d rows / %d (n,m) classes at n <= 100;"
          " Moh's table has %d rows / 4 classes.  Excess %d."
          % (len(got), len(set((r[0],r[1]) for r in got)), len(printed), len(got-printed)))
    print("   => the printed list (1)-(13) is NOT the whole of Moh's program.")
    return got, printed

def control_5_moh_counts_at_75_50():
    """p.202 l.-8: 'given deg g = 75 deg f = 50 there are 25 possible values for M_2 and
       2 possible values for V_3 etc.  The above table determines only one possible value
       for M_2 and one for V_3.'"""
    print("\n-- CONTROL 5: Moh's own counts at (n,m) = (75,50) --")
    M2 = sorted(set(Ms[0] for (m,Ms,_) in census(75, Kmin=2, with_V=False) if m == 50))
    V3 = sorted(set(V[3] for (m,Ms,V) in census(75, Kmin=2) if m == 50))
    print("   (1)-(7): #M_2 = %d %s ;  #V_3 = %d %s" % (len(M2), M2, len(V3), V3))
    surv = [(Ms, V) for (m,Ms,V) in census(75, Kmin=2, full=True) if m == 50]
    M2f = sorted(set(Ms[0] for (Ms,_) in surv)); V3f = sorted(set(V[3] for (_,V) in surv))
    print("   (1)-(13): #M_2 = %d %s ;  #V_3 = %d %s ; rows %s"
          % (len(M2f), M2f, len(V3f), V3f, [(list(Ms), dict(V)) for (Ms,V) in surv]))
    # Moh's "25 possible values for M_2" is the a-priori count: the multiples of
    # d_3 = 5 in the range [M_1, n-2) = [-50, 73).  (The census's own count, after
    # gcd(d_2,M_2) = d_3 exactly and M_2 > M_1, is 20 of those 25.)
    apriori = [x for x in range(-50, 73) if x % 5 == 0]
    check("Moh's '25 possible values for M_2' = #multiples of d_3 in [M_1, n-2)",
          len(apriori) == 25, str(len(apriori)))
    check("Moh's '2 possible values for V_3' at (75,50)", len(V3) == 2, str(V3))
    check("Moh's 'only one possible value for V_3' after (1)-(13)", V3f == [4], str(V3f))
    print("   MEASURED: after (1)-(13), M_2 is NOT pinned at (75,50): %s (Moh: only 55)"
          % M2f)

def control_6_calibration_lane():
    """the TIME-FUNCTION CALIBRATION lane's (10)_1 vs Moh's printed (12)/(13)."""
    print("\n-- CONTROL 6: calibration lane's (10)_1 vs Moh's printed (12)/(13) --")
    print("   (10)_1   : e*V_2 = 0 or 1 (mod A_1)          [one congruence]")
    print("   (12)/(13): (e V_2, d V_2) = (0,1) or (1,0) (mod A_1)  [conjunction]")
    weaker = strictly = tot = badid = 0
    for n in range(48, 101):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V); tot += 1
            A1 = S.A(1); c1 = (S.e*S.V[2]) % A1 in (0, 1 % A1)
            c2 = S.cond1213()[0]
            if c2 and not c1: weaker += 1
            if c1 and not c2: strictly += 1
            if ((S.e+S.dd)*S.V[2] - 1) % A1 != 0: badid += 1
    print("   %d V-assignments (48<=D<=100): (12)/(13) holds but (10)_1 fails: %d ;"
          " (10)_1 holds but (12)/(13) fails: %d" % (tot, weaker, strictly))
    print("   p.188 identity A_1 | (n*+m*)V_2 - 1 fails on %d of them" % badid)
    check("(12)/(13) IMPLIES (10)_1", weaker == 0)
    # MEASURED, and the reason: Moh's p.188 identity A_1 | (n*+m*)V_2-1 holds
    # identically on the census, and given it, (12) <=> A_1 | e V_2 and
    # (13) <=> A_1 | e V_2 - 1.  So (12)v(13) <=> (10)_1: the calibration lane's
    # congruence is EQUIVALENT to Moh's printed pair, not weaker.
    check("p.188 identity A_1 | (n*+m*)V_2-1 holds census-wide 48<=D<=100", badid == 0,
          str(badid))
    check("(12)v(13) <=> (10)_1 on the census (equivalent, not weaker)",
          weaker == 0 and strictly == 0, "%d/%d" % (weaker, strictly))

def control_7_reconstruction_of_10():
    """the calibration lane's reconstructed (10) at j>=2, 'A_j V_j <= V_{j+1}d_j/d_{j+1}',
       is EQUIVALENT to Moh's printed (10) 'V_j <= TRI_j' (division is exact in Z)."""
    print("\n-- CONTROL 7: reconstructed (10) == Moh's printed (10); (11) is the gap --")
    bad = only11 = tot = 0
    for n in range(48, 101):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            for j in range(S.s-1, 1, -1):
                tot += 1
                tri, sq, A, Q = S.div9(j)
                if (S.V[j] <= tri) != (A*S.V[j] <= Q): bad += 1
                ok, b10, b11 = S.cond1011(j)
                if b11 and not b10: only11 += 1
    print("   %d (level, V-assignment) pairs at 48<=D<=100: printed (10) != reconstructed"
          " (10) in %d ; admitted ONLY by the alpha=0 branch (11): %d" % (tot, bad, only11))
    check("reconstructed (10) is equivalent to printed (10)", bad == 0)
    check("branch (11) is non-vacuous (the calibration lane's OPEN[MOH-11] was real)",
          only11 > 0, str(only11))

def run_controls():
    control_0_core_identical(); control_1_delta_table(); control_2_moh_rows_pass()
    control_3_prune_equals_filter(); control_4_moh_table_is_complete()
    control_5_moh_counts_at_75_50(); control_6_calibration_lane()
    control_7_reconstruction_of_10()
    print("\n" + "="*78)
    if FAILURES:
        print("CONTROLS FAILED (%d): %s" % (len(FAILURES), FAILURES)); sys.exit(1)
    print("ALL CONTROLS PASSED.")

# ===========================================================================
# PART 2.  the integration-#17 programme, rerun on the (1)-(13) space
# ===========================================================================
#   D1-PIN (integration #17 A.3):  N = sum_B V_2(B) q(B),  sum_B V_2(B) <= u,
#   q = (1-delta_1) d e/(d+e).  Group = (m, M_2..M_s, V_s): V_s is the only global
#   datum (the multiplicity split of the top form); V_{s-1..2} are per-branch.
NLO, NHI = 6, 16          # integration #17 A.8: the frontier floor N >= 6; H2 window [6,16]

def groups_of(n, full=True, Kmin=16):
    """{(m, Ms, V_s): [(V_2, q, u), ...]} over the admissible V-assignments."""
    G = {}
    for (m, Ms, V) in census(n, Kmin=Kmin, full=full):
        S = Skel(n, m, list(Ms), V)
        G.setdefault((m, Ms, S.V[S.s]), []).append((S.V[2], S.q(), S.u))
    return G

def uni_hits(items, Nlo=NLO, Nhi=None):
    """(UNI): one Galois orbit of bottom discs.  N = k V_2 q with k V_2 <= u."""
    out = set()
    for (v, q, u) in items:
        for k in range(1, int(u)//v + 1):
            val = k*v*q
            if val.denominator == 1 and val >= Nlo and (Nhi is None or val <= Nhi):
                out.add(int(val))
    return out

def mixed_hit(items, Nlo=NLO, Nhi=NHI, CAP=60000):
    """no (UNI): N = sum_B V_2(B) q(B), sum V_2(B) <= u.  Exact knapsack over
       Fractions, pruned to partial sums <= Nhi.  CAP -> UNDECIDED (counted alive)."""
    u = int(items[0][2])
    cand = sorted(set((v, q) for (v, q, _) in items if v*q <= Nhi))
    layer = {0: {F(0)}}; capped = False
    for tv in range(0, u+1):
        if tv not in layer: continue
        for s0 in list(layer[tv]):
            for (v, q) in cand:
                if tv+v > u: continue
                s1 = s0 + v*q
                if s1 > Nhi: continue
                tgt = layer.setdefault(tv+v, set())
                if len(tgt) >= CAP: capped = True; continue
                tgt.add(s1)
                if s1.denominator == 1 and Nlo <= s1 <= Nhi: return True, capped
    return False, capped

def rerun(dlo=48, dhi=120, full=True, Kmin=16, listing=(105,108,112,117,120), do_mixed=True):
    tag = "(1)-(13)" if full else "(1)-(7)"
    print("\n== INTEGRATION-#17 RERUN on the %s space, %d <= D <= %d ==" % (tag, dlo, dhi))
    print("   %5s %9s %9s %9s %9s %9s %9s %9s" % ("D", "V-assign", "groups",
          "uni N>=6", "uni[6,16]", "mix[6,16]", "capped", "wall"))
    T = dict(a=0, g=0, u1=0, u2=0, mx=0, cap=0); empty = []; surv = {}
    for n in range(dlo, dhi+1):
        t0 = time.time(); G = groups_of(n, full=full, Kmin=Kmin)
        na = sum(len(v) for v in G.values())
        if not G: continue
        a1 = a2 = am = cp = 0; alive = []
        for key, items in G.items():
            h1 = bool(uni_hits(items, NLO, None))
            h2 = bool(uni_hits(items, NLO, NHI))
            if do_mixed: hm, c = mixed_hit(items)
            else:        hm, c = h2, False
            a1 += h1; a2 += h2; am += (hm or c); cp += c
            if hm or c: alive.append((key, items, c))
        T['a'] += na; T['g'] += len(G); T['u1'] += a1; T['u2'] += a2
        T['mx'] += am; T['cap'] += cp
        if am == 0: empty.append(n)
        if n in listing: surv[n] = alive
        print("   %5d %9d %9d %9d %9d %9d %9d %8.1fs"
              % (n, na, len(G), a1, a2, am, cp, time.time()-t0)); sys.stdout.flush()
    print("   ---- totals %d <= D <= %d ----" % (dlo, dhi))
    print("   V-assignments %d ; groups %d" % (T['a'], T['g']))
    print("   (UNI) alive with an integer N >= 6            : %d  (killed %d)"
          % (T['u1'], T['g']-T['u1']))
    print("   (UNI) alive with an integer N in [6,16]       : %d  (killed %d)"
          % (T['u2'], T['g']-T['u2']))
    print("   mixed (no (UNI)) alive in [6,16]              : %d  (killed %d, capped %d)"
          % (T['mx'], T['g']-T['mx'], T['cap']))
    print("   degrees D with EVERY group killed             : %s" % (empty if empty else "NONE"))
    return T, empty, surv

def list_survivors(surv):
    print("\n== SURVIVING GROUPS, listed in full ==")
    for n in sorted(surv):
        print("\n   -- D = %d : %d surviving groups --" % (n, len(surv[n])))
        print("      %4s %4s %-18s %4s %4s %6s %6s %-24s %-22s %s"
              % ("n","m","M_2..M_s","V_s","K","(d,e)","u","V_2 (per branch)","q (per branch)","achievable N"))
        for (key, items, capped) in sorted(surv[n]):
            (m, Ms, Vs) = key
            K = gcd(n, m); e = n//K; dd = m//K
            V2s = sorted(set(v for (v,_,_) in items)); qs = sorted(set(q for (_,q,_) in items))
            Ns = sorted(uni_hits(items, NLO, NHI))
            print("      %4d %4d %-18s %4d %4d %6s %6s %-24s %-22s %s%s"
                  % (n, m, str(list(Ms)), Vs, K, "(%d,%d)"%(dd,e), str(items[0][2]),
                     str(V2s)[:24], str([str(q) for q in qs])[:22], Ns,
                     "  [CAPPED]" if capped else ""))

def deltas_of(n, m, Ms, V):
    return Skel(n, m, list(Ms), V).delta

def count_only(dlo, dhi, full=True, Kmin=16):
    print("\n== COUNT ONLY (no knapsack), %d <= D <= %d, %s ==" %
          (dlo, dhi, "(1)-(13)" if full else "(1)-(7)"))
    print("   %5s %12s %10s %10s" % ("D", "V-assign", "groups", "wall"))
    ta = tg = 0
    for n in range(dlo, dhi+1):
        t0 = time.time(); G = groups_of(n, full=full, Kmin=Kmin)
        na = sum(len(v) for v in G.values())
        if not G: continue
        ta += na; tg += len(G)
        print("   %5d %12d %10d %9.1fs" % (n, na, len(G), time.time()-t0)); sys.stdout.flush()
    print("   TOTAL %d <= D <= %d : V-assignments %d, groups %d" % (dlo, dhi, ta, tg))
    return ta, tg

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="controls")
    ap.add_argument("--dlo", type=int, default=48)
    ap.add_argument("--dhi", type=int, default=120)
    a = ap.parse_args()
    print("box/moh_skeleton_full.py -- Moh (1)-(13) [lane CENSUS-REBASE]")
    print("=" * 78)
    if a.mode == "controls":
        run_controls()
    elif a.mode == "rerun":
        run_controls()
        T, empty, surv = rerun(a.dlo, a.dhi)
        list_survivors(surv)
    elif a.mode == "count":
        count_only(a.dlo, a.dhi)
    elif a.mode == "count7":
        count_only(a.dlo, a.dhi, full=False)

if __name__ == "__main__":
    main()
