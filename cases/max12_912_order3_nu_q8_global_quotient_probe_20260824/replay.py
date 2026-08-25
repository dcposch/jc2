#!/usr/bin/env python3
"""End-to-end replay for the Q8 localized quotient gate."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys


CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
FILES = {
    "quotient_compiler.py": "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "local_series.py": "5e3e3d8605999a21371dbd2aa54c82fbfec510b5e26f3801387c11d450da8957",
    "quotient.json": "694f5512ad78396f85f29e14566bff3e16a3ebfdf99bed3260ae708312bc0d9c",
    "local_series.json": "7d9467560ddee0aa8830e7bca4181ff7d33692865d81dfe3935f25b2e69e287e",
    "dimension.json": "129132386a26c034a7a0edf44d65e2eaaf39e13f38c0f7409806a612096422da",
}


def checked_run(command, *, input_text=None, timeout=360):
    result = subprocess.run(
        command,
        input=input_text,
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=timeout,
        check=False,
    )
    if result.returncode:
        raise RuntimeError((command, result.returncode, result.stdout, result.stderr))
    return result.stdout


def main():
    for name, expected in FILES.items():
        got = sha256((CASE / name).read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((name, got, expected))

    compiler = CASE / "quotient_compiler.py"
    local_series = CASE / "local_series.py"
    quotient_output = checked_run([sys.executable, str(compiler)])
    if quotient_output != (CASE / "quotient.json").read_text():
        raise RuntimeError("quotient compiler replay mismatch")
    series_output = checked_run([sys.executable, str(local_series)], timeout=600)
    if series_output != (CASE / "local_series.json").read_text():
        raise RuntimeError("local series replay mismatch")

    expected_dimension = json.loads((CASE / "dimension.json").read_text())["results"]
    dimension_results = {}
    for prime_text, expected in expected_dimension.items():
        source = checked_run([
            sys.executable,
            str(compiler),
            "--singular",
            "--prime", prime_text,
            "--localize",
        ])
        output = checked_run(["Singular", "-q"], input_text=source, timeout=360)
        parsed = {}
        for key in ("dim", "size", "vdim"):
            match = re.search(rf"^{key}=(-?\d+)$", output, re.MULTILINE)
            if not match:
                raise RuntimeError((prime_text, key, output))
            parsed[key] = int(match.group(1))
        if parsed != expected:
            raise RuntimeError((prime_text, parsed, expected))
        dimension_results[prime_text] = parsed

    local_payload = json.loads(series_output)
    payload = {
        "case": "max12_912_order3_nu_q8_global_quotient_probe_20260824",
        "file_sha256": FILES,
        "quotient_rows": json.loads(quotient_output)["rows"],
        "localized_dimension": dimension_results,
        "hensel_order": local_payload["order"],
        "six_rows": local_payload["six_rows"],
        "low_degree_Z_relations": local_payload[
            "bounded_Q_bidegree_search_for_Z"
        ]["nonzero_nullities"],
        "low_degree_n_q_relations": local_payload[
            "bounded_Q_relation_search_n_q"
        ]["nonzero_nullities"],
        "conclusion": (
            "the selected Q8 branch closure is one-dimensional by the reviewed "
            "formal input; the two-prime localized bases are routing evidence "
            "only, with no whole-scheme dimension theorem or global plane equation"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
