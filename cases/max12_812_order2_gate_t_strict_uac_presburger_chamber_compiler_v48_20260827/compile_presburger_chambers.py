#!/usr/bin/env python3
"""Desk compiler for the bounded V48 strict unique-AC Presburger chamber.

The primitive universe is generated before the frozen V47 manifests are read.
The latter are comparison/custody data only.  This compiler proves no fan cover.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import importlib.util
from itertools import product
import json
import math
from pathlib import Path


CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
SCHEMA_PATH = CASE / "SCHEMA.json"
FROZEN_PATH = CASE / "COMPILED.json"
SIGNATURE_KEYS = (
    "summand", "load", "fixed_sigma", "R", "A", "C", "pole",
    "coefficient", "first_grade",
)


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_digest(value: object) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(data).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def binomial(alpha: Fraction, degree: int) -> Fraction:
    out = Fraction(1)
    for index in range(degree):
        out *= alpha - index
    return out / math.factorial(degree)


def signature_record(key: tuple[object, ...], coefficient: Fraction) -> dict[str, object]:
    summand, load, fixed, rp, ap, cp, pole = key
    return {
        "summand": summand, "load": load, "fixed_sigma": int(fixed),
        "R": int(rp), "A": int(ap), "C": int(cp), "pole": int(pole),
        "coefficient": fraction_text(coefficient),
    }


def signature_tuple(item: dict[str, object], include_grade: bool = False) -> tuple[object, ...]:
    keys = SIGNATURE_KEYS if include_grade else SIGNATURE_KEYS[:-1]
    return tuple(item[key] for key in keys)


def generate_universe(schema: dict[str, object], pad: int = 0):
    """Aggregate every route whose fixed delay is <= the universal cap."""
    cap = int(schema["universal_grade_cap"])
    atoms = schema["atoms"]
    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    routes: defaultdict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for summand in schema["summands"]:
        alpha = Fraction(str(summand["alpha"]))
        summand_fixed = int(summand["fixed"])
        bounds = [(cap - summand_fixed) // int(atom["fixed"]) + pad for atom in atoms]
        for counts in product(*(range(bound + 1) for bound in bounds)):
            degree = sum(counts)
            if degree == 0:
                continue
            fixed = summand_fixed + sum(count * int(atom["fixed"]) for count, atom in zip(counts, atoms))
            if fixed > cap:
                continue
            denominator = sum(count * int(atom["denominator"]) for count, atom in zip(counts, atoms))
            pole = denominator - int(4 * alpha)
            if pole <= 0:
                continue
            powers = {
                stem: sum(count * int(atom[stem]) for count, atom in zip(counts, atoms))
                for stem in ("R", "A", "C")
            }
            scalar = math.prod(int(atom["scalar"]) ** count for count, atom in zip(counts, atoms))
            multinomial = math.factorial(degree)
            for count in counts:
                multinomial //= math.factorial(count)
            coefficient = binomial(alpha, degree) * multinomial * scalar
            key = (
                summand["id"], summand["load"], fixed,
                powers["R"], powers["A"], powers["C"], pole,
            )
            aggregate[key] += coefficient
            routes[key].append({
                "counts": list(counts), "coefficient": fraction_text(coefficient),
            })
    nonzero = [signature_record(key, value) for key, value in aggregate.items() if value]
    nonzero.sort(key=lambda item: tuple(str(item[key]) for key in SIGNATURE_KEYS[:-1]))
    cancelled = []
    for key, value in aggregate.items():
        if value:
            continue
        record = signature_record(key, value)
        record["routes"] = routes[key]
        cancelled.append(record)
    cancelled.sort(key=lambda item: tuple(str(item.get(key)) for key in SIGNATURE_KEYS[:-1]))
    return nonzero, cancelled


def pin_sources(schema: dict[str, object]) -> None:
    for name, pin in schema["source_pins"].items():
        path = ROOT / pin["path"]
        if not path.is_file() or digest(path) != pin["sha256"]:
            fail(("source pin", name, str(path)))
    for name in ("v47_freeze", "v47r1_freeze"):
        freeze = ROOT / schema["source_pins"][name]["path"]
        for line in freeze.read_text().splitlines():
            expected, relative = line.split(None, 1)
            target = freeze.parent / relative.strip()
            if not target.is_file() or digest(target) != expected:
                fail(("inner freeze", name, relative))


def validate_generation(schema, universe, cancelled) -> None:
    padded, padded_cancelled = generate_universe(schema, pad=1)
    if universe != padded or cancelled != padded_cancelled:
        fail("universal pad+1 instability")
    if len(universe) != 425 or len(cancelled) != 40:
        fail(("universal census", len(universe), len(cancelled)))

    aggregation_keys = tuple(schema["aggregation_key"])
    cancel_index = {tuple(item[key] for key in aggregation_keys): item for item in cancelled}
    for expected in schema["required_cancellations"]:
        key = tuple(expected[field] for field in aggregation_keys)
        if key not in cancel_index:
            fail(("missing cancellation", expected))
        routes = sorted(route["coefficient"] for route in cancel_index[key]["routes"])
        if routes != sorted(expected["routes"]):
            fail(("cancellation routes", expected, routes))

    allowed = schema["allowed_primitives"]
    index = {signature_tuple(item): item for item in universe}
    for name in ("AC", "C2"):
        if signature_tuple(allowed[name]) not in index:
            fail(("allowed primitive missing", name))

    # V46 is a source-side sanity witness, not the compiler's primitive list.
    v46 = json.loads((ROOT / schema["source_pins"]["v46_schema"]["path"]).read_text())
    for polar in v46["polar_inventory"]:
        matches = [item for item in universe if (
            item["summand"] == (polar.get("load") or "unloaded")
            and item["load"] == polar.get("load")
            and item["fixed_sigma"] == polar["fixed_delay"]
            and all(item[stem] == polar.get("exponents", {}).get(stem, 0) for stem in ("R", "A", "C"))
        )]
        if len(matches) != 1:
            fail(("V46 polar template", polar, matches))


def with_grade(item: dict[str, object], a: int, c: int, r: int) -> dict[str, object]:
    out = dict(item)
    out["first_grade"] = (
        int(item["fixed_sigma"]) + r * int(item["R"])
        + a * int(item["A"]) + c * int(item["C"])
    )
    return out


def inventory(universe, a: int, c: int, r: int, maximum: int) -> list[dict[str, object]]:
    out = [with_grade(item, a, c, r) for item in universe]
    out = [item for item in out if int(item["first_grade"]) <= maximum]
    return sorted(out, key=lambda item: tuple(str(item[key]) for key in SIGNATURE_KEYS))


def bad_kind(item: dict[str, object]) -> str:
    core = (item["summand"], item["load"], item["fixed_sigma"], item["R"], item["A"], item["C"], item["pole"])
    if core == ("unloaded", None, 12, 1, 2, 0, 2):
        return "RA2"
    if core == ("unloaded", None, 15, 0, 3, 0, 3):
        return "A3"
    return "OTHER_GLOBAL_POLE"


def classify(schema, universe, a: int, c: int, r: int, disabled=frozenset()):
    allowed = schema["allowed_primitives"]
    ac_sig, c2_sig = signature_tuple(allowed["AC"]), signature_tuple(allowed["C2"])
    G, T = 10 + a + c, 10 + 2 * c
    inv = inventory(universe, a, c, r, T)
    initial = [item for item in inv if int(item["first_grade"]) <= G]
    reasons: list[str] = []
    witnesses: dict[str, list[dict[str, object]]] = {}
    if "NONUNIQUE_G" not in disabled:
        if len(initial) != 1 or signature_tuple(initial[0]) != ac_sig or int(initial[0]["first_grade"]) != G:
            reasons.append("NONUNIQUE_G")
            witnesses["NONUNIQUE_G"] = [item for item in initial if signature_tuple(item) != ac_sig]

    c2 = [item for item in inv if signature_tuple(item) == c2_sig]
    if len(c2) != 1 or int(c2[0]["first_grade"]) != T:
        reasons.append("C2_PIN")
        witnesses["C2_PIN"] = c2

    bad = [item for item in inv if int(item["pole"]) >= 2 and signature_tuple(item) != c2_sig]
    bad = [item for item in bad if bad_kind(item) not in disabled]
    if bad:
        kinds = {bad_kind(item) for item in bad}
        if "RA2" in kinds:
            reasons.append("RA2")
            witnesses["RA2"] = [item for item in bad if bad_kind(item) == "RA2"]
        if "A3" in kinds:
            reasons.append("A3")
            witnesses["A3"] = [item for item in bad if bad_kind(item) == "A3"]
        if not ({"RA2", "A3"} & kinds):
            reasons.append("OTHER_GLOBAL_POLE")
            witnesses["OTHER_GLOBAL_POLE"] = bad
    if G >= 28 and "G_TARGET_WALL" not in disabled:
        reasons.append("G_TARGET_WALL")
        witnesses["G_TARGET_WALL"] = [{"G": G, "required": "G<28"}]
    if T >= 32 and "T_TARGET_WALL" not in disabled:
        reasons.append("T_TARGET_WALL")
        witnesses["T_TARGET_WALL"] = [{"T_C2": T, "required": "T_C2<32"}]
    return not reasons, reasons, witnesses, inv


def required_bound(item: dict[str, object], a: int, c: int, rhs: int) -> int | None:
    """Smallest r making fixed+Rr+Aa+Cc > rhs; None means persistent fail."""
    constant = int(item["fixed_sigma"]) + a * int(item["A"]) + c * int(item["C"])
    rp = int(item["R"])
    if rp == 0:
        return 0 if constant > rhs else None
    return max(0, (rhs - constant) // rp + 1)


def compile_threshold(schema, universe, a: int, d: int, r0: int):
    c, G, T = a + d, 10 + 2 * a + d, 10 + 2 * a + 2 * d
    if G >= 28 or T >= 32:
        return None, [{"kind": "TARGET", "G": G, "T_C2": T}]
    ac_sig = signature_tuple(schema["allowed_primitives"]["AC"])
    c2_sig = signature_tuple(schema["allowed_primitives"]["C2"])
    bound, persistent = r0, []
    facets = []
    for item in universe:
        sig = signature_tuple(item)
        obligations = []
        if sig != ac_sig:
            obligations.append(("UNIQUE_G", G))
        if int(item["pole"]) >= 2 and sig != c2_sig:
            obligations.append((bad_kind(item), T))
        for kind, rhs in obligations:
            needed = required_bound(item, a, c, rhs)
            if needed is None:
                persistent.append({"kind": kind, "primitive": item, "rhs": rhs})
            else:
                if needed > bound:
                    facets = [{"kind": kind, "primitive": item, "rhs": rhs, "r_bound": needed}]
                    bound = needed
                elif needed == bound and needed >= r0:
                    facets.append({"kind": kind, "primitive": item, "rhs": rhs, "r_bound": needed})
    return (None, persistent) if persistent else (bound, facets)


def registered_rows(schema):
    box = schema["registered_box"]
    for a in range(int(box["a_min"]), int(box["a_max"]) + 1):
        for d in box["d_values"]:
            c = a + int(d)
            if c < int(box["c_min"]):
                continue
            s_min = 1 if a <= d else 0
            r0 = a + s_min
            if r0 < 2 or a + 3 * s_min <= d:
                continue
            yield a, int(d), c, r0


def load_miner(schema):
    path = ROOT / schema["source_pins"]["support_miner"]["path"]
    spec = importlib.util.spec_from_file_location("v48_comparator_miner", path)
    if spec is None or spec.loader is None:
        fail("support miner import")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def miner_inventory(miner, a: int, d: int, r: int, pad: int = 0):
    c = a + d
    raw = miner.enumerate_primitives({
        "a": a, "d": d, "c": c, "r": r,
        "target_grade": 10 + 2 * c,
    }, pad=pad)
    stripped = [{key: item[key] for key in SIGNATURE_KEYS} for item in raw]
    return sorted(stripped, key=lambda item: tuple(str(item[key]) for key in SIGNATURE_KEYS))


def compile_result(schema, universe, cancelled):
    # Compile first; only then read V47 manifests as a comparison target.
    independent = []
    for a, d, c, r0 in registered_rows(schema):
        r_min, facets = compile_threshold(schema, universe, a, d, r0)
        if r_min is None:
            continue
        ok, reasons, _, inv = classify(schema, universe, a, c, r_min)
        if not ok:
            fail(("compiled threshold rejected", a, d, r_min, reasons))
        for sentinel in (r_min + 1, r_min + 17):
            if not classify(schema, universe, a, c, sentinel)[0]:
                fail(("nonmonotone tail", a, d, r_min, sentinel))
        raised = r_min > r0
        identifier = f"A{a}D{d}" + (f"_R{r_min}" if raised else "")
        predecessor = None
        if raised:
            pre_ok, pre_reasons, pre_witnesses, _ = classify(schema, universe, a, c, r_min - 1)
            if pre_ok:
                fail(("raised predecessor accepted", identifier))
            predecessor = {"r": r_min - 1, "reasons": pre_reasons, "witnesses": pre_witnesses}
        independent.append({
            "id": identifier, "class": "raised_subtail" if raised else "baseline",
            "a": a, "d": d, "c": c, "registered_r0": r0, "r_min": r_min,
            "G": 10 + a + c, "T_C2": 10 + 2 * c,
            "presburger_clause": f"a={a} and d={d} and c={c} and r>={r_min}",
            "primitive_count": len(inv), "inventory": inv,
            "inventory_sha256": canonical_digest(inv),
            "active_facets": facets,
            "predecessor": predecessor,
            "tail_certified_by_nonnegative_R_coefficients": True,
        })

    v47_schema = json.loads((ROOT / schema["source_pins"]["v47_schema"]["path"]).read_text())
    v47_result = json.loads((ROOT / schema["source_pins"]["v47_result"]["path"]).read_text())
    expected = v47_schema["baseline_manifests"] + v47_schema["raised_subtail_manifests"]
    expected_index = {item["id"]: item for item in expected}
    if set(expected_index) != {item["id"] for item in independent}:
        fail(("12+4 id comparison", sorted(expected_index), sorted(item["id"] for item in independent)))
    if len([item for item in independent if item["class"] == "baseline"]) != 12:
        fail("baseline count")
    if len([item for item in independent if item["class"] == "raised_subtail"]) != 4:
        fail("raised count")
    if set(v47_result["manifest_ids"]) != set(expected_index):
        fail("V47 result/schema ids")

    r1 = json.loads((ROOT / schema["source_pins"]["v47r1_result"]["path"]).read_text())
    r1_index = {item["id"]: item for item in r1["manifest_records"]}
    if set(r1_index) != set(expected_index) or r1["manifest_count"] != 16:
        fail("V47R1 manifest ids")
    coefficient_digests = {item["coefficient_sha256"] for item in r1_index.values()}
    if coefficient_digests != {"ad0c9b15ce394e554c178521fadb32b3c71318cf3a8d700a2311aceb9d12a850"}:
        fail("V47R1 coefficient digest")

    for item in independent:
        expected_item = expected_index[item["id"]]
        for key in ("a", "d", "c", "r_min", "G", "T_C2", "inventory_sha256"):
            if item[key] != expected_item[key]:
                fail(("manifest comparison", item["id"], key, item[key], expected_item[key]))
        item["endpoint_id"] = expected_item["endpoint_id"]
        item["endpoint_authority_sha256"] = expected_item["authority_sha256"]
        item["endpoint_review_sha256"] = expected_item["review_sha256"]
        item["v47r1_literal_coefficient_sha256"] = r1_index[item["id"]]["coefficient_sha256"]

    negative_results = []
    frozen_negatives = {item["id"]: item["reasons"] for item in v47_result["negative_controls"]}
    miner = load_miner(schema)
    comparison_cells = []
    for control in v47_schema["negative_controls"]:
        a, d, c, r = (int(control[key]) for key in ("a", "d", "c", "r"))
        ok, reasons, witnesses, inv = classify(schema, universe, a, c, r)
        if ok or reasons != frozen_negatives[control["id"]]:
            fail(("negative comparison", control["id"], reasons, frozen_negatives[control["id"]]))
        disabled = frozenset(reasons)
        mutated_ok, mutated_reasons, _, _ = classify(schema, universe, a, c, r, disabled=disabled)
        if not mutated_ok or mutated_reasons:
            fail(("negative mutation did not fire", control["id"], mutated_reasons))
        negative_results.append({
            "id": control["id"], "a": a, "d": d, "c": c, "r": r,
            "reasons": reasons, "witnesses": witnesses,
            "mutation_disabled_exact_reasons": list(reasons),
            "mutation_accepts": True,
        })
        comparison_cells.append((a, d, r, inv))

    # The old miner is a comparator only; no region is accepted from it.
    for item in independent:
        comparison_cells.append((item["a"], item["d"], item["r_min"], item["inventory"]))
    for a, d, r, inv in comparison_cells:
        mined = miner_inventory(miner, a, d, r)
        mined_pad = miner_inventory(miner, a, d, r, pad=1)
        if inv != mined or mined != mined_pad:
            fail(("independent/miner comparison", a, d, r))

    formula = " OR ".join(f"({item['presburger_clause']})" for item in independent)
    compressed_formula = (
        "(2<=a<=6 and d=1 and c=a+1 and r>=a) OR "
        "(1<=a<=6 and d=2 and c=a+2 and r>=a and r>=3) OR "
        "(2<=a<=6 and d=3 and c=a+3 and r>=a and r>=5)"
    )
    threshold_index = {(item["a"], item["d"]): item["r_min"] for item in independent}
    compressed_thresholds = {
        **{(a, 1): a for a in range(2, 7)},
        **{(a, 2): max(a, 3) for a in range(1, 7)},
        **{(a, 3): max(a, 5) for a in range(2, 7)},
    }
    if threshold_index != compressed_thresholds:
        fail(("compressed Presburger formula", threshold_index, compressed_thresholds))
    universal_table = {
        "nonzero": universe,
        "cancelled": cancelled,
    }
    return {
        "status": "PASS-GATE-T-STRICT-UAC-PRESBURGER-CHAMBERS-V48-PRODUCER",
        "scope": "exact 12+4 semilinear rays in the registered V47 box; no strict-fan cover claim",
        "schema_sha256": digest(SCHEMA_PATH),
        "universal_grade_cap": schema["universal_grade_cap"],
        "universal_nonzero_primitive_count": len(universe),
        "universal_cancelled_signature_count": len(cancelled),
        "universal_table_sha256": canonical_digest(universal_table),
        "unique_AC_inequality_count": len(universe) - 1,
        "global_pole_inequality_count": sum(
            int(item["pole"]) >= 2 and signature_tuple(item) != signature_tuple(schema["allowed_primitives"]["C2"])
            for item in universe
        ),
        "compressed_chamber_family_count": 3,
        "compressed_presburger_formula": compressed_formula,
        "compressed_presburger_formula_sha256": sha256(compressed_formula.encode()).hexdigest(),
        "presburger_formula": formula,
        "presburger_formula_sha256": sha256(formula.encode()).hexdigest(),
        "baseline_count": 12,
        "raised_subtail_count": 4,
        "chambers": independent,
        "chamber_records_sha256": canonical_digest(independent),
        "negative_control_count": len(negative_results),
        "negative_mutation_count": sum(item["mutation_accepts"] for item in negative_results),
        "negative_controls": negative_results,
        "support_miner_comparison_cell_count": len(comparison_cells),
        "v46_scope_attached": "reviewed V0,V1,V3,V4 source naturality only; no shifted-root V2",
        "v47r1_scope_attached": "reviewed exact 16-manifest literal contraction; endpoint types/localizations inherited",
        "fan_cover_status": "NOT_CLAIMED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-once", type=Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA_PATH.read_text())
    pin_sources(schema)
    universe, cancelled = generate_universe(schema)
    validate_generation(schema, universe, cancelled)
    result = compile_result(schema, universe, cancelled)
    if args.write_once is not None:
        target = args.write_once.resolve()
        if target.exists():
            fail(("refuse overwrite", str(target)))
        target.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    if FROZEN_PATH.exists() and json.loads(FROZEN_PATH.read_text()) != result:
        fail("frozen compiled result mismatch")
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
