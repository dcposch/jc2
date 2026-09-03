#!/usr/bin/env python3
"""Rigid-stratum ∩ gap-free tree screen, congruence scan, cofinal-ray attempt.

Lane rigid-congruence-grok46-20260903.  Standard library only.

Frozen copies of moh_skeleton_full.py and full_tree_partition.py live in
this directory (repro/ and ./); SHA-256 must match the charged inputs.

Screens
-------
GAP-FREE operative (AUDIT 17(u); whole-tree-review §7.4):
  partition + universal siblings + (12)/(13), Prop.5.6 disabled
  (TreePartition.embed_node starting with dangerous=False).
  Optional ODE (3.7) and passport (3.8).
GAPPED side column: C_FULL_TREE / C_FULL_TREE_ODE (ungated Prop.5.6).

Fail-closed: Moh's six survive every screen; unscreened counts reproduce
658 / 23720/14016 and pre-screen u_s>1 = 4012/14016 groups, or the run
aborts before any result number is printed.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import sys
import time
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "repro"))
import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as FT  # noqa: E402


INPUTS = Path("/tmp/jc2-lane.hDXm11/inputs")
CHARGED_SHA = {
    "moh_skeleton_full.py":
        "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
    "full_tree_partition.py":
        "875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8",
}

FAILURES: list[str] = []
NCHECK = [0]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def check(name: str, cond, detail: str = "") -> bool:
    NCHECK[0] += 1
    if cond:
        print("  [ok]   %s" % name, flush=True)
        return True
    print("  [FAIL] %s   %s" % (name, detail), flush=True)
    FAILURES.append(name)
    return False


def abort_if_failed(stage: str) -> None:
    if FAILURES:
        print("%s FAILED: %s" % (stage, FAILURES), flush=True)
        sys.exit(1)


def frac_text(x) -> str:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else "%s/%s" % (x.numerator, x.denominator)
    return str(x)


def row_tuple(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)),
            tuple((i, S.V[i]) for i in range(2, S.s + 1)))


def v_map(S):
    return {i: S.V[i] for i in range(2, S.s + 1)}


def m_list(S):
    return [S.M[i] for i in range(2, S.s + 1)]


def d_list(S):
    return [S.d[i] for i in range(1, S.s + 2)]


# ---------------------------------------------------------------------------
# screens
# ---------------------------------------------------------------------------
_GAP = {}


def gap_tree(S, ode=False, passport=False) -> FT.TreePartition:
    key = (bool(ode), bool(passport)) + FT.skel_key(S)
    T = _GAP.get(key)
    if T is None:
        T = FT.TreePartition(
            S,
            ode_nondegenerate=bool(ode or passport),
            ode_passport=bool(passport),
        )
        _GAP[key] = T
    return T


def gap_embed(S, ode=False, passport=False):
    T = gap_tree(S, ode=ode, passport=passport)
    required = {i: S.V[i] for i in range(2, S.s)}
    return T.embed_node(T.s - 1, T.initial_path(), False, required)


def gap_ok(S, ode=False, passport=False) -> bool:
    return gap_embed(S, ode=ode, passport=passport)[0]


def gapped_ok(S, ode=False, passport=False) -> bool:
    return FT.evaluator(
        S, ode_nondegenerate=bool(ode or passport), ode_passport=bool(passport)
    ).embeds(S)[0]


def screen_bundle(S) -> dict:
    g0, w0 = gap_embed(S, False, False)
    g1, w1 = gap_embed(S, True, False)
    g2, w2 = gap_embed(S, True, True)
    c0 = FT.full_tree_ok(S)
    c1 = FT.full_tree_ode_ok(S)
    return {
        "gap_partition": g0,
        "gap_ode": g1,
        "gap_passport": g2,
        "C_FULL_TREE": c0,
        "C_FULL_TREE_ODE": c1,
        "gap_partition_witness_j": None if g0 else w0.get("j"),
        "gap_partition_failure": None if g0 else _fail_text(w0),
        "C_FULL_TREE_j": None if c0 else FT.evaluator(S).embeds(S)[1].get("j"),
    }


def _fail_text(w) -> str:
    if not isinstance(w, dict):
        return repr(w)
    if "failure" in w:
        return str(w["failure"])
    fails = w.get("failures") or []
    if fails:
        bits = []
        for item in fails[:6]:
            if isinstance(item, dict):
                bits.append("b=%s:%s" % (item.get("b"), item.get("failure")))
            else:
                bits.append(str(item))
        return "; ".join(bits)
    return "j=%s A=%s P=%s Q=%s" % (w.get("j"), w.get("A"), w.get("P"), w.get("Q"))


# ---------------------------------------------------------------------------
# packets / UNI / descent
# ---------------------------------------------------------------------------
def orbit_sizes(S):
    opts = []
    for j in range(2, S.s):
        _ok, b10, b11 = S.cond1011(j)
        A = int(S.A(j))
        o = []
        if b11:
            o.append(1)
        if b10:
            o.append(A)
        if not o:
            o.append(1)
        opts.append(sorted(set(o)))
    if not opts:
        return {1}
    sizes = set()
    for combo in itertools.product(*opts):
        p = 1
        for c in combo:
            p *= c
        sizes.add(p)
    return sizes


def packets_of(S, Nhi=10 ** 9):
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
        out.append({"w": w, "c": frac_text(c), "om": om, "tag": tag})
    return out


def uni_packets(S, nlo=6, nhi=None):
    v2 = int(S.V[2])
    q = S.q()
    u = int(S.u)
    out = []
    if v2 <= 0:
        return out
    kmax = int(u) // v2
    for k in range(1, kmax + 1):
        val = k * v2 * q
        if val.denominator == 1 and val >= nlo and (nhi is None or val <= nhi):
            out.append({"k": k, "N": int(val)})
    return out


def k_sat(S) -> int:
    v2 = int(S.V[2])
    if v2 <= 0:
        return 0
    return int(S.u) // v2


def u_s_of(S) -> int:
    return S.d[S.s] - S.V[S.s]


def anchor_zero(S) -> bool:
    """M_{s-1} = n - d_s  (Opus H1 / OPEN[DESCENT-ANCHOR])."""
    if S.s < 2:
        return False
    return S.M[S.s - 1] == S.n - S.d[S.s]


def descend_once(S):
    s, ds, vs = S.s, S.d[S.s], S.V[S.s]
    us = ds - vs
    if us != 1:
        return {"status": "NOT-US1", "us": us, "vs": vs, "ds": ds}
    vals = [S.n, S.m] + [S.M[i] for i in range(1, s)] + [S.d[i] for i in range(1, s + 1)]
    if any(x % ds != 0 for x in vals):
        return {"status": "NOT-INTEGRAL", "us": us, "vs": vs, "ds": ds}
    n2, m2 = S.n // ds, S.m // ds
    k = vs - us - 1
    M2 = {i: S.M[i] // ds for i in range(1, s)}
    d2 = {i: S.d[i] // ds for i in range(1, s + 1)}
    V2 = {i: S.V[i] for i in range(2, s)}
    sprime = max(M2) if M2 else 0
    chain = [n2]
    gcd_ok = True
    for i in range(1, sprime + 1):
        chain.append(gcd(chain[-1], M2[i]))
        want = d2.get(i + 1)
        if want is None or chain[-1] != want:
            gcd_ok = False
    M_last = M2.get(sprime)
    az = (M_last == n2 - 1) if M_last is not None else False
    return {
        "status": "DESCENDED",
        "n": n2, "m": m2,
        "M": [M2[i] for i in range(2, sprime + 1)],
        "V": [V2[i] for i in range(2, sprime + 1)] if sprime >= 2 else [],
        "k": k, "s": sprime, "us": us, "vs": vs, "ds": ds,
        "gcd_ok": gcd_ok, "anchor_zero": az,
        "K": gcd(n2, m2),
    }


def def51(n, M, d, V, s, i):
    den0 = n - M[s] - 1
    if den0 == 0:
        raise ZeroDivisionError("anchor")
    num = F(n - M[i])
    den = F(den0)
    for j in range(i + 1, s + 1):
        num *= (V[j] * (n - M[j]) - d[j])
        den_j = V[j] * (n - M[j - 1]) - d[j]
        if den_j == 0:
            raise ZeroDivisionError("window")
        den *= den_j
    return 1 - num / den


def h_monomials(delta1, deg_y, deg_x, tot):
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if i + j > tot:
                continue
            if F(i) <= delta1 * F(j + 1):
                out.append((i, j))
    return out


def beta_monomials(delta1, deg_y, deg_x, tot, weight):
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if tot is not None and i + j > tot:
                continue
            if F(i) <= delta1 * F(j + weight):
                out.append((i, j))
    return out


def appendix2_size(desc):
    """Estimate Appendix-II unknown count on a descended s'=2 pair.

    Uses the D1 monomial count of box/appendix2/shape.py (not charged; the
    formula is the unique D1 bound reproducing Moh pp.208, 210-211).  On
    anchor-zero the Def 5.1(3) denominator vanishes: typed OPEN, not filled.
    """
    if desc is None or desc.get("status") != "DESCENDED":
        return {"status": "NO-DESCENT", "detail": None if desc is None else desc.get("status")}
    n, m, s = desc["n"], desc["m"], desc["s"]
    K = desc["K"]
    crude = K * (K + 1) // 2
    out = {
        "status": "CRUDE",
        "s_prime": s,
        "n_prime": n,
        "m_prime": m,
        "K_prime": K,
        "crude_h_triangular": crude,
        "anchor_zero": desc.get("anchor_zero"),
        "k": desc.get("k"),
    }
    if desc.get("anchor_zero"):
        out["status"] = "ANCHOR-ZERO-UNDEFINED"
        out["n_ord"] = None
        return out
    if s != 2:
        out["status"] = "NOT-S2"
        out["note"] = "Appendix II is the s'=2 endgame; further descent required"
        return out
    M2 = desc["M"][0] if desc["M"] else None
    V2 = desc["V"][0] if desc["V"] else None
    k = desc["k"]
    if M2 is None or V2 is None:
        out["status"] = "MISSING-MV"
        return out
    d2 = gcd(n, m)
    Md = {1: -m, 2: M2}
    dd = {1: n, 2: d2, 3: gcd(d2, M2)}
    Vd = {2: V2, 3: dd[3]}
    try:
        raw2 = def51(n, Md, dd, Vd, 2, 2)
        raw1 = def51(n, Md, dd, Vd, 2, 1)
    except ZeroDivisionError:
        out["status"] = "DEF51-UNDEFINED"
        return out
    d2p, d1p = (k + 1) * raw2, (k + 1) * raw1
    u = d2 - V2
    degx_h = (u * K // d2) if d2 else 0
    degx_f = (u * m // d2) if d2 else 0
    if u < 0 or degx_h < 0:
        out["status"] = "U-NEGATIVE"
        return out
    hm = h_monomials(d1p, K, degx_h, K)
    bm = beta_monomials(d1p, K - 1, degx_f, m, m // K if K else 0)
    h_free = [t for t in hm if t != (0, K)]
    n_ord = len(h_free) + len(bm) + 1
    out.update({
        "status": "S2-D1",
        "delta2_prime": frac_text(d2p),
        "delta1_prime": frac_text(d1p),
        "n_h_free": len(h_free),
        "n_beta": len(bm),
        "n_ord": n_ord,
        "u_prime": u,
        "V2_prime": V2,
        "M2_prime": M2,
    })
    return out


# ---------------------------------------------------------------------------
# level-data / congruence tuples
# ---------------------------------------------------------------------------
def selected_path(S):
    path = [0] * (S.s + 1)
    for i in range(2, S.s + 1):
        path[i] = S.V[i]
    return tuple(path)


def node_tuple(T: FT.TreePartition, j: int, path):
    delta, L, A, P, Q, lo = T.level_data(j, path)
    b = P % A if A else None
    # H4: lo = d_j/(n-M_j) equals P/Q identically
    pq = F(P, Q) if Q else None
    return {
        "j": j,
        "delta": frac_text(delta),
        "L": L,
        "A": A,
        "P": P,
        "Q": Q,
        "P_mod_A": b,
        "h": frac_text(lo),
        "P_over_Q": frac_text(pq) if pq is not None else None,
        "h_eq_P_over_Q": (pq == lo) if pq is not None else None,
        "Q_gt_P": Q > P,
        "A_divides_P": (A != 0 and P % A == 0),
        "forced_major_zero": (b is not None and b > lo),
        "path_V_from_j": [path[i] for i in range(j, T.s + 1)],
    }


def congruence_dump(S):
    T = gap_tree(S, ode=False, passport=False)
    path = selected_path(S)
    selected = []
    siblings = []
    for j in range(S.s - 1, 1, -1):
        nt = node_tuple(T, j, path)
        selected.append(nt)
        A, P, Q, lo = nt["A"], nt["P"], nt["Q"], F(nt["h"])
        residue = P % A if A else 0
        # forced major siblings at this node: every b ≡ P (mod A), 0 ≤ b ≤ P,
        # with b > lo (the zero factor) AND every major orbit value that the
        # selected path does not itself occupy.  Child level-data uses the
        # extended path (A,P,Q at node j do not depend on V_j).
        forced_b = [b for b in range(residue, P + 1, A) if F(b) > lo]
        for b in forced_b:
            child_path = T.extend(path, j, b)
            entry = {
                "parent_j": j,
                "sibling_kind": "zero-factor" if b == residue or True else "orbit",
                "V_j": b,
                "is_selected": (b == S.V[j]),
                "zero_factor": True,
            }
            if j > 2:
                entry["child"] = node_tuple(T, j - 1, child_path)
            else:
                ok12, wit = T.bottom(child_path)
                entry["bottom"] = wit
                entry["bottom_12_or_13"] = ok12
            siblings.append(entry)
        # major nonzero orbit values that option_data would force
        total = (P - residue) // A if A else 0
        # we cannot list every orbit value without the tree; emit the selected
        # V_j as a nonzero sibling when it is major and not the zero remainder
        vj = S.V[j]
        if vj > lo and vj != residue:
            child_path = T.extend(path, j, vj)
            entry = {
                "parent_j": j,
                "sibling_kind": "selected-nonzero",
                "V_j": vj,
                "is_selected": True,
                "zero_factor": False,
            }
            if j > 2:
                entry["child"] = node_tuple(T, j - 1, child_path)
            else:
                ok12, wit = T.bottom(child_path)
                entry["bottom"] = wit
                entry["bottom_12_or_13"] = ok12
            siblings.append(entry)
        path = T.extend(path, j, S.V[j])
    return {"selected": selected, "forced_siblings": siblings}


def row_record(S, screens=None):
    us = u_s_of(S)
    desc = descend_once(S) if us == 1 else {"status": "NOT-US1", "us": us}
    uni = uni_packets(S)
    rec = {
        "n": S.n, "m": S.m, "s": S.s,
        "M": m_list(S), "V": v_map(S),
        "d": d_list(S),
        "K": S.K, "de": [S.dd, S.e],
        "u": frac_text(S.u),
        "q": frac_text(S.q()),
        "u_s": us,
        "anchor_zero": anchor_zero(S),
        "k_sat": k_sat(S),
        "orbit_sizes": sorted(orbit_sizes(S)),
        "packets": packets_of(S),
        "uni_N": uni,
        "N_ge_6": [p["N"] for p in uni],
        "delta": {str(i): frac_text(S.delta[i]) for i in range(1, S.s + 1)},
        "A": {str(j): S.A(j) for j in range(1, S.s)},
        "screens": screens if screens is not None else screen_bundle(S),
        "descent": desc,
        "appendix2": appendix2_size(desc) if us == 1 else None,
    }
    return rec


# ---------------------------------------------------------------------------
# the 19 rigid assignments (dessin-tower-dim-grok46 §6.4)
# ---------------------------------------------------------------------------
RIGID_SPEC = [
    # n, m, M, V2, (d,e), s, ks, Ns   — V-path recovered from the census
    (60, 40, (-10, 45, 58), 11, (2, 3), 4, (1,), (10,)),
    (80, 60, (68, 78), 7, (3, 4), 3, (1, 2), (7, 14)),
    (84, 63, (49, 82), 7, (3, 4), 3, (1, 2), (7, 14)),
    (96, 72, (-8, 20, 94), 7, (3, 4), 4, (1, 2), (8, 16)),
    (96, 72, (-8, 76, 94), 7, (3, 4), 4, (1, 2), (8, 16)),
    (96, 72, (56, 92, 94), 7, (3, 4), 4, (1, 2), (7, 14)),
    (96, 72, (80, 84, 94), 7, (3, 4), 4, (1, 2), (7, 14)),
    (100, 75, (85, 98), 7, (3, 4), 3, (2,), (7,)),
    (108, 72, (60, 80, 106), 20, (2, 3), 4, (1,), (16,)),
    (108, 72, (60, 100, 106), 20, (2, 3), 4, (1,), (16,)),
    (108, 72, (90, 106), 17, (2, 3), 3, (1,), (17,)),
    (108, 72, (90, 99, 106), 17, (2, 3), 4, (1,), (17,)),
    (120, 72, (12, 44, 118), 8, (3, 5), 4, (1, 2), (10, 20)),
    (120, 72, (12, 76, 118), 8, (3, 5), 4, (1, 2), (10, 20)),
    (120, 90, (-10, 25, 118), 7, (3, 4), 4, (2,), (8,)),
    (120, 90, (-10, 95, 118), 7, (3, 4), 4, (2,), (8,)),
    (120, 90, (100, 105, 118), 7, (3, 4), 4, (2,), (7,)),
    (120, 80, (88, 118), 17, (2, 3), 3, (1, 2), (17, 34)),
    (120, 80, (100, 110, 118), 17, (2, 3), 4, (1, 2), (17, 34)),
]


def recover_rigid():
    """Match each §6.4 line to census V-assignments (Kmin=16, full (1)-(13))."""
    by_n = {}
    ns = sorted({spec[0] for spec in RIGID_SPEC})
    for n in ns:
        by_n[n] = list(M.census(n, Kmin=16, full=True))
    recovered = []
    missing = []
    for spec in RIGID_SPEC:
        n, m, Ms, V2, de, s, ks, Ns = spec
        Ms = tuple(Ms)
        hits = []
        for mm, MM, V in by_n[n]:
            if mm != m or tuple(MM) != Ms:
                continue
            if V.get(2) != V2:
                continue
            S = M.Skel(n, mm, list(MM), V)
            if S.s != s:
                continue
            if (S.dd, S.e) != de:
                continue
            uni = uni_packets(S)
            Ngot = tuple(p["N"] for p in uni)
            kgot = tuple(p["k"] for p in uni)
            hits.append((S, kgot, Ngot))
        if not hits:
            missing.append(spec)
            continue
        # prefer the unique assignment whose UNI N-set contains the printed N
        prefer = [h for h in hits if set(Ns) <= set(h[2])]
        use = prefer or hits
        use.sort(key=lambda h: (abs(k_sat(h[0]) - (max(ks) if ks else 0)),
                                tuple(h[0].V[i] for i in range(2, h[0].s + 1))))
        S, kgot, Ngot = use[0]
        recovered.append({
            "spec": {"n": n, "m": m, "M": list(Ms), "V2": V2, "de": list(de),
                     "s": s, "k_printed": list(ks), "N_printed": list(Ns)},
            "S": S,
            "k_got": list(kgot),
            "N_got": list(Ngot),
            "V": v_map(S),
            "expdim": max(k_sat(S) - 2, 0),
            "n_alt_Vpaths": len(hits),
        })
    return recovered, missing, by_n


# ---------------------------------------------------------------------------
# linear-family construction (keep (d,e) and s; V2, V3 linear)
# ---------------------------------------------------------------------------
def try_skel(n, m, Ms, Vs):
    """Build a Skel and return it if windows+(8)-(13) hold, else None."""
    if n <= 2 or m <= 0 or m >= n:
        return None
    if any(v <= 0 for v in Vs.values()):
        return None
    try:
        S = M.Skel(n, m, list(Ms), dict(Vs))
    except Exception:
        return None
    if S.s != 1 + len(Ms):
        return None
    if not S.windows_ok():
        return None
    if not S.full_ok():
        return None
    return S


def family_member(seed, t, lam, vslopes, windows):
    """(d,e)-fixed linear family.

    n(t)=e*(K0+lam*t), m(t)=d*(K0+lam*t),
    M_i(t)=n(t)-w_i  (i<s), M_s=n-2,
    V_i(t)=V_i0 + slope_i * t  for i=2,3 (others constant unless listed).
    """
    n0, m0, K0 = seed.n, seed.m, seed.K
    d, e = seed.dd, seed.e
    K = K0 + lam * t
    if K < 4 or n0 % K0 or m0 % K0:
        return None
    n = e * K
    m = d * K
    if gcd(d, e) != 1:
        return None
    Ms = []
    for i in range(2, seed.s + 1):
        if i == seed.s:
            Ms.append(n - 2)
        else:
            Ms.append(n - windows[i])
    Vs = dict(v_map(seed))
    for i, sl in vslopes.items():
        Vs[i] = Vs[i] + sl * t
    return try_skel(n, m, Ms, Vs)


def scan_linear_family(seed, t_max=30):
    """Scan small (λ, V2-slope, V3-slope) and report residue behaviour.

    A hit is an arithmetic progression of t on which every node of the
    selected path (and the seed's forced-zero siblings at those nodes)
    has either A|P or P mod A ≤ h, AND the gap-free partition screen
    holds, AND some UNI N≥6 exists.
    """
    windows = {i: seed.n - seed.M[i] for i in range(2, seed.s)}
    windows[seed.s] = 2
    K0 = seed.K
    # λ candidates: keep d3 = gcd(K, w2) from collapsing too often
    w2 = windows.get(2, 1)
    lams = sorted(set(
        [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, w2, K0, 2 * K0]
        + [g for g in range(1, 37) if w2 % g == 0 or K0 % g == 0]
    ))
    lams = [lam for lam in lams if lam > 0][:24]
    slopes = list(itertools.product(range(-2, 3), range(-2, 3)))
    # put (0,0) and small nonzero first
    slopes.sort(key=lambda ab: (abs(ab[0]) + abs(ab[1]), abs(ab[0]), abs(ab[1])))
    reports = []
    hits = []
    t0 = time.time()
    budget = 90.0
    for lam in lams:
        for a, b in slopes:
            if time.time() - t0 > budget:
                break
            vslopes = {2: a}
            if seed.s >= 3:
                vslopes[3] = b
            members = []
            residues = []  # per t, list of (j, A, P, P%A)
            for t in range(0, t_max + 1):
                S = family_member(seed, t, lam, vslopes, windows)
                if S is None:
                    members.append(None)
                    residues.append(None)
                    continue
                T = gap_tree(S)
                path = selected_path(S)
                nodes = []
                ok_cong = True
                for j in range(S.s - 1, 1, -1):
                    nt = node_tuple(T, j, path)
                    nodes.append(nt)
                    if nt["Q_gt_P"] and not nt["A_divides_P"]:
                        # on Q>P, b=0 is the only minor residue
                        ok_cong = False
                    elif (not nt["Q_gt_P"]) and nt["forced_major_zero"]:
                        # still may survive if the zero sibling is feasible;
                        # congruence form of "no forced major zero" fails
                        ok_cong = False
                    path = T.extend(path, j, S.V[j])
                gok = gap_ok(S, ode=False, passport=False)
                gok_pass = gap_ok(S, ode=True, passport=True)
                cok = FT.full_tree_ok(S)
                uni = uni_packets(S)
                members.append({
                    "t": t, "n": S.n, "m": S.m, "M": m_list(S), "V": v_map(S),
                    "K": S.K, "de": [S.dd, S.e],
                    "nodes": nodes,
                    "gap_partition": gok,
                    "gap_passport": gok_pass,
                    "C_FULL_TREE": cok,
                    "uni_N": [p["N"] for p in uni],
                    "cong_ok": ok_cong,
                    "full_ok": True,
                })
                residues.append([(nt["j"], nt["A"], nt["P"], nt["P_mod_A"]) for nt in nodes])
            # analyse eventual residue
            alive_t = [mem["t"] for mem in members if mem and mem["gap_partition"] and mem["uni_N"]]
            cong_t = [mem["t"] for mem in members if mem and mem["cong_ok"] and mem["gap_partition"] and mem["uni_N"]]
            # residue constancy on defined members
            const_nonzero = False
            residue_note = ""
            defined = [(t, residues[t]) for t in range(0, t_max + 1) if residues[t] is not None]
            if defined:
                # per-node sequence of (A, P mod A)
                jset = {item[0] for _, rec in defined for item in rec}
                notes = []
                all_const_nz = True
                any_node = False
                for j in sorted(jset):
                    seq = []
                    for t, rec in defined:
                        hit = [item for item in rec if item[0] == j]
                        if hit:
                            seq.append((t, hit[0][1], hit[0][2], hit[0][3]))
                    if len(seq) < 3:
                        all_const_nz = False
                        continue
                    any_node = True
                    As = {x[1] for x in seq}
                    bs = {x[3] for x in seq}
                    if len(As) == 1 and len(bs) == 1:
                        A0 = next(iter(As))
                        b0 = next(iter(bs))
                        if b0 != 0:
                            notes.append("j=%d: A=%d constant, P mod A = %d ≠ 0 on %d members" %
                                         (j, A0, b0, len(seq)))
                        else:
                            all_const_nz = False
                            notes.append("j=%d: A=%d constant, P mod A = 0 (divides)" % (j, A0))
                    else:
                        all_const_nz = False
                        notes.append("j=%d: A in %s, b in %s" % (j, sorted(As)[:8], sorted(bs)[:8]))
                const_nonzero = any_node and all_const_nz and bool(notes)
                residue_note = "; ".join(notes)
            rec = {
                "lam": lam, "V2_slope": a, "V3_slope": b,
                "n_defined": sum(mem is not None for mem in members),
                "n_gap_N": len(alive_t),
                "n_cong_gap_N": len(cong_t),
                "alive_t": alive_t,
                "cong_t": cong_t,
                "const_nonzero": const_nonzero,
                "residue_note": residue_note,
                "members_brief": [
                    {k: mem[k] for k in ("t", "n", "m", "M", "V", "gap_partition",
                                         "gap_passport", "C_FULL_TREE", "uni_N", "cong_ok")
                     if mem}
                    for mem in members if mem
                ],
            }
            reports.append(rec)
            if len(cong_t) >= 6:
                # check they form an AP
                diffs = {cong_t[i + 1] - cong_t[i] for i in range(len(cong_t) - 1)}
                rec["cong_is_AP"] = (len(diffs) == 1)
                rec["cong_step"] = next(iter(diffs)) if len(diffs) == 1 else None
                hits.append(rec)
                return reports, hits  # first closed-form hit is enough
        if time.time() - t0 > budget:
            break
    return reports, hits


def verify_hit_members(seed, hit, min_n=6):
    """Re-check ≥6 members of a claimed ray with the drivers."""
    windows = {i: seed.n - seed.M[i] for i in range(2, seed.s)}
    lam, a, b = hit["lam"], hit["V2_slope"], hit["V3_slope"]
    vslopes = {2: a}
    if seed.s >= 3:
        vslopes[3] = b
    checked = []
    ts = hit["cong_t"][:12]
    for t in ts:
        S = family_member(seed, t, lam, vslopes, windows)
        if S is None:
            checked.append({"t": t, "ok": False, "why": "not a skeleton"})
            continue
        sb = screen_bundle(S)
        uni = uni_packets(S)
        ok13 = S.full_ok() and S.windows_ok()
        ok = (ok13 and sb["gap_partition"] and sb["gap_ode"] and sb["gap_passport"]
              and uni and min(p["N"] for p in uni) >= 6)
        checked.append({
            "t": t, "n": S.n, "m": S.m, "M": m_list(S), "V": v_map(S),
            "ok13": ok13, "screens": sb, "uni_N": [p["N"] for p in uni],
            "u_s": u_s_of(S), "ok": ok,
        })
    return checked


# ---------------------------------------------------------------------------
# census helpers
# ---------------------------------------------------------------------------
def iter_degree_rows(nlo, nhi, Kmin=16):
    for n in range(nlo, nhi + 1):
        for m, Ms, V in M.census(n, Kmin=Kmin, full=True):
            yield M.Skel(n, m, list(Ms), V)


def group_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    t_all = time.time()
    print("== rigid-congruence-20260903 ==", flush=True)

    # custody
    print("\n-- hashes --", flush=True)
    check("frozen moh_skeleton_full",
          sha256_file(INPUTS / "moh_skeleton_full.py") == CHARGED_SHA["moh_skeleton_full.py"])
    check("frozen full_tree_partition",
          sha256_file(INPUTS / "full_tree_partition.py") == CHARGED_SHA["full_tree_partition.py"])
    check("box copy moh_skeleton_full",
          sha256_file(HERE / "repro" / "moh_skeleton_full.py") == CHARGED_SHA["moh_skeleton_full.py"])
    check("box copy full_tree_partition",
          sha256_file(HERE / "full_tree_partition.py") == CHARGED_SHA["full_tree_partition.py"])
    abort_if_failed("HASH")

    # controls
    print("\n-- CONTROL: Moh's six survive every screen --", flush=True)
    printed_skels = []
    for n, m, Ms, Vs, lab, *_ in M.MOH_TABLE:
        S = M.Skel(n, m, list(Ms), Vs)
        printed_skels.append((lab, S))
        sb = screen_bundle(S)
        check("%s (1)-(13)" % lab, S.full_ok() and S.windows_ok())
        for name in ("gap_partition", "gap_ode", "gap_passport", "C_FULL_TREE", "C_FULL_TREE_ODE"):
            check("%s %s" % (lab, name), sb[name], str(sb))
    abort_if_failed("MOH6")

    print("\n-- CONTROL: unscreened counts --", flush=True)
    t0 = time.time()
    small = [M.Skel(n, m, list(Ms), V)
             for n in range(4, 101)
             for m, Ms, V in M.census(n, Kmin=2, full=True)]
    check("n<=100 (1)-(13) rows = 658", len(small) == 658, str(len(small)))
    check("n<=100 (n,m) classes = 63",
          len({(S.n, S.m) for S in small}) == 63)
    print("   n<=100 census %.2fs" % (time.time() - t0), flush=True)

    print("\n-- CONTROL: gap-free / gapped residue at n<=100 --", flush=True)
    t0 = time.time()
    n100_counts = {
        "gap_partition": 0, "gap_ode": 0, "gap_passport": 0,
        "C_FULL_TREE": 0, "C_FULL_TREE_ODE": 0,
    }
    n100_classes = {k: set() for k in n100_counts}
    for S in small:
        sb = screen_bundle(S)
        for k in n100_counts:
            if sb[k]:
                n100_counts[k] += 1
                n100_classes[k].add((S.n, S.m))
    print("   n<=100 screens %.2fs" % (time.time() - t0), flush=True)
    check("gap_partition n<=100 = 348", n100_counts["gap_partition"] == 348,
          str(n100_counts["gap_partition"]))
    check("gap_partition classes = 52", len(n100_classes["gap_partition"]) == 52,
          str(len(n100_classes["gap_partition"])))
    check("gap_ode n<=100 = 347", n100_counts["gap_ode"] == 347, str(n100_counts["gap_ode"]))
    check("gap_passport n<=100 = 330", n100_counts["gap_passport"] == 330,
          str(n100_counts["gap_passport"]))
    check("C_FULL_TREE n<=100 = 60", n100_counts["C_FULL_TREE"] == 60,
          str(n100_counts["C_FULL_TREE"]))
    check("C_FULL_TREE_ODE n<=100 = 58", n100_counts["C_FULL_TREE_ODE"] == 58,
          str(n100_counts["C_FULL_TREE_ODE"]))
    abort_if_failed("N100-SCREENS")

    print("\n-- CONTROL: D48-200 unscreened + pre-screen u_s>1 --", flush=True)
    t0 = time.time()
    degree_rows = []
    groups = {}
    us_gt1_groups = 0
    us_gt1_rows = 0
    for n in range(48, 201):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            degree_rows.append(S)
            gk = group_key(S)
            groups.setdefault(gk, []).append(S)
            if u_s_of(S) > 1:
                us_gt1_rows += 1
    for gk, items in groups.items():
        if u_s_of(items[0]) > 1:
            us_gt1_groups += 1
    print("   D48-200 census %.2fs  rows=%d groups=%d" %
          (time.time() - t0, len(degree_rows), len(groups)), flush=True)
    check("D48-200 V-assignments = 23720", len(degree_rows) == 23720, str(len(degree_rows)))
    check("D48-200 groups = 14016", len(groups) == 14016, str(len(groups)))
    check("pre-screen u_s>1 groups = 4012/14016", us_gt1_groups == 4012,
          "%d/14016" % us_gt1_groups)
    abort_if_failed("UNSCREENED")

    # ===================================================================
    # (A) rigid ∩ screen
    # ===================================================================
    print("\n== (A) RIGID ∩ SCREEN ==", flush=True)
    recovered, missing, _ = recover_rigid()
    check("19 rigid specs recovered from census",
          len(recovered) == 19 and not missing,
          "got %d missing %s" % (len(recovered), missing))
    abort_if_failed("RIGID-RECOVER")

    rigid_rows = []
    for item in recovered:
        S = item["S"]
        sb = screen_bundle(S)
        rec = row_record(S, screens=sb)
        rec["spec"] = item["spec"]
        rec["expdim_A"] = item["expdim"]
        rec["k_got"] = item["k_got"]
        rec["N_got"] = item["N_got"]
        rec["congruence"] = congruence_dump(S)
        rigid_rows.append(rec)
        print("   n=%d m=%d M=%s V=%s expdim=%d  gapP=%s gapODE=%s gapPASS=%s  TREE=%s ODE=%s  killj=%s" %
              (S.n, S.m, m_list(S), v_map(S), item["expdim"],
               sb["gap_partition"], sb["gap_ode"], sb["gap_passport"],
               sb["C_FULL_TREE"], sb["C_FULL_TREE_ODE"],
               sb["gap_partition_witness_j"]), flush=True)

    rigid_gap = [r for r in rigid_rows if r["screens"]["gap_partition"]]
    rigid_gap_pass = [r for r in rigid_rows if r["screens"]["gap_passport"]]
    rigid_tree = [r for r in rigid_rows if r["screens"]["C_FULL_TREE"]]
    rigid_ode = [r for r in rigid_rows if r["screens"]["C_FULL_TREE_ODE"]]
    print("   rigid survivors: gap_partition %d / gap_passport %d / C_FULL_TREE %d / ODE %d  of 19" %
          (len(rigid_gap), len(rigid_gap_pass), len(rigid_tree), len(rigid_ode)), flush=True)

    # ===================================================================
    # (B) congruence scan at D=108,112,120
    # ===================================================================
    print("\n== (B) CONGRUENCE SCAN D=108,112,120 ==", flush=True)
    scan = {}
    seeds_108 = []
    for D in (108, 112, 120):
        rows = [S for S in degree_rows if S.n == D]
        block = {
            "baseline_rows": len(rows),
            "survivors": {"gap_partition": [], "gap_passport": [],
                          "C_FULL_TREE": [], "C_FULL_TREE_ODE": []},
        }
        for S in rows:
            sb = screen_bundle(S)
            rec = {
                "n": S.n, "m": S.m, "M": m_list(S), "V": v_map(S),
                "s": S.s, "K": S.K, "de": [S.dd, S.e],
                "u_s": u_s_of(S), "anchor_zero": anchor_zero(S),
                "uni_N": [p["N"] for p in uni_packets(S)],
                "screens": sb,
                "congruence": congruence_dump(S),
                "q": frac_text(S.q()),
                "u": frac_text(S.u),
                "orbit_sizes": sorted(orbit_sizes(S)),
                "packets": packets_of(S),
            }
            for k in block["survivors"]:
                if sb[k]:
                    block["survivors"][k].append(rec)
            if D == 108 and sb["gap_partition"] and uni_packets(S):
                seeds_108.append(S)
        scan[str(D)] = {
            "baseline_rows": block["baseline_rows"],
            "counts": {k: len(v) for k, v in block["survivors"].items()},
            "groups": {k: len({(r["n"], r["m"], tuple(r["M"]), r["V"][max(r["V"])])
                               for r in v})
                       for k, v in block["survivors"].items()},
            "uni_alive": {k: len({(r["n"], r["m"], tuple(r["M"]), r["V"][max(r["V"])])
                                  for r in v if r["uni_N"]})
                          for k, v in block["survivors"].items()},
            "survivors": block["survivors"],
        }
        print("   D=%d baseline=%d  gapP=%d gapPASS=%d TREE=%d ODE=%d" %
              (D, block["baseline_rows"],
               scan[str(D)]["counts"]["gap_partition"],
               scan[str(D)]["counts"]["gap_passport"],
               scan[str(D)]["counts"]["C_FULL_TREE"],
               scan[str(D)]["counts"]["C_FULL_TREE_ODE"]), flush=True)

    # expected C_FULL_TREE counts from candidate-results.json
    check("C_FULL_TREE D=108 rows = 21", scan["108"]["counts"]["C_FULL_TREE"] == 21,
          str(scan["108"]["counts"]["C_FULL_TREE"]))
    check("C_FULL_TREE D=112 rows = 8", scan["112"]["counts"]["C_FULL_TREE"] == 8,
          str(scan["112"]["counts"]["C_FULL_TREE"]))
    check("C_FULL_TREE D=120 rows = 94", scan["120"]["counts"]["C_FULL_TREE"] == 94,
          str(scan["120"]["counts"]["C_FULL_TREE"]))
    check("C_FULL_TREE_ODE D=108 rows = 20", scan["108"]["counts"]["C_FULL_TREE_ODE"] == 20,
          str(scan["108"]["counts"]["C_FULL_TREE_ODE"]))
    abort_if_failed("D-SCAN-COUNTS")

    print("\n== (B) LINEAR FAMILY from a D=108 gap-free UNI survivor ==", flush=True)
    # prefer a UNI N>=6 gap-passport survivor, else gap-partition
    seed = None
    for S in seeds_108:
        if gap_ok(S, True, True) and uni_packets(S):
            seed = S
            break
    if seed is None and seeds_108:
        seed = seeds_108[0]
    family_result = None
    if seed is None:
        print("   no D=108 gap-free UNI seed", flush=True)
        family_result = {"status": "NO-SEED"}
    else:
        print("   seed n=%d m=%d M=%s V=%s de=%s s=%d u_s=%d N=%s" %
              (seed.n, seed.m, m_list(seed), v_map(seed), (seed.dd, seed.e),
               seed.s, u_s_of(seed), [p["N"] for p in uni_packets(seed)]),
              flush=True)
        reports, hits = scan_linear_family(seed, t_max=30)
        print("   scanned %d (λ,slope) pairs; hits with ≥6 cong members: %d" %
              (len(reports), len(hits)), flush=True)
        # summarise residue behaviour
        n_const = sum(1 for r in reports if r["const_nonzero"])
        n_alive = sum(1 for r in reports if r["n_gap_N"] >= 1)
        print("   pairs with any gap+N member: %d; constant-nonzero residue: %d" %
              (n_alive, n_const), flush=True)
        verified = []
        if hits:
            verified = verify_hit_members(seed, hits[0])
            print("   verifying first hit λ=%s V2'=%s V3'=%s  t=%s" %
                  (hits[0]["lam"], hits[0]["V2_slope"], hits[0]["V3_slope"],
                   hits[0]["cong_t"][:8]), flush=True)
            for ch in verified:
                print("      t=%s n=%s ok=%s N=%s gapP=%s TREE=%s" %
                      (ch["t"], ch.get("n"), ch["ok"], ch.get("uni_N"),
                       (ch.get("screens") or {}).get("gap_partition"),
                       (ch.get("screens") or {}).get("C_FULL_TREE")), flush=True)
        family_result = {
            "seed": row_record(seed),
            "n_pairs_scanned": len(reports),
            "n_const_nonzero": n_const,
            "n_any_alive": n_alive,
            "hits": hits[:3],
            "verified": verified,
            "pair_summaries": [
                {k: r[k] for k in ("lam", "V2_slope", "V3_slope", "n_defined",
                                   "n_gap_N", "n_cong_gap_N", "alive_t", "cong_t",
                                   "const_nonzero", "residue_note")}
                for r in reports
            ],
        }

    # ===================================================================
    # (C) post-screen u_s>1 and anchor-zero
    # ===================================================================
    print("\n== (C) POST-SCREEN u_s>1 AND ANCHOR-ZERO, 48≤D≤200 ==", flush=True)
    t0 = time.time()
    Cstats = {
        k: {
            "rows": 0, "groups": set(), "us_gt1_rows": 0, "us_gt1_groups": set(),
            "us1_rows": 0, "us1_groups": set(),
            "anchor_zero_us1_rows": 0, "anchor_zero_us1_groups": set(),
            "uni_us1_rows": 0, "uni_us1_anchor_zero": 0,
        }
        for k in ("gap_partition", "gap_ode", "gap_passport", "C_FULL_TREE", "C_FULL_TREE_ODE")
    }
    # H4 identity failures
    h_eq_failures = 0
    h_checked = 0
    for i, S in enumerate(degree_rows):
        sb = screen_bundle(S)
        us = u_s_of(S)
        az = anchor_zero(S)
        gk = group_key(S)
        uni = bool(uni_packets(S))
        # H4 check on selected path at j=2..s-1
        T = gap_tree(S)
        path = T.initial_path()
        # fill selected V into path for radii of higher levels
        path = selected_path(S)
        for j in range(2, S.s):
            try:
                _d, _L, A, P, Q, lo = T.level_data(j, path)
                h_checked += 1
                if Q and F(P, Q) != lo:
                    h_eq_failures += 1
            except Exception:
                pass
        for k, ok in sb.items():
            if k not in Cstats:
                continue
            if not ok:
                continue
            st = Cstats[k]
            st["rows"] += 1
            st["groups"].add(gk)
            if us > 1:
                st["us_gt1_rows"] += 1
                st["us_gt1_groups"].add(gk)
            else:
                st["us1_rows"] += 1
                st["us1_groups"].add(gk)
                if az:
                    st["anchor_zero_us1_rows"] += 1
                    st["anchor_zero_us1_groups"].add(gk)
                if uni:
                    st["uni_us1_rows"] += 1
                    if az:
                        st["uni_us1_anchor_zero"] += 1
        if (i + 1) % 4000 == 0:
            print("   ... %d/%d rows (%.1fs)" % (i + 1, len(degree_rows), time.time() - t0),
                  flush=True)
    print("   (C) wall %.2fs" % (time.time() - t0), flush=True)
    check("H4: h = P/Q identically on selected nodes", h_eq_failures == 0,
          "%d failures / %d checked" % (h_eq_failures, h_checked))

    C_out = {}
    for k, st in Cstats.items():
        C_out[k] = {
            "rows": st["rows"],
            "groups": len(st["groups"]),
            "us_gt1_rows": st["us_gt1_rows"],
            "us_gt1_groups": len(st["us_gt1_groups"]),
            "us1_rows": st["us1_rows"],
            "us1_groups": len(st["us1_groups"]),
            "anchor_zero_us1_rows": st["anchor_zero_us1_rows"],
            "anchor_zero_us1_groups": len(st["anchor_zero_us1_groups"]),
            "uni_us1_rows": st["uni_us1_rows"],
            "uni_us1_anchor_zero_rows": st["uni_us1_anchor_zero"],
            "us_gt1_row_frac": (st["us_gt1_rows"] / st["rows"]) if st["rows"] else None,
            "us_gt1_group_frac": (len(st["us_gt1_groups"]) / len(st["groups"])) if st["groups"] else None,
        }
        print("   %s  rows=%d groups=%d  us>1 rows=%d (%.4f) groups=%d (%.4f)  "
              "us=1 anchor-zero rows=%d groups=%d" %
              (k, C_out[k]["rows"], C_out[k]["groups"],
               C_out[k]["us_gt1_rows"], C_out[k]["us_gt1_row_frac"] or 0,
               C_out[k]["us_gt1_groups"], C_out[k]["us_gt1_group_frac"] or 0,
               C_out[k]["anchor_zero_us1_rows"], C_out[k]["anchor_zero_us1_groups"]),
              flush=True)

    check("C_FULL_TREE D48-200 rows = 3090", C_out["C_FULL_TREE"]["rows"] == 3090,
          str(C_out["C_FULL_TREE"]["rows"]))
    check("C_FULL_TREE D48-200 groups = 1516", C_out["C_FULL_TREE"]["groups"] == 1516,
          str(C_out["C_FULL_TREE"]["groups"]))
    check("C_FULL_TREE_ODE D48-200 rows = 2824", C_out["C_FULL_TREE_ODE"]["rows"] == 2824,
          str(C_out["C_FULL_TREE_ODE"]["rows"]))
    abort_if_failed("C-GAPPED-COUNTS")

    payload = {
        "controls": {
            "n100": n100_counts,
            "n100_classes": {k: len(v) for k, v in n100_classes.items()},
            "degree_rows": len(degree_rows),
            "degree_groups": len(groups),
            "pre_us_gt1_groups": us_gt1_groups,
            "pre_us_gt1_rows": us_gt1_rows,
            "h_eq_failures": h_eq_failures,
            "h_checked": h_checked,
        },
        "rigid": {
            "n": len(rigid_rows),
            "survivors": {
                "gap_partition": len(rigid_gap),
                "gap_passport": len(rigid_gap_pass),
                "C_FULL_TREE": len(rigid_tree),
                "C_FULL_TREE_ODE": len(rigid_ode),
            },
            "rows": [{k: v for k, v in r.items() if k != "congruence"} | {"congruence": r["congruence"]}
                     for r in rigid_rows],
        },
        "scan_108_112_120": {
            D: {
                "baseline_rows": scan[D]["baseline_rows"],
                "counts": scan[D]["counts"],
                "groups": scan[D]["groups"],
                "uni_alive": scan[D]["uni_alive"],
                # keep full survivor dumps; they are the bounded quantity
                "survivors": scan[D]["survivors"],
            }
            for D in scan
        },
        "family": family_result,
        "post_screen": C_out,
        "elapsed_seconds": time.time() - t_all,
        "n_checks": NCHECK[0],
    }

    def _json_default(o):
        if isinstance(o, F):
            return frac_text(o)
        if isinstance(o, Path):
            return str(o)
        raise TypeError(type(o))

    out_path = HERE / "results.json"
    # survivors dumps can be large; keep them, they are the deliverable
    text = json.dumps(payload, indent=2, sort_keys=True, default=_json_default)
    out_path.write_text(text)
    print("\nWrote %s (%d bytes) in %.2fs" % (out_path, len(text.encode()), time.time() - t_all),
          flush=True)
    print("ALL CONTROLS PASSED." if not FAILURES else "FAILURES: %s" % FAILURES, flush=True)
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    raise SystemExit(main())
