#!/usr/bin/env python3
"""Replay OPEN[SECOND-GEN-NUMERICS-DESCENT-INVARIANT] on the 1,420 operative rows.

Row source: box/child-own-v-20260905/enumerated-source-rows.json (the frozen
operative set).  Child data: live box/lib/descend_own.py (exact rationals).
Parent A_1^{act}: OwnVRouteTree witness bottom A1 (zero coefficient adds no
denominator).  Parent A_1^{moh}: Skel.A(1) = Moh p.201 (8).

Empty own-V is UNDEFINED, never a failure.  Set-valued own-V is checked on
every vector; none occur in this population.

Also replays controls.py (d) / second_gen (SD) window emptiness on the
(1)-(13) census at Kmin=2, 16<=n<=200.
"""
from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F
from math import lcm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/ubuntu/jc2"
sys.path.insert(0, os.path.join(ROOT, "box", "centre-gate-20260903"))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "box", "residual65-20260905"))
import moh_skeleton_full_frozen as B
from box.lib.descend_own import descend_own
from box.lib.own_v_routes import OwnVRouteTree
import second_gen as SG

ENUM = os.path.join(ROOT, "box", "child-own-v-20260905", "enumerated-source-rows.json")
OUT = HERE


def Q(x):
    return x if isinstance(x, F) else F(x)


def child_A1(delta, s):
    L = 1
    for i in range(2, s + 1):
        L = lcm(L, Q(delta[i]).denominator)
    return (L * Q(delta[1])).denominator


def extract_A1(node):
    """Bottom A1 from a nested OwnVRouteTree witness."""
    cur = node
    for _ in range(16):
        if not isinstance(cur, dict):
            return None
        if "A1" in cur and "j" not in cur:
            return int(cur["A1"])
        nxt = cur.get("selected_child")
        if nxt is None and "A1" in cur:
            return int(cur["A1"])
        cur = nxt
    return None


def row_key(n, m, Ms, V):
    return (int(n), int(m), tuple(int(x) for x in Ms),
            tuple(sorted((int(i), int(v)) for i, v in V.items())))


def ident_record():
    return dict(pass_=0, fail=0, undefined=0, fails=[])


def bump(rec, status, data=None):
    if status == "pass":
        rec["pass_"] += 1
    elif status == "fail":
        rec["fail"] += 1
        if data is not None:
            rec["fails"].append(data)
    else:
        rec["undefined"] += 1


def sd_window_census(op_keys):
    """controls.py (d): parent-side SD kill window on the (1)-(13) census."""
    t0 = time.time()
    sd_window = Counter()
    sd_rows = []
    census = 0
    op_hit = 0
    for n in range(16, 201):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            census += 1
            key = row_key(n, m, Ms, V)
            op = key in op_keys
            if op:
                op_hit += 1
            sk = B.Skel(n, m, list(Ms), V)
            s = sk.s
            ds = sk.d[s]
            vs = V[s]
            us = ds - vs
            if us == 1 and s >= 3:
                dprev = sk.d[s - 1]
                top_minus1 = (sk.M[s - 1] == n - ds * (ds - 1))
                ell2 = dprev // ds - ds
                lo_prev = F(dprev, n - sk.M[s - 1])
                simple_minor = (lo_prev >= 1)
                k = ("op" if op else "nonop",
                     "top-1" if top_minus1 else "top!=-1",
                     "ell2<0" if ell2 < 0 else ("ell2=0" if ell2 == 0 else "ell2>0"),
                     "simple-minor" if simple_minor else "simple-major")
                sd_window[k] += 1
                if top_minus1 and ell2 < 0 and simple_minor:
                    sd_rows.append(dict(n=n, m=m, Ms=list(Ms), V=dict(V),
                                        op=op, lo_prev=str(lo_prev), ell2=ell2))
    elapsed = time.time() - t0
    return dict(census=census, op_hit=op_hit, elapsed_s=elapsed,
                sd_window={"|".join(k): v for k, v in sorted(sd_window.items())},
                sd_kill_window_n=len(sd_rows), sd_kill_window_rows=sd_rows)


