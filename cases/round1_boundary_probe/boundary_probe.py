#!/usr/bin/env python3
"""Exact covariance probe for boundary gradient/log/action data.

Replay with:

    uv run --no-project --with sympy==1.14.0 \
      python3 cases/round1_boundary_probe/boundary_probe.py

The script writes nothing.  It prints one deterministic JSON document.  All
arithmetic is over QQ.  A 2x2 matrix over the generic boundary DVR is recorded
by its two Smith exponents (a,b): a is the valuation of Fitt_1 (the ideal of
entries), and a+b is the valuation of Fitt_0 (the determinant).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any

import sympy as sp


x, y = sp.symbols("x y")
u, v = sp.symbols("u v")          # X=1 chart: u=Z/X, v=Y/X
z, r = sp.symbols("z r")          # Y=1 chart: z=Z/Y, r=X/Y
s, w = sp.symbols("s w")          # blow-up parameter and exceptional coordinate


def total_degree(poly: sp.Expr) -> int:
    return int(sp.Poly(sp.expand(poly), x, y, domain=sp.QQ).total_degree())


def canonical_poly_payload(poly: sp.Expr) -> list[list[Any]]:
    """Canonical sparse QQ[x,y] representation for content hashes."""
    p = sp.Poly(sp.expand(poly), x, y, domain=sp.QQ)
    out: list[list[Any]] = []
    for monom, coeff in p.terms():
        out.append([int(monom[0]), int(monom[1]), str(coeff)])
    return out


def poly_hash(poly: sp.Expr) -> str:
    payload = json.dumps(
        canonical_poly_payload(poly), separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def ord_var(expr: sp.Expr, parameter: sp.Symbol) -> int | None:
    """Exact valuation over the generic DVR QQ(other variables)[[parameter]]."""
    expr = sp.cancel(expr)
    if expr == 0:
        return None
    num, den = sp.fraction(expr)
    pn = sp.Poly(sp.expand(num), parameter)
    pd = sp.Poly(sp.expand(den), parameter)
    vn = min(int(m[0]) for m, _ in pn.terms())
    vd = min(int(m[0]) for m, _ in pd.terms())
    return vn - vd


def expr_hash(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> str:
    """Hash an exact polynomial expression after expansion."""
    p = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    payload = [[*[int(e) for e in monom], str(coeff)] for monom, coeff in p.terms()]
    blob = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(blob).hexdigest()


def matrix_metrics(
    matrix: list[list[sp.Expr]], parameter: sp.Symbol, variables: tuple[sp.Symbol, ...]
) -> dict[str, Any]:
    """Fitting and generic Smith data for a nonzero 2x2 matrix."""
    entries = [sp.cancel(q) for row in matrix for q in row]
    entry_orders = [ord_var(q, parameter) for q in entries]
    finite = [q for q in entry_orders if q is not None]
    if not finite:
        raise AssertionError("zero matrix has no rank-two Smith data")
    determinant = sp.factor(sp.det(sp.Matrix(matrix)))
    det_order = ord_var(determinant, parameter)
    if det_order is None:
        raise AssertionError("matrix determinant vanished")
    first = min(finite)
    second = det_order - first
    # The matrices used here are polynomial or Laurent-polynomial.  Hash the
    # cleared tuple via exact strings as an audit fingerprint.
    matrix_blob = "\n".join(sp.srepr(q) for q in entries).encode("utf-8")
    return {
        "entry_orders_row_major": entry_orders,
        "fitt1_order": first,
        "fitt0_order": det_order,
        "smith_exponents": [first, second],
        "determinant": str(determinant),
        "matrix_srepr_sha256": hashlib.sha256(matrix_blob).hexdigest(),
        "chart_variables": [str(q) for q in variables],
    }


def homogeneous_chart(poly: sp.Expr, axis: str) -> tuple[int, sp.Expr]:
    """Degree and homogenization restricted to X=1 or Y=1."""
    degree = total_degree(poly)
    p = sp.Poly(sp.expand(poly), x, y, domain=sp.QQ)
    if axis == "X":
        chart = sum(
            coeff * v ** j * u ** (degree - i - j)
            for (i, j), coeff in p.terms()
        )
    elif axis == "Y":
        chart = sum(
            coeff * r ** i * z ** (degree - i - j)
            for (i, j), coeff in p.terms()
        )
    else:
        raise ValueError(axis)
    return degree, sp.expand(chart)


def homogeneous_gradient_matrix(f: sp.Expr, g: sp.Expr, axis: str) -> list[list[sp.Expr]]:
    """[[F_X,G_X],[F_Y,G_Y]] in one projective affine chart."""
    d, fh = homogeneous_chart(f, axis)
    e, gh = homogeneous_chart(g, axis)
    if axis == "X":
        fx = sp.expand(d * fh - v * sp.diff(fh, v) - u * sp.diff(fh, u))
        fy = sp.diff(fh, v)
        gx = sp.expand(e * gh - v * sp.diff(gh, v) - u * sp.diff(gh, u))
        gy = sp.diff(gh, v)
    else:
        fx = sp.diff(fh, r)
        fy = sp.expand(d * fh - r * sp.diff(fh, r) - z * sp.diff(fh, z))
        gx = sp.diff(gh, r)
        gy = sp.expand(e * gh - r * sp.diff(gh, r) - z * sp.diff(gh, z))
    return [[fx, gx], [fy, gy]]


def gradient_probe(f: sp.Expr, g: sp.Expr, axis: str) -> dict[str, Any]:
    d, _ = homogeneous_chart(f, axis)
    e, _ = homogeneous_chart(g, axis)
    jac = sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
    matrix = homogeneous_gradient_matrix(f, g, axis)
    if axis == "X":
        expected = sp.cancel(u ** (d + e - 2) * jac.subs({x: 1 / u, y: v / u}))
        parameter = u
        variables = (u, v)
        blown = [[sp.expand(q.subs({u: s, v: s * w})) for q in row] for row in matrix]
    else:
        expected = sp.cancel(z ** (d + e - 2) * jac.subs({x: r / z, y: 1 / z}))
        parameter = z
        variables = (z, r)
        blown = [[sp.expand(q.subs({z: s, r: s * w})) for q in row] for row in matrix]
    determinant = sp.factor(sp.det(sp.Matrix(matrix)))
    assert sp.cancel(determinant - expected) == 0
    return {
        "standard_boundary": matrix_metrics(matrix, parameter, variables),
        "blowup_exceptional": matrix_metrics(blown, s, (s, w)),
    }


def log_coframe_matrix(f: sp.Expr, g: sp.Expr, axis: str, blowup: bool) -> list[list[sp.Expr]]:
    """Columns df,dg in the basis (dlog boundary, tangent differential)."""
    if axis == "X" and not blowup:
        fc = sp.cancel(f.subs({x: 1 / u, y: v / u}))
        gc = sp.cancel(g.subs({x: 1 / u, y: v / u}))
        return [[sp.cancel(u * sp.diff(fc, u)), sp.cancel(u * sp.diff(gc, u))],
                [sp.cancel(sp.diff(fc, v)), sp.cancel(sp.diff(gc, v))]]
    if axis == "X" and blowup:
        fc = sp.cancel(f.subs({x: 1 / s, y: w}))
        gc = sp.cancel(g.subs({x: 1 / s, y: w}))
        return [[sp.cancel(s * sp.diff(fc, s)), sp.cancel(s * sp.diff(gc, s))],
                [sp.cancel(sp.diff(fc, w)), sp.cancel(sp.diff(gc, w))]]
    if axis == "Y" and not blowup:
        fc = sp.cancel(f.subs({x: r / z, y: 1 / z}))
        gc = sp.cancel(g.subs({x: r / z, y: 1 / z}))
        return [[sp.cancel(z * sp.diff(fc, z)), sp.cancel(z * sp.diff(gc, z))],
                [sp.cancel(sp.diff(fc, r)), sp.cancel(sp.diff(gc, r))]]
    if axis == "Y" and blowup:
        fc = sp.cancel(f.subs({x: w, y: 1 / s}))
        gc = sp.cancel(g.subs({x: w, y: 1 / s}))
        return [[sp.cancel(s * sp.diff(fc, s)), sp.cancel(s * sp.diff(gc, s))],
                [sp.cancel(sp.diff(fc, w)), sp.cancel(sp.diff(gc, w))]]
    raise ValueError((axis, blowup))


def log_probe(f: sp.Expr, g: sp.Expr, axis: str) -> dict[str, Any]:
    standard = log_coframe_matrix(f, g, axis, False)
    blown = log_coframe_matrix(f, g, axis, True)
    parameter = u if axis == "X" else z
    variables = (u, v) if axis == "X" else (z, r)
    return {
        "standard_boundary": matrix_metrics(standard, parameter, variables),
        "blowup_exceptional": matrix_metrics(blown, s, (s, w)),
    }


def integrate_closed_form(a: sp.Expr, b: sp.Expr) -> sp.Expr:
    candidate = sp.integrate(sp.expand(a), x)
    remainder = sp.expand(b - sp.diff(candidate, y))
    primitive = sp.expand(candidate + sp.integrate(remainder, y))
    assert sp.expand(sp.diff(primitive, x) - a) == 0
    assert sp.expand(sp.diff(primitive, y) - b) == 0
    return primitive


def finite_laurent_coefficient(expr: sp.Expr, parameter: sp.Symbol, exponent: int) -> sp.Expr:
    """Coefficient of a finite Laurent polynomial in one parameter."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    order = ord_var(expr, parameter)
    if order is None:
        return sp.Integer(0)
    if order < 0:
        shifted = sp.expand(expr * parameter ** (-order))
        p = sp.Poly(shifted, parameter)
        wanted = exponent - order
    else:
        p = sp.Poly(expr, parameter)
        wanted = exponent
    if wanted < 0:
        return sp.Integer(0)
    return sp.expand(p.coeff_monomial(parameter ** wanted))


