"""Cross-check of the LEMMA identities on the six p.207-type controls and
three seeded-random operative rows.  Every number here is also derived by hand
in the report; this file is a check, not the derivation."""
import json, random, sys
from fractions import Fraction as Q
from math import gcd, lcm
sys.path.insert(0, '/home/ubuntu/jc2')
from box.lib.descend_own import descend_own

class Skel:
    def __init__(self, n, m, M, V):
        self.n, self.m = n, m
        self.s = len(M)
        self.M = {i+1: v for i, v in enumerate(M)}
        self.V = {i+2: v for i, v in enumerate(V)}

def parent(n, m, M, V):
    s = len(M); d = {1: n}
    Md = {i+1: v for i, v in enumerate(M)}
    Vd = {i+2: v for i, v in enumerate(V)}
    for i in range(1, s+1): d[i+1] = gcd(d[i], Md[i])
    Vd[s+1] = d[s+1]
    delta = {}
    for i in range(1, s+1):
        r = Q(n-Md[i], n-Md[s]-1)
        for j in range(i+1, s+1):
            r *= Q(Vd[j]*(n-Md[j])-d[j], Vd[j]*(n-Md[j-1])-d[j])
        delta[i] = 1-r
    return s, Md, d, Vd, delta

def A_moh(delta, s):
    L = 1
    for i in range(2, s+1): L = lcm(L, delta[i].denominator)
    return (L*delta[1]).denominator, L

def PQ(n, Md, d, Vd, i):
    return Q(Vd[i+1]*d[i], d[i+1]), Q(Vd[i+1]*(n-Md[i]), d[i+1])

def report(tag, n, m, M, V):
    s, Md, d, Vd, delta = parent(n, m, M, V)
    ds, vs = d[s], Vd[s]; us, ell = ds-vs, 2*vs-ds-1; c = Q(us, ds)
    A1m, L = A_moh(delta, s)
    N, Mm = Q(n, d[2])*Vd[2], Q(m, d[2])*Vd[2]
    out = descend_own(Skel(n, m, M, V))
    np_, mp_ = out['n'], out['m']; Mp, dp = out['M'], out['d']; sp = out['s']
    print(f"\n== {tag}: n={n} m={m} s={s} M={M} V={V}")
    print(f"   d={[d[i] for i in range(1,s+2)]} delta={[str(delta[i]) for i in range(1,s+1)]}")
    print(f"   d_s={ds} v_s={vs} u_s={us} ell={ell} c={c} L={L} A_1^moh={A1m} N={N} M={Mm}")
    print(f"   child n'={np_} m'={mp_} s'={sp} M'={Mp} d'={dp} dropped={out['dropped']}"
          f" route={out['route_state']} V'={out['V_vectors']}")
    print(f"   lattice scale check: n'=c*n {np_==c*n}  m'=c*m {mp_==c*m}"
          f"  M'_i=c*M_i {all(out['raw_M'][i]==c*Md[i] for i in out['raw_M'])}"
          f"  d'_i=c*d_i {all(out['raw_d'][i]==c*d[i] for i in out['raw_d'])}")
    for rad in out['child_radii']:
        j = rad['first_nonzero']; met = rad['delta']
        Vp = {i: rad['V'][i-2] for i in range(2, sp+1)}; Vp[sp+1] = dp[sp+1]
        # child Def 5.1(3) with multiplier ell+1, computed here from the print formula
        f51 = {}
        for i in range(1, sp+1):
            r = Q(np_-Mp[i], np_-Mp[sp]-1)
            for jj in range(i+1, sp+1):
                r *= Q(Vp[jj]*(np_-Mp[jj])-dp[jj], Vp[jj]*(np_-Mp[jj-1])-dp[jj])
            f51[i] = (ell+1)*(1-r)
        Lp = 1
        for i in range(2, sp+1): Lp = lcm(Lp, met[i].denominator)
        A1p = (Lp*met[1]).denominator
        Np, Mmp = Q(np_, dp[2])*Vp[2], Q(mp_, dp[2])*Vp[2]
        e = delta[j]
        mob = all(met[i] == vs - Q(us)/delta[i] for i in range(j, sp+1))
        aff = all(met[i] == vs - us - Q(us)/e*(1-delta[i]) for i in range(1, j+1))
        print(f"   route j={j}: delta'={[str(met[i]) for i in range(1,sp+1)]}"
              f" | (ell+1)*Def5.1(3)={[str(f51[i]) for i in range(1,sp+1)]} agree={f51==met}")
        print(f"      mobius(i>=j)={mob} affine(i<=j)={aff} L'={Lp} A'_1={A1p}"
              f" [den(({us}/e)*b*delta_1)={(Q(us,gcd(delta[j].numerator,us))*delta[j].denominator*delta[1]).denominator}]"
              f" A'_1|A_1^moh={A1m % A1p == 0}  N'={Np} M'={Mmp} N'=N {Np==N} M'=M {Mmp==Mm}")
        pq = []
        for i in range(2, sp):
            P, Qq = PQ(n, Md, d, Vd, i); Pp, Qp = Q(Vp[i+1]*dp[i], dp[i+1]), Q(Vp[i+1]*(np_-Mp[i]), dp[i+1])
            pq.append((i, str(P), str(Qq), str(Pp), str(Qp), Vp[i+1] == Vd[i+1], P/Qq == Pp/Qp))
        print(f"      P,Q levels 2..s'-1: {pq}")
        lpp = dp[sp]-3-ell
        print(f"      l''=d'_s'-3-ell={lpp}  closed form d_(s-1)/d_s-d_s={Q(d[s-1],ds)-ds if us==1 else 'n/a'}"
              f"  general u_s*d_(s-1)/d_s-d_s+2u_s-2={c*d[s-1]-ds+2*us-2}")
        lo = Q(dp[sp], np_-Mp[sp]); lop = Q(d[s-1], n-Md[s-1])
        print(f"      lo'=d'_s'/(n'-M'_s')={lo} lo_(s-1)={lop} equal={lo==lop}"
              f"  delta'_s'=-1 iff n-M_(s-1)=d_s(d_s-1): {met[sp]==-1} vs {n-Md[s-1]==ds*(ds-1)}")

