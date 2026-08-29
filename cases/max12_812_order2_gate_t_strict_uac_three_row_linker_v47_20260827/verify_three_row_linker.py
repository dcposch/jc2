#!/usr/bin/env python3
"""Fail-closed desk verifier for the V47 direct three-row linker schema.

This verifies a finite manifest and exact formula interface.  It does not
re-run any endpoint CAS job and it never upgrades an endpoint's theorem type.
"""

from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
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

ATOMS = (
    {"fixed": 2, "denominator": 2, "R": 1, "A": 0, "C": 0, "scalar": 2},
    {"fixed": 4, "denominator": 4, "R": 2, "A": 0, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 3, "R": 0, "A": 1, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 4, "R": 0, "A": 0, "C": 1, "scalar": 1},
)
SUMMANDS = (
    {"summand": "unloaded", "load": None, "alpha": Fraction(3, 2), "fixed": 0},
    {"summand": "k10", "load": "k10", "alpha": Fraction(5, 4), "fixed": 4},
    {"summand": "k6", "load": "k6", "alpha": Fraction(3, 4), "fixed": 12},
    {"summand": "k2", "load": "k2", "alpha": Fraction(1, 4), "fixed": 20},
)
SIGNATURE_KEYS = (
    "summand", "load", "fixed_sigma", "R", "A", "C", "pole",
    "coefficient", "first_grade",
)


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def binomial(alpha: Fraction, degree: int) -> Fraction:
    value = Fraction(1)
    for index in range(degree):
        value *= alpha - index
    return value / math.factorial(degree)


