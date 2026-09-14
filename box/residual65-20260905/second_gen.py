#!/usr/bin/env python3
"""Second-generation necessary-tower tests on the 66-row residual roster.

Population: box/residual66-20260905/roster.jsonl (frozen copy in the lane inputs).
Every row is a NECESSARY TOWER CONFIGURATION, never a polynomial pair.

Tests applied to the CHILD tower (n', m', M', d', V', delta', ell), all exact rationals:

  (W)  child's own Def 5.1(2) window at level j:  P'_j >= V'_j > d'_j/(n'-M'_j)
       [Moh p.179 Def 5.1(2); p.201 (7)].
  (GO) child-level Galois pattern + ODE at level j (Moh p.201 (8)-(11) + Prop 4.6 (2)-(5)
       via the p.171 Remark for J = x^l, + Prop A.3 p.205):
         p(xi) = xi^z prod (xi^A - c_nu)^{r_nu},  z + A*sum r = P'_j,
         A = den(L'_j delta'_j), L'_j = lcm{den delta'_i : i > j}   (p.201 (8)),
         V'_j in {z} u {r_nu}                                        (p.201 (10),(11)),
         [z>0] + A*#orbits <= Q'_j   (q squarefree, roots(p) c roots(q): 4.6(3),(4)),
         no multiplicity equals P'_j/Q'_j  ((P-Qv) q'(a) = c != 0 from A.3's identity;
         this also excludes p = q^w, 4.6(5)),
         some multiplicity > P'_j/Q'_j   (A.3(4)).
       P'_j = V'_{j+1} d'_j/d'_{j+1},  Q'_j = V'_{j+1}(n'-M'_j)/d'_{j+1}.
       At the child's top (u_s = 1 only, chain closed, d'_{s'+1} = 1): V'_{s'+1} = 1,
       so P'_{s'} = d'_{s'}, Q'_{s'} = n' - M'_{s'}.
  (B)  child-bottom divisibility, Moh p.188 / p.201 (12),(13), l-independent because the
       Galois action is field theory and the r = 1 ODE D(n,-M_1,g_s,T_s) = const is
       l-valid (p.171 Remark):
         A'_1 | N' and A'_1 | M'-1   or   A'_1 | M' and A'_1 | N'-1,
         N' = (n'/d'_2) V'_2,  M' = (m'/d'_2) V'_2,  A'_1 = den(L'_1 delta'_1).
  (SD) second-descent polynomiality.  If delta'_{s'} = -1 (Prop 6.3 hypothesis) and the
       child's top form has a MINOR point of multiplicity u (u <= d'_{s'}/(n'-M'_{s'}),
       p.190) whose minor-disc radius is >= v'/u (Prop 6.4 when u = 1, as Moh himself
       uses on the l=1 child (16,12), p.207-208), then Prop 6.3(1) gives a POLYNOMIAL
       grandchild whose Jacobian is, by the p.198 chain rule with J(P,Q) = c gamma^l,
           c' gamma'^{(v'-u-1) - u*l} * (1 - e'gamma'^u - ... - pi' gamma'^{u+v'})^l ,
       hence (v'-u-1) - u*l >= 0 is necessary, v' = d'_{s'} - u.
       Licence: u = 1 -> Prop 6.4 under J = x^l (Prop 6.1(2)'s Prop 4.4 conditions shift
       by -l and reduce to the same V_r <= d_r/(n-M_r), p.192); u >= 2 -> conditional on
       the child's split window (OPEN[PROP6.3-RADIUS-US>1] analogue).

Controls: Moh's five p.207 rows (R001-R004, R007) must PASS every test typed DETERMINED;
(99,66) (R015) must PASS everything.  Parent-level replay (l = 0) in controls.py.
"""
from __future__ import annotations
import json, sys, os
from fractions import Fraction as F
from math import gcd, lcm
from functools import lru_cache
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROSTER = "/tmp/jc2-lane.3peIuR/inputs/roster.jsonl"
if not os.path.exists(ROSTER):
    ROSTER = os.path.join(HERE, "roster.frozen.jsonl")


def Fr(x):
    return F(x) if not isinstance(x, str) else F(x)


def def51_radii(n, M, d, V, s, mult=1):
    """Def 5.1(3) p.179 radii for the tower (n, M_1..M_s, d, V_2..V_s); Phi_eff scaling mult=l+1."""
    out = {}
    for i in range(1, s + 1):
        ratio = F(n - M[i], n - M[s] - 1)
        for j in range(i + 1, s + 1):
            ratio *= F(V[j] * (n - M[j]) - d[j], V[j] * (n - M[j - 1]) - d[j])
        out[i] = mult * (1 - ratio)
    return out


