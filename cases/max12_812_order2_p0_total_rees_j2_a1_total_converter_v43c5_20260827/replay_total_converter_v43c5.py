#!/usr/bin/env python3
"""Exact circuit converter from C4 special and G4 generic certificates."""

from __future__ import annotations

import argparse
import copy
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
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_"

C4_CASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_factor_v43c4_20260827"
C4_FREEZE = C4_CASE / "FREEZE.sha256"
C4_FREEZE_SHA256 = "67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6"
C4_SOURCE = C4_CASE / "replay_constructive_circuit_rebased_factor_v43c4.py"
C4_SOURCE_SHA256 = "cd3e17b8b08617fb6d576d36313e8d08ec0d488bc63f375d62d11da321c7d633"
C4_PROOF = C4_CASE / "evidence/r6b/output/a1_104_exact_derivation_dag_rebased_factor.json"
C4_PROOF_SHA256 = "3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862"
C4_RESULT = C4_CASE / "evidence/r6b/output/result.json"
C4_RESULT_SHA256 = "629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c"

G4_CASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827"
G4_FREEZE = G4_CASE / "FREEZE.sha256"
G4_FREEZE_SHA256 = "777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91"
G4_SOURCE = G4_CASE / "rehomogenize_generic_qt_v43g4.py"
G4_SOURCE_SHA256 = "62560313f046b8a7935852bc75e5ba5125c6db5441c19e5f75083a3c0951e902"
G4_CERTIFICATE = G4_CASE / "aws_r6b_rehom_20260827T111531Z/output/generic_total_t_certificate.json"
G4_CERTIFICATE_SHA256 = "e737b9ef129e5022c47100553d3a1725dbd6bc67e2486760e6d3d523db07b740"
G4_RESULT = G4_CASE / "aws_r6b_rehom_20260827T111531Z/output/result.json"
G4_RESULT_SHA256 = "e97ebd6a893e73d8e3751692b56300f0df230a75184f20b05d91282ac455e962"
G4_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-generic-rehom-v43g4-hostile-review-grok-20260827.md"
G4_REVIEW_SHA256 = "8a34756e4b3433f4b4817fb711d923360f188a66fd9ff2975d703375136658f1"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith(TAG_PREFIX)):
        fail("registered V43C5 AWS lane required")
    return tag


