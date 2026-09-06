#!/usr/bin/env python3
"""Independent hostile-gate recomputation of the shifted final-major child sums.

Own code; nothing imported from the lane driver.  Rules re-derived from the
print (Moh 1983, JRAM 340), page images read directly:

  Def 5.1(2) p.179 : V_{i+1} d_i/d_{i+1} >= V_i > d_i/(n-M_i),  V_{s+1}=d_{s+1}
  Def 5.1(3) p.179 : delta_i = 1 - (n-M_i) PROD_{j=i+1..s}[V_j(n-M_j)-d_j]
                             / ( (n-M_s-1) PROD_{j=i+1..s}[V_j(n-M_{j-1})-d_j] )
                     ell-shift (p.171 Remark (3)*): the bracket scales by H=1+ell
  Def 5.1(4) p.179 : Prop 4.6 holds at each tower disc, v = V_{i+1} d_i/d_{i+1}
  Prop 4.6   p.170 : deg p = v =: P_i ; T*_{r,sigma}=p^E q, deg q = v(n-M_r)/d_r =: Q_i
                     q squarefree; roots(p) subset roots(q); p not a power of q;
                     r=1 => D(n,-M_1,g_s,T*_1) = nonzero constant (=> squarefree+coprime)
  p.171 (6)        : reduces to  P p q' - Q p' q = c p, c != 0  =>  mult != P/Q
  Prop 5.3   p.180 : ANY factor with V_r > d_r/(n-M_r) yields D_{r-1}, the MINIMAL
                     disc on its cluster, at the prescribed radius; the extended
                     tower is again a tower of major discs.
"""
import json, hashlib
from fractions import Fraction as F
from itertools import product

MAN = "/tmp/jc2-lane.gFUAtE/inputs"
EXPECT = {
 "six-rows-child-sum-sol56-20260906.md":"20e01ccd41b0df8f58439698538023010a74c018fa2eab9aaef1d8af1f89fe09",
 "audit.py":"218460521fdc1175fa3cdfb6b4321f47d8ba027bc28b3d279e10a0bc3e50b9c3",
 "r063-ell-gate-sol56-20260906.md":"5bc210cd3d20d00752d4bbde1dc7cc4d8139c4755c867bca2347f7844d1c28d0",
 "orbit-transport-gate-opus5-20260906.md":"571de68164ed5c8c1ba2a4a159a4c24f4f4c217d8530ec15712b1605c58c771a",
 "descent-partition-theorem-astra-20260906.md":"628c1b0939717b8e6046aac2fb501a401dd4b8739f9f18af5450f552b4bee2c2",
 "descend_own.py":"3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2",
 "roster.jsonl":"cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf",
 "moh1983_jram340_configurations_of_roots.pdf":"6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51",
 "FALLACY-v2.md":"e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5"}
CUSTODY = {}
for _b, _h in EXPECT.items():
    _g = hashlib.sha256(open(f"{MAN}/{_b}","rb").read()).hexdigest()
    assert _g == _h, (_b, _g)
    CUSTODY[_b] = "OK"

ROWS = {}
for _l in open(f"{MAN}/roster.jsonl"):
    if _l.strip():
        _d = json.loads(_l); ROWS[_d["row_id"]] = _d

def child(rid):
    oc = ROWS[rid]["own_child"]; s = oc["s_prime"]
    n, m, ell = oc["n_prime"], oc["m_prime"], oc["ell"]
    M = {i+1: oc["M_prime"][i] for i in range(s)}
    d = {i+1: oc["d_prime"][i] for i in range(s+1)}
    V = {i+2: oc["V_prime"][i] for i in range(len(oc["V_prime"]))}
    V[s+1] = d[s+1]
    dl = {i+1: F(oc["delta_prime"][i]) for i in range(s)}
    assert M[1] == -m
    return dict(rid=rid, s=s, n=n, m=m, ell=ell, H=1+ell, M=M, d=d,
                Vroster=V, delta_roster=dl)

def delta_of(C, i, Vsel):
    n, s, M, d, H = C["n"], C["s"], C["M"], C["d"], C["H"]
    num, den = F(n-M[i]), F(n-M[s]-1)
    for j in range(i+1, s+1):
        num *= (Vsel[j]*(n-M[j]) - d[j])
        den *= (Vsel[j]*(n-M[j-1]) - d[j])
    return H*(1 - num/den)

def P_of(C,i,Vin): return F(Vin*C["d"][i], C["d"][i+1])
def Q_of(C,i,Vin): return F(Vin*(C["n"]-C["M"][i]), C["d"][i+1])
def major(C,i,k):  return k*(C["n"]-C["M"][i]) > C["d"][i]
def rho(C,i,k):    return (F(C["m"]*k, C["d"][i]), F(C["n"]*k, C["d"][i]))
def term(C,rP,df): return F(C["n"], C["n"]+C["m"]) * rP * (C["H"] - df)
def minor_delta(C,i,k,di): return di + (C["H"]-di)*F(C["d"][i], k*(C["n"]-C["M"][i]))

