#!/usr/bin/env python3
"""BNF bridge-chart builder and audit driver for the K=16 ray.

All charged inputs are read from the frozen lane directory.  This driver writes
only under box/bridgegate-20260903.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys
import time
from typing import Iterable

import sympy as sp
from sympy import Rational as R


ROOT = pathlib.Path("/home/ubuntu/jc2")
HERE = ROOT / "box/bridgegate-20260903"
INPUTS = pathlib.Path("/tmp/jc2-lane.VZaWdW/inputs")
ORDER = INPUTS / "t_order_system.py"
TRIANGULAR = INPUTS / "triangular_preprocess.py"
FALLACY = INPUTS / "FALLACY-v2.md"

EXPECTED = {
    "t_order_system.py": "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
    "triangular_preprocess.py": "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
    "bridge_chart.py": "34e6f380532943539f8686255986c551fe96534ff46109fd00fd8cc9c9e97d9e",
    "moh_p209_control.py": "9fa7dc7a82aa722fc5b7da641379a374815cdfb0b6e2fb2e7f5112fbd20f206c",
    "FALLACY-v2.md": "e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5",
}

gamma, pi = sp.symbols("gamma pi")


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_expected() -> dict[str, str]:
    out = {}
    for name, expected in EXPECTED.items():
        path = INPUTS / name
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError(f"frozen hash mismatch for {name}: {actual}")
        out[name] = actual
    return out


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def jac(left: sp.Expr, right: sp.Expr) -> sp.Expr:
    return sp.diff(left, gamma) * sp.diff(right, pi) - sp.diff(left, pi) * sp.diff(right, gamma)


@dataclasses.dataclass
class BridgeData:
    t: int
    e: int
    q: int
    n: int
    m: int
    h: sp.Expr
    A: sp.Expr
    B: sp.Expr
    z: sp.Expr
    params: list[sp.Symbol]
    c: sp.Symbol
    beta: dict[int, sp.Expr]
    alpha: dict[int, sp.Expr]
    p_terms: list[tuple[sp.Expr, int]]
    q_terms: list[tuple[sp.Expr, int]]
    p_series: dict[int, sp.Expr]
    q_series: dict[int, sp.Expr]
    by_power: dict[int, sp.Expr]
    tagged: list[tuple[int, tuple[int, int], sp.Expr]]
    equations: list[sp.Expr]
    gauges: dict[str, list[int]]
    elapsed_build_seconds: float


class Hadic:
    def __init__(self, t: int):
        self.t = t
        self.e = 3 * t + 1
        self.q = 2 * t + 1
        self.b1, self.b2, self.b3, self.b4 = sp.symbols("b1 b2 b3 b4")
        self.z = pi - gamma
        self.B = sp.expand(pi * self.z + self.b1 * pi + self.b2)
        self.A = sp.expand(pi * self.B + self.b3)
        self.h = sp.expand(pi * self.A + self.b4)
        self.h_poly = sp.Poly(self.h, pi)
        self.lo = -(self.e + 3)

    def red(self, expr: sp.Expr) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        cur = sp.Poly(sp.expand(expr), pi)
        h_poly = self.h_poly
        i = 0
        while True:
            if cur.is_zero:
                break
            if cur.degree() < 4:
                out[i] = sp.expand(cur.as_expr())
                break
            quotient, remainder = sp.div(cur, h_poly)
            if not remainder.is_zero:
                out[i] = sp.expand(remainder.as_expr())
            cur = quotient
            i += 1
        return {k: v for k, v in out.items() if v != 0}

    def hmul(self, left: dict[int, sp.Expr], right: dict[int, sp.Expr], lo: int | None = None) -> dict[int, sp.Expr]:
        if lo is None:
            lo = self.lo
        raw: dict[int, sp.Expr] = {}
        for i, u in left.items():
            for j, v in right.items():
                if i + j >= lo - 1:
                    raw[i + j] = raw.get(i + j, 0) + u * v
        out: dict[int, sp.Expr] = {}
        for power, expr in raw.items():
            expr = sp.expand(expr)
            if expr == 0:
                continue
            for delta, coeff in self.red(expr).items():
                target = power + delta
                if target >= lo:
                    out[target] = sp.expand(out.get(target, 0) + coeff)
        return {k: v for k, v in out.items() if v != 0}

    @staticmethod
    def hadd(*args: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
        out: dict[int, sp.Expr] = {}
        for item in args:
            for power, expr in item.items():
                out[power] = sp.expand(out.get(power, 0) + expr)
        return {k: v for k, v in out.items() if v != 0}

    @staticmethod
    def hscal(series: dict[int, sp.Expr], scalar: sp.Expr) -> dict[int, sp.Expr]:
        return {k: sp.expand(scalar * v) for k, v in series.items() if sp.expand(scalar * v) != 0}

    @staticmethod
    def shift(series: dict[int, sp.Expr], delta: int) -> dict[int, sp.Expr]:
        return {k + delta: v for k, v in series.items()}

    def hpow_unit(self, w: dict[int, sp.Expr], exponent: sp.Rational) -> dict[int, sp.Expr]:
        if not all(power <= -2 for power in w):
            raise AssertionError(f"unit tail has unexpected h-powers {sorted(w)}")
        res: dict[int, sp.Expr] = {0: sp.Integer(1)}
        term: dict[int, sp.Expr] = {0: sp.Integer(1)}
        coef = sp.Integer(1)
        for j in range(1, -2 * self.lo + 4):
            term = self.hmul(term, w)
            if not term:
                break
            coef = sp.Rational(coef) * (exponent - (j - 1)) / j
            res = self.hadd(res, self.hscal(term, coef))
        return res

    def to_poly(self, series: dict[int, sp.Expr]) -> sp.Expr:
        return sp.expand(sum(coeff * self.h**power for power, coeff in series.items() if power >= 0))

    def basis(self, deficit: int) -> list[tuple[str, sp.Expr]]:
        if deficit <= self.t:
            return [("1", sp.Integer(1))]
        if deficit <= 2 * self.t:
            return [("1", sp.Integer(1)), ("A", self.A)]
        if deficit <= 3 * self.t:
            return [("1", sp.Integer(1)), ("A", self.A), ("B", self.B)]
        return [
            ("1", sp.Integer(1)),
            ("g", gamma),
            ("A", self.A),
            ("B", self.B),
            ("z", self.z),
        ]


def hdict_to_terms(series: dict[int, sp.Expr]) -> list[tuple[sp.Expr, int]]:
    return [(sp.expand(series[power]), power) for power in sorted(series, reverse=True)]


def build_bridge(t: int, include_jacobian: bool = True) -> BridgeData:
    if t < 1:
        raise ValueError("t must be positive")
    started = time.monotonic()
    H = Hadic(t)
    e, q = H.e, H.q
    n, m = 12 * t + 4, 8 * t + 4
    params: list[sp.Symbol] = [H.b1, H.b2, H.b3, H.b4]

    beta: dict[int, sp.Expr] = {}
    u_ser: dict[int, sp.Expr] = {}
    for j in range(2, q + 1):
        coeff = sp.Integer(0)
        for name, phi in H.basis(j):
            symbol = sp.Symbol(f"q{j}_{name}")
            params.append(symbol)
            coeff = sp.expand(coeff + symbol * phi)
        beta[j] = coeff
        for delta, reduced_coeff in H.red(coeff).items():
            u_ser[-j + delta] = sp.expand(u_ser.get(-j + delta, 0) + reduced_coeff)
    u_ser = {power: coeff for power, coeff in u_ser.items() if coeff != 0}
    if not all(power <= -2 for power in u_ser):
        raise AssertionError(f"beta tail has unexpected h-powers {sorted(u_ser)}")

    avars: dict[int, sp.Expr] = {}
    free_a: list[int] = []
    for k in range(1, e + 1):
        if k in (t, e - 1, e):
            avars[k] = sp.Integer(0)
        else:
            symbol = sp.Symbol(f"a{k}")
            avars[k] = symbol
            params.append(symbol)
            free_a.append(k)

    pser: dict[int, sp.Expr] = {}
    for k in range(0, e + 1):
        ak = sp.Integer(1) if k == 0 else avars[k]
        if ak == 0:
            continue
        term = H.hpow_unit(u_ser, R(e - k, q))
        pser = H.hadd(pser, H.hscal(H.shift(term, e - k), ak))

    p_nonnegative = {power: coeff for power, coeff in pser.items() if power >= 0}
    q_nonnegative = H.hadd({q: sp.Integer(1)}, H.shift(u_ser, q))
    q_nonnegative = {power: coeff for power, coeff in q_nonnegative.items() if power >= 0}
    p_terms = hdict_to_terms(p_nonnegative)
    q_terms = hdict_to_terms(q_nonnegative)

    c = sp.Symbol("c")
    params.append(c)

    by_power: dict[int, sp.Expr] = {}
    equations: list[sp.Expr] = []
    tagged: list[tuple[int, tuple[int, int], sp.Expr]] = []
    if include_jacobian:
        for aa, r in q_terms:
            for bb, s in p_terms:
                first = jac(aa, bb)
                if first:
                    by_power[r + s] = by_power.get(r + s, 0) + first
                second = s * bb * jac(aa, H.h) + r * aa * jac(H.h, bb)
                if second:
                    by_power[r + s - 1] = by_power.get(r + s - 1, 0) + second

        max_power = max(by_power) if by_power else 0
        for power in range(0, max_power + 5):
            expr = sp.expand(by_power.get(power, 0))
            quotient, remainder = sp.div(expr, H.h, pi)
            by_power[power] = sp.expand(remainder)
            if quotient != 0:
                by_power[power + 1] = by_power.get(power + 1, 0) + quotient
            if power > max_power and quotient == 0:
                break

        for h_power in sorted(by_power):
            remainder = sp.expand(by_power[h_power])
            if h_power == 0:
                remainder = sp.expand(remainder - c * gamma)
            if remainder == 0:
                continue
            poly = sp.Poly(remainder, gamma, pi)
            for monomial, coefficient in poly.terms():
                coefficient = sp.expand(coefficient)
                if coefficient != 0:
                    equations.append(coefficient)
                    tagged.append((h_power, tuple(monomial), coefficient))

    p_series = dict(p_nonnegative)
    q_series = dict(q_nonnegative)
    alpha = {i: sp.expand(p_series.get(e - i, 0)) for i in range(1, e + 1)}

    return BridgeData(
        t=t,
        e=e,
        q=q,
        n=n,
        m=m,
        h=H.h,
        A=H.A,
        B=H.B,
        z=H.z,
        params=params[:-1],
        c=c,
        beta=beta,
        alpha=alpha,
        p_terms=p_terms,
        q_terms=q_terms,
        p_series=p_series,
        q_series=q_series,
        by_power={k: v for k, v in by_power.items() if v != 0},
        tagged=tagged,
        equations=equations,
        gauges={"a_zero": [t, e - 1, e], "a_free": free_a},
        elapsed_build_seconds=time.monotonic() - started,
    )


def bridge_dict(data: BridgeData) -> dict:
    return {
        "t": data.t,
        "e": data.e,
        "q": data.q,
        "h": data.h,
        "A": data.A,
        "B": data.B,
        "z": data.z,
        "params": data.params,
        "c": data.c,
        "tagged": data.tagged,
        "equations": data.equations,
    }


def in_span(expr: sp.Expr, phis: list[sp.Expr]) -> bool:
    if expr == 0:
        return True
    coeffs = sp.symbols(f"lam0:{len(phis)}")
    if len(phis) == 1:
        coeffs = (coeffs[0],)
    target = sp.expand(expr - sum(coeff * phi for coeff, phi in zip(coeffs, phis)))
    equations = sp.Poly(target, gamma, pi).coeffs()
    sol = sp.solve(equations, coeffs, dict=True)
    return bool(sol)


def subset_audit(ts: Iterable[int]) -> dict:
    order = load_module(ORDER, "bridgegate_order_chart")
    records = []
    for t in ts:
        H = Hadic(t)
        e, q = H.e, H.q
        order_spaces = order.chart_spaces(t, sp.Integer(1), H.A, H.B, H.z)
        alpha_failures = []
        beta_failures = []
        direct_alpha_checked = False
        direct_build_seconds = None
        if t <= 2:
            data = build_bridge(t, include_jacobian=False)
            direct_alpha_checked = True
            direct_build_seconds = round(data.elapsed_build_seconds, 6)
            for i in range(1, data.e + 1):
                if not in_span(data.alpha[i], order_spaces[i]):
                    alpha_failures.append(i)
        for j in range(2, q + 1):
            beta_j = sp.expand(sum(sp.Symbol(f"q{j}_{name}") * phi for name, phi in H.basis(j)))
            if not in_span(beta_j, order_spaces[j]):
                beta_failures.append(j)
        nesting_failures = []
        for i in range(1, e + 1):
            for k in range(i, e + 1):
                for phi in order_spaces[i]:
                    if not in_span(phi, order_spaces[k]):
                        nesting_failures.append((i, k, str(phi)))
        closure_failures = []
        for i in range(1, e + 1):
            for j in range(1, e + 1):
                for phi in order_spaces[i]:
                    for psi in order_spaces[j]:
                        for delta, coeff in H.red(sp.expand(phi * psi)).items():
                            target = i + j - delta
                            if 0 <= target <= e and not in_span(coeff, order_spaces[target]):
                                closure_failures.append({
                                    "left": i,
                                    "right": j,
                                    "delta": delta,
                                    "target": target,
                                    "coeff": str(coeff),
                                })
        if not direct_alpha_checked and (nesting_failures or closure_failures):
            alpha_failures = list(range(1, e + 1))
        h_top_degree = 4
        record = {
            "t": t,
            "e": e,
            "q": q,
            "unknowns_including_c": 6 * t + 5,
            "predicted_unknowns": 6 * t + 5,
            "jacobian_generators": None,
            "alpha_failures": alpha_failures,
            "beta_failures": beta_failures,
            "all_alpha_in_order_spaces": not alpha_failures,
            "all_beta_in_order_spaces": not beta_failures,
            "direct_alpha_checked": direct_alpha_checked,
            "direct_alpha_build_seconds": direct_build_seconds,
            "alpha_checked_by_BNF_closure_for_t_ge_3": not direct_alpha_checked,
            "nesting_failures": nesting_failures,
            "closure_failure_count": len(closure_failures),
            "closure_failures": closure_failures[:10],
            "deg_pi_P": h_top_degree * e,
            "deg_pi_Q": h_top_degree * q,
            "P_monic_by_top_h_term": True,
            "Q_monic_by_top_h_term": True,
            "free_a_indices": [k for k in range(1, e + 1) if k not in (t, e - 1, e)],
            "zero_a_indices": [t, e - 1, e],
        }
        records.append(record)
    return {
        "type": "MECHANICAL_SUBSET_AUDIT",
        "order_chart": str(ORDER),
        "t_order_system_sha256": sha256_file(ORDER),
        "records": records,
        "all_pass": all(r["all_alpha_in_order_spaces"] and r["all_beta_in_order_spaces"] for r in records),
    }


def expression_vector_hash(expressions: Iterable[sp.Expr]) -> str:
    return hashlib.sha256(("\n".join(str(sp.expand(e)) for e in expressions) + "\n").encode("utf-8")).hexdigest()


def primitive_integer_polynomial(expr: sp.Expr, variables: list[sp.Symbol]) -> tuple[sp.Poly, sp.Rational]:
    polynomial = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    den_lcm, cleared = polynomial.clear_denoms(convert=True)
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(den_lcm, content)
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    if sp.expand(primitive.as_expr() - multiplier * expr) != 0:
        raise AssertionError("primitive row is not a Q* multiple")
    return primitive, multiplier


def singular_polynomial(expr: sp.Expr, variables: list[sp.Symbol]) -> str:
    primitive, _multiplier = primitive_integer_polynomial(expr, variables)
    rendered: list[str] = []
    for monomial, coefficient in primitive.terms():
        coefficient = sp.Integer(coefficient)
        pieces = []
        for variable, exponent in zip(variables, monomial):
            if exponent == 1:
                pieces.append(str(variable))
            elif exponent > 1:
                pieces.append(f"{variable}^{exponent}")
        monomial_text = "*".join(pieces)
        magnitude = abs(coefficient)
        if monomial_text and magnitude == 1:
            body = monomial_text
        else:
            body = str(magnitude) if not monomial_text else f"{magnitude}*{monomial_text}"
        if not rendered:
            rendered.append(("-" if coefficient < 0 else "") + body)
        else:
            rendered.append((" - " if coefficient < 0 else " + ") + body)
    return "".join(rendered) if rendered else "0"


def emit_direct_singular(data: BridgeData, characteristic: int, method: str) -> str:
    if method not in {"std", "slimgb"}:
        raise ValueError(method)
    variables = data.params + [data.c, sp.Symbol("T")]
    poly_vars = data.params + [data.c]
    generators = [singular_polynomial(eq, poly_vars) for eq in data.equations]
    field = str(characteristic)
    lines = [
        f"// bridge BNF direct chart; t={data.t}; char={characteristic}; method={method}",
        f"// unknowns including c={len(data.params)+1}; Jacobian generators={len(data.equations)}",
        'LIB "resources.lib";',
        "setcores(4);",
        f"ring RAC={field},(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); } else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        f"ring R={field},({','.join(map(str, variables))}),dp;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        'print("CONTROL_EMPTY_START");',
        "ideal CE=c,T*c-1;",
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=c-1,T*c-1;",
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        f'print("MAIN_START t={data.t} direct_bridge characteristic={characteristic} method={method} generators={len(generators)+1} unknowns={len(data.params)+1}");',
        "ideal I=" + ",\n".join(generators + ["T*c-1"]) + ";",
        f"ideal G={method}(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_UNIT"); G; } else { print("MAIN_NONUNIT"); int cap=size(G); if (cap>20) { cap=20; } for (int i=1; i<=cap; i++) { G[i]; } }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def audit_chart(data: BridgeData) -> dict:
    h_hist: dict[str, int] = {}
    degree_hist: dict[str, int] = {}
    variables = data.params + [data.c]
    for h_power, _monomial, expr in data.tagged:
        key = str(h_power)
        h_hist[key] = h_hist.get(key, 0) + 1
        degree = sp.Poly(expr, *variables, domain=sp.QQ).total_degree()
        dkey = str(degree)
        degree_hist[dkey] = degree_hist.get(dkey, 0) + 1
    return {
        "t": data.t,
        "e": data.e,
        "q": data.q,
        "n": data.n,
        "m": data.m,
        "unknowns_including_c": len(data.params) + 1,
        "predicted_unknowns": 6 * data.t + 5,
        "jacobian_generators": len(data.equations),
        "total_direct_generators_with_Rabinowitsch": len(data.equations) + 1,
        "h_level_histogram": h_hist,
        "parameter_degree_histogram": degree_hist,
        "equation_vector_sha256": expression_vector_hash(data.equations),
        "free_a_indices": data.gauges["a_free"],
        "zero_a_indices": data.gauges["a_zero"],
        "build_seconds": round(data.elapsed_build_seconds, 6),
    }


def write_direct(t: int, characteristics: list[int], method: str) -> dict:
    data = build_bridge(t)
    chart_audit = audit_chart(data)
    out_dir = HERE / f"t{t}"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "chart_audit.json").write_text(json.dumps(chart_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    generated = []
    for characteristic in characteristics:
        suffix = "Q" if characteristic == 0 else f"p{characteristic}"
        path = out_dir / f"bridge_direct_{suffix}_{method}.sing"
        path.write_text(emit_direct_singular(data, characteristic, method), encoding="utf-8")
        generated.append(str(path.relative_to(ROOT)))
    return {"chart": chart_audit, "generated": generated}


def bridge_reduction(t: int, max_seconds: float, max_bytes: int):
    tp = load_module(TRIANGULAR, "bridgegate_triangular")
    data = build_bridge(t)
    reduction = tp.reduce_chart(
        bridge_dict(data),
        max_pivots=512,
        max_seconds=max_seconds,
        max_expression_bytes=max_bytes,
    )
    return data, reduction, tp


def write_preprocessed(t: int, characteristics: list[int], max_seconds: float, max_bytes: int) -> dict:
    data, reduction, tp = bridge_reduction(t, max_seconds=max_seconds, max_bytes=max_bytes)
    out_dir = HERE / f"t{t}"
    out_dir.mkdir(parents=True, exist_ok=True)
    audit = {
        "t": t,
        "source": "bridge BNF chart",
        "row_order": "descending h_power, ascending monomial, original row",
        "unknowns_including_c": len(data.params) + 1,
        "jacobian_generators": len(data.equations),
        "residual_unknowns_including_c": len(reduction.remaining_variables) + 1,
        "residual_generators": len(reduction.rows),
        "pivot_count": len(reduction.pivots),
        "pivot_variables": [str(p.variable) for p in reduction.pivots],
        "pivot_coefficients": [str(p.coefficient) for p in reduction.pivots],
        "remaining_variables": [str(v) for v in reduction.remaining_variables] + [str(reduction.c)],
        "original_equation_vector_sha256": expression_vector_hash(row.expr for row in reduction.original_rows),
        "residual_equation_vector_sha256": expression_vector_hash(row.expr for row in reduction.rows),
        "preprocess_elapsed_seconds": round(reduction.elapsed_seconds, 6),
        "chart_build_seconds": round(data.elapsed_build_seconds, 6),
    }
    (out_dir / "preprocess_audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tp.write_ring_map(out_dir / "ring_map.tsv", reduction)
    tp.write_emission_scalars(out_dir / "emission_scalars.tsv", reduction)
    generated = []
    for characteristic in characteristics:
        suffix = "Q" if characteristic == 0 else f"p{characteristic}"
        path = out_dir / f"bridge_preprocessed_{suffix}.sing"
        path.write_text(tp.emit_singular(reduction, characteristic), encoding="utf-8")
        generated.append(str(path.relative_to(ROOT)))
    return {"chart": audit_chart(data), "preprocess": audit, "generated": generated}


def run_singular(path: pathlib.Path, timeout: float | None = None) -> dict:
    out_path = path.with_suffix(path.suffix + ".out")
    err_path = path.with_suffix(path.suffix + ".err")
    resource_path = path.with_suffix(path.suffix + ".resource")
    command = ["/usr/bin/time", "-v", "Singular", "-q", str(path)]
    started = time.monotonic()
    with out_path.open("w", encoding="utf-8") as out, err_path.open("w", encoding="utf-8") as err:
        try:
            proc = subprocess.run(command, cwd=ROOT, stdout=out, stderr=err, timeout=timeout)
            timed_out = False
            returncode = proc.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
            returncode = 124
    elapsed = time.monotonic() - started
    err_text = err_path.read_text(encoding="utf-8", errors="replace")
    resource_path.write_text(err_text, encoding="utf-8")
    out_text = out_path.read_text(encoding="utf-8", errors="replace")
    verdict = "TIMEOUT" if timed_out else "UNKNOWN"
    if "MAIN_UNIT" in out_text or "MAIN_SATURATED_EMPTY" in out_text:
        verdict = "UNIT"
    elif "MAIN_NONUNIT" in out_text or "MAIN_NONTRIVIAL_SUPERSET_ONLY" in out_text:
        verdict = "NONUNIT"
    return {
        "singular": str(path.relative_to(ROOT)),
        "stdout": str(out_path.relative_to(ROOT)),
        "stderr": str(err_path.relative_to(ROOT)),
        "resource": str(resource_path.relative_to(ROOT)),
        "returncode": returncode,
        "timed_out": timed_out,
        "wall_seconds_driver": round(elapsed, 3),
        "verdict": verdict,
    }


def render_moh_page() -> dict:
    out_dir = HERE / "moh-pages"
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / "moh-p209-pdf70"
    proc = subprocess.run(
        ["pdftoppm", "-r", "200", "-f", "70", "-l", "70", "-png", str(INPUTS / "moh1983_jram340_configurations_of_roots.pdf"), str(prefix)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    images = sorted(out_dir.glob("moh-p209-pdf70-*.png"))
    return {
        "printed_page": 209,
        "pdf_page": 70,
        "pdftoppm": " ".join(["pdftoppm", "-r", "200", "-f", "70", "-l", "70", "-png", "moh1983_jram340_configurations_of_roots.pdf", str(prefix.relative_to(ROOT))]),
        "stderr": proc.stderr,
        "images": [{"path": str(p.relative_to(ROOT)), "sha256": sha256_file(p), "bytes": p.stat().st_size} for p in images],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_subset = sub.add_parser("subset")
    p_subset.add_argument("--t", type=int, nargs="+", default=[1, 2, 3, 4])

    p_direct = sub.add_parser("direct")
    p_direct.add_argument("--t", type=int, required=True)
    p_direct.add_argument("--characteristic", type=int, nargs="+", default=[0])
    p_direct.add_argument("--method", choices=["std", "slimgb"], default="std")

    p_pre = sub.add_parser("preprocess")
    p_pre.add_argument("--t", type=int, required=True)
    p_pre.add_argument("--characteristic", type=int, nargs="+", default=[0])
    p_pre.add_argument("--max-seconds", type=float, default=900.0)
    p_pre.add_argument("--max-bytes", type=int, default=60_000_000)

    p_run = sub.add_parser("run")
    p_run.add_argument("singular", nargs="+")
    p_run.add_argument("--timeout", type=float, default=None)

    sub.add_parser("moh-page")

    args = parser.parse_args()
    hashes = check_expected()
    if args.cmd == "subset":
        result = {"frozen_hashes": hashes, "subset": subset_audit(args.t)}
        path = HERE / ("subset_audit_t%s.json" % "_".join(map(str, args.t)))
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, sort_keys=True))
    elif args.cmd == "direct":
        result = {"frozen_hashes": hashes, "direct": write_direct(args.t, args.characteristic, args.method)}
        print(json.dumps(result, indent=2, sort_keys=True))
    elif args.cmd == "preprocess":
        result = {"frozen_hashes": hashes, "preprocess": write_preprocessed(args.t, args.characteristic, args.max_seconds, args.max_bytes)}
        print(json.dumps(result, indent=2, sort_keys=True))
    elif args.cmd == "run":
        results = [run_singular((ROOT / item).resolve() if not pathlib.Path(item).is_absolute() else pathlib.Path(item), timeout=args.timeout) for item in args.singular]
        print(json.dumps({"frozen_hashes": hashes, "runs": results}, indent=2, sort_keys=True))
    elif args.cmd == "moh-page":
        result = {"frozen_hashes": hashes, "moh_page": render_moh_page()}
        path = HERE / "moh_page_209_render.json"
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