def analyse_row(src, D):
    n, m = src.n, src.m
    s, us, ds, ell = src.s, D["us"], D["ds"], D["ell"]
    empty = not D["V_vectors"]
    bucket = "EMPTY" if empty else "NONEMPTY"
    V2 = int(src.V[2])
    N = n * V2 // src.d[2]
    Mm = m * V2 // src.d[2]
    Np = D["n"] * V2 // D["d"][2]
    Mp = D["m"] * V2 // D["d"][2]
    A1moh = src.A(1)
    firsts = [c["first_nonzero"] for c in D["routes"]]
    first = firsts[0] if firsts else None
    A1act = None
    if D["routes"]:
        A1act = extract_A1(D["routes"][0].get("source_tree_witness"))
    se = D["s"]
    vecs = [tuple(int(x) for x in v) for v in D["V_vectors"]]
    out = dict(n=n, m=m, s=s, se=se, us=us, ds=ds, ell=ell,
               dropped=bool(D["dropped"]), route_state=D["route_state"],
               bucket=bucket, V_set_size=len(vecs), first_nonzero=first,
               M={i: int(src.M[i]) for i in range(1, s + 1)},
               V={i: int(src.V[i]) for i in range(2, s + 1)},
               d={i: int(src.d[i]) for i in range(1, s + 2)},
               n_prime=D["n"], m_prime=D["m"],
               N=N, N_prime=Np, Mbot=Mm, M_prime_bot=Mp,
               A1_moh=A1moh, A1_act=A1act)
    # --- N'=N, M'=M (scale + D1 identity V'_2 = V_2; defined on all rows) ---
    out["I_NM"] = dict(ok=(Np == N and Mp == Mm),
                       defined=True, us_clause=("us=1" if us == 1 else "us>=2"))
    # --- l'' = d_{s-1}/d_s - d_s at us=1, licensed (not dropped) ---
    if us == 1 and s >= 3:
        claimed = src.d[s - 1] // src.d[s] - src.d[s]
        dtop = int(D["d"][se])
        child_ell2 = dtop - 3 - ell
        ell_src = 2 * (ds - us) - ds - 1
        if D["dropped"]:
            out["I_ell"] = dict(ok=None, defined=False,
                                reason="unlicensed: PROP6.3_FINITE_POLE / n-1 tail dropped",
                                claimed=claimed, child_ell2=child_ell2, dtop=dtop)
        else:
            out["I_ell"] = dict(ok=(claimed == child_ell2 and ell == ell_src
                                    and dtop * ds == src.d[s - 1] * us),
                                defined=True, claimed=claimed, child_ell2=child_ell2,
                                dtop=dtop, ell_src=ell_src)
    else:
        out["I_ell"] = dict(ok=None, defined=False,
                            reason="identity stated at u_s=1 only")
    # --- A'_1 and P',Q' need own V / own radii ---
    if empty:
        out["I_A1_eq_act"] = dict(ok=None, defined=False, reason="empty own V")
        out["I_A1_div_moh"] = dict(ok=None, defined=False, reason="empty own V")
        out["I_PQ_copied"] = dict(ok=None, defined=False, reason="empty own V",
                                  n_levels=0)
        out["I_PQ_index"] = dict(ok=None, defined=False, reason="empty own V",
                                 n_levels=0)
        return out
    # own radii: child_radii is the retained-first subset of diagnostic_radii
    radii = D["child_radii"]
    if not radii:
        out["I_A1_eq_act"] = dict(ok=None, defined=False, reason="no own child radii")
        out["I_A1_div_moh"] = dict(ok=None, defined=False, reason="no own child radii")
        out["I_PQ_copied"] = dict(ok=None, defined=False, reason="no own child radii",
                                  n_levels=0)
        out["I_PQ_index"] = dict(ok=None, defined=False, reason="no own child radii",
                                 n_levels=0)
        return out
    A1c_set = []
    for rec in radii:
        dlp = {int(i): Q(v) for i, v in rec["delta"].items()}
        A1c_set.append(child_A1(dlp, se))
        # us=1 complete: replay Def 5.1(3) * (ell+1)
        if us == 1 and not D["dropped"]:
            vec = tuple(int(x) for x in rec["V"])
            Vp = {i + 2: vec[i] for i in range(len(vec))}
            Vp[se + 1] = int(D["d"][se + 1])
            formula = SG.def51_radii(D["n"], D["M"], D["d"], Vp, se, ell + 1)
            metric = {int(i): Q(v) for i, v in rec["delta"].items()}
            if formula != metric:
                out["radii_replay_fail"] = dict(formula={k: str(v) for k, v in formula.items()},
                                                metric={k: str(v) for k, v in metric.items()})
    A1c = A1c_set[0]
    out["A1_child"] = A1c
    out["A1_child_set"] = A1c_set
    # A'_1 = A_1^{act}  (stated for licensed descendants; at us>=2 the OPEN
    # also states the weaker A'_1 | A_1)
    if A1act is None:
        out["I_A1_eq_act"] = dict(ok=None, defined=False, reason="no tree witness A1")
    else:
        out["I_A1_eq_act"] = dict(ok=(A1c == A1act), defined=True,
                                  A1_child=A1c, A1_act=A1act, us=us)
    out["I_A1_div_moh"] = dict(ok=(A1moh % A1c == 0), defined=True,
                               A1_child=A1c, A1_moh=A1moh, us=us)
    # P'_j, Q'_j at common levels.
    # Copied common: V'_{j+1} = V_{j+1} (j+1 <= first_nonzero), j in 2..se-1.
    # Index overlap: every j in 2..se-1, including Wzero images.
    pq_copied_ok, pq_copied_n = True, 0
    pq_index_ok, pq_index_n = True, 0
    pq_wzero = []
    for vec in vecs:
        Vp = {i + 2: int(vec[i]) for i in range(len(vec))}
        for j in range(2, se):
            P = src.V[j + 1] * src.d[j] // src.d[j + 1]
            Qv = src.V[j + 1] * (n - src.M[j]) // src.d[j + 1]
            Pp = Vp[j + 1] * D["d"][j] // D["d"][j + 1]
            Qp = Vp[j + 1] * (D["n"] - D["M"][j]) // D["d"][j + 1]
            copied = first is not None and (j + 1) <= first
            pq_index_n += 1
            if (P, Qv) != (Pp, Qp):
                pq_index_ok = False
            if copied:
                pq_copied_n += 1
                if (P, Qv) != (Pp, Qp):
                    pq_copied_ok = False
            else:
                if (P, Qv) != (Pp, Qp):
                    pq_wzero.append(dict(j=j, P=P, Q=Qv, P_prime=Pp, Q_prime=Qp,
                                         Vjp=int(src.V[j + 1]), Vpjp=int(Vp[j + 1])))
    out["I_PQ_copied"] = dict(ok=pq_copied_ok, defined=True, n_levels=pq_copied_n,
                              vacuous=(pq_copied_n == 0))
    out["I_PQ_index"] = dict(ok=pq_index_ok, defined=True, n_levels=pq_index_n,
                             vacuous=(pq_index_n == 0), wzero_mismatch=pq_wzero)
    return out