CTRL = [("R004 (64,48) Moh p.207 row 1", 64, 48, [-48,52,62], [3,3]),
        ("R001 (84,56) Moh p.207 row 2", 84, 56, [-56,64,82], [2,3]),
        ("R007 (84,56) Moh p.207 row 2 bracket", 84, 56, [-56,72,82], [5,3]),
        ("R002 (75,50) Moh p.207 row 3 bracket", 75, 50, [-50,55,73], [2,4]),
        ("R003 (75,50) Moh p.207 row 3", 75, 50, [-50,55,73], [3,4]),
        ("R015 (99,66) p.202 control", 99, 66, [-66,77,97], [8,8])]
for t in CTRL: report(*t)

rows = json.load(open('/home/ubuntu/jc2/box/child-own-v-20260905/enumerated-source-rows.json'))['rows']
rnd = random.Random(20260905)
for k, idx in enumerate(rnd.sample(range(len(rows)), 3), 1):
    r = rows[idx]
    report(f"RANDOM-{k} (census index {idx})", r['n'], r['m'], [-r['m']]+r['Ms'],
           [r['V'][str(i)] for i in range(2, len(r['Ms'])+2)])

# --- defined quantities on EMPTY-own-V rows (replay Sec.3 accounting) ---
print("\n\n=== EMPTY-row defined quantities (three seeded-random operative rows) ===")
rnd2 = random.Random(20260905)
for k, idx in enumerate(rnd2.sample(range(len(rows)), 3), 1):
    r = rows[idx]; n, m = r['n'], r['m']
    M = [-m]+r['Ms']; V = [r['V'][str(i)] for i in range(2, len(r['Ms'])+2)]
    s, Md, d, Vd, delta = parent(n, m, M, V)
    ds, vs = d[s], Vd[s]; us, ell = ds-vs, 2*vs-ds-1; c = Q(us, ds)
    out = descend_own(Skel(n, m, M, V))
    np_, mp_, Mp, dp, sp = out['n'], out['m'], out['M'], out['d'], out['s']
    N, Mm = Q(n, d[2])*Vd[2], Q(m, d[2])*Vd[2]
    Np, Mmp = Q(np_, dp[2])*Vd[2], Q(mp_, dp[2])*Vd[2]   # V'_2 = V_2, level2_identity
    A1m, L = A_moh(delta, s)
    lpp = Q(d[s-1], ds)-ds
    print(f"RANDOM-{k} idx={idx} (n,m)=({n},{m}) s={s} u_s={us} ell={ell} route={out['route_state']}")
    print(f"   n'/d'_2={Q(np_,dp[2])}=n/d_2={Q(n,d[2])} m'/d'_2={Q(mp_,dp[2])}=m/d_2={Q(m,d[2])}"
          f"  V'_2={out['level2_identity']['values']} -> N'={Np}=N={N} {Np==N}, M'={Mmp}=M={Mm} {Mmp==Mm}")
    print(f"   A_1^moh={A1m} (L={L}); A'_1 UNDEFINED (own V empty); P'_j,Q'_j UNDEFINED")
    print(f"   P_i/Q_i threshold transport all i<s: "
          f"{[ (i, str(Q(d[i],n-Md[i])), str(Q(out['raw_d'][i], np_-out['raw_M'][i]))) for i in range(1,s) ]}")
    print(f"   l''=d_(s-1)/d_s-d_s={lpp} (=d'_s'-3-ell={dp[sp]-3-ell}); "
          f"SD needs delta'_s'=-1 <=> n-M_(s-1)={n-Md[s-1]} == d_s(d_s-1)={ds*(ds-1)}: {n-Md[s-1]==ds*(ds-1)}; "
          f"lo_(s-1)={Q(d[s-1],n-Md[s-1])} (simple point minor iff >=1: {Q(d[s-1],n-Md[s-1])>=1})")
