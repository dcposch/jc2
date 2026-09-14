#!/usr/bin/env python3
"""Emit guarded Hilbert-guided K=16 square-tail Singular jobs.

The input is a banked preexpanded cone source containing T0..T(2t-1) in the
weighted residual ring.  This wrapper copies those row declarations, supplies
the predicted CI Hilbert numerator to Singular's guided std, and then emits
independent normal-form and lead-ideal length checks.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import pathlib
import re
import sys
from typing import Iterable


HERE = pathlib.Path(__file__).resolve().parent
FROZEN = pathlib.Path("/tmp/jc2-lane.YU5vA0/inputs/emit_preexpanded_cone_job.py")


def load_preexpanded_module():
    spec = importlib.util.spec_from_file_location("preexpanded", FROZEN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {FROZEN}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PRE = load_preexpanded_module()


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ci_numerator(degrees: Iterable[int]) -> tuple[int, ...]:
    answer = [1]
    for degree in degrees:
        old = answer
        answer = old + [0] * degree
        for index, coeff in enumerate(old):
            answer[index + degree] -= coeff
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def predicted_tail_length(t: int) -> int:
    numerator = math.prod(range(2 * t + 2, 3 * t + 2))
    denominator = math.factorial(t - 1) * (t + 1)
    return numerator // denominator


def singular_label(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", text).strip("_").upper()


def target_coefficients(t: int, selected: tuple[int, ...], kind: str) -> tuple[int, ...]:
    if kind == "file-no-bookkeeping":
        raise ValueError("file-no-bookkeeping is handled by --target-file")
    if kind in {"tail-ci", "tail-ci-perturbed", "tail-ci-no-bookkeeping"}:
        coeffs = list(ci_numerator(range(2 * t + 2, 3 * t + 2)))
        if kind == "tail-ci-perturbed":
            if len(coeffs) < 2:
                raise ValueError("cannot perturb a one-entry numerator")
            coeffs[1] += 1
        return tuple(coeffs)
    if kind == "t2-other-fibre-full":
        if t != 2 or selected != (1, 2, 3):
            raise ValueError("t2-other-fibre-full is only for the t=2 full cone")
        # Existing positive t=2 fibre y=2/5 has numerator
        # 1 - s^6 - s^7 - s^8 + s^10 + s^11 over weights (1,3).
        return (1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 1, 1)
    if kind == "unit-series":
        return (1,)
    if kind == "first-row-series":
        degree = 4 * t + 1 - selected[0]
        coeffs = [1] + [0] * degree
        coeffs[degree] = -1
        return tuple(coeffs)
    if kind == "first-row-no-bookkeeping":
        degree = 4 * t + 1 - selected[0]
        coeffs = [1] + [0] * degree
        coeffs[degree] = -1
        return tuple(coeffs)
    raise ValueError(f"unknown target kind {kind!r}")


def selected_rows(t: int, job: str) -> tuple[int, ...]:
    if job in {"tail", "full-from-tail"}:
        return tuple(range(t, 2 * t))
    if job == "tail-desc":
        return tuple(range(2 * t - 1, t - 1, -1))
    if job in {"full", "negative-full"}:
        return tuple(range(1, 2 * t))
    raise ValueError(f"unknown job {job!r}")


def source_header(cone, variables: tuple[str, ...], weights: tuple[int, ...],
                  job: str, target_kind: str, expected: str,
                  predicted_length: int | None) -> list[str]:
    lines = [
        "// Guarded Hilbert-guided K=16 square-tail job.",
        f"// source={cone.source}",
        f"// source_sha256={cone.source_sha256}",
        f"// parser={FROZEN}",
        f"// parser_sha256={sha256(FROZEN)}",
        f"// t={cone.t} job={job} target={target_kind} expected={expected}",
        f"ring R={cone.coefficient_field},({','.join(variables)}),"
        f"wp({','.join(map(str, weights))});",
    ]
    if cone.minpoly_statement:
        lines.append(cone.minpoly_statement)
    lines += [
        "option(noredSB);",
        f"intvec WTS={','.join(map(str, weights))};",
        f'print("META t={cone.t} job={job} target={target_kind} '
        f'expected={expected} vars={PRE.singular_string(",".join(variables))} '
        f'weights={PRE.singular_string(",".join(map(str, weights)))}");',
        f'print("SOURCE_SHA256={cone.source_sha256}");',
    ]
    if predicted_length is not None:
        lines.append(f'print("PREDICTED_LENGTH={predicted_length}");')
    return lines


def emit_row_declarations(cone) -> list[str]:
    lines: list[str] = []
    for index, rhs in cone.rows:
        lines.append(f"poly T{index} =\n  {rhs};")
    for index, _ in cone.rows:
        if index == 0:
            continue
        expected_degree = 4 * cone.t + 1 - index
        lines += [
            f'if (homog(T{index})!=1) '
            f'{{ print("FAIL inhomogeneous T{index}"); exit(2); }}',
            f'if (deg(T{index})!={expected_degree}) '
            f'{{ print("FAIL degree T{index}"); exit(2); }}',
        ]
    lines.append('print("ROW_GRADING_CHECK=PASS");')
    return lines


def emit_nf_checks(rows: tuple[int, ...], basis: str, prefix: str) -> list[str]:
    lines = ["int nf_all=1;"]
    for row in rows:
        lines += [
            f"poly NF_{prefix}_{row}=reduce(T{row},{basis});",
            f"int NFZ_{prefix}_{row}=(NF_{prefix}_{row}==0);",
            f"if (NFZ_{prefix}_{row}==0) {{ nf_all=0; }}",
            f'print("NF_{prefix}_T{row}_ZERO="+string(NFZ_{prefix}_{row}));',
            f'print("NF_{prefix}_T{row}_SIZE="+string(size(NF_{prefix}_{row})));',
        ]
    lines.append(f'print("NF_{prefix}_ALL_ZERO="+string(nf_all));')
    return lines


def emit_basis_analysis(basis: str, prefix: str, predicted_length: int | None,
                        expected: str, include_hnum: bool) -> list[str]:
    lines = [
        f'print("{prefix}_BASIS_SIZE="+string(size({basis})));',
        f"int dim_{prefix}=dim({basis});",
        f'print("{prefix}_DIM="+string(dim_{prefix}));',
        f"int vdim_{prefix}=-1;",
        f"if (dim_{prefix}<=0)",
        "{",
        f"  vdim_{prefix}=vdim({basis});",
        f'  print("{prefix}_VDIM="+string(vdim_{prefix}));',
        "}",
        "else",
        "{",
        f'  print("{prefix}_VDIM=NONTERMINATING");',
        "}",
        f"ideal LEADRAW_{prefix}=lead({basis});",
        f"ideal LEADMIN_{prefix}=minbase(LEADRAW_{prefix});",
        f"ideal GLEAD_{prefix}=std(LEADMIN_{prefix});",
        f'print("{prefix}_LEAD_MIN_COUNT="+string(size(LEADMIN_{prefix})));',
        f"int lead_dim_{prefix}=dim(GLEAD_{prefix});",
        f'print("{prefix}_LEAD_DIM="+string(lead_dim_{prefix}));',
        f"int lead_vdim_{prefix}=-1;",
        f"if (lead_dim_{prefix}<=0)",
        "{",
        f"  lead_vdim_{prefix}=vdim(GLEAD_{prefix});",
        f'  print("{prefix}_LEAD_VDIM="+string(lead_vdim_{prefix}));',
        "}",
        "else",
        "{",
        f'  print("{prefix}_LEAD_VDIM=NONTERMINATING");',
        "}",
    ]
    if predicted_length is not None:
        lines += [
            f"int pass_vdim_{prefix}="
            f"(lead_dim_{prefix}==0 and lead_vdim_{prefix}=={predicted_length});",
            f'print("{prefix}_VDIM_MATCH_PREDICTED="+string(pass_vdim_{prefix}));',
        ]
    if expected == "success" and predicted_length is not None:
        lines += [
            f"int accept_{prefix}=(nf_all==1 and lead_dim_{prefix}==0 "
            f"and lead_vdim_{prefix}=={predicted_length});",
            f'if (accept_{prefix}==1) {{ print("ACCEPT_{prefix}=PASS"); }} '
            f'else {{ print("ACCEPT_{prefix}=FAIL"); }}',
        ]
    elif expected == "perturbed-failure" and predicted_length is not None:
        lines += [
            f"int accept_{prefix}=(nf_all==0 or lead_dim_{prefix}!=0 "
            f"or lead_vdim_{prefix}!={predicted_length});",
            f'if (accept_{prefix}==1) {{ print("PERTURBED_CONTROL=PASS"); }} '
            f'else {{ print("PERTURBED_CONTROL=FAIL"); }}',
        ]
    elif expected == "not-dim0":
        lines += [
            f'if (dim_{prefix}!=0) {{ print("NEGATIVE_CONTROL=PASS"); }} '
            f'else {{ print("NEGATIVE_CONTROL=FAIL"); }}',
        ]
    if include_hnum:
        lines += [
            f'print("{prefix}_HILB_NUMERATOR_BEGIN");',
            f"intvec HNUM_{prefix}=hilb({basis},1,WTS); HNUM_{prefix};",
            f'print("{prefix}_HILB_NUMERATOR_END");',
        ]
    return lines


def emit_tail_job(cone, job: str, target_kind: str, expected: str,
                  target_file: pathlib.Path | None,
                  include_hnum: bool) -> tuple[str, dict]:
    variables, weights = PRE.ordered_variables(cone, "requested")
    selected = selected_rows(cone.t, job)
    target_file_meta = None
    if target_file is not None:
        raw_target = target_file.read_text(encoding="utf-8")
        target = tuple(PRE.parse_intvec(raw_target))
        target_file_meta = {"path": str(target_file), "sha256": sha256(target_file)}
    else:
        coefficients = target_coefficients(cone.t, selected, target_kind)
        target = (coefficients if target_kind in {"tail-ci-no-bookkeeping",
                                                  "first-row-no-bookkeeping"}
                  else PRE.singular_hilbert_vector(coefficients))
    predicted = (predicted_tail_length(cone.t)
                 if job in {"tail", "tail-desc", "full-from-tail"} else None)
    lines = source_header(cone, variables, weights, job, target_kind, expected, predicted)
    lines += emit_row_declarations(cone)
    lines += [
        "intvec TARGET_HNUM=" + ",".join(map(str, target)) + ";",
        'print("TARGET_HNUM_BEGIN"); TARGET_HNUM;',
        'print("TARGET_HNUM_END");',
        "ideal J=" + ",".join(f"T{row}" for row in selected) + ";",
        f'print("SELECTED_ROWS={",".join(map(str, selected))}");',
        'print("GUIDED_STD_START");',
        "timer=1; int guided_tm=timer;",
        "ideal G=std(J,TARGET_HNUM,WTS);",
        'print("GUIDED_STD_SECONDS="+string(timer-guided_tm));',
    ]
    lines += emit_nf_checks(selected, "G", "TAIL" if job != "negative-full" else "FULL")
    prefix = "TAIL" if job != "negative-full" else "FULL"
    lines += emit_basis_analysis("G", prefix, predicted, expected, include_hnum)
    if job == "full-from-tail":
        lines += [
            'print("FULL_FROM_TAIL_START");',
            "ideal Gfull=G;",
            "int full_tm=timer;",
        ]
        for row in range(cone.t - 1, 0, -1):
            lines += [
                "int step_tm=timer;",
                f"Gfull=std(Gfull,T{row});",
                f'print("FULL_ADD_ROW=T{row} SECONDS="+string(timer-step_tm)'
                '+" SIZE="+string(size(Gfull))+" DIM="+string(dim(Gfull)));',
            ]
        full_rows = tuple(range(1, 2 * cone.t))
        lines += [
            'print("FULL_FROM_TAIL_SECONDS="+string(timer-full_tm));',
            f'print("FULL_ROWS={",".join(map(str, full_rows))}");',
        ]
        lines += emit_nf_checks(full_rows, "Gfull", "FULL")
        lines += emit_basis_analysis("Gfull", "FULL", None, "none", include_hnum)
    lines += [f'print("JOB_DONE t={cone.t} job={job}");', "quit;", ""]
    source = "\n".join(lines)
    metadata = {
        "source": str(cone.source),
        "source_sha256": cone.source_sha256,
        "parser": str(FROZEN),
        "parser_sha256": sha256(FROZEN),
        "t": cone.t,
        "job": job,
        "target_kind": target_kind,
        "expected": expected,
        "variables": list(variables),
        "weights": list(weights),
        "selected_rows": list(selected),
        "selected_degrees": [4 * cone.t + 1 - row for row in selected],
        "target_hnum": list(target),
        "target_file": target_file_meta,
        "include_hnum": include_hnum,
        "predicted_tail_length": predicted,
    }
    return source, metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("--job", choices=("tail", "tail-desc", "full-from-tail",
                                          "negative-full"),
                        default="tail")
    parser.add_argument("--target-kind",
                        choices=("tail-ci", "tail-ci-perturbed",
                                 "tail-ci-no-bookkeeping",
                                 "t2-other-fibre-full", "unit-series",
                                 "first-row-series",
                                 "first-row-no-bookkeeping",
                                 "file-no-bookkeeping"),
                        default="tail-ci")
    parser.add_argument("--target-file", type=pathlib.Path)
    parser.add_argument("--no-hnum", action="store_true",
                        help="skip computed hilb(G,1,WTS) output after checks")
    parser.add_argument("--expected",
                        choices=("success", "perturbed-failure", "not-dim0", "none"),
                        default="success")
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()

    cone = PRE.parse_source(args.source, None)
    if args.target_file is not None and args.target_kind != "file-no-bookkeeping":
        raise SystemExit("--target-file requires --target-kind file-no-bookkeeping")
    if args.target_file is None and args.target_kind == "file-no-bookkeeping":
        raise SystemExit("--target-kind file-no-bookkeeping requires --target-file")
    source, metadata = emit_tail_job(
        cone, args.job, args.target_kind, args.expected, args.target_file,
        not args.no_hnum
    )
    output = args.output
    if output is None:
        stem = f"{args.source.stem}_{args.job}_{singular_label(args.target_kind)}"
        output = HERE / f"{stem}.sing"
    if output.suffix != ".sing":
        raise SystemExit("--output must end in .sing")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(source, encoding="utf-8")
    metadata["singular_source"] = str(output)
    metadata["singular_source_sha256"] = hashlib.sha256(source.encode()).hexdigest()
    metadata["run_command"] = f"box/k16stdhilb-20260903/run_singular_job.sh {output}"
    metadata_path = output.with_suffix(".json")
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n",
                             encoding="utf-8")
    print(json.dumps({"source": str(output), "metadata": str(metadata_path),
                      "sha256": metadata["singular_source_sha256"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
