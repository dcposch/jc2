#!/usr/bin/env python3
"""Exact-Q reconstruction of a replayed V24 modular unit certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / "aws_r6b_pass/output/modular_prior_reduction_v24.sing"
R4A = HERE / "aws_box02_r4a_modcerts/output"
R4A_RESULT = R4A / "RESULT.json"
PREREG = HERE / "PREREGISTRATION_R4B_EXACT_RECONSTRUCTION.md"
PRIMES = (1000003, 2147483629, 2147483587, 2147483579,
          2147483563, 2147483549, 2147483543, 2147483497)
EXPECTED = {
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    PREREG: "0a94e00d01ab72a056f9f633135a1a7fd1d0a42de3987bb424fb286aacea6aa0",
    R4A_RESULT: "TO_BE_FROZEN_AFTER_R4A",
}


class ReconstructionFailure(RuntimeError):
    """A theorem-ineligible reconstruction endpoint."""


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R4B compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R4B compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def crt(residues: list[int], primes: tuple[int, ...]) -> tuple[int, int]:
    value, modulus = 0, 1
    for residue, prime in zip(residues, primes):
        step = ((residue - value) % prime) * pow(modulus, -1, prime) % prime
        value += step * modulus
        modulus *= prime
    return value, modulus


def rational_reconstruct(value: int, modulus: int) -> Fraction:
    """Unique symmetric rational reconstruction with bound floor(sqrt(M/2))."""
    value %= modulus
    if value == 0:
        return Fraction(0, 1)
    bound = math.isqrt(modulus // 2)
    r0, r1 = modulus, value
    t0, t1 = 0, 1
    while abs(r1) > bound:
        quotient = r0 // r1
        r0, r1 = r1, r0 - quotient * r1
        t0, t1 = t1, t0 - quotient * t1
    numerator, denominator = r1, t1
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    if denominator == 0 or abs(numerator) > bound or denominator > bound:
        raise ReconstructionFailure(("rational reconstruction bound", value,
                                     modulus, numerator, denominator, bound))
    if math.gcd(numerator, denominator) != 1 or \
            (numerator - value * denominator) % modulus:
        raise ReconstructionFailure(("rational reconstruction replay", value,
                                     modulus, numerator, denominator))
    return Fraction(numerator, denominator)


def strip_outer(text: str) -> str:
    while text.startswith("(") and text.endswith(")"):
        depth = 0
        encloses = True
        for index, char in enumerate(text):
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0 and index != len(text) - 1:
                    encloses = False
                    break
            if depth < 0:
                fail(("unbalanced polynomial", text[:120]))
        if not encloses or depth:
            break
        text = text[1:-1]
    return text


def split_top(text: str, separators: str) -> list[tuple[str, str]]:
    """Split at depth-zero separators, retaining the separator for each piece."""
    pieces: list[tuple[str, str]] = []
    depth = 0
    start = 0
    marker = "+"
    for index, char in enumerate(text):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                fail(("unbalanced polynomial", text[:120]))
        elif depth == 0 and char in separators:
            if index > start:
                pieces.append((marker, text[start:index]))
            marker, start = char, index + 1
    if depth:
        fail(("unbalanced polynomial", text[:120]))
    if start < len(text):
        pieces.append((marker, text[start:]))
    return pieces


def parse_sparse(text: str, variables: tuple[str, ...]) \
        -> dict[tuple[int, ...], Fraction]:
    source = "".join(text.split())
    zero = (0,) * len(variables)
    index = {name: place for place, name in enumerate(variables)}
    if source == "0":
        return {}
    if not source or any(char in source for char in ';,"'):
        fail(("malformed exact polynomial", source[:120]))
    result: dict[tuple[int, ...], Fraction] = {}
    for sign, raw_term in split_top(source, "+-"):
        term = strip_outer(raw_term)
        factors = [strip_outer(piece) for _, piece in split_top(term, "*")]
        coefficient = Fraction(-1 if sign == "-" else 1, 1)
        exponent = [0] * len(variables)
        for factor in factors:
            match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?", factor)
            if match and match.group(1) in index:
                exponent[index[match.group(1)]] += int(match.group(2) or "1")
                continue
            if re.fullmatch(r"[+-]?\d+(?:/\d+)?", factor):
                coefficient *= Fraction(factor)
                continue
            fail(("unsupported exact polynomial factor", factor[:120]))
        key = tuple(exponent)
        result[key] = result.get(key, Fraction(0)) + coefficient
        if not result[key]:
            del result[key]
    return result


def sparse_mul(left: dict[tuple[int, ...], Fraction],
               right: dict[tuple[int, ...], Fraction]) \
        -> dict[tuple[int, ...], Fraction]:
    result: dict[tuple[int, ...], Fraction] = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            result[key] = result.get(key, Fraction(0)) + avalue * bvalue
            if not result[key]:
                del result[key]
    return result


def sparse_add_into(target: dict[tuple[int, ...], Fraction],
                    source: dict[tuple[int, ...], Fraction]) -> None:
    for key, value in source.items():
        target[key] = target.get(key, Fraction(0)) + value
        if not target[key]:
            del target[key]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def polynomial_text(poly: dict[tuple[int, ...], Fraction],
                    variables: tuple[str, ...]) -> str:
    if not poly:
        return "0"
    terms = []
    for exponent, coefficient in sorted(poly.items()):
        monomial = "*".join(
            variable if power == 1 else f"{variable}^{power}"
            for variable, power in zip(variables, exponent) if power)
        terms.append(f"({fraction_text(coefficient)})" +
                     (f"*{monomial}" if monomial else ""))
    return "+".join(terms)


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def run_singular(singular: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int = 1200) -> str:
    try:
        completed = subprocess.run([singular, "-q", str(script)],
                                   cwd=script.parent, text=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        stdout.write_text(error.stdout or "")
        stderr.write_text(error.stderr or "")
        raise ReconstructionFailure("exact replay resource cap") from error
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode or completed.stderr or "R4B_FAIL=" in completed.stdout:
        fail(("exact Singular replay failed", completed.returncode,
              completed.stderr[-2000:], completed.stdout[-3000:]))
    return completed.stdout


def emit_no_verdict(output: Path, tag: str, reason: object) -> None:
    payload = {
        "status": "RATIONAL_RECONSTRUCTION_OR_REPLAY_FAILURE",
        "registered_aws_lane": tag,
        "reason": repr(reason),
        "scope": "NO_EXACT_Q_IDENTITY_NO_CHART_VERDICT",
        "firewall": "NO_W_ZERO_NO_STRATUM_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R4B=RATIONAL_RECONSTRUCTION_OR_REPLAY_FAILURE")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if wanted.startswith("TO_BE_FROZEN") or got != wanted:
            fail(("frozen input mismatch", str(path), got, wanted))
    result = json.loads(R4A_RESULT.read_text())
    if result.get("status") != \
            "PASS_MODULAR_UNIT_CERTIFICATES_STABLE_SUPPORT_READY_FOR_EXACT_LIFT":
        fail(("R4A is not exact-lift eligible", result.get("status")))
    if tuple(result.get("primes", ())) != PRIMES:
        fail("R4A prime order mismatch")
    outcomes = {int(item["prime"]): item for item in result.get("outcomes", [])}
    if tuple(sorted(outcomes)) != tuple(sorted(PRIMES)):
        fail("R4A outcome census mismatch")

    original = ORIGINAL.read_text().splitlines()
    if len(original) != 11 or not original[0].startswith("ring R=65521,"):
        fail("frozen rational source shape mismatch")
    match = re.fullmatch(r"ring R=65521,\(([^)]+)\),dp;", original[0])
    if match is None:
        fail("variable declaration mismatch")
    variables = tuple(match.group(1).split(","))
    if len(variables) != 34 or variables[-1] != "zinv":
        fail("variable census mismatch")

    modular: dict[int, list[list[list[object]]]] = {}
    common_support: list[list[tuple[int, ...]]] | None = None
    for prime in PRIMES:
        outcome = outcomes[prime]
        if outcome.get("status") != "UNIT_CERTIFICATE_REPLAYED":
            fail(("nonreplayed R4A lane", prime, outcome.get("status")))
        path = R4A / f"p{prime}/CERTIFICATE_CANONICAL.json"
        if digest(path) != outcome.get("canonical_certificate_sha256"):
            fail(("R4A certificate hash mismatch", prime))
        entries = json.loads(path.read_text())
        if len(entries) != 36:
            fail(("R4A certificate entry census", prime, len(entries)))
        supports = []
        for entry in entries:
            keys = [tuple(int(value) for value in pair[0]) for pair in entry]
            if any(len(key) != len(variables) for key in keys) or keys != sorted(keys):
                fail(("R4A monomial encoding mismatch", prime))
            supports.append(keys)
        if common_support is None:
            common_support = supports
        elif supports != common_support:
            fail(("R4A common support mismatch", prime))
        modular[prime] = entries
    assert common_support is not None

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    try:
        certificates: list[dict[tuple[int, ...], Fraction]] = []
        modulus = math.prod(PRIMES)
        for entry_index, support in enumerate(common_support):
            certificate: dict[tuple[int, ...], Fraction] = {}
            for term_index, exponent in enumerate(support):
                residues = [int(modular[prime][entry_index][term_index][1]) % prime
                            for prime in PRIMES]
                combined, checked_modulus = crt(residues, PRIMES)
                if checked_modulus != modulus:
                    fail("CRT modulus mismatch")
                value = rational_reconstruct(combined, modulus)
                if any(value.denominator % prime == 0 or
                       value.numerator * pow(value.denominator, -1, prime) % prime
                       != residue for residue, prime in zip(residues, PRIMES)):
                    fail(("reconstructed residue replay", entry_index, exponent))
                if value:
                    certificate[exponent] = value
            if list(certificate) != support:
                raise ReconstructionFailure(("reconstruction erased support",
                                             entry_index))
            certificates.append(certificate)
    except ReconstructionFailure as error:
        emit_no_verdict(output, tag, error)
        return

    exact_json = []
    coefficient_paths = []
    for index, certificate in enumerate(certificates, 1):
        exact_json.append([[list(key), value.numerator, value.denominator]
                           for key, value in sorted(certificate.items())])
        path = output / f"EXACT_CERT_{index:02d}.txt"
        path.write_text(polynomial_text(certificate, variables) + "\n")
        coefficient_paths.append(path)
    exact_json_path = output / "EXACT_Q_CERTIFICATE_CANONICAL.json"
    exact_json_path.write_text(json.dumps(exact_json, separators=(",", ":")) + "\n")

    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    ring_q = original[0].replace("ring R=65521,", "ring R=0,", 1)
    first_nonzero = next((index, key, value)
                         for index, certificate in enumerate(certificates)
                         for key, value in certificate.items())
    mutation_index, mutation_key, mutation_value = first_nonzero
    mutation_term = polynomial_text({mutation_key: mutation_value}, variables)
    replay_script = output / "exact_q_identity_replay.sing"
    replay_lines = [ring_q, original[1], original[2],
                    'if (size(P)!=36) { print("R4B_FAIL=GENERATOR_CENSUS"); quit; }',
                    "matrix C[36][1];"]
    replay_lines.extend(
        f"C[{index},1]={path.read_text().strip()};"
        for index, path in enumerate(coefficient_paths, 1))
    replay_lines.extend([
        "matrix RES=matrix(P)*C-matrix(ideal(1));",
        'if (RES!=0) { print("R4B_FAIL=EXACT_IDENTITY"); quit; }',
        "matrix CDROP=C;",
        f"CDROP[{mutation_index + 1},1]=CDROP[{mutation_index + 1},1]-({mutation_term});",
        'if (matrix(P)*CDROP-matrix(ideal(1))==0) { print("R4B_FAIL=DROP_MUTATION"); quit; }',
        "matrix CCHANGE=C;",
        f"CCHANGE[{mutation_index + 1},1]=CCHANGE[{mutation_index + 1},1]+({mutation_term});",
        'if (matrix(P)*CCHANGE-matrix(ideal(1))==0) { print("R4B_FAIL=CHANGE_MUTATION"); quit; }',
        'print("R4B_EXACT_IDENTITY_REPLAY=1");',
        'print("R4B_SINGULAR_MUTATIONS=1");',
        "quit;",
    ])
    replay_script.write_text("\n".join(replay_lines) + "\n")
    replay_stdout = output / "exact_q_identity_replay.stdout"
    replay_stderr = output / "exact_q_identity_replay.stderr"
    markers = run_singular(singular, replay_script, replay_stdout, replay_stderr)
    if "R4B_EXACT_IDENTITY_REPLAY=1" not in markers or \
            "R4B_SINGULAR_MUTATIONS=1" not in markers:
        fail("missing exact replay markers")

    generator_paths = [output / f"EXACT_GENERATOR_{index:02d}.txt"
                       for index in range(1, 37)]
    source_script = output / "exact_q_generator_serialization.sing"
    source_lines = [ring_q, original[1], original[2],
                    'if (size(P)!=36) { print("R4B_FAIL=GENERATOR_CENSUS"); quit; }']
    source_lines.extend(f'write("{qpath(path)}",P[{index}]);'
                        for index, path in enumerate(generator_paths, 1))
    source_lines.extend(['print("R4B_GENERATORS_SERIALIZED=1");', "quit;"])
    source_script.write_text("\n".join(source_lines) + "\n")
    source_stdout = output / "exact_q_generator_serialization.stdout"
    source_stderr = output / "exact_q_generator_serialization.stderr"
    source_markers = run_singular(singular, source_script, source_stdout,
                                  source_stderr)
    if "R4B_GENERATORS_SERIALIZED=1" not in source_markers or \
            not all(path.is_file() for path in generator_paths):
        fail("generator serialization failed")

    sparse_residual: dict[tuple[int, ...], Fraction] = {
        (0,) * len(variables): Fraction(-1)}
    generators = [parse_sparse(path.read_text(), variables)
                  for path in generator_paths]
    for generator, certificate in zip(generators, certificates):
        sparse_add_into(sparse_residual, sparse_mul(generator, certificate))
    if sparse_residual:
        fail(("independent sparse exact replay nonzero", len(sparse_residual)))
    mutated_piece = sparse_mul(
        generators[mutation_index], {mutation_key: mutation_value})
    if not mutated_piece:
        fail("independent sparse mutation unexpectedly zero")

    all_values = [value for certificate in certificates
                  for value in certificate.values()]
    payload = {
        "status": "PASS_EXACT_Q_LOCALIZED_PRIOR_IDEAL_UNIT_WITH_REPLAYED_36_ENTRY_IDENTITY",
        "registered_aws_lane": tag,
        "field": "Q_exact",
        "generator_count": 36,
        "certificate_entry_count": 36,
        "certificate_term_counts": [len(value) for value in certificates],
        "crt_modulus": str(modulus),
        "rational_reconstruction_bound": str(math.isqrt(modulus // 2)),
        "max_abs_numerator_bits": max(abs(value.numerator).bit_length()
                                      for value in all_values),
        "max_denominator_bits": max(value.denominator.bit_length()
                                for value in all_values),
        "singular_exact_identity_replay": True,
        "independent_sparse_rational_identity_replay": True,
        "drop_and_coefficient_mutations": True,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in ([exact_json_path, replay_script, replay_stdout,
                          replay_stderr, source_script, source_stdout,
                          source_stderr] + coefficient_paths + generator_paths)
        },
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                         for path in EXPECTED},
        "scope": "EXACT_Q_NORMALIZED_VALUATION_ONE_PREFIX_THROUGH_GRADE6_ON_D_K10_0_W",
        "firewall": "NO_W_ZERO_NO_GRADES7TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True,
                                                   indent=2) + "\n")
    print("K00_V24R4B=" + payload["status"])
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
