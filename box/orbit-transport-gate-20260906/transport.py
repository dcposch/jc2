"""Orbit-transport gate: independent exact re-check of I'_M = u_s I_M.

Source objects are necessary configuration data, never polynomial pairs.
descend_own is the charged frozen instrument (repo copy, hash-identical);
own_v_routes is an uncharged repo dependency, declared in the report.
"""
import json, sys
from fractions import Fraction as Q
from math import gcd, lcm
sys.path.insert(0, "/home/ubuntu/jc2")
from box.lib.descend_own import descend_own, def51_radii, prefix_gcds, inverse_top

ROSTER = "/tmp/jc2-lane.cgofWX/inputs/roster.jsonl"

class Src:
    def __init__(self, n, m, M, V):
        self.n, self.m = n, m
        self.s = len(M)
        self.M = {i+1: M[i] for i in range(len(M))}
        self.V = {i+2: V[i] for i in range(len(V))}

def rows():
    out = {}
    for line in open(ROSTER):
        r = json.loads(line)
        out[r["row_id"]] = r
    return out

def parent_data(src):
    n, m, s = src.n, src.m, src.s
    M = src.M
    d = prefix_gcds(n, M)
    V = dict(src.V); V[s+1] = d[s+1]
    delta = def51_radii(n, M, d, V)
    return n, m, s, M, d, V, delta

# ---- Moh Prop 4.6 pattern data at a level -------------------------------
def level_params(n, m, s, M, d, V, delta, i):
    """P_i, Q_i, A_i for the selected level i (2<=i<=s)."""
    P = Q(V[i+1]*d[i], d[i+1]); Qq = Q(V[i+1]*(n-M[i]), d[i+1])
    L = 1
    for j in range(i+1, s+1):
        L = lcm(L, delta[j].denominator)
    A = (L*delta[i]).denominator
    assert P.denominator == 1 and Qq.denominator == 1
    return int(P), int(Qq), A

def packet_final(n, m, rho, delta0, a, ell=0):
    """Unsplit packet born at (rho, delta0) with -lambda_f = a: final major data.
    kappa = rho*((1+ell)-delta0) - a ;  ell-free I_M term (see xu-ell-shift 2.9)."""
    kappa = rho*((1+ell)-delta0) - a
    den = (n+m)*rho - m
    delta_fin = (1+ell) - Q((n+m)*kappa, den)
    term = Q(n*rho*kappa, den)
    lam_f = -a + rho*(delta_fin-delta0)          # order of f at the final disc
    lam_g = Q(n, m)*lam_f
    return dict(kappa=kappa, delta_fin=delta_fin, term=term, lam_f=lam_f, lam_g=lam_g)

def birth_a(n, m, M, delta, i):
    """-lambda_f at the birth of a level-i packet (Moh Prop 4.6(3), ell=0 parent)."""
    return Q(m*(1-delta[i]), n-M[i])

# ---- the transport test -------------------------------------------------
def child_level_params(out, i):
    """P'_i, Q'_i, A'_i from the CHILD datum returned by descend_own."""
    np_, mp = out["n"], out["m"]
    Mp, dp = out["M"], out["d"]
    sp = out["s"]
    Vp = {k: int(out["V_vectors"][0][k-2]) for k in range(2, sp+1)}
    Vp[sp+1] = dp[sp+1]
    dl = {r["first_nonzero"]: r["delta"] for r in out["child_radii"]}
    delta_p = list(dl.values())[0]
    P = Q(Vp[i+1]*dp[i], dp[i+1]); Qq = Q(Vp[i+1]*(np_-Mp[i]), dp[i+1])
    L = 1
    for j in range(i+1, sp+1):
        L = lcm(L, delta_p[j].denominator)
    A = (L*delta_p[i]).denominator
    return int(P), int(Qq), A, delta_p, Vp