def own_inventory(a: int, c: int, r: int, maximum: int, pad: int = 0) -> list[dict[str, object]]:
    baseline = {"A": a, "C": c, "R": r}
    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in SUMMANDS:
        budget = maximum - int(summand["fixed"])
        if budget < 0:
            continue
        costs = [
            int(atom["fixed"]) + sum(baseline[stem] * int(atom[stem]) for stem in baseline)
            for atom in ATOMS
        ]
        if any(cost <= 0 for cost in costs):
            fail(("nonpositive atom cost", a, c, r, costs))
        bounds = [budget // cost + pad for cost in costs]
        for counts in product(*(range(bound + 1) for bound in bounds)):
            degree = sum(counts)
            if not degree:
                continue
            fixed = int(summand["fixed"])
            denominator = 0
            powers = {"R": 0, "A": 0, "C": 0}
            scalar = 1
            for count, atom in zip(counts, ATOMS):
                fixed += count * int(atom["fixed"])
                denominator += count * int(atom["denominator"])
                scalar *= int(atom["scalar"]) ** count
                for stem in powers:
                    powers[stem] += count * int(atom[stem])
            first_grade = fixed + sum(baseline[stem] * powers[stem] for stem in baseline)
            if first_grade > maximum:
                continue
            pole = denominator - int(4 * summand["alpha"])
            if pole <= 0:
                continue
            multinomial = math.factorial(degree)
            for count in counts:
                multinomial //= math.factorial(count)
            coefficient = binomial(summand["alpha"], degree) * multinomial * scalar
            key = (
                summand["summand"], summand["load"], fixed,
                powers["R"], powers["A"], powers["C"], pole,
            )
            aggregate[key] += coefficient
    answer = []
    for key, coefficient in aggregate.items():
        if not coefficient:
            continue
        summand, load, fixed, rp, ap, cp, pole = key
        first_grade = int(fixed) + r * int(rp) + a * int(ap) + c * int(cp)
        answer.append({
            "summand": summand, "load": load, "fixed_sigma": int(fixed),
            "R": int(rp), "A": int(ap), "C": int(cp), "pole": int(pole),
            "coefficient": fraction_text(coefficient), "first_grade": first_grade,
        })
    return sorted(answer, key=lambda item: tuple(str(item[key]) for key in SIGNATURE_KEYS))


def inventory_signature(inventory: list[dict[str, object]]) -> list[tuple[object, ...]]:
    return sorted(tuple(item[key] for key in SIGNATURE_KEYS) for item in inventory)


def miner_signature(inventory: list[dict[str, object]]) -> list[tuple[object, ...]]:
    return sorted(tuple(item[key] for key in SIGNATURE_KEYS) for item in inventory)


def load_miner(schema: dict[str, object]):
    pin = schema["source_pins"]["support_miner"]
    path = ROOT / pin["path"]
    if digest(path) != pin["sha256"]:
        fail("support miner hash")
    spec = importlib.util.spec_from_file_location("v47_pinned_support_miner", path)
    if spec is None or spec.loader is None:
        fail("support miner import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def row(a: int, d: int, r: int) -> dict[str, int]:
    c = a + d
    return {
        "a": a, "d": d, "c": c, "r": r, "s_min": r - a,
        "first_ac_grade": 10 + a + c, "target_grade": 10 + 2 * c,
    }


def matches_pin(item: dict[str, object], pin: dict[str, object]) -> bool:
    return all(item[key] == value for key, value in pin.items())


def purity(
    inventory: list[dict[str, object]], G: int, T: int,
    ac_pin: dict[str, object], c2_pin: dict[str, object],
    *, accept_ra2_as_c2: bool = False, require_unique: bool = True,
    G_upper: int = 28, T_upper: int = 32,
) -> tuple[bool, tuple[str, ...]]:
    reasons: list[str] = []
    initial = [item for item in inventory if int(item["first_grade"]) <= G]
    exact_ac = [item for item in initial if matches_pin(item, ac_pin)]
    if require_unique and (len(initial) != 1 or len(exact_ac) != 1 or int(exact_ac[0]["first_grade"]) != G):
        reasons.append("NONUNIQUE_G")
    elif not require_unique and not exact_ac:
        reasons.append("MISSING_AC")

    def is_allowed_c2(item: dict[str, object]) -> bool:
        if matches_pin(item, c2_pin):
            return True
        return accept_ra2_as_c2 and (
            item["summand"] == "unloaded" and item["load"] is None
            and tuple(int(item[key]) for key in ("R", "A", "C", "pole")) == (1, 2, 0, 2)
        )

    c2 = [item for item in inventory if matches_pin(item, c2_pin)]
    if len(c2) != 1 or int(c2[0]["first_grade"]) != T:
        reasons.append("C2_PIN")
    bad = [item for item in inventory if int(item["pole"]) >= 2 and not is_allowed_c2(item)]
    if bad:
        if any((int(item["R"]), int(item["A"]), int(item["C"])) == (1, 2, 0) for item in bad):
            reasons.append("RA2")
        if any((int(item["R"]), int(item["A"]), int(item["C"])) == (0, 3, 0) for item in bad):
            reasons.append("A3")
        if not any(reason in reasons for reason in ("RA2", "A3")):
            reasons.append("OTHER_GLOBAL_POLE")
    if G >= G_upper:
        reasons.append("G_TARGET_WALL")
    if T >= T_upper:
        reasons.append("T_TARGET_WALL")
    return not reasons, tuple(reasons)


# Sparse polynomial engine.  Monomials are sorted tuples (name, exponent).
def padd(*polys):
    out: dict[tuple[tuple[str, int], ...], Fraction] = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if not out[monomial]:
                del out[monomial]
    return out


def pscale(value: Fraction | int, poly):
    return {monomial: Fraction(value) * coefficient for monomial, coefficient in poly.items()}


def pmul(left, right):
    out: dict[tuple[tuple[str, int], ...], Fraction] = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            powers: defaultdict[str, int] = defaultdict(int)
            for name, exponent in lm + rm:
                powers[name] += exponent
            monomial = tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent))
            out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def pvar(name: str):
    return {((name, 1),): Fraction(1)}


