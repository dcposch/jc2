#!/usr/bin/env python3
"""Validate seven row shards and emit the small Delta certificate client."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2_VALIDATOR = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/validate_t_rs0_stream.py"
V2_VALIDATOR_SHA256 = "4ff10d85aeb91f3853a4fd2c89ac2e0fe93bd07fd2c3769241cd8f40afb01949"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
SAFE_POLY = re.compile(r"^[A-Za-z0-9_+*/^()\-\s]+$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v2_validator():
    actual = digest(V2_VALIDATOR)
    if actual != V2_VALIDATOR_SHA256:
        fail(("V2 validator hash mismatch", actual, V2_VALIDATOR_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_v2_validator", V2_VALIDATOR)
    if spec is None or spec.loader is None:
        fail("cannot import V2 validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def transcript_values(path: Path) -> dict[str, list[str]]:
    transcript = path.read_text()
    if "T_RS0_FAIL=" in transcript or any(line.startswith("? ") or line.startswith("   ?") for line in transcript.splitlines()):
        fail(("row transcript contains a failure or Singular diagnostic", str(path)))
    values: dict[str, list[str]] = defaultdict(list)
    for raw in transcript.splitlines():
        line = raw.strip()
        if line.startswith("T_RS0_") and "=" in line:
            key, value = line.split("=", 1)
            values[key].append(value)
    return values


def unique(values: dict[str, list[str]], key: str, expected: str) -> None:
    if values.get(key) != [expected]:
        fail(("missing, duplicate, or wrong sentinel", key, values.get(key), expected))


def polynomial_text(path: Path) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        fail(("missing or empty retained polynomial", str(path)))
    raw = path.read_text()
    if ";" in raw or '"' in raw or not SAFE_POLY.fullmatch(raw):
        fail(("unsafe retained polynomial serialization", str(path)))
    value = "".join(line.strip() for line in raw.splitlines())
    if not value:
        fail(("empty retained polynomial serialization", str(path)))
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    parser.add_argument("--certificate-input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    v2 = load_v2_validator()
    candidates = tuple(v2.CANDIDATES)
    inactive = tuple(v2.INACTIVE)
    names = candidates + inactive
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("status") != "PASS-T-RS0-ROW-SHARD-COMPILER":
        fail("compiler status mismatch")
    if compiler.get("implementation") != "ROW_SHARD_DIFFSCAN_V6":
        fail("compiler implementation mismatch")
    if compiler.get("characteristic") != args.characteristic:
        fail("compiler characteristic mismatch")
    if tuple(compiler.get("candidate_manifest", ())) != candidates:
        fail("compiler candidate list differs from frozen V2 ceiling")
    if tuple(compiler.get("inactive_custody", ())) != inactive:
        fail("compiler inactive list differs from frozen V2 ceiling")
    if compiler.get("candidate_manifest_count") != 76 or compiler.get("ring_variable_count") != 85:
        fail("compiler census mismatch")
    if compiler.get("tested_atom_exponent_bound") != 72:
        fail("compiler derivative bound mismatch")

    job = args.job.resolve()
    tag = compiler.get("registered_aws_lane")
    if not isinstance(tag, str) or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_"):
        fail("bad registered row-shard tag")
    row_hashes = compiler.get("row_input_sha256")
    if not isinstance(row_hashes, dict) or set(row_hashes) != {str(row) for row in range(1, 8)}:
        fail("row input hash map mismatch")

    row_records: dict[str, object] = {}
    term_counts: dict[str, int] = {}
    grade_bits = {grade: 0 for grade in range(13)}
    dependencies = {name: 0 for name in names}
    wrong_literal = 0
    synthetic_omission = 0
    for row in range(1, 8):
        label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
        input_path = job / "compiled" / f"t_rs0_row{row}_{label}.sing"
        if digest(input_path) != row_hashes[str(row)]:
            fail(("row input hash mismatch", row, digest(input_path), row_hashes[str(row)]))
        row_tag = f"{tag}_row{row}"
        run_dir = job / "run" / f"row{row}"
        stdout = run_dir / f"{row_tag}.stdout"
        stderr = run_dir / f"{row_tag}.stderr"
        meta_path = run_dir / f"{row_tag}.meta"
        if not stdout.is_file() or not stderr.is_file() or not meta_path.is_file():
            fail(("missing row lane artifact", row))
        meta = v2.parse_meta(meta_path)
        if meta.get("lane") != row_tag or meta.get("rc") != "0":
            fail(("row AWS metadata mismatch", row, meta))
        if meta.get("stdout_sha256") != digest(stdout) or meta.get("stderr_sha256") != digest(stderr):
            fail(("row transcript hash not bound by AWS metadata", row))
        values = transcript_values(stdout)
        for key, expected in {
            "T_RS0_SOURCE_HASHES": "PASS",
            "T_RS0_SCOPE": "DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT",
            "T_RS0_IMPLEMENTATION": "ROW_SHARD_DIFFSCAN_V6",
            "T_RS0_SHARD_ROW": str(row),
            "T_RS0_PREFIX_SPECIALIZATION_MAP": "1",
            "T_RS0_RHO_DECK_INVARIANCE": "1",
            "T_RS0_EXTRACTION_IDENTITIES": "1",
            "T_RS0_EXTRACTED_SPECIALIZATION_MAP": "1",
            f"T_RS0_ROW_{row}_STREAM_RELEASED": "1",
            "T_RS0_ROW_SHARD_ENDPOINT": "PASS_NAVIGATION_ONLY",
        }.items():
            unique(values, key, expected)
        wrong = values.get("T_RS0_WRONG_LITERAL_P_NEGATIVE_CONTROL")
        omission = values.get("T_RS0_SYNTHETIC_ELL1_OMISSION_DETECTED")
        if wrong not in (["0"], ["1"]) or omission not in (["0"], ["1"]):
            fail(("row negative-control sentinel malformed", row, wrong, omission))
        wrong_literal |= int(wrong[0])
        synthetic_omission |= int(omission[0])
        for grade in range(13):
            grade_key = f"T_RS0_GRADE_{grade}_NONZERO"
            if values.get(grade_key) not in (["0"], ["1"]):
                fail(("row grade sentinel malformed", row, grade, values.get(grade_key)))
            bit = int(values[grade_key][0])
            count_key = f"T_RS0_TERMS_{grade}_{row}"
            if count_key not in values or len(values[count_key]) != 1:
                fail(("row term-count sentinel missing or duplicate", row, grade))
            count = int(values[count_key][0])
            if count < 0 or bit != int(count > 0):
                fail(("row grade bit/term count mismatch", row, grade, bit, count))
            grade_bits[grade] |= bit
            term_counts[f"{grade}:{row}"] = count
        for name in names:
            key = f"T_RS0_DEP_{name}"
            if values.get(key) not in (["0"], ["1"]):
                fail(("row dependency sentinel malformed", row, name, values.get(key)))
            dependencies[name] |= int(values[key][0])
        expected_keep = []
        if row == 2:
            expected_keep = ["KeepT10_2", "KeepF10_2"]
        elif row == 3:
            expected_keep = ["KeepT10_3", "KeepF10_3"]
        elif row == 6:
            expected_keep = ["KeepT12_6", "KeepF12_6"]
        actual_keep = sorted(
            key.removeprefix("T_RS0_KEEP_").removesuffix("_WRITTEN")
            for key, item in values.items()
            if key.startswith("T_RS0_KEEP_") and key.endswith("_WRITTEN") and item == ["1"]
        )
        if actual_keep != sorted(expected_keep):
            fail(("row retained-coefficient sentinel mismatch", row, actual_keep, expected_keep))
        row_records[str(row)] = {
            "input_sha256": digest(input_path),
            "stdout_sha256": digest(stdout),
            "stderr_sha256": digest(stderr),
            "meta_sha256": digest(meta_path),
        }

    if wrong_literal != 1 or synthetic_omission != 1:
        fail(("global negative controls not detected", wrong_literal, synthetic_omission))
    if any(dependencies[name] for name in inactive):
        fail(("inactive source unexpectedly occurs", {name: dependencies[name] for name in inactive}))
    discovered = [name for name in candidates if dependencies[name]]
    if not discovered:
        fail("empty discovered source manifest")
    nonzero_grades = [grade for grade, bit in grade_bits.items() if bit]
    if not nonzero_grades:
        fail("all seven rows vanish through grade 12")
    common_order = min(nonzero_grades)

    expected_keep_paths = {
        key: job / "compiled" / f"{key}.poly"
        for key in ("KeepT10_2", "KeepF10_2", "KeepT10_3", "KeepF10_3", "KeepT12_6", "KeepF12_6")
    }
    compiler_keep = compiler.get("keep_files")
    if not isinstance(compiler_keep, dict) or set(compiler_keep) != set(expected_keep_paths):
        fail("compiler retained-coefficient path map mismatch")
    keep_text: dict[str, str] = {}
    keep_hashes: dict[str, str] = {}
    for key, path in expected_keep_paths.items():
        if Path(compiler_keep[key]).resolve() != path.resolve():
            fail(("compiler retained-coefficient path mismatch", key, compiler_keep[key], str(path)))
        keep_text[key] = polynomial_text(path)
        keep_hashes[key] = digest(path)

    variables = ("sigma", "rho") + candidates + inactive
    if len(variables) != 85 or len(set(variables)) != 85:
        fail("certificate ring-variable census mismatch")
    cert = [
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        "ideal PrefixIdeal=std(ideal(sigma^13));",
        "qring Q=PrefixIdeal;",
        'print("T_RS0_CERTIFICATE_SCOPE=RECOMBINATION_ONLY_NO_REES_OR_CHART_VERDICT");',
    ]
    for key in ("KeepT10_2", "KeepF10_2", "KeepT10_3", "KeepF10_3", "KeepT12_6", "KeepF12_6"):
        cert.append(f"poly {key}={keep_text[key]};")
    cert += [
        "poly FrozenCert=32768*KeepF12_6-35*k*rs^4+4096*rs*KeepF10_2+8192*cs*KeepF10_3;",
        "poly FrozenOmit=32768*KeepF12_6-35*k*rs^4+4096*rs*KeepF10_2;",
        "int frozenCert=(FrozenCert==0);",
        "int frozenOmit=(FrozenOmit==-1536*cs*c0*c1 && FrozenOmit!=0);",
        'print("T_RS0_FROZEN_CUSP_CERTIFICATE="+string(frozenCert));',
        'print("T_RS0_FROZEN_OMIT_G10_3_NEGATIVE_CONTROL="+string(frozenOmit));',
        "poly Delta=32768*KeepT12_6-35*k*rs^4+4096*rs*KeepT10_2+8192*cs*KeepT10_3;",
        "int deltaSpecial=(subst(Delta,rho,0)==0);",
        "int deltaEven=(subst(Delta,rho,-rho)==Delta);",
        "ideal Rho2=std(ideal(rho^2));",
        "int deltaRho2=(reduce(Delta,Rho2)==0);",
        "poly DeltaQ=Delta/rho^2;",
        "int deltaMultiplyBack=(rho^2*DeltaQ-Delta==0);",
        "int deltaNonzero=(Delta!=0);",
        'print("T_RS0_DELTA_SPECIAL_FIBRE_ZERO="+string(deltaSpecial));',
        'print("T_RS0_DELTA_EVEN="+string(deltaEven));',
        'print("T_RS0_DELTA_RHO2_DIVISIBLE="+string(deltaRho2));',
        'print("T_RS0_DELTA_MULTIPLY_BACK="+string(deltaMultiplyBack));',
        'print("T_RS0_DELTA_NONZERO="+string(deltaNonzero));',
        'print("T_RS0_DELTA_QUOTIENT_TERMS="+string(size(DeltaQ)));',
        'if (frozenCert*frozenOmit*deltaSpecial*deltaEven*deltaRho2*deltaMultiplyBack!=1) { print("T_RS0_FAIL=CERTIFICATE_RECOMBINATION"); quit(92); }',
        'print("T_RS0_CERTIFICATE_ENDPOINT=PASS_NAVIGATION_ONLY");',
        "quit;",
    ]
    args.certificate_input.write_text("\n".join(cert) + "\n")
    result = {
        "status": "PASS-T-RS0-ROW-SHARDS-PREPARED-CERTIFICATE",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "implementation": "ROW_SHARD_DIFFSCAN_V6",
        "characteristic": args.characteristic,
        "common_sigma_order": common_order,
        "grade_nonzero": {str(grade): grade_bits[grade] for grade in range(13)},
        "term_counts": term_counts,
        "candidate_manifest": list(candidates),
        "discovered_manifest": discovered,
        "inactive_custody": list(inactive),
        "dependencies": dependencies,
        "wrong_literal_negative_control": wrong_literal,
        "synthetic_omission_negative_control": synthetic_omission,
        "row_records": row_records,
        "keep_sha256": keep_hashes,
        "certificate_input_sha256": digest(args.certificate_input),
        "compiler_result_sha256": digest(args.compiler_result),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