def patterns(P, Q, A, Vsel, lo, want_all=False):
    """Admissible (z, orbits) patterns at one level.  Returns list of dicts (empty = level dead).
    lo = d_j/(n-M_j) = P/Q.  Conditions as in the module docstring."""
    P = int(P); Q = int(Q); A = int(A); Vsel = int(Vsel)
    lo_int = lo.numerator if lo.denominator == 1 else None
    found = []

    def ok_mult(v):
        return lo_int is None or v != lo_int

    for z in range(P % A, P + 1, A):
        if z > 0 and not ok_mult(z):
            continue
        total = (P - z) // A                     # sum of orbit multiplicities
        cap = (Q - (1 if z > 0 else 0)) // A     # max number of orbits (distinct roots <= Q)
        if cap < 0:
            continue
        # enumerate partitions of `total` into k <= cap parts, parts != lo, non-increasing
        def rec(rem, maxpart, left, acc):
            if rem == 0:
                mults = ([z] if z > 0 else []) + list(acc)
                if not mults:
                    return
                if Vsel not in mults:
                    return
                if not any(v > lo for v in mults):
                    return
                found.append(dict(z=z, orbits=tuple(acc), A=A, P=P, Q=Q,
                                  distinct=(1 if z > 0 else 0) + A * len(acc)))
                return
            if left == 0:
                return
            for v in range(min(rem, maxpart), 0, -1):
                if not ok_mult(v):
                    continue
                if rem - v > (left - 1) * v:      # remaining cannot be filled with parts <= v
                    continue
                rec(rem - v, v, left - 1, acc + (v,))
                if found and not want_all:
                    return
        rec(total, total if total > 0 else 0, cap, ())
        if found and not want_all:
            break
    return found


def level_test(n, m, M, d, V, delta, s, j, Vnext, want_all=True):
    """One child level j with V_{j+1} = Vnext supplied.  Returns dict.  want_all=False: existence only."""
    P = F(Vnext * d[j], d[j + 1]); Q = F(Vnext * (n - M[j]), d[j + 1])
    assert P.denominator == 1 and Q.denominator == 1, (P, Q)
    P = int(P); Q = int(Q)
    lo = F(d[j], n - M[j])
    L = 1
    for i in range(j + 1, s + 1):
        L = lcm(L, delta[i].denominator)
    A = (L * delta[j]).denominator
    window = (P >= V[j] > lo)
    pats = patterns(P, Q, A, V[j], lo, want_all=want_all)
    return dict(j=j, P=P, Q=Q, A=A, L=L, lo=str(lo), delta=str(delta[j]), V=V[j],
                window=window, n_patterns=len(pats), alive=(window and len(pats) > 0),
                patterns=[dict(z=p["z"], orbits=list(p["orbits"]), distinct=p["distinct"]) for p in pats[:12]])


def bottom_test(n, m, M, d, V, delta, s):
    L = 1
    for i in range(2, s + 1):
        L = lcm(L, delta[i].denominator)
    A1 = (L * delta[1]).denominator
    N = F(n * V[2], d[2]); Mm = F(m * V[2], d[2])
    assert N.denominator == 1 and Mm.denominator == 1
    N = int(N); Mm = int(Mm)
    b12 = (N % A1 == 0) and ((Mm - 1) % A1 == 0)
    b13 = (Mm % A1 == 0) and ((N - 1) % A1 == 0)
    return dict(A1=A1, L=L, delta1=str(delta[1]), N=N, M=Mm, b12=b12, b13=b13,
                alive=(b12 or b13), vacuous=(A1 == 1))


def second_descent_test(n, M, d, V, delta, s, ell, top_patterns):
    """(SD) at the child's top.  Needs delta_s = -1 and the top patterns (A = 1)."""
    if delta[s] != -1:
        return dict(applies=False, reason="delta'_{s'} != -1: Prop 6.3 hypothesis fails", alive=True)
    dtop = d[s]; lo = F(dtop, n - M[s]); Vsel = V[s]
    per_pattern = []
    any_ok = False
    kill_licence = set()
    for p in top_patterns:
        mults = ([p["z"]] if p["z"] > 0 else []) + list(p["orbits"])
        # A must be 1 at an integral radius
        rest = list(mults); rest.remove(Vsel)
        pts = []
        pat_ok = True
        for u in rest:
            minor = (F(u) <= lo)
            v = dtop - u
            ell2 = (v - u - 1) - u * ell
            poly_ok = (ell2 >= 0)
            pts.append(dict(u=u, minor=minor, v=v, ell2=ell2, poly_ok=poly_ok))
            if minor and not poly_ok:
                pat_ok = False
                kill_licence.add("P64-ELL" if u == 1 else "CHILD-SPLIT-WINDOW-u%d" % u)
        per_pattern.append(dict(pattern=dict(z=p["z"], orbits=list(p["orbits"])), points=pts, ok=pat_ok))
        any_ok = any_ok or pat_ok
    # licence typing of a kill: DETERMINED-mod-P64ELL iff every pattern fails at a u=1 minor point
    if any_ok:
        typing = "SURVIVES"
    else:
        all_u1 = all(any(pt["minor"] and not pt["poly_ok"] and pt["u"] == 1 for pt in pp["points"])
                     for pp in per_pattern)
        typing = "KILL[P64-ELL]" if all_u1 else "KILL[CONDITIONAL:" + ",".join(sorted(kill_licence)) + "]"
    return dict(applies=True, alive=any_ok, typing=typing, lo_top=str(lo), d_top=dtop, ell=ell,
                per_pattern=per_pattern)


