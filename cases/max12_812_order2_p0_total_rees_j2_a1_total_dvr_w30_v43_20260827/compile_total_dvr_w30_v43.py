#!/usr/bin/env python3
"""Compile the weight-30 ordered-a1 total-rho DVR membership problem.

Heavy enumeration and exact linear algebra are AWS-only.  This compiler
regenerates the literal total rows, bridges rho=0 to all 70 frozen rows,
builds the complete fixed-weight Q[t]-module (t=rho^2), and gates the total
DVR calculation on exact/screening rho=0 membership of a1^6.
"""

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


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V35 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/evaluate_grade19_orbit_v35.py"
V35_SHA256 = "843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc"
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA256 = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
V42_REPLAY = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py"
V42_REPLAY_SHA256 = "f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459"
V42_REPORT = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md"
V42_REPORT_SHA256 = "5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-sol-20260827.md"
DESIGN_SHA256 = "e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7"
DESIGN_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-hostile-review-fable5-20260827.md"
DESIGN_REVIEW_SHA256 = "a836a978a6b9f05370322fb39c2cf1c45fa6907c337f10ef3ee9456d2e2f0f6d"
DESIGN_ERRATUM = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-erratum-v43-sol-20260827.md"
DESIGN_ERRATUM_SHA256 = "d322d4177d4592d02100a8eaaa7841c463c44d7cd67b44cbdd6529f4bc721808"
PREREG = HERE / "PREREGISTRATION.md"
WEIGHT = 30
EXPONENT = 6
ROWS = tuple(range(1, 8))
MODES = ("exact", "modp")

