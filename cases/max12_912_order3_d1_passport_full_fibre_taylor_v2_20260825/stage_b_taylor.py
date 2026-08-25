#!/usr/bin/env sage -python
"""Compile the exact 23-row Taylor ideal for one certified D1 section.

Run with Sage on AWS Linux.  The 18 Taylor-centre variables are retained.
For each coefficient in the cubic extension t^3=s, the t and t^2 parts are
forced to vanish.  The invariant part N(s)/D(s) is in C[x], x=s/(s-1), iff
after removing every factor of s-1 from D, the remaining denominator divides
N and the quotient has degree at most ord_(s=1)(D).  The code translates
that criterion into exact polynomial equations without sampling or jets.

This compiler handles one Stage-A section certificate.  It neither finds nor
proves completeness of Stage-A sections, and it does not solve the emitted
Taylor ideal.
"""

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

from sage.all import (QQ, PolynomialRing, factorial, sage_eval)  # type: ignore


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
COMPILER_PATH = HERE / "compile_gate_v2.py"
INDEPENDENT_PATH = HERE / "independent_reconstruct.py"


class TaylorFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise TaylorFailure(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_certificate(path: Path) -> dict[str, object]:
    certificate = json.loads(path.read_text())
    if certificate.get("schema") != "d1_constant_section_v1":
        raise TaylorFailure("wrong certificate schema")
    if not isinstance(certificate.get("A"), list) or len(certificate["A"]) != 8:
        raise TaylorFailure("certificate requires eight A expressions")
    return certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    tag = require_aws()
    certificate = read_certificate(args.certificate)

    compiler = load_module(COMPILER_PATH, "d1_v2_taylor_compiler")
    independent = load_module(INDEPENDENT_PATH, "d1_v2_taylor_independent")
    _, M, descended_ring, descended_rows, source_payload = compiler.compile_all()
    rebuilt = independent.build()

    # Constant field Q(k,mu,nu), optionally followed by one explicitly
    # constant algebraic extension.  The polynomial defining theta cannot
    # mention s because s has not yet been introduced.
    constant_polynomial_ring = PolynomialRing(QQ, names=("k", "mu", "nu"))
    k0, mu0, nu0 = constant_polynomial_ring.gens()
    constant_field = constant_polynomial_ring.fraction_field()
    k0, mu0, nu0 = map(constant_field, (k0, mu0, nu0))
    minpoly_text = certificate.get("theta_minpoly")
    if minpoly_text is None:
        extension_field = constant_field
        theta0 = extension_field(0)
    else:
        theta_ring = PolynomialRing(constant_field, "T")
        T = theta_ring.gen()
        minpoly = theta_ring(sage_eval(
            minpoly_text,
            locals={"T": T, "k": k0, "mu": mu0, "nu": nu0},
        ))
        if minpoly.degree() < 2 or not minpoly.is_irreducible():
            raise TaylorFailure("constant minpoly is not irreducible degree >=2")
        extension_field = constant_field.extension(minpoly, "theta")
        theta0 = extension_field.gen()

    centre_names = [f"cm{d}" for d in range(6, 0, -1)] \
        + [f"cp{d}" for d in range(1, 13)]
    centre_ring = PolynomialRing(extension_field, names=centre_names)
    centre_variables = dict(zip(centre_names, centre_ring.gens()))
    s_ring = PolynomialRing(centre_ring, "s")
    s = s_ring.gen()
    rational_field = s_ring.fraction_field()
    k = rational_field(extension_field(k0))
    mu = rational_field(extension_field(mu0))
    nu = rational_field(extension_field(nu0))
    theta = rational_field(theta0)
    centre_variables = {name: rational_field(value)
                        for name, value in centre_variables.items()}

    extension_polynomial_ring = PolynomialRing(rational_field, "Tsource")
    Tsource = extension_polynomial_ring.gen()
    cubic_field = rational_field.extension(Tsource**3 - s, "t")
    t = cubic_field.gen()
    z_ring = PolynomialRing(cubic_field, "z")
    z = z_ring.gen()

    environment = {"s": s, "k": k, "mu": mu, "nu": nu, "theta": theta}
    sections = [rational_field(sage_eval(text, locals=environment))
                for text in certificate["A"]]
    environment.update({f"A{i}": sections[i] for i in range(8)})
    if k == 0:
        raise TaylorFailure("section certificate lies outside k!=0 chart")
    for expression in certificate.get("denominators_nonzero", []):
        if rational_field(sage_eval(expression, locals=environment)) == 0:
            raise TaylorFailure(("declared denominator zero", expression))

    def evaluate_descended(value):
        result = rational_field(0)
        values = sections + [s, k, mu, nu]
        for monomial, coefficient in value.items():
            term = rational_field(QQ(coefficient.numerator)
                                  / QQ(coefficient.denominator))
            for exponent, variable in zip(monomial, values):
                term *= variable**exponent
            result += term
        return result

    for ell in range(1, 9):
        if evaluate_descended(descended_rows[ell]) != 0:
            raise TaylorFailure(("Stage-A source row failed", ell))

    source_coefficients = [t**(index % 3) * cubic_field(sections[index])
                           for index in range(8)]
    f = z**9 + sum(source_coefficients[index] * z**index
                   for index in range(8))

    def evaluate_sparse_coefficient(value):
        result = cubic_field(0)
        for monomial, coefficient in value.items():
            term = cubic_field(QQ(coefficient.numerator)
                               / QQ(coefficient.denominator))
            for index in range(8):
                term *= source_coefficients[index]**monomial[index]
            term *= cubic_field(k)**monomial[8]
            result += term
        return result

    def evaluate_laurent_polynomial(value):
        return sum(evaluate_sparse_coefficient(coefficient) * z**exponent
                   for exponent, coefficient in value.items())

    f6 = evaluate_laurent_polynomial(rebuilt["F6"])
    f12 = evaluate_laurent_polynomial(rebuilt["F12"])
    g = f12 + cubic_field(k) * f6

    R0 = rational_field(0)
    for degree in range(1, 7):
        R0 += centre_variables[f"cm{degree}"] * s**(-degree)
    for degree in range(1, 13):
        R0 += centre_variables[f"cp{degree}"] * s**degree
    u = t**2 / (s - 1)**2
    r = u * cubic_field(R0)
    x = s / (s - 1)
    h = u**3
    if h != x**2 * (x - 1)**4:
        raise TaylorFailure("D1 h identity failed")
    # dt/dx=-(s-1)^2/(3t^2).
    if 9 * (-(s - 1)**2 / (3 * t**2)) != -3 / u:
        raise TaylorFailure("D1 terminal derivative identity failed")

    def nth_derivative(polynomial, order: int):
        out = polynomial
        for _ in range(order):
            out = out.derivative()
        return out

    taylor_values = []
    for label, polynomial, maximum in (("P", f, 9), ("Q", g, 12)):
        for ell in range(maximum + 1):
            derivative = nth_derivative(polynomial, ell)
            value = u**ell * derivative(r) / factorial(ell)
            taylor_values.append((label, ell, value))

    equations = []
    row_metadata = []

    def component(value, exponent: int):
        coefficients = list(value)
        return rational_field(coefficients[exponent]) \
            if exponent < len(coefficients) else rational_field(0)

    def append_zero_equations(value, source: str):
        numerator = s_ring(value.numerator())
        denominator = s_ring(value.denominator())
        # Any dependence of a denominator on centre variables would mean the
        # fraction-field representation had silently localized a Taylor
        # stratum.  Refuse rather than saturate it away.
        for coefficient in denominator.list():
            if centre_ring(coefficient).total_degree() != 0:
                raise TaylorFailure(("centre-dependent denominator", source))
        count_before = len(equations)
        equations.extend(centre_ring(coefficient)
                         for coefficient in numerator.list() if coefficient)
        return len(equations) - count_before

    def polynomial_in_x_equations(value, source: str):
        numerator = s_ring(value.numerator())
        denominator = s_ring(value.denominator())
        for coefficient in denominator.list():
            if centre_ring(coefficient).total_degree() != 0:
                raise TaylorFailure(("centre-dependent denominator", source))
        if denominator == 0:
            raise TaylorFailure(("zero denominator", source))
        leading = extension_field(denominator.leading_coefficient())
        denominator /= leading
        numerator /= leading
        s_minus_one = s_ring(s - 1)
        pole_order = 0
        while denominator(1) == 0:
            quotient, remainder = denominator.quo_rem(s_minus_one)
            if remainder:
                raise TaylorFailure(("s=1 division failed", source))
            denominator = quotient
            pole_order += 1
        quotient, remainder = numerator.quo_rem(denominator)
        generated = [centre_ring(coefficient)
                     for coefficient in remainder.list() if coefficient]
        # Sage reports degree(0)=-Infinity, which is not a Python range bound.
        if quotient:
            for degree in range(pole_order + 1, int(quotient.degree()) + 1):
                coefficient = centre_ring(quotient[degree])
                if coefficient:
                    generated.append(coefficient)
        return pole_order, generated

    def append_polynomial_in_x_equations(value, source: str):
        pole_order, generated = polynomial_in_x_equations(value, source)
        equations.extend(generated)
        return pole_order, len(generated)

    # Executable exact controls for the membership criterion.  They do not
    # consume a Stage-A section and are the source-level test while no real
    # section certificate is known.
    control_parameter = centre_variables["cp1"]
    positive_control = 1 + control_parameter * x + x**2
    positive_pole, positive_equations = polynomial_in_x_equations(
        rational_field(positive_control), "control:polynomial-in-x"
    )
    zero_pole, zero_equations = polynomial_in_x_equations(
        rational_field(0), "control:zero"
    )
    away_pole, away_equations = polynomial_in_x_equations(
        rational_field(1 / (s + 1)), "control:pole-away-from-s1"
    )
    degree_pole, degree_equations = polynomial_in_x_equations(
        rational_field(s**2 / (s - 1)), "control:degree-over-pole-bound"
    )
    if positive_equations or zero_equations:
        raise TaylorFailure("positive/zero C[x] control rejected")
    if not away_equations or not degree_equations:
        raise TaylorFailure("negative C[x] control accepted")
    membership_controls = {
        "polynomial_in_x": {"pass": True, "pole_bound": positive_pole},
        "zero_function": {"pass": True, "pole_bound": zero_pole},
        "pole_away_from_s1": {
            "rejected": True,
            "equation_count": len(away_equations),
            "pole_bound": away_pole,
        },
        "degree_exceeds_s1_pole_bound": {
            "rejected": True,
            "equation_count": len(degree_equations),
            "pole_bound": degree_pole,
        },
    }

    for label, ell, value in taylor_values:
        noninvariant_counts = []
        for exponent in (1, 2):
            noninvariant_counts.append(append_zero_equations(
                component(value, exponent), f"{label}{ell}:t^{exponent}"
            ))
        pole_order, invariant_count = append_polynomial_in_x_equations(
            component(value, 0), f"{label}{ell}:invariant"
        )
        row_metadata.append({
            "coordinate": f"{label}{ell}",
            "noninvariant_equations": noninvariant_counts,
            "s1_pole_bound": pole_order,
            "membership_equations": invariant_count,
        })

    cleaned_equations = []
    seen = set()
    for equation in equations:
        equation = centre_ring(equation)
        if not equation:
            continue
        key = str(equation)
        if key not in seen:
            seen.add(key)
            cleaned_equations.append(equation)
    ideal = centre_ring.ideal(cleaned_equations)
    equation_strings = [str(equation) for equation in cleaned_equations]
    equation_digest = sha256(json.dumps(
        equation_strings, separators=(",", ":")
    ).encode()).hexdigest()
    output = {
        "aws_tag": tag,
        "source_payload_sha256": sha256(json.dumps(
            source_payload, sort_keys=True, separators=(",", ":")
        ).encode()).hexdigest(),
        "section_certificate_sha256": sha256(args.certificate.read_bytes()).hexdigest(),
        "centre_variables": centre_names,
        "centre_variable_count": len(centre_names),
        "taylor_coordinate_count": len(taylor_values),
        "row_metadata": row_metadata,
        "membership_controls": membership_controls,
        "equation_count_before_dedup": len(equations),
        "equation_count": len(cleaned_equations),
        "equation_sha256": equation_digest,
        "equations": equation_strings,
        "ideal_generators": [str(generator) for generator in ideal.gens()],
        "status": "EXACT_TAYLOR_IDEAL_COMPILED_NOT_SOLVED",
        "scope": "one exact Stage-A section; no section completeness or exclusion",
    }
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n")
    print("PASS-D1-STAGE-B-EXACT-TAYLOR-IDEAL-COMPILER")
    print(f"taylor_coordinate_count={len(taylor_values)}")
    print(f"equation_count={len(cleaned_equations)}")
    print(f"equation_sha256={equation_digest}")
    print("solve_status=NOT_RUN")


if __name__ == "__main__":
    main()
