#!/usr/bin/env python3
"""Compile the fixed branch-P endpoint as a literal exact coefficient ideal.

This is a desk compiler, not a solver.  It uses a tiny sparse polynomial
ring over Q to expand the D5G recurrence coefficient by coefficient while
keeping X external.  The generated ideal therefore has exactly the raw
coefficient variables and no evaluation-at-roots or characteristic rewrite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from typing import Dict, Iterable, Mapping, Sequence, Tuple


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
OUT_JSON = HERE / "RAW_DIRECT_SYSTEM.json"
OUT_SING = HERE / "raw_direct.sing"
OUT_SING_Q_DP = HERE / "raw_direct_q_dp_slimgb.sing"
OUT_SING_P = HERE / "raw_direct_p65521.sing"
OUT_SING_P_DP = HERE / "raw_direct_p65521_dp_slimgb.sing"
OUT_PARSE = HERE / "raw_parse.sing"
OUT_MSOLVE_Q = HERE / "raw_direct_q.ms"
OUT_MSOLVE_P = HERE / "raw_direct_p65521.ms"
OUT_MODES = HERE / "MODE_AUDIT.json"

PINS = {
    "raw_input": "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    "cascade_producer": "6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a",
    "cascade_hostile_review": "7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec",
    "contraction_note": "79d32289ece2010929197d0bb189582395b4bca39dd6a4b9fb4b68233e17ed78",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


Mon = Tuple[str, ...]


@dataclass(frozen=True)
class MV:
    terms: Mapping[Mon, Q]

    @staticmethod
    def zero() -> "MV":
        return MV({})

    @staticmethod
    def const(value) -> "MV":
        value = Q(value)
        return MV({(): value} if value else {})

    @staticmethod
    def var(name: str) -> "MV":
        return MV({(name,): Q(1)})

    def __add__(self, other: "MV") -> "MV":
        out: Dict[Mon, Q] = dict(self.terms)
        for mon, coefficient in other.terms.items():
            out[mon] = out.get(mon, Q(0)) + coefficient
            if not out[mon]:
                del out[mon]
        return MV(out)

    def __neg__(self) -> "MV":
        return MV({mon: -coefficient for mon, coefficient in self.terms.items()})

    def __sub__(self, other: "MV") -> "MV":
        return self + (-other)

    def __mul__(self, other: "MV") -> "MV":
        out: Dict[Mon, Q] = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                mon = tuple(sorted(left + right))
                out[mon] = out.get(mon, Q(0)) + a * b
                if not out[mon]:
                    del out[mon]
        return MV(out)

    def scale(self, value) -> "MV":
        value = Q(value)
        if not value:
            return MV.zero()
        return MV({mon: value * coefficient for mon, coefficient in self.terms.items()})

    def encode(self):
        return [[list(mon), str(coefficient)] for mon, coefficient in sorted(self.terms.items())]

    def expression(self, modulus: int = 0) -> str:
        if not self.terms:
            return "0"
        pieces = []
        for mon, coefficient in sorted(self.terms.items()):
            if modulus:
                num = coefficient.numerator % modulus
                den = pow(coefficient.denominator % modulus, -1, modulus)
                c = (num * den) % modulus
                if not c:
                    continue
                atom = "*".join(mon) if mon else "1"
                pieces.append(f"{c}*{atom}")
            else:
                atom = "*".join(mon) if mon else "1"
                pieces.append(f"({coefficient})*{atom}")
        return "+".join(pieces) if pieces else "0"


M0 = MV.zero()


def xtrim(poly: Iterable[MV]) -> Tuple[MV, ...]:
    out = list(poly)
    while out and not out[-1].terms:
        out.pop()
    return tuple(out)


def xadd(a: Sequence[MV], b: Sequence[MV]) -> Tuple[MV, ...]:
    return xtrim((a[i] if i < len(a) else M0) + (b[i] if i < len(b) else M0)
                 for i in range(max(len(a), len(b))))


def xscale(a: Sequence[MV], value) -> Tuple[MV, ...]:
    return xtrim(coefficient.scale(value) for coefficient in a)


def xmul(a: Sequence[MV], b: Sequence[MV]) -> Tuple[MV, ...]:
    if not a or not b:
        return ()
    out = [M0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = out[i + j] + left * right
    return xtrim(out)


def xder(a: Sequence[MV]) -> Tuple[MV, ...]:
    return xtrim(a[i].scale(i) for i in range(1, len(a)))


def xpow(a: Sequence[MV], exponent: int) -> Tuple[MV, ...]:
    out = (MV.const(1),)
    base = tuple(a)
    while exponent:
        if exponent & 1:
            out = xmul(out, base)
        base = xmul(base, base)
        exponent //= 2
    return out


def xvar_poly(names_by_degree: Mapping[int, str]) -> Tuple[MV, ...]:
    if not names_by_degree:
        return ()
    out = [M0] * (max(names_by_degree) + 1)
    for degree, name in names_by_degree.items():
        out[degree] = MV.var(name)
    return xtrim(out)


def raw_windows(source):
    windows = {"F": {}, "G": {}}
    for kind in windows:
        for slot in source["raw_slots_through_weight_22"][kind]:
            weight = int(slot["weight"])
            if weight <= 0:
                continue
            degree = int(slot["raw_exponents"]["x"])
            windows[kind].setdefault(weight, {})[degree] = slot["slot"]
    return windows


def expected_windows():
    return {
        "F": {
            1: (0, 15), 2: (0, 14), 3: (0, 13), 4: (0, 12),
            5: (0, 11), 6: (0, 10), 7: (0, 9), 8: (0, 8),
            9: (1, 7), 10: (1, 6), 11: (1, 5), 12: (2, 4),
            13: (2, 3), 14: (2, 2),
        },
        "G": {
            1: (0, 23), 2: (0, 22), 3: (0, 21), 4: (0, 20),
            5: (0, 19), 6: (0, 18), 7: (0, 17), 8: (0, 16),
            9: (0, 15), 10: (0, 14), 11: (0, 13), 12: (0, 12),
            13: (1, 11), 14: (1, 10), 15: (1, 9), 16: (2, 8),
            17: (2, 7), 18: (2, 6), 19: (3, 5), 20: (3, 4),
            21: (3, 3),
        },
    }


def verify_windows(windows):
    expected = expected_windows()
    census = {"F": {}, "G": {}}
    for kind in ("F", "G"):
        assert set(windows[kind]) == set(expected[kind])
        for weight, (lower, upper) in expected[kind].items():
            degrees = sorted(windows[kind][weight])
            assert degrees == list(range(lower, upper + 1))
            census[kind][str(weight)] = {
                "lower": lower, "upper": upper, "dimension": len(degrees),
                "slots": [windows[kind][weight][degree] for degree in degrees],
            }
    return census


def build_system(source):
    windows = raw_windows(source)
    census = verify_windows(windows)

    A = (MV.const(-1), M0, M0, M0, MV.const(1))
    H = xpow(A, 2)
    F = {0: xpow(H, 2), 1: H}
    G = {0: xpow(H, 3)}

    Z = tuple(MV.var(f"z_{degree}") for degree in range(7))
    T = tuple(MV.var(f"tt_{degree}") for degree in range(10))
    one = (MV.const(1),)
    F[2] = xscale(xadd(one, xmul(H, Z)), Q(1, 4))
    F[3] = xscale(xadd(Z, xmul(A, T)), Q(1, 8))

    # c2=0 baseline coefficients.  These are rederived from F^(3/2), not
    # copied from serialized producer output.
    G[1] = xscale(xpow(H, 2), Q(3, 2))
    G[2] = xadd(xscale(xmul(H, F[2]), Q(3, 2)), xscale(H, Q(3, 8)))
    G[3] = xadd(
        xadd(xscale(xmul(H, F[3]), Q(3, 2)), xscale(F[2], Q(3, 4))),
        (MV.const(Q(-1, 16)),),
    )

    for weight in range(4, 15):
        F[weight] = xvar_poly(windows["F"][weight])
    for weight in range(4, 22):
        G[weight] = xvar_poly(windows["G"][weight])

    rows = {}
    for n in range(23):
        value = ()
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            value = xadd(value, xscale(xmul(xder(F[i]), G[j]), 12 - j))
            value = xadd(value, xscale(xmul(F[i], xder(G[j])), i - 8))
        rows[n] = value

    for n in range(4):
        assert not rows[n], f"fixed/cascade row D{n} did not vanish"

    generators = []
    per_row = {}
    for n in range(4, 23):
        target = 1 if n == 22 else 0
        count = 0
        max_degree = max(len(rows[n]), 1 if target else 0)
        for degree in range(max_degree):
            coefficient = rows[n][degree] if degree < len(rows[n]) else M0
            if degree == 0 and target:
                coefficient = coefficient - MV.const(target)
            if coefficient.terms:
                generators.append({
                    "row": n,
                    "x_degree": degree,
                    "terms": coefficient.encode(),
                    "sha256": hashlib.sha256(compact(coefficient.encode())).hexdigest(),
                })
                count += 1
        per_row[str(n)] = {
            "target": target,
            "generator_count": count,
            "raw_polynomial_degree": len(rows[n]) - 1,
            "row_sha256": hashlib.sha256(compact([
                item for item in generators if item["row"] == n
            ])).hexdigest(),
        }

    variables = []
    for weight in range(21, 3, -1):
        if weight in windows["G"]:
            for degree in sorted(windows["G"][weight], reverse=True):
                variables.append(windows["G"][weight][degree])
        if weight in windows["F"] and weight >= 4:
            for degree in sorted(windows["F"][weight], reverse=True):
                variables.append(windows["F"][weight][degree])
    variables.extend(f"tt_{degree}" for degree in range(9, -1, -1))
    variables.extend(f"z_{degree}" for degree in range(6, -1, -1))
    assert len(variables) == len(set(variables)) == 303

    all_used = sorted({name for item in generators for mon, _ in item["terms"] for name in mon})
    assert set(all_used) <= set(variables)

    system = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-RAW-DIRECT-v1",
        "field": "Q",
        "fixture": {"A": "X^4-1", "H": "A^2", "F1": "H", "c2": "0"},
        "recurrence": "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')",
        "charged_rows": {"zero": list(range(7, 22)), "affine_target": {"row": 22, "value": 1}, "D23_imposed": False},
        "included_reviewed_rows": [4, 5, 6],
        "slotless": {"F_max_weight": 14, "G_max_weight": 21, "G22_present": False},
        "variables": variables,
        "variable_count": len(variables),
        "windows": census,
        "generators": generators,
        "generator_count": len(generators),
        "per_row": per_row,
        "pins": PINS,
    }
    return system, F, G, rows


def mode_audit(windows):
    A_coefficients = (-1, 0, 0, 0, 1)

    def power(exponent):
        coeffs = [Q(1)]
        base = list(map(Q, A_coefficients))
        for _ in range(exponent):
            out = [Q(0)] * (len(coeffs) + len(base) - 1)
            for i, a in enumerate(coeffs):
                for j, b in enumerate(base):
                    out[i + j] += a * b
            coeffs = out
        return coeffs

    records = []
    for weight, exponent in ((4, 4), (6, 3), (8, 2), (10, 1), (12, 0)):
        coeffs = power(exponent)
        support = [i for i, c in enumerate(coeffs) if c]
        allowed = sorted(windows["G"][weight])
        assert set(support) <= set(allowed)
        records.append({
            "weight": weight,
            "characteristic_mode": f"t^{weight} F^(({12-weight})/8)",
            "leading_polynomial": f"A^{exponent}",
            "coefficients": [str(c) for c in coeffs],
            "support_degrees": support,
            "raw_window": [min(allowed), max(allowed)],
            "retained": True,
        })
    return {
        "schema": "GGV-8_28-UPPER-P-MODE-AUDIT-v1",
        "c2_fixed_zero": True,
        "later_modes": records,
        "no_polynomial_mode_after_12_through_21": True,
    }


def decode_mv(encoded) -> MV:
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def singular_script(system, modulus=0):
    ring_char = modulus if modulus else 0
    variables = system["variables"]
    expressions = [decode_mv(item["terms"]).expression(modulus) for item in system["generators"]]
    lines = [
        "// Generated from RAW_DIRECT_SYSTEM.json; literal raw formulation.",
        f"ring endpoint={ring_char},({','.join(variables)}),lp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("RAW_DIRECT variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_STD");',
        "ideal J=std(I);",
        "int elapsed=timer-start_time;",
        'print("END_STD seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'print("UNIT="+string(size(J)==1 && J[1]==1));',
        "J;",
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def msolve_input(system, modulus):
    expressions = [decode_mv(item["terms"]).expression(modulus) for item in system["generators"]]
    return f"{', '.join(system['variables'])}\n{modulus}\n" + ",\n".join(expressions) + "\n"


def parse_script(system):
    full = singular_script(system)
    prefix = full.split("int start_time=timer;", 1)[0]
    return prefix + 'print("PARSE_PASS");\nquit;\n'


def dp_script(system, modulus):
    script = singular_script(system, modulus)
    script = script.replace("),lp;", "),dp;", 1)
    script = script.replace("ideal J=std(I);", "ideal J=slimgb(I);", 1)
    return script


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not (args.write or args.check):
        parser.error("choose --write or --check")

    assert sha256(RAW_INPUT) == PINS["raw_input"]
    assert sha256(ROOT / "xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md") == PINS["cascade_producer"]
    assert sha256(ROOT / "xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md") == PINS["cascade_hostile_review"]
    assert sha256(ROOT / "xmodel/ideation-20260827T1808Z-sol.md") == PINS["contraction_note"]

    source = json.loads(RAW_INPUT.read_text())
    system, _, _, _ = build_system(source)
    modes = mode_audit(raw_windows(source))
    outputs = {
        OUT_JSON: pretty(system),
        OUT_MODES: pretty(modes),
        OUT_SING: singular_script(system).encode(),
        OUT_SING_Q_DP: dp_script(system, 0).encode(),
        OUT_SING_P: singular_script(system, 65521).encode(),
        OUT_SING_P_DP: dp_script(system, 65521).encode(),
        OUT_PARSE: parse_script(system).encode(),
        OUT_MSOLVE_Q: msolve_input(system, 0).encode(),
        OUT_MSOLVE_P: msolve_input(system, 65521).encode(),
    }
    if args.write:
        for path, payload in outputs.items():
            path.write_bytes(payload)
    if args.check:
        for path, payload in outputs.items():
            assert path.read_bytes() == payload, f"stale generated file: {path.name}"

    print(json.dumps({
        "status": "PASS",
        "variables": system["variable_count"],
        "generators": system["generator_count"],
        "D22_generators": system["per_row"]["22"]["generator_count"],
        "raw_system_sha256": hashlib.sha256(outputs[OUT_JSON]).hexdigest(),
        "singular_sha256": hashlib.sha256(outputs[OUT_SING]).hexdigest(),
        "singular_q_dp_sha256": hashlib.sha256(outputs[OUT_SING_Q_DP]).hexdigest(),
        "singular_p65521_sha256": hashlib.sha256(outputs[OUT_SING_P]).hexdigest(),
        "singular_p65521_dp_sha256": hashlib.sha256(outputs[OUT_SING_P_DP]).hexdigest(),
        "mode_count": len(modes["later_modes"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
