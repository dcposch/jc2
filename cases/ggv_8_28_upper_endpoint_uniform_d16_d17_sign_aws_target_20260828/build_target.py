#!/usr/bin/env python3
"""Build the frozen nine-branch D16/D17 lower-system AWS target."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CLASSIFIER = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_sign_branches_20260828"
              / "classify_sign_branches.py")
CLASSIFIER_RESULT = CLASSIFIER.with_name("RESULT.json")
PRODUCER_RESULT = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
                   / "RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
TARGET = HERE / "sign_branch_elimination_target.json"
CLASSIFIER_SHA256 = "e53e6ad72e15d4ea5f8f8657ad33ac689d1f97f2fbfd69bb5dc55c35c3c79682"
CLASSIFIER_RESULT_SHA256 = "ad8f1b64b6ecd3d07867ac31e80ad0db7ddffc25a1a0ba3d831f83208fa0b6e6"
PRODUCER_RESULT_SHA256 = "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependencies():
    assert digest(CLASSIFIER) == CLASSIFIER_SHA256
    assert digest(CLASSIFIER_RESULT) == CLASSIFIER_RESULT_SHA256
    assert digest(PRODUCER_RESULT) == PRODUCER_RESULT_SHA256
    assert digest(RAW) == RAW_SHA256
    specification = importlib.util.spec_from_file_location("sign_classifier_frozen", CLASSIFIER)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    calculated = module.calculate_result()
    classifier = json.loads(CLASSIFIER_RESULT.read_text())
    assert calculated == classifier
    producer = json.loads(PRODUCER_RESULT.read_text())
    return module, classifier, producer


def parse_gaussian(text):
    if "i" not in text:
        return Q(text), Q(0)
    body = text.replace("*i", "").replace("i", "")
    separator = next((index for index in range(1, len(body))
                      if body[index] in "+-"), None)
    if separator is None:
        imag = body
        if imag in ("", "+"):
            imag = "1"
        elif imag == "-":
            imag = "-1"
        return Q(0), Q(imag)
    real = body[:separator]
    imag = body[separator:]
    if imag == "+":
        imag = "1"
    elif imag == "-":
        imag = "-1"
    return Q(real), Q(imag)


def fraction_text(value):
    return str(value)


def normalize_equation(encoded):
    return [
        {"monomial": record["monomial"],
         "coefficient": [fraction_text(value) for value in
                         parse_gaussian(record["coefficient"])]}
        for record in encoded
    ]


def structural_equation(*terms):
    return [{"monomial": list(monomial),
             "coefficient": [str(Q(real)), str(Q(imaginary))]}
            for monomial, real, imaginary in terms]


def zero_branch_system(module, producer):
    sterm, sadd, sscale, smul = module.sterm, module.sadd, module.sscale, module.smul
    ssubstitute, sencode = module.ssubstitute, module.sencode

    base8 = sadd(
        sterm(Q(1, 2), "y0"), sterm(Q(1, 8), "t0", "z0"),
        sterm(Q(1, 16), "q0", "v0"), sterm(Q(1, 4), "r0", "r0"))
    H0 = sscale(Q(3, 4), sadd(sterm(1, "lambda"), base8))
    base9_0 = sadd(
        sterm(Q(1, 2), "q0", "r0"), sterm(Q(1, 16), "t0", "v0"),
        sterm(Q(1, 8), "y0", "z0"))
    base9_1 = sadd(
        sterm(Q(1, 2), "q0", "r1"), sterm(Q(1, 2), "q1", "r0"),
        sterm(Q(1, 16), "t0", "v1"), sterm(Q(1, 16), "t1", "v0"),
        sterm(Q(1, 8), "y0", "z1"), sterm(Q(1, 8), "y1", "z0"))
    equations = {
        "F9_X0_absence": sadd(sterm(1, "c0"), base9_0),
        "C13": sadd(
            smul(sterm(1, "q0"), H0),
            sterm(Q(-3, 128), "q0", "q0", "v0"),
            sterm(Q(-3, 16), "q0", "r0", "r0"),
            sterm(Q(3, 16), "t0", "t0"),
            sterm(Q(3, 4), "t0", "y0")),
        "C14": sadd(
            smul(sterm(1, "t0"), H0),
            sterm(Q(-3, 16), "q0", "q0", "r0"),
            sterm(Q(-3, 64), "q0", "t0", "v0"),
            sterm(Q(-3, 16), "r0", "r0", "t0"),
            sterm(Q(-3, 64), "t0", "t0", "z0"),
            sterm(Q(3, 8), "y0", "y0")),
        "C15": sadd(
            smul(sterm(1, "y0"), H0),
            sterm(Q(-1, 16), "q0", "q0", "q0"),
            sterm(Q(-3, 8), "q0", "r0", "t0"),
            sterm(Q(-3, 64), "q0", "v0", "y0"),
            sterm(Q(-3, 16), "r0", "r0", "y0"),
            sterm(Q(-3, 128), "t0", "t0", "v0"),
            sterm(Q(-3, 32), "t0", "y0", "z0"),
            sterm(Q(-3, 16), "y0", "y0")),
    }
    substitutions = {
        "m0": sterm(Q(3, 8), "lambda", "lambda"),
        "m1": {},
        "n0": sadd(sterm(Q(3, 4), "lambda", "c0"),
                     sterm(Q(-3, 16), "lambda", "lambda")),
        "n1": sterm(Q(3, 4), "lambda", "c1"),
        "f91": sadd(sterm(1, "c1"), base9_1),
    }
    jets = producer["calculation"]["positive_lower_window_jets"]
    for label in ("G16_X0", "G16_X1", "G17_X0", "G17_X1"):
        equations[label] = ssubstitute(module.encoded_jet(jets[label]), substitutions)
    return {label: normalize_equation(sencode(equation))
            for label, equation in equations.items()}


def variable_union(equations):
    return sorted({symbol for equation in equations.values()
                   for term in equation for symbol in term["monomial"]})


def evaluate_equation(equation, point):
    real = Q(0)
    imaginary = Q(0)
    for term in equation:
        coefficient = tuple(Q(value) for value in term["coefficient"])
        value = coefficient
        for symbol in term["monomial"]:
            right = point[symbol]
            value = (value[0] * right[0] - value[1] * right[1],
                     value[0] * right[1] + value[1] * right[0])
        real += value[0]
        imaginary += value[1]
    return real, imaginary


def seed_point(variables, overrides):
    point = {variable: (Q(0), Q(0)) for variable in variables}
    point.update(overrides)
    return {variable: [str(value[0]), str(value[1])]
            for variable, value in point.items()}


def calculate_target():
    module, classifier, producer = load_dependencies()
    representatives = [branch for branch in classifier["J16_nonzero"]["branches"]
                       if branch["label"].startswith("+")]
    assert len(representatives) == 8
    branches = {}
    for branch in representatives:
        equations = {
            label: normalize_equation(encoded)
            for label, encoded in branch["lower_window_test"]["equations"].items()
        }
        equations["rho_localization"] = structural_equation(
            (("rho", "rhoinv"), 1, 0), ((), -1, 0))
        equations["rho_J16_relation"] = structural_equation(
            (("rho", "rho"), 3, 0), (("J16",), 8, 0))
        variables = variable_union(equations)
        assert len(variables) == 18
        record = {
            "kind": "J16_nonzero_sign_pair",
            "sign_representative": branch["label"],
            "paired_sign": "".join("-" if sign == "+" else "+"
                                    for sign in branch["label"]),
            "coefficient_field": "Q(i)",
            "variables": variables,
            "passive_variables": [],
            "equation_order": list(equations),
            "equations": equations,
            "equation_count": len(equations),
            "term_count": sum(len(equation) for equation in equations.values()),
            "coverage": (
                "both global-sign sheets are covered because rho is an unnormalized "
                "nonzero variable and (E,rho)~(-E,-rho) was proved"
            ),
            "source_branch_system_sha256": branch["lower_window_test"][
                "system_sha256"],
        }
        if branch["label"] == "++++":
            point = seed_point(variables, {
                "rho": (Q(1), Q(0)), "rhoinv": (Q(1), Q(0)),
                "J16": (Q(-3, 8), Q(0)),
            })
            decoded = {name: tuple(Q(value) for value in encoded)
                       for name, encoded in point.items()}
            assert all(evaluate_equation(equation, decoded) == (Q(0), Q(0))
                       for equation in equations.values())
            record["exact_seed_point"] = point
        branches[branch["label"]] = record

    zero_equations = zero_branch_system(module, producer)
    zero_equations["J16_zero"] = structural_equation((("J16",), 1, 0))
    zero_variables = sorted(set(variable_union(zero_equations)) |
                            {f"c{degree}" for degree in range(8)})
    passive = [f"c{degree}" for degree in range(2, 8)]
    zero_point = seed_point(zero_variables, {})
    decoded_zero = {name: tuple(Q(value) for value in encoded)
                    for name, encoded in zero_point.items()}
    assert all(evaluate_equation(equation, decoded_zero) == (Q(0), Q(0))
               for equation in zero_equations.values())
    branches["J0"] = {
        "kind": "J16_zero_collision",
        "coefficient_field": "Q(i)",
        "variables": zero_variables,
        "passive_variables": passive,
        "equation_order": list(zero_equations),
        "equations": zero_equations,
        "equation_count": len(zero_equations),
        "term_count": sum(len(equation) for equation in zero_equations.values()),
        "C_degree_bound": 7,
        "C_coefficients": [f"c{degree}" for degree in range(8)],
        "exact_seed_point": zero_point,
    }
    return {
        "schema": "jc2.ggv.uniform_d16_d17.sign_lower_aws_target.v1",
        "status": "FROZEN_DESIGN_NOT_LAUNCHED",
        "source": {
            "classifier_checker": str(CLASSIFIER.relative_to(ROOT)),
            "classifier_checker_sha256": CLASSIFIER_SHA256,
            "classifier_result": str(CLASSIFIER_RESULT.relative_to(ROOT)),
            "classifier_result_sha256": CLASSIFIER_RESULT_SHA256,
            "producer_result": str(PRODUCER_RESULT.relative_to(ROOT)),
            "producer_result_sha256": PRODUCER_RESULT_SHA256,
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
        },
        "mathematical_scope": {
            "nonzero_sign_pair_count": 8,
            "zero_collision_branch_count": 1,
            "all_lower_equations": [
                "F9_X0_absence", "C13", "C14", "C15",
                "G16_X0", "G16_X1", "G17_X0", "G17_X1",
            ],
            "degree_window_constraints": {
                "Bhat_upper": 8, "C_lower": 0, "C_upper": 7,
                "raw_F9_lower": 1, "raw_G16_lower": 2, "raw_G17_lower": 2,
            },
            "rho_relation": "3*rho^2+8*J16=0",
            "rho_nonzero": "rho*rhoinv-1=0 on each sign-pair branch",
            "normalizations": [],
        },
        "branches": branches,
        "branch_order": [branch["label"] for branch in representatives] + ["J0"],
        "execution_policy": {
            "modular": (
                "reconnaissance only; a modular unit, nonunit, dimension, or point is not "
                "promotable"
            ),
            "exact_unit": (
                "requires exact Q(i) liftstd cofactor replay with CERTIFICATE_CHECK=PASS"
            ),
            "exact_point": (
                "requires a complete point file and exact Gaussian-rational validator PASS; "
                "it proves only consistency of this necessary subsystem"
            ),
            "exact_nonunit": "inconclusive for existence and for the endpoint problem",
            "coverage": "every theorem using emptiness must account for all nine branch records",
        },
        "resource_envelope": {
            "recommended_workers": 4,
            "per_worker_address_space_gib": 16,
            "aggregate_declared_gib": 64,
            "mem_available_floor_gib": 150,
            "swap": "must be unconfigured and unused",
            "disk_available_floor_gib": 50,
            "modular_wall_per_job_minutes": 30,
            "exact_wall_per_job_hours": 4,
            "campaign_global_wall_hours": 12,
            "expected_typical_ram": "<2 GiB/job; caps are deliberately conservative",
        },
        "firewalls": [
            "no sign or rho normalization; one E representative covers its opposite only via the proved rho sign involution",
            "J16 is retained with 3*rho^2+8*J16=0 rather than silently eliminated",
            "the six passive C2..C7 coefficients on J0 are retained in the ring inventory",
            "no cutoff-three transport is imported or asserted",
            "a nonunit basis or modular point is not existence evidence",
            "this packet is an unlaunched execution design",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    target = calculate_target()
    encoded = (json.dumps(target, indent=2, sort_keys=True) + "\n").encode()
    if arguments.write:
        TARGET.write_bytes(encoded)
    if arguments.check:
        assert TARGET.read_bytes() == encoded
    if arguments.dump:
        print(encoded.decode(), end="")
    else:
        print(json.dumps({
            "status": target["status"],
            "branches": target["branch_order"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
