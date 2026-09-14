#!/usr/bin/env python3
"""s'=3 monomial-Jacobian compiler: Moh Appendix II extended by Φ_eff.

Closed form, for a general descended datum after Prop 6.3/6.4 and the p.174
drop of a terminal M_h = n-1:

    δ'_i  = (ℓ+1) · Def 5.1(3)(n', M', d', V', s', i)
    B_safe = V'_2 · δ'_1 + u' · δ'_{s'}     u' = K' - V'_2,  K' = gcd(n',m')

At s'=2 this is identical to Moh's Appendix II table (p.207) and to the
charged order_basis_full.closed_form (the ℓ-boundary case).  At s'>=3 the
outer roots of h sit in D'_2,...,D'_{s'}, so B_tight = V'_2 δ'_1 + u' δ'_2
is only a floor of the true order; cutting by it is a strict sub-slice
(FALLACY-v2 / 17(ggggg)).  B_safe is the weakest correct D1 threshold.

The necessary receiver (no two-point leading-form fix, no root-partition
slice, no tot-degree envelope) is:

    h = y^{K'} + sum_{D1, tot<=K', (a,b)!=(0,K')} h_{a,b} x^a y^b
    P = h^{e'} + sum_i α_i h^{e'-i},   Q = h^{q'} + sum_{i>=2} β_i h^{q'-i}
    J(P,Q) = c · x^ℓ,  c ≠ 0.

A class chart is the UNION of the V'-fibre inventories: if that over-
approximation is the unit ideal, every fibre row dies; matching names are
not a theorem (FALLACY-v2 variable/ring map).

Prime marks are labels, never derivatives.  ℓ = v_s - u_s - 1 is the
Prop 6.3(3) exponent (ERRATUM 17(dddddd)).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from math import floor, gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BOX = ROOT / "box"
sys.path.insert(0, str(BOX))
sys.path.insert(0, str(BOX / "orderbasis-20260903"))
sys.path.insert(0, str(BOX / "mohprog-drivers-20260903"))
sys.path.insert(0, str(BOX / "xuscreen-20260903"))
sys.path.insert(0, str(BOX / "lib"))

import sympy as sp

import moh_skeleton_full as MS
import order_basis_full as OB

FAILURES: list[str] = []


def require(name: str, cond: bool, detail: str = "") -> bool:
    if cond:
        print("  [ok]   %s" % name)
        return True
    print("  [FAIL] %s   %s" % (name, detail))
    FAILURES.append(name)
    return False


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def qstr(value: F | int) -> str:
    if isinstance(value, F):
        return str(value.numerator) if value.denominator == 1 else "%s/%s" % (
            value.numerator, value.denominator)
    return str(value)


def jdefault(obj):
    if isinstance(obj, F):
        return qstr(obj)
    if isinstance(obj, Path):
        return str(obj)
    raise TypeError(type(obj))


# ---------------------------------------------------------------------------
# Def 5.1(3), Prop 6.3 descent, p.174 drop, Φ_eff
# ---------------------------------------------------------------------------

def def51(n, M, d, V, s, i):
    """Moh Def 5.1(3) p.179.  M,d,V are 1-indexed dicts.  None if a den vanishes."""
    den0 = n - M[s] - 1
    if den0 == 0:
        return None
    num = F(n - M[i])
    den = F(den0)
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den_j = V[j] * (n - M[j - 1]) - d[j]
        if den_j == 0:
            return None
        den *= den_j
    return 1 - num / den


def descend_once(S: MS.Skel) -> dict | None:
    """Prop 6.3/6.4, u_s = 1 required.  s' = s-1, ℓ = v_s - u_s - 1."""
    ds, vs, s = S.d[S.s], S.V[S.s], S.s
    us = ds - vs
    if us != 1:
        return None
    ell = vs - us - 1
    n2, m2 = S.n * us // ds, S.m * us // ds
    s2 = s - 1
    M2 = {i: S.M[i] * us // ds for i in range(1, s2 + 1)}
    d2 = {i: S.d[i] * us // ds for i in range(1, s2 + 2)}
    V2 = {i: S.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return dict(n=n2, m=m2, s=s2, M=M2, d=d2, V=V2, ell=ell, us=us)


def drop_p174(D: dict) -> dict:
    """Moh p.174 Definition-Remark: drop M_h = n-1 (Jacobian termination)."""
    n, s = D["n"], D["s"]
    M, d, V = dict(D["M"]), dict(D["d"]), dict(D["V"])
    dropped = 0
    while s >= 1 and M.get(s) == n - 1:
        dropped += 1
        s -= 1
        M.pop(s + 1, None)
        V.pop(s + 1, None)
        if s >= 1:
            V[s + 1] = d[s + 1]
    out = dict(D)
    out.update(s=s, M=M, d=d, V=V, dropped=dropped)
    return out


def phi_eff(D: dict) -> dict | None:
    """δ'_i = (ℓ+1) · Def 5.1(3) on the (possibly p.174-truncated) child."""
    out = {}
    for i in range(1, D["s"] + 1):
        raw = def51(D["n"], D["M"], D["d"], D["V"], D["s"], i)
        if raw is None:
            return None
        out[i] = (D["ell"] + 1) * raw
    return out


def closed_form_sprime(D: dict, P: dict) -> dict:
    """Chart constants for a descended datum.  B is B_safe, never B_tight."""
    n, m, s = D["n"], D["m"], D["s"]
    K = gcd(n, m)
    e, q = n // K, m // K
    V2 = D["V"][2]
    u = K - V2
    B_safe = V2 * P[1] + u * P[s]
    B_tight = V2 * P[1] + u * P[2]
    R = n - D["M"][s] - 1
    return dict(
        K=K, e=e, q=q, u=u, V2=V2, R=R, Pi=e + q,
        delta1=P[1], delta2=P[2], delta_s=P[s],
        B=B_safe, B_safe=B_safe, B_tight=B_tight,
        lambda_P=e * B_safe, lambda_Q=q * B_safe,
        two_point=(P[s] == F(-1)),
        s=s, ell=D["ell"], n=n, m=m,
        d3prime=gcd(K, D["M"].get(2, 0)),
    )


# ---------------------------------------------------------------------------
# Necessary D1 inventories (FALLACY-v2: over-approx, not a sub-slice)
# ---------------------------------------------------------------------------

def order_allowed(delta1: F, threshold: F, xpow: int, ypow: int) -> bool:
    return -F(xpow) + delta1 * F(ypow) >= threshold


def h_inventory_necessary(C: dict) -> list[tuple[int, int]]:
    """Free leading form: every D1 monomial except monic y^K.

    No two-point (y-x)^{u'} fix, no slope partition.  deg_x <= max(u',0)
    is the y^{V2} condition on the degree-K face (tot=K and deg_x<=u'
    forces deg_y >= V2).  At s'=2 with δ_2=-1 this is a *superset* of
    Moh's fixed leading form; emptiness of this chart still kills the
    Appendix II chart.  At s'>=3 the two-point fix is not licensed.
    """
    K, u, d1, B = C["K"], max(C["u"], 0), C["delta1"], C["B"]
    out = []
    for ypow in range(K, -1, -1):
        for xpow in range(0, u + 1):
            if xpow + ypow > K:
                continue
            if xpow == 0 and ypow == K:
                continue
            if order_allowed(d1, B, xpow, ypow):
                out.append((xpow, ypow))
    return out


def coeff_inventory_envelope(C: dict, deficit: int) -> list[tuple[int, int]]:
    """17(nnnnn) tot-capped envelope (NOT the Theorem-1.2 floor).

    The extra cut `r + s <= deficit·K` is the 'conservative local finite
    envelope' of order_basis_full.coeff_inventory.  It is not in Moh
    Theorem 1.2.  When max_x_order > deficit·K − s it is a strict
    sub-slice (17(ggggg) / FALLACY-v2 floor/attainment).
    """
    K, d1, B = C["K"], C["delta1"], C["B"]
    th = deficit * B
    out = []
    for ypow in range(K - 1, -1, -1):
        max_x = floor(d1 * ypow - th)
        for xpow in range(0, max_x + 1):
            if xpow + ypow <= deficit * K:
                out.append((xpow, ypow))
    return out


def coeff_inventory_necessary(C: dict, deficit: int) -> list[tuple[int, int]]:
    """Full Theorem-1.2 D1 coefficient space at threshold deficit·B_safe.

    Every monomial x^r y^s with s < K and wt = −r + δ₁'·s >= deficit·B_safe.
    No total-degree cap.  When δ₁' = 0 this is the zero-slope centre-support
    r <= −deficit·B_safe for every centre power s < K (17(nnnnn)).
    """
    K, d1, B = C["K"], C["delta1"], C["B"]
    th = deficit * B
    out = []
    for ypow in range(K - 1, -1, -1):
        max_x = floor(d1 * ypow - th)
        for xpow in range(0, max_x + 1):
            out.append((xpow, ypow))
    return out


def inventory_cokernel(full: list[tuple[int, int]], sub: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Monomials in the full D1 inventory missing from a sub-slice."""
    return sorted(set(map(tuple, full)) - set(map(tuple, sub)),
                  key=lambda t: (-t[1], t[0]))


def apply_gauges(e: int, q: int, alpha: dict, beta: dict):
    """Same shear/translation policy as order_basis_full.full_basis_gauge_audit."""
    am = {i: list(alpha[i]) for i in alpha}
    bm = {i: list(beta[i]) for i in beta}
    shear = e - q
    a_shear = am.get(shear, [])
    scalar = a_shear == [(0, 0)]
    embeds = scalar
    if embeds:
        for deficit, basis in bm.items():
            target = set(map(tuple, am.get(deficit + shear, [])))
            if not set(map(tuple, basis)) <= target:
                embeds = False
                break
    gauges, notes = [], []
    if scalar and embeds:
        am[shear] = []
        gauges.append("P -> P - alpha_%d Q" % shear)
    else:
        notes.append("shear alpha_%d omitted in full monomial basis" % shear)
    if (0, 0) in bm.get(q, []):
        bm[q] = [m for m in bm[q] if m != (0, 0)]
        gauges.append("Q -> Q - const(beta_%d)" % q)
    if (0, 0) in am.get(e, []):
        am[e] = [m for m in am[e] if m != (0, 0)]
        gauges.append("P -> P - const(alpha_%d)" % e)
    return am, bm, gauges, notes, dict(
        shear_index=shear, alpha_shear_dim=len(a_shear),
        alpha_shear_scalar=scalar, shifted_beta_embeds=embeds,
    )


def build_spec(C: dict, h_mons, alpha_mons, beta_mons, row: OB.Row, stem_tag: str) -> dict:
    """Construct the native-builder spec.  Top face = y^K (free leading)."""
    if C["B"] >= 0:
        raise ValueError("B_safe >= 0 is outside this chart's D1 scope")
    x, y = sp.symbols("x y")
    K, e, q = C["K"], C["e"], C["q"]
    am, bm, gauges, notes, audit = apply_gauges(e, q, alpha_mons, beta_mons)
    h = y ** K
    h_params = []
    for a, b in h_mons:
        sym = sp.Symbol("h_%d_%d" % (a, b))
        h_params.append(sym)
        h = h + sym * x ** a * y ** b
    h = sp.expand(h)
    params = list(h_params)
    setup = ["poly h = %s;" % OB.sstr(h)]
    for i in range(1, e + 1):
        expr = sp.Integer(0)
        for a, b in am[i]:
            sym = sp.Symbol("A%d_%d_%d" % (i, a, b))
            params.append(sym)
            expr += sym * x ** a * y ** b
        setup.append("poly AA%d = %s;" % (i, OB.sstr(expr)))
    for i in range(2, q + 1):
        expr = sp.Integer(0)
        for a, b in bm[i]:
            sym = sp.Symbol("B%d_%d_%d" % (i, a, b))
            params.append(sym)
            expr += sym * x ** a * y ** b
        setup.append("poly BB%d = %s;" % (i, OB.sstr(expr)))
    c = sp.Symbol("c")
    params.append(c)
    sat = c
    low_terms = [("1", q)] + [("BB%d" % i, q - i) for i in range(2, q + 1)]
    high_terms = [("1", e)] + [("AA%d" % i, e - i) for i in range(1, e + 1)]
    meta = {
        "row": asdict(row),
        "partition": [],
        "partition_label": stem_tag,
        "chart": "sprime3_full_D1_thm12_nocap",
        "closed_form": {
            "K": C["K"], "e": C["e"], "q": C["q"], "u": C["u"],
            "R": C["R"], "Pi": C["Pi"], "d3prime": C["d3prime"],
            "delta1": qstr(C["delta1"]), "delta2": qstr(C["delta2"]),
            "delta_s": qstr(C["delta_s"]),
            "B": qstr(C["B"]), "B_safe": qstr(C["B_safe"]),
            "B_tight": qstr(C["B_tight"]),
            "lambda_P": qstr(C["lambda_P"]), "lambda_Q": qstr(C["lambda_Q"]),
            "s_prime": C["s"], "ell": C["ell"],
            "two_point": bool(C["two_point"]),
        },
        "top_face_factored": "y^%d" % K,
        "omega": "1",
        "saturation_factor": "c",
        "h_inventory": [list(m) for m in h_mons],
        "h_inventory_count": len(h_mons),
        "h_parameters": [str(p) for p in h_params],
        "alpha_inventories": {str(i): [list(m) for m in am[i]] for i in range(1, e + 1)},
        "beta_inventories": {str(i): [list(m) for m in bm[i]] for i in range(2, q + 1)},
        "alpha_dims": [len(am[i]) for i in range(1, e + 1)],
        "beta_dims": [len(bm[i]) for i in range(2, q + 1)],
        "delta1_zero": C["delta1"] == 0,
        "gauge_audit": audit,
        "gauges": gauges,
        "gauge_notes": notes,
        "params_without_T": len(params),
        "levels_cap": e + q + 2 * K + 12,
        "fallacy_v2": (
            "necessary over-approx: free leading form + B_safe + full "
            "Theorem-1.2 D1 inventory (no tot-degree cap); not a "
            "partition/two-point/envelope sub-slice"
        ),
    }
    return dict(
        meta=meta, setup=setup, params=params, sat=sat,
        low_terms=low_terms, high_terms=high_terms,
    )


def write_builder(spec: dict, stem: str, dest: Path) -> dict:
    rows_path = dest / "rows" / ("%s_rows.tsv" % stem)
    builder_path = dest / "builders" / ("%s_builder.sing" % stem)
    meta_path = dest / "meta" / ("%s.json" % stem)
    for p in (rows_path.parent, builder_path.parent, meta_path.parent):
        p.mkdir(parents=True, exist_ok=True)
    text = OB.native_builder_text(spec, rows_path)
    text = text.replace(str(rows_path.resolve()), "rows/%s_rows.tsv" % stem)
    header = [
        "// s'=3 monomial-Jacobian compiler  box/moh14-charts-20260905",
        "// chart=%s  stem=%s  unknowns=%d  ell=%d" % (
            spec["meta"]["chart"], stem, spec["meta"]["params_without_T"],
            spec["meta"]["row"]["k"]),
        "// B_safe=%s  (necessary receiver; not a sub-slice)" %
        spec["meta"]["closed_form"]["B_safe"],
    ]
    builder_path.write_text("\n".join(header) + "\n" + text, encoding="utf-8")
    payload = {
        "meta": spec["meta"],
        "variables": [str(p) for p in spec["params"]],
        "sat": "c",
        "builder": str(builder_path.relative_to(ROOT)),
        "rows_path": str(rows_path.relative_to(ROOT)),
        "parameter_count": spec["meta"]["params_without_T"],
    }
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=True, default=jdefault) + "\n",
                         encoding="utf-8")
    return payload


def write_fleet_job(dest: Path, stem: str, payload: dict, class_id: str) -> Path:
    """Replayable two-stage job: native builder then guided_gb exact-Q std."""
    job = dest / "jobs" / ("%s_fleet.sh" % stem)
    job.parent.mkdir(parents=True, exist_ok=True)
    body = """#!/bin/bash
# Fleet job for class {class_id} stem {stem}
# parameter_count={pc}
# chart=sprime3_necessary_D1_freelead_Bsafe
# Stage 1 extracts Jacobian coefficient generators (do this anywhere).
# Stage 2 is the exact-Q standard basis (fleet; do NOT run the big std
# on a laptop).  guided_gb markers: GG__UNIT / GG__DIM.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
SINGULAR="${{SINGULAR:-Singular}}"
echo "FLEET_START class={class_id} stem={stem} unknowns={pc}"
"$SINGULAR" --cpus=1 --threads=1 --flint-threads=1 -q --no-rc \\
    "builders/{stem}_builder.sing"
python3 "{compiler}" emit-guided --dest "$HERE" --stem "{stem}"
echo "FLEET_STAGE2 guided job at jobs/{stem}_Q_guided.sing"
echo "FLEET_HINT timeout 3600 $SINGULAR --cpus=1 --threads=1 --flint-threads=1 -q --no-rc jobs/{stem}_Q_guided.sing"
""".format(
        class_id=class_id, stem=stem, pc=payload["parameter_count"],
        compiler=str((HERE / "sprime3_compiler.py").resolve()),
    )
    job.write_text(body, encoding="utf-8")
    os.chmod(job, 0o755)
    return job


def emit_guided(dest: Path, stem: str) -> dict:
    """Turn extracted rows into a guided_gb exact-Q script (no solve)."""
    import guided_gb as GG
    meta_path = dest / "meta" / ("%s.json" % stem)
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    if not rows_path.exists():
        return {"ok": False, "reason": "no rows yet; run the builder first"}
    rows = OB.read_rows(rows_path)
    variables = payload["variables"] + ["T"]
    prelude = "\n".join([
        "// generated by sprime3_compiler.emit_guided",
        "ring R=0,(%s),dp;" % ",".join(variables),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        "ideal CE=c,T*c-1;",
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=c-1,T*c-1;",
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START equations=%d unknowns=%d char=0 algorithm=std");' % (
            len(rows), len(payload["variables"])),
    ]) + "\n"
    generators = [r["expr"] for r in rows] + ["T*c-1"]
    system = GG.SingularSystem(
        name=stem,
        prelude=prelude,
        generators=tuple(generators),
        characteristic=0,
        variables=tuple(variables),
        homogeneous=False,
        metadata={
            "parameter_count": payload["parameter_count"],
            "equations": len(rows),
            "promotion": "EXACT_Q",
            "note": "modular unit ideals are not promoted",
        },
    )
    script = GG.emit_guided_script(system, hint=None, include_perturbed_control=False)
    out = dest / "jobs" / ("%s_Q_guided.sing" % stem)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(script, encoding="utf-8")
    payload["guided_job"] = str(out.relative_to(ROOT))
    payload["equations"] = len(rows)
    payload["rows_bytes"] = rows_path.stat().st_size
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=True, default=jdefault) + "\n",
                         encoding="utf-8")
    return {
        "ok": True, "guided_job": str(out.relative_to(ROOT)),
        "equations": len(rows), "unknowns": payload["parameter_count"],
        "bytes": out.stat().st_size,
    }


# ---------------------------------------------------------------------------
# Enumeration
# ---------------------------------------------------------------------------

APPX2 = [
    ((64, 48, [52, 62], {3: 3, 2: 3}), (16, 12, 13, 3, F(-1), F(1, 4), 1)),
    ((84, 56, [64, 82], {3: 3, 2: 2}), (21, 14, 16, 2, F(-1, 2), F(7, 6), 1)),
    ((84, 56, [72, 82], {3: 3, 2: 5}), (21, 14, 18, 5, F(-1), F(1, 3), 1)),
    ((75, 50, [55, 73], {3: 4, 2: 3}), (15, 10, 11, 3, F(-1), F(1, 2), 2)),
    ((75, 50, [55, 73], {3: 4, 2: 2}), (15, 10, 11, 2, F(-1), F(4, 3), 2)),
]


def is_printed(S: MS.Skel) -> bool:
    Ms_t = tuple(S.M[i] for i in range(2, S.s + 1))
    Vs_d = {i: S.V[i] for i in range(2, S.s + 1)}
    return any(
        S.n == n and S.m == m and Ms_t == tuple(Ms) and Vs_d == Vs
        for (n, m, Ms, Vs, *_rest) in MS.MOH_TABLE
    )


def pack_row(S: MS.Skel, xu: dict) -> dict:
    D0 = descend_once(S)
    D = drop_p174(D0)
    P = phi_eff(D)
    C = closed_form_sprime(D, P)
    h = h_inventory_necessary(C)
    alpha = {i: coeff_inventory_necessary(C, i) for i in range(1, C["e"] + 1)}
    beta = {i: coeff_inventory_necessary(C, i) for i in range(2, C["q"] + 1)}
    am, bm, gauges, notes, audit = apply_gauges(C["e"], C["q"], alpha, beta)
    nunk = len(h) + sum(len(v) for v in am.values()) + sum(len(v) for v in bm.values()) + 1
    a_env = {i: coeff_inventory_envelope(C, i) for i in range(1, C["e"] + 1)}
    b_env = {i: coeff_inventory_envelope(C, i) for i in range(2, C["q"] + 1)}
    a_coker = {i: inventory_cokernel(alpha[i], a_env[i]) for i in alpha}
    b_coker = {i: inventory_cokernel(beta[i], b_env[i]) for i in beta}
    Mp = tuple(D["M"][i] for i in range(2, D["s"] + 1))
    return dict(
        src_n=S.n, src_m=S.m,
        src_M=[S.M[i] for i in range(2, S.s + 1)],
        src_V={i: S.V[i] for i in range(2, S.s + 1)},
        src_s=S.s, src_ds=S.d[S.s], src_vs=S.V[S.s], src_us=D0["us"],
        n=D["n"], m=D["m"], s=D["s"], ell=D["ell"], dropped=D["dropped"],
        M={i: D["M"][i] for i in D["M"]},
        d={i: D["d"][i] for i in D["d"]},
        V={i: D["V"][i] for i in D["V"]},
        delta={i: P[i] for i in P},
        C=C, h=h, alpha=alpha, beta=beta,
        alpha_g=am, beta_g=bm, gauges=gauges, nunk=nunk,
        envelope_cokernel={
            "delta1_zero": C["delta1"] == 0,
            "alpha_omitted": {str(i): [list(m) for m in a_coker[i]] for i in a_coker},
            "beta_omitted": {str(i): [list(m) for m in b_coker[i]] for i in b_coker},
            "alpha_coker_dim": {str(i): len(a_coker[i]) for i in a_coker},
            "beta_coker_dim": {str(i): len(b_coker[i]) for i in b_coker},
            "total_coker": sum(len(v) for v in a_coker.values()) + sum(len(v) for v in b_coker.values()),
            "shear": audit,
        },
        class_key=(D["n"], D["m"], Mp, D["ell"], D["s"]),
        xu_ok=xu["xu_ok"], IM_max=xu["IM_max"], Im_min=xu["Im_min"],
    )


def enumerate_12() -> dict:
    import full_tree_partition as FT
    from xu_screen import XuBounder

    t0 = time.time()
    printed, excess = [], []
    n_raw = 0
    for n in range(4, 101):
        for (m, Ms, V) in MS.census(n, Kmin=2, full=True):
            n_raw += 1
            S = MS.Skel(n, m, list(Ms), V)
            if not FT.full_tree_polynomial_ode_ok(S):
                continue
            (printed if is_printed(S) else excess).append(S)
    xu_dead, xu_live = [], []
    for S in excess:
        rec = XuBounder(S).row_bound()
        packed = pack_row(S, rec)
        (xu_live if rec["xu_ok"] else xu_dead).append(packed)
    classes = defaultdict(list)
    for r in xu_live:
        classes[r["class_key"]].append(r)
    return dict(
        n_raw=n_raw, n_poly=len(printed) + len(excess),
        n_printed=len(printed), n_excess=len(excess),
        n_xu_dead=len(xu_dead), n_live=len(xu_live),
        xu_dead=xu_dead, live=xu_live, classes=dict(classes),
        sec=round(time.time() - t0, 3),
    )


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------

def control_appendix2() -> None:
    print("\n== CONTROL A: Φ_eff reproduces Moh Appendix II p.207 (5/5) ==")
    for (sk, want) in APPX2:
        S = MS.Skel(*sk)
        D = drop_p174(descend_once(S))
        P = phi_eff(D)
        got = (D["n"], D["m"], D["M"][D["s"]], D["V"][2], P[2], P[1], D["ell"])
        require("Appendix II (%d,%d) V2=%d" % (sk[0], sk[1], sk[3][2]),
                got == want, str(got))
        require("p.174 drop is a no-op on (%d,%d)" % (sk[0], sk[1]),
                D["dropped"] == 0)
        C = closed_form_sprime(D, P)
        require("s'=2 => B_safe == B_tight on (%d,%d)" % (sk[0], sk[1]),
                C["B_safe"] == C["B_tight"])


def control_charged_closed_form() -> None:
    print("\n== CONTROL A2: Φ_eff == order_basis_full.closed_form on s'=2 ==")
    for key, want in (("k16a", (F(-1), F(1, 4))), ("banked", (F(-1), F(1, 2)))):
        C = OB.closed_form(OB.ROWS[key])
        require("charged closed_form %s" % OB.ROWS[key].label,
                (C["delta2"], C["delta1"]) == want)
    # reconstruct Φ_eff from the Row fields through a synthetic s'=2 datum
    for key in ("k16a", "banked", "k16b", "2515", "d108"):
        row = OB.ROWS[key]
        K = gcd(row.n, row.m)
        M = {1: -row.m, 2: row.M2}
        d = {1: row.n, 2: K, 3: gcd(K, row.M2)}
        V = {2: row.V2, 3: d[3]}
        D = dict(n=row.n, m=row.m, s=2, M=M, d=d, V=V, ell=row.k, us=1, dropped=0)
        P = phi_eff(D)
        Cch = OB.closed_form(row)
        require("Φ_eff delta == charged on %s" % row.label,
                P[1] == Cch["delta1"] and P[2] == Cch["delta2"],
                "%s vs %s,%s" % (P, Cch["delta1"], Cch["delta2"]))
        C = closed_form_sprime(D, P)
        require("B_safe == charged B on %s" % row.label, C["B"] == Cch["B"])


def control_s2_identity() -> None:
    """Algebraic specialisation: s'=2 Φ_eff equals the printed closed form."""
    print("\n== CONTROL A3: s'=2 algebraic identity (ℓ-boundary) ==")
    n, m, M2, V2, k = 16, 12, 13, 3, 1
    K = gcd(n, m)
    e, q = n // K, m // K
    u = K - V2
    R = n - M2 - 1
    Pi = e + q
    D = dict(n=n, m=m, s=2, M={1: -m, 2: M2},
             d={1: n, 2: K, 3: gcd(K, M2)},
             V={2: V2, 3: gcd(K, M2)}, ell=k, us=1)
    P = phi_eff(D)
    d2 = -F(k + 1, R)
    d1 = F((k + 1) * (Pi * u - R), R * (Pi * V2 - 1))
    require("s'=2 closed-form delta2", P[2] == d2, "%s vs %s" % (P[2], d2))
    require("s'=2 closed-form delta1", P[1] == d1, "%s vs %s" % (P[1], d1))


# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------

CLASS_ORDER = []  # filled at emit time


def class_id_of(key) -> str:
    n, m, Mp, ell, s = key
    mtag = "_".join(("m%d" % abs(x) if x < 0 else str(x) for x in Mp))
    return "C_n%dm%d_M%s_ell%d_s%d" % (n, m, mtag, ell, s)


def serial_row(r: dict) -> dict:
    C = r["C"]
    return dict(
        src=(r["src_n"], r["src_m"], r["src_M"], r["src_V"]),
        src_s=r["src_s"], u_s=r["src_us"], v_s=r["src_vs"], d_s=r["src_ds"],
        n_prime=r["n"], m_prime=r["m"], s_prime=r["s"], ell=r["ell"],
        dropped_p174=r["dropped"],
        M_prime=r["M"], d_prime=r["d"], V_prime=r["V"],
        delta_prime={str(i): qstr(r["delta"][i]) for i in r["delta"]},
        K=C["K"], e=C["e"], q=C["q"], u=C["u"], V2=C["V2"],
        B_safe=qstr(C["B_safe"]), B_tight=qstr(C["B_tight"]),
        nunk=r["nunk"], h_count=len(r["h"]),
        alpha_dims=[len(r["alpha_g"][i]) for i in sorted(r["alpha_g"])],
        beta_dims=[len(r["beta_g"][i]) for i in sorted(r["beta_g"])],
        envelope_coker_total=r["envelope_cokernel"]["total_coker"],
        delta1_zero=r["envelope_cokernel"]["delta1_zero"],
        shear_scalar=r["envelope_cokernel"]["shear"]["alpha_shear_scalar"],
        xu_ok=r["xu_ok"], IM_max=qstr(r["IM_max"]), Im_min=qstr(r["Im_min"]),
    )


def union_inv(rows: list[dict]):
    Hu, Au, Bu = set(), defaultdict(set), defaultdict(set)
    for r in rows:
        Hu.update(r["h"])
        for i, mons in r["alpha"].items():
            Au[i].update(mons)
        for i, mons in r["beta"].items():
            Bu[i].update(mons)
    # stable order: y desc, x asc
    def sord(ms):
        return sorted(ms, key=lambda t: (-t[1], t[0]))
    h = sord(Hu)
    alpha = {i: sord(Au[i]) for i in sorted(Au)}
    beta = {i: sord(Bu[i]) for i in sorted(Bu)}
    return h, alpha, beta


def emit_all(enum: dict) -> dict:
    manifest = []
    class_dir_root = HERE / "classes"
    class_dir_root.mkdir(parents=True, exist_ok=True)
    # dominating C for union: most negative B_safe (weakest cutoff) together
    # with the explicit monomial union (not a representative slice).
    for key in sorted(enum["classes"]):
        rows = enum["classes"][key]
        cid = class_id_of(key)
        dest = class_dir_root / cid
        dest.mkdir(parents=True, exist_ok=True)
        hU, aU, bU = union_inv(rows)
        # C_union uses min B_safe and max u so native_builder meta is honest;
        # inventories themselves are the union, not this C's own inventory.
        C_dom = min((r["C"] for r in rows), key=lambda C: C["B_safe"])
        C_u = max(r["C"]["u"] for r in rows)
        C_union = dict(C_dom)
        C_union["u"] = C_u
        nunkU = (len(hU) + sum(len(v) for v in aU.values())
                 + sum(len(v) for v in bU.values()) + 1)
        n, m, Mp, ell, s = key
        row_ob = OB.Row(
            key=cid + "_union", label="%s union" % cid,
            n=n, m=m, M2=Mp[-1], V2=min(r["C"]["V2"] for r in rows), k=ell,
        )
        specU = build_spec(C_union, hU, aU, bU, row_ob, "freelead_union")
        payU = write_builder(specU, cid + "_union", dest)
        jobU = write_fleet_job(dest, cid + "_union", payU, cid)
        per_row = []
        for r in rows:
            vtag = "_".join(str(r["V"][i]) for i in range(2, r["s"] + 1))
            stem = "%s_V%s" % (cid, vtag)
            rob = OB.Row(
                key=stem, label="%s V'=%s" % (cid, vtag),
                n=r["n"], m=r["m"], M2=r["M"][r["s"]], V2=r["C"]["V2"], k=r["ell"],
            )
            spec = build_spec(r["C"], r["h"], r["alpha"], r["beta"], rob, "freelead")
            pay = write_builder(spec, stem, dest)
            write_fleet_job(dest, stem, pay, cid)
            per_row.append(dict(stem=stem, **serial_row(r),
                                parameter_count=pay["parameter_count"],
                                builder=pay["builder"]))
        class_json = dict(
            class_id=cid,
            n_prime=n, m_prime=m, M_prime=list(Mp), ell=ell, s_prime=s,
            fibre_size=len(rows),
            union_parameter_count=nunkU,
            union_h_count=len(hU),
            union_alpha_dims=[len(aU[i]) for i in sorted(aU)],
            union_beta_dims=[len(bU[i]) for i in sorted(bU)],
            union_B_safe=qstr(C_union["B_safe"]),
            union_builder=payU["builder"],
            union_fleet_job=str(jobU.relative_to(ROOT)),
            chart="full_D1_thm12_nocap_class_union",
            not_a_subslice=True,
            fallacy_v2=(
                "class chart = union of V'-fibre full Theorem-1.2 D1 "
                "inventories (no tot-degree cap); a representative row "
                "is not FULL_ACTUAL"
            ),
            rows=per_row,
        )
        (dest / "class.json").write_text(
            json.dumps(class_json, indent=2, sort_keys=True, default=jdefault) + "\n",
            encoding="utf-8")
        manifest.append(class_json)
        print("  EMIT %s  union_unk=%d  fibre=%d  dest=%s" % (
            cid, nunkU, len(rows), dest.relative_to(ROOT)))
    (HERE / "classes_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True, default=jdefault) + "\n",
        encoding="utf-8")
    return dict(n_classes=len(manifest), classes=manifest)


def write_enumerate_json(enum: dict) -> None:
    dead = []
    for r in enum["xu_dead"]:
        dead.append(dict(
            src=(r["src_n"], r["src_m"], r["src_M"], r["src_V"]),
            IM_max=qstr(r["IM_max"]), Im_min=qstr(r["Im_min"]),
            reason="XU IM_max < Im_min (Cor 5.3, promoted screen)",
        ))
    live = [serial_row(r) for r in enum["live"]]
    payload = dict(
        n_raw_1_13=enum["n_raw"], poly_ode=enum["n_poly"],
        printed=enum["n_printed"], excess=enum["n_excess"],
        xu_dead_count=enum["n_xu_dead"], live_count=enum["n_live"],
        xu_deaths=dead, live=live, sec=enum["sec"],
        s_prime_of_live={
            str(s): sum(1 for r in enum["live"] if r["s"] == s)
            for s in sorted(set(r["s"] for r in enum["live"]))
        },
        p174_dropped=sum(r["dropped"] for r in enum["live"]),
    )
    (HERE / "enumerate.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=jdefault) + "\n",
        encoding="utf-8")


def tiny_guided_sanity() -> dict:
    """A 2-unknown Jacobian toy: J=c forces c=0 after saturation? No.

    Positive control of the guided_gb wrapper: <x, T*c-1> is nonempty;
    <c, T*c-1> is the unit ideal.  This is the omitted-row shape, not a
    Moh chart.
    """
    import guided_gb as GG
    dest = HERE / "controls"
    dest.mkdir(parents=True, exist_ok=True)
    prelude = 'ring R=0,(c,T),dp;\noption(redSB);\n'
    unit = GG.SingularSystem(
        name="sanity_unit", prelude=prelude,
        generators=("c", "T*c-1"), characteristic=0,
        variables=("c", "T"),
    )
    live = GG.SingularSystem(
        name="sanity_live", prelude=prelude,
        generators=("c-1", "T*c-1"), characteristic=0,
        variables=("c", "T"),
    )
    results = {}
    for sys, expect_unit in ((unit, True), (live, False)):
        script = GG.emit_guided_script(sys, hint=None, include_perturbed_control=False)
        path = dest / ("%s.sing" % sys.name)
        path.write_text(script, encoding="utf-8")
        env = os.environ.copy()
        for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                  "NUMEXPR_NUM_THREADS"):
            env[k] = "1"
        t0 = time.monotonic()
        import subprocess
        proc = subprocess.run(
            ["timeout", "30", "Singular", "--cpus=1", "--threads=1",
             "--flint-threads=1", "-q", "--no-rc", str(path)],
            cwd=str(ROOT), env=env, text=True, capture_output=True,
        )
        out = proc.stdout or ""
        (path.with_suffix(".out")).write_text(out, encoding="utf-8")
        unit_flag = "GG__UNIT main 1" in out or 'GG__UNIT main 1' in out
        # marker is: print("GG__UNIT main "+string(GG_UNIT_main));
        unit_hit = False
        for line in out.splitlines():
            if line.startswith("GG__UNIT main "):
                unit_hit = line.strip().endswith("1")
        results[sys.name] = dict(
            expect_unit=expect_unit, unit=unit_hit,
            rc=proc.returncode, sec=round(time.monotonic() - t0, 3),
            ok=(unit_hit == expect_unit and proc.returncode == 0),
        )
        require("guided_gb sanity %s (unit=%s)" % (sys.name, expect_unit),
                results[sys.name]["ok"], str(results[sys.name]))
    return results


def run_builder(dest: Path, stem: str, timeout: int = 180) -> dict:
    builder = dest / "builders" / ("%s_builder.sing" % stem)
    env = os.environ.copy()
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
              "NUMEXPR_NUM_THREADS"):
        env[k] = "1"
    import subprocess
    t0 = time.monotonic()
    proc = subprocess.run(
        ["timeout", str(timeout), "Singular", "--cpus=1", "--threads=1",
         "--flint-threads=1", "-q", "--no-rc", str(builder)],
        cwd=str(dest), env=env, text=True, capture_output=True,
    )
    out = proc.stdout or ""
    err = proc.stderr or ""
    Path(str(builder) + ".out").write_text(out, encoding="utf-8")
    Path(str(builder) + ".err").write_text(err, encoding="utf-8")
    gate = {}
    for line in out.splitlines():
        if "NATIVE_" in line:
            print("   ", line)
            if "=" in line:
                _, rest = line.split(" ", 1)
                k, _, v = rest.partition("=")
                try:
                    gate[k] = int(v)
                except ValueError:
                    gate[k] = v
    rows = dest / "rows" / ("%s_rows.tsv" % stem)
    return dict(
        rc=proc.returncode, sec=round(time.monotonic() - t0, 3),
        timed_out=(proc.returncode == 124),
        gate=gate, rows_exists=rows.exists(),
        rows_bytes=(rows.stat().st_size if rows.exists() else 0),
        stdout_tail=out.splitlines()[-15:],
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="all",
                    choices=("all", "enumerate", "validate", "emit",
                             "emit-guided", "sanity", "run-small"))
    ap.add_argument("--dest", type=str, default="")
    ap.add_argument("--stem", type=str, default="")
    a = ap.parse_args()

    print("sprime3_compiler -- Moh Appendix II extended by Φ_eff")
    print("=" * 72)
    print("frozen skeleton sha256", sha256_file(BOX / "moh_skeleton_full.py"))

    if a.mode == "emit-guided":
        dest = Path(a.dest)
        info = emit_guided(dest, a.stem)
        print(json.dumps(info, indent=2, default=jdefault))
        return 0 if info.get("ok") else 2

    if a.mode in ("all", "validate"):
        control_appendix2()
        control_charged_closed_form()
        control_s2_identity()

    enum = None
    if a.mode in ("all", "enumerate", "emit", "run-small"):
        print("\n== enumerate POLY_ODE n<=100, then Xu screen ==")
        enum = enumerate_12()
        print("  raw (1)-(13) %d  POLY_ODE %d  printed %d  excess %d  Xu-dead %d  live %d  [%.2fs]"
              % (enum["n_raw"], enum["n_poly"], enum["n_printed"], enum["n_excess"],
                 enum["n_xu_dead"], enum["n_live"], enum["sec"]))
        require("POLY_ODE survivors = 20", enum["n_poly"] == 20, str(enum["n_poly"]))
        require("printed kept = 6", enum["n_printed"] == 6)
        require("excess = 14", enum["n_excess"] == 14)
        require("Xu deaths = 2", enum["n_xu_dead"] == 2, str(enum["n_xu_dead"]))
        require("live = 12", enum["n_live"] == 12)
        require("classes = 6", len(enum["classes"]) == 6, str(len(enum["classes"])))
        print("  Xu deaths:")
        for r in enum["xu_dead"]:
            print("    (%d,%d) M=%s V=%s  IM=%s < Im=%s" % (
                r["src_n"], r["src_m"], r["src_M"], r["src_V"],
                qstr(r["IM_max"]), qstr(r["Im_min"])))
            require("Xu death is the (90,60) M=(45,80,88) class",
                    r["src_n"] == 90 and r["src_m"] == 60 and r["src_M"] == [45, 80, 88])
        print("  live s' dist", {s: sum(1 for r in enum["live"] if r["s"] == s)
                                 for s in sorted(set(x["s"] for x in enum["live"]))})
        require("p.174 drop is a no-op on all 12",
                all(r["dropped"] == 0 for r in enum["live"]))
        require("B_safe < 0 on all 12",
                all(r["C"]["B_safe"] < 0 for r in enum["live"]))
        require("u_s = 1 on all 12",
                all(r["src_us"] == 1 for r in enum["live"]))
        write_enumerate_json(enum)

    if a.mode in ("all", "emit") and enum is not None:
        print("\n== emit 6 class charts + V' fallbacks ==")
        emit_all(enum)

    if a.mode in ("all", "sanity"):
        print("\n== tiny guided_gb sanity (not a Moh chart) ==")
        tiny_guided_sanity()

    if a.mode in ("all", "run-small") and enum is not None:
        # Smallest class union: the s'=4 singleton, 79 unknowns.  Extract
        # generators only.  A full std of this size timed out previously
        # (moh14-20260905 row 5, 76 unk / 500 gens / 52 MB).
        print("\n== run smallest class builder (extract generators, no big std) ==")
        smallest = min(
            ((class_id_of(k), k, enum["classes"][k]) for k in enum["classes"]),
            key=lambda t: min(r["nunk"] for r in t[2]),
        )
        cid, key, rows = smallest
        dest = HERE / "classes" / cid
        stem = cid + "_union"
        print("  smallest class %s  union builder %s" % (cid, stem))
        br = run_builder(dest, stem, timeout=180)
        print("  BUILD rc=%s wall=%.1fs rows_bytes=%d gate=%s" % (
            br["rc"], br["sec"], br["rows_bytes"], br["gate"]))
        (HERE / "small_builder.json").write_text(
            json.dumps(dict(class_id=cid, stem=stem, **br), indent=2, default=jdefault) + "\n",
            encoding="utf-8")
        if br["rows_exists"] and br["rc"] == 0:
            info = emit_guided(dest, stem)
            print("  GUIDED", info)
            require("native gate target_xk present",
                    br["gate"].get("target_xk_level0_nonzero") == 1,
                    str(br["gate"]))
        else:
            print("  builder did not emit rows; fleet will extract")

    print("\n" + "=" * 72)
    if FAILURES:
        print("CONTROLS FAILED (%d): %s" % (len(FAILURES), FAILURES))
        return 1
    print("ALL CONTROLS PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
