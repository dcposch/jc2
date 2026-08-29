#!/usr/bin/env python3
"""Desk verifier V0--V4 for the uniform strict-UAC source transport schema.

This is deliberately independent of Singular and of the frozen source emitters.  It
checks their custody and selected literal formula tokens, but constructs the two
formal-series sides directly from the normative schema.  The all-grade theorem is
the explicit coefficient-ring jet map in SCHEMA.json; the finite expansions here are
mutation controls and compiler-interface defense, not the proof of that theorem.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCHEMA_PATH = HERE / "SCHEMA.json"
EXPECTED_SCHEMA_SHA256 = "796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673"
PRIME = 1_000_003


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


class Ring:
    def __init__(self, modulus: int | None):
        self.modulus = modulus
        self.zero = Fraction(0) if modulus is None else 0
        self.one = Fraction(1) if modulus is None else 1

    def value(self, raw: int | Fraction | str) -> Fraction | int:
        q = raw if isinstance(raw, Fraction) else Fraction(str(raw))
        if self.modulus is None:
            return q
        return (q.numerator * pow(q.denominator, -1, self.modulus)) % self.modulus

    def add(self, x: Fraction | int, y: Fraction | int) -> Fraction | int:
        z = x + y
        return z if self.modulus is None else z % self.modulus

    def mul(self, x: Fraction | int, y: Fraction | int) -> Fraction | int:
        z = x * y
        return z if self.modulus is None else z % self.modulus

    def neg(self, x: Fraction | int) -> Fraction | int:
        return -x if self.modulus is None else (-x) % self.modulus


class Series:
    def __init__(self, degree: int, ring: Ring):
        self.n = degree
        self.ring = ring

    def zeros(self) -> list[Fraction | int]:
        return [self.ring.zero] * (self.n + 1)

    def one(self) -> list[Fraction | int]:
        out = self.zeros()
        out[0] = self.ring.one
        return out

    def add(self, x: list[Any], y: list[Any]) -> list[Any]:
        return [self.ring.add(a, b) for a, b in zip(x, y)]

    def neg(self, x: list[Any]) -> list[Any]:
        return [self.ring.neg(a) for a in x]

    def sub(self, x: list[Any], y: list[Any]) -> list[Any]:
        return self.add(x, self.neg(y))

    def scale(self, x: list[Any], scalar: int | Fraction | str) -> list[Any]:
        q = self.ring.value(scalar)
        return [self.ring.mul(q, a) for a in x]

    def shift(self, x: list[Any], amount: int) -> list[Any]:
        out = self.zeros()
        if amount <= self.n:
            out[amount:] = x[: self.n + 1 - amount]
        return out

    def mul(self, x: list[Any], y: list[Any]) -> list[Any]:
        out = self.zeros()
        rx = [(i, a) for i, a in enumerate(x) if a != self.ring.zero]
        ry = [(i, a) for i, a in enumerate(y) if a != self.ring.zero]
        for i, a in rx:
            for j, b in ry:
                if i + j > self.n:
                    break
                out[i + j] = self.ring.add(out[i + j], self.ring.mul(a, b))
        return out

    def power(self, x: list[Any], exponent: int) -> list[Any]:
        if exponent < 0:
            fail("negative series exponent")
        out = self.one()
        base = x
        power = exponent
        while power:
            if power & 1:
                out = self.mul(out, base)
            power >>= 1
            if power:
                base = self.mul(base, base)
        return out


def deterministic_series(tag: str, engine: Series) -> list[Any]:
    values: list[Any] = []
    for index in range(engine.n + 1):
        raw = int(sha256(f"{tag}:{index}".encode()).hexdigest()[:12], 16) % 23 - 11
        if raw == 0:
            raw = (index % 7) + 1
        values.append(engine.ring.value(raw))
    return values


def assemble_f(
    e: Series,
    p: list[Any],
    ctot: list[Any],
    rtot: list[Any],
    n3: list[Any],
    n2: list[Any],
    n1: list[Any],
    n0: list[Any],
) -> dict[int, list[Any]]:
    p2 = e.mul(p, p)
    return {
        6: e.scale(p, 2),
        5: e.scale(ctot, 2),
        4: e.add(p2, e.scale(rtot, 2)),
        3: e.add(e.scale(e.mul(p, ctot), 2), e.shift(n3, 2)),
        2: e.add(e.add(e.mul(ctot, ctot), e.scale(e.mul(p, rtot), 2)), e.shift(n2, 2)),
        1: e.add(e.scale(e.mul(ctot, rtot), 2), e.shift(n1, 2)),
        0: e.add(e.mul(rtot, rtot), e.shift(n0, 2)),
    }


def source_pair(
    a: int,
    c: int,
    r: int,
    degree: int,
    ring: Ring,
    mutation: str | None = None,
) -> tuple[dict[int, list[Any]], dict[int, list[Any]], dict[str, list[Any]], dict[str, list[Any]]]:
    """Build total and shifted-D1 primitives by separate formula paths."""
    e = Series(degree, ring)
    p_d1 = deterministic_series("P", e)
    p_total = list(p_d1)
    if mutation == "drop_ell1":
        p_total[1] = ring.zero

    az = deterministic_series("AzD1", e)
    ac = deterministic_series("AcD1", e)
    cz = deterministic_series("CzD1", e)
    cc = deterministic_series("CcD1", e)
    bz = deterministic_series("BzD1", e)
    bc = deterministic_series("BcD1", e)

    c_factor = 1 if mutation == "C_factor_1" else 2
    r_factor = 1 if mutation == "R_factor_1" else 4
    total_az = e.shift(az, a)
    total_ac = e.shift(ac, a)
    total_ez = e.scale(e.shift(cz, c), c_factor)
    total_ec = e.scale(e.shift(cc, c), c_factor)
    total_s = e.shift(bz, r)
    total_q = e.scale(e.shift(bc, r), r_factor)

    ctot = e.shift(total_s, 2)
    rtot = e.scale(e.add(e.mul(p_total, p_total), e.shift(total_q, 2)), Fraction(1, 4))
    total_n3 = e.shift(total_az, 3)
    total_n2 = e.shift(total_ac, 3)
    total_n1 = e.scale(e.shift(e.add(e.mul(p_total, total_az), total_ez), 3), Fraction(1, 2))
    total_n0 = e.scale(e.shift(e.add(e.mul(p_total, total_ac), total_ec), 3), Fraction(1, 2))
    total_f = assemble_f(e, p_total, ctot, rtot, total_n3, total_n2, total_n1, total_n0)

    # Independent D1 path: no total auxiliary S,Q,Ez,Ec is reused here.
    kc = e.shift(bz, r + 2)
    kr = e.add(e.scale(e.mul(p_d1, p_d1), Fraction(1, 4)), e.shift(bc, r + 2))
    d1_n3 = e.shift(az, a + 3)
    d1_n2 = e.shift(ac, a + 3)
    d1_n1 = e.add(e.scale(e.shift(e.mul(p_d1, az), a + 3), Fraction(1, 2)), e.shift(cz, c + 3))
    d1_n0 = e.add(e.scale(e.shift(e.mul(p_d1, ac), a + 3), Fraction(1, 2)), e.shift(cc, c + 3))
    d1_f = assemble_f(e, p_d1, kc, kr, d1_n3, d1_n2, d1_n1, d1_n0)

    loads = {name: deterministic_series(name, e) for name in ("k10", "k6", "k2")}
    targets: dict[str, list[Any]] = {}
    for name in ("mu2", "mu4", "mu6", "J"):
        scalar = e.zeros()
        scalar[0] = deterministic_series(name, e)[0]
        targets[name] = scalar
    return total_f, d1_f, loads, targets


def row_series(
    tails: dict[str, list[list[object]]],
    row: int,
    f: dict[int, list[Any]],
    loads: dict[str, list[Any]],
    targets: dict[str, list[Any]],
    degree: int,
    ring: Ring,
    omit_target: bool = False,
) -> list[Any]:
    e = Series(degree, ring)
    max_exp = [0] * 7
    for raw_monomial, _ in tails[str(row)]:
        for index, exponent in enumerate(raw_monomial[:7]):
            max_exp[index] = max(max_exp[index], int(exponent))
    powers: dict[tuple[int, int], list[Any]] = {}
    for index in range(7):
        for exponent in range(max_exp[index] + 1):
            powers[(index, exponent)] = e.power(f[index], exponent)

    out = e.zeros()
    load_names = ("k10", "k6", "k2")
    load_delays = (4, 12, 20)
    for raw_monomial, raw_coefficient in tails[str(row)]:
        monomial = [int(value) for value in raw_monomial]
        term = e.one()
        for index, exponent in enumerate(monomial[:7]):
            if exponent:
                term = e.mul(term, powers[(index, exponent)])
        for offset, exponent in enumerate(monomial[7:]):
            if exponent:
                if exponent != 1:
                    fail(("nonlinear load", row, monomial))
                term = e.mul(term, e.shift(loads[load_names[offset]], load_delays[offset]))
        out = e.add(out, e.scale(term, Fraction(str(raw_coefficient))))

    schedule = {2: ("mu2", 28, Fraction(1)), 4: ("mu4", 32, Fraction(1)),
                6: ("mu6", 36, Fraction(1)), 7: ("J", 38, Fraction(1, 4))}
    # The only omission mutation used below is the terminal J target.  Earlier
    # targets remain present so the negative control isolates grade 38.
    if row in schedule and not (omit_target and row == 7):
        name, grade, scale = schedule[row]
        out = e.sub(out, e.scale(e.shift(targets[name], grade), scale))
    return out


def compare_rows(
    tails: dict[str, list[list[object]]],
    a: int,
    c: int,
    r: int,
    degree: int,
    ring: Ring,
    mutation: str | None = None,
    omit_total_target: bool = False,
) -> tuple[list[tuple[int, int]], bool]:
    total_f, d1_f, loads, targets = source_pair(a, c, r, degree, ring, mutation)
    primitive_equal = all(total_f[index] == d1_f[index] for index in range(7))
    mismatches: list[tuple[int, int]] = []
    for row in range(1, 8):
        total_row = row_series(tails, row, total_f, loads, targets, degree, ring, omit_total_target)
        d1_row = row_series(tails, row, d1_f, loads, targets, degree, ring, False)
        for grade, (left, right) in enumerate(zip(total_row, d1_row)):
            if left != right:
                mismatches.append((row, grade))
    return mismatches, primitive_equal


def first_mismatch(mismatches: list[tuple[int, int]]) -> tuple[int, int] | None:
    if not mismatches:
        return None
    return min(mismatches, key=lambda pair: (pair[1], pair[0]))


def v0_pins(schema: dict[str, Any]) -> dict[str, Any]:
    if digest(SCHEMA_PATH) != EXPECTED_SCHEMA_SHA256:
        fail("schema hash drift")
    tails_info = schema["tails"]
    tails_path = ROOT / tails_info["path"]
    if digest(tails_path) != tails_info["byte_sha256"]:
        fail("tails byte hash drift")
    tails = json.loads(tails_path.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != tails_info["canonical_sha256"]:
        fail("tails canonical hash drift")
    census = [len(tails[str(row)]) for row in range(1, 8)]
    if census != tails_info["row_census"] or sum(census) != tails_info["total_census"]:
        fail(("tail census drift", census))
    if schema["load_delays_sigma"] != {"k10": 4, "k6": 12, "k2": 20}:
        fail("load-delay drift")
    expected_targets = {"2": ("mu2", 28), "4": ("mu4", 32),
                        "6": ("mu6", 36), "7": ("J", 38)}
    for row, (name, grade) in expected_targets.items():
        if schema["target_schedule"][row]["name"] != name or schema["target_schedule"][row]["grade"] != grade:
            fail(("target schedule drift", row))
    if len(schema["endpoint_families"]) != 11:
        fail("endpoint family count is not eleven")

    witness_count = 0
    for witness in schema["semantic_witnesses"]:
        path = ROOT / witness["path"]
        if digest(path) != witness["sha256"]:
            fail(("semantic witness hash drift", witness["role"]))
        witness_count += 1

    total_source = (ROOT / schema["semantic_witnesses"][0]["path"]).read_text()
    d1_source = (ROOT / schema["semantic_witnesses"][1]["path"]).read_text()
    tail_source = (ROOT / schema["semantic_witnesses"][2]["path"]).read_text()
    for token in ("p_total = \"-2*rho^2+\"", "sigma^2*({series(r_names)}))/4", "sigma^3*(({prefix}p*({az})+({ez}))/2"):
        if token not in total_source:
            fail(("total source semantic token missing", token))
    for token in ("sigma^2*({rz})", "sigma^2*({rc})", "(({pp})*({az}))/2+({cz})"):
        if token not in d1_source:
            fail(("D1 source semantic token missing", token))
    for token in ("LOAD_WEIGHTS = [2, 6, 10]", "Lambda^{lambda_power}", "Lambda^{12 + ell}"):
        if token not in tail_source:
            fail(("tail emitter semantic token missing", token))

    return {
        "schema_sha256": EXPECTED_SCHEMA_SHA256,
        "tails_byte_sha256": tails_info["byte_sha256"],
        "tails_canonical_sha256": tails_info["canonical_sha256"],
        "row_census": census,
        "semantic_witnesses": witness_count,
        "endpoint_families": 11,
    }


def v1_naturality(schema: dict[str, Any], tails: dict[str, Any]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for family in schema["endpoint_families"]:
        test = family["test"]
        modulus = None if test["field"] == "Q" else PRIME
        ring = Ring(modulus)
        mismatches, primitive_equal = compare_rows(
            tails, test["a"], test["c"], test["r"], test["T"], ring
        )
        if mismatches or not primitive_equal:
            fail(("V1 naturality mismatch", family["id"], first_mismatch(mismatches), primitive_equal))
        results.append({
            "family": family["id"],
            "contact": [test["a"], test["c"], test["r"]],
            "T": test["T"],
            "field": test["field"],
            "primitive_equal": True,
            "row_coefficients_compared": 7 * (test["T"] + 1),
        })
    return {"representatives": results, "total_representatives": len(results)}


def generated_alias_map(a: int, c: int, r: int, maxima: dict[str, int]) -> dict[str, str]:
    def total_name(family: str, index: int) -> str:
        fixed = {
            "Az": ["a1", "aa1", "aaa1"], "Ac": ["a0", "aa0", "aaa0"],
            "Cz": ["c1", "e1", "ee1"], "Cc": ["c0", "e0", "ee0"],
            "Bz": ["cs", "cs1", "cs2"], "Bc": ["rs", "rs1", "rs2"],
        }
        if index < 3:
            return fixed[family][index]
        prefix = {"Az": "az", "Ac": "ac", "Cz": "ez", "Cc": "ec", "Bz": "cs", "Bc": "rs"}[family]
        return f"{prefix}{index}"

    out: dict[str, str] = {}
    for family, order, relative_max, factor in (
        ("Az", a, maxima["A"], "1"), ("Ac", a, maxima["A"], "1"),
        ("Cz", c, maxima["C"], "2"), ("Cc", c, maxima["C"], "2"),
        ("Bz", r, maxima["R"], "1"), ("Bc", r, maxima["R"], "4"),
    ):
        for index in range(order):
            out[total_name(family, index)] = "0"
        for relative in range(relative_max + 1):
            total = total_name(family, order + relative)
            d1 = f"{family}D1_{relative}"
            out[total] = d1 if factor == "1" else f"{factor}*{d1}"
    for index in range(1, maxima["p"] + 1):
        out[f"ell{index}"] = f"ell{index}"
    for index in range(maxima["k10"] + 1):
        total = ("k", "k1", "k2c")[index] if index < 3 else f"k10_{index}"
        out[total] = f"k10_{index}"
    for index in range(maxima["k6"] + 1):
        out["k6" if index == 0 else f"k6_{index}"] = f"k6_{index}"
    for index in range(maxima["k2"] + 1):
        out["k2" if index == 0 else f"k2_{index}"] = "k2load" if index == 0 else f"k2load_{index}"
    return out


def check_shifted_root() -> dict[str, Any]:
    depth = 10
    rho = Fraction(3)
    ell = [Fraction(0)] + [Fraction((7 * n) % 11 - 5) for n in range(1, depth + 1)]
    p = [-2 * rho * rho] + [2 * ell[n] for n in range(1, depth + 1)]

    branches: dict[str, list[Fraction]] = {}
    for epsilon in (1, -1):
        lam = [Fraction(epsilon) * rho]
        for n in range(1, depth + 1):
            convolution = sum(lam[i] * lam[n - i] for i in range(1, n))
            lam.append((-ell[n] - convolution) / (2 * lam[0]))
        for n in range(depth + 1):
            coefficient = sum(lam[i] * lam[n - i] for i in range(n + 1)) + p[n] / 2
            if coefficient != 0:
                fail(("Hensel recurrence failure", epsilon, n, coefficient))
        branches[str(epsilon)] = lam
    if branches["-1"] != [-value for value in branches["1"]]:
        fail("deck exchange failure")

    inversion_checks = 0
    map_depth = 3
    for epsilon in ("1", "-1"):
        lam = branches[epsilon]
        az = [Fraction(2 + i) for i in range(map_depth + 1)]
        ac = [Fraction(9 - i) for i in range(map_depth + 1)]
        cz = [Fraction(5 + 2 * i) for i in range(map_depth + 1)]
        cc = [Fraction(4 - i) for i in range(map_depth + 1)]
        bz = [Fraction(7 + i) for i in range(map_depth + 1)]
        bc = [Fraction(3 + 3 * i) for i in range(map_depth + 1)]
        conv_az = [sum(lam[i] * az[n - i] for i in range(n + 1)) for n in range(map_depth + 1)]
        conv_cz = [sum(lam[i] * cz[n - i] for i in range(n + 1)) for n in range(map_depth + 1)]
        conv_bz = [sum(lam[i] * bz[n - i] for i in range(n + 1)) for n in range(map_depth + 1)]
        apl = [ac[n] + conv_az[n] for n in range(map_depth + 1)]
        ami = [ac[n] - conv_az[n] for n in range(map_depth + 1)]
        cpl = [(cc[n] + conv_cz[n]) / 2 for n in range(map_depth + 1)]
        cmi = [(cc[n] - conv_cz[n]) / 2 for n in range(map_depth + 1)]
        rpl = [bc[n] + conv_bz[n] for n in range(map_depth + 1)]
        rmi = [bc[n] - conv_bz[n] for n in range(map_depth + 1)]

        raz: list[Fraction] = []
        rcz: list[Fraction] = []
        rbz: list[Fraction] = []
        for n in range(map_depth + 1):
            target_az = (apl[n] - ami[n]) / 2
            target_cz = cpl[n] - cmi[n]
            target_bz = (rpl[n] - rmi[n]) / 2
            raz.append((target_az - sum(lam[i] * raz[n - i] for i in range(1, n + 1))) / lam[0])
            rcz.append((target_cz - sum(lam[i] * rcz[n - i] for i in range(1, n + 1))) / lam[0])
            rbz.append((target_bz - sum(lam[i] * rbz[n - i] for i in range(1, n + 1))) / lam[0])
        if raz != az or rcz != cz or rbz != bz:
            fail(("shifted root-map inversion failure", epsilon))
        if [(apl[n] + ami[n]) / 2 for n in range(map_depth + 1)] != ac:
            fail("A companion recovery failure")
        if [cpl[n] + cmi[n] for n in range(map_depth + 1)] != cc:
            fail("C companion recovery failure")
        if [(rpl[n] + rmi[n]) / 2 for n in range(map_depth + 1)] != bc:
            fail("R companion recovery failure")
        inversion_checks += 3 * (map_depth + 1)

    return {
        "hensel_depth": depth,
        "deck_branches": 2,
        "shifted_map_depth": map_depth,
        "triangular_inversion_coefficients": inversion_checks,
        "localization": "D(rho)",
        "diagonal_determinants": ["-2*lambda0", "-lambda0/2", "-lambda0/2"],
    }


def v2_mutations(schema: dict[str, Any], tails: dict[str, Any]) -> dict[str, Any]:
    ring = Ring(PRIME)
    expected = {"R_factor_1": 16, "C_factor_1": 15, "drop_ell1": 16}
    fired: dict[str, Any] = {}
    for mutation, grade in expected.items():
        mismatches, primitive_equal = compare_rows(tails, 2, 3, 2, 16, ring, mutation)
        first = first_mismatch(mismatches)
        if primitive_equal or first is None or first[1] != grade:
            fail(("mutation failed", mutation, first, primitive_equal))
        fired[mutation] = {"first_row": first[0], "first_grade": first[1]}

    mismatches, _ = compare_rows(tails, 8, 11, 8, 38, ring, None, omit_total_target=True)
    first = first_mismatch(mismatches)
    if first != (7, 38):
        fail(("target omission mutation failed", first))
    fired["omit_J_target"] = {"first_row": 7, "first_grade": 38}

    current_maxima = schema["support_expectations"]["D23_LOW_A6"]["maxima"]
    alias_map = generated_alias_map(2, 5, 3, current_maxima)
    for stage_zero in ("a1", "a0", "c1", "c0", "cs", "rs"):
        if alias_map.get(stage_zero) != "0":
            fail(("stage-zero mutation firewall failed", stage_zero, alias_map.get(stage_zero)))
    if alias_map.get("k2c") != "k10_2" or alias_map.get("k2") != "k2load":
        fail(("k2c/k2load collision firewall failed", alias_map.get("k2c"), alias_map.get("k2")))
    fired["stage_zero_pairs"] = "rejected_by_generated_lower_ideal"
    fired["k2c_to_k2load"] = "rejected_syntactically"

    endpoints = {item["id"]: item for item in schema["endpoint_families"]}
    for endpoint_id in ("D23_A8D3", "D23_A9", "AGE10_CEILING"):
        test = endpoints[endpoint_id]["test"]
        if test["T"] == 10 + 2 * test["c"]:
            fail(("universal C2 ceiling mutation not rejected", endpoint_id))
    special = endpoints["D23_A8D3"]
    if special["authority"] is not None or special["status"] != "confirmed_but_unpromoted":
        fail("A8D3 lifecycle firewall failed")
    if "analytic-only" not in special["literal_row_policy"]:
        fail("A8D3 analytic-only firewall missing")
    if "rho=0 ramified fibre" not in schema["scope"]["exclusions"]:
        fail("rho=0 relabel firewall missing")
    fired["wrong_C2_ceiling"] = "rejected_at_A8D3_A9_AGE10"
    fired["analytic_only_A8D3"] = "rejected"
    fired["rho0_as_general_rho"] = "rejected"

    root = check_shifted_root()
    return {"mutations": fired, "generated_current_map_entries": len(alias_map), "shifted_root": root}


def derive_support(schema: dict[str, Any], a: int, c: int, r: int, terminal: int) -> dict[str, Any]:
    contacts = {"A": a, "C": c, "R": r}
    arrivals: dict[str, int] = {}
    contents: dict[str, set[str]] = {}
    for primitive in schema["polar_inventory"]:
        grade = primitive["fixed_delay"]
        families: set[str] = set()
        for name, exponent in primitive.get("exponents", {}).items():
            grade += exponent * contacts[name]
            families.add(name)
        if "load" in primitive:
            families.add(primitive["load"])
        arrivals[primitive["name"]] = grade
        contents[primitive["name"]] = families

    maxima: dict[str, int] = {}
    active: set[str] = set()
    for family in ("A", "C", "R", "k10", "k6", "k2"):
        candidates = [terminal - arrivals[name] for name in arrivals
                      if family in contents[name] and arrivals[name] <= terminal]
        if candidates:
            maxima[family] = max(candidates)
            active.add(family)
        else:
            maxima[family] = 0
    polar_candidates = [terminal - grade for grade in arrivals.values() if grade <= terminal]
    maxima["p"] = max(polar_candidates) if polar_candidates else 0
    if polar_candidates:
        active.add("p")
    ordered = {name: maxima[name] for name in ("p", "A", "C", "R", "k10", "k6", "k2")}
    return {"maxima": ordered, "active": sorted(active), "arrivals": arrivals}


def v3_support(schema: dict[str, Any]) -> dict[str, Any]:
    checked: list[dict[str, Any]] = []
    for endpoint in schema["endpoint_families"]:
        test = endpoint["test"]
        actual = derive_support(schema, test["a"], test["c"], test["r"], test["T"])
        expected = schema["support_expectations"][endpoint["id"]]
        if actual["maxima"] != expected["maxima"] or set(actual["active"]) != set(expected["active"]):
            fail(("support expectation mismatch", endpoint["id"], actual, expected))
        checked.append({"family": endpoint["id"], "maxima": actual["maxima"], "active": actual["active"]})
    for sentinel in schema["support_sentinels"]:
        actual = derive_support(schema, sentinel["a"], sentinel["c"], sentinel["r"], sentinel["T"])
        if actual["maxima"] != sentinel["maxima"] or set(actual["active"]) != set(sentinel["active"]):
            fail(("support sentinel mismatch", sentinel["id"], actual, sentinel))
        checked.append({"family": sentinel["id"], "maxima": actual["maxima"], "active": actual["active"]})
    current = next(item for item in checked if item["family"] == "D23_LOW_A6")
    if current["maxima"] != {"p": 3, "A": 3, "C": 3, "R": 1, "k10": 2, "k6": 0, "k2": 0}:
        fail("G20 current maxima regression")
    return {
        "tables_checked": len(checked),
        "current_G20_maxima": current["maxima"],
        "raw_bound_policy": "cancellation only raises valuation; raw census over-retains; useful P bound consumes reviewed first polar grade",
        "details": checked,
    }


def v4_provenance(schema: dict[str, Any]) -> dict[str, Any]:
    checked = 0
    promoted = 0
    conditional = 0
    for endpoint in schema["endpoint_families"]:
        for key in ("authority", "review", "parent_authority", "parent_review", "rejected_route"):
            artifact = endpoint.get(key)
            if artifact is None:
                continue
            path = ROOT / artifact["path"]
            if digest(path) != artifact["sha256"]:
                fail(("endpoint provenance hash drift", endpoint["id"], key))
            checked += 1
        if endpoint["status"] == "promoted":
            authority = endpoint.get("authority")
            if authority is None or "PROMOTED" not in (ROOT / authority["path"]).read_text()[:1200]:
                fail(("promoted endpoint lacks pinned promoted status", endpoint["id"]))
            promoted += 1
        elif endpoint["status"] == "confirmed_but_unpromoted":
            if endpoint.get("authority") is not None:
                fail("conditional endpoint has an authority")
            review_text = (ROOT / endpoint["review"]["path"]).read_text()[:2000]
            route_text = (ROOT / endpoint["rejected_route"]["path"]).read_text()[:1200]
            if "CONFIRMED" not in review_text or "PROMOTED ROUTE FALSIFICATION ONLY" not in route_text:
                fail("A8D3 exact status provenance failed")
            conditional += 1
        else:
            fail(("unknown endpoint lifecycle", endpoint["id"], endpoint["status"]))
    if promoted != 10 or conditional != 1:
        fail(("endpoint lifecycle census", promoted, conditional))
    return {"artifacts_hash_checked": checked, "promoted_families": promoted,
            "confirmed_but_unpromoted_families": conditional,
            "filename_inference": "forbidden"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    schema = json.loads(SCHEMA_PATH.read_text())
    tails_path = ROOT / schema["tails"]["path"]
    tails = json.loads(tails_path.read_text())
    checks = {
        "V0_pins": v0_pins(schema),
        "V1_naturality": v1_naturality(schema, tails),
        "V2_mutations_and_shifted_root": v2_mutations(schema, tails),
        "V3_support": v3_support(schema),
        "V4_provenance": v4_provenance(schema),
    }
    result = {
        "status": "PASS-UNIFORM-CONTACT-NATURALITY-V46-V0-V4",
        "scope": "desk verifier for normative schema; endpoint union remains conditional at D23_A8D3",
        "schema_sha256": EXPECTED_SCHEMA_SHA256,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "checks": checks,
    }
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
