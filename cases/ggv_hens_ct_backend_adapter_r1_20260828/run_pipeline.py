#!/usr/bin/env python3
"""Exact upstream gate and conditionally charged HENS-CT rank-one control."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import traceback
from datetime import datetime, timezone
from pathlib import Path

from sage.all__sagemath_symbolics import PolynomialRing, ZZ
from ore_algebra import OreAlgebra


ORE_COMMIT = "18680180c884fac869a064db99f29a221aad9dfe"


class ExactFailure(RuntimeError):
    def __init__(self, label, detail):
        super().__init__(detail)
        self.label = label
        self.detail = str(detail)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_text(path, text):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_json(path, value):
    atomic_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def exp_tuple(exp):
    try:
        return tuple(int(item) for item in exp)
    except TypeError:
        return (int(exp),)


def operator_payload(operator):
    terms = []
    for exp, coefficient in operator.dict().items():
        terms.append({
            "exponents": list(exp_tuple(exp)),
            "coefficient": str(coefficient),
        })
    terms.sort(key=lambda item: tuple(item["exponents"]))
    return {"repr": repr(operator), "terms": terms}


def derive_extension(element, field, generator, base_variable, generator_derivative):
    """Differentiate an algebraic-extension element by the implicit rule."""
    element = field(element)
    answer = field.zero()
    for degree, coefficient in enumerate(element.list()):
        answer += field(coefficient.derivative(base_variable)) * generator**degree
        if degree:
            answer += field(degree * coefficient) * generator ** (degree - 1) * generator_derivative
    return field(answer)


def apply_operator(operator, element, field, derivations):
    """Apply a sparse differential Ore operator with explicit field derivations."""
    names = [str(generator) for generator in operator.parent().gens()]
    answer = field.zero()
    for raw_exp, coefficient in operator.dict().items():
        exponents = exp_tuple(raw_exp)
        if len(exponents) != len(names):
            raise ExactFailure("FAIL_OPERATOR_ARITY", (exponents, names))
        value = field(element)
        for name, exponent in zip(names, exponents):
            if name not in derivations:
                raise ExactFailure("FAIL_MISSING_DERIVATION", name)
            for _ in range(exponent):
                value = derivations[name](value)
        answer += field(coefficient) * value
    return field(answer)


def bridge_probe():
    """Require the frozen failure and the patched generic fallback."""
    base = PolynomialRing(ZZ, names=("x", "y"))
    from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular

    original_failure = None
    try:
        MPolynomialRing_libsingular(base, 1, ("Dx", "Dy"))
    except NotImplementedError as exc:
        original_failure = repr(exc)
    if original_failure is None:
        raise ExactFailure("FAIL_MUTATION_NOT_LIVE", "explicit libSingular constructor did not fail")

    algebra = OreAlgebra(base, "Dx", "Dy")
    generators = algebra.gens()
    commutative = algebra.associated_commutative_algebra()
    class_name = type(commutative).__module__ + "." + type(commutative).__name__
    if "libsingular" in class_name.lower():
        raise ExactFailure("FAIL_FALLBACK_NOT_SELECTED", class_name)
    if tuple(map(str, generators)) != ("Dx", "Dy"):
        raise ExactFailure("FAIL_FALLBACK_GENERATORS", generators)
    return {
        "original_constructor_failure": original_failure,
        "fallback_parent": repr(commutative),
        "fallback_class": class_name,
        "generators": list(map(str, generators)),
    }


def run_upstream(output_dir, bridge):
    atomic_text(output_dir / "CURRENT_STAGE", "UPSTREAM_COMPOSITION\n")
    base, base_gens = PolynomialRing(ZZ, names=("x", "y")).objgens()
    x, y = base_gens
    t_polynomial_ring = PolynomialRing(base.fraction_field(), names=("t",))
    t0 = t_polynomial_ring.gen()
    modulus = (x - y) * t0**3 + t0 - x**2 * y - x**2
    field = base.fraction_field().extension(modulus, names=("t",))
    t = field.gen()

    outer, operators = OreAlgebra(base, "Dx", "Dy").objgens()
    Dx0, Dy0 = operators
    outer_ideal = outer.ideal([x * Dx0 - 1, y * Dy0 - 1])
    composed = outer_ideal.annihilator_of_composition(x=t, infolevel=2)
    by_name = {str(operator): operator for operator in composed.ring().gens()}
    if set(by_name) != {"Dx", "Dy"}:
        raise ExactFailure("FAIL_UPSTREAM_OPERATOR_NAMES", sorted(by_name))
    Dx = by_name["Dx"]
    Dy = by_name["Dy"]

    atomic_text(output_dir / "CURRENT_STAGE", "UPSTREAM_CT\n")
    telescoper_output, certificates = composed.ct(
        Dy, certificates=True, early_termination=False, infolevel=2
    )
    telescopers = list(telescoper_output.gens()) if hasattr(telescoper_output, "gens") else list(telescoper_output)
    if not telescopers or not certificates:
        raise ExactFailure("FAIL_UPSTREAM_EMPTY_CT", (telescoper_output, certificates))
    L = telescopers[0]
    C = certificates[0]
    if L.is_zero() or C is None or C.is_zero():
        raise ExactFailure("FAIL_UPSTREAM_ZERO_CT", (L, C))
    L_ambient = composed.ring()(L)
    C_ambient = composed.ring()(C)
    candidate = {
        "schema": "ore-algebra-upstream-algebraic-integral-candidate-v1",
        "utc": utc(),
        "modulus": str(modulus),
        "bridge": bridge,
        "L": operator_payload(L_ambient),
        "C": operator_payload(C_ambient),
    }
    atomic_json(output_dir / "upstream_candidate.json", candidate)

    expected = (
        (252 * x**5 - 108 * x**4 - 81 * x**3 + 36 * x**2) * Dx**2
        + (-504 * x**4 + 108 * x**3 + 36 * x) * Dx
        + 224 * x**3 + 360 * x**2 + 66 * x - 16
    )
    scale = L_ambient.lc() / expected.lc()
    if scale == 0 or L_ambient != scale * expected:
        raise ExactFailure(
            "FAIL_UPSTREAM_DOCTEST_OPERATOR",
            {"got": repr(L_ambient), "expected": repr(expected), "scale": str(scale)},
        )

    atomic_text(output_dir / "CURRENT_STAGE", "UPSTREAM_ORE_REDUCTION\n")
    ore_remainder = (L_ambient - Dy * C_ambient).reduce(composed)
    if not ore_remainder.is_zero():
        raise ExactFailure("FAIL_UPSTREAM_ORE_REDUCER", repr(ore_remainder))

    denominator = 3 * (x - y) * t**2 + 1
    tx = (-t**3 + 2 * x * y + 2 * x) / denominator
    ty = (t**3 + x**2) / denominator
    dx = lambda value: derive_extension(value, field, t, x, tx)
    dy = lambda value: derive_extension(value, field, t, y, ty)
    derivations = {"Dx": dx, "Dy": dy}
    q = t * y
    B = apply_operator(C_ambient, q, field, derivations)
    atomic_text(output_dir / "CURRENT_STAGE", "UPSTREAM_FIELD_REDUCTION\n")
    field_remainder = apply_operator(L_ambient, q, field, derivations) - dy(B)
    if not field(field_remainder).is_zero():
        raise ExactFailure("FAIL_UPSTREAM_FIELD_REDUCER", repr(field_remainder))

    result = {
        **candidate,
        "schema": "ore-algebra-upstream-algebraic-integral-certificate-v1",
        "doctest_operator_scale": str(scale),
        "ore_membership_remainder": repr(ore_remainder),
        "B": repr(B),
        "direct_field_remainder": repr(field_remainder),
        "exact_certificate": True,
    }
    atomic_json(output_dir / "upstream_certificate.json", result)
    atomic_text(output_dir / "UPSTREAM_PASS", "UPSTREAM_PASS\n")
    print("UPSTREAM_PASS", flush=True)
    print("UPSTREAM_L", repr(L_ambient), flush=True)
    print("UPSTREAM_C", repr(C_ambient), flush=True)
    print("UPSTREAM_B", repr(B), flush=True)
    return result


def polynomial_residue(poly, modulus):
    residues = set()
    for raw_degree, coefficient in poly.dict().items():
        if not coefficient:
            continue
        degree = exp_tuple(raw_degree)[0]
        residues.add(degree % modulus)
    if len(residues) != 1:
        raise ExactFailure("FAIL_NONSECTIONABLE", {"polynomial": repr(poly), "residues": sorted(residues)})
    return next(iter(residues))


def sectionability(operator):
    checks = []
    for raw_exp, coefficient in operator.dict().items():
        exponent = exp_tuple(raw_exp)
        if len(exponent) != 1:
            raise ExactFailure("FAIL_NONSECTIONABLE", {"operator_arity": exponent})
        order = exponent[0]
        numerator = coefficient.numerator()
        denominator = coefficient.denominator()
        numerator_residue = polynomial_residue(numerator, 4)
        denominator_residue = polynomial_residue(denominator, 4)
        preserved = (numerator_residue - denominator_residue - order) % 4 == 0
        checks.append({
            "order": order,
            "coefficient": str(coefficient),
            "numerator_residue_mod_4": numerator_residue,
            "denominator_residue_mod_4": denominator_residue,
            "condition": preserved,
        })
        if not preserved:
            raise ExactFailure("FAIL_NONSECTIONABLE", checks[-1])
    return sorted(checks, key=lambda item: item["order"])


def run_control(output_dir, bridge):
    atomic_text(output_dir / "CURRENT_STAGE", "CONTROL_COMPOSITION\n")
    outer_base, outer_gens = PolynomialRing(ZZ, names=("ss", "xx", "yy")).objgens()
    ss0, xx0, yy0 = outer_gens
    outer, operators = OreAlgebra(outer_base, "Dss", "Dxx", "Dyy").objgens()
    Dss0, Dxx0, Dyy0 = operators
    monomial_ideal = outer.ideal([Dss0, xx0 * Dxx0 - 2, yy0 * Dyy0 - 2])

    base, base_gens = PolynomialRing(ZZ, names=("ss", "xx")).objgens()
    ss, xx = base_gens
    y_polynomial_ring = PolynomialRing(base.fraction_field(), names=("ya",))
    ya0 = y_polynomial_ring.gen()
    h = 1 + xx ** (-3) + xx ** (-7)
    modulus = ya0**8 - 1 - ss * h * ya0
    field = base.fraction_field().extension(modulus, names=("ya",))
    ya = field.gen()
    print("CONTROL_MODULUS", modulus, flush=True)
    print("CONTROL_BRANCH_SEED ya(ss=0)=1", flush=True)

    composed = monomial_ideal.annihilator_of_composition(
        ss=field(ss), xx=field(xx), yy=ya, infolevel=2
    )
    by_name = {str(operator): operator for operator in composed.ring().gens()}
    if "Dxx" not in by_name:
        raise ExactFailure("FAIL_CONTROL_NO_DXX", sorted(by_name))
    Dxx = by_name["Dxx"]

    atomic_text(output_dir / "CURRENT_STAGE", "CONTROL_CT\n")
    telescoper_output, certificates = composed.ct(
        Dxx,
        certificates=True,
        early_termination=True,
        iteration_limit=96,
        infolevel=2,
    )
    telescopers = list(telescoper_output.gens()) if hasattr(telescoper_output, "gens") else list(telescoper_output)
    if not telescopers or not certificates:
        raise ExactFailure("FAIL_CONTROL_EMPTY_CT", (telescoper_output, certificates))
    L = telescopers[0]
    C = certificates[0]
    if L.is_zero() or C is None or C.is_zero():
        raise ExactFailure("FAIL_CONTROL_ZERO_CT", (L, C))
    L_ambient = composed.ring()(L)
    C_ambient = composed.ring()(C)
    candidate = {
        "schema": "ggv-hens-ct-rank-one-candidate-r1",
        "utc": utc(),
        "modulus": str(modulus),
        "branch_seed": "ya(ss=0)=1",
        "bridge": bridge,
        "L": operator_payload(L),
        "C": operator_payload(C_ambient),
    }
    atomic_json(output_dir / "control_candidate.json", candidate)

    atomic_text(output_dir / "CURRENT_STAGE", "CONTROL_ORE_REDUCTION\n")
    ore_remainder = (L_ambient - Dxx * C_ambient).reduce(composed)
    if not ore_remainder.is_zero():
        raise ExactFailure("FAIL_CONTROL_ORE_REDUCER", repr(ore_remainder))

    fy = 8 * ya**7 - ss * h
    hprime = h.derivative(xx)
    yas = h * ya / fy
    yax = ss * hprime * ya / fy
    ds = lambda value: derive_extension(value, field, ya, ss, yas)
    dx = lambda value: derive_extension(value, field, ya, xx, yax)
    derivations = {"Dss": ds, "Dxx": dx}
    q = xx**2 * ya**2
    B = apply_operator(C_ambient, q, field, derivations)
    atomic_text(output_dir / "CURRENT_STAGE", "CONTROL_FIELD_REDUCTION\n")
    field_remainder = apply_operator(L_ambient, q, field, derivations) - dx(B)
    if not field(field_remainder).is_zero():
        raise ExactFailure("FAIL_CONTROL_FIELD_REDUCER", repr(field_remainder))

    section_checks = sectionability(L)
    result = {
        **candidate,
        "schema": "ggv-hens-ct-rank-one-certificate-r1",
        "ore_membership_remainder": repr(ore_remainder),
        "B": repr(B),
        "direct_field_remainder": repr(field_remainder),
        "sectionability_checks": section_checks,
        "exact_certificate": True,
    }
    atomic_json(output_dir / "control_certificate.json", result)
    print("CONTROL_PASS", flush=True)
    print("CONTROL_L", repr(L), flush=True)
    print("CONTROL_C", repr(C_ambient), flush=True)
    print("CONTROL_B", repr(B), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    arguments = parser.parse_args()
    output_dir = arguments.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata = {
        "schema": "ggv-hens-ct-backend-adapter-r1-run",
        "start_utc": utc(),
        "host": platform.node(),
        "python": platform.python_version(),
        "ore_algebra_version": importlib.metadata.version("ore_algebra"),
        "ore_commit_expected": os.environ.get("ORE_COMMIT"),
        "aws_run_tag": os.environ.get("AWS_RUN_TAG"),
        "upstream_exact_certificate": False,
        "control_charged": False,
        "control_exact_certificate": False,
    }
    atomic_json(output_dir / "run_metadata.json", metadata)
    if os.environ.get("ORE_COMMIT") != ORE_COMMIT:
        raise ExactFailure("FAIL_COMMIT_ENV", os.environ.get("ORE_COMMIT"))

    try:
        atomic_text(output_dir / "CURRENT_STAGE", "BRIDGE_PROBE\n")
        bridge = bridge_probe()
        atomic_json(output_dir / "bridge_probe.json", bridge)
        run_upstream(output_dir, bridge)
        metadata["upstream_exact_certificate"] = True
        metadata["control_charged"] = True
        atomic_json(output_dir / "run_metadata.json", metadata)
        run_control(output_dir, bridge)
        metadata["control_exact_certificate"] = True
        metadata["end_utc"] = utc()
        metadata["terminal"] = "PASS"
        atomic_json(output_dir / "run_metadata.json", metadata)
        atomic_text(output_dir / "TERMINAL", "PASS\n")
        atomic_text(output_dir / "CURRENT_STAGE", "COMPLETE\n")
        print("PASS", flush=True)
    except ExactFailure as exc:
        metadata["end_utc"] = utc()
        metadata["terminal"] = exc.label
        metadata["failure_detail"] = exc.detail
        atomic_json(output_dir / "run_metadata.json", metadata)
        atomic_json(output_dir / "failure.json", {
            "label": exc.label, "detail": exc.detail, "utc": utc()
        })
        atomic_text(output_dir / "TERMINAL", exc.label + "\n")
        print(exc.label, exc.detail, flush=True)
        raise SystemExit(2)
    except Exception as exc:
        stage = (output_dir / "CURRENT_STAGE").read_text().strip()
        label = "FAIL_UPSTREAM_BACKEND" if stage.startswith("UPSTREAM") or stage == "BRIDGE_PROBE" else "FAIL_CONTROL_BACKEND"
        detail = repr(exc)
        metadata["end_utc"] = utc()
        metadata["terminal"] = label
        metadata["failure_detail"] = detail
        atomic_json(output_dir / "run_metadata.json", metadata)
        atomic_json(output_dir / "failure.json", {
            "label": label,
            "detail": detail,
            "stage": stage,
            "traceback": traceback.format_exc(),
            "utc": utc(),
        })
        atomic_text(output_dir / "TERMINAL", label + "\n")
        print(label, stage, detail, flush=True)
        raise SystemExit(3)


if __name__ == "__main__":
    main()
