#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
BRIDGE_BUILDER = HERE / "build_row_bridge_v39.py"
BRIDGE_BUILDER_SHA = "657cd20d790435e09d7f771d800b016efe02589aa20b62dea164acf3d2ff4f19"
BRIDGE = HERE / "ROW_BRIDGE.json"
BRIDGE_SHA = "d119796fb6cbfc93460fe821e8f64664d48934a0537c670a280c3fd693345dc9"
PREREG = HERE / "PREREGISTRATION.md"
PREREG_SHA = "eac2819c9a30dea3a350991b3608d75b1b66306ef08f6f06d80b3326f03e66ea"
STATUS = "PASS-A1-W19-TG19-7-COMPATIBILITY-V39-COMPILER"
SCOPE = "ordinary unsaturated homogeneous weight-19 ideal membership in all other frozen ordered-a1 rho-zero raw rows through grade19; no radical, saturation, Rees-chart, Gate-T, or JC2 inference"
PRIMES = (65521, 65519)
TARGET_NAME = "Tg19_7"
TARGET_GRADE = 19
V34_SUPPORT = frozenset({"a1", "ell2", "cs1", "rs2", "aa0", "ee1", "ec3"})
EXPECTED_PRODUCTS = 802
EXPECTED_UNION_SUPPORT = 5078
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_w19_tg19_7_compatibility_v39_[0-9]{8}T[0-9]{6}Z_q(65521|65519)_(r6d|box01)")

FIRST_OCCURRENCE = {
    10: (),
    11: ("a1", "e0"),
    12: ("ell1", "aa0", "aa1", "e1", "ee0"),
    13: ("ell2", "cs1", "rs1", "k", "aaa0", "aaa1", "ee1", "ec3"),
    14: ("ell3", "cs2", "rs2", "k1", "ac3", "az3", "ez3", "ec4"),
    15: ("ell4", "cs3", "rs3", "k2c", "ac4", "az4", "ez4", "ec5"),
    16: ("ell5", "cs4", "rs4", "k10_3", "ac5", "az5", "ez5", "ec6"),
    17: ("ell6", "cs5", "rs5", "k10_4", "ac6", "az6", "ez6", "ec7"),
    18: ("ell7", "cs6", "rs6", "k10_5", "ac7", "az7", "ez7", "k6", "ec8"),
    19: ("ell8", "cs7", "rs7", "k10_6", "ac8", "az8", "ez8", "k6_1", "ec9"),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def object_hash(value: object) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw)
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail(("noncanonical JSON", str(path)))
    return value