def analyse_row(r):
    src = r["source"]; ch = r["own_child"]; desc = r["descent"]; rc = r["receiver_chart"]
    n, m, s = src["n"], src["m"], src["s"]
    us, vs = src["u_s"], src["v_s"]
    ell = vs - us - 1
    assert ell == ch["ell"]
    np_, mp, sp = ch["n_prime"], ch["m_prime"], ch["s_prime"]
    Mp = {i + 1: ch["M_prime"][i] for i in range(sp)}
    dp = {i + 1: ch["d_prime"][i] for i in range(sp + 1)}
    Vp = {i + 2: ch["V_prime"][i] for i in range(sp - 1)}
    dlp = {i + 1: Fr(ch["delta_prime"][i]) for i in range(sp)}
    prefix = desc["prefix_only"]
    complete = not prefix
    # sanity: d' chain
    dchk = {1: np_}
    for i in range(1, sp + 1):
        dchk[i + 1] = gcd(dchk[i], Mp[i])
    assert dchk == dp, (r["row_id"], dchk, dp)
    assert Mp[1] == -mp
    # radii replay (Phi_eff = (l+1) Def 5.1(3)) for complete chains
    radii_replay = None
    if complete:
        assert dp[sp + 1] == 1 and us == 1
        Vfull = dict(Vp); Vfull[sp + 1] = 1
        rad = def51_radii(np_, Mp, dp, Vfull, sp, ell + 1)
        radii_replay = (rad == dlp)
        assert radii_replay, (r["row_id"], rad, dlp)
    out = dict(row_id=r["row_id"], source=(n, m), s=s, u_s=us, v_s=vs, ell=ell,
               M=src["M"], V=src["V"], delta=src["delta"],
               child=(np_, mp), s_prime=sp, M_prime=ch["M_prime"], V_prime=ch["V_prime"],
               d_prime=ch["d_prime"], delta_prime=ch["delta_prime"],
               K=rc["K"], e=np_ // rc["K"], q=mp // rc["K"], unknowns=rc["unknowns_without_T"],
               receiver_key=rc["receiver_key_string"], route=desc["route"], prefix=prefix,
               tags=r["controls"]["tags"], n_le_100=(n <= 100),
               radii_replay=radii_replay)
    # level tests
    levels = []
    top_pats = None
    js = list(range(sp, 1, -1)) if complete else list(range(sp - 1, 1, -1))
    for j in js:
        Vnext = 1 if (j == sp) else Vp[j + 1]
        lt = level_test(np_, mp, Mp, dp, Vp, dlp, sp, j, Vnext)
        levels.append(lt)
        if j == sp:
            top_pats = patterns(lt["P"], lt["Q"], lt["A"], Vp[sp], F(dp[sp], np_ - Mp[sp]), want_all=True)
    out["levels"] = levels
    out["levels_alive"] = all(l["alive"] for l in levels)
    out["top_untested_prefix"] = prefix
    # bottom
    bt = bottom_test(np_, mp, Mp, dp, Vp, dlp, sp)
    out["bottom"] = bt
    # second descent
    if complete:
        out["sd"] = second_descent_test(np_, Mp, dp, Vp, dlp, sp, ell, top_pats)
    else:
        # prefix: top pattern unknown; report the numeric envelope only
        dtop = dp[sp]; lo = F(dtop, np_ - Mp[sp])
        out["sd"] = dict(applies=(dlp[sp] == -1), alive=True, typing="PREFIX-UNTESTED",
                         note="V'_{s'+1} unknown at u_s>1; d'_{s'}-3-l=%d; u'=d'-V'=%d, lo=%s"
                         % (dtop - 3 - ell, dtop - Vp[sp], lo))
    # sibling-major flag at top (complete rows): does EVERY admissible top pattern force a
    # second MAJOR point (u > lo)?
    if complete and top_pats:
        lo = F(dp[sp], np_ - Mp[sp])
        forced_major = all(any(F(u) > lo for u in (([p["z"]] if p["z"] > 0 else []) + list(p["orbits"]))
                                if True) and
                           (lambda ms: (ms.remove(Vp[sp]) or True) and any(F(u) > lo for u in ms))(
                               ([p["z"]] if p["z"] > 0 else []) + list(p["orbits"]))
                           for p in top_pats)
        out["top_forced_major_sibling"] = forced_major
    else:
        out["top_forced_major_sibling"] = None
    verdict = []
    if not out["levels_alive"]:
        verdict.append("GO-KILL")
    if not bt["alive"]:
        verdict.append("B-KILL")
    if out["sd"].get("applies") and not out["sd"]["alive"]:
        verdict.append("SD-" + out["sd"]["typing"])
    out["verdict"] = verdict or ["SURVIVES"]
    return out