def action_one_form(f: sp.Expr, g: sp.Expr, which: str) -> tuple[sp.Expr, sp.Expr]:
    if which == "P":
        return sp.expand(f * sp.diff(g, x)), sp.expand(f * sp.diff(g, y) - x)
    if which == "Q":
        return sp.expand(g * sp.diff(f, x) - y), sp.expand(g * sp.diff(f, y))
    raise ValueError(which)


def action_probe(f: sp.Expr, g: sp.Expr, axis: str, jac: sp.Expr) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for which in ("P", "Q"):
        a, b = action_one_form(f, g, which)
        curl = sp.expand(sp.diff(b, x) - sp.diff(a, y))
        expected = sp.expand(jac - 1 if which == "P" else 1 - jac)
        assert sp.expand(curl - expected) == 0
        if curl != 0:
            output[which] = {
                "closed": False,
                "curl_sha256": poly_hash(curl),
                "curl": str(sp.factor(curl)),
            }
            continue
        primitive = integrate_closed_form(a, b)
        if axis == "X":
            standard = sp.expand(primitive.subs({x: 1 / u, y: v / u}))
            blown = sp.expand(primitive.subs({x: 1 / s, y: w}))
            standard_parameter = u
        else:
            standard = sp.expand(primitive.subs({x: r / z, y: 1 / z}))
            blown = sp.expand(primitive.subs({x: w, y: 1 / s}))
            standard_parameter = z
        std_val = ord_var(standard, standard_parameter)
        blow_val = ord_var(blown, s)
        std_res = finite_laurent_coefficient(sp.diff(standard, standard_parameter), standard_parameter, -1)
        blow_res = finite_laurent_coefficient(sp.diff(blown, s), s, -1)
        assert std_res == 0 and blow_res == 0
        pp = sp.Poly(primitive, x, y, domain=sp.QQ)
        output[which] = {
            "closed": True,
            "primitive_total_degree": int(pp.total_degree()) if primitive != 0 else None,
            "primitive_x_degree": int(pp.degree(x)) if primitive != 0 else None,
            "primitive_terms": len(pp.terms()) if primitive != 0 else 0,
            "primitive_sha256": poly_hash(primitive),
            "standard_valuation": std_val,
            "standard_pole_order": max(0, -std_val) if std_val is not None else None,
            "standard_differential_residue": str(std_res),
            "blowup_valuation": blow_val,
            "blowup_pole_order": max(0, -blow_val) if blow_val is not None else None,
            "blowup_differential_residue": str(blow_res),
        }
    return output


