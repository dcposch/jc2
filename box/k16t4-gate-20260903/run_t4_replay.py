#!/usr/bin/env python3
"""Lane-local replay driver for the K=16, t=4 normalizer gate.

The charged source files are left untouched in /tmp/jc2-lane.F6oLuI/inputs.
This wrapper only patches path constants in the frozen audit emitters so fresh
artifacts land in box/k16t4-gate-20260903.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import json
import pathlib
import sys
import time

import sympy as sp


ROOT = pathlib.Path("/home/ubuntu/jc2")
INPUT = pathlib.Path("/tmp/jc2-lane.F6oLuI/inputs")
OUT = ROOT / "box/k16t4-gate-20260903"
DEPS = OUT / "deps"

EXPECTED = {
    "t4_order_system.py": "db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee",
    "triangular_preprocess.py": "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
    "t4_normalization_probe.py": "085aac73eafda284514bb2f10478f242d3535cca16ef7249043ed85b30a27faf",
    "t4_affine_reduce.py": "66463156f99204648456ddf0105273517b64252ce6e792f92c051d13b2a3591f",
    "t4_emit_exact_certificate.py": "42bfd85b39665717c6a885ba5c4b538f59020021b3ef9ad900bd06cb67db7312",
}

HELPER_EXPECTED = {
    "deps/t3_normalized_slice.py": "9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7",
    "deps/t_order_system.py": "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
}


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


def expression_vector_hash(expressions) -> str:
    text = "\n".join(str(sp.expand(expr)) for expr in expressions) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_tagged(path: pathlib.Path, tagged) -> None:
    lines = ["source_index_0based\th_power\tgamma_power\tpi_power\texpression"]
    for index, (h_power, monomial, expr) in enumerate(tagged):
        lines.append(
            f"{index}\t{h_power}\t{monomial[0]}\t{monomial[1]}\t{sp.expand(expr)}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_full_chart_jobs(driver, data) -> dict:
    jobs = {}
    for prime in (32003, 65521, 1000003):
        path = OUT / f"t4_full_gauged_p{prime}.sing"
        with path.open("w", encoding="utf-8") as handle:
            with contextlib.redirect_stdout(handle):
                driver.emit_singular(data, prime)
        jobs[str(prime)] = {
            "path": path.name,
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
    return jobs


def run_frozen_module(path: pathlib.Path, module_name: str, patches: dict, stdout_name: str) -> str:
    module = load(path, module_name)
    for key, value in patches.items():
        setattr(module, key, value)
    old_argv = sys.argv[:]
    sys.argv = [path.name]
    try:
        out_path = OUT / stdout_name
        err_path = OUT / stdout_name.replace(".out", ".err")
        with out_path.open("w", encoding="utf-8") as out, err_path.open("w", encoding="utf-8") as err:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                module.main()
    finally:
        sys.argv = old_argv
    return sha256(out_path)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        actual = sha256(INPUT / name)
        if actual != expected:
            raise RuntimeError(f"frozen input hash mismatch {name}: {actual}")
    for rel, expected in HELPER_EXPECTED.items():
        actual = sha256(OUT / rel)
        if actual != expected:
            raise RuntimeError(f"helper hash mismatch {rel}: {actual}")

    driver = load(INPUT / "t4_order_system.py", "gate_t4_order_system")
    started = time.monotonic()
    data = driver.build(gauged=True)
    build_seconds = time.monotonic() - started
    all_vars = data["params"] + [data["c"]]
    degree_hist = {}
    level_hist = {}
    for h_power, _monomial, equation in data["tagged"]:
        degree = sp.Poly(equation, *all_vars).total_degree()
        degree_hist[str(degree)] = degree_hist.get(str(degree), 0) + 1
        level_hist[str(h_power)] = level_hist.get(str(h_power), 0) + 1
    chart = {
        "source": "t4_order_system.py",
        "source_sha256": sha256(INPUT / "t4_order_system.py"),
        "gauged": True,
        "t": data["t"],
        "tuple": [52, 36, 49, 3],
        "e": data["e"],
        "q": data["q"],
        "unknowns_including_c": len(data["params"]) + 1,
        "equations": len(data["equations"]),
        "h_power_max": max(data["by_power"]),
        "degree_histogram": degree_hist,
        "h_level_histogram": level_hist,
        "equation_vector_sha256": expression_vector_hash(data["equations"]),
        "tagged_vector_sha256": expression_vector_hash(row[2] for row in data["tagged"]),
        "build_seconds": build_seconds,
    }
    if (chart["unknowns_including_c"], chart["equations"]) != (45, 65):
        raise AssertionError(chart)
    write_tagged(OUT / "t4_full_gauged_tagged.tsv", data["tagged"])
    chart["tagged_tsv_sha256"] = sha256(OUT / "t4_full_gauged_tagged.tsv")
    chart["full_chart_modular_jobs"] = emit_full_chart_jobs(driver, data)
    (OUT / "t4_chart_audit.json").write_text(
        json.dumps(chart, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    norm_stdout_hash = run_frozen_module(
        INPUT / "t4_normalization_probe.py",
        "gate_t4_normalization_probe",
        {"INPUT": INPUT, "OUT": OUT},
        "t4_normalization_probe.out",
    )
    affine_stdout_hash = run_frozen_module(
        INPUT / "t4_affine_reduce.py",
        "gate_t4_affine_reduce",
        {
            "HERE": OUT,
            "INPUT": DEPS,
            "ROWS": OUT / "t4_normalized_rows.tsv",
            "OUT": OUT / "t4_affine_audit.json",
        },
        "t4_affine_reduce.out",
    )
    cert_stdout_hash = run_frozen_module(
        INPUT / "t4_emit_exact_certificate.py",
        "gate_t4_emit_exact_certificate",
        {
            "HERE": OUT,
            "INPUT": DEPS,
            "AUDIT": OUT / "t4_affine_audit.json",
            "OUT": OUT / "t4_exact_Qsqrt15_nfmodstd.sing",
        },
        "t4_emit_exact_certificate.out",
    )

    generated = sorted(
        p for p in OUT.iterdir()
        if p.is_file() or (p.is_symlink() and p.exists())
    )
    manifest = {
        "driver": pathlib.Path(__file__).name,
        "normalization_stdout_sha256": norm_stdout_hash,
        "affine_stdout_sha256": affine_stdout_hash,
        "certificate_stdout_sha256": cert_stdout_hash,
        "generated_sha256": {p.name: sha256(p) for p in generated},
    }
    (OUT / "replay_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "chart": chart,
        "normalization_audit_sha256": sha256(OUT / "t4_normalization_audit.json"),
        "normalized_rows_sha256": sha256(OUT / "t4_normalized_rows.tsv"),
        "affine_audit_sha256": sha256(OUT / "t4_affine_audit.json"),
        "exact_singular_sha256": sha256(OUT / "t4_exact_Qsqrt15_nfmodstd.sing"),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
