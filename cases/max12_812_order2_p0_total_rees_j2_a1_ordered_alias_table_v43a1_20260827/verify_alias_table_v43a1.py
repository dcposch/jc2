#!/usr/bin/env python3
"""Desk-scale fail-closed verifier for the additive V37/V43 alias pin."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = HERE / "ALIAS_TABLE.json"
EXPECTED_TABLE_SHA256 = "fa88ffbe06b3f50f06e3118f7d841513d45c95ac9402dfc002fcab604eaf2188"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    if digest(TABLE) != EXPECTED_TABLE_SHA256:
        fail(("alias-table hash", digest(TABLE), EXPECTED_TABLE_SHA256))
    table = json.loads(TABLE.read_text())
    for pin in table["source_pins"].values():
        path = ROOT / pin["path"]
        actual = digest(path)
        if actual != pin["sha256"]:
            fail(("source pin", str(path), actual, pin["sha256"]))

    v37_pin = table["source_pins"]["v37_loader"]
    v37 = load(ROOT / v37_pin["path"], "v43a1_v37")
    parser, _, _, rho0 = v37.load_rows()
    if rho0 != table["alphabets"]["rho0_positive"] or len(rho0) != 65:
        fail("V37 rho-zero alphabet drift")

    v43_pin = table["source_pins"]["v43_total_compiler"]
    v43 = load(ROOT / v43_pin["path"], "v43a1_v43")
    (_, _, _, _, _, total, frozen, general_only, _) = v43.reconstruct_rows()
    if frozen != rho0:
        fail("V43/V37 rho-zero alphabet mismatch")
    if total != table["alphabets"]["total_positive"] or len(total) != 66:
        fail("V43 total alphabet drift")
    if general_only != table["alphabets"]["general_only"] or general_only != ["ez9"]:
        fail(("general-only drift", general_only))

    v46_pin = table["source_pins"]["actual_total_v46_schema"]
    v46 = json.loads((ROOT / v46_pin["path"]).read_text())
    firewall = table["load_aliases"]["collision_firewall"]
    v46_firewall = v46["aliases"]["collision_firewall"]
    if (
        v46_firewall["total_k10_jet_2"] != firewall["ordered_total_k10_jet_2"]
        or v46_firewall["total_k2_leading"] != firewall["ordered_total_k2_leading"]
        or v46_firewall["d1_k2_leading"] != firewall["d1_k2_leading"]
    ):
        fail(("V46 collision firewall drift", v46_firewall, firewall))
    if v46["aliases"]["total"]["k10"][:3] != ["k", "k1", "k2c"]:
        fail("V46 total k10 prefix drift")
    if v46["aliases"]["d1"]["k2"] != "k2load_{relative index}":
        fail("V46 D1 k2 alias drift")

    weights = {item["symbol"]: item["sigma_weight"]
               for item in table["load_aliases"]["ordered_total_k10"]}
    weights.update({item["symbol"]: item["sigma_weight"]
                    for item in table["load_aliases"]["ordered_total_k6"]})
    for symbol, expected in weights.items():
        if parser.sigma_weight(symbol) != expected:
            fail(("sigma weight", symbol, parser.sigma_weight(symbol), expected))
    if parser.sigma_weight("k2c") != 6 or parser.sigma_weight("k2") != 20:
        fail("k2c/k2 weight firewall")
    if any(symbol in total for symbol in ("k2", "k2load")) or "k2c" not in rho0:
        fail("ordered grade<=19 presence firewall")

    out = {
        "status": "PASS-ORDERED-A1-ALIAS-TABLE-V43A1",
        "alias_table_sha256": EXPECTED_TABLE_SHA256,
        "rho0_positive_count": len(rho0),
        "total_positive_count": len(total),
        "general_only": general_only,
        "k2c": "total.k10[2]",
        "k2": "total.k2[0] (absent through grade 19)",
        "k2load": "d1.k2[0] (absent from ordered V37/V43 alphabets)",
        "v46_schema_sha256": v46_pin["sha256"],
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
