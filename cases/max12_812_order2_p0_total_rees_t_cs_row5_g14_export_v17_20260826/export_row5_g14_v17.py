#!/usr/bin/env python3
"""AWS-only sparse export of the total moving-p row-five grade-14 coefficient."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPLAY = ROOT / "cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py"
REPLAY_SHA256 = "2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
TAILS_SHA256 = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
V9 = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9",
        "86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_p65521_v9",
        "dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4",
    ),
}
PREREG = HERE / "PREREGISTRATION.md"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_")
    ):
        fail("V17 exporter requires a registered AWS EC2 lane")
    return tag


def load_replay():
    if digest(REPLAY) != REPLAY_SHA256 or digest(TAILS) != TAILS_SHA256:
        fail("frozen replay or tail hash mismatch")
    spec = importlib.util.spec_from_file_location("odd_row5_replay_frozen", REPLAY)
    if spec is None or spec.loader is None:
        fail("cannot import frozen row-five replay")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dense_series(base, names: list[str]):
    return base.named_series(list(enumerate(names)))


def poly_pow(base, polynomial, exponent: int):
    answer = base.poly_const(1)
    factor = polynomial
    power = exponent
    while power:
        if power & 1:
            answer = base.poly_mul(answer, factor)
        power //= 2
        if power:
            factor = base.poly_mul(factor, factor)
    return answer


def poly_substitute(base, polynomial, replacements):
    answer = base.poly_const(0)
    for monomial, coefficient in polynomial.items():
        term = base.poly_const(coefficient)
        for name, exponent in monomial:
            factor = replacements.get(name, base.poly_var(name))
            term = base.poly_mul(term, poly_pow(base, factor, exponent))
            if not term:
                break
        answer = base.poly_add(answer, term)
    return answer


def variable_names(polynomials) -> list[str]:
    names = {
        name
        for polynomial in polynomials
        for monomial in polynomial
        for name, _ in monomial
    }
    priority = ["rho"]
    return [name for name in priority if name in names] + sorted(names - set(priority))


def coefficient_text(value: Fraction, characteristic: int) -> str:
    if characteristic:
        return str((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def singular_text(polynomial, characteristic: int) -> str:
    if not polynomial:
        return "0"
    terms: list[str] = []
    for monomial, coefficient in sorted(polynomial.items()):
        factors = [name if exponent == 1 else f"{name}^{exponent}" for name, exponent in monomial]
        factors.insert(0, coefficient_text(coefficient, characteristic))
        terms.append("*".join(factors))
    return "+".join(terms)


def build_total(base, tails):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 15):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))

    c0 = dense_series(base, ["cs"] + [f"cs{i}" for i in range(1, 13)])
    c = base.series_shift(c0, 2)
    r0 = dense_series(base, ["rs"] + [f"rs{i}" for i in range(1, 13)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))

    az = dense_series(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 10)])
    ac = dense_series(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 10)])
    ez = dense_series(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 10)])
    ec = dense_series(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 10)])

    n3 = base.series_shift(az, 3)
    n2 = base.series_shift(ac, 3)
    n1 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, az), ez)), 3)
    n0 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, ac), ec)), 3)
    coefficients = {
        6: base.series_scale(2, p),
        5: base.series_scale(2, c),
        4: base.series_add(base.series_mul(p, p), base.series_scale(2, r)),
        3: base.series_add(base.series_scale(2, base.series_mul(p, c)), base.series_shift(n3, 2)),
        2: base.series_add(base.series_mul(c, c), base.series_scale(2, base.series_mul(p, r)), base.series_shift(n2, 2)),
        1: base.series_add(base.series_scale(2, base.series_mul(c, r)), base.series_shift(n1, 2)),
        0: base.series_add(base.series_mul(r, r), base.series_shift(n0, 2)),
    }
    k10 = dense_series(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 11)])
    k6 = dense_series(base, ["k6", "k6_1", "k6_2"])
    k2 = dense_series(base, ["k2"])
    loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}

    total = base.series_zero()
    contribution_counts = [0] * 15
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    for raw_monomial, raw_coefficient in tails["5"]:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10 or sum(a * b for a, b in zip(monomial, weights)) != 17:
            fail(("row-five tail contract", monomial))
        term = base.series_zero()
        term[0] = base.poly_const(Fraction(str(raw_coefficient)))
        for index, exponent in enumerate(monomial[:7]):
            if exponent:
                term = base.series_mul(term, base.series_pow(coefficients[index], exponent))
        for index, exponent in enumerate(monomial[7:], start=7):
            if exponent not in (0, 1):
                fail(("load nonlinearity", monomial))
            if exponent:
                term = base.series_mul(term, loads[index])
        for degree in range(15):
            if term[degree]:
                contribution_counts[degree] += 1
        total = base.series_add(total, term)
    return total, contribution_counts


def compile_export(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    base = load_replay()
    tails = json.loads(TAILS.read_text())
    total, contribution_counts = build_total(base, tails)
    for degree in (10, 11, 12, 14):
        if not total[degree]:
            fail(("missing registered coefficient", degree))
    if any(exponent % 2 for monomial in total[14] for name, exponent in monomial if name == "rho"):
        fail("rho-deck parity failure")

    b = base.poly_var("b")
    w = base.poly_var("w")
    b2w = base.poly_mul(base.poly_mul(b, b), w)
    w2 = base.poly_mul(w, w)
    normalized = {
        "rho": base.poly_const(0),
        "ell1": base.poly_const(0),
        "rs": base.poly_const(0),
        "a0": base.poly_const(0),
        "c1": base.poly_const(0),
        "c0": base.poly_const(0),
        "e0": base.poly_const(0),
        "cs": b,
        "e1": b2w,
        "k": base.poly_scale(Fraction(12, 5), w2),
    }
    special = poly_substitute(base, total[14], normalized)
    expected = {(('b', 5), ('w', 2)): Fraction(-21, 320)}
    if special != expected:
        fail(("normalized odd specialization mismatch", base.serialize(special), base.serialize(expected)))
    wrong = dict(normalized)
    wrong["k"] = base.poly_scale(Fraction(11, 5), w2)
    wrong_special = poly_substitute(base, total[14], wrong)
    if wrong_special == expected or wrong_special == special:
        fail("normalization negative control failed")

    v9_dir, v9_manifest_sha = V9[characteristic]
    v9_manifest = v9_dir / "COEFFICIENTS.json"
    if digest(v9_manifest) != v9_manifest_sha:
        fail("V9 coefficient manifest mismatch")
    v9_data = json.loads(v9_manifest.read_text())
    v9_hashes = v9_data.get("coefficient_sha256")
    if (
        v9_data.get("status") != "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9"
        or v9_data.get("characteristic") != characteristic
        or not isinstance(v9_hashes, dict)
    ):
        fail("V9 coefficient manifest fields")
    refs = {}
    for degree in (10, 11, 12):
        path = v9_dir / "compiled" / f"Tg{degree}_5.poly"
        if digest(path) != v9_hashes.get(f"Tg{degree}_5"):
            fail(("V9 coefficient hash mismatch", degree))
        text = path.read_text().strip()
        if not text or ";" in text or "qring" in text:
            fail(("unsafe V9 coefficient", degree))
        refs[degree] = (path, text)

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    coefficient_path = output / f"Tg14_5_{label}.poly"
    coefficient_path.write_text(singular_text(total[14], characteristic) + "\n")
    variables = variable_names([total[10], total[11], total[12], total[14]])
    control = output / f"t_cs_row5_g14_bridge_{label}.sing"
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        'print("V17_QRING_DISABLED=1");',
    ]
    for degree in (10, 11, 12):
        lines += [
            f"poly Mine{degree}={singular_text(total[degree], characteristic)};",
            f"poly Ref{degree}={refs[degree][1]};",
            f"if (Mine{degree}-Ref{degree}!=0) {{ print(\"FAIL_V9_BRIDGE_G{degree}\"); quit; }}",
            f'print("V17_V9_BRIDGE_G{degree}=1");',
        ]
    lines += [
        f"poly G14={singular_text(total[14], characteristic)};",
        'if (G14==0) { print("FAIL_G14_ZERO"); quit; }',
        'if (subst(G14,rho,-rho)-G14!=0) { print("FAIL_RHO_PARITY"); quit; }',
        'print("V17_G14_NONZERO=1");',
        'print("V17_RHO_DECK_EVEN=1");',
        'print("V17_NORMALIZED_ODD_SPECIALIZATION=1");',
        'print("V17_NEGATIVE_NORMALIZATION_CONTROL=1");',
        'print("PASS_T_CS_ROW5_G14_EXPORT_V17");',
        "quit;",
    ]
    control.write_text("\n".join(lines) + "\n")
    if "qring " in control.read_text() or control.read_text().count("PASS_T_CS_ROW5_G14_EXPORT_V17") != 1:
        fail("control script sentinel")
    result = {
        "status": "PASS-T-CS-ROW5-G14-EXPORT-V17-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "replay_sha256": REPLAY_SHA256,
        "tails_sha256": TAILS_SHA256,
        "v9_manifest_sha256": v9_manifest_sha,
        "v9_reference_sha256": {str(degree): digest(path) for degree, (path, _) in refs.items()},
        "preregistration_sha256": digest(PREREG),
        "tail_terms_checked": len(tails["5"]),
        "coefficient_term_counts": {str(degree): len(total[degree]) for degree in (10, 11, 12, 14)},
        "contributing_tail_counts": {str(degree): contribution_counts[degree] for degree in (10, 11, 12, 14)},
        "rho_deck_even": True,
        "normalized_odd_specialization": "-(21/320)*b^5*w^2",
        "negative_normalization_control": True,
        "coefficient": str(coefficient_path),
        "coefficient_sha256": digest(coefficient_path),
        "control_script": str(control),
        "control_script_sha256": digest(control),
        "ring_variable_count": len(variables),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    compile_export(args.output, args.characteristic, require_aws())


if __name__ == "__main__":
    main()
