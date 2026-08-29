#!/usr/bin/env python3
"""Additive V44R1 repair: rerun the pinned V44 producer with the corrected receiver gate."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44_20260827/compile_actual_total_g20_v44.py"
BASE_SHA256 = "dd8681a66f150069db3e4553caa0fd66e70f360994b9a1328a34a4a50cac5003"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def substitute_once(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        raise RuntimeError(("V44 transform multiplicity", old, source.count(old)))
    return source.replace(old, new)


def main() -> None:
    if digest(BASE) != BASE_SHA256:
        raise RuntimeError(("V44 base compiler pin", digest(BASE), BASE_SHA256))
    source = BASE.read_text()
    source = substitute_once(
        source,
        'tag.startswith("max12_812_order2_gate_t_actual_total_g20_custody_v44_")',
        'tag.startswith("max12_812_order2_gate_t_actual_total_g20_custody_v44r1_")',
    )
    source = substitute_once(
        source,
        'if any(not rows for rows in receiver_rows.values()):\n        fail(("terminal receiver absent from all rows", receiver_rows))',
        'if any(rows for rows in receiver_rows.values()):\n        fail(("unexpected terminal receiver occurrence", receiver_rows))',
    )
    source = substitute_once(
        source,
        '"compiler_sha256": digest(Path(__file__)),',
        '"compiler_sha256": digest(Path(__file__)),\n'
        '        "base_compiler_sha256": "' + BASE_SHA256 + '",\n'
        '        "terminal_grade20_receiver_free": True,',
    )
    if source.count("V44") != 2:
        raise RuntimeError(("V44 status/banner multiplicity", source.count("V44")))
    source = source.replace("V44", "V44R1")
    namespace = {
        "__file__": str(Path(__file__).resolve()),
        "__name__": "v44r1_transformed_base",
    }
    exec(compile(source, str(BASE), "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()