def run_row(rid, rec, orbit_extra=True):
    s = rec["source"]
    src = Src(s["n"], s["m"], s["M"], s["V"])
    n, m, ss, M, d, V, delta = parent_data(src)
    out = descend_own(src)
    us, vs, ell = out["us"], out["vs"], out["ell"]
    res = dict(row=rid, n=n, m=m, s=ss, u_s=us, v_s=vs, ell=ell,
               np=out["n"], mp=out["m"], parent_delta={k: str(v) for k, v in delta.items()},
               top_license=out["top_license"], route=out["route_state"])
    if not out["child_radii"]:
        res["status"] = "NO_CHILD_ROUTE"; return res
    cr = out["child_radii"][0]
    j = cr["first_nonzero"]
    res["first_nonzero"] = j
    res["eps"] = str(delta[j])
    res["radius_rule_equals_child_def51"] = cr.get("effective_formula_agrees")
    # --- parent level-j packet, canonical pattern z=0 -------------------
    P, Qq, A = level_params(n, m, ss, M, d, V, delta, j)
    res["parent_PQA"] = (P, Qq, A)
    if P < A*V[j]:
        res["status"] = "CANONICAL_PATTERN_UNAVAILABLE"; return res
    fill = (P - A*V[j])//A
    z = P - A*V[j] - A*fill
    orbits = (V[j],) + (1,)*fill
    res["parent_orbits"] = orbits; res["parent_zero_part"] = z
    rho = Q(m*V[j], d[j]); a = birth_a(n, m, M, delta, j)
    par = packet_final(n, m, rho, delta[j], a, ell=0)
    res["parent_packet"] = dict(N=A, rho=str(rho), delta0=str(delta[j]),
                                a=str(a), kappa=str(par["kappa"]),
                                delta_fin=str(par["delta_fin"]),
                                lam_g=str(par["lam_g"]), term=str(par["term"]),
                                orbit_total=str(A*par["term"]))
    # --- the local rule's prediction -----------------------------------
    eps = delta[j]
    pred = dict(Np=eps*A, rhop=rho,
                deltap_fin=(vs-us) + (Q(us)/eps)*(par["delta_fin"]-1),
                lam_gp=(Q(us)/eps)*par["lam_g"],
                deltap_0=(vs-us) + (Q(us)/eps)*(delta[j]-1))
    res["transport_prediction"] = {k: str(v) for k, v in pred.items()}
    # --- the child's OWN computation ------------------------------------
    it = inverse_top(n, d[ss], d[j], us, vs, delta[j], z, orbits)
    res["inverse_top_W0"] = str(it["inverse_groups"][0]["V"])
    if us == 1:
        Pp, Qp, Ap, dpv, Vp = child_level_params(out, j)
        npp, mpp, Mp, dp = out["n"], out["m"], out["M"], out["d"]
        res["child_PQA"] = (Pp, Qp, Ap)
        res["child_A_equals_eps_N"] = (Ap == eps*A)
        res["child_P_matches_inverse_top"] = (
            Pp == int(it["inverse_groups"][0]["V"]) + int(eps.numerator)*sum(orbits))
        # total child f-roots at level j: zero part + eps*N*rho over the orbits
        W0 = it["inverse_groups"][0]["V"]
        tot = Q(mpp*W0, dp[j]) + sum(Q(mpp*r, dp[j])*Ap for r in orbits)
        par_tot = sum(Q(m*r, d[j])*A for r in orbits) + Q(m*z, d[j])
        res["child_level_f_roots"] = str(tot)
        res["parent_level_f_roots"] = str(par_tot)
        res["Nrho_transport_eps"] = str(Q(mpp*W0, dp[j])/Q(m*z, d[j])) if z else None
        rhop = Q(mpp*Vp[j], dp[j])
        ap = Q(mpp*((1+ell)-dpv[j]), npp-Mp[j])
        ch = packet_final(npp, mpp, rhop, dpv[j], ap, ell=ell)
        res["child_packet"] = dict(N=Ap, rho=str(rhop), delta0=str(dpv[j]),
                                   a=str(ap), kappa=str(ch["kappa"]),
                                   delta_fin=str(ch["delta_fin"]),
                                   lam_g=str(ch["lam_g"]), term=str(ch["term"]),
                                   orbit_total=str(Ap*ch["term"]))
        res["rho_preserved"] = (rhop == rho)
        res["delta_fin_matches_rule"] = (ch["delta_fin"] == pred["deltap_fin"])
        res["lam_g_matches_rule"] = (ch["lam_g"] == pred["lam_gp"])
        ratio = Q(Ap*ch["term"], A*par["term"]) if par["term"] else None
        res["orbit_term_ratio"] = str(ratio)
        res["ratio_equals_us"] = (ratio == us)
    else:
        # u_s>1: no licensed child terminal identification -> rule-only check
        Np = eps*A
        res["child_packet_rule_only"] = dict(
            N=str(Np), rho=str(rho), delta_fin=str(pred["deltap_fin"]),
            lam_g=str(pred["lam_gp"]),
            orbit_total=str(-Np*rho*pred["lam_gp"]))
        res["orbit_term_ratio"] = str(
            Q(-Np*rho*pred["lam_gp"], -A*rho*par["lam_g"]))
        res["ratio_equals_us"] = (Np*pred["lam_gp"] == us*A*par["lam_g"])
    res["status"] = "OK"
    return res