def main():
    t0 = time.time()
    W = sys.stdout.write
    enum = json.loads(open(ENUM).read())
    assert enum["operative_count"] == 1420 and enum["census_count"] == 24063
    rows = enum["rows"]
    assert len(rows) == 1420
    op_keys = {row_key(r["n"], r["m"], r["Ms"], r["V"]) for r in rows}
    assert len(op_keys) == 1420

    W("=== (1) identity replay on 1,420 operative rows, live descend_own ===\n")
    t1 = time.time()
    I = {name: ident_record() for name in
         ("NM_all", "NM_us1", "NM_usge2",
          "A1_eq_act_us1", "A1_eq_act_usge2",
          "A1_div_moh_us1", "A1_div_moh_usge2",
          "PQ_copied", "PQ_index",
          "ell_us1_licensed")}
    I_empty = {name: ident_record() for name in I}
    I_nonempty = {name: ident_record() for name in I}
    states = Counter()
    Vsize = Counter()
    us_c = Counter()
    observations = dict(wzero_PQ=[], A1_eq_act_fail=[], A1_div_fail=[],
                        NM_fail=[], ell_fail=[], radii_replay_fail=[],
                        A1_usge2_neq_act=[])
    analysed = []
    for r in rows:
        V = {int(k): int(v) for k, v in r["V"].items()}
        sk = B.Skel(r["n"], r["m"], r["Ms"], V)
        D = descend_own(sk)
        states[D["route_state"]] += 1
        Vsize[len(D["V_vectors"])] += 1
        us_c[D["us"]] += 1
        a = analyse_row(sk, D)
        analysed.append(a)
        empty = a["bucket"] == "EMPTY"
        bank = I_empty if empty else I_nonempty

        def take(name, status, data=None):
            bump(I[name], status, data)
            bump(bank[name], status, data)

        # N', M'
        st = "pass" if a["I_NM"]["ok"] else "fail"
        data = a if st == "fail" else None
        take("NM_all", st, data)
        take("NM_us1" if a["us"] == 1 else "NM_usge2", st, data)
        if st == "fail":
            observations["NM_fail"].append(a)
        # A1
        eq = a["I_A1_eq_act"]
        if not eq["defined"]:
            take("A1_eq_act_us1" if a["us"] == 1 else "A1_eq_act_usge2", "undef")
        else:
            st = "pass" if eq["ok"] else "fail"
            take("A1_eq_act_us1" if a["us"] == 1 else "A1_eq_act_usge2", st,
                 a if st == "fail" else None)
            payload = dict(n=a["n"], m=a["m"], us=a["us"], A1_child=a.get("A1_child"),
                           A1_act=a["A1_act"], A1_moh=a["A1_moh"],
                           first=a["first_nonzero"], V=a["V"],
                           route=a["route_state"])
            if st == "fail" and a["us"] == 1:
                observations["A1_eq_act_fail"].append(payload)
            elif a["us"] >= 2 and a.get("A1_child") != a["A1_act"]:
                observations["A1_usge2_neq_act"].append(payload)
        div = a["I_A1_div_moh"]
        if not div["defined"]:
            take("A1_div_moh_us1" if a["us"] == 1 else "A1_div_moh_usge2", "undef")
        else:
            st = "pass" if div["ok"] else "fail"
            take("A1_div_moh_us1" if a["us"] == 1 else "A1_div_moh_usge2", st,
                 a if st == "fail" else None)
            if st == "fail":
                observations["A1_div_fail"].append(dict(
                    n=a["n"], m=a["m"], us=a["us"], A1_child=a.get("A1_child"),
                    A1_moh=a["A1_moh"], A1_act=a["A1_act"]))
        # P/Q
        for which, key in (("I_PQ_copied", "PQ_copied"), ("I_PQ_index", "PQ_index")):
            rec = a[which]
            if not rec["defined"]:
                take(key, "undef")
            else:
                st = "pass" if rec["ok"] else "fail"
                take(key, st, a if st == "fail" else None)
        if a["I_PQ_index"].get("wzero_mismatch"):
            observations["wzero_PQ"].append(dict(
                n=a["n"], m=a["m"], us=a["us"], s=a["s"], se=a["se"],
                first=a["first_nonzero"], V=a["V"],
                mismatch=a["I_PQ_index"]["wzero_mismatch"]))
        # l''
        ellr = a["I_ell"]
        if not ellr["defined"]:
            take("ell_us1_licensed", "undef")
        else:
            st = "pass" if ellr["ok"] else "fail"
            take("ell_us1_licensed", st, a if st == "fail" else None)
            if st == "fail":
                observations["ell_fail"].append(dict(
                    n=a["n"], m=a["m"], claimed=ellr.get("claimed"),
                    child=ellr.get("child_ell2"), dropped=a["dropped"]))
        if a.get("radii_replay_fail"):
            observations["radii_replay_fail"].append(dict(n=a["n"], m=a["m"],
                                                          **a["radii_replay_fail"]))

    t_id = time.time() - t1
    W("   descend_own route states: %s\n" % dict(states))
    W("   V_set_size: %s   us: %s\n" % (dict(Vsize), dict(us_c)))
    W("   elapsed identity pass: %.2fs\n" % t_id)

    def show(title, recs, which):
        W("   %s\n" % title)
        for name in recs:
            r = recs[name]
            W("      %-22s pass=%d fail=%d undefined=%d\n" %
              (name, r["pass_"], r["fail"], r["undefined"]))

    show("ALL 1,420", I, "all")
    show("NONEMPTY  (own V nonempty)", I_nonempty, "ne")
    show("EMPTY     (own V empty; not a failure)", I_empty, "e")
    W("   Wzero-image P'/Q' index-overlap (not copied-common): %d rows\n" %
      len(observations["wzero_PQ"]))
    for x in observations["wzero_PQ"]:
        W("      %s\n" % (x,))
    W("   A'_1 = A_1^{act} failures: %d\n" % len(observations["A1_eq_act_fail"]))
    for x in observations["A1_eq_act_fail"]:
        W("      %s\n" % (x,))
    W("   A'_1 | A_1^{moh} failures: %d\n" % len(observations["A1_div_fail"]))
    W("   N'/M' failures: %d   l'' failures: %d   radii replay fail: %d\n" %
      (len(observations["NM_fail"]), len(observations["ell_fail"]),
       len(observations["radii_replay_fail"])))

    W("\n=== (3) SD window emptiness on the (1)-(13) census ===\n")
    t2 = time.time()
    sd = sd_window_census(op_keys)
    W("   census=%d op_hit=%d (expect 24063 / 1420)  [%.1fs]\n" %
      (sd["census"], sd["op_hit"], sd["elapsed_s"]))
    for k, v in sd["sd_window"].items():
        W("   %-45s %d\n" % (k, v))
    W("   rows in the SD kill window (top=-1, l''<0, simple point minor): %d\n" %
      sd["sd_kill_window_n"])
    assert sd["census"] == 24063, sd["census"]
    assert sd["op_hit"] == 1420, sd["op_hit"]

    # headline
    defined_fail_total = sum(I[k]["fail"] for k in
                             ("NM_us1", "A1_eq_act_us1", "A1_div_moh_usge2",
                              "PQ_copied", "ell_us1_licensed"))
    W("\n=== HEADLINE ===\n")
    W("   defined-fail on OPEN identities (NM@us1, A1=act@us1, A1|A@us>=2, "
      "PQ_copied, ell licensed): %d\n" % defined_fail_total)
    W("   PQ_index (every overlapping j, including Wzero images) fail: %d\n" %
      I["PQ_index"]["fail"])
    W("   A1_eq_act_usge2 fail (OPEN states only A'|A at us>=2): %d\n" %
      I["A1_eq_act_usge2"]["fail"])
    verdict = "HOLD" if defined_fail_total == 0 else "FAIL"
    W("   VERDICT %s\n" % verdict)
    W("   total %.1fs\n" % (time.time() - t0))

    def slim(rec):
        return {k: dict(pass_=v["pass_"], fail=v["fail"], undefined=v["undefined"],
                        n_fail_listed=len(v["fails"]))
                for k, v in rec.items()}

    payload = dict(
        schema="jc2.descent-invariance-replay/v1",
        enumerator=dict(path=ENUM, operative_count=enum["operative_count"],
                        census_count=enum["census_count"],
                        enumerator_sha256=enum.get("enumerator_sha256")),
        route_states=dict(states),
        V_set_size=dict(Vsize),
        us=dict(us_c),
        identities_all=slim(I),
        identities_nonempty=slim(I_nonempty),
        identities_empty=slim(I_empty),
        observations=observations,
        sd=sd,
        defined_fail_total=defined_fail_total,
        verdict=verdict,
        elapsed_s=time.time() - t0,
    )
    json.dump(payload, open(os.path.join(OUT, "replay.json"), "w"),
              indent=1, default=str)
    W("wrote %s/replay.json\n" % OUT)


if __name__ == "__main__":
    main()