def load_module(path: Path, expected: str, name: str):
    actual = digest(path)
    if actual != expected:
        fail(("module pin", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_freeze(path: Path, expected: str) -> None:
    if digest(path) != expected:
        fail(("freeze pin", str(path), digest(path), expected))
    for line in path.read_text().splitlines():
        wanted, relative = line.split(maxsplit=1)
        item = ROOT / relative
        if not item.is_file() or digest(item) != wanted:
            fail(("frozen file", relative,
                  digest(item) if item.is_file() else "MISSING", wanted))


def decode_polynomial(encoded) -> dict:
    result = {}
    for item in encoded:
        monomial = tuple((str(name), int(exponent))
                         for name, exponent in item["monomial"])
        coefficient = Fraction(*item["coefficient"])
        if not coefficient or monomial in result:
            fail(("noncanonical encoded polynomial", item))
        result[monomial] = coefficient
    return result


def specialize_t0(polynomial: dict) -> dict:
    result = {}
    for monomial, coefficient in polynomial.items():
        if dict(monomial).get("t", 0) == 0:
            result[monomial] = coefficient
    return result


def divide_exact_t(polynomial: dict, canonical) -> dict:
    result = {}
    for monomial, coefficient in polynomial.items():
        powers = dict(monomial)
        exponent = powers.get("t", 0)
        if exponent <= 0:
            fail(("not divisible by t", monomial))
        if exponent == 1:
            powers.pop("t")
        else:
            powers["t"] = exponent - 1
        key = canonical(powers)
        value = result.get(key, Fraction(0)) + coefficient
        if value:
            result[key] = value
        else:
            result.pop(key, None)
    return result


def c4_context():
    verify_freeze(C4_FREEZE, C4_FREEZE_SHA256)
    for path, expected in ((C4_PROOF, C4_PROOF_SHA256),
                           (C4_RESULT, C4_RESULT_SHA256)):
        if digest(path) != expected:
            fail(("C4 evidence pin", str(path), digest(path), expected))
    c4 = load_module(C4_SOURCE, C4_SOURCE_SHA256, "frozen_v43c4_converter")
    c1 = c4.load_c1()
    p = c1.load_v42()
    v37 = p.load_v37()
    _, row_items, row_hashes, _ = v37.load_rows()
    rows = {
        item["name"]: {tuple(monomial): coefficient
                       for monomial, coefficient in item["polynomial"].items()}
        for item in row_items
    }
    if len(rows) != 51 or len(row_hashes) != 70:
        fail(("C4 row census", len(rows), len(row_hashes)))
    generators = dict(rows)
    assumptions = {}
    labels = {name: "assume:" + name for name in
              ("e0", "e1", "ee0", "ell1", "rs1", "aa0", "cs1",
               "ee1", "ec3", "rs2", "ez3")}
    for name, label in labels.items():
        generators[label] = p.variable(name)
        assumptions[label] = generators[label]
    a, ell, aa, cs2 = (p.variable(name) for name in
                       ("a1", "ell1", "aa0", "cs2"))
    extra = {
        "assume:e1_minus_4a1ell1": p.add(p.variable("e1"),
                                           p.scale(p.multiply(a, ell), -4)),
        "assume:ee0_plus_4aa0ell1": p.add(p.variable("ee0"),
                                            p.scale(p.multiply(aa, ell), 4)),
        "assume:ec4_minus_a1cs2": p.add(p.variable("ec4"),
                                          p.scale(p.multiply(a, cs2), -1)),
        "assume:a1_minus_6cs2ell1": p.add(a,
                                             p.scale(p.multiply(cs2, ell), -6)),
    }
    generators.update(extra)
    assumptions.update(extra)
    record = json.loads(C4_PROOF.read_text())
    final = c4.replay_record(record, p, rows, generators, set(assumptions))
    if final.target != p.power(a, 104):
        fail("C4 replay target")
    if set(final.terms) - set(rows) or len(final.terms) != 16:
        fail(("C4 final labels", sorted(final.terms)))
    if record["final_certificate"]["terms"] != {
            name: root for name, root in sorted(final.terms.items())}:
        fail("C4 final root commitment")
    return c4, p, rows, row_hashes, record, final


def total_context(p):
    verify_freeze(G4_FREEZE, G4_FREEZE_SHA256)
    for path, expected in ((G4_CERTIFICATE, G4_CERTIFICATE_SHA256),
                           (G4_RESULT, G4_RESULT_SHA256),
                           (G4_REVIEW, G4_REVIEW_SHA256)):
        if digest(path) != expected:
            fail(("G4 evidence pin", str(path), digest(path), expected))
    g4 = load_module(G4_SOURCE, G4_SOURCE_SHA256, "frozen_v43g4_converter")
    v43 = load_module(g4.V43, g4.V43_SHA256, "frozen_v43_total_converter")
    (parser, _, total_items, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = v43.reconstruct_rows()
    if (len(total_items), len(variables), len(frozen_variables), general_only) != (
            59, 66, 65, ["ez9"]):
        fail(("literal total census", len(total_items), len(variables),
              len(frozen_variables), general_only))
    total_rows = {
        item["name"]: g4.ordinary_t_polynomial(item["polynomial"])
        for item in total_items
    }
    if len(total_rows) != 59 or len(total_hashes) != 59:
        fail(("literal total map", len(total_rows), len(total_hashes)))
    generic = json.loads(G4_CERTIFICATE.read_text())
    if (generic.get("identity") != "5*t^6*a1^4=sum_i H_i*Tg_i"
            or generic.get("t_valuation") != 6
            or generic.get("q_t") != 5
            or generic.get("q_at_zero") != 5
            or len(generic.get("multipliers", {})) != 11):
        fail("G4 certificate contract")
    generic_multipliers = {
        name: decode_polynomial(encoded)
        for name, encoded in generic["multipliers"].items()
    }
    direct = {}
    for name, multiplier in generic_multipliers.items():
        if name not in total_rows:
            fail(("generic row name", name))
        direct = p.add(direct, p.multiply(multiplier, total_rows[name]))
    target = p.scale(
        p.multiply(p.power(p.variable("t"), 6),
                   p.power(p.variable("a1"), 4)),
        5,
    )
    p.assert_equal("reviewed G4 direct replay", direct, target)
    return (g4, total_rows, total_hashes, variables, frozen_variables,
            nonzero_general, generic, generic_multipliers)


def row_bridge(p, total_rows: dict, special_rows: dict, special_names: list[str],
               canonical):
    deltas = {}
    t = p.variable("t")
    for name in special_names:
        if name not in total_rows or name not in special_rows:
            fail(("special bridge name", name))
        fibre = specialize_t0(total_rows[name])
        p.assert_equal("literal special fibre:" + name, fibre,
                       special_rows[name])
        difference = p.add(total_rows[name], p.scale(fibre, -1))
        delta = divide_exact_t(difference, canonical)
        p.assert_equal("literal t bridge:" + name,
                       p.add(fibre, p.multiply(t, delta)), total_rows[name])
        deltas[name] = delta
    return deltas


def universal_converter_schema(p, power: int) -> None:
    if power != 6:
        fail(("registered converter power", power))
    x, y, z = (p.variable(name) for name in
               ("__converter_x", "__converter_y", "__converter_z"))
    geometric = {}
    for index in range(power):
        geometric = p.add(
            geometric,
            p.multiply(p.power(x, power - 1 - index), p.power(y, index)),
        )
    left = p.multiply(z, p.power(x, power))
    right = p.multiply(
        z,
        p.add(p.multiply(p.add(x, p.scale(y, -1)), geometric),
              p.power(y, power)),
    )
    p.assert_equal("universal special/generic converter", left, right)


def reconstruct_converter(record: dict, c4, p, c4_record: dict,
                          c4_final, special_rows: dict, total_rows: dict,
                          total_hashes: dict, generic: dict,
                          generic_multipliers: dict, canonical):
    if record.get("format") != "JC2-EXACT-TOTAL-A1-CIRCUIT-CONVERTER-V43C5":
        fail("converter format")
    if record.get("ambient_ring") != "Q[t,X19_total], t maps to rho^2":
        fail("converter ambient ring")
    if record.get("special_exponent") != 104 or record.get("generic_a1_exponent") != 4:
        fail("converter source exponents")
    power = record.get("converter_power")
    if power != generic.get("t_valuation") or power != 6:
        fail(("converter/generic valuation", power, generic.get("t_valuation")))
    if record.get("target_exponent") != 4 + power * 104 or record.get("target_exponent") != 628:
        fail("converter target exponent")
    bridge_sign = Fraction(*record.get("bridge_sign"))
    if bridge_sign != -1:
        fail(("bridge sign", bridge_sign))
    generic_scale = Fraction(*record.get("generic_scale"))
    if generic_scale * generic.get("q_t") != 1:
        fail(("generic rational normalization", generic_scale, generic.get("q_t")))
    if record.get("total_row_sha256") != total_hashes:
        fail("total row hash commitment")

    expressions = c4.ExprStore.from_record(p, record["expression_nodes"])
    original_count = len(c4_record["expression_nodes"])
    if expressions.nodes[:original_count] != c4_record["expression_nodes"]:
        fail("C4 expression prefix")
    special_names = sorted(c4_final.terms)
    deltas = row_bridge(p, total_rows, special_rows, special_names, canonical)

    def existing(operation, expected, label):
        actual = operation()
        if actual != expected:
            fail(("converter root commitment", label, actual, expected))
        return actual

    delta_roots = {}
    h_terms = []
    for name in special_names:
        delta_root = existing(lambda value=deltas[name]: expressions.sparse(value),
                              record["delta_roots"][name], "delta:" + name)
        delta_roots[name] = delta_root
        h_terms.append(existing(
            lambda c=c4_final.terms[name], d=delta_root: expressions.mul(c, d),
            record["h_term_roots"][name], "h-term:" + name,
        ))
    h_sum = expressions.add(*h_terms)
    existing(lambda: h_sum, record["delta_sum_root"], "delta-sum")
    h_root = existing(lambda: expressions.scale(h_sum, bridge_sign),
                      record["h_root"], "H")
    x_root = existing(lambda: expressions.sparse(p.power(p.variable("a1"), 104)),
                      record["x_root"], "x")
    t_root = existing(lambda: expressions.sparse(p.variable("t")),
                      record["t_root"], "t")
    y_root = existing(lambda: expressions.mul(t_root, h_root),
                      record["y_root"], "y")
    geometric_terms = [
        expressions.mul(expressions.power(x_root, power - 1 - index),
                        expressions.power(y_root, index))
        for index in range(power)
    ]
    geometric_root = existing(lambda: expressions.add(*geometric_terms),
                               record["geometric_root"], "geometric")
    a4_root = existing(lambda: expressions.sparse(p.power(p.variable("a1"), 4)),
                       record["a4_root"], "a1^4")
    h_power_root = existing(lambda: expressions.power(h_root, power),
                            record["h_power_root"], "H^6")

    special_fibre_sum = expressions.add(*[
        expressions.mul(c4_final.terms[name], expressions.sparse(special_rows[name]))
        for name in special_names
    ])
    existing(lambda: special_fibre_sum, record["special_fibre_sum_root"],
             "special-fibre-sum")
    total_lift_sum = expressions.add(*[
        expressions.mul(c4_final.terms[name], expressions.sparse(total_rows[name]))
        for name in special_names
    ])
    existing(lambda: total_lift_sum, record["total_lift_sum_root"],
             "total-lift-sum")
    bridge_expanded = expressions.add(
        special_fibre_sum, expressions.mul(t_root, h_sum)
    )
    existing(lambda: bridge_expanded, record["bridge_expanded_root"],
             "bridge-expanded")

    expected_terms = {}
    for name in special_names:
        expected_terms[name] = expressions.mul(
            c4_final.terms[name], geometric_root, a4_root
        )
    for name, multiplier in sorted(generic_multipliers.items()):
        generic_root = existing(lambda value=multiplier: expressions.sparse(value),
                                record["generic_multiplier_roots"][name],
                                "generic:" + name)
        contribution = expressions.mul(
            h_power_root, expressions.scale(generic_root, generic_scale)
        )
        expected_terms[name] = expressions.add(
            expected_terms.get(name, expressions.zero), contribution
        )
    if expected_terms != record.get("final_multiplier_roots"):
        fail("final multiplier root commitment")
    if set(expected_terms) - set(total_rows) or not expected_terms:
        fail("final total row labels")
    universal_converter_schema(p, power)
    generic_normalized_sum = expressions.add(*[
        expressions.mul(expressions.scale(
            record["generic_multiplier_roots"][name], generic_scale),
            expressions.sparse(total_rows[name]))
        for name in sorted(generic_multipliers)
    ])
    existing(lambda: generic_normalized_sum,
             record["generic_normalized_sum_root"], "generic-normalized-sum")
    final_sum = expressions.add(*[
        expressions.mul(root, expressions.sparse(total_rows[name]))
        for name, root in sorted(expected_terms.items())
    ])
    existing(lambda: final_sum, record["final_sum_root"], "final-sum")
    x_minus_y = expressions.add(x_root, expressions.scale(y_root, -1))
    schema_rhs = expressions.mul(
        a4_root,
        expressions.add(expressions.mul(x_minus_y, geometric_root),
                        expressions.power(y_root, power)),
    )
    existing(lambda: schema_rhs, record["schema_rhs_root"], "schema-rhs")
    target_root = expressions.mul(a4_root, expressions.power(x_root, power))
    existing(lambda: target_root, record["target_root"], "target-root")
    target = decode_polynomial(record["target"])
    p.assert_equal("converter target", target,
                   p.power(p.variable("a1"), record["target_exponent"]))
    return {
        "expression_node_count": len(expressions.nodes),
        "original_c4_expression_node_count": original_count,
        "final_rows": sorted(expected_terms),
        "final_row_count": len(expected_terms),
        "h_root": h_root,
        "geometric_root": geometric_root,
        "h_power_root": h_power_root,
    }


def build_record(tag: str, c4, p, special_rows: dict, c4_record: dict,
                 c4_final, total_rows: dict, total_hashes: dict,
                 variables: list, frozen_variables: list,
                 nonzero_general, generic: dict, generic_multipliers: dict,
                 canonical):
    expressions = c4.ExprStore.from_record(p, c4_record["expression_nodes"])
    expressions.frozen = False
    special_names = sorted(c4_final.terms)
    deltas = row_bridge(p, total_rows, special_rows, special_names, canonical)
    delta_roots = {name: expressions.sparse(deltas[name]) for name in special_names}
    h_term_roots = {
        name: expressions.mul(c4_final.terms[name], delta_roots[name])
        for name in special_names
    }
    bridge_sign = Fraction(-1)
    delta_sum_root = expressions.add(*h_term_roots.values())
    h_root = expressions.scale(delta_sum_root, bridge_sign)
    x_root = expressions.sparse(p.power(p.variable("a1"), 104))
    t_root = expressions.sparse(p.variable("t"))
    y_root = expressions.mul(t_root, h_root)
    power = 6
    geometric_root = expressions.add(*[
        expressions.mul(expressions.power(x_root, power - 1 - index),
                        expressions.power(y_root, index))
        for index in range(power)
    ])
    a4_root = expressions.sparse(p.power(p.variable("a1"), 4))
    h_power_root = expressions.power(h_root, power)
    generic_scale = Fraction(1, 5)
    generic_roots = {
        name: expressions.sparse(multiplier)
        for name, multiplier in sorted(generic_multipliers.items())
    }
    final_terms = {
        name: expressions.mul(c4_final.terms[name], geometric_root, a4_root)
        for name in special_names
    }
    for name, root in generic_roots.items():
        contribution = expressions.mul(
            h_power_root, expressions.scale(root, generic_scale)
        )
        final_terms[name] = expressions.add(
            final_terms.get(name, expressions.zero), contribution
        )
    special_fibre_sum_root = expressions.add(*[
        expressions.mul(c4_final.terms[name], expressions.sparse(special_rows[name]))
        for name in special_names
    ])
    total_lift_sum_root = expressions.add(*[
        expressions.mul(c4_final.terms[name], expressions.sparse(total_rows[name]))
        for name in special_names
    ])
    bridge_expanded_root = expressions.add(
        special_fibre_sum_root, expressions.mul(t_root, delta_sum_root)
    )
    generic_normalized_sum_root = expressions.add(*[
        expressions.mul(expressions.scale(generic_roots[name], generic_scale),
                        expressions.sparse(total_rows[name]))
        for name in sorted(generic_roots)
    ])
    final_sum_root = expressions.add(*[
        expressions.mul(root, expressions.sparse(total_rows[name]))
        for name, root in sorted(final_terms.items())
    ])
    x_minus_y_root = expressions.add(x_root, expressions.scale(y_root, -1))
    schema_rhs_root = expressions.mul(
        a4_root,
        expressions.add(expressions.mul(x_minus_y_root, geometric_root),
                        expressions.power(y_root, power)),
    )
    target_root = expressions.mul(a4_root, expressions.power(x_root, power))
    record = {
        "format": "JC2-EXACT-TOTAL-A1-CIRCUIT-CONVERTER-V43C5",
        "ambient_ring": "Q[t,X19_total], t maps to rho^2",
        "rho_map": "Q[t,X19_total] -> Q[rho,X19_total], t |-> rho^2",
        "registered_aws_lane": tag,
        "special_exponent": 104,
        "generic_a1_exponent": 4,
        "converter_power": power,
        "target_exponent": 628,
        "bridge_sign": [bridge_sign.numerator, bridge_sign.denominator],
        "generic_scale": [generic_scale.numerator, generic_scale.denominator],
        "special_rows": special_names,
        "generic_rows": sorted(generic_multipliers),
        "literal_total_row_count": len(total_rows),
        "literal_positive_variable_count": len(variables),
        "rho0_positive_variable_count": len(frozen_variables),
        "general_only_nonzero_rows": nonzero_general,
        "total_row_sha256": total_hashes,
        "c4_proof_sha256": C4_PROOF_SHA256,
        "g4_certificate_sha256": G4_CERTIFICATE_SHA256,
        "expression_nodes": expressions.nodes,
        "delta_roots": delta_roots,
        "h_term_roots": h_term_roots,
        "delta_sum_root": delta_sum_root,
        "h_root": h_root,
        "x_root": x_root,
        "t_root": t_root,
        "y_root": y_root,
        "geometric_root": geometric_root,
        "a4_root": a4_root,
        "h_power_root": h_power_root,
        "generic_multiplier_roots": generic_roots,
        "final_multiplier_roots": final_terms,
        "special_fibre_sum_root": special_fibre_sum_root,
        "total_lift_sum_root": total_lift_sum_root,
        "bridge_expanded_root": bridge_expanded_root,
        "generic_normalized_sum_root": generic_normalized_sum_root,
        "final_sum_root": final_sum_root,
        "schema_rhs_root": schema_rhs_root,
        "target_root": target_root,
        "derivation_steps": [
            "C4 replay: special_fibre_sum_root = x_root = a1^104",
            "row bridges: total_lift_sum_root = bridge_expanded_root = x_root-y_root",
            "G4 replay and 1/5 normalization: generic_normalized_sum_root = t^6*a1^4",
            "definition: y_root=t*H, so H^6*generic_normalized_sum_root=a1^4*y^6",
            "final_sum_root = a1^4*(x-y)*Phi + a1^4*y^6",
            "sixth-power schema: schema_rhs_root = target_root = a1^628",
        ],
        "target": c4.encoded_certificate(
            p, c4.Certificate(p.power(p.variable("a1"), 628), {})
        )["target"],
    }
    return record


def mutation_rejected(record, mutate, replay) -> bool:
    changed = copy.deepcopy(record)
    mutate(changed)
    try:
        replay(changed)
    except Exception:
        return True
    return False


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    c4, p, special_rows, row_hashes, c4_record, c4_final = c4_context()
    (g4, total_rows, total_hashes, variables, frozen_variables,
     nonzero_general, generic, generic_multipliers) = total_context(p)
    record = build_record(
        tag, c4, p, special_rows, c4_record, c4_final, total_rows,
        total_hashes, variables, frozen_variables, nonzero_general, generic,
        generic_multipliers, g4.canonical,
    )
    proof_path = output / "total_a1_628_circuit_certificate.json"
    proof_path.write_text(json.dumps(record, sort_keys=True,
                                     separators=(",", ":")) + "\n")
    loaded = json.loads(proof_path.read_text())

    def replay(candidate):
        return reconstruct_converter(
            candidate, c4, p, c4_record, c4_final, special_rows, total_rows,
            total_hashes, generic, generic_multipliers, g4.canonical,
        )

    replay_stats = replay(loaded)
    mutations = {
        "wrong_bridge_sign": mutation_rejected(
            loaded, lambda item: item.__setitem__("bridge_sign", [1, 1]), replay),
        "wrong_generic_scale": mutation_rejected(
            loaded, lambda item: item.__setitem__("generic_scale", [1, 4]), replay),
        "wrong_converter_power": mutation_rejected(
            loaded, lambda item: item.__setitem__("converter_power", 5), replay),
        "deleted_Tg19_7_multiplier": mutation_rejected(
            loaded, lambda item: item["final_multiplier_roots"].pop("Tg19_7"), replay),
        "wrong_target_exponent": mutation_rejected(
            loaded, lambda item: item.__setitem__("target_exponent", 627), replay),
    }
    if not all(mutations.values()):
        fail(("serialized mutation accepted", mutations))

    corrupted_generic = {name: dict(row) for name, row in total_rows.items()}
    generic_key = sorted(corrupted_generic["Tg15_7"])[0]
    corrupted_generic["Tg15_7"][generic_key] += 1
    generic_residual = {}
    for name, multiplier in generic_multipliers.items():
        generic_residual = p.add(
            generic_residual,
            p.multiply(multiplier, corrupted_generic[name]),
        )
    generic_target = p.scale(
        p.multiply(p.power(p.variable("t"), 6),
                   p.power(p.variable("a1"), 4)), 5)
    if generic_residual == generic_target:
        fail("literal Tg15_7 corruption accepted")

    corrupted_special = dict(total_rows["Tg19_7"])
    fibre_keys = [monomial for monomial in sorted(corrupted_special)
                  if dict(monomial).get("t", 0) == 0]
    if not fibre_keys:
        fail("Tg19_7 has no special-fibre mutation target")
    corrupted_special[fibre_keys[0]] += 1
    if specialize_t0(corrupted_special) == special_rows["Tg19_7"]:
        fail("literal Tg19_7 special corruption accepted")
    mutations["literal_Tg15_7_generic_row"] = True
    mutations["literal_Tg19_7_special_fibre"] = True

    result = {
        "status": "PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5",
        "scope": "frozen literal total raw ordered-a1 rows through grade 19",
        "conclusion": "a1^628 belongs to the literal total ideal over Q[t], hence after t->rho^2 over Q[rho]",
        "proof_sha256": digest(proof_path),
        "proof_bytes": proof_path.stat().st_size,
        **replay_stats,
        "special_row_count": len(c4_final.terms),
        "generic_row_count": len(generic_multipliers),
        "literal_total_row_count": len(total_rows),
        "literal_positive_variable_count": len(variables),
        "rho0_positive_variable_count": len(frozen_variables),
        "mutations": mutations,
        "c4_freeze_sha256": C4_FREEZE_SHA256,
        "c4_proof_sha256": C4_PROOF_SHA256,
        "g4_freeze_sha256": G4_FREEZE_SHA256,
        "g4_certificate_sha256": G4_CERTIFICATE_SHA256,
        "g4_review_sha256": G4_REVIEW_SHA256,
        "preregistration_sha256": digest(PREREG),
        "producer_sha256": digest(Path(__file__)),
        "firewalls": [
            "ordinary polynomial arithmetic only; no t localization",
            "t maps exactly to rho^2; the resulting pure target has W=0",
            "no normalized K00 or terminal-receiver implication without a chain map",
        ],
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5")
    print("PROOF_SHA256=" + digest(proof_path))
    print("RESULT_SHA256=" + digest(result_path))
    print("EXPRESSION_NODES=" + str(replay_stats["expression_node_count"]))
    print("FINAL_ROWS=" + str(replay_stats["final_row_count"]))


if __name__ == "__main__":
    main()
