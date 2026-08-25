#!/usr/bin/env python3
"""Generate a fail-closed Singular shard for a sparse plane curve over F_(p^e).

The input curve has coefficients in F_p and is supplied as a sparse table
``nonzero_support[v_degree] = [[w_degree, coefficient], ...]``.  The program
does no point-count arithmetic: it validates the finite-field presentation and
transcribes the curve into a Singular source file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def sub(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % p
    return trim(out)


def divmod_poly(left: list[int], right: list[int], p: int) -> tuple[list[int], list[int]]:
    numerator = trim(left[:])
    denominator = trim(right[:])
    if denominator == [0]:
        raise ZeroDivisionError
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, p)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inverse % p
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] = (numerator[index + shift] - coefficient * value) % p
        trim(numerator)
    return trim(quotient), trim(numerator)


def mod_poly(poly: list[int], modulus: list[int], p: int) -> list[int]:
    return divmod_poly(poly, modulus, p)[1]


def mul_mod(left: list[int], right: list[int], modulus: list[int], p: int) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            product[i + j] = (product[i + j] + x * y) % p
    return mod_poly(product, modulus, p)


def pow_mod(base: list[int], exponent: int, modulus: list[int], p: int) -> list[int]:
    result = [1]
    power = mod_poly(base, modulus, p)
    while exponent:
        if exponent & 1:
            result = mul_mod(result, power, modulus, p)
        exponent >>= 1
        if exponent:
            power = mul_mod(power, power, modulus, p)
    return result


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    a = trim(left[:])
    b = trim(right[:])
    while b != [0]:
        a, b = b, divmod_poly(a, b, p)[1]
    if a == [0]:
        return a
    inverse = pow(a[-1], -1, p)
    return [(value * inverse) % p for value in a]


def prime_divisors(n: int) -> list[int]:
    result = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            result.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        result.append(n)
    return result


def validate_irreducible(modulus: list[int], p: int) -> None:
    degree = len(modulus) - 1
    x = [0, 1]
    frobenius = [x]
    for _ in range(degree):
        frobenius.append(pow_mod(frobenius[-1], p, modulus, p))
    if trim(sub(frobenius[degree], x, p)) != [0]:
        raise SystemExit("extension modulus does not divide X^(p^e)-X")
    for divisor in prime_divisors(degree):
        test = sub(frobenius[degree // divisor], x, p)
        if len(gcd_poly(modulus, test, p)) != 1:
            raise SystemExit("extension modulus is reducible")


def load_curve(path: Path, expected_sha256: str) -> tuple[int, int, dict[str, list[list[int]]]]:
    actual = sha256(path)
    if actual != expected_sha256:
        raise SystemExit(f"curve hash mismatch: {actual}")
    data = json.loads(path.read_text())
    p = int(data["prime"])
    degree_v = int(data["degree_v"])
    support = data["nonzero_support"]
    if not is_prime(p) or p == 2:
        raise SystemExit("an odd prime is required")
    if degree_v <= 0 or set(map(int, support)) - set(range(degree_v + 1)):
        raise SystemExit("invalid v support")
    normalized: dict[str, list[list[int]]] = {}
    for key, terms in support.items():
        vd = int(key)
        seen: set[int] = set()
        normalized[str(vd)] = []
        for raw_wd, raw_coefficient in terms:
            wd = int(raw_wd)
            coefficient = int(raw_coefficient) % p
            if wd < 0 or wd in seen or coefficient == 0:
                raise SystemExit(f"invalid support row v^{vd}")
            seen.add(wd)
            normalized[str(vd)].append([wd, coefficient])
        normalized[str(vd)].sort()
    if normalized.get(str(degree_v)) != [[0, 1]]:
        raise SystemExit("curve must be monic of declared degree in v")
    return p, degree_v, normalized


def parse_modulus(text: str, p: int) -> list[int]:
    try:
        modulus = [int(value) % p for value in text.split(",")]
    except ValueError as exc:
        raise SystemExit("modulus must be comma-separated integer coefficients") from exc
    modulus = trim(modulus)
    if len(modulus) < 2 or modulus[-1] != 1:
        raise SystemExit("extension modulus must be monic and nonconstant")
    validate_irreducible(modulus, p)
    return modulus


def a_power(power: int) -> str:
    if power == 0:
        return "1"
    if power == 1:
        return "a"
    return f"a{power}"


def minpoly_expression(modulus: list[int], p: int) -> str:
    terms = []
    for degree in range(len(modulus) - 1, -1, -1):
        coefficient = modulus[degree] % p
        if coefficient == 0:
            continue
        monomial = a_power(degree)
        terms.append(monomial if coefficient == 1 else f"{coefficient}*{monomial}")
    return "+".join(terms)


def field_expression(index: int, p: int, degree: int) -> str:
    digits = []
    value = index
    for power in range(degree):
        digit = value % p
        value //= p
        if digit:
            monomial = a_power(power)
            digits.append(monomial if digit == 1 else f"{digit}*{monomial}")
    if value:
        raise SystemExit("field index overflow")
    return "+".join(digits) if digits else "0"


def emit_build_proc(name: str, support: dict[str, list[list[int]]], p: int, derivative_w: bool) -> None:
    print(f"proc {name}(number ww)")
    print("{")
    print("  poly out=0;")
    for vd in sorted(map(int, support)):
        for wd, coefficient in support[str(vd)]:
            if derivative_w:
                if wd == 0:
                    continue
                coefficient = coefficient * wd % p
                wd -= 1
            if coefficient == 0:
                continue
            wp = "1" if wd == 0 else ("ww" if wd == 1 else f"ww^{wd}")
            vp = "1" if vd == 0 else ("v" if vd == 1 else f"v^{vd}")
            print(f"  out=out+{coefficient}*({wp})*({vp});")
    print("  return(out);")
    print("}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--curve", required=True, type=Path)
    parser.add_argument("--curve-sha256", required=True)
    parser.add_argument("--modulus", required=True)
    parser.add_argument("--start", required=True, type=int)
    parser.add_argument("--stop", required=True, type=int)
    args = parser.parse_args()

    p, degree_v, support = load_curve(args.curve, args.curve_sha256)
    modulus = parse_modulus(args.modulus, p)
    extension_degree = len(modulus) - 1
    field_order = p**extension_degree
    if not (0 <= args.start < args.stop <= field_order):
        raise SystemExit("invalid shard interval")

    print("option(noredefine);")
    print(f"ring E=({p},a),(v),lp;")
    print(f"minpoly={minpoly_expression(modulus, p)};")
    emit_build_proc("buildH", support, p, False)
    emit_build_proc("buildHw", support, p, True)
    print("proc powMod(poly base,int exponent,ideal G)")
    print("{")
    print("  poly result=1;")
    print("  poly power=reduce(base,G);")
    print("  int e=exponent;")
    print("  int half;")
    print("  while(e>0)")
    print("  {")
    print("    half=e div 2;")
    print("    if(e-2*half==1){result=reduce(result*power,G);}")
    print("    e=half;")
    print("    if(e>0){power=reduce(power*power,G);}")
    print("  }")
    print("  return(result);")
    print("}")
    print("proc countFiber(number ww)")
    print("{")
    print("  poly h=buildH(ww);")
    print(f'  if(deg(h)!={degree_v}){{print("FIBRE_DEGREE_FAILURE");exit;}}')
    print("  poly hv=diff(h,v);")
    print("  poly hw=buildHw(ww);")
    print("  ideal G=std(h);")
    print(f"  poly frob=powMod(v,{field_order},G)-v;")
    print("  poly rationalRoots=gcd(h,frob);")
    print("  poly singularRoots=gcd(gcd(rationalRoots,hv),hw);")
    print("  int total=deg(rationalRoots);")
    print("  int singular=deg(singularRoots);")
    print("  int smooth=total-singular;")
    print('  if(total<0 || singular<0 || smooth<0){print("NEGATIVE_COUNT_FAILURE");exit;}')
    print("  return(list(total,smooth,singular));")
    print("}")
    print('print("EXTENSION_SMOOTH_POINT_ORACLE_BEGIN");')
    print(f'print("curve_sha256={args.curve_sha256}");')
    print(f'print("prime={p}");')
    print(f'print("extension_degree={extension_degree}");')
    print(f'print("field_order={field_order}");')
    print(f'print("modulus={args.modulus}");')
    for index in range(args.start, args.stop):
        print(f"number w{index}={field_expression(index, p, extension_degree)};")
        print(f"list C{index}=countFiber(w{index});")
        print(
            f'print("RECORD|index={index}|total="+string(C{index}[1])'
            f'+"|smooth="+string(C{index}[2])+"|singular="+string(C{index}[3]));'
        )
    print('print("EXTENSION_SMOOTH_POINT_ORACLE_SHARD_PASS");')
    print("exit;")


if __name__ == "__main__":
    main()