def load_module(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module hash", str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode_fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def decode_fraction(raw) -> Fraction:
    if type(raw) is not list or len(raw) != 2 or any(type(item) is not int for item in raw):
        fail(("fraction schema", raw))
    value = Fraction(raw[0], raw[1])
    if raw != [value.numerator, value.denominator]:
        fail(("noncanonical fraction", raw))
    return value


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def decode_monomial(raw):
    if type(raw) is not list:
        fail("monomial list")
    answer = []
    for pair in raw:
        if (type(pair) is not list or len(pair) != 2 or type(pair[0]) is not str
                or type(pair[1]) is not int or pair[1] <= 0):
            fail(("monomial pair", pair))
        answer.append((pair[0], pair[1]))
    value = tuple(answer)
    if value != tuple(sorted(value)) or len({name for name, _ in value}) != len(value):
        fail(("noncanonical monomial", raw))
    return value


def encode_polynomial(polynomial) -> dict[str, object]:
    return {
        "terms": [
            {"coefficient": encode_fraction(coefficient), "monomial": encode_monomial(monomial)}
            for monomial, coefficient in sorted(polynomial.items())
        ]
    }


def decode_polynomial(raw):
    if type(raw) is not dict or set(raw) != {"terms"} or type(raw["terms"]) is not list:
        fail("polynomial schema")
    answer = {}
    for entry in raw["terms"]:
        if type(entry) is not dict or set(entry) != {"coefficient", "monomial"}:
            fail("polynomial term schema")
        monomial = decode_monomial(entry["monomial"])
        coefficient = decode_fraction(entry["coefficient"])
        if not coefficient or monomial in answer:
            fail("polynomial term canonicality")
        answer[monomial] = coefficient
    if list(answer) != sorted(answer):
        fail("polynomial ordering")
    return answer


def monomial(variables: dict[str, int]):
    return tuple(sorted((name, exponent) for name, exponent in variables.items() if exponent))


def poly(*terms):
    answer = {}
    for coefficient, variables in terms:
        key = monomial(variables)
        answer[key] = answer.get(key, Fraction(0)) + Fraction(coefficient)
        if not answer[key]:
            answer.pop(key)
    return answer


def add_scaled(target, source, scale: Fraction) -> None:
    if not scale:
        return
    for key, coefficient in source.items():
        value = target.get(key, Fraction(0)) + scale * coefficient
        if value:
            target[key] = value
        else:
            target.pop(key, None)


def multiply(left, right):
    answer = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            exponents = dict(lm)
            for name, exponent in rm:
                exponents[name] = exponents.get(name, 0) + exponent
            key = monomial(exponents)
            answer[key] = answer.get(key, Fraction(0)) + lc * rc
            if not answer[key]:
                answer.pop(key)
    return answer


def power(value, exponent: int):
    answer = poly((1, {}))
    base = value
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return answer


def load_sources():
    v37 = load_module(V37, V37_SHA, "v39_v37")
    builder = load_module(BRIDGE_BUILDER, BRIDGE_BUILDER_SHA, "v39_bridge_builder")
    if digest(BRIDGE) != BRIDGE_SHA or digest(PREREG) != PREREG_SHA:
        fail("V39 frozen input hash")
    bridge = canonical_json(BRIDGE)
    rebuilt_bridge = builder.build_manifest()
    if bridge != rebuilt_bridge:
        fail("row bridge replay")
    parser, rows, row_hashes, variables = v37.load_rows()
    if (len(row_hashes), len(rows), len(variables)) != (70, 51, 65):
        fail("row census")
    if bridge["rows"] != rebuilt_bridge["rows"]:
        fail("row bridge records")
    return v37, parser, rows, row_hashes, variables, bridge


def coefficient_in_newcomer(polynomial, newcomer: str, all_newcomers: frozenset[str]):
    answer = {}
    for key, coefficient in polynomial.items():
        seen = [(name, exponent) for name, exponent in key if name in all_newcomers]
        if len(seen) > 1:
            fail(("two newcomers", newcomer, key))
        if seen:
            name, exponent = seen[0]
            if exponent != 1:
                fail(("nonlinear newcomer", name, key))
            if name == newcomer:
                stripped = tuple((n, e) for n, e in key if n != newcomer)
                answer[stripped] = answer.get(stripped, Fraction(0)) + coefficient
    return {key: value for key, value in answer.items() if value}


def stationary_expected(grade: int):
    newcomers = FIRST_OCCURRENCE[grade]
    L, C, R, K, AC, AZ, EZ = newcomers[:7]
    if grade >= 18:
        H, EC = newcomers[7:]
    else:
        H, EC = None, newcomers[7]
    p = poly((Fraction(-3, 8), {"a1": 2}), (Fraction(5, 16), {"e0": 1, "k": 1}),
             (Fraction(15, 256), {"k": 1, "rs1": 2}))
    q1 = poly((Fraction(15, 128), {"cs1": 1, "k": 1, "rs1": 1}),
              (Fraction(5, 64), {"e1": 1, "k": 1}))
    s1 = poly((Fraction(5, 16), {"cs1": 1, "e0": 1}),
              (Fraction(15, 256), {"cs1": 1, "rs1": 2}),
              (Fraction(5, 64), {"e1": 1, "rs1": 1}))
    q2 = poly((Fraction(-3, 32), {"a1": 2}), (Fraction(5, 64), {"e0": 1, "k": 1}),
              (Fraction(15, 1024), {"k": 1, "rs1": 2}))
    s2 = poly((Fraction(5, 64), {"e0": 1, "rs1": 1}), (Fraction(5, 1024), {"rs1": 3}))
    h1 = poly((Fraction(3, 16), {"cs1": 1, "rs1": 1}), (Fraction(3, 8), {"e1": 1}))
    h2 = poly((Fraction(3, 8), {"e0": 1}), (Fraction(3, 128), {"rs1": 2}))
    matrix = {(row, name): {} for row in range(1, 8) for name in newcomers}
    entries = {
        (1, C): p, (1, R): q1, (1, K): s1,
        (1, AC): poly((Fraction(3, 8), {"e1": 1})),
        (1, AZ): poly((Fraction(3, 8), {"e0": 1})),
        (1, EZ): poly((Fraction(3, 8), {"aa0": 1})),
        (1, EC): poly((Fraction(3, 8), {"a1": 1})),
        (2, L): poly((Fraction(-3, 8), {"a1": 1, "e1": 1})),
        (2, R): q2, (2, K): s2,
        (2, AC): poly((Fraction(3, 8), {"e0": 1})),
        (2, EZ): poly((Fraction(-3, 8), {"a1": 1, "ell1": 1}),
                      (Fraction(3, 16), {"e1": 1})),
        (3, L): poly((Fraction(-3, 16), {"a1": 1, "e0": 1})),
        (3, EZ): poly((Fraction(3, 16), {"e0": 1})),
    }
    if H is not None:
        entries[(1, H)] = h1
        entries[(2, H)] = h2
    matrix.update(entries)
    return matrix


def exact_controls(parser, rows):
    by_name = {item["name"]: item["polynomial"] for item in rows}
    observed_first = {grade: [] for grade in range(10, 20)}
    seen = set()
    for grade in range(10, 20):
        grade_variables = {name for item in rows if item["grade"] == grade
                           for key in item["polynomial"] for name, _ in key}
        newly_seen = grade_variables - seen
        if newly_seen != set(FIRST_OCCURRENCE[grade]):
            fail(("first occurrence", grade, sorted(newly_seen), FIRST_OCCURRENCE[grade]))
        observed_first[grade] = list(FIRST_OCCURRENCE[grade])
        seen.update(grade_variables)
    expected_first = {grade: list(names) for grade, names in FIRST_OCCURRENCE.items()}
    if observed_first != expected_first:
        fail(("first occurrence", observed_first))

    stationary_serialized = {}
    grade19_compatibility_literal_newcomer_terms = 0
    grade19_compatibility_after_e0_terms = 0
    for grade in range(14, 20):
        newcomers = frozenset(FIRST_OCCURRENCE[grade])
        expected = stationary_expected(grade)
        encoded_entries = {}
        for row in range(1, 8):
            polynomial = by_name.get(f"Tg{grade}_{row}", {})
            for newcomer in FIRST_OCCURRENCE[grade]:
                actual = coefficient_in_newcomer(polynomial, newcomer, newcomers)
                if actual != expected[(row, newcomer)]:
                    fail(("stationary matrix", grade, row, newcomer, actual, expected[(row, newcomer)]))
                if actual:
                    encoded_entries[f"r{row}:{newcomer}"] = encode_polynomial(actual)
                    if grade == 19 and row >= 3:
                        grade19_compatibility_literal_newcomer_terms += len(actual)
                        after_e0 = {key: coefficient for key, coefficient in actual.items()
                                    if all(name != "e0" for name, _ in key)}
                        grade19_compatibility_after_e0_terms += len(after_e0)
        stationary_serialized[str(grade)] = encoded_entries
    if grade19_compatibility_literal_newcomer_terms != 2 or grade19_compatibility_after_e0_terms != 0:
        fail(("grade19 compatibility newcomer control", grade19_compatibility_literal_newcomer_terms,
              grade19_compatibility_after_e0_terms))

    tg11 = by_name["Tg11_1"]
    expected_tg11 = poly((Fraction(3, 8), {"a1": 1, "e0": 1}))
    if tg11 != expected_tg11:
        fail("Tg11_1 identity")

    X = poly((-32, {"a1": 2}))
    Y = poly((5, {"k": 1, "rs1": 2}))
    Q = dict(X); add_scaled(Q, Y, Fraction(1))
    S = poly((1, {"rs1": 3}))
    factor = power(X, 2); add_scaled(factor, multiply(X, Y), Fraction(-1)); add_scaled(factor, power(Y, 2), Fraction(1))
    long_residual = multiply(Q, factor)
    add_scaled(long_residual, multiply(poly((125, {"k": 3})), power(S, 2)), Fraction(-1))
    add_scaled(long_residual, power(X, 3), Fraction(-1))
    q = poly((Fraction(-3, 32), {"a1": 2}), (Fraction(15, 1024), {"k": 1, "rs1": 2}))
    h = poly((Fraction(3, 128), {"rs1": 2}))
    short_residual = dict(q)
    add_scaled(short_residual, multiply(poly((Fraction(5, 8), {"k": 1})), h), Fraction(-1))
    add_scaled(short_residual, poly((Fraction(3, 32), {"a1": 2})), Fraction(1))
    if long_residual or short_residual:
        fail(("Bezout identity", long_residual, short_residual))
    return {
        "first_occurrence": {str(grade): names for grade, names in observed_first.items()},
        "stationary_matrix_sha256": object_hash(stationary_serialized),
        "stationary_nonzero_entry_count": sum(len(entries) for entries in stationary_serialized.values()),
        "grade19_rows3_to7_literal_newcomer_coefficient_terms": grade19_compatibility_literal_newcomer_terms,
        "grade19_rows3_to7_newcomer_terms_after_e0_zero": grade19_compatibility_after_e0_terms,
        "tg11_1_exact": True,
        "row2_fraction_free_bezout_exact": True,
        "row2_grade18_19_short_bezout_exact": True,
    }


def pivot_key(key):
    names = {name for name, _ in key}
    return (1 if names <= V34_SUPPORT else 0, len(names - V34_SUPPORT), key)


def target_component(products, target):
    incidence = {}
    for index, product in enumerate(products):
        for key in product["polynomial"]:
            incidence.setdefault(key, []).append(index)
    monomials = set(target)
    product_indices = set()
    queue = deque(sorted(target, key=pivot_key))
    while queue:
        key = queue.popleft()
        for index in incidence.get(key, ()):
            if index in product_indices:
                continue
            product_indices.add(index)
            for neighbor in products[index]["polynomial"]:
                if neighbor not in monomials:
                    monomials.add(neighbor)
                    queue.append(neighbor)
    chosen = sorted(product_indices)
    ordered_monomials = sorted(monomials, key=pivot_key)
    # Fail closed if an edge crosses the purported complete component.
    chosen_set = set(chosen)
    for key in monomials:
        if any(index not in chosen_set for index in incidence.get(key, ())):
            fail("incomplete target component")
    return chosen, ordered_monomials


def modular_value(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad selector denominator", prime, value))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def modular_skeleton(polynomials, ordered_monomials, prime: int):
    column = {key: index for index, key in enumerate(ordered_monomials)}
    basis = {}
    selected = []
    pivots = []
    for original_index, polynomial in enumerate(polynomials):
        vector = {}
        for key, coefficient in polynomial.items():
            value = modular_value(coefficient, prime)
            if value:
                vector[column[key]] = value
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, prime)
                vector = {index: value * inverse % prime for index, value in vector.items()
                          if value * inverse % prime}
                basis[pivot] = vector
                selected.append(original_index)
                pivots.append(pivot)
                break
            old = basis[pivot]
            for index, value in old.items():
                new = (vector.get(index, 0) - coefficient * value) % prime
                if new:
                    vector[index] = new
                else:
                    vector.pop(index, None)
    return selected, pivots


def as_fraction(value) -> Fraction:
    return Fraction(int(value.p), int(value.q))


def reduction_term(component_products, component_indices, basis_index: int, coefficient: Fraction):
    product = component_products[basis_index]
    return {
        "coefficient": encode_fraction(coefficient),
        "component_product_index": basis_index,
        "full_product_index": component_indices[basis_index],
        "row": product["row"],
        "grade": product["grade"],
        "multiplier": encode_monomial(product["multiplier"]),
    }


def exact_certificate(products, component_indices, ordered_monomials, target, selector_prime: int):
    from flint import fmpq, fmpq_mat

    component_products = [products[index] for index in component_indices]
    selected, pivot_indices = modular_skeleton(
        [item["polynomial"] for item in component_products], ordered_monomials, selector_prime)
    rank = len(selected)
    pivot_monomials = [ordered_monomials[index] for index in pivot_indices]
    if rank == 0:
        fail("unexpected zero rank")
    flat = []
    for selected_index in selected:
        polynomial = component_products[selected_index]["polynomial"]
        for key in pivot_monomials:
            value = polynomial.get(key, Fraction(0))
            flat.append(fmpq(value.numerator, value.denominator))
    matrix = fmpq_mat(rank, rank, flat)
    if matrix.rank() != rank:
        fail("selector minor singular over Q")

    # Prove, over Q, that the selected rows span every product in the complete
    # component.  This prevents a modular rank drop from masquerading as a
    # full exact basis.
    rhs_flat = []
    for pivot_key_value in pivot_monomials:
        for product in component_products:
            value = product["polynomial"].get(pivot_key_value, Fraction(0))
            rhs_flat.append(fmpq(value.numerator, value.denominator))
    rhs_all = fmpq_mat(rank, len(component_products), rhs_flat)
    all_coordinates = matrix.transpose().solve(rhs_all)
    for product_index, product in enumerate(component_products):
        replay = {}
        for basis_position, selected_index in enumerate(selected):
            coefficient = as_fraction(all_coordinates[basis_position, product_index])
            if coefficient:
                add_scaled(replay, component_products[selected_index]["polynomial"], coefficient)
        if replay != product["polynomial"]:
            fail(("exact full-span replay", product_index))

    target_rhs = fmpq_mat(rank, 1, [
        fmpq(target.get(key, Fraction(0)).numerator, target.get(key, Fraction(0)).denominator)
        for key in pivot_monomials
    ])
    coefficients_q = matrix.transpose().solve(target_rhs)
    coefficients = [as_fraction(coefficients_q[index, 0]) for index in range(rank)]
    residual = dict(target)
    reduction_terms = []
    for coefficient, selected_index in zip(coefficients, selected):
        if coefficient:
            add_scaled(residual, component_products[selected_index]["polynomial"], -coefficient)
            reduction_terms.append(reduction_term(component_products, component_indices, selected_index, coefficient))

    if not residual:
        certificate = {
            "kind": "member",
            "selector_prime": selector_prime,
            "exact_rank": rank,
            "exact_full_span_replayed": True,
            "full_product_replay_count": len(products),
            "terms": reduction_terms,
        }
    else:
        functional = None
        for witness in sorted(residual, key=pivot_key):
            witness_scale = Fraction(1, 1) / residual[witness]
            rhs = []
            for selected_index in selected:
                value = -component_products[selected_index]["polynomial"].get(witness, Fraction(0)) * witness_scale
                rhs.append(fmpq(value.numerator, value.denominator))
            solution = matrix.solve(fmpq_mat(rank, 1, rhs))
            candidate = {witness: witness_scale}
            for index, key in enumerate(pivot_monomials):
                value = candidate.get(key, Fraction(0)) + as_fraction(solution[index, 0])
                if value:
                    candidate[key] = value
                else:
                    candidate.pop(key, None)
            if (sum(coefficient * candidate.get(key, Fraction(0)) for key, coefficient in target.items()) == 1
                    and all(sum(coefficient * candidate.get(key, Fraction(0))
                                for key, coefficient in product["polynomial"].items()) == 0
                            for product in products)):
                functional = candidate
                break
        if functional is None:
            fail("no exact full-product dual")
        certificate = {
            "kind": "nonmember",
            "selector_prime": selector_prime,
            "exact_rank": rank,
            "exact_full_span_replayed": True,
            "full_product_replay_count": len(products),
            "functional": [
                {"coefficient": encode_fraction(coefficient), "monomial": encode_monomial(key)}
                for key, coefficient in sorted(functional.items())
            ],
        }
    return certificate, residual, reduction_terms


def decode_reduction_terms(raw, products, component_indices):
    if type(raw) is not list:
        fail("reduction terms list")
    component_products = [products[index] for index in component_indices]
    answer = []
    seen = set()
    for term in raw:
        keys = {"coefficient", "component_product_index", "full_product_index", "row", "grade", "multiplier"}
        if type(term) is not dict or set(term) != keys:
            fail("reduction term schema")
        ci = term["component_product_index"]
        fi = term["full_product_index"]
        if type(ci) is not int or type(fi) is not int or ci < 0 or ci >= len(component_products):
            fail("reduction index")
        product = component_products[ci]
        if (fi != component_indices[ci] or type(term["row"]) is not str or term["row"] != product["row"]
                or type(term["grade"]) is not int or term["grade"] != product["grade"]
                or decode_monomial(term["multiplier"]) != product["multiplier"]):
            fail("reduction metadata")
        if ci in seen:
            fail("duplicate reduction basis row")
        seen.add(ci)
        coefficient = decode_fraction(term["coefficient"])
        if not coefficient:
            fail("zero reduction coefficient")
        answer.append((coefficient, product))
    return answer


def replay_payload(payload, products, component_indices, target):
    certificate = payload["certificate"]
    residual_record = payload["residual"]
    reduction = decode_reduction_terms(residual_record["reduction_terms"], products, component_indices)
    residual = dict(target)
    for coefficient, product in reduction:
        add_scaled(residual, product["polynomial"], -coefficient)
    decoded_residual = decode_polynomial(residual_record["polynomial"])
    if (residual != decoded_residual or residual_record["term_count"] != len(residual)
            or residual_record["polynomial_sha256"] != object_hash(encode_polynomial(residual))):
        fail("residual replay")
    if certificate["kind"] == "member":
        if residual or certificate["terms"] != residual_record["reduction_terms"]:
            fail("membership replay")
    elif certificate["kind"] == "nonmember":
        functional = {}
        for entry in certificate["functional"]:
            key = decode_monomial(entry["monomial"])
            coefficient = decode_fraction(entry["coefficient"])
            if not coefficient or key in functional:
                fail("functional schema")
            functional[key] = coefficient
        evaluate = lambda polynomial: sum(coefficient * functional.get(key, Fraction(0))
                                          for key, coefficient in polynomial.items())
        if (evaluate(target) != 1 or any(evaluate(product["polynomial"]) for product in products)
                or evaluate(residual) != 1):
            fail("dual full replay")
    else:
        fail("certificate kind")


def mutation_control(certificate, target):
    if certificate["kind"] == "member":
        detected = min(target)
    else:
        functional = {decode_monomial(entry["monomial"]): decode_fraction(entry["coefficient"])
                      for entry in certificate["functional"]}
        candidates = [key for key in target if functional.get(key, Fraction(0))]
        if not candidates:
            fail("no mutation-detected target term")
        detected = min(candidates)
    removed = target[detected]
    mutated = dict(target)
    mutated.pop(detected)
    if object_hash(encode_polynomial(mutated)) == object_hash(encode_polynomial(target)):
        fail("mutation bridge not detected")
    if certificate["kind"] == "member":
        replay_rejected = True  # the exact pristine combination equals target, not target-minus-term
    else:
        functional = {decode_monomial(entry["monomial"]): decode_fraction(entry["coefficient"])
                      for entry in certificate["functional"]}
        replay_rejected = (sum(coefficient * functional.get(key, Fraction(0))
                               for key, coefficient in mutated.items()) != 1)
    if not replay_rejected:
        fail("mutation exact replay not detected")
    return {
        "deleted_monomial": encode_monomial(detected),
        "deleted_coefficient": encode_fraction(removed),
        "mutated_target_sha256": object_hash(encode_polynomial(mutated)),
        "target_bridge_rejected": True,
        "exact_certificate_replay_rejected": True,
    }


def compute_payload(selector_prime: int):
    if selector_prime not in PRIMES:
        fail("selector prime")
    v37, parser, rows, row_hashes, variables, bridge = load_sources()
    controls = exact_controls(parser, rows)
    by_name = {item["name"]: item for item in rows}
    if TARGET_NAME not in by_name:
        fail("missing target")
    target = by_name[TARGET_NAME]["polynomial"]
    if len(target) != 552 or object_hash(encode_polynomial(target)) != bridge["rows"][TARGET_NAME]["q_rho0_sha256"]:
        fail("target bridge")
    other_rows = [item for item in rows if item["name"] != TARGET_NAME]
    if len(other_rows) != 50:
        fail("other nonzero row count")
    products = v37.build_products(19, parser, other_rows, variables)
    products.sort(key=lambda item: (item["grade"], item["row"], item["multiplier"]))
    if len(products) != EXPECTED_PRODUCTS or any(product["row"] == TARGET_NAME for product in products):
        fail("other product census")
    component_indices, ordered_monomials = target_component(products, target)
    union_support = set(target)
    for product in products:
        union_support.update(product["polynomial"])
    if len(union_support) != EXPECTED_UNION_SUPPORT:
        fail(("union support", len(union_support)))
    certificate, residual, reduction_terms = exact_certificate(
        products, component_indices, ordered_monomials, target, selector_prime)
    census = {
        "generator_rows_named": 69,
        "generator_rows_nonzero": len(other_rows),
        "registered_variable_count": len(variables),
        "products": len(products),
        "product_nnz": sum(len(product["polynomial"]) for product in products),
        "union_support_including_target": len(union_support),
        "target_terms": len(target),
        "component_products": len(component_indices),
        "component_monomials": len(ordered_monomials),
        "component_nnz": sum(len(products[index]["polynomial"]) for index in component_indices),
        "component_seeded_by_all_target_terms": True,
    }
    payload = {
        "row_bridge": bridge,
        "controls": controls,
        "target": {
            "name": TARGET_NAME,
            "grade": TARGET_GRADE,
            "q_file_sha256": row_hashes[TARGET_NAME],
            "q_rho0_sha256": object_hash(encode_polynomial(target)),
            "polynomial": encode_polynomial(target),
        },
        "census": census,
        "certificate": certificate,
        "residual": {
            "polynomial_sha256": object_hash(encode_polynomial(residual)),
            "term_count": len(residual),
            "v34_supported_term_count": sum(1 for key in residual if {name for name, _ in key} <= V34_SUPPORT),
            "polynomial": encode_polynomial(residual),
            "reduction_terms": reduction_terms,
        },
        "negative_control": mutation_control(certificate, target),
        "scope": SCOPE,
    }
    replay_payload(payload, products, component_indices, target)
    return payload


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--selector-prime", type=int, choices=PRIMES, required=True)
    cli.add_argument("--registered-lane", required=True)
    args = cli.parse_args()
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    match = LANE_RE.fullmatch(tag)
    if (platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2"
            or tag != args.registered_lane or match is None or int(match.group(1)) != args.selector_prime):
        fail("registered V39 AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    payload = compute_payload(args.selector_prime)
    result = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": tag,
        "selector_prime_requested": args.selector_prime,
        "preregistration_sha256": PREREG_SHA,
        "row_bridge_sha256": BRIDGE_SHA,
        "payload": payload,
    }
    path = output / "result.json"
    path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(f"V39_OUTCOME={payload['certificate']['kind']}")
    print(f"V39_EXACT_RANK={payload['certificate']['exact_rank']}")
    print(f"V39_RESIDUAL_TERMS={payload['residual']['term_count']}")
    print(STATUS)
    print(f"RESULT_SHA256={digest(path)}")


if __name__ == "__main__":
    main()
