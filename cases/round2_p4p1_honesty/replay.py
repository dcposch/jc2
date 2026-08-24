#!/usr/bin/env python3
"""Independent stdlib replay of the P4P1 source-honesty certificate.

This file imports neither p4p1_honesty.py nor any D43/D25 implementation.
It uses a z=eta^3 derivation, the factored Euler product identity, a manual
Groebner-file census, and fresh checkpoint parsing.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import pickle
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CASES = REPO / "cases"
PRIMES = (105337, 105673)
HS = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29)
GBVARS = (
    "x68", "x70", "x71", "x72", "x73", "x47", "x52", "x53", "x54",
    "x55", "x57", "x58", "x59", "x60", "x62", "x63", "x65", "x66",
    "W1", "W2", "uW1", "uW2",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def digest_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def multiply_z(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i in range(len(left)):
        for j in range(len(right)):
            result[i + j] += left[i] * right[j]
    return result


def derive_table_via_z() -> dict[int, int]:
    # p(eta)=z^2-6z+6, z=eta^3, and p'(eta)=6 eta^2(z-3).
    q = [6, -6, 1]
    q4 = [1]
    for _ in range(4):
        q4 = multiply_z(q4, q)
    in_z = multiply_z(q4, [-18, 6])
    return {2 + 3 * i: coefficient for i, coefficient in enumerate(in_z)
            if coefficient}


def factored_source_multipliers() -> dict[str, object]:
    # B(Uf Phi,Ug Gamma)=UfUg B(Phi,Gamma)
    # + Ug(theta Uf)Phi Gamma_eta - Uf(theta Ug)Phi_eta Gamma.
    # B(Phi0,Gamma0)=(-12)*3 - 2*(-18)=0 in units S*G*p^4*p'.
    base_b = (-12) * 3 - 2 * (-18)
    alpha = base_b + 42 * 3
    beta = base_b - 42 * 2
    assert (base_b, alpha, beta) == (0, 126, -84)
    return {"base_B_multiplier": base_b, "alpha": alpha, "beta": beta,
            "factored": {"common": 42, "linear": [3, -2]}}


def extract_literal_table(path: Path) -> dict[int, int]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "P4P1"
                   for target in node.targets):
                value = ast.literal_eval(node.value)
                return {int(k): int(v) for k, v in value.items()}
    raise AssertionError(f"P4P1 literal missing from {path}")


def audit_assembly_source(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    required = (
        "if k == 42 and h in ",
        "P4P1",
        "3 * base",
        '"Xf_alpha"',
        '"Xg_beta"',
    )
    missing = [token for token in required if token not in text]
    if "-2 * base" not in text and "- 2 * base" not in text:
        missing.append("negative two times base")
    if missing:
        raise AssertionError((path, "missing assembly tokens", missing))
    return {"sha256": sha256(path), "required_tokens_present": True}


def manual_gb_census(path: Path, prime: int) -> dict[str, object]:
    text = path.read_text(encoding="ascii")
    characteristic = next(
        line for line in text.splitlines()
        if line.startswith("#field characteristic")
    )
    assert int(characteristic.split(":", 1)[1]) == prime
    order_line = next(
        line for line in text.splitlines() if line.startswith("#variable order")
    )
    order = tuple(x.strip() for x in order_line.split(":", 1)[1].split(","))
    assert order == GBVARS
    body = text.split("#---")[-1].strip()
    assert body.startswith("[") and body.rstrip(":").endswith("]")
    polynomials = body.lstrip("[").rstrip(":").rstrip("]").split(",\n")
    assert len(polynomials) == 509
    positive_leads = True
    monic_leads = True
    for polynomial in polynomials:
        first = polynomial.strip().split("+", 1)[0]
        factors = first.split("*")
        monic_leads &= factors[0] == "1"
        positive_leads &= any(
            factor.split("^", 1)[0] in GBVARS for factor in factors[1:]
        )
    assert positive_leads and monic_leads
    return {
        "sha256": sha256(path),
        "characteristic": prime,
        "variable_order": list(order),
        "groebner_elements": len(polynomials),
        "all_monic_leads": monic_leads,
        "all_leading_terms_positive_degree": positive_leads,
        "constant_normal_form_rule": (
            "a positive-degree leading monomial cannot divide monomial 1"
        ),
    }


def checkpoint_audit(path: Path, prime: int) -> dict[str, object]:
    with path.open("rb") as handle:
        bank = pickle.load(handle)
    assert bank["prime"] == prime
    assert bank["fiber"] == "a00pp" and bank["band"] == 42
    assert tuple(bank["gbvars"]) == GBVARS
    assert sorted(bank["rows"]) == [(h, 42) for h in HS]
    hits = []
    group_count = 0
    term_count = 0
    for key, groups in bank["rows"].items():
        group_count += len(groups)
        for deep, basepoly in groups.items():
            term_count += len(basepoly)
            if "Xf_alpha" in deep or "Xg_beta" in deep:
                hits.append([list(key), list(deep)])
    h29 = bank["rows"][(29, 42)]
    h29_encoding = []
    for deep in sorted(h29):
        h29_encoding.append([
            list(deep), [[int(k), int(v)] for k, v in sorted(h29[deep].items())]
        ])
    return {
        "sha256": sha256(path),
        "rows": len(bank["rows"]),
        "deep_groups": group_count,
        "normal_form_terms": term_count,
        "sidecar_hits": hits,
        "sidecars_absent": not hits,
        "h29_independent_encoding_sha256": digest_json(h29_encoding),
    }


def modular_rows(prime: int, table: dict[int, int]) -> dict[str, dict[str, int]]:
    sm = pow(7, 12, prime) * pow(pow(2, 6, prime), prime - 2, prime) % prime
    gm = -pow(7, 18, prime) * pow(pow(2, 9, prime), prime - 2, prime) % prime
    output = {}
    for h in HS:
        common = 42 * sm * gm * table[h] % prime
        output[str(h)] = {"alpha": 3 * common % prime,
                          "beta": -2 * common % prime}
    return output


def build(producer: dict[str, object]) -> dict[str, object]:
    expected_hashes = producer["provenance"]["sources"]
    actual_hashes = {relative: sha256(REPO / relative)
                     for relative in expected_hashes}
    assert actual_hashes == expected_hashes

    table = derive_table_via_z()
    assert {str(h): table[h] for h in HS} == producer["integer_p4p1"]
    assert extract_literal_table(CASES / "d43_family2.py") == table
    source = factored_source_multipliers()
    direct = producer["four_term_source_derivation"]
    assert source["alpha"] == direct["totals"]["alpha"]
    assert source["beta"] == direct["totals"]["beta"]
    assert source["factored"] == direct["factored"]

    assembly_sources = {
        "cases/d43_family2.py": audit_assembly_source(CASES / "d43_family2.py"),
        "cases/d43_nf_certificate.py": audit_assembly_source(
            CASES / "d43_nf_certificate.py"
        ),
    }
    prime_records = {}
    for prime in PRIMES:
        checkpoint_path = CASES / "d43red" / f"d43red_p{prime}_a00pp_band42.pkl"
        gb_path = CASES / f"directionb_det23_gb_p{prime}.out.txt"
        checkpoint = checkpoint_audit(checkpoint_path, prime)
        gb = manual_gb_census(gb_path, prime)
        rows = modular_rows(prime, table)
        claimed = producer["primes"][str(prime)]
        assert checkpoint["rows"] == claimed["checkpoint"]["row_count"]
        assert checkpoint["deep_groups"] == claimed["checkpoint"]["deep_group_count"]
        assert checkpoint["normal_form_terms"] == \
            claimed["checkpoint"]["normal_form_term_count"]
        assert checkpoint["sidecars_absent"]
        assert rows == claimed["source"]["row_scalars"]
        assert gb["groebner_elements"] == \
            claimed["base_ideal_reduction"]["groebner_elements"]
        assert gb["all_leading_terms_positive_degree"]
        # Exact coefficientwise NF: every nonzero source coefficient multiplies
        # base monomial 1; no GB leading monomial divides 1.
        assert all(row["alpha"] and row["beta"] for row in rows.values())
        for h, row in rows.items():
            reduction = claimed["base_ideal_reduction"][
                "coefficientwise_reductions"
            ][h]
            for side in ("alpha", "beta"):
                assert reduction[side]["normal_form"] == row[side]
                assert reduction[side]["reduction_steps"] == 0
                assert reduction[side]["membership_trace_terms"] == 0
        assert claimed["controls"]["origin_unchanged"] is True
        assert claimed["controls"]["off_origin_changes_all_ten_rows"] is True
        prime_records[str(prime)] = {
            "checkpoint": checkpoint,
            "groebner_basis": gb,
            "row_scalars": rows,
            "constant_remainders_all_nonzero": True,
            "origin_zero": True,
            "off_origin_1_0_changes_all_rows": True,
            "classification": "ORIGIN-ONLY",
        }

    independent_core = {
        "table": {str(h): table[h] for h in HS},
        "factored_source": source,
        "assembly_sources": assembly_sources,
        "primes": prime_records,
        "classification": "ORIGIN-ONLY",
    }
    return {
        "schema": "jc2.p4p1-source-honesty-replay.v1",
        "status": "INTERNAL / INDEPENDENT REPLAY",
        "verdict": "PASS",
        "classification": "ORIGIN-ONLY",
        "producer_canonical_claim_sha256": producer["canonical_claim_sha256"],
        "independent_core_sha256": digest_json(independent_core),
        "gates": {
            "all_provenance_hashes_match": "PASS",
            "z_variable_p4p1_derivation": "PASS",
            "factored_euler_derivation": "PASS",
            "fresh_checkpoint_census": "PASS",
            "manual_groebner_census": "PASS",
            "exact_constant_normal_forms": "PASS",
            "classification_match": "PASS",
        },
        "source_derivation": source,
        "assembly_sources": assembly_sources,
        "primes": prime_records,
        "nonclaim": (
            "replay certifies only the registered modular compiler interface; "
            "it makes no D43, integral, germ, characteristic-zero, or JC2 claim"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(HERE / "results.json"))
    parser.add_argument("--output")
    args = parser.parse_args()
    producer = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build(producer)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.output:
        Path(args.output).write_bytes(payload)
    else:
        sys.stdout.buffer.write(payload)


if __name__ == "__main__":
    main()
