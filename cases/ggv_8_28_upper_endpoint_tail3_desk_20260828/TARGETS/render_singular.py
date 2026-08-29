#!/usr/bin/env python3
"""Render a frozen cutoff-three AWS target as a standalone Singular job.

This renderer uses only the Python standard library.  It does not run a CAS.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_TARGET = HERE / "tail3_v_nonzero_d22_target.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(encoded):
    return [(tuple(monomial), Fraction(coefficient))
            for monomial, coefficient in encoded]


def coefficient_text(value, field, prime):
    if field == "q":
        if value.denominator == 1:
            return str(value.numerator)
        return f"({value.numerator}/{value.denominator})"
    denominator = value.denominator % prime
    assert denominator
    return str((value.numerator % prime) * pow(denominator, -1, prime) % prime)


def polynomial_text(encoded, names, field, prime):
    pieces = []
    for monomial, coefficient in decode(encoded):
        negative = field == "q" and coefficient < 0
        scalar = coefficient_text(abs(coefficient) if negative else coefficient,
                                  field, prime)
        factor = "*".join(names[variable] for variable in monomial)
        term = scalar if not factor else f"{scalar}*{factor}"
        if not pieces:
            pieces.append(f"-{term}" if negative else term)
        else:
            pieces.append(("-" if negative else "+") + term)
    return "".join(pieces) if pieces else "0"


def variables_in(polynomials):
    return sorted({variable for encoded in polynomials
                   for monomial, _coefficient in decode(encoded)
                   for variable in monomial})


def render(args):
    target = json.loads(args.target.read_text())
    assert target["schema"] == (
        "GGV-8_28-UPPER-ENDPOINT-TAIL3-VNONZERO-D22-AWS-TARGET-v1"
    )
    assert target["authoritative_raw_system_sha256"] == RAW_SHA256
    assert target["raw_slot_inventory_sha256"] == RAW_INPUT_SHA256
    case_dir = HERE.parent
    pinned_files = {
        "source_tail_compile_sha256": case_dir / "TAIL3/TAIL_DEFORMATION_SYSTEM.json",
        "producer_analysis_sha256": case_dir / "TAIL3_DESK_ANALYSIS.json",
        "producer_script_sha256": case_dir / "analyze_tail3.py",
        "authoritative_raw_system_sha256": (
            case_dir.parent
            / "ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
        ),
        "raw_slot_inventory_sha256": (
            case_dir.parent
            / "ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
        ),
    }
    for field, path in pinned_files.items():
        assert path.is_file(), path
        assert sha256(path) == target[field], (field, path)
    polynomials = list(target["scopes"][args.scope])
    chart_variable = None
    if args.scope == "root":
        if args.branch is None:
            raise SystemExit("--branch is required with --scope root")
        if args.chart is not None:
            raise SystemExit("--chart is forbidden with --scope root")
        polynomials.extend(target["root_branches"][args.branch])
    else:
        if args.branch is not None:
            raise SystemExit("--branch is only valid with --scope root")
        if args.chart is None:
            raise SystemExit("--chart is required with --scope core/full")
        chart_variable = target["nonzero_cover"]["coefficient_ids"][args.chart]

    names = {int(variable): name
             for variable, name in target["variable_names"].items()}
    names.update({int(variable): name for variable, name
                  in target["synthetic_branch_variable_names"].items()})
    used = variables_in(polynomials)
    if chart_variable is not None:
        used.append(chart_variable)
    used = sorted(set(used))
    assert all(variable in names for variable in used)

    # For lexicographic root diagnostics, put the nine nonscalar root
    # coordinates first so the seven corrected scalar coordinates occupy the
    # elimination tail.  Main D22 jobs use degree reverse lexicographic order.
    scalar_tail = [152, 189, 208, 3000, 3200, 3400, 3600,
                   3900, 3901, 3902]
    if args.order == "lp":
        ordered = ([variable for variable in used
                    if variable not in scalar_tail]
                   + [variable for variable in scalar_tail if variable in used])
    else:
        ordered = used
    ring_names = (["chartinv"] if chart_variable is not None else []) + [
        names[variable] for variable in ordered
    ]
    characteristic = "0" if args.field == "q" else str(args.prime)
    generators = [polynomial_text(poly, names, args.field, args.prime)
                  for poly in polynomials]
    if chart_variable is not None:
        generators.append(f"chartinv*{names[chart_variable]}-1")

    lines = [
        f"// frozen_schema={target['schema']}",
        f"// scope={args.scope} branch={args.branch} chart={args.chart}",
        f"ring R={characteristic},({','.join(ring_names)}),{args.order};",
        "option(redSB);",
        "ideal I=",
        ",\n".join(generators) + ";",
        f'print("SCOPE={args.scope}");',
        f'print("BRANCH={args.branch or "none"}");',
        f'print("CHART={args.chart if args.chart is not None else -1}");',
        f'print("FIELD={args.field}");',
        'print("GENERATOR_COUNT="+string(size(I)));',
        f'print("VARIABLE_COUNT={len(ring_names)}");',
        "int started=timer;",
    ]
    if args.certify:
        if args.field != "q":
            raise SystemExit("--certify is restricted to exact Q jobs")
        lines.extend([
            "matrix TRANS;",
            "ideal G=liftstd(I,TRANS);",
        ])
    else:
        lines.append("ideal G=std(I);")
    lines.extend([
        'print("STD_SECONDS="+string(timer-started));',
        'print("STD_SIZE="+string(size(G)));',
        "int unit_index=0;",
        "for (int gi=1; gi<=size(G); gi++)",
        "{",
        "  if ((G[gi]<>0) && (deg(G[gi])==0)) { unit_index=gi; break; }",
        "}",
        "if (unit_index==0)",
        "{",
        '  print("UNIT=0");',
        '  print("NONUNIT_OR_INCONCLUSIVE=1");',
        "}",
        "else",
        "{",
        '  print("UNIT=1");',
    ])
    if args.certify:
        lines.extend([
            "  poly constant=G[unit_index];",
            "  poly check=0;",
            "  for (int ii=1; ii<=size(I); ii++)",
            "  {",
            "    check=check+I[ii]*TRANS[ii,unit_index]/constant;",
            "  }",
            "  if (check==1) { print(\"CERTIFICATE_CHECK=PASS\"); }",
            "  else { print(\"CERTIFICATE_CHECK=FAIL\"); exit(7); }",
            '  print("CERTIFICATE_BEGIN");',
            "  for (ii=1; ii<=size(I); ii++)",
            "  {",
            "    if (TRANS[ii,unit_index]<>0)",
            "    {",
            '      print("C["+string(ii)+"]="+string(TRANS[ii,unit_index]/constant));',
            "    }",
            "  }",
            '  print("CERTIFICATE_END");',
        ])
    lines.extend(["}", "exit(0);", ""])
    args.output.write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--scope", choices=("root", "core", "full"),
                        required=True)
    parser.add_argument("--branch", choices=("q0_l0", "q0_4b_minus_l",
                                              "qnonzero_simplified"))
    parser.add_argument("--chart", type=int, choices=range(6))
    parser.add_argument("--field", choices=("mod", "q"), required=True)
    parser.add_argument("--prime", type=int, default=65521)
    parser.add_argument("--order", choices=("dp", "lp"), default="dp")
    parser.add_argument("--certify", action="store_true")
    args = parser.parse_args()
    render(args)


if __name__ == "__main__":
    main()
