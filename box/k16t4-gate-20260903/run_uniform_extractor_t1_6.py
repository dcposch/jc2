#!/usr/bin/env python3
"""Run the charged normalizer extractor for t=1..6 with lane-local paths."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import pathlib
import sys


ROOT = pathlib.Path("/home/ubuntu/jc2")
OUT = ROOT / "box/k16t4-gate-20260903"
INPUT = pathlib.Path("/tmp/jc2-lane.F6oLuI/inputs")
DEPS = OUT / "deps"


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    source = INPUT / "uniform_extract_normalizers.py"
    module = load(source, "gate_uniform_extract_normalizers")
    module.INPUTS = DEPS
    module.CHART = DEPS / "t_order_system.py"
    module.PREPROCESS = DEPS / "triangular_preprocess.py"
    module.EXPECTED = {
        module.CHART: "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
        module.PREPROCESS: "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
    }
    old_argv = sys.argv[:]
    sys.argv = [source.name, "1", "2", "3", "4", "5", "6"]
    out_path = OUT / "uniform_extract_normalizers_t1_6.out"
    err_path = OUT / "uniform_extract_normalizers_t1_6.err"
    try:
        with out_path.open("w", encoding="utf-8") as out, err_path.open("w", encoding="utf-8") as err:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                module.main()
    finally:
        sys.argv = old_argv
    print(f"{out_path} sha256={sha256(out_path)}")
    print(f"{err_path} sha256={sha256(err_path)}")


if __name__ == "__main__":
    main()
