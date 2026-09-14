#!/usr/bin/env python3
"""Independent, bounded toy semantics for the frozen D125 exporter.

This deliberately constructs only a degree-six, four-slot-per-member fixture.
It does not call production_spec, construct a production row, invoke a CAS, or
open any network/worker resource.  Jacobian expectations come from formal
differentiation; lift expectations come from finite Laurent-polynomial powers.
"""
import argparse
from collections import Counter
import copy
from fractions import Fraction
import hashlib
import importlib
import json
from pathlib import Path
import resource
import signal
import sys
import time


LIMIT_AS = 512 * 1024**2
EXPECTED_PINS = {
    "exporter.py": "9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703",
    "baseline.py": "ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53",
    "test_exporter.py": "331e97c84f22592a1a28842df7c11e84e4f72355a906c156403eb5eaca490b2b",
}


class ControlFailure(Exception):
    pass


def require(condition, message):
    if not condition:
        raise ControlFailure(message)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def strict_load(line):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    return json.loads(line, object_pairs_hook=unique)


# A Q(rho) element is (a,b), with rho^2 = 3*rho - 1.  This implementation is
# intentionally separate from baseline.F.
QZERO = (Fraction(0), Fraction(0))
QONE = (Fraction(1), Fraction(0))
QRHO = (Fraction(0), Fraction(1))


def qadd(left, right):
    return (left[0] + right[0], left[1] + right[1])


def qneg(value):
    return (-value[0], -value[1])


def qscale(number, value):
    return (number * value[0], number * value[1])


def qmul(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0] + 3 * left[1] * right[1],
    )


def qwire(value):
    return [
        [str(value[0].numerator), str(value[0].denominator)],
        [str(value[1].numerator), str(value[1].denominator)],
    ]


def qdecode(wire):
    require(
        type(wire) is list
        and len(wire) == 2
        and all(type(pair) is list and len(pair) == 2 for pair in wire),
        "field wire shape",
    )
    try:
        value = (
            Fraction(int(wire[0][0]), int(wire[0][1])),
            Fraction(int(wire[1][0]), int(wire[1][1])),
        )
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ControlFailure("invalid field wire") from exc
    require(qwire(value) == wire, "noncanonical field wire")
    return value


def cadd_term(polynomial, monomial, value):
    if value == QZERO:
        return
    key = tuple(sorted(monomial))
    total = qadd(polynomial.get(key, QZERO), value)
    if total == QZERO:
        polynomial.pop(key, None)
    else:
        polynomial[key] = total


