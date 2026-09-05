#!/usr/bin/env python3
"""Instant identity + target-table controls (no chart build).

(1) pole_coeff == table.get at every n other than the leading power.
(2) target tables match the gate/rekill faces, including the constant 1
    at the top monomial (the 1=0 the old emission would have written if
    that k were tagged; it is not, but k=0 of the same polynomial is).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
BOX = HERE.parent
sys.path.insert(0, str(HERE))
import leading_pole as LP
import importlib.util

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

sys.path.insert(0, str(BOX / "d108-rekill-20260905" / "work"))
sys.path.insert(0, str(BOX / "g9966band-20260903"))
sys.path.insert(0, str(BOX / "g9966-repair-gate-20260905"))
sys.path.insert(0, str(BOX / "g108gate-20260903"))
RE = load("rekill_engine", BOX / "d108-rekill-20260905" / "work" / "rekill_engine.py")
BE = load("g9966band_engine", BOX / "g9966band-20260903" / "band_engine.py")
CFE = load("cfe", BOX / "g9966-repair-gate-20260905" / "corrected_face_engine.py")
G108GATE = load("g108gate_engine", BOX / "g108gate-20260903" / "band_engine.py")

pi, c, zeta, rho = sp.symbols("pi c zeta rho")
out = {}

# Dummy table with a sentinel so identity is a real equality, not 0==0.
sentinel = sp.Symbol("SENTINEL")
dummy = {(n, k): sentinel for n in range(0, 200) for k in range(0, 30)}

def ident_d108(eng, label):
    bad = []
    for name in ("F", "G"):
        lead = eng.leading_pole_power(name)
        for n in list(eng.raw_minor_support(name, False)) + [lead]:
            for k in eng.raw_minor_support(name, False).get(n, range(5)):
                got = eng.pole_coeff(dummy, n, k, name)
                expect = dummy[(n, k)] if n != lead else sp.expand(
                    dummy[(n, k)] - eng.leading_pole_target_table(name).get(k, 0)
                )
                if sp.expand(got - expect) != 0:
                    bad.append((name, n, k, str(got), str(expect)))
    # Shared helper agrees with the engine copy.
    for name in ("F", "G"):
        assert eng.leading_pole_power(name) == LP.d108_lead_n(name)
        assert eng.leading_pole_target_table(name) == LP.d108_target_table(name)
    tgtF = eng.leading_pole_target_table("F")
    tgtG = eng.leading_pole_target_table("G")
    return {
        "engine": label,
        "identity_failures": bad,
        "identity_ok": not bad,
        "F_lead_n": eng.leading_pole_power("F"),
        "G_lead_n": eng.leading_pole_power("G"),
        "F_pi24": str(tgtF.get(24, 0)),
        "F_pi0": str(tgtF.get(0, 0)),
        "G_pi16": str(tgtG.get(16, 0)),
        "G_pi0": str(tgtG.get(0, 0)),
        "F_pi24_is_1": tgtF.get(24, 0) == 1,
        "G_pi16_is_1": tgtG.get(16, 0) == 1,
        "F_pi0_is_c12": sp.expand(tgtF.get(0, 0) - c**12) == 0,
        "G_pi0_is_c8": sp.expand(tgtG.get(0, 0) - c**8) == 0,
        "F_poly_is_p12": sp.expand(
            sum(cf * pi**k for k, cf in tgtF.items()) - (pi**2 - c)**12
        ) == 0,
        "support_F96_kmax": max(eng.raw_minor_support("F", False)[96]),
        "support_G64_kmax": max(eng.raw_minor_support("G", False)[64]),
        "top_monomial_not_tagged_F": 24 not in eng.raw_minor_support("F", False)[96],
        "top_monomial_not_tagged_G": 16 not in eng.raw_minor_support("G", False)[64],
        "k0_IS_tagged_F96": 0 in eng.raw_minor_support("F", False)[96],
        "k0_IS_tagged_G64": 0 in eng.raw_minor_support("G", False)[64],
        "stage_F_leading": 96 - 4,
        "stage_G_leading": 64 - 4,
    }

out["rekill"] = ident_d108(RE, "rekill_engine")

out["g108gate"] = {
    "F_lead": G108GATE.leading_pole_power("F"),
    "G_lead": G108GATE.leading_pole_power("G"),
    "F_pi24": str(G108GATE.leading_pole_target_table("F")[24]),
    "identity_below": all(
        G108GATE.pole_coeff(dummy, n, 0, "F") == dummy[(n, 0)]
        for n in range(1, 96)
    ),
    "leading_targets_doc": G108GATE.continuation_schedule()["pole_rows"]["leading_targets"],
}

def ident_g9966(eng, label):
    bad = []
    for branch in ("delta2", "delta52"):
        for name in ("F", "G"):
            lead = eng.leading_pole_power(branch, name)
            tags = eng.raw_minor_support(branch, name)
            for n in list(tags):
                for k in tags.get(n, ()):
                    got = eng.pole_coeff(dummy, n, k, branch, name)
                    expect = dummy[(n, k)] if n != lead else sp.expand(
                        dummy[(n, k)] - eng.leading_pole_target_table(branch, name).get(k, 0)
                    )
                    if sp.expand(got - expect) != 0:
                        bad.append((branch, name, n, k))
            assert eng.leading_pole_power(branch, name) == LP.g9966_lead_n(branch, name)
            assert eng.leading_pole_target_table(branch, name) == LP.g9966_target_table(branch, name)
    face2 = zeta**2 * (zeta + 3 * rho)
    tgtF = eng.leading_pole_target_table("delta2", "F")
    tgtG = eng.leading_pole_target_table("delta2", "G")
    return {
        "engine": label,
        "identity_failures": bad,
        "identity_ok": not bad,
        "delta2_F_lead": eng.leading_pole_power("delta2", "F"),
        "delta2_G_lead": eng.leading_pole_power("delta2", "G"),
        "delta2_F_zeta27": str(tgtF.get(27, 0)),
        "delta2_G_zeta18": str(tgtG.get(18, 0)),
        "delta2_F_poly": sp.expand(
            sum(cf * zeta**k for k, cf in tgtF.items()) - face2**9
        ) == 0,
        "delta2_G_poly": sp.expand(
            sum(cf * zeta**k for k, cf in tgtG.items()) - face2**6
        ) == 0,
        "delta2_F81_kmax": max(eng.raw_minor_support("delta2", "F")[81]),
        "delta2_G54_kmax": max(eng.raw_minor_support("delta2", "G")[54]),
        "top_not_tagged_F": 27 not in eng.raw_minor_support("delta2", "F")[81],
        "top_not_tagged_G": 18 not in eng.raw_minor_support("delta2", "G")[54],
        "k0_tagged_F81": 0 in eng.raw_minor_support("delta2", "F")[81],
        "stage_F_leading": 81 - 4,
        "stage_G_leading": 54 - 4,
    }

out["g9966band"] = ident_g9966(BE, "g9966band")
out["corrected_face"] = ident_g9966(CFE, "corrected_face_engine")

(HERE / "ctl_identity.json").write_text(json.dumps(out, indent=2, default=str) + "\n")
ok = (
    out["rekill"]["identity_ok"]
    and out["g9966band"]["identity_ok"]
    and out["corrected_face"]["identity_ok"]
    and out["rekill"]["F_pi24_is_1"]
    and out["rekill"]["k0_IS_tagged_F96"]
    and out["g108gate"]["identity_below"]
)
print(json.dumps({k: {kk: vv for kk, vv in rec.items() if kk != "identity_failures"}
                  if isinstance(rec, dict) else rec
                  for k, rec in out.items()}, indent=2, default=str))
print("IDENTITY_OK" if ok else "IDENTITY_FAIL")
sys.exit(0 if ok else 1)
