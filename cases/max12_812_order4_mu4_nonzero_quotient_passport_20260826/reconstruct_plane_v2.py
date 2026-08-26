#!/usr/bin/env python3
"""AWS-only CRT/rational reconstruction of the corrected-V2 plane relation."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pathlib
import platform
import re


PRIMES = (
    32003, 32009, 32027, 32029, 32051, 32057, 32059, 32063,
    32069, 32077, 32083, 32089, 32099, 32117, 32119, 32141,
    32143, 32159, 32173, 32183, 32189, 32191, 32203, 32213,
    32233, 32237, 32251, 32257, 32261, 32297, 32303, 32309,
)
SUPPORT = (
    (2, 21), (4, 18), (6, 15), (8, 12), (10, 9), (12, 6),
    (14, 3), (16, 0), (0, 16), (2, 13), (4, 10), (6, 7),
    (8, 4), (10, 1), (0, 8), (2, 5), (4, 2), (0, 0),
)


def require_aws() -> None:
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered AWS lane tag")


def parse_term(term: str, prime: int) -> tuple[tuple[int, int], int]:
    sign = 1
    if term.startswith("-"):
        sign = -1
        term = term[1:]
    elif term.startswith("+"):
        term = term[1:]
    if not term:
        raise RuntimeError("empty polynomial term")
    coefficient = sign
    powers = {"a5": 0, "a6": 0}
    for factor in term.split("*"):
        if re.fullmatch(r"[0-9]+", factor):
            coefficient *= int(factor)
            continue
        match = re.fullmatch(r"(a5|a6)(?:\^([0-9]+))?", factor)
        if match is None:
            raise RuntimeError(f"unparsed factor {factor!r} in {term!r}")
        powers[match.group(1)] += int(match.group(2) or "1")
    return (powers["a5"], powers["a6"]), coefficient % prime


def parse_output(path: pathlib.Path, prime: int) -> dict[tuple[int, int], int]:
    text = path.read_text(encoding="utf-8")
    required = (
        f"PRIME={prime}", "SAT_UNIT=0", "SAT_DIM=1", "PLANE_SIZE=1",
        "FACTOR_COUNT=1", "PRIME_COMPLETE=PASS",
    )
    for sentinel in required:
        if sentinel not in text:
            raise RuntimeError(f"{path}: missing {sentinel}")
    try:
        body = text.split("PLANE_BEGIN\n", 1)[1].split("\nPLANE_END", 1)[0]
    except IndexError as exc:
        raise RuntimeError(f"{path}: missing plane block") from exc
    expression = "".join(body.split()).replace("+-", "-")
    terms = re.findall(r"[+-]?[^+-]+", expression)
    result: dict[tuple[int, int], int] = {}
    for term in terms:
        monomial, coefficient = parse_term(term, prime)
        if monomial in result:
            raise RuntimeError(f"{path}: repeated monomial {monomial}")
        result[monomial] = coefficient
    if set(result) != set(SUPPORT):
        raise RuntimeError(
            f"{path}: support mismatch missing={set(SUPPORT)-set(result)} "
            f"extra={set(result)-set(SUPPORT)}"
        )
    lead = result[(2, 21)]
    if lead == 0:
        raise RuntimeError(f"{path}: zero normalization coefficient")
    inverse = pow(lead, -1, prime)
    return {monomial: coefficient * inverse % prime for monomial, coefficient in result.items()}


def crt_pair(a: int, modulus: int, b: int, prime: int) -> tuple[int, int]:
    correction = ((b - a) % prime) * pow(modulus % prime, -1, prime) % prime
    new_modulus = modulus * prime
    return (a + modulus * correction) % new_modulus, new_modulus


def rational_reconstruct(residue: int, modulus: int) -> tuple[int, int]:
    residue %= modulus
    if residue == 0:
        return 0, 1
    bound = math.isqrt(modulus // 2)
    r0, r1 = modulus, residue
    t0, t1 = 0, 1
    while r1 > bound:
        quotient = r0 // r1
        r0, r1 = r1, r0 - quotient * r1
        t0, t1 = t1, t0 - quotient * t1
    numerator, denominator = r1, t1
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    common = math.gcd(abs(numerator), denominator)
    numerator //= common
    denominator //= common
    if (
        denominator == 0
        or abs(numerator) > bound
        or denominator > bound
        or (denominator * residue - numerator) % modulus != 0
    ):
        raise RuntimeError(f"rational reconstruction failed modulo {modulus}")
    return numerator, denominator


def reconstruct_prefix(
    tables: list[dict[tuple[int, int], int]], count: int
) -> tuple[dict[tuple[int, int], tuple[int, int]], int]:
    residues = {monomial: 0 for monomial in SUPPORT}
    modulus = 1
    for prime, table in zip(PRIMES[:count], tables[:count], strict=True):
        old_modulus = modulus
        for monomial in SUPPORT:
            residues[monomial], candidate_modulus = crt_pair(
                residues[monomial], old_modulus, table[monomial], prime
            )
        modulus = candidate_modulus
    return ({m: rational_reconstruct(residues[m], modulus) for m in SUPPORT}, modulus)


def fraction_text(fraction: tuple[int, int]) -> str:
    numerator, denominator = fraction
    return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"


def polynomial_text(
    coefficients: dict[tuple[int, int], tuple[int, int]],
    variables: tuple[str, str],
    support: tuple[tuple[int, int], ...],
) -> str:
    pieces: list[str] = []
    for exponent, monomial in zip(support, support, strict=True):
        numerator, denominator = coefficients[exponent]
        factors: list[str] = []
        for variable, power in zip(variables, monomial, strict=True):
            if power == 1:
                factors.append(variable)
            elif power > 1:
                factors.append(f"{variable}^{power}")
        monomial_text = "*".join(factors)
        absolute = (abs(numerator), denominator)
        coefficient_text = fraction_text(absolute)
        if monomial_text and absolute == (1, 1):
            term = monomial_text
        elif monomial_text:
            term = f"{coefficient_text}*{monomial_text}"
        else:
            term = coefficient_text
        if not pieces:
            pieces.append(("-" if numerator < 0 else "") + term)
        else:
            pieces.append(("-" if numerator < 0 else "+") + term)
    return "".join(pieces)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=pathlib.Path)
    parser.add_argument("candidate_json", type=pathlib.Path)
    args = parser.parse_args()
    require_aws()

    tables = [parse_output(args.output_directory / f"prime_{p}.stdout", p) for p in PRIMES]
    recon16, modulus16 = reconstruct_prefix(tables, 16)
    recon24, modulus24 = reconstruct_prefix(tables, 24)
    recon32, modulus32 = reconstruct_prefix(tables, 32)
    if recon16 != recon24 or recon24 != recon32:
        raise RuntimeError("reconstruction did not stabilize at 16/24/32 primes")

    for prime, table in zip(PRIMES, tables, strict=True):
        for monomial, (numerator, denominator) in recon32.items():
            if numerator * pow(denominator, -1, prime) % prime != table[monomial]:
                raise RuntimeError(f"replay mismatch at prime={prime}, monomial={monomial}")

    residual_support: list[tuple[int, int]] = []
    for s_power, t_power in SUPPORT:
        if s_power % 2:
            raise RuntimeError("non-invariant odd s exponent")
        q_power = s_power // 2
        numerator = t_power + 3 * q_power
        if numerator % 8:
            raise RuntimeError("monomial is not in Q[q,v]")
        residual_support.append((q_power, numerator // 8))

    plane = polynomial_text(recon32, ("a5", "a6"), SUPPORT)
    residual_coefficients = {
        residual: recon32[source]
        for source, residual in zip(SUPPORT, residual_support, strict=True)
    }
    residual = polynomial_text(
        residual_coefficients, ("q", "v"), tuple(residual_support)
    )
    payload = {
        "schema": 1,
        "source_normalization_monomial": [2, 21],
        "primes": list(PRIMES),
        "modulus_16": str(modulus16),
        "modulus_24": str(modulus24),
        "modulus_32": str(modulus32),
        "coefficients": {
            f"{i},{j}": fraction_text(recon32[(i, j)]) for i, j in SUPPORT
        },
        "plane_polynomial": plane,
        "residual_polynomial": residual,
        "prime_stdout_sha256": {
            str(prime): hashlib.sha256(
                (args.output_directory / f"prime_{prime}.stdout").read_bytes()
            ).hexdigest()
            for prime in PRIMES
        },
        "scope": "candidate relation pending exact saturated-ideal membership",
    }
    args.candidate_json.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, sort_keys=True, indent=2) + "\n").encode()
    args.candidate_json.write_bytes(encoded)
    print(f"RECONSTRUCTION_STABLE_16_24_32=1")
    print(f"ALL_PRIME_REPLAYS=1")
    print(f"SUPPORT_SIZE={len(SUPPORT)}")
    print(f"CANDIDATE_SHA256={hashlib.sha256(encoded).hexdigest()}")
    print("MULTIPRIME_RECONSTRUCTION=PASS_CANDIDATE_ONLY")


if __name__ == "__main__":
    main()
