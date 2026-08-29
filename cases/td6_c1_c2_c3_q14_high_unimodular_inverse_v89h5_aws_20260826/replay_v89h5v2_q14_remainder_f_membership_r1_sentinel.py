#!/usr/bin/env python3
"""Exact localized-(F) membership gate for the V89H5 q14 remainder."""

import ast
import csv
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V1_CLIENT = HERE / "replay_v89h5_q14_high_unimodular_total_f_v1.py"
V1_CLIENT_SHA256 = "a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b"
REMAINDER = HERE / "V1_Q14_HIGH_P12_REMAINDER_BOX02.tsv"
REMAINDER_SHA256 = "eb939448f5636a3084ca129aa3a5cdf44709ac3a8ca28be77a14c2e5fdea7c14"
REMAINDER_DUAL = HERE / "V1_Q14_HIGH_P12_REMAINDER_R6D.tsv"

assert sha256(V1_CLIENT.read_bytes()).hexdigest() == V1_CLIENT_SHA256
assert sha256(REMAINDER.read_bytes()).hexdigest() == REMAINDER_SHA256
assert sha256(REMAINDER_DUAL.read_bytes()).hexdigest() == REMAINDER_SHA256
assert REMAINDER.read_bytes() == REMAINDER_DUAL.read_bytes()

spec = importlib.util.spec_from_file_location("td6_v89h5v2_v1_parent", V1_CLIENT)
v1 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v1
spec.loader.exec_module(v1)

m, v85 = v1.m, v1.v85
E3, Rat3 = v1.E3, v1.Rat3
C, V, U, F, H, B3 = v1.C, v1.V, v1.U, v1.F, v1.H, v1.B3


def parse_base_polynomial(text):
    """Parse the frozen Q[C,V,U] printer grammar through a tiny AST."""
    tree = ast.parse(text.replace("^", "**"), mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant):
            assert isinstance(node.value, int)
            return m.tri.CTX(node.value)
        if isinstance(node, ast.Name):
            assert node.id in {"C", "V", "U"}
            return {"C": C, "V": V, "U": U}[node.id]
        if isinstance(node, ast.UnaryOp):
            assert isinstance(node.op, (ast.UAdd, ast.USub))
            value = evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp):
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                assert right.total_degree() == 0 and right
                return left / right
            if isinstance(node.op, ast.Pow):
                assert isinstance(node.right, ast.Constant)
                assert isinstance(node.right.value, int) and node.right.value >= 0
                return left ** node.right.value
        raise AssertionError(("unsupported_frozen_expression", ast.dump(node)))

    return evaluate(tree)


def parse_e3(text):
    frozen = ast.literal_eval(text)
    assert isinstance(frozen, tuple) and len(frozen) == 18
    coordinates = tuple(
        Rat3(parse_base_polynomial(numerator))
        / Rat3(parse_base_polynomial(denominator))
        for numerator, denominator in frozen
    )
    return m.from_vector(coordinates), coordinates