# ---- row-level selected-final-major transport ---------------------------
def orbit_sizes(delta, s, j):
    """Actual centre-stabilizer orbit sizes: only the level-j nonzero centre
    enlarges the denominator lattice (descend_own l.151-152; exact-contact
    gate sec.4 'actual zero-centre stabilizer')."""
    A = {}
    for i in range(s, 1, -1):
        if i > j:                      # selected factor is the ZERO part: one disc
            A[i] = 1
            continue
        L = 1
        for k in range(i+1, j+1):      # only nonzero centre coefficients count
            L = lcm(L, delta[k].denominator)
        A[i] = (L*delta[i]).denominator
    return A

def row_transport(rid, rec):
    s0 = rec["source"]; src = Src(s0["n"], s0["m"], s0["M"], s0["V"])
    n, m, ss, M, d, V, delta = parent_data(src)
    out = descend_own(src)
    us, vs, ell = out["us"], out["vs"], out["ell"]
    r = dict(row=rid, nm=(n, m), s=ss, u_s=us, ell=ell, child_nm=(out["n"], out["m"]))
    if not out["child_radii"]:
        r["status"] = "NO_CHILD"; return r
    cr = out["child_radii"][0]; j = cr["first_nonzero"]
    r["j"] = j; r["eps"] = str(delta[j])
    A = orbit_sizes(delta, ss, j)
    N = 1
    for i in range(2, ss+1):
        N *= A[i]
    rho = Q(m*V[2], d[2])
    r["parent"] = dict(N=N, rho=str(rho), delta_1=str(delta[1]),
                       A=({i: A[i] for i in A}))
    IM = Q(n, n+m)*N*rho*(1-delta[1])
    r["I_M_selected"] = str(IM)
    if us != 1:
        r["status"] = "U_GE_2_NO_LICENSED_CHILD_DEF51"
        r["child_delta_1_rule"] = str(cr["delta"][1])
        Np = delta[j]*A[j]*(N//A[j])
        r["child_rule_only"] = dict(N=str(Np), rho=str(rho),
                                    delta_1=str(cr["delta"][1]))
        r["IMp_rule_only"] = str(Q(n, n+m)*Np*rho*((1+ell)-cr["delta"][1]))
        r["ratio_rule_only"] = str(Q(n, n+m)*Np*rho*((1+ell)-cr["delta"][1])/IM)
        return r
    npp, mpp, Mp, dp, sp = out["n"], out["m"], out["M"], out["d"], out["s"]
    dpv = cr["delta"]
    Ap = orbit_sizes(dpv, sp, j)
    Np = 1
    for i in range(2, sp+1):
        Np *= Ap[i]
    Vp = {k: int(out["V_vectors"][0][k-2]) for k in range(2, sp+1)}
    rhop = Q(mpp*Vp[2], dp[2])
    IMp = Q(npp, npp+mpp)*Np*rhop*((1+ell)-dpv[1])
    r["child"] = dict(N=Np, rho=str(rhop), delta_1=str(dpv[1]),
                      A=({i: Ap[i] for i in Ap}))
    r["I_Mprime_selected"] = str(IMp)
    r["ratio"] = str(IMp/IM) if IM else None
    r["ratio_equals_us"] = (IMp == us*IM)
    r["Nrho_equals_eps_Nrho"] = (Np*rhop == delta[j]*N*rho)
    r["status"] = "OK"
    return r
