#!/usr/bin/env python3
"""Syntax-only repair of the frozen V18 T-cs compiler."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
BASE = HERE / "compile_t_cs_rho_unit_v18.py"
BASE_SHA256 = "50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6"
PREREG = HERE / "PREREGISTRATION_V18R1.md"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_cs_rho_unit_v18r1_")
    ):
        raise RuntimeError("V18R1 compiler requires a registered AWS EC2 lane")
    return tag


def load_base():
    if digest(BASE) != BASE_SHA256:
        raise RuntimeError("frozen V18 compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("jc2_t_cs_v18_base", BASE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    base = load_base()
    result = base.compile_job(args.output, args.characteristic, tag)
    script = Path(result["script"])
    before = script.read_text()
    input_names = ",".join(f"E{i}" for i in range(1, 22))
    replacements = (
        (f"ideal E12={input_names};", f"ideal Prefix12={input_names};"),
        ("ideal E=E12,E22;", "ideal E=Prefix12,E22;"),
        ("ideal NoG14=std(E12+Localizers);", "ideal NoG14=std(Prefix12+Localizers);"),
    )
    after = before
    for old, new in replacements:
        if after.count(old) != 1 or new in after:
            raise RuntimeError(("repair occurrence contract", old, after.count(old)))
        after = after.replace(old, new)
    if before == after or "ideal E12=" in after:
        raise RuntimeError("V18R1 repair sentinel")
    script.write_text(after)
    result.update(
        {
            "status": "PASS-T-CS-RHO-UNIT-V18R1-COMPILER",
            "repair": "E12_POLYNOMIAL_PREFIX_IDEAL_COLLISION_ONLY",
            "base_compiler_sha256": BASE_SHA256,
            "base_script_sha256": sha256(before.encode()).hexdigest(),
            "script_sha256": digest(script),
            "repair_preregistration_sha256": digest(PREREG),
        }
    )
    (args.output / "result.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
