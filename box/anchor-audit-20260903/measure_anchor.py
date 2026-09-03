#!/usr/bin/env python3
"""DESCENT-ANCHOR AUDIT — desk measurement.

Frozen copies: repro/moh_skeleton_full.py, full_tree_partition.py, phi_delta.py.
Reproduces Opus 38/57 (n<=100) and 12/20 (n=108); lists every anchor-zero row;
checks p.207 non-degeneracy; negative control (drop the Def 5.1(3) factor);
repaired rule (drop M_h = n'-1, Moh p.174 Definition-Remark).
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "repro"))

import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as T  # noqa: E402


def def51(n, M, d, V, s, i):
    """Def 5.1(3) p.179 as printed, 1-based M,d,V dicts. M[s] is last effective."""
    num = F(n - M[i])
    den = F(n - M[s] - 1)
    if den == 0:
        return None  # undefined
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den *= V[j] * (n - M[j - 1]) - d[j]
        if den == 0:
            return None
    return 1 - num / den


def def51_drop_factor(n, M, d, V, s, i):
    """Negative control: omit 1/(n-M_s-1), i.e. replace that factor by 1."""
    num = F(n - M[i])
    den = F(1)
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den *= V[j] * (n - M[j - 1]) - d[j]
    return 1 - num / den


def u_s_of(S):
    return S.d[S.s] - S.V[S.s]


def descend(S):
    """Prop 6.3 map as used by the charged lanes (u_s = 1 required)."""
    us = u_s_of(S)
    ds = S.d[S.s]
    Vs = S.V[S.s]
    k = Vs - us - 1  # = V_s - 2 when u_s = 1
    n2, m2 = S.n // ds, S.m // ds
    s2 = S.s - 1
    M2 = {i: S.M[i] // ds for i in range(1, s2 + 1)}
    d2 = {i: S.d[i] // ds for i in range(1, s2 + 2)}
    V2 = {i: S.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return {
        "n": n2, "m": m2, "s": s2, "M": M2, "d": d2, "V": V2,
        "k": k, "u_s": us, "d_s": ds, "V_s": Vs,
    }


def truncate_jacobian(D):
    """Moh p.174 Definition-Remark: drop M_h if M_h = n-1."""
    n, s, M, d, V = D["n"], D["s"], dict(D["M"]), dict(D["d"]), dict(D["V"])
    dropped = 0
    while s >= 1 and M.get(s) == n - 1:
        dropped += 1
        s -= 1
        M.pop(s + 1, None)
        V.pop(s + 1, None)
        if (s + 1) in d and s >= 1:
            V[s + 1] = d[s + 1]
    D2 = dict(D)
    D2.update({"s": s, "M": M, "d": d, "V": V, "dropped": dropped})
    return D2


def anchor_den(D):
    """n - M_s - 1 on the (possibly untruncated) descended tuple."""
    if D["s"] < 1 or D["s"] not in D["M"]:
        return None
    return D["n"] - D["M"][D["s"]] - 1


def phi_on(D):
    """(k+1) * Def 5.1(3) at every i=1..s. None if undefined."""
    n, M, d, V, s, k = D["n"], D["M"], D["d"], D["V"], D["s"], D["k"]
    if s < 1:
        return None
    if n - M[s] - 1 == 0:
        return None
    out = []
    for i in range(1, s + 1):
        raw = def51(n, M, d, V, s, i)
        if raw is None:
            return None
        out.append((k + 1) * raw)
    return out


def skel_tuple(S):
    Ms = [S.M[i] for i in range(2, S.s + 1)]
    Vs = {i: S.V[i] for i in range(2, S.s + 1)}
    return S.n, S.m, tuple(Ms), tuple(sorted(Vs.items()))


def collect_rows(nmax=100, nmin=4, only_n=None):
    if only_n is not None:
        ns = [only_n]
    else:
        ns = list(range(nmin, nmax + 1))
    rows = []
    for n in ns:
        for m, Ms, V in M.census(n, Kmin=2, full=True):
            rows.append(M.Skel(n, m, list(Ms), V))
    return rows


def screen_ode(rows):
    surv = []
    for S in rows:
        if T.full_tree_ode_ok(S):
            surv.append(S)
    return surv


# ---------------------------------------------------------------------------
print("=" * 78)
print("ANCHOR-AUDIT measurement  (frozen moh_skeleton_full + full_tree_partition)")
print("=" * 78)

# ---- A. Def 5.1(3) factor and the 10 printed rationals --------------------
print("\n== A. Def 5.1(3) as coded vs p.207 Φ; negative control ==")
from phi_delta import rows as PHI_ROWS, def51 as phi_def51  # charged copy

# reconstruct the charged 10/10
ok10 = True
for n, m, M2, V2, k, pd2, pd1, lab in PHI_ROWS:
    d2 = gcd(n, m)
    Md = {1: -m, 2: M2}
    dd = {1: n, 2: d2, 3: gcd(d2, M2)}
    Vd = {2: V2, 3: dd[3]}
    raw2, raw1 = def51(n, Md, dd, Vd, 2, 2), def51(n, Md, dd, Vd, 2, 1)
    p2, p1 = (k + 1) * raw2, (k + 1) * raw1
    match = (p2 == pd2 and p1 == pd1)
    ok10 = ok10 and match
    drop2 = def51_drop_factor(n, Md, dd, Vd, 2, 2)
    print("  %-44s Phi=(%s, %s) printed=(%s, %s) %s  drop-factor δ2=%s"
          % (lab, p2, p1, pd2, pd1, "MATCH" if match else "FAIL", drop2))
print("  10/10 MATCH:", ok10)

# the charged negative control: (15,10) drop-factor gives -3 not -1/3
n, m, M2, V2 = 15, 10, 11, 3
d2 = gcd(n, m)
Md = {1: -m, 2: M2}
dd = {1: n, 2: d2, 3: gcd(d2, M2)}
Vd = {2: V2, 3: dd[3]}
raw2 = def51(n, Md, dd, Vd, 2, 2)
drop2 = def51_drop_factor(n, Md, dd, Vd, 2, 2)
print("  (15,10) V2=3  Def51 δ2 = %s  (expect -1/3);  drop-factor δ2 = %s  (expect -3)"
      % (raw2, drop2))
print("  drop-factor BREAKS the match:", drop2 != raw2 and drop2 == F(-3) and raw2 == F(-1, 3))

# repaired Φ is a no-op on p.207 (no M_s' = n'-1)
print("\n== A2. repaired Φ (drop M_h=n'-1) is a no-op on all five p.207 rows ==")
p207_parents = [
    (64, 48, [52, 62], {3: 3, 2: 3}, " (64,48)"),
    (84, 56, [64, 82], {3: 3, 2: 2}, " (84,56) M2=64,V2=2"),
    (84, 56, [72, 82], {3: 3, 2: 5}, " (84,56) M2=72,V2=5"),
    (75, 50, [55, 73], {3: 4, 2: 3}, " (75,50) V2=3"),
    (75, 50, [55, 73], {3: 4, 2: 2}, " (75,50) V2=2"),
]
print("  %-32s u_s d_s  n' m'  M'                 Ms_raw  n'-1  n'-2  den  dropped  Phi"
      % "parent")
for n, m, Ms, Vs, lab in p207_parents:
    S = M.Skel(n, m, Ms, Vs)
    D = descend(S)
    Dt = truncate_jacobian(D)
    den = anchor_den(D)
    den_t = anchor_den(Dt)
    Ms_raw = [D["M"][i] for i in range(2, D["s"] + 1)]
    print("  %-32s %3d %3d  %2d %2d  %-18s %5s  %4d  %4d  %3s  drop=%d  Φ=%s  Φt=%s"
          % (lab, D["u_s"], D["d_s"], D["n"], D["m"], Ms_raw,
             D["M"][D["s"]], D["n"] - 1, D["n"] - 2, den, Dt["dropped"],
             phi_on(D), phi_on(Dt)))

# ---- B. (84,56) census vs p.202 ------------------------------------------
print("\n== B. all (1)-(13) rows at (n,m)=(84,56) vs p.202 ==")
rows8456 = []
for m, Ms, V in M.census(84, Kmin=2, full=True):
    if m == 56:
        S = M.Skel(84, m, list(Ms), V)
        rows8456.append(S)
        us = u_s_of(S)
        ds = S.d[S.s]
        Ms_l = [S.M[i] for i in range(1, S.s + 1)]
        print("    s=%d  M=%s  V=%s  d=%s  d_s=%d u_s=%d  M_{s-1}=%s  n-d_s=%s  anchor0=%s"
              % (S.s, Ms_l, {i: S.V[i] for i in range(2, S.s + 1)},
                 [S.d[i] for i in range(1, S.s + 2)],
                 ds, us, S.M[S.s - 1], 84 - ds,
                 S.M[S.s - 1] == 84 - ds))
print("  count (84,56) (1)-(13) rows:", len(rows8456))
printed_8456 = {
    (84, 56, (64, 82), ((2, 2), (3, 3))),
    (84, 56, (72, 82), ((2, 5), (3, 3))),
}
got_8456 = {skel_tuple(S) for S in rows8456}
print("  p.202 two rows present:", printed_8456 <= got_8456)
print("  extra (84,56) rows beyond p.202:", len(got_8456 - printed_8456))

# hypothetical d_s=7 rows named by Opus
print("\n== B2. Opus-named d_s=7 (84,56) skeletons (may or may not be (1)-(13)) ==")
hyp = [
    (84, 56, [-56, 42, 77, 82]),
    (84, 56, [-56, 70, 77, 82]),
]
for n, m, fullM in hyp:
    Ms = fullM[1:]  # M_2..M_s
    # try every V that census would admit at this M
    found = [(S.V, u_s_of(S), S.d[S.s]) for S in rows8456
             if [S.M[i] for i in range(1, S.s + 1)] == fullM]
    print("  M=%s  in (1)-(13) with V's: %s" % (fullM, found if found else "NONE"))
    # also list (1)-(7) V-assignments (no (8)-(13) prune)
    v17 = []
    for mm, Mss, V in M.census(n, Kmin=2, full=False):
        if mm == m and list(Mss) == Ms:
            S = M.Skel(n, m, list(Mss), V)
            v17.append(({i: S.V[i] for i in range(2, S.s + 1)}, u_s_of(S), S.d[S.s],
                        S.M[S.s - 1] == n - S.d[S.s]))
    print("    (1)-(7) V-assignments: %s" % (v17 if v17 else "NONE"))

# ---- C. n<=100 C_FULL_TREE_ODE screen + descent/anchor --------------------
print("\n== C. n<=100 C_FULL_TREE_ODE + descent/anchor (reproduce 38/57) ==")
rows100 = collect_rows(100)
print("  (1)-(13) rows n<=100:", len(rows100))
surv100 = screen_ode(rows100)
print("  C_FULL_TREE_ODE survivors:", len(surv100))

desc, us_gt1, az, az_after_drop, evalable = [], [], [], [], []
records = []
for S in surv100:
    us = u_s_of(S)
    rec = {
        "n": S.n, "m": S.m,
        "M": [S.M[i] for i in range(1, S.s + 1)],
        "V": {i: S.V[i] for i in range(2, S.s + 1)},
        "d": [S.d[i] for i in range(1, S.s + 2)],
        "s": S.s, "d_s": S.d[S.s], "u_s": us, "V_s": S.V[S.s],
    }
    if us != 1:
        rec["status"] = "US-GT-1"
        us_gt1.append(rec)
        records.append(rec)
        continue
    D = descend(S)
    den = anchor_den(D)
    Dt = truncate_jacobian(D)
    den_t = anchor_den(Dt)
    rec.update({
        "n_prime": D["n"], "m_prime": D["m"], "k": D["k"],
        "M_prime": [D["M"][i] for i in range(1, D["s"] + 1)],
        "s_prime": D["s"],
        "den": den,
        "dropped": Dt["dropped"],
        "s_eff": Dt["s"],
        "M_eff": [Dt["M"][i] for i in range(1, Dt["s"] + 1)] if Dt["s"] >= 1 else [],
        "den_eff": den_t,
        "n_minus_2_child": D["n"] - 2,
        "n_minus_1_child": D["n"] - 1,
        "top_raw": D["M"][D["s"]] if D["s"] in D["M"] else None,
        "top_eff": Dt["M"][Dt["s"]] if Dt["s"] in Dt["M"] else None,
        "phi_raw": None if den == 0 else [str(x) for x in (phi_on(D) or [])],
        "phi_eff": None if den_t == 0 else [str(x) for x in (phi_on(Dt) or [])],
    })
    rec["M_s_eq_n_minus_2_child"] = rec["top_raw"] == rec["n_minus_2_child"]
    rec["anchor_zero"] = (den == 0)
    desc.append(rec)
    if den == 0:
        az.append(rec)
        if den_t == 0:
            az_after_drop.append(rec)
            rec["status"] = "ANCHOR-ZERO-AFTER-DROP"
        else:
            rec["status"] = "ANCHOR-ZERO-DROPPED-OK"
            evalable.append(rec)
    else:
        rec["status"] = "EVALABLE-AS-CHARGED"
        evalable.append(rec)
    records.append(rec)

print("  survivors:", len(surv100))
print("  u_s=1 (descendable):", len(desc))
print("  u_s>1:", len(us_gt1))
print("  anchor-zero (n'-M_s'-1=0, before drop):", len(az))
print("  evaluable as charged (den!=0):", len(desc) - len(az))
print("  after p.174 drop, still den=0:", len(az_after_drop))
print("  evaluable after repair:", len(evalable))
print("  s_eff after drop, among anchor-zero:")
from collections import Counter
print("   ", Counter(r["s_eff"] for r in az))
print("  top_eff == n'-2 among repaired az:",
      sum(1 for r in az if r["top_eff"] == r["n_prime"] - 2))
print("  top_eff <  n'-2 among repaired az:",
      sum(1 for r in az if r["top_eff"] is not None and r["top_eff"] < r["n_prime"] - 2))

print("\n  u_s>1 rows:")
for r in us_gt1:
    print("    n=%s m=%s M=%s V=%s d_s=%s u_s=%s" %
          (r["n"], r["m"], r["M"], r["V"], r["d_s"], r["u_s"]))

print("\n  ANCHOR-ZERO rows (n<=100), with (n,m,M,V,d_s) and repaired data:")
for r in az:
    print("    n=%s m=%s M=%s V=%s d_s=%s k=%s -> (n',m')=(%s,%s) M'=%s den=0 "
          "drop=%s s_eff=%s M_eff=%s den_eff=%s top_eff=%s n'-2=%s Φt=%s"
          % (r["n"], r["m"], r["M"], r["V"], r["d_s"], r["k"],
             r["n_prime"], r["m_prime"], r["M_prime"],
             r["dropped"], r["s_eff"], r["M_eff"], r["den_eff"],
             r["top_eff"], r["n_prime"] - 2, r["phi_eff"]))

# ---- D. n=108 screen ------------------------------------------------------
print("\n== D. n=108 C_FULL_TREE_ODE + descent/anchor (reproduce 12/20) ==")
rows108 = collect_rows(only_n=108)
print("  (1)-(13) rows n=108:", len(rows108))
# partition vs ode: Opus 217→21→20 is (1)-(13) of something?  compute-notes
# said 206 V at D=108.  The 217 may be a different Kmin/window.  We report both
# (1)-(13) count and the ODE-screened count.
surv108_part = [S for S in rows108 if T.full_tree_ok(S)]
surv108 = [S for S in rows108 if T.full_tree_ode_ok(S)]
print("  C_FULL_TREE (no ODE) survivors n=108:", len(surv108_part))
print("  C_FULL_TREE_ODE survivors n=108:", len(surv108))

desc108, us108, az108 = [], [], []
for S in surv108:
    us = u_s_of(S)
    if us != 1:
        us108.append(S)
        continue
    D = descend(S)
    den = anchor_den(D)
    Dt = truncate_jacobian(D)
    rec = {
        "n": S.n, "m": S.m,
        "M": [S.M[i] for i in range(1, S.s + 1)],
        "V": {i: S.V[i] for i in range(2, S.s + 1)},
        "d_s": S.d[S.s], "u_s": us, "k": D["k"],
        "n_prime": D["n"], "m_prime": D["m"],
        "M_prime": [D["M"][i] for i in range(1, D["s"] + 1)],
        "den": den, "dropped": Dt["dropped"],
        "s_eff": Dt["s"],
        "M_eff": [Dt["M"][i] for i in range(1, Dt["s"] + 1)] if Dt["s"] >= 1 else [],
        "den_eff": anchor_den(Dt),
        "top_eff": Dt["M"][Dt["s"]] if Dt["s"] in Dt["M"] else None,
        "phi_eff": None if anchor_den(Dt) == 0 else [str(x) for x in (phi_on(Dt) or [])],
    }
    desc108.append(rec)
    if den == 0:
        az108.append(rec)

print("  u_s=1:", len(desc108), " u_s>1:", len(us108),
      " anchor-zero:", len(az108),
      " evaluable-as-charged:", len(desc108) - len(az108))
print("  u_s>1 at n=108:")
for S in us108:
    print("    n=%s m=%s M=%s V=%s d_s=%s u_s=%s" %
          (S.n, S.m, [S.M[i] for i in range(1, S.s + 1)],
           {i: S.V[i] for i in range(2, S.s + 1)}, S.d[S.s], u_s_of(S)))
print("  ANCHOR-ZERO at n=108:")
for r in az108:
    print("    n=%s m=%s M=%s V=%s d_s=%s k=%s -> (%s,%s) M'=%s drop=%s s_eff=%s "
          "M_eff=%s den_eff=%s top_eff=%s n'-2=%s Φt=%s"
          % (r["n"], r["m"], r["M"], r["V"], r["d_s"], r["k"],
             r["n_prime"], r["m_prime"], r["M_prime"], r["dropped"],
             r["s_eff"], r["M_eff"], r["den_eff"], r["top_eff"],
             r["n_prime"] - 2, r["phi_eff"]))

# ---- E. five p.207 + two d_s=7: top characteristic exponent ---------------
print("\n== E. top characteristic exponent of the descended pair ==")
extra = []
# any (1)-(13) (84,56) with d_s=7
for S in rows8456:
    if S.d[S.s] == 7:
        extra.append(S)
print("  (84,56) (1)-(13) rows with d_s=7: %d" % len(extra))
for S in [M.Skel(n, m, Ms, Vs) for n, m, Ms, Vs, _ in p207_parents] + extra:
    D = descend(S)
    Dt = truncate_jacobian(D)
    print("  parent (%s,%s) M=%s V=%s d_s=%s u_s=%s"
          % (S.n, S.m, [S.M[i] for i in range(1, S.s + 1)],
             {i: S.V[i] for i in range(2, S.s + 1)}, S.d[S.s], u_s_of(S)))
    print("    child n'=%s m'=%s M'=%s  top_raw=%s  n'-2=%s n'-1=%s  "
          "Keller-top? %s  Jacobian-top? %s  drop=%s  top_eff=%s  Φ=%s Φt=%s"
          % (D["n"], D["m"], [D["M"][i] for i in range(1, D["s"] + 1)],
             D["M"][D["s"]], D["n"] - 2, D["n"] - 1,
             D["M"][D["s"]] == D["n"] - 2,
             D["M"][D["s"]] == D["n"] - 1,
             Dt["dropped"], Dt["M"].get(Dt["s"]),
             phi_on(D), phi_on(Dt)))

# ---- dump JSON ------------------------------------------------------------
out = {
    "n100": {
        "input_rows": len(rows100),
        "ode_survivors": len(surv100),
        "u_s_eq_1": len(desc),
        "u_s_gt_1": len(us_gt1),
        "anchor_zero": len(az),
        "evaluable_as_charged": len(desc) - len(az),
        "anchor_zero_after_drop": len(az_after_drop),
        "evaluable_after_repair": len(evalable),
        "anchor_zero_rows": az,
        "u_s_gt_1_rows": us_gt1,
    },
    "n108": {
        "input_rows": len(rows108),
        "partition_survivors": len(surv108_part),
        "ode_survivors": len(surv108),
        "u_s_eq_1": len(desc108),
        "u_s_gt_1": len(us108),
        "anchor_zero": len(az108),
        "evaluable_as_charged": len(desc108) - len(az108),
        "anchor_zero_rows": az108,
    },
    "rows8456_count": len(rows8456),
    "phi_10_of_10": ok10,
}
(HERE / "measure_anchor.json").write_text(json.dumps(out, indent=2, default=str) + "\n")
print("\nwrote", HERE / "measure_anchor.json")
print("DONE")
