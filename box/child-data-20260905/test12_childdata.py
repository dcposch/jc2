#!/usr/bin/env python3
"""TEST 1 (UNEG-SHAPE-LICENCE) + TEST 2 (CHILD-TOP-CONVENTION): mechanical part.

Arithmetic on PRINTED definitions only, cited inline:

  p.150  characteristic data {M_j,d_j} of a pair (f,g) w.r.t. x:
           d_1 = n,  d_{j+1} = g.c.d.(n, M_1, ..., M_j),
           M_j = min{ i : f_i(x) != 0, d_j /| i },   M_{h+1} = infinity.
         Consequence used below: since d_j = 1 makes {i : d_j /| i} EMPTY, the
         chain terminates at exactly the first h with d_{h+1} = 1, and nowhere
         else.  M_1 = -m.
  p.179  Def 5.1(1): in D_i the polynomials g(y) have precisely (n/d_{i+1})V_{i+1}
         roots;  T_j^psi(y) has precisely (-mu_j/d_{i+1})V_{i+1} roots.
         Def 5.1(2): V_{i+1} d_i/d_{i+1} >= V_i > d_i/(n-M_i),  V_{s+1}=d_{s+1}.
         Def 5.1(3): the delta_i formula.
  p.197  Prop 6.3(2): gbar(sigma) is monic in pi with pi-degree u_s*n/d_s.
  p.198  the inversion x=(1/b)[theta^-1+...], y=theta^-1, z=y-bx-e, and
         deg gbar_sigma(pi) = u_s n/d_s.
"""
import json
from fractions import Fraction as F
from math import gcd

SRC = "/home/ubuntu/jc2/box/scopeleaks-20260905/scope_enum.json"
OUT = "/home/ubuntu/jc2/box/child-data-20260905/test12-childdata.json"
ROWS = json.load(open(SRC))["operative_rows"]


def chain(n, Mlist):
    """p.150: d_1=n, d_{j+1}=gcd(n,M_1..M_j).  Mlist = [M_1, M_2, ...]."""
    d, g = [n], n
    for M in Mlist:
        g = gcd(g, abs(int(M)))
        d.append(g)
    return d                       # d[0]=d_1, d[1]=d_2, ...


def parent_M(r):
    return [-r["m"]] + list(r["Ms"])            # M_1 = -m, then M_2..M_s


def child_M(r):
    return [-r["m1"]] + [int(F(x)) for x in r["Mp"]]   # M'_1 = -m', M'_2..M'_{s'}


out = {"schema": "jc2.child-data.test12/v1", "source": SRC, "n_operative": len(ROWS)}

# ============================ TEST 2 =========================================
# (a) the closed form  d'_{s'+1} = gcd(n', M'_1..M'_{s'}) = (u_s/d_s)*d_s = u_s
bad, closes, open_chain = [], 0, 0
for r in ROWS:
    dch = chain(r["n1"], child_M(r))
    dtop = dch[-1]                                   # = d'_{s'+1}
    if dtop != r["u_s"]:
        bad.append({"n": r["n"], "m": r["m"], "Ms": r["Ms"], "d_top": dtop, "u_s": r["u_s"]})
    if dtop == 1:
        closes += 1
    else:
        open_chain += 1
out["T2_closed_form"] = {
    "claim": "d'_{s'+1} = gcd(n', M'_1..M'_{s'}) = u_s   [p.150 chain on the descended M']",
    "violations": bad, "holds_on": len(ROWS) - len(bad),
    "child_chain_reaches_1_at_level_s'+1": closes,
    "child_chain_still_>1_at_level_s'+1": open_chain}

# (b) cross-tab against u_s
by_us = {}
for r in ROWS:
    by_us.setdefault(r["u_s"], [0, 0])
    by_us[r["u_s"]][0 if chain(r["n1"], child_M(r))[-1] == 1 else 1] += 1
out["T2_by_u_s"] = {str(k): {"closes(d'=1)": v[0], "stays_open(d'>1)": v[1]}
                    for k, v in sorted(by_us.items())}

# (c) the named instance, in full
inst = [r for r in ROWS if r["n"] == 96 and r["m"] == 72
        and list(r["Ms"]) == [36, 78, 94]]
