#!/usr/bin/env python3
"""AWS-only exact receiver compiler for the normalized p=0 odd sheet."""

from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
from hashlib import sha256
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import sys
from typing import Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DESIGN = ROOT / "xmodel/max12-812-order2-p0-odd-sheet-terminal-taylor-pullback-design-20260826.md"
ODD_DESIGN = ROOT / "xmodel/max12-812-order2-p0-odd-face-g11-g12-design-20260826.md"
ODD_COMPILER = ROOT / "cases/max12_812_order2_p0_odd_face_g11_g12_20260826/compile_p0_odd_g11_g12.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE_COMPILER = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py"
SHARED = ROOT / "cases/max12_high_row_probe_20260824/shared_faber_probe.py"
STRICT_CLIENT = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md"
ONEPARAM_PROMOTION = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md"
SHARP_PROMOTION = ROOT / "xmodel/max12-812-order2-square-third-tail-sharp-v2-promotion-20260826.md"
CONTACT_CLOSURE = ROOT / "xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md"

EXPECTED_STATIC = {
    DESIGN: "68ccd9f24318473039ce56e969915663df6bf538c5fcf72a98055f605daab4a0",
    ODD_DESIGN: "fea8194c2cb959dd4eb0d2de0955162669a834f3ac68924e72349dc0b8f4156e",
    ODD_COMPILER: "e8db8b5a2026647bcc291bf930f9bd39f9f13ebd68bf222f822fd9ac1cdfa439",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "840a12e29386d37801f986e39273c3fb34f5542019cc1da7043ee1730dcb31f2",
    SHARED: "69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f",
    STRICT_CLIENT: "e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7",
    ONEPARAM_PROMOTION: "82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f",
    SHARP_PROMOTION: "dfc448503b1ce05a7ef0ee21d01c0c9aaf5531c0ca6bdc9bbdf82032461d784e",
    CONTACT_CLOSURE: "3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_GRADE = 38


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("receiver compiler is restricted to a registered AWS EC2 lane")
    return tag


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical_tails() -> dict[str, list[list[object]]]:
    tails = json.loads(TAILS.read_text())
    encoded = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(encoded.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    return tails


class Dag:
    """Small exact commutative expression DAG; it never distributes products."""

    def __init__(self) -> None:
        self.nodes: list[dict[str, object]] = []
        self.cache: dict[tuple[object, ...], int] = {}
        self.zero = self.const(Fraction(0))
        self.one = self.const(Fraction(1))

    def _intern(self, key: tuple[object, ...], payload: dict[str, object]) -> int:
        old = self.cache.get(key)
        if old is not None:
            return old
        index = len(self.nodes)
        self.nodes.append(payload)
        self.cache[key] = index
        return index

    def const(self, value: Fraction | int) -> int:
        q = Fraction(value)
        return self._intern(
            ("c", q.numerator, q.denominator),
            {"op": "const", "n": q.numerator, "d": q.denominator},
        )

    def var(self, name: str) -> int:
        return self._intern(("v", name), {"op": "var", "name": name})

    def add(self, *items: int) -> int:
        flat: list[int] = []
        for item in items:
            if item == self.zero:
                continue
            node = self.nodes[item]
            if node["op"] == "add":
                flat.extend(int(v) for v in node["args"])
            else:
                flat.append(item)
        if not flat:
            return self.zero
        if len(flat) == 1:
            return flat[0]
        args = tuple(sorted(flat))
        return self._intern(("a",) + args, {"op": "add", "args": args})

    def mul(self, *items: int) -> int:
        flat: list[int] = []
        scalar = Fraction(1)
        for item in items:
            if item == self.zero:
                return self.zero
            node = self.nodes[item]
            if node["op"] == "const":
                scalar *= Fraction(int(node["n"]), int(node["d"]))
            elif node["op"] == "mul":
                for child in node["args"]:
                    child = int(child)
                    child_node = self.nodes[child]
                    if child_node["op"] == "const":
                        scalar *= Fraction(int(child_node["n"]), int(child_node["d"]))
                    else:
                        flat.append(child)
            else:
                flat.append(item)
        if scalar == 0:
            return self.zero
        if scalar != 1:
            flat.append(self.const(scalar))
        if not flat:
            return self.one
        if len(flat) == 1:
            return flat[0]
        args = tuple(sorted(flat))
        return self._intern(("m",) + args, {"op": "mul", "args": args})

    def scale(self, value: Fraction | int, item: int) -> int:
        return self.mul(self.const(Fraction(value)), item)

    def neg(self, item: int) -> int:
        return self.scale(-1, item)


Series = list[int]


def series_zero(dag: Dag) -> Series:
    return [dag.zero] * (MAX_GRADE + 1)


def series_add(dag: Dag, *series: Series) -> Series:
    return [dag.add(*(s[i] for s in series)) for i in range(MAX_GRADE + 1)]


def series_scale(dag: Dag, value: Fraction | int, series: Series) -> Series:
    return [dag.scale(value, item) for item in series]


def series_shift(dag: Dag, series: Series, amount: int) -> Series:
    out = series_zero(dag)
    for i in range(MAX_GRADE + 1 - amount):
        out[i + amount] = series[i]
    return out


def series_mul(dag: Dag, left: Series, right: Series) -> Series:
    out = series_zero(dag)
    for degree in range(MAX_GRADE + 1):
        terms = []
        for i in range(degree + 1):
            if left[i] != dag.zero and right[degree - i] != dag.zero:
                terms.append(dag.mul(left[i], right[degree - i]))
        out[degree] = dag.add(*terms)
    return out


def series_pow(dag: Dag, series: Series, exponent: int) -> Series:
    out = series_zero(dag)
    out[0] = dag.one
    base = series
    power = exponent
    while power:
        if power & 1:
            out = series_mul(dag, out, base)
        power //= 2
        if power:
            base = series_mul(dag, base, base)
    return out


def named_series(
    dag: Dag,
    entries: Iterable[tuple[int, str | int]],
) -> Series:
    out = series_zero(dag)
    for degree, value in entries:
        out[degree] = dag.var(value) if isinstance(value, str) else dag.const(value)
    return out


def range_series(dag: Dag, prefix: str, first: int, last: int) -> Series:
    return named_series(dag, ((i, f"{prefix}{i}") for i in range(first, last + 1)))


def all_expression_shas(nodes: list[dict[str, object]]) -> list[str]:
    answer: list[str] = []
    for node in nodes:
        if node["op"] == "const":
            text = f"c:{node['n']}/{node['d']}"
        elif node["op"] == "var":
            text = f"v:{node['name']}"
        else:
            children = ",".join(answer[int(i)] for i in node["args"])
            text = f"{node['op']}({children})"
        answer.append(sha256(text.encode()).hexdigest())
    return answer


def target_masks(nodes: list[dict[str, object]]) -> list[int]:
    bits = {
        "mu2_0": 1,
        "mu4_0": 2,
        "mu6_0": 4,
        "J0": 8,
    }
    answer: list[int] = []
    for node in nodes:
        if node["op"] == "var":
            mask = bits.get(str(node["name"]), 0)
        elif node["op"] in ("add", "mul"):
            mask = 0
            for child in node["args"]:
                mask |= answer[int(child)]
        else:
            mask = 0
        answer.append(mask)
    return answer


def terminal_source(dag: Dag, tails: dict[str, list[list[object]]]):
    # Primitive series after the reduced predecessor substitutions, but before F.
    p = series_zero(dag)
    p[2] = dag.scale(2, dag.var("ell2"))
    for i in range(3, MAX_GRADE + 1):
        p[i] = dag.scale(2, dag.var(f"ell{i}"))

    cs = range_series(dag, "cs", 1, 36)
    cs[0] = dag.var("b")
    c = series_shift(dag, cs, 2)

    rs = range_series(dag, "rs", 1, 36)
    r = series_scale(
        dag,
        Fraction(1, 4),
        series_add(dag, series_mul(dag, p, p), series_shift(dag, rs, 2)),
    )

    az = range_series(dag, "az", 2, 33)
    az[0] = dag.var("a1")
    az[1] = dag.var("aa1")
    ac = range_series(dag, "ac", 2, 33)
    ac[1] = dag.var("aa0")

    b = dag.var("b")
    w = dag.var("w")
    e1 = dag.mul(b, b, w)
    ez = range_series(dag, "ez", 3, 33)
    ez[1] = e1
    ez[2] = dag.var("ee1")
    ec = range_series(dag, "ec", 3, 33)
    ec[2] = dag.var("ee0")

    n3 = series_shift(dag, az, 3)
    n2 = series_shift(dag, ac, 3)
    n1 = series_shift(
        dag,
        series_scale(dag, Fraction(1, 2), series_add(dag, series_mul(dag, p, az), ez)),
        3,
    )
    n0 = series_shift(
        dag,
        series_scale(dag, Fraction(1, 2), series_add(dag, series_mul(dag, p, ac), ec)),
        3,
    )

    coeffs: dict[int, Series] = {
        6: series_scale(dag, 2, p),
        5: series_scale(dag, 2, c),
        4: series_add(dag, series_mul(dag, p, p), series_scale(dag, 2, r)),
        3: series_add(dag, series_scale(dag, 2, series_mul(dag, p, c)), series_shift(dag, n3, 2)),
        2: series_add(
            dag,
            series_mul(dag, c, c),
            series_scale(dag, 2, series_mul(dag, p, r)),
            series_shift(dag, n2, 2),
        ),
        1: series_add(dag, series_scale(dag, 2, series_mul(dag, c, r)), series_shift(dag, n1, 2)),
        0: series_add(dag, series_mul(dag, r, r), series_shift(dag, n0, 2)),
    }

    k10 = range_series(dag, "k10_", 1, 34)
    k10[0] = dag.scale(Fraction(12, 5), dag.mul(w, w))
    k6 = range_series(dag, "k6_", 0, 26)
    k2 = range_series(dag, "k2_", 0, 18)
    loads = {
        7: series_shift(dag, k10, 4),
        8: series_shift(dag, k6, 12),
        9: series_shift(dag, k2, 20),
    }

    targets = {
        2: range_series(dag, "mu2_", 0, 10),
        4: range_series(dag, "mu4_", 0, 6),
        6: range_series(dag, "mu6_", 0, 2),
        7: series_scale(dag, Fraction(1, 4), named_series(dag, [(0, "J0")])),
    }

    rows: dict[tuple[int, int], int] = {}
    source_rows: dict[tuple[int, int], int] = {}
    for ell in range(1, 8):
        total = series_zero(dag)
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10:
                fail(("tail monomial width", ell, monomial))
            weights = [8 - i for i in range(7)] + [2, 6, 10]
            if sum(e * wt for e, wt in zip(monomial, weights)) != 12 + ell:
                fail(("tail weight", ell, monomial))
            term = series_zero(dag)
            term[0] = dag.const(Fraction(str(raw_coefficient)))
            for i, exponent in enumerate(monomial[:7]):
                if exponent:
                    term = series_mul(dag, term, series_pow(dag, coeffs[i], exponent))
            for i, exponent in enumerate(monomial[7:], start=7):
                if exponent not in (0, 1):
                    fail(("load nonlinearity", ell, monomial))
                if exponent:
                    term = series_mul(dag, term, loads[i])
            total = series_add(dag, total, term)
        for degree in range(13, MAX_GRADE + 1):
            source_rows[(ell, degree)] = total[degree]
        if ell in targets:
            total = series_add(
                dag,
                total,
                series_scale(dag, -1, series_shift(dag, targets[ell], 2 * (12 + ell))),
            )
        for degree in range(13, MAX_GRADE + 1):
            rows[(ell, degree)] = total[degree]

    k0 = dag.scale(Fraction(12, 5), dag.mul(w, w))
    predecessor_f = dag.add(
        dag.scale(Fraction(3, 8), dag.add(dag.mul(dag.var("a1"), dag.var("ee0")), dag.mul(dag.var("aa0"), e1))),
        dag.scale(Fraction(-3, 8), dag.mul(b, dag.var("a1"), dag.var("a1"))),
        dag.scale(Fraction(15, 256), dag.mul(k0, b, dag.var("rs1"), dag.var("rs1"))),
        dag.scale(Fraction(-5, 16), dag.mul(k0, dag.var("ell2"), b, b, b)),
    )
    return rows, source_rows, predecessor_f


def emit_terminal(output: Path, tails: dict[str, list[list[object]]], characteristic: int) -> dict[str, object]:
    if characteristic != 0:
        fail("the first terminal DAG lane is registered over exact Q")
    dag = Dag()
    rows, source_rows, predecessor_f = terminal_source(dag, tails)

    expected_first_rows = {
        (2, 28): dag.add(source_rows[(2, 28)], dag.neg(dag.var("mu2_0"))),
        (4, 32): dag.add(source_rows[(4, 32)], dag.neg(dag.var("mu4_0"))),
        (6, 36): dag.add(source_rows[(6, 36)], dag.neg(dag.var("mu6_0"))),
        (7, 38): dag.add(source_rows[(7, 38)], dag.scale(Fraction(-1, 4), dag.var("J0"))),
    }
    if any(rows[key] != expected for key, expected in expected_first_rows.items()):
        fail("first target coefficient failed its exact structural identity")

    hashes = all_expression_shas(dag.nodes)
    masks = target_masks(dag.nodes)
    if any(masks[root] for root in source_rows.values()):
        fail("a target variable leaked into an uncharged source row")
    first_target_masks = {
        (2, 28): 1,
        (4, 32): 2,
        (6, 36): 4,
        (7, 38): 8,
    }
    for key, expected_mask in first_target_masks.items():
        if masks[rows[key]] != expected_mask:
            fail(("wrong first target grade", key, masks[rows[key]], expected_mask))

    # Exact target-grade contract.  Targets do not occur in source_rows by construction.
    target_contract = {
        "mu2_0": {"row": 2, "grade": 28, "coefficient": "-1"},
        "mu4_0": {"row": 4, "grade": 32, "coefficient": "-1"},
        "mu6_0": {"row": 6, "grade": 36, "coefficient": "-1"},
        "J0": {"row": 7, "grade": 38, "coefficient": "-1/4"},
    }
    row_manifest = []
    for ell in range(1, 8):
        for degree in range(13, MAX_GRADE + 1):
            row_manifest.append(
                {
                    "row": ell,
                    "grade": degree,
                    "source_root": source_rows[(ell, degree)],
                    "source_sha256": hashes[source_rows[(ell, degree)]],
                    "full_root": rows[(ell, degree)],
                    "full_sha256": hashes[rows[(ell, degree)]],
                }
            )

    dag_payload = {
        "format": "JC2_COMMUTATIVE_FACTOR_DAG_V1",
        "normalization": {"e1": "b^2*w", "k0": "12*w^2/5", "open": "b*w!=0"},
        "raw_predecessor_F_root": predecessor_f,
        "raw_predecessor_F_sha256": hashes[predecessor_f],
        "rows": row_manifest,
        "nodes": dag.nodes,
    }
    dag_path = output / "terminal_raw_dag.json.gz"
    with gzip.open(dag_path, "wt", encoding="utf-8", compresslevel=6) as stream:
        json.dump(dag_payload, stream, sort_keys=True, separators=(",", ":"))
        stream.write("\n")

    result = {
        "status": "PASS-P0-ODD-TERMINAL-RAW-DAG-TYPED",
        "scope": "INFINITY_SOURCE_GRADES_13_TO_38_RAW_NO_UNIT_LIFT_OR_ORDER2_VERDICT",
        "characteristic": 0,
        "dag_nodes": len(dag.nodes),
        "raw_rows": len(row_manifest),
        "target_contract": target_contract,
        "target_contract_status": "PASS_EXACT_FIRST_GRADES",
        "all_corrections": {
            "p": "ell2..ell38",
            "c": "b,cs1..cs36",
            "r": "rs1..rs36",
            "A_z": "a1,aa1,az2..az33",
            "A_0": "aa0,ac2..ac33",
            "C_z": "b^2*w,ee1,ez3..ez33",
            "C_0": "ee0,ec3..ec33",
            "k10": "12*w^2/5,k10_1..k10_34",
            "k6": "k6_0..k6_26",
            "k2": "k2_0..k2_18",
            "targets": "mu2_0..10,mu4_0..6,mu6_0..2,J0",
        },
        "raw_predecessor_retained": True,
        "localized_by": "b*w only (not performed in this emitter)",
        "gate_A_needed_for_terminal_infinity": False,
        "dag_sha256": digest(dag_path),
        "mathematical_endpoint": "RAW_TYPED_NOT_SOLVED",
    }
    return result


def build_faber_g(shared):
    names = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
    ring = shared.Ring(names)
    one = ring.one
    shifted_f = {i - 8: ring.var(f"a{i}") for i in range(7)}
    faber = {}
    for degree in range(13):
        polynomial = {degree: one}
        power = {0: one}
        for exponent in range(1, degree // 2 + 1):
            power = shared.zmul(power, shifted_f)
            contribution = {
                zdegree + degree: coefficient
                for zdegree, coefficient in power.items()
                if zdegree + degree >= 0
            }
            polynomial = shared.zadd(
                polynomial,
                shared.zscale(shared.binomial(Fraction(degree, 8), exponent), contribution),
            )
        faber[degree] = shared.zclean(polynomial)
    g = dict(faber[12])
    for degree in (10, 6, 2):
        load = ring.var(f"k{degree}")
        g = shared.zadd(
            g,
            {zdegree: shared.cmul(load, coefficient) for zdegree, coefficient in faber[degree].items()},
        )
    return ring, g


def serialize_tail(tail) -> list[list[object]]:
    return [[list(monomial), str(coefficient)] for monomial, coefficient in sorted(tail.items())]


def modular_fraction(value: Fraction, prime: int) -> int | None:
    if prime == 0:
        return None
    if value.denominator % prime == 0:
        fail(("bad Taylor control prime", value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def taylor_terms_for_family(
    family: str,
    degree: int,
    coefficient_polynomials: dict[int, dict[tuple[int, ...], Fraction]],
    prime: int,
) -> dict[str, list[dict[str, object]]]:
    answer: dict[str, list[dict[str, object]]] = {}
    weights = [8 - i for i in range(7)] + [2, 6, 10]
    expected_weight = 8 if family == "P" else 12
    for ell in range(degree + 1):
        terms = []
        for zdegree in sorted(coefficient_polynomials):
            if zdegree < ell:
                continue
            for monomial, coefficient in sorted(coefficient_polynomials[zdegree].items()):
                if sum(e * wt for e, wt in zip(monomial, weights)) + zdegree != expected_weight:
                    fail(("Taylor Faber weight", family, ell, zdegree, monomial))
                odd_count = sum(monomial[i] for i in (1, 3, 5))
                if (zdegree + odd_count) % 2:
                    fail(("Taylor character parity", family, ell, zdegree, monomial))
                half = (zdegree + odd_count) // 2
                q = coefficient * math.comb(zdegree, ell)
                terms.append(
                    {
                        "coefficient_Q": str(q),
                        "coefficient_mod_p": modular_fraction(q, prime),
                        "z_degree": zdegree,
                        "A_exponents": list(monomial[:7]),
                        "load_exponents": list(monomial[7:]),
                        "R0_exponent": zdegree - ell,
                        "odd_coefficient_count": odd_count,
                        "x_exponent": (3 * zdegree - odd_count) // 2,
                        "x_minus_1_exponent": half,
                    }
                )
        answer[str(ell)] = terms
    return answer


def emit_taylor(
    output: Path,
    tails: dict[str, list[list[object]]],
    characteristic: int,
    branch: int,
) -> dict[str, object]:
    shared = load_module("p0_odd_receivers_shared_faber", SHARED)
    base = load_module("p0_odd_receivers_base_compiler", BASE_COMPILER)
    _, rebuilt_tails = base.build_faber_and_tails(shared)
    rebuilt = {str(ell): serialize_tail(rebuilt_tails[ell]) for ell in range(1, 8)}
    if rebuilt != tails:
        fail("independent exact Faber reconstruction did not reproduce tails.json")

    ring, g = build_faber_g(shared)
    zero_monomial = tuple(0 for _ in ring.names)
    f_coefficients: dict[int, dict[tuple[int, ...], Fraction]] = {8: {zero_monomial: Fraction(1)}}
    for i in range(7):
        f_coefficients[i] = ring.var(f"a{i}")

    p_terms = taylor_terms_for_family("P", 8, f_coefficients, characteristic)
    q_terms = taylor_terms_for_family("Q", 12, g, characteristic)
    branch_payload = {
        "branch": f"x={branch}",
        "uniformizer": "s0" if branch == 0 else "s1",
        "x_substitution": "x=s0^2" if branch == 0 else "x=1+s1^2",
        "u_x_substitution": (
            "u_x=s0^3*eta0, eta0^2=s0^2-1"
            if branch == 0
            else "u_x=s1*eta1, eta1^2=(1+s1^2)^3"
        ),
        "R0_base_order_lower_bound": -12 if branch == 0 else -4,
        "P": p_terms,
        "Q": q_terms,
    }
    path = output / f"taylor_x{branch}_typed_terms.json.gz"
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=6) as stream:
        json.dump(branch_payload, stream, sort_keys=True, separators=(",", ":"))
        stream.write("\n")

    p_count = sum(len(items) for items in p_terms.values())
    q_count = sum(len(items) for items in q_terms.values())
    return {
        "status": f"PASS-P0-ODD-TAYLOR-X{branch}-TYPED-WAITING-GATE-A",
        "scope": f"UNIVERSAL_X{branch}_P_AND_Q_TAYLOR_TERMS_NO_GLOBAL_GERMS_OR_REGULARITY_VERDICT",
        "characteristic": characteristic,
        "exact_Q_coefficients_retained": True,
        "modular_control": characteristic if characteristic else None,
        "faber_reconstruction": "PASS_EXACT_ALL_SEVEN_TAILS",
        "P_coordinate_count": 9,
        "Q_coordinate_count": 13,
        "P_term_count": p_count,
        "Q_term_count": q_count,
        "parity_and_weight_checks": "PASS",
        "gate_A": "REQUIRED_NOT_PROVED",
        "finite_regularity": "NOT_EVALUATED",
        "typed_terms_sha256": digest(path),
        "mathematical_endpoint": "TYPED_WAITING_GATE_A",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("terminal", "taylor0", "taylor1"), required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED_STATIC.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen source mismatch", str(path), actual, expected))
    tails = canonical_tails()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    if args.mode == "terminal":
        result = emit_terminal(output, tails, args.characteristic)
    else:
        result = emit_taylor(output, tails, args.characteristic, int(args.mode[-1]))
    result.update(
        {
            "registered_aws_lane": tag,
            "mode": args.mode,
            "design_sha256": digest(DESIGN),
            "tails_sha256": digest(TAILS),
            "all_tails_sha256": EXPECTED_ALL_TAILS,
            "gate_A_definition": "sheet-to-global A_i(x),R0(x) algebraization and two-sided overlap",
            "order2_closed": False,
            "JC2": "NOT_CLAIMED",
        }
    )
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_RECEIVER_SOURCE_HASHES=PASS")
    print(f"P0_ODD_RECEIVER_MODE={args.mode}")
    print(f"P0_ODD_RECEIVER_STATUS={result['status']}")
    print(f"P0_ODD_RECEIVER_MATHEMATICAL_ENDPOINT={result['mathematical_endpoint']}")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