Monomial = tuple[tuple[str, int], ...]
TPolynomial = dict[int, Fraction]
ModulePolynomial = dict[Monomial, TPolynomial]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_module(path: Path, expected: str, name: str):
    actual = digest(path)
    if actual != expected:
        fail(("module hash", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(mode: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    prefix = "max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_"
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith(prefix)
        or f"_{mode}_" not in tag
    ):
        fail("registered V43 AWS EC2 lane required")
    return tag


def encode_fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def encode_monomial(monomial: Monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def canonical_t_polynomial(polynomial: ModulePolynomial) -> bytes:
    record = [
        {
            "monomial": encode_monomial(monomial),
            "t_coefficients": [[degree, *encode_fraction(coefficient)]
                               for degree, coefficient in sorted(tpoly.items())],
        }
        for monomial, tpoly in sorted(polynomial.items())
    ]
    return json.dumps(record, sort_keys=True, separators=(",", ":")).encode()


def clean_t(tpoly: TPolynomial) -> TPolynomial:
    return {degree: coefficient for degree, coefficient in tpoly.items() if coefficient}


def total_to_t(polynomial, parser, grade: int) -> ModulePolynomial:
    answer: ModulePolynomial = {}
    for monomial, coefficient in polynomial.items():
        exponents = dict(monomial)
        rho_exponent = exponents.pop("rho", 0)
        if rho_exponent % 2:
            fail(("odd rho exponent", grade, monomial))
        positive = tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))
        if sum(parser.sigma_weight(name) * exponent for name, exponent in positive) != grade:
            fail(("total sigma homogeneity", grade, monomial))
        tpoly = answer.setdefault(positive, {})
        degree = rho_exponent // 2
        tpoly[degree] = tpoly.get(degree, Fraction(0)) + coefficient
    return {monomial: clean_t(tpoly) for monomial, tpoly in answer.items() if clean_t(tpoly)}


def multiply_monomial(v37, polynomial: ModulePolynomial, multiplier: Monomial) -> ModulePolynomial:
    return {v37.merge_monomials(monomial, multiplier): dict(tpoly)
            for monomial, tpoly in polynomial.items()}


def build_products(v37, parser, rows, variables):
    products = []
    multiplier_cache = {}
    for item in rows:
        complement = WEIGHT - item["grade"]
        if complement < 0:
            continue
        multipliers = multiplier_cache.setdefault(
            complement, v37.monomials_of_weight(variables, parser, complement)
        )
        for multiplier in multipliers:
            products.append({
                "row": item["name"],
                "grade": item["grade"],
                "multiplier": multiplier,
                "polynomial": multiply_monomial(v37, item["polynomial"], multiplier),
            })
    return products


def target_component(products, target: Monomial):
    incidence: dict[Monomial, list[int]] = {}
    for index, product in enumerate(products):
        for monomial in product["polynomial"]:
            incidence.setdefault(monomial, []).append(index)
    monomials = {target}
    indices: set[int] = set()
    queue = deque((target,))
    while queue:
        monomial = queue.popleft()
        for index in incidence.get(monomial, ()):
            if index in indices:
                continue
            indices.add(index)
            for neighbor in products[index]["polynomial"]:
                if neighbor not in monomials:
                    monomials.add(neighbor)
                    queue.append(neighbor)
    return sorted(indices), sorted(monomials)


def specialize_t0(polynomial: ModulePolynomial):
    return {monomial: tpoly[0] for monomial, tpoly in polynomial.items()
            if tpoly.get(0)}


def modular_value(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad modular denominator", prime, value))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def modular_membership(polynomials, monomials, target: Monomial, prime: int):
    column = {monomial: index for index, monomial in enumerate(monomials)}
    basis = {}
    selected = []
    for original_index, polynomial in enumerate(polynomials):
        vector = {
            column[monomial]: modular_value(coefficient, prime)
            for monomial, coefficient in polynomial.items()
            if modular_value(coefficient, prime)
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, prime)
                vector = {index: value * inverse % prime for index, value in vector.items()
                          if value * inverse % prime}
                basis[pivot] = vector
                selected.append(original_index)
                break
            old = basis[pivot]
            for index, value in old.items():
                new_value = (vector.get(index, 0) - coefficient * value) % prime
                if new_value:
                    vector[index] = new_value
                else:
                    vector.pop(index, None)
    target_vector = {column[target]: 1}
    while target_vector:
        pivot = min(target_vector)
        coefficient = target_vector[pivot]
        if pivot not in basis:
            break
        old = basis[pivot]
        for index, value in old.items():
            new_value = (target_vector.get(index, 0) - coefficient * value) % prime
            if new_value:
                target_vector[index] = new_value
            else:
                target_vector.pop(index, None)
    return {
        "outcome": "member" if not target_vector else "nonmember",
        "rank": len(basis),
        "selected_product_indices": selected,
        "residual_pivot": None if not target_vector else min(target_vector),
    }


def leaf_peel_dual(polynomials, monomials, target: Monomial):
    """Peel the underdetermined dual constraints, solving exactly if core-free."""
    coordinate = {monomial: index for index, monomial in enumerate(monomials)}
    target_index = coordinate[target]
    equations = []
    right_hand_sides = []
    incidence = [set() for _ in monomials]
    for equation_index, polynomial in enumerate(polynomials):
        equation = {coordinate[monomial]: coefficient
                    for monomial, coefficient in polynomial.items()
                    if monomial != target and coefficient}
        equations.append(equation)
        right_hand_sides.append(-polynomial.get(target, Fraction(0)))
        for variable_index in equation:
            incidence[variable_index].add(equation_index)
    active = [True] * len(equations)
    queue = deque(index for index, neighbors in enumerate(incidence)
                  if index != target_index and len(neighbors) == 1)
    peeled = []
    while queue:
        variable_index = queue.popleft()
        neighbors = incidence[variable_index]
        if len(neighbors) != 1:
            continue
        equation_index = next(iter(neighbors))
        if not active[equation_index]:
            fail("inactive leaf incidence")
        peeled.append((equation_index, variable_index))
        active[equation_index] = False
        for neighbor_variable in equations[equation_index]:
            incidence[neighbor_variable].discard(equation_index)
            if len(incidence[neighbor_variable]) == 1:
                queue.append(neighbor_variable)
    core_equations = [index for index, live in enumerate(active) if live]
    core_variables = sorted({variable for equation_index in core_equations
                             for variable in equations[equation_index]})
    forced_core_equations = [index for index in core_equations
                             if right_hand_sides[index]]
    census = {
        "equations": len(equations),
        "variables_including_target": len(monomials),
        "target_incident_equations": sum(target_index in {
            coordinate[monomial] for monomial in polynomial
        } for polynomial in polynomials),
        "peeled_equations": len(peeled),
        "core_equations": len(core_equations),
        "core_variables": len(core_variables),
        "core_nnz": sum(len(equations[index]) for index in core_equations),
        "forced_core_equations": len(forced_core_equations),
    }
    if forced_core_equations:
        return {"outcome": "core", "census": census,
                "core_equation_indices": core_equations,
                "core_variable_indices": core_variables}

    # A homogeneous cyclic core is solved by zero.  Only the component of
    # the affine target condition needs back-substitution through the peel.
    values = {target_index: Fraction(1)}
    for equation_index, pivot_variable in reversed(peeled):
        equation = equations[equation_index]
        residual = right_hand_sides[equation_index] - sum(
            coefficient * values.get(variable_index, Fraction(0))
            for variable_index, coefficient in equation.items()
            if variable_index != pivot_variable
        )
        values[pivot_variable] = residual / equation[pivot_variable]
    functional = {monomials[index]: value for index, value in values.items() if value}
    if functional.get(target) != 1:
        fail("leaf dual target")
    if any(sum(coefficient * functional.get(monomial, Fraction(0))
               for monomial, coefficient in polynomial.items())
           for polynomial in polynomials):
        fail("leaf dual replay")
    return {"outcome": "nonmember", "census": census, "functional": functional}


def coefficient_text(value: Fraction, characteristic: int) -> str:
    if characteristic:
        return str(modular_value(value, characteristic))
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def tpoly_text(tpoly: TPolynomial, characteristic: int) -> str:
    pieces = []
    for degree, coefficient in sorted(tpoly.items()):
        text = coefficient_text(coefficient, characteristic)
        if degree:
            text += "*t" if degree == 1 else f"*t^{degree}"
        pieces.append(text)
    return ("+".join(pieces) if pieces else "0").replace("+-", "-")


def vector_text(polynomial: ModulePolynomial, monomial_index, characteristic: int) -> str:
    pieces = []
    for monomial, tpoly in sorted(polynomial.items()):
        coefficient = tpoly_text(tpoly, characteristic)
        if coefficient != "0":
            pieces.append(f"({coefficient})*gen({monomial_index[monomial]})")
    return "+".join(pieces) if pieces else "0"


def write_singular(path: Path, component_products, component_monomials,
                   target: Monomial, characteristic: int, output: Path):
    if not component_products or target not in component_monomials:
        fail("empty total target component")
    monomial_index = {monomial: index + 1 for index, monomial in enumerate(component_monomials)}
    lines = [
        f"ring R={characteristic},(t),dp;",
        "option(redSB);",
        # Positive and homogeneous-even specialization/saturation-gap controls.
        "module NEG=(1)*gen(1)+(-t)*gen(2); vector NT=gen(1); module NE=NEG,NT; module NZ=syz(NE);",
        "int cj; int negFound=0;",
        "for (cj=1;cj<=ncols(NZ);cj++) { if (subst(NZ[2,cj],t,0)!=0) { negFound=1; } }",
        "if (negFound!=0) { print(\"FAIL_DVR_NEGATIVE_CONTROL\"); quit; }",
        "module POS=(1)*gen(1); vector PT=gen(1); module PE=POS,PT; module PZ=syz(PE); int posFound=0;",
        "for (cj=1;cj<=ncols(PZ);cj++) { if (subst(PZ[2,cj],t,0)!=0) { posFound=1; } }",
        "if (posFound!=1) { print(\"FAIL_DVR_POSITIVE_CONTROL\"); quit; }",
        "print(\"V43_DVR_TOY_CONTROLS=1\");",
        "module M=",
    ]
    for index, product in enumerate(component_products):
        suffix = "," if index + 1 < len(component_products) else ";"
        lines.append(vector_text(product["polynomial"], monomial_index, characteristic) + suffix)
    target_index = monomial_index[target]
    certificate_path = output / "dvr_syzygy_certificate.txt"
    unit_path = output / "dvr_unit_factor.poly"
    lines += [
        f"vector T=gen({target_index});",
        "module E=M,T;",
        "module Z=syz(E);",
        "matrix CHECK=matrix(E)*matrix(Z);",
        "if (CHECK!=0) { print(\"FAIL_DVR_SYZYGY_REPLAY\"); quit; }",
        "int found=0; int chosen=0; poly uc;",
        "for (cj=1;cj<=ncols(Z);cj++)",
        "{",
        f"  uc=Z[{len(component_products) + 1},cj];",
        "  if ((found==0) && (subst(uc,t,0)!=0)) { found=1; chosen=cj; }",
        "}",
        f"print(\"V43_DVR_SYZYGY_ROWS={len(component_products) + 1}\");",
        "print(\"V43_DVR_SYZYGY_COLS=\"+string(ncols(Z)));",
        "if (found==1)",
        "{",
        "  poly U=uc/subst(uc,t,0);",
        "  if (subst(U,t,0)!=1) { print(\"FAIL_DVR_UNIT_NORMALIZATION\"); quit; }",
        "  matrix C[nrows(Z)][1]; int ci;",
        "  for (ci=1;ci<=nrows(Z);ci++) { C[ci,1]=Z[ci,chosen]; }",
        "  matrix CREPLAY=matrix(E)*C;",
        "  if (CREPLAY!=0) { print(\"FAIL_DVR_CHOSEN_REPLAY\"); quit; }",
        f"  write(\"{certificate_path}\",C);",
        f"  write(\"{unit_path}\",U);",
        "  print(\"V43_DVR_OUTCOME=member\");",
        "  print(\"V43_DVR_UNIT_CONSTANT=1\");",
        "}",
        "else",
        "{",
        "  print(\"V43_DVR_OUTCOME=nonmember\");",
        "}",
        "print(\"PASS_A1_TOTAL_DVR_W30_V43_SINGULAR\");",
        "quit;",
    ]
    path.write_text("\n".join(lines) + "\n")


def reconstruct_rows():
    v35 = load_module(V35, V35_SHA256, "v43_v35")
    v37 = load_module(V37, V37_SHA256, "v43_v37")
    v33 = v35.load(v35.V33_MODULE, v35.V33_MODULE_SHA, "v43_v33")
    v28 = v33.load_module(v33.V28_MODULE, v33.V28_MODULE_SHA, "v43_v28")
    v20 = v33.load_module(v33.V20_MODULE, v33.V20_SHA, "v43_v20")
    parser = v33.load_module(v33.V23_PARSER, v33.V23_PARSER_SHA, "v43_parser")
    frozen_parser, frozen_rows, frozen_hashes, frozen_variables = v37.load_rows()
    if frozen_variables != sorted(frozen_variables) or len(frozen_variables) != 65:
        fail("frozen variable census")
    if any(parser.sigma_weight(name) != frozen_parser.sigma_weight(name)
           for name in frozen_variables):
        fail("parser weight disagreement")

    base = v20.load_replay()
    base.MAX_DEGREE = 19
    tails = json.loads(v20.TAILS.read_text())
    coefficients, loads = v35.build_source_series_19(base)
    totals = {row: v28.build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}
    frozen_by_name = {item["name"]: item["polynomial"] for item in frozen_rows}
    killed = parser.J1 | frozenset({"a0"})
    total_rows = []
    total_hashes = {}
    bridge_count = 0
    nonzero_general = 0
    for grade in range(10, 20):
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            face = parser.specialize(totals[row][grade], killed, {})
            rho0 = parser.specialize(face, frozenset({"rho"}), {})
            if rho0 != frozen_by_name.get(name, {}):
                fail(("rho-zero frozen bridge", name))
            bridge_count += 1
            tform = total_to_t(face, parser, grade)
            total_hashes[name] = sha256(canonical_t_polynomial(tform)).hexdigest()
            if tform:
                total_rows.append({"name": name, "grade": grade, "row": row, "polynomial": tform})
                nonzero_general += 1
    active = sorted({name for item in total_rows for monomial in item["polynomial"]
                     for name, _ in monomial})
    general_only = sorted(set(active) - set(frozen_variables))
    missing_frozen = sorted(set(frozen_variables) - set(active))
    if (bridge_count != 70 or missing_frozen
            or any(parser.sigma_weight(name) <= 0 for name in active)):
        fail(("total source census", bridge_count, general_only, missing_frozen))
    return (parser, v37, total_rows, frozen_hashes, total_hashes, active,
            frozen_variables, general_only, nonzero_general)


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--mode", choices=MODES, required=True)
    cli.add_argument("--selector-prime", type=int, choices=(65519, 65521), required=True)
    cli.add_argument("--phase", choices=("preflight", "solve"), default="solve")
    args = cli.parse_args()
    tag = require_aws(args.mode)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    for path, expected in (
        (V42_REPLAY, V42_REPLAY_SHA256),
        (V42_REPORT, V42_REPORT_SHA256),
        (DESIGN, DESIGN_SHA256),
        (DESIGN_REVIEW, DESIGN_REVIEW_SHA256),
        (DESIGN_ERRATUM, DESIGN_ERRATUM_SHA256),
    ):
        if digest(path) != expected:
            fail(("custody hash", str(path), digest(path), expected))

    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only_variables, nonzero_general) = reconstruct_rows()
    general_only_records = []
    for item in total_rows:
        for monomial, tpoly in sorted(item["polynomial"].items()):
            if any(name in general_only_variables for name, _ in monomial):
                general_only_records.append({
                    "row": item["name"],
                    "grade": item["grade"],
                    "monomial": encode_monomial(monomial),
                    "t_coefficients": [
                        [degree, *encode_fraction(coefficient)]
                        for degree, coefficient in sorted(tpoly.items())
                    ],
                })
    if (not general_only_records
            or any(record["t_coefficients"][0][0] < 1 for record in general_only_records)):
        fail(("general-only specialization support", general_only_records[:2]))
    general_only_path = output / "general_only_total_terms.json"
    general_only_path.write_text(json.dumps(general_only_records, sort_keys=True, indent=2) + "\n")
    target: Monomial = (("a1", EXPONENT),)
    products = build_products(v37, parser, total_rows, variables)
    total_indices, total_monomials = target_component(products, target)
    total_component = [products[index] for index in total_indices]
    special_products = []
    for product in products:
        polynomial = specialize_t0(product["polynomial"])
        if polynomial:
            special_products.append({**{key: product[key] for key in ("row", "grade", "multiplier")},
                                     "polynomial": polynomial})
    special_indices, special_monomials = v37.target_component(special_products, target)
    special_component = [special_products[index] for index in special_indices]
    special_polynomials = [item["polynomial"] for item in special_component]
    peel = leaf_peel_dual(special_polynomials, special_monomials, target)
    census = {
        "weight": WEIGHT,
        "exponent": EXPONENT,
        "named_rows": len(frozen_hashes),
        "general_nonzero_rows": nonzero_general,
        "rho0_positive_variables": len(frozen_variables),
        "positive_variables": len(variables),
        "general_only_variables": general_only_variables,
        "general_only_term_records": len(general_only_records),
        "general_only_min_t_degree": min(
            coefficient[0]
            for record in general_only_records
            for coefficient in record["t_coefficients"]
        ),
        "products": len(products),
        "total_support": len({target} | {m for product in products for m in product["polynomial"]}),
        "total_component_products": len(total_component),
        "total_component_monomials": len(total_monomials),
        "total_component_nnz": sum(len(item["polynomial"]) for item in total_component),
        "rho0_nonzero_products": len(special_products),
        "rho0_component_products": len(special_component),
        "rho0_component_monomials": len(special_monomials),
        "rho0_component_nnz": sum(len(item["polynomial"]) for item in special_component),
        "rho0_dual_leaf_peel": peel["census"],
        "max_t_degree_rows": max((degree for item in total_rows for tpoly in item["polynomial"].values()
                                  for degree in tpoly), default=0),
    }
    print("V43_PREFLIGHT=" + json.dumps(census, sort_keys=True, separators=(",", ":")), flush=True)

    base_result = {
        "schema_version": 1,
        "status": "PASS-A1-TOTAL-DVR-W30-V43-PREFLIGHT" if args.phase == "preflight"
                  else "PASS-A1-TOTAL-DVR-W30-V43-COMPILER",
        "registered_aws_lane": tag,
        "mode": args.mode,
        "phase": args.phase,
        "selector_prime_requested": args.selector_prime,
        "preregistration_sha256": digest(PREREG),
        "design_sha256": DESIGN_SHA256,
        "design_review_sha256": DESIGN_REVIEW_SHA256,
        "design_erratum_sha256": DESIGN_ERRATUM_SHA256,
        "general_only_total_terms": str(general_only_path),
        "general_only_total_terms_sha256": digest(general_only_path),
        "v35_sha256": V35_SHA256,
        "v37_sha256": V37_SHA256,
        "v42_replay_sha256": V42_REPLAY_SHA256,
        "v42_report_sha256": V42_REPORT_SHA256,
        "frozen_row_sha256": frozen_hashes,
        "total_t_row_sha256": total_hashes,
        "census": census,
        "scope": (
            "literal total ordered-a1 rows through grade19 at weight30; "
            "closure-first Q[t]_(t) exponent-six discriminator only"
        ),
    }
    if args.phase == "preflight":
        result_path = output / "result.json"
        result_path.write_text(json.dumps(base_result, sort_keys=True, indent=2) + "\n")
        print("PASS-A1-TOTAL-DVR-W30-V43-PREFLIGHT")
        print(f"RESULT_SHA256={digest(result_path)}")
        return

    if args.mode == "exact":
        if peel["outcome"] != "nonmember":
            fail(("rho0 dual cyclic core requires sparse exact solver", peel["census"]))
        certificate = {
            "outcome": "nonmember",
            "selector_prime": args.selector_prime,
            "rank": None,
            "functional": [
                {"monomial": encode_monomial(monomial),
                 "coefficient": encode_fraction(coefficient)}
                for monomial, coefficient in sorted(peel["functional"].items())
            ],
            "leaf_peel_census": peel["census"],
        }
        v37.replay_certificate(certificate, special_products, special_indices, target)
        rho0 = {"evidence_tier": "exact-Q-leaf-dual", **certificate}
    else:
        rho0 = {
            "evidence_tier": "finite-field-screen",
            "selector_prime": args.selector_prime,
            **modular_membership(special_polynomials, special_monomials, target, args.selector_prime),
        }
    print(f"V43_RHO0_OUTCOME={rho0['outcome']}", flush=True)

    singular_path = None
    if rho0["outcome"] == "member":
        singular_path = output / f"total_dvr_w30_{args.mode}.sing"
        characteristic = 0 if args.mode == "exact" else args.selector_prime
        write_singular(singular_path, total_component, total_monomials, target,
                       characteristic, output)
    result = {
        **base_result,
        "rho0": rho0,
        "total_dvr_required": rho0["outcome"] == "member",
        "singular_script": None if singular_path is None else str(singular_path),
        "singular_script_sha256": None if singular_path is None else digest(singular_path),
        "implication": (
            "rho0 nonmembership excludes exponent-six total certificate"
            if rho0["outcome"] == "nonmember"
            else "rho0 membership is necessary only; run closure-first DVR syzygy"
        ),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
