#!/usr/bin/env python3
"""Compile exact receiver deduplication and bounded modular portfolio inputs.

This consumes the frozen general reduction.  It proves every discarded G14
or G15 receiver row is an exact nonzero rational scalar multiple of its kept
representative before emitting smaller, ideal-equivalent systems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
REDUCTION = HERE / "input/REDUCTION.json"
SYSTEM = HERE / "input/ORIGIN_Q15_SYSTEM.json"
GENERATED = HERE / "input/GENERATED.sha256.json"
PINS = {
    REDUCTION: "b3f1196f9d69fd060c8acfd21d867c6da1b5447af984bbce6013c5c9a4ec0ba6",
    SYSTEM: "16a1d0ec3206a0c0a870c7a1395e4bb36e6788c847d30e6be3b445e453a05bd0",
    GENERATED: "0751cb1bad59ee7ac70326ce628121b8ee4f8068e63412e9727e1be3d85586ed",
}
PRIMES = (65521, 65519, 65497)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def decode(terms):
    return {tuple(monomial): Fraction(coefficient) for monomial, coefficient in terms}


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items()) if coefficient]


def verify_record(item):
    assert hashlib.sha256(compact(item["terms"])).hexdigest() == item["sha256"]
    assert decode(item["terms"])


def normalized_key(item):
    poly = decode(item["terms"])
    first = min(poly)
    lead = poly[first]
    return tuple((monomial, coefficient / lead)
                 for monomial, coefficient in sorted(poly.items()))


def scalar_multiple(left, right):
    a, b = decode(left["terms"]), decode(right["terms"])
    assert set(a) == set(b)
    first = min(a)
    scalar = a[first] / b[first]
    assert scalar
    assert all(a[monomial] == scalar * b[monomial] for monomial in a)
    return scalar


def deduplicate(items, family):
    classes = {}
    order = []
    for index, item in enumerate(items):
        verify_record(item)
        key = normalized_key(item)
        if key not in classes:
            classes[key] = {"representative": item, "representative_index": index, "members": []}
            order.append(key)
        entry = classes[key]
        scalar = scalar_multiple(item, entry["representative"])
        entry["members"].append({
            "source_index": index,
            "x_degree": item.get("x_degree"),
            "source_kind": item.get("source_kind"),
            "source_sha256": item["sha256"],
            "scalar_from_representative": str(scalar),
        })
    representatives = []
    certificate = []
    for class_index, key in enumerate(order):
        entry = classes[key]
        record = dict(entry["representative"])
        record["constraint_id"] = f"{family}_class_{class_index}"
        representatives.append(record)
        certificate.append({
            "constraint_id": record["constraint_id"],
            "representative_index": entry["representative_index"],
            "representative_sha256": record["sha256"],
            "members": entry["members"],
        })
    return representatives, certificate


def support(items):
    return sorted({name for item in items for monomial, _ in item["terms"] for name in monomial})


def expression(item, modulus):
    pieces = []
    for monomial, coefficient_text in item["terms"]:
        coefficient = Fraction(coefficient_text)
        if modulus:
            coefficient = (coefficient.numerator % modulus) * pow(
                coefficient.denominator % modulus, -1, modulus
            ) % modulus
            if not coefficient:
                continue
            atom = "*".join(monomial) if monomial else "1"
            pieces.append(f"{coefficient}*{atom}")
        else:
            atom = "*".join(monomial) if monomial else "1"
            pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces) if pieces else "0"


def endpoint_residual(target):
    poly = decode(target["terms"])
    poly[()] = poly.get((), Fraction(0)) - 1
    if not poly[()]:
        del poly[()]
    return {"constraint_id": "endpoint_equals_1", "terms": encode(poly)}


def variable_profile(items, target, profile):
    names = support(items + [target])
    target_names = set(support([target]))
    core = [name for name in names
            if name.startswith("Q_") or name.startswith("c") or name == "invc2"]
    endpoint = [name for name in names if name in target_names and name not in set(core)]
    receiver = [name for name in names if name not in set(core) | set(endpoint)]
    if profile == "core_endpoint_receiver":
        blocks = [core, endpoint, receiver]
    elif profile == "receiver_endpoint_core":
        blocks = [receiver, endpoint, core]
    elif profile == "endpoint_core_receiver":
        blocks = [endpoint, core, receiver]
    elif profile == "reverse_lexical":
        blocks = [list(reversed(names))]
    elif profile == "lexical":
        blocks = [names]
    else:
        raise AssertionError(profile)
    blocks = [block for block in blocks if block]
    variables = [name for block in blocks for name in block]
    assert len(variables) == len(set(variables)) == len(names)
    return variables, [len(block) for block in blocks]


def singular_script(items, target, modulus, profile, algorithm, block_order):
    variables, block_sizes = variable_profile(items, target, profile)
    if block_order and len(block_sizes) > 1:
        ordering = "(" + ",".join(f"dp({size})" for size in block_sizes) + ")"
    else:
        ordering = "lp" if algorithm == "std" and profile == "lexical" else "dp"
    generators = [expression(item, modulus) for item in items]
    lines = [
        f"ring portfolio={modulus},({','.join(variables)}),{ordering};",
        "option(redSB);",
        "ideal I=", ",\n".join(generators) + ";",
        f'print("PROFILE={profile} ALGORITHM={algorithm} VARIABLES="+string(nvars(basering))+" GENERATORS="+string(size(I)));',
        "int start_time=timer;",
        f"ideal J={algorithm}(I);",
        "int elapsed=timer-start_time;",
        'print("SECONDS="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        f"poly target={expression(target, modulus)};",
        "poly target_nf=reduce(target,J);",
        'print("TARGET_NF_ZERO="+string(target_nf==0));',
        'print("TARGET_NF_TERMS="+string(size(target_nf)));',
        "quit;", "",
    ]
    return "\n".join(lines)


def singular_parse_script(items, target, modulus, profile, algorithm, block_order):
    text = singular_script(items, target, modulus, profile, algorithm, block_order)
    return text.split("int start_time=timer;", 1)[0] + 'print("PARSE_PASS");\nquit;\n'


def msolve_input(items, target, modulus, profile):
    variables, _ = variable_profile(items, target, profile)
    endpoint = endpoint_residual(target)
    expressions = [expression(item, modulus) for item in items + [endpoint]]
    return f"{', '.join(variables)}\n{modulus}\n" + ",\n".join(expressions) + "\n"


VARIANTS = {
    "g15_core_block_std": {
        "subset": "g15", "profile": "core_endpoint_receiver",
        "algorithm": "std", "block_order": True,
    },
    "g15_receiver_block_slimgb": {
        "subset": "g15", "profile": "receiver_endpoint_core",
        "algorithm": "slimgb", "block_order": True,
    },
    "g13_g15_endpoint_block_std": {
        "subset": "g13_g15", "profile": "endpoint_core_receiver",
        "algorithm": "std", "block_order": True,
    },
    "g14_core_block_slimgb": {
        "subset": "g14", "profile": "core_endpoint_receiver",
        "algorithm": "slimgb", "block_order": True,
    },
    "full_core_block_slimgb": {
        "subset": "full", "profile": "core_endpoint_receiver",
        "algorithm": "slimgb", "block_order": True,
    },
    "full_reverse_dp_slimgb": {
        "subset": "full", "profile": "reverse_lexical",
        "algorithm": "slimgb", "block_order": False,
    },
}


def compile_portfolio(output_dir: Path):
    for path, digest in PINS.items():
        assert sha256(path) == digest, (path, sha256(path), digest)
    generated = json.loads(GENERATED.read_text())
    assert generated["REDUCTION.json"] == PINS[REDUCTION]
    reduction = json.loads(REDUCTION.read_text())
    assert reduction["schema"] == "GGV-8_28-UPPER-LAMBDA0-ORIGIN-Q5-Q15-REDUCED-v1"
    assert reduction["source_system_sha256"] == PINS[SYSTEM]
    assert len(reduction["q_compatibility"]) == 5
    assert {weight: len(items) for weight, items in reduction["G8_G15_raw_constraints"].items()} == {
        "8": 0, "9": 0, "10": 0, "11": 0, "12": 0,
        "13": 1, "14": 89, "15": 73,
    }
    q, q_cert = deduplicate(reduction["q_compatibility"], "q")
    g13, g13_cert = deduplicate(reduction["G8_G15_raw_constraints"]["13"], "G13")
    g14, g14_cert = deduplicate(reduction["G8_G15_raw_constraints"]["14"], "G14")
    g15, g15_cert = deduplicate(reduction["G8_G15_raw_constraints"]["15"], "G15")
    assert (len(q), len(g13), len(g14), len(g15)) == (5, 1, 5, 5)
    open_condition = dict(reduction["open_condition"])
    open_condition["constraint_id"] = "c2_open"
    verify_record(open_condition)
    target = dict(reduction["endpoint_value"])
    target["constraint_id"] = "endpoint_value"
    verify_record(target)
    subsets = {
        "g15": q + g15 + [open_condition],
        "g13_g15": q + g13 + g15 + [open_condition],
        "g14": q + g13 + g14 + [open_condition],
        "full": q + g13 + g14 + g15 + [open_condition],
    }
    dedup = {
        "schema": "GGV-8_28-ORIGIN-Q15-EXACT-RECEIVER-DEDUP-v1",
        "source_reduction_sha256": PINS[REDUCTION],
        "source_system_sha256": PINS[SYSTEM],
        "original_counts": {"q": 5, "G13": 1, "G14": 89, "G15": 73, "open": 1},
        "representative_counts": {"q": len(q), "G13": len(g13), "G14": len(g14),
                                  "G15": len(g15), "open": 1, "full": len(subsets["full"])},
        "ideal_equality_method": "exact nonzero rational scalar normalization within each named receiver family",
        "certificates": {"q": q_cert, "G13": g13_cert, "G14": g14_cert, "G15": g15_cert},
        "subsets": subsets,
        "endpoint_value": target,
        "scope": {
            "membership_in_any_subset_implies_membership_in_full_base": True,
            "nonmembership_or_timeout_in_a_subset_does_not_classify": True,
            "G15_only_remains_diagnostic_unless_a_membership_certificate_is_replayed": True,
        },
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {"DEDUP.json": pretty(dedup)}
    for name, spec in VARIANTS.items():
        items = subsets[spec["subset"]]
        for prime in PRIMES:
            payloads[f"{name}_p{prime}.sing"] = singular_script(
                items, target, prime, spec["profile"], spec["algorithm"], spec["block_order"]
            ).encode()
            payloads[f"{name}_p{prime}_parse.sing"] = singular_parse_script(
                items, target, prime, spec["profile"], spec["algorithm"], spec["block_order"]
            ).encode()
    for subset, profile in (("g15", "core_endpoint_receiver"),
                            ("full", "core_endpoint_receiver")):
        for prime in PRIMES:
            payloads[f"msolve_{subset}_endpoint_p{prime}.in"] = msolve_input(
                subsets[subset], target, prime, profile
            ).encode()
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(pretty(manifest))
    summary = {
        "status": "PORTFOLIO_COMPILE_PASS",
        "source_reduction_sha256": PINS[REDUCTION],
        "dedup_sha256": manifest["DEDUP.json"],
        "representative_counts": dedup["representative_counts"],
        "variants": VARIANTS,
        "artifact_count": len(manifest),
    }
    print(json.dumps(summary, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    compile_portfolio(args.output_dir)


if __name__ == "__main__":
    main()
