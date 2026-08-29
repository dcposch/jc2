#!/usr/bin/env python3
"""Construct and replay an unsplit rho=0 a1-power certificate.

The proof is a certificate tree, not a Gröbner-basis computation.  It turns
the reviewed V41/V42 field-point cascade into ordinary ideal membership by
clearing every branch equation algebraically.  All arithmetic is exact
``Fraction`` sparse-polynomial arithmetic.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V42 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py"
V42_SHA256 = "f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459"
PINS = {
    ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md":
        "5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f",
    ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-hostile-review-opus5-20260827.md":
        "a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v42():
    if digest(V42) != V42_SHA256:
        fail(("V42 replay hash", digest(V42), V42_SHA256))
    for path, expected in PINS.items():
        if digest(path) != expected:
            fail(("pin", str(path), digest(path), expected))
    spec = importlib.util.spec_from_file_location("constructive_cascade_v42", V42)
    if spec is None or spec.loader is None:
        fail("V42 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    prefix = "max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_"
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith(prefix)):
        fail("registered constructive-cascade AWS lane required")
    return tag


@dataclass
class Certificate:
    target: dict
    terms: dict[str, dict]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    registered_tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    p = load_v42()
    v37 = p.load_v37()
    parser, row_items, row_hashes, _ = v37.load_rows()
    rows = {
        item["name"]: {tuple(monomial): coefficient
                       for monomial, coefficient in item["polynomial"].items()}
        for item in row_items
    }
    if len(rows) != 51 or len(row_hashes) != 70:
        fail(("row census", len(rows), len(row_hashes)))

    zero = {}
    one = p.const(1)
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

    generators = dict(rows)
    assumption_polynomials: dict[str, dict] = {}

    def register(label: str, polynomial: dict) -> None:
        prior = generators.get(label)
        if prior is not None and prior != polynomial:
            fail(("generator collision", label))
        generators[label] = polynomial
        assumption_polynomials[label] = polynomial

    labels = {
        "e0": "assume:e0",
        "e1": "assume:e1",
        "ee0": "assume:ee0",
        "ell1": "assume:ell1",
        "rs1": "assume:rs1",
        "aa0": "assume:aa0",
        "cs1": "assume:cs1",
        "ee1": "assume:ee1",
        "ec3": "assume:ec3",
        "rs2": "assume:rs2",
        "ez3": "assume:ez3",
    }
    for name, label in labels.items():
        register(label, p.variable(name))
    G = "assume:e1_minus_4a1ell1"
    Q0 = "assume:ee0_plus_4aa0ell1"
    Q4 = "assume:ec4_minus_a1cs2"
    H = "assume:a1_minus_6cs2ell1"
    register(G, p.add(p.variable("e1"), p.scale(p.multiply(a, ell), -4)))
    register(Q0, p.add(p.variable("ee0"), p.scale(p.multiply(aa, ell), -4 * -1)))
    register(Q4, p.add(ec4, p.scale(p.multiply(a, cs2), -1)))
    register(H, p.add(a, p.scale(p.multiply(cs2, ell), -6)))

    def add_term(terms: dict[str, dict], label: str, multiplier: dict) -> None:
        if not multiplier:
            return
        value = p.add(terms.get(label, {}), multiplier)
        if value:
            terms[label] = value
        else:
            terms.pop(label, None)

    def cert_add(*certificates: Certificate) -> Certificate:
        target = {}
        terms: dict[str, dict] = {}
        for certificate in certificates:
            target = p.add(target, certificate.target)
            for label, multiplier in certificate.terms.items():
                add_term(terms, label, multiplier)
        return Certificate(target, terms)

    def cert_scale(certificate: Certificate, scalar) -> Certificate:
        return Certificate(
            p.scale(certificate.target, scalar),
            {label: p.scale(multiplier, scalar)
             for label, multiplier in certificate.terms.items()
             if p.scale(multiplier, scalar)},
        )

    def cert_multiply(certificate: Certificate, polynomial: dict) -> Certificate:
        return Certificate(
            p.multiply(certificate.target, polynomial),
            {label: p.multiply(multiplier, polynomial)
             for label, multiplier in certificate.terms.items()
             if p.multiply(multiplier, polynomial)},
        )

    def residual(certificate: Certificate, override: dict[str, dict] | None = None) -> dict:
        total = {}
        source = generators if override is None else {**generators, **override}
        for label, multiplier in certificate.terms.items():
            if label not in source:
                fail(("unknown generator", label))
            total = p.add(total, p.multiply(multiplier, source[label]))
        return p.add(certificate.target, p.scale(total, -1))

    def verify(label: str, certificate: Certificate) -> None:
        answer = residual(certificate)
        if answer:
            fail(("certificate residual", label, len(answer), p.polynomial_hash(answer)))

    def specialize_cert(certificate: Certificate, variable: str, value: dict,
                        assumption: str) -> Certificate:
        expected = p.add(p.variable(variable), p.scale(value, -1))
        if generators.get(assumption) != expected:
            fail(("bad specialization generator", variable, assumption))
        quotient = p.divided_difference(certificate.target, variable, value)
        target = p.substitute(certificate.target, {variable: value})
        terms = dict(certificate.terms)
        add_term(terms, assumption, p.scale(quotient, -1))
        answer = Certificate(target, terms)
        verify("specialize:" + assumption, answer)
        return answer

    def row_certificate(name: str, specs: list[tuple[str, dict, str]]) -> Certificate:
        answer = Certificate(rows[name], {name: one})
        for variable, value, assumption in specs:
            answer = specialize_cert(answer, variable, value, assumption)
        return answer

    def assert_target(label: str, certificate: Certificate, target: dict) -> None:
        p.assert_equal(label, certificate.target, target)
        verify(label, certificate)

    def clear_power(certificate: Certificate, assumption: str, exponent: int,
                    relation: Certificate, factor: dict, label: str) -> Certificate:
        """Clear f^exponent using target(relation)=factor*f^exponent."""
        if exponent <= 0 or assumption not in certificate.terms:
            fail(("clear-power contract", label, exponent, assumption,
                  sorted(certificate.terms)))
        f = generators[assumption]
        p.assert_equal(label + ":relation-target", relation.target,
                       p.multiply(factor, p.power(f, exponent)))
        if assumption in relation.terms:
            fail(("relation retains assumption", label, assumption))
        multiplier = certificate.terms[assumption]
        bf = p.multiply(multiplier, f)
        geometric = {}
        for index in range(exponent):
            geometric = p.add(
                geometric,
                p.multiply(p.power(certificate.target, exponent - 1 - index),
                           p.power(bf, index)),
            )
        terms: dict[str, dict] = {}
        for name, value in certificate.terms.items():
            if name != assumption:
                add_term(terms, name, p.multiply(factor, geometric, value))
        replacement_scale = p.power(multiplier, exponent)
        for name, value in relation.terms.items():
            add_term(terms, name, p.multiply(replacement_scale, value))
        answer = Certificate(
            p.multiply(factor, p.power(certificate.target, exponent)), terms
        )
        verify(label, answer)
        return answer

    def clear_linear(certificate: Certificate, assumption: str,
                     relation: Certificate, factor: dict, label: str) -> Certificate:
        return clear_power(certificate, assumption, 1, relation, factor, label)

    def combine_branches(left: Certificate, left_assumption: str,
                         right: Certificate, right_assumption: str,
                         relation: Certificate, factor: dict,
                         label: str) -> Certificate:
        """Multiply branch certificates and replace factor*f*g by relation."""
        if left_assumption not in left.terms or right_assumption not in right.terms:
            fail(("branch multipliers absent", label,
                  left_assumption in left.terms, right_assumption in right.terms,
                  sorted(left.terms), sorted(right.terms)))
        if right_assumption in left.terms or left_assumption in right.terms:
            fail(("crossed branch assumptions", label))
        f = generators[left_assumption]
        g = generators[right_assumption]
        p.assert_equal(label + ":relation-target", relation.target,
                       p.multiply(factor, f, g))
        if left_assumption in relation.terms or right_assumption in relation.terms:
            fail(("branch relation retains split", label))
        af = left.terms[left_assumption]
        bg = right.terms[right_assumption]
        terms: dict[str, dict] = {}
        for name, value in left.terms.items():
            if name != left_assumption:
                add_term(terms, name,
                         p.multiply(factor, right.target, value))
        for name, value in right.terms.items():
            if name != right_assumption:
                add_term(terms, name,
                         p.multiply(factor, af, f, value))
        for name, value in relation.terms.items():
            add_term(terms, name, p.multiply(af, bg, value))
        answer = Certificate(
            p.multiply(factor, left.target, right.target), terms
        )
        verify(label, answer)
        return answer

    def specs_zero(names: list[str]) -> list[tuple[str, dict, str]]:
        return [(name, zero, labels[name]) for name in names]

    # Rebuild the V42 A1 a1^8 certificate, then lift all five zero
    # specializations to named assumption generators.
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
    p13 = p.substitute(rows["Tg13_1"], a1_sub)
    p14 = p.substitute(rows["Tg14_2"], a1_sub)
    raw_diagonal = {
        grade: p.substitute(rows[name], a1_sub)
        for grade, name in {15: "Tg15_3", 17: "Tg17_5",
                            18: "Tg18_6", 19: "Tg19_7"}.items()
    }
    reduced = {grade: p.substitute(polynomial, eliminations)
               for grade, polynomial in raw_diagonal.items()}
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
    a1_rows = {13: "Tg13_1", 14: "Tg14_2", 15: "Tg15_3",
               17: "Tg17_5", 18: "Tg18_6", 19: "Tg19_7"}
    a1_certificate = Certificate({}, {})
    for grade, row_name in a1_rows.items():
        a1_certificate = cert_add(
            a1_certificate,
            cert_multiply(row_certificate(row_name, a1_specs), cleared[grade]),
        )
    assert_target("A1 lifted a1^8", a1_certificate, p.power(a, 8))

    B = specs_zero(["e0", "e1", "ee0"])
    BL = B + [("ell1", zero, labels["ell1"])]

    # V42 stated the A2 identity after aa0=0, but direct replay shows that
    # aa0 cancels: this two-row identity already holds modulo B+(ell1).
    a2 = cert_add(
        row_certificate("Tg16_6", BL),
        cert_multiply(row_certificate("Tg13_2", BL),
                      p.scale(rs, Fraction(-3, 32))),
    )
    a2 = cert_scale(a2, Fraction(1024, 21))
    assert_target("A2 a^2*rs1^2", a2, p.multiply(p.power(a, 2), p.power(rs, 2)))
    a18_mod_ell = clear_power(
        a1_certificate, labels["rs1"], 2, a2, p.power(a, 2),
        "A2 converted directly to a18 modulo ell1",
    )
    assert_target("a18 modulo ell1", a18_mod_ell, p.power(a, 18))

    # Construct the D(ell1) contradiction without division.  Reverse
    # elimination produces a^11*ell1^4 before the A1 ell1=0 branch clears it.
    K0 = B + [("rs1", zero, labels["rs1"]),
              ("cs1", zero, labels["cs1"])]
    rel_ee1 = cert_scale(row_certificate("Tg13_2", K0), Fraction(-8, 3))
    assert_target("caseB a*ell*ee1", rel_ee1, p.multiply(a, ell, ee1))
    K1 = K0 + [("ee1", zero, labels["ee1"])]
    rel_ec3 = cert_scale(row_certificate("Tg13_1", K1), Fraction(8, 3))
    assert_target("caseB a*ec3", rel_ec3, p.multiply(a, ec3))
    K2 = K1 + [("ec3", zero, labels["ec3"])]
    rel_rs2 = cert_scale(row_certificate("Tg15_4", K2), Fraction(32, 3))
    assert_target("caseB a2*ell*rs2", rel_rs2,
                  p.multiply(p.power(a, 2), ell, rs2))
    K3 = K2 + [("rs2", zero, labels["rs2"])]
    rel_ez3 = cert_scale(row_certificate("Tg14_2", K3), Fraction(-8, 3))
    assert_target("caseB a*ell*ez3", rel_ez3, p.multiply(a, ell, ez3))
    K4 = K3 + [("ez3", zero, labels["ez3"])]
    rel_q4 = cert_scale(row_certificate("Tg14_1", K4), Fraction(8, 3))
    assert_target("caseB a*q4", rel_q4, p.multiply(a, generators[Q4]))
    K5 = K4 + [("ec4", p.multiply(a, cs2), Q4)]
    rel_h = cert_scale(row_certificate("Tg15_3", K5), -16)
    assert_target("caseB a2*h", rel_h, p.multiply(p.power(a, 2), generators[H]))
    K6 = K5 + [("a1", p.scale(p.multiply(cs2, ell), 6), H)]
    terminal = cert_scale(row_certificate("Tg16_5", K6), Fraction(2, 27))
    assert_target("caseB terminal", terminal, p.multiply(p.power(cs2, 3), p.power(ell, 4)))
    terminal_lift = clear_linear(
        terminal, H, rel_h, p.power(a, 2), "caseB clear h"
    )
    assert_target("caseB a2*cs2^3*ell4", terminal_lift,
                  p.multiply(p.power(a, 2), p.power(cs2, 3), p.power(ell, 4)))
    recurrence_factor = p.multiply(
        ell,
        p.add(p.power(a, 2),
              p.scale(p.multiply(a, cs2, ell), 6),
              p.scale(p.multiply(p.power(cs2, 2), p.power(ell, 2)), 36)),
    )
    a5ell = cert_add(cert_multiply(rel_h, recurrence_factor),
                     cert_scale(terminal_lift, 216))
    assert_target("caseB a5*ell", a5ell, p.multiply(p.power(a, 5), ell))
    a6ell = clear_linear(a5ell, Q4, rel_q4, a, "caseB clear q4")
    # The reverse lift cancels the rs2 and ez3 assumption multipliers
    # identically, so those two reviewed field-point eliminations are not
    # needed in the constructive certificate.
    if labels["rs2"] in a6ell.terms or labels["ez3"] in a6ell.terms:
        fail("unexpected rs2/ez3 dependence in compact caseB lift")
    a7ell = clear_linear(a6ell, labels["ec3"], rel_ec3,
                         a, "caseB clear ec3")
    if labels["ee1"] in a7ell.terms:
        fail("unexpected ee1 dependence after compact ec3 lift")
    assert_target("caseB monomial", a7ell,
                  p.multiply(p.power(a, 7), ell))
    a15_case = clear_power(
        a1_certificate, labels["ell1"], 1, a7ell, p.power(a, 7),
        "caseB clear ell1 with A1",
    )
    assert_target("caseB a15", a15_case, p.power(a, 15))

    # In rs1=0, split ell1 versus cs1 using the reviewed combined row.
    combined = cert_add(
        row_certificate("Tg14_3", B),
        cert_multiply(row_certificate("Tg13_1", B), p.scale(ell, Fraction(1, 2))),
    )
    combined_rs0 = specialize_cert(combined, "rs1", zero, labels["rs1"])
    rel_ell_cs = cert_scale(combined_rs0, Fraction(8, 3))
    assert_target("rs1=0 a2*ell*cs1", rel_ell_cs,
                  p.multiply(p.power(a, 2), ell, cs))
    a25_mod_rs = combine_branches(
        a1_certificate, labels["ell1"], a15_case, labels["cs1"],
        rel_ell_cs, p.power(a, 2), "rs1 branch ell1-cs1 split",
    )
    assert_target("a25 modulo rs1", a25_mod_rs, p.power(a, 25))

    rel_ell_rs = cert_scale(row_certificate("Tg14_4", B), Fraction(32, 3))
    assert_target("a2*ell*rs1", rel_ell_rs,
                  p.multiply(p.power(a, 2), ell, rs))
    a45_mod_B = combine_branches(
        a18_mod_ell, labels["ell1"], a25_mod_rs, labels["rs1"],
        rel_ell_rs, p.power(a, 2), "base ell1-rs1 split",
    )
    assert_target("a45 modulo e0,e1,ee0", a45_mod_B, p.power(a, 45))

    # Clear ee0 on the e1=0 branch.
    e0e1 = specs_zero(["e0", "e1"])
    rel_ee0 = cert_scale(row_certificate("Tg12_1", e0e1), Fraction(8, 3))
    assert_target("a*ee0", rel_ee0, p.multiply(a, p.variable("ee0")))
    a46_mod_e0e1 = clear_linear(
        a45_mod_B, labels["ee0"], rel_ee0, a, "clear ee0"
    )
    assert_target("a46 modulo e0,e1", a46_mod_e0e1, p.power(a, 46))

    # The second e1 branch first clears ell1^3, then q=ee0+4aa0ell1.
    e0_g_q_specs = [
        ("e0", zero, labels["e0"]),
        ("e1", p.scale(p.multiply(a, ell), 4), G),
    ]
    rel_q0 = cert_scale(row_certificate("Tg12_1", e0_g_q_specs), Fraction(8, 3))
    assert_target("a*q0", rel_q0, p.multiply(a, generators[Q0]))
    rel_ell3 = cert_scale(row_certificate(
        "Tg13_4",
        e0_g_q_specs + [("ee0", p.scale(p.multiply(aa, ell), -4), Q0)],
    ), Fraction(-2, 3))
    assert_target("a2*ell3", rel_ell3,
                  p.multiply(p.power(a, 2), p.power(ell, 3)))
    a56_mod_e0gq = clear_power(
        a18_mod_ell, labels["ell1"], 3, rel_ell3, p.power(a, 2),
        "second e1 branch clear ell1^3",
    )
    assert_target("a56 modulo e0,g,q0", a56_mod_e0gq, p.power(a, 56))
    a57_mod_e0g = clear_linear(
        a56_mod_e0gq, Q0, rel_q0, a, "second e1 branch clear q0"
    )
    assert_target("a57 modulo e0,g", a57_mod_e0g, p.power(a, 57))

    rel_e1_split = cert_scale(
        row_certificate("Tg12_2", [("e0", zero, labels["e0"])]),
        Fraction(32, 3),
    )
    assert_target("e1 split", rel_e1_split,
                  p.multiply(p.variable("e1"), generators[G]))
    a103_mod_e0 = combine_branches(
        a46_mod_e0e1, labels["e1"], a57_mod_e0g, G,
        rel_e1_split, one, "e1 versus e1-4aell split",
    )
    assert_target("a103 modulo e0", a103_mod_e0, p.power(a, 103))

    rel_e0 = cert_scale(row_certificate("Tg11_1", []), Fraction(8, 3))
    assert_target("a*e0", rel_e0, p.multiply(a, p.variable("e0")))
    final = clear_linear(a103_mod_e0, labels["e0"], rel_e0, a, "clear e0")
    assert_target("global a104", final, p.power(a, 104))
    surviving_assumptions = sorted(set(final.terms) & set(assumption_polynomials))
    if surviving_assumptions:
        fail(("assumptions survived", surviving_assumptions))
    if any(exponent < 0 for multiplier in final.terms.values()
           for monomial in multiplier for _, exponent in monomial):
        fail("negative exponent in final multipliers")

    # Actual row-data mutation: alter one frozen Tg19_7 coefficient while
    # holding the banked multipliers fixed.  This is not a target tautology.
    if "Tg19_7" not in final.terms or not final.terms["Tg19_7"]:
        fail("Tg19_7 absent from final certificate")
    mutated_row = dict(rows["Tg19_7"])
    mutated_monomial = sorted(mutated_row)[0]
    mutated_row[mutated_monomial] += 1
    mutation_residual = residual(final, {"Tg19_7": mutated_row})
    if not mutation_residual:
        fail("row-data mutation undetected")

    raw_terms = {name: multiplier for name, multiplier in final.terms.items()
                 if multiplier}
    certificate_record = {
        "target": p.encoded_polynomial(final.target),
        "row_multipliers": {
            name: p.encoded_polynomial(multiplier)
            for name, multiplier in sorted(raw_terms.items())
        },
    }
    certificate_path = output / "a1_104_raw_rho0_certificate.json"
    certificate_path.write_text(json.dumps(certificate_record, sort_keys=True,
                                           separators=(",", ":")) + "\n")
    stage_exponents = {
        "A1_branch": 8,
        "ell1_zero_via_stronger_A2": 18,
        "caseB_terminal_monomial_a_power": 7,
        "caseB_terminal_monomial_ell_power": 1,
        "caseB_pure": 15,
        "rs1_zero": 25,
        "base_e0_e1_ee0_zero": 45,
        "e1_zero": 46,
        "second_e1_branch": 57,
        "e0_zero": 103,
        "global": 104,
    }
    result = {
        "status": "PASS-A1-RHO0-RAW-CONSTRUCTIVE-CASCADE-A1-104",
        "scope": "all 70 frozen raw ordered-a1 rho-zero rows through grade 19 over Q",
        "conclusion": "a1^104 belongs to the unspecialized frozen rho-zero raw ideal",
        "registered_aws_lane": registered_tag,
        "v42_replay_sha256": V42_SHA256,
        "v42_report_sha256": PINS[next(path for path in PINS if path.name.endswith("sol-20260827.md"))],
        "named_row_count": len(rows),
        "frozen_row_file_count": len(row_hashes),
        "row_sha256": row_hashes,
        "stage_exponents": stage_exponents,
        "certificate_sha256": digest(certificate_path),
        "nonzero_row_multiplier_count": len(raw_terms),
        "row_multiplier_term_counts": {name: len(multiplier)
                                        for name, multiplier in sorted(raw_terms.items())},
        "total_multiplier_terms": sum(len(multiplier) for multiplier in raw_terms.values()),
        "mutation": {
            "row": "Tg19_7",
            "changed_source_monomial": [[name, exponent]
                                         for name, exponent in mutated_monomial],
            "residual_term_count": len(mutation_residual),
            "residual_sha256": p.polynomial_hash(mutation_residual),
        },
        "firewalls": [
            "rho was specialized to zero in the frozen source rows",
            "raw-row ideal only; no saturated-Rees or Gate-T comparison",
            "no unspecialized-rho certificate follows from this identity alone",
        ],
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-RAW-CONSTRUCTIVE-CASCADE-A1-104")
    print("CERTIFICATE_SHA256=" + digest(certificate_path))
    print("RESULT_SHA256=" + digest(result_path))
    print("TOTAL_MULTIPLIER_TERMS=" + str(result["total_multiplier_terms"]))


if __name__ == "__main__":
    main()