def probe_map(
    name: str,
    f: sp.Expr,
    g: sp.Expr,
    *,
    axis: str = "X",
    orbit_minimizes_to_identity: bool,
    construction: str,
) -> dict[str, Any]:
    f = sp.expand(f)
    g = sp.expand(g)
    jac = sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
    return {
        "name": name,
        "construction": construction,
        "chart": "X=1, p=[1:0:0]" if axis == "X" else "Y=1, p=[0:1:0]",
        "degrees": [total_degree(f), total_degree(g)],
        "jacobian": str(sp.factor(jac)),
        "is_keller_j1": bool(jac == 1),
        "map_hashes": {"f": poly_hash(f), "g": poly_hash(g)},
        "map_terms": {
            "f": len(sp.Poly(f, x, y).terms()),
            "g": len(sp.Poly(g, x, y).terms()),
        },
        "gradient_cokernel": gradient_probe(f, g, axis),
        "log_coframe": log_probe(f, g, axis),
        "action": action_probe(f, g, axis, jac),
        "orbit_minimization": {
            "available": orbit_minimizes_to_identity,
            "representative": "identity" if orbit_minimizes_to_identity else None,
            "metrics_reference": "identity.raw" if orbit_minimizes_to_identity else None,
        },
    }


def henon_tower(r_index: int) -> tuple[sp.Expr, sp.Expr, list[int]]:
    length = r_index + 4
    qs = [7, 3] + [2] * (length - 2)
    chain = [x, y]
    for q in qs:
        chain.append(sp.expand(chain[-1] ** q - chain[-2]))
    return chain[length], chain[length + 1], qs