def digest_records(records, include_header=False):
    lines = []
    if include_header:
        lines.append("parameter_monomial\tq_monomial\tcoefficient_exact")
    lines.extend(
        f"{parameter!r}\t{q_monomial!r}\t{m.e3_exact(coefficient)}"
        for parameter, q_monomial, coefficient, _ in records
    )
    text = "\n".join(lines) + "\n"
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h5v2_q14_remainder_f_membership_"
    )
    print("producer=TD6-V89H5V2-Q14-REMAINDER-F-MEMBERSHIP")
    print(f"v1_client_sha256={V1_CLIENT_SHA256}")
    print(f"dual_v1_remainder_sha256={REMAINDER_SHA256}")
    print("coefficient_ring=Q[C,V,U] localized at U*H*B3")
    print("extension_rank=18")
    print("F_not_inverted=true")
    print("q_not_inverted=true", flush=True)

    records = []
    with REMAINDER.open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        assert rows.fieldnames == [
            "parameter_monomial", "q_monomial", "coefficient_exact"
        ]
        for row in rows:
            parameter = ast.literal_eval(row["parameter_monomial"])
            q_monomial = ast.literal_eval(row["q_monomial"])
            coefficient, coordinates = parse_e3(row["coefficient_exact"])
            records.append((parameter, q_monomial, coefficient, coordinates))

    constant = [record for record in records if not record[1]]
    positive = [record for record in records if record[1]]
    assert len(constant) == 1 and len(positive) == 16
    assert {record[1] for record in positive} == {(14,)}
    assert digest_records(records, include_header=True) == REMAINDER_SHA256
    print("remainder_records=17")
    print("positive_q14_records=16")
    print("positive_other_q_records=0", flush=True)

    original_coefficients = [record[2] for record in positive]
    original_common = v85.monic(m.denominator_for(original_coefficients))
    assert v85.factors_allowed(original_common), original_common.factor()
    assert original_common.gcd(F).total_degree() == 0

    quotient_records = []
    inventory_lines = [
        "record\tparameter_monomial\tq_monomial\tcoordinate\t"
        "original_numerator\toriginal_denominator\t"
        "quotient_numerator\tquotient_denominator\t"
        "quotient_denominator_factor\tF_denominator_gcd\tregistered"
    ]
    failures = []
    divisor = Rat3(F)
    for record_index, (parameter, q_monomial, coefficient, coordinates) in enumerate(
        positive
    ):
        quotient_coordinates = []
        for coordinate_index, coordinate in enumerate(coordinates):
            quotient = coordinate / divisor
            assert quotient*divisor == coordinate
            denominator = quotient.denominator
            f_gcd = denominator.gcd(F)
            registered = (
                v85.factors_allowed(denominator)
                and f_gcd.total_degree() == 0
            )
            inventory_lines.append(
                f"{record_index}\t{parameter!r}\t{q_monomial!r}\t"
                f"{coordinate_index}\t{coordinate.numerator}\t"
                f"{coordinate.denominator}\t{quotient.numerator}\t"
                f"{denominator}\t{denominator.factor()!r}\t{f_gcd}\t"
                f"{str(registered).lower()}"
            )
            if coordinate and not registered:
                numerator_quotient = coordinate.numerator // F
                numerator_residue = coordinate.numerator - numerator_quotient*F
                assert numerator_residue
                failures.append(
                    (
                        record_index,
                        parameter,
                        q_monomial,
                        coordinate_index,
                        coordinate,
                        quotient,
                        numerator_residue,
                    )
                )
            quotient_coordinates.append(quotient)
        quotient_coefficient = m.from_vector(tuple(quotient_coordinates))
        assert E3(Rat3(F))*quotient_coefficient == coefficient
        quotient_records.append(
            (parameter, q_monomial, quotient_coefficient, quotient_coordinates)
        )

    inventory_text = "\n".join(inventory_lines) + "\n"
    inventory_path = outdir / "Q14_F_QUOTIENT_COORDINATE_INVENTORY.tsv"
    inventory_path.write_text(inventory_text)
    inventory_sha = sha256(inventory_text.encode()).hexdigest()

    quotient_coefficients = [record[2] for record in quotient_records]
    quotient_common = v85.monic(m.denominator_for(quotient_coefficients))
    membership = (
        v85.factors_allowed(quotient_common)
        and quotient_common.gcd(F).total_degree() == 0
    )
    assert membership == (not failures)

    # Fraction-field replay is exact even when its F denominator is unlicensed.
    assert all(
        E3(Rat3(F))*quotient[2] == original[2]
        for original, quotient in zip(positive, quotient_records)
    )
    omitted = quotient_records[1:]
    assert len(omitted) == 15
    assert digest_records(omitted) != digest_records(quotient_records)
    print(f"original_common_denominator=({original_common})")
    print(f"original_common_denominator_factor={original_common.factor()}")
    print(f"formal_F_quotient_common_denominator=({quotient_common})")
    print(f"formal_F_quotient_common_denominator_factor={quotient_common.factor()}")
    print(f"coordinate_inventory_sha256={inventory_sha}")
    print(f"failed_nonzero_coordinates={len(failures)}")
    print("quotient_record_omission_negative_control_index=0")
    print("quotient_record_omission_changes_replay=true", flush=True)

    if membership:
        quotient_lines = [
            "parameter_monomial\tq_monomial\tcoefficient_exact"
        ]
        quotient_lines.extend(
            f"{parameter!r}\t{q_monomial!r}\t{m.e3_exact(coefficient)}"
            for parameter, q_monomial, coefficient, _ in quotient_records
        )
        quotient_text = "\n".join(quotient_lines) + "\n"
        quotient_path = outdir / "Q14_POSITIVE_F_QUOTIENT.tsv"
        quotient_path.write_text(quotient_text)
        quotient_sha = sha256(quotient_text.encode()).hexdigest()
        print("positive_remainder_in_localized_F_ideal=true")
        print(f"polynomial_F_quotient_sha256={quotient_sha}")
        verdict = "MEMBERSHIP-PASS"
        certificate_sha = "NONE"
    else:
        (
            record_index,
            parameter,
            q_monomial,
            coordinate_index,
            coordinate,
            quotient,
            numerator_residue,
        ) = failures[0]
        certificate_lines = [
            "claim=positive_q14_remainder_not_in_localized_principal_F_ideal",
            f"record_index={record_index}",
            f"parameter_monomial={parameter!r}",
            f"q_monomial={q_monomial!r}",
            f"extension_coordinate={coordinate_index}",
            f"original_numerator={coordinate.numerator}",
            f"original_denominator={coordinate.denominator}",
            f"original_denominator_factor={coordinate.denominator.factor()!r}",
            f"original_denominator_gcd_F={coordinate.denominator.gcd(F)}",
            f"numerator_mod_F={numerator_residue}",
            f"formal_quotient_numerator={quotient.numerator}",
            f"formal_quotient_denominator={quotient.denominator}",
            f"formal_quotient_denominator_factor={quotient.denominator.factor()!r}",
            f"formal_quotient_denominator_gcd_F={quotient.denominator.gcd(F)}",
            "localization_factors=U,H,B3",
            "localization_factors_each_coprime_to_F=true",
        ]
        assert all(factor.gcd(F).total_degree() == 0 for factor in (U, H, B3))
        certificate_text = "\n".join(certificate_lines) + "\n"
        certificate_path = outdir / "Q14_F_MEMBERSHIP_NEGATIVE_CERTIFICATE.txt"
        certificate_path.write_text(certificate_text)
        certificate_sha = sha256(certificate_text.encode()).hexdigest()
        print("positive_remainder_in_localized_F_ideal=false")
        print(f"negative_certificate_sha256={certificate_sha}")
        print(f"first_failed_record={record_index}")
        print(f"first_failed_extension_coordinate={coordinate_index}")
        verdict = "NONMEMBERSHIP-PASS"

    exact_lines = [
        f"v1_client_sha256={V1_CLIENT_SHA256}",
        f"v1_remainder_sha256={REMAINDER_SHA256}",
        "positive_q14_records=16",
        f"original_common={original_common}",
        f"quotient_common={quotient_common}",
        f"membership={str(membership).lower()}",
        f"failed_nonzero_coordinates={len(failures)}",
        f"inventory_sha256={inventory_sha}",
        f"certificate_sha256={certificate_sha}",
        "claim=coefficientwise_localized_F_membership_gate_only",
    ]
    exact_text = "\n".join(exact_lines) + "\n"
    exact_path = outdir / "Q14_F_MEMBERSHIP_EXACT_RESULT.txt"
    exact_path.write_text(exact_text)
    exact_sha = sha256(exact_text.encode()).hexdigest()
    print(f"exact_result_sha256={exact_sha}")
    print("P12_FIRST_F_unit_ideal_claim=false")
    print("alternate_FIRST_combination_excluded=false")
    print("low_q_unit_charts_covered=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print(f"TD6-V89H5V2-Q14-REMAINDER-F-MEMBERSHIP {verdict}")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