def patterns(P, Q, A, forbid):
    """Galois-stable multiplicity multisets of p_i: mult z at pi=0 (orbit 1)
       plus orbits of size A.  #distinct roots <= Q ; no multiplicity == forbid."""
    P, Q = int(P), int(Q); out = []
    def rec(rem, slots, cur, acc):
        if rem == 0: acc.append(list(cur)); return
        lo = cur[-1] if cur else 1
        for k in range(lo, rem//A + 1):
            if k == forbid or slots < A: continue
            cur.append(k); rec(rem-k*A, slots-A, cur, acc); cur.pop()
    for z in range(0, P+1):
        if z == forbid: continue
        rem = P - z
        if rem % A: continue
        slots = Q - (1 if z > 0 else 0)
        if slots < 0: continue
        acc = []; rec(rem, slots, [], acc)
        for orbs in acc: out.append((z, tuple(orbs)))
    return out

def expand(C, i, Vin, L, Vsel, chain):
    """All admissible completions of disc D_i.  chain = remaining roster-selected
       multiplicities (chain[0] must occur at D_i) or () if off-tower.
       Returns list of dicts: IM, Im, shape, ok(residues)."""
    di = delta_of(C, i, Vsel)
    P, Q = P_of(C,i,Vin), Q_of(C,i,Vin)
    A = (L*di).denominator
    forbid = int(P//Q) if P % Q == 0 else None
    need = chain[0] if chain else None
    res = []
    for z, orbs in patterns(P, Q, A, forbid):
        facs = ([(z, True)] if z > 0 else []) + [(k, False) for k in orbs for _ in range(A)]
        ks = [k for k,_ in facs]
        if need is not None and need not in ks: continue
        # which factor carries the tower chain (only matters for its own subtree)
        carriers = [j for j,(k,_) in enumerate(facs) if k == need] if need is not None else [None]
        for car in carriers:
            per = []
            for j,(k, iszero) in enumerate(facs):
                sub_chain = chain[1:] if (car is not None and j == car) else ()
                per.append(child_options(C, i, k, (L if iszero else L*A), Vsel, di, sub_chain))
            if any(len(p) == 0 for p in per): continue
            for combo in product(*per):
                res.append(dict(
                    IM=sum(c["IM"] for c in combo), Im=sum(c["Im"] for c in combo),
                    ok=all(c["ok"] for c in combo),
                    shape=(z, orbs, tuple(c["shape"] for c in combo))))
    return res

def child_options(C, i, k, Lk, Vsel, di, chain):
    """One factor of multiplicity k at D_i."""
    if not major(C, i, k):
        if chain: return []                       # a minor cannot carry the tower
        df = minor_delta(C, i, k, di)
        assert df > C["H"]                        # control: minor <=> delta > 1+ell
        rP, rQ = rho(C, i, k)
        return [dict(IM=F(0), Im=(df - C["H"]), ok=True, shape=("minor", k))]
    V2 = dict(Vsel); V2[i] = k
    dnext = delta_of(C, i-1, V2)
    assert dnext < C["H"]                         # control: major <=> delta < 1+ell
    if i-1 >= 2:
        if len(chain) > 1 or (len(chain) == 1):
            return expand(C, i-1, k, Lk, V2, chain)
        return expand(C, i-1, k, Lk, V2, ())
    # i-1 == 1 : Prop 4.6 r=1 -> squarefree & coprime -> FINAL disc
    rP, rQ = rho(C, i, k)
    A1 = (Lk*dnext).denominator
    ok = (rP.denominator == 1 and rQ.denominator == 1
          and int(rP) % A1 in (0,1) and int(rQ) % A1 in (0,1))
    return [dict(IM=term(C, rP, dnext), Im=F(0), ok=ok,
                 shape=("final", k, str(dnext), A1, int(rP), int(rQ)))]

def analyse(rid):
    C = child(rid); s = C["s"]
    # control 1: Def 5.1(3) shifted reproduces the roster radii
    rad = {i: delta_of(C, i, C["Vroster"]) for i in range(1, s+1)}
    assert rad == C["delta_roster"], (rid, rad, C["delta_roster"])
    chain = tuple(C["Vroster"][i] for i in range(s, 1, -1))   # V_s, ..., V_2
    Vtop = {s+1: C["d"][s+1]}
    allc = expand(C, s, C["d"][s+1], 1, Vtop, chain)
    for c in allc: c["Im"] = c["Im"] + C["H"]   # I_m^ell = (1+ell) + sum(delta-1-ell)
    valid  = [c for c in allc if c["ok"]]
    intg   = [c for c in valid if c["IM"].denominator == 1]
    floors = [c for c in intg if c["IM"] >= c["Im"]]
    return C, rad, allc, valid, intg, floors

if __name__ == "__main__":
    out = {"custody": CUSTODY, "rows": {}}
    for rid in ["R025","R026","R027","R028","R057","R058","R063"]:
        C, rad, allc, valid, intg, floors = analyse(rid)
        sums_all   = sorted({str(c["IM"]) for c in allc})
        sums_valid = sorted({str(c["IM"]) for c in valid})
        sums_int   = sorted({str(c["IM"]) for c in floors})
        out["rows"][rid] = dict(
            n=C["n"], m=C["m"], ell=C["ell"], H=C["H"],
            M=[C["M"][i] for i in range(1,C["s"]+1)],
            d=[C["d"][i] for i in range(1,C["s"]+2)],
            V=[C["Vroster"][i] for i in range(2,C["s"]+1)],
            delta_recomputed={str(i): str(rad[i]) for i in rad},
            delta_roster={str(i): str(C["delta_roster"][i]) for i in C["delta_roster"]},
            n_configs=len(allc), n_galois_valid=len(valid),
            n_integral=len(intg), n_integral_above_floor=len(floors),
            distinct_sums_all=sums_all, distinct_sums_galois_valid=sums_valid,
            distinct_sums_surviving=sums_int)
        print(f"{rid}: configs={len(allc):4d} galois-valid={len(valid):4d} "
              f"integral={len(intg):3d} integral&floor={len(floors):3d}")
        print(f"      sums(all)   = {sums_all}")
        print(f"      sums(valid) = {sums_valid}")
        print(f"      sums(final) = {sums_int}")
    json.dump(out, open("box/six-rows-gate-20260906/gate.json","w"), indent=1)
