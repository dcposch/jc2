#!/usr/bin/env python3
"""Emit the proved G_i-only Moh residual charts.

The charged source-support theorem gives, in the coordinate
``phi=(x,y+eta(x))``, the class-uniform inventories

    G_i = {(b,a): 0 <= a < K, 0 <= b <= floor(d*(i*K-a))}.

This driver deliberately does not retain the decorative D1 coordinates.  It
uses the charged compiler for inventory/gauge/spec construction and the
charged ``builder_fix`` for a polynomial ring

    Q[y,x,parameters,c], (lp(1),dp(...)).

There is one executable chart per class and one alias/specialization receipt
per fibre.  The native compiler historically put Q first and hence extracted
J(Q,P).  Here the two h-adic term lists are intentionally swapped before
calling ``native_builder_text``; emitted rows are literally the coefficients
of J(P,Q)-c*x^ell.  ``emit-guided`` appends T*c-1.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import sys
from fractions import Fraction as F
from math import floor, gcd
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
HSGATE = ROOT / "box/moh14-charts-20260905/hsupport-gate-20260905"
SOURCE = HSGATE / "source-complete"
DEFAULT_FROZEN = Path("/tmp/jc2-lane.ymMTCq/inputs")
RECEIPT = ROOT / "xmodel/gi-only-charts-sol56-20260905.run.v2"

EXPECTED = {
    "source-support-closeout-opus5-20260905.md": "a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c",
    "moh-hsupport-gate-astra-20260905.md": "4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354",
    "sprime3_compiler.py": "7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833",
    "builder_fix.py": "d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b",
    "guided_gb.py": "501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3",
    "fleet.sh": "ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d",
    "dispatch.sh": "dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599",
    "FALLACY-v2.md": "e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5",
}

WORKSPACE_COPIES = {
    "source-support-closeout-opus5-20260905.md": ROOT / "xmodel/source-support-closeout-opus5-20260905.md",
    "moh-hsupport-gate-astra-20260905.md": ROOT / "xmodel/moh-hsupport-gate-astra-20260905.md",
    "sprime3_compiler.py": ROOT / "box/moh14-charts-20260905/sprime3_compiler.py",
    "builder_fix.py": ROOT / "box/moh14-charts-20260905/builder_fix.py",
    "guided_gb.py": ROOT / "box/lib/guided_gb.py",
    "fleet.sh": ROOT / "ops/fleet/fleet.sh",
    "dispatch.sh": ROOT / "ops/fleet/dispatch.sh",
    "FALLACY-v2.md": ROOT / "FALLACY-v2.md",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def repo_path(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def json_write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def verify_charged_inputs(frozen: Path = DEFAULT_FROZEN, require_all: bool = True) -> dict:
    """Verify the receipt and exact charged bytes; prefer the frozen copies."""
    receipt_text = RECEIPT.read_text(encoding="utf-8")
    receipt_pairs: dict[str, str] = {}
    bases: dict[str, str] = {}
    hashes: dict[str, str] = {}
    for line in receipt_text.splitlines():
        m = re.fullmatch(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if not m:
            continue
        (bases if m.group(2) == "basename" else hashes)[m.group(1)] = m.group(3)
    for i in sorted(set(bases) & set(hashes), key=int):
        receipt_pairs[bases[i]] = hashes[i]
    if receipt_pairs != EXPECTED:
        raise RuntimeError("charged-input receipt does not equal the frozen expected manifest")

    results = []
    for name, want in EXPECTED.items():
        frozen_path = frozen / name
        path = frozen_path if frozen_path.is_file() else WORKSPACE_COPIES[name]
        if require_all and not path.is_file():
            raise FileNotFoundError(path)
        if not path.is_file():
            continue
        got = sha256(path)
        if got != want:
            raise RuntimeError(f"charged input mismatch: {path}: {got} != {want}")
        results.append({"basename": name, "path": str(path), "sha256": got,
                        "frozen_copy": path == frozen_path})
    return {"status": "PASS", "receipt": repo_path(RECEIPT), "inputs": results}


def import_at(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_charged_modules(frozen: Path = DEFAULT_FROZEN):
    # Dependencies of sprime3_compiler.py are unchanged workspace modules.
    for path in (
        ROOT / "box",
        ROOT / "box/orderbasis-20260903",
        ROOT / "box/mohprog-drivers-20260903",
        ROOT / "box/xuscreen-20260903",
        ROOT / "box/lib",
        ROOT / "box/moh14-charts-20260905",
    ):
        sys.path.insert(0, str(path))
    chosen = {}
    for name in ("sprime3_compiler.py", "builder_fix.py", "guided_gb.py"):
        candidate = frozen / name
        chosen[name] = candidate if candidate.is_file() else WORKSPACE_COPIES[name]
        got = sha256(chosen[name])
        if got != EXPECTED[name]:
            raise RuntimeError(f"charged module mismatch: {chosen[name]}: {got}")
    # Install these canonical names because the charged compiler imports them lazily.
    B = import_at("builder_fix", chosen["builder_fix.py"])
    GG = import_at("guided_gb", chosen["guided_gb.py"])
    S = import_at("gi_charged_sprime3_compiler", chosen["sprime3_compiler.py"])
    # The frozen module's source location is /tmp; emitted paths are repository-relative.
    S.ROOT = ROOT
    S.BOX = ROOT / "box"
    V = import_at("gi_frozen_verify_source_complete", HSGATE / "verify_source_complete.py")
    return S, B, GG, V, {k: str(v) for k, v in chosen.items()}


def f(value: Any) -> F:
    return F(str(value))


def setup_map(text: str) -> dict[str, str]:
    return dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*);$", text, re.M))


def term_set(expr: str) -> set[tuple[str, ...]]:
    return {tuple(sorted(part.strip().split("*"))) for part in expr.split("+")}


def inventory_variable(block: str, i: int, mon: tuple[int, int]) -> str:
    b, a = mon
    if block == "h":
        return f"h_{b}_{a}"
    if block == "alpha":
        return f"A{i}_{b}_{a}"
    if block == "beta":
        return f"B{i}_{b}_{a}"
    raise ValueError(block)


def make_C(row: dict, source_meta: dict) -> dict:
    cf = source_meta["meta"]["closed_form"]
    ints = ("K", "e", "q", "u", "R", "Pi", "d3prime", "s_prime", "ell")
    C = {key: int(cf[key]) for key in ints}
    C["s"] = C.pop("s_prime")
    for key in ("delta1", "delta2", "delta_s", "B", "B_safe", "B_tight",
                "lambda_P", "lambda_Q"):
        C[key] = f(cf[key])
    C.update(n=int(row["n_prime"]), m=int(row["m_prime"]), V2=int(row["V2"]),
             two_point=bool(cf["two_point"]),
             support_basis="proved_outer_disc_G_only_H1_H2_H3_v1")
    return C


def supports(S, C: dict) -> dict:
    e, q = C["e"], C["q"]
    h = S.coeff_inventory_outer_disc(C, 1)
    alpha0 = {i: S.coeff_inventory_outer_disc(C, i) for i in range(1, e + 1)}
    beta0 = {i: S.coeff_inventory_outer_disc(C, i) for i in range(2, q + 1)}
    alpha, beta, gauges, notes, audit = S.apply_gauges(e, q, alpha0, beta0)
    wanted = {f"Q -> Q - const(beta_{q})", f"P -> P - const(alpha_{e})"}
    if set(gauges) != wanted or any("P -> P - alpha_" in g for g in gauges):
        raise AssertionError(f"unexpected G_i gauge set: {gauges}")
    return {"h": h, "alpha_pre": alpha0, "beta_pre": beta0,
            "alpha": alpha, "beta": beta, "gauges": gauges,
            "gauge_notes": notes, "gauge_audit": audit}


def source_supports(S, C: dict) -> dict:
    e, q = C["e"], C["q"]
    h = S.coeff_inventory_source_complete(C, 1)
    alpha0 = {i: S.coeff_inventory_source_complete(C, i) for i in range(1, e + 1)}
    beta0 = {i: S.coeff_inventory_source_complete(C, i) for i in range(2, q + 1)}
    alpha, beta, gauges, notes, audit = S.apply_gauges(e, q, alpha0, beta0)
    return {"h": h, "alpha_pre": alpha0, "beta_pre": beta0,
            "alpha": alpha, "beta": beta, "gauges": gauges,
            "gauge_notes": notes, "gauge_audit": audit}


def raw_supports(S, C: dict) -> dict:
    e, q = C["e"], C["q"]
    h = S.coeff_inventory_necessary(C, 1)
    alpha0 = {i: S.coeff_inventory_necessary(C, i) for i in range(1, e + 1)}
    beta0 = {i: S.coeff_inventory_necessary(C, i) for i in range(2, q + 1)}
    alpha, beta, gauges, notes, audit = S.apply_gauges(e, q, alpha0, beta0)
    return {"h": h, "alpha_pre": alpha0, "beta_pre": beta0,
            "alpha": alpha, "beta": beta, "gauges": gauges,
            "gauge_notes": notes, "gauge_audit": audit}


def block_items(inv: dict):
    yield "h", 1, inv["h"]
    for i, mons in sorted(inv["alpha"].items()):
        yield "alpha", i, mons
    for i, mons in sorted(inv["beta"].items()):
        yield "beta", i, mons


def block_lookup(inv: dict, block: str, i: int) -> list[tuple[int, int]]:
    return inv["h"] if block == "h" else inv[block][i]


def audit_fibre(S, V, row: dict, completion: dict, source_meta_path: Path,
                g_support: dict) -> dict:
    source_payload = json.loads(source_meta_path.read_text(encoding="utf-8"))
    C = make_C(row, source_payload)
    g_here = supports(S, C)
    if ({k: g_here[k] for k in ("h", "alpha", "beta")} !=
            {k: g_support[k] for k in ("h", "alpha", "beta")}):
        raise AssertionError(f"G_i not class-uniform at {row['stem']}")
    s_inv = source_supports(S, C)
    d_inv = raw_supports(S, C)
    source_actual = {
        "h": [tuple(x) for x in source_payload["meta"]["h_inventory"]],
        "alpha": {int(i): [tuple(x) for x in mons]
                  for i, mons in source_payload["meta"]["alpha_inventories"].items()},
        "beta": {int(i): [tuple(x) for x in mons]
                 for i, mons in source_payload["meta"]["beta_inventories"].items()},
    }
    for block, i, mons in block_items(s_inv):
        if set(mons) != set(block_lookup(source_actual, block, i)):
            raise AssertionError(f"compiler S_i != emitted S_i at {row['stem']} {block}{i}")

    comp = completion[row["stem"]]
    if f(comp["delta_s"]) != C["delta_s"]:
        raise AssertionError(f"completion delta_s mismatch at {row['stem']}")
    blocks = []
    removed_variables = []
    for block, i, Gm in block_items(g_here):
        Sm = set(block_lookup(s_inv, block, i))
        Dm = set(block_lookup(d_inv, block, i))
        Gm = set(Gm)
        # Literal use of the frozen verifier's independent union arithmetic.
        entire0, raw0, outer0 = V.inventory(
            C["K"], C["delta1"], C["B_safe"], C["delta_s"], i)
        if block in ("alpha", "beta") and ((block == "alpha" and i == C["e"]) or
                                             (block == "beta" and i == C["q"])):
            entire0 -= {(0, 0)}
            raw0 -= {(0, 0)}
            outer0 -= {(0, 0)}
        if Sm != entire0 or Dm != raw0 or Gm != outer0:
            raise AssertionError(f"frozen verifier/compiler inventory mismatch {row['stem']} {block}{i}")
        if not Gm <= Sm or Sm - Gm != Dm - Gm:
            raise AssertionError(f"G_i subset/specialization failure {row['stem']} {block}{i}")
        removed = sorted(Sm - Gm, key=lambda z: (-z[1], z[0]))
        removed_variables.extend(inventory_variable(block, i, mon) for mon in removed)
        blocks.append({
            "block": "h" if block == "h" else f"{block}_{i}", "i": i,
            "G_count": len(Gm), "D_count": len(Dm), "S_count": len(Sm),
            "G_subset_S": True, "S_minus_G_count": len(Sm - Gm),
            "D_minus_G_count": len(Dm - Gm),
            "S_minus_G_equals_D_minus_G": True,
            "specialize_to_zero": removed_variables[-len(removed):] if removed else [],
        })

    # Check the frozen completion receipt on every block, not just h.
    outer_h = set(S.coeff_inventory_outer_disc(C, 1))
    if set(map(tuple, comp["outer_h_support"])) != outer_h:
        raise AssertionError(f"outer h receipt mismatch at {row['stem']}")
    if set(map(tuple, comp["h_added_beyond_raw"])) != (
            set(s_inv["h"]) - set(d_inv["h"])):
        raise AssertionError(f"h completion receipt mismatch at {row['stem']}")
    for block, key in (("alpha", "alpha_added_beyond_raw"),
                       ("beta", "beta_added_beyond_raw")):
        for i in s_inv[block]:
            got = set(map(tuple, comp[key][str(i)]))
            # Completion JSON was made before terminal constant gauges; the
            # set difference is unchanged because the gauged constant is in D and G.
            want = set(s_inv[block][i]) - set(d_inv[block][i])
            if got != want:
                raise AssertionError(f"{key} mismatch at {row['stem']} block {i}")

    g_count = (len(g_here["h"]) + sum(map(len, g_here["alpha"].values())) +
               sum(map(len, g_here["beta"].values())) + 1)
    s_count = source_payload["parameter_count"]
    if s_count != len(source_payload["variables"]):
        raise AssertionError(f"source parameter count mismatch at {row['stem']}")
    return {
        "stem": row["stem"], "class_id": source_meta_path.parents[1].name,
        "status": "PASS", "K": C["K"], "e": C["e"], "q": C["q"],
        "ell": C["ell"], "d": str(-C["delta_s"]),
        "source_complete_unknowns_without_T": s_count,
        "G_unknowns_without_T": g_count,
        "G_unknowns_with_T": g_count + 1,
        "source_minus_G_unknowns": s_count - g_count,
        "blockwise_subset_verified": True,
        "specialization_coordinate_count": len(removed_variables),
        "specialization_map": {
            "domain": "frozen native S_i=D_i union G_i chart (J(Q,P), post terminal-constant gauges)",
            "codomain": "G_i-only native Q-first specialization companion",
            "kept_coordinates": "identity", "c_native": "c_native", "T_native": "T_native",
            "set_to_zero": removed_variables,
            "set_to_zero_is_exactly_D_minus_G": True,
        },
        "blocks": blocks,
        "source_meta": repo_path(source_meta_path),
    }


def orientation_control() -> dict:
    """Independent P/Q orientation and native-to-literal sign-map checks."""
    x, y = sp.symbols("x y")
    h = y**2 + x*y + x**2 + 1
    p_terms = [(sp.Integer(1), 3), (x + y, 2), (x*y + 2, 1), (x**2 - y, 0)]
    q_terms = [(sp.Integer(1), 2), (x - 2*y, 0)]  # beta_1 is absent

    def jac(a, b):
        return sp.diff(a, x) * sp.diff(b, y) - sp.diff(a, y) * sp.diff(b, x)

    P = sum(a * h**r for a, r in p_terms)
    Q = sum(b * h**s for b, s in q_terms)
    expanded = 0
    for a, r in p_terms:
        for b, s in q_terms:
            expanded += jac(a, b) * h**(r + s)
            if r + s and (r or s):
                expanded += (s * b * jac(a, h) + r * a * jac(h, b)) * h**(r + s - 1)
    ok = sp.expand(jac(P, Q) - expanded) == 0
    if not ok:
        raise AssertionError("P-first native Jacobian identity failed")
    c_native, c_literal, T_native, T_literal = sp.symbols(
        "c_native c_literal T_native T_literal")
    ell = 3
    native_target = jac(Q, P) - c_native * x**ell
    literal_target = jac(P, Q) - c_literal * x**ell
    target_image = sp.expand(native_target.subs(c_native, -c_literal))
    inverse_image = sp.expand(
        (T_native * c_native - 1).subs({T_native: -T_literal, c_native: -c_literal}))
    sign_ok = sp.expand(target_image + literal_target) == 0 and inverse_image == T_literal * c_literal - 1
    if not sign_ok:
        raise AssertionError("native J(Q,P) to literal J(P,Q) sign isomorphism failed")
    return {
        "status": "PASS", "P_first_identity": "native pair formula = J(P,Q)",
        "Q_first_identity": "native pair formula = J(Q,P) after reversing term lists",
        "sign_isomorphism": {
            "coefficient_coordinates": "identity", "c_native": "-c_literal",
            "T_native": "-T_literal",
            "target_image": "-(J(P,Q)-c_literal*x^ell)",
            "inverse_image": "T_literal*c_literal-1", "verified": True,
        },
        "beta_1_absent": True,
    }


def class_inputs() -> tuple[list[dict], dict[str, dict]]:
    classes = json.loads((SOURCE / "classes_manifest.json").read_text(encoding="utf-8"))
    completion = {x["stem"]: x for x in json.loads(
        (SOURCE / "support-completion.json").read_text(encoding="utf-8"))}
    if len(classes) != 6 or sum(len(c["rows"]) for c in classes) != 12 or len(completion) != 12:
        raise AssertionError("expected six classes and twelve fibres")
    return classes, completion


def emit_class(S, B, V, out_root: Path, cls: dict, completion: dict) -> dict:
    cid = cls["class_id"]
    stem = cid + "_G"
    dest = out_root / "classes" / cid
    source_class = SOURCE / "classes" / cid
    representative = cls["rows"][0]
    representative_meta = source_class / "meta" / f"{representative['stem']}.json"
    C = make_C(representative, json.loads(representative_meta.read_text(encoding="utf-8")))
    G = supports(S, C)

    fibre_audits = []
    for row in cls["rows"]:
        source_meta = source_class / "meta" / f"{row['stem']}.json"
        fibre_audits.append(audit_fibre(S, V, row, completion, source_meta, G))

    row_ob = S.OB.Row(
        key=stem, label=f"{cid} proved G_i-only class chart",
        n=int(cls["n_prime"]), m=int(cls["m_prime"]),
        M2=int(cls["M_prime"][-1]), V2=int(representative["V2"]),
        k=int(cls["ell"]),
    )
    spec = S.build_spec(C, G["h"], G["alpha_pre"], G["beta_pre"], row_ob,
                        "proved_G_only_class_uniform")
    # This untouched Q-first copy is the literal specialization companion for
    # the frozen S_i builders, which use the charged compiler's native order.
    native_spec = copy.deepcopy(spec)
    native_spec["meta"].update({
        "chart": "proved_G_i_only_native_QP_specialization_companion_v1",
        "support_basis": "G_i={(b,a):0<=a<K,0<=b<=floor(d*(iK-a))}",
        "coordinate": "phi=(x,y+eta(x))", "class_uniform": True,
        "class_id": cid, "canonical_stem": stem + "_native_QP",
        "beta_1": "0", "jacobian_orientation": "J(Q,P)-c_native*x^ell",
        "native_first_terms": "Q", "native_second_terms": "P",
        "role": "zero-specialization companion for frozen source S_i; not production solver",
    })
    # native_builder_text differentiates its first list against its second.
    # Charged build_spec calls them low=Q, high=P; swap for literal J(P,Q).
    P_terms = list(spec["high_terms"])
    Q_terms = list(spec["low_terms"])
    spec["low_terms"] = P_terms
    spec["high_terms"] = Q_terms
    meta = spec["meta"]
    meta.update({
        "chart": "proved_G_i_only_H1_H2_H3_v1",
        "support_basis": "G_i={(b,a):0<=a<K,0<=b<=floor(d*(iK-a))}",
        "coordinate": "phi=(x,y+eta(x))",
        "class_uniform": True,
        "class_id": cid,
        "canonical_stem": stem,
        "fibre_stems": [r["stem"] for r in cls["rows"]],
        "d": str(-C["delta_s"]),
        "beta_1": "0",
        "terminal_constant_gauges": [f"alpha_{C['e']}[0,0]=0", f"beta_{C['q']}[0,0]=0"],
        "P_expansion": "h^e + sum_{i=1}^e alpha_i*h^(e-i)",
        "Q_expansion": "h^q + sum_{i=2}^q beta_i*h^(q-i); beta_1=0",
        "jacobian_orientation": "J(P,Q)-c*x^ell",
        "native_first_terms": "P",
        "native_second_terms": "Q",
        "coefficient_ideal": "coefficients_{x,y,h-adic}(J(P,Q)-c*x^ell) + <T*c-1>",
        "inverse_equation": "T*c-1",
        "theorem_hypotheses": ["H1 licensed descendant", "H2 Q is root replacement",
                                "H3 d=-delta_s=(ell+1)/(n-M_s-1)>0"],
        "fallacy_v2": "exact proved G_i envelope in every block; no smaller block; modular UNIT is screen only",
    })
    if meta["beta_inventories"].get("1") is not None or any("BB1" in x for x in spec["setup"]):
        raise AssertionError("beta_1 was emitted")

    rows_path = dest / "rows" / f"{stem}_rows.tsv"
    builder_path = dest / "builders" / f"{stem}_builder.sing"
    native_rows_path = dest / "rows" / f"{stem}_native_QP_rows.tsv"
    native_builder_path = dest / "builders" / f"{stem}_native_QP_specialization_builder.sing"
    native_meta_path = dest / "meta" / f"{stem}_native_QP_specialization.json"
    meta_path = dest / "meta" / f"{stem}.json"
    for directory in (rows_path.parent, builder_path.parent, meta_path.parent, dest / "fibres", dest / "jobs",
                      dest / "specialization-sources/builders", dest / "specialization-sources/rows",
                      dest / "specialization-sources/meta"):
        directory.mkdir(parents=True, exist_ok=True)
    text = S.OB.native_builder_text(spec, rows_path)
    text = text.replace(str(rows_path.resolve()), f"rows/{stem}_rows.tsv")
    text, fix_info = B.fix_text(text)
    header = "\n".join([
        "// G_i-ONLY chart; source theorem H1-H3; coordinate phi=(x,y+eta(x))",
        f"// class={cid} stem={stem} fibres={len(cls['rows'])}",
        f"// P=h^{C['e']}+sum_i AAi*h^({C['e']}-i)",
        f"// Q=h^{C['q']}+sum_i>=2 BBi*h^({C['q']}-i); beta_1=0",
        f"// literal coefficient ideal: J(P,Q)-c*x^{C['ell']}; append T*c-1",
        "// native term order intentionally P first, Q second",
    ]) + "\n"
    builder_path.write_text(header + text, encoding="utf-8")

    native_text = S.OB.native_builder_text(native_spec, native_rows_path)
    native_text = native_text.replace(str(native_rows_path.resolve()),
                                      f"rows/{stem}_native_QP_rows.tsv")
    native_text, native_fix_info = B.fix_text(native_text)
    native_header = "\n".join([
        "// G_i-ONLY NATIVE SPECIALIZATION COMPANION; not the production solve orientation",
        f"// class={cid} stem={stem}_native_QP",
        "// literal zero-coordinate image of frozen source-complete native S_i builders",
        f"// native coefficient ideal: J(Q,P)-c*x^{C['ell']}; here builder symbol c means c_native",
        "// native term order intentionally Q first, P second",
        "// production isomorphism: c_native=-c_literal, T_native=-T_literal",
    ]) + "\n"
    native_builder_path.write_text(native_header + native_text, encoding="utf-8")

    variables = [str(p) for p in spec["params"]]
    g_count = len(variables)
    if any(a["G_unknowns_without_T"] != g_count for a in fibre_audits):
        raise AssertionError(f"G count mismatch in {cid}")
    payload = {
        "gi_only": True,
        "blockwise_subset_verified": True,
        "specialization_verified": True,
        "specialization_semantics": "production is the coordinate-only image of emitted literal-PQ S_i domains; frozen native custody is separately QP zero-map plus sign isomorphism",
        "orientation_verified": True,
        "jacobian_orientation": "J(P,Q)-c*x^ell",
        "native_specialization_orientation": "J(Q,P)-c_native*x^ell",
        "production_sign_isomorphism_verified": True,
        "native_specialization_companion": repo_path(native_builder_path),
        "native_specialization_companion_meta": repo_path(native_meta_path),
        "canonical_stem": stem,
        "class_id": cid,
        "shared_by_fibres": [a["stem"] for a in fibre_audits],
        "class_uniform_one_chart_suffices": True,
        "variables": variables,
        "inverse_variable": "T",
        "sat": "c",
        "parameter_count": g_count,
        "unknowns_without_T": g_count,
        "unknowns_with_T": g_count + 1,
        "jacobian_coefficient_generator_count": None,
        "generator_count_including_inverse": None,
        "builder": repo_path(builder_path),
        "rows_path": repo_path(rows_path),
        "guided_job": None,
        "verification_receipt": repo_path(out_root / "verification.json"),
        "builder_fix": fix_info,
        "meta": meta,
    }
    json_write(native_meta_path, {
        "gi_only": True, "role": "specialization_companion_not_production_solver",
        "class_id": cid, "canonical_production_stem": stem,
        "jacobian_orientation": "J(Q,P)-c_native*x^ell",
        "variables": variables, "inverse_variable": "T_native", "parameter_count": g_count,
        "builder_symbol_interpretation": {"c": "c_native", "adjoined_T": "T_native"},
        "builder": repo_path(native_builder_path), "rows_path": repo_path(native_rows_path),
        "builder_fix": native_fix_info,
        "zero_specialization_from_each_frozen_S_i": True,
        "production_sign_isomorphism": {
            "coefficient_coordinates": "identity", "c_native": "-c_literal",
            "T_native": "-T_literal", "verified": True,
        },
        "meta": native_spec["meta"],
    })

    # Strict production specialization domains: one P-first S_i presentation
    # per fibre.  These use the exact source-complete S_i inventories but the
    # same literal J(P,Q) orientation as the production G chart.  Consequently
    # production G is their image under D_i\G_i -> 0 with c,T fixed, with no
    # sign map in this leg.  They need not be extracted or solved.
    literal_source_presentations = []
    for row, audit in zip(cls["rows"], fibre_audits):
        source_payload_path = source_class / "meta" / f"{row['stem']}.json"
        source_payload = json.loads(source_payload_path.read_text(encoding="utf-8"))
        C_i = make_C(row, source_payload)
        S_i = source_supports(S, C_i)
        source_row_ob = S.OB.Row(
            key=row["stem"] + "_S_literal_PQ",
            label=f"{row['stem']} source-complete S_i literal P-first specialization domain",
            n=int(row["n_prime"]), m=int(row["m_prime"]),
            M2=int(cls["M_prime"][-1]), V2=int(row["V2"]), k=int(row["ell"]),
        )
        source_spec = S.build_spec(
            C_i, S_i["h"], S_i["alpha_pre"], S_i["beta_pre"], source_row_ob,
            "source_complete_S_literal_PQ_specialization_domain")
        source_P_terms = list(source_spec["high_terms"])
        source_Q_terms = list(source_spec["low_terms"])
        source_spec["low_terms"] = source_P_terms
        source_spec["high_terms"] = source_Q_terms
        source_spec["meta"].update({
            "chart": "source_complete_S_i_literal_PQ_specialization_domain_v1",
            "class_id": cid, "fibre_stem": row["stem"],
            "jacobian_orientation": "J(P,Q)-c*x^ell",
            "native_first_terms": "P", "native_second_terms": "Q",
            "role": "strict zero-coordinate specialization domain for production G_i chart",
        })
        source_stem = row["stem"] + "_S_literal_PQ"
        source_rows_path = dest / "specialization-sources/rows" / f"{source_stem}_rows.tsv"
        source_builder_path = dest / "specialization-sources/builders" / f"{source_stem}_builder.sing"
        source_literal_meta_path = dest / "specialization-sources/meta" / f"{source_stem}.json"
        source_text = S.OB.native_builder_text(source_spec, source_rows_path)
        source_text = source_text.replace(
            str(source_rows_path.resolve()), f"specialization-sources/rows/{source_stem}_rows.tsv")
        source_text, source_fix_info = B.fix_text(source_text)
        source_header = "\n".join([
            "// SOURCE-COMPLETE S_i LITERAL P-FIRST SPECIALIZATION DOMAIN; not a solve target",
            f"// fibre={row['stem']} class={cid}",
            f"// coefficient ideal: J(P,Q)-c*x^{C_i['ell']}; append T*c-1",
            "// production G_i is obtained ONLY by setting every D_i\\G_i coordinate to zero",
            "// native term order intentionally P first, Q second",
        ]) + "\n"
        source_builder_path.write_text(source_header + source_text, encoding="utf-8")
        source_variables = [str(p) for p in source_spec["params"]]
        if source_variables != source_payload["variables"]:
            raise AssertionError(f"literal P-first S variables differ from frozen S at {row['stem']}")
        zero_variables = sorted(set(source_variables) - set(variables))
        if set(zero_variables) != set(audit["specialization_map"]["set_to_zero"]):
            raise AssertionError(f"literal P-first S zero map mismatch at {row['stem']}")
        source_literal_payload = {
            "role": "strict_production_zero_specialization_domain_not_solver_chart",
            "class_id": cid, "fibre_stem": row["stem"], "stem": source_stem,
            "jacobian_orientation": "J(P,Q)-c*x^ell", "variables": source_variables,
            "inverse_variable": "T", "parameter_count": len(source_variables),
            "builder": repo_path(source_builder_path), "rows_path": repo_path(source_rows_path),
            "builder_fix": source_fix_info, "frozen_native_source_meta": repo_path(source_payload_path),
            "production_G_meta": repo_path(meta_path),
            "coordinate_only_specialization": {
                "kept_G_coordinates": "identity", "c": "c", "T": "T",
                "set_every_D_minus_G_coordinate_to_zero": zero_variables,
                "verified": True,
            },
            "meta": source_spec["meta"],
        }
        json_write(source_literal_meta_path, source_literal_payload)
        literal_source_presentations.append({
            "fibre_stem": row["stem"], "stem": source_stem,
            "builder": repo_path(source_builder_path), "meta": repo_path(source_literal_meta_path),
            "unknowns_without_T": len(source_variables), "set_to_zero_count": len(zero_variables),
        })
    payload["production_coordinate_only_specialization_verified"] = True
    payload["literal_PQ_source_presentations"] = literal_source_presentations
    json_write(meta_path, payload)

    alias_paths = []
    for audit in fibre_audits:
        alias = {
            "gi_only": True, "status": "PASS", "fibre_stem": audit["stem"],
            "class_id": cid, "canonical_stem": stem,
            "canonical_meta": repo_path(meta_path), "canonical_builder": repo_path(builder_path),
            "native_specialization_companion": repo_path(native_builder_path),
            "native_specialization_companion_meta": repo_path(native_meta_path),
            "same_G_chart_for_every_fibre_in_class": True,
            "blockwise_subset_verified": True, "specialization_verified": True,
            "specialization_semantics": "native S_i zero-map to native G_i companion; sign isomorphism to literal production",
            "jacobian_orientation": "J(P,Q)-c*x^ell",
            "native_specialization_orientation": "J(Q,P)-c_native*x^ell",
            "production_sign_isomorphism_verified": True,
            "production_coordinate_only_specialization_verified": True,
            "literal_PQ_source_presentation": next(
                x for x in literal_source_presentations if x["fibre_stem"] == audit["stem"]),
            "unknowns_without_T": g_count, "unknowns_with_T": g_count + 1,
            "jacobian_coefficient_generator_count": None,
            "generator_count_including_inverse": None,
            "audit": audit,
        }
        alias_path = dest / "fibres" / f"{audit['stem']}_G.json"
        json_write(alias_path, alias)
        alias_paths.append(repo_path(alias_path))

    job_path = dest / "jobs" / f"{stem}_fleet.sh"
    job_text = f'''#!/bin/bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
GI_ROOT="$(cd "$HERE/../.." && pwd)"
python3 "$GI_ROOT/solve_class.py" --class-id "{cid}" --timeout 600 --output-dir "$HERE/solve" \\
  --modular-screen --screen-timeout 600 --msolve-threads 8
'''
    job_path.write_text(job_text, encoding="utf-8")
    os.chmod(job_path, 0o755)

    class_payload = {
        "class_id": cid, "canonical_stem": stem, "status": "PASS",
        "gi_only": True, "class_uniform_one_chart_suffices": True,
        "blockwise_subset_verified": True, "specialization_verified": True,
        "specialization_semantics": "native S_i zero-map to native G_i companion; sign isomorphism to literal production",
        "orientation_verified": True, "jacobian_orientation": "J(P,Q)-c*x^ell",
        "native_specialization_orientation": "J(Q,P)-c_native*x^ell",
        "production_sign_isomorphism_verified": True,
        "production_coordinate_only_specialization_verified": True,
        "fibre_count": len(fibre_audits), "fibre_stems": [a["stem"] for a in fibre_audits],
        "fibre_aliases": alias_paths,
        "n_prime": cls["n_prime"], "m_prime": cls["m_prime"],
        "M_prime": cls["M_prime"], "ell": cls["ell"], "s_prime": cls["s_prime"],
        "K": C["K"], "e": C["e"], "q": C["q"], "d": str(-C["delta_s"]),
        "G_h_count": len(G["h"]),
        "G_alpha_dims": [len(G["alpha"][i]) for i in sorted(G["alpha"])],
        "G_beta_dims": [len(G["beta"][i]) for i in sorted(G["beta"])],
        "parameter_count": g_count, "unknowns_without_T": g_count,
        "unknowns_with_T": g_count + 1,
        "jacobian_coefficient_generator_count": None,
        "generator_count_including_inverse": None,
        "source_complete_union_unknowns_without_T": cls["union_parameter_count"],
        "source_complete_union_minus_G": cls["union_parameter_count"] - g_count,
        "per_fibre_size_comparison": [{
            "stem": a["stem"],
            "S_unknowns_without_T": a["source_complete_unknowns_without_T"],
            "G_unknowns_without_T": g_count,
            "S_minus_G": a["source_complete_unknowns_without_T"] - g_count,
        } for a in fibre_audits],
        "meta": repo_path(meta_path), "builder": repo_path(builder_path),
        "native_specialization_companion": repo_path(native_builder_path),
        "native_specialization_companion_meta": repo_path(native_meta_path),
        "literal_PQ_source_presentations": literal_source_presentations,
        "rows_path": repo_path(rows_path), "fleet_job": repo_path(job_path),
        "verification_receipt": repo_path(out_root / "verification.json"),
        "fibre_audits": fibre_audits,
    }
    json_write(dest / "class.json", class_payload)
    return class_payload


def verify_specialized_setup(cls: dict, out_root: Path) -> list[dict]:
    cid, stem = cls["class_id"], cls["canonical_stem"]
    dest = out_root / "classes" / cid
    g_meta = json.loads((dest / "meta" / f"{stem}.json").read_text(encoding="utf-8"))
    g_text = (dest / "builders" / f"{stem}_builder.sing").read_text(encoding="utf-8")
    g_setup = setup_map(g_text)
    g_vars = set(g_meta["variables"])
    native_meta = json.loads((ROOT / cls["native_specialization_companion_meta"]).read_text(encoding="utf-8"))
    native_text = (ROOT / cls["native_specialization_companion"]).read_text(encoding="utf-8")
    native_setup = setup_map(native_text)
    native_vars = set(native_meta["variables"])
    if not g_text.count("native term order intentionally P first, Q second") == 1:
        raise AssertionError(f"missing orientation marker in {stem}")
    if not native_text.count("native term order intentionally Q first, P second") == 1:
        raise AssertionError(f"missing native companion orientation marker in {stem}")
    ring = re.search(r"^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$", g_text, re.M)
    native_ring = re.search(r"^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$",
                            native_text, re.M)
    if not ring or ring.group(1).split(",") != g_meta["variables"]:
        raise AssertionError(f"bad y-first polynomial ring in {stem}")
    if not native_ring or native_ring.group(1).split(",") != native_meta["variables"]:
        raise AssertionError(f"bad native companion ring in {stem}")
    if int(ring.group(2)) != len(g_meta["variables"]) + 1:
        raise AssertionError(f"bad block size in {stem}")
    if native_vars != g_vars or int(native_ring.group(2)) != len(native_vars) + 1:
        raise AssertionError(f"native/literal variable mismatch in {stem}")
    if f"H0 = H0 - c*x^{cls['ell']};" not in g_text:
        raise AssertionError(f"target missing in {stem}")
    if f"H0 = H0 - c*x^{cls['ell']};" not in native_text:
        raise AssertionError(f"native companion target missing in {stem}")
    if "BB1" in g_text or "BB1" in native_text:
        raise AssertionError(f"beta_1 present in {stem}")
    if g_setup != native_setup:
        raise AssertionError(f"native/literal G setups differ in {stem}")
    e, q = cls["e"], cls["q"]
    pq_probe = (f"tmpSame = diff((AA{e}),x)*diff((BB{q}),y)-"
                f"diff((AA{e}),y)*diff((BB{q}),x);")
    qp_probe = (f"tmpSame = diff((BB{q}),x)*diff((AA{e}),y)-"
                f"diff((BB{q}),y)*diff((AA{e}),x);")
    if pq_probe not in g_text or qp_probe not in native_text:
        raise AssertionError(f"P/Q pair-loop orientation probe failed in {stem}")
    literal_sources = {x["fibre_stem"]: x for x in cls["literal_PQ_source_presentations"]}

    results = []
    for audit in cls["fibre_audits"]:
        source_meta = json.loads((ROOT / audit["source_meta"]).read_text(encoding="utf-8"))
        source_builder = ROOT / source_meta["builder"]
        source_text = source_builder.read_text(encoding="utf-8")
        s_setup = setup_map(source_text)
        s_vars = set(source_meta["variables"])
        if qp_probe not in source_text:
            raise AssertionError(f"frozen S builder is not verified Q-first at {audit['stem']}")
        tail_anchor = "ideal HDIV = h;"
        if source_text[source_text.index(tail_anchor):] != native_text[native_text.index(tail_anchor):]:
            raise AssertionError(f"native executable tails differ at {audit['stem']}")
        literal_record = literal_sources.get(audit["stem"])
        if literal_record is None:
            raise AssertionError(f"missing literal P-first S domain at {audit['stem']}")
        literal_source_meta = json.loads((ROOT / literal_record["meta"]).read_text(encoding="utf-8"))
        literal_source_text = (ROOT / literal_record["builder"]).read_text(encoding="utf-8")
        literal_source_setup = setup_map(literal_source_text)
        literal_source_vars = set(literal_source_meta["variables"])
        if pq_probe not in literal_source_text:
            raise AssertionError(f"literal S domain is not P-first at {audit['stem']}")
        literal_ring = re.search(
            r"^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$", literal_source_text, re.M)
        if (not literal_ring or literal_ring.group(1).split(",") != literal_source_meta["variables"] or
                int(literal_ring.group(2)) != len(literal_source_meta["variables"]) + 1):
            raise AssertionError(f"bad literal P-first S ring at {audit['stem']}")
        if literal_source_vars != s_vars or literal_source_setup != s_setup:
            raise AssertionError(f"literal P-first S is not the same S support/setup at {audit['stem']}")
        if literal_source_text[literal_source_text.index(tail_anchor):] != g_text[g_text.index(tail_anchor):]:
            raise AssertionError(f"literal P-first S/G executable tails differ at {audit['stem']}")
        if not g_vars <= s_vars:
            raise AssertionError(f"G variables not a subset of S variables at {audit['stem']}")
        removed = s_vars - g_vars
        declared = set(audit["specialization_map"]["set_to_zero"])
        if removed != declared:
            raise AssertionError(f"declared zero map != S\\G at {audit['stem']}")
        if set(s_setup) != set(native_setup):
            raise AssertionError(f"setup blocks differ at {audit['stem']}")
        for block in s_setup:
            specialized = {term for term in term_set(s_setup[block]) if not set(term) & removed}
            if specialized != term_set(native_setup[block]):
                raise AssertionError(f"setup specialization failed {audit['stem']} {block}")
            literal_specialized = {
                term for term in term_set(literal_source_setup[block]) if not set(term) & removed}
            if literal_specialized != term_set(g_setup[block]):
                raise AssertionError(f"literal production specialization failed {audit['stem']} {block}")
        results.append({
            "stem": audit["stem"], "status": "PASS",
            "blockwise_subset_verified": True, "specialization_verified": True,
            "native_orientation_verified": True, "production_orientation_verified": True,
            "production_sign_isomorphism_verified": True,
            "native_executable_tail_byte_identical_after_setup": True,
            "literal_PQ_S_to_production_G_executable_tail_byte_identical_after_setup": True,
            "set_to_zero_count": len(removed),
            "kept_parameter_count": len(g_vars),
            "native_zero_specialization": {
                "domain": "frozen emitted S_i native ideal: coeff(J(Q,P)-c_source*x^ell)+<T_source*c_source-1>",
                "codomain": "G_i native companion: coeff(J(Q,P)-c_native*x^ell)+<T_native*c_native-1>",
                "map": "G_i coordinates identity; c_source->c_native; T_source->T_native; every D_i\\G_i coordinate->0",
                "verified": True,
            },
            "production_sign_isomorphism": {
                "domain": "G_i native Q-first companion", "codomain": "G_i literal P-first production chart",
                "map": "coefficient coordinates identity; c_native->-c_literal; T_native->-T_literal",
                "target_image": "-(J(P,Q)-c_literal*x^ell)",
                "inverse_image": "T_literal*c_literal-1", "verified": True,
            },
            "production_coordinate_only_specialization": {
                "domain": "emitted source-complete S_i literal P-first presentation: coeff(J(P,Q)-c*x^ell)+<T*c-1>",
                "codomain": "literal P-first production G_i chart",
                "map": "G_i coordinates,c,T identity; every D_i\\G_i coordinate->0",
                "orientation_change": "none", "verified": True,
            },
            "production_coordinate_only_specialization_verified": True,
            "chain_to_production": "frozen native S_i --zero D_i\\G_i--> native G_i companion --sign isomorphism--> literal J(P,Q) production G_i",
            "no_coordinate_only_orientation_overclaim": True,
            "commutation": "differentiation, coefficient extraction, and monic h-adic division commute with the zero-coordinate map",
        })
    return results


def verification_payload(S, V, out_root: Path, module_paths: dict) -> dict:
    manifest = json.loads((out_root / "classes_manifest.json").read_text(encoding="utf-8"))
    source_classes, completion = class_inputs()
    source_by_id = {c["class_id"]: c for c in source_classes}
    orientation = orientation_control()
    results = []
    for cls in manifest:
        source_cls = source_by_id.get(cls["class_id"])
        if source_cls is None:
            raise AssertionError(f"unknown emitted class {cls['class_id']}")
        cid, stem = cls["class_id"], cls["canonical_stem"]
        source_class = SOURCE / "classes" / cid
        representative = source_cls["rows"][0]
        rep_meta_path = source_class / "meta" / f"{representative['stem']}.json"
        C = make_C(representative, json.loads(rep_meta_path.read_text(encoding="utf-8")))
        G = supports(S, C)
        fresh_audits = [audit_fibre(
            S, V, row, completion, source_class / "meta" / f"{row['stem']}.json", G)
            for row in source_cls["rows"]]
        canonical_meta = json.loads(
            (out_root / "classes" / cid / "meta" / f"{stem}.json").read_text(encoding="utf-8"))
        actual_G = {
            "h": [tuple(x) for x in canonical_meta["meta"]["h_inventory"]],
            "alpha": {int(i): [tuple(x) for x in mons]
                      for i, mons in canonical_meta["meta"]["alpha_inventories"].items()},
            "beta": {int(i): [tuple(x) for x in mons]
                     for i, mons in canonical_meta["meta"]["beta_inventories"].items()},
        }
        if any(set(block_lookup(actual_G, block, i)) != set(mons)
               for block, i, mons in block_items(G)):
            raise AssertionError(f"canonical metadata is not exact G_i at {cid}")
        expected_count = (len(G["h"]) + sum(map(len, G["alpha"].values())) +
                          sum(map(len, G["beta"].values())) + 1)
        if canonical_meta["parameter_count"] != expected_count or cls["parameter_count"] != expected_count:
            raise AssertionError(f"canonical parameter count mismatch at {cid}")
        fibres = verify_specialized_setup(cls, out_root)
        if {x["stem"] for x in fresh_audits} != {x["stem"] for x in fibres}:
            raise AssertionError(f"fibre set mismatch at {cid}")
        results.append({
            "class_id": cls["class_id"], "canonical_stem": cls["canonical_stem"],
            "status": "PASS", "blockwise_subset_verified": True,
            "specialization_verified": True, "orientation_verified": True,
            "native_zero_specialization_verified": True,
            "production_sign_isomorphism_verified": True,
            "production_coordinate_only_specialization_verified": True,
            "class_uniform_one_chart_suffices": True,
            "unknowns_without_T": cls["unknowns_without_T"],
            "unknowns_with_T": cls["unknowns_with_T"],
            "fresh_frozen_inventory_audits": fresh_audits, "fibres": fibres,
        })
    return {
        "status": "PASS",
        "scope": "G_i-only emission; production is the coordinate-only image of emitted P-first S_i presentations; separately, frozen native Q-first S_i specializes to a Q-first G_i companion followed by the verified (c,T)->(-c,-T) isomorphism",
        "classes": len(results), "fibres": sum(len(x["fibres"]) for x in results),
        "all_blockwise_subset": True, "all_specializations": True,
        "all_orientation_checks": True,
        "all_native_zero_specializations": True,
        "all_production_sign_isomorphisms": True,
        "all_production_coordinate_only_specializations": True,
        "orientation_control": orientation,
        "source_support_theorem": repo_path(WORKSPACE_COPIES["source-support-closeout-opus5-20260905.md"]),
        "source_complete_manifest_sha256": sha256(SOURCE / "classes_manifest.json"),
        "support_completion_sha256": sha256(SOURCE / "support-completion.json"),
        "frozen_verify_source_complete": repo_path(HSGATE / "verify_source_complete.py"),
        "frozen_verify_source_complete_sha256": sha256(HSGATE / "verify_source_complete.py"),
        "charged_modules": module_paths, "results": results,
    }


def emit(out_root: Path, frozen: Path) -> dict:
    custody = verify_charged_inputs(frozen, require_all=True)
    S, B, _GG, V, module_paths = load_charged_modules(frozen)
    classes, completion = class_inputs()
    orientation_control()
    emitted = [emit_class(S, B, V, out_root, cls, completion) for cls in classes]
    emitted.sort(key=lambda x: (x["unknowns_without_T"], x["class_id"]))
    json_write(out_root / "classes_manifest.json", emitted)
    json_write(out_root / "input-custody.json", custody)
    verify = verification_payload(S, V, out_root, module_paths)
    json_write(out_root / "verification.json", verify)
    return {"status": "PASS", "classes": len(emitted),
            "fibres": sum(x["fibre_count"] for x in emitted),
            "verification": repo_path(out_root / "verification.json"),
            "order": [{"class_id": x["class_id"],
                       "unknowns_without_T": x["unknowns_without_T"],
                       "unknowns_with_T": x["unknowns_with_T"]} for x in emitted]}


def emit_guided_one(S, out_root: Path, cid: str) -> dict:
    dest = out_root / "classes" / cid
    class_path = dest / "class.json"
    if not class_path.is_file():
        raise FileNotFoundError(class_path)
    cls = json.loads(class_path.read_text(encoding="utf-8"))
    stem = cls["canonical_stem"]
    result = S.emit_guided(dest, stem)
    if not result.get("ok"):
        raise RuntimeError(result.get("reason", "guided emission failed"))
    meta_path = dest / "meta" / f"{stem}.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    row_count = int(result["equations"])
    meta.update({
        "jacobian_coefficient_generator_count": row_count,
        "generator_count_including_inverse": row_count + 1,
        "guided_job": result["guided_job"],
    })
    json_write(meta_path, meta)
    cls.update({
        "jacobian_coefficient_generator_count": row_count,
        "generator_count_including_inverse": row_count + 1,
        "guided_job": result["guided_job"],
    })
    json_write(class_path, cls)
    for alias_path in (dest / "fibres").glob("*_G.json"):
        alias = json.loads(alias_path.read_text(encoding="utf-8"))
        alias["jacobian_coefficient_generator_count"] = row_count
        alias["generator_count_including_inverse"] = row_count + 1
        alias["guided_job"] = result["guided_job"]
        json_write(alias_path, alias)
    manifest_path = out_root / "classes_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest = [cls if x["class_id"] == cid else x for x in manifest]
    json_write(manifest_path, manifest)
    return {"status": "PASS", "class_id": cid, "canonical_stem": stem,
            "jacobian_coefficient_generators": row_count,
            "generators_including_Tc_minus_1": row_count + 1,
            **result}


def cmd_emit_guided(S, out_root: Path, class_id: str | None, all_classes: bool) -> dict:
    if all_classes:
        manifest = json.loads((out_root / "classes_manifest.json").read_text(encoding="utf-8"))
        results = []
        for cls in manifest:
            rows = ROOT / cls["rows_path"]
            if rows.is_file() and rows.stat().st_size > 42:
                results.append(emit_guided_one(S, out_root, cls["class_id"]))
        return {"status": "PASS", "emitted": len(results), "results": results}
    if not class_id:
        raise ValueError("emit-guided requires --class-id or --all")
    return emit_guided_one(S, out_root, class_id)


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", nargs="?", default="emit", choices=("emit", "verify", "emit-guided"))
    p.add_argument("--output-root", type=Path, default=HERE)
    p.add_argument("--frozen-input-dir", type=Path, default=DEFAULT_FROZEN)
    p.add_argument("--class-id")
    p.add_argument("--stem", help="accepted for compatibility; class id is inferred by dropping _G")
    p.add_argument("--all", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = parse_args(sys.argv[1:] if argv is None else argv)
    out_root = a.output_root.resolve()
    if a.mode == "emit":
        result = emit(out_root, a.frozen_input_dir)
    else:
        # Workers need only the three exact charged Python modules.
        S, _B, _GG, _V, module_paths = load_charged_modules(a.frozen_input_dir)
        if a.mode == "emit-guided":
            cid = a.class_id or (a.stem[:-2] if a.stem and a.stem.endswith("_G") else None)
            result = cmd_emit_guided(S, out_root, cid, a.all)
        else:
            result = verification_payload(S, _V, out_root, module_paths)
            json_write(out_root / "verification.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