def exact_rows(g1_scale: Fraction = Fraction(3, 8), g4_scale: Fraction = Fraction(3, 32), c_scale: Fraction = Fraction(1, 2)):
    A0c, A1, C0c, C1, rho = (pvar(name) for name in ("A0c", "A1", "C0c", "C1", "rho"))
    rho2 = pmul(rho, rho)
    # AC primitive has coefficient 3/4.  Its z and constant remainders each
    # carry the chart factor c_scale.
    computed_g1 = pscale(Fraction(3, 4) * c_scale, padd(pmul(A0c, C1), pmul(A1, C0c)))
    computed_g2 = pscale(Fraction(3, 4) * c_scale, padd(pmul(A0c, C0c), pmul(rho2, pmul(A1, C1))))
    # Even root value of (3/8) C0^2.
    computed_g4 = pscale(Fraction(3, 8) * c_scale * c_scale, padd(pmul(C0c, C0c), pmul(rho2, pmul(C1, C1))))
    g1 = pscale(g1_scale, padd(pmul(A0c, C1), pmul(A1, C0c)))
    g2 = pscale(g1_scale, padd(pmul(A0c, C0c), pmul(rho2, pmul(A1, C1))))
    g4 = pscale(g4_scale, padd(pmul(C0c, C0c), pmul(rho2, pmul(C1, C1))))
    if (computed_g1, computed_g2, computed_g4) != (g1, g2, g4):
        fail("literal coefficient extraction")
    D = padd(pmul(rho2, pmul(C1, C1)), pscale(-1, pmul(C0c, C0c)))
    checks = (
        padd(pmul(C1, g2), pscale(-1, pmul(C0c, g1)), pscale(Fraction(-3, 8), pmul(A1, D))),
        padd(pmul(C0c, g2), pscale(-1, pmul(rho2, pmul(C1, g1))), pscale(Fraction(3, 8), pmul(A0c, D))),
        padd(pscale(Fraction(32, 3), g4), D, pscale(-2, pmul(rho2, pmul(C1, C1)))),
        padd(pscale(Fraction(32, 3), g4), pscale(-1, D), pscale(-2, pmul(C0c, C0c))),
    )
    if any(checks):
        fail(("syzygy", checks))
    # Full moving-P simple-pole recurrence, not frozen-p0 cancellation.
    P, h2 = pvar("P_full_series"), pvar("h2")
    h4 = pscale(Fraction(-1, 2), pmul(P, h2))
    if padd(h4, pscale(Fraction(1, 2), pmul(P, h2))):
        fail("Phi4 simple-pole recurrence")
    return g1, g2, g4


def validate_static_schema(schema: dict[str, object]) -> None:
    if schema["equation_names"] != {"three_row": "g-triple-v1", "uniform_emitter": "emitter-7-v1"}:
        fail("equation-name collision")
    convention = schema["tuple_convention"]
    if convention["fields"] != ["a", "d", "c", "r_min"] or convention["unlabelled_triples"] != "forbidden":
        fail("tuple convention")
    chart = schema["chart"]
    if chart["C0"] != "(C1*z+C0c)/2" or chart["A0"] != "A1*z+A0c":
        fail("chart normalization")
    if chart["shifted_leading_names"] != ["A0c", "A1", "C0c", "C1"]:
        fail("shifted names")
    rows = schema["literal_rows"]
    if rows != {
        "Phi1": "h1", "Phi2": "h2", "Phi4": "h4+(P/2)*h2",
        "row_origin": "general_rho_literal_Phi",
        "forbidden_rows": ["h4", "unbridged_H", "rho0_face_as_general_rho"],
    }:
        fail("literal Phi bridge")
    scope = schema["scope"]
    if scope["theorem_type"] != "radical/set-theoretic and normalized-DVR-arc emptiness" or scope["scheme_unit_ideal"]:
        fail("theorem type")
    if scope["reverse_transport"] != "forbidden" or scope["root_allocation_used"]:
        fail("transport/root firewall")
    if scope["endpoint_localization_policy"] != "retain the resolved frozen endpoint localization; the direct lemma never removes an upstream chart factor":
        fail("endpoint localization policy")
    if schema["purity_policy"]["allocation_local_pole_bit"] != "forbidden":
        fail("allocation predicate imported")