inst_rec = []
for r in inst:
    pM, cM = parent_M(r), child_M(r)
    pd, cd = chain(r["n"], pM), chain(r["n1"], cM)
    # would a further child level at n'-2 or the p.174 terminal n'-1 be legal?
    nxt2 = gcd(cd[-1], abs(r["n1"] - 2))
    nxt1 = gcd(cd[-1], abs(r["n1"] - 1))
    inst_rec.append({
        "parent": {"n": r["n"], "m": r["m"], "M_1..M_s": pM, "V": r["V"], "s": r["s"],
                   "d_1..d_{s+1}": pd,
                   "note": "d_{s+1}=%d>1 so the PARENT chain also continues; the p.174 "
                           "terminal level is M=n-1=%d, and gcd(d_{s+1},n-1)=%d=1 closes it"
                           % (pd[-1], r["n"] - 1, gcd(pd[-1], r["n"] - 1))},
        "child": {"n'": r["n1"], "m'": r["m1"], "M'_1..M'_{s'}": cM, "s'": r["sp"],
                  "d'_1..d'_{s'+1}": cd, "d'_{s'+1}": cd[-1], "u_s": r["u_s"],
                  "M'_{s'+1} by p.150": ("infinity (d'_{s'+1}=1: the set {i : d /| i} is empty)"
                                         if cd[-1] == 1 else "finite: chain not closed"),
                  "could_continue_to_n'-2=%d" % (r["n1"] - 2):
                      ("NO - d'_{s'+1}=1 forbids any further level" if cd[-1] == 1
                       else "possible, gcd->%d" % nxt2),
                  "p174_terminal_n'-1=%d" % (r["n1"] - 1):
                      ("not needed" if cd[-1] == 1 else "gcd->%d" % nxt1)},
        "V'_{s'} vs d'_{s'}": {"V'_s'": r["Vp"][-1], "d'_s'": cd[-2],
                               "CTOP_holds": r["Vp"][-1] <= cd[-2]},
        "ell": r["ell"], "delta'_{s'}_is_-1":
            (int(F(r["Mp"][-1])) == r["n1"] - r["ell"] - 2)})
out["T2_named_instance_96_72"] = inst_rec

