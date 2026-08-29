#!/usr/bin/env python3
"""Shared deterministic utilities for the GGV 8_28 LF40 custody case."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable


CASE_REL = Path("cases/ggv_8_28_lower_facepin_lf40_v1_20260827")
RAW_REL = Path("cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json")

SOURCE_PINS = {
    "lib/families.py": "729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e",
    "tests/test_families.py": "845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d",
    "lib/FAMILIES.md": "1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88",
    "jc72108/SECTION4-AUTOMATION.md": "836e3c4a8ef491799cd258a26cd0b7ae04a1309b0eefcedcc3964f5288c71427",
    str(RAW_REL): "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256": "012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022",
    "xmodel/ggv-8_28-raw-to-global-M-cokernel-interface-d3-sol-20260827.md": "c7ea900bdf0552c50d2a61c5a8f0f41a7b06e24eccedf5e5ab9cef3946c53556",
    "xmodel/ggv-second-newton-face-nu17-opus5-hostile-review-grok-20260827.md": "72f10ad7b42fd15d24bfc578ba1f8f9722ba695341307ae61642f614fe34a1ab",
    "xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md": "7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8",
    "xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-hostile-review-grok-20260827.md": "971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316",
    "cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/FREEZE.sha256": "676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b",
    "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md": "3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be",
    "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md": "171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0",
    "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256": "6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f",
    "xmodel/ggv-8_28-lower-facepin-s1-family-compiler-spec-sol-ultra-20260827.md": "94c10fd8c95424d7161ef4b13b7321529109426282dd0da0da2c94f6594f61c7",
    "xmodel/ggv-8_28-lower-facepin-s1-family-compiler-spec-hostile-review-opus5-20260827.md": "681357cef07f9b3fb053a320f72375f65a3c988369e002281e8179c4c874b950",
}

PRIMARY_SOURCE_PINS = {
    "https://export.arxiv.org/e-print/1708.07936v1": "2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e",
    "https://export.arxiv.org/e-print/2204.14178v1": "cac83f92efca63de3da6ca811b9837061e1a343a44b8039c8748d1b72423cba7",
}


def fail(message: Any) -> None:
    raise SystemExit(f"LF40_FAIL: {message}")


def digest_file(path: Path) -> str:
    h = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def write_json(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value))


def verify_source_pins(root: Path) -> dict[str, str]:
    actual: dict[str, str] = {}
    for rel, expected in SOURCE_PINS.items():
        path = root / rel
        if not path.is_file():
            fail(("missing pinned source", rel))
        got = digest_file(path)
        if got != expected:
            fail(("source pin mismatch", rel, expected, got))
        actual[rel] = got
    return actual


def freeze_directory(directory: Path, manifest_name: str) -> None:
    lines = []
    for path in sorted(p for p in directory.rglob("*") if p.is_file() and p.name != manifest_name):
        lines.append(f"{digest_file(path)}  {path.relative_to(directory)}\n")
    (directory / manifest_name).write_text("".join(lines), encoding="utf-8")


Monomial = tuple[tuple[str, int], ...]
SparsePoly = dict[Monomial, int]


def normalize_monomial(factors: Iterable[tuple[str, int]]) -> Monomial:
    powers: dict[str, int] = {}
    for variable, exponent in factors:
        if exponent < 0:
            fail(("negative monomial exponent", variable, exponent))
        if exponent:
            powers[variable] = powers.get(variable, 0) + exponent
    return tuple(sorted(powers.items()))


def multiply_monomials(left: Monomial, right: Monomial) -> Monomial:
    return normalize_monomial((*left, *right))


def add_term(poly: SparsePoly, coefficient: int, monomial: Monomial = ()) -> None:
    if coefficient == 0:
        return
    value = poly.get(monomial, 0) + coefficient
    if value:
        poly[monomial] = value
    else:
        poly.pop(monomial, None)


def serialize_poly(poly: SparsePoly) -> list[dict[str, Any]]:
    return [
        {
            "coefficient": coefficient,
            "monomial": [{"variable": variable, "exponent": exponent}
                         for variable, exponent in monomial],
        }
        for monomial, coefficient in sorted(poly.items())
    ]


def singular_poly(poly: SparsePoly) -> str:
    if not poly:
        return "0"
    chunks: list[str] = []
    for monomial, coefficient in sorted(poly.items()):
        factors = [variable if exponent == 1 else f"{variable}^{exponent}"
                   for variable, exponent in monomial]
        body = "*".join(factors)
        magnitude = abs(coefficient)
        if body:
            atom = body if magnitude == 1 else f"{magnitude}*{body}"
        else:
            atom = str(magnitude)
        if not chunks:
            chunks.append(atom if coefficient > 0 else f"-{atom}")
        else:
            chunks.append(("+" if coefficient > 0 else "-") + atom)
    return "".join(chunks)


def univariate_mul(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, 0) + a * b
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def univariate_pow(poly: dict[int, int], exponent: int) -> dict[int, int]:
    out = {0: 1}
    base = dict(poly)
    power = exponent
    while power:
        if power & 1:
            out = univariate_mul(out, base)
        base = univariate_mul(base, base)
        power >>= 1
    return out


def univariate_derivative(poly: dict[int, int]) -> dict[int, int]:
    return {degree - 1: degree * coefficient for degree, coefficient in poly.items()
            if degree and degree * coefficient}


def univariate_add_scaled(target: dict[int, int], source: dict[int, int], scale: int) -> None:
    for degree, coefficient in source.items():
        value = target.get(degree, 0) + scale * coefficient
        if value:
            target[degree] = value
        else:
            target.pop(degree, None)

