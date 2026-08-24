#!/usr/bin/env python3
"""Exact, read-only replay for WEIGHTED-D-SOURCE-GATE-20260824.

The script hashes the frozen producer perimeter, inventories the typed source
interfaces, and verifies the universal q=t^42 coefficient algebra through
q^2.  It never treats the formal alpha/beta variables as a producer-owned
source tangent.  It writes nothing; --expected checks a frozen JSON artifact.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, Tuple


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]

EXPECTED_SOURCES = {
    "xmodel/ideation-20260824T0453Z-synthesis.md":
        "76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790",
    "xmodel/sol-xside-spec.md":
        "f946a4ae65965200d5138b6a213945f1a3be6076fa8da1bfac9d4ba24381d9ff",
    "ladder/SHEET6-DIRECTIONB.md":
        "1b26369fdadfa41c7c575b9106d386d2bad182d7e0b91f7a0a604dac8ad3cdef",
    "ladder/SHEET6-DIRECTIONB-REVIEW.md":
        "5da561d3faf834cdb3acc764b3a4c4fba4150832886b50c1279b183a3e096a18",
    "ladder/SHEET6-R1.md":
        "ad63701bc1614dfd53edf99ade0e5c1743ceada3c9a9cdac38ef29a5e9701fe9",
    "cases/valuation_e2.py":
        "c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8",
    "cases/round2_dstate_gate/PREREGISTRATION.md":
        "e34d1b090dcf4447bc735f9b289e445a87b1168eeb5a70678f0f8d03348b98ab",
    "cases/round2_dstate_gate/provenance.json":
        "7cb56a470ffa437f7afda684f07ebeb71a4d2a85ad80068670ffb673e535dbdc",
    "cases/round2_dstate_gate/dstate_gate.py":
        "d312c84bfe601e667c74b2453ef09287d5b2dd9796e4201d57b6b364debae309",
    "cases/round2_dstate_gate/results.json":
        "4ca07ad9c922acec962b508e857d69c5db7ae336c3f0723837e2a0799d6f225f",
    "cases/round2_dstate_gate/replay.py":
        "770fc71405d2d5c819508451c454af7f59a25c46867934af9e302603e15f232a",
    "cases/round2_dstate_gate/replay.json":
        "7a0e534563085950a90fd0a54da9f63f541713d212bf412485ee7c4ab365f72c",
    "cases/round2_dstate_gate/MANIFEST.sha256":
        "725edba2f34a20bcd4a062ac97baf0924000c84efccab38dbb1565b3fefbaa99",
    "xmodel/round2-dstate-gate-20260824.md":
        "57536d0557d4aaaf267ce493c3236b33eed1c1d2829484e496211934ea78d512",
    "xmodel/review-dstate-grok.md":
        "b4a0fec6d4aa0e21ccaf325c8ad12b78c426b131698903500c018393251426dc",
    "cases/eplus43.py":
        "94db6c25df5254a040522b7bd5afe38f19577c267c8e61f57b05d3b0dfd3fe1c",
    "cases/d43_family2.py":
        "8c0f7fd3ea1efb54293036e1caa481519682251ec554e8dac4cb254b4f2ca013",
    "cases/d43_nf_certificate.py":
        "41865448d3de9d0d47a9c0d086a343ea7a46b00688699d2e8b304adb0be5945b",
    "cases/round2_p4p1_honesty/PREREGISTRATION.md":
        "ea4593958acfddb66366a32d45693329052f24ae99d71cc26d43ad3fcf68f4e6",
    "cases/round2_p4p1_honesty/provenance.json":
        "87d0e620f5c4275f9c6f5b8f5d559601066d8520e99d3e4bd6a0d804dbed50b5",
    "cases/round2_p4p1_honesty/p4p1_honesty.py":
        "c8d0c688f0bbe7ae1f47b6777c93db914df7835dd6c1eb6ee2c131662a49fb1f",
    "cases/round2_p4p1_honesty/results.json":
        "d0123adb31a1ee7aead8c7b5b0899fc68094a87700bbdff69867514f2efd002c",
    "cases/round2_p4p1_honesty/MANIFEST.sha256":
        "fef9eae832f53634e4cb29e8b850ba79d28f326688fab919787dc1ad1aeb10c2",
    "xmodel/round2-p4p1-honesty-20260824.md":
        "c744c983c41055f45a509b0764b60d07312d5b172ef162183fa4342b7be1042f",
    "xmodel/review-p4p1-honesty-grok.md":
        "64a64c29493c46f86e05657457666b02ecab053cfe2e025ca914e6eb7af14d6e",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


VARS = (
    "a1", "a2", "b1", "b2", "r1", "r2", "c1", "c2",
    "B1", "B2", "A0", "A1", "D1",
)
ZERO_EXP = (0,) * len(VARS)


class Poly:
    """Tiny integral polynomial ring, sufficient for the exact replay."""

    def __init__(self, terms: Dict[Tuple[int, ...], int] | None = None):
        self.terms = {m: int(c) for m, c in (terms or {}).items() if c}

    @classmethod
    def constant(cls, value: int) -> "Poly":
        return cls({ZERO_EXP: value})

    @classmethod
    def variable(cls, name: str) -> "Poly":
        exponent = [0] * len(VARS)
        exponent[VARS.index(name)] = 1
        return cls({tuple(exponent): 1})

    def __add__(self, other: "Poly" | int) -> "Poly":
        other = other if isinstance(other, Poly) else Poly.constant(other)
        terms = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            terms[monomial] = terms.get(monomial, 0) + coefficient
            if not terms[monomial]:
                del terms[monomial]
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: "Poly" | int) -> "Poly":
        return self + (-other if isinstance(other, Poly) else -other)

    def __rsub__(self, other: "Poly" | int) -> "Poly":
        return (other if isinstance(other, Poly) else Poly.constant(other)) - self

    def __mul__(self, other: "Poly" | int) -> "Poly":
        other = other if isinstance(other, Poly) else Poly.constant(other)
        terms: Dict[Tuple[int, ...], int] = {}
        for left, lc in self.terms.items():
            for right, rc in other.terms.items():
                monomial = tuple(a + b for a, b in zip(left, right))
                terms[monomial] = terms.get(monomial, 0) + lc * rc
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, power: int) -> "Poly":
        assert power >= 0
        result = Poly.constant(1)
        factor = self
        while power:
            if power & 1:
                result = result * factor
            factor = factor * factor
            power //= 2
        return result

    def derivative(self, name: str) -> "Poly":
        index = VARS.index(name)
        terms = {}
        for monomial, coefficient in self.terms.items():
            if monomial[index]:
                exponent = list(monomial)
                terms[tuple(exponent[:index] + [exponent[index] - 1] +
                            exponent[index + 1:])] = coefficient * monomial[index]
        return Poly(terms)

    def canonical(self) -> list[list[object]]:
        return [[list(monomial), coefficient]
                for monomial, coefficient in sorted(self.terms.items())]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            other = Poly.constant(other)
        return isinstance(other, Poly) and self.terms == other.terms


def var(name: str) -> Poly:
    return Poly.variable(name)


def s_add(left: list[Poly], right: list[Poly]) -> list[Poly]:
    return [a + b for a, b in zip(left, right)]


def s_mul(left: list[Poly], right: list[Poly]) -> list[Poly]:
    degree = len(left) - 1
    out = [Poly.constant(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] = out[i + j] + a * b
    return out


def s_pow(series: list[Poly], power: int) -> list[Poly]:
    result = [Poly.constant(1)] + [Poly.constant(0)] * (len(series) - 1)
    for _ in range(power):
        result = s_mul(result, series)
    return result


def s_inv(series: list[Poly]) -> list[Poly]:
    assert series[0] == 1
    out = [Poly.constant(1)]
    for n in range(1, len(series)):
        coefficient = Poly.constant(0)
        for i in range(1, n + 1):
            coefficient = coefficient + series[i] * out[n - i]
        out.append(-coefficient)
    return out


def s_theta(series: list[Poly]) -> list[Poly]:
    return [Poly.constant(0)] + [42 * n * series[n]
                                for n in range(1, len(series))]


def formula_replay() -> dict[str, object]:
    a1, a2, b1, b2 = (var(name) for name in ("a1", "a2", "b1", "b2"))
    uf = [Poly.constant(1), a1, a2]
    ug = [Poly.constant(1), b1, b2]
    c = s_mul(ug, s_inv(uf))
    r = s_mul(s_pow(uf, 3), s_pow(s_inv(ug), 2))
    expected_c1 = b1 - a1
    expected_c2 = b2 - a2 + a1 ** 2 - a1 * b1
    expected_r1 = 3 * a1 - 2 * b1
    expected_r2 = 3 * a2 - 2 * b2 + 3 * (a1 - b1) ** 2
    assert c[1] == expected_c1 and c[2] == expected_c2
    assert r[1] == expected_r1 and r[2] == expected_r2
    assert s_mul(r, s_pow(c, 2)) == uf
    assert s_mul(r, s_pow(c, 3)) == ug

    r1, r2, c1, c2 = (var(name) for name in ("r1", "r2", "c1", "c2"))
    R = [Poly.constant(1), r1, r2]
    C = [Poly.constant(1), c1, c2]
    B = [Poly.constant(0), var("B1"), var("B2")]
    A = [var("A0"), var("A1"), Poly.constant(0)]
    D = [Poly.constant(0), var("D1"), Poly.constant(0)]
    # Exact weighted form of the unreduced product identity:
    # R^2 C^5 B + R C^5 theta(R) A + R^2 C^4 theta(C) D.
    full = s_add(
        s_add(s_mul(s_mul(s_pow(R, 2), s_pow(C, 5)), B),
              s_mul(s_mul(s_mul(R, s_pow(C, 5)), s_theta(R)), A)),
        s_mul(s_mul(s_mul(s_pow(R, 2), s_pow(C, 4)), s_theta(C)), D),
    )
    expected_e1 = var("B1") + 42 * r1 * var("A0")
    H = 84 * r2 + 42 * r1 * (r1 + 5 * c1)
    expected_e2 = (
        var("B2") + (2 * r1 + 5 * c1) * var("B1")
        + 42 * r1 * var("A1") + H * var("A0")
        + 42 * c1 * var("D1")
    )
    assert full[1] == expected_e1 and full[2] == expected_e2

    chain = {
        "c1": expected_c1,
        "c2": expected_c2,
        "r1": expected_r1,
        "r2": expected_r2,
        "E42": expected_e1,
        "E84": expected_e2,
    }
    jacobian = {
        label: {name: polynomial.derivative(name).canonical()
                for name in VARS if polynomial.derivative(name).terms}
        for label, polynomial in chain.items()
    }
    canonical = {name: polynomial.canonical() for name, polynomial in chain.items()}
    formula_hash = hashlib.sha256(
        json.dumps({"formulas": canonical, "jacobian": jacobian},
                   sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "change_of_coordinates": {
            "c1": "beta_1-alpha_1",
            "c2": "beta_2-alpha_2+alpha_1^2-alpha_1*beta_1",
            "r1": "3*alpha_1-2*beta_1",
            "r2": "3*alpha_2-2*beta_2+3*(alpha_1-beta_1)^2",
            "inverse_checked_through_q2": True,
        },
        "unreduced_weighted_identity": (
            "R^2*C^5*B_y + R*C^5*theta(R)*A "
            "+ R^2*C^4*theta(C)*D"
        ),
        "definitions": {
            "A": "Phi_y*Gamma_y,eta-Phi_y,eta*Gamma_y",
            "D": "2*Phi_y*Gamma_y,eta-3*Phi_y,eta*Gamma_y",
            "B0": "0", "D0": "0",
            "A0": "S_M*G_M*p(eta)^4*p'(eta)",
        },
        "level_42": "B42+42*r1*A0",
        "level_84": (
            "B84+(2*r1+5*c1)*B42+42*r1*A42+"
            "(84*r2+42*r1*(r1+5*c1))*A0+42*c1*D42"
        ),
        "formal_formula_sha256": formula_hash,
        "all_formal_jacobian_terms_checked": True,
        "interpretation": (
            "r1 is the only weighted x coefficient at level 42; level 84 "
            "contains r2 and the older carrier tangent c1, while c2 cancels "
            "because B0=D0=0"
        ),
    }


def build_result() -> dict[str, object]:
    hashes = {name: sha256(REPO / name) for name in EXPECTED_SOURCES}
    assert hashes == EXPECTED_SOURCES

    dstate = json.loads((REPO / "cases/round2_dstate_gate/results.json")
                        .read_text(encoding="utf-8"))
    interface = dstate["full_source_interface"]
    assert dstate["verdict"] == "NO-TYPED-STATIONARITY"
    assert interface["alpha_beta_classification"] is None
    assert interface["typed_shift_projection_map_present"] is False
    assert interface["registered_y_stream_contains_alpha_beta"] is False
    assert interface["registered_y_stream_count"] == 30

    valuation_text = (REPO / "cases/valuation_e2.py").read_text(encoding="utf-8")
    tree = ast.parse(valuation_text)
    build = next(node for node in tree.body
                 if isinstance(node, ast.FunctionDef) and node.name == "build_jets")
    build_args = [argument.arg for argument in build.args.args]
    assert build_args == ["point", "p", "Z"]

    spec = (REPO / "xmodel/sol-xside-spec.md").read_text(encoding="utf-8")
    for marker in (
        "CONJECTURE X-SIDE-DERIVATION", "CONJECTURE X-SIDE-30",
        "numerical value of the two level-42 x-factor coefficients",
        "alpha_m&=\\frac{c_{f,42-m}}{c_f}",
        "beta_m&=\\frac{c_{g,63-m}}{c_g}",
    ):
        assert marker in spec

    r1_text = (REPO / "ladder/SHEET6-R1.md").read_text(encoding="utf-8")
    assert "Next-tier spec: the R2 window build" in r1_text
    assert "future sec 17" in r1_text

    eplus = (REPO / "cases/eplus43.py").read_text(encoding="utf-8")
    for marker in (
        "repository value or derivation of (alpha, beta) exists",
        "declared INDEPENDENT filtered tangent coordinates",
        "NAMED finite-support completion alpha = beta = 0",
        "U_f = 1 + alpha t^42 + O(t^84)",
    ):
        assert marker in eplus
    assert "Xf_alpha2" not in eplus and "Xg_beta2" not in eplus

    family = (REPO / "cases/d43_family2.py").read_text(encoding="utf-8")
    nf = (REPO / "cases/d43_nf_certificate.py").read_text(encoding="utf-8")
    assert "adjoined with alpha, beta as independent variables" in family
    assert 'groups[("Xf_alpha",)]' in nf and 'groups[("Xg_beta",)]' in nf

    p4 = json.loads((REPO / "cases/round2_p4p1_honesty/results.json")
                    .read_text(encoding="utf-8"))
    assert p4["verdict"] == "ORIGIN-ONLY"
    for prime in ("105337", "105673"):
        record = p4["primes"][prime]
        assert record["checkpoint"]["sidecars_absent"] is True
        assert record["checkpoint"]["sidecar_occurrences"] == []
        assert record["base_ideal_reduction"]["external_variables"] == [
            "Xf_alpha", "Xg_beta"]

    prereg_hash = sha256(HERE / "PREREGISTRATION.md")
    result = {
        "schema_version": 1,
        "gate": "WEIGHTED-D-SOURCE-GATE-20260824",
        "basis": "dd11599b07eb05591b5c006791005eef19457d8e",
        "verdict": "NO-TYPED-SOURCE/NO-QUOTIENT",
        "first_stop": (
            "the promoted constructor and reviewed D-state artifact provide "
            "no named full-source tangent map even for alpha_1,beta_1; the "
            "factor-level-two alpha_2,beta_2 occur only in the implementation "
            "specification and have no producer registry, completion values, "
            "or chain rule"
        ),
        "preregistration_sha256": prereg_hash,
        "source_hashes": hashes,
        "producer_inventory": {
            "normalized_factor_definition": (
                "alpha_m=c_f,42-m/c_f (m=1..42); "
                "beta_m=c_g,63-m/c_g (m=1..63)"
            ),
            "pure_y_build_jets_signature": "(" + ", ".join(build_args) + ")",
            "pure_y_streams": 30,
            "pure_y_contains_x_factor_labels": False,
            "promoted_alpha_beta_classification": None,
            "promoted_shift_projection_map": False,
            "p4p1_sidecars": "external variables; absent from both checkpoints",
            "eplus43_status": (
                "internal/unreviewed constructor choice: independent alpha,beta "
                "with named zero values; explicitly not a source derivation"
            ),
            "factor_level_two_implementation_registry": None,
            "r2_xside_model": "future work",
        },
        "formal_identity_replay": formula_replay(),
        "source_tangent_instantiated": False,
        "quotient_covariance_proved": False,
        "two_driver_test_licensed": False,
        "hankel_test_licensed": False,
        "recurrence_test_licensed": False,
        "forbidden_work_entered": [],
    }
    core = dict(result)
    result["core_sha256"] = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", type=Path)
    args = parser.parse_args()
    result = build_result()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.expected:
        expected = args.expected.read_text(encoding="utf-8")
        if expected != encoded:
            raise SystemExit("frozen result differs from exact replay")
        print("PASS", result["verdict"], result["core_sha256"])
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