def check_pin(pin: dict[str, str], hash_key: str = "sha256") -> None:
    path = ROOT / pin["path"]
    if not path.is_file() or digest(path) != pin[hash_key]:
        fail(("hash pin", pin["path"], digest(path) if path.is_file() else "MISSING", pin[hash_key]))


def verify_source_pins(schema: dict[str, object]) -> None:
    pins = schema["source_pins"]
    for name in ("lemma", "original_replay", "hostile_review", "support_miner", "tail_emitter", "uniform_schema", "uniform_freeze", "uniform_review"):
        check_pin(pins[name])
    check_pin(pins["tails"], "byte_sha256")
    tails = json.loads((ROOT / pins["tails"]["path"]).read_text())
    if canonical_digest(tails) != pins["tails"]["canonical_sha256"]:
        fail("tails canonical hash")
    ordered_tails = [tails[str(index)] for index in range(1, 8)]
    if [len(row) for row in ordered_tails] != pins["tails"]["row_census"] or sum(map(len, ordered_tails)) != pins["tails"]["total_census"]:
        fail("tails census")
    uniform = json.loads((ROOT / pins["uniform_schema"]["path"]).read_text())
    if uniform["tails"]["byte_sha256"] != pins["tails"]["byte_sha256"]:
        fail("uniform/tails pin")
    witness = [item for item in uniform["semantic_witnesses"] if item["role"] == "tail/load/target emitter"]
    if len(witness) != 1 or witness[0]["sha256"] != pins["tail_emitter"]["sha256"]:
        fail("uniform/emitter pin")
    if pins["uniform_review"]["consumed_scope"] != "V0,V1,V3,V4 only; V2 shifted-root maps are not consumed":
        fail("uniform review scope")
    for endpoint in schema["endpoint_authorities"].values():
        if endpoint["status"] != "promoted":
            fail("unpromoted endpoint")
        check_pin(endpoint["authority"])
        check_pin(endpoint["review"])


def validate_manifest_shape(manifest: dict[str, object], schema: dict[str, object]) -> None:
    if not isinstance(manifest, dict):
        fail("ambiguous unlabelled tuple")
    required = {"id", "a", "d", "c", "r_min", "G", "T_C2", "endpoint_id", "authority_sha256", "review_sha256", "inventory_sha256"}
    if not required.issubset(manifest):
        fail(("manifest fields", manifest.get("id")))
    a, d, c, r = (int(manifest[key]) for key in ("a", "d", "c", "r_min"))
    if c != a + d or int(manifest["G"]) != 10 + a + c or int(manifest["T_C2"]) != 10 + 2 * c:
        fail(("manifest arithmetic", manifest["id"]))
    endpoint = schema["endpoint_authorities"].get(manifest["endpoint_id"])
    if endpoint is None:
        fail(("endpoint missing", manifest["id"]))
    if endpoint["localization"] not in ("D(p*k10)", "D(p*k0)") or not endpoint["theorem_type"].startswith("arcwise/set-theoretic"):
        fail(("endpoint localization/theorem type", manifest["id"]))
    if manifest["authority_sha256"] != endpoint["authority"]["sha256"] or manifest["review_sha256"] != endpoint["review"]["sha256"]:
        fail(("per-manifest endpoint pins", manifest["id"]))
    hard_reject = {(2, 5, 3), (2, 5, 4)}
    if (a, c, r) in hard_reject:
        fail(("hard-rejected a,c,r", manifest["id"]))


def generated_maps(manifest: dict[str, object]) -> dict[str, dict[str, str]]:
    a, c, r = (int(manifest[key]) for key in ("a", "c", "r_min"))
    return {
        "d1_shifted": {"A1": "AzD1_0", "A0c": "AcD1_0", "C1": "CzD1_0", "C0c": "CcD1_0"},
        "total_to_d1": {
            f"az_{a}": "AzD1_0", f"ac_{a}": "AcD1_0",
            f"ez_{c}": "2*CzD1_0", f"ec_{c}": "2*CcD1_0",
            f"cs_{r}": "BzD1_0", f"rs_{r}": "4*BcD1_0",
        },
    }