def main():
    rows = [json.loads(l) for l in open(ROSTER)]
    res = [analyse_row(r) for r in rows]
    json.dump(res, open(os.path.join(HERE, "second_gen.json"), "w"), indent=1, default=str)
    # ------- report -------
    W = sys.stdout.write
    W("second_gen.py on %d roster rows (R001 kept as the Xu-removed control)\n\n" % len(res))
    W("%-5s %-9s u s s' l  %-9s %-14s %-9s %-22s  W/GO  B(A1)   SD\n" % ("row", "(n,m)", "child", "M'", "V'", "delta'"))
    for o in res:
        go = "ok" if o["levels_alive"] else "KILL"
        if o["prefix"]:
            go += "(pfx)"
        b = ("ok" if o["bottom"]["alive"] else "KILL") + "(%d)" % o["bottom"]["A1"]
        sd = o["sd"]["typing"] if o["sd"].get("applies") else "n/a"
        W("%-5s (%3d,%3d) %d %d %d  %d  (%2d,%2d)   %-14s %-9s %-22s  %-6s %-8s %s %s\n" % (
            o["row_id"], o["source"][0], o["source"][1], o["u_s"], o["s"], o["s_prime"], o["ell"],
            o["child"][0], o["child"][1], str(o["M_prime"]), str(o["V_prime"]), str(o["delta_prime"]),
            go, b, sd, ",".join(o["tags"])))
    W("\n== counts ==\n")
    c = Counter(tuple(o["verdict"]) for o in res)
    for k, v in sorted(c.items(), key=lambda kv: -kv[1]):
        W("  %-45s %d\n" % ("+".join(k), v))
    W("\n== controls ==\n")
    for o in res:
        if o["tags"]:
            W("  %s %s tags=%s verdict=%s\n" % (o["row_id"], o["source"], o["tags"], o["verdict"]))
    W("\n== bottom test detail (child (12')/(13')) ==\n")
    vac = sum(1 for o in res if o["bottom"]["vacuous"])
    W("  vacuous (A'_1 = 1): %d ; nonvacuous pass: %d ; fail: %d\n" % (
        vac, sum(1 for o in res if not o["bottom"]["vacuous"] and o["bottom"]["alive"]),
        sum(1 for o in res if not o["bottom"]["alive"])))
    W("\n== SD detail ==\n")
    for o in res:
        sd = o["sd"]
        if sd.get("applies") and not o["prefix"]:
            W("  %s child=%s d'_top=%d l=%d lo_top=%s -> %s\n" % (o["row_id"], o["child"], sd["d_top"], sd["ell"], sd["lo_top"], sd["typing"]))
            for pp in sd["per_pattern"]:
                W("      pattern %s : %s -> %s\n" % (pp["pattern"], [(pt["u"], "minor" if pt["minor"] else "MAJOR", pt["ell2"]) for pt in pp["points"]], "ok" if pp["ok"] else "FAIL"))
        elif o["prefix"]:
            W("  %s PREFIX %s\n" % (o["row_id"], sd.get("note", "")))
    W("\n== top-level forced major sibling (complete rows) ==\n")
    fm = [o["row_id"] for o in res if o["top_forced_major_sibling"]]
    W("  rows where every admissible top pattern has a second MAJOR point: %d %s\n" % (len(fm), fm))
    W("\n== levels detail (GO) ==\n")
    for o in res:
        for l in o["levels"]:
            W("  %s j=%d P=%d Q=%d A=%d L=%d lo=%s delta=%s V=%d window=%s patterns=%d %s\n" % (
                o["row_id"], l["j"], l["P"], l["Q"], l["A"], l["L"], l["lo"], l["delta"], l["V"], l["window"], l["n_patterns"],
                "" if l["alive"] else "DEAD"))


if __name__ == "__main__":
    main()
