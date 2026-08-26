#!/usr/bin/env python3
"""AWS-only v2 compiler for the exact finite control-2 Rees degeneration."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHARGED_SOURCE = (
    ROOT / "cases" /
    "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
    "independent_reconstruct.py"
)
CHARGED_SOURCE_SHA256 = (
    "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"
)

NAMES = ("la", "tau", "rho", "q1", "q0", "r2", "r1", "r0")
WEIGHTS = (4, 1, 1, 22, 22, 30, 30, 30)
INDEX = {name: position for position, name in enumerate(NAMES)}
ZERO = (0,) * len(NAMES)
RESIDUE = {
    "la": Fraction(1),
    "tau": Fraction(1),
    "rho": Fraction(1),
    "q1": Fraction(1),
    "q0": Fraction(-1),
    "r2": Fraction(1),
    "r1": Fraction(1),
    "r0": Fraction(-2),
}

# Images of a0,...,a7,k for K=z^3-3z+2, q2=k=0.  Encoding A
# substitutes their Rees-scaled compact forms directly in the charged source.
COEFFICIENT_REES_STRINGS = (
    "(8+2*s^22*q0+s^30*r0)",
    "(-36+s^22*(-3*q0+2*q1)+s^30*r1)",
    "(54-3*s^22*q1+s^30*r2)",
    "(-15+s^22*q0)",
    "(-36+s^22*q1)",
    "27",
    "6",
    "-9",
    "0",
)


class ReesCompileFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_control2_rees_v2_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_charged_source():
    got = sha256(CHARGED_SOURCE.read_bytes()).hexdigest()
    if got != CHARGED_SOURCE_SHA256:
        raise ReesCompileFailure(("charged source hash", got))
    spec = importlib.util.spec_from_file_location(
        "d1_control2_rees_charged_source", CHARGED_SOURCE
    )
    if spec is None or spec.loader is None:
        raise ReesCompileFailure("cannot load charged source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(poly):
    return {monomial: scalar for monomial, scalar in poly.items() if scalar}


def add(left, right):
    out = dict(left)
    for monomial_value, scalar in right.items():
        out[monomial_value] = out.get(monomial_value, Fraction(0)) + scalar
    return clean(out)


def scale(scalar, poly):
    scalar = Fraction(scalar)
    return clean({monomial_value: scalar * value
                  for monomial_value, value in poly.items()})


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial_value = tuple(a + b for a, b in zip(lm, rm))
            out[monomial_value] = (
                out.get(monomial_value, Fraction(0)) + lv * rv
            )
    return clean(out)


def constant(value):
    value = Fraction(value)
    return {} if not value else {ZERO: value}


def monomial(scalar=1, **powers):
    exponent = [0] * len(NAMES)
    for name, power_value in powers.items():
        if name not in INDEX or not isinstance(power_value, int) or power_value < 0:
            raise ReesCompileFailure(("bad monomial", name, power_value))
        exponent[INDEX[name]] = power_value
    scalar = Fraction(scalar)
    return {} if not scalar else {tuple(exponent): scalar}


def power(poly, exponent):
    out = constant(1)
    base = poly
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return out


def coefficient_images():
    q1 = monomial(q1=1)
    q0 = monomial(q0=1)
    r2 = monomial(r2=1)
    r1 = monomial(r1=1)
    r0 = monomial(r0=1)
    return (
        add(add(constant(8), scale(2, q0)), r0),
        add(add(constant(-36), add(scale(-3, q0), scale(2, q1))), r1),
        add(add(constant(54), scale(-3, q1)), r2),
        add(constant(-15), q0),
        add(constant(-36), q1),
        constant(27),
        constant(6),
        constant(-9),
        {},
    )


def source_power_table(images, tails):
    maxima = [0] * len(images)
    for row in tails.values():
        for source_monomial in row:
            for index, exponent in enumerate(source_monomial):
                maxima[index] = max(maxima[index], exponent)
    table = []
    for image, maximum in zip(images, maxima):
        entries = [constant(1)]
        for _ in range(maximum):
            entries.append(multiply(entries[-1], image))
        table.append(entries)
    return table


def substitute(source_poly, table):
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = constant(scalar)
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, table[index][exponent])
            if not term:
                break
        out = add(out, term)
    return clean(out)


def target(ell):
    if ell == 3:
        return monomial(Fraction(2, 3), la=15)
    if ell == 8:
        return add(monomial(la=20), monomial(la=20, tau=1))
    return {}


def relation():
    return add(monomial(la=1), scale(-1, monomial(tau=3, rho=1)))


def weighted_degree(exponents):
    return sum(weight * exponent for weight, exponent in zip(WEIGHTS, exponents))


def initial_data(poly):
    if not poly:
        raise ReesCompileFailure("zero polynomial in initial_data")
    minimum = min(weighted_degree(exponents) for exponents in poly)
    initial = {
        exponents: scalar for exponents, scalar in poly.items()
        if weighted_degree(exponents) == minimum
    }
    value = Fraction(0)
    for exponents, scalar in initial.items():
        term = scalar
        for name, exponent in zip(NAMES, exponents):
            term *= RESIDUE[name] ** exponent
        value += term
    return minimum, clean(initial), value


def fraction_string(value):
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def expanded_poly_string(poly, rees=False):
    chunks = []
    for exponents, scalar in sorted(poly.items(), reverse=True):
        factors = []
        if rees:
            s_power = weighted_degree(exponents)
            if s_power == 1:
                factors.append("s")
            elif s_power:
                factors.append(f"s^{s_power}")
        for name, exponent in zip(NAMES, exponents):
            if exponent == 1:
                factors.append(name)
            elif exponent:
                factors.append(f"{name}^{exponent}")
        body = "*".join(factors)
        coefficient = fraction_string(scalar)
        chunks.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(chunks).replace("+-", "-") or "0"


def compact_source_string(source_poly):
    chunks = []
    for exponents, scalar in sorted(source_poly.items(), reverse=True):
        factors = []
        for atom, exponent in zip(COEFFICIENT_REES_STRINGS, exponents):
            if atom == "0" and exponent:
                factors = ["0"]
                break
            if exponent == 1:
                factors.append(atom)
            elif exponent:
                factors.append(f"({atom})^{exponent}")
        body = "*".join(factors)
        coefficient = fraction_string(scalar)
        chunks.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(chunks).replace("+-", "-") or "0"


def compact_row_string(source_poly, ell):
    raw = compact_source_string(source_poly)
    if ell == 3:
        return f"({raw})-(2/3)*s^60*la^15"
    if ell == 8:
        return f"({raw})-s^80*la^20*(1+s*tau)"
    return raw


def canonical(poly):
    return [
        [list(exponents), scalar.numerator, scalar.denominator]
        for exponents, scalar in sorted(poly.items())
    ]


def digest(poly):
    encoded = json.dumps(canonical(poly), separators=(",", ":"))
    return sha256(encoded.encode()).hexdigest()


def residue_equations():
    return (
        "la-1,tau-1,rho-1,q1-1,q0+1,"
        "r2-1,r1-1,r0+2"
    )


def source_a(tails, tag):
    variables = "s," + ",".join(NAMES)
    lines = [
        "// Exact finite control-2 Rees degeneration v2, encoding A.",
        'LIB "elim.lib";',
        f"ring R=0,({variables}),dp;",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly E{ell}={compact_row_string(tails[ell], ell)};")
    lines.extend([
        "poly LT=s^4*(la-tau^3*rho);",
        "ideal CS=s;",
        "ideal TOY_VERTICAL=s;",
        "list TV=sat(TOY_VERTICAL,CS);",
        "ideal GTV=std(TV[1]);",
        'if (reduce(1,GTV)!=0) { print("FAIL_A_VERTICAL_CONTROL"); quit; }',
        "ideal TOY_FACTOR=s*(q1-1);",
        "list TF=sat(TOY_FACTOR,CS);",
        "ideal GTF=std(TF[1]);",
        'if (reduce(1,GTF)==0 || reduce(q1-1,GTF)!=0) { print("FAIL_A_FACTOR_CONTROL"); quit; }',
        'print("PASS_A_SYNTHETIC_CONTROLS");',
        f'print("AWS_TAG={tag}");',
        'print("ENCODING=A_FACTORED_REES_SAT_DP_V2");',
        'print("START_A_REES_SATURATION");',
        "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;",
        "list SC=sat(I,CS);",
        "ideal C=SC[1];",
        'print("A_CONTRACTION_GENERATORS="+string(size(C)));',
        "ideal H=C,s;",
        "ideal GH=std(H);",
        'print("A_SPECIAL_FIBRE_GENERATORS="+string(size(GH)));',
        "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;",
        "ideal CT=TORUS;",
        "list HT=sat(GH,CT);",
        "ideal GHT=std(HT[1]);",
        'print("A_TORUS_SPECIAL_FIBRE_GENERATORS="+string(size(GHT)));',
        "if (reduce(1,GHT)==0)",
        "{",
        '  print("TORUS_SPECIAL_FIBRE_IS_UNIT=1");',
        "}",
        "else",
        "{",
        '  print("TORUS_SPECIAL_FIBRE_IS_UNIT=0");',
        "}",
        'print("TORUS_SPECIAL_FIBRE_BASIS_BEGIN");',
        "GHT;",
        'print("TORUS_SPECIAL_FIBRE_BASIS_END");',
        f"ideal P=GHT,{residue_equations()};",
        "ideal GP=std(P);",
        "if (reduce(1,GP)==0)",
        "{",
        '  print("RESIDUE_IDEAL_IS_UNIT=1");',
        '  print("CONTROL2_REES_RESIDUE_SURVIVES=0");',
        "}",
        "else",
        "{",
        '  print("RESIDUE_IDEAL_IS_UNIT=0");',
        '  print("CONTROL2_REES_RESIDUE_SURVIVES=1");',
        "}",
        'print("FIREWALL=EXACT_ONLY_FOR_FROZEN_AXIS_FIXED_LOAD_SUPPORT_WEIGHT_AND_RESIDUE");',
        'print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_A");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def source_b(rows, tag):
    variables = "u,v,s," + ",".join(NAMES)
    lines = [
        "// Exact finite control-2 Rees degeneration v2, encoding B.",
        'LIB "elim.lib";',
        f"ring R=0,({variables}),(lp(3),dp({len(NAMES)}));",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly E{ell}={expanded_poly_string(rows[ell], rees=True)};")
    lines.extend([
        f"poly LT={expanded_poly_string(relation(), rees=True)};",
        "ideal TOY_VERTICAL=s,u*s-1;",
        "ideal GTV0=std(TOY_VERTICAL);",
        "ideal GTV=eliminate(GTV0,u);",
        'if (reduce(1,std(GTV))!=0) { print("FAIL_B_VERTICAL_CONTROL"); quit; }',
        "ideal TOY_FACTOR=s*(q1-1),u*s-1;",
        "ideal GTF0=std(TOY_FACTOR);",
        "ideal GTF=eliminate(GTF0,u);",
        "ideal SGTF=std(GTF);",
        'if (reduce(1,SGTF)==0 || reduce(q1-1,SGTF)!=0) { print("FAIL_B_FACTOR_CONTROL"); quit; }',
        'print("PASS_B_SYNTHETIC_CONTROLS");',
        f'print("AWS_TAG={tag}");',
        'print("ENCODING=B_EXPANDED_REES_INVERSE_ELIM_LPDP_V2");',
        'print("START_B_REES_INVERSE_ELIMINATION");',
        "ideal J=E1,E2,E3,E4,E5,E6,E7,E8,LT,u*s-1;",
        "ideal GJ=std(J);",
        "ideal C=eliminate(GJ,u);",
        'print("B_CONTRACTION_GENERATORS="+string(size(C)));',
        "ideal H=C,s;",
        "ideal GH=std(H);",
        'print("B_SPECIAL_FIBRE_GENERATORS="+string(size(GH)));',
        "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;",
        "ideal JT=GH,v*TORUS-1;",
        "ideal GJT=std(JT);",
        "ideal HT=eliminate(GJT,v);",
        "ideal GHT=std(HT);",
        'print("B_TORUS_SPECIAL_FIBRE_GENERATORS="+string(size(GHT)));',
        "if (reduce(1,GHT)==0)",
        "{",
        '  print("TORUS_SPECIAL_FIBRE_IS_UNIT=1");',
        "}",
        "else",
        "{",
        '  print("TORUS_SPECIAL_FIBRE_IS_UNIT=0");',
        "}",
        'print("TORUS_SPECIAL_FIBRE_BASIS_BEGIN");',
        "GHT;",
        'print("TORUS_SPECIAL_FIBRE_BASIS_END");',
        f"ideal P=GHT,{residue_equations()};",
        "ideal GP=std(P);",
        "if (reduce(1,GP)==0)",
        "{",
        '  print("RESIDUE_IDEAL_IS_UNIT=1");',
        '  print("CONTROL2_REES_RESIDUE_SURVIVES=0");',
        "}",
        "else",
        "{",
        '  print("RESIDUE_IDEAL_IS_UNIT=0");',
        '  print("CONTROL2_REES_RESIDUE_SURVIVES=1");',
        "}",
        'print("FIREWALL=EXACT_ONLY_FOR_FROZEN_AXIS_FIXED_LOAD_SUPPORT_WEIGHT_AND_RESIDUE");',
        'print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_B");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    tag = require_aws()
    charged = load_charged_source()
    built = charged.build()
    if tuple(built["names"]) != tuple([f"a{i}" for i in range(8)] + ["k"]):
        raise ReesCompileFailure(("charged names", built["names"]))
    tails = built["tails"]
    if set(tails) != set(range(1, 9)):
        raise ReesCompileFailure(("charged rows", sorted(tails)))

    images = coefficient_images()
    table = source_power_table(images, tails)
    raw_rows = {ell: substitute(tails[ell], table) for ell in range(1, 9)}
    rows = {ell: add(raw_rows[ell], scale(-1, target(ell)))
            for ell in range(1, 9)}
    zero_names = {"q1", "q0", "r2", "r1", "r0"}
    zero_positions = {INDEX[name] for name in zero_names}
    for ell, raw in raw_rows.items():
        base = {
            exponents: scalar for exponents, scalar in raw.items()
            if all(exponents[position] == 0 for position in zero_positions)
        }
        if clean(base):
            raise ReesCompileFailure(("common cubic did not vanish", ell))

    all_rows = dict(rows)
    all_rows[9] = relation()
    initial_report = {}
    for ell, row in all_rows.items():
        minimum, initial, value = initial_data(row)
        if value:
            raise ReesCompileFailure(("residue misses generator initial", ell, value))
        initial_report[str(ell)] = {
            "minimum_weight": minimum,
            "initial_support": len(initial),
            "initial_sha256": digest(initial),
            "residue_value": "0",
        }

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    path_a = output / "control2_rees_v2_A_factored_sat_dp.sing"
    path_b = output / "control2_rees_v2_B_expanded_inverse_lpdp.sing"
    path_a.write_text(source_a(tails, tag), encoding="utf-8")
    path_b.write_text(source_b(rows, tag), encoding="utf-8")

    payload = {
        "aws_tag": tag,
        "charged_source_sha256": CHARGED_SOURCE_SHA256,
        "finite_variables": list(NAMES),
        "weights": dict(zip(NAMES, WEIGHTS)),
        "support_mask_zero": ["a-1", "h", "q2", "k", "nu"],
        "fixed": {"a": "1", "h": "0", "k": "0", "mu": "2/3", "nu": "0"},
        "residue": {name: str(value) for name, value in RESIDUE.items()},
        "initial_generators": initial_report,
        "outputs": {
            path_a.name: sha256(path_a.read_bytes()).hexdigest(),
            path_b.name: sha256(path_b.read_bytes()).hexdigest(),
        },
        "semantics": (
            "dual nonunit residue ideals give an exact Puiseux lift only in "
            "the frozen-axis fixed-load support/weight/residue; dual units "
            "exclude only that datum"
        ),
    }
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")
    print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_COMPILER")


if __name__ == "__main__":
    main()