def compact_metrics(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "degrees": entry["degrees"],
        "gradient_smith_standard": entry["gradient_cokernel"]["standard_boundary"]["smith_exponents"],
        "gradient_smith_blowup": entry["gradient_cokernel"]["blowup_exceptional"]["smith_exponents"],
        "log_smith_standard": entry["log_coframe"]["standard_boundary"]["smith_exponents"],
        "log_smith_blowup": entry["log_coframe"]["blowup_exceptional"]["smith_exponents"],
        "action_P_poles": [
            entry["action"]["P"].get("standard_pole_order"),
            entry["action"]["P"].get("blowup_pole_order"),
        ],
        "action_Q_poles": [
            entry["action"]["Q"].get("standard_pole_order"),
            entry["action"]["Q"].get("blowup_pole_order"),
        ],
    }


def frozen_matrix_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "entry_orders_row_major": metrics["entry_orders_row_major"],
        "fitt1_order": metrics["fitt1_order"],
        "fitt0_order": metrics["fitt0_order"],
        "smith_exponents": metrics["smith_exponents"],
        "determinant": metrics["determinant"],
        "matrix_srepr_sha256": metrics["matrix_srepr_sha256"],
    }


def frozen_map_result(entry: dict[str, Any]) -> dict[str, Any]:
    actions: dict[str, Any] = {}
    for which in ("P", "Q"):
        item = entry["action"][which]
        if not item["closed"]:
            actions[which] = {
                "closed": False,
                "curl": item["curl"],
                "curl_sha256": item["curl_sha256"],
            }
        else:
            actions[which] = {
                "closed": True,
                "primitive_total_degree": item["primitive_total_degree"],
                "primitive_x_degree": item["primitive_x_degree"],
                "primitive_terms": item["primitive_terms"],
                "primitive_sha256": item["primitive_sha256"],
                "standard_pole_order": item["standard_pole_order"],
                "blowup_pole_order": item["blowup_pole_order"],
                "standard_differential_residue": item["standard_differential_residue"],
                "blowup_differential_residue": item["blowup_differential_residue"],
            }
    return {
        "construction": entry["construction"],
        "chart": entry["chart"],
        "degrees": entry["degrees"],
        "jacobian": entry["jacobian"],
        "is_keller_j1": entry["is_keller_j1"],
        "map_hashes": entry["map_hashes"],
        "map_terms": entry["map_terms"],
        "gradient_cokernel": {
            "standard_boundary": frozen_matrix_metrics(
                entry["gradient_cokernel"]["standard_boundary"]
            ),
            "blowup_exceptional": frozen_matrix_metrics(
                entry["gradient_cokernel"]["blowup_exceptional"]
            ),
        },
        "log_coframe": {
            "standard_boundary": frozen_matrix_metrics(
                entry["log_coframe"]["standard_boundary"]
            ),
            "blowup_exceptional": frozen_matrix_metrics(
                entry["log_coframe"]["blowup_exceptional"]
            ),
        },
        "action": actions,
        "orbit_minimization": entry["orbit_minimization"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        action="store_true",
        help="print the frozen compact result rather than the full audit object",
    )
    args = parser.parse_args()
    identity = probe_map(
        "identity", x, y,
        orbit_minimizes_to_identity=True,
        construction="(x,y)",
    )
    t2 = probe_map(
        "T_2", x, y + x ** 2,
        orbit_minimizes_to_identity=True,
        construction="T_n=(x,y+x^n), n=2",
    )
    t4 = probe_map(
        "T_4", x, y + x ** 4,
        orbit_minimizes_to_identity=True,
        construction="T_n=(x,y+x^n), n=4",
    )
    # Keep the composition syntax in the construction string, but simplify the
    # polynomial pair before probing: an invariant of a map cannot see word
    # history once T_4^{-1} o T_4 is the identity.
    composed_f = x
    composed_g = sp.expand((y + x ** 4) - x ** 4)
    tinv_t = probe_map(
        "T_4_inverse_after_T_4", composed_f, composed_g,
        orbit_minimizes_to_identity=True,
        construction="T_4^{-1}∘T_4=(x,(y+x^4)-x^4)",
    )
    h0f, h0g, h0q = henon_tower(0)
    h1f, h1g, h1q = henon_tower(1)
    h0 = probe_map(
        "Henon_r0", h0f, h0g,
        orbit_minimizes_to_identity=True,
        construction=f"P_(i+1)=P_i^q-P_(i-1), q={h0q}",
    )
    h1 = probe_map(
        "Henon_r1", h1f, h1g,
        orbit_minimizes_to_identity=True,
        construction=f"P_(i+1)=P_i^q-P_(i-1), q={h1q}",
    )
    classkill = probe_map(
        "class_kill_B2_alpha2_beta3",
        x ** 4 + y,
        x ** 6 + y ** 5,
        axis="Y",
        orbit_minimizes_to_identity=False,
        construction="f=x^(B alpha)+y, g=x^(B beta)+y^(B beta-1), (B,alpha,beta)=(2,2,3)",
    )

    suite = [identity, t2, t4, tinv_t, h0, h1]
    raw_compact = {entry["name"]: compact_metrics(entry) for entry in suite}
    minimized_compact = {
        entry["name"]: compact_metrics(identity) for entry in suite
    }

    assert raw_compact["identity"] != raw_compact["T_2"]
    assert raw_compact["T_2"] != raw_compact["T_4"]
    assert raw_compact["identity"] == raw_compact["T_4_inverse_after_T_4"]
    assert len({tuple(vv["log_smith_standard"]) for vv in raw_compact.values()}) > 1
    assert len({tuple(vv["gradient_smith_standard"]) for vv in raw_compact.values()}) > 1
    assert all(vv == compact_metrics(identity) for vv in minimized_compact.values())
    assert all(
        entry["log_coframe"]["standard_boundary"]["fitt0_order"] == -2
        and entry["log_coframe"]["blowup_exceptional"]["fitt0_order"] == -1
        for entry in suite
    )
    assert all(
        entry["action"][which]["standard_differential_residue"] == "0"
        and entry["action"][which]["blowup_differential_residue"] == "0"
        for entry in suite for which in ("P", "Q")
    )
    assert not classkill["is_keller_j1"]
    assert not classkill["action"]["P"]["closed"]
    assert "Z" not in classkill["gradient_cokernel"]["standard_boundary"]["determinant"]

    result = {
        "schema_version": 1,
        "engine": {"python": "3", "sympy": sp.__version__, "domain": "QQ"},
        "charts": {
            "keller_suite_standard": "X=1: u=Z/X, v=Y/X; boundary u=0 over QQ(v)",
            "keller_suite_blowup": "u=s, v=s*w at [1:0:0]; exceptional s=0 over QQ(w)",
            "class_kill_standard": "Y=1: z=Z/Y, r=X/Y; boundary z=0 over QQ(r)",
            "class_kill_blowup": "z=s, r=s*w at [0:1:0]; exceptional s=0 over QQ(w)",
        },
        "definitions": {
            "gradient_matrix": "[[F_X,G_X],[F_Y,G_Y]] for separate-degree homogenizations F,G",
            "smith": "(a,b), a=ord(Fitt_1)=min entry order, a+b=ord(Fitt_0)=ord(det)",
            "log_matrix": "columns df,dg in (du/u,dv), or (ds/s,dw) after blowup",
            "action_forms": "f*dg-x*dy and g*df-y*dx",
        },
        "maps": {
            entry["name"]: frozen_map_result(entry)
            for entry in [*suite, classkill]
        },
        "covariance_summary": {
            "raw_metric_vectors": raw_compact,
            "after_exact_orbit_minimization": {
                "maps": [entry["name"] for entry in suite],
                "common_representative": "identity",
                "common_metrics": compact_metrics(identity),
            },
            "stable_on_raw_keller_suite": {
                "standard_log_determinant_order": -2,
                "blowup_log_determinant_order": -1,
                "action_differential_residues": 0,
            },
            "not_stable_on_equivalent_presentations": [
                "degrees",
                "gradient Fitt_0 order",
                "gradient Fitt_1 order / Smith split",
                "log-coframe Smith split",
                "action primitive pole order",
            ],
            "after_minimization": "all Keller controls are polynomial automorphisms and reduce exactly to identity",
        },
        "verdict": "COSTUME",
        "verdict_reason": (
            "No measured quantity is both stable under the allowed equivalent "
            "presentations and stronger than the determinant/log-volume identity. "
            "The class-kill decoy is separated only because its determinant has a residual Jacobian curve."
        ),
    }
    if args.summary:
        compact_maps: dict[str, Any] = {}
        for entry in [*suite, classkill]:
            frozen = result["maps"][entry["name"]]
            action_compact: dict[str, Any] = {}
            for which in ("P", "Q"):
                action_item = frozen["action"][which]
                if action_item["closed"]:
                    action_compact[which] = {
                        "closed": True,
                        "primitive_degrees_total_x": [
                            action_item["primitive_total_degree"],
                            action_item["primitive_x_degree"],
                        ],
                        "pole_orders_standard_blowup": [
                            action_item["standard_pole_order"],
                            action_item["blowup_pole_order"],
                        ],
                        "differential_residues_standard_blowup": [
                            action_item["standard_differential_residue"],
                            action_item["blowup_differential_residue"],
                        ],
                        "primitive_sha256": action_item["primitive_sha256"],
                    }
                else:
                    action_compact[which] = {
                        "closed": False,
                        "curl": action_item["curl"],
                        "curl_sha256": action_item["curl_sha256"],
                    }
            map_pair_blob = (
                frozen["map_hashes"]["f"] + frozen["map_hashes"]["g"]
            ).encode("ascii")
            compact_maps[entry["name"]] = {
                "degrees": frozen["degrees"],
                "jacobian": frozen["jacobian"],
                "is_keller_j1": frozen["is_keller_j1"],
                "map_pair_sha256": hashlib.sha256(map_pair_blob).hexdigest(),
                "gradient_smith_standard": frozen["gradient_cokernel"]["standard_boundary"]["smith_exponents"],
                "gradient_smith_blowup": frozen["gradient_cokernel"]["blowup_exceptional"]["smith_exponents"],
                "gradient_determinant_orders_standard_blowup": [
                    frozen["gradient_cokernel"]["standard_boundary"]["fitt0_order"],
                    frozen["gradient_cokernel"]["blowup_exceptional"]["fitt0_order"],
                ],
                "log_smith_standard": frozen["log_coframe"]["standard_boundary"]["smith_exponents"],
                "log_smith_blowup": frozen["log_coframe"]["blowup_exceptional"]["smith_exponents"],
                "log_determinant_orders": [
                    frozen["log_coframe"]["standard_boundary"]["fitt0_order"],
                    frozen["log_coframe"]["blowup_exceptional"]["fitt0_order"],
                ],
                "action": action_compact,
                "orbit_minimized_to": frozen["orbit_minimization"]["representative"],
            }
        full_blob = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
        # The frozen file keeps every measured map vector once.  The full
        # audit object (default output) retains the duplicated raw covariance
        # table and all matrix fingerprints; its hash binds this compact file
        # to that richer replay without making the checked-in result unwieldy.
        compact_covariance = dict(result["covariance_summary"])
        compact_covariance.pop("raw_metric_vectors")
        summary = {
            "schema_version": result["schema_version"],
            "engine": result["engine"],
            "charts": result["charts"],
            "definitions": result["definitions"],
            "maps": compact_maps,
            "covariance_summary": compact_covariance,
            "full_audit_json_sha256": hashlib.sha256(full_blob).hexdigest(),
            "verdict": result["verdict"],
            "verdict_reason": result["verdict_reason"],
        }
        print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
