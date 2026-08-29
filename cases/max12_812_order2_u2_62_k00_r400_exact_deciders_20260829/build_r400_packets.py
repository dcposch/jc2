#!/usr/bin/env python3
"""Build exact R4-00 R1/R2 decision packets from the frozen literal tails.

This compiler deliberately does not consume any polynomial printed in the
producer report.  The report is hash-pinned as the typing/provenance packet;
all equations below are expanded anew from tails.json under the coordinate,
load, target, and truncation conventions pinned by the V20R2 compiler.

The expansion is potentially memory-heavy and is therefore AWS-only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import platform
import re
from typing import Iterable


TRUNCATION = 20
TAIL_WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 2, 6, 10]
FORMAT = "K00_R400_EXACT_PACKET_V1"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = ROOT / "xmodel/k00-r4-00-entry-solve-fable5-20260829.md"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
COMPILER = ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py"
EXPECTED = {
    REPORT: "0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
}

# A6/B6 and A7/B7 are retained long enough to replay the two forcing steps,
# then set to zero for both typed residuals.  q/ii and open variables are
# present in the common ambient namespace so substitutions never rename a
# monomial silently.
VARIABLES = [
    "s", "t", "s1", "t1", "kappa", "az", "bz", "uz", "vz", "A6", "B6",
]
for _m in range(7, 14):
    VARIABLES.extend([f"a{_m}", f"b{_m}", f"u{_m}", f"v{_m}", f"A{_m}", f"B{_m}"])
VARIABLES.extend([f"k10_{j}" for j in range(1, 10)])
VARIABLES.extend([f"k6_{j}" for j in range(1, 10)])
VARIABLES.extend([f"k2_{j}" for j in range(1, 6)])
VARIABLES.extend([f"mu2_{j}" for j in range(1, 6)])
VARIABLES.extend([f"mu4_{j}" for j in range(1, 4)])
VARIABLES.extend(["mu6_1", "Jdet_0", "q", "ii", "zinv", "ws", "wt", "jinv"])
INDEX = {name: index for index, name in enumerate(VARIABLES)}
NVAR = len(VARIABLES)
ZERO_MONOMIAL = (0,) * NVAR

# Sparse polynomial: exponent tuple -> exact rational coefficient.
Poly = dict[tuple[int, ...], Fraction]
Series = list[Poly]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("R4-00 packet compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("R4-00 packet compiler refused non-Amazon EC2 host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def const(value: int | Fraction) -> Poly:
    value = Fraction(value)
    return {} if value == 0 else {ZERO_MONOMIAL: value}


def var(name: str) -> Poly:
    monomial = [0] * NVAR
    monomial[INDEX[name]] = 1
    return {tuple(monomial): Fraction(1)}


def add(left: Poly, right: Poly, scale: int | Fraction = 1) -> Poly:
    factor = Fraction(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, Fraction(0)) + factor * coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def scale(poly: Poly, factor: int | Fraction) -> Poly:
    factor = Fraction(factor)
    if factor == 0:
        return {}
    return clean({monomial: coefficient * factor for monomial, coefficient in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return {}
    out: Poly = {}
    for lmon, lcoef in left.items():
        for rmon, rcoef in right.items():
            monomial = tuple(a + b for a, b in zip(lmon, rmon))
            out[monomial] = out.get(monomial, Fraction(0)) + lcoef * rcoef
    return clean(out)


def power(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        fail(("negative exponent", exponent))
    out = const(1)
    base = poly
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        exponent >>= 1
        if exponent:
            base = mul(base, base)
    return out


def zero_series() -> Series:
    return [{} for _ in range(TRUNCATION)]


def series_add(left: Series, right: Series) -> Series:
    return [add(a, b) for a, b in zip(left, right)]


def series_scale(series: Series, factor: int | Fraction) -> Series:
    return [scale(poly, factor) for poly in series]


def series_mul(left: Series, right: Series) -> Series:
    out = zero_series()
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: TRUNCATION - i]):
            if b:
                out[i + j] = add(out[i + j], mul(a, b))
    return out


def series_power(series: Series, exponent: int) -> Series:
    out = zero_series()
    out[0] = const(1)
    base = series
    while exponent:
        if exponent & 1:
            out = series_mul(out, base)
        exponent >>= 1
        if exponent:
            base = series_mul(base, base)
    return out


def series_shift(series: Series, amount: int) -> Series:
    if amount < 0:
        fail(("negative shift", amount))
    return [{} for _ in range(min(amount, TRUNCATION))] + series[: max(0, TRUNCATION - amount)]


def put(series: Series, grade: int, poly: Poly) -> None:
    series[grade] = poly


def linear(*items: tuple[int | Fraction, Poly]) -> Poly:
    out: Poly = {}
    for coefficient, poly in items:
        out = add(out, poly, coefficient)
    return out


def source_series() -> dict[str, Series]:
    d = [zero_series() for _ in range(6)]
    s, t, s1, t1 = (var(name) for name in ("s", "t", "s1", "t1"))

    ell = lambda x, y: [scale(x, 2), scale(y, Fraction(1, 8)), x, y, x, scale(y, 2)]
    for grade, coordinates in ((4, ell(s, t)), (5, ell(s1, t1))):
        for index, poly in enumerate(coordinates):
            put(d[index], grade, poly)

    def adapted(a: Poly, b: Poly, u: Poly, v: Poly, A: Poly, B: Poly) -> list[Poly]:
        return [
            linear((2, b), (2, u), (1, B)),
            a,
            b,
            linear((8, a), (1, v)),
            add(b, u, -1),
            linear((16, a), (4, v), (1, A)),
        ]

    coordinates6 = adapted(var("az"), var("bz"), var("uz"), var("vz"), var("A6"), var("B6"))
    for index, poly in enumerate(coordinates6):
        put(d[index], 6, poly)
    for grade in range(7, 14):
        coordinates = adapted(*(var(f"{prefix}{grade}") for prefix in ("a", "b", "u", "v", "A", "B")))
        for index, poly in enumerate(coordinates):
            put(d[index], grade, poly)

    k10, k6, k2 = zero_series(), zero_series(), zero_series()
    put(k10, 0, var("kappa"))
    for j in range(1, 10):
        put(k10, j, var(f"k10_{j}"))
        put(k6, j, var(f"k6_{j}"))
    for j in range(1, 6):
        put(k2, j, var(f"k2_{j}"))

    mu2, mu4, mu6, jdet = zero_series(), zero_series(), zero_series(), zero_series()
    for j in range(1, 6):
        put(mu2, j, var(f"mu2_{j}"))
    for j in range(1, 4):
        put(mu4, j, var(f"mu4_{j}"))
    put(mu6, 1, var("mu6_1"))
    put(jdet, 0, var("Jdet_0"))
    return {
        **{f"d{i}": series for i, series in enumerate(d)},
        "k10": k10,
        "k6": k6,
        "k2": k2,
        "mu2": mu2,
        "mu4": mu4,
        "mu6": mu6,
        "Jdet": jdet,
    }


def normalized_coordinates(source: dict[str, Series]) -> list[Series]:
    one, three = zero_series(), zero_series()
    one[0], three[0] = const(1), const(3)
    return [
        series_scale(series_add(one, source["d0"]), Fraction(1, 256)),
        source["d1"],
        series_scale(series_add(one, source["d2"]), Fraction(1, 16)),
        source["d3"],
        series_scale(series_add(three, source["d4"]), Fraction(1, 8)),
        source["d5"],
        one,
    ]


def build_rows(tails: dict[str, list[list[object]]]) -> dict[tuple[int, int], Poly]:
    source = source_series()
    tail_series = normalized_coordinates(source) + [
        series_shift(source["k10"], 2),
        series_shift(source["k6"], 6),
        series_shift(source["k2"], 10),
    ]
    powers: dict[tuple[int, int], Series] = {}
    rows = [zero_series() for _ in range(7)]
    census = 0
    for ell in range(1, 8):
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            census += 1
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10 or any(value < 0 for value in monomial):
                fail(("malformed tail monomial", ell, monomial))
            if sum(a * b for a, b in zip(monomial, TAIL_WEIGHTS)) != 12 + ell:
                fail(("tail weight mismatch", ell, monomial))
            if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
                fail(("tail load nonlinearity", ell, monomial))
            term = zero_series()
            term[0] = const(Fraction(str(raw_coefficient)))
            for index, exponent in enumerate(monomial):
                if not exponent:
                    continue
                key = (index, exponent)
                if key not in powers:
                    powers[key] = series_power(tail_series[index], exponent)
                term = series_mul(term, powers[key])
            rows[ell - 1] = series_add(rows[ell - 1], term)
    if census != 569:
        fail(("tail census", census))

    for ell, name, shift, coefficient in (
        (2, "mu2", 14, Fraction(-1)),
        (4, "mu4", 16, Fraction(-1)),
        (6, "mu6", 18, Fraction(-1)),
        (7, "Jdet", 19, Fraction(-1, 4)),
    ):
        rows[ell - 1] = series_add(rows[ell - 1], series_scale(series_shift(source[name], shift), coefficient))
    return {(ell, grade): rows[ell - 1][grade] for ell in range(1, 8) for grade in range(TRUNCATION)}


def substitute(poly: Poly, replacements: dict[str, Poly]) -> Poly:
    if not replacements or not poly:
        return dict(poly)
    replacement_by_index = {INDEX[name]: value for name, value in replacements.items()}
    caches: dict[tuple[int, int], Poly] = {}
    out: Poly = {}
    for monomial, coefficient in poly.items():
        term = const(coefficient)
        for index, exponent in enumerate(monomial):
            if not exponent:
                continue
            if index in replacement_by_index:
                key = (index, exponent)
                if key not in caches:
                    caches[key] = power(replacement_by_index[index], exponent)
                factor = caches[key]
            else:
                new_monomial = [0] * NVAR
                new_monomial[index] = exponent
                factor = {tuple(new_monomial): Fraction(1)}
            term = mul(term, factor)
        out = add(out, term)
    return out


def coefficient(poly: Poly, name: str, exponent: int = 1) -> Poly:
    index = INDEX[name]
    out: Poly = {}
    for monomial, value in poly.items():
        if monomial[index] != exponent:
            continue
        lowered = list(monomial)
        lowered[index] = 0
        out[tuple(lowered)] = value
    return out


def reduce_i(poly: Poly) -> Poly:
    """Return the canonical representative modulo ii^2+1."""

    index = INDEX["ii"]
    out: Poly = {}
    for monomial, value in poly.items():
        exponent = monomial[index]
        reduced = list(monomial)
        reduced[index] = exponent % 2
        out = add(out, {tuple(reduced): value * ((-1) ** (exponent // 2))})
    return out


def support(poly: Poly) -> set[str]:
    return {VARIABLES[index] for monomial in poly for index, exponent in enumerate(monomial) if exponent}


def evaluate(poly: Poly, assignment: dict[str, Fraction]) -> Fraction:
    total = Fraction(0)
    for monomial, coefficient_value in poly.items():
        value = coefficient_value
        for index, exponent in enumerate(monomial):
            if exponent:
                value *= assignment[VARIABLES[index]] ** exponent
        total += value
    return total


def lcm(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result = math.lcm(result, value)
    return result


def primitive_integer(poly: Poly) -> tuple[Poly, dict[str, int]]:
    if not poly:
        fail("zero generator cannot be serialized")
    denominator = lcm(coefficient.denominator for coefficient in poly.values())
    integers = [coefficient.numerator * (denominator // coefficient.denominator) for coefficient in poly.values()]
    divisor = reduce(math.gcd, (abs(value) for value in integers))
    scaled = scale(poly, Fraction(denominator, divisor))
    first = next(value for _, value in sorted(scaled.items()) if value)
    sign = -1 if first < 0 else 1
    if sign < 0:
        scaled = scale(scaled, -1)
    if any(value.denominator != 1 for value in scaled.values()):
        fail("primitive integer normalization failed")
    return scaled, {"cleared_denominator": denominator, "content": divisor, "sign": sign}


def poly_text(poly: Poly, *, integer_required: bool = False) -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for monomial, coefficient_value in sorted(poly.items()):
        if integer_required and coefficient_value.denominator != 1:
            fail("noninteger packet coefficient")
        factors = [
            VARIABLES[index] if exponent == 1 else f"{VARIABLES[index]}^{exponent}"
            for index, exponent in enumerate(monomial)
            if exponent
        ]
        body = "*".join(factors)
        if coefficient_value.denominator == 1:
            number = str(abs(coefficient_value.numerator))
        else:
            number = f"({abs(coefficient_value.numerator)}/{coefficient_value.denominator})"
        term = number if not body else (body if number == "1" else f"{number}*{body}")
        if not terms:
            terms.append(("-" if coefficient_value < 0 else "") + term)
        else:
            terms.append(("-" if coefficient_value < 0 else "+") + term)
    return "".join(terms)


def exact_sparse(poly: Poly) -> list[list[object]]:
    return [
        [
            [[VARIABLES[index], exponent] for index, exponent in enumerate(monomial) if exponent],
            str(coefficient_value),
        ]
        for monomial, coefficient_value in sorted(poly.items())
    ]


def numeric_zero() -> list[Fraction]:
    return [Fraction(0)] * TRUNCATION


def numeric_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [a + b for a, b in zip(left, right)]


def numeric_scale(series: list[Fraction], factor: Fraction) -> list[Fraction]:
    return [factor * value for value in series]


def numeric_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = numeric_zero()
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: TRUNCATION - i]):
            out[i + j] += a * b
    return out


def numeric_power(series: list[Fraction], exponent: int) -> list[Fraction]:
    out = numeric_zero()
    out[0] = Fraction(1)
    base = series
    while exponent:
        if exponent & 1:
            out = numeric_mul(out, base)
        exponent >>= 1
        if exponent:
            base = numeric_mul(base, base)
    return out


def numeric_shift(series: list[Fraction], amount: int) -> list[Fraction]:
    return [Fraction(0)] * amount + series[: TRUNCATION - amount]


def numeric_source(assignment: dict[str, Fraction]) -> dict[str, list[Fraction]]:
    result = {f"d{i}": numeric_zero() for i in range(6)}
    def adapted(a: Fraction, b: Fraction, u: Fraction, v: Fraction, A: Fraction, B: Fraction) -> list[Fraction]:
        return [2 * b + 2 * u + B, a, b, 8 * a + v, b - u, 16 * a + 4 * v + A]
    ell = lambda x, y: [2 * x, y / 8, x, y, x, 2 * y]
    for grade, coordinates in ((4, ell(assignment["s"], assignment["t"])),
                               (5, ell(assignment["s1"], assignment["t1"]))):
        for index, value in enumerate(coordinates):
            result[f"d{index}"][grade] = value
    coordinates = adapted(*(assignment[name] for name in ("az", "bz", "uz", "vz", "A6", "B6")))
    for index, value in enumerate(coordinates):
        result[f"d{index}"][6] = value
    for grade in range(7, 14):
        coordinates = adapted(*(assignment[f"{prefix}{grade}"] for prefix in ("a", "b", "u", "v", "A", "B")))
        for index, value in enumerate(coordinates):
            result[f"d{index}"][grade] = value
    for name in ("k10", "k6", "k2", "mu2", "mu4", "mu6", "Jdet"):
        result[name] = numeric_zero()
    result["k10"][0] = assignment["kappa"]
    for j in range(1, 10):
        result["k10"][j] = assignment[f"k10_{j}"]
        result["k6"][j] = assignment[f"k6_{j}"]
    for j in range(1, 6):
        result["k2"][j] = assignment[f"k2_{j}"]
        result["mu2"][j] = assignment[f"mu2_{j}"]
    for j in range(1, 4):
        result["mu4"][j] = assignment[f"mu4_{j}"]
    result["mu6"][1] = assignment["mu6_1"]
    result["Jdet"][0] = assignment["Jdet_0"]
    return result


def numeric_direct_rows(tails: dict[str, list[list[object]]], assignment: dict[str, Fraction],
                        *, target_sign: int = -1, mutate_row4: bool = False) -> dict[tuple[int, int], Fraction]:
    source = numeric_source(assignment)
    one, three = numeric_zero(), numeric_zero()
    one[0], three[0] = Fraction(1), Fraction(3)
    coordinates = [
        numeric_scale(numeric_add(one, source["d0"]), Fraction(1, 256)),
        source["d1"],
        numeric_scale(numeric_add(one, source["d2"]), Fraction(1, 16)),
        source["d3"],
        numeric_scale(numeric_add(three, source["d4"]), Fraction(1, 8)),
        source["d5"],
        one,
        numeric_shift(source["k10"], 2),
        numeric_shift(source["k6"], 6),
        numeric_shift(source["k2"], 10),
    ]
    powers: dict[tuple[int, int], list[Fraction]] = {}
    rows = [numeric_zero() for _ in range(7)]
    mutation_target = [0, 0, 0, 0, 0, 2, 5, 0, 0, 0]
    mutation_seen = 0
    for ell in range(1, 8):
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            coefficient_value = Fraction(str(raw_coefficient))
            if mutate_row4 and ell == 4 and list(raw_monomial) == mutation_target:
                coefficient_value += 1
                mutation_seen += 1
            term = numeric_zero()
            term[0] = coefficient_value
            for index, exponent in enumerate(raw_monomial):
                exponent = int(exponent)
                if not exponent:
                    continue
                key = (index, exponent)
                if key not in powers:
                    powers[key] = numeric_power(coordinates[index], exponent)
                term = numeric_mul(term, powers[key])
            rows[ell - 1] = numeric_add(rows[ell - 1], term)
    if mutate_row4 and mutation_seen != 1:
        fail(("row4 mutation target census", mutation_seen))
    for ell, name, shift, coefficient_value in (
        (2, "mu2", 14, Fraction(target_sign)),
        (4, "mu4", 16, Fraction(target_sign)),
        (6, "mu6", 18, Fraction(target_sign)),
        (7, "Jdet", 19, Fraction(target_sign, 4)),
    ):
        rows[ell - 1] = numeric_add(rows[ell - 1], numeric_scale(numeric_shift(source[name], shift), coefficient_value))
    return {(ell, grade): rows[ell - 1][grade] for ell in range(1, 8) for grade in range(TRUNCATION)}


def row_combo(rows: dict[tuple[int, int], Poly], grade: int, terms: list[tuple[int | Fraction, int]]) -> Poly:
    return linear(*( (coefficient_value, rows[(row, grade)]) for coefficient_value, row in terms))


def zero_forced(poly: Poly) -> Poly:
    return substitute(poly, {"A6": {}, "B6": {}, "A7": {}, "B7": {}})


def r1_substitution(epsilon: int) -> dict[str, Poly]:
    if epsilon not in (-1, 1):
        fail(("epsilon", epsilon))
    s, t, kappa, q, ii = (var(name) for name in ("s", "t", "kappa", "q", "ii"))
    return {
        "uz": scale(add(scale(mul(ii, q), 8 * epsilon), mul(kappa, s), -5), Fraction(1, 6)),
        "vz": scale(add(scale(mul(kappa, t), 5), q, -1), Fraction(1, 6)),
    }


def packet(output: Path, packet_id: str, core: list[tuple[str, Poly]], opens: list[tuple[str, Poly]],
           scope: str, route: str, source_hashes: dict[str, str]) -> dict[str, object]:
    named = core + opens
    if len({name for name, _ in named}) != len(named):
        fail(("duplicate generator label", packet_id))
    normalized: list[dict[str, object]] = []
    all_support: set[str] = set()
    for label, poly in named:
        primitive, normalization = primitive_integer(poly)
        all_support |= support(primitive)
        normalized.append({
            "label": label,
            "normalization": normalization,
            "singular": poly_text(primitive, integer_required=True),
            "sha256": sha256((poly_text(primitive, integer_required=True) + "\n").encode()).hexdigest(),
            "sparse": exact_sparse(primitive),
        })
    ordered_variables = [name for name in VARIABLES if name in all_support]
    payload: dict[str, object] = {
        "format": FORMAT,
        "packet_id": packet_id,
        "route": route,
        "field": "Qbar encoded over exact Q; R1 includes ii^2+1",
        "characteristic": 0,
        "variables": ordered_variables,
        "generators": normalized,
        "core_generator_count": len(core),
        "open_equation_count": len(opens),
        "scope": scope,
        "opens_encoding": "Rabinowitsch equations; s*ws+t*wt-1 encodes (s,t)!=(0,0)",
        "source_sha256": source_hashes,
        "msolve_unit_caveat": "char-0 [1] is screening only; exact Singular unit cofactor replay required",
    }
    json_path = output / f"{packet_id}.json"
    json_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    polynomials = [str(item["singular"]) for item in normalized]
    ms_path = output / f"{packet_id}.ms"
    ms_path.write_text(", ".join(ordered_variables) + "\n0\n" + ",\n".join(polynomials) + "\n")
    sing_path = output / f"{packet_id}.sing"
    sing_path.write_text(
        f"ring R=0,({','.join(ordered_variables)}),dp;\n"
        + "ideal J=" + ",\n".join(f"({value})" for value in polynomials) + ";\n"
        + f'print("PACKET_ID={packet_id}"); print("NGEN="+string(size(J))); print("DIM="+string(dim(std(J)))); quit;\n'
    )
    payload["artifacts"] = {
        json_path.name: digest(json_path),
        ms_path.name: digest(ms_path),
        sing_path.name: digest(sing_path),
    }
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    lane = require_aws()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen source hash mismatch", str(path), actual, expected))
    compiler_text = COMPILER.read_text()
    compiler_markers = (
        "TRUNCATION = 20",
        '"C0": "(1+d0)/256"',
        'target_specs = {2: ("mu2", 14, Fraction(target_sign)),',
        '7: ("Jdet", 19, Fraction(target_sign, 4))}',
    )
    # The exact compiler hash is the authority; these markers make a future
    # hash update fail legibly if it changes a convention this builder copied.
    if any(marker not in compiler_text for marker in compiler_markers):
        fail("pinned compiler convention marker missing")
    tails = json.loads(TAILS.read_text())
    if sorted(tails) != [str(index) for index in range(1, 8)]:
        fail(("tails keys", sorted(tails)))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    rows = build_rows(tails)

    # Exact forcing replays from literal source rows.
    c31_12 = row_combo(rows, 12, [(1, 3), (Fraction(1, 8), 1)])
    expected_c31_12 = scale(mul(var("A6"), var("B6")), Fraction(3, 16384))
    expected_g4_12 = scale(add(power(var("B6"), 2), scale(power(var("A6"), 2), -64)), Fraction(3, 524288))
    if c31_12 != expected_c31_12 or rows[(4, 12)] != expected_g4_12:
        fail("literal grade-12 cone forcing identity mismatch")

    rows_a6 = {key: substitute(value, {"A6": {}, "B6": {}}) for key, value in rows.items()}
    p = add(scale(var("uz"), 6), scale(mul(var("kappa"), var("s")), 5))
    qbase = add(scale(var("vz"), -6), scale(mul(var("kappa"), var("t")), 5))
    expected_t = {
        (1, "A7"): scale(p, Fraction(1, 2048)),
        (1, "B7"): scale(qbase, Fraction(1, 2048)),
        (2, "A7"): scale(qbase, Fraction(-1, 512)),
        (2, "B7"): scale(p, Fraction(1, 32768)),
    }
    for (row, name), expected in expected_t.items():
        if coefficient(rows_a6[(row, 13)], name) != expected:
            fail(("literal T coefficient mismatch", row, name))
    for row in range(1, 8):
        remainder = substitute(rows_a6[(row, 13)], {"A7": {}, "B7": {}})
        if remainder:
            fail(("grade13 non-T remainder", row, len(remainder)))
    c31_14 = row_combo(rows_a6, 14, [(1, 3), (Fraction(1, 8), 1)])
    expected_c31_14 = scale(mul(var("A7"), var("B7")), Fraction(3, 16384))
    expected_g4_14 = scale(add(power(var("B7"), 2), scale(power(var("A7"), 2), -64)), Fraction(3, 524288))
    if c31_14 != expected_c31_14 or rows_a6[(4, 14)] != expected_g4_14:
        fail("literal grade-14 A7/B7 forcing identity mismatch")

    residual = {key: zero_forced(value) for key, value in rows.items()}
    c31 = lambda grade: row_combo(residual, grade, [(1, 3), (Fraction(1, 8), 1)])
    d51 = lambda grade: row_combo(residual, grade, [(1, 5), (Fraction(1, 8), 3), (Fraction(3, 128), 1)])
    d71 = lambda grade: row_combo(residual, grade, [(1, 7), (Fraction(1, 128), 3), (Fraction(1, 512), 1)])

    r2_core = [
        ("G1_14", residual[(1, 14)]),
        ("G2_14", residual[(2, 14)]),
        ("C31_16", c31(16)),
        ("G4_16", residual[(4, 16)]),
        ("G6_18", residual[(6, 18)]),
        ("D51_18", d51(18)),
        ("D71_18", d71(18)),
    ]
    r2_allowed = {"s", "t", "kappa", "uz", "vz", "A8", "B8"}
    for label, poly in r2_core:
        if support(poly) - r2_allowed:
            fail(("R2 base generator has omitted-variable content", label, sorted(support(poly) - r2_allowed)))

    ii_relation = add(power(var("ii"), 2), const(1))
    branch_core: dict[int, list[tuple[str, Poly]]] = {}
    for epsilon in (1, -1):
        sub = r1_substitution(epsilon)
        branch_rows = {key: reduce_i(substitute(value, sub)) for key, value in residual.items()}
        # Insert ii into the coefficient only after forming eps/2 * row1.
        c21 = reduce_i(add(
            branch_rows[(2, 14)],
            mul(scale(var("ii"), Fraction(-epsilon, 2)), branch_rows[(1, 14)]),
        ))
        core = [
            ("II2_PLUS_1", ii_relation),
            ("C21_14", c21),
            ("G1_14", branch_rows[(1, 14)]),
            ("C31_16", row_combo(branch_rows, 16, [(1, 3), (Fraction(1, 8), 1)])),
            ("G4_16", branch_rows[(4, 16)]),
            ("G6_18", branch_rows[(6, 18)]),
            ("D51_18", row_combo(branch_rows, 18, [(1, 5), (Fraction(1, 8), 3), (Fraction(3, 128), 1)])),
            ("D71_18", row_combo(branch_rows, 18, [(1, 7), (Fraction(1, 128), 3), (Fraction(1, 512), 1)])),
        ]
        allowed = {"s", "t", "kappa", "q", "ii", "A8", "B8"}
        for label, poly in core:
            if support(poly) - allowed:
                fail(("R1 base generator has omitted-variable content", epsilon, label, sorted(support(poly) - allowed)))
        if "q" in support(c21) or "A8" in support(c21) or "B8" in support(c21):
            fail(("R1 closed grade14 generator failed cancellation", epsilon, sorted(support(c21))))
        branch_core[epsilon] = core

    conjugation = {"ii": scale(var("ii"), -1)}
    plus_map = {label: poly for label, poly in branch_core[1]}
    minus_map = {label: poly for label, poly in branch_core[-1]}
    for label in plus_map:
        if substitute(plus_map[label], conjugation) != minus_map[label]:
            fail(("R1 branch conjugation mismatch", label))

    # Literal full residual conditions; zero identities are omitted only after
    # exact expansion.  This is an existential grade-19 packet, not an arc.
    full_core_r2: list[tuple[str, Poly]] = []
    for grade in range(12, 20):
        for row in range(1, 8):
            value = residual[(row, grade)]
            if value:
                full_core_r2.append((f"G{row}_{grade}", value))
    if not full_core_r2:
        fail("empty full residual packet")

    expected_inert = {
        *(f"a{m}" for m in range(10, 14)), *(f"b{m}" for m in range(10, 14)),
        "u12", "v12", "u13", "v13",
        *(f"k10_{j}" for j in range(6, 10)), *(f"k6_{j}" for j in range(6, 10)),
    }
    full_support = set().union(*(support(poly) for _, poly in full_core_r2))
    if full_support & expected_inert:
        fail(("claimed inert variable occurs in literal full packet", sorted(full_support & expected_inert)))

    # Direct second implementation: every literal coefficient agrees at two
    # deterministic exact-Q fixtures.  Mutations must be visible.
    fixture_records = []
    for fixture in (1, 2):
        assignment: dict[str, Fraction] = {}
        for name in VARIABLES:
            raw = int.from_bytes(sha256(f"R400|{fixture}|{name}".encode()).digest()[:4], "big")
            assignment[name] = Fraction(raw % 7 - 3)
        assignment["kappa"] = Fraction(fixture + 1)
        assignment["Jdet_0"] = Fraction(fixture + 2)
        direct = numeric_direct_rows(tails, assignment)
        for key, poly in rows.items():
            if evaluate(poly, assignment) != direct[key]:
                fail(("direct literal-row fixture mismatch", fixture, key))
        wrong_sign = numeric_direct_rows(tails, assignment, target_sign=1)
        mutated = numeric_direct_rows(tails, assignment, mutate_row4=True)
        if wrong_sign == direct or mutated == direct:
            fail(("mandatory mutation survived", fixture))
        fixture_records.append({
            "fixture": fixture,
            "all_140_roots_match": True,
            "target_sign_mutation_detected": True,
            "row4_tail_mutation_detected": True,
            "assignment_sha256": sha256(canonical_json({key: str(value) for key, value in sorted(assignment.items())}).encode()).hexdigest(),
        })

    source_hashes = {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED}
    d_open = add(power(p, 2), scale(power(qbase, 2), 64))
    nonzero_st = add(add(mul(var("s"), var("ws")), mul(var("t"), var("wt"))), const(-1))
    r2_opens = [
        ("OPEN_D_KAPPA", add(mul(mul(d_open, var("kappa")), var("zinv")), const(-1))),
        ("OPEN_ST", nonzero_st),
    ]
    r1_opens = [
        ("OPEN_Q_KAPPA", add(mul(mul(var("q"), var("kappa")), var("zinv")), const(-1))),
        ("OPEN_ST", nonzero_st),
    ]
    j_open = ("OPEN_JDET", add(mul(var("Jdet_0"), var("jinv")), const(-1)))

    packets: dict[str, dict[str, object]] = {}
    packets["R2_BASE_LIFT"] = packet(
        output, "R2_BASE_LIFT", r2_core, r2_opens,
        "Exact CELL-R2 closed base through grade18 with D,kappa,(s,t) opens; no grade19 Jdet claim",
        "R4-00-R2-BASE-DECIDE", source_hashes,
    )
    for epsilon, suffix in ((1, "PLUS"), (-1, "MINUS")):
        packets[f"R1_{suffix}_BASE_LIFT"] = packet(
            output, f"R1_{suffix}_BASE_LIFT", branch_core[epsilon], r1_opens,
            f"Exact CELL-R1 eps={epsilon} closed base through grade18 over Q(ii), with q,kappa,(s,t) opens; no grade19 Jdet claim",
            "R4-00-R1-BASE-DECIDE", source_hashes,
        )

    packets["R2_FULL_GRADE19"] = packet(
        output, "R2_FULL_GRADE19", full_core_r2, r2_opens + [j_open],
        "Exact literal field-valued R4-00 CELL-R2 finite-jet equations through grade19; not an arc or map",
        "R4-00-R2-FULL-GRADE19-DECIDE", source_hashes,
    )
    for epsilon, suffix in ((1, "PLUS"), (-1, "MINUS")):
        substitution = r1_substitution(epsilon)
        full_branch = [(label, reduce_i(substitute(poly, substitution))) for label, poly in full_core_r2]
        # ii^2+1 is part of the coefficient-field encoding, but we work in an
        # ordinary exact-Q polynomial ring so the certificate is portable.
        full_branch.insert(0, ("II2_PLUS_1", ii_relation))
        packets[f"R1_{suffix}_FULL_GRADE19"] = packet(
            output, f"R1_{suffix}_FULL_GRADE19", full_branch, r1_opens + [j_open],
            f"Exact literal field-valued R4-00 CELL-R1 eps={epsilon} finite-jet equations through grade19; not an arc or map",
            "R4-00-R1-FULL-GRADE19-DECIDE", source_hashes,
        )

    controls = {
        "format": "K00_R400_SOURCE_CONTROLS_V1",
        "tail_census": 569,
        "literal_equation_census": 140,
        "grade12_cone_forcing": True,
        "grade13_T_ladder": True,
        "grade14_A7_B7_forcing": True,
        "R1_sign_conjugation": True,
        "R1_c21_q_and_A8_B8_cancel": True,
        "full_packet_inert_support_absent": sorted(expected_inert),
        "fixtures": fixture_records,
    }
    controls_path = output / "SOURCE_CONTROLS.json"
    controls_path.write_text(json.dumps(controls, sort_keys=True, indent=2) + "\n")

    result = {
        "status": "PASS_EXACT_R400_PACKETS_REBUILT_FROM_FROZEN_LITERAL_SOURCE",
        "registered_aws_lane": lane,
        "format": FORMAT,
        "source_sha256": source_hashes,
        "packets": {name: data["artifacts"] for name, data in packets.items()},
        "controls_sha256": digest(controls_path),
        "scope": "TWO_TYPED_OPEN_R4-00_RESIDUALS_ONLY; FIELD-VALUED FINITE JETS; NO ARC MAP ATTAINMENT OR JC2 CLAIM",
        "review": "PRODUCER_TOOLING_UNREVIEWED",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    artifacts = [path for path in sorted(output.iterdir()) if path.is_file() and path.name != "PACKETS.sha256"]
    manifest = output / "PACKETS.sha256"
    manifest.write_text("".join(f"{digest(path)}  {path.name}\n" for path in artifacts))
    print("K00_R400_PACKET_ENDPOINT=PASS_EXACT_R400_PACKETS_REBUILT_FROM_FROZEN_LITERAL_SOURCE")
    print(canonical_json(result), end="")


if __name__ == "__main__":
    main()