def cadd(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        cadd_term(result, monomial, coefficient)
    return result


def cscale(number, polynomial):
    result = {}
    for monomial, coefficient in polynomial.items():
        cadd_term(result, monomial, qscale(number, coefficient))
    return result


def cmul(left, right):
    result = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            cadd_term(
                result,
                left_monomial + right_monomial,
                qmul(left_coefficient, right_coefficient),
            )
    return result


def p2_add_term(polynomial, exponent, coefficient):
    if not coefficient:
        return
    total = cadd(polynomial.get(exponent, {}), coefficient)
    if total:
        polynomial[exponent] = total
    else:
        polynomial.pop(exponent, None)


def p2_mul(left, right):
    result = {}
    for (i, j), left_coefficient in left.items():
        for (k, ell), right_coefficient in right.items():
            p2_add_term(result, (i + k, j + ell), cmul(left_coefficient, right_coefficient))
    return result


def derivative(polynomial, coordinate):
    """Formal derivative of a two-variable polynomial."""
    result = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[coordinate]
        if power == 0:
            continue
        reduced = list(exponent)
        reduced[coordinate] -= 1
        p2_add_term(result, tuple(reduced), cscale(power, coefficient))
    return result


def formal_jacobian(left, right):
    first = p2_mul(derivative(left, 0), derivative(right, 1))
    second = p2_mul(derivative(left, 1), derivative(right, 0))
    result = dict(first)
    for exponent, coefficient in second.items():
        p2_add_term(result, exponent, cscale(-1, coefficient))
    return result


def laurent_mul(left, right):
    result = {}
    for (u, v), left_coefficient in left.items():
        for (w, z), right_coefficient in right.items():
            p2_add_term(result, (u + w, v + z), cmul(left_coefficient, right_coefficient))
    return result


def finite_inverse_composition(source, lambda2, lambda3):
    """Expand gamma=v^-1 and pi=v^4*u-l2*v^2-l3*v-v^-1 by finite powers."""
    pi = {
        (1, 4): {(): QONE},
        (0, 2): {(lambda2,): qneg(QONE)},
        (0, 1): {(lambda3,): qneg(QONE)},
        (0, -1): {(): qneg(QONE)},
    }
    result = {}
    for (i, j), coefficient in source.items():
        power = {(0, -i): coefficient}
        for unused in range(j):
            power = laurent_mul(power, pi)
        for exponent, expanded_coefficient in power.items():
            p2_add_term(result, exponent, expanded_coefficient)
    return result


def negative_indices(degree):
    return [
        (t, e)
        for t in range((degree - 1) // 5 + 1)
        for e in range(5 * t - degree, 0)
    ]


def fixed_entry(who, point, value):
    return {
        "point": list(point),
        "name": f"{who}_g{point[0]}_p{point[1]}",
        "fixed": qwire(value),
        "reasons": ["TOY_FIXED"],
    }


def variable_entry(who, point, variable):
    return {
        "point": list(point),
        "name": f"{who}_g{point[0]}_p{point[1]}",
        "variable": variable,
    }


def contract_data():
    maps = [
        [
            fixed_entry("A", (0, 0), QZERO),
            fixed_entry("A", (0, 2), QRHO),
            variable_entry("A", (0, 6), 0),
            fixed_entry("A", (1, 0), QONE),
        ],
        [
            fixed_entry("B", (0, 0), QZERO),
            variable_entry("B", (0, 1), 1),
            fixed_entry("B", (2, 1), QONE),
            fixed_entry("B", (3, 0), QONE),
        ],
    ]
    return {
        "header": {
            "schema": "jc2.d125-small-source-literal/v1",
            "mode": "toy",
            "case": "DECLARED_TOY_NOT_D125",
            "branch": "golden",
            "field": "Q[rho]/(rho^2-3*rho+1)",
            "expected_rows": 71,
            "expected_jacobian_rows": 49,
            "expected_lift_rows": 14,
            "expected_variables": 6,
            "target": "J-c*gamma^2",
            "status": "TOY_ONLY",
        },
        "variables": ["a", "b", "c", "z", "lambda2", "lambda3"],
        "maps": maps,
        "degrees": (6, 6),
        "jac_indices": [(i, j) for i in range(7) for j in range(7)],
        "lambda_ids": (4, 5),
        "scalar": {(2,): QONE},
        "scalar_guard": {(2, 3): QONE, (): qneg(QONE)},
        "guards": [
            {
                "label": "GUARD/A/0/2",
                "value": qwire(QRHO),
                "inverse": qwire((Fraction(3), Fraction(-1))),
            }
        ],
    }


def source_map(entries):
    result = {}
    for entry in entries:
        point = tuple(entry["point"])
        if "fixed" in entry:
            result[point] = {(): qdecode(entry["fixed"])}
        else:
            result[point] = {(entry["variable"],): QONE}
    return result


def row_record(label, polynomial, kind):
    return {
        "type": "row",
        "kind": kind,
        "label": label,
        "terms": [
            [qwire(coefficient), list(monomial)]
            for monomial, coefficient in sorted(polynomial.items())
            if coefficient != QZERO
        ],
    }


def expected_prefix(specification):
    records = [{"type": "header", **specification["header"]}]
    for index, name in enumerate(specification["variables"]):
        records.append({"type": "variable", "id": index, "name": name})
    for who, entries in zip(("A", "B"), specification["maps"]):
        for entry in entries:
            records.append({"type": "coefficient", "member": who, **entry})
    for who, entries in zip(("A", "B"), specification["maps"]):
        for entry in entries:
            if "fixed" in entry:
                records.append(row_record("FIX/" + entry["name"], {}, "fixed_assignment"))

    sources = [source_map(entries) for entries in specification["maps"]]
    jacobian = formal_jacobian(sources[0], sources[1])
    for i, j in specification["jac_indices"]:
        coefficient = dict(jacobian.get((i, j), {}))
        if (i, j) == (2, 0):
            coefficient = cadd(coefficient, cscale(-1, specification["scalar"]))
        records.append(row_record(f"J/{i}/{j}", coefficient, "jacobian"))

    for who, source, degree in zip(("A", "B"), sources, specification["degrees"]):
        composition = finite_inverse_composition(source, *specification["lambda_ids"])
        for t, e in negative_indices(degree):
            records.append(
                row_record(f"LIFT/{who}/{t}/{e}", composition.get((t, e), {}), "polynomiality")
            )
    for guard in specification["guards"]:
        require(qmul(qdecode(guard["value"]), qdecode(guard["inverse"])) == QONE, "guard inverse")
        records.append(
            {
                **row_record(guard["label"], {}, "fixed_unit_guard"),
                "value": guard["value"],
                "inverse": guard["inverse"],
            }
        )
    records.append(row_record("GUARD/c", specification["scalar_guard"], "scalar_guard"))
    return records


def footer_for(prefix, variable_count):
    counts = Counter()
    used = set()
    for record in prefix:
        if record.get("type") != "row":
            continue
        counts["rows"] += 1
        counts[record["kind"]] += 1
        counts["terms"] += len(record["terms"])
        counts["zero_rows"] += not record["terms"]
        for field_wire, monomial in record["terms"]:
            qdecode(field_wire)
            require(monomial == sorted(monomial), "unsorted monomial")
            require(
                all(type(index) is int and 0 <= index < variable_count for index in monomial),
                "invalid variable id",
            )
            used.update(monomial)
    digest = hashlib.sha256(b"".join(canonical(record) for record in prefix)).hexdigest()
    return {
        "type": "footer",
        "complete": True,
        "prefix_sha256": digest,
        "prefix_records": len(prefix),
        "counts": dict(counts),
        "unused_variables": [index for index in range(variable_count) if index not in used],
    }


def parse_stream(data):
    require(data.endswith(b"\n"), "stream lacks final newline")
    lines = data.splitlines(keepends=True)
    require(lines, "empty stream")
    records = []
    for line in lines:
        record = strict_load(line)
        require(canonical(record) == line, "noncanonical record")
        records.append(record)
    require(records[-1].get("type") == "footer", "missing terminal footer")
    require(all(record.get("type") != "footer" for record in records[:-1]), "nonterminal footer")
    return records


def verify_footer_only(data, variable_count):
    records = parse_stream(data)
    require(records[-1] == footer_for(records[:-1], variable_count), "footer not fully repaired")
    return records


def independent_verify(data, specification):
    records = verify_footer_only(data, len(specification["variables"]))
    expected = expected_prefix(specification)
    require(len(records) - 1 == len(expected), "semantic record count mismatch")
    for index, (actual, wanted) in enumerate(zip(records[:-1], expected)):
        require(actual == wanted, f"semantic mismatch at record {index}: {wanted.get('label', wanted['type'])}")
    require(records[-1] == footer_for(expected, len(specification["variables"])), "semantic footer mismatch")


def repaired_bytes(records, variable_count):
    prefix = records[:-1]
    repaired = prefix + [footer_for(prefix, variable_count)]
    return b"".join(canonical(record) for record in repaired)


def exporter_spec(exporter, specification):
    baseline = exporter.B
    maps = copy.deepcopy(specification["maps"])
    return {
        "header": copy.deepcopy(specification["header"]),
        "variables": list(specification["variables"]),
        "maps": maps,
        "sources": [exporter.source_map(entries) for entries in maps],
        "degrees": specification["degrees"],
        "jac_indices": list(specification["jac_indices"]),
        "lambda_ids": specification["lambda_ids"],
        "scalar": {(2,): baseline.ONE},
        "scalar_guard": {(2, 3): baseline.ONE, (): -baseline.ONE},
        "guards": copy.deepcopy(specification["guards"]),
    }


def mutations(original_records):
    changed = {}

    row = copy.deepcopy(original_records)
    row = [record for record in row if record.get("label") != "LIFT/A/0/-1"]
    changed["row"] = row

    field = copy.deepcopy(original_records)
    field_index = next(
        index
        for index, record in enumerate(field)
        if record.get("type") == "row"
        and any(qdecode(field_wire)[1] != 0 for field_wire, monomial in record["terms"])
    )
    old = field[field_index]
    parts = []
    for component_index, suffix in ((0, "a"), (1, "b")):
        terms = []
        for field_wire, monomial in old["terms"]:
            component = qdecode(field_wire)[component_index]
            if component:
                terms.append([qwire((component, Fraction(0))), monomial])
        parts.append({**old, "label": old["label"] + "/" + suffix, "terms": terms})
    field[field_index : field_index + 1] = parts
    changed["field"] = field

    target = copy.deepcopy(original_records)
    target_row = next(record for record in target if record.get("label") == "J/2/0")
    target_term = next(term for term in target_row["terms"] if term[1] == [2])
    target_term[0] = qwire(qneg(qdecode(target_term[0])))
    changed["target"] = target

    face = copy.deepcopy(original_records)
    face_record = next(
        record
        for record in face
        if record.get("type") == "coefficient" and record.get("fixed") == qwire(QZERO)
    )
    face_record["fixed"] = qwire(QONE)
    changed["face"] = face

    guard = copy.deepcopy(original_records)
    guard_row = next(record for record in guard if record.get("label") == "GUARD/c")
    guard_row["terms"] = [term for term in guard_row["terms"] if term[1] != []]
    changed["guard"] = guard

    exponent = copy.deepcopy(original_records)
    exponent_row = next(
        record
        for record in exponent
        if record.get("kind") == "polynomiality" and any(term[1] for term in record["terms"])
    )
    exponent_term = next(term for term in exponent_row["terms"] if term[1])
    exponent_term[1] = sorted(exponent_term[1] + [exponent_term[1][-1]])
    changed["exponent"] = exponent
    return changed


def expect_rejection(function, label):
    try:
        function()
    except (ControlFailure, ValueError, RuntimeError, OSError, ZeroDivisionError) as exc:
        return type(exc).__name__ + ": " + str(exc)
    raise ControlFailure(label + " was accepted")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", required=True, help="relocatable frozen input directory")
    parser.add_argument("--artifacts", required=True)
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    resource.setrlimit(resource.RLIMIT_AS, (LIMIT_AS, LIMIT_AS))
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
    signal.alarm(30)
    started = time.monotonic()

    input_directory = Path(arguments.inputs).resolve()
    artifact_directory = Path(arguments.artifacts).resolve()
    output_path = Path(arguments.output).resolve()
    require(input_directory.is_dir(), "inputs directory absent")
    require(artifact_directory.parent == output_path.parent, "evidence must share owned directory")
    artifact_directory.mkdir(parents=False, exist_ok=False)
    require(not output_path.exists(), "exclusive result path already exists")

    observed_pins = {}
    for name, expected in EXPECTED_PINS.items():
        path = input_directory / name
        observed_pins[name] = sha256(path)
        require(observed_pins[name] == expected, "frozen input pin mismatch: " + name)

    sys.path.insert(0, str(input_directory))
    exporter = importlib.import_module("exporter")
    require(Path(exporter.__file__).resolve() == input_directory / "exporter.py", "wrong exporter import")

    specification = contract_data()
    frozen_specification = exporter_spec(exporter, specification)
    generated_records = list(exporter.records(frozen_specification))
    generated_data = b"".join(exporter.B.canonical(record) for record in generated_records)
    original_path = artifact_directory / "original.jsonl"
    original_path.write_bytes(generated_data)

    independent_verify(generated_data, specification)
    exporter.verify_stream(original_path, frozen_specification)
    expected = expected_prefix(specification)
    require(len(expected) == 1 + 6 + 8 + 71, "unexpected independent prefix length")
    expected_rows = [record for record in expected if record.get("type") == "row"]
    require(len(expected_rows) == 71, "independent row count")
    require(sum(record.get("kind") == "jacobian" for record in expected_rows) == 49, "Jacobian row count")
    require(sum(record.get("kind") == "polynomiality" for record in expected_rows) == 14, "lift row count")

    outcomes = {}
    for name, records in mutations(generated_records).items():
        data = repaired_bytes(records, len(specification["variables"]))
        path = artifact_directory / (name + ".jsonl")
        path.write_bytes(data)
        verify_footer_only(data, len(specification["variables"]))
        semantic_error = expect_rejection(
            lambda candidate=data: independent_verify(candidate, specification),
            "independent " + name,
        )
        replay_error = expect_rejection(
            lambda candidate_path=path: exporter.verify_stream(candidate_path, frozen_specification),
            "frozen replay " + name,
        )
        outcomes[name] = {
            "footer_repaired": True,
            "independent_rejected": semantic_error,
            "frozen_replay_rejected": replay_error,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }

    require(set(outcomes) == {"row", "field", "target", "face", "guard", "exponent"}, "mutation coverage")
    elapsed = time.monotonic() - started
    result = {
        "status": "PASS",
        "python_optimized": bool(sys.flags.optimize),
        "method": {
            "jacobian": "independent formal derivatives then polynomial multiplication",
            "lift": "independent finite powers of the four-term Laurent substitution",
            "footer": "canonical syntax plus independently recomputed counts, used ids, record count, and SHA-256",
        },
        "pins": observed_pins,
        "source_stream": {
            "path": str(original_path),
            "bytes": len(generated_data),
            "sha256": hashlib.sha256(generated_data).hexdigest(),
            "rows": 71,
            "jacobian_rows": 49,
            "lift_rows": 14,
        },
        "mutations": outcomes,
        "mutation_count": len(outcomes),
        "each_rejected_by": ["independent_semantic_verifier", "frozen_strict_replay"],
        "production_rows_generated": 0,
        "cas_sympy_aws_network": False,
        "limits": {"wall_seconds": 30, "cpu_seconds": 25, "address_space_bytes": LIMIT_AS},
        "elapsed_seconds": elapsed,
        "maxrss_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    with output_path.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "optimized": bool(sys.flags.optimize), "mutations": 6, "seconds": elapsed}))


if __name__ == "__main__":
    main()
