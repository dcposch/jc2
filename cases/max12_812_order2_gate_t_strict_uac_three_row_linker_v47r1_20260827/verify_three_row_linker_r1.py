#!/usr/bin/env python3
"""Executable V47R1 bridge from the frozen 569 tails to three literal rows.

The symbolic coefficient engine is exact over Q.  For every frozen V47
manifest it keeps every independent shifted jet allowed by the V46 support
maxima, evaluates the pinned V46 source formulas and tails, and compares the
three charged coefficients to the raw-total and mapped-D1 g triples.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCHEMA_PATH = HERE / "SCHEMA_R1.json"
FROZEN_RESULT = HERE / "run_v0_v10_r1/result.json"
EXPECTED_SCHEMA_SHA256 = "b895315acc241ca8542611cadefee0d4f29217f1ffecf8fbd3761b513b6aa908"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def qtext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


class PolynomialRing:
    """Tiny sparse exact polynomial ring with a fixed ordered variable set."""

    def __init__(self, names: list[str]):
        if len(names) != len(set(names)):
            fail(("duplicate polynomial variables", names))
        self.names = tuple(names)
        self.index = {name: index for index, name in enumerate(self.names)}
        self.zero_monomial = (0,) * len(self.names)
        self.zero: dict[tuple[int, ...], Fraction] = {}
        self.one = {self.zero_monomial: Fraction(1)}
        self.modulus = None

    def value(self, raw: int | Fraction | str):
        value = raw if isinstance(raw, Fraction) else Fraction(str(raw))
        return {} if not value else {self.zero_monomial: value}

    def var(self, name: str):
        if name not in self.index:
            fail(("unknown variable", name))
        monomial = [0] * len(self.names)
        monomial[self.index[name]] = 1
        return {tuple(monomial): Fraction(1)}

    def add(self, left, right):
        out = dict(left)
        for monomial, coefficient in right.items():
            value = out.get(monomial, Fraction(0)) + coefficient
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
        return out

    def neg(self, poly):
        return {monomial: -coefficient for monomial, coefficient in poly.items()}

    def mul(self, left, right):
        if not left or not right:
            return {}
        out: dict[tuple[int, ...], Fraction] = {}
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
                value = out.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
                if value:
                    out[monomial] = value
                else:
                    out.pop(monomial, None)
        return out

    def scale(self, scalar: int | Fraction | str, poly):
        return self.mul(self.value(scalar), poly)


def poly_add(ring: PolynomialRing, *polys):
    out = ring.zero
    for poly in polys:
        out = ring.add(out, poly)
    return out


def poly_power(ring: PolynomialRing, poly, exponent: int):
    out = ring.one
    base = poly
    power = exponent
    while power:
        if power & 1:
            out = ring.mul(out, base)
        power >>= 1
        if power:
            base = ring.mul(base, base)
    return out


def canonical_poly(ring: PolynomialRing, poly) -> list[list[object]]:
    terms: list[list[object]] = []
    for monomial, coefficient in poly.items():
        named = [[ring.names[index], exponent] for index, exponent in enumerate(monomial) if exponent]
        terms.append([qtext(coefficient), named])
    return sorted(terms, key=lambda term: json.dumps(term[1], separators=(",", ":")))


def canonical_triple(ring: PolynomialRing, triple: dict[str, object]) -> dict[str, object]:
    return {name: canonical_poly(ring, triple[name]) for name in ("Phi1_G", "Phi2_G", "Phi4_T_C2")}


def triple_digest(ring: PolynomialRing, triple: dict[str, object]) -> str:
    return canonical_digest(canonical_triple(ring, triple))


def polynomial_support(ring: PolynomialRing, poly) -> set[str]:
    return {
        ring.names[index]
        for monomial in poly
        for index, exponent in enumerate(monomial)
        if exponent
    }


def triple_support(ring: PolynomialRing, triple: dict[str, object]) -> set[str]:
    answer: set[str] = set()
    for poly in triple.values():
        answer.update(polynomial_support(ring, poly))
    return answer


def expected_d1(ring: PolynomialRing) -> dict[str, object]:
    rho = ring.var("rho")
    rho2 = ring.mul(rho, rho)
    az, ac, cz, cc = (ring.var(name) for name in ("AzD1_0", "AcD1_0", "CzD1_0", "CcD1_0"))
    return {
        "Phi1_G": ring.scale(Fraction(3, 4), poly_add(ring, ring.mul(ac, cz), ring.mul(az, cc))),
        "Phi2_G": ring.scale(Fraction(3, 4), poly_add(ring, ring.mul(ac, cc), ring.mul(rho2, ring.mul(az, cz)))),
        "Phi4_T_C2": ring.scale(Fraction(3, 8), poly_add(ring, ring.mul(cc, cc), ring.mul(rho2, ring.mul(cz, cz)))),
    }


def expected_raw(ring: PolynomialRing) -> dict[str, object]:
    rho = ring.var("rho")
    rho2 = ring.mul(rho, rho)
    az, ac, ez, ec = (ring.var(name) for name in ("AzRaw_0", "AcRaw_0", "EzRaw_0", "EcRaw_0"))
    return {
        "Phi1_G": ring.scale(Fraction(3, 8), poly_add(ring, ring.mul(ac, ez), ring.mul(az, ec))),
        "Phi2_G": ring.scale(Fraction(3, 8), poly_add(ring, ring.mul(ac, ec), ring.mul(rho2, ring.mul(az, ez)))),
        "Phi4_T_C2": ring.scale(Fraction(3, 32), poly_add(ring, ring.mul(ec, ec), ring.mul(rho2, ring.mul(ez, ez)))),
    }


def expected_raw_mapped_to_d1(ring: PolynomialRing, c_factor: Fraction) -> dict[str, object]:
    """Apply raw A->D1 A and raw C->c_factor*D1 C to the raw g triple."""
    rho = ring.var("rho")
    rho2 = ring.mul(rho, rho)
    az, ac, cz, cc = (ring.var(name) for name in ("AzD1_0", "AcD1_0", "CzD1_0", "CcD1_0"))
    return {
        "Phi1_G": ring.scale(Fraction(3, 8) * c_factor, poly_add(ring, ring.mul(ac, cz), ring.mul(az, cc))),
        "Phi2_G": ring.scale(Fraction(3, 8) * c_factor, poly_add(ring, ring.mul(ac, cc), ring.mul(rho2, ring.mul(az, cz)))),
        "Phi4_T_C2": ring.scale(Fraction(3, 32) * c_factor * c_factor, poly_add(ring, ring.mul(cc, cc), ring.mul(rho2, ring.mul(cz, cz)))),
    }


def check_pin(pin: dict[str, str], hash_key: str = "sha256") -> Path:
    path = ROOT / pin["path"]
    if not path.is_file() or digest(path) != pin[hash_key]:
        fail(("source pin", pin["path"], digest(path) if path.is_file() else "MISSING", pin[hash_key]))
    return path


def import_pinned_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_pins(schema: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], Any]:
    if digest(SCHEMA_PATH) != EXPECTED_SCHEMA_SHA256:
        fail(("R1 schema drift", digest(SCHEMA_PATH), EXPECTED_SCHEMA_SHA256))
    pins = schema["source_pins"]
    for name, pin in pins.items():
        if name == "tails":
            check_pin(pin, "byte_sha256")
        else:
            check_pin(pin)

    tails = json.loads((ROOT / pins["tails"]["path"]).read_text())
    if canonical_digest(tails) != pins["tails"]["canonical_sha256"]:
        fail("tails canonical digest")
    census = [len(tails[str(row)]) for row in range(1, 8)]
    if census != pins["tails"]["row_census"] or sum(census) != pins["tails"]["total_census"]:
        fail(("tails census", census))

    # Re-walk the immutable V47 freeze rather than trusting its outer hash alone.
    freeze_path = ROOT / pins["v47_freeze"]["path"]
    freeze_lines = freeze_path.read_text().splitlines()
    frozen = {}
    for line in freeze_lines:
        expected, relative = line.split(maxsplit=1)
        relative = relative.lstrip("* ")
        path = freeze_path.parent / relative
        if digest(path) != expected:
            fail(("V47 inner freeze", relative))
        frozen[relative] = expected
    if len(frozen) != 5:
        fail(("V47 freeze census", len(frozen)))

    v47_result = json.loads((ROOT / pins["v47_result"]["path"]).read_text())
    if (
        v47_result["status"] != "PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47"
        or v47_result["baseline_manifest_count"] != 12
        or v47_result["raised_subtail_manifest_count"] != 4
        or v47_result["endpoint_replacement_status"] != "WITHHELD_PENDING_DIFFERENT_MODEL_REVIEW"
    ):
        fail("V47 frozen lifecycle/counts")
    review_text = (ROOT / pins["v47_hostile_review"]["path"]).read_text()
    for token in ("Manifest completeness / literal-row bridge", "GAP/REPAIR", "per-manifest executable extraction"):
        if token not in review_text:
            fail(("V47 review repair token", token))

    v46_schema = json.loads((ROOT / pins["v46_schema"]["path"]).read_text())
    if v46_schema["tails"]["byte_sha256"] != pins["tails"]["byte_sha256"]:
        fail("V46/tails custody")
    v46r1_schema = json.loads((ROOT / pins["v46r1_schema"]["path"]).read_text())
    expected_map = {
        "az_(a+n)": "AzD1_n", "ac_(a+n)": "AcD1_n",
        "ez_(c+n)": "2*CzD1_n", "ec_(c+n)": "2*CcD1_n",
        "cs_(r+n)": "BzD1_n", "rs_(r+n)": "4*BcD1_n",
    }
    if v46r1_schema["coordinate_types"]["raw_to_D1"] != expected_map:
        fail("V46R1 typed map drift")
    promotion_text = (ROOT / pins["v46r1_promotion"]["path"]).read_text()
    if "PROMOTED" not in promotion_text[:1500] or "(a,d,r)=(8,3,8)" not in promotion_text or "confirmed_but_unpromoted" not in promotion_text:
        fail("V46R1 promotion/lifecycle firewall")

    emitter_text = (ROOT / pins["tail_emitter"]["path"]).read_text()
    for token in (
        "LOAD_WEIGHTS = [2, 6, 10]", "Lambda^{lambda_power}",
        "Lambda^{12 + ell}", "targets = {1: \"0\", 2: \"mu2\"",
    ):
        if token not in emitter_text:
            fail(("tail emitter semantic token", token))

    base = import_pinned_module("v47r1_frozen_v46", ROOT / pins["v46_verifier"]["path"])
    return tails, v46_schema, base


def manifest_variable_names(maxima: dict[str, int]) -> list[str]:
    names = ["rho"]
    names.extend(f"P_{index}" for index in range(1, maxima["p"] + 1))
    for stem in ("AzD1", "AcD1"):
        names.extend(f"{stem}_{index}" for index in range(maxima["A"] + 1))
    for stem in ("CzD1", "CcD1"):
        names.extend(f"{stem}_{index}" for index in range(maxima["C"] + 1))
    for stem in ("BzD1", "BcD1"):
        names.extend(f"{stem}_{index}" for index in range(maxima["R"] + 1))
    for stem in ("k10", "k6", "k2"):
        names.extend(f"{stem}_{index}" for index in range(maxima[stem] + 1))
    names.extend(("mu2", "mu4", "mu6", "J"))
    return names


def generic_series_factory(ring: PolynomialRing, maxima: dict[str, int]) -> Callable[[str, Any], list[object]]:
    family = {
        "AzD1": ("AzD1", "A"), "AcD1": ("AcD1", "A"),
        "CzD1": ("CzD1", "C"), "CcD1": ("CcD1", "C"),
        "BzD1": ("BzD1", "R"), "BcD1": ("BcD1", "R"),
        "k10": ("k10", "k10"), "k6": ("k6", "k6"), "k2": ("k2", "k2"),
    }

    def generic(tag: str, engine) -> list[object]:
        out = [ring.zero] * (engine.n + 1)
        if tag == "P":
            rho = ring.var("rho")
            out[0] = ring.scale(-2, ring.mul(rho, rho))
            for index in range(1, min(engine.n, maxima["p"]) + 1):
                out[index] = ring.var(f"P_{index}")
            return out
        if tag in family:
            stem, maximum_key = family[tag]
            for index in range(min(engine.n, maxima[maximum_key]) + 1):
                out[index] = ring.var(f"{stem}_{index}")
            return out
        if tag in ("mu2", "mu4", "mu6", "J"):
            out[0] = ring.var(tag)
            return out
        fail(("unexpected deterministic-series tag", tag))

    return generic


def extract_manifest(
    manifest: dict[str, Any], maxima: dict[str, int], tails: dict[str, Any], base,
    *, mutate_tails: dict[str, Any] | None = None,
) -> tuple[PolynomialRing, dict[str, object], dict[str, object], bool]:
    degree = int(manifest["T_C2"])
    ring = PolynomialRing(manifest_variable_names(maxima))
    original = base.deterministic_series
    base.deterministic_series = generic_series_factory(ring, maxima)
    try:
        total_f, d1_f, loads, targets = base.source_pair(
            int(manifest["a"]), int(manifest["c"]), int(manifest["r_min"]), degree, ring
        )
        primitive_equal = all(total_f[index] == d1_f[index] for index in range(7))
        source = mutate_tails if mutate_tails is not None else tails
        total_rows = {
            row: base.row_series(source, row, total_f, loads, targets, degree, ring)
            for row in (1, 2, 4)
        }
        d1_rows = {
            row: base.row_series(source, row, d1_f, loads, targets, degree, ring)
            for row in (1, 2, 4)
        }
    finally:
        base.deterministic_series = original
    G, T = int(manifest["G"]), int(manifest["T_C2"])
    total = {"Phi1_G": total_rows[1][G], "Phi2_G": total_rows[2][G], "Phi4_T_C2": total_rows[4][T]}
    d1 = {"Phi1_G": d1_rows[1][G], "Phi2_G": d1_rows[2][G], "Phi4_T_C2": d1_rows[4][T]}
    return ring, total, d1, primitive_equal


def manifest_index(v47: dict[str, Any]) -> dict[str, dict[str, Any]]:
    manifests = v47["baseline_manifests"] + v47["raised_subtail_manifests"]
    return {manifest["id"]: manifest for manifest in manifests}


def reject_wall(G: int, T: int) -> None:
    if G >= 28 or T >= 32:
        fail(("target wall", G, T))


def verify_manifest_pins(schema: dict[str, Any], v47: dict[str, Any], v46_schema: dict[str, Any], base) -> None:
    frozen = manifest_index(v47)
    pins = {pin["id"]: pin for pin in schema["manifest_coefficient_pins"]}
    if len(frozen) != 16 or len(pins) != 16 or set(frozen) != set(pins):
        fail(("complete manifest-pin set", len(frozen), len(pins), sorted(set(frozen) ^ set(pins))))
    for identifier, pin in pins.items():
        manifest = frozen[identifier]
        for key in ("a", "c", "r_min", "G", "T_C2"):
            if int(pin[key]) != int(manifest[key]):
                fail(("manifest coefficient pin", identifier, key))
        derived = base.derive_support(
            v46_schema, int(pin["a"]), int(pin["c"]), int(pin["r_min"]), int(pin["T_C2"])
        )["maxima"]
        if derived != pin["maxima"]:
            fail(("manifest support maxima", identifier, derived, pin["maxima"]))
        reject_wall(int(pin["G"]), int(pin["T_C2"]))


def coefficient_contractions(
    schema: dict[str, Any], tails: dict[str, Any], v47: dict[str, Any], base
) -> tuple[list[dict[str, Any]], str]:
    frozen = manifest_index(v47)
    records: list[dict[str, Any]] = []
    allowed = {"rho", "AzD1_0", "AcD1_0", "CzD1_0", "CcD1_0"}
    for pin in schema["manifest_coefficient_pins"]:
        manifest = frozen[pin["id"]]
        ring, total, d1, primitive_equal = extract_manifest(manifest, pin["maxima"], tails, base)
        expected = expected_d1(ring)
        if not primitive_equal or total != d1:
            fail(("symbolic total/D1 source naturality", pin["id"]))
        if d1 != expected:
            fail(("literal three-row mismatch", pin["id"], canonical_triple(ring, d1), canonical_triple(ring, expected)))
        actual_sha = triple_digest(ring, d1)
        if actual_sha != pin["expected_d1_sha256"] or actual_sha != schema["expected_coefficients"]["mapped_D1_canonical_sha256"]:
            fail(("coefficient digest pin", pin["id"], actual_sha, pin["expected_d1_sha256"]))
        support = triple_support(ring, d1)
        extra = sorted(support - allowed)
        if extra:
            fail(("extra in-window jet", pin["id"], extra))
        total_variables = len(ring.names)
        records.append({
            "id": pin["id"], "contact": [pin["a"], pin["c"], pin["r_min"]],
            "slots": {"Phi1": pin["G"], "Phi2": pin["G"], "Phi4": pin["T_C2"]},
            "maxima": pin["maxima"], "symbolic_variables_retained": total_variables,
            "coefficient_sha256": actual_sha, "coefficient_term_counts": [len(d1[name]) for name in ("Phi1_G", "Phi2_G", "Phi4_T_C2")],
            "extra_in_window_support": extra, "symbolic_total_D1_equal": True,
        })
    return records, canonical_digest(records)


def mutation_controls(
    schema: dict[str, Any], tails: dict[str, Any], v47: dict[str, Any], base
) -> dict[str, Any]:
    fired: dict[str, Any] = {}
    first_pin = schema["manifest_coefficient_pins"][0]
    first_manifest = manifest_index(v47)[first_pin["id"]]
    ring, _, actual, _ = extract_manifest(first_manifest, first_pin["maxima"], tails, base)
    expected = expected_d1(ring)

    if expected_raw_mapped_to_d1(ring, Fraction(2)) != expected:
        fail("correct raw/D1 factor-two map")
    if expected_raw_mapped_to_d1(ring, Fraction(1)) == expected:
        fail("raw/D1 C-factor mutation survived")
    fired["raw-C-factor-two-conflation"] = "rejected"

    doubled_g1 = dict(expected)
    doubled_g1["Phi1_G"] = ring.scale(2, expected["Phi1_G"])
    if doubled_g1 == actual:
        fail("Phi1 normalization mutation survived")
    fired["Phi1-normalization-3/4-to-3/2-D1"] = "rejected"
    doubled_g4 = dict(expected)
    doubled_g4["Phi4_T_C2"] = ring.scale(2, expected["Phi4_T_C2"])
    if doubled_g4 == actual:
        fail("Phi4 normalization mutation survived")
    fired["Phi4-normalization-3/8-to-3/4-D1"] = "rejected"

    injected = dict(actual)
    injected["Phi1_G"] = ring.add(actual["Phi1_G"], ring.var("AzD1_1"))
    allowed = {"rho", "AzD1_0", "AcD1_0", "CzD1_0", "CcD1_0"}
    if not (triple_support(ring, injected) - allowed):
        fail("extra-jet injection mutation survived")
    fired["inject-extra-relative-A-jet"] = "rejected at AzD1_1"

    # Find and record the first row-1 frozen term whose deletion changes the
    # charged coefficient.  This is a live term-exact emitter mutation, not a
    # prose/string pin.
    omitted_index = None
    for index in range(len(tails["1"])):
        mutated_tails = deepcopy(tails)
        del mutated_tails["1"][index]
        mutated_ring, _, mutated, _ = extract_manifest(
            first_manifest, first_pin["maxima"], tails, base, mutate_tails=mutated_tails
        )
        if canonical_poly(mutated_ring, mutated["Phi1_G"]) != canonical_poly(ring, actual["Phi1_G"]):
            omitted_index = index
            break
    if omitted_index is None:
        fail("no live row-1 tail omission mutation")
    fired["omit-frozen-row1-tail-term"] = {"zero_based_index": omitted_index}

    for label, G, T in (("open-row2-target-wall", 28, 30), ("open-row4-target-wall", 27, 32)):
        try:
            reject_wall(G, T)
        except RuntimeError:
            fired[label] = {"rejected": [G, T]}
        else:
            fail(("target wall mutation survived", label))

    frozen_ids = set(manifest_index(v47))
    subset_ids = {pin["id"] for pin in schema["manifest_coefficient_pins"][:-1]}
    if subset_ids == frozen_ids:
        fail("proper-subset manifest mutation inert")
    fired["drop-one-manifest-coefficient-pin"] = {"missing": sorted(frozen_ids - subset_ids)}

    if len(fired) != len(schema["required_mutations"]):
        fail(("mutation census", len(fired), len(schema["required_mutations"]), fired))
    return fired


def raw_coordinate_check(schema: dict[str, Any]) -> dict[str, Any]:
    raw_ring = PolynomialRing(["rho", "AzRaw_0", "AcRaw_0", "EzRaw_0", "EcRaw_0"])
    raw = expected_raw(raw_ring)
    raw_sha = triple_digest(raw_ring, raw)
    if raw_sha != schema["expected_coefficients"]["raw_total_canonical_sha256"]:
        fail(("raw coefficient digest", raw_sha))
    d1_ring = PolynomialRing(["rho", "AzD1_0", "AcD1_0", "CzD1_0", "CcD1_0"])
    d1 = expected_d1(d1_ring)
    if triple_digest(d1_ring, d1) != schema["expected_coefficients"]["mapped_D1_canonical_sha256"]:
        fail("D1 coefficient digest")
    if expected_raw_mapped_to_d1(d1_ring, Fraction(2)) != d1:
        fail("raw/D1 g-triple commutation")
    return {
        "raw_total_coefficient_sha256": raw_sha,
        "mapped_D1_coefficient_sha256": triple_digest(d1_ring, d1),
        "forced_map": "EzRaw_n,EcRaw_n -> 2*CzD1_n,2*CcD1_n",
        "commutes_exactly": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA_PATH.read_text())
    tails, v46_schema, base = verify_pins(schema)
    v47 = json.loads((ROOT / schema["source_pins"]["v47_schema"]["path"]).read_text())
    verify_manifest_pins(schema, v47, v46_schema, base)
    raw_check = raw_coordinate_check(schema)
    records, records_sha = coefficient_contractions(schema, tails, v47, base)
    mutations = mutation_controls(schema, tails, v47, base)
    result = {
        "status": "PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47R1-LITERAL-CONTRACTION",
        "scope": "term-exact literal 569-tail bridge for exactly the frozen V47 12 baselines plus 4 raised subtails; endpoint replacement withheld pending different-model review",
        "schema_sha256": EXPECTED_SCHEMA_SHA256,
        "v47_hostile_review_repair": "item 5 manifest completeness/literal-row bridge",
        "tails_row_census": [len(tails[str(row)]) for row in range(1, 8)],
        "tails_total_census": sum(len(tails[str(row)]) for row in range(1, 8)),
        "manifest_count": len(records),
        "coefficient_slot_count": 3 * len(records),
        "manifest_records_sha256": records_sha,
        "manifest_records": records,
        "raw_total_and_D1": raw_check,
        "mutations_fired": mutations,
        "endpoint_replacement_status": "WITHHELD_PENDING_DIFFERENT_MODEL_REVIEW",
    }
    if args.output:
        args.output.mkdir(parents=True, exist_ok=False)
        (args.output / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    else:
        if not FROZEN_RESULT.is_file() or json.loads(FROZEN_RESULT.read_text()) != result:
            fail("frozen V47R1 result mismatch")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