# (d) Moh's own six p.202 rows, descended on p.207 -- printed cross-check
MOH = [  # (n, m, [M_2..M_s], V dict)   p.202 table, as banked in CONTROL P
    (64, 48, [52, 62], {2: 3, 3: 3}),
    (84, 56, [64, 82], {2: 2, 3: 3}),
    (84, 56, [72, 82], {2: 5, 3: 3}),
    (75, 50, [55, 73], {2: 3, 3: 4}),
    (75, 50, [55, 73], {2: 2, 3: 4}),
    (99, 66, [77, 97], {2: 8, 3: 8}),
]
PRINTED_207 = {  # (n',m'); M'_2; V'_2   as printed by Moh on p.207
    (64, 48, 3): ((16, 12), 13, 3),
    (84, 56, 2): ((21, 14), 16, 2),
    (84, 56, 5): ((21, 14), 18, 5),
    (75, 50, 3): ((15, 10), 11, 3),
    (75, 50, 2): ((15, 10), 11, 2),
}
moh_rec = []
for (n, m, Ms, V) in MOH:
    s = len(Ms) + 1
    ds = chain(n, [-m] + Ms)[-1]           # d_{s+1}
    # tower gcds: d_1..d_{s+1}; d_s is the one at index s-1
    dch = chain(n, [-m] + Ms)
    d_s = dch[s - 1]
    us, vs = d_s - V[s], V[s]
    n1, m1 = n * us // d_s, m * us // d_s
    cM = [-m1] + [M * us // d_s for M in Ms[:-1]]
    cd = chain(n1, cM)
    key = (n, m, V[2])
    pr = PRINTED_207.get(key)
    moh_rec.append({"parent": {"n": n, "m": m, "M": [-m] + Ms, "V": V, "s": s,
                               "d_1..d_{s+1}": dch, "d_s": d_s, "u_s": us, "v_s": vs},
                    "child": {"n'": n1, "m'": m1, "M'": cM, "d'": cd,
                              "d'_{s'+1}": cd[-1], "closes": cd[-1] == 1},
                    "moh_p207_printed": pr,
                    "matches_p207": (pr is not None
                                     and pr[0] == (n1, m1) and pr[1] == cM[1] and pr[2] == V[2]),
                    "skipped_by_moh": pr is None})
out["T2_moh_p207_crosscheck"] = moh_rec

# ============================ TEST 1 =========================================
# Def 5.1(1) at i=1 -- root counts.  Parent: (n/d_2)V_2 roots of g in D_1.
# Child : (n'/d'_2)V'_2 roots of g' in D'_1, and g' has exactly n' roots (p.197 (2)).
uneg = [r for r in ROWS if r["up"] < 0]
t1 = []
for r in uneg:
    par_D1 = F(r["n"], r["d2"]) * r["V2p"]
    ch_D1 = F(r["n1"], r["d2p"]) * r["V2p"]
    t1.append({"n": r["n"], "m": r["m"], "Ms": r["Ms"], "V": r["V"], "u_s": r["u_s"],
               "n'": r["n1"], "m'": r["m1"], "K'=d'_2": r["d2p"], "V'_2": r["V2p"],
               "u'": r["up"], "ell": r["ell"], "s'": r["sp"],
               "roots_of_g_in_D1": str(par_D1), "roots_of_g'_in_D1'": str(ch_D1),
               "counts_equal": par_D1 == ch_D1,
               "child_total_roots_n'": r["n1"],
               "Def51_1_violated": ch_D1 > r["n1"]})
out["T1_uneg_root_counts"] = {"rows": len(t1), "all_counts_preserved":
                              all(x["counts_equal"] for x in t1),
                              "all_violate_Def51_1": all(x["Def51_1_violated"] for x in t1),
                              "sample": t1[:6], "all": t1}

# control: the same count on the NON-U-NEGATIVE operative rows must be legal
nonneg = [r for r in ROWS if r["up"] >= 0]
viol = [r for r in nonneg if F(r["n1"], r["d2p"]) * r["V2p"] > r["n1"]]
out["T1_control_nonuneg"] = {"rows": len(nonneg), "Def51_1_violations": len(viol),
                             "pass": len(viol) == 0}

# control: Moh's own five descended rows
mohc = []
for rec in moh_rec:
    if rec["skipped_by_moh"]:
        continue
    n1, m1 = rec["child"]["n'"], rec["child"]["m'"]
    V2 = rec["parent"]["V"][2]
    d2p = gcd(n1, m1)
    mohc.append({"child": (n1, m1), "V'_2": V2, "K'": d2p,
                 "roots_in_D1'": str(F(n1, d2p) * V2), "n'": n1,
                 "legal": F(n1, d2p) * V2 <= n1})
out["T1_control_moh5"] = {"all_legal": all(c["legal"] for c in mohc), "rows": mohc}

# h-support envelope: can it ever be negative?   d = -delta'_{s'} > 0
out["T1_hsupport"] = {
    "theorem": "deg_x [y^a] h' <= floor(d*(K'-a)), d = -delta_s > 0  (frozen h-support gate)",
    "note": "floor(d*(K'-a)) >= 0 for every 0<=a<K', so the envelope G_1 is NEVER empty; "
            "it cannot produce the shape.py U-NEGATIVE early return and cannot supply the licence.",
    "shape_py_mechanism": "shape.py:141-147 returns U-NEGATIVE when u<0 or degx_h<0, where "
                          "degx_h = u*K//d2 uses the OLD cap deg_x h = u' = K'-V'_2, which the "
                          "frozen h-support gate rejects as 'not justified by D1'."}

json.dump(out, open(OUT, "w"), indent=1, sort_keys=False, default=str)

print("=== TEST 2 ===")
print("d'_{s'+1} = u_s  holds on %d/%d operative rows; violations: %d"
      % (out["T2_closed_form"]["holds_on"], len(ROWS), len(out["T2_closed_form"]["violations"])))
print("child chain closes (d'=1) :", out["T2_closed_form"]["child_chain_reaches_1_at_level_s'+1"])
print("child chain stays open    :", out["T2_closed_form"]["child_chain_still_>1_at_level_s'+1"])
print("by u_s:", json.dumps(out["T2_by_u_s"]))
print("\nnamed instance (96,72):")
print(json.dumps(inst_rec, indent=1, default=str))
print("\nMoh p.207 cross-check:")
for r in moh_rec:
    print("  parent", r["parent"]["n"], r["parent"]["m"], r["parent"]["V"],
          "u_s=%d" % r["parent"]["u_s"], "-> child", r["child"]["n'"], r["child"]["m'"],
          "M'=%s d'=%s closes=%s" % (r["child"]["M'"], r["child"]["d'"], r["child"]["closes"]),
          "| p207", r["moh_p207_printed"], "match", r["matches_p207"])
print("\n=== TEST 1 ===")
print("U-NEG rows:", out["T1_uneg_root_counts"]["rows"],
      "counts preserved:", out["T1_uneg_root_counts"]["all_counts_preserved"],
      "all violate Def5.1(1):", out["T1_uneg_root_counts"]["all_violate_Def51_1"])
print("control non-U-NEG:", out["T1_control_nonuneg"])
print("control Moh 5:", out["T1_control_moh5"]["all_legal"])
for x in t1[:3]:
    print("  ", x["n"], x["m"], x["Ms"], "V'_2=%d K'=%d" % (x["V'_2"], x["K'=d'_2"]),
          "roots of g in D_1 =", x["roots_of_g_in_D1"],
          "| roots of g' in D'_1 =", x["roots_of_g'_in_D1'"],
          "> n' =", x["child_total_roots_n'"])