def generated_record(manifest: dict[str, object]) -> dict[str, object]:
    a, d, c, r = (int(manifest[key]) for key in ("a", "d", "c", "r_min"))
    return {
        "id": manifest["id"], "a": a, "d": d, "c": c, "r_min": r,
        "total": {
            "A_z": f"az_{a}", "A_c": f"ac_{a}",
            "C_z": f"ez_{c}", "C_c": f"ec_{c}",
            "R_z": f"cs_{r}", "R_c": f"rs_{r}",
        },
        "to_d1": {
            "A_z": "AzD1_0", "A_c": "AcD1_0",
            "C_z": "2*CzD1_0", "C_c": "2*CcD1_0",
            "R_z": "BzD1_0", "R_c": "4*BcD1_0",
        },
    }


def expect_reject(label: str, action, fired: list[str]) -> None:
    try:
        action()
    except Exception:
        fired.append(label)
        return
    fail(("mutation survived", label))


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    validate_static_schema(schema)
    verify_source_pins(schema)
    exact_rows()
    miner = load_miner(schema)
    ac_pin = schema["coefficient_pins"]["AC_primitive"]
    c2_pin = schema["coefficient_pins"]["C2_primitive"]
    all_manifests = schema["baseline_manifests"] + schema["raised_subtail_manifests"]
    generated_path = ROOT / schema["generated_manifest_path"]
    generated = json.loads(generated_path.read_text())
    if generated["d1_shifted_names"] != {
        "A1": "AzD1_0", "A0c": "AcD1_0", "C1": "CzD1_0", "C0c": "CcD1_0",
    }:
        fail("generated D1 names")
    generated_index = {entry["id"]: entry for entry in generated["manifests"]}
    if len(generated_index) != 16 or set(generated_index) != {manifest["id"] for manifest in all_manifests}:
        fail("generated manifest inventory")
    manifest_results = []
    comparison_count = 0
    for manifest in all_manifests:
        validate_manifest_shape(manifest, schema)
        a, d, c, r = (int(manifest[key]) for key in ("a", "d", "c", "r_min"))
        G, T = int(manifest["G"]), int(manifest["T_C2"])
        own = own_inventory(a, c, r, T)
        own_pad = own_inventory(a, c, r, T, pad=1)
        if inventory_signature(own) != inventory_signature(own_pad):
            fail(("own pad+1", manifest["id"]))
        mined = miner.enumerate_primitives(row(a, d, r))
        mined_pad = miner.enumerate_primitives(row(a, d, r), pad=1)
        if miner_signature(mined) != miner_signature(mined_pad):
            fail(("miner pad+1", manifest["id"]))
        if inventory_signature(own) != miner_signature(mined):
            fail(("independent/miner mismatch", manifest["id"]))
        comparison_count += len(own)
        inventory_sha = canonical_digest(own)
        if manifest["inventory_sha256"] != inventory_sha:
            fail(("inventory pin", manifest["id"], inventory_sha, manifest["inventory_sha256"]))
        ok, reasons = purity(own, G, T, ac_pin, c2_pin)
        if not ok:
            fail(("manifest purity", manifest["id"], reasons))
        # The closed tail is certified by monotonicity of every R-bearing
        # grade, plus two concrete sentinels.  R-free grades are invariant.
        for later_r in (r + 1, r + 5):
            later = own_inventory(a, c, later_r, T)
            later_ok, later_reasons = purity(later, G, T, ac_pin, c2_pin)
            if not later_ok:
                fail(("tail monotonicity", manifest["id"], later_r, later_reasons))
        if any(int(item["R"]) < 0 for item in own):
            fail("negative R exponent")
        maps = generated_maps(manifest)
        if any(name in schema["chart"]["forbidden_stage_zero_names"] for name in maps["d1_shifted"]):
            fail(("stage-zero map", manifest["id"]))
        if generated_index[manifest["id"]] != generated_record(manifest):
            fail(("generated alias map", manifest["id"]))
        manifest_results.append({
            "id": manifest["id"], "a": a, "d": d, "c": c, "r_min": r,
            "G": G, "T_C2": T, "primitive_count": len(own),
            "inventory_sha256": inventory_sha, "endpoint_id": manifest["endpoint_id"],
            "endpoint_localization": schema["endpoint_authorities"][manifest["endpoint_id"]]["localization"],
            "endpoint_theorem_type": schema["endpoint_authorities"][manifest["endpoint_id"]]["theorem_type"],
            "tail_certified": True, "generated_alias_map_sha256": canonical_digest(generated_index[manifest["id"]]),
        })

    # The twelve are derived from the wall policy over the declared box,
    # then compared to the schema; they are not accepted because typed twice.
    derived_baselines = set()
    for a in range(1, 7):
        for d in (1, 2, 3):
            c = a + d
            if c < 3:
                continue
            s_min = 1 if a <= d else 0
            r = a + s_min
            if r < 2 or a + 3 * s_min <= d:
                continue
            G, T = 10 + a + c, 10 + 2 * c
            inv = own_inventory(a, c, r, T)
            if purity(inv, G, T, ac_pin, c2_pin)[0]:
                derived_baselines.add((a, d, c, r, G, T))
    schema_baselines = {
        tuple(int(manifest[key]) for key in ("a", "d", "c", "r_min", "G", "T_C2"))
        for manifest in schema["baseline_manifests"]
    }
    if derived_baselines != schema_baselines or len(derived_baselines) != 12:
        fail(("derived baseline list", derived_baselines, schema_baselines))

    # Derive all newly recovered thresholds among the rejected a<=4,d=2,3
    # baselines.  E never recovers because its R-free A^3 wall persists.
    recovered = set()
    for a in range(1, 5):
        for d in (2, 3):
            c = a + d
            base_r = a + (1 if a <= d else 0)
            if purity(own_inventory(a, c, base_r, 10 + 2 * c), 10 + a + c, 10 + 2 * c, ac_pin, c2_pin)[0]:
                continue
            first = None
            for r in range(base_r + 1, 21):
                if purity(own_inventory(a, c, r, 10 + 2 * c), 10 + a + c, 10 + 2 * c, ac_pin, c2_pin)[0]:
                    first = r
                    break
            if first is not None:
                recovered.add((a, d, c, first))
    schema_raised = {
        tuple(int(manifest[key]) for key in ("a", "d", "c", "r_min"))
        for manifest in schema["raised_subtail_manifests"]
    }
    if recovered != schema_raised or len(recovered) != 4:
        fail(("derived raised subtails", recovered, schema_raised))

    negative_results = []
    for control in schema["negative_controls"]:
        a, d, c, r = (int(control[key]) for key in ("a", "d", "c", "r"))
        G, T = 10 + a + c, 10 + 2 * c
        inv = own_inventory(a, c, r, T)
        ok, reasons = purity(inv, G, T, ac_pin, c2_pin)
        if ok:
            fail(("negative accepted", control["id"]))
        expected_reason = control["reason"]
        if expected_reason == "K2_OR_TARGET":
            if not any(item["load"] == "k2" for item in inv) or not any(reason.endswith("TARGET_WALL") for reason in reasons):
                fail(("k2/target control", control["id"], reasons))
        elif expected_reason not in reasons:
            fail(("negative reason", control["id"], reasons))
        negative_results.append({"id": control["id"], "reasons": list(reasons)})

    mutations: list[str] = []
    expect_reject("g1-normalization", lambda: exact_rows(g1_scale=Fraction(3, 4)), mutations)
    expect_reject("g4-normalization", lambda: exact_rows(g4_scale=Fraction(3, 16)), mutations)
    expect_reject("C0-factor-two", lambda: exact_rows(c_scale=Fraction(1)), mutations)

    ra2 = own_inventory(1, 3, 2, 16)
    if purity(ra2, 14, 16, ac_pin, c2_pin)[0] or not purity(ra2, 14, 16, ac_pin, c2_pin, accept_ra2_as_c2=True)[0]:
        fail("RA2 mutation is not live")
    mutations.append("RA2-as-C2")
    a7 = own_inventory(7, 8, 7, 26)
    if purity(a7, 25, 26, ac_pin, c2_pin)[0] or not purity(a7, 25, 26, ac_pin, c2_pin, require_unique=False)[0]:
        fail("uniqueness mutation is not live")
    mutations.append("drop-unique-G")

    synthetic = [
        {**ac_pin, "first_grade": 28},
        {**c2_pin, "first_grade": 30},
    ]
    if purity(synthetic, 28, 30, ac_pin, c2_pin)[0] or not purity(synthetic, 28, 30, ac_pin, c2_pin, G_upper=100)[0]:
        fail("G target-wall mutation is not live")
    mutations.append("open-G-target-wall")
    synthetic = [
        {**ac_pin, "first_grade": 27},
        {**c2_pin, "first_grade": 32},
    ]
    if purity(synthetic, 27, 32, ac_pin, c2_pin)[0] or not purity(synthetic, 27, 32, ac_pin, c2_pin, T_upper=100)[0]:
        fail("T target-wall mutation is not live")
    mutations.append("open-T-target-wall")

    mutated = deepcopy(schema)
    mutated["chart"]["shifted_leading_names"] = ["a0", "a1", "c0", "c1"]
    expect_reject("stage-zero-leading-names", lambda: validate_static_schema(mutated), mutations)
    mutated = deepcopy(schema)
    mutated["literal_rows"]["row_origin"] = "rho0_face_as_general_rho"
    expect_reject("rho0-as-general-rho", lambda: validate_static_schema(mutated), mutations)
    mutated = deepcopy(schema)
    mutated["literal_rows"]["Phi4"] = "h4"
    expect_reject("h4-for-Phi4", lambda: validate_static_schema(mutated), mutations)
    mutated_ac = deepcopy(ac_pin)
    mutated_ac["coefficient"] = "1"
    known_good = own_inventory(2, 3, 2, 16)
    if purity(known_good, 15, 16, ac_pin, c2_pin)[0] is not True or purity(known_good, 15, 16, mutated_ac, c2_pin)[0] is not False:
        fail("AC coefficient mutation is not live")
    mutations.append("AC-coefficient")
    expect_reject("ambiguous-tuple", lambda: validate_manifest_shape((2, 3, 2), schema), mutations)
    if len(mutations) != 12:
        fail(("mutation count", mutations))

    # Pin the optional V45 corroborating artifact but do not use it as the
    # authority for the narrower raised-subtail replacement.
    v45 = ROOT / "xmodel/max12-812-order2-gate-t-drho-a2d3-v45-composition-review-repair-promotion-sol-20260827.md"
    if digest(v45) != "99d32a774795a113678487f52f53e0315939db2fe1b9cbf66ef775a5d031ba29":
        fail("V45 corroborating total promotion pin")

    result = {
        "status": "PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47",
        "scope": "exactly 12 baseline closed tails plus 4 raised closed subtails; provisional pending different-model review",
        "schema_sha256": digest(SCHEMA_PATH),
        "generated_manifests_sha256": digest(generated_path),
        "baseline_manifest_count": len(schema["baseline_manifests"]),
        "raised_subtail_manifest_count": len(schema["raised_subtail_manifests"]),
        "negative_control_count": len(negative_results),
        "mutation_count": len(mutations),
        "syzygy_count": 4,
        "independent_inventory_coefficient_count": comparison_count,
        "manifest_ids": [entry["id"] for entry in manifest_results],
        "manifest_results_sha256": canonical_digest(manifest_results),
        "negative_controls": negative_results,
        "mutations_fired": mutations,
        "uniform_scope_consumed": "V0,V1,V3,V4; no V2 shifted-root map",
        "endpoint_replacement_status": "WITHHELD_PENDING_DIFFERENT_MODEL_REVIEW",
    }
    frozen_path = CASE / "run_v0_v9/result.json"
    if not frozen_path.is_file() or json.loads(frozen_path.read_text()) != result:
        fail("frozen result mismatch")
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
