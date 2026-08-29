#!/usr/bin/env python3
"""Exact rebased arithmetic-circuit compilation of the a1^104 proof tree."""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
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
C1 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_20260827/replay_constructive_cascade_v43c1.py"
C1_SHA256 = "af590ff872552944528dda41497329e1b1534cc211290d622034defd70bac2ca"
INVALIDATION = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION.md"
INVALIDATION_SHA256 = "dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89"
INVALIDATION_FREEZE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION_R1_FREEZE.sha256"
INVALIDATION_FREEZE_SHA256 = "8c3f2ecab6b16ee9c6e3c338f9f88883a33e20baf2cf7aabe69c0bdfca9bd787"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3_"


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
        fail("registered V43C2 AWS lane required")
    return tag


def load_c1():
    if digest(C1) != C1_SHA256:
        fail(("V43C1 source pin", digest(C1), C1_SHA256))
    spec = importlib.util.spec_from_file_location("frozen_v43c1", C1)
    if spec is None or spec.loader is None:
        fail("V43C1 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def decode_polynomial(encoded) -> dict:
    answer = {}
    for item in encoded:
        monomial = tuple((str(name), int(exponent))
                         for name, exponent in item["monomial"])
        coefficient = Fraction(*item["coefficient"])
        if not coefficient or monomial in answer:
            fail(("noncanonical encoded polynomial", item))
        answer[monomial] = coefficient
    return answer


def fraction_record(value) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


class ExprStore:
    """Hash-consed polynomial arithmetic DAG.  Nodes never denote fractions."""

    def __init__(self) -> None:
        self.nodes: list[dict] = []
        self.keys: dict[str, int] = {}
        self.frozen = False
        self.zero = self.sparse({})
        self.one = None

    @staticmethod
    def _key(node: dict) -> str:
        return json.dumps(node, sort_keys=True, separators=(",", ":"))

    def _intern(self, node: dict) -> int:
        key = self._key(node)
        prior = self.keys.get(key)
        if prior is not None:
            return prior
        if self.frozen:
            fail(("verifier requested missing expression node", node))
        index = len(self.nodes)
        self.nodes.append(node)
        self.keys[key] = index
        return index

    def sparse(self, polynomial: dict) -> int:
        for monomial in polynomial:
            if any(exponent < 0 for _, exponent in monomial):
                fail(("negative exponent in circuit leaf", monomial))
        encoded = self.p.encoded_polynomial(polynomial) if hasattr(self, "p") else None
        if encoded is None:
            # Bootstrap only for the zero leaf; p is installed immediately.
            if polynomial:
                fail("ExprStore polynomial backend not installed")
            encoded = []
        return self._intern({"op": "Sparse", "polynomial": encoded})

    def install_backend(self, p) -> None:
        self.p = p
        self.one = self.sparse(p.const(1))

    def add(self, *arguments: int) -> int:
        args = []
        for argument in arguments:
            if argument == self.zero:
                continue
            node = self.nodes[argument]
            if node["op"] == "Add":
                args.extend(node["args"])
            else:
                args.append(argument)
        if not args:
            return self.zero
        if len(args) == 1:
            return args[0]
        return self._intern({"op": "Add", "args": sorted(args)})

    def mul(self, *arguments: int) -> int:
        args = []
        for argument in arguments:
            if argument == self.zero:
                return self.zero
            if argument == self.one:
                continue
            node = self.nodes[argument]
            if node["op"] == "Mul":
                args.extend(node["args"])
            else:
                args.append(argument)
        if not args:
            return self.one
        if len(args) == 1:
            return args[0]
        return self._intern({"op": "Mul", "args": sorted(args)})

    def scale(self, argument: int, scalar) -> int:
        scalar = Fraction(scalar)
        if not scalar:
            return self.zero
        if scalar == 1:
            return argument
        node = self.nodes[argument]
        if node["op"] == "Scale":
            prior = Fraction(*node["scalar"])
            return self.scale(node["arg"], scalar * prior)
        return self._intern({"op": "Scale", "arg": argument,
                             "scalar": fraction_record(scalar)})

    def power(self, argument: int, exponent: int) -> int:
        if not isinstance(exponent, int) or exponent < 0:
            fail(("circuit exponent", exponent))
        if exponent == 0:
            return self.one
        if exponent == 1 or argument in (self.zero, self.one):
            return argument
        return self._intern({"op": "Pow", "arg": argument,
                             "exponent": exponent})

    def expand_exact(self, root: int, term_cap: int = 1_000_000):
        """Expand one named circuit exactly, with a fail-closed term cap."""
        # Deliberately do not retain all intermediate sparse polynomials.
        # The zero checks are small DAGs but some internal products are large;
        # retaining every descendant simultaneously is unnecessary and caused
        # the separately frozen v3 producer to reach its 14-GiB resource gate.
        # Shared descendants may be recomputed.  This changes only memory/time,
        # never the exact Q-polynomial denoted by the circuit.
        visited: set[int] = set()
        evaluated_node_calls = 0
        peak = 0

        def checked(polynomial: dict) -> dict:
            nonlocal peak
            peak = max(peak, len(polynomial))
            if len(polynomial) > term_cap:
                fail(("PruneZeroTerms term cap", root, len(polynomial), term_cap))
            return polynomial

        def visit(index: int) -> dict:
            nonlocal evaluated_node_calls
            evaluated_node_calls += 1
            visited.add(index)
            node = self.nodes[index]
            op = node["op"]
            if op == "Sparse":
                answer = decode_polynomial(node["polynomial"])
            elif op == "Add":
                answer = {}
                for argument in node["args"]:
                    answer = checked(self.p.add(answer, visit(argument)))
            elif op == "Mul":
                answer = self.p.const(1)
                for argument in node["args"]:
                    if not answer:
                        break
                    answer = checked(self.p.multiply(answer, visit(argument)))
            elif op == "Scale":
                answer = self.p.scale(visit(node["arg"]), Fraction(*node["scalar"]))
            elif op == "Pow":
                base = visit(node["arg"])
                answer = self.p.const(1)
                for _ in range(node["exponent"]):
                    answer = checked(self.p.multiply(answer, base))
            else:
                fail(("expand unknown node", index, op))
            answer = checked(answer)
            return answer

        polynomial = visit(root)
        return polynomial, {"root": root, "visited_nodes": len(visited),
                            "evaluated_node_calls": evaluated_node_calls,
                            "peak_sparse_terms": peak, "term_cap": term_cap,
                            "expanded_sha256": self.p.polynomial_hash(polynomial),
                            "expanded_term_count": len(polynomial)}

    @classmethod
    def from_record(cls, p, nodes: list[dict]):
        store = cls()
        store.install_backend(p)
        # The bootstrap creates canonical zero and one at indices 0 and 1.
        if len(nodes) < 2:
            fail("truncated expression table")
        for index, node in enumerate(nodes):
            if index < len(store.nodes):
                if store.nodes[index] != node:
                    fail(("bootstrap expression node", index))
                continue
            op = node.get("op")
            if op == "Sparse":
                value = store.sparse(decode_polynomial(node.get("polynomial")))
            elif op == "Add":
                value = store.add(*node.get("args", []))
            elif op == "Mul":
                value = store.mul(*node.get("args", []))
            elif op == "Scale":
                value = store.scale(node.get("arg"), Fraction(*node.get("scalar")))
            elif op == "Pow":
                value = store.power(node.get("arg"), node.get("exponent"))
            else:
                fail(("unknown expression node", index, op))
            if value != index or store.nodes[index] != node:
                fail(("noncanonical expression node", index, value))
        store.frozen = True
        return store


@dataclass
class Certificate:
    target: dict
    terms: dict[str, int]


def encoded_certificate(p, certificate: Certificate) -> dict:
    return {
        "target": p.encoded_polynomial(certificate.target),
        "terms": {name: value for name, value in sorted(certificate.terms.items())},
    }


class Kernel:
    """Exact certificate-rule kernel; final exactness follows inductively."""

    def __init__(self, p, rows: dict[str, dict], generators: dict[str, dict],
                 assumptions: set[str], expressions: ExprStore) -> None:
        self.p = p
        self.rows = rows
        self.generators = generators
        self.assumptions = assumptions
        self.e = expressions

    def add_term(self, terms: dict[str, int], label: str, value: int) -> None:
        value = self.e.add(terms.get(label, self.e.zero), value)
        if value == self.e.zero:
            terms.pop(label, None)
        else:
            terms[label] = value

    def row(self, name: str, specs: list[tuple[str, dict, str]]) -> Certificate:
        if name not in self.rows:
            fail(("row leaf", name))
        target = self.rows[name]
        terms = {name: self.e.one}
        for variable, value, assumption in specs:
            expected = self.p.add(self.p.variable(variable), self.p.scale(value, -1))
            if self.generators.get(assumption) != expected:
                fail(("row specialization assumption", name, variable, assumption))
            quotient = self.p.divided_difference(target, variable, value)
            specialized = self.p.substitute(target, {variable: value})
            reconstructed = self.p.add(specialized,
                                       self.p.multiply(expected, quotient))
            self.p.assert_equal("row divided difference", reconstructed, target)
            self.add_term(terms, assumption,
                          self.e.scale(self.e.sparse(quotient), -1))
            target = specialized
        return Certificate(target, terms)

    def add(self, certificates: list[Certificate]) -> Certificate:
        target = {}
        terms: dict[str, int] = {}
        for certificate in certificates:
            target = self.p.add(target, certificate.target)
            for name, value in certificate.terms.items():
                self.add_term(terms, name, value)
        return Certificate(target, terms)

    def scale(self, certificate: Certificate, scalar) -> Certificate:
        return Certificate(
            self.p.scale(certificate.target, scalar),
            {name: self.e.scale(value, scalar)
             for name, value in certificate.terms.items()
             if self.e.scale(value, scalar) != self.e.zero},
        )

    def multiply(self, certificate: Certificate, polynomial: dict) -> Certificate:
        factor = self.e.sparse(polynomial)
        return Certificate(
            self.p.multiply(certificate.target, polynomial),
            {name: self.e.mul(value, factor)
             for name, value in certificate.terms.items()
             if self.e.mul(value, factor) != self.e.zero},
        )

    def rebase_assumptions(self, certificate: Certificate,
                           old_e1: str, new_g: str,
                           old_ee0: str, new_q0: str,
                           ell_label: str,
                           e1_ell_scalar, ee0_ell_scalar) -> Certificate:
        """Change the inherited (e1,ee0,ell1) basis to (G,Q0,ell1)."""
        required = (old_e1, old_ee0, ell_label)
        if any(label not in certificate.terms for label in required):
            fail(("rebase missing inherited label", required,
                  sorted(certificate.terms)))
        if new_g in certificate.terms or new_q0 in certificate.terms:
            fail(("rebase new label already present", new_g, new_q0))
        e1_ell_scalar = Fraction(e1_ell_scalar)
        ee0_ell_scalar = Fraction(ee0_ell_scalar)
        a = self.p.variable("a1")
        aa = self.p.variable("aa0")
        ell = self.p.variable("ell1")
        self.p.assert_equal(
            "rebase e1 identity",
            self.generators[old_e1],
            self.p.add(self.generators[new_g],
                       self.p.scale(self.p.multiply(a, ell), e1_ell_scalar)),
        )
        self.p.assert_equal(
            "rebase ee0 identity",
            self.generators[old_ee0],
            self.p.add(self.generators[new_q0],
                       self.p.scale(self.p.multiply(aa, ell), ee0_ell_scalar)),
        )
        terms = dict(certificate.terms)
        c_e1 = terms.pop(old_e1)
        c_ee0 = terms.pop(old_ee0)
        self.add_term(terms, new_g, c_e1)
        self.add_term(terms, new_q0, c_ee0)
        self.add_term(
            terms, ell_label,
            self.e.mul(self.e.scale(c_e1, e1_ell_scalar), self.e.sparse(a)),
        )
        self.add_term(
            terms, ell_label,
            self.e.mul(self.e.scale(c_ee0, ee0_ell_scalar), self.e.sparse(aa)),
        )
        if old_e1 in terms or old_ee0 in terms:
            fail("rebase retained old labels")
        return Certificate(certificate.target, terms)

    def clear_power(self, certificate: Certificate, assumption: str, exponent: int,
                    relation: Certificate, factor: dict) -> Certificate:
        if exponent <= 0 or assumption not in certificate.terms:
            fail(("clear_power contract", assumption, exponent))
        f = self.generators[assumption]
        self.p.assert_equal("clear_power relation", relation.target,
                            self.p.multiply(factor, self.p.power(f, exponent)))
        if assumption in relation.terms:
            fail(("clear_power relation retains assumption", assumption))
        multiplier = certificate.terms[assumption]
        bf = self.e.mul(multiplier, self.e.sparse(f))
        geometric = self.e.zero
        for index in range(exponent):
            geometric = self.e.add(
                geometric,
                self.e.mul(
                    self.e.sparse(self.p.power(certificate.target,
                                               exponent - 1 - index)),
                    self.e.power(bf, index),
                ),
            )
        terms: dict[str, int] = {}
        common = self.e.mul(self.e.sparse(factor), geometric)
        for name, value in certificate.terms.items():
            if name != assumption:
                self.add_term(terms, name, self.e.mul(common, value))
        replacement = self.e.power(multiplier, exponent)
        for name, value in relation.terms.items():
            self.add_term(terms, name, self.e.mul(replacement, value))
        return Certificate(
            self.p.multiply(factor, self.p.power(certificate.target, exponent)),
            terms,
        )

    def combine(self, left: Certificate, left_assumption: str,
                right: Certificate, right_assumption: str,
                relation: Certificate, factor: dict) -> Certificate:
        if (left_assumption not in left.terms
                or right_assumption not in right.terms):
            fail(("combine missing branch multiplier", left_assumption,
                  right_assumption))
        if right_assumption in left.terms or left_assumption in right.terms:
            fail(("combine crossed assumptions require PruneZeroTerms",
                  {"right_in_left": left.terms.get(right_assumption),
                   "left_in_right": right.terms.get(left_assumption)}))
        f = self.generators[left_assumption]
        g = self.generators[right_assumption]
        self.p.assert_equal("combine relation", relation.target,
                            self.p.multiply(factor, f, g))
        if left_assumption in relation.terms or right_assumption in relation.terms:
            fail("combine relation retains split")
        af = left.terms[left_assumption]
        bg = right.terms[right_assumption]
        terms: dict[str, int] = {}
        left_common = self.e.mul(self.e.sparse(factor),
                                 self.e.sparse(right.target))
        for name, value in left.terms.items():
            if name != left_assumption:
                self.add_term(terms, name, self.e.mul(left_common, value))
        right_common = self.e.mul(self.e.sparse(factor), af, self.e.sparse(f))
        for name, value in right.terms.items():
            if name != right_assumption:
                self.add_term(terms, name, self.e.mul(right_common, value))
        relation_common = self.e.mul(af, bg)
        for name, value in relation.terms.items():
            self.add_term(terms, name, self.e.mul(relation_common, value))
        return Certificate(self.p.multiply(factor, left.target, right.target), terms)

    def prune_zero_terms(self, certificate: Certificate, labels: list[str]):
        terms = dict(certificate.terms)
        checks = []
        for label in labels:
            if label not in terms:
                fail(("PruneZeroTerms absent label", label))
            polynomial, telemetry = self.e.expand_exact(terms[label])
            telemetry = {"label": label, **telemetry}
            if polynomial:
                fail(("PruneZeroTerms nonzero", telemetry))
            checks.append(telemetry)
            terms.pop(label)
        return Certificate(certificate.target, terms), checks


@dataclass
class Derived:
    certificate: Certificate
    proof: int


class Builder:
    def __init__(self, kernel: Kernel) -> None:
        self.k = kernel
        self.nodes: list[dict] = []
        self.checkpoints: list[dict] = []

    def commit(self, rule: str, payload: dict, certificate: Certificate) -> Derived:
        node = {"rule": rule, **payload,
                "output": encoded_certificate(self.k.p, certificate)}
        proof = len(self.nodes)
        self.nodes.append(node)
        return Derived(certificate, proof)

    def row(self, name: str, specs: list[tuple[str, dict, str]]) -> Derived:
        encoded_specs = [
            {"variable": variable, "value": self.k.p.encoded_polynomial(value),
             "assumption": assumption}
            for variable, value, assumption in specs
        ]
        return self.commit("RowSpecialize", {"name": name, "specs": encoded_specs},
                           self.k.row(name, specs))

    def add(self, certificates: list[Derived]) -> Derived:
        return self.commit("Add", {"inputs": [item.proof for item in certificates]},
                           self.k.add([item.certificate for item in certificates]))

    def scale(self, certificate: Derived, scalar) -> Derived:
        return self.commit("Scale", {"input": certificate.proof,
                                      "scalar": fraction_record(scalar)},
                           self.k.scale(certificate.certificate, scalar))

    def multiply(self, certificate: Derived, polynomial: dict) -> Derived:
        return self.commit("Mul", {"input": certificate.proof,
                                    "polynomial": self.k.p.encoded_polynomial(polynomial)},
                           self.k.multiply(certificate.certificate, polynomial))

    def rebase_assumptions(self, certificate: Derived,
                           old_e1: str, new_g: str,
                           old_ee0: str, new_q0: str,
                           ell_label: str,
                           e1_ell_scalar, ee0_ell_scalar) -> Derived:
        payload = {
            "input": certificate.proof,
            "old_e1": old_e1,
            "new_g": new_g,
            "old_ee0": old_ee0,
            "new_q0": new_q0,
            "ell_label": ell_label,
            "e1_ell_scalar": fraction_record(e1_ell_scalar),
            "ee0_ell_scalar": fraction_record(ee0_ell_scalar),
        }
        return self.commit(
            "RebaseAssumptions", payload,
            self.k.rebase_assumptions(
                certificate.certificate, old_e1, new_g, old_ee0, new_q0,
                ell_label, e1_ell_scalar, ee0_ell_scalar,
            ),
        )

    def clear_power(self, certificate: Derived, assumption: str, exponent: int,
                    relation: Derived, factor: dict) -> Derived:
        return self.commit(
            "ClearPower",
            {"input": certificate.proof, "assumption": assumption,
             "exponent": exponent, "relation": relation.proof,
             "factor": self.k.p.encoded_polynomial(factor)},
            self.k.clear_power(certificate.certificate, assumption, exponent,
                               relation.certificate, factor),
        )

    def combine(self, left: Derived, left_assumption: str,
                right: Derived, right_assumption: str,
                relation: Derived, factor: dict) -> Derived:
        return self.commit(
            "CombineBranches",
            {"left": left.proof, "left_assumption": left_assumption,
             "right": right.proof, "right_assumption": right_assumption,
             "relation": relation.proof,
             "factor": self.k.p.encoded_polynomial(factor)},
            self.k.combine(left.certificate, left_assumption, right.certificate,
                           right_assumption, relation.certificate, factor),
        )

    def prune_zero_terms(self, certificate: Derived, labels: list[str]) -> Derived:
        answer, checks = self.k.prune_zero_terms(certificate.certificate, labels)
        return self.commit("PruneZeroTerms",
                           {"input": certificate.proof, "labels": labels,
                            "zero_checks": checks}, answer)

    def checkpoint(self, label: str, derived: Derived, expected: dict) -> None:
        self.k.p.assert_equal(label, derived.certificate.target, expected)
        self.checkpoints.append({"label": label, "proof": derived.proof,
                                 "target": self.k.p.encoded_polynomial(expected)})


def verify_rule_schemas(p, exponents: set[int]) -> None:
    T, U, m, f, z = (p.variable(name) for name in ("T", "U", "m", "f", "z"))
    for exponent in sorted(exponents):
        geometric = {}
        mf = p.multiply(m, f)
        for index in range(exponent):
            geometric = p.add(geometric,
                              p.multiply(p.power(T, exponent - 1 - index),
                                         p.power(mf, index)))
        lhs = p.multiply(z, p.power(T, exponent))
        rhs = p.add(
            p.multiply(z, p.add(T, p.scale(mf, -1)), geometric),
            p.multiply(p.power(m, exponent), z, p.power(f, exponent)),
        )
        p.assert_equal("universal clear_power schema", lhs, rhs)
    af, bg, g = (p.variable(name) for name in ("af", "bg", "g"))
    lhs = p.multiply(z, T, U)
    rhs = p.add(
        p.multiply(z, U, p.add(T, p.scale(p.multiply(af, f), -1))),
        p.multiply(z, af, f, p.add(U, p.scale(p.multiply(bg, g), -1))),
        p.multiply(af, bg, z, f, g),
    )
    p.assert_equal("universal combine schema", lhs, rhs)


def replay_record(record: dict, p, rows: dict[str, dict], generators: dict[str, dict],
                  assumptions: set[str]) -> Certificate:
    expressions = ExprStore.from_record(p, record["expression_nodes"])
    kernel = Kernel(p, rows, generators, assumptions, expressions)
    certificates: list[Certificate] = []
    used_clear_exponents = set()
    for index, node in enumerate(record["derivation_nodes"]):
        rule = node.get("rule")
        if rule == "RowSpecialize":
            specs = [(item["variable"], decode_polynomial(item["value"]),
                      item["assumption"]) for item in node["specs"]]
            certificate = kernel.row(node["name"], specs)
        elif rule == "Add":
            certificate = kernel.add([certificates[item] for item in node["inputs"]])
        elif rule == "Scale":
            certificate = kernel.scale(certificates[node["input"]],
                                       Fraction(*node["scalar"]))
        elif rule == "Mul":
            certificate = kernel.multiply(certificates[node["input"]],
                                          decode_polynomial(node["polynomial"]))
        elif rule == "RebaseAssumptions":
            certificate = kernel.rebase_assumptions(
                certificates[node["input"]],
                node["old_e1"], node["new_g"],
                node["old_ee0"], node["new_q0"], node["ell_label"],
                Fraction(*node["e1_ell_scalar"]),
                Fraction(*node["ee0_ell_scalar"]),
            )
        elif rule == "ClearPower":
            exponent = node["exponent"]
            used_clear_exponents.add(exponent)
            certificate = kernel.clear_power(
                certificates[node["input"]], node["assumption"], exponent,
                certificates[node["relation"]], decode_polynomial(node["factor"]),
            )
        elif rule == "CombineBranches":
            certificate = kernel.combine(
                certificates[node["left"]], node["left_assumption"],
                certificates[node["right"]], node["right_assumption"],
                certificates[node["relation"]], decode_polynomial(node["factor"]),
            )
        elif rule == "PruneZeroTerms":
            certificate, checks = kernel.prune_zero_terms(
                certificates[node["input"]], node["labels"]
            )
            if checks != node.get("zero_checks"):
                fail(("PruneZeroTerms telemetry commitment", index))
        else:
            fail(("unknown derivation rule", index, rule))
        if encoded_certificate(p, certificate) != node.get("output"):
            fail(("derivation output commitment", index, rule))
        certificates.append(certificate)
    verify_rule_schemas(p, used_clear_exponents)
    for item in record["checkpoints"]:
        p.assert_equal("checkpoint:" + item["label"],
                       certificates[item["proof"]].target,
                       decode_polynomial(item["target"]))
    final = certificates[record["final_proof"]]
    if encoded_certificate(p, final) != record["final_certificate"]:
        fail("final certificate commitment")
    return final


def build_proof(p, rows: dict[str, dict], generators: dict[str, dict],
                labels: dict[str, str], assumptions: set[str]):
    expressions = ExprStore()
    expressions.install_backend(p)
    kernel = Kernel(p, rows, generators, assumptions, expressions)
    b = Builder(kernel)
    zero, one = {}, p.const(1)
    a = p.variable("a1")
    ell = p.variable("ell1")
    rs = p.variable("rs1")
    aa = p.variable("aa0")
    cs = p.variable("cs1")
    cs2 = p.variable("cs2")
    ee1 = p.variable("ee1")
    ec3 = p.variable("ec3")
    rs2 = p.variable("rs2")
    ez3 = p.variable("ez3")
    ec4 = p.variable("ec4")
    G = "assume:e1_minus_4a1ell1"
    Q0 = "assume:ee0_plus_4aa0ell1"
    Q4 = "assume:ec4_minus_a1cs2"
    H = "assume:a1_minus_6cs2ell1"

    def specs_zero(names: list[str]):
        return [(name, zero, labels[name]) for name in names]

    def combine_clean(left: Derived, left_assumption: str,
                      right: Derived, right_assumption: str,
                      relation: Derived, factor: dict) -> Derived:
        left_cross = ([right_assumption]
                      if right_assumption in left.certificate.terms else [])
        right_cross = ([left_assumption]
                       if left_assumption in right.certificate.terms else [])
        if left_cross:
            left = b.prune_zero_terms(left, left_cross)
        if right_cross:
            right = b.prune_zero_terms(right, right_cross)
        return b.combine(left, left_assumption, right, right_assumption,
                         relation, factor)

    # Reviewed A1 branch certificate, with all specializations lifted to
    # assumption generators but multiplier arithmetic kept as a DAG.
    a1_specs = specs_zero(["e0", "e1", "ee0", "ell1", "rs1"])
    a1_sub = {name: zero for name in ("e0", "e1", "ee0", "ell1", "rs1")}
    ec3_value = p.add(p.multiply(a, cs),
                      p.scale(p.multiply(p.variable("a1", -1), aa, ee1), -1))
    ell2 = p.variable("ell2")
    rs2_value = p.add(
        p.scale(p.multiply(p.variable("a1", -3), p.power(aa, 2), ee1), -4),
        p.multiply(p.variable("a1", -2), p.power(ee1, 2)),
        p.scale(p.multiply(p.variable("a1", -1), aa, cs), -4),
        p.scale(p.multiply(p.variable("a1", -1), ee1, ell2), -4),
    )
    eliminations = {"ec3": ec3_value, "rs2": rs2_value}
    raw_diagonal = {
        grade: p.substitute(rows[name], a1_sub)
        for grade, name in {15: "Tg15_3", 17: "Tg17_5",
                            18: "Tg18_6", 19: "Tg19_7"}.items()
    }
    h15 = p.add(
        p.scale(p.multiply(p.power(aa, 3), ee1, p.variable("a1", -8)), -96),
        p.scale(p.multiply(aa, p.power(ee1, 2), p.variable("a1", -7)), 24),
        p.scale(p.multiply(p.power(aa, 2), cs, p.variable("a1", -6)), -96),
        p.scale(p.multiply(aa, ee1, ell2, p.variable("a1", -6)), -192),
        p.scale(p.multiply(aa, p.power(ell2, 2), p.variable("a1", -5)), 144),
        p.scale(p.multiply(ee1, cs, p.variable("a1", -5)), 48),
        p.scale(p.multiply(cs, ell2, p.variable("a1", -4)), 48),
        p.scale(p.variable("a1", -3), -16),
    )
    h17 = p.add(
        p.scale(p.multiply(aa, ee1, p.variable("a1", -6)), -192),
        p.scale(p.multiply(aa, ell2, p.variable("a1", -5)), 192),
        p.scale(p.multiply(cs, p.variable("a1", -4)), 96),
    )
    h18 = p.scale(p.multiply(ee1, p.variable("a1", -5)), 192)
    h19 = p.scale(p.multiply(aa, p.variable("a1", -5)), 384)
    quotient_multipliers = {15: h15, 17: h17, 18: h18, 19: h19}
    raw_sum = {}
    for grade, multiplier in quotient_multipliers.items():
        raw_sum = p.add(raw_sum, p.multiply(multiplier, raw_diagonal[grade]))
    difference = p.add(raw_sum, p.scale(one, -1))
    q3 = p.divided_difference(difference, "ec3", ec3_value)
    after_ec3 = p.substitute(difference, {"ec3": ec3_value})
    q2 = p.divided_difference(after_ec3, "rs2", rs2_value)
    h13 = p.add(
        p.scale(p.multiply(p.variable("a1", -1), q3), Fraction(-8, 3)),
        p.scale(p.multiply(aa, p.variable("a1", -3), q2), Fraction(-32, 3)),
    )
    h14 = p.scale(p.multiply(p.variable("a1", -2), q2), Fraction(32, 3))
    direct = {13: h13, 14: h14, **quotient_multipliers}
    cleared = {grade: p.multiply(p.power(a, 8), multiplier)
               for grade, multiplier in direct.items()}
    if any(exponent < 0 for polynomial in cleared.values()
           for monomial in polynomial for _, exponent in monomial):
        fail("A1 clearing retained a negative exponent")
    a1_rows = {13: "Tg13_1", 14: "Tg14_2", 15: "Tg15_3",
               17: "Tg17_5", 18: "Tg18_6", 19: "Tg19_7"}
    a1_pieces = [b.multiply(b.row(row_name, a1_specs), cleared[grade])
                 for grade, row_name in a1_rows.items()]
    a1_certificate = b.add(a1_pieces)
    b.checkpoint("A1 lifted a1^8", a1_certificate, p.power(a, 8))

    B = specs_zero(["e0", "e1", "ee0"])
    BL = B + [("ell1", zero, labels["ell1"])]
    a2 = b.add([
        b.row("Tg16_6", BL),
        b.multiply(b.row("Tg13_2", BL), p.scale(rs, Fraction(-3, 32))),
    ])
    a2 = b.scale(a2, Fraction(1024, 21))
    b.checkpoint("A2 a2rs2", a2, p.multiply(p.power(a, 2), p.power(rs, 2)))
    a18_mod_ell = b.clear_power(a1_certificate, labels["rs1"], 2, a2,
                                p.power(a, 2))
    b.checkpoint("a18 modulo ell1", a18_mod_ell, p.power(a, 18))

    K0 = B + [("rs1", zero, labels["rs1"]),
              ("cs1", zero, labels["cs1"])]
    rel_ee1 = b.scale(b.row("Tg13_2", K0), Fraction(-8, 3))
    b.checkpoint("caseB a ell ee1", rel_ee1, p.multiply(a, ell, ee1))
    K1 = K0 + [("ee1", zero, labels["ee1"])]
    rel_ec3 = b.scale(b.row("Tg13_1", K1), Fraction(8, 3))
    b.checkpoint("caseB a ec3", rel_ec3, p.multiply(a, ec3))
    K2 = K1 + [("ec3", zero, labels["ec3"])]
    rel_rs2 = b.scale(b.row("Tg15_4", K2), Fraction(32, 3))
    b.checkpoint("caseB a2 ell rs2", rel_rs2,
                 p.multiply(p.power(a, 2), ell, rs2))
    K3 = K2 + [("rs2", zero, labels["rs2"])]
    rel_ez3 = b.scale(b.row("Tg14_2", K3), Fraction(-8, 3))
    b.checkpoint("caseB a ell ez3", rel_ez3, p.multiply(a, ell, ez3))
    K4 = K3 + [("ez3", zero, labels["ez3"])]
    rel_q4 = b.scale(b.row("Tg14_1", K4), Fraction(8, 3))
    b.checkpoint("caseB a q4", rel_q4, p.multiply(a, generators[Q4]))
    K5 = K4 + [("ec4", p.multiply(a, cs2), Q4)]
    rel_h = b.scale(b.row("Tg15_3", K5), -16)
    b.checkpoint("caseB a2 h", rel_h, p.multiply(p.power(a, 2), generators[H]))
    K6 = K5 + [("a1", p.scale(p.multiply(cs2, ell), 6), H)]
    terminal = b.scale(b.row("Tg16_5", K6), Fraction(2, 27))
    b.checkpoint("caseB terminal", terminal,
                 p.multiply(p.power(cs2, 3), p.power(ell, 4)))
    terminal_lift = b.clear_power(terminal, H, 1, rel_h, p.power(a, 2))
    b.checkpoint("caseB terminal lift", terminal_lift,
                 p.multiply(p.power(a, 2), p.power(cs2, 3), p.power(ell, 4)))
    recurrence = p.multiply(
        ell,
        p.add(p.power(a, 2),
              p.scale(p.multiply(a, cs2, ell), 6),
              p.scale(p.multiply(p.power(cs2, 2), p.power(ell, 2)), 36)),
    )
    a5ell = b.add([b.multiply(rel_h, recurrence), b.scale(terminal_lift, 216)])
    b.checkpoint("caseB a5ell", a5ell, p.multiply(p.power(a, 5), ell))
    a6ell = b.clear_power(a5ell, Q4, 1, rel_q4, a)
    a7ell = b.clear_power(a6ell, labels["ec3"], 1, rel_ec3, a)
    b.checkpoint("caseB a7ell", a7ell, p.multiply(p.power(a, 7), ell))
    a15_case = b.clear_power(a1_certificate, labels["ell1"], 1, a7ell,
                             p.power(a, 7))
    b.checkpoint("caseB a15", a15_case, p.power(a, 15))

    combined = b.add([
        b.row("Tg14_3", B),
        b.multiply(b.row("Tg13_1", B), p.scale(ell, Fraction(1, 2))),
    ])
    combined_rs0 = b.row("Tg14_3", B)  # placeholder overwritten below
    # Specialize an already-derived certificate by rebuilding its exact
    # two row leaves with the additional rs1=0 specialization.
    combined_rs0 = b.add([
        b.row("Tg14_3", B + [("rs1", zero, labels["rs1"])]),
        b.multiply(b.row("Tg13_1", B + [("rs1", zero, labels["rs1"])]),
                   p.scale(ell, Fraction(1, 2))),
    ])
    rel_ell_cs = b.scale(combined_rs0, Fraction(8, 3))
    b.checkpoint("rs1 zero a2 ell cs1", rel_ell_cs,
                 p.multiply(p.power(a, 2), ell, cs))
    a25_mod_rs = combine_clean(a1_certificate, labels["ell1"], a15_case,
                               labels["cs1"], rel_ell_cs, p.power(a, 2))
    b.checkpoint("a25 modulo rs1", a25_mod_rs, p.power(a, 25))

    rel_ell_rs = b.scale(b.row("Tg14_4", B), Fraction(32, 3))
    b.checkpoint("a2 ell rs1", rel_ell_rs, p.multiply(p.power(a, 2), ell, rs))
    a45_mod_B = combine_clean(a18_mod_ell, labels["ell1"], a25_mod_rs,
                              labels["rs1"], rel_ell_rs, p.power(a, 2))
    b.checkpoint("a45 modulo base", a45_mod_B, p.power(a, 45))

    e0e1 = specs_zero(["e0", "e1"])
    rel_ee0 = b.scale(b.row("Tg12_1", e0e1), Fraction(8, 3))
    b.checkpoint("a ee0", rel_ee0, p.multiply(a, p.variable("ee0")))
    a46_mod_e0e1 = b.clear_power(a45_mod_B, labels["ee0"], 1, rel_ee0, a)
    b.checkpoint("a46 modulo e0e1", a46_mod_e0e1, p.power(a, 46))

    e0_g_q_specs = [("e0", zero, labels["e0"]),
                    ("e1", p.scale(p.multiply(a, ell), 4), G)]
    rel_q0 = b.scale(b.row("Tg12_1", e0_g_q_specs), Fraction(8, 3))
    b.checkpoint("a q0", rel_q0, p.multiply(a, generators[Q0]))
    rel_ell3 = b.scale(b.row(
        "Tg13_4",
        e0_g_q_specs + [("ee0", p.scale(p.multiply(aa, ell), -4), Q0)],
    ), Fraction(-2, 3))
    b.checkpoint("a2 ell3", rel_ell3,
                 p.multiply(p.power(a, 2), p.power(ell, 3)))
    a18_mod_gqell = b.rebase_assumptions(
        a18_mod_ell,
        labels["e1"], G, labels["ee0"], Q0, labels["ell1"],
        Fraction(4), Fraction(-4),
    )
    if (labels["e1"] in a18_mod_gqell.certificate.terms
            or labels["ee0"] in a18_mod_gqell.certificate.terms):
        fail("second branch rebase retained old labels")
    b.checkpoint("a18 rebased modulo e0 G Q0 ell1", a18_mod_gqell,
                 p.power(a, 18))
    a56_mod_e0gq = b.clear_power(a18_mod_gqell, labels["ell1"], 3, rel_ell3,
                                 p.power(a, 2))
    b.checkpoint("a56 modulo e0gq", a56_mod_e0gq, p.power(a, 56))
    a57_mod_e0g = b.clear_power(a56_mod_e0gq, Q0, 1, rel_q0, a)
    b.checkpoint("a57 modulo e0g", a57_mod_e0g, p.power(a, 57))

    rel_e1_split = b.scale(b.row("Tg12_2", [("e0", zero, labels["e0"])]),
                           Fraction(32, 3))
    b.checkpoint("e1 split", rel_e1_split,
                 p.multiply(p.variable("e1"), generators[G]))
    a103_mod_e0 = combine_clean(a46_mod_e0e1, labels["e1"], a57_mod_e0g, G,
                                rel_e1_split, one)
    b.checkpoint("a103 modulo e0", a103_mod_e0, p.power(a, 103))
    rel_e0 = b.scale(b.row("Tg11_1", []), Fraction(8, 3))
    b.checkpoint("a e0", rel_e0, p.multiply(a, p.variable("e0")))
    final = b.clear_power(a103_mod_e0, labels["e0"], 1, rel_e0, a)
    final_zero_candidates = sorted(set(final.certificate.terms) & assumptions)
    if final_zero_candidates:
        final = b.prune_zero_terms(final, final_zero_candidates)
    b.checkpoint("global a104", final, p.power(a, 104))
    return expressions, b, final


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    for path, expected in (
        (INVALIDATION, INVALIDATION_SHA256),
        (INVALIDATION_FREEZE, INVALIDATION_FREEZE_SHA256),
    ):
        if digest(path) != expected:
            fail(("invalidation pin", str(path), digest(path), expected))
    for line in INVALIDATION_FREEZE.read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        path = ROOT / relative
        if not path.is_file() or digest(path) != expected:
            fail(("invalidation frozen file", relative,
                  digest(path) if path.is_file() else "MISSING", expected))
    c1 = load_c1()
    p = c1.load_v42()
    v37 = p.load_v37()
    _, row_items, row_hashes, _ = v37.load_rows()
    rows = {item["name"]: {tuple(monomial): coefficient
                           for monomial, coefficient in item["polynomial"].items()}
            for item in row_items}
    if len(rows) != 51 or len(row_hashes) != 70:
        fail(("row census", len(rows), len(row_hashes)))
    alphabet = sorted({name for polynomial in rows.values()
                       for monomial in polynomial for name, _ in monomial})
    if len(alphabet) != 65 or "rho" in alphabet or "ez9" in alphabet:
        fail(("rho0 alphabet", len(alphabet), alphabet))

    generators = dict(rows)
    assumption_polynomials = {}
    labels = {name: "assume:" + name for name in
              ("e0", "e1", "ee0", "ell1", "rs1", "aa0", "cs1",
               "ee1", "ec3", "rs2", "ez3")}
    for name, label in labels.items():
        generators[label] = p.variable(name)
        assumption_polynomials[label] = generators[label]
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
    assumption_polynomials.update(extra)

    expressions, builder, final = build_proof(
        p, rows, generators, labels, set(assumption_polynomials)
    )
    if final.certificate.target != p.power(a, 104):
        fail("final target")
    surviving = sorted(set(final.certificate.terms) & set(assumption_polynomials))
    if surviving:
        fail(("surviving assumptions", surviving))
    if not final.certificate.terms or set(final.certificate.terms) - set(rows):
        fail(("final literal-row labels", sorted(final.certificate.terms)))
    if "Tg19_7" not in final.certificate.terms:
        fail("Tg19_7 missing from final circuit")

    record = {
        "format": "JC2-EXACT-POLYNOMIAL-CERTIFICATE-DAG-REBASED-V2",
        "ambient_ring": "Q[X19_rho0]",
        "alphabet": alphabet,
        "row_sha256": row_hashes,
        "expression_nodes": expressions.nodes,
        "derivation_nodes": builder.nodes,
        "checkpoints": builder.checkpoints,
        "final_proof": final.proof,
        "final_certificate": encoded_certificate(p, final.certificate),
        "target": "a1^104",
        "registered_aws_lane": tag,
        "producer_sha256": digest(Path(__file__)),
        "v43c1_sha256": C1_SHA256,
        "v43c2_invalidation_sha256": INVALIDATION_SHA256,
        "v43c2_invalidation_freeze_sha256": INVALIDATION_FREEZE_SHA256,
        "preregistration_sha256": digest(PREREG),
    }
    proof_path = output / "a1_104_exact_derivation_dag_rebased.json"
    proof_path.write_text(json.dumps(record, sort_keys=True,
                                     separators=(",", ":")) + "\n")
    loaded = json.loads(proof_path.read_text())
    replayed = replay_record(loaded, p, rows, generators,
                             set(assumption_polynomials))
    if replayed.target != p.power(a, 104):
        fail("serialized replay target")

    omission = copy.deepcopy(loaded)
    omission["final_certificate"]["terms"].pop("Tg19_7")
    omission_rejected = False
    try:
        replay_record(omission, p, rows, generators, set(assumption_polynomials))
    except Exception:
        omission_rejected = True
    if not omission_rejected:
        fail("omission mutation accepted")

    wrong_exponent = copy.deepcopy(loaded)
    changed_index = None
    for index, node in enumerate(wrong_exponent["derivation_nodes"]):
        if node.get("rule") == "ClearPower" and node.get("exponent") == 2:
            node["exponent"] = 3
            changed_index = index
            break
    if changed_index is None:
        fail("no exponent mutation target")
    exponent_rejected = False
    try:
        replay_record(wrong_exponent, p, rows, generators,
                      set(assumption_polynomials))
    except Exception:
        exponent_rejected = True
    if not exponent_rejected:
        fail("wrong-exponent mutation accepted")

    rebase_indices = [index for index, node in enumerate(loaded["derivation_nodes"])
                      if node.get("rule") == "RebaseAssumptions"]
    if len(rebase_indices) != 1:
        fail(("rebase rule census", rebase_indices))
    rebase_index = rebase_indices[0]
    sign_mutations = {}
    for field, expected in (("e1_ell_scalar", [4, 1]),
                            ("ee0_ell_scalar", [-4, 1])):
        if loaded["derivation_nodes"][rebase_index].get(field) != expected:
            fail(("rebase scalar commitment", field,
                  loaded["derivation_nodes"][rebase_index].get(field), expected))
        mutated = copy.deepcopy(loaded)
        mutated["derivation_nodes"][rebase_index][field][0] *= -1
        rejected = False
        try:
            replay_record(mutated, p, rows, generators,
                          set(assumption_polynomials))
        except Exception:
            rejected = True
        if not rejected:
            fail(("rebase sign mutation accepted", field))
        sign_mutations[field] = {
            "derivation_index": rebase_index,
            "from": expected,
            "to": [-expected[0], expected[1]],
            "rejected": True,
        }

    result = {
        "status": "PASS-A1-RHO0-RAW-CONSTRUCTIVE-CIRCUIT-REBASED-A1-104-V43C3",
        "scope": "all frozen raw ordered-a1 rho-zero rows through grade 19 over Q",
        "conclusion": "a1^104 belongs to the unsplit frozen rho-zero raw ideal",
        "proof_sha256": digest(proof_path),
        "proof_bytes": proof_path.stat().st_size,
        "expression_node_count": len(expressions.nodes),
        "derivation_node_count": len(builder.nodes),
        "checkpoint_count": len(builder.checkpoints),
        "final_nonzero_row_multiplier_count": len(final.certificate.terms),
        "final_rows": sorted(final.certificate.terms),
        "named_row_count": len(rows),
        "frozen_row_file_count": len(row_hashes),
        "alphabet_size": len(alphabet),
        "omission_mutation": {"removed": "Tg19_7", "rejected": True},
        "wrong_exponent_mutation": {"derivation_index": changed_index,
                                      "from": 2, "to": 3, "rejected": True},
        "rebase_rule_count": 1,
        "rebase_derivation_index": rebase_index,
        "rebase_sign_mutations": sign_mutations,
        "rebase_old_labels_absent_before_clear": ["assume:e1", "assume:ee0"],
        "v43c2_invalidation_sha256": INVALIDATION_SHA256,
        "v43c2_invalidation_freeze_sha256": INVALIDATION_FREEZE_SHA256,
        "universal_rule_schemas": "exact polynomial replay",
        "firewalls": [
            "rho=0 frozen raw ordered-a1 rows only",
            "arithmetic DAG denotes ordinary polynomials, never localized fractions",
            "no unspecialized-rho or saturated-Rees conclusion without converter/map",
        ],
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-RAW-CONSTRUCTIVE-CIRCUIT-REBASED-A1-104-V43C3")
    print("PROOF_SHA256=" + digest(proof_path))
    print("RESULT_SHA256=" + digest(result_path))
    print("EXPRESSION_NODES=" + str(len(expressions.nodes)))
    print("DERIVATION_NODES=" + str(len(builder.nodes)))
    print("FINAL_ROWS=" + str(len(final.certificate.terms)))


if __name__ == "__main__":
    main()
